# Reviewed Handoff Request — 055_clear_writing_release_convergence

## Objective

Execute the approved `055` Clear Writing release convergence package for
`writing-style` / Clear Writing.

Canonical contract:

- Goal: `docs/goals/055_CLEAR_WRITING_RELEASE_CONVERGENCE_GOAL.md` v0.2
- Execution Plan: `docs/design/clear-writing/NEXT_RELEASE_EXECUTION_PLAN.md` v0.2
- Execution-ready Critic PASS:
  `docs/design/clear-writing/NEXT_RELEASE_EXECUTION_CRITIC_REVIEW_R2.md`
- Approved kickoff:
  `docs/operations/prompts/055_CLEAR_WRITING_RELEASE_CONVERGENCE_KICKOFF.md`

This task must converge the next compatible Clear Writing release without
reopening the already approved architecture, gate taxonomy, A/B/C review
rubric, or recovery model.

## User-provided inputs

- Goal objective file:
  `/overflow/htzhu/mingcheng_new/.codex-homes/Longleaf_Connection_Bridge/attachments/48260d89-5681-4955-8909-e4dfb26213ed/goal-objective.md`
- Authorized branch:
  `reviewed/055_clear_writing_release_convergence`
- Authorized worktree:
  `/tmp/ai-skills-055-clear-writing-release-convergence`
- Private read scope:
  `private/exports/054_clear_writing_release_closure/inputs/`,
  `private/exports/054_clear_writing_release_closure/deep_research_attempt1/`
- Private write scope:
  `private/exports/055_clear_writing_release_convergence/` and task-local
  ignored `.local-runtime/`

## User constraints

- Explicitly use `workflow-core + ai-skills-core + writing-style`.
- Do not redesign the approved architecture or create a successor task.
- Do not modify Bridge Kit, Host Policy, execpolicy, or add a new provider,
  account, credential location, runtime, state machine, schema, or ledger.
- Do not run fresh holdouts or Terra before the pre-final Critic PASS required
  by the canonical Goal.
- The pre-final private Critic bundle must be prepared locally and then stop for
  the user to manually upload the manifest-listed source/candidate/render to
  the existing Critic thread.
- Final paid review is limited to exactly one `gpt-5.6-terra` Text Review under
  the approved cost and credential boundary.
- Integration to `main` is allowed only after all gates, final GPT Reviewer, and
  explicit user `ACCEPT`.
