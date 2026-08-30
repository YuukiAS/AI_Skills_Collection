# ai-skills-core — Long-Term TODO

Canonical maintenance inbox for the `ai-skills-core` plugin and repository-maintenance product surface.

## Open candidates

### Establish independent plugin SemVer and per-plugin changelogs
status: PROMOTE_NOW
source: long-term real-world maintenance redesign + user requirement on 2026-08-30
evidence: `docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md`; current `scripts/codex_marketplace_config.json` already carries one version per plugin, but all ten are still lockstep and root CHANGELOG is the only release history
target layer: distribution
problem: repository release, plugin release, and capability maturity are still too easy to conflate; lockstep plugin bumps obscure which capability actually changed and make long-term release history hard to audit.
candidate action: add one repository/CLI version source of truth, allow independent plugin SemVer from the existing marketplace config, create `docs/plugin-changelogs/<plugin>.md` for all ten central plugins, show plugin version + maturity in README, and add consistency regressions. Treat `4.4.2` as the common baseline and do not invent pre-baseline per-plugin history.
promotion gate: version/changelog/README/generated-payload consistency tests + real plugin install smoke; maintenance changelogs remain source-only.

## Recently promoted / established

### Repository release version consistency
status: PROMOTED
source: 4.4.2 baseline stabilization
evidence: `CHANGELOG.md` 4.4.2, `setup.py`, `registry.json`, `scripts/codex_marketplace_config.json`, README and generated plugin metadata are aligned on 4.4.2; regression exists in `tests/test_codex_marketplace.py`.

### Release SemVer is separate from capability maturity
status: PROMOTED
source: long-term maintenance redesign
evidence: `docs/PLUGIN_MATURITY.md`, `docs/workflows/CONTINUOUS_REAL_WORLD_SKILL_REFINEMENT.md`, README.

### One source-only TODO inbox per central plugin
status: PROMOTED
source: 4.4.2 maintenance consolidation
evidence: `docs/plugin-todos/` contains exactly one inbox for each central Marketplace plugin; regression protects set equality and generated payload exclusion.

## Do not do

- Do not create new top-level plugins to organize TODOs.
- Do not hand-edit generated marketplace/plugin layers.
- Do not turn maturity labels into another package version.
- Do not bump all ten plugin versions merely because the repository released a new patch.
- Do not fabricate detailed per-plugin changelog history before the 4.4.2 independent-tracking baseline.
