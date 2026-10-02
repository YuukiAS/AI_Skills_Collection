# Slurm Workflows — Critic R1 最小返修交接

日期：2026-10-02  
角色：Planner  
任务：`hpc--slurm-workflows-routing-refactor`  
目标仓库：`YuukiAS/AI_Skills_Collection`  
执行分支：`reviewed/hpc--slurm-workflows-routing-refactor`  
既有 worktree：`/tmp/ai-skills-hpc-slurm-workflows-routing-refactor`  
本轮进入时 latest main：`1c7ff0d5d2037e7a0ef2ba4bf44bdb829d3c26e6`  
Critic review commit：`f59b8f35793f661bde454a85291fee65e9fa53c4`  
被审 product candidate：`a2b511ebaca3abebb0515cd9acec8c35b58ec1d6`  
Critic review：`results/hpc--slurm-workflows-routing-refactor/PREFINAL_CRITIC_REVIEW_R1_2026-10-02.md`

这不是新任务、successor 或 architecture round。Proposal / Execution Plan v0.6 保持有效，不新增 gate、daemon、registry、state machine，不修改 Bridge Kit，不执行真实 `sbatch` / `salloc` / `scancel`。

## Planner 对 Critic 四项意见的处理

- `SWR-PF1 = ACCEPT`。当前 `_scope_digest` 没有绑定完整日历窗口与 mutation action scope，确实允许授权范围实质变化后沿用旧 enrollment。
- `SWR-PF2 = ACCEPT`。当前 reconciliation 在 active allocation 覆盖第一个窗口时直接 `reuse_active`，没有继续寻找 earliest uncovered recurrence；当前 recurrence 计算也会在 start 已过但 useful window 尚未结束时过早跳到下一周。
- `SWR-PF3 = ACCEPT`。现有 G6 证明 installed routing normal entry，但没有证明 installed candidate 从 user-local enrolled capacity state 执行 persistent-capacity reconciliation。
- `SWR-PF4 = ACCEPT`。lower-case / sanitize 不是隐私处理；repo-targeted generated reference / manifest 仍可能写入由 raw `ClusterName` 直接派生的可识别 token。

四项均属于已经批准的 v0.6 合同内实现/证据缺口，不改变 architecture、Capability Gate taxonomy、版本方向或授权边界。

## 允许修改的最小范围

优先限制在：

- `skills/tools/hpc/slurm-workflows/scripts/slurm_routing.py`
- `scripts/skills.py`
- `tests/test_slurm_workflows.py`
- `results/hpc--slurm-workflows-routing-refactor/RESULT.md`

只有 generator/validation 因真实 source 变化要求同步时，才更新现有生成产物。不要修改 Bridge Kit、中央 Plugin topology、其他 domain skill、Project Instructions Editor 内容或无关 workflow。

Repository target 继续是 `5.4.1`；`slurm-workflows` 继续是 `0.3`；central Plugins = `NO_BUMP`；Bridge Kit = `NO CHANGE`；Issue #95 保持 `DOING`。

## SWR-PF1 — 完整 enrollment scope digest

实现一个单一、确定性的 normalized enrollment scope，并让 digest 只由该对象产生。至少绑定：

- `local_site_id`
- `capacity_family_id`
- `activation_scope`
- `accepted_resource_contract`
- `allowed_resource_envelope`
- durable recurrence / timezone
- durable availability-window fields：`target_ready_by`、`successor_lead_time`、`minimum_useful_duration`、`latest_useful_end` / `cutoff`、必要的 duration/window shape
- `max_successor`
- `submit_successor`
- optional lifecycle-owned stale-successor cancel/retarget permission

不要把每周由 recurrence 推导出的 occurrence date 当成新的授权 scope；同一冻结 recurrence/window 仍应跨 occurrence 复用 enrollment。相反，修改上述任一 durable window/action 字段后旧 digest 必须失效。

`_valid_enrollment` 必须按同一 normalized object 重新计算 digest；CLI `scope-digest` 也必须走同一实现，不能维护第二套字段清单。

测试至少证明：

1. unchanged same-scope recurrence 的 digest 仍有效；
2. 改 `successor_lead_time` / `minimum_useful_duration` / `latest_useful_end` 或等价 calendar-window 字段后旧 digest 失效；
3. 改 authorized action，例如新增/撤销 stale-successor retarget 权限后旧 digest 失效；
4. missing/wrong digest 继续 fail closed。

## SWR-PF2 — earliest uncovered recurrence

把 reconciliation 从“检查一个 next window”改成“找到 earliest uncovered occurrence”。

要求保持 invariant：

```text
at most one compatible active allocation
+
at most one lifecycle-owned intended successor
```

语义必须覆盖：

