# Presentations Stage 1 Execution Package v1.1

**Status:** COMPLETE PACKAGE FOR EXECUTION-READY CRITIC RE-REVIEW / NOT EXECUTION AUTHORIZATION  
**Task key:** \`presentations--stage1-front-door-two-template-foundation\`  
**Package version:** 1.1  
**Date:** 2026-09-29

This manifest binds the complete revised Stage 1 execution package after the v1.0 execution-ready Critic returned \`REVISE\`.

## 1. Architecture authority

Approved architecture:

\`docs/design/PRESENTATIONS_TWO_TEMPLATE_PRODUCTION_REDESIGN_PLAN_V1_1_2026-09-28.md\`
@ \`f71e97c06938ab2ce175ccf3b4ac19da9309fda1\`

Architecture Critic PASS:

\`results/presentations--two-template-production-redesign/CRITIC_REVIEW_V2.md\`
@ \`ef2f1488b5e7479a4dd504f02ac2bd02b8825c07\`

## 2. Prior execution-ready review

\`results/presentations--stage1-front-door-two-template-foundation/CRITIC_EXECUTION_READY_REVIEW_V1.md\`
@ \`c4fd2c64b3211529a61a33e5f80eb7afc2e2960a\`

Verdict:

\`REVISE / READY_FOR_CODEX=NO\`

Stable blockers:

- \`PRES-S1-ER-F01\` — missing first-bootstrap Planner-owned task-local Plan transaction;
- \`PRES-S1-ER-F02\` — bootstrap omitted \`--ci-required\`.

## 3. Revised package objects

### Proposal / Plan v1.1

Path:

\`docs/design/PRESENTATIONS_STAGE1_FRONT_DOOR_TWO_TEMPLATE_EXECUTION_PLAN_V1_1_2026-09-29.md\`

First commit:

\`eadfa649b373949be79c4da9a69045e2df2655f3\`

### Canonical Goal v1.1

Path:

\`docs/goals/PRESENTATIONS_STAGE1_FRONT_DOOR_TWO_TEMPLATE_GOAL_V1_1.md\`

First commit:

\`479a865aee7a10ca1601452c37bbbf821d8d02ef\`

### Kickoff Draft v1.1

Path:

\`docs/operations/prompts/PRESENTATIONS_STAGE1_FRONT_DOOR_TWO_TEMPLATE_KICKOFF_V1_1.md\`

First commit:

\`b4d1b10bd6852f2b1e92a9101b25971d94616cc7\`

The three files above are the only execution package objects to approve.

The v1.0 files remain historical evidence and must not be emitted as the approved Kickoff after v1.1 review.

---

## 4. PRES-S1-ER-F01 closure

The three v1.1 objects now consistently freeze:

\`\`\`text
user sends Critic-approved Kickoff
-> exact task bootstrap
-> PLAN_REQUESTED / RUN_GPT_PLANNER
-> only first-bootstrap REQUEST/CURRENT control metadata may be published
-> Executor/product implementation stops
-> external GPT Planner reads approved package + task state + current PLAN template
-> Planner writes task-local AI_BRIDGE_REVIEWED_PLAN_V2
-> Planner self-checks Plan
-> PLAN_REQUESTED -> PLAN_FROZEN
-> next_action = RUN_CODEX_EXECUTOR
-> plan_revision = 0
-> publish Planner transaction
-> only then Executor implements Stage 1
\`\`\`

Executor is explicitly forbidden from writing/freezing its own task-local Plan.

Existing-task recovery later uses artifact-bound \`materialize-worktree --mode resume\`, not a second bootstrap.

## 5. PRES-S1-ER-F02 closure

The exact first-bootstrap command in Plan, Goal and Kickoff now includes:

\`--ci-required\`

The package requires:

\`\`\`text
CURRENT.ci_required = true
implementation candidate published
-> WAITING_FOR_CI
-> CURRENT.ci_status = PENDING
-> real GitHub CI
-> only after CI PASS, legal external implementation review transition
\`\`\`

No paid Text/Visual review flag is added.

---

## 6. Product scope unchanged

The revision does not change the Stage 1 product contract:

- unified Presentations front door;
- Marketplace/plugin interface routing;
- research/business source skill boundary;
- shared routing;
- presentation-desktop consistency;
- local-edit fast path;
- business/editable route preservation;
- CUHK canonical adapter identity/provenance;
- course-standard reconstruction adapter foundation;
- generated layer only through existing generator;
- G1;
- G5 actual source consumption + visual fidelity.

Still excluded:

- Stages 2–6 implementation;
- universal IR/schema;
- third built-in template;
- new top-level presentation skill/plugin;
- implicit-invocation workaround;
- geometry engine;
- #44–#48 promotion;
- Bridge changes;
- new workflow/state machine;
- paid review/API;
- production release/install;
- version bump;
- main integration.

## 7. Routing contract unchanged

\`\`\`text
research/group meeting/seminar/QE/oral/defense, no format
-> cuhk-research Beamer

Tutorial/lecture/teaching, no format
-> course-standard Beamer

business/executive/product/strategy/client, no format
-> editable PPTX/Slides

explicit PPTX/Slides
-> official editable adapter

existing deck/local edit
-> preserve current format/template

external locked template
-> pass-through, not built-in registry

plan-only
-> plan only
\`\`\`

## 8. Required private reference unchanged

\`\`\`text
Chapter1.pdf
sha256 =
ed205507a6d2de320b77d47d41e55bb0b406aef48144bc2c55d3bbba8c77ddf7
pages = 50
\`\`\`

Direct implementation-side and Reviewer-side reference access remains mandatory for course-standard G5.

## 9. Version / release state

\`\`\`text
Repository bump decision: NONE
Affected plugin:
- presentations: NO_BUMP
\`\`\`

This is still an unreleased Stage 1 candidate package.

## 10. Maintenance Board

Canonical Issues \`#29–#48\` keep current source maturity.

Project lifecycle remains:

\`DOING\`

After this manifest commit, the correct execution anchor is:

\`results/presentations--stage1-front-door-two-template-foundation/EXECUTION_PACKAGE_V1_1.md @ <this manifest commit>\`

Next action:

\`independent execution-ready Critic re-review, prioritizing PRES-S1-ER-F01 and PRES-S1-ER-F02\`

Do not mark PROMOTED/DONE or close issues.

## 11. Critic review contract

The next Critic must review all three v1.1 objects as one package.

Priority:
1. \`PRES-S1-ER-F01 = CLOSED ?\`
2. \`PRES-S1-ER-F02 = CLOSED ?\`
3. direct regression check caused by these two revisions.

If PASS:
- \`READY_FOR_CODEX=YES\`;
- the Critic must return the exact contents of \`PRESENTATIONS_STAGE1_FRONT_DOOR_TWO_TEMPLATE_KICKOFF_V1_1.md\` verbatim;
- the user must still send that approved Kickoff before task/branch/worktree/implementation authorization exists.
