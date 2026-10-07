# Raw Research Notes For Report Cases

Project: compact lesion-segmentation reliability check.

Audience: advisor deciding whether the next week should prioritize calibration or model architecture.

Observed evidence:

- Dataset: 18 validation volumes from the internal development split.
- Baseline model: nnU-Net style 3D U-Net, fixed preprocessing, same split for all rows.
- Candidate method: baseline plus test-time intensity percentile clipping.
- Mean Dice: baseline 0.742; candidate 0.758.
- Small-lesion Dice: baseline 0.421; candidate 0.469.
- HD95: baseline 18.4 mm; candidate 17.9 mm.
- Failure case: one scan with severe motion still has disconnected false positives under both methods.
- Interpretation boundary: the candidate is promising for small lesions, but this is a small validation-only check and not a final benchmark.
- Advisor decision needed: whether to run a calibration analysis before changing architecture.

Formatting preference: concise advisor-facing technical report with a short comparison table and a clear next decision.
