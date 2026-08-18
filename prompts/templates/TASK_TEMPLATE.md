---
task_key: "000_short_task"
project: "project-name"
status: "READY"
task_type: "execution"
controller_mode: false
planner: "ChatGPT/GPT thread"
strategic_controller: "user-supervised GPT thread"
execution_controller: "none"
executor: "Codex executor session"
auditor: "ChatGPT reviewer"
review_required: false
risk_level: "low"
mechanism_class: "general"
promotion_gate: "Task goal met with result evidence; independent review optional for low risk."
failure_escalation_policy: "Stop on missing permission, missing evidence, or out-of-scope direction; return to GPT planner for new direction."
forbidden_substitutes: []
required_evidence: []
allowed_next_states: ["EXECUTED_UNAUDITED", "NEEDS_EVIDENCE", "NEEDS_REVISION", "NEEDS_HUMAN_APPROVAL", "NEEDS_GPT_PLANNER", "STOP"]
auto_git_commit: true
auto_git_push: true
allow_code_change: false
allow_shell_command: true
allow_network: false
allow_external_upload: false
requires_human_approval: false
---

# Task 000 Short Task

This is the normal execution-task template. For controller tasks, use
`CONTROLLER_TASK_TEMPLATE.md` or set `task_type: "controller"` and fill the
controller sections explicitly.

## Goal

State the single outcome Codex must complete.

## Background

Explain why this task exists and list the exact files, directories, notes,
issues, or artifacts that are in scope. Do not place long research notes in this
task; reference their paths instead.

## Mechanism Class And Completion Definition

- Mechanism class:
- Completion definition:
- Promotion gate:

For medium/high risk tasks, define what evidence proves the mechanism worked.
Executor self-assessment is not final completion.

## Allowed Actions

- Read files directly related to this task.
- Run authorized low-risk shell commands.
- Modify files only when `allow_code_change: true`.
- Write `results/000_short_task/result.md`.
- Write `results/000_short_task/MANIFEST.md` when creating or updating
  `results/000_short_task/`.

## Forbidden Actions

- Do not use the network unless `allow_network: true`.
- Do not upload anything unless `allow_external_upload: true`.
- Do not delete data unless explicitly authorized.
- Do not expand into unrelated refactors or optimizations.
- Do not execute unreferenced `docs/notes/` or `docs/wiki/` material.
- Do not treat `result.md` as the final audited status when review is required.

## Forbidden Substitutes

- List routes that would look like progress but would not satisfy this task.
- For low-risk tasks, write `none` if there are no special forbidden
  substitutes.

## Required Evidence

- Files read:
- Files changed:
- Commands and exit statuses:
- Tests or validation:
- Artifact paths:
- Claims to audit:

For low-risk tasks this can be short. For medium/high risk or controller tasks,
make it explicit before execution starts.

## Review Requirements

- `review_required`:
- Auditor:
- Review path: `results/000_short_task/review.md`
- Audit decision enum, if required:
  `AUDITED_GO`, `NEEDS_EVIDENCE`, `NEEDS_REVISION`,
  `NEEDS_HUMAN_APPROVAL`, `NEEDS_GPT_PLANNER`, `STOP`

If this is an execution task with `review_required: true`, Codex executor must
stop at `EXECUTED_UNAUDITED` after writing result.

## Subtask / Subsession Orchestration

For normal execution tasks, write `none`.

For controller tasks, specify how the Codex execution controller should create
or launch separate executor and auditor sessions. If the runtime cannot launch
subagents automatically, require prompt files under:

```text
results/000_short_task/subagents/
```

and set state to `NEEDS_SUBAGENT_LAUNCH` or `NEEDS_HUMAN_APPROVAL`.

## Expected Output

- `results/000_short_task/result.md`
- `results/000_short_task/MANIFEST.md`
- Any generated artifacts under `results/000_short_task/`
- If code changed, a concise diff summary.
- If commands ran, command, purpose, result, and exit status.
- Claim lines in result using `claim.<name>: <description>`.

## Failure Escalation Policy

State what Codex may retry or revise inside this task. GPT planner must define
the fallback before execution starts. If a new direction is needed, Codex must
write `NEEDS_GPT_PLANNER` and stop.

## Git Automatic Commit And Push Policy

Default policy:

- `auto_git_commit: true`
- `auto_git_push: true`

When the promotion gate is satisfied and no human approval is triggered, a
controller should commit and push. A plain executor should only commit/push if
the task explicitly authorizes it without a separate audit requirement. Any
skipped commit or push must be explained in result or controller report.

## Stop Conditions

- Required files are missing.
- An unauthorized action is needed.
- Evidence is insufficient and continuing would expand scope.
- The task needs a new direction from GPT planner.
- The task goal has been met within authorized scope.

## Human Decision Points

- Permission escalation.
- Acceptance of audited result.
- Rollback, stop, or new GPT-authored task.
