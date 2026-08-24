# Template Routing

Use the most specific trustworthy template available.

1. Company, client, course, conference, or project template supplied by the user.
2. Repo-local project template.
3. CUHK default template in `templates/cuhk/`.
4. Plain editable deck with the same design tokens when official Presentation/Slides tooling cannot load a template.

Default routing:

- Explicit PPT, PowerPoint, `.pptx`, editable, Slides, Google Slides, or "I will edit it later" -> editable Presentation/Slides route.
- Group meeting, research update, paper talk, seminar, journal club, defense, method/result update, "research slides", or "deck" in the `presentation-desktop` context without a specified format -> exact CUHK Beamer route by default, producing source-editable `.tex` from `templates/cuhk/beamer/source/` plus rendered PDF.
- Explicit "Beamer", "Overleaf", "LaTeX slides", ".tex", academic PDF, or a venue/project-locked TeX template -> `.tex` plus PDF.
- Business, teaching, operations, marketing, or executive decision decks -> editable `.pptx` through official Presentation/Slides or ChatGPT for PowerPoint unless the user asks for another format.
- Existing PPTX/Google Slides minor edit -> official Presentation/Slides only.

Do not route explicitly requested editable PPTX/Slides work to Beamer only because the content is academic. Do not use `python-pptx`, python-ppt, rendered PDF pages, or whole-slide images to fake an editable PPTX when official Presentation/Slides should create editable objects.

CUHK exact mode:

- Use `templates/cuhk/beamer/source/` as the canonical template source.
- The first/title slide layout must match the CUHK template. Only metadata/content fields such as title, subtitle, author, institute, date, and similar text placeholders may change.
- Do not use `templates/cuhk/design-tokens.json`, `templates/cuhk/beamer/main.tex`, `templates/cuhk/pptx/build_reference_deck.py`, or `templates/cuhk/pptx/cuhk-reference-deck.pptx` for exact CUHK reproduction; those files are derived convenience scaffolds for non-exact/test workflows.
