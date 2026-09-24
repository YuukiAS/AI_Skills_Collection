ADAPTING consumer handoff packet added for `ai-skills-core--machine-update-orchestration`.

Reviewed branch commit `2fb3ef1d8de7b383812e9fa386eee4acfcf76f85` adds:

- `results/ai-skills-core--machine-update-orchestration/ADAPTING_CONSUMER_HANDOFF.md`

The handoff packet gives exact bounded prompts for the remaining consumers:

- `Longleaf_Codex`
- `Longleaf_Backup_Codex`
- `CUHK_Workstation_WSL_Codex`
- `Legion`

It does not authorize this `Workstation` session to control another machine, and it does not change any remaining consumer to PASS. Each packet must be used only from the named consumer itself, or from a session with explicit bounded authority for that exact consumer.

Current central identity remains unchanged:

- AI_Skills `main` / `release`: `c7776e202ae0324fc00b719b6ef8224b8e0498fe`
- repository version: `5.2.0`
- `ai-skills-core`: `0.5`
- `workflow-core`: `0.4`

`Workstation` remains the only PASS consumer. The Project should stay `ADAPTING`; do not close this issue or move it to DONE until every required consumer is PASS or has a frozen durable N/A reason.
