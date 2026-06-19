# Statsmodels Workflow Notes

- Formula models are readable but require explicit reference levels and transformations.
- Check residuals, leverage/influence, heteroskedasticity, autocorrelation, convergence, and separation where relevant.
- Use robust covariance or clustered standard errors when the design requires it.
- For GLM/discrete models, interpret effects on the correct link or response scale.
- For time series, check stationarity, residual autocorrelation, forecast validation, and leakage.
