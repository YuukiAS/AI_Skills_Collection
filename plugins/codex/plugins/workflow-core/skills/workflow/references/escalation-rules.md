# Failure Escalation Rules

Use these rules when a simple method fails, a baseline gives weak results, or an artifact exists but does not meet the target.

## General rules

- Simple rerun fails -> inspect the real error, log, config, environment, inputs, and working directory. Do not rerun blindly.
- Smoke works but target is unmet -> run targeted real validation against the acceptance criterion.
- Baseline method is weak -> try a stronger valid method or report `blocked_target_not_met` with evidence.
- PDF/page/artifact exists but QA fails -> report `qa_failed`, not `complete`.
- Stronger method needs expensive compute, destructive action, network, secrets, or approval -> stop with `blocked` and state the required approval.

## Domain escalation examples

- Registration or segmentation weak results -> use the relevant medical imaging domain skill for stronger baselines, geometry checks, surface metrics, Jacobian/folding checks, or learning/classical alternatives.
- Training pipeline weak metric -> inspect data splits, evaluator contract, logs, checkpoint/prediction paths, baseline, and target metric before claiming completion.
- Bayesian inference or simulation weak result -> use Bayesian domain skills for model assumptions, convergence diagnostics, prior/posterior predictive checks, sensitivity, and replication uncertainty.
- Rendered writing artifact fails -> use writing-fidelity and document/PDF skills for protected spans, render QA, and honest completion states.
