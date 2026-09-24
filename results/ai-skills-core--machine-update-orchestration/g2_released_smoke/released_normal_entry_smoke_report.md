# Released Normal Entry Smoke Report

## Scope

Read-only replay for the normal request `sync this machine`.

No update, install, remove, Git, Bridge, Host, network, or Marketplace mutation
commands were run.

## Evidence

- `codex --version`: `codex-cli 0.148.0-alpha.9`
- Marketplace query:
  `codex plugin list --marketplace yuukias-ai-skills --available --json`
- Installed plugin:
  `ai-skills-core@yuukias-ai-skills`
- Installed plugin version: `0.5`
- Installed/enabled state: `installed: true`, `enabled: true`
- Visible Marketplace source path:
  `/home/yuukias/.codex/.tmp/marketplaces/yuukias-ai-skills/plugins/codex/plugins/ai-skills-core`
- Production snapshot manifest read:
  `/home/yuukias/.codex/plugins/cache/yuukias-ai-skills/ai-skills-core/0.5/.codex-plugin/plugin.json`
- Production snapshot skill read:
  `/home/yuukias/.codex/plugins/cache/yuukias-ai-skills/ai-skills-core/0.5/skills/orchestrator/SKILL.md`

## Result

The released AI Skills Maintainer normal entry is loaded.

The internal skill that owns `sync this machine` is:

`ai-skills-core:machine-update-orchestrator`

The plugin-facing display name is `AI Skills Maintainer`.

The expected user-facing state for an already updated current session is:

`ALREADY_CURRENT`

If an update had actually installed or refreshed plugin code, the session-boundary
state would be `UPDATED_RELOAD_REQUIRED`; this replay was intentionally read-only,
so no reload-triggering mutation occurred.
