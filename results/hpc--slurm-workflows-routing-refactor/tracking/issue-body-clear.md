问题：
Slurm Workflows 在 post-integration repair 中暴露出路由与容量维护闭环的回归。需要在同一个 final candidate 上重新验证并收口以下内容：sticky state、calendar-aware capacity lifecycle、exact enrollment scope_digest、legacy race defaults cleanup、site-aware doctor、true installed G6 normal entry，以及 public-safe generated artifacts。

当前进度：
Codex 正在同一个 Reviewed Handoff task `hpc--slurm-workflows-routing-refactor` 上恢复旧线程已完成的 repair。现有 worktree 可以继续使用；latest `origin/main` 已无冲突合入 reviewed branch。对比 task merge base 与 latest main，暂未发现新的相关 Slurm production source/test semantic drift。

正式 release 已前进到 repository `5.4.0` / standalone `slurm-workflows 0.2`。因此，如果本 repair 进入正式交付，应按当前版本规范收口为 repository `5.4.1` / standalone `slurm-workflows 0.3`；central Plugins 为 `NO_BUMP`，Bridge Kit 为 `NO CHANGE`。

当前执行锚点：
- Repository: `YuukiAS/AI_Skills_Collection`
- Branch: `reviewed/hpc--slurm-workflows-routing-refactor`
- Worktree: `/tmp/ai-skills-hpc-slurm-workflows-routing-refactor`
- Task key: `hpc--slurm-workflows-routing-refactor`
- Current candidate status: latest compatible main has been merged; final candidate is not frozen yet.

下一步：
完成 version/catalog/generated parity，绑定 canonical standalone-skill TODO backlink，在同一个 exact new candidate 上重新运行 G1-G8 和 full deterministic test suite，更新 `results/hpc--slurm-workflows-routing-refactor/RESULT.md`，以非 force 方式推送 reviewed branch，然后停在 independent final Critic review。此步骤未授权 real Slurm mutation、main integration 或 release advancement。

Classification:
- `maintenance-track`
- `kind:regression`
- `scope:standalone-skill`
- `area:standalone-skill`
