---
schema: AI_BRIDGE_REVIEWED_RESULT_V1
task_key: 051_writing_style_rebuild
implementation_commit: ee8dd6edda2a2e4dd8f3210504225a56432b11a0
---

# Codex Result

## Status

Production behavior candidate is frozen at
`ee8dd6edda2a2e4dd8f3210504225a56432b11a0`.

Gate 1 local implementation/mechanism PROCESS evidence is passing.

Gate 2 production behavior is PASS:

- `GATE2_PRODUCT_BEHAVIOR=PASS`
- `GATE2_HARNESS=FALSE_NEGATIVE`
- fresh child Codex read the candidate
  `plugins/cache/ai-skills-candidate/writing-style/0.1/skills/scientific-rewrite/SKILL.md`;
- the ordinary user prompt did not name internal route/plugin identities;
- route selection recorded `selected_route=scientific-rewrite`,
  `forced_route=false`, and `ordinary_user_prompt=true`;
- `SCIENTIFIC_REWRITE_HEAVY_ROUTE_RECEIPT_V2` was generated;
- candidate cleanup passed;
- production `writing-style@yuukias-ai-skills` identity remained unchanged.

Gate 2 was not rerun after the parser repair merely to manufacture a clean
`exit 0`. The PASS claim is based on the existing fresh-child production
behavior evidence plus a subsequent offline parser regression against the same
failed-run JSONL.

Earlier Gate 2 attempts exposed infrastructure and harness failures. They are
retained below as diagnostic history and are not product failures.

Initial Gate 2 was stopped at `NEEDS_BRIDGE_RUNTIME_REFRESH`. This was not a
`writing-style` failure: the shell runtime used `codex-cli 0.142.0` and an
older installed `ai-bridge` that did not expose `candidate-plugin-replay`. The
Bridge B0 command was visible only when invoked from the task-local accepted
Bridge Kit copy at `87893855332c665063e71f907c2c534b86cc3b39`, and that copy
then failed against the current Codex runtime because process-local marketplace
overrides were not recognized by `codex-cli 0.142.0`.

Refresh check on 2026-09-08 confirmed the same runtime gap:

- Current `codex` wrappers resolve to the existing
  `/overflow/htzhu/mingcheng_new/conda/lib/node_modules/@openai/codex/bin/codex.js`
  install, whose package version is `0.142.0`.
- Current installed `/overflow/htzhu/mingcheng_new/.local/bin/ai-bridge`
  still does not expose `candidate-plugin-replay`.
- Accepted Bridge implementation
  `87893855332c665063e71f907c2c534b86cc3b39` does expose
  `candidate-plugin-replay` when invoked from the task-local Bridge copy.
- The validated B0 reference runtime remains the Bridge evidence runtime
  `codex-cli 0.153.4`; no alternate Codex CLI version is accepted here as a
  substitute for that runtime refresh.

Per user instruction, no persistent marketplace add/remove, no B1 fallback, no
051 architecture change, and no A/B/C artifact replay occurred after this
runtime mismatch was confirmed.

Later repo-local runtime provisioning for `codex-cli 0.153.4` initially used
the wrong standalone asset and lacked `bin/codex-code-mode-host`. The harness
was repaired to use the official complete package asset and to validate both
`bin/codex` and `bin/codex-code-mode-host`.

The child plugin enable override also had a harness bug:
`plugins."writing-style@ai-skills-candidate".enabled=true` quoted the plugin id
as part of the TOML key. It was repaired to
`plugins.writing-style@ai-skills-candidate.enabled=true`.

After those harness/runtime repairs, an ordinary Gate 2 replay proved candidate
consumption but exposed a real production routing failure: the candidate loaded
`chinese-prose` / `writing-fidelity` but did not load `scientific-rewrite`.
This was classified as `051_ROUTING_REVISE`, not a harness failure.

Routing was then revised in the canonical source skills and regenerated
writing-style plugin payload:

