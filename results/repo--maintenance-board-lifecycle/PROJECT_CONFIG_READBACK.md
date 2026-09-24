# Project Configuration Readback

Task: `repo--maintenance-board-lifecycle`

Readback time: 2026-09-24

## Project identity

```text
owner = YuukiAS
title = AI Skills Maintenance
number = 5
id = PVT_kwHOA0Lgf84BkjCU
url = https://github.com/users/YuukiAS/projects/5
private = true
linked repository = YuukiAS/AI_Skills_Collection
```

Repository label:

```text
maintenance-track = present
description = Tracked by AI Skills Maintenance board
color = #5319e7
```

## Fields

Required fields are present:

```text
Status = TODO / DOING / ADAPTING / DONE
Area = workflow-core / ai-skills-core / writing-style / research-writing /
       presentations / scientific-visualization / web-development /
       statistical-modeling / bioinformatics / medical-imaging /
       standalone-skill / repo / cross-plugin
Resolution commit = text
```

Field ids:

```text
Project id = PVT_kwHOA0Lgf84BkjCU
Status field = PVTSSF_lAHOA0Lgf84BkjCUzhjTPss
  TODO = ab128b18
  DOING = 5bc96327
  ADAPTING = 7527fc31
  DONE = 53de53ba
Area field = PVTSSF_lAHOA0Lgf84BkjCUzhjTQOI
Resolution commit field = PVTF_lAHOA0Lgf84BkjCUzhjTQOw
```

## Views

Created/read back views:

```text
Board
  id = PVTV_lAHOA0Lgf84BkjCUzgLyFx4
  layout = BOARD_LAYOUT
  visible fields = Title, Status, Area

Active
  id = PVTV_lAHOA0Lgf84BkjCUzgLyFy0
  layout = TABLE_LAYOUT
  filter = status:DOING,ADAPTING
  visible fields = Title, Status, Area

By area
  id = PVTV_lAHOA0Lgf84BkjCUzgLyFx8
  layout = TABLE_LAYOUT
  visible fields = Title, Status, Area

History
  id = PVTV_lAHOA0Lgf84BkjCUzgLyFyw
  layout = TABLE_LAYOUT
  filter = status:DONE
  visible fields = Title, Status, Area, Resolution commit
```

Limit observed: the available GraphQL configuration surface set visible fields,
layout, and filter. It did not expose a writable group-by configuration in the
input object. Current readback shows `groupByFields = []`.

## Workflows

Readback after deleting the default `Auto-add sub-issues to project` workflow:

```text
Auto-close issue = disabled
Item added to project = disabled
Item closed = disabled
Pull request linked to issue = disabled
Pull request merged = disabled
```

`Pull request merged` is disabled, which satisfies the false-DONE guard.

Still required before backfill:

```text
1. Enable label-gated issue-only auto-add:
   is:issue label:maintenance-track

2. Enable/confirm issue closed -> DONE only as the final mechanical closure path.

3. If the GitHub UI supports view grouping, set:
   Board grouped by Status
   By area grouped by Area
```

These settings were not exposed through the supported `gh project` / GraphQL
write surface used in this task. Per the kickoff, backfill must wait for this
minimal UI setup and readback.

## Items

Current Project item count:

```text
0
```

No Issue backfill has started yet.
