# workflow-core 0.5 Release Closure

Date: 2026-10-02

## Approved identities

- Final production candidate: `671eb532e0ec949dc7889427379a1113cf7a6ea9`
- Final handoff HEAD: `5f2cfdeb8682f2b152bb29cfc2fcdc2269036663`
- Integration base before merge: `origin/main` at `98721a202bc557c0b9c0800e66e50cab466bfba2`
- Integrated main HEAD: `8c55d467ab4b7fdf6158d4104b8889480344653c`
- Initial release closure evidence commit: `b43d9a1d7ccedd29ee90075b74f4e657e9c53731`
- workflow-core version: `0.5`
- Repository version: `5.4.1`

## Main drift preflight

`git fetch origin main` completed before integration.

The merge base between latest `origin/main` and the final candidate was:

```text
613cf2d7399ecacc360809f4e58f48ad7870df61
```

Drift from that base to latest `origin/main` did not touch the sensitive
workflow-core release surface:

- `skills/core/codex-system/codex-workflow-protocol`
- `plugins/codex/plugins/workflow-core`
- `.agents/plugins/marketplace.json`
- marketplace generator/config paths
- `VERSION`
- `CHANGELOG.md`
- `README.md`
- `registry.json`
- `docs/SKILL_CATALOG.md`
- `docs/plugin-changelogs/workflow-core.md`
- `docs/plugin-todos/workflow-core.md`

Local obsolete numbered reviewed work was discarded before integration per user
authorization. Local `main` was reset to `origin/main`, and the local
`reviewed/050_writing_style_host_codex_runtime` branch was deleted. No matching
local `044` through `050` numbered branches remained afterward.

## Integration result

The final handoff HEAD was merged into canonical `main` with an ordinary merge
commit:

```text
8c55d467ab4b7fdf6158d4104b8889480344653c
```

The integrated production release payload is byte-equivalent to the approved
final production candidate for workflow-core source, generated Marketplace
payload, version, and release metadata:

```text
git diff --quiet 671eb532e0ec949dc7889427379a1113cf7a6ea9..HEAD -- \
  skills/core/codex-system/codex-workflow-protocol \
  plugins/codex/plugins/workflow-core \
  .agents/plugins/marketplace.json \
  scripts/codex_marketplace_config.json \
  VERSION CHANGELOG.md README.md registry.json \
  docs/SKILL_CATALOG.md docs/plugin-changelogs/workflow-core.md

BYTE_EQUIVALENT_PASS
```

## Integration checks

PASS:

- `python scripts/build_codex_marketplace.py --check --validate`
- `python -m unittest tests.test_workflow_core_normal_entry_reliability tests.test_workflow_core_reviewed_handoff_routing tests.test_codex_marketplace tests.test_standalone_skill_baselines tests.test_candidate_plugin_replay`
  - Result: `Ran 85 tests ... OK`
- `python scripts/skills.py validate`
  - Result: `validated 154 active skills, 18 profiles, templates, and trigger eval scaffolds`
- `python scripts/skills.py audit`
  - Result: warnings only for broad repo profile budget; no blocking errors
- `git diff --check HEAD^..HEAD`

During integration validation, several source files had workspace-local `0600`
permissions while Git tracked them as normal `100644` files. They were normalized
to `0644` in the working copy only so `build_codex_marketplace.py --check` could
compare generated file modes deterministically. This did not change repository
content, production workflow-core source, generated payload, or version metadata.

## Production identity and install/update smoke

PASS:

- `plugins/codex/plugins/workflow-core/.codex-plugin/plugin.json`
  - `name`: `workflow-core`
  - `version`: `0.5`
- `.agents/plugins/marketplace.json`
  - workflow-core source path: `./plugins/codex/plugins/workflow-core`
- `VERSION`
  - `5.4.1`
- `python scripts/skills.py verify-server-installation --skill core/codex-system/codex-workflow-protocol --mode copy --json`
  - `ok`: `true`
  - `installed_skill_count`: `1`
  - `collection_commit`: `8c55d467ab4b7fdf6158d4104b8889480344653c`
  - marketplace payload check: `errors=0`
- Temporary managed update dry-run:
  - install target: `CODEX_HOME=/tmp/ai-skills-workflow-core-release-smoke-8c55d467`
  - selected skill: `core/codex-system/codex-workflow-protocol`
  - `python scripts/skills.py update --manifest /tmp/ai-skills-workflow-core-release-smoke-8c55d467/skills/.ai-skills-collection-manifest.json --dry-run --json`
  - `manifest_count`: `1`
  - `selected_skill_count`: `1`
  - `warnings`: `[]`

An earlier smoke attempt passed `--project` to `install --target codex-home`,
which does not control the codex-home target. It attempted the current real
`CODEX_HOME` and failed before completing any install because that location is
read-only. The final smoke used process-local `CODEX_HOME=/tmp/...` and passed.

## Release ref preflight

Current `origin/release` before release ref closure:

```text
a7028195f3e97d32d51c32ef8c87f658f92048e5
```

`origin/release` is an ancestor of integrated `main` HEAD
`8c55d467ab4b7fdf6158d4104b8889480344653c`, so the required release ref closure
is eligible for fast-forward-only update after bounded `main` publication.

## Publication and release ref closure

`main` publication used the canonical bounded current-branch publisher:

```text
ai-bridge host publish-current-branch \
  --expected-repo YuukiAS/AI_Skills_Collection \
  --expected-branch main
```

Result:

```json
{
  "branch": "main",
  "destination": "origin/refs/heads/main",
  "pushed_oid": "b43d9a1d7ccedd29ee90075b74f4e657e9c53731",
  "repo": "YuukiAS/AI_Skills_Collection",
  "status": "published"
}
```

The release ref closure also used the bounded current-branch publisher, not a
raw Git fallback. A direct raw release-ref push was rejected by host policy before
execution, and no raw fallback was used. The local `release` branch was created
at the verified release commit, bound to `origin/release`, and then published
through:

```text
ai-bridge host publish-current-branch \
  --expected-repo YuukiAS/AI_Skills_Collection \
  --expected-branch release
```

Result:

```json
{
  "branch": "release",
  "destination": "origin/refs/heads/release",
  "pushed_oid": "b43d9a1d7ccedd29ee90075b74f4e657e9c53731",
  "repo": "YuukiAS/AI_Skills_Collection",
  "status": "published"
}
```

This document update is the final release-closure writeback. It does not alter
production workflow-core source, generated payload, version metadata, changelog
semantics, or release behavior. The final release target after this writeback is
the commit containing this file update; both `origin/main` and `origin/release`
must be advanced to that same commit through the same bounded publisher and
verified after publication.
