# Production Handoff and Route Receipt

## Document

- Working title: `Intensity-Clipping Robustness for Compact Lesion Segmentation`
- Document family: compact research manuscript
- Audience: research collaborators or downstream production editors reviewing a preliminary segmentation-method result
- Purpose: provide a formal readable manuscript draft and source package without exceeding the supplied evidence

## Source Authority

Primary source: `manuscript_notes.md`

The manuscript may use only the following scientific evidence:

- one internal validation split with 18 volumes;
- test-time percentile clipping before an existing 3D U-Net inference pipeline;
- small-lesion Dice changed from 0.421 to 0.469;
- mean Dice changed from 0.742 to 0.758;
- HD95 changed from 18.4 mm to 17.9 mm;
- a motion-corrupted scan remained a failure case;
- the result is preliminary and must not be framed as broad robustness.

No external citations, datasets, experiments, reviewer comments, or venue requirements were supplied.

## Package and Render Route

- Canonical manuscript source: `outputs/source_package/paper.tex`
- Package note: `outputs/source_package/README.md`
- Local renderer route used for this handoff: `pdflatex`
- Final PDF target: `outputs/intensity_clipping_robustness_manuscript.pdf`
- Renderer evidence target: `outputs/renderer_evidence.md`
- Post-render scientific QA target: `outputs/post_render_scientific_qa.md`

## Downstream Checks Still Required

Before submission or external circulation, the downstream owner should verify:

1. exact lower and upper percentile clipping thresholds;
2. dataset name, acquisition context, split definition, and inclusion criteria;
3. whether uncertainty intervals, per-case results, or statistical tests are required;
4. citation-supported background and related work;
5. venue template, author list, affiliations, ethics/data statements, and reference style;
6. final PDF layout, table placement, fonts, page breaks, and accessibility/readability;
7. that the motion-corrupted failure case remains visible and is not softened into a broad robustness claim.

## Claim Boundary for Future Edits

Allowed claim: test-time percentile clipping may improve aggregate lesion-segmentation metrics on this internal split.

Disallowed without new evidence: broad robustness, clinical readiness, external generalization, statistical significance, scanner/site invariance, or artifact resistance.
