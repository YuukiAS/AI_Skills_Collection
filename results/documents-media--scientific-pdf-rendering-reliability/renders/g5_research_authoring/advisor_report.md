# Regularized Regression as a Candidate Baseline

## Scientific Question

Is a simple regularized model a reasonable baseline before a larger
experiment? This note considers a synthetic, public-safe prediction example
to support a narrow decision about the next comparison set.

The running example is a prediction problem with paired observations
$(x_i, y_i)$, where $x_i \in \mathbb{R}^{p}$ and $y_i$ is a continuous endpoint.
The baseline estimator solves

$$
\hat{\theta}_0 =
\operatorname*{argmin}_{\theta \in \mathbb{R}^{p}}
\frac{1}{n}\sum_{i=1}^{n}(y_i - x_i^\top\theta)^2.
$$

The regularized candidate uses

$$
\hat{\theta}_\lambda =
\operatorname*{argmin}_{\theta \in \mathbb{R}^{p}}
\left[
\frac{1}{n}\sum_{i=1}^{n}(y_i - x_i^\top\theta)^2
+ \lambda \|\theta\|_2^2
\right].
$$

## Evidence Design

The comparison is intentionally small. It is meant to check rendering and
decision structure, not to claim a scientific discovery. We evaluate two
synthetic folds, report root mean squared error, and inspect whether the
regularized model is consistently lower without hiding the uncertainty.

| Fold | Baseline RMSE | Regularized RMSE | Delta | Interpretation |
| --- | ---: | ---: | ---: | --- |
| A | 1.42 | 1.18 | -0.24 | regularization helps |
| B | 1.36 | 1.29 | -0.07 | effect is smaller |
| Mean | 1.39 | 1.235 | -0.155 | promising but limited |

The average reduction is

$$
\Delta_{\mathrm{mean}} =
\frac{1}{2}\sum_{k \in \{A,B\}}
\left(\mathrm{RMSE}_{\lambda,k} - \mathrm{RMSE}_{0,k}\right)
= -0.155.
$$

## Interpretation

The result supports using the regularized model as a conservative baseline in a
larger experiment. It does not justify a claim that the regularized model is
optimal, and it does not distinguish whether the improvement comes from variance
reduction, implicit feature weighting, or fold-specific noise. The advisor
decision is therefore narrow: keep the regularized model in the next comparison
set, but do not make it the final method.

The main caveat is that two folds are not enough to estimate variability. A
larger run should include at least five folds or repeated random splits, and the
report should show the distribution of fold-level differences rather than only
the mean. If the next run still shows a negative mean delta and no severe
outlier fold, the method is worth using as the default baseline.
