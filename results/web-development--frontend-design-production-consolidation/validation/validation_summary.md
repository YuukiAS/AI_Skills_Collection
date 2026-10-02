# Frontend Design Production Consolidation Validation Summary

Task key: `web-development--frontend-design-production-consolidation`

Candidate state: implementation commit `1bb4650d8192d829b850abaccee53773ef50e091`.

## Implemented

- Shared Marketplace generator supports opt-in `routing_mode = coordinator-first`.
- Invalid or missing `coordinator_artifact_id` fails closed.
- Default aggregates without `routing_mode` keep choose-one workflow text.
- `web-development` main `frontend-visual-systems` aggregate is coordinator-first with coordinator artifact `system`.
- `product-ux-planning`, `visual-direction`, `design-system-tokens`, `figma-design-to-code`, `motion-interaction`, `responsive-accessibility-review`, `webapp-testing`, and `research-product-frontend` are coordinator delegates.
- The standalone generated `research-product-frontend` active route was removed from the `web-development` plugin payload; its canonical source remains as a delegate snapshot.
- `frontend-reference-research` remains an explicit narrow `refs` active skill.
- `implementation-react-tailwind` remains a downstream builder source and is not a design owner.
- Version closure is applied once: repository `5.3.1`, `web-development 0.3`, all other central plugins unchanged, maturity unchanged.

## Commands Run

- `python -m unittest tests.test_codex_marketplace.CodexMarketplaceTests.test_coordinator_first_aggregate_requires_valid_coordinator_source ...`
  - Result: PASS, 4 targeted generator/topology tests.
- `python -m unittest tests.test_codex_marketplace.CodexMarketplaceTests.test_coordinator_first_aggregate_requires_valid_coordinator_source ... tests.test_056_product_delivery_discipline_gates`
  - Result: PASS, 15 targeted tests including 056 F-A/F-B/F-C regression.
- `python scripts/build_codex_marketplace.py --write --validate --check --path-report`
  - Result: PASS. `plugins=10`, `active_skills=28`, `source_snapshots=71`, Windows path budget `over_budget=0`.
- `python scripts/skills.py registry --write`
  - Result: PASS. `registry.json` regenerated with 153 skills.
- `python scripts/skills.py validate`
  - Result: PASS. 153 active skills, 18 profiles, templates, and trigger eval scaffolds validated.
- `python scripts/skills.py audit --all`
  - Result: PASS. Only existing profile/domain budget advice emitted.
- `python scripts/skills.py catalog --write`
  - Result: PASS. `docs/SKILL_CATALOG.md` and 16 domain pages regenerated.
- `python -m unittest discover -s tests`
  - Result: PASS. 296 tests run.

## Candidate Replay Status

Candidate plugin replay completed with the repository's canonical helper. The earlier global Codex marketplace mutation path was rejected by auto-review and is retained as negative evidence; it was not used for the final replay.

Repo-local pinned runtime:

```text
version: codex-cli 0.153.4
path: .local-runtime/codex/0.153.4/bin/codex
archive_sha256: a822187e1a2420c61c5926721bfbd878701ed95547c9bb0d4de4498a16ba1821
binary_sha256: 56ef98ab4032d317ab26e9b5e5a175650717351edb16ed9cde0cb6d1734d62da
```

Replay command:

```bash
python scripts/candidate_plugin_replay.py replay \
  --plugin web-development \
  --candidate-commit 1bb4650d8192d829b850abaccee53773ef50e091 \
  --task results/web-development--frontend-design-production-consolidation/replay/frontend_candidate_replay_task.md \
  --input results/web-development--frontend-design-production-consolidation/candidate_visible_regressions/scenarios.json
```

Replay result:

- Run id: `20260928T030747Z-2077704`
- Actual plugin consumption: `proven=true`, event `item.started`, line index `8`
- Candidate selector: `web-development@ai-skills-candidate`
- Durable outputs:
  - `results/web-development--frontend-design-production-consolidation/replay/candidate_routing_decisions.md`
  - `results/web-development--frontend-design-production-consolidation/replay/candidate_source_evidence.json`
  - `results/web-development--frontend-design-production-consolidation/replay/candidate_plugin_replay_run.json`
- Output validation: PASS for 8 frozen scenarios and required routing/admission fields.

## G6 Real-Project Replay Status

Bobbio/Lucerna/Asteria real replay completed through the candidate plugin normal entry after explicit user authorization for the frozen project-source transmission.

Replay command:

```bash
python scripts/candidate_plugin_replay.py replay \
  --plugin web-development \
  --candidate-commit df01fac271e030f9259a1510034380e2ec422f76 \
  --task results/web-development--frontend-design-production-consolidation/replay/real_project_replays/real_project_replay_task.md \
  --input results/web-development--frontend-design-production-consolidation/replay/real_project_replays/real_project_replay_freeze_manifest.json \
  --input results/web-development--frontend-design-production-consolidation/replay/real_project_replays/real_project_replay_rubric.md
```

Replay result:

- Run id: `20260928T032921Z-2135985`
- Actual plugin consumption: `proven=true`, event `item.started`, line index `8`
- Durable outputs:
  - `results/web-development--frontend-design-production-consolidation/replay/real_project_replays/real_project_attribution.md`
  - `results/web-development--frontend-design-production-consolidation/replay/real_project_replays/real_project_attribution.json`
  - `results/web-development--frontend-design-production-consolidation/replay/real_project_replays/real_project_source_consumption.json`
  - `results/web-development--frontend-design-production-consolidation/replay/real_project_replays/real_project_replay_run.json`
- Attribution: Bobbio, Lucerna, and Asteria all count as compatibility/regression only; all three have `COUNTS_AS_PLUGIN_CAPABILITY=false`.
- Maturity remains `unclassified`.
