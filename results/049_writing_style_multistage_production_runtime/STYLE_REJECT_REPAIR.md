# 049 STYLE_REJECT Repair Receipt

Date: 2026-09-02

User decision: `STYLE_REJECT`.

Reason: the first 049 implementation produced SMOKE-A, SMOKE-B, and SMOKE-C without a material improvement over 048. The multistage receipt existed, but the production output still reflected the failed source-surface prose regime.

This is an Executor implementation failure, not a Planner failure and not a Reviewer round. `review_round` and `plan_revision` remain unchanged.

## Verified Implementation Failures

### F001 — Model-generated Document Map is not consumed

The runtime calls the document-map model stage, but `doc_map_model_output` is recorded only as hash/char metadata. It is not parsed, validated, or used as the downstream document map.

### F002 — Model-generated Meaning Card is not consumed

The runtime calls the meaning-card model stage, but `meaning_model_output` is recorded only as hash/char metadata. The writer packet still receives the deterministic card built from source-surface extraction.

### F003 — Coverage check is superficial

Coverage is based on sentence presence or keyword overlap against a card that was itself extracted from the source. It does not prove proposition-level preservation of claims, evidence, conditions, comparators, caveats, attribution, or decision logic.

### F004 — Argument-unit segmentation is not implemented

Segmentation is heading-driven. Long multi-paragraph text without headings can become a single unit. The prior private smoke receipts showed `unit_count=1` for SMOKE-A, SMOKE-B, and SMOKE-C.

### F005 — Semantic audit is not semantic

The deterministic semantic audit is equivalent to literal-missing detection. The model audit output is not parsed into findings and does not control PASS/REVISE.

### F006 — Reader Review does not see the candidate

The candidate-only reader review packet contains only `candidate_sha256`, audience, questions, and `source_visible=false`. It does not include the actual candidate text.

### F007 — Reader Review result is ignored

Reader-review model output is recorded as hash/char metadata only. A REVISE decision cannot route back to unit repair.

### F008 — Final coherence review also does not see prose

The final assembly/coherence model sees hashes and counts rather than actual assembled prose, so it cannot inspect transitions, terminology consistency, repeated explanations, or local style outliers.

### F009 — Technical trace relocation is not active in OpenAI path

For `driver=openai-responses`, the writer result is assigned entirely to `reader_core` and `technical_trace` is always empty.

### F010 — Example selection is weakly adaptive

Example selection is based on source keyword guessing rather than validated Meaning Card metadata, so it can select the same examples for different discourse roles.

## Repair Boundary

The repair must keep the 049 frozen objective and transport boundary:

- no 050;
- no full 22-page report before style acceptance;
- no version bump;
- no main merge;
- no Bridge Kit or Host Policy change unless current evidence proves the secure transport itself cannot support the frozen route;
- no phrase blacklist or target-document hardcode;
- no silent fallback from structured production stages to deterministic approximations.
