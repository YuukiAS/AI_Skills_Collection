---
schema: AI_BRIDGE_REVIEWED_PLAN_V2
task_key: presentations--stage1-front-door-two-template-foundation
decision: PLAN_FROZEN
---

# Reviewed Handoff Plan

## Objective and value

Implement only the Critic-approved Presentations Stage 1 v1.3 execution package, with one minimal dependency-sequencing revision:

- this task must continue all Stage-1 work that does **not** require ownership of the final canonical \`course-standard\` template body;
- an independent canonical standard-Beamer task is now the sole owner of the final \`course-standard\` template source;
- this task must wait only for the exact canonical \`course-standard\` source locator/commit/consumption boundary before final adapter integration and final G1/G5 closure;
- this task must not create or continue a second canonical \`course-standard\` template body.

The user-visible value remains unchanged: a single Presentations front door that preserves editable/business/local-edit routes while establishing exactly two built-in Beamer adapters, portable render-environment ownership through \`render-chinese-math-pdf\`, and the approved private G5 visual evidence path.

Authority remains:

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
- current Planner re-entry trigger:
  \`results/presentations--stage1-front-door-two-template-foundation/RESULT.md\`

This revision changes dependency sequencing/source ownership only. Executor must not redesign product architecture, expand Stage 1, weaken any approved Gate, or change release boundaries.

## Frozen decisions

### Product entry and routing

Normal presentation requests must enter the installed Presentations plugin before routing.

Frozen routing remains:

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

\`local-edit\` remains lightweight and must not trigger full semantic planning or unrelated redesign.

### Exactly two built-in templates

Built-in template identities remain exactly:

1. \`cuhk-research\`
2. \`course-standard\`

No third built-in template is allowed.

\`course-standard\` 16:9 remains a ratio variant of the same template identity.

### Canonical course-standard source ownership

The final canonical \`course-standard\` template body is owned by the independent canonical standard-Beamer task.

This Stage 1 task must therefore:

- keep the \`course-standard\` identity/registry/routing contract;
- keep the approved 4:3 default and explicit 16:9 same-template semantics;
- keep #49 requirements as acceptance requirements;
- leave the canonical source locator unresolved until the independent task provides:
  - exact source path;
  - exact candidate commit;
  - allowed consumption/integration boundary;
- consume that exact canonical source only after those locators are supplied;
- never create, restore, or promote a second task-local canonical \`course-standard\` template body;
- never treat any previously temporary \`course-standard\` source as authority.

Dependency wait label:

\`WAITING_FOR_CANONICAL_COURSE_STANDARD_TEMPLATE\`

This is a dependency label, not a Reviewed Handoff CURRENT state and not a global stop condition for all Stage-1 implementation.

### #49 / #50–#53

TODO disposition remains:

\`\`\`text
#49 = PROMOTE_NOW
#50 = NEW
#51 = NEW
#52 = NEW
#53 = NEW
\`\`\`

#49 remains template-foundation scope only.

The final canonical course-standard source, once available, must provide the already-approved #49 behavior:

- canonical sparse opening/title frame;
- section-aware navigation/state;
- PDF outline/bookmarks;
- nonintrusive top navigation where appropriate;
- normal-Beamer bottom navigation/action affordances where appropriate;
- stable footline/page-number behavior;
- distinct title/content/section-aware/closing frame states;
- canonical closing-frame primitive.

This task must not independently implement a second version of those primitives while the canonical template is pending.

Stage 1 still must not choose the semantic closing job; recap/question/Q&A/thanks selection remains later semantic/storyline work.

### course-standard visual and ratio identity

The final integrated canonical source must preserve the approved identity:

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

Ratio precedence remains:

1. existing deck / external locked template ratio;
2. explicit user ratio;
3. otherwise new course-standard defaults to 4:3.

Explicit teaching 16:9 must remain recognizably course-standard and must not route to CUHK merely because CUHK is wide.

### exact private Chapter1 reference

Required private reference identity remains:

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

remains the sole owner of:

- render resource-root discovery;
- project/local/environment/namespace/home/ancestor override resolution;
- TeX executable/resource environment;
- writable TeX cache strategy;
- font resource discovery;
- canonical PDF/font/text/layout QA primitives.

Presentations owns:

- template selection;
- template-specific required files/packages/fonts;
- source generation around the consumed canonical template;
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
- arbitrary Times/Windows font lookup;
- DejaVu;
- Liberation;
- Fandol substitution;
- unrelated renderer;
- rasterized substitute;
- lower-fidelity template/route.

Unexpected fallback font remains a canonical render/G5 failure even if compilation exits zero.

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

Full teaching-route G1 cannot be claimed until the final canonical course-standard source has been integrated.

### G5

For each built-in template, G5 remains two non-compensating evidence streams:

1. actual canonical source consumption;
2. visual fidelity.

A PASS in one cannot offset failure in the other.

For course-standard 4:3:
- compare the final integrated canonical source output against exact private Chapter1 reference/default identity;
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

Full course-standard G5 cannot be claimed until the final canonical source is integrated.

### private G5 evidence path

The approved non-paid private pixel evidence owner remains:

\`PRESENTATIONS_LONG_TERM_PLANNER_CHAT_PRIVATE_G5_EVIDENCE\`

Executor must eventually freeze one exact \`implementation_commit\` and generate:

\`results/presentations--stage1-front-door-two-template-foundation/g5_private_review/G5_REVIEW_INPUTS.json\`

Actual private review files remain under:

\`private/exports/presentations--stage1-front-door-two-template-foundation/g5-review-bundle/\`

The user-visible Presentations ChatGPT thread verifies hashes and directly inspects pixels, then writes metadata/findings only to:

\`results/presentations--stage1-front-door-two-template-foundation/g5_private_review/G5_PRIVATE_VISUAL_REVIEW.md\`

Scheduled GPT Reviewer remains the sole Reviewed Handoff implementation-review authority and must not claim direct access to private pixels it cannot access.

If evidence is missing/stale/mismatched at \`READY_FOR_GPT_REVIEW\`:
- leave CURRENT unchanged;
- write no \`REVIEW_<n>.md\`;
- consume no review round;
- wait on \`PRIVATE_G5_REVIEW_PENDING\`.

\`PRIVATE_G5_REVIEW_PENDING\` is not a CURRENT state.

### Reviewed Handoff / CI / release

Task flags remain:

\`\`\`text
ci_required = true
visual_review_required = false
text_review_required = false
paid review = NOT AUTHORIZED
\`\`\`

Bridge Kit 0.9.3+ bounded first-publication path remains required.
No raw first push.

Release boundary remains:

\`\`\`text
Repository bump decision = NONE
presentations = NO_BUMP
no production install/release
no main integration
no maturity promotion
\`\`\`

Stage 1 PASS does not authorize Stage 2.

## Positive completion

Stage 1 is complete only after the dependency sequence A -> B -> C below finishes on one final integrated candidate.

### A. CONTINUE_NOW

Executor must continue now with all approved Stage-1 work that does not require ownership of the final canonical course-standard template body.

This includes, when directly required by the approved package:

- unified Presentations front door;
- Marketplace/plugin routing;
- research / teaching / business intent routing infrastructure;
- editable PPTX/Slides route preservation;
- local-edit fast path;
- external locked template pass-through;
- plan-only route;
- exactly-two-template registry/identity infrastructure while the course-standard canonical source locator remains unresolved;
- presentation-desktop consistency;
- source/generated authority cleanup;
- canonical generator parity;
- \`render-chinese-math-pdf\` owner integration;
- removal of reusable Presentations host-path assumptions:
  \`/home/yuukias\`, \`/overflow\`, \`/users\`, private TinyTeX/TeXLive/font/resource hardcodes;
- CUHK adapter integration with the render owner;
- typed \`blocked_missing_dependency\`;
- forbidden fallback/font QA;
- RP-G2;
- RP-G3;
- RP-G4;
- RP-G1/RP-G5 infrastructure that does not depend on the final course-standard source;
- \`G5_REVIEW_INPUTS\` / private review bundle / evidence plumbing;
- routing tests;
- Marketplace/generator tests;
- source/generated parity tests;
- broad/risk-matched tests that do not require final course-standard pixels;
- other already-approved Stage-1 implementation that does not require the final canonical course-standard source.

The dependency must not be used as a reason to stop these workstreams.

### B. WAIT_FOR_CANONICAL_COURSE_STANDARD

Only the following remain pending on the independent canonical standard-Beamer task:

- exact canonical course-standard source path;
- exact candidate commit;
- allowed consumption boundary;
- canonical source identity;
- final 4:3 source;
- final 16:9 same-template behavior;
- canonical #49 opening/navigation/bookmark/footline/closing primitives;
- course-standard template-specific compile/render;
- course-standard template-specific fidelity evidence.

Dependency label:

\`WAITING_FOR_CANONICAL_COURSE_STANDARD_TEMPLATE\`

This wait does not authorize a second template implementation and does not stop A.

### C. FINAL_INTEGRATION

After the independent task supplies exact source path + exact commit + allowed consumption boundary, this task must:

1. consume/integrate that exact canonical course-standard adapter/source;
2. complete teaching default 4:3;
3. complete teaching explicit 16:9;
4. complete RP-G1/RP-G5 final two-adapter evidence;
5. run course-standard structural/navigation checks;
6. run full G1, including teaching routes;
7. generate the complete G5 private review bundle;
8. run final broad regression on the final integrated candidate;
9. freeze one exact \`implementation_commit\`;
10. enter \`WAITING_FOR_CI\`;
11. obtain real GitHub CI PASS;
12. obtain private G5 direct-pixel evidence;
13. proceed to Scheduled GPT implementation review.

Maximum supported completion claim remains:

> The exact final integrated Stage 1 candidate implements and validates the unified Presentations front door/routing and two-template adapter foundation, including #49, portable render-environment ownership, and the approved hash-bound private G5 visual evidence path, under G1/G5 with required CI.

A partial A-only candidate cannot claim Stage 1 PASS.

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
18. G5 source consumption and visual fidelity remain non-compensating;
19. private G5 evidence cannot be replaced by OCR/text summary, Executor self-review, or unapproved paid review;
20. Scheduled GPT Reviewer cannot claim it directly saw private pixels it cannot access;
21. Bridge 0.9.3+ bounded first-publication path cannot be replaced by raw first push;
22. \`ci_required=true\` cannot be removed;
23. \`visual_review_required=false\`, \`text_review_required=false\`, paid review remains unauthorized;
24. Stage 2–6 cannot enter this task;
25. no release/version bump/main integration/maturity promotion;
26. the independent canonical standard-Beamer task is the sole owner of the final canonical course-standard template body;
27. this task must not create/promote/restore a second canonical course-standard template body;
28. previously temporary course-standard source cannot become authority;
29. \`WAITING_FOR_CANONICAL_COURSE_STANDARD_TEMPLATE\` is a scoped dependency wait, not a reason to stop independent A work;
30. final Stage 1 PASS/G1/G5 must bind the exact final canonical course-standard source path + commit + allowed consumption boundary supplied by the owner task.

If implementation requires changing any item above, return \`NEEDS_GPT_PLANNER\`.

## Implementation scope

### A. CONTINUE_NOW scope

Allowed now, when directly required:

- \`scripts/codex_marketplace_config.json\` Presentations interface/routing;
- \`skills/tools/documents-media/presentations/research-presentations/SKILL.md\`;
- \`skills/tools/documents-media/presentations/business-presentations/SKILL.md\`;
- \`skills/tools/documents-media/presentations/shared/template-routing.md\`;
- \`skills/tools/documents-media/presentations/shared/ppt-skill-routing.md\`;
- \`profiles/presentation-desktop.json\`;
- canonical CUHK adapter/template source only for approved adapter/portable-render integration;
- Presentations shared render/adapter scripts required to remove host-specific environment ownership;
- routing/template registry infrastructure that can hold unresolved course-standard source identity without inventing a replacement body;
- directly relevant Presentations/Marketplace tests;
- task-local tracked evidence/results;
- task-owned private evidence plumbing/bundle structure;
- generated layers rebuilt only through the canonical generator.

Generated layers such as:

- \`plugins/codex/plugins/**\`;
- \`.agents/plugins/marketplace.json\`;
- other generator-owned mirrors

must not be hand-edited.

### B. Deferred source ownership

Until the canonical standard-Beamer owner supplies exact path/commit/boundary, this task must not create or edit a replacement canonical course-standard body.

Any temporary/experimental course-standard source previously created by this task remains non-authoritative and must not be promoted into normal runtime.

### C. FINAL_INTEGRATION scope

Once exact canonical source path + commit + allowed consumption boundary are supplied, this task may perform only the adapter/integration work necessary to consume that source within the already-approved Stage-1 architecture.

Do not redesign the imported template, fork it into a second canonical source, or silently vendor a divergent copy outside the allowed boundary.

\`render-chinese-math-pdf\` production semantics remain out of scope; reuse its current resolver/probe/environment contract. If that support skill itself needs semantic change, stop with \`NEEDS_GPT_PLANNER\`.

No new top-level plugin/skill, third template, universal IR/schema, resource registry, workflow/state machine, or Bridge Kit change is allowed.

## Acceptance and regression gates

### A-phase gates that may complete before the dependency arrives

The Executor should continue and may record partial PASS evidence for all gates/regressions that do not require final course-standard pixels/source identity, including:

- routing infrastructure behavior that does not require rendering course-standard;
- editable/business/local-edit/external-template/plan-only preservation;
- exactly-two-template registry/identity infrastructure with course-standard source unresolved;
- source/generated authority and generator parity;
- CUHK render-owner integration;
- RP-G2 forbidden reusable host-path scan;
- RP-G3 typed missing dependency;
- RP-G4 fallback-font rejection;
- RP-G1 infrastructure and any valid non-course-standard/root-resolution evidence;
- RP-G5 infrastructure and CUHK-side owner evidence;
- G5 private evidence plumbing/manifest/bundle mechanics independent of final course-standard files;
- targeted routing tests;
- Marketplace/generator/source-generated parity tests;
- broad/risk-matched tests not requiring final course-standard source/pixels.

A-phase evidence is partial task evidence only. It cannot produce overall Stage 1 PASS.

### Dependency gate

Before final integration, require all of:

\`\`\`text
CANONICAL_COURSE_STANDARD_SOURCE_PATH = known
CANONICAL_COURSE_STANDARD_COMMIT = known
CANONICAL_COURSE_STANDARD_CONSUMPTION_BOUNDARY = known
CANONICAL_COURSE_STANDARD_IDENTITY = verified
\`\`\`

If these are not yet available after A work is exhausted, record:

\`WAITING_FOR_CANONICAL_COURSE_STANDARD_TEMPLATE\`

without inventing a replacement source.

### Final G1

G1 must ultimately use the exact final integrated candidate installed in a fresh supported runtime and natural user requests.

Required route families remain:

- research no-format;
- teaching default 4:3;
- teaching explicit 16:9;
- business/executive no-format;
- explicit editable;
- existing-deck revision route;
- local edit;
- external locked template;
- plan-only.

Teaching route G1 is deferred until the canonical course-standard source is integrated.

Beamer routes must produce real source -> PDF -> render through the portable render-owner contract.

Editable routes require the real supported official editable surface.

### Final G5

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

Course-standard G5 is deferred until final canonical source integration.

### RP-G1 — two configured resource roots

Final RP-G1 requires the same unmodified final integrated Presentations source to resolve/render through two different valid configured resource roots.

Before course-standard integration, Executor may complete infrastructure/root-resolution work and CUHK-side evidence, but final RP-G1 evidence must bind the final integrated candidate.

### RP-G2 — forbidden reusable host-path scan

Scan reusable:
- \`skills/tools/documents-media/presentations/**\`;
- generated \`plugins/codex/plugins/presentations/**\`.

Fail if private host render/font/TeX paths remain in reusable payload.

Historical results/audits are not reusable runtime and do not need rewriting.

RP-G2 may complete in A and must be rerun on the final integrated candidate.

### RP-G3 — typed missing dependency

Controlled missing required dependency must produce:
- \`blocked_missing_dependency\`;
- exact missing item;
- no substitute PASS artifact.

RP-G3 may complete in A and must remain valid after final integration.

### RP-G4 — fallback-font rejection

A candidate PDF using an unexpected font outside the template-approved font contract must fail canonical render/G5 QA even if compile exit code is zero.

RP-G4 may complete in A and must remain valid after final integration.

### RP-G5 — shared render owner

Final build manifests for CUHK and course-standard must both record:
- \`render-chinese-math-pdf\` as environment owner;
- resolved route/profile identity.

CUHK-side and shared infrastructure evidence may complete in A. Final two-adapter RP-G5 awaits canonical course-standard integration.

### Broad regression / repository validation

Run current canonical equivalents of:

- targeted Presentations tests;
- Marketplace generator write/validate/check/path-report;
- source/generated parity;
- skills validation;
- broad/risk-matched repository tests;
- Reviewed Handoff validation;
- \`git diff --check\`.

During A, run the subset not requiring final course-standard source/pixels.

After C integration, run the full final candidate suite, including:
- course-standard 4:3 and 16:9 compile/render probes;
- opening/navigation/bookmark/footline/closing structural checks;
- final RP-G1/RP-G5 two-adapter evidence;
- complete G1;
- complete G5 bundle;
- final broad regression.

Then enter:
\`WAITING_FOR_CI / ci_status=PENDING\`
for real GitHub CI.

Mechanical tests/CI do not replace G1/G5.

### Private G5 evidence acceptance

Final integrated candidate must generate:

\`results/presentations--stage1-front-door-two-template-foundation/g5_private_review/G5_REVIEW_INPUTS.json\`

bound to exact final \`implementation_commit\`, including the final canonical course-standard source identity.

Actual files remain in:

\`private/exports/presentations--stage1-front-door-two-template-foundation/g5-review-bundle/\`

Direct-pixel evidence is produced through the approved user-visible ChatGPT file-upload review surface and recorded metadata-only in:

\`results/presentations--stage1-front-door-two-template-foundation/g5_private_review/G5_PRIVATE_VISUAL_REVIEW.md\`

Scheduled GPT Reviewer consumes the evidence but does not claim inaccessible direct-pixel access.

Missing/stale/mismatched evidence:
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
- \`WAITING_FOR_CANONICAL_COURSE_STANDARD_TEMPLATE\` as scoped dependency wait;
- \`PRIVATE_G5_REVIEW_PENDING\` as nonterminal evidence wait;
- \`BLOCKED_PRIVATE_G5_REVIEW_ACCESS\`;
- \`NEEDS_GPT_PLANNER\`.

No lower-fidelity fallback is allowed.

## Natural-language usage / routing expectations

Representative user requests and expected final behavior remain:

- “把这篇论文做成组会汇报，没特别格式要求。”
  -> Presentations intake -> research route -> \`cuhk-research\` Beamer.

- “把明天 Tutorial 做成课件。”
  -> Presentations intake -> teaching route -> final canonical \`course-standard\` 4:3 by default.

- “这个 Tutorial 要 16:9。”
  -> Presentations intake -> same final canonical \`course-standard\` template with explicit 16:9 ratio.

- “做一套给管理层的产品策略汇报。”
  -> Presentations intake -> editable PPTX/Slides route.

- “把这个现有 PPT 第 6 页标题改短一点。”
  -> Presentations intake -> \`local-edit\` fast path -> preserve current format/template/ratio.

- “按这个会议官方模板做。”
  -> external locked template pass-through.

- “只先给我逐页 storyline，不生成 PPT。”
  -> plan-only; no artifact-completion claim.

During A, routing infrastructure may recognize teaching/course-standard intent, but the task must not claim the teaching artifact path is fully operational until the canonical course-standard source is integrated.

For formal Beamer routes, users never need machine-local TeX/font/resource paths; those remain resolved through \`render-chinese-math-pdf\`.

For private G5 fidelity, the user-visible handoff remains explicit after the final integrated candidate is frozen.

## Out of scope

Do not implement or treat as blockers for this Stage 1:

- redesign of Presentations architecture;
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
- a second canonical course-standard template body;
- promotion of any prior temporary course-standard source into authority;
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
- modification of the independent canonical standard-Beamer task;
- modification of STAT5060 project content.

Reviewer must judge the final integrated Stage 1 v1.3 scope and respect the A/B/C dependency sequence above.
