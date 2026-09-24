# AI Skills Maintainer Machine Update Orchestration Evidence

Task key: `ai-skills-core--machine-update-orchestration`

## Candidate Identity

- AI_Skills task branch: `reviewed/ai-skills-core--machine-update-orchestration`
- AI_Skills candidate replay commit: `12ca08dc127f8eee4c13a3a2c9cc598d00ce04ee`
- Planner decision commit: `10ed6848bba9ad812c892bd3a39441f41034323a`
- Base integrated during implementation: `origin/main` at `7b76e94ad29cf3bd8547026b942553068754d51f` (`5.1.0` Project Thread Handoff)
- Version decision after live drift: repository `5.2.0`, `ai-skills-core 0.4 -> 0.5`

## Implemented Source Scope

- Added `machine-update-orchestrator` inside `ai-skills-core`.
- Added `bridge-kit-maintainer` inside `ai-skills-core`.
- Added Route A/B/C references for isolated AI_Skills updates, formal cross-layer composition and Bridge Kit distribution/runtime update.
- Added formal `release` / `### Update impact` contract, legacy Marketplace bootstrap rules, selective managed-consumer boundary, Human Gate/recovery rules and fresh-session truthfulness.
- Updated `ai-skills-repository-maintainer` and `project-skill-installer` boundaries to route current-machine update requests through the orchestrator.
- Updated Marketplace config, generated payload, profile, README, root/plugin changelogs, TODO and tests.

## Bridge-Side Locator

- Bridge repo: `YuukiAS/GPT_Codex_AI_Bridge_Kit`
- Bridge locator commit on `origin/main`: `dfe093c6f78cdadb22905e811935a772af5cb034`
- Bridge file changed: `AGENTS.md` only.
- Locator states that Bridge runtime / Host / Lite / Review / Control / Persistent Run implementation remains in Bridge Kit, while formal Bridge distribution/version closure including `release` ref ownership belongs to AI Skills Maintainer -> `bridge-kit-maintainer`.
- No Bridge README, QUICKSTART, CHANGELOG or runtime source was modified for the locator.

## Release Ref Bootstrap

- `YuukiAS/AI_Skills_Collection:refs/heads/release` created and verified at `7b76e94ad29cf3bd8547026b942553068754d51f`.
- `YuukiAS/GPT_Codex_AI_Bridge_Kit:refs/heads/release` created and verified at `d27259d6706dee951dc0c0ede8c9b03c65f55ca3`.
- Both pushes were non-force exact-ref creations after origin identity and target evidence checks.

## Validation

- `python scripts/skills.py registry --write` -> PASS, `153` skills.
- `python scripts/skills.py validate` -> PASS, `153` active skills, `18` profiles.
- `python scripts/skills.py audit --all` -> PASS with budget advice only.
- `python scripts/skills.py catalog --write` -> PASS.
- `python scripts/build_codex_marketplace.py --write --validate --check --path-report` -> PASS, `10` plugins, `29` active skills, Windows path budget OK.
- Targeted Maintainer/candidate replay tests -> PASS, `67` tests.
- `python -m unittest discover -s tests` -> PASS, `254` tests.

## Candidate Replay Status

- Repo-local replay runtime was verified: `codex-cli 0.153.4`, archive SHA256 `a822187e1a2420c61c5926721bfbd878701ed95547c9bb0d4de4498a16ba1821`.
- Public-safe replay task/input are saved under `results/ai-skills-core--machine-update-orchestration/candidate_replay/`.
- Planner decision `10ed6848bba9ad812c892bd3a39441f41034323a` clarified that this canonical candidate replay is the approved no-paid G1/G3 path and is not a Terra/OpenAI Responses paid API call.
- Actual `candidate_plugin_replay.py replay` ran against commit `12ca08dc127f8eee4c13a3a2c9cc598d00ce04ee` with task `candidate_replay/machine_update_g1_g3_short_requests.md`.
- Candidate plugin loaded as `ai-skills-core@ai-skills-candidate` version `0.5`.
- Actual candidate consumption was proven from parsed child JSONL line `4`, event type `item.started`, reading candidate `skills/orchestrator/SKILL.md`.
- Child route report covered `update AI Skills`, `sync this machine`, and `update Bridge Kit`; it returned Route A, Route A/B/C composition, and Route C respectively, without asking for versions, commits, checkout paths, `CODEX_HOME`, repo inventories, adaptation templates, or component lists.
- Bridge G3 used the frozen `BRIDGE_REVALIDATION_SNAPSHOT.md` and current repair-start revalidation. The real snapshot case is `LAGGING`: current Bridge `release` is behind latest provable formal release, so the child reported formal distribution closure as pending/incomplete and did not call the older ref latest.
- Replay evidence is recorded in `results/ai-skills-core--machine-update-orchestration/candidate_replay/CANDIDATE_REPLAY_EVIDENCE.md`.

## G4/G5 Fixture Status

- Task-owned local fixture repositories were created under `private/exports/ai-skills-core--machine-update-orchestration/fixtures/`.
- Fixture execution covered stale managed consumer update, unaffected repo preservation, unmanaged conflict preservation, unrelated dirty non-overlap, overlapping dirty Human Gate, bounded failure/restoration, rerun convergence and should-not-change evidence.
- The repaired fixture harness owns fixture setup, bounded failure injection, before/after hashing, Git-state capture, invariant assertions and evidence collation only. Actual semantic states and fixture mutations came from the committed candidate via `candidate_plugin_replay.py`.
- Fixture summary is recorded in `results/ai-skills-core--machine-update-orchestration/fixture_execution/G4_G5_FIXTURE_EVIDENCE.md`.
- JSON evidence is recorded in `results/ai-skills-core--machine-update-orchestration/fixture_execution/g4_g5_fixture_evidence.json`.

## Legacy Marketplace Discovery

- Current configured AI_Skills Marketplace name: `yuukias-ai-skills`.
- Source: `https://github.com/YuukiAS/AI_Skills_Collection.git`.
- Current snapshot metadata file: `/home/yuukias/.codex/.tmp/marketplaces/yuukias-ai-skills/.codex-marketplace-install.json`.
- Discovered `ref_name`: `main`.
- Discovered sparse paths: `.agents/plugins`, `plugins/codex/plugins`.
- Snapshot revision before bootstrap: `999afbfd65702e4c2fb089a36a8d3ebf40baa9e5`, repository version `5.0.7`.
- Installed production plugin state before bootstrap: `ai-skills-core@yuukias-ai-skills` version `0.4`, enabled.
- Remote AI_Skills `release` was verified at `7b76e94ad29cf3bd8547026b942553068754d51f`, which is repository `5.1.0` and still contains `ai-skills-core 0.4`.
- Actual `main -> release` Marketplace migration was **not executed** in this pre-release validation run because Planner decision D2 requires Reviewer PASS and formal promotion first. The current remote `release` ref does not yet contain the capability-bearing `ai-skills-core 0.5` candidate; migrating now would only reinstall `0.4` and would not satisfy G2.
