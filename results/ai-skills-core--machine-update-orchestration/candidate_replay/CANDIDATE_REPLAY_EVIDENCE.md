# Candidate Replay Evidence - G1/G3

Task key: `ai-skills-core--machine-update-orchestration`  
Replay date: 2026-09-23 UTC  
Replay path: canonical `scripts/candidate_plugin_replay.py replay`

## Candidate Identity

- Candidate commit: `24f574ff20028fedaa3c5382594717cb28234184`
- Runtime: `codex-cli 0.153.4`
- Candidate plugin id: `ai-skills-core@ai-skills-candidate`
- Candidate plugin version: `0.5`
- Candidate installed path during replay: `/home/yuukias/.codex/plugins/cache/ai-skills-candidate/ai-skills-core/0.5`
- Production plugin after cleanup: `ai-skills-core@yuukias-ai-skills` remained installed and enabled at version `0.4`

## Run Evidence

- Run directory: `.local-runtime/candidate-plugin-replay/runs/20260923T163350Z-82391/`
- `run.json` SHA256: `4233f8f8ef919af9b1ac2ad9006c39d1e16d4ef32d8cbf1e889589495805941a`
- `child.stdout.jsonl` SHA256: `f98c0e43707a26b7da150e1ad345976f46164d984483db90714e5509106ba79c`
- `workspace/outputs/route-report.md` SHA256: `279fd3e73ae7e11f44191082ba3943c5e1a15e5ea760baf623a57d3e68bb2d39`
- Actual candidate consumption: `proven=true`, event type `item.started`, JSONL line `4`
- Parsed consumption command read candidate `skills/orchestrator/SKILL.md` under the `ai-skills-candidate` plugin cache.
- Child stderr: empty.

## Normal-Entry Route Results

The fresh child handled the natural task `Use AI Skills Maintainer` with the short requests:

| Request | Result |
|---|---|
| `update AI Skills` | Route A by default; Route B only if formal release metadata declares cross-layer impact. Owner split: `ai-skills-repository-maintainer` for AI_Skills release production and `project-skill-installer` for managed install/profile refresh. |
| `sync this machine` | Composition of Route A/B/C for participating installed components; not a fourth route. Scope expansion only from each formal release's matching root `### Update impact`. |
| `update Bridge Kit` | Route C with internal owner `bridge-kit-maintainer`; stable target is Bridge `release` at `0.8.5` / `d27259d6706dee951dc0c0ede8c9b03c65f55ca3`; newer Bridge `main` docs/plans are not stable update target. |

The child did not ask for versions, commits, checkout paths, `CODEX_HOME`, repository inventories, adaptation templates or dependency/component lists. The requested replay was a no-mutation dry run and returned `DRY_RUN / NOT_EXECUTED`.

This evidence closes pre-release G1/G3 candidate normal-entry replay only. It does not claim G2 production Marketplace migration or released production smoke.
