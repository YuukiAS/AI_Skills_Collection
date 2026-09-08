---
schema: AI_BRIDGE_REVIEWED_RESULT_V1
task_key: 051_writing_style_rebuild
implementation_commit: f58b83dcb59d6893c73060f7e8b2c5f1afa7543c
---

# Codex Result

## Status

Implementation candidate is frozen at
`f58b83dcb59d6893c73060f7e8b2c5f1afa7543c`.

Gate 1 local implementation/mechanism PROCESS evidence is passing.

Gate 2 is stopped at `NEEDS_BRIDGE_RUNTIME_REFRESH`. This is not a
`writing-style` failure: the current shell runtime is using `codex-cli 0.142.0`
and an older installed `ai-bridge` that does not expose
`candidate-plugin-replay`. The Bridge B0 command is visible only when invoked
from the task-local accepted Bridge Kit copy at
`87893855332c665063e71f907c2c534b86cc3b39`, and that copy then fails against
the current Codex runtime because process-local marketplace overrides are not
recognized by `codex-cli 0.142.0`.

Per user instruction, no persistent marketplace add/remove, no B1 fallback, no
051 architecture change, and no A/B/C artifact replay occurred after this
runtime mismatch was confirmed.

## Implemented

- Added source `skills/writing/core/scientific-rewrite/` as the heavy Chinese
  source-faithful structural rewrite route inside `writing-style`.
- Added `rewrite_support.py` mechanical validation for Meaning Map, Reader Plan,
  ordinary `writing-style` route selection, realization/repair/assembly packet
  leakage, exact-item preservation, structural rewrite fidelity, semantic audit,
  privacy/paid-generation receipt fields, and the compatibility
  `validate-host-stage` CLI entrypoint.
- Updated `writing-fidelity` with the `STRUCTURAL_REWRITE` handoff that protects
  claims, evidence, numbers, formulas, citations, comparators, conditions,
  scope, uncertainty, caveats, attribution, and conclusion strength while
  allowing source headings/order to change when the heavy route authorizes it.
- Updated `chinese-prose` final-pass rules for heavy-route Reader Plan output.
- Updated `scripts/codex_marketplace_config.json`,
  `profiles/codex-writing-style.json`, and regenerated the
  `plugins/codex/plugins/writing-style/` payload.
- Added focused tests in `tests/test_scientific_rewrite.py`.

No repository or plugin version bump was made. Per Plan, version/changelog
updates belong to the final accepted release closure, not this initial
implementation stage.

## Verification

- `python3 scripts/build_codex_marketplace.py --write --validate --check --path-report`
  - PASS: 10 plugins, 27 active plugin skills, 65 source snapshots,
    `over_budget=0`.
- `python3 -m unittest tests.test_scientific_rewrite tests.test_skill_runtime_text_audit tests.test_codex_marketplace -q`
  - PASS: 51 tests.
- `python3 scripts/skills.py validate`
  - PASS: validated 150 active skills, 18 profiles, templates, and trigger eval
    scaffolds.
- `python3 scripts/skills.py audit --all`
  - PASS: command completed successfully; output contained profile/domain budget
    advice only.
- `python3 scripts/build_codex_marketplace.py --validate --check`
  - PASS: 10 plugins, 27 active plugin skills, 65 source snapshots.
- `python3 -m unittest discover -s tests -q`
  - PASS: 185 tests.
- `ai-bridge reviewed-handoff validate --target /tmp/ai-skills-051-bootstrap-20260907`
  - PASS with only legacy PLAN V1 warnings for old tasks.

## Bridge Runtime Preflight

- `which -a ai-bridge`
  - `/overflow/htzhu/mingcheng_new/.local/bin/ai-bridge`
  - `/overflow/htzhu/mingcheng_new/conda/bin/ai-bridge`
- `which -a codex`
  - `/overflow/htzhu/mingcheng_new/bin/codex`
  - `/overflow/htzhu/mingcheng_new/conda/bin/codex`
- `codex --version`
  - `codex-cli 0.142.0`
