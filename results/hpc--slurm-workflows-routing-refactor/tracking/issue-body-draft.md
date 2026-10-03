问题：
Slurm Workflows 的路由与容量维护闭环在 post-integration repair 中暴露出回归：sticky state、calendar-aware capacity lifecycle、exact enrollment scope_digest、legacy race defaults cleanup、site-aware doctor、true installed G6 normal entry 和 public-safe generated artifacts 都需要在同一个 final candidate 上重新验证并发布收口。

当前进度：
Codex 正在同一个 Reviewed Handoff task `hpc--slurm-workflows-routing-refactor` 上恢复旧线程已经完成的 repair。现有 worktree 可恢复，latest `origin/main` 已经无冲突合入 reviewed branch；从 task merge base 到 latest main 未发现新的相关 Slurm production source/test semantic drift。正式 release 已经前进到 repository `5.4.0` / standalone `slurm-workflows 0.2`，因此本 repair 若进入正式交付，需要按当前版本规范收口为 repository `5.4.1` / standalone `slurm-workflows 0.3`，central Plugins `NO_BUMP`，Bridge Kit `NO CHANGE`。

当前执行锚点：
- Repository: `YuukiAS/AI_Skills_Collection`
- Branch: `reviewed/hpc--slurm-workflows-routing-refactor`
- Worktree: `/tmp/ai-skills-hpc-slurm-workflows-routing-refactor`
- Task key: `hpc--slurm-workflows-routing-refactor`
- Current candidate status: latest compatible main has been merged; final candidate is not frozen yet.

下一步：
Finish version/catalog/generated parity, bind the canonical standalone-skill TODO backlink, rerun G1-G8 and the full deterministic test suite on one exact new candidate, update `results/hpc--slurm-workflows-routing-refactor/RESULT.md`, push the reviewed branch without force, and stop at independent final Critic review. No real Slurm mutation, main integration, or release advancement is authorized in this step.

Classification:
- `maintenance-track`
- `kind:regression`
- `scope:standalone-skill`
- `area:standalone-skill`
