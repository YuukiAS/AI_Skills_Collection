# CUHK Workstation WSL Codex Machine Sync Evidence

Date: 2026-09-29
Task key: `ai-skills-core--machine-update-orchestration`
Consumer: `CUHK_Workstation_WSL_Codex`
Status: `PASS`

This evidence is for the required WSL consumer only. It does not reuse the
previous `Workstation`, `Workstation_Windows_Codex`, `Longleaf_*`, or `Legion`
consumer status.

## Consumer Identity

- hostname: `Workstation`
- platform: Linux WSL2, `6.6.87.2-microsoft-standard-WSL2`
- user: `yuukias`
- `HOME`: `/home/yuukias`
- `CODEX_HOME`: `/home/yuukias/.codex`
- Codex executable: `/home/yuukias/.local/bin/codex`
- Codex version: `codex-cli 0.148.0-alpha.9`

## AI Skills Marketplace

Before this run, `yuukias-ai-skills` was already configured as the formal
release Marketplace, but it was pinned to an older release snapshot:

- name: `yuukias-ai-skills`
- source: `https://github.com/YuukiAS/AI_Skills_Collection.git`
- ref: `release`
- sparse paths: `.agents/plugins`, `plugins/codex/plugins`
- owning config layer: `/home/yuukias/.codex/config.toml`
- before revision: `72ebd56705713c01d05fef34ccab1c5c04c15671`
- after revision: `a7028195f3e97d32d51c32ef8c87f658f92048e5`
- repository version after: `5.4.0`

Official command used:

```text
codex plugin marketplace upgrade yuukias-ai-skills --json
```

No legacy `main -> release` migration was needed because the Marketplace was
already configured with `ref = "release"`.

## Installed AI Skills Plugins

Only plugins already installed on this consumer were refreshed. Optional
uninstalled plugins stayed uninstalled.

| Plugin | Before | After | Action | Result |
|---|---:|---:|---|---|
| `workflow-core@yuukias-ai-skills` | `0.4 enabled` | `0.4 enabled` | official `codex plugin add` refresh | current |
| `ai-skills-core@yuukias-ai-skills` | `0.5 enabled` | `0.5 enabled` | official `codex plugin add` refresh | required maintainer installed/enabled |
| `writing-style@yuukias-ai-skills` | `0.3 enabled` | `0.4 enabled` | official `codex plugin add` refresh | updated |
| `research-writing@yuukias-ai-skills` | `0.2 enabled` | `0.2 enabled` | official `codex plugin add` refresh | current |
| `presentations@yuukias-ai-skills` | `0.3 enabled` | `0.3 enabled` | official `codex plugin add` refresh | current |
| `web-development@yuukias-ai-skills` | `0.3 enabled` | `0.4 enabled` | official `codex plugin add` refresh | updated |
| `statistical-modeling@yuukias-ai-skills` | `0.1 enabled` | `0.1 enabled` | official `codex plugin add` refresh | current |

Left uninstalled by design:

- `scientific-visualization@yuukias-ai-skills` `0.1`
- `bioinformatics@yuukias-ai-skills` `0.1`
- `medical-imaging@yuukias-ai-skills` `0.1`

## Bridge Route C

- `ai-bridge`: `/home/yuukias/conda/bin/ai-bridge`
- `ai-bridge where`: `/home/yuukias/GPT_Codex_AI_Bridge_Kit`
- origin: `https://github.com/YuukiAS/GPT_Codex_AI_Bridge_Kit.git`
- source branch: `main`
- local source HEAD: `5a640ec02a20106c778a35ba94eb2164d2b91537`
- remote formal `release`: `9dad0ba4bfa54e251f345091c5151ae991251ec9`
- remote `main`: `5a640ec02a20106c778a35ba94eb2164d2b91537`
- module version after: `0.9.3`
- package metadata after: `gpt-codex-ai-bridge-kit 0.9.3`
- editable source: `/home/yuukias/GPT_Codex_AI_Bridge_Kit`
- source state after: clean, `main...origin/main`

The fresh normal-entry process found the editable package metadata stale at
`0.7.3` and refreshed it to `0.9.3`. No Bridge source logic was modified and no
Bridge `release` ref was advanced.

Non-blocking release-channel observation: Bridge `origin/release` remains behind
`origin/main` while both exposed package/runtime versions now report `0.9.3`.
This consumer sync did not perform producer release-ref advancement.

## Host Policy

`ai-bridge host validate` completed with:

```text
overall state: configured
```

Because Host Policy was already configured, no `ai-bridge host install` was
required after the final validation.

## Fresh Normal Entry

- method: fresh `codex exec`
- session id: `01a0ec12-f8bd-74e0-90df-b28a5e96b350`
- exact request: `使用 AI Skills Maintainer，同步这台机器。`
- production plugin loaded from:
  `/home/yuukias/.codex/plugins/cache/yuukias-ai-skills/ai-skills-core/0.5`
- route observed: `machine-update-orchestrator`
- result: `UPDATED`

Fresh process verified:

1. production `ai-skills-core@yuukias-ai-skills` is installed/enabled at `0.5`;
2. the normal request routes to `machine-update-orchestrator`;
3. Marketplace `yuukias-ai-skills` is `release@a7028195f3e97d32d51c32ef8c87f658f92048e5`;
4. installed AI_Skills plugins are aligned with current formal release;
5. optional uninstalled AI_Skills plugins remain uninstalled;
6. Bridge module/package metadata reports `0.9.3`;
7. Host Policy validates as `configured`.

Fresh final message is recorded in
`cuhk_workstation_wsl_fresh_normal_entry_last_message.txt`.

## Should-Not-Change Evidence

- optional AI_Skills plugins installed: no
- AI_Skills `release` advanced: no
- Bridge `release` advanced: no
- Bridge source logic modified: no
- unrelated consumer evidence reused as PASS: no
- unrelated project/user dirty work overwritten: no
- paid API used: no
- private artifact uploaded: no

## Result

```text
CONSUMER=CUHK_Workstation_WSL_Codex
STATUS=PASS
MARKETPLACE=release@a7028195f3e97d32d51c32ef8c87f658f92048e5
AI_SKILLS_MAINTAINER=ai-skills-core@yuukias-ai-skills 0.5 enabled
UPDATED_PLUGINS=writing-style 0.3->0.4, web-development 0.3->0.4
BRIDGE_VERSION=0.9.3
HOST_POLICY=configured
FRESH_SESSION=codex exec session 01a0ec12-f8bd-74e0-90df-b28a5e96b350 UPDATED
OPTIONAL_PLUGINS_INSTALLED=NO
OVERALL_DONE=NO
ISSUE_86_CLOSE=NO
```
