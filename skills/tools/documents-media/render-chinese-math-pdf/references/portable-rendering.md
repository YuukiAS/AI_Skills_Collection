# Portable Rendering

## Route Selection

Prefer routes in this order:

1. Project-owned render command, if it is documented and matches the requested
   output.
2. Project-local or override-selected render resources, for example
   `render_resources/chinese_math_pdf` or a checked-in `texmf/` tree.
3. System `pandoc` with `xelatex` for Markdown sources when the CJK font chain
   is visible in a raster preview and `pdffonts` reports `uni yes` for the CJK
   font. This is the preferred route for final reports, group-meeting PDFs,
   manuscripts, and documents where font provenance should remain auditable in
   `pdffonts`.
4. System `xelatex` for LaTeX sources that already include the unified header.
5. Block with exact dependency evidence when none of the above can handle CJK
   text and math safely.

Do not hardcode a machine-specific resource path in reusable skill source,
references, tests, or generated payloads. Private paths belong in repo-external
local overrides or a one-off `CHINESE_MATH_PDF_RESOURCE_DIRS` environment value.
If a future machine lacks a resource, compiler, TeX package, font, or PDF QA
tool, report the missing dependency and ask before installing; do not invent or
fall back to retired server-only absolute paths.

## Useful Probes

```bash
python scripts/probe_pdf_render_env.py --root <project-root>
command -v pandoc xelatex kpsewhich pdfinfo pdftotext pdffonts pdftoppm
kpsewhich xeCJK.sty
kpsewhich fontspec.sty
```

`probe_pdf_render_env.py` checks an explicit resource root first, then
`CHINESE_MATH_PDF_RESOURCE_DIRS`, namespace/global/home local overrides, and
finally generic ancestor discovery for `render_resources/chinese_math_pdf`.
This matters on clusters where `HOME` and the active Codex namespace can point
at different storage roots. Host-specific resource locations belong in the local
override file or in `CHINESE_MATH_PDF_RESOURCE_DIRS`, not in the reusable skill.

This mirrors the Slurm skill's site-profile pattern: the reusable skill stays
generic, while private or machine-local facts live in a local override/profile.
For rendering, the local fact is usually only `render_resource_dirs`.

## Font Downloads For A New Server

Use official font sources and keep the downloaded files in a server-local
resource directory, for example a project-adjacent
`render_resources/chinese_math_pdf`. Record the path in a repo-external
`.config/ai-skills/local-overrides.toml` as
`render_resource_dirs = "/that/path"`, or set
`CHINESE_MATH_PDF_RESOURCE_DIRS=/that/path` for one-off sessions when the
directory is not under the project.

Recommended download links:

- TeX Gyre Termes and TeX Gyre Termes Math from TeX Live or CTAN's TeX Gyre
  packages. Keep `texgyretermes-regular.otf`, `texgyretermes-bold.otf`,
  `texgyretermes-italic.otf`, `texgyretermes-bolditalic.otf`, and
  `texgyretermes-math.otf` in the resource bundle.
- Noto Sans Simplified Chinese, robust browser/system sans font:
  `https://github.com/notofonts/noto-cjk/releases/download/Sans2.004/18_NotoSansSC.zip`.
- Noto Serif Simplified Chinese, robust browser/system serif font:
  `https://github.com/notofonts/noto-cjk/releases/download/Serif2.003/14_NotoSerifSC.zip`.

For final-standard XeLaTeX PDFs, a local resource bundle should prefer one of
the viewer-compatible CJK families above. The current default is Noto Serif SC
regular/bold plus Noto Sans SC regular/bold under
`texmf/fonts/opentype/public/noto-cjk/`. Fandol can remain in the same bundle as
legacy or emergency manual fallback, but it must not be the default PDF font.

Minimal no-root override setup:

```bash
mkdir -p "$(dirname "$LOCAL_OVERRIDE")"
printf '[sites.local]\nrender_resource_dirs = "%s"\n' "$RESOURCE_DIR" > "$LOCAL_OVERRIDE"
python scripts/probe_pdf_render_env.py --root <project-root> --pretty
```

## Final-Standard Pandoc/XeLaTeX Skeleton

Use this route when the PDF needs clean font provenance, stable Chinese glyphs,
and reviewable tables. It avoids requiring Times New Roman; TeX Gyre Termes is
the portable Times-compatible default on TeX Live systems. The helper loads
TeX Gyre Termes, TeX Gyre Termes Math, Noto Serif SC, and Noto Sans SC by file
from the selected local resource bundle. It does not use Times New Roman,
fontconfig fallback, Windows font mounts, DejaVu, Liberation, or Fandol as the
default route.

```bash
python scripts/build_chinese_math_header.py --root <project-root> --output /tmp/chinese-math-header.tex
mkdir -p /tmp/tex-cache
TEXMFVAR=/tmp/tex-cache/var \
TEXMFCONFIG=/tmp/tex-cache/config \
TEXMFCACHE=/tmp/tex-cache/cache \
TEXINPUTS="$(python scripts/probe_pdf_render_env.py --root <project-root> | python -c 'import json,sys; d=json.load(sys.stdin); p=d["summary"].get("recommended_resource_dir"); print((p + "/texmf//:") if p else "")')" \
pandoc input.md \
  --from markdown+tex_math_dollars+tex_math_single_backslash \
  --pdf-engine=xelatex \
  --include-in-header=/tmp/chinese-math-header.tex \
  -o output.pdf
```

If the project has a repo-local `texmf` tree, include it through `TEXINPUTS` or
the project's documented wrapper rather than copying files into global TeX
locations.

## Explicit Chromium HTML Renderer

Use this route only when the user explicitly asks for browser/HTML/CSS
rendering or when running an isolated diagnostic experiment. It is not an
automatic fallback for Pandoc + XeLaTeX failures:

```bash
python scripts/render_markdown_pdf_chromium.py input.md output.pdf --root <project-root>
python scripts/validate_pdf_layout.py output.pdf --source input.md
```

The helper converts Markdown to standalone HTML with Pandoc, prints with
headless Chromium, suppresses browser headers/footers, and leaves PDF QA to
`validate_pdf_layout.py`. Chrome/Skia may report local CJK fonts as unnamed
Type 3 fonts in `pdffonts`; report that limitation when the user asks what font
the PDF uses.

## Dependency Failure Handling

- Missing `pandoc`: try direct `.tex` compilation only if the source is already
  LaTeX; otherwise report that Markdown-to-PDF conversion is blocked.
- Missing `xelatex`: report `blocked_missing_dependency`.
- Missing `xeCJK`, `unicode-math`, or another required package: use the selected
  resource bundle's local TeX tree if present; otherwise report the missing
  package.
- Missing CJK or math fonts: report the missing bundle-local font file; do not
  replace Chinese text with images or transliteration.
- TeX cache permission failure: set writable cache variables and rerun once.

## Validation Is Part Of Rendering

A zero exit code is not enough. The final answer should include evidence that
the PDF is readable: page count, text extraction sample or summary, font
embedding status, `pdffonts` `uni` status for CJK fonts, and a first-page PNG
visual spot check. If Chinese text is meant for a collaborator or author, also
check that the document reads like a clean Chinese note rather than a build log.
When the user reports a PDF viewer rendering Chinese as blank, treat that viewer
as the acceptance target; Poppler preview success is not enough.
