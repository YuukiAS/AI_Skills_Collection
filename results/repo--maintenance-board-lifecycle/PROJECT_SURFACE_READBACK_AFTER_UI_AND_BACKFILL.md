# Project Surface Readback After UI Gate And Backfill

Task: `repo--maintenance-board-lifecycle`
Readback date: 2026-09-24

## Project Identity

- title: `AI Skills Maintenance`
- number: `5`
- id: `PVT_kwHOA0Lgf84BkjCU`
- url: https://github.com/users/YuukiAS/projects/5
- private: `true`
- closed: `false`
- linked repositories: `YuukiAS/AI_Skills_Collection`

## Workflows

- `Item closed`: `enabled` (number `1`, updated `2026-09-24T12:12:50Z`)
- `Pull request merged`: `disabled` (number `2`, updated `2026-09-24T12:19:16Z`)
- `Auto-close issue`: `disabled` (number `3`, updated `2026-09-24T12:18:53Z`)
- `Pull request linked to issue`: `disabled` (number `5`, updated `2026-09-24T12:19:05Z`)
- `Item added to project`: `enabled` (number `6`, updated `2026-09-24T12:13:16Z`)
- `Auto-add to project`: `enabled` (number `7`, updated `2026-09-24T12:12:01Z`)

GitHub GraphQL exposes Project workflow name/enabled/number/timestamps, but not the auto-add filter text. The label-gated issue-only path was therefore verified by live readback: labeled Issue #4 and the 81 source tracking Issues all auto-added to this Project as Issues, while `Pull request merged` remains disabled.

## Views

- `Board`: layout `BOARD_LAYOUT`, filter `none`, visible fields `Title, Status, Area`, groupBy `none exposed`
- `By area`: layout `TABLE_LAYOUT`, filter ``, visible fields `Title, Status, Area`, groupBy `Area`
- `History`: layout `TABLE_LAYOUT`, filter `status:DONE`, visible fields `Title, Status, Area, Resolution commit`, groupBy `none exposed`
- `Active`: layout `TABLE_LAYOUT`, filter `status:DOING,ADAPTING`, visible fields `Title, Status, Area`, groupBy `none exposed`

BOARD-01 readback: Project items are Issues carrying `maintenance-track`; `Pull request merged` is disabled; `Auto-close issue` is disabled; the central implementation Issue #4 remains open and DOING, so no false DONE path was observed.

## Backfill Counts

- open `maintenance-track` Issues: 82
- checked Project items through Issue `projectItems`: 82
- missing Project items: []

Status distribution:
- `DOING`: 1
- `TODO`: 81

Area distribution:
- `repo`: 1
- `workflow-core`: 7
- `writing-style`: 8
- `research-writing`: 9
- `presentations`: 20
- `scientific-visualization`: 3
- `web-development`: 21
- `statistical-modeling`: 6
- `bioinformatics`: 1
- `medical-imaging`: 2
- `standalone-skill`: 4

Known surface note: `gh project item-list` / `ProjectV2.items` returned an empty list during this run, while every Issue-level `projectItems` readback showed the expected Project item. Verification therefore uses Issue-level Project item readback, which is also the surface used for field mutation.

## Review 1 Reader-Facing Repair

After `REVIEW_1.md` returned `REVISE`, the live GitHub surface was repaired and read back again. The repair replaced all literal `...` truncated Issue titles, updated Issue #4 body to the current review handoff state, and verified that all 82 open `maintenance-track` Issues still have Project items. Post-repair readback: `ellipsisTitles=[]`, `missingProjectItems=[]`, Status distribution `DOING=1`, `TODO=81`.
