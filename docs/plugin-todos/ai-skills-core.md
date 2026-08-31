# ai-skills-core — Long-Term TODO

Canonical maintenance inbox for the `ai-skills-core` plugin and repository-maintenance product surface.

## Open candidates

No active ai-skills-core implementation candidate is required for the feedback-location policy itself. The current rule is now documented in root `README.md`, root `TODO.md`, `AGENTS.md`, `docs/plugin-todos/README.md`, the continuous-refinement workflow, and the Planner contract.

## Recently promoted / established

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
