# Slurm Workflows — Critic R2 最小返修交接

日期：2026-10-02  
角色：Planner  
任务：`hpc--slurm-workflows-routing-refactor`  
目标仓库：`YuukiAS/AI_Skills_Collection`  
执行分支：`reviewed/hpc--slurm-workflows-routing-refactor`  
既有 worktree：`/tmp/ai-skills-hpc-slurm-workflows-routing-refactor`  
本轮 latest main：`ee852eff9278fda18952f687dda12bd787f01f72`  
Critic R2 commit：`c4a8ef9df090840562107a06f2ab378cbb36dd71`  
被审 product candidate：`ed48521941f82eeedcfc490c55fa175780db64c9`  
Critic R2：`results/hpc--slurm-workflows-routing-refactor/PREFINAL_CRITIC_REVIEW_R2_2026-10-02.md`

这是同一个 task 的第二次最小 pre-final repair，不是新架构轮次，不创建 successor、branch 或 worktree。Proposal / Execution Plan v0.6 保持有效。

## Planner 对 R2 的处理

- `SWR-PF1 = ACCEPT`。当前已经统一了 window/action digest 路径，但 normalized enrollment scope 确实遗漏 durable top-level `timezone`。这会允许真实 recurring target window 因 timezone 改变而继续沿用旧授权。
- `SWR-PF2 = ACCEPT`。当前 `capacity_windows()` 在 explicit `target_occurrence` 有 start 时立即返回单窗口；对同时带 recurrence 的 family，这会重新引入“active 覆盖 N 后不继续维护 N+1”的缺口。
- `SWR-PF3 = CLOSED`，保持现有 installed persistent-capacity G6，不重新设计。
- `SWR-PF4 = CLOSED`，保持 tracked/raw site identity 分离与 ClusterName privacy，不扩大修改。

这两个 OPEN blocker 都属于已批准 v0.6 的直接实现/测试缺口，不改变 architecture、Gate taxonomy、版本方向、授权边界或 Slurm 机制。

## 允许修改的最小范围

优先仅修改：

- `skills/tools/hpc/slurm-workflows/scripts/slurm_routing.py`
- `tests/test_slurm_workflows.py`
- `results/hpc--slurm-workflows-routing-refactor/RESULT.md`

只有现有 generator/validation 因真实 source 变化要求同步时，才更新现有生成产物。不得修改 Bridge Kit、中央 Plugin topology、PF3/PF4 架构或无关 domain/workflow。

版本和生命周期保持：

- Repository：`5.4.1`
- `slurm-workflows`：`0.3`
- central Plugins：`NO_BUMP`
- Bridge Kit：`NO CHANGE`
- Issue #95：`DOING`
- `REAL_SLURM_MUTATION = NO`

## SWR-PF1 — top-level timezone 必须进入现有 normalized scope

在现有唯一 digest 路径中加入 durable top-level `timezone`。不要新增第二套 authorization schema、第二个 digest 或额外 enrollment 状态。

要求：

1. `_scope_window_contract(family)` 或其现有等价 normalized window object 必须包含 `family.get("timezone")`；
2. `_scope_digest()`、`_valid_enrollment()` 和 CLI `scope-digest` 继续共享同一 normalized object；
3. 保持现有 recurrence/window/action digest 字段不回退；
4. occurrence date 是运行时 occurrence，不是 durable scope。相同 timezone + 相同 durable recurrence/window/action scope 下，仅 occurrence 日期变化不得要求重新 enrollment；
5. 只修改 top-level `timezone` 后，旧 digest 必须失效，`capacity_reconcile` 回到 read-only proposal。

G8 至少新增两个确定性断言：

- family 使用固定 timezone，例如 `America/New_York`，保存 valid digest；对同一 durable scope 的不同 occurrence date，enrollment 继续有效；
- clone family，仅把 top-level timezone 改成另一个值，保留旧 enrollment digest；reconcile 必须 `read_only_proposal`。

不要把 invocation-level occurrence start/end 写入 durable digest 来“解决”这个测试。

