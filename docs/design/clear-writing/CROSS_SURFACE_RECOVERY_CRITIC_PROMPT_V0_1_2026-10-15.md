# Critic Prompt — Clear Writing 真实网页回归与 CI 恢复 v0.1

你现在担任 Clear Writing 当前 Reviewed Handoff 恢复包的独立 Critic。不要重新设计整个 Clear Writing，也不要重新审已经冻结的 v0.3 跨端架构。

Active Review Context：

- target_repo: `YuukiAS/AI_Skills_Collection`
- target_plugin_or_domain: `writing-style / Clear Writing`
- design_topic_or_task_key: `clear-writing--cross-surface-language-layer`
- source_branch_or_ref: `reviewed/clear-writing--cross-surface-language-layer`
- review_stage: `execution-ready recovery amendment`
- current implementation commit: `cac70c3bfcce6aeeba9c3e80adfa317235b54ee9`
- current workflow state: `NEEDS_GPT_PLANNER / ci_status=FAIL / review_round=1 / plan_revision=0`

先读取最新 main：

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/plugin-todos/writing-style.md`
- `docs/skill-todos/project-instructions-editor.md`

再读取 reviewed branch 的原任务：

- `automation/reviewed_handoff/tasks/clear-writing--cross-surface-language-layer/REQUEST.md`
- `automation/reviewed_handoff/tasks/clear-writing--cross-surface-language-layer/PLAN.md`
- `automation/reviewed_handoff/tasks/clear-writing--cross-surface-language-layer/CURRENT.json`
- `results/clear-writing--cross-surface-language-layer/REVIEW_1.md`
- `results/clear-writing--cross-surface-language-layer/PLANNER_CI_RECOVERY_DECISION_2026-10-13.md`
- `results/clear-writing--cross-surface-language-layer/CRITIC_CW_CI_01_RECOVERY_BOUNDARY_2026-10-13.md`

本轮必须审同一 package：

- `docs/design/clear-writing/CROSS_SURFACE_RECOVERY_PLAN_V0_1_2026-10-15.md`
- `docs/goals/CLEAR_WRITING_CROSS_SURFACE_RECOVERY_GOAL_V0_1_2026-10-15.md`
- `docs/operations/prompts/CLEAR_WRITING_CROSS_SURFACE_RECOVERY_KICKOFF_V0_1_2026-10-15.md`
- `results/clear-writing--cross-surface-language-layer/REAL_WEB_REGRESSION_BANK_V1.md`

重点独立判断：

1. 五个用户真实 Web 正反例是否被正确降为 known regression，而没有偷当 G7 fresh；正例是否足以防止“修清晰度 = 强制短答”。
2. 当前 `response-clarity` 架构是否应该保留，是否允许“先 replay 当前 candidate，失败才 bounded repair”，而不是先按样本改代码。
3. 新规则是否避免变成禁词、箭头/代码框禁用、英文比例、固定长度等表面特判。
4. 本 recovery 是否真的最小化了 10 月 13 日的 CI blocker，而没有用 narrow CI、删测试、VERSION 假升级或隐藏生成差异来冒充通过。
5. 是否可以批准 Presentations / Research Authoring 的 generated-only parity 修复，条件是 current canonical source 已唯一决定生成结果、source semantics / route / version / professional behavior 完全不改。若仍过宽，请给最小可执行边界，不要要求无限等待其他 owner。
6. 是否应允许 Executor 在同一 reviewed branch 普通 merge 最新 main，并在 full CI PASS 前不消耗第二轮 Reviewer。
7. Goal 与 Kickoff 是否忠实于 Plan，没有扩大账号、费用、private transcript、PIE 0.2、release/main merge、fresh evaluation 或跨领域 source-semantic 权限。

请给 PASS 或 REVISE。若 REVISE，只列真正阻断执行的最小 finding，并给 Planner 可直接继续的完整 prompt。

若 PASS，请按 Critic Role Contract 的 execution-ready 要求：

- 明确 `APPROVED_PLAN_PATH`、`APPROVED_GOAL_PATH`、`APPROVED_KICKOFF_PATH`、`APPROVED_COMMIT`;
- `READY_FOR_CODEX=YES`;
- 逐字附上你实际审过的 `CLEAR_WRITING_CROSS_SURFACE_RECOVERY_KICKOFF_V0_1_2026-10-15.md` 作为可直接发送给 Codex 的 prompt，不要自己临场改写一个新版本。

本轮 PASS 只授权 recovery execution，不等于 Clear Writing Web、G7、PIE 0.2 或正式发布 PASS。
