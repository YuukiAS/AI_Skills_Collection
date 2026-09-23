# ai-skills-core Changelog

## Unreleased

No unreleased changes.

## 0.5 - 2026-09-23

Before:

- AI Skills Maintainer could maintain AI_Skills_Collection releases and project profile installs, but a normal current-machine update still required the user or operator to know versions, refs, checkout paths, Marketplace details, Bridge location, and companion routing.
- Bridge Kit distribution/version maintenance was not available through AI Skills Maintainer, and formal release scope expansion was not single-sourced in the Maintainer payload.

After:

- Added `machine-update-orchestrator` as the normal AI Skills Maintainer entry for short requests such as `update presentations`, `update workflow-core`, `update AI Skills`, `update Bridge Kit`, and `sync this machine`.
- Added `bridge-kit-maintainer` for Bridge Kit source/version/distribution maintenance, formal Bridge `release` channel ownership, editable package refresh, runtime path/version verification, and delegation back to canonical `ai-bridge` commands.
- Added formal release and `### Update impact` routing references so cross-layer mutation scope comes from the formal release ref and matching root changelog entry, with isolated-by-default behavior.
- Added Route A/B/C references for isolated AI_Skills updates, formal cross-layer composition, and Bridge Kit distribution/runtime update.
- Added legacy AI_Skills Marketplace `main -> release` bootstrap, fresh-session truthfulness, selective managed-consumer adaptation, dirty/source safety, Human Gate, recovery, and should-not-change contracts.

Repository bump decision: MINOR
Reason: after repository `5.1.0` was assigned to Project Thread Handoff, AI_Skills_Collection gains the next repository-level user capability in `5.2.0`: one short Maintainer request can discover and synchronize the current machine's participating AI Research Stack, including Bridge Kit distribution and selective managed adaptation, without user-supplied versions, paths, components or templates.

Affected plugins:
- `ai-skills-core`: `0.4` -> `0.5`
  Reason: new current-machine update orchestration and Bridge Kit maintenance capability.
- `workflow-core`: NO_BUMP
  Reason: existing delivery semantics are consumed unchanged.
- domain plugins: NO_BUMP
  Reason: no domain production behavior changes.

## 0.4 - 2026-09-22

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

## 0.3 - 2026-09-20

Before:

- Central plugin maintenance checked source authority, generated parity, replay, regression, versions, and changelogs, but did not explicitly own gate lifecycle decisions.
- New real failures could still be tempting to encode as duplicate gates or same-meaning TODO rules.
- Task identity guidance did not explicitly separate semantic machine keys from human-readable labels and UI titles.

After:

- `ai-skills-core` now requires production regressions to map to existing capability gates unless a distinct capability, evidence type, failure semantics, normal entry, or owner boundary justifies a split/new gate.
- Gate split, merge, and retirement require historical regression and should-not-change coverage to be preserved in the Plan, RESULT, TODO, changelog, or tests.
- Release checks run cheap deterministic regression banks first, require isolation arguments for narrow gates, and escalate shared runtime/schema/generator, routing/default prompt, Marketplace/profile, artifact review, credential/paid transport, or cross-plugin user-visible changes to broad/full gates.
- Maintainer guidance now treats Bridge / Reviewed Handoff task keys as semantic technical locators and keeps human labels, thread titles, sidebar titles, and plugin display names separate.

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
