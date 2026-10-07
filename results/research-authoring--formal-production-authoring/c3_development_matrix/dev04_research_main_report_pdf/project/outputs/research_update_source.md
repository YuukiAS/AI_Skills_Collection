---
title: "Compact Lesion-Segmentation Reliability Check"
subtitle: "Advisor-facing research update"
author: "Project update prepared from report_notes.md"
geometry: margin=1in
fontsize: 11pt
linestretch: 1.08
---

# Compact Lesion-Segmentation Reliability Check

## Decision point

The current question is whether next week's effort should focus on calibration analysis before changing the segmentation architecture. On the internal development validation split, test-time intensity percentile clipping gives a small overall gain and a larger gain on small lesions, but it does not remove the main visible failure mode.

## Evidence available

All rows use the same 18 validation volumes, fixed preprocessing, and the same development split. Here, "Baseline" denotes the nnU-Net style 3D U-Net, and "Candidate clipping" denotes the same model with test-time intensity percentile clipping.

| Method | Mean Dice (higher is better) | Small-lesion Dice (higher is better) | HD95, mm (lower is better) |
|---|---:|---:|---:|
| Baseline | 0.742 | 0.421 | 18.4 |
| Candidate clipping | 0.758 | 0.469 | 17.9 |
| Change | +0.016 | +0.048 | -0.5 |

## Interpretation

The candidate is most promising for small lesions. The small-lesion Dice increase is larger than the overall Dice increase, which suggests that clipping may be helping a reliability-sensitive part of the task rather than only shifting the aggregate score. HD95 also moves in the expected direction, but the change is modest.

The evidence does not yet support an architecture change. The check is validation-only, limited to 18 volumes, and does not include calibration, external validation, or repeated runs. One scan with severe motion still produces disconnected false positives under both methods, so the current candidate does not resolve the clearest failure case.

## Recommended next step

Run a calibration analysis before changing architecture. The calibration pass should test whether percentile clipping improves confidence behavior and failure-case triage, especially for small lesions and motion-corrupted scans. If calibration shows better uncertainty alignment without introducing new failure modes, the clipping step is a low-cost candidate to keep. If calibration remains poor or the severe-motion false positives persist, the next architecture work should target false-positive control rather than a broad model redesign.

## Evidence boundary

This is a compact reliability check, not a final benchmark. The current conclusion is limited to the internal development validation split and the metrics listed above. No statistical significance, generalization claim, or final model selection claim is made from this evidence alone.
