# Template Routing

Use the most specific trustworthy template available.

1. Honour the requested output format. Explicit PowerPoint, PPTX, editable objects, or Google Slides uses the editable route.
2. Use an explicit user-supplied template for that format before any repository default. A locked venue or project template also takes precedence over built-in skins.
3. For Beamer, use the explicit or repository-selected skin as shown below.
4. When an editable tool cannot load the requested template, keep the deck editable and apply the available design tokens.

Default routing:

- Explicit PPT, PowerPoint, `.pptx`, editable, Slides, Google Slides, or "I will edit it later" -> editable Presentation/Slides route.
- Group meeting, research update, paper talk, seminar, journal club, defense, method/result update, "research slides", or "deck" in the `presentation-desktop` context without a specified format -> standard blue Beamer by default, producing source-editable `.tex` plus PDF from `course-standard`.
- Explicit "Beamer", "Overleaf", "LaTeX slides", ".tex", academic PDF, or a venue/project-locked TeX template -> `.tex` plus PDF.
- Business, teaching, operations, marketing, or executive decision decks -> editable `.pptx` through official Presentation/Slides or ChatGPT for PowerPoint unless the user asks for another format.
- Existing PPTX/Google Slides minor edit -> official Presentation/Slides only.

Do not route explicitly requested editable PPTX/Slides work to Beamer only because the content is academic. Do not use `python-pptx`, python-ppt, rendered PDF pages, or whole-slide images to fake an editable PPTX when official Presentation/Slides should create editable objects.

| Request or repository selection | Canonical source |
|---|---|
| Standard Beamer, unspecified built-in Beamer, teaching LaTeX or a repository selection of `course-standard` | `templates/course-standard/beamer/source/` |
| Explicit CUHK request or a repository selection of `cuhk` / `cuhk-research` | `templates/cuhk/beamer/source/` |
| User-supplied or locked Beamer template | The supplied template |
| Explicit editable PPTX or Google Slides | The existing editable Presentation/Slides route |

The two built-in templates share the title, body, navigation and closing geometry in `templates/_shared/beamer-core-v1/`. CUHK keeps its purple school palette, title bar, school logo and school footer while sharing the standard template's typography and layout metrics. Build either editable template with `scripts/build_beamer_template.py`. The CUHK PPTX reference and design-token JSON are separate scaffolds.


## Canonical Beamer Font Contract

All formal Beamer routes must read and obey `shared/font-policy.md`.

The font set is fixed. Presentation generation must not choose fonts from the host at runtime and must not use Times New Roman, Liberation, DejaVu, Windows font mounts, or fontconfig substitution as a fallback.

Both `cuhk-research` and `course-standard` use the same generated-text font identities, role sizes, leading, margins, grid, caption alignment, list spacing and formula sizing. Their template-specific colours, title-bar treatment, branding and footer identity remain distinct.
