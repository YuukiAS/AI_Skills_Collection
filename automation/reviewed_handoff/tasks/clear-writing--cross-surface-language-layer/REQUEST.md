# Reviewed Handoff Request — clear-writing--cross-surface-language-layer

## Objective

实现经执行前 Critic 批准的 Clear Writing v0.3 跨 ChatGPT/Codex 通用表达层；原五项标识不变，新增 response-clarity，证明无 @ 正常入口和领域真实消费；Research Authoring/PIE 不在范围。

## User-provided inputs

- Repository: `YuukiAS/AI_Skills_Collection`
- Task key: `clear-writing--cross-surface-language-layer`
- Reviewed branch: `reviewed/clear-writing--cross-surface-language-layer`
- Reviewed worktree path: `/overflow/htzhu/mingcheng_new/AI_Skills_Collection-clear-writing--cross-surface-language-layer`
- APPROVED_V03_PACKAGE_COMMIT: `b960ec57941fc058a22ca8896c92d5dc19191009`
- EXECUTION_CRITIC_REVIEW_PATH: `docs/design/clear-writing/CROSS_SURFACE_LANGUAGE_LAYER_EXECUTION_CRITIC_REVIEW_V0_3_2026-10-12.md`
- EXECUTION_CRITIC_REVIEW_COMMIT: `0f8ee7d98ba8890d074b488c87cb65c20cd8b82f`
- Critic decision: `PASS`; `READY_FOR_CODEX=YES`

Approved v0.3 package paths at `b960ec57941fc058a22ca8896c92d5dc19191009`:

1. `docs/design/clear-writing/CROSS_SURFACE_LANGUAGE_LAYER_PROPOSAL_V0_3_2026-10-12.md`
2. `docs/design/clear-writing/CROSS_SURFACE_LANGUAGE_LAYER_GATE_MATRIX_V0_3_2026-10-12.md`
3. `docs/design/clear-writing/CROSS_SURFACE_LANGUAGE_LAYER_EXECUTION_PLAN_V0_3_2026-10-12.md`
4. `docs/goals/CLEAR_WRITING_CROSS_SURFACE_LANGUAGE_LAYER_GOAL_V0_3.md`
5. `docs/operations/prompts/CLEAR_WRITING_CROSS_SURFACE_LANGUAGE_LAYER_KICKOFF_V0_3.md`
6. `docs/design/clear-writing/CROSS_SURFACE_LANGUAGE_LAYER_EXECUTION_CRITIC_PROMPT_V0_3_2026-10-12.md`

The user explicitly authorized starting this formal task from the approved v0.3 Kickoff, Goal and execution package. The draft-stage statements in the Kickoff and Goal saying the package lacks Critic PASS or is for future use are superseded by the real review record above and the current user authorization; all other task scope, execution constraints, authority boundaries and non-goals remain in force.

The reviewed branch is based on `origin/main` and is not expected to contain the planner branch's v0.3 design files. The Planner must read the approved package and review record by the exact Git commits and paths recorded above, then freeze a task-local PLAN before any Executor implementation. Executor must not skip Planner approval or treat this REQUEST as a frozen implementation plan.

## User constraints

- Reviewed worktree locator: /overflow/htzhu/mingcheng_new/AI_Skills_Collection-clear-writing--cross-surface-language-layer

- Preserve explicit branch / deployment / product / scientific constraints from the user.
- The user should not need to participate again unless the workflow reaches `AWAIT_HUMAN_DECISION` or `BLOCKED`.
- Use the Bridge Kit Reviewed Handoff flow. First commit and first remote publication must contain only this task's `REQUEST.md` and `CURRENT.json`.
- Do not modify production source, generated payloads, version files, changelogs, README, personal ChatGPT plugin state, Project instructions, or account settings during this bootstrap stage.
- Do not merge to `main`, move `release`, publish a formal release, create a PR, or create/update personal ChatGPT plugins before the later authorized gates in the approved contract.
- Personal ChatGPT plugin creation and account operations retain their separate authorization boundaries from the approved v0.3 contract.
