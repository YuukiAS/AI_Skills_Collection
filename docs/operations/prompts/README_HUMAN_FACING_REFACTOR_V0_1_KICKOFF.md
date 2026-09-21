# README Human-Facing Refactor — Codex Kickoff Draft

- Execution package version: `v0.1`
- Task: `readme_human_facing_refactor`
- Plan: `docs/design/readme/README_HUMAN_FACING_REFACTOR_EXECUTION_PLAN_V0_1_2026-09-20.md` v0.1
- Goal: `docs/goals/README_HUMAN_FACING_REFACTOR_V0_1_GOAL.md` v0.1
- Approved design: `docs/design/readme/README_HUMAN_FACING_REFACTOR_V0_2_2026-09-20.md` v0.2
- Status: `DRAFT_NOT_AUTHORIZED`

只有独立 Critic 对本 exact Plan + Goal + Kickoff 同版返回 `READY_FOR_CODEX=YES` 后，用户实际发送下面的 Kickoff 正文才授权执行。

## Kickoff

执行 `readme_human_facing_refactor`，严格按已审 v0.1 Plan/Goal 和已通过的 README design v0.2；不要重新设计。

Repository：`YuukiAS/AI_Skills_Collection`  
Exact branch：`reviewed/readme_human_facing_refactor`  
Exact task-owned worktree：`/tmp/ai-skills-readme-human-facing-refactor`

从届时最新、仍包含获批 package 且无相关语义漂移的 `origin/main` 开始。只允许修改：

- `README.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`

README 按 Goal 收敛成人类项目首页：Hero、当前 Repository / CLI version、十个中央 plugin 的本地 SVG + display name + version + 一句自然中文用途、一个最小使用入口、2–4 个现有文档链接。display name/version 以 `scripts/codex_marketplace_config.json` 为准，Repository / CLI version 以 `VERSION` 为准。

两列 gallery 是首选，不是硬要求。必须查看已 push branch 上的真实 GitHub README render；若宽/窄或 light/dark 下不佳，在已批准范围内自行按 `两列 -> 一列 -> 更简单原生布局` 调整，不把普通排版调试甩给用户。不得引入外部 badge、自定义 CSS、README generator、schema、build chain 或 README runtime。

两个 Role Contract 只删除 README-template dependency，保持现有角色职责、PASS/REVISE 与 handoff 语义不变。

本次授权允许完成任务所需的 ordinary read/fetch、创建上述 exact branch/worktree、内容检查、现有 tests、真实 GitHub render/check、stage/commit，以及 ordinary non-force push 到上述 exact task branch。

明确不授权：merge `main`、force/history rewrite、其他 branch/tag mutation、paid API、provider、credential、private artifact、plugin production/generated mutation、profiles/skills/Marketplace source 修改、`AGENTS.md`、Versioning Policy、Capability Gate Policy 或 Bridge Kit 修改。

Repository bump = `NONE`；所有中央 plugin = `NO_BUMP`。

完成后报告 final candidate commit、最终布局、VERSION/Marketplace parity、三个文件的 exact diff scope，以及真实 GitHub wide/narrow + light/dark visual evidence locator；然后停止等待独立 implementation review，不 merge main。

若必须扩大三个文件范围、改变 Role Contract 实质语义、引入新构建链/外部 provider，或 exact branch/worktree ownership 不清，停止并回 Planner。
