# Renderer Evidence

## Final render command

```bash
env TEXMFVAR=/overflow/htzhu/mingcheng_new/AI_Skills_Collection-research-authoring--formal-production-authoring/results/research-authoring--formal-production-authoring/c3_development_matrix/dev04_research_main_report_pdf_run2/project/outputs/texmf-var TEXMFCONFIG=/overflow/htzhu/mingcheng_new/AI_Skills_Collection-research-authoring--formal-production-authoring/results/research-authoring--formal-production-authoring/c3_development_matrix/dev04_research_main_report_pdf_run2/project/outputs/texmf-config TEXMFCACHE=/overflow/htzhu/mingcheng_new/AI_Skills_Collection-research-authoring--formal-production-authoring/results/research-authoring--formal-production-authoring/c3_development_matrix/dev04_research_main_report_pdf_run2/project/outputs/texmf-cache pandoc outputs/research_update.md -s --pdf-engine=xelatex -o outputs/research_update.pdf
```

The first render attempt failed because XeLaTeX tried to create `xelatex.fmt` under the read-only home TeX cache. The successful render used project-local TeX cache directories under `outputs/`.

## Tool probes

- `pandoc --version`: pandoc 2.14.0.3.
- `xelatex --version`: XeTeX 3.14159265-2.6-0.999992, TeX Live 2020.
- `kpsewhich article.cls`: `/usr/share/texlive/texmf-dist/tex/latex/base/article.cls`.
- PDF QA tools available: `pdfinfo`, `pdffonts`, `pdftotext`, `pdftoppm`.

## PDF identity

- PDF path: `outputs/research_update.pdf`.
- SHA-256: `fc5682a470c298a379d9781d00487aac2c05911bdd697c2850fdd615b6e6c1c9`.
- Page count: 1.
- Page size: letter, 612 x 792 pt.
- File size: 22098 bytes.
- Producer: `xdvipdfmx (20200315)`.

## Font QA

`pdffonts outputs/research_update.pdf` reported embedded, subsetted Unicode fonts:

```text
name                                 type              encoding         emb sub uni object ID
------------------------------------ ----------------- ---------------- --- --- --- ---------
SFKKCJ+LMRoman17-Regular-Identity-H  CID Type 0C       Identity-H       yes yes yes      5  0
HNFREB+LMRoman12-Regular-Identity-H  CID Type 0C       Identity-H       yes yes yes      7  0
WYWMPA+LMRoman12-Bold-Identity-H     CID Type 0C       Identity-H       yes yes yes      9  0
VJKATZ+LMRoman10-Regular-Identity-H  CID Type 0C       Identity-H       yes yes yes     11  0
```

## Text extraction QA

`pdftotext -layout` output is saved at `outputs/research_update_text.txt`.

Representative extracted table rows:

```text
Method                                               Mean Dice     Small-lesion Dice    HD95 (mm)
Baseline nnU-Net-style 3D U-Net                           0.742                0.421            18.4
Baseline + test-time intensity percentile clipping        0.758                0.469            17.9
Absolute change                                          +0.016               +0.048            -0.5
```

The extracted text preserves the title, section headings, comparison table, metric directions, interpretation boundary, recommendation, and advisor question.

## Visual QA

- First-page PNG preview: `outputs/research_update_page1.png`.
- Visual inspection result: pass. The PDF is a one-page formal report; title block, sections, table, and final advisor question are visible with no clipping, overlap, mojibake, or unreadable table wrapping.

## Renderer status

Complete: Pandoc + XeLaTeX render succeeded, the PDF is non-empty, fonts are embedded, text is extractable, the table survives text extraction, and the rendered page passed visual inspection.
