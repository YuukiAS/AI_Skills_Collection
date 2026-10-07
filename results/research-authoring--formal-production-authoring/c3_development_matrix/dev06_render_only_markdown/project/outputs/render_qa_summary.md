# Render QA Summary

Source: `finalized_note.md`

Final PDF: `outputs/finalized_note.pdf`

Route: canonical Markdown -> Pandoc LaTeX -> XeLaTeX -> PDF.

Render command:

```bash
python .agents/skills/tools-documents-media-render-chinese-math-pdf/scripts/render_scientific_pdf.py finalized_note.md outputs/finalized_note.pdf --root . --route canonical-markdown --work-dir outputs/render_work --preview-dir outputs/preview --preview-pages all --receipt outputs/render_receipt.json
```

Effective profile:

- `profile_id`: `canonical-formal-note-v0.2`
- Engine: `pandoc-ast-to-latex-xelatex`
- Paper: A4
- Font size: 11pt
- Margin: 25mm
- Line stretch: 1.15
- Fonts: TeX Gyre Termes, TeX Gyre Termes Math, Noto Serif SC, Noto Sans SC
- Resource root: `/users/a/e/aereinh/render_resources/chinese_math_pdf`

QA results:

- `pdfinfo`: 1 page, A4, non-empty PDF.
- `pdffonts`: TeX Gyre Termes, TeX Gyre Termes Math, and NotoSerifSC are embedded, subset, and Unicode mapped.
- `pdftotext -layout`: Chinese text, inline Dice formula, and all table rows are extractable.
- Layout validator: `errors: []`; table survival `3/3`; CJK fragmentation check passed.
- Visual preview checked: `outputs/preview_independent/finalized_note-1.png` shows readable Chinese, formula, table, and no visible truncation or mojibake.

Known QA note:

- `outputs/layout_qa.json` contains a warning that no obvious CJK font name was detected. This is a validator naming-regex limitation: `outputs/pdffonts.txt` shows `NotoSerifSC-Regular-Identity-H` embedded with Unicode mapping.

Evidence files:

- `outputs/render_env_probe.json`
- `outputs/render_receipt.json`
- `outputs/pdfinfo.txt`
- `outputs/pdffonts.txt`
- `outputs/finalized_note.layout.txt`
- `outputs/layout_qa.json`
- `outputs/preview/finalized_note-1.png`
- `outputs/preview_independent/finalized_note-1.png`

SHA-256:

```text
9488a3d627f89ec111a79d0e05f994b46fe350ed2ef69a2cd8c367d2caeec190  finalized_note.md
ac5e5e96b8279b82ba50cc42ed32a009b353cb59213831ddfd36e43b48827dfb  outputs/finalized_note.pdf
db9f6a2d36f87dc808764de23c57a19101c56107e0d63662ebf9949af37b1165  outputs/render_receipt.json
8857af8a69e86b1aecd799750cd02014b918ca0152ed911a4fb0e133c435e061  outputs/layout_qa.json
a5eca47e9ace0955e7e248e5987bc9c8cb8570a75c9d573ea9a46bb29e029bd6  outputs/preview_independent/finalized_note-1.png
```
