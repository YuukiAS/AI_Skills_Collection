# ADAPTING Consumer Handoff Packets

Task key: `ai-skills-core--machine-update-orchestration`  
Prepared date: 2026-09-25

## Purpose

This file gives exact bounded prompts for the remaining Maintenance Board
`ADAPTING` consumers. It does not authorize the current `Workstation` session to
control another machine. Use a packet only from that target consumer itself, or
from a session with explicit bounded authority for that exact consumer.

Current central release identity:

- Tracking Issue: `#86`
- Project Status: `ADAPTING`
- Resolution commit: `c7776e202ae0324fc00b719b6ef8224b8e0498fe`
- AI_Skills `main`: `c7776e202ae0324fc00b719b6ef8224b8e0498fe`
- AI_Skills `release`: `c7776e202ae0324fc00b719b6ef8224b8e0498fe`
- repository version: `5.2.0`
- `ai-skills-core`: `0.5`
- `workflow-core`: `0.4`

Current aggregate:

- `Workstation`: `PASS`
- `Longleaf_Codex`: `PENDING_CONSUMER_AUTHORITY`
- `Longleaf_Backup_Codex`: `PENDING_CONSUMER_AUTHORITY`
- `CUHK_Workstation_WSL_Codex`: `PENDING_CONSUMER_AUTHORITY`
- `Legion`: `PENDING_CONSUMER_AUTHORITY`

Do not mark Issue `#86`, the Project, or this Goal `DONE` until every required
consumer is `PASS` or has a frozen durable `N/A` reason.

## Shared Consumer Prompt Template

Replace `<CONSUMER_NAME>` with one exact consumer below and run only on that
consumer or from an explicitly authorized session for that consumer.

```text
Continue AI_Skills_Collection Maintenance Board ADAPTING for consumer `<CONSUMER_NAME>`.

Repository: `YuukiAS/AI_Skills_Collection`
Task branch: `reviewed/ai-skills-core--machine-update-orchestration`
Tracking Issue: `#86`
Project Status must remain: `ADAPTING`
Resolution commit: `c7776e202ae0324fc00b719b6ef8224b8e0498fe`
AI_Skills `main` / `release`: `c7776e202ae0324fc00b719b6ef8224b8e0498fe`
Released repository version: `5.2.0`
Released `ai-skills-core`: `0.5`
Released `workflow-core`: `0.4`

Read first from the reviewed branch:

- `results/ai-skills-core--machine-update-orchestration/ADAPTING_CONSUMER_RUNBOOK.md`
- `results/ai-skills-core--machine-update-orchestration/ADAPTING_CONSUMER_STATUS.md`
- `results/ai-skills-core--machine-update-orchestration/consumers/<CONSUMER_NAME>_PENDING.md`

Scope:

1. Discover this consumer's actual identity without asking for paths/versions/commits.
2. Inspect this consumer's Codex Marketplace/plugin state.
3. If this consumer has the expected legacy `yuukias-ai-skills` source at `main`, migrate it to `release` using official Codex Marketplace/plugin commands only, preserving exact old metadata for restoration.
4. Reinstall/verify `ai-skills-core@yuukias-ai-skills` version `0.5` when needed.
5. Run a fresh installed production normal-entry smoke for `sync this machine` through `ai-bridge plugin-replay` if available.
6. Update that consumer's pending evidence file with PASS / N/A / FAILED_CLOSED / still PENDING truth, including all required evidence fields from the runbook.
7. Update `ADAPTING_CONSUMER_STATUS.md` and `.json` for this consumer only.
8. Commit and push the same reviewed branch with durable evidence.
9. If this was the final remaining consumer and all consumers are PASS/N/A, then and only then follow the Maintenance Board DONE closure policy.

Forbidden:

- no paid API;
- no automation;
- no Bridge runtime/source mutation;
- no Bridge `release` advancement;
- no AI_Skills `release` advancement unless a separate formal release task authorizes it;
- no unrelated project mutation;
- no hand-editing Codex config;
- no force push, reset, stash, clean, or destructive Git;
- no PASS inference from `Workstation` or another consumer.

If this session does not have authority for `<CONSUMER_NAME>`, leave the status as `PENDING_CONSUMER_AUTHORITY`, record that durable fact, and stop without trying another consumer.
```

## Consumer-Specific Packets

### Longleaf_Codex

Use the shared prompt with:

```text
<CONSUMER_NAME>=Longleaf_Codex
```

Durable pending evidence file:

```text
results/ai-skills-core--machine-update-orchestration/consumers/Longleaf_Codex_PENDING.md
```

Current status: `PENDING_CONSUMER_AUTHORITY`

### Longleaf_Backup_Codex

Use the shared prompt with:

```text
<CONSUMER_NAME>=Longleaf_Backup_Codex
```

Durable pending evidence file:

```text
results/ai-skills-core--machine-update-orchestration/consumers/Longleaf_Backup_Codex_PENDING.md
```

Current status: `PENDING_CONSUMER_AUTHORITY`

### CUHK_Workstation_WSL_Codex

Use the shared prompt with:

```text
<CONSUMER_NAME>=CUHK_Workstation_WSL_Codex
```

Durable pending evidence file:

```text
results/ai-skills-core--machine-update-orchestration/consumers/CUHK_Workstation_WSL_Codex_PENDING.md
```

Current status: `PENDING_CONSUMER_AUTHORITY`

### Legion

Use the shared prompt with:

```text
<CONSUMER_NAME>=Legion
```

Durable pending evidence file:

```text
results/ai-skills-core--machine-update-orchestration/consumers/Legion_PENDING.md
```

Current status: `PENDING_CONSUMER_AUTHORITY`

## Current Workstation Boundary

The current `Workstation` consumer already has PASS evidence in
`ADAPTING_CONSUMER_EVIDENCE.md`. Do not rerun or reinterpret that PASS as proof
for any other consumer.

This handoff file is evidence preparation only. It does not prove remaining
consumer adaptation and does not change `OVERALL_DONE=NO`.