- `skills/writing/core/scientific-rewrite/SKILL.md`
- `skills/writing/core/chinese-prose/SKILL.md`
- `skills/writing/core/writing-fidelity/SKILL.md`
- `plugins/codex/plugins/writing-style/skills/**`

The final production behavior run used candidate
`ee8dd6edda2a2e4dd8f3210504225a56432b11a0` and run directory:

```text
/tmp/ai-skills-051-bootstrap-20260907/.local-runtime/candidate-plugin-replay/runs/20260908T081523Z-1763498
```

Evidence from that run:

- `child.stdout.jsonl`: 24 parsed JSON lines, 111077 bytes;
- `child.stderr`: 0 bytes;
- candidate cache path hits included
  `skills/scientific-rewrite/SKILL.md` 3 times,
  `skills/zh/SKILL.md` 2 times, and `skills/fidelity/SKILL.md` 4 times;
- `workspace/outputs/stage_packets/route_selection.json`:
  `schema=SCIENTIFIC_REWRITE_ROUTE_SELECTION_V1`,
  `selector_owner=writing-style`,
  `selected_route=scientific-rewrite`,
  `forced_route=false`,
  `ordinary_user_prompt=true`;
- `workspace/outputs/stage_packets/stage_receipt.json`:
  `schema=SCIENTIFIC_REWRITE_HEAVY_ROUTE_RECEIPT_V2`,
  `runtime=scientific-rewrite.meaning-realization.v2`,
  `paid_generation_used=false`,
  `external_api_call_count=0`.

That run still exited with:

```text
ERROR: candidate actual consumption was not proven by parsed JSON event
```

The root cause was a harness parser false negative: the parser required JSON
events to contain the exact absolute `installedPath` prefix, while real
fresh-child command events contained the stable candidate cache suffix under a
different absolute prefix:

```text
/plugins/cache/ai-skills-candidate/writing-style/0.1/skills/...
```

The parser was repaired offline in
`a77aa87a370797fef9c6f83c608ca93016abe736` to:

- keep exact full `installedPath` matching as a fast path;
- extract stable
  `/plugins/cache/<marketplace>/<plugin>/<version>` from `installedPath`;
- accept only successfully parsed JSON events whose structure is
  `command_execution`;
- require command evidence under
  `/plugins/cache/ai-skills-candidate/writing-style/0.1/skills/` and pointing
  to `SKILL.md`;
- reject raw stdout substrings, ordinary assistant text, staged marketplace
  source paths, other marketplaces, or plugin-name-only evidence.

Offline parser regression against the existing failed run used diagnostic
`installedPath`:

```text
/diagnostic-prefix/plugins/cache/ai-skills-candidate/writing-style/0.1
```

It returned consumption evidence from `child.stdout.jsonl` line 4 with
`event_type=item.started`. No Codex process was run for this offline repair
validation.

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

Current parser/routing closure checks:

- `python3 -m unittest tests.test_candidate_plugin_replay -q`
  - PASS: 23 tests.
- Offline parser regression against
  `.local-runtime/candidate-plugin-replay/runs/20260908T081523Z-1763498/child.stdout.jsonl`
  with diagnostic installedPath
  `/diagnostic-prefix/plugins/cache/ai-skills-candidate/writing-style/0.1`
  - PASS: `line_index=4`, `event_type=item.started`.
- `git diff --check`
  - PASS.
- `python3 -m unittest discover -s tests -q`
  - PASS: 209 tests.
- `python3 scripts/skills.py validate`
  - PASS: validated 150 active skills, 18 profiles, templates, and trigger eval
    scaffolds.

Earlier implementation checks:

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

- Gate 2 is closed as product behavior PASS with the harness false negative
  repaired offline.
- The final parser repair was not followed by another Gate 2 replay, by explicit
  user instruction.
- Gates for known A/B/C regression, full private report, fresh holdout, Text
  Review, final CI, version/changelog, Reviewer PASS, and integration are not
  started.
