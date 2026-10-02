# Maintenance Board v7 — Stage B Auto-Add Recovery Critic Review v0.4

Date: 2026-10-01  
Review stage: `STAGE_B_AUTO_ADD_RECOVERY_REVIEW_V0_4`  
Result: `PASS`

Repository: `YuukiAS/AI_Skills_Collection`  
Task: `repo--maintenance-board-issue-maturity`  
Package snapshot: `135c5271e31ab9f88fb796332499677a515d0565`

Reviewed:
- `docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V7_STAGE_B_RECOVERY_PLAN_V0_4_2026-10-01.md`
- `docs/goals/AI_SKILLS_MAINTENANCE_BOARD_V7_STAGE_B_RECOVERY_GOAL_V0_4.md`
- `docs/operations/prompts/AI_SKILLS_MAINTENANCE_BOARD_V7_STAGE_B_RECOVERY_KICKOFF_V0_4.md`

Reviewed blocker:
`DUPLICATE_PROJECT_AUTOMATION_READD_FALSE_DONE`

## 1. Conclusion

PASS.

The observed chronology plus current GitHub documentation support the root-cause assessment strongly enough for a bounded recovery:

1. the eleven duplicate Issues were removed from the Project;
2. they remained `CLOSED / DUPLICATE` and retained `maintenance-track`;
3. later taxonomy label updates modified those Issues;
4. the same eleven Issues reappeared in the Project as DONE;
5. GitHub documents that the built-in auto-add workflow evaluates repository items when they are created or updated if they match its filter;
6. the existing broad filter lacks an open-state predicate.

The minimal durable repair is therefore to narrow active admission from:

`is:issue label:maintenance-track`

to:

`is:issue is:open label:maintenance-track`

and then remove the reviewed duplicate cohort once more.

No compensating bot, Action, watcher, daemon, controller or database is justified.

## 2. Independent GitHub documentation check

Current GitHub official documentation confirms:

- auto-add adds new items when they are created or updated and match the configured filter;
- auto-add supports `is:open`, `is:issue` and label qualifiers;
- documented auto-add `reason:` values are `completed`, `reopened` and `"not planned"`; `duplicate` is not listed;
- enabling/configuring auto-add does not bulk-add existing matching items, and the documented workflow is an add mechanism rather than a continuous remove/reconcile mechanism;
- the documented configuration path is Project -> Workflows -> Auto-add to project -> Edit -> Filters -> Save and turn on workflow;
- the current public GraphQL Projects schema exposes `ProjectV2Workflow` identity/enabled metadata and includes `deleteProjectV2Workflow`, but does not expose a documented `updateProjectV2Workflow` mutation or a workflow-filter-body update field.

References checked:
- https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/adding-items-automatically
- https://docs.github.com/en/issues/planning-and-tracking-with-projects/customizing-views-in-your-project/filtering-projects
- https://docs.github.com/en/graphql/reference/projects
- https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/using-the-built-in-automations

No undocumented API capability is assumed.

## 3. A / B / C comparison

### A — open-only built-in auto-add

Accepted.

It changes the admission predicate at the source of the false-DONE loop and keeps the rest of the lifecycle model intact.

### B — remove maintenance-track on non-completion close

Not selected.

It would make the historical tracking label carry a cleanup side effect solely to compensate for an overly broad Project filter. The source backlink and historical tracking contract do not need to be weakened when the built-in filter can express the correct active-admission predicate directly.

### C — compensating automation

Rejected.

A second Action/watcher/controller would race against the built-in Project automation, require extra credentials/runtime ownership, and create another reconciliation mechanism for a problem the built-in filter can prevent directly.

Therefore A is the smallest correct route.

## 4. Canonical policy semantics

PASS.

The v0.4 policy amendment correctly distinguishes:

- active admission: open + `maintenance-track`;
- completed historical items: already-present completed Project items remain DONE/History;
- closed non-completion: removed from the Project, while `maintenance-track` may remain historical metadata;
- reopened tracked items: if absent from the Project and truthfully reopened, the Issue becomes open and is again eligible for auto-add;
- closure workflow: existing issue-closed -> DONE remains unchanged.

This does not create a second lifecycle. Project Status remains the only lifecycle.

