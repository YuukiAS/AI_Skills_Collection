# Compact Manuscript Source Package

This package contains a preliminary manuscript draft for:

`Intensity-Clipping Robustness for Compact Lesion Segmentation`

## Contents

- `paper.tex`: canonical LaTeX manuscript source.

## Evidence Boundary

The source is based only on `manuscript_notes.md`.

Protected facts:

- internal validation split: 18 volumes;
- method change: test-time percentile clipping before an existing 3D U-Net inference pipeline;
- small-lesion Dice: 0.421 to 0.469;
- mean Dice: 0.742 to 0.758;
- HD95: 18.4 mm to 17.9 mm;
- motion-corrupted scan remains a failure case;
- no external citations, datasets, venue requirements, reviewer comments, or additional experiments are supplied.

## Build Route

Expected local build command:

```bash
pdflatex -interaction=nonstopmode -halt-on-error paper.tex
pdflatex -interaction=nonstopmode -halt-on-error paper.tex
```

The final PDF generated for this task is saved outside the package as:

`outputs/intensity_clipping_robustness_manuscript.pdf`

## Submission Readiness

This is a compact manuscript source package, not a venue-ready submission. Before submission, a downstream production pass must verify exact clipping thresholds, dataset/split details, citation support, venue template requirements, and final layout.
