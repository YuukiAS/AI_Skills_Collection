# Downstream production handoff

## Delivered artifact and readiness

Canonical manuscript: `paper.md` (UTF-8 Markdown). This is a substantially revised, evidence-bounded manuscript source, prepared for author completion and subsequent formal PDF production. It is not submission-ready: methodological details, result confirmation, references, author metadata, and venue selection remain pending. `authoring_brief.md` records the frozen scientific scope; `qa_receipt.md` records source checks.

The source/package stage is complete within the supplied evidence boundary. No PDF was compiled, opened, rendered, previewed, visually inspected, or PDF-QA checked. Renderer admission is absent on this standalone Research Authoring surface. Do not interpret source checks as a successful PDF build.

## Audience, purpose, and authority

Audience: lesion-segmentation researchers, coauthors, and eventual reviewers. Purpose: report a preliminary evaluation of test-time percentile clipping before an existing 3D U-Net pipeline. Sole scientific authority: `inputs/01-manuscript_notes.md`, preserved as `provenance/01-manuscript_notes.md`. File hashes are in `manifest.sha256`.

Keep the 18-volume internal-split boundary, provisional Dice language, absence of uncertainty estimates, and persistent motion-corruption failure visible. Do not infer external validation, lesion counts, participant counts, thresholds, significance, mechanism, or robustness. Arithmetic differences are derived from the supplied rounded aggregates, not new experimental evidence.

## Author completion before submission

| Item | Required resolution | Owner |
|---|---|---|
| Numerical authority | Confirm aggregates against evaluation records; supply case-level outputs if available; confirm comparison identities | Study authors |
| Data and annotations | State modality, lesion type, acquisitions, inclusion criteria, participant and lesion counts, split construction, and reference procedure | Study authors |
| Clipping and pipeline | Specify percentiles, estimation scope, background handling, normalization order, checkpoint, inference settings, and controls; disclose threshold-selection history | Study authors |
| Metrics and uncertainty | Define small lesions, Dice aggregation, HD95 computation and units, empty-mask handling, denominators, and any uncertainty analysis actually performed | Study authors / analysis owner |
| Declarations | Supply authorship, affiliations, funding, interests, applicable ethics/consent, and data/code availability | Study authors |
| Citation support | Verify methodological attribution and relevant prior work, then add real references and bibliography | Citation owner with author approval |
| Venue | Select target and verify its current template, article type, limits, citation style, declarations, and submission requirements | Authors / venue owner |

Do not fill these gaps through editorial inference. The renderer can produce a clearly labelled draft with unresolved statements retained; submission-quality production requires the author-completion items to be resolved or explicitly accepted within the chosen scope. Broader robustness claims require additional evidence, not a wording change.

## Production route and display roles

An explicitly admitted downstream renderer should consume `paper.md`, preserve its scientific semantics, and produce the requested PDF through the selected venue template. A Markdown-to-LaTeX/PDF route is possible, but no engine, font, template, build command, or venue is prescribed or tested here. Consult the admitted renderer's own instructions before choosing mechanics. Keep this handoff, the brief, QA receipt, manifest, and provenance out of the manuscript body.

Table 1 is the quantitative evidence display; keep its caption, all three rows, exact decimals, signed differences, and HD95 millimetre units together and readable. There are no figures, image dependencies, equations, or external assets. Do not fabricate illustrative scans or uncertainty bars. Citation support is explicitly pending; no `.bib` file or citation keys are supplied, and the References placeholder must not become a fictitious entry.

## Renderer and venue QA still required

- Verify the chosen venue's current author instructions and official template; no venue compliance has been assessed.
- Confirm title and author block, abstract treatment, heading hierarchy, page size, margins, fonts, line spacing, pagination, and any required line numbering.
- Check Table 1 width, caption placement, decimal and sign fidelity, repeated headers if split, and absence of clipped columns or orphaned caption text.
- Verify Unicode minus signs, numeric extraction, embedded fonts, readable body text, and working cross-references after conversion.
- Validate bibliography rendering and citation resolution once genuine references are added.
- Inspect every rendered page for overflow, overlap, unreadable text, unexpected blank pages, and inappropriate breaks.
- Deliver the PDF, editable source, build dependencies and instructions, build log, and actual renderer QA receipt. Do not label unperformed checks as passed.

## Return to Research Authoring after rendering

Research Authoring must compare the rendered title, abstract, Methods, Results, Table 1, Discussion, Limitations, and Conclusion against the approved source. Recheck 18 volumes; Dice 0.421 → 0.469 and 0.742 → 0.758; HD95 18.4 → 17.9 mm; differences +0.048, +0.016, and −0.5 mm. Verify that provisional language and the motion failure remain visible, and that neither typesetting nor author completion has introduced unsupported claims. Audit new citations against their actual support. Only then record final scientific QA for the actual PDF.

## Governing route

`research-writing/0.3/skills/paper/SKILL.md` and its `_src/core/source.md` define this standalone boundary: “produce stable Markdown/LaTeX/source package plus a complete downstream production handoff, then stop.” An installed rendering tool alone is not admission. This handoff is the intended output boundary, not a failed rendering attempt.
