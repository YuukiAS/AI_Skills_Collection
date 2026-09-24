# AI Skills Maintainer Machine Update Orchestration Evidence

Task key: `ai-skills-core--machine-update-orchestration`

## Candidate Identity

- AI_Skills task branch: `reviewed/ai-skills-core--machine-update-orchestration`
- Reconciled product-surface candidate replayed: `4b8414733f3efc2d8707c5fbf448cbe8ec7a7d00`
- Planner recovery amendment 2 commit: `65b7d85a47f3bea8b42e342d1801dfbb5df04442`
- Latest `origin/main` integrated before this candidate: `58884c1b093e363dc772d17aba8bfbdc51005336`
- Version decision: repository `5.2.0`, `ai-skills-core 0.4 -> 0.5`, `workflow-core` remains `0.4`

## Implemented Source Scope

- Added `machine-update-orchestrator` inside `ai-skills-core`.
- Added `bridge-kit-maintainer` inside `ai-skills-core`.
- Added Route A/B/C references for isolated AI_Skills updates, formal cross-layer composition and Bridge Kit distribution/runtime update.
- Added formal `release` / `### Update impact` contract, legacy Marketplace bootstrap rules, selective managed-consumer boundary, Human Gate/recovery rules and fresh-session truthfulness.
- Updated `ai-skills-repository-maintainer` and `project-skill-installer` boundaries to route current-machine update requests through the orchestrator.
- Reconciled latest main's `5.1.1` / `workflow-core 0.4` baseline into the task branch and regenerated the canonical registry/catalog/Marketplace/plugin payload.

## Bridge Snapshot And Locator

- Bridge repo: `YuukiAS/GPT_Codex_AI_Bridge_Kit`
- Bridge `main` observed for the frozen repair snapshot: `ff22c97c8193e110d606e179ec1a8a2741b97fad`
- Bridge `release` observed for the frozen repair snapshot: `d27259d6706dee951dc0c0ede8c9b03c65f55ca3`
- Bridge `AGENTS.md` owner locator remained present and semantically equivalent.
- Task-owned raw Bridge source snapshots were made available under `private/exports/ai-skills-core--machine-update-orchestration/bridge_git_snapshot` and `private/exports/ai-skills-core--machine-update-orchestration/bridge_source_snapshot`.
- No Bridge runtime/source files were modified during this repair round, and Bridge `release` was not advanced.

## Validation

- `python scripts/skills.py registry --write` -> PASS, `153` skills.
- `python scripts/skills.py catalog --write` -> PASS.
- `python scripts/build_codex_marketplace.py --write` -> PASS, `10` plugins, `29` active skills, `69` source snapshots.
- `python scripts/build_codex_marketplace.py --check --json` -> PASS, no errors/warnings.
- `python scripts/build_codex_marketplace.py --validate --json` -> PASS, no errors/warnings.
- `python -m unittest tests.test_codex_marketplace tests.test_standalone_skill_baselines tests.test_workflow_core_reviewed_handoff_routing` -> PASS, `45` tests.
- `python -m unittest discover -s tests -p 'test_*.py'` -> PASS, `264` tests. The first sandboxed attempt hit read-only filesystem errors in generated-artifact tests; the successful full run used the authorized reviewed worktree write boundary.

## G1/G3 Candidate Replay

- Public-safe replay task/input are saved under `results/ai-skills-core--machine-update-orchestration/candidate_replay/`.
- Actual `candidate_plugin_replay.py replay` ran against commit `4b8414733f3efc2d8707c5fbf448cbe8ec7a7d00`.
- Candidate plugin loaded as `ai-skills-core@ai-skills-candidate` version `0.5`.
- Actual candidate consumption was proven from parsed child JSONL line `4`, event type `item.started`, reading candidate `skills/orchestrator/SKILL.md`.
- G3 input no longer supplied latest Bridge formal release, current release version, relation/classification, or expected `LAGGING` interpretation.
- The child read the allowed Bridge source, owner locator, version sources, CHANGELOG, formal closure evidence and refs, then selected `LAGGING` dynamically through Git ancestry evidence.
- Replay evidence is recorded in `results/ai-skills-core--machine-update-orchestration/candidate_replay/CANDIDATE_REPLAY_EVIDENCE.md`.

## G4/G5 Fixture Status

- Task-owned local fixture repositories were created under `private/exports/ai-skills-core--machine-update-orchestration/fixtures/`.
- Fixture execution covered stale managed consumer update, unaffected repo preservation, unmanaged conflict preservation, unrelated dirty non-overlap, overlapping dirty Human Gate, bounded failure/restoration, rerun convergence and should-not-change evidence.
- The repaired fixture harness owns fixture setup/reset, bounded failure injection, before/after hashing, Git-state capture, invariant assertions and evidence collation only.
- Actual semantic states, fixture mutations, `PARTIAL_UPDATE`, and Marketplace restoration came from the candidate child through `candidate_plugin_replay.py`.
- Marketplace failure/recovery used an isolated task-owned `CODEX_HOME` and official `codex plugin marketplace list/remove/add --json` commands. The runner verified the exact legacy source was restored through a final official `list --json`.
- Fixture summary is recorded in `results/ai-skills-core--machine-update-orchestration/fixture_execution/G4_G5_FIXTURE_EVIDENCE.md`.
- JSON evidence is recorded in `results/ai-skills-core--machine-update-orchestration/fixture_execution/g4_g5_fixture_evidence.json`.

## G2 Sequencing

G2 remains `SEQUENCED WAITING`. This repair did not execute formal promotion, did not fast-forward AI_Skills `release`, did not perform real production Marketplace migration, did not reinstall production `ai-skills-core 0.5`, and did not run released fresh-session smoke.
