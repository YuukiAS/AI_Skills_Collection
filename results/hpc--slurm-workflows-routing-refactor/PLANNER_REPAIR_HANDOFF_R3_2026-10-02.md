# Slurm Workflows — Critic R3 最小返修交接

日期：2026-10-02  
角色：Planner  
任务：`hpc--slurm-workflows-routing-refactor`  
目标仓库：`YuukiAS/AI_Skills_Collection`  
执行分支：`reviewed/hpc--slurm-workflows-routing-refactor`  
既有 worktree：`/tmp/ai-skills-hpc-slurm-workflows-routing-refactor`  
本轮 latest main：`98721a202bc557c0b9c0800e66e50cab466bfba2`  
Critic R3 commit：`3006227a139e8b21fd416540a335ff8dea2d3340`  
被审 product candidate：`569f85dde6f676fb2c249f89062c3f81168cac9e`  
Critic R3：`results/hpc--slurm-workflows-routing-refactor/PREFINAL_CRITIC_REVIEW_R3_2026-10-02.md`  
前一 Planner handoff：`results/hpc--slurm-workflows-routing-refactor/PLANNER_REPAIR_HANDOFF_R2_2026-10-02.md`

这是同一个 task 的最小 pre-final repair，不是新架构轮次，不创建 successor、branch 或 worktree，不重写 Proposal / Execution Plan v0.6。

## Planner 对 R3 的处理

- `SWR-PF1 = CLOSED`
- `SWR-PF2 = CLOSED`
- `SWR-PF3 = CLOSED`
- `SWR-PF4 = CLOSED`
- `SWR-PF5 = ACCEPT`

PF5 是真实实现缺口：candidate 已把 `family["timezone"]` 放进 durable enrollment scope，但 recurring window 仍用 invocation/current datetime 的 `tzinfo` 构造。这样 `America/New_York` 的 Monday 09:00 可能被错误解释成 09:00 UTC。timezone 既然是 capacity-family calendar contract 的一部分，就必须同时决定 recurrence 的 wall-clock 语义。

这不改变批准架构、Gate taxonomy、状态模型、版本方向或 Slurm 机制。

## 当前 main drift

当前 `main` 相对 branch merge base 只多两个与 Slurm 无关的文件：

- Project Instructions Editor review 文档；
- Bridge consumer-run evidence。

未发现新的 Slurm production/source/test/version semantic drift。Executor 开始时仍需 fetch/recheck；若 main 继续只有无关 drift，按已有 Reviewed Handoff 规则普通 non-force 同步，不 rebase/force。

## 允许修改的最小范围

优先仅修改：

- `skills/tools/hpc/slurm-workflows/scripts/slurm_routing.py`
- `tests/test_slurm_workflows.py`
- `results/hpc--slurm-workflows-routing-refactor/RESULT.md`

只有现有 generator/validation 因真实 source 变化要求同步时，才更新既有生成产物。

不得修改：

- Proposal / Execution Plan v0.6 架构；
- PF1-PF4 已关闭机制；
- Bridge Kit；
- central Plugin topology；
- 其他 domain/workflow；
- 新 gate / daemon / watcher / registry / state machine。

保持：

- Repository = `5.4.1`
- `slurm-workflows` = `0.3`
- central Plugins = `NO_BUMP`
- Bridge Kit = `NO CHANGE`
- Issue #95 = `DOING`
- `REAL_SLURM_MUTATION = NO`

## SWR-PF5 — family timezone 必须真正控制 recurrence

使用 Python 标准库 `zoneinfo.ZoneInfo`；不得新增第三方依赖、tz database 管理器或日历系统。

### 1. Timezone 解析与 fail-closed

增加一个小的单一 helper 即可，不要建立第二套 calendar abstraction。

语义：

- `family["timezone"]` 存在时，用 `ZoneInfo(<IANA key>)` 解析；
- 合法 timezone 用于所有 recurrence-derived weekday/start_time 计算；
- timezone 缺失时保留当前既有 fallback 语义，不为本轮另设默认策略；
- timezone 非法，或者当前运行环境没有该 zone 的可用数据时，不得静默回退 UTC / invocation timezone 后继续 successor mutation；
- mutation path 必须明确 fail closed，例如 `read_only_proposal` + 稳定 reason（可用 `invalid_or_unavailable_timezone` 或等价清楚原因），并保持 `successor_mutation = False`。

不要通过只让 `capacity_windows()` 返回空列表来实现 fail-closed，因为当前 reconciliation 对空窗口不能被允许落到 mutation planning。

### 2. Recurrence-only 路径

若 family timezone 有效：

1. 先把 invocation `now` 转成 family timezone；
2. 用转换后的 local weekday/date 判断 current / next occurrence；
3. recurrence 的 `weekday` + `start_time` 表示 family-local wall-clock；
4. 构造 occurrence 时使用 `ZoneInfo`，而不是复制 `now.tzinfo` 或固定数字 offset；
5. current useful window 的 previous-occurrence 判断也必须基于 family-local calendar。

例如：

```text
timezone = America/New_York
weekday = Monday
start_time = 09:00
invocation now = UTC
```

目标是纽约当地 Monday 09:00；在 EDT 时对应 13:00 UTC，而不是 09:00 UTC。

