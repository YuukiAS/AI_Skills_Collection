# ADAPTING Consumer Runbook

Task key: `ai-skills-core--machine-update-orchestration`  
Prepared date: 2026-09-25

## Purpose

This runbook is for the Maintenance Board `ADAPTING` phase after central
implementation, formal release, real G2, and current `Workstation` consumer PASS.

It does not authorize cross-machine control. AI Skills Maintainer is a
per-current-consumer adaptation executor, not a five-machine orchestrator. Run
this only from the target consumer itself, or from a session that has explicit
bounded authority for that exact consumer.

## Current Global State To Preserve

- Tracking Issue: `#86`
- Project: `AI Skills Maintenance`
- Project Status: `ADAPTING`
- Area: `ai-skills-core`
- Resolution commit: `c7776e202ae0324fc00b719b6ef8224b8e0498fe`
- AI_Skills remote `main`: `c7776e202ae0324fc00b719b6ef8224b8e0498fe`
- AI_Skills remote `release`: `c7776e202ae0324fc00b719b6ef8224b8e0498fe`
- Released repository version: `5.2.0`
- Released `ai-skills-core`: `0.5`
- Released `workflow-core`: `0.4`
- Bridge `release`: not advanced by this task
- Bridge runtime/source/Host: not modified by this task

## Required Consumers

| Consumer | Current Status | Evidence |
|---|---|---|
| `Workstation` | `PASS` | `ADAPTING_CONSUMER_EVIDENCE.md` |
| `Longleaf_Codex` | `PENDING_CONSUMER_AUTHORITY` | this runbook |
| `Longleaf_Backup_Codex` | `PENDING_CONSUMER_AUTHORITY` | this runbook |
| `CUHK_Workstation_WSL_Codex` | `PENDING_CONSUMER_AUTHORITY` | this runbook |
| `Legion` | `PENDING_CONSUMER_AUTHORITY` | this runbook |

Do not infer PASS for one consumer from another. Each consumer needs its own
identity, installed/loaded state, normal-entry consumption, fresh-session or
reload boundary, should-not-change evidence, and durable locator.

## Per-Consumer Authority Boundary

Before running on a remaining consumer, verify the current user has authorized
that exact consumer by name. Authorization should identify:

- consumer name from the required list;
- local/remote execution surface to use;
- permission to inspect Codex config/plugin state;
- permission to mutate that consumer's Codex Marketplace/plugin installation if
  legacy `main` bootstrap or reinstall is needed;
- no paid API;
- no automation;
- no Bridge runtime/source mutation;
- no Bridge `release` advancement;
- no unrelated project mutation.

If authority is absent, record `PENDING_CONSUMER_AUTHORITY` and stop for that
consumer.

## Per-Consumer Discovery

On the target consumer, discover current identity without asking the user for
paths/versions/commits:

```bash
hostname
uname -a
id -un
printf 'HOME=%s\n' "$HOME"
printf 'CODEX_HOME=%s\n' "${CODEX_HOME:-$HOME/.codex}"
codex --version
codex plugin marketplace list --json
codex plugin list --marketplace yuukias-ai-skills --available --json
```

If `yuukias-ai-skills` is missing, check whether this consumer is supposed to be
in scope. Missing marketplace may be `N/A` only with a frozen durable reason from
the user/owner or Board policy; otherwise it is an adaptation task for that
consumer.

If `yuukias-ai-skills` exists, read only the relevant Marketplace/plugin config
facts from the consumer's Codex config layer:

```bash
rg -n -C 2 '\[marketplaces\.yuukias-ai-skills\]|last_revision|source_type|source =|ref =|sparse_paths|\[plugins\."ai-skills-core@yuukias-ai-skills"\]' "${CODEX_HOME:-$HOME/.codex}/config.toml"
```

Do not print or inspect secrets. Do not read `auth.json`.

## Expected Stable State

PASS-compatible stable state:

```text
[marketplaces.yuukias-ai-skills]
source_type = "git"
source = "https://github.com/YuukiAS/AI_Skills_Collection.git"
ref = "release"
sparse_paths = [".agents/plugins", "plugins/codex/plugins"]
last_revision = "c7776e202ae0324fc00b719b6ef8224b8e0498fe"

[plugins."ai-skills-core@yuukias-ai-skills"]
enabled = true
```

`codex plugin list --marketplace yuukias-ai-skills --available --json` should
show:

- `ai-skills-core@yuukias-ai-skills`: installed true, enabled true, version `0.5`
- `workflow-core@yuukias-ai-skills`: version `0.4`

