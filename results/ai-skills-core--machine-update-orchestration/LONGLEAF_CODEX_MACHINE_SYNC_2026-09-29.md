# Longleaf_Codex Machine Sync Evidence - 2026-09-29

Tracking task: `ai-skills-core--machine-update-orchestration`
Reviewed branch: `reviewed/ai-skills-core--machine-update-orchestration`
Consumer: `Longleaf_Codex`
Host/user: `c0810.ll.unc.edu` / `aereinh`
Timestamp: `2026-09-29 00:51:22 EDT`

## Discovery

| Field | Value |
|---|---|
| HOME | `/overflow/htzhu/mingcheng_new` |
| CODEX_HOME | `/overflow/htzhu/mingcheng_new/.codex` |
| Codex CLI version | `codex-cli 0.142.0` |
| AI_Skills repository remote | `https://github.com/YuukiAS/AI_Skills_Collection.git` |
| AI_Skills formal release ref | `origin/release` = `72ebd56705713c01d05fef34ccab1c5c04c15671` |
| Latest formal release section read | `5.3.1 - 2026-09-28` |

## Branch Cleanup Preflight

Remote cleanup was performed before sync on the shared AI_Skills checkout.

- Deleted remote A-list branches after verifying their tips were ancestors of latest `origin/main` and there were no open PRs.
- Deleted additional user-authorized remote branches: `reviewed/050_writing_style_host_codex_runtime`, `reviewed/051_writing_style_rebuild`, `reviewed/053_clear_writing_release_quality_hardening`, and `reviewed/054_clear_writing_release_closure`.
- Kept other B-list diverged branches not explicitly named by the user.
- Local branch cleanup used only `git branch -d`. Only `reviewed/infra_paid_review_safety_migration_20260903` was deleted locally; other local branches were protected by current/prunable worktree records or were absent.

## Before

Marketplace `yuukias-ai-skills` before migration:

```toml
[marketplaces.yuukias-ai-skills]
source_type = "git"
source = "https://github.com/YuukiAS/AI_Skills_Collection.git"
ref = "main"
sparse_paths = [".agents/plugins", "plugins/codex/plugins"]
last_revision = "c4fd2c64b3211529a61a33e5f80eb7afc2e2960a"
```

Before installed/enabled AI_Skills plugins:

| Plugin | Before |
|---|---|
| `workflow-core@yuukias-ai-skills` | installed, enabled, `0.1` |
| `ai-skills-core@yuukias-ai-skills` | installed, enabled, `0.2` |
| `writing-style@yuukias-ai-skills` | installed, enabled, `0.3` |
| `research-writing@yuukias-ai-skills` | installed, enabled, `0.1` |
| `presentations@yuukias-ai-skills` | installed, enabled, `0.3` |
| `bioinformatics@yuukias-ai-skills` | installed, enabled, `0.1` |
| `medical-imaging@yuukias-ai-skills` | installed, enabled, `0.1` |

Before not-installed AI_Skills plugins observed in local marketplace:

- `scientific-visualization`
- `web-development`
- `statistical-modeling`

## Formal Release Impact

Latest formal AI_Skills release read from `origin/release:CHANGELOG.md`:

- `5.3.1` affects `web-development` only: `0.2 -> 0.3`.
- It states all other central plugins are `NO_BUMP`, including `workflow-core 0.4`, `ai-skills-core 0.5`, `writing-style 0.3`, `research-writing 0.2`, `presentations 0.3`, `bioinformatics 0.1`, and `medical-imaging 0.1`.
- The `5.3.1` section has no `### Update impact`, so it does not require Route B companion mutation or Bridge managed-consumer refresh.

Resulting scope for this Longleaf_Codex sync:

- Route A: migrate the AI_Skills Marketplace from legacy `main` to formal `release`; refresh only already installed/enabled AI_Skills plugins.
- Route B: no required companions declared by formal release metadata.
- Route C: inspect Bridge Kit source/runtime/formal release state. Do not modify Bridge runtime/source under the current user boundary.

## Actions

Official Codex CLI commands used:

```bash
codex plugin marketplace remove yuukias-ai-skills --json
codex plugin marketplace add YuukiAS/AI_Skills_Collection --ref release --sparse .agents/plugins --sparse plugins/codex/plugins --json
codex plugin add ai-skills-core@yuukias-ai-skills --json
codex plugin add workflow-core@yuukias-ai-skills --json
codex plugin add writing-style@yuukias-ai-skills --json
codex plugin add research-writing@yuukias-ai-skills --json
codex plugin add presentations@yuukias-ai-skills --json
codex plugin add medical-imaging@yuukias-ai-skills --json
```

Notes:

- `bioinformatics@yuukias-ai-skills` was already installed/enabled at release version `0.1`; no refresh command was rerun after Auto-review rejected an additional add attempt as too broad.
- No optional AI_Skills plugin was newly installed.
- Current Codex session did not hot-reload the newly installed `ai-skills-core 0.5`; a fresh Codex process/session is required for normal interactive consumption.

