# Strain / registration benchmark plan

## Why this stage is special

The pipeline does not use registration as an end in itself. Registration quality matters because it directly perturbs downstream strain phenotypes. That means a backend swap can look visually acceptable while still biasing biomarkers.

## Compare backends on the same subjects

- legacy MIRTK
- ANTsPy classical path
- VoxelMorph or other learning-based candidate

## Minimum outputs to compare

- global longitudinal strain
- global circumferential strain
- global radial strain
- segmental strain distributions
- ED / ES and derived timing landmarks
- contour propagation stability through the cardiac cycle

## Useful diagnostics

- warped contour overlays
- warped segmentation Dice or contour distance
- Jacobian determinant histograms for deformable methods
- frame-to-frame smoothness
- failure-case review, not only median-case metrics

## Migration rule

Keep the old backend available until the new backend:

1. matches or improves phenotype stability
2. does not introduce obvious geometric artifacts
3. preserves output contracts
4. has at least smoke-level automated coverage
