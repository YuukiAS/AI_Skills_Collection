# ai-skills-core — Long-Term TODO

Canonical maintenance inbox for the `ai-skills-core` plugin and repository-maintenance product surface.

## Open candidates

### Make repo-local recording guidance travel with future project installs
status: PROMOTE_NOW
source: user requirement on 2026-08-31 after TRACE / Presentation real-workflow setup
evidence: root `README.md` and `AGENTS.md` now define the rule; TRACE has the same rule in its own `AGENTS.md`; however arbitrary existing/future project repos do not automatically inherit it unless their own repo guidance is updated
target layer: distribution / repo-local install guidance
problem: a user can say “记录 repo 并保存到合适的地方” in any project thread, but a repo that has not been taught this convention may not know to keep project-specific work in the project repo and only leave a short AI_Skills feedback note for possible plugin problems.
candidate action: make future repo-local AI_Skills installation/update with `--write-agents-md` carry a short generic recording rule into the managed AGENTS block: use the project's existing TODO/ROADMAP/result/review/decision files first; do not create a second TODO system; when real plugin behavior is the problem, leave a short AI_Skills feedback handoff in the same project record for later central triage.
boundary: do not force every repository to use `results/<task_key>/result.md` or any single directory layout; respect each project's existing structure. Do not write raw project science directly into central plugin TODOs.
promotion gate: installer/AGENTS regression proves a newly installed test repo receives the generic rule without overwriting user-owned AGENTS content; one unrelated repo-local install/update smoke passes.

## Recently promoted / established

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
