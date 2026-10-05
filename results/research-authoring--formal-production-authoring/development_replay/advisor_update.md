# Research update: robustness under a shifted evaluation split

## Scientific question and advisor decision

Does the candidate method remain more robust when the evaluation split shifts? The current evidence supports a conditional calibration improvement; overall robustness remains unresolved. We recommend using the package for a short **provisional internal milestone report**, with the incomplete evaluation explicit. Advisor agreement is needed on this provisional scope before treating the package as ready.

## Evidence and interpretation

The baseline has strong validation performance on the original split, according to the notes. This provides context but does not establish robustness under shift. Three shifted-split seeds are complete, with two still queued. The notes describe improved calibration error in the completed seeds, while Dice changes are mixed.

**Bounded result slot — shifted split, incomplete.** The table records qualitative observations only. Numerical baseline/candidate values and uncertainty estimates were not supplied; pending cells are not zeroes or estimated outcomes. Lower calibration error and higher Dice indicate improvement.

| Seed | Evaluation status | Calibration error, relative to baseline | Dice, relative to baseline |
|---|---|---|---|
| 1 | Complete | Improved; value pending | Improved; value pending |
| 2 | Complete | Improved; value pending | Neutral; value pending |
| 3 | Complete | Improved; value pending | Slight decrease; value pending |
| 4 | Queued | Unresolved | Unresolved |
| 5 | Queued | Unresolved | Unresolved |

A small ablation suggests that the consistency term helps calibration but may reduce boundary accuracy. This is a possible trade-off, not an established mechanism. Together with the mixed Dice response, it limits any broader robustness claim.

The notes identify a draft reliability-curve comparison for the shifted split. That figure could help assess calibration differences once checked; it was not available for inspection here. Segmentation overlays are not ready and provide no current evidence about boundary behavior.

## Next actions

- **Scientific:** Complete seeds 4–5, fill the numerical comparison, and summarize variation across all five seeds before revisiting the robustness claim. Document the split, metric definitions, and baseline/candidate evaluation comparability, which the notes do not specify.
- **Scientific:** Check whether the calibration benefit and possible boundary penalty persist in the consistency-term ablation; use the planned overlays to support interpretation once available.
- **Artifact cleanup:** Replace table placeholders only with verified results, check the reliability figure and caption, and retain notebook history and execution logs in author-only provenance.
