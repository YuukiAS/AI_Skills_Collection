# scientific-visualization — Long-Term TODO

Canonical maintenance inbox for the `scientific-visualization` plugin.

## Open candidates

### Delegate captions/annotations without giving away visual semantics

status: READY_FOR_PROMOTION_AFTER_LANGUAGE_LAYER
tracking: #49
source: cross-plugin communication boundary audit, 2026-09-05
proposal: Keep `scientific-visualization` as the owner of visual encoding, axes/scales, panels, uncertainty display, statistical annotations, figure hierarchy and the decision of whether a plot/schematic is scientifically appropriate. After those semantics are frozen, use the canonical generic language layer for figure titles/captions, axis/legend/annotation wording, concise takeaway text and terminology consistency. See `docs/design/READER_FACING_COMMUNICATION_PLUGIN_BOUNDARIES.md`.
required boundary: the language layer may improve wording only; it must not change the scientific comparison, plotted quantity, statistical meaning, axis semantics, uncertainty encoding or figure structure merely to make the text easier to write. Presentation-specific placement/size remains owned by `presentations`.
promotion gate: after task 050 closes and the generic language layer identity is settled, replay one real scientific figure caption/annotation handoff and verify both visual-semantic fidelity and improved reader-facing language.

### Expert-audience visualization must be result-first, and the GPT planner owns the scientific selection

status: NEW
owner: GPT_PLANNER
source: CAT-TRACE real-use failure, 2026-10-28; repeated user rejection of low-information architecture/status/formula visuals for advisor-facing research updates
problem: When the audience is an experienced advisor, collaborator, reviewer, or domain scientist, a visually polished architecture diagram, status card, formula restatement, toy trajectory, or “what is implemented” schematic can still be a poor scientific artifact. Repeated CAT-TRACE planning failures showed that the GPT planner may satisfy the literal request for “a figure” while choosing something that conveys almost no new evidence to an expert audience. This wastes presentation space, makes mature researchers look as if they are being taught basics, and can create the appearance of progress without a substantive result.

required GPT-side behavior:
- Before delegating any scientific figure to Codex or a renderer, identify the actual audience, the claim/evidence the audience should learn, and why a figure or table is the right carrier. For advisor/peer/reviewer audiences, assume substantial domain knowledge unless the user says otherwise.
- For expert-facing research updates, default to evidence-bearing outputs: fitted or simulated recovery, calibration, sensitivity analysis, regime maps, error surfaces, ablations, benchmark comparisons, uncertainty displays, failure-mode scans, or exact quantitative tables. Prefer the artifact that most directly answers the scientific question, not the artifact that is easiest to render.
- Treat architecture diagrams, workflow schematics, formula-only figures, status matrices, implementation cards, and toy examples as secondary. Use them in the main narrative only when the architecture/derivation itself is the scientific contribution or when the audience genuinely needs that structure to interpret a substantive result.
- Do not turn “we implemented X” into a presentation figure merely by arranging X into boxes. If implementation is the real progress, first ask whether there is a numerical validation, calibration experiment, benchmark, stress test, or other evidence that demonstrates the implementation did the intended scientific computation.
- If no substantive expert-facing figure is supported by current evidence, say so. The GPT planner should then propose the smallest scientifically meaningful analysis or experiment that can generate a real result. It must not fabricate an impressive-looking status/architecture/formula visual to hide the absence of evidence.
- “Impressive” must mean high evidence density, a nontrivial quantitative pattern, a meaningful scientific comparison, or a result that changes confidence/decision-making. It must not mean decorative complexity, more boxes, more arrows, more equations, or more visual polish.
- When a user asks what is “actually worth showing,” the GPT planner must rank candidate artifacts by scientific information gained by the intended expert audience. A technically correct but low-information artifact may be explicitly rejected from the main presentation even if it is useful as backup evidence.
- Codex/renderers have no authority to choose the scientific message, analysis, result, comparison, or figure type. GPT must freeze those decisions first; Codex may only execute and visually refine the approved contract.

expert-audience preflight:
1. What will a domain expert learn from this artifact in 20 seconds that they did not already know?
2. Is that learning supported by actual data, simulation, numerical analysis, or a necessary new methodological derivation?
3. Could the same slide be replaced by one sentence without losing evidence? If yes, the figure is probably too weak for the main research narrative.
4. Is the artifact showing a scientific result, or merely showing that software/modules/formulas exist?
5. If the artifact is explanatory rather than evidential, is that explanation truly necessary for this audience?
6. If the current evidence is insufficient, what analysis should be run before asking Codex to make a figure?

required boundary:
- scientific-visualization owns whether the proposed plot/table/schematic is scientifically appropriate and information-dense for the stated audience.
- Domain/statistical reasoning still determines which analysis is scientifically valid; this TODO does not authorize the visualization plugin to invent experiments or estimands outside the research plan.
- presentations owns page-level placement and deck narrative after the scientific artifact itself is selected.
- Codex owns rendering/implementation only after GPT freezes the scientific artifact contract.

promotion gate:
- Replay this rule on at least two expert-facing real research updates from different projects.
- In each case compare the first-pass GPT-selected artifact against a result-first alternative and obtain explicit review that the promoted rule avoids low-information status/architecture/formula visuals.
- At least one benchmark must include the case where the correct GPT action is “there is not yet a worthwhile main figure; run this bounded analysis first.”
- Production acceptance requires inspection of the final rendered artifact and confirmation that its main value comes from scientific evidence rather than explanatory packaging.
### Interactive scientific schematic connectors need actual-render qualitative QA

status: NEW
tracking: #50
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
tracking: #51
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
