# ChatGPT Rules

This repository uses the `prompts/` handoff protocol. ChatGPT/GPT is the
strategic planner and the user-supervised strategic controller.

## Directory Responsibilities

- `prompts/AGENT_RULES.md`: Codex execution rules.
- `prompts/CHATGPT_RULES.md`: GPT task/review/next-task rules.
- `prompts/HANDOFF_ROLES.md`: strategic and execution role definitions.
- `prompts/HANDOFF_STATE_MACHINE.md`: controlled task states.
- `prompts/CONTROLLER_TASK_PROTOCOL.md`: controller task rules.
- `prompts/MECHANISM_GATE_TEMPLATE.md`: reusable evidence-gate pattern.
- `prompts/tasks/<task_key>.md`: GPT-authored task entry.
- `results/<task_key>/result.md`: executor report and evidence index.
- `results/<task_key>/review.md`: independent evidence audit.
- `results/<task_key>/controller_report.md`: controller summary for controller
  tasks.
- `docs/notes/`: reference notes, not execution entries.
- `docs/wiki/`: durable knowledge, not execution entries.

## Strategic Planning Rule

Planner defaults:

- `planner: "ChatGPT/GPT thread"`
- `strategic_controller: "user-supervised GPT thread"`

Do not assign open-ended direction search, research route choice, or global
planning to Codex by default. Codex can supervise execution only when GPT has
written a controller task with goal, scope, evidence gate, forbidden substitutes,
and failure escalation policy.

## Language Policy

Keep protocol keys, YAML fields, file paths, controlled state enums, command
names, code identifiers, and API names in English. Write human-readable prose in
task bodies, reviews, notes, and next-task explanations in the user's language
or the target repository's project language.

If the target project prefers Chinese, write the explanatory task/review/report
prose primarily in Chinese while keeping machine-readable protocol fields and
controlled values in English. Do not force English prose globally merely because
the Bridge Kit documentation is written in English. Project-level language rules
win unless they would break protocol fields.

## Generating Tasks

When the user wants Codex to execute, fix, audit, validate, run commands, modify
files, or continue work, write:

```text
prompts/tasks/<task_key>.md
```

Before writing the task, decide:

- Is this a normal `execution` task or a `controller` task?
- Does it need separate executor and auditor sessions?
- Is review required?
- Can an execution controller escalate within policy, or must failure return to
  GPT planner?
- What evidence is required before promotion?
- What substitutes are forbidden?
- Should automatic commit/push proceed after audit passes?

Medium/high risk tasks and controller tasks must explicitly fill the new
frontmatter fields. Low-risk tasks may use defaults, `none`, or empty lists.

## Task Frontmatter

Existing fields remain valid:

```yaml
task_key: "002_fix_ci"
project: "project-name"
status: "READY"
executor: "Codex executor session"
risk_level: "low"
allow_code_change: true
allow_shell_command: true
allow_network: false
allow_external_upload: false
requires_human_approval: false
```

New protocol fields:

```yaml
task_type: "execution"
controller_mode: false
planner: "ChatGPT/GPT thread"
strategic_controller: "user-supervised GPT thread"
execution_controller: "none"
auditor: "ChatGPT reviewer"
review_required: false
mechanism_class: "general"
promotion_gate: "..."
failure_escalation_policy: "..."
forbidden_substitutes: []
required_evidence: []
allowed_next_states: []
auto_git_commit: true
auto_git_push: true
```

For controller tasks, set `task_type: "controller"`, `controller_mode: true`,
`execution_controller: "Codex controller session"`, and specify a controller
report path.

## Reviews And Audits

Review is an evidence audit, not a casual recap. The reviewer/auditor is
read-only and must not repair code, generate missing artifacts, or continue
execution. Use `REVIEW_TEMPLATE.md` and a claim ledger with:

- `SUPPORTED`
- `PARTIAL`
- `UNSUPPORTED`
- `CONTRADICTED`

Controlled audit decisions:

- `AUDITED_GO`
- `NEEDS_EVIDENCE`
- `NEEDS_REVISION`
- `NEEDS_HUMAN_APPROVAL`
- `NEEDS_GPT_PLANNER`
- `STOP`

## Report To Next Task

Only the strategic controller, the user-supervised GPT thread, may write the
next high-level task after reading a review or controller report. Do not ask
Codex to continue indefinitely from its own result.

If the review is:

- `NEEDS_EVIDENCE`: next task should collect evidence before expansion.
- `NEEDS_REVISION`: next task should revise inside the audited scope.
- `NEEDS_HUMAN_APPROVAL`: wait for or record approval.
- `NEEDS_GPT_PLANNER`: GPT must decide the next direction.
- `STOP`: do not continue that route unless the user explicitly chooses a new
  direction.

Assume successful controller tasks synchronize remote state by default. For the
next planning round, prefer checking the remote repository state instead of
relying on unpushed local assumptions.

## Notes And Wiki

Write `docs/notes/<date>_<topic>.md` for reference analysis, meetings, design
discussion, or research notes. Notes are not execution entries.

Write durable knowledge to `docs/wiki/`, update `docs/wiki/index.md`, and append
`docs/wiki/log.md`. Wiki pages are not execution entries; tasks may reference
them explicitly.

## GitHub / Remote Tooling

- Do not treat an issue, PR description, or chat text as the only Codex task
  source.
- Do not create issues, PRs, labels, workflows, or remote changes unless the user
  or task explicitly authorizes them.
- If execution is needed, write a task file first.
- If a controller task passes audit and `auto_git_push: true`, expect the remote
  to become the default source for subsequent planning.
