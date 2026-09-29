# Longleaf_Backup_Codex ADAPTING Evidence Stub

Task key: `ai-skills-core--machine-update-orchestration`  
Consumer: `Longleaf_Backup_Codex`  
Status: `PASS`  
Updated date: 2026-09-29

## Current Central Identity

- Tracking Issue: `#86`
- Project Status: `ADAPTING`
- Area: `ai-skills-core`
- Resolution commit: `c7776e202ae0324fc00b719b6ef8224b8e0498fe`
- Current formal AI_Skills `release` observed on this consumer: `72ebd56705713c01d05fef34ccab1c5c04c15671`
- Released `ai-skills-core`: `0.5`
- Released `workflow-core`: `0.4`

## Consumer Identity Verified

- Hostname: `c151404.ll.unc.edu`
- Platform: Longleaf Linux
- User: `aereinh`
- HOME: `/overflow/htzhu/mingcheng_new`
- CODEX_HOME: `/overflow/htzhu/mingcheng_new/.codex`
- Codex executable: `/overflow/htzhu/mingcheng_new/bin/codex`
- Codex version: `codex-cli 0.142.0`

## PASS Evidence

Durable evidence for this consumer is recorded in:

- `../LONGLEAF_BACKUP_CODEX_MACHINE_SYNC_2026-09-29.md`
- `../LONGLEAF_BACKUP_CODEX_MACHINE_SYNC_2026-09-29.json`
- `../fresh_longleaf_backup_plugin_replay_last_message.txt`

Summary:

- Marketplace `yuukias-ai-skills` is on `release` at `72ebd56705713c01d05fef34ccab1c5c04c15671`.
- Installed AI_Skills plugins were refreshed with official `codex plugin add` commands.
- `ai-skills-core@yuukias-ai-skills` is installed and enabled at `0.5`.
- Optional AI_Skills plugins that were not installed stayed uninstalled.
- Bridge Route C is aligned to formal release `6bbaca5a3af6240fbc88fa54cf78fa9acc147f67`, version `0.9.2`.
- `ai-bridge host validate` reports `overall state: configured`.
- Fresh Codex child session consumed the installed AI Skills Maintainer path and reported `STATE=ALREADY_CURRENT`.
- Replay wrapper returned `exit_code=70` because of the harness diagnostic `child Codex reported danger-full-access`; this is recorded in the evidence and did not indicate component misalignment.

## Forbidden Side Effects Preserved

This adapting run did not:

- use paid APIs;
- advance AI_Skills or Bridge `release`;
- install optional plugins that were previously absent;
- hand-edit Codex config;
- modify Bridge source logic;
- stash/reset/restore/clean user dirty work;
- modify unrelated research repositories;
- mark the Board `DONE`.

## Current Handoff

```text
CONSUMER=Longleaf_Backup_Codex
STATUS=PASS
OVERALL_DONE=NO
REMAINING_CONSUMERS=CUHK_Workstation_WSL_Codex
```
