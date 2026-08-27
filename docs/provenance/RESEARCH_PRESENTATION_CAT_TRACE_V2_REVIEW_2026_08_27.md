# Research presentation review notes — CAT-TRACE v2, 2026-08-27

This file records the user's Acrobat review of the CAT-TRACE group-meeting deck version **v2**. It is a project-specific review record, not yet a set of general presentation rules.

The review source is the annotated PDF `group_meeting-v2(1).pdf`, 27 pages. Acrobat contains 74 highlight annotations across pages 2–25 and 27. The user's color convention is approximate rather than absolute: blue is usually a style-system issue; purple is usually unnatural / AI-like wording; yellow and orange are mixed; green was used once for terminology presentation.

## Scope and workflow status

- **Current step:** preserve all v2 complaints and group them by failure type.
- **Do not yet change active presentation rules or `research-presentations/TODO.md`.**
- **Next step:** discuss the review with the user page by page and agree on concrete fixes.
- **Only after that agreement:** extract the genuinely reusable rules, compare them against existing skill/TODO coverage, and update the general presentation guidance through the normal review path.
- CAT-TRACE-specific scientific decisions must stay in this record / TRACE work, not become universal presentation rules.

## External language-style research consulted for the later rule-design step

The user specifically asked for a more systematic treatment of AI-like prose. The following evidence was checked now but is not yet promoted into active rules:

- Juzek & Ward, COLING 2025, documented lexical over-representation in LLM-generated scientific English, including words such as *delve*, *intricate*, and *underscore*. This supports maintaining a lexical warning list, but it does **not** justify treating any single word as proof of AI authorship.
- Broader public editing guidance on AI-like writing also flags stock rhetorical shells and repeated contrastive patterns as warning signs. For this deck, the user's strongest objections are not mainly vocabulary; they are formulaic sentence architecture such as “This is not X; it is Y”, “X does ..., it does not ...”, “not only ...”, meta-commentary about what the slide is doing, and overly compressed label-like prose.
- Microsoft style guidance uses sentence-style capitalization for most titles/headings. This is relevant to the unresolved capitalization inconsistency in the deck, but the final CAT-TRACE / CUHK slide rule still needs to be chosen deliberately rather than copied mechanically.
- MIT/Broad scientific-presentation guidance recommends one main point per slide and titles that convey the page's main message. This supports a stronger slide-title contract, but the exact CUHK template convention still needs a project decision.

## Annotation inventory by page

### P1

No Acrobat complaint annotation.

### P2 — Biodiversity surveys reveal an expanding species space

1. **Rendered overlap was not caught before delivery.** The labels “known catalogue taxa” and “catalogue-external” overlap in the diagram. User explicitly asks for a pre-delivery rendered check that can catch this even without manual screenshots.
2. **Terminology needs a defined presentation style.** `OTU (operational taxonomic unit)` raises a larger question: when a domain term deserves its own mini-slide / callout versus a compact same-slide definition.
3. **A biological example may need a real image.** `arthropod` is understandable to specialists but a small image may reduce audience effort.
4. **Example wording should use audience language.** For a spoken example, “columns appearing in exactly one sample” feels too matrix-centric; use the real-world object once the concept is grounded.

### P3 — Two types of future discovery

1. **“Victoria example” is rejected as unnatural project shorthand.** Same issue applies to the highlighted “Malagasy example”.
2. **COI appears before it has been explained.** Every domain-specific term must be checked against previous pages, not merely expanded somewhere later.
3. **Example-label wording is inconsistent across the deck.** “Victoria example”, “Malagasy example”, and later “Victoria plant examples” should not coexist as ad hoc variants.

### P4 — TRACE: keeping an infinite response space locally sparse

1. **The sentence defining `p` is technically correct but unnatural.** User prefers direct speech-like scientific explanation: define `p`, then say explicitly that the infinite model is approximated with a finite truncation.
2. **Problem and solution are separated badly.** The fixed-prior failure is presented as a bullet, but the corresponding mechanism / why the scaling fixes it is not paired clearly enough.
3. **Meta-slide narration is unacceptable.** “This page explains ...; the next page shows ...” is explicitly rejected and should be caught automatically before delivery.

### P5 — TRACE: calibrating expected richness as `p` grows

