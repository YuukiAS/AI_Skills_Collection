---
name: latex-paper-authoring
description: Author, organize, repair, and prepare LaTeX research paper source/packages for arXiv, Overleaf, templates, or submission. Use directly for existing-LaTeX compile/debug/source hygiene; for new/substantial manuscripts, act after Research Authoring/paper admission and do not become final PDF owner before renderer handoff.
status: active
provenance: external-adapted
source_repo_url: https://github.com/yunshenwuchuxun/latex-paper-skills
source_path: .
source_ref: d0f106108cb09e448604a56ce973d35b340cf497
source_imported_at: 2026-07-09
source_license: MIT
source_note: Distilled from latex-paper-skills, latex-document-skill, claude-scholar LaTeX template organizer, and existing render-chinese-math-pdf practice.
trusted: false
requires_network: false
writes_files: true
executes_code: true
secrets_needed:
last_reviewed: 2026-07-09
profile_tags:
  - research-writing
  - latex
recommended_scope: project
icon_small: assets/app-facing.svg
icon_large: assets/app-facing.svg
metadata:
  skill-author: AI Skills Collection maintainers with recorded upstream sources
---
# LaTeX Paper Authoring

Use this when the source format and compilation path matter. Prefer `scientific-writing` when the main work is prose, and `paper-workflow-orchestrator` when the main work is paper strategy.

## Entry Boundary

Directly own tasks where the user already has LaTeX source and the main work is compile/debug, template cleanup, source hygiene, Overleaf/arXiv readiness, bibliography wiring, figure inclusion, or build troubleshooting.

For new manuscripts or substantial manuscript revisions, enter `research-authoring-core` and `paper-workflow-orchestrator` first. In that route this skill may prepare the LaTeX source tree, package files, bibliography, figures, and reproducibility notes, but it must not become the final artifact owner merely because the source is compilable.

For Research Authoring-owned final PDF production, prepare source/package and downstream handoff. Actual compile/render/PDF QA belongs to the admitted renderer route unless the task is genuinely existing-LaTeX render/debug work from the start.

## Workflow

1. Identify the build system: `latexmk`, `tectonic`, `pdflatex`, `xelatex`, `lualatex`, Overleaf, arXiv, or journal template.
2. Locate the canonical root `.tex` file and bibliography file. Do not edit generated outputs as source.
3. Normalize structure before content edits:
   - root file;
   - sections;
   - figures/tables;
   - bibliography;
   - macros;
   - supplementary material.
4. Preserve template-required commands and class files.
5. After edits, compile or provide an explicit reason compilation was not run.
6. Report warnings that affect submission: missing figures, unresolved refs, undefined citations, overfull boxes in visible areas, non-portable paths, and shell-escape dependencies.
7. Route figure palette choice, plot snippets, color accessibility, and publication
   figure export QA to `scientific-visualization`; keep this skill focused on
   LaTeX source structure and compilation.

## arXiv And Submission Checks

- Avoid absolute paths and local-only fonts.
- Keep source package small and reproducible.
- Include `.bbl` when the target requires it.
- Ensure figure formats are accepted by the venue.
- Ensure any journal-inspired figure palette is documented as non-official and
  sourced from the canonical scientific palette library.
- Check that generated files are not treated as authoritative manuscript source.

## Boundaries

- Do not silently rewrite mathematical notation.
- Do not remove packages or macros without checking usage.
- Do not invent citation keys or bibliography entries.
