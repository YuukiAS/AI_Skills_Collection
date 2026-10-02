# Presentations Stage 1 Execution Plan — Front Door + Routing + Two-Template Adapter Foundation

**Package version:** 1.3  
**Status:** READY FOR EXECUTION-READY CRITIC REVIEW / NOT EXECUTION AUTHORIZATION  
**Date:** 2026-09-29  
**Repository:** \`YuukiAS/AI_Skills_Collection\`  
**Target plugin:** \`presentations\`  
**Task key:** \`presentations--stage1-front-door-two-template-foundation\`  
**Source ref:** current \`main\`

## 0. Authority and revision scope

Architecture authority remains:

\`docs/design/PRESENTATIONS_TWO_TEMPLATE_PRODUCTION_REDESIGN_PLAN_V1_1_2026-09-28.md @ f71e97c06938ab2ce175ccf3b4ac19da9309fda1\`

Prior reviewed Stage 1 package:

\`results/presentations--stage1-front-door-two-template-foundation/EXECUTION_PACKAGE_V1_2.md @ 6fe1b561bcebec7f9a6f677bb6ce3b26b91e6ca1\`

Latest Critic review:

\`results/presentations--stage1-front-door-two-template-foundation/CRITIC_EXECUTION_READY_REVIEW_V4.md @ faae612ea90aa1e7db948ae29837e699b8d13e25\`

Stable earlier blockers remain closed:

\`\`\`text
PRES-S1-ER-F01 = CLOSED
PRES-S1-ER-F02 = CLOSED
PRES-S1-ER-F03 = CLOSED
\`\`\`

This v1.3 is a complete replacement Stage 1 execution package, not a patch note. It accepts and closes only the two new execution-readiness findings:

- \`PRES-S1-ER-F04\`: Presentations must stop owning host-specific render-resource discovery and must consume \`render-chinese-math-pdf\` as the single environment/resource-resolution owner.
- \`PRES-S1-ER-F05\`: G5 private Chapter1 fidelity must use a concrete non-paid, direct-pixel review handoff that the GitHub-only Scheduled GPT Reviewer can consume without pretending it saw inaccessible private pixels.

Do not reopen already accepted:
- #49 Stage-1 template-foundation scope;
- #50–#53 deferral;
- 4:3 / 16:9 same-template ratio semantics;
- exactly two built-in templates;
- research/business/local-edit routing;
- Bridge Kit 0.9.3 first-publication closure;
- CI chronology;
- NO_BUMP / NO_RELEASE / no main integration.

No production code is authorized by this document.

---

## 1. Planner response to Critic v1.2 blockers

### PRES-S1-ER-F04 — ACCEPT

Direct current source proves the defect is in Presentations, not in \`render-chinese-math-pdf\`.

Current reusable Presentations source still contains:

\`\`\`text
/home/yuukias/render_resources/chinese_math_pdf
/home/yuukias/.TinyTeX/bin/x86_64-linux
\`\`\`

inside:

\`skills/tools/documents-media/presentations/shared/scripts/generate_cuhk_scientific_layout_stage3.py\`

and the normal research production entry consumes that module's dependency/render functions.

Meanwhile the installed support skill:

\`skills/tools/documents-media/render-chinese-math-pdf/\`

already owns:
- portable resource-root resolution;
- host-local overrides;
- TeX/font/cache environment;
- dependency probing;
- fail-closed missing-dependency semantics;
- diagnostic-only Chromium boundary;
- font/PDF QA.

Therefore v1.3 removes duplicate environment ownership from Presentations. No redesign of \`render-chinese-math-pdf\` is allowed unless new direct evidence proves that skill itself defective.

### PRES-S1-ER-F05 — ACCEPT

Current Bridge Scheduled GPT Reviewer is GitHub-connector-only and cannot directly read server-local private \`Chapter1.pdf\`.

v1.3 therefore binds one concrete non-paid evidence path:

\`\`\`text
exact final implementation candidate
-> exact G5 render bundle + hashes
-> user-visible Presentations long-term ChatGPT Planner thread
   receives exact private Chapter1 + exact candidate render files as uploads
-> that thread directly inspects pixels and verifies hashes
-> it writes a repo-tracked metadata-only G5_PRIVATE_VISUAL_REVIEW.md
   on the reviewed branch
-> Scheduled GPT Reviewer consumes that evidence
   plus diff/tests/CI, but explicitly does not claim direct access to Chapter1 pixels
\`\`\`

This is not a new Reviewed Handoff role or state machine. It is a private visual evidence handoff. The Scheduled GPT Reviewer remains the sole implementation-review authority.

---

## 2. Positive completion for Stage 1

One exact implementation candidate must prove all of the following:

1. natural presentation requests reach the installed candidate Presentations plugin;
2. routing/deliverable/template behavior matches the frozen matrix;
3. local-edit remains a lightweight preserve-format/template/ratio path;
4. business/executive and explicit PPTX/Slides remain editable routes;
5. exactly two built-in templates exist:
   - \`cuhk-research\`;
   - \`course-standard\`;
6. \`course-standard\` includes promoted #49 structural/navigation identity and 4:3 default + explicit 16:9 variant;
7. both Beamer adapters render through one portable \`render-chinese-math-pdf\` environment/resource-resolution contract, with no Presentations-owned private host path;
8. missing render dependency/font/package fails closed with typed exact dependency evidence;
9. canonical render QA rejects unexpected font fallback;
10. G5 source consumption and visual fidelity both pass independently;
11. private Chapter1 visual fidelity is decided through the concrete non-paid private G5 evidence path in this Plan;
12. real GitHub CI passes;
13. Stage 2–6 behavior remains unimplemented.

Mechanical tests alone cannot satisfy positive completion.

---

## 3. Product scope remains Stage 1 only

Stage 1 remains:

\`\`\`text
unified Presentations front door
+ routing/deliverable selection
+ local-edit fast path
+ two-template adapter foundation
+ #49 course-standard structural/navigation + ratio support
+ portable Beamer render-owner integration
+ generated-layer consistency
+ G1
+ G5
\`\`\`

Still excluded:

- Stage 2 semantic sequence / first-use / transition intelligence;
- Stage 3 composition intelligence;
- Stage 4 citation/language implementation;
- Stage 5 existing-deck revision runtime;
- Stage 6 final generalization/release;
- presenter-learning companion (#50);
- lecture/source cross-reference (#51);
- assessment semantic/answer-leakage behavior (#52);
- semantic closing choice (#53);
- new universal IR/schema;
- third built-in template;
- new top-level presentation skill/plugin;
- new geometry engine;
- new workflow/state machine;
- Bridge Kit mutation;
- paid Visual Review / Terra / Text Review;
- plugin release/version bump;
- main integration.

---

## 4. Routing contract remains frozen

\`\`\`text
research/group meeting/seminar/paper talk/journal club/QE/oral/defense, no format
-> cuhk-research Beamer

Tutorial/lecture/teaching, no explicit ratio
-> course-standard Beamer 4:3

teaching, explicit 16:9
-> same course-standard template identity, 16:9 variant

generic non-branded Beamer/LaTeX, no stronger context
-> course-standard, default 4:3 unless explicit ratio override

business/executive/product/strategy/client, no format
-> editable PPTX/Slides

explicit PPTX/Slides/editable
-> official editable adapter

existing deck/local edit
-> preserve current format/template/ratio

external locked template
-> pass-through locked input

plan-only
-> plan/notes only; no artifact claim
\`\`\`

Ratio remains an adapter parameter, not a third template or universal schema.

---

## 5. Two built-in template contracts

### 5.1 cuhk-research

Canonical template source remains:

\`skills/tools/documents-media/presentations/shared/templates/cuhk/beamer/source/\`

No product-identity change.

Stage 1 must preserve:
- exact canonical source consumption;
- CUHK visual identity;
- template-specific font/resource requirements;
- 16:9 research behavior.

Its environment/resource path ownership changes only as described in §7: Presentations may declare what the template requires but may not hardcode where a machine stores those resources.

### 5.2 course-standard

Private reference:

\`Chapter1.pdf\`

Expected identity:

\`\`\`text
sha256 =
ed205507a6d2de320b77d47d41e55bb0b406aef48144bc2c55d3bbba8c77ddf7
pages = 50
\`\`\`

Visual identity remains:
- black top band;
- blue frame-title band;
- white body;
- restrained academic Beamer;
- ordinary blue bullets;
- sparse teaching hierarchy;
- lower-right page number;
- sans body + compatible math;
- no annotation/highlight replication;
- no CUHK research branding.

Structural identity remains:
- canonical sparse opening/title frame;
- section-aware state/navigation;
- PDF outline/bookmarks;
- nonintrusive top navigation where appropriate;
- normal-Beamer bottom navigation/action affordances where appropriate;
- stable footline + page number;
- distinct title/content/section-aware/closing states;
- canonical closing-frame primitive.

Stage 1 does not choose recap/question/Q&A/thanks semantics.

Ratio:
- no explicit ratio -> 4:3 reference/default;
- explicit 16:9 -> same course-standard identity, wide variant;
- existing/local edit -> preserve ratio;
- external locked template -> preserve locked ratio.

---

## 6. TODO disposition remains frozen

\`\`\`text
#49 = PROMOTE_NOW
#50 = NEW
#51 = NEW
#52 = NEW
#53 = NEW
\`\`\`

#49 is limited to template-level structural/navigation and ratio support.

Do not pull #35/#38/#40/#47/#48 or #50–#53 into Stage 1 implementation.

No issue is DONE/closed by this package.

---

## 7. Render portability and owner boundary — closes PRES-S1-ER-F04

### 7.1 Single environment owner

For **both** built-in Beamer adapters:

\`render-chinese-math-pdf\`

is the sole owner of:
- render resource-root discovery;
- local override/environment resolution;
- TeX executable/resource environment;
- writable TeX cache strategy;
- font resource discovery;
- canonical PDF QA primitives.

Presentations owns:
- which template is selected;
- template-specific required files/packages/fonts;
- source generation;
- template fidelity criteria;
- adapter-specific render manifest.

Presentations does **not** own a second machine-discovery algorithm.

### 7.2 Required consumption contract

The Presentations adapter must consume the installed support skill's canonical resolved environment through its existing portable probe/resolution contract, including:

\`skills/tools/documents-media/render-chinese-math-pdf/scripts/probe_pdf_render_env.py\`

or a current equivalent canonical resolver owned by that same skill.

The implementation may factor a reusable helper **inside the existing render skill only if current source already exposes/needs a minimal reusable API and direct implementation evidence shows subprocess/probe consumption is insufficient**. Such a change is not pre-authorized by this Plan; it requires \`NEEDS_GPT_PLANNER\` unless it is purely mechanical and leaves the skill contract unchanged.

Default implementation assumption:
- reuse the existing render-skill probe/resolution outputs;
- do not redesign that skill.

### 7.3 Forbidden reusable paths

No reusable Presentations source or generated Presentations payload may contain a host-specific absolute render dependency path, including:

\`\`\`text
/home/yuukias
/overflow
/users
machine-specific TinyTeX/TeXLive bin roots
machine-specific font directories
\`\`\`

The rule applies to:
- \`skills/tools/documents-media/presentations/**\`;
- generated \`plugins/codex/plugins/presentations/**\`;
- reusable templates/scripts/config shipped in the candidate.

It does not forbid runtime evidence/receipts from recording the **resolved** absolute path actually used on a machine.

### 7.4 TeX environment

For native \`.tex\`/Beamer compilation, Presentations must use the resolved environment/resource contract supplied by \`render-chinese-math-pdf\`, including the applicable canonical strategy for:
- \`TEXMFHOME\`;
- \`TEXMFVAR\`;
- \`TEXMFCONFIG\`;
- \`TEXMFCACHE\`;
- \`TEXINPUTS\`;
- \`OSFONTDIR\`;
- compiler discovery.

Presentations may add template-local \`TEXINPUTS\` entries for canonical template source directories, but it may not replace the render owner's resource-root search with private absolute paths.

### 7.5 Font policy

The render skill owns environment/font discovery; the selected template owns its required font identity.

For course-standard:
- use only the approved template font family/resources;
- do not silently substitute another font.

For exact CUHK:
- if the canonical template requires a specific font family/resource, treat it as a template-specific dependency;
- locate it only through the resolved render environment/legal host-local override;
- if unavailable, fail closed.

Do not use as automatic substitutes:
- system font guessing;
- fontconfig Times lookup;
- arbitrary Times/Windows mount;
- DejaVu;
- Liberation;
- Fandol;
- another unrelated font.

The render skill's general default font policy does not override an explicit template/venue font contract; its environment resolver and PDF QA still own locating/validating the route.

### 7.6 Missing dependency semantics

If a required:
- resource bundle;
- compiler;
- TeX package;
- template file;
- font;
- PDF QA tool required by the frozen gate

is unavailable, Stage 1 must return a typed fail-closed dependency result.

Canonical class:

\`blocked_missing_dependency\`

Presentations task evidence must include the exact missing dependency and the attempted canonical route.

No automatic fallback to:
- Chromium;
- unrelated renderer;
- lower-fidelity template;
- system-font substitute;
- rasterized slide/image substitute.

### 7.7 Chromium boundary

Chromium remains diagnostic-only under the existing render-skill contract.

A Chromium-produced PDF cannot satisfy formal Beamer G1/G5 completion.

### 7.8 Portability regression gates

The Stage 1 candidate must directly prove:

**RP-G1 — two configured roots**
- the same unmodified Presentations source can compile/render a template probe using configured render root A;
- it can then compile/render using a different configured render root B;
- root selection is through the canonical render-skill resolver;
- receipts record which root was resolved;
- no source edit occurs between runs.

The two roots should exercise two supported configuration mechanisms where practical, such as environment override vs repo-external local override/project-local root. A second hardcoded constant is not evidence.

**RP-G2 — forbidden-path scan**
- scan reusable Presentations source and generated plugin payload;
- fail if forbidden private host roots or private TinyTeX/font absolute paths remain;
- historical results/audits are not reusable runtime and are not required to be rewritten.

**RP-G3 — typed missing-dependency block**
- remove or mask one required template font/package/resource in a controlled test;
- canonical route must return \`blocked_missing_dependency\` plus exact missing item;
- no alternative renderer/font may produce a PASS artifact.

**RP-G4 — fallback-font rejection**
- inject/observe a PDF that resolves an unexpected font outside the template-approved font contract;
- canonical G5 render gate must fail;
- a zero compiler exit code is insufficient.

**RP-G5 — both adapters consume same owner**
- CUHK and course-standard build manifests both record the render-skill resolution/route identity;
- neither adapter has a private environment resolver.

These are Stage 1 regressions because both adapters are being established/refined here.

---

## 8. Bridge Kit 0.9.3 chronology remains current

Verified formal Bridge release:

\`\`\`text
version = 0.9.3
formal release target =
9dad0ba4bfa54e251f345091c5151ae991251ec9
FORMAL_DISTRIBUTION_COMPLETE = YES
\`\`\`

Historical \`PRES-S1-ER-F03\` stays closed.

Execution-machine preflight must verify compatible 0.9.3+ runtime and:

\`ai-bridge reviewed-handoff task publish-first --help\`

If stale:

\`BLOCKED_BRIDGE_RUNTIME_STALE\`

Do not revive old F03 wording or raw-push fallback.

### Exact Reviewed task topology

Canonical checkout:

\`/home/yuukias/AI_Skills_Collection\`

Task:

\`presentations--stage1-front-door-two-template-foundation\`

Derived branch:

\`reviewed/presentations--stage1-front-door-two-template-foundation\`

Derived sibling worktree:

\`/home/yuukias/AI_Skills_Collection-presentations--stage1-front-door-two-template-foundation\`

### Bootstrap

Use current:

\`\`\`bash
ai-bridge reviewed-handoff task bootstrap \
  --task-key presentations--stage1-front-door-two-template-foundation \
  --expected-repo YuukiAS/AI_Skills_Collection \
  --expected-base-commit <POST_SYNC_ORIGIN_MAIN_OID> \
  --objective "Implement approved Presentations Stage 1 v1.3 only." \
  --ci-required
\`\`\`

Expected:

\`\`\`text
PLAN_REQUESTED
RUN_GPT_PLANNER
ci_required = true
plan_revision = 0
\`\`\`

### First metadata publication

Commit only exact first-bootstrap REQUEST/CURRENT, then:

\`\`\`bash
ai-bridge reviewed-handoff task publish-first \
  --task-key presentations--stage1-front-door-two-template-foundation \
  --expected-repo YuukiAS/AI_Skills_Collection
\`\`\`

No raw \`git push -u\`.

### Initial Plan freeze

External GPT Planner writes task-local \`AI_BRIDGE_REVIEWED_PLAN_V2\` and transitions:

\`\`\`text
PLAN_REQUESTED -> PLAN_FROZEN
next_action = RUN_CODEX_EXECUTOR
plan_revision = 0
\`\`\`

Only then may Executor edit production source.

---

## 9. G1 remains installed normal-entry routing

G1 still requires:
- exact committed candidate;
- installed candidate Presentations plugin;
- fresh supported runtime;
- natural user requests;
- actual candidate consumption.

Route families:
- research no-format;
- teaching default 4:3;
- teaching explicit 16:9;
- business no-format;
- explicit editable;
- existing-deck revision route;
- local edit;
- external locked template;
- plan-only.

Beamer routes must use the portable canonical render-owner contract from §7 and produce real source -> PDF -> render.

Editable routes still require the real supported official editable surface.

---

## 10. G5 remains non-compensating

For each built-in template:

### A. Actual source consumption
- canonical template source identity/hash;
- implementation commit;
- render owner/route identity;
- candidate-bound build manifest.

### B. Visual fidelity
- actual candidate renders;
- qualitative direct-pixel review;
- relevant reference identity.

A failure in A cannot be offset by B, and vice versa.

### Course-standard 4:3
Directly compare against exact private Chapter1 for visual/reference identity plus:
- opening/title;
- section navigation/state;
- bookmarks/outline;
- footline/page number;
- closing primitive.

### Course-standard 16:9
Verify:
- actual 16:9;
- same course-standard identity;
- coherent opening/navigation/footline/closing behavior;
- no clipping/safe-area regression.

Do not require exact 4:3 pixel geometry under a 16:9 override.

### CUHK
Existing exact canonical source/fidelity contract remains unchanged, now rendered through the same portable environment owner.

---

## 11. Concrete non-paid G5 private visual evidence path — closes PRES-S1-ER-F05

### 11.1 Ownership

The pixel-level private-reference evidence owner is:

\`PRESENTATIONS_LONG_TERM_PLANNER_CHAT_PRIVATE_G5_EVIDENCE\`

Meaning:
- a user-visible ChatGPT conversation/thread with direct file-upload access and GitHub connector access;
- independent from the Codex Executor;
- used only to produce G5 private visual evidence;
- **not** a new Reviewed Handoff role and **not** the final implementation Reviewer.

The Scheduled GPT Reviewer remains the only Reviewed Handoff implementation-review authority.

The private evidence thread may be the current long-term Presentations Planner thread if available.

### 11.2 Candidate identity freeze

After implementation source/tests are stable, Executor freezes one exact:

\`implementation_commit\`

and renders all G5 candidate probes from that commit.

Executor writes a repo-tracked metadata manifest:

\`results/presentations--stage1-front-door-two-template-foundation/g5_private_review/G5_REVIEW_INPUTS.json\`

It contains no private pixels/text and must include at minimum:

\`\`\`text
schema
task_key
implementation_commit
chapter1_expected_sha256
course_standard_source_sha256 / source manifest identity
cuhk_source_sha256 / source manifest identity
course_4_3_pdf_sha256
course_4_3_contact_sheet_sha256
course_16_9_pdf_sha256
course_16_9_contact_sheet_sha256
cuhk_pdf_sha256
cuhk_contact_sheet_sha256
render_input_identity for each probe
resolved_render_owner = render-chinese-math-pdf
resolved_route/profile identity
\`\`\`

### 11.3 Durable file bundle

Executor stores the actual files needed for direct review under:

\`private/exports/presentations--stage1-front-door-two-template-foundation/g5-review-bundle/\`

including:
- exact \`Chapter1.pdf\` input or a stable locator to the already-held exact file;
- course-standard 4:3 candidate PDF and contact sheet;
- course-standard 16:9 candidate PDF and contact sheet;
- CUHK candidate PDF/contact sheet when G5 review requires it;
- a copy of \`G5_REVIEW_INPUTS.json\`.

Candidate probe content must be repo-safe/generic and must not copy Chapter1 teaching content.

The private bundle is not committed/pushed.

### 11.4 User-visible ChatGPT transfer

When the exact implementation candidate is frozen and candidate files exist, the task reports:

\`PRIVATE_G5_REVIEW_PENDING\`

This is an operational evidence-wait label, **not a new CURRENT state**.

The user supplies/uploads to the Presentations long-term ChatGPT Planner thread:
- exact \`Chapter1.pdf\`;
- exact candidate render files from the G5 bundle;
- \`G5_REVIEW_INPUTS.json\` when useful.

The ChatGPT thread must directly access the file bytes/pixels and recompute/check:
- Chapter1 SHA-256 equals the frozen expected hash;
- each candidate upload hash equals \`G5_REVIEW_INPUTS.json\`;
- implementation/render identity matches the manifest.

A mismatched upload cannot be reviewed as the current candidate.

### 11.5 Qualitative review criteria

The private evidence thread directly evaluates:
- course-standard 4:3 reference/default fidelity;
- course-standard structural/navigation identity;
- course-standard 16:9 invariant identity and ratio correctness;
- no highlight replication;
- no clipping/safe-area/navigation regression;
- CUHK pixel fidelity where included in G5 handoff;
- rendered font identity/fallback evidence relevant to visible fidelity.

It may return:
- \`PASS\`;
- \`REVISE\`;
- \`BLOCKED_PRIVATE_G5_REVIEW_ACCESS\`.

It does not assign overall implementation PASS.

### 11.6 Durable evidence artifact

After direct inspection, the private evidence thread writes or causes a verbatim transaction to write:

\`results/presentations--stage1-front-door-two-template-foundation/g5_private_review/G5_PRIVATE_VISUAL_REVIEW.md\`

on the exact reviewed branch.

This committed artifact contains metadata/findings only, never Chapter1 pages or private screenshots.

Required fields/content:

\`\`\`text
schema = PRESENTATIONS_G5_PRIVATE_VISUAL_REVIEW_V1
task_key
implementation_commit
review_surface = USER_VISIBLE_CHATGPT_FILE_UPLOAD
direct_private_pixel_access = YES
chapter1_sha256
candidate file sha256 values
render identity values
criteria reviewed
decision = PASS | REVISE | BLOCKED_PRIVATE_G5_REVIEW_ACCESS
blocking findings if any
reviewed_at
private_pixels_committed = NO
\`\`\`

The review artifact is evidence/control-plane output after \`implementation_commit\`; committing it does not redefine the implementation candidate.

### 11.7 Relationship to CI

Preferred chronology:

\`\`\`text
freeze implementation_commit
-> generate G5 bundle + G5_REVIEW_INPUTS.json
-> publish reviewed branch / RESULT as required
-> WAITING_FOR_CI
-> real CI PASS
-> READY_FOR_GPT_REVIEW
-> if G5_PRIVATE_VISUAL_REVIEW.md missing: Scheduled GPT performs NO semantic review and leaves CURRENT unchanged
-> user-visible private G5 evidence handoff
-> commit G5_PRIVATE_VISUAL_REVIEW.md
-> next Scheduled GPT run consumes it
-> normal implementation REVIEW_<n>
\`\`\`

The private G5 handoff may be performed before CI finishes, but any implementation change invalidates it. Evidence is valid only when \`implementation_commit\` and all candidate hashes still match.

### 11.8 Scheduled GPT Reviewer consumption

The Scheduled GPT Reviewer must:
- read \`G5_REVIEW_INPUTS.json\`;
- read \`G5_PRIVATE_VISUAL_REVIEW.md\`;
- verify its \`implementation_commit\` equals CURRENT implementation commit;
- verify tracked candidate/hash metadata is consistent;
- require \`decision=PASS\` for the private visual portion of G5;
- review the actual source/diff/tests/CI and other evidence independently.

The Scheduled GPT Reviewer must explicitly state:

> It did not directly inspect the private Chapter1 pixels; it consumed a hash-bound direct-pixel evidence artifact produced by the user-visible ChatGPT private G5 review surface.

It must never write that it directly viewed an inaccessible private reference.

Missing/stale/mismatched evidence:
- leave \`CURRENT\` unchanged in \`READY_FOR_GPT_REVIEW\`;
- do not write \`REVIEW_<n>.md\`;
- do not consume review_round;
- report \`PRIVATE_G5_REVIEW_PENDING\` as the recovery need.

If the private review evidence says \`REVISE\`, the Scheduled GPT Reviewer may use it as a blocking frozen-requirement failure and enter the ordinary Reviewed Handoff REVISE path.

### 11.9 Unavailable private review surface

If the user-visible ChatGPT surface cannot receive/open the exact files after one bounded retry, or GitHub evidence transaction cannot be made available, fail closed as:

\`BLOCKED_PRIVATE_G5_REVIEW_ACCESS\`

Recovery owner:

\`USER + GPT PLANNER\`

Recovery:
- restore file-upload/direct-vision access;
- re-upload exact hash-bound artifacts;
- or explicitly authorize a different review mechanism in a new Planner/Critic decision.

Do not auto-enable:
- paid Bridge Visual Review;
- Terra;
- external API upload;
- OCR/text-summary substitute;
- Executor self-review.

No new workflow state is introduced.

---

## 12. Private Chapter1 handling

Exact private Chapter1 identity remains:

\`\`\`text
sha256 =
ed205507a6d2de320b77d47d41e55bb0b406aef48144bc2c55d3bbba8c77ddf7
pages = 50
\`\`\`

Preferred durable execution-machine locator:

\`/home/yuukias/AI_Skills_Collection/private/exports/presentations--stage1-front-door-two-template-foundation/inputs/Chapter1.pdf\`

Do not commit/push it.

Do not use the annotated STAT5060 PDF as plugin runtime input.

Do not convert private pixels into OCR/text summaries as a substitute for G5 visual review.

---

## 13. CI and automated review flags

Bridge task:

\`\`\`text
ci_required = true
visual_review_required = false
text_review_required = false
paid review = NOT AUTHORIZED
\`\`\`

Real GitHub CI is mandatory.

The private G5 evidence path is non-paid and manual/user-visible; it does not use the Bridge paid Visual Review route.

---

## 14. Source/generated authority

Primary source remains:
- \`scripts/codex_marketplace_config.json\`;
- Presentations research/business source skills;
- shared routing;
- \`profiles/presentation-desktop.json\`;
- canonical CUHK template source;
- new course-standard source;
- Presentations shared render adapter scripts;
- directly relevant tests.

The current Stage 1 implementation **must** modify the Presentations render adapter/source as necessary to remove host-specific environment ownership.

Generated:
- \`plugins/codex/plugins/**\`;
- \`.agents/plugins/marketplace.json\`;
- generator-owned mirrors.

Generated outputs only through current generator.

\`render-chinese-math-pdf\` production behavior is not in scope unless a new direct defect is proven. If such a defect appears, stop with \`NEEDS_GPT_PLANNER\`.

---

## 15. Validation matrix

### Routing/template
- G1 normal-entry families;
- course-standard default 4:3;
- course-standard explicit 16:9;
- existing/local ratio preservation;
- external locked template preservation.

### Template fidelity
- G5 actual consumption;
- G5 4:3 visual/structural fidelity;
- G5 16:9 invariant identity;
- CUHK exact source/fidelity.

### Render portability
- RP-G1 two configured resource roots;
- RP-G2 no forbidden host path in reusable source/generated payload;
- RP-G3 typed missing dependency;
- RP-G4 unexpected fallback font rejected;
- RP-G5 both adapters consume render-skill owner.

### Build/repo
- targeted Presentations tests;
- Marketplace generator write/validate/check/path-report;
- skills validation;
- broad/risk-matched repository tests;
- Reviewed Handoff validation;
- \`git diff --check\`;
- real GitHub CI.

### Review
- hash-bound \`G5_REVIEW_INPUTS.json\`;
- direct-pixel \`G5_PRIVATE_VISUAL_REVIEW.md\`;
- Scheduled GPT implementation review consumes rather than impersonates private visual access.

---

## 16. Non-substitutable semantics

The implementation is not this Stage 1 if any of the following change:

1. built-in template count != 2;
2. research no-format stops -> CUHK;
3. teaching default stops -> course-standard 4:3;
4. teaching explicit 16:9 stops -> same course-standard wide variant;
5. business no-format stops -> editable;
6. explicit PPTX/Slides stops -> official editable adapter;
7. existing/local edit changes format/template/ratio by default;
8. external locked template enters built-in registry;
9. local edit becomes full planning;
10. Chapter1 direct private-reference requirement is weakened;
11. #50–#53 teaching intelligence enters Stage 1;
12. Presentations keeps or adds a private host-specific render path/discovery path;
13. either Beamer adapter bypasses \`render-chinese-math-pdf\` environment ownership;
14. missing dependency silently falls back;
15. Chromium/system-font/lower-fidelity rendering is accepted as canonical Stage 1 PASS;
16. unexpected fallback font can pass G5;
17. private G5 review is replaced by OCR/text summary, Executor self-review or unapproved paid review;
18. Scheduled GPT claims it directly saw private pixels that it cannot access;
19. Bridge 0.9.3 normal entry is bypassed by raw first push;
20. \`--ci-required\` is removed;
21. Stage 2–6 enters scope.

Any required change returns Planner/Critic.

---

## 17. Stop / recovery

Fail closed on:

- \`BLOCKED_BRIDGE_RUNTIME_STALE\`;
- \`BLOCKED_REVIEWED_FIRST_BOOTSTRAP\`;
- \`BLOCKED_FIRST_PUBLICATION\`;
- \`BLOCKED_PLANNER_FREEZE\`;
- \`BLOCKED_CI_STATE\`;
- \`BLOCKED_DISCOVERY_CONSUMER\`;
- \`BLOCKED_REFERENCE_UNAVAILABLE\`;
- \`BLOCKED_REAL_EDITABLE_ADAPTER_SURFACE\`;
- \`BLOCKED_TEMPLATE_PROVENANCE\`;
- \`BLOCKED_RENDER_ENVIRONMENT\`;
- \`blocked_missing_dependency\`;
- \`BLOCKED_UNEXPECTED_FONT_FALLBACK\`;
- \`BLOCKED_GENERATOR_ARCHITECTURE\`;
- \`PRIVATE_G5_REVIEW_PENDING\` as nonterminal evidence wait;
- \`BLOCKED_PRIVATE_G5_REVIEW_ACCESS\` only after actual review-surface access failure;
- \`NEEDS_GPT_PLANNER\`.

No raw Git fallback.
No arbitrary renderer/font fallback.
No paid-review fallback.
No consumer-local workaround.

---

## 18. Version / release / integration

This remains planning-only / unreleased Stage 1 work.

\`\`\`text
Repository bump decision = NONE
Affected plugins:
- presentations = NO_BUMP
- workflow-core = NO_BUMP
- ai-skills-core = NO_BUMP
- writing-style = NO_BUMP
\`\`\`

No production install/release.
No main integration.
No maturity promotion.
No Stage 2+.

Current released Presentations remains rollback boundary.

---

## 19. Maintenance Board

Source truth:

\`\`\`text
#49 = PROMOTE_NOW
#50-#53 = NEW
other maturity unchanged
\`\`\`

Project lifecycle:

\`Area = presentations\`
\`Status = DOING\`

Issues in current tracking scope:

\`#29–#53\`

No issue is DONE/closed by this package.

If reader-facing Project mutation cannot be performed with required Clear Writing, record exact pending mutation and do not claim sync.

---

## 20. Execution-ready Critic target

The next Critic reviews the same v1.3:
- Plan v1.3;
- Goal v1.3;
- Kickoff v1.3;
- manifest v1.3;
- Planner response/validation v1.3.

Priority:

\`\`\`text
PRES-S1-ER-F04 = CLOSED ?
PRES-S1-ER-F05 = CLOSED ?
\`\`\`

Then only direct regression from these changes.

Only independent Critic PASS may set:

\`READY_FOR_CODEX=YES\`

and reproduce the exact approved v1.3 Kickoff for later user authorization.
