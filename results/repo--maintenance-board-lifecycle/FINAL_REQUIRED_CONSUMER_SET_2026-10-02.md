# Final Required Consumer Set — 2026-10-02

Task: `repo--maintenance-board-lifecycle`
Tracking Issue: `#4`
Repository: `YuukiAS/AI_Skills_Collection`

## Result

```text
CURRENT_REQUIRED_SET_FROZEN = YES
CURRENT_REQUIRED_SET = AI Research Stack ChatGPT Project instructions, Longleaf_Codex
PROJECT_INSTRUCTIONS = PASS
LONGLEAF_CODEX = PASS
ALL_REQUIRED_CONSUMERS = PASS_OR_NA
FINAL_REMAINING_CONSUMER = NONE
ISSUE_4_READY_FOR_COMPLETED_CLOSE = YES
```

## Required Consumers

### AI Research Stack ChatGPT Project instructions

Status: `PASS`

Evidence:
`results/repo--maintenance-board-lifecycle/CENTRAL_CLOSURE_STATUS.md`

The user confirmed semantic installation of the Maintenance Board trigger in
the AI Research Stack ChatGPT Project instructions. The installed semantics
cover latest-main board policy reading, active tracking-state maintenance,
exact pending Project mutation output when a surface cannot mutate Project
metadata, and no manual Kanban maintenance request to the user.

### Longleaf_Codex

Status: `PASS`

Evidence:

- #92 v7 final closure: `CLOSED / COMPLETED`, Project `DONE`.
- v7 final closure commit:
  `700234d7e94bb5613f951b8adeb7155d3b15ec3f`.
- `results/repo--maintenance-board-issue-maturity/V7_FINAL_CLOSURE.md`
  records `V7_ISSUE_MATURITY = COMPLETE`.
- `results/repo--maintenance-board-lifecycle/METADATA_AUDIT_CURRENT_2026-10-02.json`
  records current live audit evidence.
- #93 is a real tracked standalone-skill Issue with Project `DOING`, Area
  `standalone-skill`, correct taxonomy labels, and source backlinks in
  `docs/skill-todos/project-instructions-editor.md`.
- #94 is the historical pre-admission smoke Issue: `CLOSED / NOT_PLANNED`,
  label `triage:needed`, no Project item.
- Auto-add open-only evidence:
  `results/repo--maintenance-board-issue-maturity/STAGE_B_AUTO_ADD_POST_CHANGE.md`.
- Duplicate false-DONE repair evidence:
  `results/repo--maintenance-board-issue-maturity/STAGE_B_DUPLICATE_REPAIR_V0_4.json`.

## Historical Non-Required Consumers

The following are historical evidence only, not current Issue #4 closure
prerequisites:

```text
CUHK_Workstation_WSL_Codex = NOT_REQUIRED_FOR_ISSUE_4_CURRENT_CONTRACT
Longleaf_Backup_Codex = NOT_REQUIRED_FOR_ISSUE_4_CURRENT_CONTRACT
Workstation = NOT_REQUIRED_FOR_ISSUE_4_CURRENT_CONTRACT
Legion = NOT_REQUIRED_FOR_ISSUE_4_CURRENT_CONTRACT
```

This is not a PASS shortcut and not outage-based N/A. It is the current
required-set determination under v6.1: a machine is required only when it is an
actual normal-entry consumer or an explicitly promised fallback environment for
the tracked item's frozen completion claim.

## Boundary

No Workstation / WSL access was used or required. No machine adaptation remains
for Issue #4 under the current contract.
