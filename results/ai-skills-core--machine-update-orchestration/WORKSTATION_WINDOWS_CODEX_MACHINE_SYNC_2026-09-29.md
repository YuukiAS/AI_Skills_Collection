# Workstation Windows Codex Freshness Refresh

Consumer: `Workstation_Windows_Codex`
Date: 2026-09-29
Status: `PASS`

Windows 本机 Codex 已对齐当前正式发布。Marketplace 从旧 revision
`72ebd56705713c01d05fef34ccab1c5c04c15671` 更新到
`a7028195f3e97d32d51c32ef8c87f658f92048e5`；已安装的
`writing-style` 从 `0.3` 更新到 `0.4`，并补齐任务明确要求的
`ai-skills-core 0.5`。其余 optional plugin 未安装，也没有在本轮新增。

Bridge runtime 与正式 `0.9.2` release 对齐，因此没有重装。Host Policy
最终为 `configured`。fresh Codex process 已实际加载 production
`ai-skills-core`，将“使用 AI Skills Maintainer，同步这台机器。”路由到
`machine-update-orchestrator`，返回 `ALREADY_CURRENT`。

## Identity

- hostname: `Workstation`
- platform: Windows
- user: `WORKSTATION\humc2`
- `HOME` environment variable: unset
- `USERPROFILE`: `C:\Users\humc2`
- resolved user home: `C:\Users\humc2`
- `CODEX_HOME` environment variable: unset
- effective `CODEX_HOME`: `C:\Users\humc2\.codex`
- Codex: `codex-cli 0.158.0-alpha.2.1`

## AI_Skills Marketplace

- name: `yuukias-ai-skills`
- source: `https://github.com/YuukiAS/AI_Skills_Collection.git`
- ref: `release`
- sparse paths: `.agents/plugins`, `plugins/codex/plugins`
- before revision: `72ebd56705713c01d05fef34ccab1c5c04c15671`
- current formal release: `a7028195f3e97d32d51c32ef8c87f658f92048e5`
- repository version: `5.4.0`
- after revision: `a7028195f3e97d32d51c32ef8c87f658f92048e5`

## Installed AI_Skills plugins

| Plugin | Before | Formal target | After | Action |
|---|---:|---:|---:|---|
| `writing-style@yuukias-ai-skills` | `0.3`, enabled | `0.4` | `0.4`, enabled | refreshed by formal Marketplace upgrade |
| `ai-skills-core@yuukias-ai-skills` | not installed | `0.5` | `0.5`, enabled | installed because this task requires the formal maintainer to remain enabled |

Confirmed uninstalled before and after:

- `workflow-core`
- `research-writing`
- `presentations`
- `scientific-visualization`
- `web-development`
- `statistical-modeling`
- `bioinformatics`
- `medical-imaging`

## Bridge Route C

- executable: `D:\Code\env\Scripts\ai-bridge.exe`
- editable source: `D:\Code\GPT_Codex_AI_Bridge_Kit`
- package/runtime version: `0.9.2`
- formal release ref: `6bbaca5a3af6240fbc88fa54cf78fa9acc147f67`
- local source HEAD: `9d15247d5cec5472a0f3c280a6bdd9d194a193fc`
- source state: clean; local `main` is intentionally not advanced to newer `origin/main`
- formal-release comparison: `origin/release..HEAD` changes only `README.md` and
  formal `0.9.2` closure evidence under `results/`; runtime/package content is
  unchanged from the formal release
- action: verification only; no source fast-forward and no editable-package refresh
- Host Policy: `ai-bridge host validate` -> `overall state: configured`

## Fresh normal entry

- method: production `ai-bridge plugin-replay`
- plugin: `ai-skills-core@yuukias-ai-skills`
- exact normal request: `使用 AI Skills Maintainer，同步这台机器。`
- first diagnostic run: `20260929T070615Z-4c247fca9702`
  - result: wrapper `CHILD_CONTRACT_DRIFT`, `exit_code=70`
  - cause: Windows CP1252 reader raised `UnicodeDecodeError` while consuming
    UTF-8 child output; this run is retained as failed diagnostic evidence and
    is not counted as acceptance
- accepted run: `20260929T070826Z-0baf3faafa82`
  - process-level recovery: `PYTHONUTF8=1`
  - status: `completed`
  - exit code: `0`
  - production plugin check: installed `true`
  - route: `machine-update-orchestrator`
  - write isolation: `passed`; canary unchanged
  - result state: `ALREADY_CURRENT`

Accepted run hashes:

- task input: `5deb112e2ba95f9ed6f3730ad44f8ccac44e1f29cd23103842a6ae7f3dd80c7d`
- machine-state input: `e9322b3f7af285d81dda8b174e711fda3a933c53429a5291dcbf955c399d832e`
- machine-local `run.json`: `7531A6373FAE8E33EEE6BE599E72D35E4D61FCA5FDC7516E2A1480BC6ECB2B6A`
- machine-local `last-message.txt`: `C3D97B092E7F14BD216EB90032F3942A3D5FE917EFC7E8033B3A2DFC7FB5BD88`
- machine-local generated report: `86F8534FF618C863FBBB9299AD53D0EA633A9EEB98EA2200196AD961F26A3746`

## Should-not-change

- optional AI_Skills plugins installed: no
- Bridge `release` advanced: no
- Bridge source logic modified: no
- Bridge editable package refreshed: no, already formal-runtime aligned
- Host Policy installed/rewritten: no, validation only
- unrelated consumer evidence modified: no
- paid API used: no
- private artifact uploaded: no

## Durable artifacts

- `WORKSTATION_WINDOWS_CODEX_MACHINE_SYNC_2026-09-29.json`
- `workstation_windows_fresh_normal_entry_task.md`
- `workstation_windows_machine_state_input.md`
- `workstation_windows_fresh_replay_run.json`
- `workstation_windows_fresh_replay_last_message.txt`
- `workstation_windows_fresh_normal_entry_report.md`