1. 当前 occurrence N 仍在 useful window 内，即使其 start 已早于 `now`，也先把 N 作为当前窗口判断，不能无条件跳到 N+1；
2. active allocation 覆盖 N 时，继续检查 N+1；如果 N+1 未覆盖且 enrollment 有效，则计划 exactly one successor；
3. active allocation 覆盖 N 且已有 lifecycle-owned successor 覆盖 N+1 时，不重复；
4. 如果 active allocation 本身跨越多个 recurrence，继续推进到第一个真正 uncovered occurrence；
5. 多个 lifecycle-owned compatible successor 继续 fail closed；
6. unrelated workload / activation mismatch 保持 read-only。

不要引入 watcher/daemon。实现可以重构 window helper，但必须保持 weekly recurrence 的当前 approved semantics 和 calendar-submit capability gate。

## SWR-PF3 — G6 installed persistent-capacity normal entry

新增一个真正从 materialized installed candidate 运行的 G6 场景，不允许直接 import source helper 代替。

测试必须：

1. 通过现有真实 environment/install path materialize exact candidate；
2. 从 installed `slurm-workflows/scripts/slurm_routing.py` 加载 helper；
3. 使用临时 HOME 或显式 user-local state path 建立 `~/.config/ai-skills/slurm-workflows.toml` 等价 fixture；
4. fixture 中包含 capacity family + valid enrollment digest；
5. installed helper 重新加载该 state；
6. matching persistent workload 下证明 compatible active capacity 可复用，同时 earliest uncovered recurrence 缺 successor 时只计划一个 successor；
7. 已有 successor 时不重复；
8. unrelated CPU/batch workload 保持 read-only；
9. digest/state 行为来自 installed candidate，而不是 source-tree helper。

这只是 deterministic fake/local fixture；不得提交真实 Slurm job。

## SWR-PF4 — tracked public-safe identity

把 runtime/private identity 与 repo-targeted tracked identity 分开。

最小方向：

- runtime/local `local_site_id` 可以继续用于本机 binding、routing、state；
- 如果 local override 已显式提供 `local_site_id`，可把它视为用户给出的 local alias；
- 如果 repo-targeted materialization 的 identity 只来自 discovered raw `ClusterName`，tracked reference/manifest 必须使用稳定、不可逆的 alias/hash，例如 `local-slurm-<sha256-prefix>`；
- repo-targeted reference 中的 local-only `display_name` / site id 等所有字段都必须使用同一 public-safe identity，不能只替换一个字段后从其他字段再次泄漏；
- user-local non-tracked runtime state 不必为了这一项丢失实际 identity。

回归 fixture 继续使用明显私有值 `PrivateClusterSecret`，并对完整 tracked reference 与 manifest 的 lower-cased 文本同时断言：

```text
privateclustersecret
```

完全不存在。另补一个显式 local alias 场景，证明 alias 可稳定进入 tracked output，而 raw ClusterName 不进入。

## 执行与验证顺序

1. 在既有 worktree 核实当前 branch；不得创建新 branch/worktree。
2. `git fetch origin main`，确认 latest main 相对 Critic 观察值的 drift；若仍与 Slurm 无关，普通 merge 进入同一 reviewed branch。不得 rebase/force。
3. 仅实现 PF1–PF4。
4. 先跑受影响的 G6/G8 定向测试，再跑完整 `tests.test_slurm_workflows`，确保 G1–G8 全部重新成立。
5. 继续跑现有验证：
   - `python -m unittest tests.test_skill_update`
   - `python scripts/skills.py validate`
   - `python scripts/skills.py audit --all`
   - `python scripts/build_codex_marketplace.py --write --validate --check --path-report`
   - `python -m unittest discover -s tests`
6. 不得用旧 candidate 的 PASS 拼接 final gate；所有发布相关证据绑定同一个新的 exact product candidate。
7. 更新 `RESULT.md`，逐项把 PF1–PF4 的直接测试证据写清楚，并保留：
   - repository `5.4.1`
   - `slurm-workflows 0.3`
   - central Plugins `NO_BUMP`
   - Bridge Kit `NO CHANGE`
   - Issue #95 = `DOING`
   - real Slurm mutation = `NO`
8. 冻结新的 exact product candidate commit；证据/交接文档可以后续单独提交，但 Critic 必须明确审这个 exact candidate。
9. 交回独立 Critic，只复核 PF1–PF4、受影响 G6/G8、完整 G1–G8/full suite 与 candidate identity。不要扩大到新 architecture review。

## 外部语义复核

本轮重新核对了 SchedMD 官方说明：`sbatch --begin` 只表示最早可分配时间，`--deadline` 在无法于截止时间前完成时移除 job，`--time-min` 只允许 backfill 在分配前降低 time limit；`salloc --no-shell` 会创建保持 active 的 allocation，并可由后续 `srun --jobid` 使用。它们与已批准 v0.6 架构一致，因此本轮不需要改变 Slurm 机制，只需要修实现和 Gate evidence。
