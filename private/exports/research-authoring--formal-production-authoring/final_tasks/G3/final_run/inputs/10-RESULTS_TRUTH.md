# RESULTS_TRUTH.md

This file records result facts that are currently traceable. Do not promote README text, source comments, preflight checks, or contaminated diagnostics into manuscript results. Leaderboard rows dated 2026-06-01 or later are treated as MoSAIC by explicit author decision recorded in `review/AUTHOR_DECISIONS.md`.

## Confirmed Assets

- MoSAIC paper repository: `/users/a/e/aereinh/MoSAIC/paper`.
- Source evidence snapshot: `/users/a/e/aereinh/MoSAIC/code/source`, commit `d334bd1fb2a99dbbc230510590cd8e3ee08cc377`.
- Canonical local weights: `/users/a/e/aereinh/MoSAIC/code/weights`.
- CARE-side completion package copied into this repository: `review/evidence/20260726_mosaic_paper_results_completion/`.
- CARE leaderboard alignment checked by the main thread: `/users/a/e/aereinh/CARE/results/leaderboard/care2026_validation_submission_alignment_20260726.md`.

## Active Manuscript Baseline

The active manuscript uses the author attachment version of `submission/mosaic.tex` as its retained five-fold-result source. The existing five-fold table values in that attachment, including scar `0.668 +/- 0.022`, lesion union `0.645 +/- 0.024`, and cine-only scar `0.457 +/- 0.038`, are retained for this pass by author instruction. Their table-generation provenance remains unresolved in the current evidence package, so do not expand them into additional claims or replace them with the scar-path audit numbers unless the author explicitly requests that.

## Clean Scar-Path Audit Record

The CARE-side MyoPS MoSAIC scar-path OOF audit remains a traceable audit record. It is not the active manuscript mainline for this author-attachment pass.

Evidence:

- `review/evidence/20260726_mosaic_paper_results_completion/paper_results/cv/main_cv_summary.csv`
- `review/evidence/20260726_mosaic_paper_results_completion/paper_results/cv/myops_fold_metrics.json`
- `review/evidence/20260726_mosaic_paper_results_completion/paper_results/cv/myops_casewise_metrics.csv`

Audit numbers, mean +/- s.d. across five folds:

| Dataset | Model boundary | Label | Dice | HD95 mm | Manuscript status |
|---|---|---:|---:|---:|---|
| MyoPS | MoSAIC scar-path OOF only | myocardium | 0.366 +/- 0.028 | 16.05 +/- 1.65 | evidence/audit record |
| MyoPS | MoSAIC scar-path OOF only | LV | 0.569 +/- 0.102 | 15.28 +/- 3.37 | evidence/audit record |
| MyoPS | MoSAIC scar-path OOF only | RV | 0.324 +/- 0.020 | 20.55 +/- 2.22 | evidence/audit record |
| MyoPS | MoSAIC scar-path OOF only | scar | 0.378 +/- 0.013 | 25.52 +/- 2.02 | evidence/audit record only; do not make active mainline |
| MyoPS | MoSAIC scar-path OOF only | lesion union | 0.337 +/- 0.025 | 29.36 +/- 2.74 | evidence/audit record only; do not make active mainline |
| MyoPS | MoSAIC scar-path OOF only | pure edema | 0.019 +/- 0.043 | 4.81 +/- 10.75 | do not use as edema result |

Required wording boundary: describe these numbers only as a clean MyoPS scar-path out-of-fold audit. Do not describe them as complete final MoSAIC performance, edema-stage performance, CineMyoPS performance, official validation performance, or the current manuscript main result.

## Unsupported Or Unresolved Result Categories