## After

Marketplace `yuukias-ai-skills` after migration:

```toml
[marketplaces.yuukias-ai-skills]
source_type = "git"
source = "https://github.com/YuukiAS/AI_Skills_Collection.git"
ref = "release"
sparse_paths = [".agents/plugins", "plugins/codex/plugins"]
```

Installed snapshot after migration:

```text
branch: release
revision: 72ebd56705713c01d05fef34ccab1c5c04c15671
```

After installed/enabled AI_Skills plugins:

| Plugin | After |
|---|---|
| `workflow-core@yuukias-ai-skills` | installed, enabled, `0.4` |
| `ai-skills-core@yuukias-ai-skills` | installed, enabled, `0.5` |
| `writing-style@yuukias-ai-skills` | installed, enabled, `0.3` |
| `research-writing@yuukias-ai-skills` | installed, enabled, `0.2` |
| `presentations@yuukias-ai-skills` | installed, enabled, `0.3` |
| `bioinformatics@yuukias-ai-skills` | installed, enabled, `0.1` |
| `medical-imaging@yuukias-ai-skills` | installed, enabled, `0.1` |

After not-installed AI_Skills plugins:

- `scientific-visualization`
- `web-development`
- `statistical-modeling`

Installed `ai-skills-core 0.5` verification:

- The installed release payload contains `skills/orchestrator/SKILL.md` with `name: machine-update-orchestrator`.
- It also contains Route references:
  - `references/ai-skills-plugin-profile-update.md`
  - `references/cross-layer-stack-workflow-composition.md`
  - `references/bridge-kit-distribution-runtime-update.md`

## Standalone / Legacy Codex-Home Skills

Observed legacy/advanced codex-home skill state:

- `/overflow/htzhu/mingcheng_new/.codex-global/skills/tools-documents-media-render-chinese-math-pdf` is symlinked to this shared AI_Skills checkout.
- Its managed manifest points at target `/overflow/htzhu/mingcheng_new/.codex-global`, not the active `CODEX_HOME`.
- `render-chinese-math-pdf` is behind the formal release source, but refreshing it would mutate through the shared development checkout/source path, so no update was performed in this consumer sync.
- `slurm-workflows` exists as a legacy local skill without a matching manifest update path observed in this run.

## Bridge Route C Discovery

| Field | Value |
|---|---|
| `ai-bridge` executable | `/overflow/htzhu/mingcheng_new/.local/bin/ai-bridge` |
| `ai-bridge where` | `/overflow/htzhu/mingcheng_new/GPT_Codex_AI_Bridge_Kit` |
| runtime/import source | `/overflow/htzhu/mingcheng_new/GPT_Codex_AI_Bridge_Kit/ai_bridge_kit/__init__.py` |
| runtime version before/after | `0.9.1` / `0.9.1` |
| local Bridge branch | `main` |
| local Bridge HEAD | `ff22c97c8193e110d606e179ec1a8a2741b97fad` |
| local Bridge dirty state | `.gitignore` modified |
| Bridge `origin/release` | `6bbaca5a3af6240fbc88fa54cf78fa9acc147f67` |
| Bridge `origin/release` version source | `0.9.2` |
| Bridge `origin/main` | `7573dba5a9d8085480d25feab7e86ccd90d6538f` |
| release relation | `local_head_ancestor_of_release=YES`; local checkout is `17` commits behind `origin/release` |
| classification | `LAGGING_LOCAL_RUNTIME`: formal Bridge release `0.9.2` exists, while current editable runtime remains `0.9.1` |

Formal Bridge release evidence read:

- `origin/release:pyproject.toml` declares `version = "0.9.2"`.
- `origin/release:ai_bridge_kit/__init__.py` declares `__version__ = "0.9.2"`.
- `origin/release:CHANGELOG.md` contains `## 0.9.2 - 2026-09-25`.
- Bridge `AGENTS.md` contains the owner locator delegating formal distribution/version closure to AI Skills Maintainer / `bridge-kit-maintainer`.

Bridge/Host validation:

- `ai-bridge host validate` returned `overall state: drifted`.
- Drift evidence included `global AGENTS managed block: drifted`, `ai-bridge-global.rules: drifted`, missing expected allow matches for bounded Bridge/GitHub commands, and an unexpected allow for raw `git push origin main`.

Bridge actions not taken:

- Did not advance Bridge `release`.
- Did not fast-forward the Bridge checkout.
- Did not run `pip install -e` for Bridge.
- Did not run `ai-bridge host install`.
- Did not modify Bridge source/runtime or Host Policy files.

## Result

Status: `PENDING_BRIDGE_HOST_UPDATE`

AI_Skills Marketplace and already-installed AI_Skills plugins were updated to the formal release channel. Bridge Kit and Host Policy were inspected and found lagging/drifted, but were not mutated because this run's user boundary explicitly prohibited Bridge runtime/source mutation and the Bridge checkout was dirty.

Current session reload status: `UPDATED_RELOAD_REQUIRED`.