1. **“Two sources are distinct” should become visible structure, not compressed prose.** If there are two logically separate points, use a two-item list / two-step structure.
2. **Formula order is hard to follow.** Several equations are stacked without enough narrative connection; related equations should be grouped, and minimal explanatory text should establish why each equation follows from the previous one.
3. **Mathematical slides need an explicit layout rule.** “More equations” is not automatically clearer; use line grouping, alignment, and textual bridges based on derivational structure.

### P6 — HMSC and CORAL

1. **CORAL flow diagram was highlighted without a comment, indicating dissatisfaction with the current diagram execution.** Later comments make clear that box-and-arrow diagrams need a stronger necessity and geometry check.
2. **HMSC needs a reason for appearing in the story, not only a definition.** The slide should state why it is a relevant baseline/reference and what it is good at, with appropriate citation / status.
3. **The sentence “CORAL helps ... It does not ...” is rejected as strongly AI-like.** The scientific boundary is valid; the rhetorical shell is not.

### P7 — CAT-TRACE: one model with a finite catalogue and an open tail

1. **Peer headings use inconsistent font treatment.** “Finite catalogue component” does not visually match the opposite side.
2. **Residual dependence and discovery target are dropped below the two columns without a heading.** User questions both the lack of a title and the reflexive use of two columns.
3. **Need a clear rule for when two columns are justified.** Two columns should encode a true parallel comparison, not be the default layout for any two model pieces.

### P8 — CAT-TRACE architecture

1. **A highlighted phrase (“whether / not observed in first n”) is visually / linguistically awkward even without a typed comment.**
2. **Arrow geometry failed.** Short, overlapping arrows and connectors were not caught by QA. The entire diagram needs connector spacing / overlap / direction validation.

### P9 — Matching observed features to the catalogue

1. **Avoid symbolic shorthand when words are clearer.** The isolated `+` in “sequence + taxonomy-like labels” is called out as unnecessary notation in prose/table cells.
2. **“currently hard/partial only” is rejected as AI/project-status shorthand.** It sounds like an internal note rather than audience-facing scientific wording.

### P10 — Identity-aware catalogue borrowing

1. **Text does not fit inside the component boxes.** Basic rendered containment/alignment should have failed QA.
2. **Raw code / encoding names are unacceptable on audience slides.** `Poll_Abiotic`, `Disp_Wind`, `Glycophyte` are implementation field names; slides should show complete human-readable trait descriptions.
3. **Example naming is inconsistent.** “Victoria plant examples” conflicts with earlier “Victoria example”. User wants one consistent example convention across the deck.

### P11 — What information exists before a species is discovered?

1. **Capitalization of table headers / first column is unresolved.** Need one fixed capitalization convention for slide tables.
2. **Many table cells sound compressed and machine-written.** Examples the user dislikes include telegraphic fragments such as `generally unavailable`, `only coarse mark if modeled`, `unavailable without later placement`, `not defensible before identity exists`. Later revision must identify which cells need full human phrasing and which can remain terse labels.

### P12 — From one TRACE tail to several marked groups

1. **Examples need a dedicated visual treatment.** Instead of a loose label “Malagasy order-level examples”, consider one explicit example callout or a clearly delimited example block.
2. **The closing sentence is AI-like and poorly ordered.** In particular, ending with “not only how many OTUs will appear” feels like generated contrastive rhetoric.
3. **The main equation is too small.** If it is the core scientific object, it should dominate the slide.
4. **New notation should be visually distinguished.** Color or another controlled emphasis can show which group-specific terms are new relative to original TRACE.

### P13 — Residual dependence

1. **The HMSC vs CAT-TRACE comparison is badly laid out.** User again questions default two-column composition.
2. **“This is not just a different factor notation” is explicitly rejected as AI-like.**
3. **“Residual association is ..., not evidence of ...” is also rejected as AI-like.** Scientific caution is needed, but the contrastive template is not.

### P14 — Priors for the open tail and residual factors

1. **“Part 1 / Part 2” needs a rule.** User questions when `Part` is appropriate versus using descriptive subheads or a sequential list.
2. **Mathematical environment choice needs a standard.** User accepts the current multi-line equations but wants a rule for when to use ordinary display math, `align`, or `cases`.
3. **The explanatory paragraph may be better as bullets.** Need a rule for when short consequence statements should be bullets rather than paragraph prose.

