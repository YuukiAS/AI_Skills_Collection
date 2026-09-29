# Presentations Stage 1 Execution Package v1.2

**Status:** COMPLETE PACKAGE FOR EXECUTION-READY CRITIC REVIEW / NOT EXECUTION AUTHORIZATION  
**Task key:** \`presentations--stage1-front-door-two-template-foundation\`  
**Package version:** 1.2  
**Date:** 2026-09-29

This manifest binds the complete bounded Stage 1 amendment after new real teaching-deck evidence and Bridge Kit 0.9.3 closure.

## 1. Architecture authority

\`docs/design/PRESENTATIONS_TWO_TEMPLATE_PRODUCTION_REDESIGN_PLAN_V1_1_2026-09-28.md\`
@ \`f71e97c06938ab2ce175ccf3b4ac19da9309fda1\`

No new major architecture round is opened.

## 2. Why v1.2 exists

v1.1 had become execution-ready after:
- \`PRES-S1-ER-F01 = CLOSED\`;
- \`PRES-S1-ER-F02 = CLOSED\`;
- \`PRES-S1-ER-F03 = CLOSED\` after Bridge Kit 0.9.3.

New real-use evidence from STAT5060 Tutorial 1 then showed one Stage-1-owned gap:

\`#49 Course-standard teaching template needs structural navigation, not only colours and bands\`

v1.2 therefore amends only:
1. course-standard structural/navigation identity;
2. course-standard 4:3 default + explicit 16:9 variant semantics;
3. execution-control wording to use actual Bridge Kit 0.9.3 \`task publish-first\`.

## 3. Package objects

### Stage 1 Plan v1.2

Path:

\`docs/design/PRESENTATIONS_STAGE1_FRONT_DOOR_TWO_TEMPLATE_EXECUTION_PLAN_V1_2_2026-09-29.md\`

First commit:

\`63f854ca095a6d9b8353ac803ff13c2f4cbc7f92\`

### Canonical Goal v1.2

Path:

\`docs/goals/PRESENTATIONS_STAGE1_FRONT_DOOR_TWO_TEMPLATE_GOAL_V1_2.md\`

First commit:

\`56ac9e9dbb3923957a58b3154d290448b4d68f06\`

### Kickoff Draft v1.2

Path:

\`docs/operations/prompts/PRESENTATIONS_STAGE1_FRONT_DOOR_TWO_TEMPLATE_KICKOFF_V1_2.md\`

First commit:

\`718a45118e23e0a3c5801574801ce7e515c1f127\`

## 4. Canonical TODO amendment

\`docs/plugin-todos/presentations.md\`

#49 status changed:

\`NEW -> PROMOTE_NOW\`

Commit:

\`e6d4058e2716583012ffda5f310a8aadfce819df\`

#50–#53 remain \`NEW\`.

No other TODO maturity is promoted by this package.

## 5. Bridge dependency truth

Historical dependency record:

\`results/presentations--stage1-front-door-two-template-foundation/F03_BRIDGE_DEPENDENCY.md\`

now records:

\`CLOSED_BY_BRIDGE_0_9_3\`

Closure update commit:

\`8d283d74046a624e51241512fa5113031b14bc8f\`

Verified Bridge formal state:

\`\`\`text
version = 0.9.3
formal release target =
9dad0ba4bfa54e251f345091c5151ae991251ec9
formal distribution complete = YES
production first-publication entry =
ai-bridge reviewed-handoff task publish-first
\`\`\`

Old generic Bridge blocker is not carried into v1.2.

Execution-machine runtime freshness remains a preflight condition, not a product blocker.

## 6. Frozen Stage 1 product scope

Still only:

\`\`\`text
front door
+ routing
+ local-edit fast path
+ two-template adapter foundation
+ #49 course-standard structural/navigation + ratio support
+ generated-layer parity
+ G1
+ G5
\`\`\`

Explicitly excluded:
- #50 presenter-learning companion;
- #51 lecture/source cross-reference;
- #52 assessment semantics/answer-leakage guardrails;
- #53 semantic closing choice;
- Stage 2–6 capabilities;
- third template;
- new plugin/skill/schema/state machine;
- Bridge Kit modification;
- paid review;
- release/version bump;
- main integration.

## 7. Course-standard amendment summary

### Visual identity

Preserve private Chapter1 reference family:
- black top band;
- blue frame-title;
- white body;
- ordinary blue bullet;
- sparse academic teaching hierarchy;
- lower-right page number;
- sans body + compatible math;
- no annotation/highlight replication;
- no CUHK branding.

### Structural identity

Add template-level:
- canonical opening/title frame;
- section-aware navigation/state;
- PDF outline/bookmarks;
- nonintrusive top navigation where appropriate;
- normal-Beamer bottom navigation/action affordances where appropriate;
- stable footline/page number;
- distinct title/content/section-aware/closing states;
- canonical closing-frame primitive.

Stage 1 does not choose recap/question/Q&A/thanks semantics.

### Ratio policy

\`\`\`text
course-standard no explicit ratio -> 4:3
course-standard explicit 16:9 -> same template identity, 16:9 variant
existing/local edit -> preserve ratio
external locked template -> preserve locked ratio
\`\`\`

No third built-in template.

## 8. G1 / G5 amendment

G1 remains installed natural-entry routing and now explicitly tests:
- teaching default 4:3;
- teaching explicit 16:9.

G5 remains non-compensating:
- canonical source actually consumed;
- independent visual fidelity.

For course-standard:
- 4:3 compares exact reference/default identity to Chapter1;
- 16:9 verifies actual ratio + invariant course-standard identity, not exact 4:3 dimensions;
- structural navigation/bookmark/footline/opening/closing support is part of fidelity.

## 9. CI / visual-review truth

\`\`\`text
ci_required = true
visual_review_required = false
text_review_required = false
paid review = NOT AUTHORIZED
\`\`\`

Real GitHub CI remains mandatory.

Independent G5 pixel-level visual review remains mandatory and must directly access renders + exact private Chapter1 reference.

## 10. Version / integration

\`\`\`text
Repository bump decision: NONE
Affected plugin:
- presentations: NO_BUMP
\`\`\`

No main integration.
No production install/release.
No maturity promotion.

## 11. Maintenance tracking

Presentations issues remain active.

Current source disposition:
- #49 = PROMOTE_NOW;
- #50–#53 = NEW;
- existing #44–#48 maturity unchanged.

Project lifecycle should remain:

\`Area = presentations\`
\`Status = DOING\`

No issue is DONE/closed.

## 12. Approval boundary

This package is not Codex authorization.

A new independent execution-ready Critic must review the complete v1.2 Plan + Goal + Kickoff + manifest + Planner validation.

Only that Critic may set:

\`READY_FOR_CODEX=YES\`

and return the exact approved Kickoff for later user authorization.
