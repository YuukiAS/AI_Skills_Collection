# PPT Skill Routing Notes

Reviewed on 2026-07-13 from private Notion `AI Resources` PPT pages, two local screenshot assets, the user-supplied `魔法指令-Word版.docx`, and the public ChatGPT for PowerPoint page.

## Boundary

This repository plans deck structure, style routing, source fidelity, and QA. Editable `.pptx` or Google Slides object creation and direct slide editing belong to the official Presentation/Slides capability or the ChatGPT for PowerPoint app when available.

Use whole-slide images only when the user explicitly asks for image/PDF/social-card slides. Otherwise keep text, charts, and diagrams editable.

## Style And Tool Routing

| User intent | Route |
|---|---|
| Professional editable PowerPoint with conventional layouts | Editable PPTX through official Presentation/Slides or ChatGPT for PowerPoint, with this repo providing deck plan and QA |
| High visual ceiling, multi-format visual outputs, or poster-like pages | Visual direction first, then confirm whether the user accepts image-heavy slides |
| Narrative, storyline, decision logic, or quality control | `research-presentations` or `business-presentations` deck plan before file creation |
| HTML-style expressive slides | Frontend visual system plus explicit HTML/PDF routing; do not pretend it is an editable PPTX |
| Swiss/offline sharing style | Template/style brief plus editable deck if possible |
| Speaker mode, script, or presenter notes | Add notes/script requirements to deck plan and route file operations to official tooling |
| Social card or Xiaohongshu-style pages | Image-oriented deliverable; mark editability tradeoff |
| Material collation into NotebookLM-like workflows | Treat as research organization, not professional PPT generation |

## Official PowerPoint App Notes

The ChatGPT for PowerPoint app can create and update slides from notes, documents, spreadsheets, prompts, and existing decks, while keeping content editable where supported. It is useful for slide cleanup, narrative tightening, chart/story conversion, and template-guided deck updates.

Known limitations to account for in prompts and QA:

- advanced PowerPoint features, fonts, templates, and complex formatting may not be fully supported;
- vague instructions can change or remove content unexpectedly;
- users should give concrete edit instructions, review output, and keep a backup of important decks.

## Prompt Intake Pattern

For non-trivial decks, collect:

- audience and decision or learning goal;
- time limit and slide count;
- source anchors and required citations;
- editable PPTX, Google Slides, Beamer, HTML, PDF, or image-slide output;
- visual reference and template constraints;
- whether presenter notes, handout version, or script is required.

## Reusable Prompt Blueprint

The reviewed Word prompt collection is useful as a structure, not as copy-ready text. For deck prompts and deck plans, use this reusable sequence:

1. Role and audience: name the domain role, audience, and decision or learning context.
2. Topic placeholder: state the subject and required output format.
3. Style intent: describe the visual job in plain terms, such as consulting brief, product strategy teardown, classroom flow, review handout, OKR roadmap, self-review evidence chain, portfolio, campus activity, or traditional-culture lesson.
4. Deck length: keep ordinary generated decks within 10-15 slides unless the user asks otherwise.
5. Slide logic: provide a flexible outline instead of fixed page titles when source material does not fit.
6. Evidence and charts: request charts only for meaningful data; use `example data` or `to-be-replaced data` labels when values are illustrative.
7. Images: require every image, screenshot, or illustration to support the slide conclusion, not decorate the page.
8. Per-slide message: require one named message line, such as `Insight`, `Plan conclusion`, `Statement conclusion`, `Teaching design intent`, or `Learning tip`.
9. Notes: add presenter notes or classroom guidance only when requested or natural for the audience.
10. Honesty gate: forbid fabricated precise data, fake citations, unsupported benchmark claims, and decorative visual rules that conflict with editability.

## Scenario Patterns Worth Keeping

| Scenario | Deck logic | Message line |
|---|---|---|
| Competitor or industry research | market context -> selection logic -> comparison -> evidence -> implications -> recommendation | `Insight` |
| Product strategy teardown | positioning -> user scenario -> feature/path analysis -> growth/commercial mechanism -> opportunity | `Insight` |
| Work plan or mid-year roadmap | background judgment -> objective -> key results -> projects -> resources -> risks -> review cadence | `Plan conclusion` |
| Self-review, promotion, or defense | role scope -> total results -> project evidence -> capability growth -> reflection -> future plan | `Statement conclusion` |
| Open class, demo class, or teaching competition | objectives -> learner analysis -> scenario introduction -> knowledge construction -> activities -> evaluation -> transfer | `Teaching design intent` |
| Daily teaching courseware | learning goal -> knowledge frame -> concepts -> examples -> practice -> misconceptions -> summary | `Learning tip` |
| Review lesson | knowledge overview -> exam points -> methods -> errors -> examples -> practice -> feedback | `Learning tip` |
| Interactive classroom | scenario -> question -> material observation -> individual thinking -> group work -> presentation -> feedback -> summary | `Teaching design intent` |

## Not Adopted From The Word Prompts

- Do not copy the full long prompt templates into a skill.
- Do not force exact fonts, colors, page decorations, or style reproduction unless the user supplies a real template or explicitly asks for a style study.
- Do not require images every fixed number of pages when no trustworthy image source exists.
- Do not enforce "strict 16:9" or "15 slides max" when the user, venue, or source document requires another format.
- Do not use highly specific aesthetic claims such as "publication-grade" or "top creative agency standard" as a quality substitute; turn them into concrete, testable layout and content requirements.
- Do not use chart-heavy instructions unless the source data can support charting.

## Private Asset Notes

The Notion page `5 个 AI PPT 万能提示词` contained a Word attachment named `魔法指令-Word版.docx`. The Notion connector returned only an internal attachment reference, not a signed binary download URL, and browser access required Notion login. The user later supplied the Word file locally, so reusable prompt structure was merged here while full templates and private source text were not committed.
