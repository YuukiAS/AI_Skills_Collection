# Handoff State Machine

Use these states in task frontmatter, results, reviews, and controller reports
when a controlled state is needed.

## States

- `READY`: GPT planner has written the task and it is ready to execute.
- `EXECUTION_PLANNED`: an execution controller has read the task and written an
  execution plan.
- `EXECUTOR_RUNNING`: an executor session is active.
- `EXECUTED_UNAUDITED`: executor has written result artifacts, but no independent
  audit has accepted the claims.
- `AUDITOR_RUNNING`: a separate auditor is reviewing evidence.
- `AUDITED_GO`: audit supports the claims and the promotion gate is satisfied.
- `NEEDS_EVIDENCE`: evidence is missing or insufficient.
- `NEEDS_REVISION`: implementation or output must be revised inside the current
  task scope.
- `NEEDS_HUMAN_APPROVAL`: a human approval point was reached.
- `NEEDS_SUBAGENT_LAUNCH`: the controller generated executor/auditor prompts but
  the runtime could not launch separate sessions automatically.
- `ESCALATE_WITHIN_POLICY`: the controller may use an escalation path that the
  task explicitly allowed.
- `NEEDS_GPT_PLANNER`: the next move requires strategic judgment or a new
  direction from the GPT planner.
- `STOP`: do not continue this route.

## Rules

- After an executor writes `result.md`, the state may become
  `EXECUTED_UNAUDITED`, `NEEDS_EVIDENCE`, `NEEDS_REVISION`,
  `NEEDS_HUMAN_APPROVAL`, or `STOP`. The executor must not self-promote to final
  completion.
- Medium/high risk tasks and controller tasks should not move to release,
  deployment, submission, commit, push, or expensive expansion without an
  independent audit unless the task explicitly says review is not required.
- `STOP`, `NEEDS_EVIDENCE`, `NEEDS_REVISION`, `NEEDS_HUMAN_APPROVAL`, and
  `NEEDS_GPT_PLANNER` cannot be bypassed by the executor or execution
  controller.
- Only the strategic controller, meaning the user-supervised GPT thread, may
  decide a new research/product direction or write the next high-level task.
- A controller can continue only along `allowed_next_states` and only within the
  task's `failure_escalation_policy`.
