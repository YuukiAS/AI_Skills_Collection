# Required Consumer Handoffs

Task: `repo--maintenance-board-lifecycle`
Status date: 2026-09-25
Pre-cutover `main` tip when this handoff was prepared:
`1323616c44680a80938fc4778e6f6f18ba5ca408`
Final published anchor: use the live `origin/main` tip and Issue #4 `当前执行锚点`.
Tracking Issue: `#4`
Project: `AI Skills Maintenance`
Project status after central cutover: `ADAPTING`

## Current Contract Note — 2026-10-02

This file preserves the original five-consumer handoff text as historical
evidence. The current Issue #4 closure contract is recorded in the sections:

- `Historical Handoff Matrix`
- `Current Required Set — 2026-10-02`
- `Current Non-Required Historical Consumers`

Under v6.1, the current required set is:

```text
AI Research Stack ChatGPT Project instructions = PASS
Longleaf_Codex = PASS
```

The old five-consumer matrix below is not the current Issue #4 prerequisite set.

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

## Historical Handoff Matrix

The five-consumer material above is preserved as historical handoff evidence
from the pre-v6.1 contract. It is not the current Issue #4 closure prerequisite
set.

Current canonical policy now uses the v6.1 evidence-backed rule:
required consumers are the actual normal-entry consumers and explicitly promised
fallback environments needed for the tracked item's frozen completion claim.

## Current Required Set — 2026-10-02

```text
CURRENT_REQUIRED_SET_FROZEN = YES
AI Research Stack ChatGPT Project instructions = PASS
Longleaf_Codex = PASS
ALL_REQUIRED_CONSUMERS = PASS_OR_NA
FINAL_REMAINING_CONSUMER = NONE
```

### AI Research Stack ChatGPT Project instructions

Status: `PASS`

Direct evidence locator:
`results/repo--maintenance-board-lifecycle/CENTRAL_CLOSURE_STATUS.md`

Evidence summary:

- The user confirmed semantic installation of the Maintenance Board trigger in
  the AI Research Stack ChatGPT Project instructions.
- The installed semantics require AI_Skills maintenance work to read latest
  `main` board policy, actively maintain tracking state, output exact pending
  Project mutation when the current surface cannot mutate Project metadata, and
  avoid asking the user to manually synchronize Kanban.

### Longleaf_Codex

Status: `PASS`

Direct evidence locators:

- `results/repo--maintenance-board-issue-maturity/V7_FINAL_CLOSURE.md`
- `results/repo--maintenance-board-issue-maturity/LIVE_INTAKE_ACCEPTANCE.md`
- `results/repo--maintenance-board-issue-maturity/SEARCH_ACCEPTANCE.md`
- `results/repo--maintenance-board-issue-maturity/STALE_SAFETY.md`
- `results/repo--maintenance-board-lifecycle/METADATA_AUDIT_CURRENT_2026-10-02.json`
- GitHub Issue #92 live readback: `CLOSED / COMPLETED`, Project `DONE`.
- GitHub Issue #93 live readback: `OPEN`, Project `DOING`,
  Area `standalone-skill`, taxonomy labels present.
- GitHub Issue #94 live readback: `CLOSED / NOT_PLANNED`,
  label `triage:needed`, no Project item.

Evidence summary:

- v7 final closure commit:
  `700234d7e94bb5613f951b8adeb7155d3b15ec3f`.
- v7 final closure result is `V7_ISSUE_MATURITY = COMPLETE`.
- Latest live metadata audit in this branch reports `ok = true` and
  `violation_count = 0`.
- #93 is a real tracked standalone-skill Issue with entry-level source
  backlinks in `docs/skill-todos/project-instructions-editor.md`.
- #94 proves the pre-admission action smoke: a non-tracked acceptance Issue
  received only `triage:needed`, did not receive `maintenance-track`, did not
  receive guessed taxonomy labels, and did not enter the Project.
- Project auto-add open-only evidence is preserved in
  `results/repo--maintenance-board-issue-maturity/STAGE_B_AUTO_ADD_POST_CHANGE.md`.
- The duplicate false-DONE cohort remains absent from the Project in the live
  Project item-list readback.

## Current Non-Required Historical Consumers

These consumers remain historical evidence only. They are not marked PASS and
are not outage-based N/A for Issue #4.

### CUHK_Workstation_WSL_Codex

Status: `NOT_REQUIRED_FOR_ISSUE_4_CURRENT_CONTRACT`

Direct evidence locators:

- Historical locator:
  `results/repo--maintenance-board-lifecycle/CONSUMER_HANDOFFS.md`
  section `CUHK_Workstation_WSL_Codex`.
- Current scope authority:
  `docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_FINAL_CLOSURE_IMPLEMENTATION_PLAN_V0_2_2026-10-02.md`
  sections `1`, `4.3`.
- Current canonical policy:
  `docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md` §14.

Reason:

Historical WSL usage evidence proves the environment existed and previously ran
AI_Skills work. Under v6.1, that does not make it a current Issue #4 required
consumer without a current normal-entry or explicit fallback promise.

### Longleaf_Backup_Codex

Status: `NOT_REQUIRED_FOR_ISSUE_4_CURRENT_CONTRACT`

Direct evidence locators:

- Historical locator:
  `results/repo--maintenance-board-lifecycle/CONSUMER_HANDOFFS.md`
  section `Longleaf_Backup_Codex`.
- Current scope authority:
  `docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_FINAL_CLOSURE_IMPLEMENTATION_PLAN_V0_2_2026-10-02.md`
  sections `1`, `4.3`.
- Current canonical policy:
  `docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md` §14.

Reason:

The display name includes `Backup`, but Issue #4 has no current product promise
that this backup environment must consume the Maintenance Board contract before
closure.

### Workstation

Status: `NOT_REQUIRED_FOR_ISSUE_4_CURRENT_CONTRACT`

Direct evidence locators:

- Historical locator:
  `results/repo--maintenance-board-lifecycle/CONSUMER_HANDOFFS.md`
  section `Workstation`.
- Current scope authority:
  `docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_FINAL_CLOSURE_IMPLEMENTATION_PLAN_V0_2_2026-10-02.md`
  sections `1`, `4.3`.
- Current canonical policy:
  `docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md` §14.

Reason:

Workstation was part of the historical five-consumer matrix, but the current
Issue #4 completion claim no longer requires workstation access or adaptation.

### Legion

Status: `NOT_REQUIRED_FOR_ISSUE_4_CURRENT_CONTRACT`

Direct evidence locators:

- Historical locator:
  `results/repo--maintenance-board-lifecycle/CONSUMER_HANDOFFS.md`
  section `Legion`.
- Current scope authority:
  `docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_FINAL_CLOSURE_IMPLEMENTATION_PLAN_V0_2_2026-10-02.md`
  sections `1`, `4.3`.
- Current canonical policy:
  `docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md` §14.

Reason:

Legion was part of the historical matrix only. There is no current Issue #4
normal-entry or promised fallback evidence requiring it for final closure.
