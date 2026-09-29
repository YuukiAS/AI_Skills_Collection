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

Final fresh normal-entry evidence is a direct Codex fresh process, not the previous `ai-bridge plugin-replay` wrapper run.

Command shape:

```text
codex exec --ephemeral --skip-git-repo-check --disable memories -s workspace-write -C /tmp/longleaf_backup_direct_fresh_20260929 -o /tmp/longleaf_backup_direct_fresh_20260929/last-message.txt -
```

Direct fresh evidence:

- Codex session id: `01a0ebb5-74b6-76e1-a4d3-afde618dc3eb`
- Last message: `fresh_longleaf_backup_direct_codex_last_message.txt`
- Request: `使用 AI Skills Maintainer，同步这台机器。`
- Scope: read-only verification only; no Marketplace/plugin/Bridge/Host mutation
- Result: `PASS`

Verified by the direct fresh process:

1. `ai-skills-core@yuukias-ai-skills` is installed/enabled at `0.5` and loaded from the production plugin cache.
2. `sync this machine` routes to `machine-update-orchestrator`.
3. Marketplace `yuukias-ai-skills` is on `release`.
4. Bridge package/runtime is `0.9.2`.
5. Bridge release relation is `ALIGNED`: `HEAD == origin/release == 6bbaca5a3af6240fbc88fa54cf78fa9acc147f67`; later `origin/main` evidence/docs commits were not treated as formal release.
6. `ai-bridge host validate` reports `overall state: configured`.

Previous replay-wrapper evidence is retained as diagnostic history only: `ai-bridge plugin-replay` child semantics passed, but the wrapper returned `exit_code=70` with `child Codex reported danger-full-access`, so it is not used as the sole final fresh-session PASS basis.

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
FRESH_SESSION=direct codex exec --ephemeral PASS
OPTIONAL_PLUGINS_INSTALLED=NO
OVERALL_DONE=NO
```
