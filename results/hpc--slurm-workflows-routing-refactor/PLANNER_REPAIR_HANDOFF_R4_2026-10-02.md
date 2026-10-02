# Slurm Workflows — Critic R4 最小返修交接

日期：2026-10-02  
角色：Planner  
任务：`hpc--slurm-workflows-routing-refactor`  
目标仓库：`YuukiAS/AI_Skills_Collection`  
执行分支：`reviewed/hpc--slurm-workflows-routing-refactor`  
既有 worktree：`/tmp/ai-skills-hpc-slurm-workflows-routing-refactor`  
本轮 latest main：`98721a202bc557c0b9c0800e66e50cab466bfba2`  
Critic R4 commit：`307e02323bc280c4e32404585136bf004aa10b2c`  
被审 product candidate：`0bdfc91f56a6bce0bfee5aea7a4b9770f4a8172d`  
Critic R4：`results/hpc--slurm-workflows-routing-refactor/PREFINAL_CRITIC_REVIEW_R4_2026-10-02.md`  
前一 Planner handoff：`results/hpc--slurm-workflows-routing-refactor/PLANNER_REPAIR_HANDOFF_R3_2026-10-02.md`

这是同一个 task 的最小 pre-final repair，不是新架构轮次，不创建 successor、branch 或 worktree，不重写 Proposal / Execution Plan v0.6。

## Planner 对 R4 的处理

- `SWR-PF1 = CLOSED`
- `SWR-PF2 = CLOSED`
- `SWR-PF3 = CLOSED`
- `SWR-PF4 = CLOSED`
- `SWR-PF5 = ACCEPT`，只剩 fold/gap fail-closed 子项。

Critic R4 的 finding 成立，而且不是新增要求。R3 handoff 已明确：ambiguous/nonexistent local time 不能猜选 instant，必须 fail closed。当前 candidate 的 `_recurrence_datetime()` 直接把 local date/time 与 `ZoneInfo` 组合；Python 允许这种构造，即使 local wall-clock 落在 DST fold 或 gap，也不会自动替应用做严格有效性检查。

因此本轮只补 recurrence local datetime 的严格有效性判断；现有 `ZoneInfo` calendar 路径、family timezone 语义、explicit-aware seed、DST 跨周行为与 PF1-PF4 都保持。

## 允许修改的最小范围

优先仅修改：

- `skills/tools/hpc/slurm-workflows/scripts/slurm_routing.py`
- `tests/test_slurm_workflows.py`
- `results/hpc--slurm-workflows-routing-refactor/RESULT.md`

只有现有 generator/validation 因真实 source 变化要求同步时，才更新既有生成产物。

不得修改：

- Proposal / Execution Plan v0.6；
- PF1-PF4 已关闭机制；
- PF5 已通过的 family timezone / DST / explicit-aware / invalid-zone 语义；
- Bridge Kit；
- central Plugin topology；
- 其他 domain/workflow；
- 新 gate / daemon / watcher / registry / state machine；
- 新 timezone/calendar 依赖。

保持：

- Repository = `5.4.1`
- `slurm-workflows` = `0.3`
- central Plugins = `NO_BUMP`
- Bridge Kit = `NO CHANGE`
- Issue #95 = `DOING`
- `REAL_SLURM_MUTATION = NO`

## SWR-PF5 — fold/gap local wall-clock 必须 fail closed

### 1. 在 recurrence local datetime 构造处做严格有效性判断

保持标准库 `zoneinfo.ZoneInfo`。

对一个待构造的 family-local wall-clock，例如：

```text
local date + recurrence start_time + ZoneInfo(family["timezone"])
```

不要直接把默认 `fold=0` 的结果当作唯一合法 instant。

最小可接受实现可以在现有 `_recurrence_datetime()` 附近增加一个小 helper，使用 `fold=0` / `fold=1` 和 UTC round-trip 判断：

1. 以相同 naive local wall-clock 分别构造 `fold=0` 与 `fold=1` 的 aware candidate；
2. 每个 candidate 转到 UTC，再转回同一个 family timezone；
3. 比较 round-trip 后的 naive local date/time 是否仍等于原请求 wall-clock；
4. 若两个 fold 都 round-trip 回原 wall-clock，且对应的 UTC instant 不同：
   - 这是 ambiguous/fold；
   - 不得默认选 `fold=0` 或 `fold=1`；
   - 返回稳定 calendar error；
5. 若两个 fold 都不能 round-trip 回原 wall-clock：
   - 这是 nonexistent/gap；
   - 返回稳定 calendar error；
6. 若 round-trip 合法且两个 fold 指向同一个 UTC instant：
   - 这是普通唯一 local time；
   - 沿用当前行为。

不要只比较 `utcoffset()` 就把所有 offset difference 当作 fold，因为 gap 也可能在 `fold=0/1` 下表现为不同 offset。round-trip validity 必须参与判断。

### 2. 错误传播必须明确且不会落入 mutation

建议使用一个极小的内部 calendar error 传播方式，例如本地 exception 或 `(datetime, error)` 结果；不要新建 schema/state machine。

无论具体内部形式如何，最终要求是：

- fold -> `capacity_reconcile(...)` 返回：
  - `action = "read_only_proposal"`
  - stable reason，例如 `ambiguous_recurrence_local_time`
  - `successor_mutation = False`
