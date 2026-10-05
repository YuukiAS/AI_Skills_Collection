# PAPER_STATUS.md

Updated on 2026-07-27 after returning to the author attachment TeX and applying this pass validation-focused edits.

## Current State

- Active manuscript source is `submission/mosaic.tex` restored from the author attachment after commit `d4a2860`.
- The attachment five-fold main table remains active by author instruction. It was not replaced by the clean scar-path audit values.
- Official validation text now foregrounds best MoSAIC validation Dice entries per official track, plus scar/Cine and mean-Dice improvement compared with nnU-Net.
- The old edema `0.6496 / 22.0125` row is aligned by CARE local evidence to nnU-Net MyoPS and is not used as a MoSAIC main result.

## Active Manuscript Result Boundary

Retained from the author attachment:

- MyoPS scar Dice `0.668 +/- 0.022`, lesion union Dice `0.645 +/- 0.024`.
- CineMyoPS scar Dice `0.457 +/- 0.038`.
- These values remain pending table-generation provenance recovery; do not add extra claims beyond the current table/prose.

Official validation rows allowed by author decision:

- Best MoSAIC MyoPS scar validation Dice entry: `0.6965 / 13.7827`, 2026-07-06, rank 13.
- Best MoSAIC MyoPS edema validation Dice entry: `0.5983 / 26.7067`, 2026-07-06, rank 74.
- Best MoSAIC CineMyoPS scar validation Dice entry: `0.2069 / 48.7463`, 2026-06-27, rank 22.
- nnU-Net validation may be used only as a comparator, not as MoSAIC. The active text may report mean Dice improvement from `0.492` to `0.501`, but must not claim mean HD95 improvement from these best-Dice rows.

## Evidence/Audit Record Not Active Mainline

- MyoPS scar-path OOF audit scar Dice `0.378 +/- 0.013`, HD95 `25.52 +/- 2.02` mm.
- MyoPS scar-path OOF audit lesion union Dice `0.337 +/- 0.025`, HD95 `29.36 +/- 2.74` mm.
- Evidence: `review/evidence/20260726_mosaic_paper_results_completion/paper_results/cv/main_cv_summary.csv` and `myops_fold_metrics.json`.

## Required Before Stronger Results

- Table-generation provenance for the attachment five-fold main table.
- Full edema-stage folds 1-4 training/prediction/evaluation artifacts before expanding local edema claims.
- CineMyoPS MoSAIC prediction/GT evaluation artifacts before expanding local CineMyoPS claims.
- Clean five-fold ablation artifacts before any module-causal claims.
- Controlled sequence-withdrawal evaluation before robustness claims.
