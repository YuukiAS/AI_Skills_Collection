---
schema: PRODUCT_UI_COPY_H0_PREFLIGHT_V1
task_key: product-ui-copy--cross-plugin-production-integration
plan_revision: 0
created_for: H0 fresh-evidence preflight
---

# H0 Fresh-Evidence Preflight

This file freezes only the evidence shape required before implementation. It
does not expose the exact H3 fresh-holdout prompts.

## Batch Size

Final fresh holdout batch size: 8 scenarios.

## Task Families

- Product UI microcopy wording under frozen meaning.
- Locale/register realization for `zh-Hans` and `zh-Hant-HK`.
- Frontend content architecture and disclosure decisions.
- Product semantics escalation when product truth is missing.
- Legal/trust/safety escalation when required facts are not known.
- KEEP controls for already-good interface copy.
- Rendered interface rhythm across dense, multi-block, and constrained
  viewports.
- Platform-aware Frontend discovery for browser extension, web, desktop/WebView
  and mobile/Compose UI work, with backend/runtime/data/docs negatives.

## Coverage Matrix

The final hidden H3 batch must collectively cover:

- `zh-Hans` natural Product UI Copy.
- `zh-Hant-HK` natural Product UI Copy.
- CTA/action consequence.
- State/help/error copy.
- Landing or multi-block page rhythm.
- KEEP.
- CONTENT ARCHITECTURE escalation.
- PRODUCT SEMANTICS escalation.
- LEGAL/TRUST/SAFETY escalation.

One scenario may cover multiple dimensions, but every listed dimension must be
represented at least once across the batch.

## Outcome Classes

- `KEEP`: copy is already clear and must not be rewritten just to show activity.
- `WORDING/NATURALNESS`: wording can be improved without changing meaning.
- `LOCALE/REGISTER`: same protected meaning requires locale-specific wording.
- `CONTENT ARCHITECTURE`: Frontend must change placement, amount, hierarchy,
  disclosure, or neighboring copy before wording can be finalized.
- `PRODUCT SEMANTICS`: product truth, state, eligibility, consequence, or
  reversibility is missing or inconsistent.
- `LEGAL/TRUST/SAFETY`: trust, privacy, consent, retention, deletion, safety,
  pricing, or external-visibility meaning needs explicit product/domain/legal
  authority.

## Locale Balance

The final batch must include both Simplified Chinese and Traditional Chinese
for Hong Kong contexts. At least one case must require independent
`zh-Hant-HK` wording rather than mechanical character conversion.

## Rubric

A candidate passes a scenario only when:

- The selected route matches the user-visible task: Product UI Copy for
  interface copy, long-form Chinese prose for reports/README, and
  scientific-rewrite for heavy source-faithful technical rewrites.
- Protected product meaning is preserved, or the candidate escalates instead of
  inventing product/legal truth.
- The output respects the owner boundary: Frontend decides content architecture
  and rendered rhythm, Writing decides natural wording under frozen meaning, and
  product/domain/legal authority owns missing facts.
- `zh-Hans` and `zh-Hant-HK` are natural in their own locale and semantically
  equivalent under the protected meaning.
- KEEP controls remain substantially unchanged.
- Frontend discovery activates for user-interface work and stays inactive for
  backend/runtime/data/docs-only work.
- Rendered evidence, where applicable, shows readable text, non-overlapping
  layout, coherent hierarchy, and trust/help/CTA relationships at the bound
  viewport.

## Reviewer Criteria

The independent Reviewer must inspect the real evidence files, not summaries
alone. Reviewer checks must bind each decision to the exact candidate commit,
the route actually consumed, and any screenshot or replay artifact used as
evidence.

Release-critical PASS cannot splice pre-H2 development evidence with post-H2
H4/CI evidence. Exact-H2 G1-G6 must be rerun after version bump and
regeneration before H3 can be frozen.
