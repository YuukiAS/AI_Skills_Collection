# ai-skills-core — Long-Term TODO

Canonical maintenance inbox for the `ai-skills-core` plugin and repository-maintenance product surface.

## Open candidates

### Establish repository 5.0 release epoch with independent plugin versions and changelogs
status: PROMOTE_NOW
source: long-term real-world maintenance redesign + user requirement on 2026-08-30
evidence: `docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md`; current Marketplace config already has per-plugin version fields, but 4.x history still reflects lockstep release semantics and root CHANGELOG remains the only release history
target layer: distribution
problem: repository release、plugin release 和 capability status 仍容易混淆；长期 lockstep 会掩盖到底哪个 plugin 真正变化，也无法自然支撑真实项目持续 refinement。
candidate action: publish the repository-level maintenance epoch as `5.0.0`; add one repository-version source of truth; start all ten central plugins at independent two-part version `0.1`; create `docs/plugin-changelogs/<plugin>.md` for all ten central plugins; make root CHANGELOG the repository release homepage and show plugin version/status/changelog links in README.
promotion gate: version/changelog/README/generated-payload consistency tests + real install/upgrade smoke; maintenance changelogs remain source-only; plugin versions use two-part numbers such as `0.1`, not three-part package SemVer.

### Make README a compact release dashboard without becoming source of truth
status: PROMOTE_NOW
source: user requirement on 2026-08-30
evidence: current README shows repository release and plugin entrypoints but not independent plugin version history
target layer: distribution
problem: after plugin versions diverge, users need one place to see repository release, each plugin version, capability status and changelog without opening config files.
candidate action: render/maintain a compact `Plugin | Version | Status | Main entry | Changelog` table whose values are checked against Marketplace config and `docs/PLUGIN_MATURITY.md`; root CHANGELOG links the plugin-changelog index.
promotion gate: README consistency regression and generated plugin install smoke; no duplicate hand-maintained version source.

## Recently promoted / established

### Repository release version consistency
status: PROMOTED
source: 4.4.2 baseline stabilization
evidence: `CHANGELOG.md` 4.4.2, `setup.py`, `registry.json`, Marketplace config, README and generated plugin metadata were aligned under the old lockstep model.

### Release version is separate from capability status
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
- Do not turn capability status into another package version.
- Do not bump all ten plugin versions after `0.1` merely because the repository publishes another release.
- Do not use three-part plugin versions such as `0.1.0`.
- Do not fabricate detailed per-plugin changelog history before repository `5.0.0`; earlier `4.x` values were legacy lockstep metadata.
