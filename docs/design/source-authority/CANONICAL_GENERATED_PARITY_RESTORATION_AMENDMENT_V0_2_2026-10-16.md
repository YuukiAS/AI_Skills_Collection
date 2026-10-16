# Canonical Generated Parity Restoration — Planner Amendment v0.2

Date: 2026-10-16
Status: PLANNER_AMENDMENT_AFTER_EXECUTION_EVIDENCE
Supersedes only the v0.1 byte-identity rule where explicitly stated.

## New evidence

The first execution proved that source-first restoration can make the official generator clean and preserve the two generated plugin trees, but full tests exposed four remaining failures.

Three failures are stale repository-test assumptions already identified by the Clear Writing recovery:

1. `tests/test_central_plugin_icon_assets.py` hard-codes repository `VERSION == 5.5.0` although current canonical repository version is `5.4.4`; repository-version consistency is already tested elsewhere.
2. `tests/test_codex_marketplace.py::test_central_plugins_have_exactly_one_source_only_todo_inbox` incorrectly requires every Markdown file in `docs/plugin-todos/` to be one of the ten central plugins, even though the repository intentionally contains workflow-specific TODO notes.
3. `tests/test_codex_marketplace.py::test_plugin_changelogs_match_marketplace_set_and_versions` repeats the same invalid exact-set assumption for `docs/plugin-todos/`.

The fourth failure is different and must NOT be fixed by weakening the test:

- `tests/test_presentations.py::test_research_presentation_todo_consolidation_and_promotions` requires the canonical research-presentation source skill to preserve `accepted_element_ledger`.
- Current main canonical source contains that guard.
- Current generated research wrapper contains newer October 6–7 workflow hardening but lost the exact older `accepted_element_ledger` clause.
- Therefore the v0.1 assumption that the current generated wrapper was a complete preservation target was too strong. The correct authority is the semantic union of already-accepted canonical source behavior and already-accepted generated-only October hardening.

## Revised authority rule

For Presentations shared runtime contracts and Research Writing shared contracts, keep the v0.1 byte-identical generated preservation invariant.

For the two Presentations wrapper SKILL files only:

- canonical source is the primary source authority;
- preserve every pre-repair canonical-source semantic guard;
- merge in the already-accepted generated-only October hardening;
- regenerate from that merged canonical source;
- generated wrapper bytes are allowed to change only to restore source-preserved semantics that were missing from the generated wrapper;
- do not remove any existing generated-only hardening.

In particular, the research wrapper must retain the `accepted_element_ledger` revision guard while also retaining the newer runbook, cumulative-acceptance, anti-shortcut, independent-validation and monotone-convergence requirements.

## Exact allowed test repairs

### Repository version assertion

In `tests/test_central_plugin_icon_assets.py`, remove the unrelated hard-coded `VERSION == 5.5.0` assertion from the icon/plugin-version test. Do not change `VERSION`.

Repository-version consistency remains covered by the dedicated release/version consistency tests that compare `VERSION`, setup/registry/README and SemVer policy.

### Plugin TODO inventory assertions

In `tests/test_codex_marketplace.py`:

- keep the assertion that Marketplace plugin names equal `CENTRAL_PLUGIN_NAMES`;
- require that every central plugin has its canonical `docs/plugin-todos/<plugin>.md` file;
- allow additional workflow/domain-specific Markdown notes in `docs/plugin-todos/`;
- in the changelog test, keep `docs/plugin-changelogs/` exact to the central plugin set, but change the TODO check from exact equality to central-plugin subset coverage.

Do not delete or rename valid workflow TODO files to satisfy the old assertion.

## Revised generated-diff invariant

After official regeneration:

- all pre-existing generated files remain byte-identical except the Presentations `skills/research/SKILL.md` and, only if required by source reconciliation, `skills/business/SKILL.md`;
- any changed wrapper line must map to a pre-existing canonical-source semantic guard or a pre-existing generated-only October hardening; no new product rule is allowed;
- Presentations shared generated contracts remain byte-identical;
- Research Writing generated plugin tree remains byte-identical;
- the generated Marketplace snapshot may change mechanically to reflect the new Research Writing shared mapping;
- a second generator check must be clean/idempotent.

## Completion

After applying this amendment, rerun focused tests, full repository tests, generator clean/idempotence, generated-tree diff audit and `git diff --check`.

If full tests reveal a new semantic conflict outside these four known failures, stop and report it. Otherwise commit/push and integrate the repair branch to main as already authorized by v0.1.