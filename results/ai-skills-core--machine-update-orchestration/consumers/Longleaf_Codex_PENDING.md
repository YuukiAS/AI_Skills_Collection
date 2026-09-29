# Longleaf_Codex Consumer Sync Evidence

Task key: `ai-skills-core--machine-update-orchestration`  
Consumer: `Longleaf_Codex`  
Status: `PENDING_BRIDGE_HOST_UPDATE`
Updated date: 2026-09-29

Longleaf_Codex has now been inspected from the actual consumer environment.

Durable evidence:

- `results/ai-skills-core--machine-update-orchestration/LONGLEAF_CODEX_MACHINE_SYNC_2026-09-29.md`
- `results/ai-skills-core--machine-update-orchestration/LONGLEAF_CODEX_MACHINE_SYNC_2026-09-29.json`

Summary:

- AI_Skills Marketplace was migrated from `main` to formal `release`.
- Already installed AI_Skills plugins were refreshed or verified at release versions.
- No optional uninstalled AI_Skills plugin was installed.
- `ai-skills-core@yuukias-ai-skills` is now installed/enabled at `0.5` and contains `machine-update-orchestrator`, `bridge-kit-maintainer`, and Route A/B/C references.
- Current Codex session requires restart/reopen to consume the newly installed plugin payload.
- Bridge Kit was checked and found lagging/drifted: local runtime remains `0.9.1`, formal `origin/release` is `0.9.2`, and `ai-bridge host validate` reports drift.
- Bridge source/runtime and Host Policy were not mutated in this run because the user boundary explicitly prohibited Bridge runtime/source mutation, and the Bridge checkout also has a local `.gitignore` modification.

Current handoff:

```text
CONSUMER=Longleaf_Codex
STATUS=PENDING_BRIDGE_HOST_UPDATE
AI_SKILLS_MARKETPLACE=UPDATED_TO_RELEASE
AI_SKILLS_INSTALLED_PLUGINS=UPDATED_OR_VERIFIED
BRIDGE=CHECKED_NOT_UPDATED
RELOAD_REQUIRED=YES
OVERALL_DONE=NO
```