- `python3 -c "import ai_bridge_kit; print(ai_bridge_kit.__file__)"`
  - `/overflow/htzhu/mingcheng_new/GPT_Codex_AI_Bridge_Kit/ai_bridge_kit/__init__.py`
- `git -C /overflow/htzhu/mingcheng_new/GPT_Codex_AI_Bridge_Kit rev-parse HEAD`
  - `3b061167794d593b113ca8f4a8a43c4c8000fc01`
- `ai-bridge candidate-plugin-replay --help`
  - FAIL: installed `ai-bridge` reports invalid command and lists only
    `init`, `validate`, `host`, `notifier`, `private`, `agent-flow`, `prompt`,
    and `where`.
- `PYTHONPATH=/tmp/bridge-candidate-replay-8789385 python3 -m ai_bridge_kit.bridge_cli candidate-plugin-replay --help`
  - PASS: accepted Bridge Kit copy at `87893855332c665063e71f907c2c534b86cc3b39`
    exposes `candidate-plugin-replay`.
- `ai-bridge host validate`
  - PASS: host config is configured; it reports trusted ai-bridge executable
    `/overflow/htzhu/mingcheng_new/.local/bin/ai-bridge` and Codex version
    `codex-cli 0.142.0`.

Actual `PATH` begins:

```text
/overflow/htzhu/mingcheng_new/bin:/overflow/htzhu/mingcheng_new/.local/bin:/usr/share/Modules/bin:...
```

## Candidate Replay Attempt

Public smoke input and prompt:

- `results/051_writing_style_rebuild/production_replay/public_rewrite_source.md`
- `results/051_writing_style_rebuild/production_replay/PRODUCTION_REPLAY_TASK.md`

Command:

```bash
env -u HTTP_PROXY -u HTTPS_PROXY -u ALL_PROXY -u http_proxy -u https_proxy -u all_proxy PYTHONPATH=/tmp/bridge-candidate-replay-8789385 python3 -m ai_bridge_kit.bridge_cli candidate-plugin-replay --target /tmp/ai-skills-051-bootstrap-20260907 --plugin writing-style --candidate-commit f58b83dcb59d6893c73060f7e8b2c5f1afa7543c --task results/051_writing_style_rebuild/production_replay/PRODUCTION_REPLAY_TASK.md --input results/051_writing_style_rebuild/production_replay/public_rewrite_source.md
```

Result:

```text
ERROR: CANDIDATE_PLUGIN_ADD_FAILED: Error: plugin `writing-style` was not found in marketplace `ai-bridge-candidate-20260908T025155Z-753c1036ec8c`
```

Follow-up probes staged the exact committed candidate tree from
`f58b83dcb59d6893c73060f7e8b2c5f1afa7543c` into a temporary marketplace under
`/tmp/051-candidate-marketplace-probe/marketplace`. The staged plugin tree
digest was:

```text
a4be0026be584f26e95b7be6b0fbfa9fc86c0072260bc76cee7813f145a2de62
```

Both dotted and whole-table process-local Codex overrides failed to add the
temporary marketplace to `codex plugin marketplace list --json` or
`codex plugin list --json`; only the existing `openai-bundled`,
`openai-curated`, and `yuukias-ai-skills` marketplaces appeared. This matches
the user's note that Bridge B0 was validated on `codex-cli 0.153.4`, while the
current runtime is `codex-cli 0.142.0`.

## Deviations / blockers

- Gate 2 remains pending on compatible Bridge/Codex runtime refresh, classified
  as `NEEDS_BRIDGE_RUNTIME_REFRESH`.
- The current environment does not satisfy the user-provided Bridge precondition:
  actual `ai-bridge` lacks `candidate-plugin-replay`, and actual Codex is
  `0.142.0` rather than the B0-validated `0.153.4`.
- Per explicit user instruction, persistent marketplace add/remove and B1
  fallback are not authorized and were not run.
- Gates for known A/B/C regression, full private report, fresh holdout, Text
  Review, final CI, version/changelog, Reviewer PASS, and integration are not
  started.
