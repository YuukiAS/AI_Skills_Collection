# Planner Validation — Presentations Stage 1 Execution Package v1.2

**Date:** 2026-09-29  
**Task key:** \`presentations--stage1-front-door-two-template-foundation\`  
**Planner status:** READY FOR INDEPENDENT EXECUTION-READY CRITIC REVIEW

## 1. Validation summary

\`\`\`text
PLAN_REVISION_STATUS = COMPLETE
STAGE1_PLAN_VERSION = 1.2

BRIDGE_KIT_VERSION = 0.9.3
OLD_BRIDGE_BLOCKER_STATUS = CLOSED

COURSE_STANDARD_49_STATUS = PROMOTE_NOW_IN_STAGE1
DEFERRED_50_53_STATUS = DEFERRED_UNCHANGED

ASPECT_RATIO_POLICY =
COURSE_STANDARD_DEFAULT_4_3_EXPLICIT_16_9_SAME_TEMPLATE_VARIANT

CI_REQUIRED = YES
BRIDGE_VISUAL_REVIEW_REQUIRED = NO
G5_INDEPENDENT_PIXEL_REVIEW_REQUIRED = YES

REPOSITORY_BUMP_DECISION = NONE
PRESENTATIONS_PLUGIN_BUMP = NO_BUMP
MAIN_INTEGRATION_AUTHORIZED = NO

READY_FOR_EXECUTION_READY_CRITIC = YES
READY_FOR_CODEX = NO
\`\`\`

## 2. Current package

Plan:

\`docs/design/PRESENTATIONS_STAGE1_FRONT_DOOR_TWO_TEMPLATE_EXECUTION_PLAN_V1_2_2026-09-29.md\`
first commit \`63f854ca095a6d9b8353ac803ff13c2f4cbc7f92\`

Goal:

\`docs/goals/PRESENTATIONS_STAGE1_FRONT_DOOR_TWO_TEMPLATE_GOAL_V1_2.md\`
first commit \`56ac9e9dbb3923957a58b3154d290448b4d68f06\`

Kickoff:

\`docs/operations/prompts/PRESENTATIONS_STAGE1_FRONT_DOOR_TWO_TEMPLATE_KICKOFF_V1_2.md\`
first commit \`718a45118e23e0a3c5801574801ce7e515c1f127\`

Manifest:

\`results/presentations--stage1-front-door-two-template-foundation/EXECUTION_PACKAGE_V1_2.md\`
first commit \`6fe1b561bcebec7f9a6f677bb6ce3b26b91e6ca1\`

## 3. #49 promotion check

Canonical source:

\`docs/plugin-todos/presentations.md\`

Planner changed only #49 from:

\`NEW -> PROMOTE_NOW\`

at:

\`e6d4058e2716583012ffda5f310a8aadfce819df\`

Reason:
- real STAT5060 course-standard deck exposed that visual colours/bands alone do not define a usable teaching template;
- the minimum generic remedy is owned by Stage 1 template adapter foundation;
- it does not require semantic storyline/composition intelligence.

#50–#53 were not promoted.

No STAT5060-specific page/example/HW/content rule was added.

## 4. Bridge Kit check

Current Bridge repository formal release state was re-read.

Verified:
- \`pyproject.toml = 0.9.3\`;
- \`ai_bridge_kit.__version__ = 0.9.3\`;
- formal release target =
  \`9dad0ba4bfa54e251f345091c5151ae991251ec9\`;
- formal release closure records \`FORMAL_DISTRIBUTION_COMPLETE=YES\`;
- current CLI source exposes:
  \`ai-bridge reviewed-handoff task publish-first --task-key ... --expected-repo ...\`;
- Machine Policy contains a bounded allow entry for that exact command family;
- current README documents the same production entry;
- fresh real-consumer evidence exists in Bridge results.

Therefore the historical first-remote-publication capability blocker is closed at product/release level.

The v1.2 package does not claim every execution machine is updated. It adds an execution preflight and uses \`BLOCKED_BRIDGE_RUNTIME_STALE\` if the local runtime is not compatible.

No raw Git/manual fallback remains.

## 5. Bridge chronology check

v1.2 uses current 0.9.3 sequence:

\`\`\`text
bootstrap --ci-required
-> PLAN_REQUESTED / RUN_GPT_PLANNER
-> commit only first REQUEST/CURRENT
-> reviewed-handoff task publish-first
-> external Planner task-local PLAN V2
-> PLAN_FROZEN / RUN_CODEX_EXECUTOR
-> implementation
-> WAITING_FOR_CI / PENDING
-> real GitHub CI
-> implementation review
\`\`\`

Historical \`UPSTREAM_REMOTE_MISMATCH\` workaround wording is removed from the active package.

## 6. Course-standard structural check

v1.2 now freezes both:

A. visual identity:
- black top band;
- blue frame-title;
- white body;
- restrained academic style;
- ordinary blue bullets;
- sparse teaching hierarchy;
- lower-right page number;
- sans body + compatible math;
- no annotations;
- no CUHK branding.

B. structural identity:
- title/opening frame;
- section-aware state/navigation;
- PDF outline/bookmarks;
- nonintrusive top navigation where appropriate;
- bottom navigation/action affordances where appropriate;
- stable footline/page number;
- distinct title/content/section-aware/closing states;
- closing-frame primitive.

The closing-frame **semantic choice** remains deferred to #53.

## 7. Aspect-ratio check

Frozen behavior:

\`\`\`text
new course-standard, no ratio -> 4:3
explicit teaching 16:9 -> course-standard 16:9
existing/local edit -> preserve ratio
external locked template -> preserve locked ratio
\`\`\`

No third template is introduced.

G5 distinguishes:
- exact/default 4:3 reference fidelity;
- 16:9 invariant-identity fidelity + ratio correctness.

Expected ratio-driven spacing differences are not treated as template-fidelity failures.

## 8. Beamer reality check

Targeted official-source recheck:
- Beamer remains version 3.78 (2026-08-20);
- Beamer appearance is template/theme driven;
- the class supports explicit \`aspectratio\` settings, including wide ratios;
- Beamer contains navigation infrastructure;
- the PDF stack uses Hyperref, whose section commands feed PDF outline/bookmark structure.

References:
- https://ctan.org/pkg/beamer
- https://tug.ctan.org/macros/latex/contrib/beamer/doc/beameruserguide.pdf
- https://tug.ctan.org/macros/latex/contrib/hyperref/doc/paper.pdf

No new renderer or third-party theme dependency is required for this amendment.

## 9. Deferred-scope check

Confirmed absent from v1.2 implementation scope:
- #50 presenter-learning companion;
- #51 lecture/source cross-reference;
- #52 assessment semantics / answer leakage;
- #53 closing semantic choice;
- simulation explanation framework;
- natural-language rewrite framework;
- semantic table/list/paragraph selection;
- full responsive-layout intelligence;
- Stage 2–6 capabilities;
- STAT5060-specific repairs.

## 10. Existing architecture regression check

Still exactly two built-in templates:
- \`cuhk-research\`;
- \`course-standard\`.

Preserved:
- editable business/PPTX route;
- external locked template route;
- local-edit fast path;
- source/generated authority;
- Chapter1 private reference;
- no third template;
- no new top-level skill/plugin/schema/state machine;
- no architecture rewrite;
- no Stage 2–6 implementation.

## 11. CI / visual-review distinction

Current Reviewed task must use \`--ci-required\`.

Do not use \`--visual-review-required\` or \`--text-review-required\`.

This does not weaken visual acceptance:
- G5 independent pixel-level review is still mandatory;
- Reviewer must directly access candidate renders + exact Chapter1;
- OCR/text summaries cannot substitute for visual inspection.

No paid OpenAI/Terra review is authorized in Stage 1.

## 12. Version/readme/release check

This turn changes planning/TODO source only.

\`\`\`text
Repository bump decision: NONE
Affected plugins:
- presentations: NO_BUMP
\`\`\`

README checked:
no update required for this planning-only amendment.

Plugin changelog checked:
no released behavior exists yet; no release entry required.

No production plugin code changed.
No generated plugin payload changed.
No main integration/release is authorized.

## 13. Maintenance Board pending mutation

Current surface has not performed reader-facing GitHub Project mutation because the required installed Clear Writing invocation is not available here.

Do not claim sync.

Exact pending mutation:

\`\`\`text
Project = AI Skills Maintenance
Area = presentations
Issues = #29-#53
Status = DOING

Current execution anchor =
results/presentations--stage1-front-door-two-template-foundation/EXECUTION_PACKAGE_V1_2.md
@ 6fe1b561bcebec7f9a6f677bb6ce3b26b91e6ca1

Next action =
independent execution-ready Critic review of Stage 1 package v1.2

Source truth:
#49 = PROMOTE_NOW
#50-#53 = NEW
all other issue maturity unchanged

Do not mark DONE/PROMOTED implementation-complete.
Do not close issues.
\`\`\`

## 14. Planner verdict

\`\`\`text
PLANNER_RESULT = READY_FOR_EXECUTION_READY_CRITIC
READY_FOR_EXECUTION_READY_CRITIC = YES
READY_FOR_CODEX = NO
NEXT_HANDOFF = CRITIC
\`\`\`
