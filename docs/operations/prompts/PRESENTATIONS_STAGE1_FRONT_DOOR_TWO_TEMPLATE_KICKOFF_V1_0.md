# Presentations Stage 1 — Codex Kickoff Draft v1.0

**Status:** DRAFT FOR EXECUTION-READY CRITIC REVIEW / NOT YET EXECUTION AUTHORIZATION  
**Task key:** \`presentations--stage1-front-door-two-template-foundation\`

This file is not executable authorization by itself. It becomes the approved Codex kickoff only if an independent execution-ready Critic returns this exact draft as approved and the user then sends that approved text to Codex.

---

你现在只执行 Presentations 已批准架构的 **Stage 1 — Front door + routing + two-template adapter foundation**。

## Authority

Repository:
\`YuukiAS/AI_Skills_Collection\`

Approved architecture:
\`docs/design/PRESENTATIONS_TWO_TEMPLATE_PRODUCTION_REDESIGN_PLAN_V1_1_2026-09-28.md\`
@ \`f71e97c06938ab2ce175ccf3b4ac19da9309fda1\`

Stage 1 Proposal/Plan:
\`docs/design/PRESENTATIONS_STAGE1_FRONT_DOOR_TWO_TEMPLATE_EXECUTION_PLAN_V1_0_2026-09-29.md\`

Canonical Goal:
\`docs/goals/PRESENTATIONS_STAGE1_FRONT_DOOR_TWO_TEMPLATE_GOAL_V1_0.md\`

完整范围、Gate、停止条件、恢复边界以以上 Stage 1 Plan + Goal 为准；不要重新设计。

## Exact task placement

Canonical checkout:
\`/home/yuukias/AI_Skills_Collection\`

Task key:
\`presentations--stage1-front-door-two-template-foundation\`

Derived branch:
\`reviewed/presentations--stage1-front-door-two-template-foundation\`

Derived worktree:
\`/home/yuukias/AI_Skills_Collection-presentations--stage1-front-door-two-template-foundation\`

先在 canonical checkout 验证 repo identity、clean state，并同步当前 \`origin/main\`。记录同步后的 \`origin/main\` OID，随后只通过当前 Bridge 的 repo-local Reviewed Handoff normal entry 创建任务：

\`\`\`bash
ai-bridge reviewed-handoff task bootstrap \
  --task-key presentations--stage1-front-door-two-template-foundation \
  --expected-repo YuukiAS/AI_Skills_Collection \
  --expected-base-commit <同步后当前 origin/main OID> \
  --objective "Implement only approved Presentations Stage 1: unified front door/routing and two-template adapter foundation."
\`\`\`

不得用 raw \`git worktree add\`、其他 branch/worktree、另一个 clone 或 \`/tmp\` 替代。若 exact task 已存在但不匹配当前批准 package，停止并返回 Planner；不要自行重建或覆盖。

## Required capabilities

按仓库规则同时使用：
- \`workflow-core\`
- \`ai-skills-core\` / AI Skills Maintainer
- \`presentations\`

它们不得扩大 frozen Stage 1 scope。

## Required private reference

Stage 1 开始 substantive implementation 前，必须直接读取用户提供的 exact：

\`Chapter1.pdf\`

Expected SHA-256:
\`ed205507a6d2de320b77d47d41e55bb0b406aef48144bc2c55d3bbba8c77ddf7\`

优先 durable private locator:
\`/home/yuukias/AI_Skills_Collection/private/exports/presentations--stage1-front-door-two-template-foundation/inputs/Chapter1.pdf\`

我发送这段经 Critic 批准的 kickoff，即授权本 Stage 1 为实现 \`course-standard\` 和 G5 review 读取这一个 private reference，并在上述 task-owned durable \`private/exports\` 范围保存必要的 reference render / candidate render / review bundle；不得打印、commit、push 其正文或页面内容。

若文件不可达或 hash 不符：
\`BLOCKED_REFERENCE_UNAVAILABLE\`
并停止 substantive implementation。不得根据 Plan 摘要、截图、OCR 摘要或记忆自行复现。

CUHK canonical authority仍是：
\`skills/tools/documents-media/presentations/shared/templates/cuhk/beamer/source/\`

## Implement only Stage 1

必须完成：
- Presentations unified front door；
- Marketplace/plugin interface routing；
- research/business source skill boundary；
- shared routing；
- \`presentation-desktop\` profile consistency；
- \`local-edit\` fast path；
- business/editable route preservation；
- \`cuhk-research\` canonical adapter identity/provenance；
- \`course-standard\` canonical reconstruction adapter foundation；
- generated layer only through existing generator；
- G1；
- G5 actual consumption + visual fidelity foundation；
- corresponding targeted + broad regression required by the Plan。

Routing invariants必须保持：

\`\`\`text
research/group meeting/seminar/QE/oral/defense, no format
-> cuhk-research Beamer

Tutorial/lecture/teaching, no format
-> course-standard Beamer

business/executive/product/strategy/client, no format
-> editable PPTX/Slides

explicit PPTX/Slides
-> official editable adapter

existing deck / local edit
-> preserve current format/template

external locked template
-> pass-through; never register as third built-in template

plan-only
-> plan only; never claim a generated deck
\`\`\`

Local edit必须先进入 Presentations intake，但直接走轻量 fast path；不得跑 full semantic planning。

## G1 / G5 are product gates, not helper gates

G1：
必须用 exact committed candidate 在 fresh supported runtime 中，通过真实安装后的 Presentations plugin 接收自然请求。不得用 helper、fixture、直接 script、route receipt 单独冒充 PASS。

Beamer route要真实产出 \`.tex -> PDF -> render\`。
Editable route要使用真实支持的 official Presentation/Slides surface；不得用 \`python-pptx\`、重建 PDF、route receipt 替代。若该 surface 当前不可用，返回：
\`BLOCKED_REAL_EDITABLE_ADAPTER_SURFACE\`
不得静默降级。

G5：
两个 built-in template 都必须分别证明：
1. canonical source actually consumed；
2. rendered visual fidelity。

两项不能互相抵消。

对 \`course-standard\`，Reviewer 必须直接拿到 exact private \`Chapter1.pdf\` 与 candidate render 做 visual review；不能拿 Planner 摘要替代。

## Strict out of scope

不得进入：
- Stage 2 semantic sequence；
- Stage 3 composition；
- Stage 4 citation/language；
- Stage 5 existing-deck runtime；
- Stage 6 final generalization/release；
- new universal IR/schema；
- third built-in template；
- new top-level presentation skill/plugin；
- implicit-invocation hack；
- new geometry engine；
- #44–#48 promotion；
- Bridge Kit changes；
- new workflow/state machine/ledger/database；
- paid API/model review；
- production plugin install/sync/release；
- version bump；
- PR/main merge/integration。

如果 Stage 1 需要上述任一变化才能成立，停止并返回 \`NEEDS_GPT_PLANNER\`，给直接证据。

## Validation / evidence

先 deterministic regression，再做 real candidate evidence。

至少按当前 repo contract运行：
- targeted presentations tests；
- Marketplace generator write/validate/check/path-report；
- skills validation；
- full/risk-matched repo regression；
- Reviewed Handoff validation；
- \`git diff --check\`；
- required GitHub CI；
- G1 natural installed-candidate evidence；
- G5 source-consumption + real render evidence。

Candidate replay必须针对 exact committed candidate；receipt只能证明 candidate identity/consumption，不能替代 G1/G5 产品判断。

future-required private artifacts在 task worktree cleanup 前必须复制到 canonical checkout：
\`/home/yuukias/AI_Skills_Collection/private/exports/presentations--stage1-front-door-two-template-foundation/\`
并记录必要 hash/locator。

## Git / side-effect authorization

我发送这段经 Critic 批准的 kickoff，仅授权：
- exact Reviewed task bootstrap；
- exact reviewed worktree内 task-owned Stage 1 source edits；
- tests、local rendering、candidate replay；
- 上述 exact private reference读取与 task-owned durable private evidence写入；
- exact reviewed branch上的普通 commits；
- 为 CI/Reviewer 所需的 exact reviewed branch普通 non-force publication。

不授权：
- alternate branch/worktree；
- force/destructive Git；
- PR；
- main merge/integration；
- tag/release；
- production plugin install/sync；
- version bump；
- paid model/API；
- credential/provider changes；
- Bridge Kit mutation。

## Stop / handoff

current released \`presentations 0.3\` / latest released plugin继续作为 rollback boundary。

遇到以下情况 fail closed：
- \`BLOCKED_DISCOVERY_CONSUMER\`
- \`BLOCKED_REFERENCE_UNAVAILABLE\`
- \`BLOCKED_REAL_EDITABLE_ADAPTER_SURFACE\`
- \`BLOCKED_TEMPLATE_PROVENANCE\`
- \`BLOCKED_GENERATOR_ARCHITECTURE\`
- \`NEEDS_GPT_PLANNER\`

不要绕过。

Stage 1 完成后按当前 Reviewed Handoff 合同提交真实 RESULT、CI 状态和 implementation review evidence。Stage 1 implementation PASS 不等于 architecture V1.1 全部完成，不授权 Stage 2、不授权 main integration、不授权 release。
