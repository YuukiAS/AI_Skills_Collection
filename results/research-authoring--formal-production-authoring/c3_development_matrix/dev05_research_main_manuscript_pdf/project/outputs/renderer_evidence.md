# Renderer Evidence

## Render Route

- Source: `outputs/source_package/paper.tex`
- Renderer: `pdfTeX 3.14159265-2.6-1.40.21 (TeX Live 2020)`
- Command:

```bash
env TEXMFVAR=outputs/render_evidence/texlive-cache/texmf-var \
  TEXMFCONFIG=outputs/render_evidence/texlive-cache/texmf-config \
  pdflatex -interaction=nonstopmode -halt-on-error paper.tex
```

The first sandboxed compile attempt failed because TeX tried to create `pdflatex.fmt` under a read-only user home. The successful route pinned `TEXMFVAR` and `TEXMFCONFIG` to `outputs/render_evidence/texlive-cache/`.

## Render Outputs

- Final PDF: `outputs/intensity_clipping_robustness_manuscript.pdf`
- Source archive: `outputs/intensity_clipping_source_package.tar.gz`
- Build log: `outputs/render_evidence/pdflatex_second_pass.log`
- Extracted PDF text: `outputs/render_evidence/extracted_text.txt`
- Page 1 preview image: `outputs/render_evidence/page1_preview.png`

## PDF Metadata

`pdfinfo outputs/intensity_clipping_robustness_manuscript.pdf` reported:

- Title: `Intensity-Clipping Robustness for Compact Lesion Segmentation`
- Author: `Internal manuscript draft`
- Producer: `pdfTeX-1.40.21`
- Pages: 3
- Page size: letter, 612 x 792 pts
- Encrypted: no
- PDF version: 1.5
- File size: 135740 bytes

## Build Log Check

The second-pass build log was searched for:

`Warning|Undefined|Overfull|Underfull|Error|Fatal`

No matches were found in `outputs/render_evidence/pdflatex_second_pass.log`.

## Text Extraction Check

`pdftotext` successfully extracted the title, abstract, methods, results table, limitations, discussion, and citation-status text into `outputs/render_evidence/extracted_text.txt`.

The extracted text includes the protected numeric evidence:

- `18 volumes`
- `0.421 to 0.469`
- `0.742 to 0.758`
- `18.4 mm to 17.9 mm`
- `motion-corrupted scan remained a failure case`
- `no external validation or statistical testing`

## Visual Readability Check

`pdftoppm` generated a page-1 preview at `outputs/render_evidence/page1_preview.png`. Visual inspection confirmed that the title, abstract, section headings, and body text are readable and not visibly clipped or overlapped on the first page.

## SHA-256 Hashes

```text
43def2d36365a0af95d032caa3c32d3f5b334cac71dcee98622712bb947a37e6  outputs/intensity_clipping_robustness_manuscript.pdf
eee1535fa0988b8051c18c691ce48f9c99c536af6d989cae77c703fbaf113482  outputs/intensity_clipping_source_package.tar.gz
25db9001d07d9e315897eb64aaab12e4af44dd54e6af64848c9f2ccf2bb3287c  outputs/source_package/paper.tex
d7cbbc80395bc7f1c514a7d5f7f62ebe3f712efdba28cf162be62bba86d1f784  outputs/source_package/README.md
bce0d1b3fc5548fd029fc3e85cfbb947fca474d844f609062b4464bd600a51a5  outputs/production_handoff.md
```
