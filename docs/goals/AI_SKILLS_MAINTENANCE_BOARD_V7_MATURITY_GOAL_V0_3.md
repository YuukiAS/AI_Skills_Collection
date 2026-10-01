# AI Skills Maintenance Board — Issue Maturity Goal v0.3

Task: repo--maintenance-board-issue-maturity
Repository: YuukiAS/AI_Skills_Collection
Package version: v0.3
Approved v7 design: docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V7_MATURITY_PROPOSAL_2026-10-01.md
Approved design commit: 3d091421c7afe8d4f90687ef6e0ce2686bcaf426
Previous Stage A candidate: c6202533b7617a4eec95eca60accd4d2c620192f
Stage A review: results/repo--maintenance-board-issue-maturity/IMPLEMENTATION_REVIEW.md
Stage A review commit: 78bb326a73aaa1cd44aeb17414648ae0b89c90bc
Stable blocker addressed: BOARD-V7-AUDIT-CLOSURE-DEADEND-01
Plan: docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V7_IMPLEMENTATION_PLAN_V0_3_2026-10-01.md
Branch: reviewed/repo--maintenance-board-issue-maturity
Worktree: ../AI_Skills_Collection-repo--maintenance-board-issue-maturity
Primary environment: Longleaf_Codex
Status: READY_FOR_EXECUTION_CRITIC_REVIEW

This Goal becomes executable only after independent execution-ready Critic PASS and the user sends the approved v0.3 Kickoff.

## 1. Goal

Continue the already-implemented v7 Stage A candidate without redesigning v7.

Before any G7 label cutover, truthfully reconcile the 21 pre-existing Maintenance Board lifecycle metadata violations proven by Stage A, then obtain independent review of the repair.

The final v7 live audit contract remains unchanged and must genuinely PASS.

## 2. Known drift cohort

Completed closed + Project DONE + missing Resolution commit:

#53, #54, #55, #56, #57, #58, #59, #63, #64, #65

Duplicate closed + Project DONE:

#52, #60, #61, #62, #66, #67, #68, #69, #70, #71, #72

No other historical drift is implicitly added to this amendment.

## 3. Pre-repair freeze

Before any lifecycle mutation create:

- results/repo--maintenance-board-issue-maturity/LIFECYCLE_DRIFT_PRE_REPAIR.json
- results/repo--maintenance-board-issue-maturity/LIFECYCLE_DRIFT_RECONCILIATION_PLAN.json

The plan must cover all 21 Issues and contain one action per Issue:

- SET_RESOLUTION_COMMIT
- REMOVE_FROM_PROJECT_AS_NON_COMPLETION
- BLOCKED_NO_TRUTHFUL_REPAIR

If live state materially differs from the reviewed cohort, stop Planner/Reviewer.

## 4. Completed Issue rule

For #53–#59 and #63–#65:

- Issue state remains CLOSED / COMPLETED;
- Project Status remains DONE;
- Project Area remains unchanged;
- Resolution commit may be filled only when existing durable closure evidence directly identifies the exact owner-repo closure/evidence commit for that same Issue/source/task.

Chronology, title similarity, PROMOTED status, related-file commits, latest commits or another Issue's Resolution commit are not evidence.

Any unresolved/ambiguous completed Issue blocks the entire repair before mutation.

## 5. Duplicate Issue rule

For #52, #60–#62 and #66–#72:

- preserve CLOSED / DUPLICATE;
- do not re-close/reopen;
- do not touch source maturity/evidence/tracking:#N;
- do not invent Resolution commit;
- remove the Project item so the non-completion Issue no longer appears as DONE/History;
- verify it remains absent.

If auto-add recreates the Project item, stop Planner; do not remove maintenance-track or alter Issue state under this package.

## 6. Required independent review before mutation

The complete reconciliation plan and direct evidence mapping must receive independent review PASS before live repair.

Required:

LIFECYCLE_RECONCILIATION_PLAN = PASS
LIVE_LIFECYCLE_REPAIR_AUTHORIZED = YES

Without PASS, no lifecycle repair and no G7.

## 7. Live repair authority

After plan review PASS, v0.3 authorizes only:

- write the reviewed Resolution commit to the existing Project field for the ten completed Issues;
- remove the eleven reviewed duplicate Issue items from AI Skills Maintenance;
- read back results.

It does not authorize:

- Issue reopen/close;
- Issue body/title edits;
- source TODO changes;
- tracking:#N changes;
- taxonomy label changes;
- Project Area changes;
- unrelated Project Status changes.

## 8. Post-repair review

Create:

- LIFECYCLE_DRIFT_POST_REPAIR.json
- LIFECYCLE_DRIFT_ROLLBACK.json
- LIFECYCLE_DRIFT_REVIEW.md

An independent Reviewer must verify exact live repair and return:

LIFECYCLE_DRIFT_REPAIR = PASS
G7_LABEL_CUTOVER_AUTHORIZED = YES

Only then may the already-approved v0.2 G7 label cutover begin.

## 9. Rollback

Completed Issue repair rollback:
- restore exact pre-repair Resolution commit value.

Duplicate repair rollback:
- re-add same Issue to same Project;
- restore exact pre-repair Area / Status / Resolution values.

Never change maintenance-track, Issue state/reason, canonical TODO or tracking:#N.

Rollback to the pre-repair state does not make that state valid; G7 remains blocked after rollback.

## 10. v7 continuation

After lifecycle-repair review PASS, continue unchanged:

G7 label-definition snapshot/cutover
-> labels ready
-> main integration
-> taxonomy migration
-> full live metadata audit
-> live Forms / Action / search acceptance
-> v7 closure

No audit exceptions or grandfathering.

## 11. Environment

Primary environment remains Longleaf_Codex.

Workstation / CUHK_Workstation_WSL_Codex outage does not block reconciliation, review, G7, migration, audit or search.

The existing final bounded Issue chooser UI fallback remains unchanged.

## 12. Version / scope

Repository bump decision: NONE
Affected plugins: all NO_BUMP
Production Plugin Capability Gate Matrix: NOT REQUIRED

v6.1 remains independent and is not implemented by this Goal.

## 13. Completion boundary

v7 cannot proceed to G7 until:

- all ten completed Resolution commits have direct reviewed support;
- all eleven duplicate repair actions are reviewed;
- live repair has executed;
- post-repair independent review PASSes.

The final live metadata audit must PASS without grandfathering known historical drift.
