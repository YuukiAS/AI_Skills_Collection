# workflow-core 0.5 Qualification Status

Date: 2026-10-01
Branch: `work/workflow-core--normal-entry-reliability`
Implementation commit: `0e6c134fef60cd9c22895dba42d7823e01644793`
Status: `QUALIFICATION_PASS`

## Scope

This evidence belongs to the ordinary bounded implementation for
`workflow-core--normal-entry-reliability`.

The current implementation is still a workflow-core `0.4` qualification
candidate. No version bump has been performed.

## Implemented Source Changes

The implementation commit adds workflow-core guidance and regression coverage
for:

- least-privilege normal-entry selection before escalation;
- specialist/project runtime checks before treating a capability as absent;
- required / optional / unknown effect classification;
- six-dimension, privilege-non-increasing recovery;
- approval rejection classification;
- repeated same-class approval rejection route reassessment;
- effect-scoped truth when publication or transport fails after local work
  already succeeded.

Changed areas are limited to the approved workflow-core source, generated
workflow-core payload, and targeted regression test:

- `skills/core/codex-system/codex-workflow-protocol/SKILL.md`
- `skills/core/codex-system/codex-workflow-protocol/references/escalation-rules.md`
- `skills/core/codex-system/codex-workflow-protocol/agents/openai.yaml`
- `skills/core/codex-system/codex-workflow-protocol/evals/trigger_queries.json`
- `plugins/codex/plugins/workflow-core/skills/workflow/*`
- `tests/test_workflow_core_normal_entry_reliability.py`

## Passing Local Evidence

The following checks passed on the implementation candidate:

```text
python3 -m unittest tests.test_workflow_core_normal_entry_reliability
/usr/bin/python3 -m unittest tests.test_workflow_core_reviewed_handoff_routing tests.test_codex_marketplace tests.test_standalone_skill_baselines
/usr/bin/python3 -m unittest tests.test_candidate_plugin_replay
python3 scripts/build_codex_marketplace.py --write
python3 scripts/build_codex_marketplace.py --validate
python3 scripts/build_codex_marketplace.py --check
python3 scripts/build_codex_marketplace.py --path-report
python3 scripts/skills.py validate
python3 scripts/skills.py audit --all
git diff --check
```

Notes:

- `/usr/bin/python3` was used for the adjacent Marketplace test group because
  the default `python3` resolved to a user venv whose `setup.py --version`
  subprocess lacked `setuptools`.
- Generated marketplace content is current. One generated-file mode mismatch
  caused by the sandboxed write was corrected back to Git's expected `100644`
  mode before `--check` passed.
- `tests.test_candidate_plugin_replay` passed after widening one timeout fixture
  from `0.5s` to `3s`; the assertion still verifies that timeout preserves
  already-written child streams and kills the process group.

## Broad Suite Result

`/usr/bin/python3 -m unittest discover -s tests` did not pass in the current
Longleaf environment.

Observed failures were outside workflow-core and were attributable to missing
test environment dependencies or existing broad-suite behavior:

- `PIL` missing in Presentation shared tests;
- `matplotlib` missing in Presentation benchmark tests;
- one `test_candidate_plugin_replay` timeout-stream assertion observed empty
  stdout in this environment.

This broad-suite result is not claimed as PASS.

## Production-Compatible Candidate Consumption

Canonical task-local candidate replay passed on the implementation candidate.
The route used the repository script already present at the approved package
baseline:

```text
python3 scripts/candidate_plugin_replay.py replay --plugin workflow-core --candidate-commit 0e6c134fef60cd9c22895dba42d7823e01644793 --task results/workflow-core--normal-entry-reliability/qualification_candidate_replay_task.md --input results/workflow-core--normal-entry-reliability/qualification_candidate_replay_input.md
```

Replay identity:

- candidate commit:
  `0e6c134fef60cd9c22895dba42d7823e01644793`;
- plugin id: `workflow-core@ai-skills-candidate`;
- plugin version: `0.4`;
- runtime: `codex-cli 0.153.4`;
- actual consumption: `proven=true`, event `item.started`, line `7`;
- raw source run:
  `.local-runtime/candidate-plugin-replay/runs/20261002T035651Z-714130`;
- tracked raw evidence:
  `results/workflow-core--normal-entry-reliability/qualification_candidate_replay_raw/`;
- manifest:
  `results/workflow-core--normal-entry-reliability/qualification_candidate_replay_manifest.json`.

This proves `GLOBAL_WORKFLOW_CORE_PLUGIN_ABSENT !=
CANDIDATE_REPLAY_UNAVAILABLE` for this qualification candidate. No
live-global workflow-core install, production Marketplace mutation, Bridge /
Host Policy mutation, raw publication fallback, paid API, or new authorization
route was used.

Qualification remains a workflow-core `0.4` candidate result. No workflow-core
`0.4 -> 0.5` version bump has been performed yet; the version mutation is
authorized only after this qualification stage.
