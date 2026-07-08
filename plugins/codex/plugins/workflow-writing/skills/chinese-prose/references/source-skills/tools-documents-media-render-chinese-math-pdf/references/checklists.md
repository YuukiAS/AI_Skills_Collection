# Checklists

## Preflight

- Identify the source file, target PDF path, and expected language/math content.
- Check whether the repo already has a render script, Makefile, template,
  Pandoc defaults file, TeX header, font directory, or
  `render_resources/chinese_math_pdf`.
- Run `scripts/probe_pdf_render_env.py --root <project-root>` or equivalent
  local checks for `pandoc`, `xelatex`/`lualatex`, `kpsewhich`, and PDF QA tools.
- Confirm the output/cache directory is writable.

## Source Integrity

- Keep display equations, inline math, tables, captions, and technical paths.
- Do not remove Chinese text or references merely to compile.
- Clean AI citation handles and private-use markers only when they are clearly
  non-source artifacts; disclose unresolved citation uncertainty.

## Render QA

- Command exits successfully.
- PDF exists and is non-empty.
- `pdfinfo` or an equivalent tool reports a plausible page count.
- `pdftotext` output contains representative Chinese text and surrounding math
  prose when the PDF is not image-only by design.
- `pdffonts` shows embedded/subset fonts when available.
- First page and any equation/table-heavy pages are visually checked if layout
  risk exists.

## Final Report

- Source path and output PDF path.
- Exact render command and any environment variables used.
- Page count and QA evidence.
- Missing dependencies, warnings, or partial-completion caveats.
- Next stronger route if the current route failed.
