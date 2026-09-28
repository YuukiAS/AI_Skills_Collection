# Presentations Stage 1 Execution Plan — Front Door + Routing + Two-Template Adapter Foundation

**Package version:** 1.0  
**Status:** READY FOR EXECUTION-READY CRITIC REVIEW / NOT EXECUTION AUTHORIZATION  
**Date:** 2026-09-29  
**Repository:** \`YuukiAS/AI_Skills_Collection\`  
**Target plugin:** \`presentations\`  
**Stage:** 1 of approved V1.1 architecture  
**Task key:** \`presentations--stage1-front-door-two-template-foundation\`  
**Source branch/ref for planning:** \`main\`

## 0. Design authority

Approved architecture:

\`docs/design/PRESENTATIONS_TWO_TEMPLATE_PRODUCTION_REDESIGN_PLAN_V1_1_2026-09-28.md\`  
approved design commit: \`f71e97c06938ab2ce175ccf3b4ac19da9309fda1\`

Independent architecture Critic PASS:

\`results/presentations--two-template-production-redesign/CRITIC_REVIEW_V2.md\`  
Critic PASS commit: \`ef2f1488b5e7479a4dd504f02ac2bd02b8825c07\`

This Stage 1 Plan implements only the first approved stage:

> Front door + routing + two-template adapter foundation.

It does **not** reopen V1.1 architecture and does not authorize Stages 2–6.

---

## 1. Product value and positive completion

Stage 1 adds one observable user capability:

> A normal presentation request can enter the installed Presentations plugin, select the correct mode/deliverable/template path without the user naming an internal skill, preserve the existing editable business route and local-edit behavior, and reach a real adapter whose template source is actually consumed.

Stage 1 positive completion requires all of the following on one exact implementation candidate:

1. a natural presentation request reaches the installed candidate Presentations plugin rather than only a repo helper or direct script;
2. the route matrix below is respected;
3. \`local-edit\` is a fast path, not a full-deck planning run;
4. \`business/executive\` no-format and explicit PPTX/Slides remain editable Presentation/Slides routes;
5. \`cuhk-research\` consumes the existing canonical CUHK Beamer source rather than a derived imitation;
6. \`course-standard\` has a new canonical reconstructed Beamer source whose implementation directly reads the user-provided \`Chapter1.pdf\` reference;
7. G5 has two independent evidence streams for each built-in template:
   - canonical source actually consumed;
   - visual fidelity of the rendered result;
8. generated Marketplace/plugin files are rebuilt only through the existing generator and match source;
9. the candidate does not implement Stage 2 semantic sequence, Stage 3 composition, Stage 4 citation/language, Stage 5 revision runtime, or Stage 6 release/generalization.

Mechanical test success alone is insufficient.

---

## 2. Execution placement and Reviewed Handoff normal entry

This package does not create a task, branch, worktree, or \`CURRENT.json\`. If execution-ready Critic later gives PASS and the user sends the approved Kickoff, execution must use the current Bridge Reviewed Handoff first-bootstrap normal entry.

### 2.1 Expected canonical checkout

Current repository evidence identifies the canonical Linux checkout as:

\`/home/yuukias/AI_Skills_Collection\`

Execution must revalidate this path, repo identity and clean/current state before mutation. The path is an expected locator, not permission to use an arbitrary alternate checkout.

### 2.2 Exact task topology

\`\`\`text
task_key = presentations--stage1-front-door-two-template-foundation
derived_branch = reviewed/presentations--stage1-front-door-two-template-foundation
derived_worktree = /home/yuukias/AI_Skills_Collection-presentations--stage1-front-door-two-template-foundation
base_ref = origin/main
\`\`\`

The current Bridge normal entry derives branch and sibling worktree from the task key. No raw \`git worktree add\`, caller-selected alternate branch, alternate clone or \`/tmp\` worktree is authorized.

### 2.3 Bootstrap contract

After syncing/fetching the canonical checkout, record the exact post-sync \`origin/main\` OID and invoke the installed Bridge command from the canonical repo cwd:

\`\`\`bash
ai-bridge reviewed-handoff task bootstrap \
  --task-key presentations--stage1-front-door-two-template-foundation \
  --expected-repo YuukiAS/AI_Skills_Collection \
  --expected-base-commit <POST_SYNC_ORIGIN_MAIN_OID> \
  --objective "Implement only approved Presentations Stage 1: unified front door/routing and two-template adapter foundation."
\`\`\`

The exact \`expected-base-commit\` cannot be hard-coded in this planning document because the execution-ready Critic review itself must already be present on \`main\`. It must equal the post-sync local \`origin/main\` OID at kickoff.

If this canonical bootstrap capability is unavailable, stale, rejected, or resolves a different branch/worktree/base, stop before substantive implementation and return a truthful blocker. Do not fall back to raw Git or modify Bridge Kit.

---

## 3. Current reality Stage 1 must change

Current \`main\` still contains the pre-Stage-1 behavior:

- Marketplace config describes the plugin mainly as research/business presentation planning;
- the plugin exposes \`research-presentations\` and \`business-presentations\`;
- both source skills exclude some minor existing-deck edits from their own trigger boundary;
- shared routing already handles Beamer vs editable routes, but teaching and local-edit are not a unified plugin intake contract;
- \`presentation-desktop\` is an installation/profile description and currently carries routing wording that can drift from shared routing;
- exact CUHK exists under the canonical Beamer source;
- no \`course-standard\` template source exists yet;
- generated plugin files are source-derived and must not be hand-edited.

This is a real consumer/routing task, not a documentation-only cleanup.

---

## 4. Normal-entry routing contract

The exact causal chain to make real is:

\`\`\`text
natural presentation request
-> installed Presentations plugin discovery/intake
-> mode + deliverable + template decision
-> shared core OR local-edit fast path
-> official Presentation/Slides adapter OR Beamer adapter
-> artifact/render QA appropriate to the selected route
\`\`\`

The plugin must not require the user to say \`research-presentations\`, \`business-presentations\`, an internal mode name, a script path, or a template path.

### 4.1 Default deliverable matrix

| Natural task | Mode | Default deliverable | Adapter/template |
|---|---|---|---|
| research group meeting / research update / seminar / paper talk / journal club, no format | new-deck | source-editable \`.tex\` + PDF + render | \`cuhk-research\` Beamer |
| QE / oral / defense, no venue template | new-deck | \`.tex\` + PDF + render | \`cuhk-research\` Beamer |
| Tutorial / lecture / teaching / formula walkthrough, no format | new-deck | \`.tex\` + PDF + render | \`course-standard\` Beamer |
| generic non-branded Beamer / LaTeX slides | new-deck | \`.tex\` + PDF + render | \`course-standard\`, unless CUHK explicitly requested |
| business / executive / product / strategy / client deck, no format | new-deck | editable PPTX/Slides | official Presentation/Slides |
| explicit PPT / PowerPoint / \`.pptx\` / editable / Slides / Google Slides | new-deck or revision | editable PPTX/Slides | official Presentation/Slides |
| explicit Beamer / LaTeX / \`.tex\` / academic PDF | new-deck | \`.tex\` + PDF + render | context-selected built-in Beamer template or explicit locked template |
| existing deck + feedback | existing-deck-revision | preserve current source/format | preserve current template; Stage 1 only routes, Stage 5 owns real revision runtime |
| one title / color / alignment / page number / object / small text change | local-edit | preserve current source/format | fast adapter path; no full storyboard |
| user/course/venue/client supplied locked template | applicable mode | format supported by supplied template | pass-through locked input; never added as third built-in template |
| storyline / outline / page plan / notes only | plan-only | plan/notes only | no fake artifact completion |

### 4.2 Local-edit fast path

Stage 1 must replace the current “minor edit does not trigger the presentation skill” concept with:

\`\`\`text
natural presentation edit request
-> Presentations intake
-> classify local-edit
-> preserve existing template + format
-> delegate directly to the appropriate real adapter
-> render/check affected pages or affected objects
\`\`\`

It must **not**:
- create a semantic storyboard;
- re-plan the whole deck;
- switch Beamer to PPTX or PPTX to Beamer;
- replace the user's template with one of the two defaults;
- redesign unrelated pages.

If the requested local change actually modifies story order, evidence meaning, cross-slide first-use or a previously accepted element, the route may escalate to \`existing-deck-revision\`. Stage 1 only establishes that routing boundary; Stage 5 owns the future revision runtime.

---

## 5. Source and consumer authority

Stage 1 must keep one source of truth per layer.

### 5.1 Marketplace/plugin interface authority

Canonical source:
- \`scripts/codex_marketplace_config.json\`

Allowed Stage 1 changes:
- Presentations description;
- default prompts;
- existing plugin skill exposure metadata only as necessary to make the approved intents discoverable.

Do not add a new top-level plugin or a third top-level presentation skill.

### 5.2 Source skill / shared routing authority

Canonical:
- \`skills/tools/documents-media/presentations/research-presentations/SKILL.md\`
- \`skills/tools/documents-media/presentations/business-presentations/SKILL.md\`
- \`skills/tools/documents-media/presentations/shared/template-routing.md\`
- \`skills/tools/documents-media/presentations/shared/ppt-skill-routing.md\`

The existing two source skills remain compatibility triggers for this stage.

Shared routing owns the mode/deliverable/template matrix.

Research/business skills must not independently contradict shared routing. In particular:
- small/minor edits must no longer bypass the Presentations plugin;
- business no-format must remain editable;
- explicit PPTX/Slides remains editable;
- teaching no-format must be routable to \`course-standard\`;
- exact CUHK remains research default where V1.1 says so.

### 5.3 Profile

Canonical:
- \`profiles/presentation-desktop.json\`

The profile describes installed capability composition. It must not become a second routing authority. Update only enough to remove semantic contradiction with the shared routing contract.

### 5.4 Generated layer

Generated only:
- \`plugins/codex/plugins/**\`
- \`.agents/plugins/marketplace.json\`
- other files already owned by the existing Marketplace/catalog generator.

Do not hand-edit generated files. Rebuild through the existing generator and verify source/generated parity.

If the current generator cannot carry the new \`course-standard\` shared source through the existing shared-payload mechanism, Executor may make the smallest AI_Skills-owned packaging fix necessary **only if it is a direct generator compatibility defect**. It must not create a second generator or a presentation-specific packaging framework.

---

## 6. Two-template adapter foundation

### 6.1 \`cuhk-research\`

Canonical source remains:

\`skills/tools/documents-media/presentations/shared/templates/cuhk/beamer/source/\`

Stage 1 may:
- clarify adapter identity/routing;
- preserve/prove source provenance and license notes;
- add focused tests/manifests proving actual canonical source consumption;
- build/render a template probe from that canonical source.

Stage 1 must not:
- replace the canonical source with design tokens, reference PPTX or a helper;
- redesign the CUHK template;
- alter semantic/page composition behavior;
- add new scientific layout rules.

One-time provenance closure must distinguish:
- Beamer class license;
- derived theme source/header provenance;
- CUHK logo/assets source and redistribution boundary;
- derived convenience assets vs canonical exact source.

If a material license/asset uncertainty prevents legitimate use, stop and report it instead of silently stripping or replacing branding.

### 6.2 \`course-standard\`

New canonical source is expected under a source-owned path such as:

\`skills/tools/documents-media/presentations/shared/templates/course-standard/beamer/source/\`

Exact final filenames may follow the existing CUHK source organization, but no additional template registry or third-party theme framework is needed.

Stage 1 implements only template-level primitives:
- 4:3 page geometry;
- black top band;
- blue frame-title band;
- white body;
- blue itemize marker;
- lower-right page number;
- sans body font with compatible math font;
- stable ordinary frame/title/body/bullet/page-number behavior.

Standard Beamer content mechanisms remain available. Stage 1 does not design teaching storyline, definition pedagogy, derivation choreography or layout-composition intelligence.

### 6.3 User-provided \`Chapter1.pdf\` is a required private reference

Known reference identity from the user-provided attachment:

\`\`\`text
filename: Chapter1.pdf
sha256: ed205507a6d2de320b77d47d41e55bb0b406aef48144bc2c55d3bbba8c77ddf7
size observed in Planner environment: ~455 KiB
pages: 50
\`\`\`

The Planner has verified the attachment exists in the current ChatGPT session; this does **not** prove it will automatically be present in the Codex execution environment.

Before substantive Stage 1 implementation, Executor must obtain the exact reference file and verify its SHA-256. Acceptable acquisition is only:
- an existing user-authorized private repo-local copy;
- a task input/attachment mechanism that supplies the exact user file;
- a user-authorized transfer into the durable private input path.

Recommended durable private locator on the execution machine:

\`/home/yuukias/AI_Skills_Collection/private/exports/presentations--stage1-front-door-two-template-foundation/inputs/Chapter1.pdf\`

The file must not be committed or pushed.

If the exact reference is not accessible, stop before course-standard implementation with:

\`BLOCKED_REFERENCE_UNAVAILABLE\`

Do not implement from V1.1 prose, screenshots, memory, OCR summaries or inferred colors alone.

### 6.4 Direct reference inspection requirement

Executor and the implementation Reviewer must directly inspect the exact \`Chapter1.pdf\` rather than rely on the Planner's summary.

Minimum implementation-side inspection:
- confirm metadata/page geometry;
- render the source PDF pages or a contact sheet;
- inspect the full reference for stable theme elements and variation;
- distinguish PDF highlight annotations from template visuals;
- identify representative pages for frame title/body/bullets/math/page-number behavior;
- record source SHA and inspected page set in task-local evidence.

The reference is copyrighted/private input. Do not copy its teaching content into the plugin or public evidence.

### 6.5 G5 evidence is non-compensating

For each built-in template, G5 has two required subevidence streams.

**A. Actual source consumption**
- the build must prove it consumed the approved canonical template source;
- use manifest/hash/compile-path evidence bound to the implementation candidate;
- source existence alone is not enough.

**B. Visual fidelity**
- render the template probe through the real Beamer toolchain;
- compare with the frozen template identity/reference;
- independent review must directly see the relevant pixels;
- no weighted score may allow A PASS to compensate B FAIL or vice versa.

For \`course-standard\`, visual review must compare the generated probe with the exact private \`Chapter1.pdf\` reference.

For \`cuhk-research\`, visual review must prove canonical CUHK identity remains intact and no derived convenience scaffold replaced the exact source.

Teaching readability beyond basic template legibility belongs to later G3/G8, not Stage 1.

---

## 7. Stage 1 Capability Gate Matrix

Only architecture G1 and G5 are in Stage 1 scope. H1–H4 apply horizontally where relevant.

### G1 — Installed normal-entry routing and deliverable preservation

**Capability / claim**  
A normal user presentation request reaches the installed candidate Presentations plugin and selects the correct mode/deliverable/template path.

**Why distinct**  
This gate proves discovery/intake/routing. It does not prove semantic story quality or advanced page composition.

**Normal entry**  
Use an actual installed candidate plugin in a fresh supported ChatGPT/Codex runtime. Prompts must be natural user prompts and must not name internal skills, scripts, route IDs or modes.

The repo-local candidate replay tool may stage the exact committed candidate and preserve identity, but **its receipt/helper output is not G1 PASS evidence by itself**. G1 must judge the actual child/runtime interaction with the installed candidate.

**Route-family evidence**  
Exercise every distinct routing branch in §4.1 because each is a different contract, not because a fixed sample count is a quality metric:
- research no-format;
- teaching no-format;
- business/executive no-format;
- explicit PPTX/Slides;
- existing-deck revision;
- local edit;
- external locked template;
- plan-only.

**Artifact/adapter requirement**
- Beamer routes: complete through real \`.tex -> PDF -> rendered page\` production and inspect the result.
- Editable Presentation/Slides routes: use a real supported official adapter surface when available; do not substitute \`python-pptx\`, a PDF reconstruction or a route-receipt-only fake.
- If the execution environment cannot reach the official editable adapter, return \`BLOCKED_REAL_EDITABLE_ADAPTER_SURFACE\` for that branch. Do not silently downgrade the gate.

**Failure**
- natural request does not consume the candidate plugin;
- teaching/local-edit is undiscoverable;
- business no-format becomes Beamer;
- explicit editable request becomes Beamer;
- local edit launches full planning or changes template/format;
- external locked template is inserted into built-in registry;
- plan-only claims an artifact was produced;
- adapter route cannot produce/validate the expected artifact and silently falls back.

**Regression boundary**
- explicit user format/template overrides defaults;
- existing deck keeps current template;
- production plugin identity outside the candidate remains unchanged;
- current research/CUHK default remains intact.

**Final-candidate requirement**
YES for the Stage 1 implementation candidate.

### G5 — Built-in template actual consumption + visual fidelity

**Capability / claim**  
\`cuhk-research\` and \`course-standard\` both use their approved source and render with the frozen template identity.

**Why distinct**  
G5 tests the adapter/template foundation rather than routing discovery.

**Normal entry**
Natural research/teaching prompts from G1 must reach the respective Beamer adapter. A direct template compilation may be used as additional diagnostic evidence, not as the only proof.

**Evidence A: actual consumption**
- exact source identity/hash;
- build/compile manifest;
- candidate-bound path showing the real canonical source was consumed.

**Evidence B: visual fidelity**
- real rendered PDF/PNG;
- source reference accessible to reviewer;
- template identity checks;
- independent qualitative inspection of representative pixels.

**Failure**
- helper/tokens mimic theme without canonical source;
- course-standard is implemented without the exact Chapter1 reference;
- reference highlights are baked into template;
- CUHK title/header/footer/logo identity drifts;
- actual source and rendered reference do not correspond;
- A/B evidence disagree.

**Regression boundary**
- no storyline or composition changes;
- no new template;
- external locked inputs stay outside built-in registry;
- no claim of full teaching quality.

**Final-candidate requirement**
YES for the Stage 1 implementation candidate.

---

## 8. Broad regression required by blast radius

Stage 1 changes shared routing, Marketplace/plugin interface, profile exposure and generated payloads, so it is **not** eligible for a narrow routing-only test.

Before implementation review, run:

1. targeted presentation routing/template tests;
2. Marketplace generation/source parity tests;
3. source skill validation;
4. full repository tests required by current repo contract;
5. explicit should-not-change cases:
   - current CUHK research route;
   - explicit editable PPTX route;
   - business no-format editable route;
   - explicit external template;
   - existing deck format/template preservation;
   - plan-only;
   - local edit fast path;
6. candidate normal-entry G1 evidence;
7. template G5 source-consumption + render evidence.

Do not call this Stage 2–6 generalization. It is risk-matched regression for Stage 1's shared routing/profile/Marketplace blast radius.

---

## 9. Expected source modification scope

Primary source files allowed when directly necessary:

- \`scripts/codex_marketplace_config.json\`
- \`skills/tools/documents-media/presentations/research-presentations/SKILL.md\`
- \`skills/tools/documents-media/presentations/business-presentations/SKILL.md\`
- \`skills/tools/documents-media/presentations/shared/template-routing.md\`
- \`skills/tools/documents-media/presentations/shared/ppt-skill-routing.md\`
- \`profiles/presentation-desktop.json\`
- \`skills/tools/documents-media/presentations/shared/templates/cuhk/**\` only for provenance/adapter identity tests or directly required non-semantic foundation repair
- new \`skills/tools/documents-media/presentations/shared/templates/course-standard/**\`
- \`tests/test_presentations.py\`
- \`tests/test_codex_marketplace.py\`
- existing Marketplace/catalog generation outputs through the canonical generator
- task-local \`results/presentations--stage1-front-door-two-template-foundation/**\`
- durable private task evidence/input under canonical \`private/exports/presentations--stage1-front-door-two-template-foundation/**\`

Conditionally allowed:
- the existing Marketplace generator source only if direct evidence shows it cannot package the new shared template through its current generic shared-payload contract. Any change must be the smallest generic compatibility fix and must not create a presentation-specific generator.

Not allowed:
- \`deck-plan.schema.json\` expansion;
- Stage 2 semantic sequence implementation;
- Stage 3 composition core;
- Stage 4 citation/language changes;
- Stage 5 revision runtime;
- Stage 6 release/generalization;
- root workflow redesign;
- Bridge Kit changes.

---

## 10. Explicit non-substitutable semantics

The implementation is not the same Stage 1 task if any of these change:

1. there are more or fewer than two built-in templates;
2. business/executive no-format stops defaulting to editable PPTX/Slides;
3. explicit PPTX/Slides stops using the official editable adapter;
4. research/group meeting/seminar/QE/oral/defense no-format stops defaulting to \`cuhk-research\`;
5. teaching no-format stops defaulting to \`course-standard\`;
6. existing deck/local edit changes current format/template by default;
7. local edit runs full semantic planning;
8. external locked templates enter the built-in registry;
9. course-standard is reconstructed without directly reading the exact user reference;
10. G5 actual-consumption and visual-fidelity evidence are collapsed into one compensating score;
11. discovery failure is bypassed by a new top-level skill/plugin, implicit invocation hack or new control plane;
12. Stage 2–6 behavior is implemented inside Stage 1.

A need to change any item above requires Planner/Critic re-entry before implementation continues.

---

## 11. Out of scope

Strictly out of Stage 1:

- semantic storyboard / transition map / first-use registry;
- page-composition logic;
- scientific-object primitives beyond current unchanged behavior;
- citation/bibliography/text-layer implementation;
- Clear Writing/scientific-prose changes;
- existing-deck diagnose/edit/render/compare runtime;
- final fresh generalization batch;
- plugin release/version bump;
- maturity change;
- README release closure;
- third built-in template;
- new top-level presentation skill/plugin;
- implicit invocation hack;
- geometry engine;
- #44–#48 promotion;
- Bridge Kit modification;
- workflow/state-machine/ledger/database creation;
- paid API/review.

---

## 12. Validation sequence

The implementation Goal should follow this order.

### Phase A — preflight before mutation

- fetch/sync approved base and validate exact task topology;
- read current AI_Skills AGENTS and Stage 1 Goal;
- verify Bridge bootstrap/task state;
- verify exact \`Chapter1.pdf\` is accessible and SHA matches;
- inspect current presentation routing/source/profile/generated identity;
- inspect canonical CUHK source and provenance header;
- check renderer/TeX/font/PDF tooling using current repo/skill probes;
- if any non-substitutable input is unavailable, fail before substantive edits.

### Phase B — source implementation

- implement unified plugin intake/routing only through approved source surfaces;
- add course-standard canonical template source;
- preserve CUHK canonical source identity;
- add targeted deterministic tests;
- do not edit generated layer manually.

### Phase C — regenerate and deterministic regression

- run canonical generator with write + validate/check/path-report as required;
- run target tests;
- run full/risk-matched repository validation;
- prove source/generated parity.

### Phase D — real candidate G1/G5 evidence

- commit the candidate before replay;
- run actual installed candidate natural-request routes;
- render Beamer artifacts;
- use real editable adapter surface for editable/local-edit branches when available;
- produce candidate-bound template consumption manifests;
- render course-standard probe and CUHK probe;
- keep private reference/comparison assets in durable private storage.

### Phase E — implementation review handoff

- RESULT must separate deterministic tests from G1/G5 product evidence;
- reviewer must have access to exact candidate, route outputs, Beamer renders, template source-consumption evidence, and private \`Chapter1.pdf\` comparison bundle;
- no generator/Executor self-sign;
- no Stage 1 PASS if G1 or G5 has a material unresolved branch.

---

## 13. Stop conditions and recovery

Stop and return Planner/Critic when:

- existing plugin discovery surfaces cannot make the approved natural intents enter Presentations without a forbidden new skill/control-plane mechanism;
- official editable adapter cannot be reached for required G1 branches;
- exact \`Chapter1.pdf\` is unavailable or hash mismatches;
- course-standard reconstruction would require copying restricted course content;
- CUHK canonical provenance/license/asset boundary is materially unresolved;
- the current generator cannot include the new template without an architectural packaging change;
- implementation needs a universal IR/schema;
- local-edit cannot be made lightweight without Stage 5 runtime changes;
- any #44–#48 candidate-only mechanism becomes necessary;
- Stage 1 changes require Bridge Kit modification.

Recovery:
- do not use raw Git fallback;
- leave current released \`presentations 0.3\` / last released version as rollback boundary;
- preserve current main/production install;
- commit only truthful task evidence if the reviewed workflow permits;
- return exact blocker and the smallest needed Planner decision.

---

## 14. Git, publication and side-effect boundary

When the approved Kickoff is eventually sent, it may authorize only:

- canonical Reviewed task bootstrap for the exact task key/repo/base;
- task-owned source edits in the exact reviewed worktree;
- deterministic tests, local render and candidate replay within repo policy;
- private read of the exact user-provided template references;
- task-owned durable private evidence writes;
- ordinary commits on the exact reviewed branch;
- ordinary non-force publication of that exact reviewed branch for Critic/Reviewer/CI access when required by the reviewed workflow.

Not authorized by Stage 1:
- force push;
- alternate branch/worktree;
- PR creation;
- main merge/integration;
- tag/release;
- production plugin install/upgrade/sync;
- version bump;
- paid API/model review;
- external credential changes;
- destructive cleanup;
- Bridge Kit change.

Stage 1 implementation PASS is not a plugin release. How the reviewed Stage 1 candidate is carried into the next approved stage is a later Planner decision; do not improvise integration into \`main\`.

---

## 15. Version / README / maturity decision

This execution package itself is docs-only:

\`\`\`text
Repository bump decision: NONE
Affected plugins:
- presentations: NO_BUMP
- writing-style: NO_BUMP
- workflow-core: NO_BUMP
- ai-skills-core: NO_BUMP
\`\`\`

During Stage 1 implementation:
- no plugin release;
- no version bump;
- no maturity change;
- no claim that \`baseline\` changed;
- no final README release rewrite.

Stage 1 RESULT must record:

\`README checked: final reader-facing update deferred to approved Stage 6 release closure; Stage 1 is an unreleased intermediate candidate.\`

If current repo policy or a later Critic determines this deferral would expose partial behavior through an actual production distribution surface, stop before integration and return Planner. Do not solve it by silently releasing Stage 1.

---

## 16. External source check used for this package

Targeted recheck on 2026-09-29:

- OpenAI current plugin documentation confirms a plugin packages skills/capabilities, users can explicitly select an installed plugin in ChatGPT/Codex, Git-backed/local marketplaces expose plugins, and the host loads installed plugin copies rather than treating source-file existence as runtime consumption.
  - https://help.openai.com/en/articles/20001256-plugins-in-codex/
  - https://developers.openai.com/plugins/build/plugins
- OpenAI current Skills documentation states installed skills can be used automatically when helpful; availability and loading differ by product surface.
  - https://help.openai.com/en/articles/20001066-skills-in-chatgpt
- CTAN still reports Beamer 3.78 (2026-08-20), with a template system and Tagged PDF unsupported.
  - https://ctan.org/pkg/beamer
  - https://ctan.org/tex-archive/macros/latex2e/contrib/beamer

Impact on Stage 1:
- G1 must test an actually installed candidate on a real supported surface, not source-file presence;
- source/plugin/profile/generated parity is necessary but not sufficient;
- Beamer remains the approved template adapter foundation;
- no new renderer/class is introduced.

---

## 17. Maintenance Board

Canonical Issues \`#29–#48\` keep their current source maturity. Project lifecycle remains \`DOING\`.

This package does not mutate Project/Issue copy unless the current surface can first invoke the required installed Clear Writing capability. If not, the exact pending mutation after the execution package commit is:

\`\`\`text
Project: AI Skills Maintenance
Area: presentations
Issues: #29–#48
Status: DOING

Current execution anchor:
<Stage 1 execution package manifest path>
@ <Stage 1 package manifest commit>

Next action:
independent execution-ready Critic review of Stage 1 Proposal/Plan + Canonical Goal + Kickoff Draft

Do not:
- change source maturity
- mark PROMOTED
- mark DONE
- close issues
\`\`\`

---

## 18. Execution-ready Critic decision requested

Critic should issue \`PASS\` only if the same package version contains:
1. this Stage 1 Proposal/Plan;
2. the Stage 1 Canonical Goal;
3. the Stage 1 Kickoff Draft;

and all three agree on:
- exact task/branch/worktree semantics;
- scope;
- G1/G5;
- private Chapter1 reference boundary;
- stop/recovery conditions;
- no Stage 2–6 work;
- no release/paid/main-integration authority.

Only an execution-ready Critic PASS may produce \`READY_FOR_CODEX=YES\` and return the reviewed Kickoff verbatim.
