# Legion Machine Sync Evidence - 2026-09-29

Tracking task: `ai-skills-core--machine-update-orchestration`
Reviewed branch: `reviewed/ai-skills-core--machine-update-orchestration`
Consumer: `Legion`
Host/user: `Legion-Y9000P` / `legion-y9000p\yuukias`
Timestamp: `2026-09-29 12:09:06 +08:00`
Last updated: `2026-09-29 12:29:01 +08:00`

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
- Route C Bridge Kit required a formal runtime refresh after dynamic Bridge
  release discovery proved that `refs/heads/release` is the formally closed
  Bridge Kit `0.9.2` target.

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
| runtime version after | `0.9.2` |
| local Bridge branch | `main` |
| local Bridge HEAD before | `3b061167794d593b113ca8f4a8a43c4c8000fc01` |
| local Bridge HEAD after | `6bbaca5a3af6240fbc88fa54cf78fa9acc147f67` |
| Bridge `origin/release` | `6bbaca5a3af6240fbc88fa54cf78fa9acc147f67` |
| Bridge `origin/release` version source | `0.9.2` |
| Bridge `origin/main` | `6043689d6464fc64f51666a9198ffd509fff5a70` |
| classification | `ALIGNED`: formal release closure evidence on `main` binds Bridge Kit `0.9.2` to release target `6bbaca5a3af6240fbc88fa54cf78fa9acc147f67`, and remote `refs/heads/release` equals that target |

Formal Bridge release authority used for the corrected Route C classification:

- `origin/release:pyproject.toml` declares `version = "0.9.2"`.
- `origin/release:ai_bridge_kit/__init__.py` declares `__version__ = "0.9.2"`.
- `origin/release:CHANGELOG.md` contains `## 0.9.2 - 2026-09-25`.
- `origin/release:AGENTS.md` contains the formal distribution owner locator
  delegating Bridge distribution/version closure to AI Skills Maintainer /
  `bridge-kit-maintainer`.
- `origin/main:results/bridge-core--unattended-execution-refinement/FORMAL_RELEASE_CLOSURE.md`
  records `FORMAL_DISTRIBUTION_COMPLETE=YES`,
  `RELEASE_RELATION=ALIGNED`, `VERSION=0.9.2`, and
  `FORMAL_RELEASE_TARGET=6bbaca5a3af6240fbc88fa54cf78fa9acc147f67`.
- `origin/main:README.md` has the post-closure documentation truth: current
  formal distribution version is `0.9.2`; later `main` evidence/docs commits
  do not automatically become release targets.
- The stale `origin/release:README.md` sentence still says `0.9.1` / `0.9.2`
  candidate, but it is not the formal release authority by itself and is
  superseded for Route C classification by the version sources, changelog,
  owner locator, closure evidence, and remote release ref equality above.

Route C update actions:

- Verified canonical checkout `C:\Code\GPT_Codex_AI_Bridge_Kit` origin is
  `https://github.com/YuukiAS/GPT_Codex_AI_Bridge_Kit.git`.
- Verified checkout was clean and `HEAD` was an ancestor of `origin/release`.
- Fast-forwarded the canonical checkout from
  `3b061167794d593b113ca8f4a8a43c4c8000fc01` to
  `6bbaca5a3af6240fbc88fa54cf78fa9acc147f67`.
- Refreshed the existing editable package / entry point with
  `python -m pip install -e C:\Code\GPT_Codex_AI_Bridge_Kit`.
- Verified package metadata and module version:
  `gpt-codex-ai-bridge-kit==0.9.2` and `ai_bridge_kit.__version__ == "0.9.2"`.
- Verified `ai-bridge where` still resolves to
  `C:\Code\GPT_Codex_AI_Bridge_Kit`.
- Did not advance Bridge `release`, did not track or merge `origin/main`, did
  not edit Bridge source logic, and did not modify Host / Reviewed Mode /
  Persistent Run behavior.

Bridge validation note:

- `ai-bridge validate` against `C:\Code\AI_Skills_Collection` reported one workspace error: missing `prompts/tasks/`.
- This validates the current repository as a Bridge handoff workspace, not the Bridge package installation globally.
- `ai-bridge --version` remains unsupported as a CLI option; the supported
  version evidence for this install is package metadata plus
  `ai_bridge_kit.__version__`.

## Component Result Table

| Component | Before | After | Route | Actual action | Result |
|---|---|---|---|---|---|
| AI_Skills Marketplace source | Git source, implicit/default ref, full checkout, revision `c967b3a...` | Git source `ref = "release"`, sparse `.agents/plugins` + `plugins/codex/plugins`, revision `72ebd567...` | Route A | Official remove/add/upgrade | `UPDATED_RELOAD_REQUIRED` |
| `ai-skills-core` | `4.0.0`, installed/enabled | `0.5`, installed/enabled, includes `machine-update-orchestrator` and `bridge-kit-maintainer` | Route A | Official `plugin add` for existing installed plugin | `UPDATED_RELOAD_REQUIRED` |
| `presentations` | `4.0.0`, installed/enabled | `0.3`, installed/enabled | Route A | Official `plugin add` for existing installed plugin | `UPDATED_RELOAD_REQUIRED` |
| Release companions / managed consumers | none detected | none detected | Route B | No mutation; latest applicable `### Update impact` declares none by default | `ALREADY_CURRENT` |
| Fresh normal entry | pre-Bridge correction verification had stale Route C classification | fresh App CLI process loaded `AI Skills Maintainer` and confirmed AI_Skills release state plus Bridge `0.9.2` runtime/package | Route A/B/C composition | Fresh discovery/verification after Bridge update | `PASS` |
| Bridge Kit | runtime/source `0.7.1`, local checkout `3b061167...` | runtime/package `0.9.2`, local checkout `6bbaca5...` = `origin/release` | Route C | Fast-forward canonical checkout to formal `release`; refresh existing editable package; verify runtime identity | `UPDATED` |

## Final Status

Consumer status: `PASS`

Reason: AI_Skills components were updated through official Codex App CLI
commands and remained current; Bridge Route C was corrected from stale README
classification to formal remote release evidence, then updated from `0.7.1` to
`0.9.2`; a separate fresh Codex App CLI process loaded `AI Skills Maintainer`
0.5 and verified AI_Skills plus Bridge current state. Optional plugins remained
uninstalled. Bridge `release` was not advanced, `main` was not followed, and
Host / Reviewed Mode / Persistent Run behavior was not modified.
