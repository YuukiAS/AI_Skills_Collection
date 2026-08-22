---
name: research-presentations
description: Plan evidence-first research and technical presentations from papers, repo evidence, Markdown reports, Asteria or TRACE exports, code results, figures, and existing decks. Use for group meetings, supervisor discussions, seminars, conferences, journal clubs, defenses, and scientific project updates.
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
- Use `metadata.mode: research-group-meeting` for PhD group meetings, supervisor discussions, and research progress updates where the primary job is to update beliefs, expose failures, define next experiments, or ask for a supervisor decision.
- `research-group-meeting` mode must create a Research State and Evidence Board before slide planning. The state fields are internal planning data and must not be pasted mechanically onto slides.
- Chinese slide text uses `writing-fidelity` plus `chinese-prose` for final wording; English scientific slide text can use `scientific-prose`. These are handoffs to installed writing skills, not duplicate writing rules inside this skill.

## Narrative

Research decks should answer:

```text
why this was done -> what changed -> mechanism/method -> evidence -> limits -> discussion needed -> next step
```

Group-meeting decks should additionally answer:

```text
previous question -> prior belief -> new evidence -> belief update -> failures -> largest uncertainty -> next discriminating experiment -> decision needed
```

Do not expose internal labels such as `belief_update`, `evidence_quality`, `route promotion`, `handoff`, or `deck implication` as slide body text. Translate them into scientific questions, evidence, limits, failure diagnosis, and advisor decisions.

## Workflow

1. Read source material and identify source anchors: Markdown sections, PDF pages, figures, tables, code outputs, prior slides, or review comments.
2. For `research-group-meeting`, build the Research State and Evidence Board first. Inventory available figures, medical images, qualitative examples, quantitative plots, model diagrams, equations, experiment logs, failed experiments, literature figures to redraw, and missing evidence.
3. Choose page archetypes from the scientific job: `RESULT_FIGURE`, `FAILURE_CASE`, `MEDICAL_IMAGE_COMPARISON`, `STATISTICAL_MODEL`, `METHOD_DIAGRAM`, `EXPERIMENT_DESIGN`, `NEGATIVE_RESULT`, `RESEARCH_UPDATE`, `NEXT_EXPERIMENT`, or `SUPERVISOR_DECISION`.
4. Produce `deck-plan.yaml` before creating non-trivial slides. In `research-group-meeting` mode, every slide must include `page_function`, `required_evidence`, `source_evidence_ids`, `scientific_objects`, `evidence_status`, `layout_rationale`, `allowed_fallback`, `forbidden_fallback`, and `qa_criteria`. Run planning validation while evidence is still being gathered, then final validation before generation.
5. Keep one main research action per slide. Slide titles may be claim titles for mature results, but exploratory updates, negative results, and uncertainty pages may use question or in-progress titles.
6. Decide the format from the user's requested deliverable:
   - PPT, PowerPoint, `.pptx`, editable, Slides, or later manual edits -> editable Presentation/Slides route.
   - Beamer, LaTeX slides, `.tex`, academic PDF, or a locked TeX venue/project template -> Beamer/LaTeX route.
   - Group meeting, research update, or research slides in a desktop presentation context with no format specified -> editable Presentation/Slides route.
   - Outline, storyline, or page-by-page plan only -> stop at `deck-plan.yaml`.
7. If a slide claim has no real evidence, convert it to missing evidence, next experiment, speaker notes, backup, or delete it. Do not fill it with rounded cards, icons, slogans, empty tables, or generic arrows.
   If the frozen plan or user request requires real plot/image/table/data evidence, a fabricated proxy, decorative graphic, or conceptual illustration cannot satisfy that requirement. Conceptual grounding is allowed only when clearly labeled as conceptual and kept separate from evidence claims.