### P15 — Theorem: group-marked open-tail richness

1. **One theorem is not enough for the current theory section.** User expects the deck to consider the full set of theorem/proposition results rather than presenting a single theorem as the whole theory contribution.
2. **“Why this matters” is explicitly rejected as AI-like / generic heading language.**
3. **“the theorem says ...” is rejected as unnatural spoken/scientific phrasing.**
4. **“G=1 ... preserves TRACE calibration” may be too absolute.** Scientific strength/qualification must match what is actually proved.

### P16 — Proof idea and relation to TRACE

1. **Do not call it “Proof idea”.** User wants the actual proof / proof structure rather than a loose “idea” label on a statistics group-meeting slide.

### P17 — Discovery and marginal preservation

1. **“Under hard matching” is questioned as unnecessary lead-in.** If hard and soft matching are separate cases, structure them explicitly rather than using repeated sentence-openers.
2. **Meaning of formula components is placed after the equation in awkward prose.** Prefer introducing the two terms before the formula or using mathematical annotation such as underbraces when appropriate.
3. **Hard vs soft matching should be a list / parallel structure, not two inline prose fragments.**
4. **The sentence explaining that the decomposition is “scientifically important but mathematically ...” is questioned as unnecessary audience-facing self-commentary.**
5. **“Open theory question:” exposes an unresolved style rule.** Need a standard for when a bold inline lead-in is acceptable versus when a true subheading followed by a new line is required.

### P18 — Simulation 1A

1. **The main figure is slightly too small.** Need an objective figure-size / legibility acceptance rule rather than ad hoc trial and error.
2. **Capitalization inside the right-side fact list is inconsistent (`at ...`).**
3. **Theoretical total target `10.822` is dropped without derivation/context.** Since there are three groups, the audience needs to see where the total comes from, possibly with a small table or visible summation.
4. **“this is an oracle ... not a fitted ...” is explicitly rejected as an overused AI contrast template.**

### P19 — Simulation 1B

1. **The standalone `n` and `m` line is disconnected from the design list.** If it is the most important setup, it needs a clear structural role; otherwise integrate it into a compact design block.
2. **Metrics are dumped as terminology.** Each metric should communicate what aspect of performance it measures and why more than one metric is needed.
3. **The sentence explaining `n_max=1000` is scientifically fine but stylistically AI-like.** Need to isolate the rhetorical pattern causing that impression.
4. **Simulation / Dataset title capitalization needs to be consistent.**
5. **`1B` has inconsistent glyph sizing between numeral and letter.** Typography must be checked visually, not only syntactically.

### P20 — Simulation 2

1. **Ablation options separated by vertical bars are unacceptable.** Parallel model variants need a proper visual/list structure.
2. **Metrics again appear as an unexplained list.** Brier score, log score, PR-AUC, coverage must each have a purpose in the experiment.

### P21 — Simulation 3

1. **“Low-rank truth uses rank 3 or rank 5” is under-explained.** Audience needs to know which matrix/object has that rank and why those values matter.
2. **The `n` / `|W|` grid is again dropped as standalone notation with no narrative role.** Same structural problem as P19.
3. **Questions need a dedicated style.** `Core question:` should not be invented slide by slide; capitalization and header treatment must be standardized.
4. **The final working-set sentence sounds AI-like.** User specifically asks whether the `rather than ...` construction and punctuation contribute to that feel.

### P22 — Dataset 1: Finland airborne fungi

1. **Images are too small.** Dataset-image sizing needs a reusable acceptance rule.
2. **Right-side prose is hard to scan.** It mixes sampling explanation, OTU caveat, dimensions, rarity counts, covariates, and study purpose in one column.
3. **Repeated `This ...` sentence openings are explicitly disliked.** Dataset pages should use a human scientific structure rather than explanatory chatbot prose.

### P23 — Dataset 2: Malagasy arthropod metabarcoding

1. **`Main question:` needs the same standardized question style as P21.**
2. **Inline arrows in body text are rejected.** Arrows should be reserved for real diagrams / transformations with explicit semantics; ordinary prose should not use decorative mini-process arrows.
3. **Capitalization / naming of Simulation vs Dataset titles is inconsistent across pages.**
4. **Images are too small.**
5. **One caption for multiple unrelated panels is not informative enough.** Captions must actually identify what each panel shows.

