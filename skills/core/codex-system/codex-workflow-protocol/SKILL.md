---
name: codex-workflow-protocol
description: Use for complex or risky Codex tasks that require source-of-truth discovery, phased planning, specialist routing, gate-driven verification, live-state supervision, integration ownership, or honest final status reporting.
status: active
provenance: user-authored
trusted: false
requires_network: false
writes_files: true
executes_code: false
secrets_needed:
last_reviewed: 2026-07-13
profile_tags:
  - global
  - workflow
  - codex
recommended_scope: global
display_name: Workflow Core
short_description: Process layer for complex Codex work.
icon_small: assets/workflow-core.svg
icon_large: assets/workflow-core.svg
default_prompt:
  - Run the full source-of-truth, implementation, verification, and reporting workflow.
---
# Codex Workflow Protocol

## Trigger Boundary

Use this skill when the task is complex or risky because it has one or more of these properties:

- multi-phase implementation or execution;
- cross-file, cross-system, generated-layer, deployment, or repository-wide changes;
- explicit acceptance gates, metrics, rendered artifacts, live state, or release/commit boundaries;
- delegation to sub-agents, long-running work, external services, or repeated verification;
- failure could corrupt code, data, research conclusions, publication artifacts, or user-visible releases;
- the user asks for end-to-end execution with evidence rather than a single explanation.

Do not trigger this skill only because the prompt mentions a specific tool, format, or platform. Simple compilation, one-command help, a short wording pass, a single scheduler header, or a casual explanation should route directly to the relevant specialist skill or ordinary answer.

## Non-Negotiable Rule

Do not claim completion without evidence from the current source of truth and the task's real acceptance gates.

Smoke tests, dry runs, preflights, successful compilation, file existence, job submission, HTTP 200, child-agent launch, or old status files are intermediate evidence. They are final only when the user explicitly asked for that intermediate check.

## Specialist Routing Contract

This skill owns process only:

1. discover source-of-truth files and live state;
2. protect existing user work and dirty-tree boundaries;
3. define phases, owners, and acceptance gates;
4. route domain work to the right specialist skill;
5. monitor execution and delegation;
6. integrate results and verify the final state;
7. report precise completion, partial completion, failure, or blocking state.

Specialist skills own technical rules for their domain. They may add stricter checks, commands, schemas, or quality gates. They must not weaken the global completion boundary. Workflow Core must not override a specialist's technical instructions.

## Workflow

1. Read source-of-truth instructions, repository state, relevant skills, configs, tests, and current artifacts before acting.
2. Separate discoverable facts from preferences; ask only for decisions that cannot be derived safely.
3. Define task-owned files, generated files, pre-existing dirty files, and forbidden changes.
4. Route specialist work explicitly, then follow the specialist's gates.
5. Verify with the strongest practical evidence for the requested outcome.
6. Report status honestly, including skipped checks, residual risk, and required user decisions.

## Final Status Vocabulary

- `complete`: all acceptance criteria met and verified.
- `partial_complete`: useful work exists, but some criteria remain unmet.
- `qa_failed`: an artifact exists but fails quality, validation, rendering, metric, fidelity, or live-state checks.
- `blocked`: external state, permission, dependency, secret, or user decision is required.
- `blocked_target_not_met`: the target cannot be met under current constraints without unacceptable compromise.

## References

- Read `references/task-template.md` when starting a large reusable Codex task or writing a handoff prompt.
- Read `references/verification-matrix.md` for completion gates, dirty-tree handling, and final evidence.
- Read `references/live-state-delegation.md` for long-running work, live state, or sub-agent supervision.
- Read `references/escalation-rules.md` when a baseline, smoke test, or simple method gives weak results.
