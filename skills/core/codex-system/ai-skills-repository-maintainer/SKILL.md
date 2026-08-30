---
name: ai-skills-repository-maintainer
description: Maintain AI_Skills_Collection itself: registry, catalog, provenance, marketplace config, generated layer, icons, profiles, and validation gates. Use only when the user is working on this repository or explicitly asks to maintain the central skill collection.
status: active
provenance: user-authored
trusted: false
requires_network: false
writes_files: true
executes_code: true
secrets_needed:
last_reviewed: 2026-07-13
profile_tags:
  - ai-skills-maintainer
recommended_scope: project
icon_small: assets/app-facing.svg
icon_large: assets/app-facing.svg
allow_implicit_invocation: false
---
# AI Skills Repository Maintainer

Use this skill only for maintaining `AI_Skills_Collection`. Do not use it for ordinary coding tasks in unrelated repositories.

## Boundary

- Maintain source skills, profiles, README, registry, catalog, provenance, icon metadata, and Codex App marketplace publication.
- Do not duplicate OpenAI system skills such as `skill-creator`, `skill-installer`, or `plugin-creator`.
- Do not use this as a domain skill. Frontend taste, PPT planning, bioinformatics retrieval, writing, and statistics live in their own plugins or official capabilities.
- Treat `.agents/plugins/marketplace.json` and `plugins/codex/plugins/` as generated output.
- Keep external source intake temporary, reviewed, and provenance-recorded.

## Workflow

1. Read `README.md`, `scripts/codex_marketplace_config.json`, `profiles/`, `docs/provenance/INTEGRATION_HISTORY.md`, any v3 intake table under `docs/provenance/`, and relevant tests.
2. For Notion or GitHub intake, record the evidence boundary first: source page or repo, readable text/images/attachments, public-source verification, processing decision, target skill/reference, integration commit, and whether the external tracker has already been reconciled.
3. Decide whether each item is `merged`, `partially-merged`, `reference-only`, `reviewed-not-adopted`, `unresolved-asset`, or `rejected`. Do not collapse several weak-evidence items into a single `merge-selected` claim.
4. Route domain judgment to the right domain plugin or official capability. This skill controls repository maintenance; it does not decide frontend taste, PPT content, bioinformatics workflows, statistics, or medical-imaging methods by itself.
5. Edit source files first: `skills/`, `profiles/`, `docs/provenance/`, tests, and public docs.
6. Regenerate derived registry/catalog/marketplace files only after source-layer changes are complete.
7. Run repository validation gates with the local runtime Python when `python` is not on `PATH`.
8. Commit after validation, then reconcile external trackers only if the user requested it. If the user has already updated Notion `Utilized`, do not call the Notion connector again.
9. Report generated-layer changes separately from source-layer changes.

## Continuous real-world refinement

When maintenance originates from a real project TODO, user artifact feedback, repeated production failure, or a request to improve an existing plugin over time, first read:

```text
docs/workflows/CONTINUOUS_REAL_WORLD_SKILL_REFINEMENT.md
docs/PLUGIN_MATURITY.md
docs/plugin-todos/README.md
docs/plugin-todos/<target-plugin>.md
```

Then apply these rules:

- Treat the plugin TODO as a source-only maintenance inbox, not runtime instructions.
- Keep detailed project-specific evidence in the project repo or `docs/provenance/`; only the abstract generic candidate belongs in the plugin TODO.
- Do not promote every TODO into `SKILL.md`. Freeze a promotion decision, target layer, boundary, real evidence, user-facing effect, and regression first.
- Prefer modifying an existing routing/reasoning/rendering/QA/writing/distribution layer over creating another skill/schema/state.
- After promotion, replay the original real failure and run an unrelated regression. Synthetic checks alone do not prove maturity.
- Reviewed Handoff refinement should be bounded and batch-based. Do not keep a watcher alive to invent new work after the real blocker is closed.
- Release SemVer and capability maturity are separate; do not change package versions merely to express alpha/beta/stable maturity.
- Maintenance-only TODO/provenance files must not be copied into generated user-facing plugin payload unless they are intentionally promoted runtime references.

## Validation

Run the narrowest useful checks first, then the full gate before delivery:

```bash
python scripts/skills.py registry --write
python scripts/skills.py validate
python scripts/skills.py audit --all
python scripts/skills.py catalog --write
python scripts/build_codex_marketplace.py --write --validate --check --path-report
python -m unittest discover -s tests
```
