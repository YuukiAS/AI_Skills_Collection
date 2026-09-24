# Candidate Replay Evidence - G1/G3

Task key: `ai-skills-core--machine-update-orchestration`  
Replay date: 2026-09-24 UTC  
Replay path: canonical `scripts/candidate_plugin_replay.py replay`

## Candidate Identity

- Product-surface candidate commit replayed: `4b8414733f3efc2d8707c5fbf448cbe8ec7a7d00`
- Runtime: `codex-cli 0.153.4`
- Candidate plugin id: `ai-skills-core@ai-skills-candidate`
- Candidate plugin version: `0.5`
- Candidate installed path during replay: `/home/yuukias/.codex/plugins/cache/ai-skills-candidate/ai-skills-core/0.5`
- Production plugin after cleanup: `ai-skills-core@yuukias-ai-skills` remained installed and enabled at version `0.4`

## Run Evidence

- Run directory: `.local-runtime/candidate-plugin-replay/runs/20260924T130034Z-3045521/`
- `run.json` SHA256: `5acec163ef8657acc0c5fe50dec45bec2bf02f1a1eb72e162b71157a750e4ae0`
- `child.stdout.jsonl` SHA256: `a6fa544eb9826a844c21ddb210c248a107bab1f412e583732a10075eeb8733eb`
- `workspace/outputs/route-report.md` SHA256: `0d5ceabf860cebdb210a8db278346d72b702c612336e69dfc0133427bf617c9c`
- Actual candidate consumption: `proven=true`, event type `item.started`, JSONL line `4`
- Parsed consumption command read candidate `skills/orchestrator/SKILL.md` under the `ai-skills-candidate` plugin cache.
- Child stderr: empty.

## Bridge Dynamic Discovery

The replay input `public_machine_state.md` was regenerated as an input boundary only. It named the Bridge repo/read scope/no-mutation boundary and did not provide the latest formal release, current release version, relation classification, or expected interpretation.

The child candidate then performed read-only discovery from the allowed Bridge source:

- tried the relative source path, then consumed the absolute task-owned snapshot under `private/exports/ai-skills-core--machine-update-orchestration/bridge_git_snapshot`;
- read the candidate `bridge-kit-maintainer` skill and `bridge-release-channel` / canonical delegation references from the installed candidate plugin;
- read Bridge `AGENTS.md`, `pyproject.toml`, `ai_bridge_kit/__init__.py`, `CHANGELOG.md`, `results/reviewed-handoff--first-bootstrap-normal-entry/EVIDENCE.md`, and raw refs from the frozen Bridge snapshot;
- used Git commands against the snapshot, including `git show origin/release:pyproject.toml`, `git show origin/release:ai_bridge_kit/__init__.py`, `git show a41c2e32c630aaf2a200ca336f04c4ea31650786:...`, and `git merge-base origin/release a41c2e32c630aaf2a200ca336f04c4ea31650786`;
- concluded from that evidence that the real case is `LAGGING`: Bridge `release` identifies `0.8.5`, while the newest provable formal release evidence binds `0.9.1` at `a41c2e32c630aaf2a200ca336f04c4ea31650786`.

The child did not call the older `release` ref the latest formal release, did not treat newer `main` as a stable update target, and did not advance the Bridge `release` ref.

## Normal-Entry Route Results

The fresh child handled the natural task `Use AI Skills Maintainer` with the short requests:

| Request | Result |
|---|---|
| `update AI Skills` | Route A by default; Route B only if formal release metadata declares cross-layer impact. Owner split: `ai-skills-repository-maintainer` for AI_Skills release production and `project-skill-installer` for managed install/profile refresh. |
| `sync this machine` | Composition of Route A/B/C for participating installed components; not a fourth route. Scope expansion only from each formal release's matching root `### Update impact`. |
| `update Bridge Kit` | Route C with internal owner `bridge-kit-maintainer`; dynamic discovery selected `LAGGING`, so formal distribution closure is pending/incomplete. |

The child reported `DRY_RUN / NO_MUTATION` and did not ask the user for versions, commits, checkout paths, `CODEX_HOME`, repository inventories, adaptation templates or dependency/component lists.

This evidence closes pre-release G1/G3 candidate normal-entry replay only. It does not claim G2 production Marketplace migration or released production smoke.
