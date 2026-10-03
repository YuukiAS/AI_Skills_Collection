问题：
Slurm Workflows 的 post-integration repair 暴露了路由和容量维护闭环的回归。当前 recovery execution 已把独立 Critic PASS 后的 R4 Slurm 语义合入最新 compatible main/release truth，复核范围仍是同一个 maintenance item：sticky state、calendar-aware capacity lifecycle、exact enrollment scope_digest、legacy race defaults cleanup、site-aware doctor、true installed G6 normal entry，以及 public-safe generated artifacts。

当前进度：
Codex 已在 Reviewed Handoff task `hpc--slurm-workflows-routing-refactor` 上完成 approved release-integration recovery。原先 conflicted worktree 已按 handoff 先做 merge-abort 安全前检，恢复到 clean reviewed branch；随后刷新 `origin/main` / `origin/release`，确认没有新的 Slurm production/source/test/version semantic drift，再用普通 non-force merge 组合最新 main truth 和已批准的 Slurm R4 semantics。

本轮正式 release baseline 已前进到 repository `5.4.1`，所以 recovery late-bound next PATCH 为 repository `5.4.2`。standalone `slurm-workflows` 保持 `0.3`；latest-main 的 `workflow-core 0.5` 保留；其他 central Plugins 为 `NO_BUMP`，Bridge Kit 为 `NO CHANGE`。

当前 product candidate `9042c6eb210a519a03fcfa127d4d59cd8197ed78` 已通过本地完整 gates：PF5/G8 定向测试、完整 `tests.test_slurm_workflows` 覆盖 G1-G8、`tests.test_skill_update`、repository validate/audit、generated Marketplace parity、version/README/changelog/registry/catalog/generated consistency、G6 installed normal-entry smoke，以及完整 `python -m unittest discover -s tests`。

GitHub Actions 已对同一个 exact candidate 显式运行 `Codex Marketplace` workflow_dispatch：run `37131439668`，`head_sha = 9042c6eb210a519a03fcfa127d4d59cd8197ed78`，结论 `success`。必需 job `codex-marketplace`、`windows-sparse-checkout`、`editable-install-smoke (ubuntu-latest)`、`editable-install-smoke (windows-latest)` 均 PASS。

Slurm R4 语义保持：`America/New_York` spring-forward gap 与 fall-back fold 都 fail closed/read-only，`successor_mutation = False`；普通 09:00 recurrence、DST offset 更新、explicit aware seed + N+1 recurrence、invalid timezone fail-closed，以及 `SWR-PF1` / `SWR-PF2` / `SWR-PF3` / `SWR-PF4` 防回归继续通过。

当前执行锚点：
- Repository: `YuukiAS/AI_Skills_Collection`
- Branch: `reviewed/hpc--slurm-workflows-routing-refactor`
- Worktree: `/tmp/ai-skills-hpc-slurm-workflows-routing-refactor`
- Task key: `hpc--slurm-workflows-routing-refactor`
- Product candidate: `9042c6eb210a519a03fcfa127d4d59cd8197ed78`
- Result evidence: `results/hpc--slurm-workflows-routing-refactor/RESULT.md`
- Recovery executor handoff: `results/hpc--slurm-workflows-routing-refactor/PARALLEL_RELEASE_INTEGRATION_RECOVERY_EXECUTOR_HANDOFF_2026-10-03.md`
- Recovery Plan v2: `results/hpc--slurm-workflows-routing-refactor/PARALLEL_RELEASE_INTEGRATION_RECOVERY_PLAN_V2_2026-10-03.md`
- Recovery Critic PASS: `results/hpc--slurm-workflows-routing-refactor/PARALLEL_RELEASE_INTEGRATION_RECOVERY_CRITIC_REVIEW_R2_2026-10-03.md`
- GitHub CI: `https://github.com/YuukiAS/AI_Skills_Collection/actions/runs/37131439668`

下一步：
等待 independent Final Critic 复核 recovery execution、candidate identity、G6/G8、完整 G1-G8/full suite、GitHub CI exact-sha evidence、Issue #95 anchor、版本面和 generated parity。此步骤未授权 real Slurm mutation、main integration 或 release advancement；Project lifecycle 继续保持 `DOING`，Resolution commit 在最终 review/integration/release closure 前保持为空。

Classification:
- `maintenance-track`
- `kind:regression`
- `scope:standalone-skill`
- `area:standalone-skill`
