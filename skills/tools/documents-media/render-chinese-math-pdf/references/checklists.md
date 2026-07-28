# Checklists

## Preflight

- Identify the source file, target PDF path, and expected language/math content.
- Check whether the repo already has a render script, Makefile, template,
  Pandoc defaults file, TeX header, font directory, or
  `render_resources/chinese_math_pdf`.
- Run `scripts/probe_pdf_render_env.py --root <project-root> --pretty` or
  equivalent local checks for `pandoc`, `xelatex`/`lualatex`, `kpsewhich`, PDF QA
  tools, Chromium browser commands, fontconfig CJK matches, and usable
  `render_resources/chinese_math_pdf` bundles.
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
- `pdftotext -layout` output contains representative Chinese text and
  surrounding math prose when the PDF is not image-only by design.
- Extracted layout text does not show abnormal CJK one-character/short-line
  fragmentation.
- Source Markdown tables survive as recognizable rows/columns in extracted
  layout text when the source contains tables.
- `pdffonts` shows embedded/subset fonts when available.
- A first-page PNG preview is generated and inspected for visible Chinese,
  normal layout, no truncation, and no mojibake; this is required even when
  `pdftotext` extracts Chinese.
- Any equation/table-heavy pages are visually checked when layout risk exists.
- If LaTeX produces invisible Chinese, missing glyphs, unstable wrapping, or
  repeated header/cache failures, switch to the Chromium HTML route promptly.

## Reader-Facing Chinese QA

- The PDF can be sent directly to the intended Chinese reader without raw TeX
  blocks, build logs, duplicated titles, browser headers/footers, or needless
  English process labels.
- Questions for an author/collaborator include only points that require their
  judgment; evidence-backed facts stay out of the recipient-facing question list.
- Long paths, metric names, and method names are retained only where useful and
  do not overflow the page.

## Final Report

- Source path and output PDF path.
- Exact render command and any environment variables used.
- Page count, text/font QA evidence, and first-page preview PNG path.
- Missing dependencies, warnings, or partial-completion caveats.
- Next stronger route if the current route failed.
