# Production handoff: CARE advisor update

The scientific Markdown source is ready for downstream PDF production. No PDF has been generated or visually reviewed. This task ends at Research Authoring; the approved PDF renderer companion is unavailable on the task's standalone surface.

## Input and intended artifact

- Canonical source: `advisor_update_source.md`, alongside this handoff.
- Deliverable to produce downstream: a formal, English-language PDF for a PI/advisor meeting, suggested filename `advisor_update.pdf`.
- Purpose: support the decision between expanded robustness checks and a personalization ablation for next week.
- Source authority: `../inputs/01-C2_DEV_REPORT_RAW_NOTES.md`; provenance and claim checks are in `route_receipt.md` and should not be appended to the advisor PDF.
- No institutional template, page size, typography, author list, meeting date, or strict page limit was supplied. A concise one- to two-page report is a layout preference, not an acceptance requirement; preserve readable text and all scientific caveats.

## Owner and dependency

Research Authoring owns claims, evidence, section roles, and scientific acceptance. The downstream renderer owner must use the approved companion `render-chinese-math-pdf`, dependency `skills/tools/documents-media/render-chinese-math-pdf`, in a surface where it is installed and authorized. That owner selects the supported renderer, fonts, pagination, and production checks. Do not substitute an ad hoc XeLaTeX template, browser PDF, or another conversion path to bypass this dependency. This packet supplies the production brief; a second authoring prompt is unnecessary.

## Content to preserve

Keep the title, section sequence, Table 1 caption and rows, limitations, and final advisor decision. Retain the recommendation as a proposal. Preserve all values and the distinction between macro-F1 and recall. The +0.043 difference is arithmetic from the two main point estimates. Do not relabel the Pattern H interval as a paired bootstrap 95% confidence interval: those details are absent. Keep the single-seed caveat adjacent to the personalization result. Do not infer clinical validity, deployability, independent verification, a mechanism, or an approved experiment design.

Missing sample sizes and methods are scientific limitations already disclosed in the source. The renderer must not fill them with guesses. New data or substantive interpretation requires return to the authoring owner.

## Tables, figures, and formulas

Table 1 is the primary comparison device and must appear in the PDF. Its scientific role is to distinguish the main temporal comparison, shifted-cohort evidence, and preliminary personalization result without conflating endpoints. Keep it legible and, where practical, together with its caption. If a split is necessary, repeat column headers and preserve each row's caveats.

No figure or formula is necessary for this evidence volume. Do not invent learning curves, seed distributions, sample counts, or error bars. An interval comparison figure could be useful in a later revision after the authoring owner confirms the Pattern H metric, confidence level, and interval method; it is not part of this production request. A subgroup error plot would require counts and denominators absent from the notes.

## Pending production checks and acceptance

1. Confirm the approved renderer dependency and supported route before conversion. Record the actual toolchain and source identity.
2. Produce the PDF from the canonical source with searchable text and readable typography. Preserve the scientific content if a layout adjustment is needed.
3. Inspect every rendered page for missing glyphs, clipping, overlap, awkward page breaks, isolated headings, excessive whitespace, and readable table columns. Keep caveats visually connected to the relevant results.
4. Check extracted PDF text against the source, particularly every number, interval bracket, plus sign, comparison label, and the single-seed and clinical/deployment limitations. Verify title and caption identity.
5. Confirm no internal handoff, route receipt, QA tokens, raw workspace paths, or invented metadata entered the advisor report. Check any links included in the PDF.
6. Return the actual user-openable PDF, final path and hash, page count, and a concise record of conversion, text-fidelity, and page-by-page visual checks. Disclose any unresolved issue; rendering success alone is not visual acceptance.

All conversion, pagination, font/glyph, PDF text-extraction, and visual checks above remain pending. Source-level authoring completion is separate from formal-PDF completion.
