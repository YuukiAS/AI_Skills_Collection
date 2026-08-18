---
schema: AI_BRIDGE_REVIEWED_PLAN_V1
task_key: 010_four_slide_regression
decision: PLAN_FROZEN
---

# 010 Four Slide Regression — Plan

## Objective and value

Produce a compact, renderable regression packet that exposes the workflow boundary to external Planner review.

## Frozen decisions

The deck has exactly four main slides: RESULT_FIGURE, FAILURE_CASE, EXPERIMENT_DESIGN, STATISTICAL_MODEL.

## Implementation scope

Update generator, evidence manifest, renderer path handling, expected render PNG fixtures, and tests.

## Acceptance and regression gates

Generated PPTX renders through LibreOffice to PDF and four PNGs; reviewer reports mechanical pass; each slide has 2-5 inspected `RRL-*` references.

## Natural-language usage / routing expectations

The packet demonstrates the minimum scientific objects expected from a group-meeting deck route.

## Out of scope

Do not present synthetic regression slides as a finished user deck or clinical result.
