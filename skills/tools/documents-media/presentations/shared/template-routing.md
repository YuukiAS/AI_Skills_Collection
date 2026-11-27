# Template Routing

Use the most specific trustworthy template available.

1. Honour the requested output format. Explicit PowerPoint, PPTX, editable objects, or Google Slides uses the editable route.
2. Use an explicit user-supplied template for that format before any repository default. A locked venue or project template also takes precedence over built-in skins.
3. For Beamer, use the explicit or repository-selected skin as shown below.
4. When an editable tool cannot load the requested template, keep the deck editable and apply the available design tokens.

Default routing:

- Explicit PPT, PowerPoint, `.pptx`, editable, Slides, Google Slides, or "I will edit it later" -> editable Presentation/Slides route.
- Group meeting, research update, paper talk, seminar, journal club, defense, method/result update, "research slides", or "deck" in the `presentation-desktop` context without a specified format -> RESEARCH_STANDARD Beamer by default, producing source-editable `.tex` plus PDF.
- Explicit "Beamer", "Overleaf", "LaTeX slides", ".tex", academic PDF, or a venue/project-locked TeX template -> `.tex` plus PDF.
- Business, teaching, operations, marketing, or executive decision decks -> editable `.pptx` through official Presentation/Slides or ChatGPT for PowerPoint unless the user asks for another format.
- Existing PPTX/Google Slides minor edit -> official Presentation/Slides only.

Do not route explicitly requested editable PPTX/Slides work to Beamer only because the content is academic. Do not use `python-pptx`, python-ppt, rendered PDF pages, or whole-slide images to fake an editable PPTX when official Presentation/Slides should create editable objects.

| Request or repository selection | Canonical source |
|---|---|
| Research-standard Beamer or a repository selection of `research_standard` for Beamer | `templates/research_standard/beamer/source/` |
| User-supplied or locked Beamer template | The supplied template |
| Explicit editable PPTX or Google Slides | The existing editable Presentation/Slides route |

The built-in research-standard skin uses the title, body, navigation and closing geometry in `templates/_shared/beamer-core-v1/`. Edit title metadata in the source and build the editable template with `scripts/build_beamer_template.py`.


## Canonical Beamer Font Contract

All formal Beamer routes must read and obey `shared/font-policy.md`.

The font set is fixed. Presentation generation must not choose fonts from the host at runtime and must not use Times New Roman, Liberation, DejaVu, Windows font mounts, or fontconfig substitution as a fallback.

`research_standard` uses the fixed generated-text font identities from the shared core.
