# Portable Rendering

## Route Selection

Prefer routes in this order:

1. Project-owned render command, if it is documented and matches the requested
   output.
2. Project-local render resources, for example `render_resources/chinese_math_pdf`
   or a checked-in `texmf/` tree.
3. System `pandoc` with `xelatex` for Markdown sources when the CJK font chain
   is visible in a raster preview.
4. Pandoc HTML plus headless Chromium for Chinese Markdown when TeX CJK fonts
   are missing, invisible, unstable, or consuming repeated header fixes.
5. System `xelatex` or `lualatex` for LaTeX sources.
6. Block with exact dependency evidence when none of the above can handle CJK
   text and math safely.

Do not hardcode a machine-specific resource path in a reusable prompt or skill.
If a fixed path works on one host, describe it as an optional detected resource,
not as a requirement.

## Useful Probes

```bash
python scripts/probe_pdf_render_env.py --root <project-root>
command -v pandoc chromium-browser chromium google-chrome google-chrome-stable xelatex lualatex pdfinfo pdftotext pdffonts pdftoppm fc-match
kpsewhich xeCJK.sty
kpsewhich ctexart.cls
kpsewhich fontspec.sty
fc-match 'Noto Serif CJK SC'
fc-match 'Source Han Serif SC'
```

`probe_pdf_render_env.py` also checks `CHINESE_MATH_PDF_RESOURCE_DIRS` as a
colon-separated list, then shared host resource locations used on this machine,
including `/overflow/htzhu/mingcheng_new/render_resources`,
`/overflow/htzhu/render_resources`, and `/users/a/e/aereinh/render_resources`.

## Font Downloads For A New Server

Use official font sources and keep the downloaded files in a server-local
resource directory, for example `/overflow/htzhu/render_resources/chinese_math_pdf`
or `$HOME/render_resources/chinese_math_pdf`. Record the path in `~/.config/ai-skills/local-overrides.toml` as
`render_resource_dirs = "/that/path"`, or set
`CHINESE_MATH_PDF_RESOURCE_DIRS=/that/path` for one-off sessions when the
directory is not under the project or one of the known host roots.

Recommended download links:

- Fandol, small TeX-oriented fallback fonts: `https://mirrors.ctan.org/fonts/fandol.zip`
  from the CTAN `fandol` package. Use these for a portable
  `texmf/fonts/opentype/public/fandol/` bundle containing
  `FandolSong-Regular.otf`, `FandolHei-Regular.otf`, and
  `FandolKai-Regular.otf`.
- Noto Sans Simplified Chinese, robust browser/system sans font:
  `https://github.com/notofonts/noto-cjk/releases/download/Sans2.004/18_NotoSansSC.zip`.
- Noto Serif Simplified Chinese, robust browser/system serif font:
  `https://github.com/notofonts/noto-cjk/releases/download/Serif2.003/14_NotoSerifSC.zip`.
- Source Han Sans Simplified Chinese: `https://github.com/adobe-fonts/source-han-sans/releases/download/2.005R/09_SourceHanSansSC.zip`.
- Source Han Serif Simplified Chinese: `https://github.com/adobe-fonts/source-han-serif/releases/download/2.003R/09_SourceHanSerifSC.zip`.

Minimal no-root setup using the Fandol bundle:

```bash
RESOURCE_DIR="$HOME/render_resources/chinese_math_pdf"
mkdir -p "$RESOURCE_DIR/texmf/fonts/opentype/public/fandol"
curl -L -o /tmp/fandol.zip https://mirrors.ctan.org/fonts/fandol.zip
unzip -o /tmp/fandol.zip -d /tmp/fandol
find /tmp/fandol -name 'Fandol*.otf' -exec cp {} "$RESOURCE_DIR/texmf/fonts/opentype/public/fandol/" \;
mkdir -p "$HOME/.config/ai-skills"
printf '[sites.local]\nrender_resource_dirs = "%s"\n' "$RESOURCE_DIR" > "$HOME/.config/ai-skills/local-overrides.toml"
python scripts/probe_pdf_render_env.py --root <project-root> --pretty
```

For Chromium rendering, system-installing Noto or Source Han through fontconfig
is stronger than relying only on Fandol. Without root, unzip the font files under
`$HOME/.local/share/fonts`, then run `fc-cache -f $HOME/.local/share/fonts` and
confirm with `fc-match 'Noto Serif SC'` or `fc-match 'Source Han Serif SC'`.

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

## Chromium HTML Fallback

Use this route when the requested source is Markdown and the LaTeX CJK chain
produces invisible Chinese glyphs, missing characters, unstable wrapping, or
repeated header/cache failures:

```bash
python scripts/render_markdown_pdf_chromium.py input.md output.pdf --root <project-root>
python scripts/validate_pdf_layout.py output.pdf --source input.md
```

The helper converts Markdown to standalone HTML with Pandoc, injects local
Fandol fonts from `render_resources/chinese_math_pdf` when present, prints with
headless Chromium, suppresses browser headers/footers, and leaves PDF QA to
`validate_pdf_layout.py`. It is a fallback render route, not a reason to skip
source cleanup or visual inspection.

## Dependency Failure Handling

- Missing `pandoc`: try direct `.tex` compilation only if the source is already
  LaTeX; otherwise report that Markdown-to-PDF conversion is blocked.
- Missing `xelatex`: try `lualatex` only after checking that the CJK packages and
  fonts are available for that route.
- Missing `xeCJK`/`ctex`: use project-local TeX resources if present; otherwise
  report the missing package.
- Missing CJK fonts: detect available fonts, shared host resources, or
  checked-in fonts; do not replace Chinese text with images or transliteration.
- TeX cache permission failure: set writable cache variables and rerun once.

## Validation Is Part Of Rendering

A zero exit code is not enough. The final answer should include evidence that
the PDF is readable: page count, text extraction sample or summary, font
embedding status, and a first-page PNG visual spot check. If Chinese text is
meant for a collaborator or author, also check that the document reads like a
clean Chinese note rather than a build log.
