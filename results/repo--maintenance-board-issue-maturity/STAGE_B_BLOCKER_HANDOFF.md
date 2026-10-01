# Maintenance Board v7 Stage B Blocker Handoff

Task: `repo--maintenance-board-issue-maturity`
Branch: `reviewed/repo--maintenance-board-issue-maturity`
Environment: `Longleaf_Codex`

## Current state

G7 label cutover passed, reviewed functional work was integrated to `origin/main`,
and the reviewed taxonomy migration was applied to all 86 current
`maintenance-track` Issues.

The migration readback passed:

```text
POST_MIGRATION_ISSUE_METADATA.json
migration_status = PASS
issue_count = 86
changed_issue_count = 86
```

The live metadata audit failed:

```text
METADATA_AUDIT.json
ok = false
violation_count = 11
```

The 11 violations are the reviewed duplicate cohort:

```text
#52 #60 #61 #62 #66 #67 #68 #69 #70 #71 #72
```

Each is still `CLOSED / DUPLICATE`, still has `maintenance-track`, and is again
present in the `AI Skills Maintenance` Project with `Status = DONE`.

## Contract impact

This matches the frozen stop condition for duplicate Project automation re-add /
false-DONE after repair. Under the approved package, Codex must not continue to
Forms, Action, search acceptance, Issue #92 closure, or Project DONE while the
audit fails.

Codex has not:

- removed `maintenance-track`;
- reopened or re-closed duplicate Issues;
- changed Issue state/reason/title/body;
- changed source TODO maturity/evidence/`tracking:#N`;
- continued Forms/Action/Search acceptance after audit failure.

## Evidence

- `POST_MIGRATION_ISSUE_METADATA.json`
- `METADATA_AUDIT.json`
- `STAGE_B_DUPLICATE_AUTOMATION_READD_BLOCKER.json`
- `STAGE_B_DUPLICATE_AUTOMATION_READD_CONTINUATION_READBACK.json`

## Required next action

```text
NEXT_ACTION = PLANNER_OR_REVIEWER_DECISION_FOR_DUPLICATE_PROJECT_AUTOMATION_READD
```

The next decision should explicitly choose a reviewed recovery path for duplicate
Project auto-add/false-DONE behavior before any remaining live acceptance gates
resume.
