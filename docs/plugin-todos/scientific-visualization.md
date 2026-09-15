# scientific-visualization — Long-Term TODO

Canonical maintenance inbox for the `scientific-visualization` plugin.

## Open candidates

### Delegate captions/annotations without giving away visual semantics

status: READY_FOR_PROMOTION_AFTER_LANGUAGE_LAYER
source: cross-plugin communication boundary audit, 2026-09-05
proposal: Keep `scientific-visualization` as the owner of visual encoding, axes/scales, panels, uncertainty display, statistical annotations, figure hierarchy and the decision of whether a plot/schematic is scientifically appropriate. After those semantics are frozen, use the canonical generic language layer for figure titles/captions, axis/legend/annotation wording, concise takeaway text and terminology consistency. See `docs/design/READER_FACING_COMMUNICATION_PLUGIN_BOUNDARIES.md`.
required boundary: the language layer may improve wording only; it must not change the scientific comparison, plotted quantity, statistical meaning, axis semantics, uncertainty encoding or figure structure merely to make the text easier to write. Presentation-specific placement/size remains owned by `presentations`.
promotion gate: after task 050 closes and the generic language layer identity is settled, replay one real scientific figure caption/annotation handoff and verify both visual-semantic fidelity and improved reader-facing language.

### Interactive scientific schematic connectors need actual-render qualitative QA

status: NEW
source: Asteria 2.0 / CAT-TRACE real use, 2026-09-13 to 2026-09-14; corroborated by the user's private official ChatGPT export audit (raw conversations are not committed here)
evidence: Asteria repeatedly reached late QA with user-visible graph defects involving arrow endpoints touching the wrong part of cards, connectors crossing avoidably, labels and cards crowding paths, visually awkward relation grammar, and broken/weak math presentation. The Asteria repo subsequently added `docs/design/SCIENTIFIC_GRAPH_VISUAL_SYSTEM.md` plus developer visual self-QA, which is evidence that the failure class is real but does not by itself prove a generic Scientific Visualization rule is already needed or consumed.
problem: In an interactive scientific model map, connector routing, endpoint placement, label grouping and math rendering are not merely frontend decoration: they communicate model dependency, lineage or evidence structure. Mechanical DOM/bbox checks and generic test PASS can miss a diagram that is obviously misleading, cluttered or unreadable at normal scale.
project-specific context: Asteria's current open-chevron arrow style, exact spacing values, CAT-TRACE entities and its Architecture/Lineage/Evidence view grammar are project-specific. They must not become a universal figure style.

Planner triage before promotion:

- First determine the ownership boundary with Frontend Design. Generic component craft, interaction states, responsive UI and whole-screen product composition remain Frontend Design concerns; Scientific Visualization should own only the scientific schematic semantics and visual encoding quality that would remain relevant in another scientific graph/diagram product.
- Check whether the existing curriculum-driven candidate already covers this through schematic/figure hierarchy and real-render review. If yes, merge this case as evidence rather than adding a second production mechanism.
- Any future production rule should require direct inspection of the final rendered schematic at intended scale and should evaluate semantic routing, endpoint correctness, label/edge readability and math rendering, while avoiding Asteria-specific geometry prescriptions.
- Before calling it generic, replay against at least one additional scientific schematic/graph task or obtain independent evidence that the same failure mode exists outside Asteria. A severe single-project failure may justify earlier promotion only if the boundary is clear and the regression can be stated without encoding Asteria's style.

### Curriculum-driven capability refinement

status: BLOCKED_NEEDS_EVIDENCE
source: user-approved design direction, 2026-09-01
proposal: Learn bounded visualization competencies from visualization textbooks, graphical-perception literature, venue guidance, and strong real figure examples. See `docs/workflows/CURRICULUM_DRIVEN_DOMAIN_PLUGIN_REFINEMENT.md`.
review requirement: text review may validate extracted principles, but production acceptance must include visual review of a real rendered artifact. Mechanical checks such as DPI, font size, contrast, palette status, or export format cannot establish visual quality by themselves.
promotion_gate: show that the learned competency improves hierarchy, perceptual clarity, comparison structure, uncertainty encoding, or scientific readability on real figures without overfitting to a single venue/style.

No production change is currently frozen from this candidate.

Use this file for real publication-figure, schematic, poster and figure-QA feedback. Promote only when the issue belongs to scientific visualization rather than Presentation page composition or frontend styling.

## Watch boundaries

- Presentation figure size/placement belongs to `presentations`; underlying plot/figure quality may belong here.
- Generic caption/annotation wording should come from the canonical language layer after figure semantics are frozen; do not fork a second say-it-plain rule set here.
- Do not convert one venue/project palette preference into a global default without repeated evidence.
- Real export/readability/accessibility failures can qualify as severe single-project production failures.
