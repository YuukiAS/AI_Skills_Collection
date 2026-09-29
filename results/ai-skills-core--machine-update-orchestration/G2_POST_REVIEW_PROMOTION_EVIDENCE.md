# G2 Post-Review Promotion Evidence

Task key: `ai-skills-core--machine-update-orchestration`  
Evidence date: 2026-09-25 local / 2026-09-24 UTC

## Scope

Executed post-review formal promotion and real G2 after Independent
Implementation Review PASS.

No Bridge `release` ref was advanced. No Bridge runtime/source file was
modified. No paid API, Terra, OpenAI Responses API, or automation was used.

## Reviewed Inputs

- Reviewed product candidate: `4b8414733f3efc2d8707c5fbf448cbe8ec7a7d00`
- Approved control-doc closure tip:
  `e72ec4e520f54564cd4dd657316ca539335edfb6`
- Integrated formal AI_Skills commit:
  `c7776e202ae0324fc00b719b6ef8224b8e0498fe`

Before integration, latest `origin/main` drift was inspected. Observed drift was
board/docs/TODO/icon/test-only and did not introduce new ai-skills-core
production, generated Marketplace, repository/plugin version, or release-channel
semantic overlap requiring G1/G3/G4/G5 rerun.

During the user-requested wait for possible `5.1.2` drift, a later readback still
showed AI_Skills `main` and `release` at the same formal `5.2.0` commit:

```text
c7776e202ae0324fc00b719b6ef8224b8e0498fe refs/heads/main
c7776e202ae0324fc00b719b6ef8224b8e0498fe refs/heads/release
```

## Deterministic Release Validation

Before formal commit/promotion:

- `python scripts/skills.py registry --write` -> PASS
- `python scripts/skills.py catalog --write` -> PASS
- `python scripts/skills.py validate` -> PASS
- `python scripts/skills.py audit --all` -> PASS
- `python scripts/build_codex_marketplace.py --write --validate --check --path-report` -> PASS
- `python -m unittest tests.test_codex_marketplace tests.test_standalone_skill_baselines tests.test_candidate_plugin_replay tests.test_central_plugin_icon_assets` -> `Ran 75 tests`, OK
- `python -m unittest discover -s tests -p 'test_*.py'` -> `Ran 264 tests`, OK

Version anchors verified:

- repository `VERSION`: `5.2.0`
- `ai-skills-core`: `0.5`
- `workflow-core`: `0.4`

## Formal Promotion

- `main` was published through `ai-bridge host publish-current-branch`.
- Remote `main` verified as:
  `c7776e202ae0324fc00b719b6ef8224b8e0498fe`.
- Existing remote `release` before promotion was:
  `7b76e94ad29cf3bd8547026b942553068754d51f`.
- Verified old `release` was ancestor of formal commit.
- Fast-forwarded AI_Skills `release` non-force to:
  `c7776e202ae0324fc00b719b6ef8224b8e0498fe`.
- Remote `main` and `release` were both verified at the same formal commit.

## Maintenance Board DOING Binding

Created the required tracking Issue after Clear Writing pass on factual copy:

- Issue: `https://github.com/YuukiAS/AI_Skills_Collection/issues/86`
- Label: `maintenance-track`
- Canonical source backlink added:
  `docs/plugin-todos/ai-skills-core.md -> tracking: #86`
- Project: `AI Skills Maintenance`
- Project Status set to `DOING`
- Area set to `ai-skills-core`
- Resolution commit initially blank/unset

## G2 Legacy Marketplace Migration

Pre-migration legacy source metadata captured from official Codex commands and
user config readback:

- Marketplace name: `yuukias-ai-skills`
- Git source URL: `https://github.com/YuukiAS/AI_Skills_Collection.git`
- Old ref: `main`
- Sparse paths: `.agents/plugins`, `plugins/codex/plugins`
- Owning config layer: `/home/yuukias/.codex/config.toml`
- Installed plugin state included `ai-skills-core@yuukias-ai-skills`
  version `0.4`, installed/enabled true.

Migration used official Codex commands only:

