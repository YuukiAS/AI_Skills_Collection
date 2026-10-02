问题：
Slurm Workflows 的 post-integration repair 暴露了路由和容量维护闭环的回归。现在需要围绕同一个 final candidate 完成复核和收口，范围包括 sticky state、calendar-aware capacity lifecycle、exact enrollment scope_digest、legacy race defaults cleanup、site-aware doctor、true installed G6 normal entry，以及 public-safe generated artifacts。

当前进度：
Codex 已在同一个 Reviewed Handoff task `hpc--slurm-workflows-routing-refactor` 上完成 R3 bounded repair。本轮只关闭 `SWR-PF5`：capacity family 的 `timezone` 现在真正控制 weekly recurrence 的 calendar 解释。实现使用 Python 标准库 `zoneinfo.ZoneInfo`；family 有 timezone 时，recurrence `weekday` / `start_time` 按 family-local wall-clock 解释；invocation `now` 会先转换到 family timezone；weekly recurrence 跨 DST 时保持当地墙上时钟时间，而不是固定第一次 occurrence 的 UTC offset。Invalid/unavailable timezone 会 fail closed/read-only，不会静默回退 UTC 后继续 successor mutation。

`SWR-PF1` / `SWR-PF2` / `SWR-PF3` / `SWR-PF4` 均保持 CLOSED，并由现有回归测试继续覆盖。

Latest `origin/main` 已无冲突合入 reviewed branch。新的 main drift 只涉及 Project Instructions Editor review 文档和 Bridge consumer-run evidence，未发现新的相关 Slurm production source/test/version/generated semantic drift。

当前 product candidate `0bdfc91f56a6bce0bfee5aea7a4b9770f4a8172d` 已通过 PF5/G8 定向测试、完整 G1-G8、`tests.test_skill_update`、repository validate/audit、generated Marketplace parity，以及完整 `python -m unittest discover -s tests`。版本边界保持 repository `5.4.1` / standalone `slurm-workflows 0.3`；central Plugins 为 `NO_BUMP`，Bridge Kit 为 `NO CHANGE`。

当前执行锚点：
- Repository: `YuukiAS/AI_Skills_Collection`
- Branch: `reviewed/hpc--slurm-workflows-routing-refactor`
- Worktree: `/tmp/ai-skills-hpc-slurm-workflows-routing-refactor`
- Task key: `hpc--slurm-workflows-routing-refactor`
- Product candidate: `0bdfc91f56a6bce0bfee5aea7a4b9770f4a8172d`
- Result evidence: `results/hpc--slurm-workflows-routing-refactor/RESULT.md`
- R3 Planner handoff: `results/hpc--slurm-workflows-routing-refactor/PLANNER_REPAIR_HANDOFF_R3_2026-10-02.md`
- R3 Critic review: `results/hpc--slurm-workflows-routing-refactor/PREFINAL_CRITIC_REVIEW_R3_2026-10-02.md`

下一步：
等待 independent final Critic review 复核 PF5、PF1-PF4 防回归、完整 G1-G8/full suite、Issue anchor 和 exact candidate identity。此步骤未授权 real Slurm mutation、main integration 或 release advancement；Project lifecycle 继续保持 `DOING`，Resolution commit 在最终 review/integration/release closure 前保持为空。

Classification:
- `maintenance-track`
- `kind:regression`
- `scope:standalone-skill`
- `area:standalone-skill`
