# MoSAIC CARE 2026 paper

This repository contains the MoSAIC CARE-Myocardium paper workspace and the uploaded CARE submission package.

## Research-lead strategy

- [`PAPER_STRATEGY_AND_EXECUTION_ROADMAP_20260726.md`](PAPER_STRATEGY_AND_EXECUTION_ROADMAP_20260726.md): detailed scientific positioning, evidence boundaries, section blueprint, table/figure plan, two-day AI-assisted writing workflow, author-role recommendations, and the boundary between the MoSAIC paper and the post-paper Docker submission.
- [`roadmap_site/index.html`](roadmap_site/index.html): one-day execution dashboard for the MoSAIC CARE 2026 paper sprint, organized as Step 1 through Step 7 with claim gates, evidence gates, cut list, file map, and copyable GPT prompt blocks.

## Current paper package

- `code/source/`: read-only upstream MoSAIC source snapshot for checking manuscript methods and implementation claims; copied from `/users/a/e/aereinh/MoSAIC/code/source` at commit `d334bd1fb2a99dbbc230510590cd8e3ee08cc377`.
- `submission/`: contents unpacked from the uploaded `paperCARE.zip`; this is the current MoSAIC CARE paper source package.
- `submission/mosaic.tex`: main LaTeX source for the uploaded manuscript body.
- `submission/mosaic.pdf`: regenerated locally from `mosaic.tex` because the PDF inside `paperCARE.zip` could not be parsed by `pdfinfo`/`pdftotext`.
- `references/style/`: extracted TeX, figure, and LNCS files from two other CARE Challenge task paper packages. These are style references only; they are not MoSAIC content, evidence, claims, or submission artifacts.
- `../CARE2026_LA_Task3.zip` and `../LG_MICCAI_CARE2026_Task1_Paper_2026_7_27.zip`: original local reference archives from other groups. The zip archives themselves are not tracked here.

## CARE 2026 paper requirements

Source: [CARE 2026 Paper Submission](https://zmic.org.cn/care_2026/paper_submission/).

- Submission/review system: submit abstract and paper through OpenReview at [MICCAI.org/2026/Workshop/CARE](https://openreview.net/group?id=MICCAI.org/2026/Workshop/CARE).
- Account requirement: authors need OpenReview accounts before submission; OpenReview verification may take several days.
- Template: searchable PDF using Springer's Lecture Notes in Computer Science (LNCS) LaTeX or Word templates; template modifications are not permitted.
- Page limit: up to 8 pages for text, figures, and tables, plus up to 2 pages of references. CARE allows flexibility up to an absolute maximum of 12 pages including content and references.
- Review mode: double-blind; author identities must be anonymized or the paper can be desk rejected.
- Data declaration: declare the data origin for each CARE 2026 track and any other public/private data used. Required citations and acknowledgments must be included; this information may appear anywhere in the main text.
- Deadlines: paper submission July 27, 2026 at 23:59 Pacific Standard Time; acceptance notification August 10, 2026; camera-ready August 24, 2026.
- Accepted papers: accepted CARE 2026 satellite-event papers will be made available through the MICCAI Society website no earlier than one week before the first conference day. Patent-sensitive work should complete necessary filings before that release.

## Local QA status

- `submission/mosaic.pdf` was rebuilt with `pdflatex`, `bibtex`, `pdflatex`, `pdflatex` on July 25, 2026.
- The rebuilt PDF is parseable and reports 14 pages via `pdfinfo`.
- Because CARE 2026 allows at most 12 pages including references, the current rebuilt PDF is not submission-compliant until shortened.
- The empty JSON files under `submission/results/` are placeholders from the uploaded package and should not be treated as evidence for numerical claims.

## Build

From `submission/`:

```bash
pdflatex -interaction=nonstopmode -halt-on-error mosaic.tex
bibtex mosaic
pdflatex -interaction=nonstopmode -halt-on-error mosaic.tex
pdflatex -interaction=nonstopmode -halt-on-error mosaic.tex
```

## Evidence boundary

Paper claims must first enter `CLAIM_LEDGER.md` and be backed by code, logs, manifests, committed result files, or official receipts. Use `code/source/` for implementation facts only; do not edit it for paper writing unless intentionally refreshing the upstream snapshot. Do not infer missing numerical evidence from placeholder files.
