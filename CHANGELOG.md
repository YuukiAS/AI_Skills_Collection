# Changelog

## Unreleased

No pending changes.

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
