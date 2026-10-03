# Failure Escalation Rules

Use these rules when a baseline, smoke test, or simple method fails or produces weak evidence.

## General Rules

- Simple rerun fails: inspect the real error, log, config, inputs, and working directory before trying again.
- Smoke works but target is unmet: run validation against the real acceptance criterion.
- Baseline is weak: try a stronger valid method from the relevant specialist skill or report `blocked_target_not_met`.
- Artifact exists but QA fails: report `qa_failed`, not `complete`.
- Stronger method needs expensive compute, destructive action, network, secrets, publication, or user approval: stop with `blocked` and state the exact approval needed.
- Missing default `PATH` tools, failed optional modes, or local flag errors are not capability-absent evidence until the matched specialist probe/resource/wrapper and the project-declared runtime have been checked.
- Repo-local build, check, render, QA, and deterministic validation that fit the workspace must use the workspace normal entry before any broader authority route.
- Optional cleanup, cache pruning, convenience publication, or housekeeping does not become required merely because it failed or needs higher privilege.
- Approval-sensitive recovery must be six-dimension-equivalent: preserve the frozen effect, professional quality, evidence strength, safety/privacy, artifact identity, and authorization scope without increasing privilege. If any dimension is unknown or changed, fail closed.
- Repeated approval rejection or a plan to retry through an equal-or-higher privilege route requires route reassessment first; changing shells, wrappers, command spelling, or escalation flags is not new information.
- Bounded/canonical publication or transport failure blocks only that effect when local build, render, QA, artifact, or commit evidence is already valid. Do not replace it with a raw broader route or relabel the local evidence as failed.

## Specialist Boundary

Escalation methods must come from the relevant specialist workflow, project contract, or user-approved plan. Verified Workflow decides when escalation is required; it does not define domain-specific commands or policies.
