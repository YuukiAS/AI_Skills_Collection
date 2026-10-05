# MoSAIC G3 submission package

Source: `YuukiAS/MoSAIC_Paper@590bfbac1450fbab5e4ca8ce77c877ece845f094`, canonical manuscript `submission/mosaic.tex`. The materialized input subset is the complete authority used for this historical CARE 2026 task. Available input hashes match `MATERIALIZED_G3_SOURCE_SUBSET.json`; the historical baseline PDF is described there but was not supplied. No source repository files were modified.

Output identity: `G3_PACKAGE`, the revised anonymous CARE 2026 LNCS manuscript package. It contains exactly `mosaic.tex`, `refs.bib`, `figures/fig1_original_redraw.pdf`, `llncs.cls`, `splncs04.bst`, `mosaic.pdf`, and this manifest. This manifest is a production handoff record, not manuscript content for reviewers.

## Build and page control

Built with pdfTeX 1.40.21 / TeX Live 2020 and BibTeX 0.99d. From this package directory, the portable build route is:

```bash
pdflatex -interaction=nonstopmode -halt-on-error mosaic.tex
bibtex mosaic
pdflatex -interaction=nonstopmode -halt-on-error mosaic.tex
pdflatex -interaction=nonstopmode -halt-on-error mosaic.tex
```

In this environment, `TEXMFVAR` and `TEXMFCONFIG` were redirected to writable temporary directories. Compilation auxiliaries and inspection renders stayed outside the deliverable package. No shell escape is required.

The final searchable PDF is **10 pages total**, including references and all three retained method appendices, within the frozen absolute maximum of **12 pages**. The project records a 14-page historical baseline; that PDF was not independently rebuilt as a baseline here. Compression shortens the abstract, introduction, related work, repeated method explanations, table-value narration and conclusion. The leaderboard now pairs Dice/HD in four columns while preserving every value. All nine local main-table rows and their structure are retained. Unsupported disabled ablations, modality-withdrawal results, unused result macros and an inactive missing figure were removed from the source. No margins, global font sizes, line spacing or LNCS layout definitions were changed.

## Production checks

- **Double blind:** anonymous author, running author and affiliation; no author institution, team account, repository URL or private path appears in the manuscript. PDF author metadata is empty. The original figure was inspected for identifying content. Bibliographic authors and public dataset acknowledgments remain intact.
- **LNCS unchanged:** `llncs.cls` and `splncs04.bst` are byte-identical to the frozen inputs. The manuscript uses `\documentclass[runningheads]{llncs}` and `splncs04` without layout overrides.
- **Data origin and declaration:** the Experiments section identifies CARE-2026 CARE-Myocardium, both MyoPS and CineMyoPS cohorts, declares no other data, preserves the no-pretraining statement, acknowledges the challenge organizers and retains all four required data citations (`zhuang2019multivariate`, `qiu2023myopsnet`, `ding2023aligning`, `ding2025cinemyops`). No unsupported ethics, funding or consent declaration was invented.
- **Citations:** all 28 active citation keys resolve; `refs.bib` is byte-identical to the input. BibTeX completes without missing-entry warnings. Citation checking here establishes source preservation and build resolution, not an independent external bibliographic or claim-support audit. Sparse publication metadata in inherited entries remains unchanged.
- **Figure and cross-references:** the original vector figure is byte-identical and its relative path exists. Its caption describes the three branches and clarifies that final pure edema excludes scar from the injury zone. All 10 active labels and all references resolve; no disabled table or missing qualitative figure is active. Formulas and method appendix labels are preserved.
- **Artifact inspection:** the full extracted manuscript text and rendered pages were inspected for claim consistency, layout, tables, equations and figure placement. The PDF is searchable, unencrypted and readable. The figure retains its dense original lettering and can be enlarged in a PDF viewer.

## Remaining evidence limitations

The attachment five-fold table is retained under explicit author authority, with unresolved table-generation provenance stated in the abstract, table caption, results and limitations. No audit numbers replace its active values. Complete edema-stage folds 1–4 and local CineMyoPS prediction/ground-truth evaluation artifacts are unavailable; final checkpoint training manifests and exact seeds remain unresolved. Seed 3407 is therefore described as a configuration default, not a confirmed seed for every run.

Official validation uses only the approved best-Dice entries: MyoPS scar 0.6965/13.7827, MyoPS edema 0.5983/26.7067 and CineMyoPS scar 0.2069/48.7463 (Dice/HD). The nnU-Net rows remain comparator rows. The allowed mean-Dice change 0.492 to 0.501 is preserved without claiming mean-HD improvement. No old misattributed edema row, new ablation result, module-causal gain, SOTA claim or controlled/cross-center robustness claim is introduced. These local production checks do not replace the frozen independent G3 reviewer decision.

The frozen class with amsmath emits the benign `Unable to redefine math accent \vec` warning; hyperref omits title line-break tokens from PDF strings. Neither warning produces missing text, undefined citations or unresolved references.

**No live submission occurred.** Nothing was uploaded to OpenReview or another submission service.

## File identity (SHA-256)

- `mosaic.tex`: `04858c2d6677ed0563cbc5a3a975d7935c24aa3d64de87cef10aa5de47bbfce5`
- `refs.bib`: `5c9ce4bff4e4669c82ed9be87cffa63a864dcd5a049ce855b0fe7efeea2bfecd`
- `figures/fig1_original_redraw.pdf`: `60f78983eee2cbd238510ec97b558e6bab5bc5c521d58dbc501f6634d3edc7ac`
- `llncs.cls`: `a3cfe775b394aba8db8fbb54b8920ecbb12f4532cf787cd6d9b04712f58d0d1a`
- `splncs04.bst`: `f36c3a17e5304a692706359aafa9de709395a085e579eb47c027095aeaa35174`
- `mosaic.pdf`: `8dddea5921b08b95a0400b3057094f6d950506f34e2d17ca6abb5e985b2a9652`
