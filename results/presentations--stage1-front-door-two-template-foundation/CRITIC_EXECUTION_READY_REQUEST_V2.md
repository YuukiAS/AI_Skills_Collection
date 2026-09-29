# Execution-Ready Critic Re-Review Request — Presentations Stage 1 v1.1

你是 AI Research Stack 的独立 Critic thread。本轮不是重新审 architecture，也不是重新审旧 v1.0；只审 **Stage 1 execution package v1.1** 是否关闭上一轮两个 stable blockers，并检查这两处返修有没有引入新的直接回归。

不要实现代码。
不要创建 task/branch/worktree。
不要修改 production plugin。
不要运行付费 review。
不要发布。

## Active Review Context

\`\`\`text
target_repo = YuukiAS/AI_Skills_Collection
target_plugin_or_domain = presentations
design_topic_or_task_key = presentations--stage1-front-door-two-template-foundation
review_stage = stage1_execution_ready_re_review_v1_1
source_branch_or_ref = main

approved_architecture =
docs/design/PRESENTATIONS_TWO_TEMPLATE_PRODUCTION_REDESIGN_PLAN_V1_1_2026-09-28.md
@ f71e97c06938ab2ce175ccf3b4ac19da9309fda1

architecture_critic_pass =
results/presentations--two-template-production-redesign/CRITIC_REVIEW_V2.md
@ ef2f1488b5e7479a4dd504f02ac2bd02b8825c07

prior_execution_ready_review =
results/presentations--stage1-front-door-two-template-foundation/CRITIC_EXECUTION_READY_REVIEW_V1.md
@ c4fd2c64b3211529a61a33e5f80eb7afc2e2960a

stable_blockers =
PRES-S1-ER-F01
PRES-S1-ER-F02

revised_package_manifest =
results/presentations--stage1-front-door-two-template-foundation/EXECUTION_PACKAGE_V1_1.md
@ 049847f4638bb339229c748d3b8f97bd41fae72d

revised_plan =
docs/design/PRESENTATIONS_STAGE1_FRONT_DOOR_TWO_TEMPLATE_EXECUTION_PLAN_V1_1_2026-09-29.md
first_commit = eadfa649b373949be79c4da9a69045e2df2655f3

revised_goal =
docs/goals/PRESENTATIONS_STAGE1_FRONT_DOOR_TWO_TEMPLATE_GOAL_V1_1.md
first_commit = 479a865aee7a10ca1601452c37bbbf821d8d02ef

revised_kickoff =
docs/operations/prompts/PRESENTATIONS_STAGE1_FRONT_DOOR_TWO_TEMPLATE_KICKOFF_V1_1.md
first_commit = b4d1b10bd6852f2b1e92a9101b25971d94616cc7

planner_response =
results/presentations--stage1-front-door-two-template-foundation/PLANNER_RESPONSE_V1_1.md
@ 95c1f8a14a58613306a72a3a2010b942bbc235a9

execution_task = NOT_CREATED
execution_branch = NOT_CREATED
execution_worktree = NOT_CREATED
\`\`\`

## Required reads

Read latest AI_Skills \`main\` and:
- \`AGENTS.md\`
- current Planner / Critic role contracts
- current Plugin Capability Gate policy
- current Maintenance Board policy
- prior execution-ready Critic review v1
- complete v1.1 Plan
- complete v1.1 Goal
- complete v1.1 Kickoff
- v1.1 package manifest
- Planner response v1.1

Because both blockers are Reviewed Handoff control semantics, independently read latest:

\`YuukiAS/GPT_Codex_AI_Bridge_Kit main\`

At minimum verify current source/README for:
- repo-local \`reviewed-handoff task bootstrap\`;
- \`--ci-required\`;
- first-bootstrap initial state;
- \`AI_BRIDGE_REVIEWED_PLAN_V2\`;
- \`PLAN_REQUESTED -> PLAN_FROZEN\`;
- \`RUN_CODEX_EXECUTOR\`;
- CI-required \`WAITING_FOR_CI\` semantics;
- existing-task artifact-bound resume.

Do not use stale historical Bridge syntax.

---

## Priority 1 — PRES-S1-ER-F01

Previous blocker:

first bootstrap created:
\`\`\`text
PLAN_REQUESTED
RUN_GPT_PLANNER
\`\`\`

but v1.0 then jumped straight to production implementation.

Verify v1.1 now consistently freezes this chronology in Plan + Goal + Kickoff:

\`\`\`text
user sends approved Kickoff
-> canonical task bootstrap
-> PLAN_REQUESTED / RUN_GPT_PLANNER
-> only first-bootstrap REQUEST/CURRENT control metadata may be published
-> Executor/product implementation stops
-> external GPT Planner reads approved package + task state + current PLAN template
-> Planner writes task-local AI_BRIDGE_REVIEWED_PLAN_V2
-> Planner validates required sections
-> PLAN_REQUESTED -> PLAN_FROZEN
-> next_action = RUN_CODEX_EXECUTOR
-> plan_revision = 0
-> publish Planner transaction
-> only then Executor begins Stage 1
\`\`\`

Check specifically:

1. Executor is explicitly forbidden to write/freeze its own task-local Plan.
2. Initial freeze remains \`plan_revision=0\`.
3. No Stage 1 production source edit is authorized before \`PLAN_FROZEN\`.
4. Existing-task recovery later uses artifact-bound \`materialize-worktree --mode resume\`, not second bootstrap.
5. Waiting for external Planner is treated as normal waiting, not product failure.
6. Control-metadata publication does not silently authorize raw Git, alternate branch or Bridge changes.

If all are consistent with current Bridge source:

\`PRES-S1-ER-F01 = CLOSED\`

Otherwise state the exact remaining mismatch and minimum closure.

---

## Priority 2 — PRES-S1-ER-F02

Previous blocker:

Stage 1 required GitHub CI but v1.0 bootstrap omitted \`--ci-required\`.

Verify v1.1 exact bootstrap command in Plan + Goal + Kickoff now includes:

\`--ci-required\`

and the package consistently requires:

\`\`\`text
CURRENT.ci_required = true

implementation complete
-> exact candidate published
-> WAITING_FOR_CI
-> ci_status = PENDING
-> real GitHub checks
-> only after CI PASS, legal external implementation review transition
\`\`\`

Check:

1. CI is machine truth, not RESULT prose.
2. v1.1 does not add \`--visual-review-required\` or \`--text-review-required\`.
3. No paid review is smuggled into the fix.
4. CI-required chronology matches current Bridge source.

If so:

\`PRES-S1-ER-F02 = CLOSED\`

---

## Direct regression check only

Do not reopen already accepted Stage 1 product design unless these two changes broke it.

Confirm v1.1 still preserves:

- unified Presentations front door;
- research/business/shared/profile source authority;
- local-edit fast path;
- research no-format -> CUHK Beamer;
- teaching no-format -> course-standard Beamer;
- business no-format -> editable PPTX/Slides;
- explicit PPTX/Slides -> official editable adapter;
- existing/local edit -> preserve format/template;
- external locked template -> pass-through only;
- plan-only -> no fake artifact;
- exactly two built-in templates;
- exact Chapter1 direct-read/hash/fail-closed contract;
- G1 natural installed-candidate requirement;
- G5 actual source consumption + visual fidelity as non-compensating evidence;
- generated layer only through existing generator;
- no Stage 2–6 implementation;
- no #44–#48 promotion;
- no Bridge mutation;
- NO_BUMP / NO_RELEASE / no main integration.

Do not create a new blocker for ordinary implementation details that are already recoverable under the package.

---

## Authorization review

The v1.1 Kickoff should authorize only after the user sends the Critic-approved text:

- exact task bootstrap with \`--ci-required\`;
- first-bootstrap control-metadata publication needed by Planner;
- Planner-owned task-local V2 Plan transaction;
- exact reviewed-worktree Stage 1 edits after PLAN_FROZEN;
- tests/render/candidate replay;
- exact Chapter1 private-reference read;
- durable private evidence writes;
- exact reviewed-branch ordinary commits/publication needed for Planner/CI/Reviewer.

It must not authorize:
- alternate branch/worktree;
- raw Git fallback;
- force/destructive Git;
- PR/main merge;
- tag/release;
- production install/sync;
- version bump;
- paid model/API;
- credential/provider changes;
- Bridge mutation.

---

## Maintenance Board

Canonical Issues #29–#48:
- source maturity unchanged;
- Project lifecycle remains \`DOING\`.

Current execution anchor:

\`results/presentations--stage1-front-door-two-template-foundation/EXECUTION_PACKAGE_V1_1.md\`
@ \`049847f4638bb339229c748d3b8f97bd41fae72d\`

Next action:
execution-ready Critic v1.1 re-review; if PASS, user may send approved Kickoff.

If Project mutation surface / required Clear Writing is unavailable:
- do not claim sync;
- output exact pending mutation;
- do not ask user to manually maintain it.

---

## Blocker discipline

This is a narrow re-review after REVISE.

New blocker is allowed only for:
- new fact;
- critical risk previously missed;
- direct regression introduced by v1.1.

Do not move the goalposts.

Each blocker must have:
- requirement;
- direct evidence;
- causal risk;
- minimum closure.

---

## Expected output

First give a short user-readable closure explanation because this review object previously received REVISE.

Then:

\`\`\`text
PRES-S1-ER-F01 = CLOSED | STILL_OPEN
PRES-S1-ER-F02 = CLOSED | STILL_OPEN

RESULT = PASS | REVISE
REVIEW_STAGE = STAGE1_EXECUTION_READY_RE_REVIEW

REVIEWED_PACKAGE =
results/presentations--stage1-front-door-two-template-foundation/EXECUTION_PACKAGE_V1_1.md

REVIEWED_PACKAGE_COMMIT =
049847f4638bb339229c748d3b8f97bd41fae72d

APPROVED_PROPOSAL_PATH =
docs/design/PRESENTATIONS_STAGE1_FRONT_DOOR_TWO_TEMPLATE_EXECUTION_PLAN_V1_1_2026-09-29.md

APPROVED_GOAL_PATH =
docs/goals/PRESENTATIONS_STAGE1_FRONT_DOOR_TWO_TEMPLATE_GOAL_V1_1.md

APPROVED_KICKOFF_PATH =
docs/operations/prompts/PRESENTATIONS_STAGE1_FRONT_DOOR_TWO_TEMPLATE_KICKOFF_V1_1.md

PLANNER_RESPONSE =
results/presentations--stage1-front-door-two-template-foundation/PLANNER_RESPONSE_V1_1.md
@ 95c1f8a14a58613306a72a3a2010b942bbc235a9

CONTROL_CHRONOLOGY_VERDICT = ...
CI_REQUIRED_VERDICT = ...
PRODUCT_SCOPE_REGRESSION_VERDICT = ...
AUTHORIZATION_VERDICT = ...
RECOVERY_VERDICT = ...

READY_FOR_CODEX = YES | NO
\`\`\`

### If REVISE

- keep stable blocker IDs when applicable;
- do not modify Planner files yourself;
- return the complete next Planner prompt according to Critic Role Contract.

### If PASS

Set:

\`\`\`text
APPROVED_COMMIT =
049847f4638bb339229c748d3b8f97bd41fae72d

READY_FOR_CODEX = YES
NEXT_HANDOFF = CODEX
\`\`\`

Then read the exact file:

\`docs/operations/prompts/PRESENTATIONS_STAGE1_FRONT_DOOR_TWO_TEMPLATE_KICKOFF_V1_1.md\`

and reproduce its reviewed contents **verbatim**:

\`\`\`text
=== APPROVED CODEX KICKOFF BEGIN ===
<verbatim file contents>
=== APPROVED CODEX KICKOFF END ===
\`\`\`

Do not rewrite or improve the Kickoff after PASS.

Execution-ready PASS itself still does not create task/branch/worktree or authorize implementation; current-user authorization begins only when the user subsequently sends that exact approved Kickoff to Codex.
