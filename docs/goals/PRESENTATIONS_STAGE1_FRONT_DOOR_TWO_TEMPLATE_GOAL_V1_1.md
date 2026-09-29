# Canonical Goal — Presentations Stage 1 Front Door + Two-Template Foundation

**Goal version:** 1.1  
**Status:** DRAFT FOR EXECUTION-READY CRITIC RE-REVIEW / NOT YET USER EXECUTION AUTHORIZATION  
**Task key:** \`presentations--stage1-front-door-two-template-foundation\`  
**Repository:** \`YuukiAS/AI_Skills_Collection\`  
**Approved architecture:** \`docs/design/PRESENTATIONS_TWO_TEMPLATE_PRODUCTION_REDESIGN_PLAN_V1_1_2026-09-28.md @ f71e97c06938ab2ce175ccf3b4ac19da9309fda1\`  
**Stage 1 Execution Plan:** \`docs/design/PRESENTATIONS_STAGE1_FRONT_DOOR_TWO_TEMPLATE_EXECUTION_PLAN_V1_1_2026-09-29.md\`  
**Prior execution-ready Critic review:** \`results/presentations--stage1-front-door-two-template-foundation/CRITIC_EXECUTION_READY_REVIEW_V1.md @ c4fd2c64b3211529a61a33e5f80eb7afc2e2960a\`

## 1. Goal

Implement **only Stage 1** of the Critic-approved Presentations V1.1 architecture:

> make Presentations a real unified intake/routing front door while preserving existing editable business/PPTX behavior, establish local-edit as a lightweight pass-through mode, preserve exact CUHK template identity, and add a canonical course-standard Beamer adapter reconstructed from the exact user-provided course reference.

This v1.1 Goal also freezes the mandatory Reviewed Handoff control chronology:

\`\`\`text
current-user approved Kickoff
-> exact first bootstrap with --ci-required
-> PLAN_REQUESTED / RUN_GPT_PLANNER
-> external GPT Planner writes task-local AI_BRIDGE_REVIEWED_PLAN_V2
-> PLAN_REQUESTED -> PLAN_FROZEN
-> RUN_CODEX_EXECUTOR
-> only then Stage 1 production implementation
-> exact candidate publication
-> WAITING_FOR_CI / ci_status=PENDING
-> real GitHub CI
-> external implementation review
\`\`\`

Do not implement Stages 2–6.

---

## 2. Exact execution topology

Expected canonical checkout:

\`/home/yuukias/AI_Skills_Collection\`

Task key:

\`presentations--stage1-front-door-two-template-foundation\`

Derived Reviewed branch:

\`reviewed/presentations--stage1-front-door-two-template-foundation\`

Derived sibling worktree:

\`/home/yuukias/AI_Skills_Collection-presentations--stage1-front-door-two-template-foundation\`

Base:

post-sync \`origin/main\` OID containing the execution-ready Critic-approved v1.1 package.

From the canonical repo cwd, first bootstrap must be:

\`\`\`bash
ai-bridge reviewed-handoff task bootstrap \
  --task-key presentations--stage1-front-door-two-template-foundation \
  --expected-repo YuukiAS/AI_Skills_Collection \
  --expected-base-commit <POST_SYNC_ORIGIN_MAIN_OID> \
  --objective "Implement only approved Presentations Stage 1: unified front door/routing and two-template adapter foundation." \
  --ci-required
\`\`\`

No raw Git worktree creation, alternate branch/worktree or second bootstrap.

---

## 3. Required first-bootstrap Planner transaction

The first bootstrap is a **control-plane step only**.

Successful bootstrap must leave:

\`\`\`text
CURRENT.state = PLAN_REQUESTED
CURRENT.next_action = RUN_GPT_PLANNER
CURRENT.ci_required = true
plan_revision = 0
\`\`\`

At this point, Executor must not modify Presentations production source.

Only first-bootstrap \`REQUEST.md\` / \`CURRENT.json\` control metadata needed by the external Planner may be committed/published.

Then external GPT Planner must read:
- task \`REQUEST.md\`;
- task \`CURRENT.json\`;
- approved architecture;
- Stage 1 Plan v1.1;
- this Goal v1.1;
- durable execution-ready Critic PASS for v1.1;
- current \`automation/reviewed_handoff/templates/PLAN.md\`;
- current Planner/Reviewed Handoff contracts.

Planner writes task-local:

\`automation/reviewed_handoff/tasks/presentations--stage1-front-door-two-template-foundation/PLAN.md\`

with current schema:

\`AI_BRIDGE_REVIEWED_PLAN_V2\`

The task-local Plan must faithfully translate this already approved execution package. It must not redesign product scope.

Planner validates required sections and legally transitions:

\`\`\`text
PLAN_REQUESTED -> PLAN_FROZEN
CURRENT.next_action = RUN_CODEX_EXECUTOR
plan_revision = 0
\`\`\`

Only after this published Planner transaction may Executor begin Stage 1 implementation.

Executor must never write/freeze its own Plan.

Existing-task recovery later uses artifact-bound:

\`ai-bridge reviewed-handoff materialize-worktree --mode resume\`

not a second bootstrap.

---

## 4. Required central-plugin capabilities

Use:
- \`workflow-core\`;
- \`ai-skills-core\` / AI Skills Maintainer;
- \`presentations\`.

These are maintenance/domain companions, not scope-expansion authority.

---

## 5. Required private/reference input

### Chapter1 reference — required

Exact file:

\`\`\`text
Chapter1.pdf
sha256 = ed205507a6d2de320b77d47d41e55bb0b406aef48144bc2c55d3bbba8c77ddf7
pages = 50
\`\`\`

Preferred durable execution-machine locator:

\`/home/yuukias/AI_Skills_Collection/private/exports/presentations--stage1-front-door-two-template-foundation/inputs/Chapter1.pdf\`

Before substantive course-standard work:
- directly read the exact file;
- verify SHA;
- inspect/render it;
- distinguish stable template style from PDF highlight annotations and course content.

Unavailable/mismatched:

\`BLOCKED_REFERENCE_UNAVAILABLE\`

Stop before substantive implementation.

Do not reconstruct from Planner prose, screenshots, OCR summaries or memory.
Do not commit/push private reference pages/content.

### CUHK authority

Canonical source remains:

\`skills/tools/documents-media/presentations/shared/templates/cuhk/beamer/source/\`

Private CUHK attachments may support visual cross-check but never replace canonical production authority.

---

## 6. Required routing behavior

| Natural request | Required route |
|---|---|
| research group meeting / research update / seminar / paper talk / journal club, no format | cuhk-research Beamer |
| QE / oral / defense, no venue template | cuhk-research Beamer |
| Tutorial / lecture / teaching / formula walkthrough, no format | course-standard Beamer |
| generic non-branded Beamer / LaTeX slides | course-standard unless CUHK explicitly requested |
| business / executive / product / strategy / client, no format | editable PPTX/Slides |
| explicit PPTX / Slides / editable | official editable Presentation/Slides |
| existing deck + feedback | preserve current format/template; Stage 1 routes only |
| small existing-deck edit | Presentations intake -> local-edit fast path |
| explicit locked course/venue/client template | pass-through, not built-in registry |
| outline/storyline/notes only | plan-only, no fake artifact completion |

Local edit:
- must still enter Presentations intake;
- must skip full planning;
- must preserve current format/template;
- Stage 1 may route/escalate only; Stage 5 owns actual revision runtime.

---

## 7. Source ownership

Primary source:
- \`scripts/codex_marketplace_config.json\`
- research/business Presentations source skills
- shared routing
- \`profiles/presentation-desktop.json\`
- canonical CUHK tree only as needed for Stage 1 adapter/provenance work
- new course-standard template tree
- directly relevant tests

Generated-only:
- \`plugins/codex/plugins/**\`
- \`.agents/plugins/marketplace.json\`
- current generator-owned mirrors

No hand patching generated output.

If direct evidence proves the existing generic shared-payload generator cannot package course-standard, only the smallest generic compatibility repair is allowed. No second/presentation-specific generator.

---

## 8. Course-standard reconstruction contract

Reconstruct template system, not course content.

Required stable identity:
- 4:3;
- black top band;
- blue frame-title band;
- white body;
- blue first-level bullet;
- lower-right page number;
- sans body;
- compatible math typography;
- normal Beamer content mechanisms.

Forbidden:
- course prose/examples/references copied as template content;
- reference PDF page used as background;
- colored PDF highlight annotations baked into template;
- Stage 2/3 teaching/story/composition logic.

---

## 9. G1 — installed normal entry

G1 PASS requires:
- exact committed candidate;
- fresh supported runtime;
- installed candidate Presentations plugin;
- natural user prompts;
- actual candidate consumption.

Helper/fixture/route receipt/direct script/config presence is insufficient.

Exercise distinct route families:
- research no-format;
- teaching no-format;
- business no-format;
- explicit editable;
- existing-deck revision route;
- local edit;
- external locked template;
- plan-only.

Beamer:
- real \`.tex\`;
- real PDF compile;
- real render.

Editable:
- real supported official Presentation/Slides surface;
- no \`python-pptx\`, reconstructed PDF or route receipt substitute.

If official editable surface unavailable:

\`BLOCKED_REAL_EDITABLE_ADAPTER_SURFACE\`

Fail closed.

---

## 10. G5 — canonical consumption + visual fidelity

For both built-in templates:

### A. Actual consumption
- canonical source identity/hash;
- candidate-bound build/compile evidence;
- proof exact canonical source was consumed.

### B. Visual fidelity
- real rendered PDF/PNG;
- independent qualitative inspection;
- comparison to frozen reference identity.

A and B cannot compensate for each other.

For course-standard:
- Reviewer directly sees exact private \`Chapter1.pdf\`;
- Reviewer directly sees candidate render.

For CUHK:
- Reviewer verifies canonical exact identity remains intact.

No claim of full teaching quality beyond template foundation.

---

## 11. Required broad regression

Run current canonical equivalents of:
- targeted Presentations tests;
- Marketplace generator write/validate/check/path-report;
- skills validation;
- full/risk-matched repo test suite;
- Reviewed Handoff validation;
- \`git diff --check\`;
- real GitHub CI;
- G1 product evidence;
- G5 consumption + render evidence.

Should-not-change:
- current CUHK research route;
- explicit editable route;
- business no-format editable route;
- external locked template;
- existing deck format/template;
- plan-only;
- local-edit fast path;
- production same-name plugin identity outside candidate.

Tests/CI do not replace G1/G5.

---

## 12. Mandatory CI state

This task must be initialized with:

\`ci_required = true\`

After implementation candidate and RESULT are ready, legal chronology must use:

\`\`\`text
EXECUTING
-> WAITING_FOR_CI
ci_status = PENDING
-> real GitHub checks
-> only after CI PASS, legal external implementation review transition
\`\`\`

Do not enable paid Text/Visual Review just because CI is required.

If task state says CI is not required, stop and return Planner; RESULT prose cannot override machine truth.

---

## 13. Non-substitutable semantics

Do not change:
- exactly two built-in templates;
- research no-format -> CUHK;
- teaching no-format -> course-standard;
- business no-format -> editable;
- explicit PPTX/Slides -> official editable adapter;
- existing/local edit preserves format/template;
- local edit remains lightweight;
- external locked template remains pass-through;
- direct Chapter1 read;
- G5 actual consumption separate from fidelity;
- no new top-level presentation skill/plugin;
- no implicit invocation hack;
- no Stage 2–6 implementation;
- Executor never owns initial task-local Plan freeze;
- first bootstrap uses \`--ci-required\`.

Any required change -> \`NEEDS_GPT_PLANNER\`.

---

## 14. Strict out of scope

Do not implement:
- Stage 2 semantic sequence;
- Stage 3 composition;
- Stage 4 citation/language;
- Stage 5 revision runtime;
- Stage 6 final generalization/release;
- universal IR/schema;
- third built-in template;
- new top-level presentation skill/plugin;
- implicit invocation workaround;
- geometry engine;
- #44–#48 promotion;
- Bridge changes;
- new workflow/state machine/ledger/database;
- paid review/API;
- production install/sync/release;
- version bump;
- PR/main merge/integration.

---

## 15. Required execution sequence

1. canonical preflight;
2. bootstrap exact task with \`--ci-required\`;
3. confirm \`PLAN_REQUESTED / RUN_GPT_PLANNER\`, \`ci_required=true\`;
4. publish only first-bootstrap task control metadata required by Planner;
5. stop Executor/product implementation;
6. external Planner writes task-local V2 Plan and freezes initial Plan;
7. only after \`PLAN_FROZEN / RUN_CODEX_EXECUTOR\`, start source implementation;
8. verify Chapter1 exact input;
9. source-first implementation;
10. canonical generation + deterministic/broad regression;
11. commit exact candidate;
12. G1;
13. G5;
14. write RESULT/candidate evidence;
15. enter \`WAITING_FOR_CI / ci_status=PENDING\`;
16. real GitHub CI;
17. external implementation Reviewer;
18. stop at current human/review boundary.

Stage 1 PASS does not authorize Stage 2 or main integration.

---

## 16. Durable private evidence

Future-required private input/render/comparison artifacts must have a durable copy under:

\`/home/yuukias/AI_Skills_Collection/private/exports/presentations--stage1-front-door-two-template-foundation/\`

Suggested:
- \`inputs/\`
- \`reference_renders/\`
- \`candidate_renders/\`
- \`g1/\`
- \`g5/\`
- \`review_bundle/\`

Record hashes/locators for key private artifacts.
Do not commit/push private plaintext/pages.

---

## 17. Failure/recovery

Primary fail-closed results:
- \`BLOCKED_REVIEWED_FIRST_BOOTSTRAP\`
- \`BLOCKED_PLANNER_FREEZE\`
- \`BLOCKED_CI_STATE\`
- \`BLOCKED_DISCOVERY_CONSUMER\`
- \`BLOCKED_REFERENCE_UNAVAILABLE\`
- \`BLOCKED_REAL_EDITABLE_ADAPTER_SURFACE\`
- \`BLOCKED_TEMPLATE_PROVENANCE\`
- \`BLOCKED_GENERATOR_ARCHITECTURE\`
- \`NEEDS_GPT_PLANNER\`

No raw Git fallback, alternate worktree, silent lower-quality adapter, new skill/plugin, Bridge change or scope expansion.

Current released \`presentations 0.3\` / latest released version remains rollback boundary.

---

## 18. Version / release / maturity

Stage 1 is an unreleased reviewed-branch candidate.

\`\`\`text
Repository bump decision: NONE
Affected plugins:
- presentations: NO_BUMP
\`\`\`

No maturity change.
No production install/release.
No final README release rewrite.

RESULT must say:

\`README checked: final reader-facing update deferred to approved Stage 6; Stage 1 remains an unreleased reviewed-branch candidate.\`

If partial Stage 1 would become production-visible before Stage 6 release closure, stop before integration and return Planner.

---

## 19. Authorization envelope

Only after the user sends the independent Critic-approved v1.1 Kickoff:

Allowed:
- exact first bootstrap with \`--ci-required\`;
- first-bootstrap control metadata publication needed for external Planner;
- Planner-owned task-local V2 Plan freeze;
- exact reviewed-worktree Stage 1 edits after \`PLAN_FROZEN\`;
- tests/render/candidate replay;
- exact Chapter1 private input read;
- task-owned durable private evidence writes;
- ordinary task-owned commits;
- ordinary non-force exact reviewed-branch publication required for Planner/CI/Reviewer.

Not allowed:
- alternate branch/worktree;
- destructive/force Git;
- PR/main merge;
- tag/release;
- production plugin install/sync;
- version bump;
- paid model/API;
- credential/provider changes;
- Bridge mutation.

---

## 20. Completion claim

Maximum claim after Stage 1 implementation review PASS:

> The exact Stage 1 candidate implements and validates the approved unified front door/routing and two-template adapter foundation under G1/G5 with required CI.

It does not prove:
- full Presentations V1.1 redesign;
- release readiness;
- maturity change;
- Stage 2–6;
- all TODOs solved;
- existing-deck runtime;
- full teaching quality;
- PDF/UA.

Until execution-ready Critic approves this v1.1 package and the user sends the approved Kickoff:

\`GOAL_ACHIEVED = NO\`
