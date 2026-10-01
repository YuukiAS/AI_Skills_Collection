# AI Skills Maintenance Board — Stage B Auto-Add Recovery Goal v0.4

Task: repo--maintenance-board-issue-maturity
Repository: YuukiAS/AI_Skills_Collection
Existing branch: reviewed/repo--maintenance-board-issue-maturity
Primary environment: Longleaf_Codex
Recovery blocker: DUPLICATE_PROJECT_AUTOMATION_READD_FALSE_DONE
Plan: docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V7_STAGE_B_RECOVERY_PLAN_V0_4_2026-10-01.md
Status: READY_FOR_INDEPENDENT_CRITIC_REVIEW

This Goal is not executable until an independent Critic passes the exact v0.4 recovery package and the user sends the approved Kickoff.

## 1. Recovery objective

Repair the Stage B false-DONE loop without redesigning v7.

The selected recovery is:

```text
old Project auto-add filter:
is:issue label:maintenance-track

new Project auto-add filter:
is:issue is:open label:maintenance-track
```

Then remove the known 11 CLOSED / DUPLICATE Project items once, verify they do
not return on a representative Issue update, run the unchanged full metadata
audit, and resume the existing Stage B acceptance gates.

## 2. Canonical policy truth

After recovery, current canonical Maintenance Board policy must say:

### Active admission

```text
is:issue is:open label:maintenance-track
```

Open maintenance-track Issues are eligible for auto-add.

### Historical completed

Already-present completed Issues remain Project DONE/History. The open-only
auto-add filter does not remove them and is not responsible for reconstructing
History after manual removal.

### Closed non-completion

Duplicate/not-planned/rejected/superseded Issues must not be represented as
Project DONE.

After removal from Project they may retain `maintenance-track` as historical
tracking metadata. Because they are closed they do not match the open-only
auto-add rule.

### Reopened

A maintenance-track Issue that is truthfully reopened becomes open and can
match the active-admission auto-add rule again.

### Closure automation

The existing issue-closed -> DONE Project workflow remains unchanged.

## 3. Exact Project workflow mutation

Target only the existing enabled Auto-add to project workflow in:

```text
Project = AI Skills Maintenance
Project number = 5
repository = YuukiAS/AI_Skills_Collection
```

Change only its filter to:

```text
is:issue is:open label:maintenance-track
```

Do not:

- create a second auto-add workflow;
- change issue-closed -> DONE;
- change BOARD-01 PR workflows;
- add auto-archive;
- add a compensating Action/bot.

Before mutation capture exact visible old filter + enabled state.

After mutation use a supported UI-capable surface to read back exact filter +
enabled state.

If no supported automated UI surface exists, allow one exact HUMAN_ONLY UI
handoff for this single workflow edit. Longleaf resumes all later work.

## 4. Current 11-Issue repair

After new filter readback PASS, repair exactly:

```text
#52 #60 #61 #62 #66 #67 #68 #69 #70 #71 #72
```

For each:

- must remain CLOSED / DUPLICATE;
- must retain maintenance-track;
- must retain reviewed taxonomy labels;
- remove current AI Skills Maintenance Project item;
- do not modify Issue body/title/state/reason;
- do not modify Project Area;
- do not modify source TODO maturity/evidence/tracking:#N;
- verify Project item absent.

## 5. Re-add prevention acceptance

Required:

1. UI readback exact filter:
   `is:issue is:open label:maintenance-track`.
2. All 11 absent from Project after bounded automation settling.
3. Sentinel #52:
   - snapshot final taxonomy labels;
   - temporarily remove then restore existing `kind:enhancement`;
   - final labels must exactly equal snapshot;
   - Issue stays CLOSED / DUPLICATE;
   - maintenance-track never changes;
   - after automation settles, #52 remains absent;
   - other ten remain absent.

If sentinel is re-added, stop. No compensating bot.

## 6. Completed History acceptance

Snapshot all currently closed COMPLETED maintenance-track items that are
currently represented as DONE/History.

After filter change and duplicate repair verify:

- they remain Project items;
- Status remains DONE;
- Resolution commit values are unchanged;
- none disappeared due to the filter change.

## 7. Full audit

Run existing metadata audit unchanged.

Required:

```text
ok = true
violation_count = 0
```

No grandfathering or audit suppression.

## 8. Branch/main boundary

The v7 functional source and taxonomy migration are already on main.

This recovery prepares only a canonical-policy amendment on the existing task
branch.

Sequence:

1. independent Critic PASS on v0.4 package;
2. prepare exact policy amendment on existing task branch;
3. latest-main drift check;
4. Project workflow filter mutation/readback;
5. 11-Issue removal/readback + sentinel probe;
6. full audit PASS;
7. only then ordinary non-force integrate the reviewed policy amendment and
   recovery evidence into latest main;
8. verify remote main.

Do not replay G7 or taxonomy migration.

## 9. Rollback

Before the UI mutation, capture old filter/enabled state and duplicate Project
metadata.

If workflow mutation cannot be verified:
- restore old workflow config;
- remove no duplicates;
- stop.

If duplicate repair partially fails before recovery acceptance:
- re-add already removed duplicates;
- restore exact pre-recovery Area / Status / Resolution values;
- restore old broad filter;
- verify rollback;
- stop.

After workflow + all-11 + sentinel + audit PASS, the recovery is committed and
must not be rolled back merely because a later unrelated Forms/Action/Search
acceptance gate fails.

maintenance-track is never removed or redefined.

## 10. Remaining Stage B

After recovery and policy integration continue only the unfinished gates:

1. live Forms chooser acceptance;
2. pre-admission Action smoke;
3. search usability acceptance;
4. stale safety final readback;
5. README closure;
6. Issue #92 reader-facing closure update using Clear Writing;
7. Resolution commit;
8. close #92 completed;
9. verify Project DONE.

Do not rerun earlier classification, G7 or taxonomy migration.

If Longleaf cannot perform only the live chooser UI readback, isolate that one
final bounded UI handoff. Do not make Workstation recovery a prerequisite.

## 11. Non-goals

No v6.1 implementation.
No production plugin change.
No new bot/daemon/watcher/controller/database.
No audit relaxation.
No removal of maintenance-track from historical duplicate Issues.

## 12. Version

```text
Repository bump decision: NONE
Affected plugins: all NO_BUMP
Production Plugin Capability Gate Matrix: NOT REQUIRED
```
