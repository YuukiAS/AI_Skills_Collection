---
schema: AI_BRIDGE_REVIEWED_PLAN_V1
task_key: 005_reference_integrity_cleanup
decision: PLAN_FROZEN
---

# 005 Reference Integrity Cleanup — Plan

## Objective and value

Make the reference index evidence-backed by deleting synthetic metadata page-function rows.

## Frozen decisions

No row may be emitted unless a specific cached page was opened or rendered. `PAGE_FUNCTIONS` rotation is not allowed.

## Implementation scope

Update `build_reference_metadata.py` and regenerated committed CSV/JSON metadata only.

## Acceptance and regression gates

- `metadata page-function record` count is zero.
- Every inspected row has an actual page number, source checksum, rendered page checksum, and page-specific observation.

## Natural-language usage / routing expectations

A presentation skill can cite `RRL-*` records as inspected page patterns without copying public slides.

## Out of scope

Do not download hundreds of decks, rewrite unrelated presentation skills, or claim corpus maturity.
