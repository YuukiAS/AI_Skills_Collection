# AUTHOR_DECISIONS.md

Date: 2026-07-27

## Latest Author Boundary for Scientific Restructure

This section supersedes earlier wording that would make edema a negative headline or force the manuscript back to the scar-path audit rewrite.

- The active manuscript should foreground official validation performance.
- The current active manuscript source is the author attachment version; keep its main five-fold table structure for this pass.
- The active manuscript should report the best MoSAIC Dice entry for each official validation track, not a start/final or June-to-July process story.
- Compared with nnU-Net, the active manuscript may emphasize scar/Cine endpoint gains and mean-Dice improvement across the three official tracks.
- Do not write `edema remained weaker`, `edema degradation`, or `task-specific trade-off` as an Abstract, Results headline, or Conclusion main sentence.
- If edema relative to nnU-Net must be mentioned, keep it brief in the final Discussion limitation paragraph and immediately state future work: strengthening edema supervision, calibrating edema-zone fusion, and adding inter-slice context.

## Fixed Author Decisions

1. KEEP_AS_ATTACHMENT_BASELINE_PENDING_PROVENANCE: the author attachment five-fold main table.
   Active retained values include MyoPS scar Dice 0.668 +/- 0.022, lesion union Dice 0.645 +/- 0.024, and CineMyoPS scar Dice 0.457 +/- 0.038.
   Boundary: retain the attachment table during this pass, but do not expand these numbers into stronger claims until table-generation provenance is recovered.

2. KEEP_AS_EVIDENCE_AUDIT_NOT_MAINLINE: MyoPS scar-path OOF audit.
   Audit numbers: scar Dice 0.378 +/- 0.013; scar HD95 25.52 +/- 2.02 mm; lesion union Dice 0.337 +/- 0.025; lesion union HD95 29.36 +/- 2.74 mm.
   Boundary: clean scar-path OOF audit only, not complete final MoSAIC and not the active manuscript mainline for this pass.

3. KEEP_AS_MOSAIC_LEADERBOARD_BY_AUTHOR_RULE: CARE2026 OrganAgent leaderboard rows dated 2026-06-01 or later.
   Author rule: all OrganAgent submissions dated 2026-06-01 or later are MoSAIC.
   Allowed rows under this rule:
   - MyoPS scar: 0.6965 Dice / 13.7827 HD on 2026-07-06, best MoSAIC scar Dice entry.
   - MyoPS edema: 0.5983 Dice / 26.7067 HD on 2026-07-06, best MoSAIC edema Dice entry.
   - CineMyoPS scar: 0.2069 Dice / 48.7463 HD on 2026-06-27, best MoSAIC Cine Dice entry.
   Boundary: do not write these as `start`, `final`, or `June-to-July gains`; they are best leaderboard entries per official track.

4. DO_NOT_USE_AS_MOSAIC: old edema leaderboard row 0.6496 / 22.0125.
   Main-thread CARE check: this row maps to `nnUNet MyoPS + CineMyoPS pathology_direct`, with local manifests showing `combo.myops_model = nnUNet`, `myops.source = nnUNetv2_predict`, or nnU-Net prediction directories. It is a comparator-lineage row, not a MoSAIC main result.

5. REMOVE_FOR_NOW: complete edema-stage five-fold performance beyond the attachment table.
   Reason: edema-stage folds 1-4 are missing in the current evidence package.

6. REMOVE_FOR_NOW: CineMyoPS local five-fold performance beyond the attachment table.
   Reason: no local CineMyoPS MoSAIC prediction/GT evaluation artifact exists.

7. REMOVE_FOR_NOW: ablation gains and module-causal claims.
   Reason: no clean five-fold ablation artifact exists.

8. DOWNGRADE_TO_FUTURE_WORK: controlled modality robustness.
   Reason: current evidence is observational subgroup audit only.

9. KEEP: cohort counts and modality availability.
   Reason: confirmed by cohort_statistics.json.

10. KEEP_WITH_SOFTENING: method architecture claims.
    Reason: supported as code/config facts, not performance gains.

## What Still Needs Source Recovery

The remaining important unknown is local training/CV provenance for the attachment five-fold table and inactive draft tables:

- MyoPS scar Dice 0.668 +/- 0.022.
- MyoPS lesion union Dice 0.645 +/- 0.024.
- MyoPS edema Dice 0.349 +/- 0.065.
- CineMyoPS scar Dice 0.457 +/- 0.038.
- Edema-zone and ablation numbers such as 0.634 +/- 0.013 and 0.632 +/- 0.013.

These are not leaderboard numbers. They need local result JSON, fold evaluator logs, or the table-generation inputs that produced the old `submission/tables/main.tex` and ablation tables before claims are strengthened.
