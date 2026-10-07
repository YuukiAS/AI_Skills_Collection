# Lesion-segmentation reliability: research update

The current validation check supports prioritizing calibration analysis next week before changing the model architecture. Test-time intensity percentile clipping is promising for small lesions, while a persistent motion-related failure leaves reliability unresolved. Calibration itself has not yet been assessed.

We compared an nnU-Net style 3D U-Net baseline with the same model plus test-time intensity percentile clipping on 18 validation volumes from the internal development split. Preprocessing was fixed, and both methods used the same split.

| Metric | Baseline | With intensity clipping |
|---|---:|---:|
| Mean Dice (higher is better) | 0.742 | 0.758 |
| Small-lesion Dice (higher is better) | 0.421 | 0.469 |
| HD95, mm (lower is better) | 18.4 | 17.9 |

The larger absolute Dice gain was in small lesions; the reduction in HD95 was modest. One scan with severe motion still produced disconnected false positives under both methods. These observations support further evaluation of clipping, but the small, validation-only comparison is not a final benchmark. The notes provide no uncertainty estimates or calibration measurements, so they do not establish the consistency of the gains or improved confidence reliability.

The proposed next step is to assess whether prediction confidence tracks segmentation errors for both methods, including the motion-affected scan. This would clarify whether calibration deserves further attention before committing to an architecture change; the current results do not identify miscalibration as the cause of the remaining errors.

**Advisor decision:** Should next week prioritize this calibration analysis before changing architecture?
