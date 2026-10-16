# CUHK Default Template

Original local source files:

- `C:\Users\humc2\Downloads\CUHK Template.zip`
- `C:\Users\humc2\Downloads\CUHK Template.pdf`

The committed payload is the reproducible template subset, not the entire zip. It includes `main.tex`, `styles/`, required `assets/`, and `bibliography.bib`. Nonessential editor settings, XCF files, and sample figure/table images are not committed.

`beamer/source/` is the canonical CUHK Beamer template. Use it for academic talks and exact template reproduction.

`design-tokens.json`, `beamer/main.tex`, and `pptx/build_reference_deck.py` are derived scaffolds for non-exact workflows only. Do not use them when the user asks for CUHK template fidelity or when generating the default academic/research deck.

Title slide lock:

- Preserve the first/title slide layout from `beamer/source/` exactly.
- Only replace metadata/content fields such as title, subtitle, author, institute, date, course label, supervisor, and ID number.
- Do not change title-slide geometry, background, logo placement, theme files, spacing, or decorative elements unless the user explicitly asks to modify the CUHK template itself.

Font requirements:

- The source theme uses the canonical Presentations font policy: file-bound TeX Gyre Termes for Latin text, TeX Gyre Termes Math for mathematics, and Latin Modern Mono for code.
- `__AI_SKILLS_FONT_RESOURCE_ROOT__` is a build-time placeholder. The production entry resolves it from the installed `render-chinese-math-pdf` resource probe before XeLaTeX runs.
- The resource bundle must contain all four TeX Gyre Termes faces and TeX Gyre Termes Math. The production entry fails with the exact missing path when that bundle is incomplete.
- The build never searches host fonts or substitutes Times New Roman, Liberation, DejaVu, Caladea, or Carlito.

## Validation

Repository tests verify that the CUHK payload contains the required Beamer source files, theme files, PNG assets, `design-tokens.json`, PPTX builder, and a valid PPTX reference deck zip with slide XML.

Full render validation requires a host with:

- XeLaTeX and the Beamer dependencies used by `beamer/source/main.tex`, including `tcolorbox`.
- The fixed font files declared by `shared/font-policy.md` in the resolved `render-chinese-math-pdf` resource bundle.
- `python-pptx` when rebuilding `pptx/cuhk-reference-deck.pptx` from `pptx/build_reference_deck.py`.

If TeX has to create user formats on a read-only home filesystem, set `TEXMFVAR` and `TEXMFCONFIG` to writable local cache directories before compiling.
