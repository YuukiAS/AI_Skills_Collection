# Reviewed Handoff Request — 051_writing_style_rebuild

## Objective

重新建立 writing-style 的下一代 heavy Chinese rewrite production path，以已经通过 Critic review 的 Clear-language architecture v0.3 为设计基线，但必须由新的 GPT Planner 根据当前 main 和 Bridge Kit 0.7.1 冻结成新的 Reviewed Handoff V2 Plan。最终用户行为应类似：用户只调用正常 installed writing-style，说：把这份较长科研报告重新组织成自然中文，数字、公式、引用、比较条件和限制都不能丢。用户不需要知道 scientific-rewrite、Meaning Map、Reader Plan、REALIZE_MEANING 或内部 task 名称；正常 plugin 应自动进入 heavy Chinese rewrite route。051 必须继承 v0.3 architecture baseline：Host Codex 是正常 generation owner；禁止恢复 per-stage paid OpenAI/Terra generation；heavy Chinese rewrite path 的四个逻辑 owner 是 scientific-rewrite、chinese-prose、writing-fidelity 和 rewrite_support.py；使用 soft isolation，REALIZE_MEANING 的正式 drafting input surface 不重新提供 raw source prose；Meaning Map 必须 meaning-centric、source anchored、bidirectional traceable，并保留 claim strength、comparator、condition/scope、uncertainty、attribution，禁止 source-copy fallback；Reader Plan 按 reader question / semantic dependency 切分，禁止把 4 paragraphs / ~2800 chars 作为 heavy production splitter；seed-transformations literal rewrite templates 不得继续作为 production writer conditioning；Latin / English QA 分类不得成为主要 writing representation；STRUCTURAL_REWRITE fidelity override 保护 claim、evidence、number、formula、citation、formal identity、comparator、condition、scope、uncertainty、caveat、attribution、conclusion strength，默认不保护 source heading、paragraph boundary、section order，除非用户明确要求；semantic auditor 可读取 raw source，但 repair packet 给 realization 时只能包含 affected meaning IDs、finding type、structured required semantic correction、exact item IDs，禁止 source quotation/source paragraph/source sentence/target rewrite sentence；assembly 没有 raw-source global rewrite authority；semantic extraction 缺失必须 fail/repair，禁止 helper source excerpt -> normalized_meaning；ordinary Latin technical word 不能仅因 Latin span 自动成为 required exact item；A/B/C 只能算 known regression，不得宣称 unseen generalization；final generalization 需要 evaluation 前冻结的小型 fresh real holdout；qualitative Product PASS 最终需要真实 human artifact judgment，tests/CI/schema/receipt 不能覆盖用户拒绝。051 后续 Planner 必须冻结 Maintenance companion: ai-skills-core，Domain owner: writing-style；workflow-core / Reviewed Handoff 负责执行流程；本 bootstrap 只初始化 REQUEST/CURRENT 并停在 PLAN_REQUESTED/READY_FOR_GPT_PLANNER，不实现 plugin。

## User-provided inputs

- Add source repositories, descriptions, screenshots, documents, or other candidate inputs here.

## User constraints

- Preserve explicit branch / deployment / product / scientific constraints from the user.
- The user should not need to participate again unless the workflow reaches `AWAIT_HUMAN_DECISION` or `BLOCKED`.
