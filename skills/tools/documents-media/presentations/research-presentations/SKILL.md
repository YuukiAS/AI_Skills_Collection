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
last_reviewed: 2026-07-28
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
- Choose the presentation format from the user's deliverable: PPT, PowerPoint, `.pptx`, editable, Slides, or "I need to edit it later" means editable Presentation/Slides; Beamer, LaTeX slides, `.tex`, academic PDF, or a venue/project-locked TeX template means Beamer/LaTeX; outline/storyline-only requests can stop at the deck plan. Do not default academic or research decks to Beamer.
- In the `presentation-desktop` profile, an unspecified group-meeting, research update, or "research slides" request defaults to an editable deck plan for Presentation/Slides, not Beamer.
- Use `../../shared/deck-plan.schema.json` as the default intermediate representation.
- Chinese slide text uses `writing-fidelity` plus `chinese-prose` for final wording; English scientific slide text can use `scientific-prose`. These are handoffs to installed writing skills, not duplicate writing rules inside this skill.

## Narrative

Research decks should answer:

```text
why this was done -> what changed -> mechanism/method -> evidence -> limits -> discussion needed -> next step
```

## Workflow

1. Read source material and identify source anchors: Markdown sections, PDF pages, figures, tables, code outputs, prior slides, or review comments.
2. Produce `deck-plan.yaml` before creating non-trivial slides.
3. Keep one main message per slide. Slide titles should carry information, not only labels such as "Background" or "Result 1".
4. Decide the format from the user's requested deliverable:
   - PPT, PowerPoint, `.pptx`, editable, Slides, or later manual edits -> editable Presentation/Slides route.
   - Beamer, LaTeX slides, `.tex`, academic PDF, or a locked TeX venue/project template -> Beamer/LaTeX route.
   - Group meeting, research update, or research slides in a desktop presentation context with no format specified -> editable Presentation/Slides route.
   - Outline, storyline, or page-by-page plan only -> stop at `deck-plan.yaml`.
5. Preserve equations in LaTeX inside the deck plan. Before compiling `.tex` or producing Beamer/PDF, invoke the locally installed `render-chinese-math-pdf` skill. Use that skill to probe for the LaTeX compiler, TeX packages, font availability, writable TeX caches, and PDF QA tools instead of assuming `xelatex`/`lualatex` paths. If the local skill is not installed in the active environment, block and report that missing dependency.
6. Use the CUHK default template when no stronger project, course, company, or conference template is specified. For exact CUHK Beamer reproduction, use `../../shared/templates/cuhk/beamer/source/` as the canonical source; the title slide layout is locked and only content fields such as title, subtitle, author, institute, and date may change.
7. After file creation, render the deck to PDF/images and run visual QA. A deck is not `complete` merely because a file exists.

## References

- `../../shared/deck-plan.schema.json`
- `../../shared/template-routing.md`
- `../../shared/ppt-skill-routing.md`
- `../../shared/source-fidelity.md`
- `../../shared/visual-qa.md`
- `../../shared/templates/cuhk/`
