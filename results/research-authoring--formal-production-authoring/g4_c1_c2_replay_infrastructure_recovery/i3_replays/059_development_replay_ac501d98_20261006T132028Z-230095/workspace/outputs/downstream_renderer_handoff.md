# Downstream production handoff

Scientific source is ready for PDF production by the approved renderer owner. No PDF has been created, compiled, opened, previewed, or inspected in this authoring stage. Render-dependent acceptance remains pending.

## Document and authority

- Canonical source: `advisor_update_source.md` in this directory.
- Source evidence: `../inputs/01-C2_DEV_REPORT_RAW_NOTES.md`.
- Document: concise English advisor-facing CARE sequence-modeling research update, not a manuscript or slide deck.
- Purpose: support the PI's choice between next week's personalization ablation and expanded robustness checks.
- Authoring owner: Research Authoring (`research-authoring-core` → `research-reporting`).
- Required downstream owner: `render-chinese-math-pdf`, dependency `skills/tools/documents-media/render-chinese-math-pdf`, in an approved companion-enabled environment. The current task explicitly defines this standalone surface as lacking the approved companion; a catalog entry or generic execution tool is not a substitute for that route.
- Formatting contract: none supplied. Use a restrained, readable meeting-report layout; no mandatory page count, venue template, author identity, or meeting date. Do not invent these details.
- Proposed final artifact: `advisor_update.pdf`, returned with its canonical source and production QA result.

## Content and visual roles

Keep the decision and recommendation first, then evidence, interpretation and limitations, and the proposed experiment. The recommendation is an authoring judgment for advisor consideration, not an approved plan or an observed result.

Table 1 is the sole required visual element. It lets the advisor compare the replication, shifted-cohort evidence, and pilot while keeping their endpoints and evidence strengths distinct. Preserve its caption and all three rows. Column widths, wrapping, and orientation are renderer decisions; preserve scientific meaning if formatting changes are needed.

No figure or formula is required. A future interval plot could help compare cohort conditions, but it should wait for confirmation of the Pattern H interval's metric, method and confidence level, and its point estimate. Do not fabricate a midpoint as an effect estimate. The present table is sufficient. No external image assets, bibliography, citation keys, or LaTeX macros are required.

## Protected scientific content

Preserve 0.714, 0.671, derived difference +0.043, paired bootstrap 95% interval [0.018, 0.071], Pattern H interval [0.004, 0.049], fewer than four observations, recall 0.46 → 0.51, and the single-seed pilot qualification. Keep the Pattern H interval method/confidence level unconfirmed, as in the source. Do not translate recall into macro-F1, treat error concentration as subgroup error rate, or claim clinical validity, deployability, broad robustness, or reproducible personalization benefit.

The source notes are the sole scientific authority. Missing sample sizes, resampling details, Pattern H definition and pilot comparability must not be filled by the renderer. These gaps limit scientific interpretation but need not block faithful typesetting of the qualified source. Return any proposed substantive change to the authoring owner.

## Production steps and outstanding checks

1. In the approved companion-enabled environment, consume this handoff and the canonical Markdown source. Keep this handoff and `route_receipt.md` outside the advisor PDF.
2. Render with the companion's supported workflow. Record source identity, output path and renderer settings in production evidence.
3. Inspect every rendered page for readable body/table text, wrapping, table width, clipping, overlap, excessive whitespace, awkward page breaks, and caption/row separation. Confirm glyphs for arrows, minus signs, brackets and decimal values.
4. Check PDF text against the source, including all values, interval qualifiers, the fewer-than-four threshold, the pilot caveat, limitations and the proposed status of the next experiment. Verify fonts, page properties and selectable text using the companion's QA procedure.
5. If layout needs adjustment, change layout before content. Do not remove caveats or reduce text to unreadable size to meet an invented page target. Return meaning-changing edits to Research Authoring and repeat scientific QA.
6. Deliver the actual PDF with its path and final visual/text QA status. Rendering, pagination, font/glyph checks, PDF text fidelity and page-level visual acceptance are all pending at this handoff.

Authoring-stage checks cover source semantics, arithmetic, evidence boundaries, audience relevance and Markdown structure only. They are not PDF or layout acceptance.