```bash
codex plugin marketplace remove yuukias-ai-skills --json
codex plugin marketplace add https://github.com/YuukiAS/AI_Skills_Collection.git --ref release --sparse .agents/plugins --sparse plugins/codex/plugins --json
codex plugin marketplace upgrade yuukias-ai-skills --json
codex plugin add ai-skills-core@yuukias-ai-skills --json
```

Post-migration config readback:

```text
[marketplaces.yuukias-ai-skills]
last_revision = "c7776e202ae0324fc00b719b6ef8224b8e0498fe"
source_type = "git"
source = "https://github.com/YuukiAS/AI_Skills_Collection.git"
ref = "release"
sparse_paths = [".agents/plugins", "plugins/codex/plugins"]

[plugins."ai-skills-core@yuukias-ai-skills"]
enabled = true
```

Reinstall/update result:

```text
pluginId: ai-skills-core@yuukias-ai-skills
version: 0.5
installedPath: /home/yuukias/.codex/plugins/cache/yuukias-ai-skills/ai-skills-core/0.5
```

`codex plugin list --marketplace yuukias-ai-skills --available --json` confirmed:

- `ai-skills-core@yuukias-ai-skills`: installed true, enabled true, version `0.5`
- `workflow-core@yuukias-ai-skills`: version `0.4`

Because the replacement succeeded, the old `main` source restoration path was
not invoked.

## Fresh Released Normal-Entry Smoke

Release-critical replay used production plugin replay, not candidate replay:

```bash
ai-bridge plugin-replay \
  --target /home/yuukias/AI_Skills_Collection-ai-skills-core-machine-update-orchestration \
  --plugin ai-skills-core@yuukias-ai-skills \
  --task results/ai-skills-core--machine-update-orchestration/g2_released_smoke/released_normal_entry_task_v2.md \
  --input results/ai-skills-core--machine-update-orchestration/g2_released_smoke/released_machine_state_input.md
```

Replay result:

- run id: `20260924T172142Z-368783282d6c`
- run json: `g2_released_smoke/released_normal_entry_run.json`
- status: `completed`
- exit code: `0`
- contract errors: none
- write isolation: passed
- plugin check: installed true
- plugin: `ai-skills-core@yuukias-ai-skills`
- local report: `g2_released_smoke/released_normal_entry_smoke_report.md`

Artifact hashes:

```text
09f20c551a8b91871eaaee3fd70d9c0e1c7222c2122ac8c123c642ab82d93bd0  released_normal_entry_run.json
abcef74137efdffde5614666ac8651bdd0e59c62751759baf2001185ce40d8e1  released_normal_entry_last_message.txt
6d36ef18397c82c3b27e9038bd994336dbe5aa37fba3ba4b88141a453ab956ec  released_normal_entry_smoke_report.md
```

Fresh released normal-entry conclusion:

- `ai-skills-core@yuukias-ai-skills` is installed/enabled at `0.5`.
- Released `AI Skills Maintainer` normal entry loaded.
- `sync this machine` is owned by
  `ai-skills-core:machine-update-orchestrator`.
- For this already updated read-only smoke, expected user-facing state is
  `ALREADY_CURRENT`.
- If a real update had installed/refreshed plugin code, expected state would be
  `UPDATED_RELOAD_REQUIRED`; current session hot reload was not claimed.

A first replay attempt also proved plugin loading, but wrapper-level status was
`failed` because its contract scanner matched a generic `codex --help` sandbox
option string emitted by the child. The release-critical replay is the second
run above with wrapper `status=completed` and `exit_code=0`.

## G2 Result

`G2 = PASS` for the post-review promotion sequence:

- real legacy Marketplace `main -> release` migration was exercised;
- exact old source metadata was captured;
- official Codex Marketplace/plugin commands were used;
- `ai-skills-core 0.5` was installed from the released source;
- released fresh normal-entry smoke completed through production plugin replay;
- Bridge release/runtime/source were untouched.

Overall maintenance is not marked DONE. Per Maintenance Board policy, after
central integration + formal release + G2, lifecycle moves to `ADAPTING`.
