# Planner source-authority decision — 2026-10-16

Task: `clear-writing--cross-surface-language-layer`
Current state remains: `NEEDS_GPT_PLANNER`
Current plan revision remains: `1 / 1`

## Decision

The 2026-10-15 generator parity blocker is an external repository source-authority defect, not a reason to delete the current generated Presentations / Research Writing behavior.

Evidence establishes the generated side as behavior to preserve:

- Presentations `docs/plugin-todos/presentations-authoring-production-workflow.md` is `PROMOTE_NOW / CANONICAL WORKFLOW ADOPTION` and explicitly names the generated runtime contracts as canonical runtime.
- `docs/design/PRESENTATIONS_RENDER_REGRESSION_POSTMORTEM_AND_HARDENING_2026-10-07.md` says those generated runtime contracts were incorporated after a severe real render regression.
- Research Authoring student-assessment promotion notes are `PROMOTE_NOW / IMMEDIATE ADOPTION` and explicitly point to the current generated shared contracts.
- The generated-only files were deliberately added/strengthened on main in October 6–7 commits; blindly regenerating from older source would regress already-adopted runtime behavior.

Therefore the correct repair is source-first restoration: promote the current generated behavior into canonical source/config and require official regeneration to reproduce the pre-repair generated trees byte-for-byte.

## External repair

A separate bounded repository-maintenance branch has been created:

`work/repo--canonical-generated-parity-restoration`

Planner package:
- `docs/design/source-authority/CANONICAL_GENERATED_PARITY_RESTORATION_PLAN_2026-10-16.md`
- `docs/goals/CANONICAL_GENERATED_PARITY_RESTORATION_GOAL_2026-10-16.md`
- `docs/operations/prompts/CANONICAL_GENERATED_PARITY_RESTORATION_KICKOFF_2026-10-16.md`

This is not a Clear Writing successor. It repairs the external main-branch dependency while leaving this task's PLAN/CURRENT untouched.

After that repair is integrated into main, this Planner will verify the new main, then resume the existing Clear Writing task under the already-frozen revision-1 Plan without widening Clear Writing product scope.