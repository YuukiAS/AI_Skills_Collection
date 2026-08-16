# References: Bayesian PPL and diagnostics

## Stan / brms (canonical)

- **Stan: A Probabilistic Programming Language** — Carpenter et al., *Journal of Statistical Software*, 2017. DOI: [10.18637/jss.v076.i01](https://doi.org/10.18637/jss.v076.i01)  
- **brms: An R Package for Bayesian Multilevel Models Using Stan** — Bürkner, *Journal of Statistical Software*, 2017. DOI: [10.18637/jss.v080.i01](https://doi.org/10.18637/jss.v080.i01)

## PyMC (canonical + classic)

- **PyMC: a modern, and comprehensive probabilistic programming framework in Python** — *PeerJ Computer Science*, 2023. DOI: [10.7717/peerj-cs.1516](https://doi.org/10.7717/peerj-cs.1516)  
- **Probabilistic programming in Python using PyMC3** — Salvatier et al., *PeerJ Computer Science*, 2016. DOI: [10.7717/peerj-cs.55](https://doi.org/10.7717/peerj-cs.55) (historical PyMC3; useful for legacy notebooks)

## ArviZ

- **ArviZ a unified library for exploratory analysis of Bayesian models in Python** — Kumar et al., *JOSS*, 2019. DOI: [10.21105/joss.01143](https://doi.org/10.21105/joss.01143)

## CmdStanPy / Stan docs (documentation-first)

- CmdStanPy: [https://mc-stan.org/cmdstanpy/](https://mc-stan.org/cmdstanpy/)  
- Stan Reference Manual / User’s Guide: [https://mc-stan.org/users/documentation/](https://mc-stan.org/users/documentation/)  
- Prefer **official documentation** as the primary citable surface for CmdStanPy usage (no single “CmdStanPy paper” required).

## JAGS / BUGS interfaces (legacy ecosystem)

- JAGS manual / project: [https://mcmc-jags.sourceforge.net/](https://mcmc-jags.sourceforge.net/)  
- **R2jags** (CRAN): [https://CRAN.R-project.org/package=R2jags](https://CRAN.R-project.org/package=R2jags)  
- OpenBUGS: [http://www.openbugs.net/](http://www.openbugs.net/)  
- WinBUGS (legacy): [https://www.mrc-bsu.cam.ac.uk/software/bugs/the-bugs-project-winbugs/](https://www.mrc-bsu.cam.ac.uk/software/bugs/the-bugs-project-winbugs/)  
- **BUGS ecosystem overview (historical context for WinBUGS/OpenBUGS/JAGS):** Lunn et al., *Statistics in Medicine*, 2009. DOI: [10.1002/sim.3680](https://doi.org/10.1002/sim.3680)

## Rcpp

- **Rcpp: Seamless R and C++ Integration** — Eddelbuettel & François, *Journal of Statistical Software*, 2011. DOI: [10.18637/jss.v040.i08](https://doi.org/10.18637/jss.v040.i08)  
- Rcpp site: [https://www.rcpp.org/](https://www.rcpp.org/)

## Diagnostics & workflow (optional further reading)

- Simulation-based calibration: see Stan case studies and recent statistics literature; implement with generated quantities and ranked checks—treat as **pipeline validation**, not a replacement for per-run R-hat/ESS.
