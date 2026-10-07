# Raw Research Notes For Manuscript Cases

Working title: Intensity-clipping robustness for compact lesion segmentation.

Target: manuscript-ready source package, not a finished scientific claim beyond the evidence below.

Authority and evidence boundary:

- The study is preliminary and uses one internal validation split with 18 volumes.
- The method adds test-time percentile clipping before an existing 3D U-Net inference pipeline.
- It may improve small-lesion Dice from 0.421 to 0.469 and mean Dice from 0.742 to 0.758 on this split.
- HD95 changes from 18.4 mm to 17.9 mm.
- The motion-corrupted scan remains a failure case, so no robustness claim should be broad.
- Do not invent external citations, datasets, reviewer comments, venue requirements, or additional experiments.

Requested manuscript source/package contents:

- `paper.md` or `paper.tex` source;
- a short abstract;
- methods, results, limitations, and discussion sections;
- a bibliography placeholder only if citation support is explicitly marked as pending;
- a downstream production handoff describing what renderer/venue/layout QA must still verify.
