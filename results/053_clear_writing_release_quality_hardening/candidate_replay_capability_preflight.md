# 053 Candidate Replay Capability Preflight

Status: NEEDS_GPT_PLANNER

Date: 2026-09-12

Branch: `reviewed/053_clear_writing_release_quality_hardening`

Pinned runtime: `codex-cli 0.153.4`

Purpose: bounded Gate 0 preflight for the generic candidate-replay workflow regression. This is not a Clear Writing product replay and does not consume the private Deep Research replay budget, fresh holdout budget, or Terra review budget.

## Required boundary

The preflight tested whether pinned Codex CLI 0.153.4 can run a committed `writing-style@ai-skills-candidate` candidate with all of the following properties:

- keep the existing `CODEX_HOME` and account identity unchanged;
- do not copy, symlink, print, or migrate `auth.json`;
- do not create a second credential-bearing home;
- do not run persistent `codex plugin add` or `codex plugin remove`;
- do not mutate the live production plugin/cache/config;
- use only process-local marketplace/config overrides and repo-local ignored state under `.local-runtime/candidate-plugin-replay/**`;
- prove actual candidate `SKILL.md` consumption from child JSONL before accepting the replay.

## Observed current binding

Sanitized `codex doctor --json` and environment checks showed:

- `CODEX_HOME` remains `/overflow/htzhu/mingcheng_new/.codex-homes/Longleaf_Connection_Bridge`;
- auth is configured from the current home, storage mode `File`, auth mode `chatgpt`;
- `auth.json` exists in the current home and is an existing symlink; this preflight did not create, copy, print, or follow it;
- plugin cache/config for the current home is not writable from this sandboxed execution context;
- `CODEX_SQLITE_HOME` can redirect the reported `sqlite home` to repo-local `.local-runtime/candidate-plugin-replay/**` while leaving `CODEX_HOME` unchanged.

## Direct process-local execution attempts

Each attempt staged the candidate from committed `HEAD` into a repo-local ignored marketplace directory and invoked pinned `codex exec --ignore-user-config --json` with:

```text
marketplaces.ai-skills-candidate.source_type="local"
marketplaces.ai-skills-candidate.source="<repo-local staged marketplace>"
plugins.writing-style@ai-skills-candidate.enabled=true
```

No attempt ran `codex plugin add` or `codex plugin remove`.

Observed attempts:

| mode | result | candidate SKILL consumed |
| --- | --- | --- |
| no approval flag | failed before JSONL/model execution: `failed to initialize in-process app-server client: Read-only file system (os error 30)` | no |
| `CODEX_SQLITE_HOME=<repo-local state>` | same failure | no |
| `--disable tui_app_server` | same failure | no |
| `-c features.tui_app_server=false` | same failure | no |
| `-c sqlite_home="<repo-local state>"` | same failure | no |
| `-c app_server_mode="stdio"` | same failure | no |
| `-c app_server_mode="in_process"` | same failure | no |
| `-c app_server_mode="local_daemon"` | same failure | no |
| `-c app_server_mode="off"` | same failure | no |
| `-c history.persistence="none"` | same failure | no |
| `-c log_dir="<repo-local state>"` | same failure | no |

Additional CLI compatibility observations:

- `codex exec -a never` failed with `unexpected argument '-a'`.
- `codex exec --ask-for-approval never` failed with `unexpected argument '--ask-for-approval'`.
- The pinned `exec --help` exposes `--approve-for-me`, `--dangerously-bypass-approvals-and-sandbox`, `--ignore-user-config`, and `--ephemeral`, but no documented no-install plugin loading flag beyond process-local `-c` config overrides.

## Live-state residue check

Post-attempt `codex plugin list --json` via the pinned runtime showed:

```text
candidate_ids = []
same_name_snapshot = writing-style@yuukias-ai-skills enabled=true marketplaceName=yuukias-ai-skills
```

The attempted direct path did not install `writing-style@ai-skills-candidate` and did not mutate the same-name production identity. Staged candidate marketplace directories were removed after each probe; diagnostic stdout/stderr files remain only under ignored `.local-runtime/candidate-plugin-replay/runs/**`.

Credential copy/symlink created: `NO`.

Auto-review denial in this preflight: `NO`.

## Executor conclusion

Pinned Codex CLI 0.153.4 did not reach plugin loading or model execution under the required no-install/process-local boundary. The observed limitation is earlier than candidate selection: `codex exec` initializes an in-process app-server client that still needs writable app-server state tied to the current `CODEX_HOME`, and no tested documented process-local override redirected that app-server state while preserving the existing credential home.

Therefore Executor cannot honestly implement the direct/process-local canonical replay path yet, and must not fall back to:

- repo-local credential-bearing `CODEX_HOME`;
- copied or symlinked credentials;
- persistent live `codex plugin add/remove`;
- global Codex/cache/config mutation;
- Bridge Kit or Host Policy changes;
- `require_escalated` as the product solution.

## Required Planner comparison

Planner should decide the smallest legal next step:

A. identify an official Codex CLI 0.153.4 process-local loading/state override that allows candidate plugin execution without persistent install, live-state mutation, or credential migration; or

B. if no such official path exists, decide whether 053 needs a cross-central-plugin narrow controlled replay entrypoint, with explicit safety boundaries, before K1-K4 can resume.
