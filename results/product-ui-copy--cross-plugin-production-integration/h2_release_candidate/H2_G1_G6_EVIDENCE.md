# H2 Release-Critical G1-G6 Evidence

Task key: `product-ui-copy--cross-plugin-production-integration`

Release candidate commit:

```text
a06ff050bc82bb22358dfcb3e4faa885fddd285b
```

This file records the versioned H2 release-critical rerun after repository and
plugin version bumps.

## Version Decisions

Repository bump decision: MINOR, `5.3.1` -> `5.4.0`.

Affected plugins:

- `web-development`: `0.3` -> `0.4`.
- `writing-style`: `0.3` -> `0.4`.
- all other central plugins: NO_BUMP.

Version evidence:

- `VERSION`: `5.4.0`.
- `registry.json`: `5.4.0`.
- `scripts/codex_marketplace_config.json`: `web-development 0.4`,
  `writing-style 0.4`, `presentations 0.3`.
- Generated plugin manifests: `web-development 0.4`, `writing-style 0.4`,
  `presentations 0.3`.

## G1 Discovery / Activation / Packaging

PASS on the release candidate.

Commands:

```text
python scripts/skills.py validate
python scripts/build_codex_marketplace.py --validate --check --path-report
```

Observed:

- `validated 154 active skills, 18 profiles, templates, and trigger eval scaffolds`
- Marketplace validation/path report PASS: `plugins=10 active_skills=29`,
  `source_snapshots=72`, `over_budget=0`.

## G2 Ownership / Handoff / Protected Meaning

PASS on the release candidate.

Evidence:

- `skills/writing/core/product-ui-copy/SKILL.md`
- `skills/writing/core/writing-fidelity/SKILL.md`
- `skills/tools/frontend/frontend-visual-systems/SKILL.md`
- `skills/tools/frontend/product-ux-planning/SKILL.md`
- `skills/tools/frontend/responsive-accessibility-review/SKILL.md`
- `tests/test_product_ui_copy_cross_plugin.py`

Covered:

- Frontend Design owns interface content architecture, placement, rendered
  acceptance, and viewport fit.
- Product UI Copy owns protected-meaning microcopy wording, locale/register,
  rhythm, and KEEP decisions.
- Product/legal/trust/safety facts must be escalated when missing or ambiguous.

## G3 Naturalness / Locale / Page Rhythm

PASS on the release candidate.

Evidence:

- `skills/writing/core/product-ui-copy/SKILL.md`
- `skills/writing/core/product-ui-copy/evals/trigger_queries.json`
- `results/product-ui-copy--cross-plugin-production-integration/h2_release_candidate/H2_SAME_SESSION_REPLAY_PASS.json`

Covered:

- `zh-Hans` and `zh-Hant-HK` are independent interface realizations from one
  protected meaning.
- Character conversion alone is rejected.
- Already-good copy may remain `KEEP`.

## G4 Rendered Acceptance

PASS on the release candidate by unchanged committed browser-rendered fixture
evidence.

Evidence:

- `results/product-ui-copy--cross-plugin-production-integration/rendered_acceptance/RENDERED_ACCEPTANCE.md`
- `results/product-ui-copy--cross-plugin-production-integration/rendered_acceptance/render-manifest.json`
- `wide-desktop.png`: 1440 x 1423
- `narrow-mobile.png`: 390 x 1840
- `trust-disclosure.png`: 920 x 1423
- `keep-control.png`: 760 x 1550

Boundary:

- This is browser-rendered representative fixture evidence only.
- It does not claim native desktop, browser-extension runtime, or Android/Compose
  execution.

## G5 Should-Not-Change Regression

PASS on the release candidate.

Commands:

```text
python -m unittest tests.test_product_ui_copy_cross_plugin tests.test_candidate_plugin_replay tests.test_skill_runtime_text_audit tests.test_frontend_design_production_consolidation tests.test_codex_marketplace tests.test_standalone_skill_baselines tests.test_central_plugin_icon_assets tests.test_scientific_rewrite
python -m unittest discover -s tests -p 'test_*.py'
```

Observed:

- Focused tests: `Ran 124 tests ... OK`.
- Full exact-worktree regression: `Ran 304 tests ... OK`.

Preserved:

- `chinese-prose` remains the long-form Chinese/document route.
- `scientific-rewrite` and existing writing routes remain covered.
- Existing frontend coordinator behavior remains covered.
- Candidate replay helper single-plugin compatibility remains covered.

## G6 Same-Session Cross-Plugin Entry / Compatibility

PASS on the release candidate.

Command:

```text
python scripts/candidate_plugin_replay.py replay --plugin web-development --plugin writing-style --candidate-commit a06ff050bc82bb22358dfcb3e4faa885fddd285b --task results/product-ui-copy--cross-plugin-production-integration/candidate_replay/dev_inputs/cross_plugin_replay_task.md --input results/product-ui-copy--cross-plugin-production-integration/candidate_replay/dev_inputs/compatibility_sources.md --input results/product-ui-copy--cross-plugin-production-integration/rendered_acceptance/product-ui-copy-fixture.html --input results/product-ui-copy--cross-plugin-production-integration/rendered_acceptance/product-ui-copy-fixture.css
```

Observed by `scripts/candidate_plugin_replay.py replay`:

```json
{
  "candidate_commit": "a06ff050bc82bb22358dfcb3e4faa885fddd285b",
  "runtime_version": "codex-cli 0.153.4",
  "actual_consumption_by_plugin": {
    "web-development": {
      "version": "0.4",
      "proven": true,
      "event_type": "item.started",
      "line_index": 4
    },
    "writing-style": {
      "version": "0.4",
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
- Full replay stdout/stderr remain in `.local-runtime` and were not copied into
  repository results because stdout contains replay-expanded source and skill
  contents.
