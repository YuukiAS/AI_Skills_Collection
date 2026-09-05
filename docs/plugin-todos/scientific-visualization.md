# scientific-visualization — Long-Term TODO

Canonical maintenance inbox for the `scientific-visualization` plugin.

## Open candidates

### Delegate captions/annotations without giving away visual semantics

status: READY_FOR_PROMOTION_AFTER_LANGUAGE_LAYER
source: cross-plugin communication boundary audit, 2026-09-05
proposal: Keep `scientific-visualization` as the owner of visual encoding, axes/scales, panels, uncertainty display, statistical annotations, figure hierarchy and the decision of whether a plot/schematic is scientifically appropriate. After those semantics are frozen, use the canonical generic language layer for figure titles/captions, axis/legend/annotation wording, concise takeaway text and terminology consistency. See `docs/design/READER_FACING_COMMUNICATION_PLUGIN_BOUNDARIES.md`.
required boundary: the language layer may improve wording only; it must not change the scientific comparison, plotted quantity, statistical meaning, axis semantics, uncertainty encoding or figure structure merely to make the text easier to write. Presentation-specific placement/size remains owned by `presentations`.
promotion gate: after task 050 closes and the generic language layer identity is settled, replay one real scientific figure caption/annotation handoff and verify both visual-semantic fidelity and improved reader-facing language.

### Curriculum-driven capability refinement

status: BLOCKED_NEEDS_EVIDENCE
source: user-approved design direction, 2026-09-01
proposal: Learn bounded visualization competencies from visualization textbooks, graphical-perception literature, venue guidance, and strong real figure examples. See `docs/workflows/CURRICULUM_DRIVEN_DOMAIN_PLUGIN_REFINEMENT.md`.
review requirement: text review may validate extracted principles, but production acceptance must include visual review of a real rendered artifact. Mechanical checks such as DPI, font size, contrast, palette status, or export format cannot establish visual quality by themselves.
promotion gate: show that the learned competency improves hierarchy, perceptual clarity, comparison structure, uncertainty encoding, or scientific readability on real figures without overfitting to a single venue/style.

No production change is currently frozen from this candidate.

Use this file for real publication-figure, schematic, poster and figure-QA feedback. Promote only when the issue belongs to scientific visualization rather than Presentation page composition or frontend styling.

## Watch boundaries

- Presentation figure size/placement belongs to `presentations`; underlying plot/figure quality may belong here.
- Generic caption/annotation wording should come from the canonical language layer after figure semantics are frozen; do not fork a second say-it-plain rule set here.
- Do not convert one venue/project palette preference into a global default without repeated evidence.
- Real export/readability/accessibility failures can qualify as severe single-project production failures.
