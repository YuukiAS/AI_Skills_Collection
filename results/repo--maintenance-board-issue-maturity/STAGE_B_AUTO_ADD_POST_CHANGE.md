# Stage B Auto-add Workflow Post-change Evidence

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

Human GitHub Project Workflows UI readback:

```text
Filters
is:issue is:open label:maintenance-track
```

Required filter:

```text
is:issue is:open label:maintenance-track
```

Post-change result:

```text
filter = is:issue is:open label:maintenance-track
enabled = true
repository = YuukiAS/AI_Skills_Collection
```

Other workflow boundary:

- Same Project retained.
- Same repository retained.
- Existing `Item closed` workflow remains enabled by GraphQL readback.
- Existing `Pull request merged` workflow remains disabled by GraphQL readback.
- No duplicate auto-add workflow was created by this recovery.
- No auto-archive workflow was created by this recovery.

Supporting live metadata:

- `STAGE_B_RECOVERY_V0_4_PRE_DUPLICATE_SNAPSHOT.json`
- `STAGE_B_RECOVERY_V0_4_POST_REMOVE_SNAPSHOT.json`
