问题：
Slurm Workflows 的 post-integration repair 暴露出路由与容量维护闭环回归。需要围绕同一个 final candidate 重新验证并收口这些内容：sticky state、calendar-aware capacity lifecycle、exact enrollment scope_digest、legacy race defaults cleanup、site-aware doctor、true installed G6 normal entry，以及 public-safe generated artifacts。

当前进度：
Codex 已在同一个 Reviewed Handoff task `hpc--slurm-workflows-routing-refactor` 上恢复旧线程已完成的 repair。现有 worktree 可以继续使用，latest `origin/main` 已无冲突合入 reviewed branch。对比 task merge base 与 latest main，未发现新的相关 Slurm production source/test semantic drift。

正式 release 已前进到 repository `5.4.0` / standalone `slurm-workflows 0.2`。本 repair 的 final candidate 已按当前版本规范收口为 repository `5.4.1` / standalone `slurm-workflows 0.3`；central Plugins 为 `NO_BUMP`，Bridge Kit 为 `NO CHANGE`。

当前执行锚点：
- Repository: `YuukiAS/AI_Skills_Collection`
- Branch: `reviewed/hpc--slurm-workflows-routing-refactor`
- Worktree: `/tmp/ai-skills-hpc-slurm-workflows-routing-refactor`
- Task key: `hpc--slurm-workflows-routing-refactor`
- Final candidate: `a2b511ebaca3abebb0515cd9acec8c35b58ec1d6`
- Result evidence: `results/hpc--slurm-workflows-routing-refactor/RESULT.md`

下一步：
等待 independent final Critic review。此步骤未授权 real Slurm mutation、main integration 或 release advancement；Project lifecycle 继续保持 `DOING`，Resolution commit 在最终 review/integration/release closure 前保持为空。

Classification:
- `maintenance-track`
- `kind:regression`
- `scope:standalone-skill`
- `area:standalone-skill`
