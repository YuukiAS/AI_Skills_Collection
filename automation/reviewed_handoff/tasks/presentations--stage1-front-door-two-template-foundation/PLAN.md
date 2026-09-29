---
schema: AI_BRIDGE_REVIEWED_PLAN_V2
task_key: presentations--stage1-front-door-two-template-foundation
decision: PLAN_FROZEN
---

# Reviewed Handoff Plan

## Objective and value

Implement only the Critic-approved Presentations Stage 1 v1.3 execution package.

The user-visible value is a single Presentations front door that preserves the existing editable/business/local-edit routes while establishing exactly two built-in Beamer adapters:

- \`cuhk-research\`
- \`course-standard\`

This stage must also make the Beamer route portable across configured machines by using \`render-chinese-math-pdf\` as the sole render environment/resource-resolution owner, and must make G5 private Chapter1 visual fidelity review executable through the approved non-paid, hash-bound direct-pixel evidence handoff.

Authority:

- architecture:
  \`docs/design/PRESENTATIONS_TWO_TEMPLATE_PRODUCTION_REDESIGN_PLAN_V1_1_2026-09-28.md @ f71e97c06938ab2ce175ccf3b4ac19da9309fda1\`
- Stage 1 execution Plan v1.3:
  \`docs/design/PRESENTATIONS_STAGE1_FRONT_DOOR_TWO_TEMPLATE_EXECUTION_PLAN_V1_3_2026-09-29.md\`
- Canonical Goal v1.3:
  \`docs/goals/PRESENTATIONS_STAGE1_FRONT_DOOR_TWO_TEMPLATE_GOAL_V1_3.md\`
- approved package:
  \`results/presentations--stage1-front-door-two-template-foundation/EXECUTION_PACKAGE_V1_3.md @ 5351f304381501f27833e5c7fa4f536ae5b684f8\`
- execution-ready Critic PASS:
  \`results/presentations--stage1-front-door-two-template-foundation/CRITIC_EXECUTION_READY_REVIEW_V5.md @ 85d4b2acd990654e8439c1c0dd007493360fa82b\`

This Plan freezes the already-approved package. Executor must not redesign product architecture, expand Stage 1, or reinterpret the accepted routing/Gate decisions.

## Frozen decisions

### Product entry and routing

Normal presentation requests must enter the installed Presentations plugin before routing.

Frozen routing:

\`\`\`text
research/group meeting/seminar/paper talk/journal club/QE/oral/defense, no format
-> cuhk-research Beamer

Tutorial/lecture/teaching, no explicit ratio
-> course-standard Beamer 4:3

teaching, explicit 16:9
-> the same course-standard template identity, 16:9 variant

generic non-branded Beamer/LaTeX, no stronger context
-> course-standard, default 4:3 unless user explicitly overrides ratio

business/executive/product/strategy/client, no format
-> editable PPTX/Slides

explicit PPTX/Slides/editable
-> official editable Presentation/Slides surface

existing deck/local edit
-> preserve current format/template/ratio

external locked template
-> pass-through locked input, never a third built-in template

plan-only
-> plan/notes only; never claim a generated artifact
\`\`\`

\`local-edit\` remains a lightweight path. It must not run full semantic planning or redesign unrelated pages.

### Exactly two built-in templates

Built-in template set is frozen to:

1. \`cuhk-research\`
2. \`course-standard\`

No third built-in template is allowed.

\`course-standard\` 16:9 is a ratio variant of the same template identity, not a third template.

### course-standard template-foundation scope

TODO disposition:

\`\`\`text
#49 = PROMOTE_NOW
#50 = NEW
#51 = NEW
#52 = NEW
#53 = NEW
\`\`\`

Only #49 enters Stage 1.

The course-standard Stage-1 template foundation must provide:

- canonical sparse opening/title frame;
- section-aware navigation/state;
- PDF outline/bookmarks;
- nonintrusive top navigation where appropriate;
- normal-Beamer bottom navigation/action affordances where appropriate;
- stable footline/page-number behavior;
- distinct title/content/section-aware/closing frame states;
- canonical closing-frame primitive.

Stage 1 must not choose the semantic closing job. Recap/question/Q&A/thanks selection remains later semantic/storyline work.

### course-standard visual and ratio identity

Visual identity remains:

- black top band;
- blue frame-title band;
- white body;
- restrained academic Beamer appearance;
- ordinary blue bullets;
- sparse teaching hierarchy;
- lower-right page number;
- sans body with compatible math typography;
- no Chapter1 PDF annotation/highlight replication;
- no CUHK research branding.

Ratio precedence:

1. existing deck / external locked template ratio;
2. explicit user ratio;
3. otherwise new course-standard defaults to 4:3.

Explicit teaching 16:9 must remain recognizably course-standard and must not route to CUHK merely because CUHK is wide.

### exact private Chapter1 reference

Required private reference identity:

\`\`\`text
Chapter1.pdf
sha256 =
ed205507a6d2de320b77d47d41e55bb0b406aef48144bc2c55d3bbba8c77ddf7
pages = 50
\`\`\`

The file is private/reference input only.

It must not be committed or pushed.
The annotated STAT5060 PDF must not become a plugin runtime input.
OCR/text summaries cannot substitute for direct G5 visual comparison.

### render owner boundary

For both Beamer adapters:

\`render-chinese-math-pdf\`

is the sole owner of:

- render resource-root discovery;
- project/local/environment/namespace/home/ancestor override resolution;
- TeX executable/resource environment;
- writable TeX cache strategy;
- font resource discovery;
- canonical PDF/font/text/layout QA primitives.

Presentations owns:

- template selection;
- template-specific required files/packages/fonts;
- source generation;
- template fidelity criteria;
- adapter-specific render/build manifest.

Presentations must not maintain a second host-discovery algorithm.

Reusable Presentations source/generated payload must not hardcode host-specific render dependencies, including:

\`\`\`text
/home/yuukias
/overflow
/users
private TinyTeX/TeXLive absolute bin roots
private font/resource absolute directories
\`\`\`

Runtime evidence may record the absolute path actually resolved on a machine.

Missing required render dependency must fail closed as:

\`blocked_missing_dependency\`

with the exact missing dependency and attempted canonical route.

Formal Beamer PASS cannot use:

- Chromium;
- system-font guessing;
- arbitrary Times/Windows font mount lookup;
- DejaVu;
- Liberation;
- Fandol substitution;
- unrelated renderer;
- rasterized substitute;
- lower-fidelity template/route.

Unexpected fallback font is a canonical render/G5 failure even if compilation exits zero.

Do not redesign \`render-chinese-math-pdf\` unless new direct evidence proves its current contract defective. If that occurs, stop and return \`NEEDS_GPT_PLANNER\`.

### G1

G1 remains installed-candidate normal-entry routing.

It must use:

- exact committed candidate;
- installed candidate Presentations plugin;
- fresh supported runtime;
- natural user prompts;
- actual candidate consumption;
- real user-facing artifact/adapter behavior.

Helper, fixture, route receipt, config presence, or direct script alone cannot PASS G1.

Beamer routes require real source -> PDF -> render through the portable render-owner contract.

Editable routes require the real supported official Presentation/Slides surface.

### G5

For each built-in template, G5 has two non-compensating evidence streams:

1. actual canonical source consumption;
2. visual fidelity.

A PASS in one cannot offset failure in the other.

For course-standard 4:3:
- compare against exact private Chapter1 reference/default identity;
- verify structural/navigation fidelity.

For course-standard 16:9:
- verify actual 16:9 ratio;
- verify invariant course-standard identity;
- verify coherent opening/navigation/footline/closing behavior;
- reject clipping/safe-area regressions;
- do not require 4:3 pixel dimensions.

For CUHK:
- preserve exact canonical CUHK source/fidelity contract;
- render through the same portable render-owner boundary.

### private G5 evidence path

The approved non-paid private pixel evidence owner is:

\`PRESENTATIONS_LONG_TERM_PLANNER_CHAT_PRIVATE_G5_EVIDENCE\`

This is a user-visible Presentations ChatGPT thread with direct file-upload/visual access and GitHub connector access. It is an evidence producer only, independent from Codex Executor. It is not a new Reviewed Handoff role and does not issue the final implementation PASS.

Executor must freeze one exact \`implementation_commit\` and generate tracked metadata:

\`results/presentations--stage1-front-door-two-template-foundation/g5_private_review/G5_REVIEW_INPUTS.json\`

At minimum this binds:

- task key;
- implementation commit;
- expected Chapter1 SHA;
- template-source identities;
- candidate PDF/contact-sheet hashes;
- render identities;
- render owner/profile identity.

Actual private review files must be retained under:

\`private/exports/presentations--stage1-front-door-two-template-foundation/g5-review-bundle/\`

The user then supplies/uploads exact Chapter1 and the exact current candidate renders to the user-visible Presentations ChatGPT review thread. That thread must verify hashes and directly inspect pixels.

The private evidence thread writes only metadata/findings to:

\`results/presentations--stage1-front-door-two-template-foundation/g5_private_review/G5_PRIVATE_VISUAL_REVIEW.md\`

Required review metadata:

\`\`\`text
schema = PRESENTATIONS_G5_PRIVATE_VISUAL_REVIEW_V1
task_key
implementation_commit
review_surface = USER_VISIBLE_CHATGPT_FILE_UPLOAD
direct_private_pixel_access = YES
chapter1_sha256
candidate file hashes
render identities
criteria reviewed
decision = PASS | REVISE | BLOCKED_PRIVATE_G5_REVIEW_ACCESS
blocking findings if any
private_pixels_committed = NO
\`\`\`

The Scheduled GPT Reviewer remains the sole Reviewed Handoff implementation-review authority.

It must consume the hash-bound private G5 evidence and explicitly state that it did not itself inspect inaccessible private Chapter1 pixels.

If private evidence is missing/stale/mismatched while \`CURRENT.state=READY_FOR_GPT_REVIEW\`:

- leave CURRENT unchanged;
- write no \`REVIEW_<n>.md\`;
- consume no review round;
- operationally wait on \`PRIVATE_G5_REVIEW_PENDING\`.

\`PRIVATE_G5_REVIEW_PENDING\` is not a CURRENT state.

If the approved private file-review surface is genuinely unavailable after bounded retry:

\`BLOCKED_PRIVATE_G5_REVIEW_ACCESS\`

Recovery owner is:

\`USER + GPT PLANNER\`

Do not enable paid Visual Review/Terra, OCR-only substitution, or Executor self-review as fallback.

### Reviewed Handoff / CI

The task remains:

\`\`\`text
ci_required = true
visual_review_required = false
text_review_required = false
paid review = NOT AUTHORIZED
\`\`\`

Bridge Kit 0.9.3+ \`task publish-first\` remains the approved first-publication path.

No raw first push.

Initial task-local PLAN is Planner-owned. Executor begins production work only from:

\`PLAN_FROZEN / RUN_CODEX_EXECUTOR\`

with \`plan_revision=0\`.

Final implementation chronology must preserve:

\`\`\`text
EXECUTING
-> WAITING_FOR_CI / ci_status=PENDING
-> real GitHub CI
-> CI PASS
-> READY_FOR_GPT_REVIEW
-> private G5 evidence available and valid
-> Scheduled GPT implementation review
\`\`\`

### Release boundary

Frozen:

\`\`\`text
Repository bump decision = NONE
presentations = NO_BUMP
no production install/release
no main integration
no maturity promotion
\`\`\`

Stage 1 PASS does not authorize Stage 2.

## Positive completion

Stage 1 is complete only when one exact implementation candidate directly proves all of the following:

1. natural presentation requests enter the installed candidate Presentations plugin;
2. route/deliverable/template/ratio decisions match the frozen routing matrix;
3. local-edit remains lightweight and preserves current format/template/ratio;
4. business/executive no-format and explicit PPTX/Slides remain editable routes;
5. exactly two built-in templates exist;
6. course-standard implements #49 structural/navigation identity;
7. course-standard defaults to 4:3 and supports explicit 16:9 as the same template variant;
8. both Beamer adapters consume \`render-chinese-math-pdf\` as the sole environment/resource-resolution owner;
9. reusable Presentations source/generated payload contains no forbidden private host render/font/TeX paths;
10. missing required render dependency fails closed with typed exact evidence;
11. unexpected fallback font cannot satisfy canonical render/G5;
12. G1 passes from real installed candidate natural entry;
13. G5 source consumption and visual fidelity both pass for the applicable template variants;
14. exact private Chapter1 fidelity is reviewed through the approved hash-bound direct-pixel evidence path;
15. real GitHub CI passes;
16. #50–#53 and all Stage 2–6 capabilities remain unimplemented;
17. no release/version/main-integration/maturity action occurs.

Maximum supported completion claim:

> The exact Stage 1 candidate implements and validates the unified Presentations front door/routing and two-template adapter foundation, including #49, portable render-environment ownership, and the approved hash-bound private G5 visual evidence path, under G1/G5 with required CI.

It does not prove full Presentations V1.1 redesign completion, Stage 2–6, long-term maturity, or release readiness.

## Non-substitutable semantics

Codex must not weaken or substitute any of the following:

1. exactly two built-in templates;
2. research no-format -> \`cuhk-research\`;
3. teaching default -> \`course-standard\` 4:3;
4. explicit teaching 16:9 -> same \`course-standard\` wide variant;
5. business no-format -> editable PPTX/Slides;
6. explicit PPTX/Slides -> official editable surface;
7. existing/local edit preserves current format/template/ratio;
8. local edit remains lightweight;
9. external locked template remains pass-through and outside built-in registry;
10. Chapter1 direct private-reference requirement and exact SHA remain mandatory;
11. #49 remains template-foundation scope only;
12. #50–#53 remain deferred;
13. \`render-chinese-math-pdf\` remains sole render environment/resource-resolution owner;
14. reusable Presentations payload cannot retain/add private host render/font/TeX paths;
15. missing dependency cannot silently fall back;
16. Chromium/system-font/arbitrary-font/lower-fidelity rendering cannot satisfy formal Beamer PASS;
17. unexpected font fallback cannot pass G5;
18. G5 source consumption and fidelity remain non-compensating;
19. private G5 evidence cannot be replaced by OCR/text summary, Executor self-review, or unapproved paid review;
20. Scheduled GPT Reviewer cannot claim it directly saw private pixels it cannot access;
21. Bridge 0.9.3+ bounded first-publication path cannot be replaced by raw first push;
22. \`ci_required=true\` cannot be removed;
23. \`visual_review_required=false\`, \`text_review_required=false\`, paid review not authorized;
24. Stage 2–6 cannot enter this task;
25. no release/version bump/main integration/maturity promotion.

If implementation requires changing any item above, return \`NEEDS_GPT_PLANNER\`.

## Implementation scope

Primary implementation scope is limited to Stage-1-owned Presentations source and directly necessary tests/evidence.

Allowed source areas when directly required:

- \`scripts/codex_marketplace_config.json\` Presentations interface/routing;
- \`skills/tools/documents-media/presentations/research-presentations/SKILL.md\`;
- \`skills/tools/documents-media/presentations/business-presentations/SKILL.md\`;
- \`skills/tools/documents-media/presentations/shared/template-routing.md\`;
- \`skills/tools/documents-media/presentations/shared/ppt-skill-routing.md\`;
- \`profiles/presentation-desktop.json\`;
- canonical CUHK adapter/template source only for approved Stage-1 adapter/portable-render integration;
- new \`course-standard\` template source;
- Presentations shared render/adapter scripts required to remove host-specific environment ownership;
- directly relevant Presentations/Marketplace tests;
- task-local tracked evidence/results;
- task-owned private evidence bundle under the approved \`private/exports\` path.

Generated layers such as:

- \`plugins/codex/plugins/**\`;
- \`.agents/plugins/marketplace.json\`;
- other generator-owned mirrors

must be rebuilt only through the existing canonical generator and not hand-edited.

\`render-chinese-math-pdf\` production semantics are not in scope. Reuse its current resolver/probe/environment contract. If current implementation proves that support skill itself requires a semantic change, stop with \`NEEDS_GPT_PLANNER\`.

No new top-level plugin/skill, third template, universal IR/schema, resource registry, workflow/state machine, or Bridge Kit change is allowed.

## Acceptance and regression gates

### G1 — installed normal-entry routing

G1 must use the exact committed candidate installed in a fresh supported runtime and natural user requests.

Required route families include:

- research no-format;
- teaching default 4:3;
- teaching explicit 16:9;
- business/executive no-format;
- explicit editable;
- existing-deck revision route;
- local edit;
- external locked template;
- plan-only.

Failure includes routing drift, silent format/template/ratio substitution, helper-only proof, or lack of the real adapter/artifact behavior.

Beamer routes must produce real source -> PDF -> render through the portable render-owner contract.

Editable routes require the real supported official editable surface.

### G5 — source consumption + visual fidelity

For each built-in template:

A. prove actual canonical source consumption;
B. prove visual fidelity.

These evidence streams cannot compensate for each other.

course-standard 4:3:
- exact Chapter1 reference/default fidelity;
- structural/navigation fidelity.

course-standard 16:9:
- actual 16:9;
- invariant course-standard identity;
- coherent navigation/footline/opening/closing;
- no clipping/safe-area regression.

CUHK:
- exact canonical source/fidelity unchanged.

Private Chapter1 visual evidence must follow the frozen non-paid direct-pixel path.

### RP-G1 — two configured resource roots

Using the same unmodified Presentations source:
- render through configured resource root A;
- render through a different valid configured resource root B;
- use supported \`render-chinese-math-pdf\` resolution mechanisms;
- record resolved root in receipts;
- make no source edit between runs.

### RP-G2 — forbidden reusable host-path scan

Scan reusable:
- \`skills/tools/documents-media/presentations/**\`;
- generated \`plugins/codex/plugins/presentations/**\`.

Fail if private host render/font/TeX paths remain in reusable payload.

Historical results/audits are not reusable runtime and do not need rewriting.

### RP-G3 — typed missing dependency

In a controlled test, mask/remove one required template font/package/resource.

Expected:
- \`blocked_missing_dependency\`;
- exact missing item reported;
- no substitute PASS artifact.

### RP-G4 — fallback-font rejection

A candidate PDF using an unexpected font outside the template-approved font contract must fail canonical render/G5 QA even if compile exit code is zero.

### RP-G5 — shared render owner

CUHK and course-standard build manifests must both record:
- \`render-chinese-math-pdf\` as environment owner;
- resolved route/profile identity.

Neither adapter may retain a private environment resolver.

### Broad regression / repository validation

Run current canonical equivalents of:

- targeted Presentations tests;
- course-standard 4:3 and 16:9 compile/render probes;
- opening/navigation/bookmark/footline/closing structural checks;
- Marketplace generator write/validate/check/path-report;
- source/generated parity;
- skills validation;
- broad/risk-matched repository tests;
- Reviewed Handoff validation;
- \`git diff --check\`;
- real GitHub CI.

Mechanical tests/CI do not replace G1/G5.

Should-not-change includes:

- current CUHK research route;
- business no-format editable route;
- explicit PPTX/Slides route;
- existing/local format/template/ratio preservation;
- external locked template pass-through;
- plan-only behavior;
- generated-layer ownership;
- #50–#53 remaining unimplemented;
- production same-name plugin outside candidate remaining untouched.

### Private G5 evidence acceptance

Executor must generate:

\`results/presentations--stage1-front-door-two-template-foundation/g5_private_review/G5_REVIEW_INPUTS.json\`

bound to exact \`implementation_commit\` and render identities/hashes.

Actual files remain in:

\`private/exports/presentations--stage1-front-door-two-template-foundation/g5-review-bundle/\`

Direct-pixel evidence is produced through the approved user-visible ChatGPT file-upload review surface and recorded metadata-only in:

\`results/presentations--stage1-front-door-two-template-foundation/g5_private_review/G5_PRIVATE_VISUAL_REVIEW.md\`

Scheduled GPT Reviewer consumes the evidence but does not claim inaccessible direct-pixel access.

Missing/stale/mismatched private evidence:
- no review artifact;
- no review-round consumption;
- CURRENT remains \`READY_FOR_GPT_REVIEW\`;
- wait on \`PRIVATE_G5_REVIEW_PENDING\`.

### Stop/recovery statuses

Use as applicable:

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
- \`PRIVATE_G5_REVIEW_PENDING\` as a nonterminal evidence wait;
- \`BLOCKED_PRIVATE_G5_REVIEW_ACCESS\`;
- \`NEEDS_GPT_PLANNER\`.

No lower-fidelity fallback is allowed.

## Natural-language usage / routing expectations

Representative user requests and expected behavior:

- “把这篇论文做成组会汇报，没特别格式要求。”
  -> Presentations intake -> research route -> \`cuhk-research\` Beamer.

- “把明天 Tutorial 做成课件。”
  -> Presentations intake -> teaching route -> \`course-standard\` 4:3 by default.

- “这个 Tutorial 要 16:9。”
  -> Presentations intake -> same \`course-standard\` template with explicit 16:9 ratio.

- “做一套给管理层的产品策略汇报。”
  -> Presentations intake -> editable PPTX/Slides route, not forced into Beamer.

- “把这个现有 PPT 第 6 页标题改短一点。”
  -> Presentations intake -> \`local-edit\` fast path -> preserve current format/template/ratio.

- “按这个会议官方模板做。”
  -> external locked template pass-through; do not add it to built-in registry.

- “只先给我逐页 storyline，不生成 PPT。”
  -> plan-only; no artifact-completion claim.

For formal Beamer routes, the user should not need to know or specify machine-local TeX/font/resource paths. A correctly configured machine resolves those through \`render-chinese-math-pdf\`; an incorrectly configured machine gets an exact fail-closed dependency report rather than a silent lower-quality artifact.

For private G5 fidelity, the user-visible handoff is explicit: once the exact candidate is frozen, the user supplies the exact Chapter1 and candidate renders to the Presentations ChatGPT review surface for direct visual comparison. The Scheduled GPT Reviewer then consumes the resulting hash-bound evidence rather than pretending it directly accessed the private file.

## Out of scope

Do not implement or treat as blockers for this Stage 1:

- Stage 2 semantic sequence / first-use / transition system;
- Stage 3 composition engine/intelligence;
- Stage 4 citation/language work;
- Stage 5 existing-deck diagnose/edit/render/compare runtime;
- Stage 6 final generalization/release closure;
- #50 presenter-learning companion;
- #51 teaching lecture/source cross-reference;
- #52 assessment-introduction/answer-leakage semantics;
- #53 semantic closing choice;
- broader #35/#38/#40/#47/#48 mechanisms;
- third built-in template;
- new top-level presentation skill/plugin;
- universal presentation IR/schema;
- geometry engine;
- new resource registry;
- new workflow/state machine or Reviewer role;
- redesign of \`render-chinese-math-pdf\`;
- Bridge Kit modification;
- paid Visual Review/Terra/Text Review;
- OCR/text-only substitute for private visual fidelity;
- production plugin install/release;
- repository/plugin version bump;
- main integration;
- maturity promotion;
- modification of STAT5060 project content.

Reviewer must judge only the frozen Stage 1 v1.3 scope and its relevant regression boundaries.
