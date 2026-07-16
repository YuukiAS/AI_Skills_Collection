---
name: research-presentations
description: Plan research and technical presentations from papers, repo evidence, Markdown reports, Asteria or TRACE exports, code results, figures, and existing decks. Use for group meetings, seminars, conferences, journal clubs, defenses, and scientific project updates.
status: active
provenance: user-authored
trusted: false
requires_network: false
writes_files: true
executes_code: false
secrets_needed:
last_reviewed: 2026-07-13
profile_tags:
  - presentations
  - research-writing
recommended_scope: project
icon_small: assets/app-facing.svg
icon_large: assets/app-facing.svg
---
# Research Presentations

Use this skill for research presentation planning and quality control. File creation, object editing, export, and rendering should be handled by the official Presentation/Slides or LaTeX capability when available.

## Boundary

- Use for group meeting, academic talk, seminar, conference, journal club, defense, methods/model/result update, or Asteria/TRACE-to-deck work.
- Do not use for minor text, color, alignment, or object edits to an existing PPTX/Google Slides deck.
- Do not use generated whole-slide images as a substitute for editable PPTX unless the user explicitly asks for image/PDF slides.
- Use presentation themes/templates for deck-wide color. Scientific palettes in `palette/` may inform embedded figures, but raw palette ids should not become the slide theme.
- Use `../../shared/deck-plan.schema.json` as the default intermediate representation.

## Narrative

Research decks should answer:

```text
why this was done -> what changed -> mechanism/method -> evidence -> limits -> discussion needed -> next step
```

## Workflow

1. Read source material and identify source anchors: Markdown sections, PDF pages, figures, tables, code outputs, prior slides, or review comments.
2. Produce `deck-plan.yaml` before creating non-trivial slides.
3. Keep one main message per slide and preserve equations in LaTeX.
4. Route academic, research, technical, group-meeting, seminar, conference, journal-club, and defense decks to LaTeX plus Beamer by default. Do not use `python-pptx`, python-ppt, or editable PPTX generation for academic decks unless the user explicitly asks for editable `.pptx`.
5. Before compiling `.tex` or producing PDF, invoke the locally installed `render-chinese-math-pdf` skill. Use that skill to probe for the LaTeX compiler, TeX packages, font availability, writable TeX caches, and PDF QA tools instead of assuming `xelatex`/`lualatex` paths. If the local skill is not installed in the active environment, block and report that missing dependency.
6. Use the CUHK default template when no stronger project, course, company, or conference template is specified. For exact CUHK reproduction, use `../../shared/templates/cuhk/beamer/source/` as the canonical source; the title slide layout is locked and only content fields such as title, subtitle, author, institute, and date may change.
7. Export PDF/images for visual QA and keep the deck plan with the final deck.

## References

- `../../shared/deck-plan.schema.json`
- `../../shared/template-routing.md`
- `../../shared/ppt-skill-routing.md`
- `../../shared/source-fidelity.md`
- `../../shared/visual-qa.md`
- `../../shared/templates/cuhk/`
