ADAPTING consumer evidence update for `ai-skills-core--machine-update-orchestration`.

Reviewed branch commit `98feed2c2bb42eba7a624909567ed077522df65f` adds durable pending evidence stubs for the four remaining consumers:

- `results/ai-skills-core--machine-update-orchestration/consumers/Longleaf_Codex_PENDING.md`
- `results/ai-skills-core--machine-update-orchestration/consumers/Longleaf_Backup_Codex_PENDING.md`
- `results/ai-skills-core--machine-update-orchestration/consumers/CUHK_Workstation_WSL_Codex_PENDING.md`
- `results/ai-skills-core--machine-update-orchestration/consumers/Legion_PENDING.md`

These are explicit `PENDING_CONSUMER_AUTHORITY` placeholders, not PASS claims. They preserve the central release identity:

- AI_Skills `main` / `release`: `c7776e202ae0324fc00b719b6ef8224b8e0498fe`
- repository version: `5.2.0`
- `ai-skills-core`: `0.5`
- `workflow-core`: `0.4`

`Workstation` remains the only PASS consumer. The Project should remain `ADAPTING`; do not close this issue or move it to DONE until every required consumer is PASS or has a frozen durable N/A reason.