### P24 — Victoria plant communities

1. **`30,955 × 1,116 → 25,955 × 622` is not self-explanatory.** The transformation must name what is being filtered and why.
2. **Semicolon-separated covariate and trait lists are hard to read.** Need a standard format for presenting variable groups on slides.
3. **“This is not the main ... It checks ...” is explicitly rejected as AI-like.**
4. **Title naming regressed: Dataset 1 and 2 have `Dataset`, page 24 does not.**
5. **Images / captions are again inadequate.** User reports poor sizing, missing/weak captions, and inconsistency with the previous two dataset pages.

### P25 — Questions for discussion

1. **A/B/C options are unexpectedly centered.** Option alignment must be standardized.
2. **Option capitalization is unresolved.**
3. **“Current theorem solves ...” is rejected as unclear / low-value wording.**
4. **Question 2 abandons the A/B/C structure used by question 1.** All discussion questions should use the same option grammar if they are meant to be parallel decisions.
5. **`first-paper` wording is rejected.** It assumes a future second paper and sounds like internal project planning rather than advisor-facing science.
6. **Question 3 puts A/B/C on one line, creating a third formatting style on the same slide.** Strong consistency failure.

### P26

No Acrobat complaint annotation.

### P27 — References

1. **Reference text is still too small.** Use the full page more efficiently before reducing font size.

## Failure categories and affected pages

### A. Missing / weak presentation style system

The largest root cause. The deck lacks a fixed rule for recurring object types, so each page invents local formatting.

Affected pages: **P2, P5, P7, P10, P11, P12, P13, P14, P17, P18, P19, P20, P21, P23, P24, P25**.

Subproblems:

- terminology definition / callout style — P2, P3;
- example style — P2, P3, P10, P12;
- question style — P17, P21, P23, P25;
- heading vs bold inline lead-in — P14, P17, P21, P23;
- bullet vs paragraph — P5, P14, P22, P24;
- single-column vs two-column — P7, P13;
- table capitalization / label casing — P11, P18, P19, P23, P25;
- equation layout (`display`, `align`, `cases`, annotation) — P5, P14, P17;
- arrow usage — P6, P8, P20, P23, P24;
- metric presentation — P19, P20, P21;
- variable-list presentation — P24;
- dataset / simulation title pattern — P19, P23, P24;
- option / A-B-C decision layout — P25.

### B. Cross-slide inconsistency

Affected pages: **P3, P7, P10, P11, P18, P19, P23, P24, P25**.

Examples:

- `Victoria example` / `Malagasy example` / `Victoria plant examples`;
- peer component headings using different font treatments;
- Dataset 1 / Dataset 2 / unnumbered Victoria page;
- inconsistent capitalization of Simulation/Dataset subtitles;
- question options switching among centered A/B/C, prose-only, and inline A/B/C;
- inconsistent list-item capitalization.

### C. Rendered visual QA failures

Affected pages: **P2, P7, P8, P10, P12, P13, P18, P19, P22, P23, P24, P27**.

Observed failures:

- overlapping labels — P2;
- inconsistent font / uncontained text — P7, P10;
- overlapping / too-short connectors — P8;
- key equation too small — P12;
- weak two-column balance — P7, P13;
- main result / dataset figures too small — P18, P22, P23, P24;
- weak or missing multi-panel captions — P23, P24;
- mixed-size title token (`1B`) — P19;
- references unnecessarily small — P27.

### D. Unnatural / AI-like wording

Affected pages: **P3, P4, P6, P9, P11, P12, P13, P15, P17, P18, P19, P21, P22, P24, P25**.

Specific patterns called out by the user:

1. **Meta-commentary about the slide itself**
   - “This page explains ...; the next page shows ...” — P4.
2. **Formulaic negative contrast**
   - “CORAL helps ... It does not ...” — P6;
   - “This is not just ...” — P13;
   - “..., not evidence of ...” — P13;
   - “this is an oracle ..., not a fitted ...” — P18;
   - “This is not the main ... It checks ...” — P24.
3. **Generic explanatory headers / shells**
   - “Why this matters” — P15;
   - “the theorem says ...” — P15;
   - “This decomposition is scientifically important, but mathematically ...” — P17.