### 3. 后续 weekly occurrence 与 DST

weekly recurrence 必须保持“当地墙上时钟的同一个时间”，不能把第一次 occurrence 的 UTC offset 固定七天复制。

实现应让每个后续 occurrence 由 family timezone 的 local date + local `start_time` 构造，或使用等价、确实由 `ZoneInfo` 重新求 offset 的标准库方式。

确定性回归必须跨一次 DST offset 变化。例如 `America/New_York`：

- 2026-10-26 Monday 09:00 应是 EDT (`-04:00`)；
- 2026-11-02 Monday 09:00 应是 EST (`-05:00`)。

测试要证明 local 09:00 保持不变、absolute UTC time 随 DST 规则改变；不能出现固定 `-04:00` 或固定 UTC clock 的算法。

本轮不新增更大的 ambiguous/nonexistent-local-time 配置体系；如果实现遇到无法安全解释的 timezone/local-time 情况，应 fail closed，而不是猜测并继续 mutation。

### 4. Explicit aware target_occurrence

PF2 已关闭，必须保留：

- explicit aware `target_occurrence` 仍是第一个窗口，不能因为 family timezone 被重新解释成另一个 absolute instant；
- 如果 family 同时有 recurrence，后续 occurrence 的 calendar 计算必须切回 family timezone；
- 计算下一 recurrence 时，应以 explicit start 转换到 family timezone 后的 local calendar position 为基准，而不是使用 explicit datetime 自带 timezone 的 weekday/offset；
- no-recurrence explicit one-off 继续保持单窗口语义。

例如 explicit N 用 UTC aware timestamp 表示纽约当地 09:00；active 覆盖 N 后，N+1 应按纽约下一周 09:00 构造，并在跨 DST 时得到新的正确 offset。

### 5. G8 最小新增回归

至少加入以下确定性用例，并修正当前把纽约 09:00 断言为 `09:00+00:00` 的错误 expectation：

1. **UTC invocation / New York recurrence**
   - invocation `now` 为 aware UTC；
   - family timezone = `America/New_York`；
   - Monday `09:00`；
   - target window 必须是 family-local `09:00` 的真实 aware datetime，例如 EDT 时 `2026-09-28T09:00:00-04:00`（绝对时间 13:00 UTC），不是 09:00 UTC。

2. **DST boundary**
   - occurrence 跨 2026-11-01 DST transition；
   - 前一 Monday 09:00 为 `-04:00`，后一 Monday 09:00 为 `-05:00`；
   - active 覆盖 N 后 earliest uncovered N+1 的 offset 必须随 zone rules 更新。

3. **Explicit aware N + recurring N+1**
   - explicit aware N 保持其原 absolute instant；
   - active 覆盖 N；
   - follow-on N+1 按 family timezone 的 Monday 09:00 生成；
   - 最好与 DST boundary 合并，避免增加不必要测试数量。

4. **Invalid/unavailable timezone**
   - 为 invalid timezone 构造与自身 scope 匹配的 enrollment digest，避免测试只命中 stale-digest；
   - reconciliation 仍必须 fail closed/read-only；
   - `successor_mutation = False`。

5. PF1-PF4 现有回归全部继续通过。

## 标准库依据

Python `zoneinfo` 是标准库的 IANA timezone 实现，aware datetime 使用 `ZoneInfo` 时会按日期应用 DST offset 变化；如果指定 zone 在系统 timezone database / 可用数据源中不存在，`ZoneInfo` 会抛出 `ZoneInfoNotFoundError`。因此本轮不需要引入新依赖：有效 zone 用标准库计算，invalid/unavailable zone 直接进入 fail-closed 路径。

## 执行与验收

1. 在既有 worktree 核实 exact branch/worktree，不创建新的。
2. `git fetch origin main` 并检查 Slurm-relevant drift；无关 drift 可普通 non-force 同步，禁止 rebase/force。
3. 仅实现 PF5。
4. 先跑 PF5/G8 定向测试。
5. 重跑完整 `tests.test_slurm_workflows`，确认完整 G1-G8。
6. 重跑 `RESULT.md` 现有完整验证：
   - `python -m unittest tests.test_skill_update`
   - `python scripts/skills.py validate`
   - `python scripts/skills.py audit --all`
   - `python scripts/build_codex_marketplace.py --write --validate --check --path-report`
   - `python -m unittest discover -s tests`
7. final gate evidence 必须全部绑定同一个新的 exact product candidate；不得拼接 `569f85d...` 的旧 PASS。
8. 更新 `RESULT.md`，明确记录 PF5 timezone wall-clock/DST/invalid-zone evidence，以及 PF1-PF4 防回归。
9. 冻结新的 exact product candidate。
10. 通过现有 Clear Writing 路径更新 Issue #95 的 current candidate / current progress / next action；保持 `DOING`、classification、Area、`tracking: #95` 和空 Resolution commit。
11. 使用当前已授权 reviewed branch 的 ordinary non-force publication path。
12. 停在 `READY_FOR_FINAL_CRITIC`，附下一条 independent Critic prompt。下一轮只复核 PF5、PF1-PF4 防回归、G1-G8/full suite、Issue anchor 和 exact candidate identity，不重做 architecture review。

不得集成 main、推进 release、执行真实 Slurm mutation或自我批准。
