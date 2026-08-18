---
schema: AI_BRIDGE_REVIEWED_PLAN_V1
task_key: 009_visual_reviewer_split
decision: PLAN_FROZEN
---

# 009 Visual Reviewer Split — Plan

## Objective and value

Prevent a generated deck from being academically approved by mechanical checks alone.

## Frozen decisions

The reviewer output is `MECHANICAL_VISUAL_REVIEW.json`; `academic_visual_decision` must be `NOT_ASSESSED`.

## Implementation scope

Update the regression reviewer and tests.

## Acceptance and regression gates

Reviewer checks render PNGs, dimensions, blank area, contrast, object area, edge proximity, text-density proxy, and PPTX object summary, but does not output scientific PASS.

## Natural-language usage / routing expectations

The external Planner receives mechanical evidence and rendered PNGs, then performs human/Planner scientific review separately.

## Out of scope

Do not encode mature scientific taste as deterministic thresholds.
