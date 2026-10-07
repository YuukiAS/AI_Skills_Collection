# Render QA

Source: `finalized_note.tex`

Output PDF: `outputs/finalized_note.pdf`

Route/profile:
- Authority: user requested direct rendering of finalized LaTeX source.
- Route: native LaTeX -> XeLaTeX -> PDF.
- Engine: `xelatex` (TeX Live 2020).
- Paper size: A4, inherited from TeX output/default article setup.
- Fonts: source uses `fontspec`; PDF embeds/subsets Latin Modern/CMMI/CMR fonts.
- Cache policy: TeX cache redirected into `outputs/` to avoid read-only home cache.

Render command:

```bash
env TEXMFVAR=outputs/texmf-var TEXMFCONFIG=outputs/texmf-config TEXMFCACHE=outputs/texmf-cache \
  xelatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=outputs finalized_note.tex
```

The command was run twice; the second run exited successfully and produced the final PDF.

QA evidence:
- `outputs/finalized_note.log`: successful XeLaTeX transcript.
- `outputs/finalized_note.pdfinfo.txt`: `Pages: 1`, A4 page size, unencrypted PDF.
- `outputs/finalized_note.fonts.txt`: all listed fonts show `emb yes` and `sub yes`.
- `outputs/finalized_note.text.txt`: extracted text contains the title, Dice coefficient prose, equation terms, and reported metrics.
- `outputs/finalized_note_page1.png`: visual first-page preview generated with `pdftoppm`; manual inspection found normal readable layout with no truncation or mojibake.
- `outputs/xelatex_version.txt`: renderer version evidence.

Hashes:

```text
1cc868a8b882e4b4b13bd0629c0d6d567617ab8c1bd8588f21ce9fee97da44fc  outputs/finalized_note.pdf
f205f237044aaae0a9e30a84e0b67df5d34a3d2240a53df9e9a77934ad377a61  outputs/finalized_note_page1.png
```

Status: complete.
