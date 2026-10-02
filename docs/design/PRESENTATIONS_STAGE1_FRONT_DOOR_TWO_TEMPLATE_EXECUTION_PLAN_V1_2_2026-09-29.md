# Presentations Stage 1 Execution Plan — Front Door + Routing + Two-Template Adapter Foundation

**Package version:** 1.2  
**Status:** READY FOR EXECUTION-READY CRITIC REVIEW / NOT EXECUTION AUTHORIZATION  
**Date:** 2026-09-29  
**Repository:** \`YuukiAS/AI_Skills_Collection\`  
**Target plugin:** \`presentations\`  
**Task key:** \`presentations--stage1-front-door-two-template-foundation\`  
**Source ref:** current \`main\`

## 0. Amendment scope

This is a **bounded Stage 1 amendment**, not a new Presentations architecture round.

Architecture authority remains:

\`docs/design/PRESENTATIONS_TWO_TEMPLATE_PRODUCTION_REDESIGN_PLAN_V1_1_2026-09-28.md @ f71e97c06938ab2ce175ccf3b4ac19da9309fda1\`

The prior Stage 1 execution package v1.1 remains historical evidence:

\`results/presentations--stage1-front-door-two-template-foundation/EXECUTION_PACKAGE_V1_1.md @ 049847f4638bb339229c748d3b8f97bd41fae72d\`

Its narrow Bridge F03 review later passed after Bridge 0.9.3 release:

\`results/presentations--stage1-front-door-two-template-foundation/CRITIC_EXECUTION_READY_REVIEW_V3_F03.md\`

This v1.2 reopens execution-readiness **only because new real teaching-deck evidence changes the Stage 1 \`course-standard\` adapter contract**. It does not reopen the product architecture, routing topology, G1 definition, Chapter1 private-reference boundary, two-template decision, release boundary, or Stages 2–6.

Two bounded amendments only:

1. promote TODO #49 into Stage 1: course-standard needs structural/navigation identity and ratio-aware behavior, not only colours/bands;
2. replace stale Bridge blocker/wait language with the actual released Bridge Kit 0.9.3 normal entry.

No Presentations production code is authorized by this document.

---

## 1. New real-use evidence and Planner triage

Canonical evidence is now recorded in:

\`docs/plugin-todos/presentations.md\`

at repository commit:

\`462fe77cdb178fb521975f2b451b274126158c3c\`

The first real \`course-standard\` teaching-deck use, STAT5060 Tutorial 1, produced a 27-page Beamer candidate that was manually annotated page-by-page. The generic lesson is narrow:

> A usable teaching Beamer template needs stable structural/navigation identity and ratio-aware behavior in addition to colours, fonts and bands.

Do not copy course-local examples, page numbers, homework content, wording, or annotated PDF pages into the plugin.

### #49 disposition

\`#49 Course-standard teaching template needs structural navigation, not only colours and bands\`

Planner decision:

\`PROMOTE_NOW -> Stage 1 two-template adapter foundation\`

Canonical TODO status is updated to \`PROMOTE_NOW\`. Implementation remains pending execution-ready Critic PASS.

This promotion is justified because:
- the issue is directly about the built-in template adapter foundation already owned by Stage 1;
- it was reproduced by a real course-standard deck rather than a synthetic benchmark;
- the minimum fix is structural template capability, not Stage 2 semantic/storyline or Stage 3 composition intelligence.

### #50–#53 disposition

Remain deferred and retain current canonical maturity:

- #50 presenter-learning companion — \`NEW\`, deferred;
- #51 teaching lecture/source cross-reference — \`NEW\`, deferred;
- #52 assessment-introduction guardrails — \`NEW\`, deferred;
- #53 closing-frame semantic contract — \`NEW\`, deferred except for the template-level existence of a closing-frame primitive.

No Stage 1 mechanism is added for #50–#53.

### Other related TODOs remain outside this amendment

Do not pull into Stage 1:
- #35 full-deck responsive/reader-effort intelligence;
- #38 deck-wide typography/math hierarchy beyond existing template-level baseline;
- #40 table/list/paragraph semantic primitive selection;
- #47 simulation/metric structured-fact presentation;
- #48 natural scientific slide language.

Their current maturity remains unchanged.

---

## 2. Product scope remains Stage 1 only

Stage 1 still adds only:

\`\`\`text
unified Presentations front door
+ routing/deliverable selection
+ local-edit fast path
+ two built-in template adapter foundation
+ generated-layer consistency
+ G1
+ G5 foundation
\`\`\`

Still excluded:

- Stage 2 semantic sequence / page-job / first-use / transitions;
- Stage 3 composition intelligence;
- Stage 4 citation/language implementation;
- Stage 5 existing-deck revision runtime;
- Stage 6 final generalization/release closure;
- universal IR/schema;
- third built-in template;
- new top-level presentation skill/plugin;
- geometry engine;
- #50–#53 teaching intelligence;
- #44–#48 candidate promotion except #49 as explicitly promoted here;
- Bridge Kit modification;
- new workflow/state machine;
- paid review;
- plugin release/version bump;
- main integration.

---

## 3. Routing remains unchanged except ratio is an adapter parameter

Canonical routing still begins:

\`\`\`text
natural presentation request
-> installed Presentations plugin discovery/intake
-> mode + deliverable + template decision
-> ratio/template parameters
-> shared core OR local-edit fast path
-> official Presentation/Slides OR Beamer adapter
-> artifact/render QA
\`\`\`

Ratio does not create a third template and does not decide research-vs-teaching.

### Default routing matrix

| Natural request | Default result |
|---|---|
| research/group meeting/seminar/paper talk/journal club/QE/oral/defense, no format | \`cuhk-research\` Beamer |
| Tutorial/lecture/teaching/formula walkthrough, no format and no ratio | \`course-standard\` Beamer, default 4:3 |
| teaching request explicitly 16:9 | \`course-standard\` Beamer 16:9 variant |
| generic non-branded Beamer/LaTeX, no stronger context | \`course-standard\`; default 4:3 unless ratio explicitly overridden |
| business/executive/product/strategy/client, no format | editable PPTX/Slides |
| explicit PPTX/Slides/editable | official editable adapter |
| existing deck/local edit | preserve existing format, template and aspect ratio |
| explicit locked course/venue/client template | pass-through locked template, including its ratio |
| plan-only | plan/notes only; no artifact claim |

### Aspect-ratio precedence

For \`course-standard\`:

1. external locked template or existing-deck ratio wins when applicable;
2. explicit user aspect ratio wins next;
3. otherwise default new \`course-standard\` = 4:3 because Chapter1 is the reference/default ratio.

Explicit \`16:9\` means the same built-in \`course-standard\` identity rendered through a supported 16:9 variant/override. It must not route to \`cuhk-research\` merely because that template is 16:9, and it must not create \`course-standard-wide\` as a third built-in template.

---

## 4. Two built-in templates remain exactly two

### 4.1 \`cuhk-research\`

Canonical source remains:

\`skills/tools/documents-media/presentations/shared/templates/cuhk/beamer/source/\`

No change to:
- research identity;
- CUHK branding;
- exact-source authority;
- derived scaffold boundary;
- existing 16:9 behavior.

### 4.2 \`course-standard\` — amended Stage 1 contract

Reference:

exact private \`Chapter1.pdf\`; it remains reference-only and is not committed to ordinary plugin payload.

The Stage 1 adapter must now establish **both visual identity and structural identity**.

#### A. Visual identity

Preserve the reference family:

- black top band;
- blue frame-title band;
- white body;
- restrained academic Beamer appearance;
- ordinary blue bullets;
- sparse teaching hierarchy;
- lower-right page number;
- sans body with compatible math typography;
- no PDF annotation/highlight replication;
- no CUHK research branding.

#### B. Structural identity

The template foundation must provide:

1. a canonical sparse title/opening frame;
2. section-aware navigation/state;
3. PDF outline/bookmarks derived from normal section structure;
4. top navigation controls only where they remain consistent with the course-standard identity and are not visually intrusive;
5. bottom navigation/action affordances using normal Beamer mechanisms where appropriate;
6. stable footline and page-number behavior;
7. a clear template distinction among:
   - title/opening frame;
   - ordinary content frame;
   - section-aware content state;
   - closing frame;
8. a canonical closing-frame primitive/slot at template level.

Stage 1 **does not decide the semantic job of the closing frame**.

The primitive may support content such as:
- recap;
- integrative question;
- Q&A;
- thanks.

Selection among them belongs to later semantic/storyline logic (#53), not Stage 1.

#### C. Ratio-aware identity

The template must support:
- 4:3 reference/default variant;
- explicit 16:9 variant/override.

Across supported ratios, the recognizable identity must remain the same:
- black/blue header language;
- title/frame/body role separation;
- section-state/navigation grammar;
- footline/page numbering;
- opening/closing structural primitives;
- typography family and restrained teaching character.

Ratio adaptation may change:
- horizontal spacing;
- content-area width;
- navigation density/placement;
- line wrapping;
- safe-area measurements.

It may not silently become another theme.

### No new runtime schema

This ratio/navigation support must be implemented through ordinary template/adapter parameters and Beamer mechanisms. Do not create a universal presentation IR/schema/state machine for it.

---

## 5. External implementation reality supports this amendment

Current Beamer remains the approved TeX route.

Official Beamer 3.78 supports:
- theme/template-controlled appearance;
- explicit class \`aspectratio\` values, including wide ratios;
- navigation infrastructure;
- normal section structure.

Hyperref/Beamer PDF generation supports document outline/bookmark generation from section structure.

Therefore Stage 1 does not need a new renderer, third-party theme framework, or third built-in template to implement #49.

---

## 6. Bridge Kit 0.9.3 — stale blocker is closed

### Verified released capability

Current Bridge formal distribution:

\`\`\`text
BRIDGE_KIT_VERSION = 0.9.3
formal release target =
9dad0ba4bfa54e251f345091c5151ae991251ec9
formal distribution complete = YES
\`\`\`

Current production interface includes:

\`\`\`bash
ai-bridge reviewed-handoff task bootstrap \
  --task-key <task_key> \
  --expected-repo <owner/repo> \
  --expected-base-commit <post-sync-origin-main-oid> \
  --objective "<bounded objective>" \
  --ci-required
\`\`\`

and, after the exact first REQUEST/CURRENT commit:

\`\`\`bash
ai-bridge reviewed-handoff task publish-first \
  --task-key <task_key> \
  --expected-repo <owner/repo>
\`\`\`

Bridge 0.9.3 Machine Policy contains a bounded allow for \`task publish-first\`. The helper is restricted to the exact first Reviewed metadata publication and is not a generic branch creator.

The previous generic capability blocker:

\`PRES-S1-ER-F03\`

is therefore:

\`CLOSED / SUPERSEDED BY BRIDGE 0.9.3\`

This matches the already recorded narrow Critic closure in:

\`results/presentations--stage1-front-door-two-template-foundation/CRITIC_EXECUTION_READY_REVIEW_V3_F03.md\`

### Important execution-machine preflight

Formal release closure does not prove every machine is already updated.

Before Stage 1 bootstrap, Executor must verify on the actual execution machine:

- imported \`ai_bridge_kit.__version__ == 0.9.3\` or a later compatible version;
- \`ai-bridge reviewed-handoff task publish-first --help\` is available;
- host/Reviewed Handoff validation passes for the active environment.

If the machine is stale, report:

\`BLOCKED_BRIDGE_RUNTIME_STALE\`

This is an environment/update prerequisite, **not** resurrection of historical F03 and not a reason to modify Presentations.

---

## 7. Exact Reviewed Handoff execution chronology under Bridge 0.9.3

Expected canonical checkout:

\`/home/yuukias/AI_Skills_Collection\`

Task key:

\`presentations--stage1-front-door-two-template-foundation\`

Derived branch:

\`reviewed/presentations--stage1-front-door-two-template-foundation\`

Derived sibling worktree:

\`/home/yuukias/AI_Skills_Collection-presentations--stage1-front-door-two-template-foundation\`

### Phase 0 — preflight

From canonical checkout:
- read current repo/Goal/approved package;
- verify Bridge runtime compatibility as above;
- fetch/sync current \`origin/main\`;
- record exact post-sync \`origin/main\` OID;
- ensure no conflicting task branch/worktree.

### Phase 1 — local first bootstrap

Run exact current Bridge command with \`--ci-required\`.

Successful bootstrap must leave:

\`\`\`text
PLAN_REQUESTED
RUN_GPT_PLANNER
ci_required = true
plan_revision = 0
\`\`\`

No Presentations production edits yet.

### Phase 2 — exact first metadata commit and first publication

In the derived Reviewed worktree:
- commit **only** the first-bootstrap task-owned \`REQUEST.md\` / \`CURRENT.json\` metadata allowed by Bridge 0.9.3;
- do not include PLAN, production source, template source or unrelated task content;
- invoke:

\`\`\`bash
ai-bridge reviewed-handoff task publish-first \
  --task-key presentations--stage1-front-door-two-template-foundation \
  --expected-repo YuukiAS/AI_Skills_Collection
\`\`\`

Bridge must establish the same-name remote reviewed branch and upstream through its bounded first-publication contract.

Raw \`git push -u\` is not a fallback.

### Phase 3 — Planner-owned initial freeze

External GPT Planner reads remote \`REQUEST/CURRENT\`, the approved v1.2 package and current PLAN template.

Planner writes task-local \`AI_BRIDGE_REVIEWED_PLAN_V2\`, validates it and transitions:

\`\`\`text
PLAN_REQUESTED -> PLAN_FROZEN
next_action = RUN_CODEX_EXECUTOR
plan_revision = 0
\`\`\`

Publish that Planner transaction using the now-valid existing-branch bounded publication route.

Executor must never self-freeze the Plan.

### Phase 4 — Stage 1 implementation

Only after \`PLAN_FROZEN / RUN_CODEX_EXECUTOR\`:
- implement front door/routing;
- implement the two template adapter foundation including amended course-standard #49 contract;
- regenerate generated layers through canonical generator;
- run local/product gates.

### Phase 5 — CI-required handoff

After exact implementation candidate and RESULT are ready:

\`\`\`text
EXECUTING
-> WAITING_FOR_CI
ci_status = PENDING
-> real GitHub CI
-> CI PASS
-> legal external implementation review
\`\`\`

No RESULT prose may override CURRENT CI truth.

---

## 8. Private Chapter1 reference remains mandatory

Exact private input:

\`\`\`text
Chapter1.pdf
sha256 =
ed205507a6d2de320b77d47d41e55bb0b406aef48144bc2c55d3bbba8c77ddf7
pages = 50
\`\`\`

Preferred durable execution-machine locator:

\`/home/yuukias/AI_Skills_Collection/private/exports/presentations--stage1-front-door-two-template-foundation/inputs/Chapter1.pdf\`

Before substantive course-standard implementation:
- directly read the exact reference;
- verify hash;
- inspect/render it;
- distinguish template-level visual/structural cues from content and PDF highlight annotations.

Do not reconstruct from memory, Planner prose, screenshots or OCR summaries.
Do not commit/push private pages/content.

The newly annotated STAT5060 PDF is **not** an additional plugin input and must not be copied to this repo. Its generic lesson is already captured by TODO #49.

---

## 9. G1 remains unchanged

G1 still proves installed normal-entry routing and deliverable preservation.

It requires:
- exact committed candidate;
- fresh supported runtime;
- installed candidate Presentations plugin;
- natural prompts;
- actual candidate consumption.

Route families remain:
- research no-format;
- teaching no-format;
- business no-format;
- explicit editable;
- existing-deck revision route;
- local edit;
- external locked template;
- plan-only.

Additional ratio routing checks:
- teaching with no ratio -> course-standard 4:3;
- teaching explicit 16:9 -> course-standard 16:9;
- existing deck explicit/current ratio preserved;
- external locked template ratio preserved.

Beamer routes require real source -> PDF -> render.
Editable routes still require the real supported official editable surface.

---

## 10. G5 amended for structural and ratio fidelity

G5 remains two non-compensating evidence streams.

### A. Actual source consumption

For each built-in template:
- canonical source identity/hash;
- candidate-bound compile/build manifest;
- proof the exact approved template source was consumed.

### B. Visual/structural fidelity

#### course-standard default 4:3

Compare candidate render directly to the private Chapter1 reference for:
- reference/default 4:3 geometry;
- black top band;
- blue frame-title band;
- white body;
- ordinary blue bullets;
- typography character;
- page number position;
- restrained sparse teaching identity;
- no highlight/annotation replication.

Additionally verify the amended structural contract:
- canonical opening frame exists;
- section state/navigation is visible/usable without becoming intrusive;
- PDF outline/bookmarks exist and follow section structure;
- footline/page numbering are stable;
- ordinary vs section-aware vs closing frame states remain distinguishable;
- canonical closing-frame primitive exists.

#### course-standard explicit 16:9

A 16:9 user override is **not** expected to pixel-match the 4:3 reference dimensions.

G5 must separately compare:
1. ratio correctness: actual 16:9 output, no clipping/broken navigation/safe-area regression;
2. invariant template identity: visual language + structural navigation/footline/opening/closing roles remain recognizably course-standard.

Expected ratio-driven spacing/reflow differences are not fidelity failures.

#### cuhk-research

Existing G5 requirements remain unchanged.

A failure in actual source consumption cannot be offset by good visuals, and a fidelity failure cannot be offset by correct source consumption.

---

## 11. Current CI and visual-review requirements

### CI

\`CURRENT.ci_required = true\`

The first bootstrap must include:

\`--ci-required\`

Real GitHub CI remains mandatory.

### Bridge Visual Review flag

\`CURRENT.visual_review_required = false\` for this Stage 1 package.

Do **not** add \`--visual-review-required\` or \`--text-review-required\` merely because G5 is visual.

Reason:
- this task does not authorize paid OpenAI/Terra review;
- Stage 1 G5 still requires real pixel-level qualitative review;
- that visual acceptance is performed by the independent implementation Reviewer/human review surface with direct access to candidate renders and the private Chapter1 reference.

Therefore distinguish:

\`\`\`text
AI Bridge paid/automated visual-review flag = NOT REQUIRED / NOT AUTHORIZED
G5 independent visual fidelity review = REQUIRED
\`\`\`

If the actual Reviewer cannot access the required renders/reference, fail closed with an evidence-access blocker; do not replace visual inspection with OCR/text summaries.

---

## 12. Source/generated authority remains unchanged

Primary source:
- \`scripts/codex_marketplace_config.json\`;
- Presentations research/business source skills;
- shared routing;
- \`profiles/presentation-desktop.json\`;
- canonical CUHK source;
- new course-standard source;
- directly relevant tests.

Generated:
- \`plugins/codex/plugins/**\`;
- \`.agents/plugins/marketplace.json\`;
- existing generator-owned mirrors.

Generated outputs are rebuilt only through current generator.

No new top-level skill/plugin/schema/state machine.

---

## 13. Non-substitutable semantics

The implementation ceases to be this approved Stage 1 if it changes:

1. exactly two built-in templates;
2. research no-format -> CUHK;
3. teaching no-format -> course-standard;
4. business no-format -> editable;
5. explicit PPTX/Slides -> official editable adapter;
6. existing/local edit preserves current format/template/ratio;
7. local edit remains lightweight;
8. external locked template remains pass-through;
9. Chapter1 direct-read/private-reference requirement;
10. #49 remains template-level structural/ratio support rather than teaching intelligence;
11. #50–#53 remain deferred;
12. 16:9 becomes a third template rather than an adapter variant;
13. G5 consumption/fidelity becomes a compensating score;
14. Stage 2–6 capability enters Stage 1;
15. raw Git/manual first-publication fallback replaces Bridge 0.9.3 normal entry;
16. CI-required task is initialized without \`--ci-required\`.

Any required change returns Planner/Critic.

---

## 14. Validation / regression

Before implementation review, run current canonical equivalents of:
- targeted Presentations routing/template tests;
- course-standard 4:3 and 16:9 compile/render probes;
- structural navigation/bookmark/footline/opening/closing checks;
- Marketplace generation/write/validate/check/path-report;
- skills validation;
- broad/risk-matched repository tests;
- Reviewed Handoff validation;
- \`git diff --check\`;
- real GitHub CI;
- G1 installed-candidate evidence;
- G5 source-consumption + render evidence.

Should-not-change:
- CUHK research route;
- editable business route;
- explicit PPTX route;
- external locked template;
- existing/local edit format/template/ratio preservation;
- plan-only;
- current generated source authority;
- production same-name plugin identity outside candidate;
- no teaching-specific #50–#53 behavior.

Mechanical PASS does not replace G1/G5.

---

## 15. Stop conditions and recovery

Fail closed on:
- \`BLOCKED_BRIDGE_RUNTIME_STALE\`: execution machine lacks compatible Bridge 0.9.3+ runtime / \`publish-first\`;
- \`BLOCKED_REVIEWED_FIRST_BOOTSTRAP\`;
- \`BLOCKED_FIRST_PUBLICATION\`;
- \`BLOCKED_PLANNER_FREEZE\`;
- \`BLOCKED_CI_STATE\`;
- \`BLOCKED_DISCOVERY_CONSUMER\`;
- \`BLOCKED_REFERENCE_UNAVAILABLE\`;
- \`BLOCKED_REAL_EDITABLE_ADAPTER_SURFACE\`;
- \`BLOCKED_TEMPLATE_PROVENANCE\`;
- \`BLOCKED_GENERATOR_ARCHITECTURE\`;
- \`NEEDS_GPT_PLANNER\`.

Do not revive historical F03 wording if the only problem is a stale local Bridge install; report the actual runtime mismatch.

No raw Git fallback, no alternate worktree, no consumer-local wrapper, no silent lower-quality adapter.

Current released \`presentations 0.3\` / then-current released version remains rollback boundary.

---

## 16. Version / release / integration

This amendment is planning-only.

\`\`\`text
Repository bump decision: NONE
Affected plugins:
- presentations: NO_BUMP
- workflow-core: NO_BUMP
- ai-skills-core: NO_BUMP
- writing-style: NO_BUMP
\`\`\`

Stage 1 implementation remains an unreleased reviewed-branch candidate:
- no plugin version bump;
- no maturity change;
- no production install/release;
- no main integration;
- no final README release rewrite.

If Stage 1 would become production-visible before the later approved release closure, stop before integration.

---

## 17. Maintenance Board / tracking truth

Canonical tracking now includes #49–#53 in addition to earlier Presentations issues.

Current source disposition:
- #49 = \`PROMOTE_NOW\` for this Stage 1 amendment;
- #50–#53 remain \`NEW\`;
- #44–#48 retain their current states.

Project lifecycle should remain:

\`Area = presentations\`
\`Status = DOING\`

No issue is DONE/closed by this planning amendment.

If the current surface cannot perform reader-facing Issue/Project mutation with the required Clear Writing invocation, do not claim synchronization. Record the exact pending mutation for the next Project-capable maintainer.

---

## 18. Execution-ready review target

The next independent Critic must review the complete same-version package:
- Stage 1 Plan v1.2;
- Canonical Goal v1.2;
- Kickoff Draft v1.2;
- execution-package manifest v1.2;
- Planner validation v1.2.

Review focus:
1. #49 is genuinely template-foundation scope, not Stage 2/3 leakage;
2. #50–#53 remain deferred;
3. ratio policy is coherent and does not create a third template;
4. G5 correctly separates 4:3 exact-reference fidelity from 16:9 invariant-identity fidelity;
5. Bridge 0.9.3 chronology uses current \`publish-first\`, with no obsolete F03 workaround;
6. CI remains required;
7. automated/payed Bridge Visual Review remains not required, while independent G5 pixel review remains required;
8. no release/version/main-integration authority is introduced.

Only that Critic may set \`READY_FOR_CODEX=YES\`.
