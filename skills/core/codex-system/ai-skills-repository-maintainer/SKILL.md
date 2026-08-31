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
last_reviewed: 2026-08-31
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

- Maintain source skills, profiles, README, registry, catalog, provenance, icon metadata, version/changelog metadata, and Codex App marketplace publication.
- Do not duplicate OpenAI system skills such as `skill-creator`, `skill-installer`, or `plugin-creator`.
- Do not use this as a domain skill. Frontend taste, PPT planning, bioinformatics retrieval, writing, and statistics live in their own plugins or official capabilities.
- Treat `.agents/plugins/marketplace.json` and `plugins/codex/plugins/` as generated output.
- Keep external source intake temporary, reviewed, and provenance-recorded.

## Workflow

1. Read root `AGENTS.md`, `README.md`, `TODO.md`, `scripts/codex_marketplace_config.json`, `profiles/`, relevant workflow docs, and relevant tests.
2. For Notion or GitHub intake, record the evidence boundary first: source page or repo, readable text/images/attachments, public-source verification, processing decision, target skill/reference, integration commit, and whether the external tracker has already been reconciled.
3. Decide whether each external item is `merged`, `partially-merged`, `reference-only`, `reviewed-not-adopted`, `unresolved-asset`, or `rejected`. Do not collapse several weak-evidence items into a single `merge-selected` claim.
4. Route domain judgment to the right domain plugin or official capability. This skill controls repository maintenance; it does not decide frontend taste, PPT content, bioinformatics workflows, statistics, or medical-imaging methods by itself.
5. Edit source files first: `skills/`, `profiles/`, `docs/provenance/`, `docs/plugin-todos/`, `docs/plugin-changelogs/`, tests, and public docs.
6. Regenerate derived registry/catalog/marketplace files only after source-layer changes are complete.
7. Run repository validation gates with the local runtime Python when `python` is not on `PATH`.
8. Commit after validation, then reconcile external trackers only if the user requested it.
9. Report generated-layer changes separately from source-layer changes.

## Continuous real-world refinement

When maintenance comes from a real project using an AI_Skills plugin, first read:

```text
TODO.md
docs/workflows/CONTINUOUS_REAL_WORLD_SKILL_REFINEMENT.md
docs/PLUGIN_MATURITY.md
docs/plugin-todos/README.md
docs/plugin-todos/<target-plugin>.md
```

Apply these rules:

- Project-owned research/product/code work stays in the project repo.
- A problem caused by an AI_Skills plugin should be recorded directly in the corresponding central plugin TODO, not duplicated into the project repo as a plugin TODO.
- A real project thread may add a minimal `status: NEW` item directly to `docs/plugin-todos/<plugin>.md` with `source`, `evidence`, `problem`, and `project-specific context`.
- The project thread records the real failure; it does not decide the final generic rule or promotion status.
- Before triaging `NEW`, compare against the current plugin TODO and active skill/reference/QA/runtime. Merge duplicate evidence instead of creating near-duplicate rules.
- If an active rule already exists but real output still fails, treat it as a production regression and inspect the consumer/runtime rather than adding another synonymous rule.
- If the issue is only project-specific, mark `PROJECT_LOCAL` and do not promote it into active plugin behavior.
- Only the AI_Skills Planner/maintainer may turn a `NEW` item into `CANDIDATE_GENERIC`, `PROMOTE_NOW`, `SUPERSEDED`, or `REJECTED` after triage.
- Do not promote every TODO into `SKILL.md`. Freeze a promotion decision, target layer, boundary, real evidence, user-facing effect, and regression first.
- Prefer modifying an existing routing/reasoning/rendering/QA/writing/distribution layer over creating another skill/schema/state.
- After promotion, replay the original real failure and run an unrelated regression. Synthetic checks alone do not prove maturity.
- Reviewed Handoff refinement should be bounded and batch-based. Do not keep a watcher alive to invent new work after the real blocker is closed.
- Repository release version, two-part plugin release version, and capability maturity are separate; do not change package or plugin versions merely to express alpha/beta/stable maturity.
- Maintenance-only TODO/provenance files must not be copied into generated user-facing plugin payload unless they are intentionally promoted runtime references.

## Version and changelog discipline

Before changing any repository or plugin version, read:

```text
AGENTS.md
docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md
VERSION                         # when present after the 5.0 epoch
scripts/codex_marketplace_config.json
CHANGELOG.md
docs/plugin-changelogs/<target-plugin>.md
docs/plugin-todos/<target-plugin>.md
```

Do not infer a version bump from diff size, commit count, TODO count, test count, CI PASS, or maturity labels.

Mandatory rules:

- Repository / CLI uses three-part releases. Patch is the default compatible release; minor requires a new repository-level user capability; major requires a breaking repository contract.
- Individual plugins use independent two-part releases such as `0.1 -> 0.2 -> 0.3 -> 1.0`.
- Plugin version changes only when that plugin has a completed user-facing improvement batch with replay/regression/review evidence.
- A single plugin release normally causes a repository patch release, not a repository minor release.
- A plugin reaching `1.0` does not by itself cause a repository minor release.
- TODO/provenance/maintenance-only changes do not bump plugin versions.
- If the bump cannot be justified exactly under the canonical policy, choose `NO_BUMP` and return to Planner/user.

Every release plan/result must state:

```text
Repository bump decision: NONE | PATCH | MINOR | MAJOR
Reason: ...
Affected plugins:
- <plugin>: NO_BUMP | <old> -> <new>
  Reason: ...
```

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

For a formal release, also require relevant install/upgrade smoke, version/changelog/README consistency, generated-layer parity, and required GitHub CI.
