# Template Routing

Use the most specific trustworthy template available.

1. Company, client, course, conference, or project template supplied by the user.
2. Repo-local project template.
3. CUHK default template in `templates/cuhk/`.
4. Plain editable deck with the same design tokens when official Presentation/Slides tooling cannot load a template.

Default routing:

- "做 PPT", "组会汇报", "slides", or "deck" -> editable `.pptx`.
- Explicit "Beamer", "Overleaf", "LaTeX", or ".tex" -> `.tex` plus PDF.
- Existing PPTX/Google Slides minor edit -> official Presentation/Slides only.
