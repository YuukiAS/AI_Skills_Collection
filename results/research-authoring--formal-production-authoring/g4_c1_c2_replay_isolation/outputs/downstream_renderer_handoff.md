# CARE advisor update: downstream production handoff

The scientific Markdown source is ready for downstream PDF production. No PDF has been generated or visually checked. The current task explicitly excludes rendering because the approved renderer companion is unavailable on this standalone Research Authoring surface.

## Document and ownership

- Canonical source: `advisor_update_source.md` in this directory.
- Evidence input: `../inputs/01-C2_DEV_REPORT_RAW_NOTES.md`.
- Audience: PI/advisor deciding next week's experiment priority.
- Family and language: concise research update, English, matching the supplied notes.
- Eventual artifact: formal advisor-meeting PDF; proposed filename `advisor_update.pdf`.
- Scientific owner: Research Authoring, through `research-authoring-core` and `research-reporting`.
- Production owner: approved `render-chinese-math-pdf` companion, exact dependency `skills/tools/documents-media/render-chinese-math-pdf`, once available in the downstream environment.

The renderer owns typography, page setup, conversion, and PDF inspection. Scientific changes, new results, statistical assumptions, and altered recommendations return to the scientific owner. Do not substitute a private XeLaTeX template, Chromium conversion, or another renderer to bypass the missing companion. No installation or rendering was attempted here. This handoff contains the production context; a second authoring prompt is not required.

## Content contract

Lead with the experiment-priority decision and its rationale. Preserve the distinction between observed evidence and the proposed ablation. Keep the single-seed pilot caveat beside the recall result, and retain the limits on clinical validity and deployability.

Protected values and meanings:

- Main macro-F1: 0.714 versus 0.671; +0.043 is an arithmetic difference, not an additional measurement.
- Main difference interval: paired bootstrap 95% confidence interval [0.018, 0.071].
- Pattern H shifted-cohort interval: [0.004, 0.049]. Do not supply an unreported point estimate, method, or confidence level, or imply proven effect attenuation from interval location alone.
- Error concentration: fewer than four observations; do not turn raw error concentration into a subgroup error-rate claim.
- Personalization recall: 0.46 to 0.51, one seed, preliminary. Do not relabel recall as macro-F1.

Missing sample sizes, main-comparison seed counts, preprocessing specification, Pattern H definition, and pilot uncertainty remain missing. They need not prevent faithful rendering, but the renderer must not fill them in. The source's brief evidence-basis statement belongs in the PDF. File paths, hashes, this handoff, and the route receipt are production metadata and should not appear in the advisor-facing PDF. No bibliography or citation keys were supplied; none should be fabricated.

## Table, figure, and formula roles

Table 1 is the principal evidence display. It lets the advisor compare the main result, the shifted-cohort check, and the distinct pilot endpoint without repeated numerical prose. Preserve all three rows, the caption, metric labels, and uncertainty column. The pilot row must remain visibly qualified as preliminary.

No figure or equation is necessary. An optional interval-only figure could compare the two reported difference intervals with a zero reference, but must not invent a Pattern H point marker or confidence-level label. It would largely duplicate the table and is not requested for this concise version. Do not add a seed-distribution plot or subgroup chart without underlying data. No external assets are required.

## Pending production and acceptance checks

No page-size, font, institutional template, author identity, or meeting date was supplied. Use the approved renderer's normal formal-report defaults; aim for a readable one- or two-page report without forcing a page count or shrinking text to fit. Do not invent author or meeting metadata.

The downstream owner must:

1. Verify the source hash recorded in `route_receipt.md`, then render that exact source through the approved companion.
2. Check every PDF page visually for readable type, missing glyphs, clipping, overlap, excessive whitespace, awkward page breaks, and orphaned headings.
3. Check Table 1 width, wrapping, caption placement, and complete rows. Keep each result with its uncertainty; repeat the header if the table spans pages.
4. Compare extracted PDF text with the source, checking every protected number, interval, metric, qualifier, and the advisor decision. Inspect minus signs, brackets, and decimals visually as well.
5. Verify that no production notes or invented references entered the PDF, and that text remains selectable/searchable.
6. Return the actual PDF with its path, hash, page count, rendering route, and completed visual/content QA. Report unresolved defects explicitly.

PDF generation, pagination, font checks, table layout checks, extracted-text comparison, and visual acceptance are all pending. The Markdown deliverables complete the current authoring request; the eventual formal PDF remains outstanding.
