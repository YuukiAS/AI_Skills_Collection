# ai-skills-core Changelog

## Unreleased

No unreleased changes.

## 0.2 - 2026-09-01

Before:

- `ai-skills-core` mainly exposed installation and repository-maintenance utilities.
- Production plugin refinement could bypass `ai-skills-core` and rely only on the target domain plugin plus general workflow instructions.

After:

- Every production central-plugin refinement must use `ai-skills-core` as the explicit maintenance companion while the target domain plugin remains the professional owner.
- The user-facing display name is now `AI Skills Maintainer`; the internal plugin slug remains `ai-skills-core` to avoid unnecessary installation, profile, Marketplace, and history migrations.
- `skill-library-analysis` is now included in the `ai-skills-core` Marketplace plugin for overlap, duplicate, trigger-boundary, merge-vs-extend, and skill/plugin/profile boundary decisions.
- Maintenance closure now explicitly covers source authority, TODO/duplicate triage, generated parity, production replay, unrelated regression, version/changelog decisions, and repository release closure.
- Artifact-dependent acceptance now distinguishes `PROCESS PASS` from `PRODUCT / ARTIFACT PASS`: Reviewer must read/view the final artifact, and private/text artifacts are routed to the future Bridge Kit Text Review owner instead of being reimplemented in AI_Skills.
- Task 044 is recorded as the real regression case: a private `rewritten_report.md` was reported to still contain reader-facing `provenance`, `estimand`, `scientific gap`, `resource contract`, and `state of the art` language while review passed without reading the full artifact.
- Non-visual Reviewed Handoff tasks should leave the real Visual Review job `SKIPPED / NOT_REQUIRED` instead of presenting skipped model work as a Visual Review PASS.
- Reviewer PASS without a real human gate now routes to default integration closure: preflight, merge back to `main`, push, and delete the task branch unless an escalation condition applies.
- Production invocation is required when a task asks for plugin replay; reading a source-tree `SKILL.md` is not proof that the installed production plugin was used.
- The real-project feedback rule is included: problems caused by an AI_Skills plugin are recorded directly in that plugin's central `docs/plugin-todos/<plugin>.md`, with AI_Skills Planner/maintainer responsible for deduplication and abstraction.

## 0.1 - 2026-08-30

- Introduced independent two-part plugin release version tracking for the central Marketplace plugins, starting at `0.1`.
- Added per-plugin changelogs and repository-level release workflow documentation.
- Added repository `VERSION` as the source for CLI package and registry release metadata.
- Made README/plugin release visibility explicit with plugin version, status, purpose, and changelog links.

Independent plugin versioning starts at `0.1` with AI_Skills_Collection repository `5.0.0`. Earlier `4.x` values were legacy lockstep release metadata; see the root `CHANGELOG.md` and Git history.
