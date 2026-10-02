# Stage B Auto-add Workflow Pre-change Evidence

Task: `repo--maintenance-board-issue-maturity`
Project: `AI Skills Maintenance`
Project owner: `YuukiAS`
Project number: `5`
Project id: `PVT_kwHOA0Lgf84BkjCU`
Repository: `YuukiAS/AI_Skills_Collection`

Target workflow: existing `Auto-add to project`
Workflow id: `PWF_lAHOA0Lgf84BkjCUzgcUzTo`
Workflow number: `7`
Workflow enabled state: `true`

Expected old visible filter from approved v0.4 recovery package:

```text
is:issue label:maintenance-track
```

Readback surface:

- GitHub Project Workflows UI for visible filter body.
- Longleaf `gh api graphql` for Project/workflow identity and enabled state.

Longleaf limitation:

- Current public `ProjectV2Workflow` GraphQL fields expose workflow identity and
  `enabled`, but not the filter body.
- Current public GraphQL mutations expose `deleteProjectV2Workflow`, but no
  documented workflow filter update mutation.
- Current `gh project` commands expose Project item/field operations, not
  Project workflow filter read/edit.

Human-only UI precondition used before mutation:

The UI handoff instructed the user to stop and report if the current visible
filter was not exactly `is:issue label:maintenance-track`; otherwise replace it
with the approved open-only filter and save the existing workflow.

No mismatch was reported before the user completed the UI edit.
