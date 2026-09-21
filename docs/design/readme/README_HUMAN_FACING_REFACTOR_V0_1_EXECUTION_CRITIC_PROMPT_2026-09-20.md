# README Human-Facing Refactor v0.1 — Execution-Ready Critic Review

你是 AI Research Stack 的长期独立 Critic thread。

继续同一个 `readme-human-facing-refactor` 轮次。v0.2 design 已 PASS；本轮只审 execution package 是否忠实、最小、可执行且没有扩大授权。不要实现 README，不创建 task branch/worktree，不启动 Executor，不修改任何 production/source，也不要替用户发送 Kickoff。

## Active Review Context

- target_repo: `YuukiAS/AI_Skills_Collection`
- target_plugin_or_domain: repository human-facing README / workflow-doc dependency cleanup
- design_topic_or_task_key: `readme-human-facing-refactor`
- source_branch_or_ref: latest `main`
- review_stage: `execution-ready review`
- approved design: `docs/design/readme/README_HUMAN_FACING_REFACTOR_V0_2_2026-09-20.md` v0.2
- approved design commit: `f3e7ec12db8c1704d919e6124c9875babd67bb97`
- design result: `PASS`
- closed findings: `README-R1`, `README-R2`
- execution package version: `v0.1`
- exact package commit: `95a32529f6f3966072e0a494edcf70b9c005ba72`

同版 execution package：

1. Plan  
   `docs/design/readme/README_HUMAN_FACING_REFACTOR_EXECUTION_PLAN_V0_1_2026-09-20.md`

2. Canonical Goal  
   `docs/goals/README_HUMAN_FACING_REFACTOR_V0_1_GOAL.md`

3. Kickoff Draft  
   `docs/operations/prompts/README_HUMAN_FACING_REFACTOR_V0_1_KICKOFF.md`

## 强制读取

重新读取 latest main，并按 Critic contract 核对：

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md`
- `VERSION`
- 当前 `README.md`
- `scripts/codex_marketplace_config.json`
- approved design v0.2
- 上述 exact package commit 中的 Plan + Goal + Kickoff

如果 latest main 相比 package commit 只有本 Critic handoff prompt 或其他无关 docs 变化，不机械撤销 design/package authority；只有相关语义漂移才阻塞。

本轮不重开 design，不机械要求 Plugin Capability Gate Matrix，因为这不是 production plugin refinement。

## 重点审查

### E1 — Scope fidelity

确认 implementation mutation 只允许：

- `README.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`

两个 Role Contract 仅删除 README-template dependency，不改变角色职责、PASS/REVISE、handoff 语义或 machine-readable handoff 形态。

确认没有借 README 重构修改：

- `AGENTS.md`
- Capability Gate Policy
- Versioning Policy
- `VERSION`
- Marketplace source/generated layer
- plugins / skills / profiles
- Bridge Kit

### E2 — Product contract fidelity

确认 Goal 完整保留已批准 design：

- README 是短、美观、人类可读项目首页；
- Hero；
- 轻量 current Repository / CLI version；
- 十个中央 plugin；
- display name/version 取自 Marketplace config；
- 一句自然中文用途不扩大真实能力；
- 复用本地 SVG；
- 两列 preferred；
- 真实 render 不佳时允许 `two-column -> one-column -> simpler native layout`；
- 禁止外部 badge、自定义 CSS、README generator/schema/build chain/runtime；
- 一个最小使用入口；
- footer 只取 2–4 个现有具体文档入口；
- 删除 design 已批准移出首页的内部 workflow/HPC/Presentation/验证命令/Planner-Critic prompt 内容。

### E3 — Version contract

确认：

- Repository / CLI version 在执行时从 `VERSION` 核对；
- 当前 source 为 `5.0.5`；
- Repository bump = `NONE`；
- 十个中央 plugin = `NO_BUMP`；
- execution package 没有要求修改 Versioning Policy 或 Marketplace versions。

### E4 — Real GitHub visual acceptance

重点检查 execution contract 是否真的要求直接观察已 push task branch 的 GitHub README，而不是本地 Markdown/CI 代理。

需要确认：

- wide / narrow；
- light / dark；
- SVG 实际显示；
- 普通视觉问题由 Executor 在批准 fallback 内自行调整；
- 没有浏览能力时如实报告 environment blocker，不能伪造 PASS；
- 这套要求不过重，也不要求为 README 引入新 renderer/build chain。

### E5 — Exact execution identity / authorization envelope

检查：

- repository: `YuukiAS/AI_Skills_Collection`
- task: `readme_human_facing_refactor`
- branch: `reviewed/readme_human_facing_refactor`
- worktree: `/tmp/ai-skills-readme-human-facing-refactor`

Kickoff 只在用户实际发送后才形成授权。

允许范围应仅包括本任务所需 ordinary read/fetch、exact branch/worktree、三个批准文件修改、内容检查/现有 tests/真实 GitHub render、commit、ordinary non-force push 到 exact task branch。

确认没有授权：

- merge main
- force/history rewrite
- paid API
- provider / credential / private artifact
- plugin production/generated mutation
- Bridge Kit 或其他外部 side effect。

### E6 — Completion / handoff

确认 Executor 完成后必须报告：

- final candidate commit；
- 最终 gallery/layout；
- VERSION / Marketplace parity；
- exact three-file diff scope；
- real GitHub wide/narrow + light/dark evidence locator；

然后停止等待 independent implementation review，不自行 merge main 或宣布 release。

## 输出要求

先用正常中文给出 execution-ready 判断，说明 package 是否忠实于已 PASS 的 design，是否过重/过简，以及授权边界是否准确。

然后输出：

`RESULT = PASS | REVISE`

`REVIEW_OBJECT = execution package v0.1 @ 95a32529f6f3966072e0a494edcf70b9c005ba72`

若 REVISE：

- 给稳定 blocker ID、证据、因果风险、最小关闭条件；
- 按 `CRITIC_ROLE_CONTRACT.md` 自动附完整 Planner prompt；
- 不自己改 package。

若 PASS：

必须按 `CRITIC_ROLE_CONTRACT.md` §6.1：

`APPROVED_PROPOSAL_PATH=docs/design/readme/README_HUMAN_FACING_REFACTOR_EXECUTION_PLAN_V0_1_2026-09-20.md`

`APPROVED_GOAL_PATH=docs/goals/README_HUMAN_FACING_REFACTOR_V0_1_GOAL.md`

`APPROVED_KICKOFF_PATH=docs/operations/prompts/README_HUMAN_FACING_REFACTOR_V0_1_KICKOFF.md`

`APPROVED_COMMIT=95a32529f6f3966072e0a494edcf70b9c005ba72`

`READY_FOR_CODEX=YES`

`NEXT_HANDOFF=CODEX`

并逐字输出已经审过的 Kickoff Draft 中 `## Kickoff` 正文：

`=== APPROVED CODEX KICKOFF BEGIN ===`
<verbatim approved kickoff>
`=== APPROVED CODEX KICKOFF END ===`

不得 PASS 后重新设计或改写 kickoff；若 kickoff 需要实质修改，应返回 REVISE。
