# Canonical Goal — Presentations Stage 1 Front Door + Two-Template Foundation

**Goal version:** 1.0  
**Status:** DRAFT FOR EXECUTION-READY CRITIC REVIEW / NOT YET USER EXECUTION AUTHORIZATION  
**Task key:** \`presentations--stage1-front-door-two-template-foundation\`  
**Repository:** \`YuukiAS/AI_Skills_Collection\`  
**Approved architecture:** \`docs/design/PRESENTATIONS_TWO_TEMPLATE_PRODUCTION_REDESIGN_PLAN_V1_1_2026-09-28.md @ f71e97c06938ab2ce175ccf3b4ac19da9309fda1\`  
**Stage 1 Plan:** \`docs/design/PRESENTATIONS_STAGE1_FRONT_DOOR_TWO_TEMPLATE_EXECUTION_PLAN_V1_0_2026-09-29.md\`

## 1. Goal

Implement **only Stage 1** of the Critic-approved Presentations V1.1 architecture:

> make Presentations a real unified intake/routing front door while preserving existing editable business/PPTX behavior, establish \`local-edit\` as a lightweight pass-through mode, preserve exact CUHK template identity, and add a canonical \`course-standard\` Beamer adapter reconstructed from the exact user-provided course reference.

Do not implement Stages 2–6.

The user should no longer need to know which child presentation skill or route to invoke for an ordinary presentation task. The implementation must nevertheless remain lightweight for local edits and must not force business/editable decks into Beamer.

---

## 2. Exact execution topology

Expected canonical checkout:

\`/home/yuukias/AI_Skills_Collection\`

Task:

\`presentations--stage1-front-door-two-template-foundation\`

Derived Reviewed branch:

\`reviewed/presentations--stage1-front-door-two-template-foundation\`

Derived sibling worktree:

\`/home/yuukias/AI_Skills_Collection-presentations--stage1-front-door-two-template-foundation\`

Base:

post-sync \`origin/main\` OID containing the execution-ready Critic-approved package.

Bootstrap must use the installed current Bridge normal entry from the canonical repo cwd:

\`\`\`bash
ai-bridge reviewed-handoff task bootstrap \
  --task-key presentations--stage1-front-door-two-template-foundation \
  --expected-repo YuukiAS/AI_Skills_Collection \
  --expected-base-commit <POST_SYNC_ORIGIN_MAIN_OID> \
  --objective "Implement only approved Presentations Stage 1: unified front door/routing and two-template adapter foundation."
\`\`\`

No raw Git worktree creation and no alternate branch/worktree are allowed.

If the expected canonical checkout is not the active legitimate repo or the Bridge command cannot derive the exact branch/worktree above, stop before substantive implementation.

---

## 3. Required plugin/maintenance capabilities

This central-plugin refinement must follow current AI_Skills contracts and use the relevant installed capabilities:

- \`workflow-core\`: execution/handoff protocol;
- \`ai-skills-core\` / AI Skills Maintainer: central plugin source/generated/replay/version/release discipline;
- \`presentations\`: presentation routing/template judgment.

These capabilities do not override the frozen Goal and may not expand Stage 1 scope.

---

## 4. Required private/reference inputs

### 4.1 Course template reference — REQUIRED

Exact user-provided file:

\`\`\`text
Chapter1.pdf
sha256 = ed205507a6d2de320b77d47d41e55bb0b406aef48144bc2c55d3bbba8c77ddf7
pages = 50
\`\`\`

The implementation must directly inspect the exact file. The summary in the approved architecture is not a substitute.

Preferred durable execution-machine locator after authorized materialization:

\`/home/yuukias/AI_Skills_Collection/private/exports/presentations--stage1-front-door-two-template-foundation/inputs/Chapter1.pdf\`

The reference must never be committed or pushed.

If it is unavailable or SHA mismatches:

\`BLOCKED_REFERENCE_UNAVAILABLE\`

Stop before substantive Stage 1 edits.

### 4.2 CUHK references — OPTIONAL SUPPORT, NOT NEW AUTHORITY

If available in the authorized private input surface, the existing user-provided CUHK references may be used for visual cross-check:

\`\`\`text
CUHK Template.pdf
sha256 = a62a4bb5ec2296b875ffe9ff8c1d850b88797e27a74aac7d64f576abb91daa7e

CUHK Template.zip
sha256 = 5cbe4a545d8abbab007f5f0aceec405138f8035b9dcb09c617e1e7cf7b525ee9
\`\`\`

But the canonical production authority remains:

\`skills/tools/documents-media/presentations/shared/templates/cuhk/beamer/source/\`

Do not replace that authority with the attachment or a derived scaffold.

---

## 5. Required user-visible routing behavior

The final Stage 1 candidate must implement this contract through the installed Presentations plugin:

| Natural request | Required result |
|---|---|
| research group meeting / research update / seminar / paper talk / journal club, no format | \`cuhk-research\` Beamer; source-editable \`.tex\` + PDF/render |
| QE / oral / defense, no venue template | \`cuhk-research\` Beamer |
| Tutorial / lecture / teaching / formula walkthrough, no format | \`course-standard\` Beamer |
| generic non-branded Beamer / LaTeX slides | \`course-standard\` unless CUHK explicitly requested |
| business / executive / product / strategy / client deck, no format | editable PPTX/Slides through official Presentation/Slides |
| explicit PPTX / Slides / editable | official editable Presentation/Slides |
| existing deck with feedback | preserve current format/template; route as revision, but do not implement Stage 5 runtime |
| small existing-deck edit | Presentations intake -> \`local-edit\` fast path -> preserve current format/template |
| explicit locked course/venue/client template | pass through that template; never add it to built-in registry |
| outline/storyline/notes only | plan-only; do not claim artifact generation |

A route selected only by a test helper or internal script is not sufficient.

---

## 6. Source ownership and allowed implementation

### 6.1 Primary allowed source

- \`scripts/codex_marketplace_config.json\`
- \`skills/tools/documents-media/presentations/research-presentations/SKILL.md\`
- \`skills/tools/documents-media/presentations/business-presentations/SKILL.md\`
- \`skills/tools/documents-media/presentations/shared/template-routing.md\`
- \`skills/tools/documents-media/presentations/shared/ppt-skill-routing.md\`
- \`profiles/presentation-desktop.json\`
- existing CUHK template source only for provenance/adapter-foundation needs
- new \`skills/tools/documents-media/presentations/shared/templates/course-standard/**\`
- directly relevant tests

### 6.2 Generated layer

Generated plugin/Marketplace/catalog files may change **only** through the repository's existing canonical generator.

Do not hand-edit:
- \`plugins/codex/plugins/**\`
- \`.agents/plugins/marketplace.json\`
- other generated catalog/plugin mirrors.

### 6.3 Conditional packaging fix

If and only if direct evidence shows the existing generic shared-payload generator cannot package the new template source, make the minimum generic compatibility fix. Do not create a presentation-specific generator or second packaging system.

---

## 7. Course-standard reconstruction contract

Reconstruct the visual template system, not the course content.

Required stable identity:
- 4:3;
- black top band;
- blue frame-title band;
- white body;
- blue first-level bullet;
- lower-right page number;
- sans body font;
- compatible serif/math rendering;
- ordinary Beamer frame/content mechanisms.

Forbidden:
- copying course prose, examples, references or equations as template content;
- baking yellow/orange/green/cyan PDF highlight annotations into the template;
- copying a whole reference PDF page as slide background;
- implementing teaching pedagogy/storyline/composition rules that belong to later stages.

Direct inspection must distinguish stable theme elements from PDF annotations and content-specific formatting.

---

## 8. Positive completion evidence

### 8.1 G1 — installed normal entry

G1 is PASS only when the exact committed candidate is loaded as an installed plugin in a fresh supported runtime and natural prompts exercise the routing branches.

A candidate replay helper may stage the candidate, but its receipt is not the product proof. Evidence must include the real child/runtime interaction and candidate skill consumption.

For Beamer routes:
- actual source generation;
- actual PDF compile;
- actual rendered page inspection.

For editable routes:
- reach a real official Presentation/Slides adapter on a supported surface.
- do not use \`python-pptx\`, reconstructed PDF or a route-only receipt as a substitute.
- if unavailable, return \`BLOCKED_REAL_EDITABLE_ADAPTER_SURFACE\` and do not claim G1 PASS.

### 8.2 G5 — template consumption + visual fidelity

For **both** built-in templates:

A. Actual consumption:
- canonical template source identity/hash;
- candidate-bound compile/build evidence proving that source was read/used.

B. Visual fidelity:
- real PDF/PNG render;
- independent reviewer sees the relevant pixels;
- for \`course-standard\`, reviewer also has the exact private \`Chapter1.pdf\`;
- for CUHK, reviewer verifies the canonical CUHK identity remains intact.

A and B are non-compensating. Either failure means G5 FAIL.

### 8.3 Broad regression because routing/profile/Marketplace are shared

At minimum use current canonical repo commands appropriate at execution time, including:
- targeted presentation tests;
- Marketplace generation/validation/check/path report;
- skills validation;
- full repository regression required by current AGENTS/CI;
- Reviewed Handoff validation;
- \`git diff --check\`;
- real GitHub CI because Stage 1 changes Marketplace/profile/shared routing/generated outputs.

Mechanical PASS does not replace G1/G5.

---

## 9. Horizontal evidence rules

### H1 — Scope-honest review

- Executor cannot self-sign final qualitative PASS.
- Reviewer must directly access Stage 1 candidate and G1/G5 evidence.
- Private template fidelity cannot be approved by someone who only sees a summary/hash.

### H2 — Same candidate

G1 and G5 claims must bind to the same committed Stage 1 implementation candidate. Do not stitch route PASS from one commit with template PASS from another.

### H3 — Regression integrity

Known current routes are development regression. Do not call them fresh/unseen.

### H4 — Source/runtime/render identity

Source, generated candidate, installed candidate plugin, template source, output PDF/PPTX and reviewed render must be traceable to the same candidate chain.

---

## 10. Required implementation sequence

1. **Preflight**
   - sync current approved base;
   - bootstrap exact Reviewed task/worktree;
   - re-read Goal/Plan/current source;
   - verify private Chapter1 reference and SHA;
   - verify current routing/profile/generated behavior;
   - verify TeX/render resources;
   - stop before edits on missing non-substitutable input.

2. **Source implementation**
   - minimal Marketplace/source-skill/shared-routing/profile changes;
   - add course-standard source;
   - preserve CUHK canonical source;
   - no later-stage behavior.

3. **Deterministic tests + generation**
   - add/update targeted tests;
   - regenerate canonical outputs;
   - verify generated parity;
   - run required broad regression.

4. **Commit exact candidate**
   - candidate replay/product evidence must use committed candidate, not dirty worktree.

5. **G1**
   - natural installed-candidate requests;
   - real adapter behavior;
   - Beamer artifact/render QA;
   - editable surface or truthful blocker.

6. **G5**
   - canonical-source consumption proof;
   - template visual fidelity bundle;
   - direct Chapter1 comparison.

7. **CI / review handoff**
   - publish exact reviewed branch non-force when required;
   - wait for actual CI according to Reviewed Handoff;
   - write truthful RESULT;
   - provide private durable review bundle.

---

## 11. Required durable private evidence

Any private input/render/comparison needed by future Critic/Reviewer must have a durable copy under the canonical checkout before task worktree cleanup.

Use:

\`/home/yuukias/AI_Skills_Collection/private/exports/presentations--stage1-front-door-two-template-foundation/\`

Suggested subdirectories:
- \`inputs/\`
- \`reference_renders/\`
- \`candidate_renders/\`
- \`g1/\`
- \`g5/\`
- \`review_bundle/\`

Record SHA-256 for private input and key review artifacts. Do not commit/push private reference content.

---

## 12. Non-substitutable semantics

Do not weaken or replace:

- exactly two built-in templates;
- research no-format -> CUHK;
- teaching no-format -> course-standard;
- business no-format -> editable;
- explicit PPTX/Slides -> official editable adapter;
- existing/local edit preserves format/template;
- local edit remains lightweight;
- external locked template stays pass-through;
- Chapter1 direct-read requirement;
- G5 actual consumption separate from visual fidelity;
- no new top-level presentation skill/plugin;
- no implicit-invocation hack;
- no later-stage implementation.

If any becomes impossible, stop and return \`NEEDS_GPT_PLANNER\` with direct evidence.

---

## 13. Out of scope

Do not implement:
- semantic storyboard / first-use / transition system;
- composition engine;
- citation/bibliography/text-layer work;
- writing-style/Clear Writing production changes;
- existing-deck revision runtime;
- final cross-mode release/generalization;
- universal IR/schema;
- geometry engine;
- #44–#48 promotion;
- third built-in template;
- Bridge Kit changes;
- new workflow/state machine;
- paid review/model calls;
- production plugin install/sync/release;
- main merge/integration.

---

## 14. Failure and recovery

Use these primary blockers:

- \`BLOCKED_DISCOVERY_CONSUMER\`: approved existing plugin surfaces cannot make natural request enter Presentations.
- \`BLOCKED_REFERENCE_UNAVAILABLE\`: exact Chapter1 file missing/mismatched.
- \`BLOCKED_REAL_EDITABLE_ADAPTER_SURFACE\`: official editable adapter cannot be exercised for required G1 evidence.
- \`BLOCKED_TEMPLATE_PROVENANCE\`: CUHK/template provenance or asset boundary materially prevents legitimate use.
- \`BLOCKED_GENERATOR_ARCHITECTURE\`: existing generator would need a new architecture rather than a small compatibility fix.
- \`NEEDS_GPT_PLANNER\`: any non-substitutable semantic or scope change is required.

No raw Git fallback, no alternate worktree, no silent lower-quality adapter, no new plugin/skill/control plane.

The last released \`presentations 0.3\` / current released plugin remains the rollback boundary.

---

## 15. Completion / non-completion claims

Stage 1 can only claim:

> the Stage 1 candidate implements and validates the approved unified front door/routing and two-template adapter foundation within G1/G5.

It cannot claim:
- Presentations V1.1 full redesign complete;
- plugin release complete;
- maturity improvement;
- Stage 2–6 complete;
- all TODOs solved;
- full PDF/UA;
- teaching quality beyond template foundation;
- existing-deck revision runtime complete.

---

## 16. Version, README and release

Stage 1 is an unreleased intermediate implementation candidate.

\`\`\`text
Repository bump decision: NONE
Affected plugins:
- presentations: NO_BUMP
\`\`\`

Do not release or bump version in Stage 1.

Record in RESULT:

\`README checked: final reader-facing update deferred to approved Stage 6 release closure; Stage 1 is an unreleased intermediate candidate.\`

If the current distribution system would automatically expose Stage 1 branch/main development as a production plugin update, stop before integration and return Planner. Do not silently convert Stage 1 into a release.

---

## 17. Git / publication authorization envelope

Only after the user sends the **Critic-approved Kickoff**:

Allowed:
- exact Reviewed task bootstrap;
- task-owned edits in exact reviewed worktree;
- tests/render/candidate replay;
- exact private input read and durable task evidence writes;
- task-owned commits;
- ordinary non-force publication of exact reviewed branch if required for CI/review.

Not allowed:
- alternate branch/worktree;
- force/destructive Git;
- PR/main merge;
- tag/release;
- production install/sync;
- version bump;
- paid model/API;
- credentials/provider change;
- Bridge Kit mutation.

---

## 18. Final Stage 1 handoff

Executor must finish according to current Reviewed Handoff semantics, not by declaring the overall architecture complete.

If CI is required, use the repository's canonical \`WAITING_FOR_CI\` flow and real GitHub checks.

The implementation Reviewer must review:
- exact Goal/Plan;
- actual implementation diff;
- G1 normal-entry evidence;
- G5 actual-consumption evidence;
- G5 visual-fidelity renders;
- exact Chapter1 reference or an authorized direct-access copy;
- deterministic regression/CI;
- source/generated/installed identity.

Only the implementation Reviewer can assign the Reviewed Handoff implementation PASS. That PASS still does not authorize main integration, Stage 2, or release.
