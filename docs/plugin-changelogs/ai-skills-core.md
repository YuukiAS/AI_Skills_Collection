# ai-skills-core Changelog

## Unreleased

- Changed the long-term feedback rule so problems caused by an AI_Skills plugin are recorded directly in that plugin's central `docs/plugin-todos/<plugin>.md`, instead of first creating a duplicate plugin-problem record in the project repo.
- Real project threads may add a minimal `status: NEW` item with the real failure and evidence; AI_Skills Planner/maintainer remains responsible for deduplication, abstraction, and deciding whether the issue should become a generic plugin change.
- Root `README.md`, `TODO.md`, `AGENTS.md`, the central TODO guide, continuous-refinement workflow, and Planner contract now explain the same rule.

No version bump yet; these changes remain unreleased until they are included in a formal plugin/repository release.

## 0.1 - 2026-08-30

- Introduced independent two-part plugin release version tracking for the central Marketplace plugins, starting at `0.1`.
- Added per-plugin changelogs and repository-level release workflow documentation.
- Added repository `VERSION` as the source for CLI package and registry release metadata.
- Made README/plugin release visibility explicit with plugin version, status, purpose, and changelog links.

Independent plugin versioning starts at `0.1` with AI_Skills_Collection repository `5.0.0`. Earlier `4.x` values were legacy lockstep release metadata; see the root `CHANGELOG.md` and Git history.
