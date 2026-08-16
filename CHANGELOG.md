# Changelog

## Unreleased

No pending changes.

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
