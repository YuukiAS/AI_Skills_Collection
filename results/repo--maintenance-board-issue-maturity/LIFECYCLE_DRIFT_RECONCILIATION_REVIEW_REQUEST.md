# Lifecycle Drift Reconciliation Plan Review Request

Task: `repo--maintenance-board-issue-maturity`
Branch: `reviewed/repo--maintenance-board-issue-maturity`
Review target commit: `cc6b20936f893b9adc93289c4c63179cb9586d29`
Review stage: `LIFECYCLE_RECONCILIATION_PLAN_REVIEW`

## Purpose

This request asks an independent Reviewer to inspect the pre-repair lifecycle
drift evidence and reconciliation plan created for the Maintenance Board v7
lifecycle-metadata blocker.

This is a plan review only. No live Project or Issue repair has been executed.

## Required Inputs

Review these files on the review target commit:

- `results/repo--maintenance-board-issue-maturity/LIFECYCLE_DRIFT_PRE_REPAIR.json`
- `results/repo--maintenance-board-issue-maturity/LIFECYCLE_DRIFT_RECONCILIATION_PLAN.json`
- `results/repo--maintenance-board-issue-maturity/IMPLEMENTATION_REVIEW.md`
- `results/repo--maintenance-board-issue-maturity/PRE_MIGRATION_ISSUE_METADATA.json`
- `docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md`

The v0.3 execution contract is on latest `origin/main`:

- `docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V7_IMPLEMENTATION_PLAN_V0_3_2026-10-01.md`
- `docs/goals/AI_SKILLS_MAINTENANCE_BOARD_V7_MATURITY_GOAL_V0_3.md`
- `docs/operations/prompts/AI_SKILLS_MAINTENANCE_BOARD_V7_MATURITY_KICKOFF_V0_3.md`
- `docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V7_EXECUTION_CRITIC_REVIEW_V0_3_2026-10-01.md`

Do not require `origin/main` to be merged into the task branch.

## Reviewer Checks

The Reviewer must verify:

1. The exact 21-Issue cohort is unchanged:
   - completed missing Resolution commit:
     `#53 #54 #55 #56 #57 #58 #59 #63 #64 #65`
   - duplicate false-DONE:
     `#52 #60 #61 #62 #66 #67 #68 #69 #70 #71 #72`
2. `LIFECYCLE_DRIFT_PRE_REPAIR.json` records current live Issue/Project state
   for every affected Issue, including Issue state/reason, Project item id,
   Project Status, Project Area, Resolution commit, labels, source locators,
   and examined closure-evidence locators.
3. The plan contains exactly one action per affected Issue and only these
   action values:
   - `SET_RESOLUTION_COMMIT`
   - `REMOVE_FROM_PROJECT_AS_NON_COMPLETION`
   - `BLOCKED_NO_TRUTHFUL_REPAIR`
4. Every completed Issue proposed for `SET_RESOLUTION_COMMIT` has direct
   existing durable evidence binding the same Issue or canonical source entry
   to exact owner-repo commit:
   `c232f2ea906277f2217c4bbce4f56df1ebd5827c`.
5. Duplicate/non-completion Issues are planned only for Project removal, with
   Issue state/reason, labels, source TODOs and `tracking:#N` preserved.
6. The rollback metadata is sufficient for the authorized repair:
   - completed Issues restore the exact pre-repair Resolution commit value;
   - duplicate Issues can be re-added to the same Project and restored to the
     exact pre-repair Status, Area and Resolution values.
7. The plan proposes no Issue state/title/body edit, no source TODO edit, no
   `tracking:#N` edit, no Project Area edit, no taxonomy label mutation, no
   main integration, and no G7 label cutover.

## Required Review Result

If and only if all checks pass, return:

```text
LIFECYCLE_RECONCILIATION_PLAN = PASS
LIVE_LIFECYCLE_REPAIR_AUTHORIZED = YES
G7_LABEL_CUTOVER_AUTHORIZED = NO
NEXT_ACTION = CODEX_LIVE_LIFECYCLE_REPAIR
```

If any completed Issue lacks direct support, or any live state materially
differs from the frozen cohort, return `REVISE` or the appropriate reviewed
handoff failure state. Do not authorize repair.

## Current Executor Statement

```text
LIFECYCLE_RECONCILIATION_PLAN_READY = YES
LIVE_LIFECYCLE_REPAIR_AUTHORIZED = NO
G7_LABEL_CUTOVER_AUTHORIZED = NO
LIVE_REPAIR_PERFORMED = NO
NEXT_ACTION = INDEPENDENT_RECONCILIATION_PLAN_REVIEW
```
