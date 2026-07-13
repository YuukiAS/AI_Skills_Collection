# Failure Escalation Rules

Use these rules when a baseline, smoke test, or simple method fails or produces weak evidence.

## General Rules

- Simple rerun fails: inspect the real error, log, config, inputs, and working directory before trying again.
- Smoke works but target is unmet: run validation against the real acceptance criterion.
- Baseline is weak: try a stronger valid method from the relevant specialist skill or report `blocked_target_not_met`.
- Artifact exists but QA fails: report `qa_failed`, not `complete`.
- Stronger method needs expensive compute, destructive action, network, secrets, publication, or user approval: stop with `blocked` and state the exact approval needed.

## Specialist Boundary

Escalation methods must come from the relevant specialist workflow, project contract, or user-approved plan. Workflow Core decides when escalation is required; it does not define domain-specific commands or policies.
