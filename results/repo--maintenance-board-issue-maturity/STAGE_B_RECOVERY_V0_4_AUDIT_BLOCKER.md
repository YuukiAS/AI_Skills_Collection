# Stage B Recovery v0.4 Audit Blocker

Task: `repo--maintenance-board-issue-maturity`
Branch: `reviewed/repo--maintenance-board-issue-maturity`
Recovery blocker addressed: `DUPLICATE_PROJECT_AUTOMATION_READD_FALSE_DONE`

## Recovery actions completed before stop

- Canonical policy amendment prepared on the task branch:
  `docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md`
- Existing Project `Auto-add to project` workflow filter was changed by the
  approved HUMAN_ONLY GitHub Project Workflows UI handoff to:

```text
is:issue is:open label:maintenance-track
```

- The workflow remains enabled according to GraphQL workflow metadata.
- Exactly 11 reviewed duplicate Project items were removed:

```text
#52 #60 #61 #62 #66 #67 #68 #69 #70 #71 #72
```

- After bounded settling, all 11 remained:
  - `CLOSED / DUPLICATE`
  - with `maintenance-track`
  - with reviewed v7 taxonomy labels
  - absent from `AI Skills Maintenance`
- Sentinel #52 label remove/restore probe passed:
  - final label set exactly matched pre-probe labels;
  - Issue remained `CLOSED / DUPLICATE`;
  - all 11 duplicates remained absent from the Project.
- Completed History preservation passed for the 14 current closed/completed
  Project items in the live snapshot:
  - all remained in the Project;
  - Status remained `DONE`;
  - Resolution commit values were unchanged.

## Full audit result

The unchanged deterministic metadata audit still failed:

```text
ok = false
issue_count = 87
violation_count = 1
```

The remaining violation is a new/current tracked Issue outside the 11-duplicate
recovery cohort:

```text
issue = #93
title = Project Instructions Editor: Project 可读性与指令编辑架构
code = missing-source-backlink
message = TODO-backed plugin/standalone Issue has no canonical tracking:#N source backlink.
```

Live #93 metadata readback:

- state: `OPEN`
- Project Status: `TODO`
- labels:
  - `maintenance-track`
  - `kind:new-capability`
  - `scope:standalone-skill`
  - `area:standalone-skill`
- Issue body names source:
  `docs/skill-todos/project-instructions-editor.md`
- Source readback found no `tracking: #93` in
  `docs/skill-todos/project-instructions-editor.md`.

## Stop decision

Per the approved v0.4 recovery package, Stage B must stop before
Forms/Action/Search/Issue #92 closure when the unchanged metadata audit is not
PASS.

This run did not:

- suppress or grandfather the audit violation;
- edit #93;
- add a source backlink for #93;
- rerun taxonomy migration;
- rerun G7;
- continue to Forms/Action/Search acceptance;
- close Issue #92.

```text
DUPLICATE_PROJECT_AUTOMATION_READD_FALSE_DONE_RECOVERY = PARTIAL_EXTERNAL_PASS
FULL_METADATA_AUDIT = FAIL
NEW_TRACKED_ISSUE_DRIFT = #93 missing-source-backlink
NEXT_ACTION = PLANNER_OR_REVIEWER_DECISION_FOR_ISSUE_93_SOURCE_BACKLINK_DRIFT
```
