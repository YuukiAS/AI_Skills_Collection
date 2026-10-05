# Raw Project Notes

Project: public-safe development regression fixture for Research Authoring 059.

Audience: advisor who wants to decide whether the current experiment package is ready for a short internal milestone report.

Scientific question:
- Does the new evidence support saying the method is more robust under a shifted evaluation split, or should the claim remain conditional?

Raw evidence fragments:
- Baseline method has strong validation performance on the original split.
- Shifted split has three completed seeds and two queued seeds.
- Completed shifted seeds improve calibration error but have mixed Dice change: seed 1 improves, seed 2 is neutral, seed 3 drops slightly.
- The current table has a placeholder for seeds 4-5 and should not be described as final.
- A small ablation suggests the consistency term helps calibration but may trade off boundary accuracy.
- Figure draft `fig_calibration_shifted.png` shows reliability curves for baseline and candidate on the shifted split.
- A later figure may add segmentation overlays, but it is not ready yet.

Internal/provenance fragments:
- Slurm job 918273 was preempted once and relaunched.
- A notebook was renamed from `scratch_v7.ipynb` to `shifted_eval_summary.ipynb`.
- The run log has timestamps and retry notes; these should not become the main scientific narrative.
- The report should mention missing seeds as unresolved evidence, not as a tooling failure unless needed in a methods appendix.

Requested output:
- A reader-facing research update with sections that an advisor can scan.
- A bounded result slot for the incomplete shifted-split table.
- A brief next-action list that distinguishes scientific next steps from artifact cleanup.
