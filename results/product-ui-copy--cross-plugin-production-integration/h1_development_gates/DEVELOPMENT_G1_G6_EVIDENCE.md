# H1 Development G1-G6 Evidence

Task key: `product-ui-copy--cross-plugin-production-integration`

Development candidate commit:

```text
53d42f621864a779f93de7e8a81007ef73ed55cc
```

This file records H1 development evidence only. It is not the release-critical
H2 PASS. The versioned H2 candidate must rerun G1-G6 after version bump and
regeneration.

## G1 Discovery / Activation / Packaging

PASS in development.

Commands:

```text
python scripts/skills.py validate
python scripts/skills.py audit --all
python scripts/build_codex_marketplace.py --validate --check --path-report
python -m unittest tests.test_product_ui_copy_cross_plugin tests.test_candidate_plugin_replay tests.test_skill_runtime_text_audit tests.test_frontend_design_production_consolidation tests.test_codex_marketplace
```

Observed:

- `validated 154 active skills, 18 profiles, templates, and trigger eval scaffolds`
- Marketplace validation/path report PASS: `plugins=10 active_skills=29 ... over_budget=0`
- Focused tests: `Ran 88 tests ... OK`

## G2 Ownership / Handoff / Protected Meaning

PASS in development.

Evidence:

- `skills/writing/core/product-ui-copy/SKILL.md`
- `skills/writing/core/writing-fidelity/SKILL.md`
- `tests/test_product_ui_copy_cross_plugin.py`

Covered:

- Required handoff fields.
- `KEEP`, `WORDING/NATURALNESS`, `LOCALE/REGISTER`, `CONTENT ARCHITECTURE`,
  `PRODUCT SEMANTICS`, `LEGAL/TRUST/SAFETY`.
- Product/legal/trust facts escalate instead of being cosmetically rewritten.

## G3 Naturalness / Locale / Page Rhythm

PASS in development as source/test evidence.

Evidence:

- `skills/writing/core/product-ui-copy/SKILL.md`
- `skills/writing/core/product-ui-copy/evals/trigger_queries.json`
- `results/product-ui-copy--cross-plugin-production-integration/candidate_replay/dev_same_session/SAME_SESSION_REPLAY_PASS.json`

Covered:

- `zh-Hans` / `zh-Hant-HK` must be independent realizations.
- Character conversion alone is rejected.
- Already-good copy may remain `KEEP`.

## G4 Rendered Acceptance

PASS in development for repo-safe browser-rendered fixture evidence.

Evidence:

- `results/product-ui-copy--cross-plugin-production-integration/rendered_acceptance/RENDERED_ACCEPTANCE.md`
- `results/product-ui-copy--cross-plugin-production-integration/rendered_acceptance/render-manifest.json`
- PNG captures:
  - `wide-desktop.png`
  - `narrow-mobile.png`
  - `trust-disclosure.png`
  - `keep-control.png`

Observed rendered dimensions:

- `wide-desktop.png`: 1440 x 1423
- `narrow-mobile.png`: 390 x 1840
- `trust-disclosure.png`: 920 x 1423
- `keep-control.png`: 760 x 1550

Boundary:

- This is browser-rendered representative fixture evidence only.
- It does not claim native desktop, browser-extension runtime, or Android/Compose
  execution.

## G5 Should-Not-Change Regression

PASS in development.

Commands:

```text
python -m unittest discover -s tests -p 'test_*.py'
```

Observed:

- First sandboxed run failed only because generated probe tests needed to write
  repository outputs in an exact worktree outside the sandbox writable root.
- Escalated exact-worktree rerun: `Ran 304 tests ... OK`.
- Rerun did not leave unrelated palette/presentation generated diffs.

Preserved:

- `chinese-prose` remains the long-form Chinese/document route.
- `scientific-rewrite` and existing writing routes remain covered by tests.
- Existing frontend coordinator behavior remains covered by
  `tests.test_frontend_design_production_consolidation`.
- Candidate replay helper single-plugin compatibility remains covered by
  `tests.test_candidate_plugin_replay`.

## G6 Same-Session Cross-Plugin Entry / Compatibility

PASS in development.

Evidence:

- `results/product-ui-copy--cross-plugin-production-integration/candidate_replay/dev_inputs/cross_plugin_replay_task.md`
- `results/product-ui-copy--cross-plugin-production-integration/candidate_replay/dev_inputs/compatibility_sources.md`
- `results/product-ui-copy--cross-plugin-production-integration/candidate_replay/dev_same_session/SAME_SESSION_REPLAY_PASS.json`

Observed by `scripts/candidate_plugin_replay.py replay`:

```json
{
  "candidate_commit": "53d42f621864a779f93de7e8a81007ef73ed55cc",
  "runtime_version": "codex-cli 0.153.4",
  "actual_consumption_by_plugin": {
    "web-development": {
      "proven": true,
      "event_type": "item.started",
      "line_index": 4
    },
    "writing-style": {
      "proven": true,
      "event_type": "item.started",
      "line_index": 4
    }
  }
}
```

Compatibility inputs covered:

- Generic Product UI Copy settings/deletion fixture.
- Lucerna desktop/native-WebView compact panel.
- Mica browser-extension popup.
- SeminarArc Compose UI positive case.
- SeminarArc Room/WorkManager/data-only negative case.

Boundary:

- Compatibility replay used read-only source snippets and did not modify
  Lucerna, Mica, or SeminarArc.
- Mica source was a temporary shallow clone at `/tmp/product-ui-copy-mica-readonly`
  and was not committed.
- Full replay stdout/stderr remain in `.local-runtime` and were not copied into
  repository results because stdout contains replay-expanded source and skill
  contents.
