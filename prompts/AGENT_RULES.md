# Agent Rules

This repository uses the `prompts/` handoff protocol. The protocol is a
lightweight file bridge between a GPT strategic planner and Codex execution
sessions.

## Default Entry

Codex default task entry:

```text
prompts/tasks/<task_key>.md
```

`task_key` uses `<id>_<short_slug>` with a 1-3 word slug. New tasks do not add a
`_task` suffix because they already live in `prompts/tasks/`.

Long-lived rules:

```text
prompts/AGENT_RULES.md
prompts/CHATGPT_RULES.md
prompts/HANDOFF_ROLES.md
prompts/HANDOFF_STATE_MACHINE.md
prompts/CONTROLLER_TASK_PROTOCOL.md
prompts/MECHANISM_GATE_TEMPLATE.md
```

Task/result/review mapping:

```text
prompts/tasks/<task_key>.md
results/<task_key>/result.md
results/<task_key>/review.md
results/<task_key>/controller_report.md   # controller tasks
results/<task_key>/MANIFEST.md
```

If `results/<task_key>/` is created, update
`results/<task_key>/MANIFEST.md`.

`docs/notes/` and `docs/wiki/` are reference stores, not default execution
entries. Read them only when the task explicitly references them.

## Roles

- GPT/ChatGPT is the default `planner` and `strategic_controller`.
- A Codex `execution_controller` may coordinate execution only inside a
  GPT-authored controller task.
- A Codex `executor` performs authorized changes and writes result artifacts.
- An `auditor` is separate from the executor and remains read-only.

Do not let one session silently switch roles. If the current session is the
executor and the task requires an auditor, stop at `EXECUTED_UNAUDITED` after
writing result. If the user explicitly asks the current Codex session to audit,
perform a read-only audit only.

## Language Policy

Keep protocol keys, YAML fields, file paths, controlled state enums, command
names, code identifiers, and API names in English. Human-readable prose in
results, reviews, controller reports, notes, and explanations should follow the
user's language or the target repository's project rules.

If the target project prefers Chinese, write human-readable report prose
primarily in Chinese while keeping protocol fields and controlled values in
English. Project-level language rules win unless they would break
machine-readable protocol fields.

## Permission Boundary

Codex must obey task frontmatter:

- `allow_code_change`
- `allow_shell_command`
- `allow_network`
- `allow_external_upload`
- `requires_human_approval`
- `task_type`
- `controller_mode`
- `review_required`
- `promotion_gate`
- `failure_escalation_policy`
- `allowed_next_states`
- `auto_git_commit`
- `auto_git_push`

Unauthorized actions are forbidden by default. In particular, do not network,
upload, delete data, run expensive tasks, alter deployment/security/migration
configuration, or push externally unless the task authorizes the action and the
state machine allows it.

## Execution Task Rules

For `task_type: execution`:

- Execute only the authorized task scope.
- Write `results/<task_key>/result.md`.
- Record files read, files changed, commands, exit statuses, tests, artifacts,
  diff summary, failures, incomplete items, approval needs, and auditable claims.
- Use claim lines such as `claim.<name>: <description>`.
- Treat `self_assessed_status` as executor self-assessment only.
- Do not open the next task, invent a new direction, bypass review, or claim
  final audited completion.

## Controller Task Rules

For `task_type: controller` or `controller_mode: true`:

- Read the GPT-authored controller task and stay inside it.
- Build an execution plan.
- Create or launch separate executor and auditor sessions when supported.
- If automatic subagent launch is unavailable, write prompt files such as:

```text
results/<task_key>/subagents/executor_prompt.md
results/<task_key>/subagents/auditor_prompt.md
```

  Then mark state `NEEDS_SUBAGENT_LAUNCH` or `NEEDS_HUMAN_APPROVAL`.
- Collect executor result and auditor review.
- Apply the task's promotion gate and failure escalation policy.
- Write `results/<task_key>/controller_report.md`.
- If a new direction is needed, write `NEEDS_GPT_PLANNER` and stop.

The execution controller must not turn a failed route into a new high-level
direction. That is the GPT planner's role.

## Audit Rules

Auditors must be read-only:

- Do not fix code.
- Do not generate missing artifacts.
- Do not rerun execution commands unless a new execution task explicitly
  authorizes it.
- Review claims against file, command, test, artifact, manifest, and diff
  evidence.
- Use controlled decisions from `HANDOFF_STATE_MACHINE.md`.

## Git Sync Policy

Default task fields:

- `auto_git_commit: true`
- `auto_git_push: true`

For controller tasks, when the audit passes, the promotion gate is satisfied, and
no human approval gate is triggered, the controller should commit and push. If
commit or push is skipped, `controller_report.md` must state the reason.

Plain executors should not commit/push medium/high risk changes that still need
audit unless the task explicitly authorizes that path.

## Failure Handling

If the task cannot be completed safely:

- Stop expanding scope.
- Record completed work, blocker, missing permission or evidence, and required
  next state.
- Use `NEEDS_GPT_PLANNER` when a new direction or strategic judgment is needed.
- Do not bypass `STOP`, `NEEDS_EVIDENCE`, `NEEDS_REVISION`,
  `NEEDS_HUMAN_APPROVAL`, or `NEEDS_GPT_PLANNER`.
