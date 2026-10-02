问题：
Slurm Workflows 的 post-integration repair 暴露了路由和容量维护闭环的回归。当前收口仍围绕同一个 final candidate 进行，复核范围保持不变：sticky state、calendar-aware capacity lifecycle、exact enrollment scope_digest、legacy race defaults cleanup、site-aware doctor、true installed G6 normal entry，以及 public-safe generated artifacts。

当前进度：
Codex 已在 Reviewed Handoff task `hpc--slurm-workflows-routing-refactor` 上完成 R4 bounded repair。本轮只关闭 `SWR-PF5` 剩余的 fold/gap fail-closed 子项。capacity family 的 `timezone` 仍使用 Python 标准库 `zoneinfo.ZoneInfo`；recurrence local datetime 现在会通过 `fold=0` / `fold=1` 和 UTC round-trip 检测 ambiguous/fold 与 nonexistent/gap local wall-clock。

在 `America/New_York` 中，2026-03-08 Sunday `02:30` spring-forward gap 返回 `read_only_proposal`，reason 为 `nonexistent_recurrence_local_time`，`successor_mutation = False`。2026-11-01 Sunday `01:30` fall-back fold 也返回 `read_only_proposal`，reason 为 `ambiguous_recurrence_local_time`，`successor_mutation = False`。这两个 fixture 都使用与自身 scope 匹配的 valid enrollment digest，避免误命中 stale digest。

`SWR-PF5` 的其余语义继续通过：UTC invocation + `America/New_York` Monday `09:00` 正常；DST 跨周会从 `2026-10-26T09:00:00-04:00` 更新到 `2026-11-02T09:00:00-05:00`；explicit aware first occurrence 仍保持原 absolute instant，后续 recurrence 继续按 family timezone；invalid/unavailable timezone 继续 fail closed/read-only。`SWR-PF1` / `SWR-PF2` / `SWR-PF3` / `SWR-PF4` 均保持 CLOSED，并继续由现有回归测试覆盖。

Latest `origin/main` 已刷新并确认仍为 `98721a202bc557c0b9c0800e66e50cab466bfba2`，且是当前 reviewed branch 的祖先。本轮没有新的 Slurm production/source/test/version semantic drift，也没有 rebase 或 force-push。

当前 product candidate `d9da1dde5731f27f029dc1507a457a39b510d610` 已通过 PF5/G8 定向测试、完整 G1-G8、`tests.test_skill_update`、repository validate/audit、generated Marketplace parity，以及完整 `python -m unittest discover -s tests`。版本边界保持 repository `5.4.1` / standalone `slurm-workflows 0.3`；central Plugins 为 `NO_BUMP`，Bridge Kit 为 `NO CHANGE`。

当前执行锚点：
- Repository: `YuukiAS/AI_Skills_Collection`
- Branch: `reviewed/hpc--slurm-workflows-routing-refactor`
- Worktree: `/tmp/ai-skills-hpc-slurm-workflows-routing-refactor`
- Task key: `hpc--slurm-workflows-routing-refactor`
- Product candidate: `d9da1dde5731f27f029dc1507a457a39b510d610`
- Result evidence: `results/hpc--slurm-workflows-routing-refactor/RESULT.md`
- R4 Planner handoff: `results/hpc--slurm-workflows-routing-refactor/PLANNER_REPAIR_HANDOFF_R4_2026-10-02.md`
- R4 Critic review: `results/hpc--slurm-workflows-routing-refactor/PREFINAL_CRITIC_REVIEW_R4_2026-10-02.md`

下一步：
等待 independent final Critic review 复核 PF5 fold/gap fail-closed、PF5 其余已通过语义防回归、PF1-PF4 防回归、完整 G1-G8/full suite、Issue #95 anchor 和 exact candidate identity。此步骤未授权 real Slurm mutation、main integration 或 release advancement；Project lifecycle 继续保持 `DOING`，Resolution commit 在最终 review/integration/release closure 前保持为空。

Classification:
- `maintenance-track`
- `kind:regression`
- `scope:standalone-skill`
- `area:standalone-skill`
