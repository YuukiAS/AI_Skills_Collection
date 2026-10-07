# Post-render Scientific QA Note

Status: complete.

## Source and artifact checked

- Source notes: `report_notes.md`.
- Final source: `outputs/research_update.md`.
- Final PDF: `outputs/research_update.pdf`.
- Renderer evidence: `outputs/renderer_evidence.md`.

## Fidelity checks

- Dataset boundary preserved: 18 validation volumes from the internal development split.
- Method boundary preserved: baseline nnU-Net-style 3D U-Net with fixed preprocessing and same split; candidate adds test-time intensity percentile clipping.
- Metric values preserved: mean Dice 0.742 vs 0.758; small-lesion Dice 0.421 vs 0.469; HD95 18.4 mm vs 17.9 mm.
- Metric direction stated: Dice higher-is-better; HD95 lower-is-better.
- Failure case preserved: one severe-motion scan still has disconnected false positives under both methods.
- Interpretation boundary preserved: promising for small lesions, but validation-only and not a final benchmark.
- Advisor decision preserved: whether to run calibration analysis before changing architecture.

## Claim-strength QA

- The report states the metric changes as observed evidence, not as proof of generalization.
- The recommendation to prioritize calibration is framed as a next-step decision, not as a completed scientific conclusion.
- No external citations, additional datasets, statistical significance claims, or unreported experiments were invented.
- Internal render/cache details are kept out of the advisor-facing PDF and only recorded in `outputs/renderer_evidence.md`.

## Post-render readability QA

The rendered PDF is a one-page advisor-facing update with a compact comparison table and a clear decision question. Visual inspection of `outputs/research_update_page1.png` found no clipping, overlap, unreadable table layout, or stray build-log text.
