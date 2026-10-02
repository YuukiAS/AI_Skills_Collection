# Presentations Stage 1 Execution Package v1.3

**Status:** COMPLETE PACKAGE FOR EXECUTION-READY CRITIC REVIEW / NOT EXECUTION AUTHORIZATION  
**Task key:** \`presentations--stage1-front-door-two-template-foundation\`  
**Package version:** 1.3  
**Date:** 2026-09-29

This manifest binds the complete Stage 1 v1.3 execution package after Critic v1.2 returned REVISE on render portability and private-reference reviewer access.

## 1. Authority

Architecture authority:

\`docs/design/PRESENTATIONS_TWO_TEMPLATE_PRODUCTION_REDESIGN_PLAN_V1_1_2026-09-28.md @ f71e97c06938ab2ce175ccf3b4ac19da9309fda1\`

Prior package:

\`results/presentations--stage1-front-door-two-template-foundation/EXECUTION_PACKAGE_V1_2.md @ 6fe1b561bcebec7f9a6f677bb6ce3b26b91e6ca1\`

Critic revision basis:

\`results/presentations--stage1-front-door-two-template-foundation/CRITIC_EXECUTION_READY_REVIEW_V4.md @ faae612ea90aa1e7db948ae29837e699b8d13e25\`

## 2. Stable blocker state

\`\`\`text
PRES-S1-ER-F01 = CLOSED
PRES-S1-ER-F02 = CLOSED
PRES-S1-ER-F03 = CLOSED

PRES-S1-ER-F04 = PLANNER_ACCEPTED_IN_V1_3
PRES-S1-ER-F05 = PLANNER_ACCEPTED_IN_V1_3
\`\`\`

Independent Critic must decide F04/F05 closure.

## 3. Package objects

### Plan v1.3

Path:

\`docs/design/PRESENTATIONS_STAGE1_FRONT_DOOR_TWO_TEMPLATE_EXECUTION_PLAN_V1_3_2026-09-29.md\`

First commit:

\`a4ff0840fd57ca3d58bfd254526ebd8327b198bd\`

### Canonical Goal v1.3

Path:

\`docs/goals/PRESENTATIONS_STAGE1_FRONT_DOOR_TWO_TEMPLATE_GOAL_V1_3.md\`

First commit:

\`ef7925588f5d65b15c44d84535327bc7648544ea\`

### Kickoff Draft v1.3

Path:

\`docs/operations/prompts/PRESENTATIONS_STAGE1_FRONT_DOOR_TWO_TEMPLATE_KICKOFF_V1_3.md\`

First commit:

\`3421d6c1b53f523c01cd8bc7006f4e37cd37c0dc\`

### Planner Response v1.3

Path:

\`results/presentations--stage1-front-door-two-template-foundation/PLANNER_RESPONSE_V1_3.md\`

First commit:

\`140c0c53c4ed6d7fd0ae8ad7386056ab47fcc17c\`

## 4. v1.3 scope delta

Only two execution-readiness closures are added.

### F04
Both built-in Beamer adapters now freeze:
- \`render-chinese-math-pdf\` as sole render environment/resource-resolution owner;
- no reusable private host absolute render/font/TeX path;
- typed missing-dependency fail closed;
- no Chromium/system-font/lower-fidelity fallback;
- portability/fallback-font regression gates.

### F05
G5 private fidelity now has a concrete non-paid evidence path:
- exact implementation/render identity manifest;
- exact private review bundle;
- direct-pixel user-visible ChatGPT review surface;
- repo-tracked metadata-only qualitative evidence;
- Scheduled GPT Reviewer consumes hash-bound evidence without claiming direct private-pixel access.

## 5. Product decisions unchanged

Still:
- exactly two built-in templates;
- #49 = PROMOTE_NOW;
- #50–#53 = NEW/deferred;
- course-standard default 4:3;
- explicit 16:9 = same template variant;
- existing/local/locked ratio preserved;
- research no-format -> CUHK;
- teaching -> course-standard;
- business/editable route unchanged;
- local-edit fast path unchanged;
- external locked template pass-through;
- G5 actual consumption vs fidelity non-compensating;
- Bridge 0.9.3 first publication;
- CI required;
- automated Bridge visual/text review flags false;
- no paid review;
- no release/version/main integration.

## 6. Render portability acceptance

Required Stage 1 evidence:

\`\`\`text
RP-G1 two configured resource roots
RP-G2 forbidden reusable host-path scan
RP-G3 typed missing dependency
RP-G4 unexpected fallback font rejection
RP-G5 both adapters consume render-chinese-math-pdf owner
\`\`\`

## 7. Private G5 evidence paths

Tracked identity manifest:

\`results/presentations--stage1-front-door-two-template-foundation/g5_private_review/G5_REVIEW_INPUTS.json\`

Private review bundle:

\`private/exports/presentations--stage1-front-door-two-template-foundation/g5-review-bundle/\`

Tracked qualitative evidence:

\`results/presentations--stage1-front-door-two-template-foundation/g5_private_review/G5_PRIVATE_VISUAL_REVIEW.md\`

No private Chapter1 pages/images are committed.

Scheduled GPT Reviewer remains final implementation-review authority.

## 8. CI / review flags

\`\`\`text
ci_required = true
visual_review_required = false
text_review_required = false
paid review = NOT AUTHORIZED
G5 direct-pixel private evidence = REQUIRED
\`\`\`

## 9. Version / release

\`\`\`text
Repository bump decision = NONE
Affected plugin:
- presentations = NO_BUMP
\`\`\`

No production release/install.
No main integration.
No maturity promotion.

## 10. Maintenance tracking

\`\`\`text
Area = presentations
Status = DOING
Issues = #29-#53

#49 = PROMOTE_NOW
#50-#53 = NEW
other maturity unchanged
\`\`\`

No issue closes from this package.

## 11. Critic contract

The next Critic must review the same-version Plan + Goal + Kickoff + manifest + Planner response/validation.

Priority:
- \`PRES-S1-ER-F04 = CLOSED ?\`
- \`PRES-S1-ER-F05 = CLOSED ?\`

If PASS:
- set \`READY_FOR_CODEX=YES\`;
- reproduce the exact v1.3 Kickoff verbatim;
- user must still send it before execution authorization exists.

If REVISE:
- preserve stable blocker IDs where applicable;
- only new facts/critical missed risks/direct v1.3 regressions may add blockers;
- return full Planner prompt.
