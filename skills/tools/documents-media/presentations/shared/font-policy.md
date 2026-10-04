# Presentations — Canonical Font Policy V1

Date: 2026-10-04
Status: ACTIVE_CANONICAL_POLICY

This policy applies to all formal Beamer outputs produced by the Presentations plugin, including both built-in adapters:

- `cuhk-research`
- `course-standard`

It follows the deterministic font architecture already validated by `render-chinese-math-pdf`: fixed font identities, resolved through the renderer-owned resource environment, with no host font guessing and no silent fallback.

## 1. Fixed allowlist

Formal Beamer output may use only the following font families for generated slide text.

### Latin prose / titles / labels / tables / captions / header / footer

**TeX Gyre Termes**

Required faces:
- TeX Gyre Termes Regular
- TeX Gyre Termes Bold
- TeX Gyre Termes Italic
- TeX Gyre Termes Bold Italic

Canonical resource files:
- `fonts/texgyre-termes/texgyretermes-regular.otf`
- `fonts/texgyre-termes/texgyretermes-bold.otf`
- `fonts/texgyre-termes/texgyretermes-italic.otf`
- `fonts/texgyre-termes/texgyretermes-bolditalic.otf`

### Mathematics

**TeX Gyre Termes Math**

Canonical resource:
- `fonts/texgyre-termes-math/texgyretermes-math.otf`

For `cal` / `bfcal` glyph ranges only, Presentations may use:

**New Computer Modern Math**

Canonical resource:
- `fonts/newcomputermodern/NewCMMath-Regular.otf`

This is a narrow math-glyph exception, not another body font.

### Chinese / mixed CJK prose

Serif:
- **Noto Serif SC Regular**
- **Noto Serif SC Bold**

Sans / labels / CJK mono fallback:
- **Noto Sans SC Regular**
- **Noto Sans SC Bold**

Canonical resources:
- `texmf/fonts/opentype/public/noto-cjk/NotoSerifSC-Regular.otf`
- `texmf/fonts/opentype/public/noto-cjk/NotoSerifSC-Bold.otf`
- `texmf/fonts/opentype/public/noto-cjk/NotoSansSC-Regular.otf`
- `texmf/fonts/opentype/public/noto-cjk/NotoSansSC-Bold.otf`

### Latin code blocks

**Latin Modern Mono** is the only allowed Latin monospace family for code.

It is a TeX Live-owned fixed exception used only under `\ttfamily` / code-listing contexts. It must not become the body/title font.

## 2. Forbidden families / resolution routes

Formal Presentations output must not use or resolve any of the following as an automatic or template fallback:

- Times New Roman
- Liberation Serif / Sans / Mono
- DejaVu
- Arial
- Calibri / Carlito
- Cambria / Caladea
- Fandol
- host-specific Windows font mounts
- `fc-match` / fontconfig guessing for body or math fonts
- arbitrary system fonts
- another font chosen because the canonical font is missing

The existing legacy CUHK source currently contains Times New Roman. That is legacy source behavior, not the canonical Presentations font policy. When the CUHK adapter is migrated to the shared core, it must use this allowlist while preserving CUHK branding, geometry and colour roles.

## 3. Resource ownership

`render-chinese-math-pdf` is the sole owner of font/resource discovery.

Presentations must consume the resolved `render_resources/chinese_math_pdf` resource root and its TeX environment:

- `TEXMFHOME`
- `TEXMFVAR`
- `TEXMFCONFIG`
- `TEXMFCACHE`
- `TEXINPUTS`
- `OSFONTDIR`

Presentations must never search for a substitute font by family name on the host.

The preferred source is the bundle-local file path. If the exact canonical resource file is present, it is loaded by file/path, not by a fontconfig family lookup.

## 4. Installation / readiness contract

The Presentations runtime/profile is considered correctly installed only when its companion `render-chinese-math-pdf` resource bundle contains the required canonical font files.

This is an installation/preflight responsibility, not a normal per-deck design decision.

A production presentation task must not stop merely because Times New Roman is unavailable. Times New Roman is not a dependency.

If a canonical bundled font file is genuinely missing, the correct fix is to repair/install the canonical render resource bundle. Do not select another font.

## 5. Template parity

`cuhk-research` and `course-standard` use the same font contract.

They may differ in:
- theme/accent colour;
- logo/brand assets;
- title-background treatment;
- course/research identity fields.

They may not differ in:
- body font family;
- math font family;
- same-role font size;
- same-role weight/series;
- caption/table/header/footer font roles.

Thus “same style, different theme colour/branding” is a real implementation invariant rather than an approximate visual suggestion.

## 6. XeLaTeX binding

For direct Beamer/XeLaTeX builds, use file-bound fontspec/unicode-math declarations equivalent to the canonical renderer header.

Do not write:

`\setmainfont{Times New Roman}`

or:

`\setmainfont{Liberation Serif}`

or any family-name fallback chain.

Use the resolved resource directory and explicit `Path=...` files.

## 7. QA gate

Every formal Beamer release must run `pdffonts` and fail if the PDF contains an unexpected generated-text font family outside this allowlist.

Allowed generated-text families:
- TeX Gyre Termes
- TeX Gyre Termes Math
- New Computer Modern Math, restricted to allowed math glyph ranges
- Noto Serif SC
- Noto Sans SC
- Latin Modern Mono, code only

Fonts embedded inside externally supplied figures are not automatically treated as slide-text violations; figure provenance/legibility is reviewed separately.

The build receipt must record:
- resolved render resource root;
- canonical font file paths;
- font file SHA-256 values when available;
- `pdffonts` output;
- whether unexpected slide-text fallback fonts were detected.

## 8. Failure semantics

Forbidden:
- “Times New Roman unavailable” -> block
- “fontconfig resolved Liberation Serif” -> accept
- “use whatever serif font is installed” -> accept

Required:
- canonical resource present -> build with fixed fonts
- canonical resource incomplete -> repair/resource-dependency error naming the exact canonical file

There is no font-choice decision at deck-generation time.
