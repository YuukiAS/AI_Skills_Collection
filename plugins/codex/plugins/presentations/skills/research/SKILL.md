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
4. Route ordinary PPT requests to editable PPTX output; route explicit Beamer/Overleaf/LaTeX requests to `.tex` plus PDF.
5. Use the CUHK default visual system when no stronger project, course, company, or conference template is specified.
6. Export PDF/images for visual QA and keep the deck plan with the final deck.

## References

- `../../shared/deck-plan.schema.json`
- `../../shared/template-routing.md`
- `../../shared/ppt-skill-routing.md`
- `../../shared/source-fidelity.md`
- `../../shared/visual-qa.md`
- `../../shared/templates/cuhk/`
