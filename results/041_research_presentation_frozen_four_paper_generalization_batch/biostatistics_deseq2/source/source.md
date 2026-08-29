# Moderated estimation of fold change and dispersion for RNA-seq data with DESeq2

## Identity
Love, Huber, and Anders, Genome Biology 15:550, 2014, DOI 10.1186/s13059-014-0550-8.

## Scientific problem
The paper addresses differential analysis of high-throughput sequencing count data when experiments often have few replicates and gene-wise variance estimates are noisy.

## Negative-binomial GLM
For gene i and sample j, counts K_ij are modeled with a negative binomial distribution, mean mu_ij, dispersion alpha_i, and a logarithmic GLM link for q_ij. Size factors normalize sequencing depth.

## Dispersion shrinkage
DESeq2 first estimates gene-wise dispersions, fits a dispersion-mean trend, and forms final MAP dispersion estimates by shrinking noisy estimates toward the fitted consensus, while preserving outlier behavior when appropriate. Figure 1 is the core visual explanation.

## Fold-change shrinkage
The method shrinks logarithmic fold-change estimates toward zero with strength driven by available information. Low counts, high dispersion, or low degrees of freedom produce stronger shrinkage. Figure 2 explains the difference between MLE and MAP LFC estimates.

## Testing and evaluation
DESeq2 uses Wald tests for coefficients or contrasts and supports non-zero threshold hypotheses. Simulations and real-data reproducibility benchmarks compare sensitivity, precision, false positives, and stability against other RNA-seq methods.

## Limitations and interpretation
The paper is not a generic RNA-seq workflow. Its contribution is empirical-Bayes regularization of dispersion and LFCs inside a negative-binomial GLM framework, plus diagnostics such as rlog and variance stabilization for count data exploration.
