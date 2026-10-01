# Independent Implementation Review Request

Task: `repo--maintenance-board-issue-maturity`
Review stage: `STAGE_A_IMPLEMENTATION_REVIEW`
Repository: `YuukiAS/AI_Skills_Collection`
Branch: `reviewed/repo--maintenance-board-issue-maturity`
Candidate commit: `c6202533b7617a4eec95eca60accd4d2c620192f`
Tracking Issue: #92

## Review Goal

Review the Stage A functional candidate before any G7 label cutover or existing-Issue taxonomy migration.

The Reviewer must return `PASS` only if the current branch satisfies the approved v7 execution package through Stage A and remains within the mutation boundary. A `PASS` authorizes the Executor to proceed to the G7 label cutover gate; it does not authorize main integration, Issue taxonomy migration, or closure by itself.

## Required Source To Read

- `AGENTS.md`
- `docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md`
- `docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V7_IMPLEMENTATION_PLAN_V0_2_2026-10-01.md`
- `docs/goals/AI_SKILLS_MAINTENANCE_BOARD_V7_MATURITY_GOAL_V0_2.md`
- `docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V7_EXECUTION_CRITIC_REVIEW_V0_2_2026-10-01.md`
- `results/repo--maintenance-board-issue-maturity/RESULT.md`
- `results/repo--maintenance-board-issue-maturity/PRE_MIGRATION_ISSUE_METADATA.json`
- `results/repo--maintenance-board-issue-maturity/MIGRATION_CLASSIFICATION.csv`
- `results/repo--maintenance-board-issue-maturity/ROLLBACK_SNAPSHOT.md`

## Changed-File Scope To Verify

Allowed files only:

- `docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md`
- `.github/ISSUE_TEMPLATE/existing_capability_failure.yml`
- `.github/ISSUE_TEMPLATE/new_capability.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/workflows/maintenance-board-intake.yml`
- `scripts/audit_maintenance_board_issue_metadata.py`
- `tests/test_maintenance_board_issue_metadata.py`
- `results/repo--maintenance-board-issue-maturity/**`

Reject if the branch changes production plugin source, generated Marketplace payload, profiles, Bridge Kit source/repo, CODEOWNERS, Dependabot, PR labeler, stale workflow, or another repository.

## Review Checklist

1. Exact branch/worktree identity matches the approved package.
2. v6.1 required-consumer semantics and Issue #4 completion contract were not changed.
3. Board policy append only adds v7 Issue taxonomy, pre-admission intake, Project Area -> `area:*` mirror, native hierarchy/dependency, bounded intake Action, read-only metadata audit, and stale-close prohibition.
4. Label taxonomy in policy matches the exact v7 names, colors and descriptions; `maintenance-track` is protected and unchanged.
5. Issue Forms match the frozen contracts:
   - failure form defaults only `triage:needed`;
   - capability form defaults `triage:needed` + `kind:new-capability`;
   - neither form uses `projects:` or auto-adds `maintenance-track`, scope, area, or Project.
6. Intake Action is restricted to `issues: opened`, `issues: write`, no checkout, no repository secrets, no Issue-body execution, no `maintenance-track`, no kind/scope/area classification, no close/reopen, no Project mutation, no TODO mutation.
7. Audit helper is read-only and checks the required metadata invariants; tests cover approved valid and violation cases.
8. `PRE_MIGRATION_ISSUE_METADATA.json` is a live snapshot of current open+closed `maintenance-track` Issues and Project metadata.
9. `MIGRATION_CLASSIFICATION.csv` covers every current tracked Issue and preserves required anchors:
   - #4 governance / repo-workflow / repo
   - #5 governance / cross-repo / workflow-core / `integration:bridge-kit`
   - #35 regression / plugin / presentations
   - #63 enhancement / plugin / web-development
   - #86 new-capability / plugin / ai-skills-core
10. No `MIGRATION_EXCEPTIONS.md` is needed unless the Reviewer finds a genuinely ambiguous kind.
11. `ROLLBACK_SNAPSHOT.md` captures pre-migration Issue label memberships and correctly defers pre-cutover repository-level label definitions to G7.
12. No live v7 taxonomy label create/reconcile/application happened before Reviewer PASS.
13. No existing maintenance Issue state/title/body, Project Status/Area, canonical TODO maturity/evidence, or `tracking:#N` changed except the approved creation/configuration of tracking Issue #92.
14. Validation results in `RESULT.md` are accurately represented, including path-scoped PASS and full-suite environmental failures.

## Expected Reviewer Output

Return one of:

```text
RESULT = PASS
REVIEW_STAGE = STAGE_A_IMPLEMENTATION_REVIEW
REVIEWED_COMMIT = c6202533b7617a4eec95eca60accd4d2c620192f
G7_LABEL_CUTOVER_AUTHORIZED = YES
```

or:

```text
RESULT = REVISE
REVIEW_STAGE = STAGE_A_IMPLEMENTATION_REVIEW
REVIEWED_COMMIT = c6202533b7617a4eec95eca60accd4d2c620192f
BLOCKERS = <stable finding IDs>
G7_LABEL_CUTOVER_AUTHORIZED = NO
```

A `PASS` must not claim final v7 completion. It only unlocks the G7 pre-publication label cutover gate.
