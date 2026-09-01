# ai-skills-core — Long-Term TODO

Canonical maintenance inbox for the `ai-skills-core` plugin and repository-maintenance product surface.

## Open candidates

No active ai-skills-core implementation candidate is open after `ai-skills-core 0.2`. Future production refinement feedback should enter this inbox as `NEW` evidence before promotion.

## Recently promoted / established

### AI_Skills production refinement maintenance companion
status: PROMOTED
source: user requirement on 2026-09-01 for task 046
evidence: `ai-skills-core 0.2`, repository `5.0.1`, Marketplace `ai-skills-core` includes `project-skill-installer`, `ai-skills-repository-maintainer`, and `skill-library-analysis`; AGENTS, Reviewed Handoff Planner/Executor/Reviewer prompts, version policy, tests, and generated payload align.
target layer: distribution / maintenance workflow
problem: central plugin refinements could previously change production behavior while bypassing `ai-skills-core`, omit explicit maintenance/domain ownership, treat source `SKILL.md` reading as production invocation evidence, or deliver completed production behavior changes without same-task plugin version/changelog closure.
current behavior: any production central-plugin refinement must use `workflow-core` for process, `ai-skills-core` as maintenance companion, and the target domain plugin for professional judgment. The user-facing display name is `AI Skills Maintainer`, while the compatibility slug remains `ai-skills-core`. `ai-skills-core` enforces source-first edits, TODO/duplicate triage, generated parity, production replay, unrelated regression, version/changelog, and repository release closure, without becoming a domain expert or a second workflow/state/schema.
boundary: do not set global implicit invocation to true, do not create a new top-level plugin, do not copy `codex-workflow-protocol` into `ai-skills-core`, and do not modify domain plugin behavior from this maintenance layer alone.

### Artifact-aware Reviewed Handoff product pass
status: PROMOTED
source: user-reported task 044 regression on 2026-09-01
evidence: user reported that private `rewritten_report.md` still contained reader-facing `provenance`, `estimand`, `scientific gap`, `resource contract`, and `state of the art` language despite the frozen writing requirement; Reviewer did not read the full artifact before PASS. The same maintenance report also identified non-visual Visual Review PASS UI and missing default branch integration closure.
target layer: Reviewed Handoff prompts / visual-review consumer workflow / maintenance closure
problem: process gates and summaries were treated as enough to imply product/artifact quality, obvious frozen writing violations could be pushed to human judgment, non-visual tasks could display Visual Review PASS, and task branches lacked a default integration closure after Reviewer PASS.
current behavior: artifact-dependent acceptance must distinguish `PROCESS PASS` from `PRODUCT / ARTIFACT PASS`; Reviewer must read/view the final repo-safe artifact, or consume Bridge Kit Text Review evidence after that owner lands private/text artifact review. Missing artifact access is `WAITING_FOR_EVIDENCE / NEEDS_REVIEW`, not PASS. Obvious frozen-criteria violations must be REVISE/BLOCK, not human-gated. Non-visual tasks skip the real Visual Review job as `SKIPPED / NOT_REQUIRED`. Reviewer PASS without a real human gate proceeds to integration preflight, merge to `main`, push, and task-branch deletion unless an escalation condition applies.
boundary: do not modify the private 044 scientific text in this maintenance task; do not implement another private/text artifact transport or reviewer in AI_Skills_Collection; route domain writing quality to `writing-style` and bottom-layer private/text artifact review to `GPT_Codex_AI_Bridge_Kit` Text Review.

### Direct plugin-use feedback to the central plugin TODO
status: PROMOTED
source: user correction on 2026-08-31 after TRACE / Presentation real-workflow setup
evidence: root `README.md`, root `TODO.md`, `AGENTS.md`, `docs/plugin-todos/README.md`, `docs/workflows/CONTINUOUS_REAL_WORLD_SKILL_REFINEMENT.md`, Planner contract; TRACE `AGENTS.md` follows the same rule
target layer: distribution / maintenance workflow
problem: keeping Presentation/plugin problems first in TRACE or another project repo mixes plugin maintenance with the project's own scientific TODOs and creates duplicate records.
current behavior: project-owned research/product/code issues stay in the project repo; issues caused by an AI_Skills plugin are written directly to the corresponding central `docs/plugin-todos/<plugin>.md` as `status: NEW`. The project thread records the real failure and project-specific context; AI_Skills Planner/maintainer later deduplicates, abstracts, and decides whether the item is project-local, a generic candidate, or ready for implementation.
boundary: do not move project science, model choices, dataset interpretation, or project code TODOs into AI_Skills_Collection. Do not require project threads to invent a generic rule before recording a plugin failure.

### Repository 5.0 release epoch with independent plugin versions and changelogs
status: PROMOTED
source: long-term real-world maintenance redesign + user requirement on 2026-08-30
evidence: repository `5.0.0`, root `VERSION`, per-plugin `0.1` versions, root `CHANGELOG.md`, `docs/plugin-changelogs/`, README status table, install smoke and GitHub Actions.

### README release dashboard
status: PROMOTED
source: user requirement on 2026-08-30
evidence: README shows repository release, each central plugin version/status and changelog link; consistency is covered by repository tests.

### Legacy repository release consistency
status: PROMOTED
source: 4.4.2 baseline stabilization
evidence: `CHANGELOG.md` 4.4.2, `setup.py`, `registry.json`, Marketplace config, README and generated plugin metadata were aligned under the old lockstep model.

### Repository release is separate from capability status
status: PROMOTED
source: long-term maintenance redesign
evidence: `AGENTS.md`, `docs/PLUGIN_MATURITY.md`, `docs/workflows/CONTINUOUS_REAL_WORLD_SKILL_REFINEMENT.md`, README.

### One source-only TODO inbox per central plugin
status: PROMOTED
source: 4.4.2 maintenance consolidation
evidence: `docs/plugin-todos/` contains exactly one inbox for each central Marketplace plugin; regression protects set equality and generated payload exclusion.

## Do not do

- Do not create new top-level plugins to organize TODOs.
- Do not hand-edit generated marketplace/plugin layers.
- Do not turn capability status into another package version.
- Do not bump all ten plugin versions merely because the repository publishes a later patch/minor release.
- Do not restore the legacy rule that every plugin must share the repository version.
- Do not fabricate detailed per-plugin changelog history before repository 5.0.0; preserve earlier history in root CHANGELOG / Git history.
- Do not use three-part plugin versions such as `0.1.0`.
- Do not recreate the superseded “project repo first, central TODO later” plugin-feedback workflow.
