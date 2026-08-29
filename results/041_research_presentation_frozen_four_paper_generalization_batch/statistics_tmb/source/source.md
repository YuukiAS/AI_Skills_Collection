# TMB: Automatic Differentiation and Laplace Approximation

## Identity
Kristensen, Nielsen, Berg, Skaug, and Bell, Journal of Statistical Software 70(5), 2016, DOI 10.18637/jss.v070.i05.

## Scientific problem
The paper targets nonlinear random-effects and latent-variable models where the user can write the negative joint log-likelihood in C++ and let Template Model Builder evaluate the Laplace approximation to the marginal likelihood in R.

## Laplace approximation
Let f(u, theta) be the negative joint log-likelihood of data and random effects. Random effects u are integrated out by a Laplace approximation, and the optimizer minimizes the negative log of the approximated marginal likelihood. The paper emphasizes that objective values and derivatives with respect to theta are required for standard nonlinear optimizers.

## Automatic differentiation mechanism
CppAD records the user template as a tape. TMB differentiates the joint likelihood and the Laplace objective up to the derivatives required by the optimizer and uncertainty calculations. The paper explains the cheap-gradient property for the Laplace approximation and keeps sparse matrix calculations central.

## R and C++ workflow
The package design has the user template defining the negative joint likelihood, R controlling the top-level workflow, TMB constructing tapes and sparse derivatives, and the optimizer using obj$fn and obj$gr. Figure 3 is the paper's package-design map.

## Case studies and performance
The case studies compare TMB and ADMB across random-effects models. Tables 2-5 and Figure 5 show that models with random effects can be one to two orders of magnitude faster in TMB, while models without random effects are similar.

## Limitations and interpretation
The paper positions TMB as a general random-effects tool when the Laplace approximation is appropriate. The user still needs to encode a correct joint likelihood and understand when the approximation and sparse assumptions are scientifically defensible.
