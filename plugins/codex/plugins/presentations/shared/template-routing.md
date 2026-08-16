# Template Routing

Use the most specific trustworthy template available.

1. Company, client, course, conference, or project template supplied by the user.
2. Repo-local project template.
3. CUHK default template in `templates/cuhk/`.
4. Plain editable deck with the same design tokens when official Presentation/Slides tooling cannot load a template.

Default routing:

- Academic/research/technical decks, including "组会汇报", seminar, journal club, conference, defense, paper reading, method/result update, "slides", or "deck" in a research context -> LaTeX plus Beamer, with `.tex` and PDF output.
- Explicit "Beamer", "Overleaf", "LaTeX", or ".tex" -> `.tex` plus PDF.
- Business, teaching, operations, marketing, or explicitly editable PowerPoint requests -> editable `.pptx` through official Presentation/Slides or ChatGPT for PowerPoint.
- Existing PPTX/Google Slides minor edit -> official Presentation/Slides only.

Do not route academic decks to `python-pptx`, python-ppt, or generated editable PPTX unless the user explicitly asks for `.pptx` and accepts the template-fidelity tradeoff.

CUHK exact mode:

- Use `templates/cuhk/beamer/source/` as the canonical template source.
- The first/title slide layout must match the CUHK template. Only metadata/content fields such as title, subtitle, author, institute, date, and similar text placeholders may change.
- Do not use `templates/cuhk/beamer/main.tex` or the PPTX reference scaffold for exact CUHK reproduction; those files are derived convenience scaffolds.