- gap -> `capacity_reconcile(...)` 返回：
  - `action = "read_only_proposal"`
  - stable reason，例如 `nonexistent_recurrence_local_time`
  - `successor_mutation = False`

也可以使用一个统一稳定 reason，只要 fold/gap 都确定 fail closed、测试能够证明两种输入均不会 mutation；但分开的 reason 更便于诊断。

关键限制：不能让 `capacity_windows()` 因错误只返回空 list，然后让现有 reconciliation 把空窗口解释成可继续 `plan_one_successor`。calendar validity failure 必须被显式带到 `capacity_reconcile` 的 read-only 分支。

### 3. 普通时间与 explicit-aware 语义保持

PF5 已通过的行为不得回退：

- 普通唯一 local time，例如 New York Monday 09:00，继续正常生成 recurrence；
- invocation UTC -> family timezone 转换继续正确；
- DST 跨周继续重新计算 offset；
- explicit aware `target_occurrence` 仍保持第一个窗口的原 absolute instant；
- explicit aware N 后的 recurrence 继续按 family timezone；
- invalid/unavailable timezone key 继续 `invalid_or_unavailable_timezone` fail closed；
- no-recurrence explicit one-off 继续单窗口语义。

fold/gap 检查只应用于由 recurrence wall-clock 构造出来的 local datetime；不要把一个已经明确 aware 的 explicit occurrence 误判成需要重新 disambiguate 的 local wall-clock。

## G8 最小回归

至少增加以下 deterministic cases。可放在现有 G8 测试中，也可拆成小的同 Gate test；不要新增 Gate。

### A. Spring-forward gap

使用：

```text
timezone = America/New_York
weekday = Sunday
start_time = 02:30
date = 2026-03-08
```

该 local wall-clock 位于 DST spring-forward gap。

构造一个与该 family 自身 scope 匹配的 valid enrollment digest，避免测试只命中 stale digest。

期望：

```text
action = read_only_proposal
reason = stable gap/calendar reason
successor_mutation = False
```

不得产生 successor target instant。

### B. Fall-back fold

使用：

```text
timezone = America/New_York
weekday = Sunday
start_time = 01:30
date = 2026-11-01
```

该 local wall-clock 在 fall-back 时发生两次。

同样使用该 family 自身匹配的 valid enrollment digest。

期望：

```text
action = read_only_proposal
reason = stable fold/calendar reason
successor_mutation = False
```

不得静默选择 EDT 或 EST 其中一个 instant。

### C. 防回归

继续证明：

- New York 普通 09:00 recurrence 正常；
- UTC invocation + family-local recurrence 正常；
- 2026-10-26 -> 2026-11-02 的 DST offset 更新正常；
- explicit-aware seed 正常；
- invalid timezone fail closed；
- PF1-PF4 现有测试全部 PASS；
- installed persistent-capacity G6 与 tracked identity privacy 不回退。

## 外部标准核查

Python PEP 495 明确区分：

- backward transition 产生 fold，local time 是 ambiguous；
- forward transition 产生 gap，local time 是 missing；
- `fold` 用于区分 ambiguous local time；
- constructors 不会自动拒绝 invalid/missing local datetime；
- strict fold/gap validity checking 应由应用层根据自己的策略实现。

因此本轮 fail-closed application check 与标准库模型一致，不需要第三方 timezone 包或新的 calendar policy。

## 执行与验收

1. 在既有 worktree 核实 exact branch/worktree；不得创建新的。
2. `git fetch origin main` 并检查 Slurm-relevant drift；若只是无关 drift，可按当前 Reviewed Handoff/Host Policy 普通 non-force 同步；禁止 rebase/force。
3. 仅实现 PF5 fold/gap 子项。
4. 先跑 PF5/G8 定向测试。
5. 重跑完整 `tests.test_slurm_workflows`，确认完整 G1-G8。
6. 重跑当前 `RESULT.md` 的完整验证：
   - `python -m unittest tests.test_skill_update`
   - `python scripts/skills.py validate`
   - `python scripts/skills.py audit --all`
   - `python scripts/build_codex_marketplace.py --write --validate --check --path-report`
   - `python -m unittest discover -s tests`
7. 所有 final gate evidence 必须绑定同一个新的 exact product candidate；不得拼接 `0bdfc91...` 的旧 PASS。
8. 更新 `RESULT.md`，明确记录 gap/fold fail-closed、普通 timezone/DST 行为与 PF1-PF4 防回归。
9. 冻结新的 exact product candidate。
10. 通过现有 Clear Writing 路径更新 Issue #95 的 current candidate / current progress / next action；保持 `DOING`、classification、Area、`tracking: #95` 与空 Resolution commit。
11. 使用当前已授权 reviewed branch 的 ordinary non-force publication path。
12. 停在 `READY_FOR_FINAL_CRITIC`，附完整 independent Critic prompt。下一轮只复核：
   - PF5 fold/gap fail-closed；
   - PF5 其余已通过语义防回归；
   - PF1-PF4 防回归；
   - G1-G8 / full suite；
   - Issue #95 anchor；
   - exact candidate identity。

不得集成 main、推进 release、执行真实 Slurm mutation或自我批准。
