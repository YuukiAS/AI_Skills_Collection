# Required Consumer Handoffs

Task: `repo--maintenance-board-lifecycle`
Status date: 2026-09-25
Pre-cutover `main` tip when this handoff was prepared:
`1323616c44680a80938fc4778e6f6f18ba5ca408`
Final published anchor: use the live `origin/main` tip and Issue #4 `当前执行锚点`.
Tracking Issue: `#4`
Project: `AI Skills Maintenance`
Project status after central cutover: `ADAPTING`

## Boundary

Central maintenance-board implementation is complete. This handoff does not
authorize server, remote, or local machine adaptation. Each consumer must run a
future AI Skills Maintainer action in its own current Codex environment, or use
another separately approved route for that exact consumer.

The future consumer action must verify its current installed and loaded
AI_Skills identity, read the latest `main` copy of
`docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md`, adapt its machine-consumed
workflow/shared maintenance mechanism if needed, and leave durable evidence.
Single-consumer PASS is not enough to close Issue #4; aggregate closure requires
all five consumers to be PASS or N/A with evidence.

## Consumer Locators

### Longleaf_Codex

- Current identity status: `LOCATOR_OBSERVED`
- Codex host: `remote-ssh-discovered:Longleaf_Codex`
- Display name: `Longleaf_Codex`
- Project id: `224089a4-5b6a-49ea-b639-21cd8a06f172`
- Repository path observed from current Codex app project list:
  `/overflow/htzhu/mingcheng_new/AI_Skills_Collection`
- Required handoff: run the AI Skills Maintainer in this consumer environment
  against that repository path, verify current branch/main freshness and
  installed/loaded AI_Skills identity, then record consumer PASS or truthful
  blocker back to Issue #4.

### Longleaf_Backup_Codex

- Current identity status: `HOST_OBSERVED_REPO_LOCATOR_NOT_OBSERVED`
- Codex host: `remote-ssh-discovered:Longleaf_Backup_Codex`
- Display name: `Longleaf_Backup_Codex`
- Current surface evidence: the host is visible in the Codex app project list,
  but no `AI_Skills_Collection` project locator for this host was present in the
  current list.
- Required handoff: obtain consumer-bounded authorization or an already approved
  route to inspect this consumer's current AI_Skills repository/installation
  identity. Do not guess a path. Once resolved, run the same current-consumer
  Maintainer adaptation and evidence flow.

### CUHK_Workstation_WSL_Codex

- Current identity status: `LOCATOR_OBSERVED`
- Codex host: `remote-ssh-discovered:CUHK_Workstation_WSL_Codex`
- Display name: `CUHK_Workstation_WSL_Codex`
- Project id: `b1ba92ca-c703-44ff-bc42-91e6d18f2d27`
- Repository path observed from current Codex app project list:
  `/home/yuukias/AI_Skills_Collection`
- Required handoff: run the AI Skills Maintainer in this consumer environment
  against that repository path, verify current branch/main freshness and
  installed/loaded AI_Skills identity, then record consumer PASS or truthful
  blocker back to Issue #4.

### Workstation

- Current identity status: `LOGICAL_CONSUMER_NOT_RESOLVED_FROM_CURRENT_SURFACE`
- Current surface evidence: local Codex projects are visible, but no local
  `AI_Skills_Collection` project locator was present in the current app project
  list.
- Required handoff: obtain Workstation-local authority or a current user-provided
  locator before inspecting or adapting this consumer. Do not infer this from
  the CUHK WSL path or from other local projects.

### Legion

- Current identity status: `LOGICAL_CONSUMER_NOT_RESOLVED_FROM_CURRENT_SURFACE`
- Current surface evidence: no Legion host or local `AI_Skills_Collection`
  locator was present in the current app project list.
- Required handoff: obtain Legion-local authority or a current user-provided
  locator before inspecting or adapting this consumer. Do not guess a machine,
  path, or installed plugin identity.

## Pending Issue #4 Aggregate State

```text
CENTRAL_IMPLEMENTATION_COMPLETE = YES
PROJECT_STATUS = ADAPTING
CONSUMER_LONGLEAF_CODEX = HANDOFF_READY
CONSUMER_LONGLEAF_BACKUP_CODEX = NEEDS_CONSUMER_LOCATOR_OR_AUTHORITY
CONSUMER_CUHK_WORKSTATION_WSL_CODEX = HANDOFF_READY
CONSUMER_WORKSTATION = NEEDS_CONSUMER_LOCATOR_OR_AUTHORITY
CONSUMER_LEGION = NEEDS_CONSUMER_LOCATOR_OR_AUTHORITY
OVERALL_GOAL_ACHIEVED = NO
FINAL_DONE = OUT_OF_SCOPE_FOR_CENTRAL_STAGE
```

## Handoff Prompt Template

Use this for each consumer after the appropriate consumer authority exists:

```text
Continue AI Skills Maintenance Board adaptation for consumer <CONSUMER_NAME>.

Repository: YuukiAS/AI_Skills_Collection
Central tracking Issue: #4
Central board policy: docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md on latest main
Central closure evidence: results/repo--maintenance-board-lifecycle/

Your authority is limited to this current consumer. Do not act as a
cross-machine controller. First verify the current repository locator,
installed/loaded AI_Skills identity, normal-entry behavior, and main freshness.
Then adapt/update only the machine-consumed workflow/shared maintenance
mechanism needed for this consumer to observe and follow the maintenance-board
contract. Leave durable evidence and report this consumer as PASS, N/A, or a
truthful blocker. Do not close Issue #4 unless aggregate closure for all five
required consumers has already been verified.
```
