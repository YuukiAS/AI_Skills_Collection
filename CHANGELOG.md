# Changelog

## Unreleased

- Changed the real-project feedback rule: problems caused by an AI_Skills plugin are now recorded directly in that plugin's central `docs/plugin-todos/<plugin>.md`, instead of first creating a duplicate plugin-problem record in the project repo.
- Real project threads may add a minimal `status: NEW` item containing the real failure and evidence; AI_Skills Planner/maintainer remains responsible for deduplication, abstraction, and deciding whether the item should become a generic plugin change.
- Rewrote the root README/TODO explanation in plain Chinese and aligned `AGENTS.md`, the TODO guide, continuous-refinement workflow, maintainer skill, Planner contract, and TRACE repo guidance with the same rule.
- Cleaned the Presentation TODO so the Stage-4 validator fix and existing-deck revision contract are no longer incorrectly listed as open work after they shipped in `presentations 0.1`; the file is now ready to receive new real-use `NEW` items from CAT-TRACE and other projects.

No repository or plugin version bump yet. These changes remain in `Unreleased` until they are included in a formal release.

## 5.0.0 - 2026-08-30

Repository `5.0.0` starts the long-term real-world refinement maintenance epoch. It establishes repository-level release tracking separately from individual plugin release versions, source-only per-plugin TODO inboxes, per-plugin changelogs, bounded Reviewed Handoff batch semantics, and README release visibility.

This is not a maturity declaration for every plugin. Capability status remains in `docs/PLUGIN_MATURITY.md`.

Plugin version baseline:

| Plugin | Previous legacy metadata | Current plugin version |
|---|---:|---:|
| `workflow-core` | `4.4.2` | `0.1` |
| `ai-skills-core` | `4.4.2` | `0.1` |
| `writing-style` | `4.4.2` | `0.1` |
| `research-writing` | `4.4.2` | `0.1` |
| `presentations` | `4.4.2` | `0.1` |
| `scientific-visualization` | `4.4.2` | `0.1` |
| `web-development` | `4.4.2` | `0.1` |
| `statistical-modeling` | `4.4.2` | `0.1` |
| `bioinformatics` | `4.4.2` | `0.1` |
| `medical-imaging` | `4.4.2` | `0.1` |

Changed repository behavior:

- Added root `VERSION` as the repository / CLI release source of truth for `setup.py`, registry generation, README, and this changelog.
- Added independent plugin changelogs under `docs/plugin-changelogs/`; each plugin starts at `0.1` with repository `5.0.0`, while earlier `4.x` values remain legacy lockstep metadata in this root changelog and Git history.
- Updated `docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md`, `docs/workflows/CONTINUOUS_REAL_WORLD_SKILL_REFINEMENT.md`, plugin TODO policy, README, and maintainer guidance for two-part plugin release versions.
- Generalized Presentation normal-production validation to check source/deck contract completeness without Stage-4 fixture storyline assumptions.
- Hardened the existing-deck revision contract so natural targeted refinement requests route to revision mode with accepted-element, reviewer-seen-baseline, page-scope, and render-comparison protections.

Plugin changelog index: `docs/plugin-changelogs/README.md`.

Affected plugin changelogs:

- `docs/plugin-changelogs/ai-skills-core.md`
- `docs/plugin-changelogs/presentations.md`

## 4.4.2 - 2026-08-30

- Established the long-term real-world plugin refinement structure: source-only per-plugin TODO inboxes, promotion gates, six-layer ownership, and bounded Reviewed Handoff batch semantics.
- Moved Presentation maintenance TODO/history files out of the active `research-presentations` runtime source into `docs/provenance/research-presentation-maintenance-archive-2026-08-30/`.
- Added a compact runtime Presentation guardrails reference for mature cross-project revision rules without packaging CAT-TRACE project history or maintenance inboxes into ordinary plugin installs.
- Documented the release-version versus capability-maturity split; `presentations` remains `alpha / Base v1`, and unreviewed plugin maturity stays unclassified rather than being marked stable.
- Aligned CLI package, registry, marketplace config, generated plugin metadata, and README release version on `4.4.2`.
- Added regressions for one TODO inbox per central plugin, maintenance payload hygiene, Presentation history separation, version consistency, maturity/SemVer separation, and source-to-generated parity.

## 4.4.1 - 2026-08-18

- Accepted the post-4.4.0 research-presentation hardening release after real PPTX rendering and independent scientific visual-review evidence passed.
- Added the metadata-only research presentation reference library source manifest, search matrix, page-level reference rows, and workflow documentation while keeping downloaded deck assets in ignored cache.
- Strengthened deck-plan validation with planning/final phases, structured Evidence Board items, and `source_evidence_ids` referential-integrity checks.
- Updated the research-group-meeting regression generator so it creates PPTX, evidence manifests, render status, and visual-review inputs without self-assigning final QA PASS.
- Synchronized central Marketplace plugin metadata and registry release version to `4.4.1`.

## 4.3.0 - 2026-08-16

- Restored and confirmed the 10-plugin Codex Marketplace baseline: `workflow-core`, `ai-skills-core`, `writing-style`, `research-writing`, `presentations`, `scientific-visualization`, `web-development`, `statistical-modeling`, `bioinformatics`, and `medical-imaging`.
- Clarified research-writing routing across manuscript drafting, whole-paper orchestration, reviewer-style risk review, fixed-dimension scholarly scoring, literature review, current-paper lookup, citation verification, and citation record management.
- Narrowed citation management to known papers, known identifiers, BibTeX, metadata repair, deduplication, and bibliography hygiene; topic-level paper discovery and recent-paper expansion now route to research lookup.
- Strengthened `writing-style`: `writing-fidelity` protects source facts and artifact identity, `chinese-prose` handles natural Chinese "说人话" final passes, and `scientific-prose` handles English scientific evidence prose without generic AI style.
- Refined `presentations` so explicit PPTX/PowerPoint/editable/Slides requests route to editable Presentation/Slides, explicit Beamer/LaTeX requests stay in Beamer/LaTeX, and unspecified desktop research/group-meeting slides default to editable decks.
- Added presentation completion gates for deck planning, artifact creation, render, visual QA, editability checks, and Chinese slide wording handoff through `writing-fidelity` plus `chinese-prose`.
- Added `ai-skills verify-server-installation` and `scripts/verify_server_installation.py` for server-local installation smoke checks without login, SSH, Codex App UI verification, or Slurm submission.
- The smoke check installs the selected profile/domain/skills into a temporary Codex home by default, validates installed `SKILL.md` frontmatter and icon references, validates the generated marketplace payload paths, and reports optional local tooling availability.
- Documented the server-local smoke gate in `README.md` and `docs/INSTALLATION.md`.
