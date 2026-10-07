# Post-render Scientific QA Note

Status: PASS

## Scope

This QA note checks the rendered advisor-facing PDF against `report_notes.md` after the PDF build. It does not add new experiments or external evidence.

## Scientific fidelity checks

| Check | Result |
|---|---|
| Dataset size preserved as 18 validation volumes. | PASS |
| Baseline preserved as nnU-Net style 3D U-Net with fixed preprocessing and same split. | PASS |
| Candidate preserved as baseline plus test-time intensity percentile clipping. | PASS |
| Mean Dice preserved: 0.742 baseline, 0.758 candidate, +0.016 absolute change. | PASS |
| Small-lesion Dice preserved: 0.421 baseline, 0.469 candidate, +0.048 absolute change. | PASS |
| HD95 preserved: 18.4 mm baseline, 17.9 mm candidate, -0.5 mm absolute change. | PASS |
| Severe-motion failure case preserved as disconnected false positives under both methods. | PASS |
| Evidence boundary preserved as small validation-only check, not a final benchmark. | PASS |
| Advisor decision preserved as calibration analysis before architecture change. | PASS |

## Overclaim audit

The report does not claim statistical significance, external validation, final model selection, or architecture superiority. The recommendation is bounded to the supplied validation evidence.

## Reader-facing QA

The main body is organized around the scientific decision, comparison evidence, interpretation, and next step. Process details and render mechanics are kept outside the PDF body.
