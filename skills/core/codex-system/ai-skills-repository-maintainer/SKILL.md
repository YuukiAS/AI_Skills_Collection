---
name: ai-skills-repository-maintainer
description: Maintain AI_Skills_Collection itself, including production plugin refinement contracts, source-first changes, generated parity, replay/regression gates, versions, changelogs, registry, catalog, marketplace, and profiles. Use only when the user is working on this repository or explicitly asks to maintain the central skill collection.
status: active
provenance: user-authored
trusted: false
requires_network: false
writes_files: true
executes_code: true
secrets_needed:
last_reviewed: 2026-08-30
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

## Plugin Refinement Companion Mode

Use this mode whenever the current task maintains `AI_Skills_Collection` and will change a formal central plugin's production behavior, including changes to:

- `skills/`;
- plugin routing;
- runtime references or shared runtime;
- QA or regression behavior;
- generator or production scripts;
- Marketplace payload;
- profile exposure.

This mode is mandatory for production plugin refinement. It is a maintenance companion, not a second workflow engine and not a domain expert.

The installed plugin should be presented to users as `AI Skills Maintainer`; keep the internal plugin slug `ai-skills-core` unless a task provides strong compatibility evidence for a slug migration. Normal maintenance combinations are:

- `AI Skills Maintainer` + `Presentations`;
- `AI Skills Maintainer` + `Writing Style`;
- `AI Skills Maintainer` + `Statistical Modeling`.

The target plugin decides what is professionally correct. This maintainer decides whether the change is source-authoritative, generated, replayed, regression-tested, versioned, changeloged, and closed.

Fixed flow:

1. Identify the target plugin.
2. Identify the domain owner plugin or official capability.
3. Read the target plugin TODO, target plugin changelog, active source skill/reference/runtime/QA, Marketplace config, and version policy.
4. Check whether the failure is an existing active-rule production regression, duplicate TODO, `PROJECT_LOCAL`, `CANDIDATE_GENERIC`, or already solved.
5. Freeze the maintenance boundary: what repository contract changes, what stays out of scope, and which existing layer owns the change.
6. Keep professional judgment with the domain owner.
7. Modify source authority first.
8. Regenerate the generated layer.
9. Install or reload the real production plugin when production behavior changed.
10. Replay the original real failure or a public-safe equivalent frozen by the task.
11. Run an unrelated regression for the target plugin or affected shared path.
12. Close or update the target plugin TODO.
13. Bump the affected plugin version exactly once when the completed release changes production behavior.
14. Update the affected plugin changelog with before -> after behavior.
15. Apply the repository release/version contract.
16. Validate source/generated/version/release parity before reporting completion.

`ai-skills-core` does not judge:

- PPT scientific quality or slide visual hierarchy;
- statistical correctness;
- medical imaging semantics;
- bioinformatics scientific workflow;
- prose scientific meaning.

Those decisions must be handled by the target domain plugin or official capability. For example, a `presentations` refinement uses `workflow-core` for process, `ai-skills-core` for maintenance closure, and `presentations` for slide/deck judgment.

Before editing plugin source in this mode, verify whether the current Codex identity has the production plugin installed and enabled. When a task requires production evidence, use `ai-bridge plugin-replay --plugin ai-skills-core@yuukias-ai-skills` or the exact plugin id reported by `codex plugin list`; reading this repository's source `SKILL.md` is useful context but is not proof of production invocation.

When the refinement is responding to a real artifact failure, keep the maintenance owner separate from artifact judgment:

- record whether the failure is a `PROCESS PASS` / process-control failure, `PRODUCT / ARTIFACT PASS` failure, or both;
- ensure the Reviewed Handoff Plan/Reviewer has a real repo-safe artifact path, render, or Bridge Kit Text Review evidence locator when acceptance depends on artifact quality;
- do not accept CI, schema, protected-span, or Executor summary success as product/artifact PASS;
- if the final artifact cannot be read or viewed, the review condition is `WAITING_FOR_EVIDENCE / NEEDS_REVIEW`, not PASS.

Private/text artifact review is owned by `GPT_Codex_AI_Bridge_Kit` Text Review. Do not implement another artifact transport or reviewer in `AI_Skills_Collection`; once Bridge Kit Text Review lands, consume its evidence and artifact identity in the maintainer/review contract.

Real regression case 044: a private `rewritten_report.md` was reported by the user to still contain reader-facing `provenance`, `estimand`, `scientific gap`, `resource contract`, and `state of the art` language that violated the frozen writing requirement, while review passed without reading the full artifact. Future maintenance of the same class must be blocked at the Reviewed Handoff artifact-aware review layer; this maintainer should route it there and should not rewrite the 044 scientific text.

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
- If a bounded production plugin refinement changes user-facing behavior or workflow, passes its original-failure replay and unrelated regression, and is ready for delivery, bump that plugin exactly once in the same task. Do not leave the completed behavior change as `Unreleased` with a deferred plugin version bump.
- A single plugin release normally causes a repository patch release, not a repository minor release.
- A plugin reaching `1.0` does not by itself cause a repository minor release.
- Baseline replay, TODO/provenance/maintenance-only docs, tests-only changes, or no-runtime-behavior changes do not bump plugin versions.
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
