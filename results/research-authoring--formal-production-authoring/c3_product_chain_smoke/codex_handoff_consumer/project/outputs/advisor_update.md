---
title: "Clipping Robustness Update"
geometry: margin=1in
fontsize: 11pt
---

The clipping experiment asks whether a fixed intensity window makes the segmentation preprocessing less sensitive to scanner contrast. In this toy run, the clipped-window setting reached Dice 0.806, compared with 0.781 for the baseline.

| Setting | Dice |
|---|---:|
| Baseline | 0.781 |
| Clipped-window | 0.806 |

This is a small directional gain, not enough to claim method superiority. The useful conclusion is narrower: clipping did not hurt the pipeline in this run and may be worth a three-seed follow-up.

## Next Action

Rerun the same comparison with three seeds, keep the same train/validation split, and add a short error review for cases where lesions touch the field boundary.
