# Clustered Interval Calibration And Synthetic Segmentation Robustness

The current engineering result asks whether uncertainty calibration and center shift can be shown in one research update without losing source fidelity.

## Model

The clustered outcome model separates individual variation from center variation. The working model uses \(Y_{ij}=\beta_0+\beta_1T_{ij}+u_j+\varepsilon_{ij}\) with an intra-center component that controls how much naive iid intervals understate uncertainty.

## Quantitative Result

The simulation grid varies center count, ICC, and cluster imbalance. In imbalanced small-G settings, naive iid intervals fall below nominal 95% coverage, while cluster-robust intervals recover toward nominal as the number of centers increases.

## Experiment Design

The design is a typed sequence: choose DGP knobs, draw clustered samples, fit competing interval procedures, then compare coverage, width, and bias against the nominal target.

## Negative Evidence

The small-G, high-ICC, imbalanced condition remains anti-conservative even after robustification. The next check should compare CR2 and wild cluster bootstrap against the current cluster-robust z interval.

## Medical Image Comparison

The segmentation example uses one synthetic slice with input, ground-truth lesion, prediction, and error overlay. The same-case ROI crop is required so the visible false positive and false negative pattern remains inspectable.

## Next Experiment

The next experiment tests whether diverse batch selection changes the fragile coverage region. DPP batch query, random batch, and Mondrian partitioning should be compared before committing to a larger validation run.
