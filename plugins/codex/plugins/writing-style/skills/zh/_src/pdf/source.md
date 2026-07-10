---
name: render-chinese-math-pdf
description: Render and validate Chinese or mixed Chinese/English mathematical Markdown/LaTeX as PDF. Use for CJK text, Unicode math, equations, tables, Pandoc/XeLaTeX/LuaLaTeX, TeX font/cache failures, citation cleanup, or readable PDF QA.
status: active
provenance: user-authored
trusted: false
requires_network: false
writes_files: true
executes_code: true
secrets_needed:
last_reviewed: 2026-07-02
profile_tags:
recommended_scope: global
---
# render-chinese-math-pdf

## Trigger Boundary

Use this skill when the requested deliverable is a readable PDF from Chinese,
mixed Chinese/English, or math-heavy Markdown/LaTeX, especially when the likely
failure mode is CJK font setup, Unicode math, Pandoc/XeLaTeX/LuaLaTeX behavior,
tables, citations, or PDF text readability.

Do not use this skill for general PDF text extraction, image-only OCR, or
non-CJK documents unless the user specifically asks for the rendering QA
workflow.

## Workflow

1. Locate the source document and project-local rendering assets before
   compiling. Prefer repo-provided scripts, templates, Makefiles, fonts, or
   `render_resources/chinese_math_pdf` directories when they exist.
2. Probe the environment instead of assuming a host-specific TeX path:
   `python scripts/probe_pdf_render_env.py --root <project-root>`.
3. Choose the narrowest viable route:
   - Existing project render command when documented and current.
   - Project-local render resources for fonts, TeX headers, or `texmf`.
   - Pandoc plus XeLaTeX for Markdown with CJK and conventional math.
   - Direct XeLaTeX/LuaLaTeX for already-authored `.tex`.
   - Block with exact missing dependencies if no available route can render CJK
     safely.
4. Build in a disposable or project-appropriate output directory. Set writable
   TeX cache variables when needed, for example `TEXMFVAR`, `TEXMFCONFIG`, and
   `TEXMFCACHE`, so rendering does not fail on read-only home/cache paths.
5. If a Pandoc header is needed, generate a portable starting point:
   `python scripts/build_chinese_math_header.py --output /tmp/chinese-math-header.tex`.
   Override fonts or resource paths only after confirming they exist.
6. Preserve source meaning. Do not delete equations, tables, references, or
   Chinese prose to make compilation easier. If AI citation handles or private
   placeholder characters are present, clean them using the citation cleanup
   reference rather than inventing bibliography entries.
7. Validate the produced PDF, not only the command exit code:
   - `pdfinfo` for page count and metadata when available.
   - `pdftotext` for extractable Chinese, English, and formula context.
   - `pdffonts` for embedded/subset fonts when available.
   - `pdftoppm` or another raster preview for first/critical pages when layout
     or glyph rendering is uncertain.
8. Report the exact source, output PDF path, command(s), page count, font/text
   checks, and any unresolved warnings. A smoke test or dry run is not a final
   result unless the user explicitly asked only for environment probing.

## Escalation Rules

- If Pandoc fails on CJK/font setup, try a generated header and writable TeX
  caches before stopping.
- If generated header compilation fails because a package or font is missing,
  inspect project-local resources and TeX package availability with
  `kpsewhich`; then either switch to available fonts/packages or report the
  exact missing dependency.
- If direct compilation fails after a Markdown conversion, inspect the generated
  `.tex` around the first real error and fix source/header issues rather than
  repeatedly rerunning the same command.
- If PDF exists but text extraction or font checks fail, treat the task as
  incomplete or partially complete and state what stronger validation or render
  route is required.

## Completion States

- `complete`: PDF rendered and passed command, page-count, text-extraction, and
  visual/font sanity checks appropriate to the document.
- `partial_complete`: PDF rendered, but non-critical warnings or limited QA
  remain and are reported with next steps.
- `blocked_missing_dependency`: no safe render route exists in the current
  environment; report the missing command/package/font and the attempted routes.
- `qa_failed`: a PDF was produced but readability, glyphs, pagination, or text
  extraction failed.

## References

- Read `references/portable-rendering.md` when setting up a new repo, replacing
  a host-local render path, or handling missing TeX/font dependencies.
- Read `references/citation-cleanup.md` when source text contains AI citation
  handles, private-use marker characters, broken bibliography tokens, or
  generated reference placeholders.
- Read `references/checklists.md` before final PDF QA.
- Read `references/source-notes.md` only when you need provenance for why this
  skill avoids host-specific assumptions.
