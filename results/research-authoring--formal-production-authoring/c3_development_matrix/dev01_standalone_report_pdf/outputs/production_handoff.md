# Production handoff: advisor research update

The English report source is stable for downstream PDF production. This standalone Research Authoring surface completes source authoring and handoff; PDF creation and all rendered-artifact checks remain pending.

## Document brief and authority

- Family and audience: research update (`report`) for an advisor deciding whether next week should prioritize calibration or model architecture.
- Purpose: present the validation comparison, preserve its limits, and request a decision about calibration analysis before architecture changes.
- Canonical scientific source: `advisor_research_update.md` in this output directory.
- Evidence authority: `../inputs/01-report_notes.md`, supplied by the user. No raw predictions, case-level results, figures, code, bibliography, or independent validation were supplied or inspected.
- Language: English, preserving the language of the research notes and task. No author, institution, study date, venue, or branding has been invented.
- Edit scope: new report assembled from notes. Subsequent production should preserve wording, table values, units, method identity, caveats, and the advisor decision. Return substantive scientific changes to Research Authoring.

## Claim–evidence spine and section jobs

| Report content | Evidence anchor | Claim boundary |
| :--- | :--- | :--- |
| Comparison on 18 internal validation volumes | Notes: dataset, baseline, candidate | Fixed preprocessing and same split; no invented clipping percentiles or training settings |
| Improved reported Dice and lower HD95 | Notes: six metric values | Descriptive comparison; no statistical significance, generalization, or clinical-utility claim |
| Changes of +0.016, +0.048, and −0.5 mm | Arithmetic from supplied metric pairs | Absolute candidate-minus-baseline differences, not relative percentages |
| Persistent disconnected false positives | Notes: severe-motion scan | One observed case; no estimated failure rate or causal diagnosis |
| Small-lesion promise with limited evidence | Notes: interpretation boundary | Small validation-only check; no final benchmark claim |
| Calibration before architecture as proposed priority | Notes: advisor decision needed | Authoring proposal awaiting advisor decision; no calibration result or approved experiment claimed |

The opening states the finding and decision. “Comparison and findings” gives the design, comparable metrics, and failure case. “Interpretation and next decision” limits the inference and states the proposed next question. Internal paths and QA remain in this handoff and the receipt, outside the advisor-facing report.

Table 1 carries the exact comparison, metric direction, units, and derived changes. No figures or formulas are needed for the supplied evidence. There are no literature claims, supplied citations, citation keys, or bibliography; do not fabricate references or cite a specific nnU-Net paper as if supplied. The internal notes are provenance, not a published reference.

Missing details include clipping percentiles, the small-lesion definition and subgroup size, metric aggregation details beyond the supplied labels, case-level variability, and prediction-probability availability. These limit reproducibility or subsequent analysis but do not prevent faithful reporting of the supplied summary. Do not fill them in during rendering.

## Intended artifact and owner sequence

- Requested final format: concise, formal advisor-facing PDF, with a short comparison table and a clear next decision.
- Suggested target: `advisor_research_update.pdf` alongside this handoff; this filename is prospective and the file has not been created.
- Layout intent: a readable, compact report, preferably one page if legible. No fixed page count or venue template was supplied. Keep caption, table, and explanatory note together where practical; do not shrink text or delete limitations to meet the suggested length.
- Current route: Research Authoring coordinator → research-reporting → source-only fidelity/scientific-prose review → downstream handoff.
- Required downstream route: an integrated surface explicitly admitting `render-chinese-math-pdf` (`skills/tools/documents-media/render-chinese-math-pdf`) after Research Authoring handoff. Globally installed renderer availability alone does not admit that route for this standalone task.
- Renderer ownership: fonts, layout, compilation, PDF creation, preview, page inspection, and PDF-derived QA. Research Authoring resumes after rendering for final scientific QA.
- No PDF was created, compiled, opened, previewed, rasterized, or checked in this run. Generic compute was used only for source files and source-only checks.

## Downstream acceptance checks

1. Render the canonical report after route admission; save the PDF and renderer evidence under the requested output directory.
2. Inspect every page for legible text and table, clipping, overlaps, missing glyphs, awkward pagination, and the minus sign in the HD95 change. Verify fonts and text extraction through the admitted renderer's workflow.
3. Recheck all six original metric values, three derived differences, 18-volume denominator, method names, fixed preprocessing, same-split scope, and mm units against the source.
4. Confirm the severe-motion failure case, small validation-only limitation, absence of calibration evidence, conditional proposal, and advisor question remain visible and unchanged in strength.
5. Confirm Table 1 and its caption are intact; no invented references, institutional metadata, significance claims, or internal QA text entered the PDF.
6. Return the actual PDF with its path/hash and renderer QA evidence to Research Authoring for final scientific acceptance. Until then, PDF production, layout QA, and post-render scientific QA remain pending.
