# Planner Validation — Presentations Stage 1 Execution Package v1.3

**Date:** 2026-09-29  
**Task key:** \`presentations--stage1-front-door-two-template-foundation\`  
**Planner status:** READY FOR INDEPENDENT EXECUTION-READY CRITIC REVIEW

## 1. Validation summary

\`\`\`text
PLAN_REVISION_STATUS = COMPLETE
STAGE1_PLAN_VERSION = 1.3

PRES-S1-ER-F01 = CLOSED
PRES-S1-ER-F02 = CLOSED
PRES-S1-ER-F03 = CLOSED
PRES-S1-ER-F04 = ACCEPTED_IN_V1_3
PRES-S1-ER-F05 = ACCEPTED_IN_V1_3

RENDER_ENV_OWNER = render-chinese-math-pdf
HOST_ABSOLUTE_PATH_IN_REUSABLE_PRESENTATIONS_PAYLOAD = FORBIDDEN
MISSING_DEPENDENCY_POLICY = FAIL_CLOSED_TYPED
UNEXPECTED_FONT_FALLBACK = GATE_FAIL

PRIVATE_G5_REVIEW_OWNER =
PRESENTATIONS_LONG_TERM_PLANNER_CHAT_PRIVATE_G5_EVIDENCE

SCHEDULED_GPT_PRIVATE_PIXEL_CLAIM = FORBIDDEN
PAID_VISUAL_REVIEW = NOT_AUTHORIZED

CI_REQUIRED = YES
BRIDGE_VISUAL_REVIEW_REQUIRED = NO
BRIDGE_TEXT_REVIEW_REQUIRED = NO

REPOSITORY_BUMP_DECISION = NONE
PRESENTATIONS_PLUGIN_BUMP = NO_BUMP
MAIN_INTEGRATION_AUTHORIZED = NO

READY_FOR_EXECUTION_READY_CRITIC = YES
READY_FOR_CODEX = NO
\`\`\`

## 2. Same-version package

Plan:

\`docs/design/PRESENTATIONS_STAGE1_FRONT_DOOR_TWO_TEMPLATE_EXECUTION_PLAN_V1_3_2026-09-29.md\`
first commit:
\`a4ff0840fd57ca3d58bfd254526ebd8327b198bd\`

Goal:

\`docs/goals/PRESENTATIONS_STAGE1_FRONT_DOOR_TWO_TEMPLATE_GOAL_V1_3.md\`
first commit:
\`ef7925588f5d65b15c44d84535327bc7648544ea\`

Kickoff:

\`docs/operations/prompts/PRESENTATIONS_STAGE1_FRONT_DOOR_TWO_TEMPLATE_KICKOFF_V1_3.md\`
first commit:
\`3421d6c1b53f523c01cd8bc7006f4e37cd37c0dc\`

Planner response:

\`results/presentations--stage1-front-door-two-template-foundation/PLANNER_RESPONSE_V1_3.md\`
first commit:
\`140c0c53c4ed6d7fd0ae8ad7386056ab47fcc17c\`

Manifest:

\`results/presentations--stage1-front-door-two-template-foundation/EXECUTION_PACKAGE_V1_3.md\`
@ \`5351f304381501f27833e5c7fa4f536ae5b684f8\`

## 3. F04 source/reality check

Direct current source was re-read.

Presentations currently has host-specific reusable constants in:

\`skills/tools/documents-media/presentations/shared/scripts/generate_cuhk_scientific_layout_stage3.py\`

including private \`/home/yuukias\` resource/TinyTeX paths.

The normal production entry imports and consumes that module.

The current \`render-chinese-math-pdf\` source was also re-read and already provides:
- explicit/project/env/namespace/home/ancestor resource-root resolution;
- host-specific local override boundary;
- \`blocked_missing_dependency\`;
- no automatic Chromium fallback;
- bundle-local font policy;
- PDF/font/text/layout QA;
- direct-TeX route using the same TEXMF/cache/resource strategy.

Conclusion:

\`F04_OWNER_ATTRIBUTION = PRESENTATIONS_INTEGRATION_DEFECT\`

No render-skill redesign is required by current evidence.

## 4. F04 contract self-check

v1.3 freezes all Critic minimum closure conditions:

1. no private host render/font/TeX absolute path in reusable Presentations source/generated payload;
2. both Beamer adapters consume \`render-chinese-math-pdf\` as environment owner;
3. Presentations may declare template-specific dependencies but not machine location;
4. missing dependency fails closed;
5. Chromium/system-font/lower-fidelity substitution cannot PASS;
6. RP-G1–RP-G5 cover two roots, forbidden path scan, missing dependency, fallback font, both-adapter ownership.

Historical results may contain old absolute paths as historical evidence; they are not reusable production payload and are not rewritten.

## 5. F05 source/reality check

Current Bridge Scheduled Reviewer prompt was re-read.

It explicitly states:

> Scheduled GPT 的真实执行面是 GitHub connector，不是目标机器 shell。

Therefore a server-local unpushed \`Chapter1.pdf\` is not directly visible to the Scheduled GPT Reviewer.

v1.3 no longer says the Scheduled Reviewer must directly view that private file.

## 6. F05 executable path self-check

Concrete path now frozen:

1. Executor freezes exact \`implementation_commit\`.
2. Executor generates candidate renders and \`G5_REVIEW_INPUTS.json\` with hashes/render identities.
3. Actual files are retained in canonical \`private/exports/.../g5-review-bundle/\`.
4. User uploads exact Chapter1 + candidate render files to the user-visible Presentations long-term Planner ChatGPT thread.
5. That thread has direct file/pixel access, verifies hashes and performs qualitative G5 review.
6. It writes only metadata/findings to \`G5_PRIVATE_VISUAL_REVIEW.md\` on the reviewed branch.
7. Scheduled GPT Reviewer verifies commit/hash binding and consumes that evidence.
8. Scheduled GPT explicitly does not claim direct private-pixel access.
9. Missing evidence is a no-write/no-review-round \`PRIVATE_G5_REVIEW_PENDING\` wait.
10. Actual review-surface access failure is \`BLOCKED_PRIVATE_G5_REVIEW_ACCESS\`, recovery owner USER + GPT PLANNER.

No new CURRENT state is introduced.
No new Reviewed role is introduced.
No paid review is enabled.

## 7. Candidate identity integrity

The private review evidence binds:
- task key;
- exact implementation commit;
- exact Chapter1 SHA;
- exact template-source identity;
- exact candidate PDF/contact-sheet SHA;
- render identity/owner/profile.

Any implementation change invalidates the evidence unless all identities are regenerated and re-reviewed.

Evidence/control commits after \`implementation_commit\` do not redefine implementation source identity.

## 8. Preserved decisions

Still:
- exactly two built-in templates;
- #49 = PROMOTE_NOW;
- #50–#53 = NEW/deferred;
- course-standard default 4:3;
- explicit 16:9 = same-template variant;
- existing/local/locked ratio preserved;
- research -> CUHK;
- teaching -> course-standard;
- business/explicit editable route preserved;
- local-edit fast path;
- external locked template pass-through;
- G5 consumption vs visual fidelity non-compensating;
- Bridge 0.9.3 \`publish-first\`;
- CI required;
- automated visual/text review flags false;
- NO_BUMP / NO_RELEASE / no main integration.

## 9. Stop/recovery check

v1.3 adds specific fail-closed outcomes for:
- stale Bridge runtime;
- render environment failure;
- typed missing dependency;
- unexpected font fallback;
- private G5 review pending/access failure.

No raw Git, lower-fidelity render, OCR-only visual substitute, Executor self-review or paid-review fallback is allowed.

## 10. Version / README / generated boundary

Planning-only revision:

\`\`\`text
Repository bump decision = NONE
presentations = NO_BUMP
\`\`\`

README checked:
no update required for planning-only v1.3.

Plugin changelog checked:
no released behavior yet; no release entry.

No production plugin source/generated payload has been modified in this Planner turn.

## 11. Maintenance Board pending mutation

Current surface has not performed reader-facing Project mutation because the required installed Clear Writing invocation is not available here.

Do not claim sync.

Exact pending mutation:

\`\`\`text
Project = AI Skills Maintenance
Area = presentations
Issues = #29-#53
Status = DOING

Current execution anchor =
results/presentations--stage1-front-door-two-template-foundation/EXECUTION_PACKAGE_V1_3.md
@ 5351f304381501f27833e5c7fa4f536ae5b684f8

Next action =
independent execution-ready Critic review of Stage 1 package v1.3

Source truth:
#49 = PROMOTE_NOW
#50-#53 = NEW
all other maturity unchanged

Do not mark DONE.
Do not close issues.
\`\`\`

## 12. Planner verdict

\`\`\`text
PLANNER_RESULT = READY_FOR_EXECUTION_READY_CRITIC
READY_FOR_EXECUTION_READY_CRITIC = YES
READY_FOR_CODEX = NO
NEXT_HANDOFF = CRITIC
\`\`\`
