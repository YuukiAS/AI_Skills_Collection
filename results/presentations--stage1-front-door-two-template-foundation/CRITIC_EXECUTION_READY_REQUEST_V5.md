# Execution-Ready Critic Review Request — Presentations Stage 1 v1.3

你是 AI Research Stack 的独立 Critic thread。

本轮不是重新设计 Presentations architecture。
只审：

\`Presentations Stage 1 execution package v1.3\`

是否关闭上一轮：

- \`PRES-S1-ER-F04\`
- \`PRES-S1-ER-F05\`

并检查这两处返修有没有引入新的直接回归。

不要实现代码。
不要创建 task/branch/worktree。
不要修改 production plugin。
不要运行 paid review。
不要发布。

## Active Review Context

\`\`\`text
target_repo = YuukiAS/AI_Skills_Collection

target_plugin_or_domain = presentations

design_topic_or_task_key =
presentations--stage1-front-door-two-template-foundation

review_stage =
stage1_execution_ready_review_v1_3

source_branch_or_ref = main

architecture_authority =
docs/design/PRESENTATIONS_TWO_TEMPLATE_PRODUCTION_REDESIGN_PLAN_V1_1_2026-09-28.md
@ f71e97c06938ab2ce175ccf3b4ac19da9309fda1

prior_package =
results/presentations--stage1-front-door-two-template-foundation/EXECUTION_PACKAGE_V1_2.md
@ 6fe1b561bcebec7f9a6f677bb6ce3b26b91e6ca1

prior_critic_review =
results/presentations--stage1-front-door-two-template-foundation/CRITIC_EXECUTION_READY_REVIEW_V4.md
@ faae612ea90aa1e7db948ae29837e699b8d13e25

stable_prior_blockers =
PRES-S1-ER-F01 = CLOSED
PRES-S1-ER-F02 = CLOSED
PRES-S1-ER-F03 = CLOSED

review_blockers =
PRES-S1-ER-F04
PRES-S1-ER-F05

stage1_plan =
docs/design/PRESENTATIONS_STAGE1_FRONT_DOOR_TWO_TEMPLATE_EXECUTION_PLAN_V1_3_2026-09-29.md
first_commit = a4ff0840fd57ca3d58bfd254526ebd8327b198bd

stage1_goal =
docs/goals/PRESENTATIONS_STAGE1_FRONT_DOOR_TWO_TEMPLATE_GOAL_V1_3.md
first_commit = ef7925588f5d65b15c44d84535327bc7648544ea

stage1_kickoff =
docs/operations/prompts/PRESENTATIONS_STAGE1_FRONT_DOOR_TWO_TEMPLATE_KICKOFF_V1_3.md
first_commit = 3421d6c1b53f523c01cd8bc7006f4e37cd37c0dc

planner_response =
results/presentations--stage1-front-door-two-template-foundation/PLANNER_RESPONSE_V1_3.md
@ 140c0c53c4ed6d7fd0ae8ad7386056ab47fcc17c

stage1_manifest =
results/presentations--stage1-front-door-two-template-foundation/EXECUTION_PACKAGE_V1_3.md
@ 5351f304381501f27833e5c7fa4f536ae5b684f8

planner_validation =
results/presentations--stage1-front-door-two-template-foundation/PLANNER_VALIDATION_V1_3.md
@ 23ec57e064306e6ec60fb9e113a8e52e9efbd7b1

execution_task = NOT_CREATED
execution_branch = NOT_CREATED
execution_worktree = NOT_CREATED
\`\`\`

## 1. Required reads

Read latest AI_Skills \`main\`:

- \`AGENTS.md\`
- \`docs/workflows/PLANNER_ROLE_CONTRACT.md\`
- \`docs/workflows/CRITIC_ROLE_CONTRACT.md\`
- \`docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md\`
- \`docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md\`
- \`docs/plugin-todos/presentations.md\`
- prior Critic v4
- complete v1.3 Plan
- complete v1.3 Goal
- complete v1.3 Kickoff
- v1.3 manifest
- Planner response
- Planner validation

For F04, directly inspect current:

- \`skills/tools/documents-media/presentations/shared/scripts/generate_cuhk_scientific_layout_stage3.py\`
- \`skills/tools/documents-media/presentations/shared/scripts/generate_research_presentation_production_entry.py\`
- \`skills/tools/documents-media/render-chinese-math-pdf/SKILL.md\`
- \`skills/tools/documents-media/render-chinese-math-pdf/references/portable-rendering.md\`
- relevant current Presentations tests/profile membership

For F05, directly inspect latest Bridge:

\`YuukiAS/GPT_Codex_AI_Bridge_Kit\`

at minimum:
- \`templates/reviewed_handoff/prompts/REVIEWER_SCHEDULED_TASK.md\`
- current Reviewed Handoff state semantics sufficient to verify a missing custom evidence artifact can remain a no-write wait
- current Bridge 0.9.3 first-publication interface only if needed to confirm preserved chronology

Do not use old chat memory as authority.

---

## 2. Review discipline

This is a REVISE follow-up.

First adjudicate:

\`\`\`text
PRES-S1-ER-F04 = CLOSED | STILL_OPEN
PRES-S1-ER-F05 = CLOSED | STILL_OPEN
\`\`\`

Only add a new blocker for:
- a new fact;
- a critical risk missed last round;
- a direct regression introduced by v1.3.

Do not reopen already passed:
- #49 Stage-1 template-foundation scope;
- #50–#53 deferral;
- 4:3/16:9 same-template semantics;
- exactly two built-in templates;
- research/business/local-edit routing;
- Bridge 0.9.3 F03 closure;
- CI chronology;
- NO_BUMP / NO_RELEASE / no main integration.

---

## 3. PRES-S1-ER-F04 — render portability

Prior requirement:

Reusable Presentations production source/generated payload must not hardcode one machine's render/font/TeX paths, and both Beamer adapters must defer environment/resource-resolution ownership to \`render-chinese-math-pdf\`.

### Verify owner boundary

v1.3 freezes:

\`render-chinese-math-pdf = sole environment/resource-resolution owner\`

Presentations owns:
- template selection;
- template-specific required font/package/resource declaration;
- source generation;
- fidelity criteria;
- adapter manifests.

Presentations does **not** own:
- private resource-root discovery;
- machine TinyTeX path;
- system font guessing;
- a second TeX/font environment resolver.

Judge whether this is the correct owner split.

### Verify forbidden-path contract

Reusable Presentations source/generated payload must contain no host-specific render dependency path such as:

- \`/home/yuukias\`
- \`/overflow\`
- \`/users\`
- private TinyTeX/TeXLive bin paths
- private font directories

Runtime evidence is allowed to record the resolved path actually used.

Check that v1.3 distinguishes reusable payload from historical results/evidence so it does not demand pointless rewriting of old artifacts.

### Verify render-owner consumption

v1.3 requires both Beamer adapters to consume the canonical render-skill probe/resolution contract, including current:

\`probe_pdf_render_env.py\`

or the same skill's canonical equivalent.

Check whether the Plan improperly leaves open an Executor-created second resolver.

The expected answer should be NO: cloning discovery into Presentations is forbidden.

### Verify missing dependency/fallback semantics

Required resource/package/font/compiler/QA dependency missing:

\`blocked_missing_dependency\`

must be typed and name the exact missing dependency.

Formal Stage 1 PASS cannot be obtained by:
- arbitrary system font;
- Times/fontconfig guess;
- Windows font mount guess;
- DejaVu/Liberation/Fandol substitute;
- Chromium;
- unrelated renderer;
- rasterized substitute;
- lower-fidelity template.

Check compatibility with \`render-chinese-math-pdf\`'s current venue/template font boundary: an explicit template may own its required font identity, while the render skill owns how that dependency is resolved and QA'd.

### Verify regression gates

v1.3 adds:

\`\`\`text
RP-G1 two different configured valid render roots, no source edit
RP-G2 no forbidden host path in reusable source/generated payload
RP-G3 missing required dependency -> typed block
RP-G4 unexpected fallback font -> gate fail
RP-G5 both adapters consume render-chinese-math-pdf owner
\`\`\`

Judge whether these directly close the prior portability false-PASS risk.

Do not require a redesign of \`render-chinese-math-pdf\` unless current source itself proves defective.

---

## 4. PRES-S1-ER-F05 — exact private Chapter1 reviewer access

Prior requirement:

G5 requires direct-pixel qualitative review of:
- exact private Chapter1;
- exact current candidate renders.

Scheduled GPT Reviewer is GitHub-only, so it cannot truthfully claim direct target-machine/private-file inspection.

v1.3 chooses one concrete non-paid evidence path.

### Review owner

Private G5 pixel evidence owner:

\`PRESENTATIONS_LONG_TERM_PLANNER_CHAT_PRIVATE_G5_EVIDENCE\`

Meaning:
- user-visible ChatGPT conversation/thread;
- direct file-upload + visual access;
- GitHub connector access;
- independent from Codex Executor;
- evidence producer only;
- not a new Reviewed Handoff role;
- not final implementation PASS authority.

Scheduled GPT Reviewer remains final implementation-review authority.

Judge whether this satisfies independence/authority without creating a second workflow/state machine.

### Review identity

Executor freezes exact \`implementation_commit\`, then writes:

\`results/presentations--stage1-front-door-two-template-foundation/g5_private_review/G5_REVIEW_INPUTS.json\`

with:
- implementation commit;
- expected Chapter1 SHA;
- template source identities;
- candidate PDF/contact-sheet hashes;
- render identities;
- render owner/profile.

Actual private files remain under:

\`private/exports/presentations--stage1-front-door-two-template-foundation/g5-review-bundle/\`

and are not pushed.

Judge whether this binding is sufficient to prevent reviewing stale/wrong candidate files without inventing Control-style hash machinery.

### Direct review path

The user uploads to the Presentations long-term Planner Chat:
- exact Chapter1;
- exact candidate render files;
- manifest when needed.

The thread:
- recomputes hashes;
- verifies them against frozen identities;
- directly sees pixels;
- issues only G5 private visual evidence.

It commits metadata/findings only:

\`results/presentations--stage1-front-door-two-template-foundation/g5_private_review/G5_PRIVATE_VISUAL_REVIEW.md\`

Required:
- task key;
- implementation commit;
- Chapter1 SHA;
- candidate hashes;
- render identities;
- direct private pixel access = YES;
- decision;
- findings;
- no private pixels.

Judge whether this is actually executable without paid Visual Review/Terra.

### Scheduled Reviewer consumption

Scheduled GPT Reviewer later:
- verifies evidence implementation commit == CURRENT implementation commit;
- verifies candidate hash identities;
- requires G5 private decision PASS;
- independently reviews source/diff/tests/CI;
- explicitly states it did not itself view inaccessible Chapter1 pixels.

It must not claim direct private visual access.

### Waiting semantics

If \`G5_PRIVATE_VISUAL_REVIEW.md\` is absent/stale/mismatched:

v1.3 requires:
- keep CURRENT at \`READY_FOR_GPT_REVIEW\`;
- no \`REVIEW_<n>.md\`;
- no review-round consumption;
- operational wait label \`PRIVATE_G5_REVIEW_PENDING\`.

Check current Scheduled GPT contract permits this kind of recoverable evidence wait/no-write behavior.

If the user-visible file review surface truly cannot access exact files after bounded retry:

\`BLOCKED_PRIVATE_G5_REVIEW_ACCESS\`

Recovery owner:
\`USER + GPT PLANNER\`

No paid-review/OCR/self-review fallback.

Judge whether this closes the deterministic dead-end identified in v1.2.

---

## 5. G1/G5 regression check

Do not reopen definitions unless v1.3 broke them.

G1 still:
- exact installed candidate;
- natural user prompts;
- real route/deliverable/template;
- real Beamer source/PDF/render;
- real official editable route.

G5 still:
- actual source consumption;
- visual fidelity;
- non-compensating.

Course-standard:
- 4:3 exact/default reference;
- 16:9 same-template invariant identity.

CUHK:
- exact canonical source identity.

Both Beamer routes now additionally must satisfy the portable render-owner contract.

---

## 6. Existing product decisions that must remain unchanged

Verify:

\`\`\`text
#49 = PROMOTE_NOW
#50-#53 = NEW/deferred

built-in templates =
cuhk-research
course-standard

course-standard:
default = 4:3
explicit 16:9 = same-template variant

business/editable route = unchanged
local-edit fast path = unchanged
external locked template = pass-through
existing/local ratio = preserved

Bridge = current 0.9.3 publish-first
ci_required = true
visual_review_required = false
text_review_required = false
paid review = not authorized

Repository bump = NONE
presentations = NO_BUMP
main integration = NO
release/install = NO
maturity promotion = NO
\`\`\`

---

## 7. Scope red-team

Actively look for accidental expansion:

- render portability change turning into redesign of render-chinese-math-pdf;
- new global resource registry;
- new render workflow/state machine;
- third template;
- Stage 2/3 composition work;
- #50–#53 implementation;
- paid review;
- committing private reference pixels;
- new Reviewer role/state in Reviewed Handoff;
- Control-style hash graph;
- Scheduled GPT claiming inaccessible visual review;
- user being forced into a second Git publication approval.

If none is present, do not invent one.

---

## 8. Maintenance Board

Source truth:

\`\`\`text
#49 = PROMOTE_NOW
#50-#53 = NEW
other maturity unchanged
\`\`\`

Project:
- Area = presentations
- Status = DOING
- Issues #29–#53

If the required Clear Writing / Project mutation surface is unavailable:
- do not claim Project sync;
- output exact pending mutation;
- do not ask the user to maintain it manually.

---

## 9. Blocker standard

Every blocker requires:
- frozen requirement;
- direct evidence;
- causal risk;
- minimum closure.

Do not REVISE for:
- style preference;
- more optional tests;
- ordinary implementation detail;
- Stage 2–6 absence;
- private evidence not existing yet before implementation;
- desire to automate the manual non-paid evidence path.

The execution package needs an executable path, not already-produced implementation evidence.

---

## 10. Expected output

First give a concise user-readable judgment.

Then:

\`\`\`text
PRES-S1-ER-F04 = CLOSED | STILL_OPEN
PRES-S1-ER-F05 = CLOSED | STILL_OPEN

RESULT = PASS | REVISE
REVIEW_STAGE = STAGE1_EXECUTION_READY_V1_3

REVIEWED_PACKAGE =
results/presentations--stage1-front-door-two-template-foundation/EXECUTION_PACKAGE_V1_3.md

REVIEWED_PACKAGE_COMMIT =
5351f304381501f27833e5c7fa4f536ae5b684f8

APPROVED_PLAN_PATH =
docs/design/PRESENTATIONS_STAGE1_FRONT_DOOR_TWO_TEMPLATE_EXECUTION_PLAN_V1_3_2026-09-29.md

APPROVED_GOAL_PATH =
docs/goals/PRESENTATIONS_STAGE1_FRONT_DOOR_TWO_TEMPLATE_GOAL_V1_3.md

APPROVED_KICKOFF_PATH =
docs/operations/prompts/PRESENTATIONS_STAGE1_FRONT_DOOR_TWO_TEMPLATE_KICKOFF_V1_3.md

PLANNER_RESPONSE =
results/presentations--stage1-front-door-two-template-foundation/PLANNER_RESPONSE_V1_3.md
@ 140c0c53c4ed6d7fd0ae8ad7386056ab47fcc17c

PLANNER_VALIDATION =
results/presentations--stage1-front-door-two-template-foundation/PLANNER_VALIDATION_V1_3.md
@ 23ec57e064306e6ec60fb9e113a8e52e9efbd7b1

RENDER_OWNER_VERDICT = ...
PORTABILITY_REGRESSION_VERDICT = ...
PRIVATE_G5_REVIEW_PATH_VERDICT = ...
SCHEDULED_REVIEWER_TRUTH_VERDICT = ...
G1_G5_REGRESSION_VERDICT = ...
SCOPE_REGRESSION_VERDICT = ...
RELEASE_BOUNDARY_VERDICT = ...

READY_FOR_CODEX = YES | NO
\`\`\`

### If REVISE

- use stable blocker IDs;
- do not modify Planner package yourself;
- only new fact/missed critical risk/direct v1.3 regression may add blocker;
- automatically return the full next Planner prompt.

### If PASS

Set:

\`\`\`text
PRES-S1-ER-F04 = CLOSED
PRES-S1-ER-F05 = CLOSED
READY_FOR_CODEX = YES
NEXT_HANDOFF = CODEX
\`\`\`

Then read:

\`docs/operations/prompts/PRESENTATIONS_STAGE1_FRONT_DOOR_TWO_TEMPLATE_KICKOFF_V1_3.md\`

and reproduce its exact reviewed contents verbatim:

\`\`\`text
=== APPROVED CODEX KICKOFF BEGIN ===
<verbatim v1.3 Kickoff>
=== APPROVED CODEX KICKOFF END ===
\`\`\`

Do not rewrite the Kickoff after PASS.

Critic PASS alone does not create task/branch/worktree or authorize implementation. Current-user authorization begins only when the user subsequently sends the exact approved Kickoff.
