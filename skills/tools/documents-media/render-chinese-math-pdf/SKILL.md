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
   `python scripts/probe_pdf_render_env.py --root <project-root> --pretty`.
   Treat a usable `render_resources/chinese_math_pdf` bundle as a valid CJK
   render route even when system `kpsewhich` cannot find `xeCJK` or `ctex`.
   The probe is the local layer of this skill: it should find namespace-local
   resources and overrides without baking private paths into the reusable skill.
3. Choose the narrowest viable route:
   - Existing project render command when documented and current.
   - Project-local render resources for fonts, TeX headers, or `texmf`.
   - User-namespace render resources when available, especially
     `/users/a/e/aereinh/render_resources/chinese_math_pdf` for `/users`
     CARE work. Treat `/overflow/.../render_resources` only as a migration or
     compatibility fallback, not as the preferred dependency for `/users`.
   - For final reports, group-meeting PDFs, manuscripts, or anything where
     font provenance matters, prefer Pandoc plus XeLaTeX with named fonts
     (`TeX Gyre Termes` or another Times-compatible TeX font for Latin, and a
     viewer-compatible CJK font such as Noto/Source Han/Droid fallback when
     available). Do not require Times New Roman; it is not a portable Linux
     dependency. Treat Fandol as a compact TeX fallback, not as automatically
     final-standard on every viewer.
   - Pandoc plus XeLaTeX for Markdown with CJK and conventional math when the
     CJK font chain is known to render visibly.
   - Pandoc HTML plus headless Chromium for Chinese Markdown when TeX CJK fonts
     are missing, invisible, unstable, or taking repeated header tweaks. Use
     `python scripts/render_markdown_pdf_chromium.py input.md output.pdf --root <project-root>`.
     Treat this as an internal-report fallback unless visual QA confirms that
     wide tables, equations, and font embedding are acceptable. Chrome/Skia may
     embed local fonts as unnamed Type 3 fonts, so it is not the best route when
     the deliverable must expose clean font names in `pdffonts`.
   - Direct XeLaTeX/LuaLaTeX for already-authored `.tex`.
   - Block with exact missing dependencies if no available route can render CJK
     safely.
4. Build in a disposable or project-appropriate output directory. Set writable
   TeX cache variables when needed, for example `TEXMFVAR`, `TEXMFCONFIG`, and
   `TEXMFCACHE`, so rendering does not fail on read-only home/cache paths.
5. If a Pandoc header is needed, generate a portable starting point:
   `python scripts/build_chinese_math_header.py --root <project-root> --output /tmp/chinese-math-header.tex`.
   The helper should pick the same local resource bundle reported by the probe.
   It should prefer viewer-compatible resource fonts such as Noto, Source Han,
   or Droid over bundled Fandol when those files exist. Override fonts or
   resource paths only after confirming they exist.
6. Preserve source meaning. Do not delete equations, tables, references, or
   Chinese prose to make compilation easier. If AI citation handles or private
   placeholder characters are present, clean them using the citation cleanup
   reference rather than inventing bibliography entries.
7. Validate the produced PDF, not only the command exit code:
   - `pdfinfo` for page count and metadata when available.
   - `pdftotext -layout` for extractable Chinese, English, formula context,
     abnormal CJK line fragmentation, and table row survival.
   - `pdffonts` for embedded/subset fonts when available. For a final-standard
     PDF, named TrueType/OpenType/CID fonts are preferred, and every obvious
     CJK font used for Chinese text must report `uni yes`. If a CJK font such
     as Fandol reports `uni no`, treat the PDF as viewer-risky even when
     Poppler PNG previews or `pdftotext` look acceptable.
   - `python scripts/validate_pdf_layout.py <pdf> --source <source.md>` when the
     source is Markdown or table-heavy; by default this emits a first-page PNG
     preview beside the PDF.
   - Always inspect at least the first-page PNG, and inspect any equation/table
     heavy pages when risk exists. Text extraction and Poppler previews are not
     proof that Chinese glyphs are visible in the user's PDF viewer.
8. For Chinese documents meant for an author, collaborator, or non-technical
   reader, do a reader-facing pass before delivery: remove raw TeX/log blocks
   unless they are the subject, avoid unnecessary English process words, keep
   only questions that the recipient actually needs to answer, and check that
   long paths or duplicated titles do not dominate the page.
9. Report the exact source, output PDF path, command(s), page count, font/text
   checks, preview PNG path, and any unresolved warnings. A smoke test or dry
   run is not a final result unless the user explicitly asked only for
   environment probing.

## Escalation Rules

- If Pandoc/XeLaTeX fails on CJK/font setup, try a generated header and writable
  TeX caches once, then switch to the Chromium HTML route when it is available
  instead of repeatedly tweaking TeX headers.
- If generated header compilation fails because a package or font is missing,
  inspect project-local resources and TeX package availability with
  `kpsewhich`; then either switch to available fonts/packages or report the
  exact missing dependency.
- If direct compilation fails after a Markdown conversion, inspect the generated
  `.tex` around the first real error and fix source/header issues rather than
  repeatedly rerunning the same command.
- If PDF exists but text extraction, table survival, line-fragmentation, font
  checks, or PNG visual inspection fail, treat the task as incomplete or
  partially complete and state what stronger validation or render route is
  required.

## Completion States

- `complete`: PDF rendered and passed command, page-count, text-extraction,
  table/line-layout checks, first-page PNG visual inspection, and visual/font
  sanity checks appropriate to the document.
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
