# ADAPTING Consumer Status Matrix

Task key: `ai-skills-core--machine-update-orchestration`  
Updated date: 2026-09-29

## Current Board State

- Tracking Issue: `#86`
- Project Status: `ADAPTING`
- Area: `ai-skills-core`
- Resolution commit: `c7776e202ae0324fc00b719b6ef8224b8e0498fe`
- Formal AI_Skills `main`: `c7776e202ae0324fc00b719b6ef8224b8e0498fe`
- Formal AI_Skills `release`: `c7776e202ae0324fc00b719b6ef8224b8e0498fe`
- Overall DONE: `NO`

This matrix is an audit surface for Maintenance Board ADAPTING. It is not a
runtime registry, machine controller, daemon, watcher, database, or source of
truth for Codex config. Each consumer row must be backed by that consumer's own
durable evidence before it can be marked PASS or N/A.

## Status Matrix

| Consumer | Status | Current identity / locator | Required next evidence | Durable evidence |
|---|---|---|---|---|
| `Workstation` | `PASS` | hostname `Workstation`; WSL2; user `yuukias`; `CODEX_HOME=/home/yuukias/.codex` | none for this consumer unless future release changes scope | `ADAPTING_CONSUMER_EVIDENCE.md`; `G2_POST_REVIEW_PROMOTION_EVIDENCE.md`; `g2_released_smoke/released_normal_entry_run.json` |
| `Longleaf_Codex` | `PASS` | hostname `c0810.ll.unc.edu`; user `aereinh`; `HOME=/overflow/htzhu/mingcheng_new`; `CODEX_HOME=/overflow/htzhu/mingcheng_new/.codex`; AI_Skills Marketplace `release`; `ai-skills-core=0.5`; Bridge runtime/package `0.9.2`; Host Policy configured | none for this consumer unless future release changes scope | `LONGLEAF_CODEX_MACHINE_SYNC_2026-09-29.md`; `LONGLEAF_CODEX_MACHINE_SYNC_2026-09-29.json`; `fresh_longleaf_direct_codex_last_message.txt` |
| `Longleaf_Backup_Codex` | `PASS` | hostname `c151404.ll.unc.edu`; user `aereinh`; `HOME=/overflow/htzhu/mingcheng_new`; `CODEX_HOME=/overflow/htzhu/mingcheng_new/.codex`; AI_Skills Marketplace `release@72ebd56705713c01d05fef34ccab1c5c04c15671`; `ai-skills-core=0.5`; Bridge runtime/package `0.9.2`; Host Policy configured | none for this consumer unless future release changes scope | `LONGLEAF_BACKUP_CODEX_MACHINE_SYNC_2026-09-29.md`; `LONGLEAF_BACKUP_CODEX_MACHINE_SYNC_2026-09-29.json`; `fresh_longleaf_backup_direct_codex_last_message.txt`; `fresh_longleaf_backup_plugin_replay_last_message.txt`; `consumers/Longleaf_Backup_Codex_PENDING.md` |
| `CUHK_Workstation_WSL_Codex` | `PENDING_CONSUMER_AUTHORITY` | unknown in this task; not inferred | bounded access to that consumer; discover identity; inspect Marketplace/plugin state; migrate/reinstall if needed; production normal-entry smoke | `consumers/CUHK_Workstation_WSL_Codex_PENDING.md`; then update with runbook result |
| `Legion` | `PASS` | hostname `Legion-Y9000P`; Windows; user `legion-y9000p\yuukias`; effective Codex root `C:\Users\yuukias\.codex`; AI_Skills Marketplace `release`; `ai-skills-core=0.5`; `presentations=0.3`; Bridge runtime/package `0.9.2` | none for this consumer unless future release changes scope | `LEGION_MACHINE_SYNC_2026-09-29.md`; `LEGION_MACHINE_SYNC_2026-09-29.json`; `fresh_normal_entry_last_message.md` |

## Consumer PASS Requirements

Per `docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md`, each consumer PASS requires:

- actual target identity;
- approved adaptation / update action;
- installed / loaded identity;
- relevant normal-entry consumption;
- fresh-session / restart boundary when required;
- risk-matched should-not-change / failure safety;
- durable evidence locator.

`Workstation`, `Longleaf_Codex`, `Longleaf_Backup_Codex`, and `Legion` currently meet the consumer PASS requirements.

## DONE Guard

Do not close Issue `#86` and do not set Project Status `DONE` until:

```text
all required consumers PASS/N/A
+ durable evidence complete
+ Resolution commit = c7776e202ae0324fc00b719b6ef8224b8e0498fe
+ tracking Issue completed close
+ issue-closed workflow -> DONE
```

No remaining consumer may be marked PASS merely because another consumer passed. `CUHK_Workstation_WSL_Codex` remains pending consumer authority.
N/A requires a frozen durable reason.

Pending consumer-specific stubs now live under `consumers/`; they are
durable placeholders only and do not prove PASS. Exact bounded prompts for
executing each remaining consumer are recorded in
`ADAPTING_CONSUMER_HANDOFF.md`.

## Next Handoff

```text
NEXT_HANDOFF=CONSUMER_ADAPTATION_REQUIRED
PROJECT_STATUS=ADAPTING
ISSUE_86_OPEN=YES
OVERALL_DONE=NO
```