| Category | Current status | Manuscript action |
|---|---|---|
| Attachment five-fold table provenance | unresolved in current evidence package, but retained by author instruction for the author attachment | Keep existing table during this pass; do not add extra untraced claims. |
| Complete final MoSAIC edema-stage five-fold | unsupported beyond the attachment table | Do not add new complete edema-stage claims; fold1-fold4 edema stage rows are missing in the runtime/training manifest. |
| CineMyoPS MoSAIC five-fold provenance | unresolved beyond the attachment table | Keep the attachment table value only; do not add new local CineMyoPS claims. |
| CARE2026 leaderboard as MoSAIC | confirmed by author decision for the eligible OrganAgent rows | Report the best MoSAIC Dice entry per official track; the old edema row is not MoSAIC. |
| Ablation gains | unsupported | Existing fold0 full-data diagnostics are contaminated and diagnostic only. |
| Controlled modality robustness | unsupported | Existing evidence is observational subgroup audit only, not controlled sequence withdrawal. |

## Leaderboard Evidence Boundary

Author boundary: active manuscript should foreground the best MoSAIC official validation entries and should not make edema a negative headline.

Author decision: the eligible OrganAgent CARE2026 leaderboard submissions are MoSAIC. This resolves the rows used in the active manuscript, but does not reassign the old edema row.

The active manuscript should use the best MoSAIC Dice entry for each official validation track:

| Task | Dice | HD | Rank | Time | Manuscript status |
|---|---:|---:|---:|---|---|
| MyoPS scar | 0.6965 | 13.7827 | 13 | 2026-07-06 09:13:49 | Best MoSAIC scar Dice entry by author decision |
| MyoPS edema | 0.5983 | 26.7067 | 74 | 2026-07-06 09:13:49 | Best MoSAIC edema Dice entry by author decision |
| CineMyoPS scar | 0.2069 | 48.7463 | 22 | 2026-06-27 22:35:12 | Best MoSAIC CineMyoPS scar Dice entry by author decision |

Comparator row allowed for careful context only:

| Comparator | MyoPS scar Dice / HD | MyoPS edema Dice / HD | CineMyoPS Dice / HD |
|---|---:|---:|---:|
| nnU-Net validation comparator | 0.6258 / 14.9844 | 0.6691 / 21.0898 | 0.1816 / 52.9706 |

Allowed wording: Compared with nnU-Net, MoSAIC best validation entries improve MyoPS scar, CineMyoPS scar, and mean Dice over the three official tracks from 0.492 to 0.501. Do not claim mean HD improvement when using the best-Dice entries. Do not describe the result as `start`, `final`, or `June-to-July gains` in the active manuscript.

Important boundary: the previously drafted `0.6496` edema Dice / `22.0125` HD row belongs to the old nnU-Net lineage in the leaderboard alignment. Main-thread CARE checks align it to `nnUNet MyoPS + CineMyoPS pathology_direct` with `confidence=confirmed_by_local_readme`, and local manifests identify the MyoPS source as nnU-Net (`combo.myops_model = nnUNet`, `myops.source = nnUNetv2_predict`, or nnU-Net ensemble/prediction directories). Do not report this row as a MoSAIC main result.

## Confirmed Cohort Counts

Evidence: `review/evidence/20260726_mosaic_paper_results_completion/paper_results/cohort/cohort_statistics.json`.

- MyoPS: 220 cases; five folds with 44 validation cases and 176 training cases per fold.
- MyoPS center counts: CenterA 81, CenterB 35, CenterC 45, CenterE 7, CenterF 9, CenterG 8, CenterH 35.
- MyoPS modality availability in the OOF manifest: LGE-only 116, C0+LGE 24, C0+LGE+T2 80.
- CineMyoPS: 64 cases; centers alpha 40 and beta 24; fold validation counts 13, 13, 13, 13, 12.

## Current Manuscript Rule

The manuscript may report the implemented method, retain the author attachment five-fold table without expanding it, retain the scar-path OOF audit as evidence/audit record, and report the best MoSAIC CARE2026 OrganAgent leaderboard Dice entries by author decision. It may report the author-approved official validation entries above with the stated wording boundary. It may not report the old `0.6496/22.0125` edema row as MoSAIC, make `0.378/0.337` the active mainline, restore the Reproducibility Audit Boundary, add clean ablation claims, controlled robustness claims, SOTA claims, or cross-center robustness claims until traceable evidence is added and reviewed.
