# ai-skills-core — Long-Term TODO

Canonical maintenance inbox for the `ai-skills-core` plugin and repository-maintenance product surface.

## Open candidates

### Make release version source of truth consistent
status: PROMOTE_NOW
source: current main audit
evidence: README / registry / marketplace config report `4.4.1`, while `setup.py` still reports `4.4.0` and CHANGELOG latest formal section is `4.3.0`
target layer: distribution
problem: repository, CLI package, generated registry/marketplace and changelog can disagree about the installed release.
candidate action: choose one canonical release version source, synchronize package/config/generated layers through existing build scripts, and document the rule.
promotion gate: version-consistency regression + real install/upgrade smoke.

### Separate release SemVer from capability maturity
status: PROMOTE_NOW
source: long-term maintenance redesign
evidence: `docs/PLUGIN_MATURITY.md`
target layer: distribution
problem: a repo version such as `4.4.1` is currently easy to misread as meaning every plugin is mature/stable.
candidate action: keep SemVer for repository/Marketplace releases; maintain capability maturity separately and only promote it from real-task evidence.
promotion gate: docs/README/maintainer workflow agree; no new competing version scheme.

### Per-plugin TODO inboxes become the only central backlog entry
status: PROMOTE_NOW
source: current Presentation TODO sprawl
evidence: `docs/plugin-todos/`
target layer: distribution
problem: project TODOs can leak into active skill payload or be duplicated across plugins.
candidate action: route all long-term backlog to one source-only file per central plugin; detailed project evidence stays in provenance/project repo.
promotion gate: maintainer and Planner read the target plugin TODO before bounded refinement; generated marketplace payload excludes maintenance-only inboxes.

## Do not do

- Do not create new top-level plugins to organize TODOs.
- Do not hand-edit generated marketplace/plugin layers.
- Do not turn maturity labels into another package version.