Domain plugin versions should not be mechanically bumped.

## If Legacy `main` Is Found

A real legacy consumer may still have:

```text
ref = "main"
ai-skills-core version = "0.4"
```

Proceed only when the source URL and sparse paths match the expected AI_Skills
Marketplace and the config layer is user-owned/mutable.

Use official Codex commands only:

```bash
codex plugin marketplace remove yuukias-ai-skills --json
codex plugin marketplace add https://github.com/YuukiAS/AI_Skills_Collection.git --ref release --sparse .agents/plugins --sparse plugins/codex/plugins --json
codex plugin marketplace upgrade yuukias-ai-skills --json
codex plugin add ai-skills-core@yuukias-ai-skills --json
```

Before removing the old source, record exact old metadata for restoration:

- Marketplace name;
- Git source URL;
- ref;
- sparse paths;
- owning config layer;
- installed/enabled AI_Skills plugin state.

If replacement fails after removal, restore the exact old source at the old ref
using official Codex Marketplace commands and record `PARTIAL_UPDATE` or the
existing failure state truthfully.

Do not directly edit Codex config.

## Fresh Normal-Entry Verification

After the consumer is at release + `ai-skills-core 0.5`, verify the installed
production normal entry with `ai-bridge plugin-replay` when available. Use the
production plugin, not a reviewed/candidate worktree plugin.

Recommended task text for the replay:

```text
Use installed production plugin `ai-skills-core@yuukias-ai-skills`.
Normal request: `sync this machine`.
Read-only smoke only. Do not mutate Marketplace sources, plugin installation,
Git refs, Bridge refs, Bridge runtime/source, Host state, project consumers, or
unrelated repositories. Do not call paid APIs.
Report whether the released AI Skills Maintainer normal entry is loaded, which
internal skill owns `sync this machine`, the installed `ai-skills-core` version
and plugin path if visible, and the expected user-facing state for an already
updated current session.
```

A PASS result should prove:

- wrapper status completed / exit code 0;
- plugin check installed true;
- production plugin `ai-skills-core@yuukias-ai-skills` consumed;
- installed version `0.5`;
- owner path `ai-skills-core:machine-update-orchestrator`;
- already-current state `ALREADY_CURRENT`, or update state
  `UPDATED_RELOAD_REQUIRED` when a real install/refresh happened;
- write isolation / no unauthorized mutation evidence.

If current Codex cannot run `ai-bridge plugin-replay` on a consumer, record the
exact missing interface and keep that consumer pending rather than substituting a
source-tree `SKILL.md` read.

## Per-Consumer PASS Evidence Template

For each remaining consumer, write durable evidence with this minimum shape:

```text
# <Consumer> ADAPTING Evidence

Consumer: <name>
Status: PASS | N/A | PENDING_CONSUMER_AUTHORITY | FAILED_CLOSED
Date:
Authority:

Identity:
- hostname:
- platform:
- user:
- HOME:
- CODEX_HOME:
- codex version:

Marketplace:
- name: yuukias-ai-skills
- source:
- ref:
- sparse paths:
- last_revision:
- owning config layer:

Installed plugins:
- ai-skills-core@yuukias-ai-skills:
- workflow-core@yuukias-ai-skills:
- relevant companions:

Action performed:
- none, already current | migrated main->release | reinstalled | failed closed

Normal-entry verification:
- method:
- run id/path:
- status/exit:
- owner route:
- result state:

Should-not-change:
- Bridge release advanced: no
- Bridge runtime/source modified: no
- Host state modified: no
- unrelated project mutation: no
- dirty/user work preserved:

Durable artifacts:
- run json:
- last message:
- smoke report:
- config/plugin state capture:
```

Then add an Issue `#86` comment summarizing the consumer outcome and evidence
path. Keep Project Status `ADAPTING` unless all required consumers are PASS/N/A.

## Final DONE Rule

Do not close Issue `#86` until all required consumers are PASS or policy-backed
N/A with durable evidence. Final DONE requires:

```text
all required consumers PASS/N/A
+ durable evidence complete
+ Resolution commit = c7776e202ae0324fc00b719b6ef8224b8e0498fe
+ tracking Issue completed close
+ issue-closed workflow -> DONE
```

Current state after this runbook remains:

```text
NEXT_HANDOFF=CONSUMER_ADAPTATION_REQUIRED
PROJECT_STATUS=ADAPTING
ISSUE_86_OPEN=YES
OVERALL_DONE=NO
```
