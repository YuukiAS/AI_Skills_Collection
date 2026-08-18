---
task_key: "000_controller_task"
project: "project-name"
status: "READY"
task_type: "controller"
controller_mode: true
planner: "ChatGPT/GPT thread"
strategic_controller: "user-supervised GPT thread"
execution_controller: "Codex controller session"
executor: "Codex executor session"
auditor: "separate Codex auditor session"
review_required: true
mechanism_class: "general"
promotion_gate: "All required evidence is present, auditor marks required claims SUPPORTED, and no human approval gate is triggered."
failure_escalation_policy: "Escalate only within the explicit fallback steps below; otherwise write NEEDS_GPT_PLANNER and stop."
forbidden_substitutes: []
required_evidence: []
allowed_next_states: ["EXECUTION_PLANNED", "EXECUTOR_RUNNING", "EXECUTED_UNAUDITED", "AUDITOR_RUNNING", "AUDITED_GO", "NEEDS_EVIDENCE", "NEEDS_REVISION", "NEEDS_HUMAN_APPROVAL", "NEEDS_SUBAGENT_LAUNCH", "NEEDS_GPT_PLANNER", "STOP"]
auto_git_commit: true
auto_git_push: true
allow_code_change: true
allow_shell_command: true
allow_network: false
allow_external_upload: false
requires_human_approval: false
controller_report: "results/000_controller_task/controller_report.md"
---

# Controller Task 000

## Goal

State the exact outcome the GPT planner wants the Codex execution controller to
coordinate.

## Mechanism Class And Completion Definition

- Mechanism class:
- Completion definition:
- Promotion gate:

## Scope

The execution controller may plan executor/auditor subtasks only inside this
scope. It must not search for a new direction or replace the task goal.

## Forbidden Substitutes

- Do not replace the goal with a different route unless the failure escalation
  policy explicitly allows it.
- Do not count executor self-assessment as final completion.
- Do not skip the auditor when `review_required: true`.

## Required Evidence

- Executor result at `results/000_controller_task/subagents/executor_result.md`
  or another path listed in the controller report.
- Auditor review at `results/000_controller_task/subagents/auditor_review.md`
  or another path listed in the controller report.
- Controller report at `results/000_controller_task/controller_report.md`.
- Command/test evidence with exit status.
- Diff and artifact evidence where relevant.

## Subtask / Subsession Orchestration

1. Write or launch an executor prompt.
2. Collect executor result and artifacts.
3. Write or launch a separate read-only auditor prompt.
4. Collect auditor review and claim ledger.
5. Decide whether the promotion gate is satisfied.
6. Write controller report.

If new Codex sessions/subagents cannot be launched automatically, write:

```text
results/000_controller_task/subagents/executor_prompt.md
results/000_controller_task/subagents/auditor_prompt.md
```

Then set state to `NEEDS_SUBAGENT_LAUNCH` or `NEEDS_HUMAN_APPROVAL`.

## Failure Escalation Policy

Define what the execution controller may retry or revise inside this task. If a
new direction is needed, write `NEEDS_GPT_PLANNER` in the controller report and
stop.

## Git Automatic Commit And Push Policy

If the audit passes, the promotion gate is satisfied, and no human approval gate
is triggered:

- commit approved changes when `auto_git_commit: true`
- push to the configured remote when `auto_git_push: true`

If commit or push is skipped, the controller report must state the reason.

## Required Output

- `results/000_controller_task/controller_report.md`
- executor prompt/result paths
- auditor prompt/review paths
- `results/000_controller_task/MANIFEST.md`
