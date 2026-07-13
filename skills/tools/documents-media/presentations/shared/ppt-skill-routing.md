# PPT Skill Routing Notes

Reviewed on 2026-07-13 from private Notion `AI Resources` PPT pages, two local screenshot assets, and the public ChatGPT for PowerPoint page.

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

## Unresolved Private Assets

The Notion page `5 个 AI PPT 万能提示词` contained a Word attachment named `魔法指令-Word版.docx`. The Notion connector returned only an internal attachment reference, not a signed binary download URL, and browser access required Notion login. Do not summarize or reuse that attachment unless the user supplies the file or a downloadable URL.
