# Public-safe research update source

## Question

Does a fixed intensity-clipping preprocessing step improve a baseline 3D lesion-segmentation model enough to justify a larger replicated study?

## Study design

- Public-safe synthetic evaluation summary prepared for release acceptance.
- Eighteen validation volumes.
- The baseline and candidate use the same split, model architecture, training schedule, and post-processing.
- The only intended difference is test-time intensity clipping at the 1st and 99th percentiles.
- This is a small validation study, not a final benchmark or clinical claim.

## Results

| Metric | Baseline | Intensity clipping |
|---|---:|---:|
| Mean Dice | 0.742 | 0.758 |
| Small-lesion Dice | 0.421 | 0.469 |
| HD95 | 18.4 mm | 17.9 mm |

## Failure and uncertainty

- One motion-corrupted volume still has disconnected false positives under both methods.
- No confidence interval or repeated-seed estimate is available.
- The observed improvement may depend on this small split.
- The result supports replication, not a superiority claim.

## Proposed next experiment

- Repeat the comparison across three fixed seeds.
- Pre-register the same preprocessing and split policy.
- Report uncertainty for mean Dice, small-lesion Dice, and HD95.
- Audit the motion-corrupted case separately instead of excluding it.

## Decision request

Approve the three-seed replication before changing the model architecture.
