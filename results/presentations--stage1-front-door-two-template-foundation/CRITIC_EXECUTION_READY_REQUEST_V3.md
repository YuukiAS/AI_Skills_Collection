# Execution-Ready Critic Review Request — Presentations Stage 1 v1.2

你是 AI Research Stack 的独立 Critic thread。

本轮不是重新设计 Presentations。
只审：

\`Presentations Stage 1 execution package v1.2\`

是否可以进入 Codex execution。

不要实现代码。
不要创建 task/branch/worktree。
不要运行 paid review。
不要修改 production plugin。
不要发布。

## Active Review Context

\`\`\`text
target_repo = YuukiAS/AI_Skills_Collection
target_plugin_or_domain = presentations
design_topic_or_task_key =
presentations--stage1-front-door-two-template-foundation
review_stage = stage1_execution_ready_review_v1_2
source_branch_or_ref = main

architecture_authority =
docs/design/PRESENTATIONS_TWO_TEMPLATE_PRODUCTION_REDESIGN_PLAN_V1_1_2026-09-28.md
@ f71e97c06938ab2ce175ccf3b4ac19da9309fda1

stage1_plan =
docs/design/PRESENTATIONS_STAGE1_FRONT_DOOR_TWO_TEMPLATE_EXECUTION_PLAN_V1_2_2026-09-29.md
first_commit = 63f854ca095a6d9b8353ac803ff13c2f4cbc7f92

stage1_goal =
docs/goals/PRESENTATIONS_STAGE1_FRONT_DOOR_TWO_TEMPLATE_GOAL_V1_2.md
first_commit = 56ac9e9dbb3923957a58b3154d290448b4d68f06

stage1_kickoff =
docs/operations/prompts/PRESENTATIONS_STAGE1_FRONT_DOOR_TWO_TEMPLATE_KICKOFF_V1_2.md
first_commit = 718a45118e23e0a3c5801574801ce7e515c1f127

stage1_manifest =
results/presentations--stage1-front-door-two-template-foundation/EXECUTION_PACKAGE_V1_2.md
@ 6fe1b561bcebec7f9a6f677bb6ce3b26b91e6ca1

planner_validation =
results/presentations--stage1-front-door-two-template-foundation/PLANNER_VALIDATION_V1_2.md
@ d63c2a24789aaa0e9219bac8f0827d8d2fd0e206

prior_v1_1_package =
results/presentations--stage1-front-door-two-template-foundation/EXECUTION_PACKAGE_V1_1.md
@ 049847f4638bb339229c748d3b8f97bd41fae72d

prior_F03_closure =
results/presentations--stage1-front-door-two-template-foundation/CRITIC_EXECUTION_READY_REVIEW_V3_F03.md

execution_task = NOT_CREATED
execution_branch = NOT_CREATED
execution_worktree = NOT_CREATED
\`\`\`

## 1. Required reads

Read latest AI_Skills main:

- AGENTS.md
- docs/workflows/PLANNER_ROLE_CONTRACT.md
- docs/workflows/CRITIC_ROLE_CONTRACT.md
- docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md
- docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md
- docs/plugin-todos/presentations.md
- automation/reviewed_handoff/tasks/RESEARCH_PRESENTATION_CURRENT_ROUND.md
- architecture authority
- complete v1.2 Plan
- complete v1.2 Goal
- complete v1.2 Kickoff
- v1.2 manifest
- Planner validation
- prior v1.1/F03 reviews only where needed to confirm preserved decisions

Read latest Bridge Kit main:

\`YuukiAS/GPT_Codex_AI_Bridge_Kit\`

At minimum:
- AGENTS.md
- pyproject.toml
- README.md
- CHANGELOG.md
- current reviewed_handoff.py interface
- current Host/Machine Policy source
- results/reviewed-handoff--first-remote-publication/FORMAL_RELEASE_CLOSURE.md

Confirm current production interface, not old design docs.

## 2. Review scope

v1.2 is a bounded amendment only.

Two changes:

1. new real-use evidence promotes #49 into Stage 1:
   course-standard structural/navigation identity + ratio-aware behavior;
2. obsolete Bridge F03 blocker is removed because Bridge Kit 0.9.3 is formally available.

Do not reopen:
- unified front door architecture;
- business/editable route;
- local-edit route;
- external locked template;
- exact two built-in templates;
- Chapter1 private-reference policy;
- G1 definition;
- release boundary;
unless v1.2 directly breaks them.

## 3. #49 scope check

Canonical TODO now has:

\`#49 = PROMOTE_NOW\`

Review whether this promotion belongs to Stage 1 template foundation rather than Stage 2/3.

Required template-level additions:

- canonical sparse title/opening frame;
- section-aware navigation/state;
- PDF outline/bookmarks;
- nonintrusive top navigation where appropriate;
- bottom navigation/action affordances through ordinary Beamer mechanisms where appropriate;
- stable footline + page-number behavior;
- distinguish title/content/section-aware/closing states;
- canonical closing-frame primitive.

The closing primitive may support recap/question/Q&A/thanks, but Stage 1 must not choose which semantic closing every deck uses.

Block if v1.2 accidentally implements semantic closing selection or teaching pedagogy.

## 4. #50–#53 deferral check

Verify no Stage 1 production mechanism is introduced for:

- #50 presenter-learning companion;
- #51 lecture/source cross-reference;
- #52 assessment introduction / answer-leakage semantics;
- #53 semantic closing choice.

Also verify #35/#38/#40/#47/#48 are not pulled into Stage 1 merely because the teaching deck exposed them.

## 5. Aspect-ratio contract

Review frozen semantics:

\`\`\`text
new course-standard no explicit ratio
-> 4:3 default/reference

teaching explicit 16:9
-> same course-standard template identity, 16:9 variant

existing deck/local edit
-> preserve current ratio

external locked template
-> preserve locked ratio
\`\`\`

Check:
- 16:9 is not a third template;
- ratio is an adapter parameter, not a new universal schema;
- explicit teaching 16:9 does not route to CUHK just because CUHK is wide;
- G5 4:3 exact-reference fidelity is distinct from 16:9 invariant-identity fidelity.

## 6. G5 amendment

G5 remains non-compensating:

A. canonical source actually consumed;
B. visual fidelity.

For 4:3 course-standard:
- direct exact Chapter1 comparison;
- expected visual identity;
- structural navigation/bookmarks/footline/opening/closing.

For explicit 16:9:
- actual 16:9 ratio;
- invariant course-standard identity;
- coherent navigation/footline/opening/closing;
- no clipping/safe-area regression.

Do not require 16:9 pixel dimensions to match the 4:3 reference.

Check whether this is a real template-fidelity gate, not Stage 3 composition intelligence.

## 7. Bridge Kit 0.9.3 check

Independently verify:

\`\`\`text
Bridge version = 0.9.3
formal release target =
9dad0ba4bfa54e251f345091c5151ae991251ec9
formal distribution complete = YES
\`\`\`

Production command:

\`\`\`bash
ai-bridge reviewed-handoff task publish-first \
  --task-key <task_key> \
  --expected-repo <owner/repo>
\`\`\`

Check current Machine Policy/source confirms this is bounded first publication.

Then verify v1.2 chronology:

\`\`\`text
bootstrap --ci-required
-> PLAN_REQUESTED / RUN_GPT_PLANNER
-> exact first REQUEST/CURRENT commit only
-> task publish-first
-> external Planner PLAN V2
-> PLAN_FROZEN / RUN_CODEX_EXECUTOR
-> implementation
-> WAITING_FOR_CI / PENDING
-> real GitHub CI
-> implementation review
\`\`\`

Historical F03 must not reappear as active blocker.

The package may still require execution-machine preflight. If local runtime is stale, \`BLOCKED_BRIDGE_RUNTIME_STALE\` is correct; do not call that historical F03.

## 8. CI / visual-review distinction

Verify:

\`\`\`text
ci_required = true
visual_review_required = false
text_review_required = false
paid review = NOT AUTHORIZED
\`\`\`

At the same time:

\`G5 independent pixel-level visual review = REQUIRED\`

Judge whether this is internally coherent:
- no paid Bridge/Terra review;
- implementation Reviewer/human review surface must directly see renders + private Chapter1;
- lack of artifact access fails closed.

Do not require paid visual-review merely because G5 is visual unless current policy actually makes it mandatory.

## 9. Normal-entry / routing regression

Verify unchanged:

- research no-format -> cuhk-research;
- teaching no-format -> course-standard 4:3;
- teaching explicit 16:9 -> course-standard 16:9;
- business no-format -> editable PPTX/Slides;
- explicit PPTX/Slides -> official editable adapter;
- existing/local edit -> preserve format/template/ratio;
- external locked template -> pass-through;
- plan-only -> no artifact claim.

Only two built-in templates.

## 10. Private evidence boundary

Chapter1 remains exact private reference:

\`\`\`text
sha256 =
ed205507a6d2de320b77d47d41e55bb0b406aef48144bc2c55d3bbba8c77ddf7
\`\`\`

The annotated STAT5060 PDF is not copied into AI_Skills and course-specific content does not become runtime rules.

## 11. External targeted check

Do a small official check of Beamer current capabilities if needed.

Planner verified:
- Beamer 3.78;
- template/theme system;
- explicit aspectratio support;
- navigation infrastructure;
- Hyperref section-based bookmarks/outlines.

Do not reopen renderer choice unless current official facts contradict this.

## 12. Release boundary

Must remain:

\`\`\`text
Repository bump decision = NONE
presentations = NO_BUMP
no production install/release
no main integration
no maturity promotion
\`\`\`

This execution package is still an unreleased reviewed-branch candidate plan.

## 13. Maintenance Board

Source truth:
- #49 = PROMOTE_NOW;
- #50–#53 = NEW;
- other maturity unchanged.

Project:
- Area = presentations;
- Status = DOING.

If Project mutation surface / required Clear Writing is unavailable:
- do not claim sync;
- output exact pending mutation;
- do not ask user to manage it manually.

## 14. Blocker discipline

REVISE only for:
- direct architecture/scope contradiction;
- unsafe execution chronology;
- Gate not proving claimed capability;
- #49 leaking later teaching intelligence;
- ratio policy creating a third template or breaking routing;
- current Bridge 0.9.3 incompatibility;
- evidence/review path that cannot work.

Do not block for:
- ordinary coding details;
- desire for more tests beyond risk coverage;
- wording preferences;
- Stage 2–6 not being implemented.

## 15. Expected output

First give a concise user-readable judgment.

Then:

\`\`\`text
RESULT = PASS | REVISE
REVIEW_STAGE = STAGE1_EXECUTION_READY_V1_2

REVIEWED_PACKAGE =
results/presentations--stage1-front-door-two-template-foundation/EXECUTION_PACKAGE_V1_2.md

REVIEWED_PACKAGE_COMMIT =
6fe1b561bcebec7f9a6f677bb6ce3b26b91e6ca1

APPROVED_PLAN_PATH =
docs/design/PRESENTATIONS_STAGE1_FRONT_DOOR_TWO_TEMPLATE_EXECUTION_PLAN_V1_2_2026-09-29.md

APPROVED_GOAL_PATH =
docs/goals/PRESENTATIONS_STAGE1_FRONT_DOOR_TWO_TEMPLATE_GOAL_V1_2.md

APPROVED_KICKOFF_PATH =
docs/operations/prompts/PRESENTATIONS_STAGE1_FRONT_DOOR_TWO_TEMPLATE_KICKOFF_V1_2.md

TODO_49_VERDICT = ...
TODO_50_53_VERDICT = ...
ASPECT_RATIO_VERDICT = ...
COURSE_STANDARD_STRUCTURE_VERDICT = ...
BRIDGE_0_9_3_VERDICT = ...
CI_VERDICT = ...
VISUAL_REVIEW_VERDICT = ...
ROUTING_REGRESSION_VERDICT = ...
RELEASE_BOUNDARY_VERDICT = ...

READY_FOR_CODEX = YES | NO
\`\`\`

### If REVISE

Use stable finding IDs and automatically return the complete next Planner prompt.

### If PASS

Set:

\`\`\`text
READY_FOR_CODEX = YES
NEXT_HANDOFF = CODEX
\`\`\`

Then read the exact v1.2 Kickoff path and reproduce it verbatim between:

\`\`\`text
=== APPROVED CODEX KICKOFF BEGIN ===
<verbatim v1.2 Kickoff>
=== APPROVED CODEX KICKOFF END ===
\`\`\`

Do not rewrite it after PASS.

Critic PASS itself does not create the task or authorize execution. Current-user authorization begins only when the user subsequently sends the approved Kickoff.