The reopened claim is limited to auto-add eligibility. This review does not claim that reopening an item already present in Project DONE automatically resets its Project Status; that behavior is outside this blocker and is not required for the duplicate-readd recovery.

## 5. Completed History preservation

PASS.

GitHub documents auto-add as an add workflow and does not document filter tightening as an automatic removal mechanism. The package also refuses to rely on that inference alone: it snapshots all current completed DONE/History items before and after the filter change and requires their membership, DONE Status and Resolution commit values to remain unchanged.

That is sufficient for this recovery.

## 6. UI-only mutation boundary

PASS.

The package targets exactly one existing enabled auto-add workflow and changes only its filter.

Because the public GraphQL schema does not document a filter-body update mutation, using the supported Workflows UI is the correct current path.

The package appropriately prefers a supported UI-capable GPT/Work surface and falls back to one exact human-only edit if necessary. Longleaf retains all subsequent evidence, cleanup, audit and acceptance work. Workstation recovery is not a prerequisite.

Pre-change and post-change exact visible-filter readback are mandatory, and no duplicate cleanup begins unless the new filter is verified.

## 7. Exact duplicate repair and regression probe

PASS.

After filter verification, the only duplicate repair is to remove exactly:

`#52 #60 #61 #62 #66 #67 #68 #69 #70 #71 #72`

from the Project once, while preserving:

- `CLOSED / DUPLICATE`;
- `maintenance-track`;
- reviewed taxonomy labels;
- source TODO and `tracking:#N`;
- Issue content/state;
- Project Area semantics.

The #52 label remove/restore probe is a proportionate direct regression check. It causes the same relevant class of Issue update without changing final taxonomy or lifecycle truth. Final label equality, closed state, maintenance label preservation and all-eleven Project absence are explicitly required after automation settles.

A live reopen test is unnecessary and would be more destructive.

## 8. Rollback and main-integration boundary

PASS.

The recovery transaction is correctly ordered:

1. prepare policy amendment on the task branch;
2. latest-main drift check;
3. snapshot old workflow state;
4. mutate/read back the external Project workflow;
5. remove/read back the eleven duplicates;
6. run the update-trigger sentinel;
7. preserve completed History;
8. run the unchanged full audit;
9. only after all recovery gates PASS, integrate the policy amendment/evidence to latest main.

If workflow mutation fails, duplicates are not removed. If duplicate cleanup partially fails, Project membership/fields and the old filter are restored. Main does not publish the new policy while the external truth is unverified.

Once filter + duplicate absence + sentinel + audit PASS, later unrelated Forms/Action/Search failures do not roll back this repair.

## 9. Remaining Stage B and scope

PASS.

After recovery, only unfinished Stage B acceptance/closure remains. No G7 or taxonomy migration replay is required.

No v6.1 implementation, production plugin mutation, new control plane, repository version bump, plugin bump or production Plugin Capability Gate is introduced.

## 10. What this PASS proves

This PASS proves that v0.4 is an execution-ready recovery contract for the observed duplicate auto-add false-DONE loop.

It does not prove that:

- the Project filter has already been changed;
- the eleven duplicate Project items have been removed again;
- the sentinel update probe passes;
- completed History survives live readback;
- the full metadata audit passes;
- Forms/Action/Search acceptance or Issue #92 closure is complete.

Those remain execution obligations.

```text
RESULT = PASS
REVIEW_STAGE = STAGE_B_AUTO_ADD_RECOVERY_REVIEW_V0_4
PACKAGE_SNAPSHOT_COMMIT = 135c5271e31ab9f88fb796332499677a515d0565
SELECTED_RECOVERY = A_OPEN_ONLY_AUTO_ADD
NEW_BLOCKERS = NONE
APPROVED_PLAN_PATH = docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V7_STAGE_B_RECOVERY_PLAN_V0_4_2026-10-01.md
APPROVED_GOAL_PATH = docs/goals/AI_SKILLS_MAINTENANCE_BOARD_V7_STAGE_B_RECOVERY_GOAL_V0_4.md
APPROVED_KICKOFF_PATH = docs/operations/prompts/AI_SKILLS_MAINTENANCE_BOARD_V7_STAGE_B_RECOVERY_KICKOFF_V0_4.md
READY_FOR_CODEX = YES
NEXT_HANDOFF = CODEX
```
