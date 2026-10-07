# Production Handoff and Route Receipt

## Document brief

- Task intent: Prepare a concise advisor-facing research update from `report_notes.md` and deliver a formal readable PDF.
- Audience: Advisor deciding whether the next week should prioritize calibration or model architecture.
- Document family: Report-family research update.
- Source authority: `report_notes.md` only; no external papers, logs, figures, or additional benchmarks were used.
- Evidence boundary: 18 validation volumes from the internal development split; same split and fixed preprocessing for baseline and candidate; validation-only reliability check.
- Main claim: Test-time intensity percentile clipping is promising for small lesions but does not yet justify changing architecture.
- Weak or conditional claims: The candidate may help reliability-sensitive small-lesion behavior; this remains limited by small validation-only evidence.
- Limitation to preserve: Severe-motion scan still has disconnected false positives under both methods.
- Advisor decision requested: Run calibration analysis before architecture changes.

## Claim-evidence map

| Claim | Evidence anchor | Boundary |
|---|---|---|
| Candidate improves aggregate segmentation modestly. | Mean Dice 0.742 to 0.758. | Same 18 validation volumes only. |
| Candidate improves small-lesion Dice more than aggregate Dice. | Small-lesion Dice 0.421 to 0.469. | No per-lesion stratification beyond the supplied metric. |
| Boundary accuracy changes modestly in the expected direction. | HD95 18.4 mm to 17.9 mm. | No distributional or case-level HD95 details supplied. |
| Architecture change is premature. | Validation-only check; severe-motion false positives persist under both methods. | This is a recommendation, not a completed benchmark conclusion. |

## Authoring route

- Research owner: `research-authoring-core` then `research-reporting`.
- Fidelity guardrail: `writing-fidelity` used to preserve supplied numbers, comparators, methods, limitations, and requested decision.
- English style pass: `scientific-prose` rules applied to keep claims bounded and advisor-facing.
- Renderer owner: `render-chinese-math-pdf` admitted for the explicit final-PDF request after research source stabilization.

## Renderer route

- Source: `outputs/research_update_source.md`
- Target PDF: `outputs/advisor_research_update.pdf`
- Route: Markdown -> Pandoc -> XeLaTeX -> PDF
- Engine: `xelatex`
- Paper/layout: default Pandoc article route with 1 inch margins, 11 pt font, line stretch 1.08.
- Font selection: TeX/Pandoc default Latin fonts through XeLaTeX; the source is English-only and contains no CJK or mathematical glyph stress.
- QA evidence: recorded in `outputs/render_evidence.md`.

## Post-render scientific QA requirements

- Verify that all metric values and directions match `report_notes.md`.
- Verify that the PDF preserves the advisor decision point.
- Verify that no significance, external-validation, or final-benchmark claim was introduced.
- Verify that the severe-motion failure case remains visible.
