# Live-State and Delegation Supervision

Use this reference when the task depends on current process state, current logs, current artifacts, delegated work, or long-running execution.

## Rule

Starting a process, launching a child agent, creating an output path, or finding an old status file is not completion. Verify the current live state and the requested final output.

## Generic Checks

- Identify the owner, run identifier, start time, stop condition, budget, and expected final artifact.
- Compare timestamps of logs, state files, and artifacts against the current run.
- Confirm the latest observable state, not just a cached or stale success marker.
- Keep enough evidence for a later reviewer to distinguish in-progress, failed, stale, and complete states.
- When delegating, define scope, forbidden actions, expected artifact, and final verification owner before launch.

## Specialist Boundary

Use the specialist skill for domain-specific live-state checks. Workflow Core only requires that current state is verified and integrated before completion.

Examples:

- scheduler/job systems: specialist owns queue commands, resource policy, log interpretation, and resubmission rules;
- rendered or generated artifacts: specialist owns rendering commands, validators, and visual/semantic QA;
- frontend or service previews: specialist owns browser, server, console, and client-visible verification;
- sub-agents: the main agent owns integration, diff review, and final acceptance.

## Final Report

Report the current state, evidence paths or identifiers, final artifacts, verification command summaries, and any unverified boundaries.
