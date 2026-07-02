# Portable Rendering

## Route Selection

Prefer routes in this order:

1. Project-owned render command, if it is documented and matches the requested
   output.
2. Project-local render resources, for example `render_resources/chinese_math_pdf`
   or a checked-in `texmf/` tree.
3. System `pandoc` with `xelatex` for Markdown sources.
4. System `xelatex` or `lualatex` for LaTeX sources.
5. Block with exact dependency evidence when none of the above can handle CJK
   text and math safely.

Do not hardcode a machine-specific resource path in a reusable prompt or skill.
If a fixed path works on one host, describe it as an optional detected resource,
not as a requirement.

## Useful Probes

```bash
python scripts/probe_pdf_render_env.py --root <project-root>
command -v pandoc xelatex lualatex pdfinfo pdftotext pdffonts pdftoppm
kpsewhich xeCJK.sty
kpsewhich ctexart.cls
kpsewhich fontspec.sty
```

## Pandoc Skeleton

```bash
python scripts/build_chinese_math_header.py --output /tmp/chinese-math-header.tex
mkdir -p /tmp/tex-cache
TEXMFVAR=/tmp/tex-cache/var \
TEXMFCONFIG=/tmp/tex-cache/config \
TEXMFCACHE=/tmp/tex-cache/cache \
pandoc input.md \
  --from markdown+tex_math_dollars+tex_math_single_backslash \
  --pdf-engine=xelatex \
  --include-in-header=/tmp/chinese-math-header.tex \
  -o output.pdf
```

If the project has a repo-local `texmf` tree, include it through `TEXINPUTS` or
the project's documented wrapper rather than copying files into global TeX
locations.

## Dependency Failure Handling

- Missing `pandoc`: try direct `.tex` compilation only if the source is already
  LaTeX; otherwise report that Markdown-to-PDF conversion is blocked.
- Missing `xelatex`: try `lualatex` only after checking that the CJK packages and
  fonts are available for that route.
- Missing `xeCJK`/`ctex`: use project-local TeX resources if present; otherwise
  report the missing package.
- Missing CJK fonts: detect available fonts or checked-in fonts; do not replace
  Chinese text with images or transliteration.
- TeX cache permission failure: set writable cache variables and rerun once.

## Validation Is Part Of Rendering

A zero exit code is not enough. The final answer should include evidence that
the PDF is readable: page count, text extraction sample or summary, font
embedding status, and visual spot check when glyph/layout risk exists.