4. **Internal/project-status shorthand**
   - “currently hard/partial only” — P9;
   - “for advisor feedback rather than claimed ...” — P19;
   - `first-paper` — P25.
5. **Over-compressed telegraphic table prose**
   - `generally unavailable`, `only coarse mark if modeled`, `not defensible before identity exists` — P11.
6. **Generated contrastive endings**
   - “..., not only how many OTUs will appear” — P12;
   - “... rather than forcing all 255k OTUs ...” — P21.
7. **Repeated demonstrative openings**
   - repeated `This ...` on dataset prose — P22.
8. **Project-location labels masquerading as prose**
   - `Victoria example`, `Malagasy example` — P3.

Important: the later general rule should target **sentence architecture and rhetorical function**, not merely ban a few words. A lexical warning list can be a secondary detector, not the sole solution.

### E. Audience comprehension / domain grounding failures

Affected pages: **P2, P3, P4, P6, P9, P10, P18, P19, P20, P21, P22, P23, P24**.

Examples:

- COI used before explanation — P3;
- `p` described in an unnatural abstract way — P4;
- HMSC introduced without enough reason for inclusion — P6;
- raw implementation trait names shown to audience — P10;
- theoretical total target appears without decomposition — P18;
- metric names given without their inferential purpose — P19, P20;
- low-rank truth / rank object undefined — P21;
- dataset pages mix too many unprioritized facts — P22;
- body-arrow pipeline tries to substitute symbols for explanation — P23;
- raw-to-filtered matrix transformation is unexplained — P24.

### F. Scientific logic / completeness issues

Affected pages: **P4, P5, P6, P15, P16, P17, P18, P19, P20, P21, P25**.

Examples:

- problem and solution relationship not explicit enough — P4;
- derivation order unclear — P5;
- comparator's scientific role insufficiently motivated — P6;
- theory section appears to have only one theorem — P15;
- strength of `G=1` reduction statement may exceed what is actually established — P15;
- “Proof idea” undersells what a statistics meeting needs — P16;
- discovery partition is over-framed as theory rather than shown honestly — P17;
- oracle target lacks visible group-level calculation — P18;
- simulation metrics are not tied to claims — P19, P20, P21;
- discussion question wording should expose real choices consistently — P25.

### G. Internal implementation / project language leaking into slides

Affected pages: **P9, P10, P19, P25**.

Examples:

- `currently hard/partial only`;
- `Poll_Abiotic`, `Disp_Wind`, `Glycophyte`;
- `advisor feedback rather than claimed ...` phrasing;
- `first-paper`.

### H. Mathematical layout and notation presentation

Affected pages: **P5, P12, P14, P17, P24**.

Issues:

- formulas stacked without narrative grouping — P5;
- central equation too small and new notation not emphasized — P12;
- no explicit rule for `align` / `cases` / ordinary display math — P14;
- formula components explained awkwardly after the equation — P17;
- naked matrix-dimension arrow used where named filtering steps are needed — P24.

### I. Figures, captions, and visual evidence

Affected pages: **P2, P18, P22, P23, P24, P27**.

Issues:

- real-world image may help biological grounding — P2;
- main simulation figure slightly too small — P18;
- dataset figures too small — P22–P24;
- captions do not identify multiple panels adequately — P23, P24;
- references do not use available page area — P27.

## Root-cause summary to resolve before more Codex editing

The user's dissatisfaction is not a list of 74 isolated defects. Most defects trace to five missing controls:

1. **No stable object-style system.** Recurring slide objects (term, example, question, theorem, proof, metric, variable list, comparison, options, caption) are styled ad hoc.
2. **No deck-wide consistency pass.** The deck is checked locally but not audited for naming, capitalization, typography, list grammar, and repeated archetypes across all pages.
3. **No robust human-language pass.** Scientifically correct English is being accepted even when it sounds generated, project-internal, telegraphic, or unlike a researcher speaking to colleagues.
4. **No semantic audience check.** Undefined domain terms, code fields, metrics, dimensions, and simulation settings survive because mechanical correctness is mistaken for comprehensibility.
5. **Rendered QA is too weak.** Overlap, connector geometry, figure size, caption utility, box containment, and reference-font size pass even though they are obvious when projected.

These five controls should become the organizing framework for the next discussion. The exact universal rules should be written only after the user approves the concrete v2 fixes.
