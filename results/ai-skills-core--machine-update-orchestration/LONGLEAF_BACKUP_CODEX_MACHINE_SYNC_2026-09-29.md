# Longleaf Backup Codex Machine Sync Evidence

Date: 2026-09-29  
Task key: `ai-skills-core--machine-update-orchestration`  
Consumer: `Longleaf_Backup_Codex`  
Result: `PASS`

## Consumer Identity

- Hostname: `c151404.ll.unc.edu`
- User: `aereinh`
- HOME: `/overflow/htzhu/mingcheng_new`
- CODEX_HOME: `/overflow/htzhu/mingcheng_new/.codex`
- Codex executable: `/overflow/htzhu/mingcheng_new/bin/codex`
- Codex version: `codex-cli 0.142.0`

## AI Skills Marketplace

Before and after this run, `yuukias-ai-skills` was configured as the formal release Marketplace:

- Source: `https://github.com/YuukiAS/AI_Skills_Collection.git`
- Ref: `release`
- Sparse paths: `.agents/plugins`, `plugins/codex/plugins`
- Revision before: `72ebd56705713c01d05fef34ccab1c5c04c15671`
- Revision after: `72ebd56705713c01d05fef34ccab1c5c04c15671`
- Remote formal `release`: `72ebd56705713c01d05fef34ccab1c5c04c15671`

Official command run:

```text
codex plugin marketplace upgrade yuukias-ai-skills --json
```

Result: `upgradedRoots=[]`, `errors=[]`; the Marketplace was already current.

## Installed AI Skills Plugins

Only plugins already installed on this consumer were refreshed with official `codex plugin add` commands. No optional plugin was newly installed.

| Plugin | Before | After | Action | Result |
|---|---:|---:|---|---|
| `workflow-core@yuukias-ai-skills` | `0.4 enabled` | `0.4 enabled` | official reinstall/refresh | current |
| `ai-skills-core@yuukias-ai-skills` | `0.5 enabled` | `0.5 enabled` | official reinstall/refresh | Maintainer installed/enabled |
| `research-writing@yuukias-ai-skills` | `0.2 enabled` | `0.2 enabled` | official reinstall/refresh | current |
| `bioinformatics@yuukias-ai-skills` | `0.1 enabled` | `0.1 enabled` | official reinstall/refresh | current |
| `medical-imaging@yuukias-ai-skills` | `0.1 enabled` | `0.1 enabled` | official reinstall/refresh | current |
| `presentations@yuukias-ai-skills` | `0.3 enabled` | `0.3 enabled` | official reinstall/refresh | current |
| `writing-style@yuukias-ai-skills` | `0.3 enabled` | `0.3 enabled` | official reinstall/refresh | current |

Left uninstalled by design:

- `scientific-visualization@yuukias-ai-skills` `0.1`
- `web-development@yuukias-ai-skills` `0.3`
- `statistical-modeling@yuukias-ai-skills` `0.1`

## Bridge Route C

Bridge was handled as part of this normal machine sync and did not stop at inspection.

- `ai-bridge`: `/overflow/htzhu/mingcheng_new/conda/bin/ai-bridge`
- `ai-bridge where`: `/overflow/htzhu/mingcheng_new/GPT_Codex_AI_Bridge_Kit`
- Origin: `https://github.com/YuukiAS/GPT_Codex_AI_Bridge_Kit.git`
- Branch: `main`
- Local HEAD before/after: `6bbaca5a3af6240fbc88fa54cf78fa9acc147f67`
- Remote formal `release`: `6bbaca5a3af6240fbc88fa54cf78fa9acc147f67`
- Release relation: `ALIGNED`
- Editable package location: `/overflow/htzhu/mingcheng_new/GPT_Codex_AI_Bridge_Kit`
- Package version: `0.9.2`
- Module version: `0.9.2`

No fast-forward or editable reinstall was required because the runtime checkout and installed package already matched the formal Bridge release. The pre-existing Bridge dirty path `.gitignore` was preserved; no stash/reset/restore/clean was used.

## Host Policy

`ai-bridge host validate` completed with:

```text
overall state: configured
```

Because Host Policy was already configured, `ai-bridge host install` was not run.

## Fresh Session

After plugin refresh, a fresh Codex process was launched through Bridge's production replay entry:

```text
ai-bridge plugin-replay --target /overflow/htzhu/mingcheng_new/AI_Skills_Collection --plugin ai-skills-core@yuukias-ai-skills ...
```

Fresh child evidence:

- Run id: `20260929T052859Z-38b39c52f386`
- Child session id: `01a0eba4-7cf8-7bd2-b12c-706aadd6b670`
- Last message: `fresh_longleaf_backup_plugin_replay_last_message.txt`
- Child semantic result: `STATE=ALREADY_CURRENT`, `ROUTE_C=VALIDATED`, `HOST_VALIDATE=PASS`, `BRIDGE_RELEASE_RELATION=ALIGNED`
- Replay report: `/overflow/htzhu/mingcheng_new/.ai-bridge/plugin-replay/20260929T052859Z-38b39c52f386/outputs/machine_update_orchestration_replay_report.md`

Replay wrapper diagnostic:

- Wrapper status: `failed`
- Wrapper exit code: `70`
- Contract error: `child Codex reported danger-full-access`

Interpretation: the fresh Codex child did execute the installed AI Skills Maintainer path and completed the machine-sync semantic validation. The wrapper contract diagnostic is recorded as a replay-harness issue and did not reveal Marketplace, Bridge, Host Policy, or plugin misalignment.

## Should-Not-Change Evidence

- No AI_Skills or Bridge release ref was advanced.
- No optional AI_Skills plugin was installed.
- No Codex config was hand-edited.
- No Bridge source logic was modified.
- No research repository was modified.
- User dirty Bridge path `.gitignore` was preserved.

## Result

```text
CONSUMER=Longleaf_Backup_Codex
STATUS=PASS
MARKETPLACE=release@72ebd56705713c01d05fef34ccab1c5c04c15671
AI_SKILLS_MAINTAINER=ai-skills-core@yuukias-ai-skills 0.5 enabled
BRIDGE_ROUTE_C=ALIGNED
BRIDGE_VERSION=0.9.2
HOST_POLICY=configured
FRESH_SESSION=semantic PASS; replay wrapper diagnostic recorded
OPTIONAL_PLUGINS_INSTALLED=NO
OVERALL_DONE=NO
```