## SWR-PF2 — explicit occurrence 作为首窗口，recurrence 继续产生后续窗口

修复 `capacity_windows()` 的 explicit-target 分支。

冻结语义：

1. invocation/family 提供 explicit `target_occurrence` 时，它必须是第一个窗口；
2. family 同时存在 recurrence 时，第一个 explicit occurrence 之后继续按现有 durable recurrence 生成后续 occurrence，直到现有 bounded `limit`；
3. active allocation 覆盖 explicit N 时，reconciliation 必须继续到 earliest uncovered N+1/N+k；
4. lifecycle-owned successor 覆盖该 earliest uncovered recurrence 时继续保持，不重复；
5. 没有 recurrence 的 explicit one-off target 仍只生成一个窗口；active 覆盖它时保持现有 `reuse_active` 单窗口语义；
6. 不新增 daemon、watcher、registry、state machine，不改变现有 multiple-active / multiple-successor fail-closed 和 calendar-submit gate。

当前 recurrence 实现只支持既有 weekly weekday/time contract；本轮不要扩展 recurrence DSL。对于 recurring explicit seed，沿用当前 cadence/窗口构造逻辑即可，不要引入新的日历系统。

G8 至少新增：

- recurring family + explicit current occurrence N + active 覆盖 N + valid enrollment + no successor -> `plan_one_successor` for N+1；
- recurring family + explicit N + active 覆盖 N + existing lifecycle successor 覆盖 N+1 -> `keep_successor`；
- explicit one-off target without recurrence + active 覆盖唯一窗口 -> `reuse_active`，证明没有把 one-off 误变成 recurring。

## PF3 / PF4 防回归

PF3/PF4 已由 Critic R2 CLOSED。本轮不得重写它们，但最终候选必须继续通过：

- installed persistent-capacity G6 normal-entry；
- repo-targeted tracked identity 不含 raw/normalized private ClusterName；
- explicit local alias 保持稳定。

若 PF1/PF2 的局部修改导致上述测试失败，修回 regression；不要借机调整已关闭设计。

## 执行顺序与验收

1. 在既有 worktree 核实 exact branch/worktree；不得创建新 branch/worktree。
2. `git fetch origin main`，检查相对本 handoff 的 main drift。若只是无关改动，可按已有 Reviewed Handoff/Host Policy 使用普通 non-force 同步；不得 rebase/force。
3. 仅实现 PF1/PF2。
4. 先跑 PF1/PF2/G8 定向测试。
5. 重跑完整 `tests.test_slurm_workflows`，确认 G1-G8 全部成立。
6. 重跑当前 `RESULT.md` 中既有完整验证：
   - `python -m unittest tests.test_skill_update`
   - `python scripts/skills.py validate`
   - `python scripts/skills.py audit --all`
   - `python scripts/build_codex_marketplace.py --write --validate --check --path-report`
   - `python -m unittest discover -s tests`
7. 所有 final gate evidence 必须绑定同一个新的 exact product candidate，不得把 `ed485219...` 的旧 PASS 与新 candidate 拼接。
8. 更新 `RESULT.md`：明确记录 PF1/PF2 的新回归、PF3/PF4 防回归、G1-G8/full suite、版本边界和 `REAL_SLURM_MUTATION = NO`。
9. 冻结新的 exact product candidate。
10. 按 `AI_SKILLS_MAINTENANCE_BOARD.md` 的现有 Clear Writing 路径更新 Issue #95 的 current candidate / current progress / next action；不得改变其 `DOING`、Area、classification、`tracking: #95`、Resolution commit 或证据含义。
11. 使用已授权 reviewed branch 的 ordinary non-force publication path；不创建新的远端 branch/upstream，不 main integration，不 release advancement。
12. 停在 `READY_FOR_FINAL_CRITIC`，附独立 Critic prompt。Critic 下一轮只复核 PF1/PF2、PF3/PF4 防回归、G1-G8/full suite、Issue anchor 和 exact candidate identity，不重做 architecture review。
