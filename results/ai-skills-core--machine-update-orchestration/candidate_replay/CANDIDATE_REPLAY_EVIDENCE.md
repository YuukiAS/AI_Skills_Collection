# Candidate Replay Evidence - G1/G3

Task key: `ai-skills-core--machine-update-orchestration`  
Replay date: 2026-09-24 UTC  
Replay path: canonical `scripts/candidate_plugin_replay.py replay`

## Candidate Identity

- Candidate commit: `12ca08dc127f8eee4c13a3a2c9cc598d00ce04ee`
- Runtime: `codex-cli 0.153.4`
- Candidate plugin id: `ai-skills-core@ai-skills-candidate`
- Candidate plugin version: `0.5`
- Candidate installed path during replay: `/home/yuukias/.codex/plugins/cache/ai-skills-candidate/ai-skills-core/0.5`
- Production plugin after cleanup: `ai-skills-core@yuukias-ai-skills` remained installed and enabled at version `0.4`

## Bridge Snapshot Revalidation

Bounded repair-start revalidation checked the real Bridge source:

- Repository: `YuukiAS/GPT_Codex_AI_Bridge_Kit`
- Remote `release`: `d27259d6706dee951dc0c0ede8c9b03c65f55ca3`
- Latest provable formal release from the frozen snapshot: `a41c2e32c630aaf2a200ca336f04c4ea31650786`, version `0.9.1`
- Relation: `LAGGING`
- Material drift from `BRIDGE_REVALIDATION_SNAPSHOT.md`: none. Later Bridge `main` drift observed during repair was README-only; Bridge `AGENTS.md` owner locator, version sources and closure evidence semantics remained equivalent.

The replay input `public_machine_state.md` was regenerated from the frozen snapshot. It treats concrete Bridge versions/SHAs as snapshot evidence only, not AI_Skills product dependencies.

## Run Evidence

- Run directory: `.local-runtime/candidate-plugin-replay/runs/20260924T115704Z-2748311/`
- `run.json` SHA256: `850b1d6d5e964e7540b3153ee98d40c3e53b2f7b04f7b176cb4d46d9f1415d98`
- `child.stdout.jsonl` SHA256: `3af8b6206a04e39bb935f7f27532e12166a1803e76689fb715ce2f64edc7a716`
- `workspace/outputs/route-report.md` SHA256: `326a89d297ede4de030fdc608fff8f1709990584972b24fbd11afd97da06ea8f`
- Actual candidate consumption: `proven=true`, event type `item.started`, JSONL line `4`
- Parsed consumption command read candidate `skills/orchestrator/SKILL.md` under the `ai-skills-candidate` plugin cache.
- Child stderr: empty.

## Normal-Entry Route Results

The fresh child handled the natural task `Use AI Skills Maintainer` with the short requests:

| Request | Result |
|---|---|
| `update AI Skills` | Route A by default; Route B only if formal release metadata declares cross-layer impact. Owner split: `ai-skills-repository-maintainer` for AI_Skills release production and `project-skill-installer` for managed install/profile refresh. |
| `sync this machine` | Composition of Route A/B/C for participating installed components; not a fourth route. Scope expansion only from each formal release's matching root `### Update impact`. |
| `update Bridge Kit` | Route C with internal owner `bridge-kit-maintainer`; real snapshot relation is `LAGGING`, so formal distribution closure is pending/incomplete. The child did not call the older `release` ref latest and did not treat newer `main` as a stable update target. |

The child reported the required Bridge release-state semantics:

- `ALIGNED`: release ref equals latest provable formal release.
- `LAGGING`: release ref is behind latest provable formal release; daily update must not advance it.
- `AHEAD/INCONSISTENT`: fail closed for ahead, unrelated, inconsistent or non-fast-forward targets.
- `FORMAL_RELEASE_NOT_PROVABLE`: fail closed when version/changelog/closure evidence is insufficient.

The child did not ask for versions, commits, checkout paths, `CODEX_HOME`, repository inventories, adaptation templates or dependency/component lists. The requested replay was a no-mutation dry run and returned `DRY_RUN / NOT_EXECUTED`.

This evidence closes pre-release G1/G3 candidate normal-entry replay only. It does not claim G2 production Marketplace migration or released production smoke.
