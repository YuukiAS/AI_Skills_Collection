# ai-skills-core Changelog

## Unreleased

No unreleased changes.

## 0.3 - 2026-09-18

Before:

- AI Skills Maintainer enforced source-first maintenance, generated parity,
  replay, regression and release closure, but an existing active rule could
  still fail in production without a mandatory consumer-path diagnosis first.

After:

- Added production-consumption diagnosis for active-rule regressions: inspect
  installed plugin identity/version, source/generated/Marketplace parity,
  normal invocation, trigger/routing, task entry, session loading and replay
  fidelity before adding another synonymous rule.
- Diagnoses classify failures as `missing_rule`, `not_loaded`, `stale_install`,
  `consumer_not_routed`, `unfaithful_test`, `execution_noncompliance`, or
  `capability_gap`.
- Source `SKILL.md` reading and generated parity are explicitly supporting
  evidence, not proof that the normal production entry consumed the behavior.

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
