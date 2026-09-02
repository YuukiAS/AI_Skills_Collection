---
name: render-chinese-math-pdf
description: Render and validate Chinese or mixed Chinese/English mathematical Markdown/LaTeX as PDF. Use for CJK text, Unicode math, equations, tables, Pandoc/XeLaTeX, TeX font/cache failures, citation cleanup, or readable PDF QA.
status: active
provenance: user-authored
trusted: false
requires_network: false
writes_files: true
executes_code: true
secrets_needed:
last_reviewed: 2026-09-01
profile_tags:
recommended_scope: global
icon_small: assets/app-facing.svg
icon_large: assets/app-facing.svg
---
# render-chinese-math-pdf

## Trigger Boundary

Use this skill when the requested deliverable is a readable PDF from Chinese,
mixed Chinese/English, or math-heavy Markdown/LaTeX, especially when the likely
failure mode is CJK font setup, Unicode math, Pandoc/XeLaTeX behavior, tables,
citations, or PDF text readability.

Do not use this skill for general PDF text extraction, image-only OCR, or
non-CJK documents unless the user specifically asks for this rendering QA
workflow.

## Default Architecture

The default renderer is strictly:

```text
Markdown -> Pandoc -> XeLaTeX -> PDF
```

The production entrypoint is the current host's
`render_resources/chinese_math_pdf/scripts/render_markdown_pdf.sh`.

The resource root is resolved in this order:

1. An explicit project-local resource root, when a project command provides one.
2. `CHINESE_MATH_PDF_RESOURCE_DIRS`, split on `:`.
3. The current namespace override at
   `CODEX_NAMESPACE_ROOT/.config/ai-skills/local-overrides.toml`.
4. The global/home override at `$HOME/.config/ai-skills/local-overrides.toml`;
   helpers also check the configured `CODEX_GLOBAL_HOME` boundary when present.
5. Generic ancestor discovery for `render_resources/chinese_math_pdf`.

Host-specific resource roots belong only in repo-external local override files
or one-off environment variables. Do not hardcode a private absolute path into
the reusable skill source, references, or scripts. Once the root is found, run
its local scripts from that root.

## Font Policy

The default PDF fonts must come from bundle-local font files, not fontconfig or
Windows mounts:

- Latin main: TeX Gyre Termes regular, bold, italic, and bold italic from
  `fonts/texgyre-termes/`.
- Math: TeX Gyre Termes Math from `fonts/texgyre-termes-math/`.
- CJK serif: Noto Serif SC regular and bold from
  `texmf/fonts/opentype/public/noto-cjk/`.
- CJK sans: Noto Sans SC regular and bold from
  `texmf/fonts/opentype/public/noto-cjk/`.

Do not use Times New Roman, Windows font mounts, fontconfig Times lookup,
DejaVu, Liberation, or Fandol as default font sources. Fandol may remain in the
bundle only as a legacy or emergency manual fallback.

## Workflow

1. Locate the source document and the active resource root before compiling.
2. Probe the environment:
   `python scripts/probe_pdf_render_env.py --root <project-root> --pretty`
   when the script is available, plus `pandoc --version`, `xelatex --version`,
   and `kpsewhich` checks when needed.
3. Compile Markdown through the resource script:

```bash
<resource-root>/scripts/render_markdown_pdf.sh input.md output.pdf
```

4. For `.tex` sources, use XeLaTeX directly with the same `TEXMFHOME`,
   `TEXMFVAR`, `TEXMFCONFIG`, `TEXMFCACHE`, and `OSFONTDIR` strategy used by
   `render_markdown_pdf.sh`.
5. If XeLaTeX or a required package/font is missing, report
   `blocked_missing_dependency` with the exact missing dependency. Do not
   silently switch to Chromium.
6. If Pandoc + XeLaTeX fails, inspect the generated header/source or `.log` and
   report the real LaTeX failure. Do not present a Chromium PDF as a successful
   LaTeX build.
7. Validate the produced PDF, not only the command exit code:
   - `pdfinfo` for page count when available.
   - `pdffonts` for embedded/subset TeX Gyre Termes, TeX Gyre Termes Math,
     Noto Serif SC, and Noto Sans SC usage.
   - `pdftotext -layout` for extractable Chinese, English, formulas, and table
     row survival.
   - `pdftoppm` or `scripts/validate_pdf.sh` for a first-page PNG preview.
8. Treat the task as incomplete if Chinese glyphs, formulas, table layout, or
   text extraction fail.

## Completion States

- `complete`: PDF rendered through Pandoc + XeLaTeX and passed command,
  page-count, font, text-extraction, and first-page visual checks.
- `partial_complete`: PDF rendered, but non-critical warnings or limited QA
  remain and are reported with next steps.
- `blocked_missing_dependency`: no safe Pandoc + XeLaTeX route exists; report
  the missing command/package/font and attempted route.
- `qa_failed`: a PDF was produced but readability, glyphs, pagination, or text
  extraction failed.

## References

- Read `references/portable-rendering.md` when setting up a new repo, replacing
  a host-local override path, or handling missing TeX/font dependencies.
- Read `references/citation-cleanup.md` when source text contains AI citation
  handles, private-use marker characters, broken bibliography tokens, or
  generated reference placeholders.
- Read `references/checklists.md` before final PDF QA.
- Read `references/source-notes.md` only when you need provenance for why this
  skill avoids host-specific assumptions.
