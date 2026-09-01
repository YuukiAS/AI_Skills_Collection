# Changelog

## Unreleased

No unreleased changes.

## 5.0.3 - 2026-09-01

Repository `5.0.3` is a compatible release for YuukiAS/TRACE render-resource routing hardening.

Repository bump decision: PATCH
Reason: this release improves an existing central plugin's production render-routing behavior without adding a new repository-level capability or breaking existing contracts.

Affected plugin versions:

| Plugin | Previous | Current |
|---|---:|---:|
| `presentations` | `0.2` | `0.3` |

Affected plugins:
- `presentations`: `0.2` -> `0.3`
  Reason: Beamer/PDF presentation routing now preserves the current YuukiAS workstation render-resource path and reports missing local resources explicitly instead of substituting retired server-only paths.

Unchanged plugin versions: `workflow-core 0.1`, `ai-skills-core 0.2`, `writing-style 0.1`, `research-writing 0.1`, `scientific-visualization 0.1`, `web-development 0.1`, `statistical-modeling 0.1`, `bioinformatics 0.1`, `medical-imaging 0.1`.

Changed repository behavior:

- YuukiAS/TRACE Beamer/PDF guidance now preserves `/home/yuukias/render_resources/chinese_math_pdf` as the local render-resource location when the probe reports it.
- Render failures now require reporting exact missing resources, TinyTeX, TeX packages, fonts, or PDF QA tools for user installation approval.
- A regression test now guards tracked guidance against retired server render paths.

Plugin changelog index: `docs/plugin-changelogs/README.md`.

Affected plugin changelog:

- `docs/plugin-changelogs/presentations.md`

## 5.0.2 - 2026-09-01

Repository `5.0.2` is a compatible release for the accepted 045 Presentations real-use regression hardening result.

Repository bump decision: PATCH
Reason: this release improves an existing central plugin's production behavior without adding a new repository-level capability or breaking existing contracts.

Affected plugin versions:

| Plugin | Previous | Current |
|---|---:|---:|
| `presentations` | `0.1` | `0.2` |

Affected plugins:
- `presentations`: `0.1` -> `0.2`
  Reason: existing-deck research-presentation revisions now have a production completion gate with real replay/regression evidence, rendered scientific-object QA, first-use dependency checks, English final-pass enforcement, and independent visual-review closure.

Unchanged plugin versions: `workflow-core 0.1`, `ai-skills-core 0.2`, `writing-style 0.1`, `research-writing 0.1`, `scientific-visualization 0.1`, `web-development 0.1`, `statistical-modeling 0.1`, `bioinformatics 0.1`, `medical-imaging 0.1`.

Changed repository behavior:

- Presentations existing-deck revision requests now route to an executable completion gate instead of relying on prose-only guardrails or Codex self-inspection.
- The gate consumes reviewer-seen baselines, accepted-element ledgers, targeted feedback, rerender evidence, high-resolution problem pages, first-use dependency order, rendered scientific-object QA, English scientific-prose final pass after scientific freeze, and independent visual review.
- Public-safe known-failure and unrelated reviewed regression fixtures cover the 045 failure classes without packaging private CAT-TRACE rendered pages, TRACE absolute paths, project page numbers, or project-specific scientific content into the installed plugin payload.
- The CUHK scientific layout renderer no longer hard-codes a TRACE checkout font path.

Plugin changelog index: `docs/plugin-changelogs/README.md`.

Affected plugin changelog:

- `docs/plugin-changelogs/presentations.md`

## 5.0.1 - 2026-09-01

Repository `5.0.1` is a compatible release that makes `ai-skills-core` the required maintenance companion for future central plugin production refinements.

Affected plugin versions:

| Plugin | Previous | Current |
|---|---:|---:|
| `ai-skills-core` | `0.1` | `0.2` |

Unchanged plugin versions: `workflow-core 0.1`, `writing-style 0.1`, `research-writing 0.1`, `presentations 0.1`, `scientific-visualization 0.1`, `web-development 0.1`, `statistical-modeling 0.1`, `bioinformatics 0.1`, `medical-imaging 0.1`.

Changed repository behavior:

- Production central-plugin refinement must now explicitly use `workflow-core` for process, `ai-skills-core` for the AI_Skills maintenance contract, and the target domain plugin for professional judgment.
- Reviewed Handoff Plans for production plugin refinements must state `Maintenance companion: ai-skills-core` and `Domain owner: <target plugin>` inside existing Plan sections, without adding new schema fields, states, roles, ledgers, or receipts.
- Executors must check installed/enabled production `ai-skills-core` and use real production invocation for maintenance preflight when required; reading source `SKILL.md` alone is not proof.
- Artifact-dependent Reviewed Handoff acceptance now distinguishes `PROCESS PASS` from `PRODUCT / ARTIFACT PASS`; Reviewer must read or view the final artifact, and private/text artifacts are routed to the future Bridge Kit Text Review owner instead of being reimplemented in AI_Skills.
- Task 044 is recorded as a real regression case: the user reported private `rewritten_report.md` still contained reader-facing `provenance`, `estimand`, `scientific gap`, `resource contract`, and `state of the art` language while review passed without the full artifact.
- Non-visual Reviewed Handoff tasks now route the real Visual Review job to `SKIPPED / NOT_REQUIRED` instead of presenting skipped model work as a Visual Review PASS.
- Reviewer PASS without a real human gate now defaults to integration preflight, merge back to `main`, push, and task-branch deletion unless a PR/Planner/human escalation condition applies.
- Completed production plugin behavior changes now have a hard release gate: after implementation, original-failure replay, unrelated regression, and delivery readiness, the affected plugin version must bump exactly once in the same refinement task.
- Baseline replay, TODO/provenance/docs-only changes, tests-only changes, and no-production-change cases remain `NO_BUMP`.
- The real-project feedback rule is included in this release: problems caused by an AI_Skills plugin are recorded directly in that plugin's central `docs/plugin-todos/<plugin>.md`; project threads may add minimal `status: NEW` entries while AI_Skills Planner/maintainer owns deduplication and abstraction.
- The Presentation TODO cleanup from the previous Unreleased section is included without changing `presentations` production behavior or version.

Plugin changelog index: `docs/plugin-changelogs/README.md`.

Affected plugin changelog:

- `docs/plugin-changelogs/ai-skills-core.md`

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
