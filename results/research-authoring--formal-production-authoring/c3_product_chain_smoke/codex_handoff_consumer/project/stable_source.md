# Advisor update source

Audience: imaging methods advisor.

Purpose: produce a one-page PDF update from already stabilized Research Authoring source.

Evidence authority:

- The toy experiment tested intensity clipping robustness for a segmentation preprocessing step.
- Baseline Dice was 0.781.
- Clipped-window Dice was 0.806.
- The observed improvement is small and should be described as directional, not conclusive.
- The next action is to rerun with three seeds and report failure cases.

Allowed edit scope: production formatting, equation/table cleanup, and file QA only. Do not add new scientific claims.

## Draft body

The clipping experiment asks whether a fixed intensity window makes the segmentation preprocessing less sensitive to scanner contrast. In this toy run, the clipped-window setting reached Dice 0.806, compared with 0.781 for the baseline.

This is a small directional gain, not enough to claim method superiority. The useful conclusion is narrower: clipping did not hurt the pipeline in this run and may be worth a three-seed follow-up.

Next, rerun the same comparison with three seeds, keep the same train/validation split, and add a short error review for cases where lesions touch the field boundary.
