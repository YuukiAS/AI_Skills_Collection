# Legion Machine Sync Evidence - 2026-09-29

Tracking task: `ai-skills-core--machine-update-orchestration`
Reviewed branch: `reviewed/ai-skills-core--machine-update-orchestration`
Consumer: `Legion`
Host/user: `Legion-Y9000P` / `legion-y9000p\yuukias`
Timestamp: `2026-09-29 12:09:06 +08:00`

## Discovery

| Field | Value |
|---|---|
| HOME | empty environment variable |
| USERPROFILE | `C:\Users\yuukias` |
| CODEX_HOME | empty environment variable; effective user config root observed at `C:\Users\yuukias\.codex` |
| Codex App CLI path | `C:\Users\yuukias\AppData\Local\OpenAI\Codex\bin\bffc5354119c8421\codex.exe` |
| Codex App CLI version | `codex-cli 0.154.0-alpha.6.2` |
| PATH `codex` version | `codex-cli 0.115.0`; this older entry did not expose `plugin` subcommands and was not used for plugin mutation |
| AI_Skills repository remote | `https://github.com/YuukiAS/AI_Skills_Collection.git` |
| AI_Skills formal release ref | `origin/release` = `72ebd56705713c01d05fef34ccab1c5c04c15671` |
| Latest formal release section read | `5.3.1 - 2026-09-28` |

## Before

Marketplace `yuukias-ai-skills` before migration:

```json
{
  "source_type": "git",
  "source": "https://github.com/YuukiAS/AI_Skills_Collection.git",
  "ref_name": null,
  "sparse_paths": [],
  "revision": "c967b3a74ece11a50238c63b8b7413709ec4cf34"
}
```

Before installed/enabled AI_Skills plugins:

| Plugin | Before |
|---|---|
| `ai-skills-core@yuukias-ai-skills` | installed, enabled, `4.0.0` |
| `presentations@yuukias-ai-skills` | installed, enabled, `4.0.0` |

Before not-installed AI_Skills plugins observed in local marketplace:

- `workflow-core`
- `writing-style`
- `research-writing`
- `bioinformatics`
- `medical-imaging`

## Formal Release Impact

Latest formal AI_Skills release read from `origin/release:CHANGELOG.md`:

- `5.3.1` affects `web-development` only: `0.2 -> 0.3`.
- It states all other central plugins are `NO_BUMP`, including `ai-skills-core 0.5` and `presentations 0.3`.
- The latest explicit `### Update impact` section read in the release history is from `5.2.0`; it declares required companions: none by default, and required managed consumer refresh: none automatically.

Resulting scope for this Legion sync:

- Update currently installed/enabled AI_Skills components only: `ai-skills-core`, `presentations`.
- Keep optional/uninstalled AI_Skills plugins uninstalled.
- No managed consumer refresh was triggered by release metadata.
- Route C Bridge Kit was discovery/classification only because the user explicitly required no Bridge runtime/source mutation.

## Actions

Official Codex App CLI used:

```powershell
& 'C:\Users\yuukias\AppData\Local\OpenAI\Codex\bin\bffc5354119c8421\codex.exe' plugin marketplace remove yuukias-ai-skills --json
& 'C:\Users\yuukias\AppData\Local\OpenAI\Codex\bin\bffc5354119c8421\codex.exe' plugin marketplace add https://github.com/YuukiAS/AI_Skills_Collection.git --ref release --sparse .agents/plugins --sparse plugins/codex/plugins --json
& 'C:\Users\yuukias\AppData\Local\OpenAI\Codex\bin\bffc5354119c8421\codex.exe' plugin marketplace upgrade yuukias-ai-skills --json
& 'C:\Users\yuukias\AppData\Local\OpenAI\Codex\bin\bffc5354119c8421\codex.exe' plugin add ai-skills-core@yuukias-ai-skills --json
& 'C:\Users\yuukias\AppData\Local\OpenAI\Codex\bin\bffc5354119c8421\codex.exe' plugin add presentations@yuukias-ai-skills --json
```

Official command results:

- Removed marketplace root: `C:\Users\yuukias\.codex\.tmp\marketplaces\yuukias-ai-skills`.
- Added marketplace root: `C:\Users\yuukias\.codex\.tmp\marketplaces\yuukias-ai-skills`.
- Upgraded marketplace `yuukias-ai-skills` with no errors.
- Installed `ai-skills-core@yuukias-ai-skills` version `0.5`.
- Installed `presentations@yuukias-ai-skills` version `0.3`.

## After

Marketplace `yuukias-ai-skills` after migration:

```toml
[marketplaces.yuukias-ai-skills]
source_type = "git"
source = "https://github.com/YuukiAS/AI_Skills_Collection.git"
ref = "release"
sparse_paths = [".agents/plugins", "plugins/codex/plugins"]
```