8. Preserve equations in LaTeX inside the deck plan. Before compiling `.tex` or producing Beamer/PDF, invoke the locally installed `render-chinese-math-pdf` skill. Use that skill to probe for the LaTeX compiler, TeX packages, font availability, writable TeX caches, and PDF QA tools instead of assuming `xelatex`/`lualatex` paths. If the local skill is not installed in the active environment, block and report that missing dependency.
9. Use the CUHK default template when no stronger project, course, company, or conference template is specified. For exact CUHK Beamer reproduction, use `../../shared/templates/cuhk/beamer/source/` as the canonical source; the title slide layout is locked and only content fields such as title, subtitle, author, institute, and date may change.
10. After file creation, render the deck to PDF/images and run scientific visual QA. A deck is not `complete` merely because a file exists or mechanical checks pass. For editable PPTX regression, the PDF/images must come from the PPTX through a real presentation engine such as `soffice`, `libreoffice`, or an explicitly configured renderer.
11. Use the research presentation reference library by page function, scientific domain, statistical subdomain, and evidence type. Keep downloaded source assets in `.cache/research-presentation-reference-library/`; commit only metadata indexes and page-level lessons.

## Revision Scope

When revising an existing rendered deck from user, advisor, reviewer, or visual-review feedback, treat the cited problem as a regression constraint for the next version. Keep an `accepted_element_ledger` in the working notes or deck plan when feedback is targeted: record which slides/components were accepted, which can only be locally adjusted, and which may be restructured. A local correction does not authorize a global redesign, removal of accepted structures, or restoration of a previously rejected layout. Compare the revised render against the version the reviewer actually saw; unrelated large visual changes must be justified or reverted.

## Evidence And Concept Grounding

First-use notation and abstract concepts should be grounded in the audience's current context. Define what the symbol or concept is, where it comes from, and what role it plays in the model or experiment. When active data or audited source material contains a real example, prefer a short real example over placeholders such as `group 1` or toy evidence. If only a conceptual example is available, label it as conceptual and do not use it to satisfy a real-evidence requirement.

## Diagram Gate

Use diagrams only when the relationship, computation, mechanism, or experimental path is itself scientific content. Do not draw a diagram that merely places prose into boxes. Nodes must be real scientific objects or operations, and connectors must be structural connectors that encode data flow, dependency, transformation, control flow, time order, or experimental comparison. Arrows should be generated as connectors with semantic anchors and consistent direction, not typed arrow characters or decorative lines. Containment should use enclosure, braces, group labels, or shared background rather than misleading arrows.

## Research Group Meeting QA

Rendered-slide QA must answer these questions per page:

- Does the page have a real scientific object?
- What evidence supports the page?
- Does the visual encode data, mechanism, experimental unit, case, formula, comparison, or uncertainty?
- Can the main question or result be understood in 5-10 seconds?
- Are figures, axes, legends, case labels, and formulas readable?
- Does the page look like consulting, a report page, or a card dashboard?
- If decorative frames are removed, is scientific content still present?
- Is the page worth 30-90 seconds in a group meeting?

If the answer is clearly no for scientific content, the page must not pass.

The generator must not assign final `PASS`. It may write PPTX, raw assets, evidence manifests, and render status. An independent scientific visual reviewer must read the plan/evidence/rendered PNGs/reference IDs before assigning `PASS`, `REVISE`, or `BLOCKED`. If real PPTX rendering is unavailable, status is `BLOCKED_REAL_PPTX_RENDER`; do not reconstruct a parallel PDF and claim it represents the PPTX.

## Anti-Patterns

Treat these as QA failures when they replace evidence: title plus slogan plus giant empty table; rounded-card dashboard; consulting language; generic arrows without scientific objects; fake visualization; paragraph pasted onto slide; unreadably shrunk paper figure; every slide using the same layout; decorative icons replacing evidence; vague next steps; internal planning language leaking onto slides; evidence-free roadmap.

If an urgent real group meeting must be delivered before the editable PPTX path passes regression, use mature Beamer or the user's older template first. Plugin experimentation must not block the real meeting.

## References

- `../../shared/deck-plan.schema.json`
- `../../shared/template-routing.md`
- `../../shared/ppt-skill-routing.md`
- `../../shared/source-fidelity.md`
- `../../shared/visual-qa.md`
- `../../shared/references/RESEARCH_GROUP_MEETING_MODE.md`
- `../../shared/references/RESEARCH_SLIDE_ARCHETYPES.md`
- `../../shared/references/RESEARCH_PRESENTATION_ANTIPATTERNS.md`
- `../../shared/references/research_slide_reference_index.csv`
- `../../shared/references/reference_sources_manifest.json`
- `../../shared/references/reference_source_search_matrix.csv`
- `../../../../../docs/workflows/RESEARCH_PRESENTATION_REFERENCE_LIBRARY.md`
- `../../shared/templates/cuhk/`
