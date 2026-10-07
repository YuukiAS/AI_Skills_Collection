# Lesion-segmentation reliability: validation update

Test-time intensity percentile clipping shows a promising improvement in small-lesion segmentation in the current validation check. The decision for next week is whether to examine calibration before changing the model architecture.

## Comparison and findings

The evaluation used 18 validation volumes from the internal development split. The baseline was an nnU-Net style 3D U-Net with fixed preprocessing. The candidate added test-time intensity percentile clipping to the baseline; both methods used the same split.

**Table 1. Baseline and clipping comparison on the internal validation split.** Changes are candidate minus baseline; Dice changes are absolute differences on the reported scale.

| Metric | Baseline | With clipping | Change | Preferred direction |
| :--- | ---: | ---: | ---: | :--- |
| Mean Dice | 0.742 | 0.758 | +0.016 | Higher |
| Small-lesion Dice | 0.421 | 0.469 | +0.048 | Higher |
| HD95 (mm) | 18.4 | 17.9 | −0.5 | Lower |

The largest absolute Dice gain occurs in the small-lesion measure, while HD95 decreases modestly. One scan with severe motion still has disconnected false positives under both methods, leaving an unresolved failure mode.

## Interpretation and next decision

These results support further evaluation of clipping for small lesions within this development setting. This is a small validation-only check, not a final benchmark. The notes provide no case-level variability or uncertainty estimates, so the consistency of the improvement across volumes remains unknown. The reported overlap and distance metrics do not establish whether model confidence is calibrated.

The proposed next priority is a calibration analysis before an architecture change, subject to advisor agreement and availability of prediction probabilities and reference labels. Its immediate purpose would be to determine whether confidence tracks correctness in the current predictions. Calibration has not yet been evaluated, and the present results do not establish that calibration would resolve the motion-related false positives or remove the need for an architecture change.

**Decision requested:** Should next week's effort prioritize calibration analysis before changing the architecture?
