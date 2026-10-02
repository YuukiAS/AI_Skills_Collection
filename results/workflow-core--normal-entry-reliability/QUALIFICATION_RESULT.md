# workflow-core 0.5 Qualification Status

Date: 2026-10-01
Branch: `work/workflow-core--normal-entry-reliability`
Implementation commit: `0e6c134fef60cd9c22895dba42d7823e01644793`
Status: `BLOCKED_BEFORE_QUALIFICATION_PASS`

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

## Production-Compatible Consumption Blocker

Qualification PASS is currently blocked because the frozen Plan requires real
candidate plugin consumption / production-compatible replay evidence.

Observed state:

```text
codex plugin list
workflow-core@yuukias-ai-skills: not installed
ai-skills-core@yuukias-ai-skills: installed, enabled
```

`ai-bridge plugin-replay --dry-run` with
`workflow-core@yuukias-ai-skills` failed because the plugin is not installed or
enabled in the current Codex identity.

Task-local isolation attempts did not establish a safe production-compatible
replay path:

- setting `CODEX_HOME` and `HOME` to a task-local directory still showed the
  current user global marketplaces;
- `codex plugin marketplace list -c ...` ignored attempted temporary
  marketplace overrides;
- `codex exec --ignore-user-config` failed in this environment while
  initializing the in-process app-server client with a read-only filesystem
  error.

Therefore, continuing to qualification PASS requires either:

- explicit authorization to perform a bounded live-global candidate install /
  shadow-marketplace mutation for `workflow-core`, or
- another production-compatible replay path that does not mutate current global
  plugin state.

No workflow-core `0.4 -> 0.5` version bump has been performed.
