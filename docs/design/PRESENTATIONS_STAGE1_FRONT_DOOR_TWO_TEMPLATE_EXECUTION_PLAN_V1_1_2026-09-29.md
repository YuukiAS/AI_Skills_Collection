# Presentations Stage 1 Execution Plan — Front Door + Routing + Two-Template Adapter Foundation

**Package version:** 1.1  
**Status:** READY FOR EXECUTION-READY CRITIC RE-REVIEW / NOT EXECUTION AUTHORIZATION  
**Date:** 2026-09-29  
**Repository:** \`YuukiAS/AI_Skills_Collection\`  
**Target plugin:** \`presentations\`  
**Stage:** 1 of approved V1.1 architecture  
**Task key:** \`presentations--stage1-front-door-two-template-foundation\`  
**Source branch/ref for planning:** \`main\`

## 0. Authority and revision scope

Approved architecture:

\`docs/design/PRESENTATIONS_TWO_TEMPLATE_PRODUCTION_REDESIGN_PLAN_V1_1_2026-09-28.md\`  
approved design commit: \`f71e97c06938ab2ce175ccf3b4ac19da9309fda1\`

Architecture Critic PASS:

\`results/presentations--two-template-production-redesign/CRITIC_REVIEW_V2.md\`  
@ \`ef2f1488b5e7479a4dd504f02ac2bd02b8825c07\`

Prior Stage 1 execution-ready Critic review:

\`results/presentations--stage1-front-door-two-template-foundation/CRITIC_EXECUTION_READY_REVIEW_V1.md\`  
@ \`c4fd2c64b3211529a61a33e5f80eb7afc2e2960a\`  
verdict: \`REVISE / READY_FOR_CODEX=NO\`

This v1.1 is a complete replacement execution package, not a patch note. It changes only the two stable execution-control blockers from the v1.0 review:

- \`PRES-S1-ER-F01\`: first bootstrap must stop at \`PLAN_REQUESTED / RUN_GPT_PLANNER\`, then a Planner-owned task-local \`AI_BRIDGE_REVIEWED_PLAN_V2\` must legally freeze to \`PLAN_FROZEN / RUN_CODEX_EXECUTOR\` before production implementation.
- \`PRES-S1-ER-F02\`: the exact first-bootstrap command must include \`--ci-required\`, and the task must follow the CI-required Reviewed Handoff chronology.

All Stage 1 product semantics, G1/G5, Chapter1 contract, source/generated boundary, recovery and NO_RELEASE boundary remain unchanged unless this file explicitly says otherwise.

---

## 1. Positive completion

Stage 1 adds one observable user capability:

> A normal presentation request can enter the installed Presentations plugin, select the correct mode/deliverable/template path without naming an internal child skill, preserve the editable business route and local-edit behavior, and reach a real adapter whose canonical template source is actually consumed.

Stage 1 positive completion requires one exact implementation candidate to prove:

1. natural presentation requests reach the installed candidate Presentations plugin;
2. route matrix is correct;
3. \`local-edit\` is lightweight and preserves format/template;
4. business/executive no-format and explicit PPTX/Slides remain editable routes;
5. \`cuhk-research\` consumes the canonical CUHK Beamer source;
6. \`course-standard\` consumes a canonical reconstructed source created from direct inspection of exact \`Chapter1.pdf\`;
7. G5 actual-source-consumption and visual-fidelity evidence both pass independently;
8. generated Marketplace/plugin outputs are rebuilt only through the existing generator;
9. real GitHub CI is required by task state and passes before GPT implementation review;
10. Stage 2–6 behavior remains unimplemented.

Tests alone are insufficient.

---

## 2. Exact Reviewed Handoff topology

Expected canonical checkout:

\`/home/yuukias/AI_Skills_Collection\`

Exact task:

\`presentations--stage1-front-door-two-template-foundation\`

Bridge-derived branch:

\`reviewed/presentations--stage1-front-door-two-template-foundation\`

Bridge-derived sibling worktree:

\`/home/yuukias/AI_Skills_Collection-presentations--stage1-front-door-two-template-foundation\`

Base:

the exact post-sync \`origin/main\` OID at user-authorized kickoff time.

No raw \`git worktree add\`, alternate clone, alternate branch/worktree or \`/tmp\` substitute is allowed.

---

## 3. Corrected first-bootstrap chronology — closes PRES-S1-ER-F01

### Phase 0 — canonical checkout preflight

Before task creation:

- enter the canonical checkout;
- read current repo \`AGENTS.md\`;
- fetch current \`origin/main\`;
- confirm exact repository identity \`YuukiAS/AI_Skills_Collection\`;
- confirm the task branch/worktree do not already exist in a conflicting state;
- resolve exact post-sync \`origin/main\` OID;
- read current Bridge Reviewed Handoff normal-entry rules.

No production source edit occurs in Phase 0.

### Phase 1 — first bootstrap only

From the canonical checkout, use the current repo-local Bridge command:

\`\`\`bash
ai-bridge reviewed-handoff task bootstrap \
  --task-key presentations--stage1-front-door-two-template-foundation \
  --expected-repo YuukiAS/AI_Skills_Collection \
  --expected-base-commit <POST_SYNC_ORIGIN_MAIN_OID> \
  --objective "Implement only approved Presentations Stage 1: unified front door/routing and two-template adapter foundation." \
  --ci-required
\`\`\`

The successful first bootstrap must create only the exact reviewed branch/worktree plus first task metadata and leave:

\`\`\`text
CURRENT.state = PLAN_REQUESTED
CURRENT.next_action = RUN_GPT_PLANNER
CURRENT.ci_required = true
\`\`\`

The initial \`plan_revision\` remains \`0\`.

At this point **Executor/product implementation must stop**.

Codex/Executor must not:
- write task-local \`PLAN.md\`;
- self-freeze the Plan;
- modify Presentations production source;
- begin template reconstruction;
- begin G1/G5 implementation.

### Phase 2 — first-bootstrap control metadata publication

Only the first-bootstrap task-owned control metadata required for the external Planner to read the new task may be committed/published, using the repository's current authorized bounded publication path.

This phase may include:
- \`automation/reviewed_handoff/tasks/<task_key>/REQUEST.md\`
- \`automation/reviewed_handoff/tasks/<task_key>/CURRENT.json\`

It must not include Presentations production implementation.

If the exact reviewed branch cannot be made readable to the Planner through the current authorized Reviewed Handoff/publication path, stop and return a control-plane blocker. Do not raw-push, create a different branch, or modify Bridge Kit.

### Phase 3 — Planner-owned initial freeze

The external GPT Planner owns this transaction.

Planner must read, in the exact reviewed worktree/branch:

- current task \`REQUEST.md\`;
- current task \`CURRENT.json\`;
- this Stage 1 v1.1 Plan;
- Stage 1 Canonical Goal v1.1;
- the durable execution-ready Critic review that approved v1.1;
- approved V1.1 Presentations architecture;
- current \`automation/reviewed_handoff/templates/PLAN.md\`;
- current Planner/Reviewed Handoff contracts.

Planner then writes:

\`automation/reviewed_handoff/tasks/presentations--stage1-front-door-two-template-foundation/PLAN.md\`

using current schema:

\`AI_BRIDGE_REVIEWED_PLAN_V2\`

The task-local Plan must preserve this execution package; it is a task-local Reviewed Handoff freeze, not a new architecture round.

Before transition, Planner must re-read/self-check the task-local Plan against the current PLAN template and required V2 sections, including:

- Frozen decisions;
- Positive completion;
- Non-substitutable semantics;
- Implementation scope;
- Acceptance and regression gates;
- Out of scope.

Planner then legally advances:

\`\`\`text
PLAN_REQUESTED -> PLAN_FROZEN
next_action = RUN_CODEX_EXECUTOR
plan_revision = 0
\`\`\`

The initial freeze does **not** consume the one allowed re-plan budget.

Publish the Planner transaction on the exact reviewed branch so the Executor/watch mechanism can consume it.

### Phase 4 — production implementation may begin

Only after the branch truth is:

\`\`\`text
PLAN_FROZEN
RUN_CODEX_EXECUTOR
\`\`\`

may Executor begin Stage 1 production implementation.

If an existing task later needs worktree recovery, use the current artifact-bound:

\`ai-bridge reviewed-handoff materialize-worktree --mode resume\`

Never second-bootstrap the same task.

---

## 4. Mandatory CI chronology — closes PRES-S1-ER-F02

Stage 1 changes shared routing, Marketplace/plugin interface, profile exposure, generated payload and template source; real GitHub CI is mandatory.

Therefore the task is created with \`--ci-required\`.

After implementation and local/product evidence are ready:

1. freeze the exact implementation candidate;
2. publish the exact reviewed branch as permitted;
3. write valid \`RESULT.md\` and candidate locator;
4. transition through the current CI-required path:

\`\`\`text
EXECUTING
-> WAITING_FOR_CI
CURRENT.ci_status = PENDING
\`\`\`

5. real GitHub checks run on the current authorized branch tip;
6. only after CI PASS may the external GPT implementation review proceed via the current legal transition;
7. CI FAIL follows the existing Reviewed Handoff REVISE/non-PASS path.

Do not set \`visual_review_required\` or \`text_review_required\` merely to satisfy this Stage 1 package. No paid Text/Visual review is authorized.

Narrative RESULT text cannot override \`CURRENT.ci_required\` or \`CURRENT.ci_status\`.

---

## 5. Required central-plugin capabilities

Stage 1 implementation must use the current relevant capabilities:

- \`workflow-core\` — Reviewed Handoff execution protocol;
- \`ai-skills-core\` / AI Skills Maintainer — central-plugin source/generated/replay/release discipline;
- \`presentations\` — presentation routing/template judgment.

They do not expand frozen scope.

---

## 6. Normal-entry routing contract

The product chain remains:

\`\`\`text
natural presentation request
-> installed Presentations plugin discovery/intake
-> mode + deliverable + template decision
-> shared core OR local-edit fast path
-> official Presentation/Slides OR Beamer adapter
-> artifact/render QA
\`\`\`

### Required routing matrix

| Natural task | Mode | Default result |
|---|---|---|
| group meeting / research update / seminar / paper talk / journal club, no format | new-deck | \`cuhk-research\` Beamer: \`.tex + PDF + render\` |
| QE / oral / defense, no venue template | new-deck | \`cuhk-research\` Beamer |
| Tutorial / lecture / teaching / formula walkthrough, no format | new-deck | \`course-standard\` Beamer |
| generic non-branded Beamer / LaTeX slides | new-deck | \`course-standard\` unless CUHK explicitly requested |
| business / executive / product / strategy / client, no format | new-deck | editable PPTX/Slides via official Presentation/Slides |
| explicit PPT / PowerPoint / PPTX / editable / Slides | new-deck or revision | official editable adapter |
| existing deck + feedback | existing-deck-revision | preserve current format/template; Stage 1 routes only |
| small existing-deck edit | local-edit | preserve current format/template; lightweight adapter path |
| explicit locked course/venue/client template | applicable | pass-through; never built-in registry |
| outline/storyline/notes only | plan-only | plan/notes only; no fake artifact completion |

The user never needs to name \`research-presentations\`, \`business-presentations\`, internal route IDs or scripts.

### Local-edit fast path

\`\`\`text
natural local presentation edit
-> Presentations intake
-> classify local-edit
-> preserve current format/template
-> direct appropriate adapter
-> affected-page/object QA
\`\`\`

No full semantic storyboard, no deck rebuild, no template conversion.

If the requested edit changes story/evidence/cross-slide first-use/accepted scope, Stage 1 may route it toward \`existing-deck-revision\`; Stage 5 owns the future actual revision runtime.

---

## 7. Source and consumer authority

### Marketplace/plugin interface

Canonical:
- \`scripts/codex_marketplace_config.json\`

Allowed Stage 1 edits:
- Presentations description/default prompts;
- existing packaging/interface metadata needed for approved intent discovery.

No new top-level plugin or presentation skill.

### Source skills/shared routing

Canonical:
- \`skills/tools/documents-media/presentations/research-presentations/SKILL.md\`
- \`skills/tools/documents-media/presentations/business-presentations/SKILL.md\`
- \`skills/tools/documents-media/presentations/shared/template-routing.md\`
- \`skills/tools/documents-media/presentations/shared/ppt-skill-routing.md\`

Research/business source skills remain compatibility triggers.
Shared routing owns mode/deliverable/template decisions.

Current “small edit does not trigger this skill” semantics must become “small edit still enters Presentations intake, then takes local-edit fast path.”

### Profile

\`profiles/presentation-desktop.json\`

The profile describes installed composition, not a second routing authority.

### Generated layer

Generated only:
- \`plugins/codex/plugins/**\`
- \`.agents/plugins/marketplace.json\`
- current generator-owned catalog/registry mirrors.

Regenerate only through the existing canonical generator.

A generator source change is allowed only if direct evidence proves the existing generic shared-payload contract cannot package \`course-standard\`; any fix must be the smallest generic compatibility repair, not a second/presentation-specific generator.

---

## 8. Two-template adapter foundation

### \`cuhk-research\`

Canonical authority remains:

\`skills/tools/documents-media/presentations/shared/templates/cuhk/beamer/source/\`

Stage 1 may clarify adapter identity, provenance and source-consumption tests/manifests.

Do not redesign the template or replace canonical source with design tokens/reference PPTX/helper output.

Provenance closure must distinguish:
- Beamer class license;
- inherited/derived theme source provenance;
- CUHK logo/assets source/redistribution boundary;
- canonical exact source vs derived convenience scaffolds.

Material provenance/license uncertainty -> \`BLOCKED_TEMPLATE_PROVENANCE\`.

### \`course-standard\`

Expected canonical source root:

\`skills/tools/documents-media/presentations/shared/templates/course-standard/beamer/source/\`

Template-level visual contract only:
- 4:3;
- black top band;
- blue frame-title band;
- white body;
- blue first-level bullet;
- lower-right page number;
- sans body;
- compatible math typography;
- normal Beamer title/frame/body/bullet/page-number behavior.

Do not implement teaching storyline/pedagogy/composition intelligence.

---

## 9. Exact private Chapter1 reference

Required exact input:

\`\`\`text
Chapter1.pdf
sha256 = ed205507a6d2de320b77d47d41e55bb0b406aef48144bc2c55d3bbba8c77ddf7
pages = 50
\`\`\`

Preferred durable execution-machine location:

\`/home/yuukias/AI_Skills_Collection/private/exports/presentations--stage1-front-door-two-template-foundation/inputs/Chapter1.pdf\`

Before substantive course-standard implementation:
- obtain the exact authorized file;
- verify SHA-256;
- directly inspect/render it;
- distinguish stable template elements from PDF highlight annotations and slide content;
- record inspected representative pages and hash in task evidence.

If unavailable/mismatched:
\`BLOCKED_REFERENCE_UNAVAILABLE\`

Do not reconstruct from Planner prose, screenshots, OCR summaries or memory.

Never commit/push private reference content.

Future-required private evidence must have durable canonical-checkout copies before task-worktree cleanup.

---

## 10. G1 — installed normal-entry routing

G1 proves discovery/intake/routing, not later semantic quality.

Evidence must use:
- exact committed Stage 1 candidate;
- fresh supported runtime;
- installed candidate Presentations plugin;
- natural user prompts;
- actual candidate consumption.

A candidate replay helper may stage/identify the candidate, but helper receipt is not product PASS.

Exercise each distinct route contract:
- research no-format;
- teaching no-format;
- business no-format;
- explicit editable;
- existing-deck revision route;
- local-edit;
- external locked template;
- plan-only.

For Beamer routes:
- real source generation;
- real PDF compile;
- real rendered-page inspection.

For editable routes:
- use a real supported official Presentation/Slides surface;
- do not substitute \`python-pptx\`, reconstructed PDF or route receipt.

Unavailable official editable surface:
\`BLOCKED_REAL_EDITABLE_ADAPTER_SURFACE\`

No silent downgrade.

---

## 11. G5 — actual template consumption + visual fidelity

For **each** built-in template, both independent evidence streams are mandatory.

### A. Actual consumption
- canonical source identity/hash;
- candidate-bound compile/build manifest;
- evidence showing that exact source was actually consumed.

### B. Visual fidelity
- real PDF/PNG render;
- independent qualitative inspection;
- comparison against frozen template identity/reference.

A PASS / B FAIL = G5 FAIL.
A FAIL / B PASS = G5 FAIL.

For \`course-standard\`, Reviewer must directly access:
- exact private \`Chapter1.pdf\`;
- candidate renders.

For \`cuhk-research\`, Reviewer verifies canonical CUHK identity remains intact.

Teaching quality beyond template-level legibility is later G3/G8, not Stage 1.

---

## 12. Broad regression

Because Stage 1 touches shared routing, Marketplace interface, profile and generated payload, it is not narrow-test eligible.

Run current canonical equivalents of:

- targeted presentations routing/template tests;
- Marketplace generation/write/validate/check/path-report;
- skill validation;
- full/risk-matched repository tests;
- Reviewed Handoff validation;
- \`git diff --check\`;
- real GitHub CI;
- G1 installed-candidate product evidence;
- G5 source-consumption/render evidence.

Should-not-change:
- current CUHK research route;
- explicit editable route;
- business no-format editable route;
- external locked template;
- existing-deck format/template preservation;
- plan-only;
- local-edit fast path;
- same-name production plugin identity outside candidate.

CI/tests do not replace G1/G5.

---

## 13. Allowed source scope

Primary allowed:
- \`scripts/codex_marketplace_config.json\`
- research/business Presentations source skills
- shared routing
- \`profiles/presentation-desktop.json\`
- CUHK template tree only for adapter/provenance foundation
- new course-standard template tree
- directly relevant presentation/Marketplace tests
- task-local results/evidence
- durable private task inputs/evidence

Conditional:
- existing generic Marketplace generator source only if a directly demonstrated generic shared-payload packaging defect blocks the new template.

Not allowed:
- universal IR/schema;
- Stage 2–6 implementation;
- Bridge changes.

---

## 14. Non-substitutable semantics

Implementation is no longer the same task if any of these change:

1. built-in template count != 2;
2. research no-format no longer -> CUHK;
3. teaching no-format no longer -> course-standard;
4. business no-format no longer -> editable;
5. explicit PPTX/Slides no longer -> official editable adapter;
6. existing/local edit changes format/template by default;
7. local edit becomes full planning;
8. external locked template becomes built-in;
9. Chapter1 direct-read requirement is removed;
10. G5 actual consumption and visual fidelity become one compensating score;
11. discovery failure is bypassed via new top-level skill/plugin/implicit invocation/control plane;
12. Stage 2–6 is implemented;
13. Executor writes/freezes its own task-local Plan;
14. CI-required task is initialized without \`--ci-required\`.

Any such need -> Planner/Critic re-entry.

---

## 15. Out of scope

Strictly out:
- semantic sequence / first-use / transition system;
- composition core;
- citation/bibliography/text-layer implementation;
- writing-style production changes;
- existing-deck runtime;
- Stage 6 fresh generalization/release;
- third template;
- new top-level presentation skill/plugin;
- implicit invocation workaround;
- geometry engine;
- #44–#48 promotion;
- Bridge Kit mutation;
- workflow/state-machine/ledger/database creation;
- paid review/API;
- production plugin install/sync/release;
- version bump;
- main integration.

---

## 16. Stop conditions and recovery

Stop and return Planner/Critic if:
- exact first bootstrap cannot create the expected task topology;
- task does not start \`PLAN_REQUESTED / RUN_GPT_PLANNER\`;
- \`ci_required\` is not true after bootstrap;
- task-local V2 Plan cannot be legally written/frozen by Planner;
- existing discovery surfaces cannot implement unified intake without forbidden new control surface;
- exact Chapter1 missing/hash mismatch;
- official editable surface unavailable for required G1 evidence;
- template provenance materially unresolved;
- generator needs architecture rather than narrow compatibility repair;
- Stage 1 needs later-stage capability;
- #44–#48 candidate-only mechanism becomes necessary;
- Bridge modification becomes necessary.

Recovery:
- preserve last released \`presentations 0.3\` / current released version as rollback;
- no raw Git fallback;
- existing-task worktree recovery only through artifact-bound resume;
- preserve truthful task evidence;
- return exact blocker.

---

## 17. Git / authorization boundary

Only after user sends a Critic-approved v1.1 Kickoff:

Allowed:
- exact repo-local first bootstrap with \`--ci-required\`;
- publication of first-bootstrap control metadata required for Planner;
- Planner-owned task-local V2 Plan transaction;
- exact reviewed-worktree Stage 1 edits after \`PLAN_FROZEN\`;
- tests, rendering, candidate replay;
- exact Chapter1 private reference read;
- durable task-private evidence writes;
- task-owned commits;
- ordinary non-force publication of exact reviewed branch for Planner/CI/Reviewer as required.

Not authorized:
- alternate branch/worktree;
- force/destructive Git;
- PR/main merge;
- tag/release;
- production install/sync;
- version bump;
- paid model/API;
- credential/provider change;
- Bridge mutation.

---

## 18. Version / README / maturity

This package revision itself is docs-only:

\`\`\`text
Repository bump decision: NONE
Affected plugins:
- presentations: NO_BUMP
- workflow-core: NO_BUMP
- ai-skills-core: NO_BUMP
- writing-style: NO_BUMP
\`\`\`

Stage 1 implementation is an unreleased intermediate candidate:
- no release;
- no version bump;
- no maturity change;
- no final README release rewrite.

RESULT must state:

\`README checked: final reader-facing release update deferred to approved Stage 6; Stage 1 remains an unreleased reviewed-branch candidate.\`

If Stage 1 would become production-visible before Stage 6 release closure, stop before integration and return Planner.

---

## 19. Maintenance Board

Issues \`#29–#48\` retain canonical source maturity.
Project lifecycle remains \`DOING\`.

After v1.1 manifest commit:

\`\`\`text
Current execution anchor:
results/presentations--stage1-front-door-two-template-foundation/EXECUTION_PACKAGE_V1_1.md
@ <v1.1 manifest commit>

Next action:
independent execution-ready Critic re-review focused first on
PRES-S1-ER-F01 and PRES-S1-ER-F02
\`\`\`

No PROMOTED/DONE/issue close.

If current surface cannot perform reader-facing Project mutation with required Clear Writing, output exact pending mutation and do not claim sync.

---

## 20. Execution-ready Critic decision requested

Critic must review the same v1.1:
1. Plan;
2. Canonical Goal;
3. Kickoff Draft;
4. manifest binding them.

Priority:
- \`PRES-S1-ER-F01 = CLOSED ?\`
- \`PRES-S1-ER-F02 = CLOSED ?\`

Then check only for direct regressions introduced by these two corrections.

Only execution-ready PASS may return the exact reviewed v1.1 Kickoff verbatim with \`READY_FOR_CODEX=YES\`.
