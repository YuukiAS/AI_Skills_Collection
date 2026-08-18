# Controller Task Protocol

A controller task lets a Codex execution controller coordinate executor and
auditor work for one GPT-approved task. It does not authorize Codex to become
the strategic planner.

## Required Shape

Controller tasks should include:

- `task_type: "controller"`
- `controller_mode: true`
- `planner: "ChatGPT/GPT thread"`
- `strategic_controller: "user-supervised GPT thread"`
- `execution_controller: "Codex controller session"`
- `executor: "Codex executor session"`
- `auditor: "separate Codex auditor session"` or `ChatGPT reviewer`
- `review_required: true`
- `promotion_gate`
- `failure_escalation_policy`
- `forbidden_substitutes`
- `required_evidence`
- `allowed_next_states`
- `auto_git_commit: true`
- `auto_git_push: true`
- a controller report path, normally
  `results/<task_key>/controller_report.md`

## Subagent Fallback

Do not assume every Codex runtime can open new sessions automatically.

If automatic launch is supported, the controller records:

- launch command
- session id
- prompt path
- log path
- exit status

If automatic launch is not supported, the controller must write files such as:

```text
results/<task_key>/subagents/executor_prompt.md
results/<task_key>/subagents/auditor_prompt.md
```

The controller then marks the state as `NEEDS_SUBAGENT_LAUNCH` or
`NEEDS_HUMAN_APPROVAL`. It must not pretend executor/auditor separation already
happened.

## Controller Report

Controller tasks must end with:

```text
results/<task_key>/controller_report.md
```

The report must include:

- controller task id
- executor subtask list
- auditor subtask list
- prompt, result, and review path for every subtask
- session, command, and log evidence
- claims summary
- audited decision
- promotion decision
- whether automatic commit was executed
- whether automatic push was executed
- incomplete items
- whether GPT planner is needed

When `auto_git_commit: true`, audit passes, and no human approval is triggered,
the controller should commit the approved changes. When `auto_git_push: true`
under the same conditions, it should push to the remote. Not committing or not
pushing requires an explicit reason in the controller report.
