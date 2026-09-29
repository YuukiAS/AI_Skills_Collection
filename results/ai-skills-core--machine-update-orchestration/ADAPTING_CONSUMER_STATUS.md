# ADAPTING Consumer Status Matrix

Task key: `ai-skills-core--machine-update-orchestration`  
Updated date: 2026-09-29

## Current Board State

- Tracking Issue: `#86`
- Project Status: `ADAPTING`
- Area: `ai-skills-core`
- Resolution commit: not assigned for final closure yet
- AI_Skills formal `release`: `a7028195f3e97d32d51c32ef8c87f658f92048e5`
- Current formal repository version: `5.4.0`
- Bridge current `main`: `5a640ec02a20106c778a35ba94eb2164d2b91537`
- Bridge formal `release`: `9dad0ba4bfa54e251f345091c5151ae991251ec9`
- Bridge formal version: `0.9.3`
- Closure freeze: `FINAL_CLOSURE_FREEZE.json`
- Overall DONE: `NO`

This matrix tracks the final closure freeze batch. It is not a runtime registry,
machine controller, daemon, watcher, database, or source of truth for Codex
config. Earlier pre-freeze consumer evidence remains in this directory as
history, but a current PASS for this closure batch requires fresh evidence from
that consumer after `FINAL_CLOSURE_FREEZE.json`.

Note: `Longleaf_Backup_Codex` live remote discovery observed
`YuukiAS/AI_Skills_Collection` `main=5351f304381501f27833e5c7fa4f536ae5b684f8`
and `release=a7028195f3e97d32d51c32ef8c87f658f92048e5`. The existing freeze is
reused for the batch; the ai-skills-core production/version diff from release to
current main was empty.

## Required Consumers

The final closure contract has exactly five required logical consumers:

1. `Longleaf_Codex`
2. `Longleaf_Backup_Codex`
3. `CUHK_Workstation_WSL_Codex`
4. `Workstation`
5. `Legion`

## Status Matrix

| Consumer | Current freeze status | Current identity / locator | Required next evidence | Durable evidence |
|---|---|---|---|---|
| `Longleaf_Codex` | `PASS` | hostname `c0810.ll.unc.edu`; Longleaf USERS namespace; user `aereinh`; `HOME=/users/a/e/aereinh`; `CODEX_HOME=/users/a/e/aereinh/.codex`; AI_Skills Marketplace `release@a7028195f3e97d32d51c32ef8c87f658f92048e5`; `ai-skills-core=0.5`; `writing-style=0.4`; `research-writing=0.2`; `web-development=0.4`; Bridge runtime/package `0.9.3`; Host Policy configured | none for this consumer in this freeze batch | `FINAL_CLOSURE_FREEZE.json`; `LONGLEAF_CODEX_FINAL_CLOSURE_REFRESH_2026-09-29.md`; `LONGLEAF_CODEX_FINAL_CLOSURE_REFRESH_2026-09-29.json`; `fresh_longleaf_users_direct_codex_last_message.txt` |
| `Longleaf_Backup_Codex` | `PASS` | hostname `c151404.ll.unc.edu`; Longleaf OVERFLOW namespace; user `aereinh`; `HOME=/overflow/htzhu/mingcheng_new`; `CODEX_HOME=/overflow/htzhu/mingcheng_new/.codex`; AI_Skills Marketplace `release@a7028195f3e97d32d51c32ef8c87f658f92048e5`; `ai-skills-core=0.5`; `workflow-core=0.4`; `writing-style=0.4`; `research-writing=0.2`; `presentations=0.3`; `bioinformatics=0.1`; `medical-imaging=0.1`; `web-development` not installed; Bridge runtime/package `0.9.3`; Bridge relation `ALIGNED`; Host Policy configured | none for this consumer in this freeze batch | `FINAL_CLOSURE_FREEZE.json`; `LONGLEAF_BACKUP_CODEX_FINAL_CLOSURE_REFRESH_2026-09-29.md`; `LONGLEAF_BACKUP_CODEX_FINAL_CLOSURE_REFRESH_2026-09-29.json`; `fresh_longleaf_backup_final_direct_codex_last_message.txt` |
| `CUHK_Workstation_WSL_Codex` | `PENDING_CURRENT_FREEZE_REFRESH` | Linux WSL2 consumer; exact current identity must be rediscovered on that consumer | run this same freeze batch from the WSL2 consumer | earlier pre-freeze files retained: `CUHK_WORKSTATION_WSL_CODEX_MACHINE_SYNC_2026-09-29.md`; `CUHK_WORKSTATION_WSL_CODEX_MACHINE_SYNC_2026-09-29.json` |
| `Workstation` | `PENDING_CURRENT_FREEZE_REFRESH` | Windows consumer; expected user `WORKSTATION\humc2`; expected `CODEX_HOME=C:\Users\humc2\.codex`; exact current identity must be rediscovered on that consumer | run this same freeze batch from Windows Workstation; only Windows may perform final aggregate cleanup after all five required consumers are current PASS | earlier pre-freeze Windows files retained: `WORKSTATION_WINDOWS_CODEX_MACHINE_SYNC_2026-09-29.md`; `WORKSTATION_WINDOWS_CODEX_MACHINE_SYNC_2026-09-29.json` |
| `Legion` | `PENDING_CURRENT_FREEZE_REFRESH` | must be discovered on that consumer | run this same freeze batch from `Legion` | earlier pre-freeze files retained: `LEGION_MACHINE_SYNC_2026-09-29.md`; `LEGION_MACHINE_SYNC_2026-09-29.json` |

## Consumer PASS Requirements

Per `docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md`, each consumer PASS requires:

- actual target identity;
- approved adaptation / update action;
- installed / loaded identity;
- relevant normal-entry consumption;
- fresh-session / restart boundary when required;
- risk-matched should-not-change / failure safety;
- durable evidence locator.

No consumer may be marked current-freeze PASS merely because another consumer
passed, or because it has older pre-freeze evidence.

## DONE Guard

Do not close Issue `#86` and do not set Project Status `DONE` until:

```text
exactly five required consumers fresh/current PASS under FINAL_CLOSURE_FREEZE
+ durable evidence complete
+ clean final aggregate evidence from latest main
+ Issue #86 reader-facing copy updated through Clear Writing
+ Project Status DONE and Resolution commit synchronized
+ Issue #86 closed
```

## Next Handoff

```text
NEXT_REQUIRED_CONSUMER=CUHK_Workstation_WSL_Codex
PROJECT_STATUS=ADAPTING
ISSUE_86_OPEN=YES
OVERALL_DONE=NO
```
