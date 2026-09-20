# Workflow Identity And Gate Lifecycle Evidence

Task key: `cross-repo--workflow-identity-gate-lifecycle`  
Human label: 工作流命名与插件回归机制完善（AI_Skills + Bridge）  
Production candidate commit: `ce63f50238555849a48256068e6fa0d46e21a97b`  
Branch: `reviewed/cross-repo--workflow-identity-gate-lifecycle`

## Remote Identity Gate

- AI_Skills remote identity was checked before branch/worktree creation.
- `origin` fetch/push URL: `https://github.com/YuukiAS/AI_Skills_Collection.git`
- Baseline `origin/main`: `2b6a5b5`

## Version Decisions

Repository bump decision: PATCH
Reason: compatible workflow-control and central-plugin-maintenance behavior hardening without a new repository-level capability or breaking contract.

Affected plugins:

- `workflow-core`: `0.1` -> `0.2`
  Reason: task-key identity, human-label separation, and release gate selection behavior changed.
- `ai-skills-core`: `0.2` -> `0.3`
  Reason: central-plugin gate lifecycle, regression bank, narrow/broad gate selection, and task identity maintenance behavior changed.

Unchanged plugins: `writing-style 0.3`, `research-writing 0.1`, `presentations 0.3`, `scientific-visualization 0.1`, `web-development 0.1`, `statistical-modeling 0.1`, `bioinformatics 0.1`, `medical-imaging 0.1`.

## Local Validation

- `python scripts/skills.py registry --write` -> PASS, wrote `registry.json` with 150 skills.
- `python scripts/skills.py catalog --write` -> PASS, wrote `docs/SKILL_CATALOG.md` and 16 domain pages.
- `python scripts/build_codex_marketplace.py --write --validate --check --path-report` -> PASS, `plugins=10`, `active_skills=27`, `source_snapshots=65`, `over_budget=0`.
- `python scripts/skills.py validate` -> PASS, validated 150 active skills, 18 profiles, templates, and trigger eval scaffolds.
- `python scripts/skills.py audit --all` -> PASS with advisory profile/domain context-budget output only.
- `python -m unittest tests.test_codex_marketplace` -> PASS, 36 tests.
- `python -m unittest discover -s tests` -> PASS, 232 tests.

## Candidate Plugin Replay

Runtime:

- `python scripts/candidate_plugin_replay.py ensure-runtime` -> PASS
- Runtime version: `codex-cli 0.153.4`
- Runtime binary SHA-256: `56ef98ab4032d317ab26e9b5e5a175650717351edb16ed9cde0cb6d1734d62da`

Fixed public-safe scenarios:

1. `workflow-core`
   - Command: `python scripts/candidate_plugin_replay.py replay --plugin workflow-core --candidate-commit ce63f50 --task results/cross-repo--workflow-identity-gate-lifecycle/replay/workflow-core-task.md --input results/cross-repo--workflow-identity-gate-lifecycle/replay/workflow-core-input.md`
   - Result: PASS
   - Candidate plugin id: `workflow-core@ai-skills-candidate`
   - Candidate plugin version: `0.2`
   - Actual consumption proven: true
   - Artifact: `results/cross-repo--workflow-identity-gate-lifecycle/replay/artifacts/workflow-core-run.json`

2. `ai-skills-core`
   - Command: `python scripts/candidate_plugin_replay.py replay --plugin ai-skills-core --candidate-commit ce63f50 --task results/cross-repo--workflow-identity-gate-lifecycle/replay/ai-skills-core-task.md --input results/cross-repo--workflow-identity-gate-lifecycle/replay/ai-skills-core-input.md`
   - Result: PASS
   - Candidate plugin id: `ai-skills-core@ai-skills-candidate`
   - Candidate plugin version: `0.3`
   - Actual consumption proven: true
   - Artifact: `results/cross-repo--workflow-identity-gate-lifecycle/replay/artifacts/ai-skills-core-run.json`

Replay evidence proves candidate plugin loading, fresh-runtime consumption, cleanup, and production-identity preservation. It does not replace independent implementation review.
