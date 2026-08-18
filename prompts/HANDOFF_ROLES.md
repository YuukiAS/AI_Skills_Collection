# Handoff Roles

This kit defines a two-layer execution protocol. It is a general repository
protocol, not a domain-specific research policy.

## Layer 1: Strategic Planning

The strategic planning layer is the user-supervised ChatGPT/GPT thread.

Responsibilities:

- Understand the user goal and repository context.
- Search for new directions, compare alternatives, and make research or product
  judgments.
- Decide whether the next handoff is a normal execution task or a controller
  task.
- Write high-quality `prompts/tasks/<task_key>.md` files with scope, evidence
  gates, forbidden substitutes, and failure escalation policy.
- Read audits and controller reports before deciding whether to stop, roll back,
  ask for human approval, or write the next high-level task.

Codex is not the default strategic planner. A Codex session may execute within a
task, but it must not invent a new direction when the GPT-authored task fails.

## Layer 2: Execution Control

The execution-control layer may be a Codex controller session, but only inside a
GPT-authored controller task.

Responsibilities:

- Read the controller task and build an execution plan inside its authorized
  scope.
- Create or launch executor and auditor sessions when the runtime supports it.
- If automatic subagent launch is unavailable, write reusable subagent prompt
  files and stop at `NEEDS_SUBAGENT_LAUNCH` or `NEEDS_HUMAN_APPROVAL`.
- Collect executor results and auditor reviews.
- Decide whether the promotion gate is satisfied.
- Write `results/<task_key>/controller_report.md`.
- When `auto_git_commit: true` and the audited gate passes, commit the approved
  changes.
- When `auto_git_push: true` and human approval was not triggered, push the
  commit to the remote.
- Output `NEEDS_GPT_PLANNER` and stop if the task needs a new direction or
  exceeds the failure escalation policy.

The execution controller is a supervisor for one approved task, not an open-ended
planner.

## Four Roles

- `planner`: the ChatGPT/GPT main thread that writes tasks. Default:
  `ChatGPT/GPT thread`.
- `strategic_controller`: the user-supervised GPT thread that reads results,
  reviews, and controller reports, then decides the next high-level direction.
  Default: `user-supervised GPT thread`.
- `execution_controller`: a Codex controller session that coordinates execution
  only inside a GPT-authored controller task. Default for controller tasks:
  `Codex controller session`.
- `executor`: a Codex executor session that performs authorized changes,
  commands, and result writing. Default: `Codex executor session`.
- `auditor`: a separate read-only reviewer. It may be a separate Codex auditor
  session or ChatGPT reviewer with enough file evidence. The auditor must not
  fix code, generate missing artifacts, or continue execution unless a new task
  explicitly authorizes that role change.

Executor self-assessment is never the final completion state. A controller
report is also not a replacement for GPT strategic planning.
