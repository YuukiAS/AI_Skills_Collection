# Clear Writing Cross-Surface Language Layer - Implementation Evidence

Task: `clear-writing--cross-surface-language-layer`
Branch: `reviewed/clear-writing--cross-surface-language-layer`
Frozen executor base: `7231343c47b8af029258aaaa96f332af09c8ae56`
Approved v0.3 package: `b960ec57941fc058a22ca8896c92d5dc19191009`
Execution Critic PASS: `0f8ee7d98ba8890d074b488c87cb65c20cd8b82f`

## Implemented Scope

- Added `skills/writing/core/response-clarity/` as a sixth Clear Writing source skill for ordinary user-facing explanations, diagnostics, advice, progress updates, and task-result summaries.
- Preserved the existing five source skill names and artifact ids: `fidelity`, `sci`, `product-ui-copy`, `scientific-rewrite`, and `zh`.
- Narrowed `chinese-prose` only at the trigger boundary: formal Chinese documents, README files, reports, Markdown/PDF final passes, and Chinese document polishing remain there; ordinary reply explanations route to `response-clarity`.
- Updated the single `writing-style` Marketplace source entry and regenerated `.agents/plugins/marketplace.json` plus `plugins/codex/plugins/` with the existing generator.
- Updated `profiles/codex-writing-style.json` so the curated Codex profile can install `response-clarity` and the already-released `product-ui-copy` sibling route.

Research Authoring, PIE 0.2, Frontend Design source, Presentations source, Bridge Kit, repository version, plugin version, changelog, and README were not modified.

## Generated Identity

`python scripts/build_codex_marketplace.py --write --validate --check --path-report` was run after adding `response-clarity`. It regenerated the full layer successfully, but the full diff also removed unrelated preexisting generated payload from `presentations` and `research-writing`. Those non-task changes were restored to keep the frozen scope intact.

Final committed candidate validation:

`python scripts/build_codex_marketplace.py --validate --path-report`

- result: PASS
- plugins: 10
- active skills: 30
- Windows path budget: PASS, max file length 120 / 140

Known full-generation drift not committed:

- `python scripts/build_codex_marketplace.py --validate --check --path-report` reports 16 non-`writing-style` differences under `plugins/codex/plugins/presentations` and `plugins/codex/plugins/research-writing`.
- The drift is outside the approved task scope. Committing it would modify generated Presentations and Research Authoring payloads even though those areas are frozen for this task.

Generated `writing-style` skills:

- `plugins/codex/plugins/writing-style/skills/fidelity/SKILL.md`
- `plugins/codex/plugins/writing-style/skills/response-clarity/SKILL.md`
- `plugins/codex/plugins/writing-style/skills/sci/SKILL.md`
- `plugins/codex/plugins/writing-style/skills/product-ui-copy/SKILL.md`
- `plugins/codex/plugins/writing-style/skills/scientific-rewrite/SKILL.md`
- `plugins/codex/plugins/writing-style/skills/zh/SKILL.md`

The source and generated `response-clarity/SKILL.md` hashes match:

```text
142b49b8b89f89701a10e55c36aafae8d010478ce7885774a7b6ff9efcac8f67  skills/writing/core/response-clarity/SKILL.md
142b49b8b89f89701a10e55c36aafae8d010478ce7885774a7b6ff9efcac8f67  plugins/codex/plugins/writing-style/skills/response-clarity/SKILL.md
```

## Test Results

PASS:

- `python scripts/skills.py validate`
- `python scripts/build_codex_marketplace.py --validate --path-report`
- `python -m unittest tests.test_skill_runtime_text_audit tests.test_product_ui_copy_cross_plugin.ProductUiCopyCrossPluginTests.test_marketplace_source_exposes_product_ui_copy_with_release_bump tests.test_codex_marketplace.CodexMarketplaceTests.test_writing_style_exposes_response_clarity_without_renaming_existing_skills tests.test_codex_marketplace.CodexMarketplaceTests.test_repository_config_has_marketplace_plugin_set tests.test_codex_marketplace.CodexMarketplaceTests.test_current_repository_marketplace_paths_fit_windows_budget tests.test_codex_marketplace.CodexMarketplaceTests.test_manifest_is_generated_at_repository_root tests.test_scientific_rewrite.ScientificRewriteHeavyRouteTests.test_writing_style_surface_keeps_existing_scientific_prose_route tests.test_scientific_rewrite.ScientificRewriteHeavyRouteTests.test_routing_text_sends_structural_scientific_rewrite_to_heavy_route tests.test_research_writing_routing`

Environment note:

- `python -m pytest ...` could not run because the active Python environment has no `pytest` module.

Known unrelated failure when running the broader selected `unittest` files together:

- `tests.test_codex_marketplace.CodexMarketplaceTests.test_central_plugins_have_exactly_one_source_only_todo_inbox`
- `tests.test_codex_marketplace.CodexMarketplaceTests.test_plugin_changelogs_match_marketplace_set_and_versions`

Both failures preexist this implementation scope and come from extra `docs/plugin-todos/*.md` workflow TODO files not represented in `CENTRAL_PLUGIN_NAMES`. They are not caused by `response-clarity`, Marketplace generation, profile updates, or the writing-style skill changes.

## G0-G7 Status

- G0 source/generated identity: PARTIAL PASS for Codex source and generated payload. ChatGPT personal Plugin Creator installation was not performed because account mutation remains a separate permission boundary.
- G1 normal entry and candidate increment: NOT CLAIMED. The implemented skill has trigger tests and generated payload identity, but A/E and B/C ChatGPT matched comparisons require a real authorized personal plugin candidate and controlled Project conditions. Current status is pending human/GPT account-side execution, not product PASS.
- G2 natural target-language first replies: covered by the `response-clarity` source contract and trigger examples; real full-answer human review remains a later artifact gate.
- G3 fidelity and machine strings: covered by `response-clarity` independent protection rules and unchanged `writing-fidelity`; real proposition-level review remains a later artifact gate.
- G4 existing writing skills: preserved names and artifact ids; targeted regression passed for Chinese document routing, product UI copy, scientific rewrite, scientific prose, and Research Authoring boundary.
- G5 Frontend Design and Presentations consumers: source integrations were not changed. Existing Product UI Copy and Presentations routes remain available in generated payload; full rendered artifact review remains a later gate.
- G6 long-session and language-mode behavior: not claimed from local static tests. The new skill explicitly preserves current-message language override and pure-machine negative cases; real multi-turn ChatGPT checks remain later.
- G7 final candidate unseen evaluation: not reached. This commit is an implementation candidate for CI/Reviewer, not a final product PASS.

Conclusion: the task-owned source and Codex generated candidate are ready for CI and independent review. Product-level G1/G7 claims must wait for the authorized personal ChatGPT candidate and full artifact review.
