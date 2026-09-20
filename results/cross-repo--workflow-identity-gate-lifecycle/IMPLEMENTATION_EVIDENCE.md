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

### Preserved Initial Replay Runs

The initial replay runs are preserved and not deleted:

- `results/cross-repo--workflow-identity-gate-lifecycle/replay/artifacts/workflow-core-run.json`
- `results/cross-repo--workflow-identity-gate-lifecycle/replay/artifacts/ai-skills-core-run.json`

Independent Critic R1 found these initial runs insufficient for `C-WIGL-I2-REPLAY-CAPABILITY-EVIDENCE`: they proved candidate loading / SKILL consumption but did not preserve substantive repo-resident model output or prove the required G3/G5/G6 behavior. They remain provenance only and are not treated as corrected acceptance PASS.

### Corrected Frozen Replay Scenarios

Authorization boundary:

- User explicitly approved exactly one fixed `ai-skills-core` corrected candidate replay after auto-review rejected the escalated command.
- Scope: current Codex identity, repo-owned public-safe frozen scenario/input, no private artifact, no Terra/OpenAI Responses paid review, no new provider/account/credential, no third replay scenario.

Corrected public-safe scenarios:

1. `workflow-core`
   - Frozen task sha256: `37ddf02b8fe1f59d9e5cb816869f74b20f37341dc89a26231c37e13d0756c7f1`
   - Frozen input sha256: `e2146d8b8094a6855ee2b2512ead8e20c9756034cd3a4993e7775e9d33e6d5b3`
   - Command: `python scripts/candidate_plugin_replay.py replay --plugin workflow-core --candidate-commit ce63f50 --task results/cross-repo--workflow-identity-gate-lifecycle/replay/corrected/workflow-core-task.md --input results/cross-repo--workflow-identity-gate-lifecycle/replay/corrected/workflow-core-input.md`
   - Result: PASS
   - Candidate plugin id: `workflow-core@ai-skills-candidate`
   - Candidate plugin version: `0.2`
   - Actual consumption proven: true
   - Run receipt: `results/cross-repo--workflow-identity-gate-lifecycle/replay/corrected/artifacts/workflow-core-run.json`
   - Substantive output: `results/cross-repo--workflow-identity-gate-lifecycle/replay/corrected/outputs/workflow-core-final-response.md`
   - Verdict: `results/cross-repo--workflow-identity-gate-lifecycle/replay/corrected/verdicts/workflow-core-verdict.md`
   - Verified behavior: explainably isolated local change -> `NARROW_OK`; shared normal-entry/runtime surface change -> `BROAD_FULL_REQUIRED`; unresolved multi-Gate failure -> `NOT_RELEASE_READY`; maturity promotion -> `MATURITY_NOT_PROVEN`; same-final-candidate requirement preserved; no fixed paid/fresh count invented.

2. `ai-skills-core`
   - Frozen task sha256: `32b78110a2d88bf349c7c4061f58104cad679f018330b3db4bcd3ccc1999f838`
   - Frozen input sha256: `4fc42405f3ec5a7e3096358186c845d1e171499b72c219f5276ebb5a941a48df`
   - Command: `python scripts/candidate_plugin_replay.py replay --plugin ai-skills-core --candidate-commit ce63f50 --task results/cross-repo--workflow-identity-gate-lifecycle/replay/corrected/ai-skills-core-task.md --input results/cross-repo--workflow-identity-gate-lifecycle/replay/corrected/ai-skills-core-input.md`
   - Result: PASS
   - Candidate plugin id: `ai-skills-core@ai-skills-candidate`
   - Candidate plugin version: `0.3`
   - Actual consumption proven: true
   - Run receipt: `results/cross-repo--workflow-identity-gate-lifecycle/replay/corrected/artifacts/ai-skills-core-run.json`
   - Substantive output: `results/cross-repo--workflow-identity-gate-lifecycle/replay/corrected/outputs/ai-skills-core-final-response.md`
   - Verdict: `results/cross-repo--workflow-identity-gate-lifecycle/replay/corrected/verdicts/ai-skills-core-verdict.md`
   - Verified behavior: single plugin classification; one AI_Skills repository / multiple production plugins classification; AI_Skills + Bridge mutable with product repos read-only; existing capability regression -> existing Gate; genuinely new capability -> Gate redesign consideration; domain ownership preserved.

Corrected replay evidence proves candidate plugin loading, fresh-runtime consumption, substantive behavior, cleanup, and production-identity preservation. It does not replace independent implementation review.

## Frozen Cross-Repo Candidate Tuple

- AI_Skills production candidate: `ce63f50238555849a48256068e6fa0d46e21a97b`
- AI_Skills source-change decision after corrected replay: unchanged; no real consumer defect found.
- Bridge production candidate: `7f2707dd4020951650d561303c82a17e22b27317`
- Bridge evidence branch tip after R1 repair: `d09306f180634aa4d4ad4ec3ee46295a8b20945b`
- Next owner after both branches are pushed: `INDEPENDENT_IMPLEMENTATION_REVIEW`