Installed snapshot metadata after migration:

```json
{
  "source_type": "git",
  "source": "https://github.com/YuukiAS/AI_Skills_Collection.git",
  "ref_name": "release",
  "sparse_paths": [
    ".agents/plugins",
    "plugins/codex/plugins"
  ],
  "revision": "72ebd56705713c01d05fef34ccab1c5c04c15671"
}
```

After installed/enabled AI_Skills plugins:

| Plugin | After |
|---|---|
| `ai-skills-core@yuukias-ai-skills` | installed, enabled, `0.5` |
| `presentations@yuukias-ai-skills` | installed, enabled, `0.3` |

After not-installed AI_Skills plugins:

- `workflow-core`
- `writing-style`
- `research-writing`
- `scientific-visualization`
- `web-development`
- `statistical-modeling`
- `bioinformatics`
- `medical-imaging`

Fresh-process evidence:

- A fresh `codex.exe plugin list` process after install reported `ai-skills-core@yuukias-ai-skills installed, enabled 0.5` and `presentations@yuukias-ai-skills installed, enabled 0.3`.
- The installed `ai-skills-core 0.5` cache contains `skills\orchestrator\SKILL.md` and `skills\bridge\SKILL.md`.
- A fresh Codex CLI ephemeral process then ran the normal entry request and loaded `ai-skills-core@0.5` from the installed cache. It read `machine-update-orchestrator`, verified the post-update state, and wrote `results/ai-skills-core--machine-update-orchestration/fresh_normal_entry_last_message.md`.
- Reload status for the fresh process: `YES`.

## Bridge Route C Discovery

| Field | Value |
|---|---|
| `ai-bridge` executable | `C:\Anaconda\Scripts\ai-bridge.exe` |
| `ai-bridge where` | `C:\Code\GPT_Codex_AI_Bridge_Kit` |
| runtime/import source | `C:\Code\GPT_Codex_AI_Bridge_Kit\ai_bridge_kit\__init__.py` |
| runtime version before | `0.7.1` |
| runtime version after | `0.7.1` |
| local Bridge branch | `main` |
| local Bridge HEAD | `3b061167794d593b113ca8f4a8a43c4c8000fc01` |
| Bridge `origin/release` | `6bbaca5a3af6240fbc88fa54cf78fa9acc147f67` |
| Bridge `origin/release` version source | `0.9.2` |
| Bridge `origin/main` | `0a6d55361f358cd38aee48e92af9ecf701145c64` |
| classification | `AHEAD/INCONSISTENT` for formal-consumer purposes: `origin/release` points at a 0.9.2 candidate while README still states current formal distribution is `0.9.1`; source/runtime intentionally unchanged |

Bridge validation note:

- `ai-bridge validate` against `C:\Code\AI_Skills_Collection` reported one workspace error: missing `prompts/tasks/`.
- This validates the current repository as a Bridge handoff workspace, not the Bridge package installation globally.

## Component Result Table

| Component | Before | After | Route | Actual action | Result |
|---|---|---|---|---|---|
| AI_Skills Marketplace source | Git source, implicit/default ref, full checkout, revision `c967b3a...` | Git source `ref = "release"`, sparse `.agents/plugins` + `plugins/codex/plugins`, revision `72ebd567...` | Route A | Official remove/add/upgrade | `UPDATED_RELOAD_REQUIRED` |
| `ai-skills-core` | `4.0.0`, installed/enabled | `0.5`, installed/enabled, includes `machine-update-orchestrator` and `bridge-kit-maintainer` | Route A | Official `plugin add` for existing installed plugin | `UPDATED_RELOAD_REQUIRED` |
| `presentations` | `4.0.0`, installed/enabled | `0.3`, installed/enabled | Route A | Official `plugin add` for existing installed plugin | `UPDATED_RELOAD_REQUIRED` |
| Release companions / managed consumers | none detected | none detected | Route B | No mutation; latest applicable `### Update impact` declares none by default | `ALREADY_CURRENT` |
| Fresh normal entry | not applicable before update | fresh `codex exec --ephemeral` loaded `ai-skills-core@0.5` and confirmed current state | Route A/B/C composition | Fresh discovery only; no mutation | `ALREADY_CURRENT` |
| Bridge Kit | runtime/source `0.7.1`, local checkout `3b061167...` | unchanged `0.7.1` | Route C | Discovery/classification only; no source/runtime mutation per user constraint | `AHEAD/INCONSISTENT_UNCHANGED` |

## Final Status

Consumer status: `PASS`

Reason: AI_Skills components were updated through official Codex App CLI commands, a separate fresh Codex CLI process loaded `AI Skills Maintainer` 0.5 and verified the current state, optional plugins remained uninstalled, and Bridge runtime/source was not mutated per user constraint.
