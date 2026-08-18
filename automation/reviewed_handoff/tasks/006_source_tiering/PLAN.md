---
schema: AI_BRIDGE_REVIEWED_PLAN_V1
task_key: 006_source_tiering
decision: PLAN_FROZEN
---

# 006 Source Tiering — Plan

## Objective and value

Make retrieval prefer real research presentations while keeping lower-confidence sources visible but gated.

## Frozen decisions

Use exactly these tiers: `PRIMARY_RESEARCH_PRESENTATION`, `SECONDARY_TEACHING_REFERENCE`, `PRESENTATION_GUIDANCE`, `CANDIDATE_BACKLOG`.

## Implementation scope

Update manifest/source CSV generation and workflow documentation.

## Acceptance and regression gates

Manifest retrieval priority lists all four tiers; uninspected URL leads use `CANDIDATE_BACKLOG`.

## Natural-language usage / routing expectations

When generating group-meeting slides, inspected primary records should be preferred over teaching PDFs or candidate URL leads.

## Out of scope

Do not delete cache files, submit source files, or silently promote backlog entries.
