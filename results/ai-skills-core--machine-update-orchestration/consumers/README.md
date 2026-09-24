# ADAPTING Consumer Evidence Index

Task key: `ai-skills-core--machine-update-orchestration`  
Prepared date: 2026-09-25

This directory holds per-consumer durable evidence surfaces for Maintenance
Board `ADAPTING`. These files are not a registry, controller, daemon, watcher,
or source of truth for Codex config. They prevent unresolved consumers from
being represented only by a generic runbook.

| Consumer | Status | Evidence |
|---|---|---|
| `Workstation` | `PASS` | `../ADAPTING_CONSUMER_EVIDENCE.md` |
| `Longleaf_Codex` | `PENDING_CONSUMER_AUTHORITY` | `Longleaf_Codex_PENDING.md` |
| `Longleaf_Backup_Codex` | `PENDING_CONSUMER_AUTHORITY` | `Longleaf_Backup_Codex_PENDING.md` |
| `CUHK_Workstation_WSL_Codex` | `PENDING_CONSUMER_AUTHORITY` | `CUHK_Workstation_WSL_Codex_PENDING.md` |
| `Legion` | `PENDING_CONSUMER_AUTHORITY` | `Legion_PENDING.md` |

Each pending consumer must be updated from that exact consumer or an explicitly
authorized surface for that consumer, following `../ADAPTING_CONSUMER_RUNBOOK.md`.
Do not mark Issue `#86` or the Project `DONE` until every required consumer is
`PASS` or has a frozen durable `N/A` reason.
