# Canonical Goal — Presentations Stage 1 Front Door + Two-Template Foundation

**Goal version:** 1.3  
**Status:** DRAFT FOR EXECUTION-READY CRITIC REVIEW / NOT USER EXECUTION AUTHORIZATION  
**Task key:** \`presentations--stage1-front-door-two-template-foundation\`  
**Repository:** \`YuukiAS/AI_Skills_Collection\`

## 1. Authority

Architecture authority:

\`docs/design/PRESENTATIONS_TWO_TEMPLATE_PRODUCTION_REDESIGN_PLAN_V1_1_2026-09-28.md @ f71e97c06938ab2ce175ccf3b4ac19da9309fda1\`

Stage 1 execution Plan v1.3:

\`docs/design/PRESENTATIONS_STAGE1_FRONT_DOOR_TWO_TEMPLATE_EXECUTION_PLAN_V1_3_2026-09-29.md\`

Latest Critic revision basis:

\`results/presentations--stage1-front-door-two-template-foundation/CRITIC_EXECUTION_READY_REVIEW_V4.md @ faae612ea90aa1e7db948ae29837e699b8d13e25\`

Stable earlier blockers remain closed:

\`\`\`text
PRES-S1-ER-F01 = CLOSED
PRES-S1-ER-F02 = CLOSED
PRES-S1-ER-F03 = CLOSED
\`\`\`

This Goal changes v1.2 only to close F04/F05. It does not reopen architecture/routing/#49/ratio/release decisions.

---

## 2. Goal

Implement only Presentations Stage 1:

> unified Presentations front door + routing + local-edit fast path + exactly two built-in Beamer adapters, including #49 structural/ratio-aware course-standard, with portable render-environment ownership and an executable non-paid G5 private-reference review path.

Do not implement Stage 2–6 teaching/composition/writing intelligence.

---

## 3. Frozen routing

\`\`\`text
research/group meeting/seminar/paper talk/journal club/QE/oral/defense, no format
-> cuhk-research Beamer

Tutorial/lecture/teaching, no ratio
-> course-standard 4:3

teaching, explicit 16:9
-> same course-standard template 16:9

business/executive/product/strategy/client, no format
-> editable PPTX/Slides

explicit PPTX/Slides
-> official editable adapter

existing deck/local edit
-> preserve current format/template/ratio

external locked template
-> pass-through

plan-only
-> plan/notes only
\`\`\`

Exactly two built-in templates:
- \`cuhk-research\`
- \`course-standard\`

---

## 4. course-standard contract

Visual identity:
- black top band;
- blue frame-title band;
- white body;
- restrained academic Beamer;
- ordinary blue bullets;
- sparse teaching hierarchy;
- lower-right page number;
- sans body + compatible math;
- no highlight/annotation replication;
- no CUHK branding.

Structural identity:
- canonical opening/title frame;
- section-aware state/navigation;
- PDF outline/bookmarks;
- nonintrusive top navigation where appropriate;
- normal-Beamer bottom navigation/action affordances where appropriate;
- stable footline/page number;
- distinct title/content/section-aware/closing states;
- canonical closing-frame primitive.

Stage 1 does not choose recap/question/Q&A/thanks semantics.

Ratio:
- default/reference = 4:3;
- explicit 16:9 = same template variant;
- existing/local/locked ratio preserved.

#49 remains \`PROMOTE_NOW\`.
#50–#53 remain \`NEW\`.

---

## 5. Render portability contract — F04

For both Beamer adapters:

\`render-chinese-math-pdf\`

is the environment/resource-resolution owner.

Presentations may decide:
- template;
- required packages/files/fonts;
- source generation;
- template fidelity;
- template-local inputs.

Presentations must not decide machine-specific resource locations.

Reusable Presentations source/generated payload must not hardcode:
- \`/home/yuukias\`;
- \`/overflow\`;
- \`/users\`;
- private TinyTeX/TeXLive bin roots;
- private font/resource directories.

Runtime receipts may record the resolved absolute path actually used.

The adapters must consume the canonical render-skill resolver/probe and its environment contract for:
- compiler/resource root;
- TEXMF variables;
- writable cache;
- font discovery;
- PDF QA.

Required dependency absent:
- return \`blocked_missing_dependency\`;
- include exact missing dependency;
- no Chromium/system-font/unrelated renderer/lower-fidelity fallback.

Unexpected font fallback:
- canonical render gate fails.

Do not redesign \`render-chinese-math-pdf\` without new direct evidence of a defect.

---

## 6. Render portability acceptance

Required direct regression evidence:

\`\`\`text
RP-G1:
same source renders from two different valid configured resource roots without source edits

RP-G2:
reusable Presentations source/generated payload contains no forbidden host paths

RP-G3:
missing required font/package/resource -> typed blocked_missing_dependency

RP-G4:
unexpected fallback font -> canonical render/G5 failure

RP-G5:
both cuhk-research and course-standard record render-chinese-math-pdf as the resolved environment owner
\`\`\`

Formal Beamer PASS cannot be obtained via Chromium or an unrelated renderer.

---

## 7. Private Chapter1 contract

Exact private reference:

\`\`\`text
Chapter1.pdf
sha256 =
ed205507a6d2de320b77d47d41e55bb0b406aef48144bc2c55d3bbba8c77ddf7
pages = 50
\`\`\`

Do not commit/push Chapter1 or derived private page images.

Do not use OCR/text summary as a substitute for G5 pixel review.

---

## 8. G5 private visual evidence path — F05

### Owner

Private pixel evidence owner:

\`PRESENTATIONS_LONG_TERM_PLANNER_CHAT_PRIVATE_G5_EVIDENCE\`

This is the user-visible Presentations ChatGPT Planner thread with:
- file-upload access;
- direct visual access;
- GitHub connector access.

It is an evidence producer only. It does not issue the final implementation PASS.

The Scheduled GPT Reviewer remains the sole Reviewed Handoff implementation-review authority.

### Candidate binding

Executor freezes one exact \`implementation_commit\` and generates:

\`results/presentations--stage1-front-door-two-template-foundation/g5_private_review/G5_REVIEW_INPUTS.json\`

with:
- task key;
- implementation commit;
- Chapter1 expected SHA;
- template source hashes;
- candidate PDF/contact-sheet hashes;
- render identities;
- render owner/profile identity.

Actual review files are durably stored under:

\`private/exports/presentations--stage1-front-door-two-template-foundation/g5-review-bundle/\`

The bundle includes exact Chapter1 locator/file and exact candidate render files.

### Direct review

The user uploads to the Presentations long-term Planner Chat:
- exact Chapter1;
- exact candidate render PDFs/contact sheets;
- manifest when useful.

That thread must:
- recompute/verify file hashes;
- reject mismatched/stale files;
- directly inspect pixels;
- review course-standard 4:3 and 16:9;
- review CUHK candidate pixels when included;
- never rely on OCR summary alone.

### Durable verdict

The private evidence thread writes:

\`results/presentations--stage1-front-door-two-template-foundation/g5_private_review/G5_PRIVATE_VISUAL_REVIEW.md\`

with:
- schema \`PRESENTATIONS_G5_PRIVATE_VISUAL_REVIEW_V1\`;
- task key;
- implementation commit;
- review surface;
- direct_private_pixel_access = YES;
- Chapter1 SHA;
- candidate hashes;
- render identities;
- criteria;
- decision \`PASS | REVISE | BLOCKED_PRIVATE_G5_REVIEW_ACCESS\`;
- blocking findings;
- no private pixels.

### Scheduled Reviewer consumption

Scheduled GPT Reviewer:
- verifies artifact binds current \`implementation_commit\`;
- verifies candidate hashes/manifest;
- requires private G5 decision PASS to support G5 PASS;
- independently reviews source/diff/tests/CI;
- must explicitly state it consumed hash-bound private visual evidence and did **not** itself view inaccessible Chapter1 pixels.

Missing/stale artifact:
- CURRENT stays \`READY_FOR_GPT_REVIEW\`;
- no REVIEW round consumed;
- operational status is \`PRIVATE_G5_REVIEW_PENDING\`.

If the private surface is genuinely unavailable after bounded retry:

\`BLOCKED_PRIVATE_G5_REVIEW_ACCESS\`

Recovery owner:
\`USER + GPT PLANNER\`

No automatic paid Visual Review/Terra fallback.

---

## 9. G1

G1 remains installed natural-entry routing.

Beamer branches must use the portable render-owner contract and real source -> PDF -> render.

Explicit ratio checks:
- teaching default 4:3;
- teaching explicit 16:9.

Editable branches still require the real official editable adapter.

---

## 10. G5

For each built-in template:
1. actual canonical source consumption;
2. visual fidelity.

These are non-compensating.

course-standard 4:3:
- exact Chapter1 visual/default fidelity;
- structural/navigation fidelity.

course-standard 16:9:
- actual 16:9;
- same template identity;
- coherent navigation/footline/opening/closing;
- no clipping.

CUHK:
- exact canonical source/fidelity unchanged.

All Beamer G5 artifacts must also satisfy the portable render contract and font QA.

---

## 11. Reviewed Handoff / Bridge

Required Bridge:

\`\`\`text
0.9.3+ compatible
publish-first available
\`\`\`

Bootstrap:

\`\`\`bash
ai-bridge reviewed-handoff task bootstrap \
  --task-key presentations--stage1-front-door-two-template-foundation \
  --expected-repo YuukiAS/AI_Skills_Collection \
  --expected-base-commit <POST_SYNC_ORIGIN_MAIN_OID> \
  --objective "Implement approved Presentations Stage 1 v1.3 only." \
  --ci-required
\`\`\`

First REQUEST/CURRENT publication:

\`\`\`bash
ai-bridge reviewed-handoff task publish-first \
  --task-key presentations--stage1-front-door-two-template-foundation \
  --expected-repo YuukiAS/AI_Skills_Collection
\`\`\`

Then external Planner writes task-local \`AI_BRIDGE_REVIEWED_PLAN_V2\` and freezes:

\`\`\`text
PLAN_REQUESTED -> PLAN_FROZEN
next_action = RUN_CODEX_EXECUTOR
plan_revision = 0
\`\`\`

No raw first push.

---

## 12. CI / review flags

\`\`\`text
ci_required = true
visual_review_required = false
text_review_required = false
paid review = NOT AUTHORIZED
\`\`\`

Real GitHub CI required.

G5 private visual review is still required through §8.

---

## 13. Strict out of scope

Do not:
- implement Stage 2–6;
- implement #50–#53;
- create third template;
- create new plugin/skill/schema/state machine;
- redesign render-chinese-math-pdf;
- modify Bridge Kit;
- enable paid visual/text review;
- bump versions;
- install/release Presentations;
- integrate main;
- modify STAT5060 repo.

---

## 14. Stop conditions

Use:
- \`BLOCKED_BRIDGE_RUNTIME_STALE\`;
- \`BLOCKED_REVIEWED_FIRST_BOOTSTRAP\`;
- \`BLOCKED_FIRST_PUBLICATION\`;
- \`BLOCKED_PLANNER_FREEZE\`;
- \`BLOCKED_CI_STATE\`;
- \`BLOCKED_DISCOVERY_CONSUMER\`;
- \`BLOCKED_REFERENCE_UNAVAILABLE\`;
- \`BLOCKED_REAL_EDITABLE_ADAPTER_SURFACE\`;
- \`BLOCKED_RENDER_ENVIRONMENT\`;
- \`blocked_missing_dependency\`;
- \`BLOCKED_UNEXPECTED_FONT_FALLBACK\`;
- \`BLOCKED_GENERATOR_ARCHITECTURE\`;
- \`PRIVATE_G5_REVIEW_PENDING\` as nonterminal evidence wait;
- \`BLOCKED_PRIVATE_G5_REVIEW_ACCESS\`;
- \`NEEDS_GPT_PLANNER\`.

No lower-fidelity fallback.

---

## 15. Version / release boundary

\`\`\`text
Repository bump decision = NONE
presentations = NO_BUMP
\`\`\`

No release/install.
No main integration.
No maturity promotion.

---

## 16. Maximum completion claim

Stage 1 implementation Reviewer PASS may claim only:

> the exact Stage 1 candidate implements and validates the unified front door/routing and two-template adapter foundation, including #49, portable render-environment ownership, and the hash-bound private G5 visual evidence path, under G1/G5 with required CI.

Until execution-ready Critic approves v1.3 and the user sends the exact approved Kickoff:

\`READY_FOR_CODEX = NO\`
