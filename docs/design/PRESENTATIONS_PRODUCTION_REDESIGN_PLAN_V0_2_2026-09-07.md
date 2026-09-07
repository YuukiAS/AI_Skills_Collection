# Presentations Production Redesign Plan

**Plan version:** 0.2  
**Status:** READY FOR CRITIC REVIEW / NOT EXECUTION AUTHORIZATION  
**Date:** 2026-09-07  
**Repository:** `YuukiAS/AI_Skills_Collection`  
**Repository baseline reviewed:** `c827037b253a18a928103f22936ddb3477c74a73`

This is a complete versioned architecture plan. It revises, but does not overwrite, `PRESENTATIONS_PRODUCTION_REDESIGN_PLAN_V0_1_2026-09-07.md`. Later Critic revisions must be recorded as `v0.3`, `v0.4`, and so on rather than silently replacing this file.

The v0.1 Critic verdict was `REVISE — narrow revision; main architecture accepted`. The required correction is precise: the semantic storyboard must decide what the audience should understand and in what order, while a separate page-composition planner decides how that meaning occupies a slide. The storyboard must not become a renamed `deck-plan.yaml` containing layout families, scientific-object types, two-column instructions, or density settings.

`CLEAR_LANGUAGE_PRODUCTION_REDESIGN_PLAN_V0_2_2026-09-06.md` is still absent from the reviewed repository baseline. This plan therefore preserves an explicit interface to a future generic language layer without treating that absent file, or `READER_FACING_COMMUNICATION_PLUGIN_BOUNDARIES.md`, as frozen production truth.

---

## 0. Why this plan exists

The current presentations plugin contains real capabilities: source fidelity, audience-aware planning, page jobs, exact-template handling, rendered review, bounded repair, and preservation of accepted elements during revision. The central problem is not that all of this work was wrong. The problem is that the architecture has mixed four responsibilities:

1. deciding what the audience must understand or decide;
2. deciding how each idea should be represented spatially and visually;
3. producing an artifact through Beamer, PPTX, Slides, or another renderer;
4. proving completion through schemas, packets, validators, fixtures, and reviewer decisions.

CAT-TRACE v4–v8 repeatedly showed that more complete packets and more local checks did not prevent a deck from remaining difficult to follow. CAT-TRACE v9 improved mainly because the task fixed the audience, page job, prerequisite knowledge, reason for introducing each term, and intended takeaway before writing visible copy. CAT-TRACE v10–v14 then showed that local page correctness still does not guarantee cross-page continuity, useful diagrams, claim-first figures, or honest review scope.

V0.1 correctly moved the architectural center away from exact CUHK generation, gold layouts, and schema completeness toward a semantic storyboard. The Critic identified one remaining structural ambiguity: v0.1 allowed the page brief to carry the scientific object, composition intent, and density budget while the page-composition planner also owned form, hierarchy, density, and spatial organization. That overlap would let a future implementation create `semantic_storyboard.yaml` with fields such as `RESULT_FIGURE`, `two-column`, and `density=medium`, then continue the old architecture under a new name.

**Core judgment:** the main direction is accepted. Production must use a strict two-step contract:

```text
what the audience must understand, and why this page follows now
  -> how that meaning should occupy this page
  -> language/visual asset realization
  -> renderer adapter
  -> rendered review
```

The first step is semantic and sequential. The second is compositional and spatial. Neither may silently take over the other.

---

## 1. Verified repository reality

### 1.1 Current plugin composition

| Item | Verified repository fact |
|---|---|
| Marketplace plugin | `presentations` |
| Plugin version | `0.3` |
| Capability status | `baseline` |
| User-visible source skills | `research-presentations`, `business-presentations` |
| Shared implementation | `skills/tools/documents-media/presentations/shared/**` |
| Dominant research route | exact CUHK Beamer/PDF in the current desktop profile |
| Current broad planning artifact | `shared/deck-plan.schema.json` / `deck-plan.yaml` |
| Executable research entry | `generate_research_presentation_production_entry.py` |
| Existing-deck gate | `validate_existing_deck_revision_entry.py` |
| Main real-use evidence | CAT-TRACE v4–v14 feedback, current-cycle reports, Reviewed Handoff history, plugin TODO |

### 1.2 Current production behavior

**VERIFIED FACT.** `research-presentations/SKILL.md` combines task routing, Research State, Evidence Board, page archetypes, scientific objects, deck planning, format routing, exact CUHK behavior, language handoff, reference-library use, visual review, and existing-deck revision rules.

**VERIFIED FACT.** `deck-plan.schema.json` mixes semantic intent, evidence traceability, visual intent, layout hints, renderer/template choices, fallback policy, notes, and QA. It is therefore not a neutral interchange layer.

**VERIFIED FACT.** `generate_research_presentation_production_entry.py` is a real executable route but is strongly coupled to exact CUHK Beamer, a research-group-meeting bundle, composition selection, rendering, manifests, contact sheets, and a bounded quality loop. It is not a universal presentations front door.

**VERIFIED FACT.** `validate_existing_deck_revision_entry.py` checks whether a revision packet contains baseline, accepted-element, first-use, rendered-QA, language, and review evidence. It does not itself diagnose, edit, or produce the revised deck.

### 1.3 Real production feedback

**VERIFIED FACT.** CAT-TRACE feedback repeatedly found the following failures despite valid files and increasingly complete QA artifacts:

- a page existed without a clear reason for appearing at that moment;
- a term was defined but the audience still did not know why it mattered now;
- each page was individually defensible while the deck transition chain was broken;
- a diagram was semantically legal but slower than two sentences;
- a result figure contained numbers but did not expose the claim the audience should see;
- a local repair damaged accepted pages;
- a scoped review issued a global PASS;
- a full deck remained visually uneven even when page-level checks were marked ready.

**VERIFIED FACT.** CAT-TRACE v9 improved substantially while the installed runtime remained essentially unchanged. The improvement came from pre-writing audience/page-job/prerequisite/takeaway planning and a full-deck first-use pass.

**VERIFIED FACT.** The frozen real four-paper batch failed 4/4. Two cases failed before rendering because no compatible gold composition was found; two rendered cases did not receive effective pixel-changing repair and retained visible blockers.

**INFERENCE.** These facts do not make every schema, validator, or reference record useless. They show that these mechanisms cannot remain the architectural center or universal completion proof.

### 1.4 V0.2 revision fact

**VERIFIED FACT.** No production source changed between the v0.1 plan and this v0.2 planning task. The repository baseline adds only the two v0.1 design documents.

**PROPOSAL.** V0.2 therefore changes design authority only. It does not authorize implementation, migration, version bumps, benchmark execution, or retirement.

---

## 2. Product target

A user does not primarily call presentations to obtain a `.pptx`, `.tex`, or PDF. The user wants a bounded audience, in a finite amount of time, to undergo the intended belief, understanding, or decision update while preserving the underlying evidence.

The shared product target is:

> Turn source-grounded material into a coherent spatial-temporal communication artifact whose sequence, page meanings, page compositions, wording, notes, template use, and rendered behavior jointly serve a defined audience purpose.

| Scenario | Final artifact | Real success | Render/tests can pass while the product fails when… |
|---|---|---|---|
| Research group meeting | source-editable deck, render, optional notes | advisor sees the question, evidence, uncertainty, and decision | execution chronology replaces the scientific decision story |
| Supervisor discussion | small deck or bounded revision | options and consequences are explicit | the system redesigns unrelated pages or manufactures discussion questions |
| Seminar | full talk with references and notes | prerequisites and argument survive a longer arc | every page works alone but the dependency chain is lost |
| Conference talk | time-bounded deck | contribution and decisive evidence are memorable | manuscript sections are merely compressed |
| Journal club | paper-centered deck | question, method, evidence, limits, and critique are clear | screenshots and summaries replace interpretation |
| Defense | contribution-led deck plus backup | claims, evidence, limitations, and challenges are navigable | a generic seminar route omits defense-specific ownership and backup logic |
| Business presentation | decision deck | trade-offs, evidence, request, and action are explicit | research/CUHK machinery leaks into the task |
| Existing-deck revision | revised source/render plus change record | targeted problems are fixed and accepted content remains stable | revision silently becomes regeneration |
| Template-constrained deck | artifact using the actual template | master/layout/branding/editability constraints are preserved | colors are imitated without loading the template itself |

Group meeting, seminar, conference, journal club, and defense may share a lifecycle. They must not share one frozen storyline, one density policy, or one evidence allocation rule.

---

## 3. Current architecture map

The current research path is approximately:

```text
user request
  -> route to research-presentations
  -> Research State / Evidence Board when applicable
  -> deck-plan.yaml + schema validation
  -> page archetype + scientific object + layout/fallback/QA fields
  -> exact CUHK or editable-deck route
  -> renderer / production entry
  -> render, manifests, contact sheet
  -> quality loop and review
```

The existing-deck path is approximately:

```text
existing artifact + feedback
  -> revision packet assembled elsewhere
  -> accepted-element, first-use, render, language, reviewer evidence
  -> validation gate
  -> PASS_REVIEWED / REVISE / BLOCKED
```

The structural defect is that the current plan object carries both semantic decisions and page-form decisions. This makes it easy to satisfy a schema without demonstrating that the page form is the best way to communicate the meaning. The v0.2 architecture separates those decisions before renderer selection.

---

## 4. What currently works

The redesign should preserve the following unless later real evidence disproves them.

1. **Source and scientific fidelity.** Claims, numbers, equations, citations, uncertainty, and evidence status need traceable anchors.
2. **Audience and page-job reasoning.** A page must exist for a reason tied to what this audience needs now.
3. **First-use as dependency order.** A central method, symbol, dataset, or figure label cannot be used before the audience has enough context.
4. **Transition reasoning.** The end of page `k` must create the need for page `k+1`; a list of good pages is not a story.
5. **Visible versus notes separation.** Preparation, caveats, likely advisor counterquestions, and detail may belong in notes rather than visible copy.
6. **Render-and-look behavior.** Real pixels, text layers, citations, and contact sheets are required evidence.
7. **Existing-deck preservation.** Reviewer-seen baseline, accepted-element scope, and bounded edits address a real regression class.
8. **Bounded repair and fail-closed behavior.** Missing evidence, renderer, or template support must not silently degrade into cards, screenshots, or synthetic stand-ins.
9. **Exact template support.** The CUHK route has real user value as an adapter.

---

## 5. What may be a dead end

### 5.1 Universal schema-first planning

`deck-plan.yaml` is overloaded. Continuing to add fields would improve observability more reliably than deck quality.

**Proposal:** retire it as the universal production intermediate representation. Keep a compatibility reader/export only during migration.

### 5.2 A renamed storyboard that still contains page morphology

A `semantic_storyboard.yaml` containing `RESULT_FIGURE`, `two-column`, `density`, `layout_family`, or `dominant_object` would reproduce the current architecture under a new name.

**Proposal:** semantic storyboard records may not choose visual form, page archetype, dominant object, layout family, density, or spatial arrangement. Those decisions belong only to page composition.

### 5.3 Exact CUHK Beamer as general product architecture

**Proposal:** keep it as one strict template/renderer adapter, not the default theory of research presentations.

### 5.4 Gold-layout compatibility as a hard gate

A missing match has already blocked real papers before rendering.

**Proposal:** gold layouts and references may suggest candidates. No match must not block generation, and a match must not overrule page meaning.

### 5.5 Validator proliferation

A validator is justified only when it prevents a named real failure through the normal user entrypoint. Packet-field existence is not product quality.

### 5.6 Existing-deck gate mistaken for revision runtime

The current validator should not be treated as the production reviser. A true revision mode must diagnose, plan, edit, render, and compare.

### 5.7 Reviewer role mistaken for review authority

A reviewer cannot issue global PASS outside its declared scope, approve unsupported science, or count as independent merely because the prompt names it reviewer.

### 5.8 Synthetic success used as maturity

Synthetic fixtures remain regression tools. They cannot establish group-meeting, seminar, defense, business, or revision quality.

---

## 6. Authority boundaries

The proposed chain is:

```text
domain semantics
  -> presentation semantic storyboard
  -> page composition
  -> generic language and scientific-visualization handoffs
  -> artifact adapter
  -> scoped rendered review
```

### 6.1 The decisive v0.2 boundary

| Semantic storyboard owns | Semantic storyboard does not own |
|---|---|
| audience question or confusion | figure versus table versus equation versus diagram versus text |
| page job | dominant scientific/decision object |
| intended takeaway or decision contribution | page archetype or layout family |
| source/evidence anchors and uncertainty | hierarchy, density, scale, or whitespace allocation |
| prerequisites and first-use order | columns, cards, panels, tracks, or spatial relationships |
| incoming and outgoing dependency | whether to call `scientific-visualization` |
| visible-content obligation versus notes obligation | renderer-specific geometry |
| revision preservation constraints | gold/reference composition selection |

| Page-composition planner owns | Page-composition planner does not own |
|---|---|
| choose communication form | change the takeaway or evidence boundary |
| choose dominant object and supporting objects | reorder pages or redefine prerequisites |
| visual hierarchy, density, and spatial relationships | strengthen a claim or invent a transition |
| decide whether a plot/table/diagram/equation is useful | recompute domain science without the domain owner |
| request a new figure from `scientific-visualization` | alter accepted revision scope |
| produce renderer-neutral composition contract | polish prose independently of the language handoff |

A user or domain owner may impose a non-substitutable material constraint, such as `show this MRI case`, `include this theorem`, or `use this supplied table`. That constraint enters the task/evidence contract. It still does not authorize the semantic storyboard to choose layout or density.

### 6.2 Domain plugins

`statistical-modeling`, `medical-imaging`, `bioinformatics`, and other domain owners decide the validity of estimands, comparisons, models, uncertainty, images, and scientific conclusions. Presentations may expose a missing explanation or evidence gap but cannot repair science through storytelling.

### 6.3 Research-writing

Research-writing may supply a research-question map, contribution hierarchy, claims, evidence, literature synthesis, or report/manuscript structure. Presentations owns the live sequence and page-level audience experience. Manuscript sections are not slide order.

The two plugins may share vocabulary—audience, question, claim, evidence, limitation—but not a universal runtime schema.

### 6.4 Generic language layer

After semantic meaning and composition constraints are available, the language layer may realize titles, labels, captions, concise copy, transitions, and notes. It may not choose page order, communication form, evidence, or visual encoding. Presentations rechecks the returned wording in the rendered artifact.

### 6.5 Scientific visualization

Presentations supplies the question, claim, evidence requirement, available space, and desired audience reading task. `scientific-visualization` owns scientifically valid encoding, plot construction, uncertainty display, accessibility, and export. Presentations cannot silently change estimands, axes, or uncertainty semantics.

### 6.6 Rendering and documents

Beamer, PPTX, Google Slides, HTML, PDF, fonts, text layers, editability, and exact-template mechanics belong to artifact adapters. Renderers consume composition contracts; they do not choose the story.

### 6.7 Citations and literature

Citation services own metadata and support verification. Presentations owns whether a source must be visible, where it is placed, and whether it remains readable. A readable but unsupported citation fails citation verification; a valid but unreadable citation fails presentation QA.

### 6.8 Business presentations

Business mode may share front door, semantic-sequence lifecycle, composition, rendering, and review interfaces. It must not inherit Research State, scientific-object requirements, exact CUHK, or research evidence policies by default.

---

## 7. Alternative architectures

| Architecture | Strength | Failure risk | Decision |
|---|---|---|---|
| A. Current schema-heavy orchestrator | observable and already implemented | schema completion can masquerade as communication quality | reject as center |
| B. V0.1 mixed storyboard/composition | moves focus toward audience meaning | page brief and composer can both decide page form | revise, not selected |
| C. Strict semantic storyboard + page-composition planner + adapters | directly matches CAT-TRACE evidence and prevents renamed-schema regression | boundary can still erode unless tested on real artifacts | **selected** |
| D. Slide-object compiler as center | strong geometry and editability | polished but semantically wrong decks | use below composition as adapter mechanism |
| E. Direct whole-deck generation | low control-plane overhead | unstable revisions, hidden fallback, weak traceability | experimental baseline only |

Architecture C is selected. The choice is based on the real v9 improvement and later transition/figure/diagram failures, not on preserving current implementation investment.

---

## 8. Selected architecture

### 8.1 Core identity

Presentations is the orchestrator of live communication planning, page composition, artifact production, and rendered review. Slide generation by itself is an adapter capability.

### 8.2 Semantic storyboard

The semantic storyboard contains four logical views:

1. **Deck brief:** audience, occasion, duration, purpose, desired understanding/decision update, source boundary, output/template constraints.
2. **Narrative dependency map:** what unresolved question or prerequisite makes each page necessary now.
3. **Semantic page briefs:** audience question, page job, intended takeaway, evidence anchors, uncertainty, prerequisites, first-use, transitions, visible-versus-notes obligation, and revision preservation constraints.
4. **Review scope:** whole-deck requirements, page-specific requirements, preserved elements, and reviewer authority.

It does **not** contain scientific-object type, visual intent, layout hint, density, dominant object, archetype, panel count, columns, geometry, or gold ID.

The architecture does not require a new YAML or JSON schema. A concise Markdown storyboard or in-memory typed object may be sufficient. Formal serialization is justified only by a demonstrated production failure.

### 8.3 Page-composition planner

The page-composition planner receives a semantic page brief and the available evidence assets. It decides:

- whether the page should use a result figure, comparison table, equation, mechanism diagram, annotated image, decision matrix, sparse transition, or mostly verbal explanation;
- the dominant object and supporting objects;
- hierarchy, density, scale, whitespace, annotation, caption, and spatial relationship;
- whether existing assets are sufficient or `scientific-visualization` must produce a new presentation-specific figure;
- whether one semantic page job needs to split across pages rather than shrink.

Its output is a renderer-neutral composition contract. It may consult reference examples, but no reference match is mandatory.

### 8.4 Page job

Page job remains the central per-page semantic representation. It is not a composition label and not a complete deck model. A sequence of valid page jobs still requires dependency, pacing, first-use, and whole-deck rhythm checks.

### 8.5 New deck and existing-deck revision

They share vocabulary, adapters, and review infrastructure but use distinct production modes.

```text
new deck:
source -> deck brief -> dependency map -> semantic page briefs
       -> page composition -> language/visual assets -> renderer -> full review

revision:
existing source + reviewer-seen render + feedback
       -> accepted/preserved scope -> semantic diagnosis
       -> bounded composition/source changes -> matching renderer -> rerender
       -> targeted review + whole-deck regression review
```

Revision never silently regenerates. Missing editable source or unavailable template fidelity produces an explicit blocker or a separately authorized deliverable.

### 8.6 Renderer neutrality

Beamer, PPTX, Google Slides, reveal.js/HTML, and future renderers are adapters. Exact CUHK remains a high-priority project adapter. It is not the universal default architecture.

### 8.7 Reference intelligence

Reference material is an optional advisory service. It counts as integrated only when the normal runtime selects it, consumes it, changes the output, and the changed artifact passes qualitative review. `DISCOVERED`, `DOWNLOADED`, `INSPECTED`, or `STRUCTURED` alone does not establish value.

### 8.8 Explicit answers to the required product questions

1. **Core:** an orchestrator across scientific communication planning, visual storytelling, artifact production, and review; not slide generation alone.
2. **Page job:** central semantic unit, but never a layout or archetype field.
3. **`deck-plan.yaml`:** retire as universal production IR; retain temporary compatibility only.
4. **Current schema:** over-designed because it mixes semantics, composition, renderer, fallback, and QA.
5. **Reference library:** optional until real output-effect evidence justifies selected mandatory use.
6. **Visual review:** after real rendering, combining whole-deck scope and declared high-resolution page scope; early composition critique cannot close delivery.
7. **Reviewer authority:** limited to inspected artifact, declared requirements, and reader-facing evidence; no global PASS from partial scope.
8. **New versus revision:** separate modes with different failure contracts.
9. **Beamer/PPTX/Slides:** renderer adapters.
10. **Boundary with scientific visualization:** presentations owns the communication request and page role; visualization owns valid encoding and figure production.
11. **Boundary with generic language:** presentations freezes semantic and spatial constraints; language realizes copy; presentations validates the rendered fit.
12. **Shared core with research-writing:** shared vocabulary and handoff, not one runtime or schema.
13. **Group meeting, conference, defense:** shared lifecycle; separate mode policies for audience, time, repetition, evidence, backup, and decision needs.
14. **Business presentations:** remain temporarily as an isolated sibling mode; future split depends on real routing and quality evidence.

---

## 9. Runtime components

The proposed architecture has five production components.

### 9.1 Entry router and task contract

**Owns:** user front door, mode, new versus revision, audience/occasion/output/template constraints, source inventory, review scope.  
**Does not own:** science, story sequence, page form, prose, figure encoding.  
**Input:** request, sources, existing deck where applicable, explicit constraints.  
**Forbidden input:** invented audience, duration, template, or decision.  
**Output:** task contract and blockers.  
**Failure behavior:** ask only for non-inferable constraints or block; never select exact CUHK merely because the task is academic.

### 9.2 Semantic storyboard planner

**Owns:** deck brief, desired understanding/decision update, narrative dependency, page jobs, evidence allocation, first-use order, transitions, visible-versus-notes obligation, advisor-question value, revision preservation.  
**Does not own:** visual form, dominant object, density, hierarchy, layout, scientific-visualization invocation, renderer mechanics.  
**Input:** task contract plus domain-validated source/evidence map.  
**Forbidden input:** execution chronology as default story; layout/archetype fields disguised as semantics.  
**Output:** semantic storyboard and unresolved meaning/evidence gaps.  
**Failure behavior:** return to domain/user; never fill a gap with generic background or a preselected layout.

### 9.3 Page-composition planner

**Owns:** communication form, dominant/supporting objects, visual hierarchy, density, split-versus-shrink, spatial relationships, annotation/caption strategy, requests to scientific visualization.  
**Does not own:** page takeaway, evidence boundary, order, prerequisite, claim strength, revision scope.  
**Input:** semantic page brief, validated assets, template constraints, optional references.  
**Forbidden input:** mandatory gold match, decorative diagram, or automatic two-column/card fallback.  
**Output:** renderer-neutral composition contract and asset requests.  
**Failure behavior:** choose a simpler honest form, split the page, or block; never emit generic cards to satisfy structure.

### 9.4 Artifact adapter orchestrator

**Owns:** selecting and invoking the matching renderer/template adapter, mapping composition to editable/source objects, exact-template use, rendering, notes, text layer, source manifest.  
**Does not own:** story, science, composition rationale, reviewer verdict.  
**Input:** artifact contract, composition contracts, realized copy/assets, template/source.  
**Forbidden input:** flattened screenshots pretending to be editable; token imitation pretending to use an exact template.  
**Output:** requested source artifact and render.  
**Failure behavior:** fail closed on unavailable editability, template fidelity, or render support.

### 9.5 Artifact reviewer and bounded-repair controller

**Owns:** declared review scope, whole-deck contact-sheet checks, high-resolution page checks, layout/text-layer/accessibility checks, transitions/rhythm, preservation regression, findings-to-source repair mapping, rerender confirmation.  
**Does not own:** scientific approval, unbounded redesign, PASS outside reviewed scope.  
**Input:** frozen render/source, storyboard, composition contracts, baseline constraints, reviewer evidence.  
**Forbidden input:** validator summaries as substitute for pixels; self-reported authoring PASS.  
**Output:** scoped `PASS`, `REVISE`, or `BLOCKED` with evidence.  
**Failure behavior:** unresolved findings remain open; a repair counts only after source and pixels change and are rereviewed.

---

## 10. Production entrypoint

One presentations front door should accept ordinary requests such as:

- `把这些结果做成周三组会汇报，老师需要决定下一步做理论还是扩实验。`
- `按这个 CUHK 模板做 15 分钟 seminar。`
- `只修现有 deck 的第 4、9、10 页，其他页不要动。`
- `把这篇论文做成 journal club，最后保留两个真正值得讨论的问题。`
- `做一个给非技术负责人决策的商业方案 deck。`

The normal path is:

1. determine mode and task contract;
2. resolve domain semantics and source boundaries;
3. construct semantic storyboard without page morphology;
4. construct page compositions without changing semantic obligations;
5. invoke bounded generic-language and scientific-visualization handoffs;
6. select the actual renderer/template adapter;
7. render and inspect the real artifact;
8. apply only bounded evidence-grounded repair;
9. return source, render, review scope, and unresolved limitations.

Benchmark helpers, exact-CUHK generators, gold selectors, and validators may consume these components. None is the user-facing production entrypoint.

---

## 11. Existing implementation disposition

| Current implementation | Disposition | Reason |
|---|---|---|
| `research-presentations/SKILL.md` | **REPLACE / SIMPLIFY** | preserve strong policies but remove all-in-one authority |
| `business-presentations/SKILL.md` | **KEEP AS ISOLATED POLICY PACK, THEN REVIEW** | do not inherit research/CUHK machinery |
| `shared/deck-plan.schema.json` | **RETIRE AS UNIVERSAL IR; TEMPORARY COMPATIBILITY ONLY** | overloaded semantic/composition/control-plane object |
| `markdown_to_deck_plan.py` | **RETIRE FROM NORMAL PATH; COMPATIBILITY ONLY** | converts content into the old IR rather than the selected architecture |
| page archetype records | **REFERENCE_ONLY FOR COMPOSITION VOCABULARY** | must not enter the semantic storyboard as required labels |
| `scientific_object_semantics.py` | **PORT ONLY TO COMPOSITION/DOMAIN HANDOFF IF USEFUL** | scientific-object typing must not be a storyboard responsibility |
| `generate_research_presentation_production_entry.py` | **KEEP CUHK CAPABILITY AS ADAPTER; REPLACE AS UNIVERSAL ENTRY** | real executable route, but template- and mode-coupled |
| exact CUHK template/layout code | **KEEP / PORT INTO STRICT TEMPLATE ADAPTER** | real project value |
| gold composition store and hard compatibility selector | **RETIRE HARD GATE; REFERENCE_ONLY BY DEFAULT** | blocked real papers and can force irrelevant layouts |
| reference-library metadata/retrieval | **KEEP AS OPTIONAL ADVISORY SERVICE** | value requires actual output effect |
| `deck_quality_loop.py` | **SIMPLIFY / PORT BOUNDED REPAIR CONCEPTS** | bounded repair is sound; mappings and assumptions are brittle |
| `validate_existing_deck_revision_entry.py` | **KEEP SELECTED CHECKS; REPLACE AS SOLE REVISION ENTRY** | useful scope checks, not a reviser |
| `visual-qa.md` | **KEEP / NARROW VERDICT SEMANTICS** | rendered review is essential; scope integrity must be explicit |
| manifests, trace, contact sheets | **KEEP WHEN THEY SUPPORT REAL REVIEW** | supporting evidence, not a product substitute |
| synthetic fixtures and benchmark generators | **KEEP FOR REGRESSION ONLY** | cannot establish production maturity |

---

## 12. External resources / mature implementations

No external repository is adopted wholesale.

| Source | Version / commit | License | Capability | Decision |
|---|---|---|---|---|
| `RFYoung/slideweaver` | `8735c40d5c7bfe647f35f293a902fc02cc81c9a4` | MIT | native PPTX, layout solver, deck profile, render QA | **SELECTIVELY_PORTED proposed** for adapter/composition mechanics only |
| `wmyung/manuscript-to-editable-slides` | `2b7c9b5b234384d69ee0c153aa98107fc3f037bc` | MIT | source coverage, layout rhythm, editable output, repair loop | **SELECTIVELY_PORTED proposed** below semantic planning |
| `andyqiu847-ai/high-quality-slides` | `30a90be3561e61580cd52800a43f867513a8b144` | MIT | assertion/evidence/visual planning | **REFERENCE_ONLY** |
| `zarazhangrui/frontend-slides` | `9906a34d640d2111f724544cbc50f7f130569ae1` | MIT | same-content visual auditions and design lock | **REFERENCE_ONLY** until real A/B value |
| Assertion–Evidence approach | repository audit record | reuse boundary recorded in audit | assertion plus visual evidence | **REFERENCE_ONLY** |
| MIT Communication Lab guidance | repository audit record | CC BY-NC 4.0 | audience, message, hierarchy, talk figures | **REFERENCE_ONLY** |
| PLOS Ten Simple Rules | 2021 publication | CC BY | one idea, message heading, progressive build | **REFERENCE_ONLY** |
| CUHK Beamer template and current copy | current project material | project/template terms | exact institutional rendering | **MERGED as existing adapter**, not general architecture |

The integration ladder remains: `DISCOVERED -> DOWNLOADED -> INSPECTED -> STRUCTURED -> RUNTIME_SELECTED -> ACTUALLY_CONSUMED -> OUTPUT_AFFECTED -> QUALITY_REVIEWED`.

---

## 13. Real-artifact validation strategy

### 13.1 Minimum real task set

1. CAT-TRACE group meeting with real advisor decisions;
2. conference-length talk from a manuscript;
3. defense or long seminar with prerequisites and backup;
4. bounded existing-deck revision with accepted pages;
5. strict CUHK template task;
6. native editable PPTX task;
7. business decision deck.

### 13.2 Architecture-specific validation

The implementation must prove both directions of the new boundary:

- the semantic storyboard contains no layout/archetype/density/dominant-object decisions;
- the page-composition planner cannot change takeaway, evidence boundary, page order, first-use, or revision preservation.

A useful real comparison is the same source package under:

1. current `deck-plan.yaml` route;
2. a renamed storyboard that still embeds morphology;
3. the selected strict two-step route.

Reviewers must inspect the final decks, not just intermediate files. Success requires a visible improvement in sequence, form selection, readability, and revision stability.

### 13.3 Review dimensions

Audience/purpose fidelity, source fidelity, dependency order, page job, form utility, figure/table/equation claim alignment, transitions, rhythm, spoken readability, notes separation, template fidelity, editability, citations/text layer/accessibility, and revision preservation.

### 13.4 Maturity threshold

Promotion beyond baseline requires repeated real success across at least three research modes and one revision mode, with no silent fallback and at least one renderer other than exact CUHK Beamer. Fixtures alone cannot change maturity.

---

## 14. Non-substitutable semantics

The following cannot be silently inferred or replaced:

- audience, duration, purpose, decision, and template;
- domain-validated claims, numbers, equations, uncertainty, and citations;
- page job, intended takeaway, evidence anchors, prerequisites, first-use, and dependency order;
- visible-versus-notes obligation;
- accepted-element preservation;
- requested editability and exact-template use;
- scientific meaning of figures and tables;
- declared review scope and reviewer authority;
- real rendered artifact for final review;
- the boundary between semantic storyboard and page composition.

Failure to resolve any of these must produce a blocker or narrower authorized deliverable, not cards, paragraph dumps, fake charts, screenshots-as-editable, or synthetic evidence.

---

## 15. Red-team failure paths

1. `semantic_storyboard.yaml` is merely `deck-plan.yaml` renamed and still contains `RESULT_FIGURE`, `two-column`, or `density=medium`.
2. The storyboard preselects a scientific object, so the composer only retrieves the old gold layout.
3. The composer improves geometry by changing the page takeaway or deleting a caveat.
4. Every page job is valid, but the dependency map is broken.
5. First-use fields pass while the audience still lacks purpose/context.
6. A diagram is correct but has no utility over text.
7. A paper figure is enlarged but the decisive claim remains unreadable.
8. The reference library is logged but does not affect output.
9. A reference affects output by forcing an irrelevant composition.
10. Beamer compiles but communication fails.
11. Page QA passes while the contact sheet reveals monotonous or unstable rhythm.
12. A reviewer inspects selected pages and issues global PASS.
13. The authoring model changes its role name and calls itself independent.
14. A revision fixes target pages but damages accepted elements.
15. The template is imitated rather than loaded.
16. Missing renderer support degrades silently to flat images.
17. Generic language improves wording while sequence or form remains wrong.
18. Presentations redraws a statistical figure and changes the estimand.
19. Business mode receives research-state or CUHK defaults.
20. A synthetic benchmark passes while a real group meeting remains unusable.

---

## 16. Proposed future implementation phases

These are bounded planning units, not implementation authorization and not Codex prompts.

### Phase 1 — Real front door and separate new/revision contracts

**New user capability:** ordinary requests enter the correct mode; targeted revision cannot silently become regeneration.

### Phase 2 — Strict semantic storyboard on real decks

**New user capability:** audience question, page job, takeaway, evidence, prerequisites, first-use, transitions, visible/notes split, and preservation are decided before any page-form choice.

A schema alone does not complete this phase.

### Phase 3 — Page-composition planning

**New user capability:** the system chooses figure/table/equation/diagram/text, dominant object, hierarchy, density, spatial relation, and split-versus-shrink based on the semantic brief rather than old archetype or gold compatibility.

### Phase 4 — Renderer and strict-template adapters

**New user capability:** the same semantic and composition contracts can produce exact CUHK Beamer, editable PPTX, or another declared format without changing the story or silently degrading editability.

### Phase 5 — Artifact-grounded review and bounded repair

**New user capability:** whole-deck and page-scoped findings map to actual source changes and rereviewed pixels while preserving accepted content.

### Phase 6 — Optional reference intelligence proven by A/B output effect

**New user capability:** relevant inspected references improve composition without blocking unfamiliar content or copying style blindly.

### Phase 7 — Business-mode validation or split decision

**New user capability:** business tasks gain a validated decision-deck route or are intentionally separated if shared architecture creates real failures.

---

## 17. What is deliberately NOT being implemented yet

- no production source, plugin, profile, test, runtime, workflow, or generated-layer change;
- no new storyboard schema;
- no migration of `deck-plan.yaml`;
- no renderer rewrite;
- no version bump;
- no Reviewed Handoff task;
- no benchmark or paid review;
- no gold/reference corpus expansion;
- no automatic retirement;
- no claim that the absent clear-language design is frozen;
- no implementation prompt.

---

## 18. Questions for Critic

1. Is the storyboard/composition boundary now strict enough to prevent a renamed `deck-plan.yaml`?
2. Are any remaining storyboard fields secretly page-form decisions?
3. Should a user-mandated scientific object be represented in the task contract, evidence contract, or composition input?
4. Is one page-composition planner sufficient, or should domain-valid object selection and spatial layout later be separated?
5. Does the five-component runtime remain the smallest useful architecture?
6. Which current validators should survive because they prevent named real failures?
7. Can exact CUHK remain a first-class adapter without distorting generic routing?
8. Is the proposed reviewer scope strict enough for full-deck claims?
9. Are group meeting, seminar, conference, and defense adequately separated through mode policies?
10. Should business presentations remain an isolated mode or move to a different plugin after real validation?
11. What real A/B evidence would justify mandatory reference retrieval for any task class?
12. Which external layout mechanisms should be dependencies rather than selectively ported?
13. What migration evidence is required before retiring the old IR and hard gold selector?
14. Does the handoff to research-writing and a future generic language layer preserve medium-specific responsibility?

---

### Cross-plan consistency

This plan is consistent with `RESEARCH_WRITING_PRODUCTION_REDESIGN_PLAN_V0_2_2026-09-07.md`:

```text
domain semantics
  -> medium-specific information architecture
  -> generic language realization and domain-valid visual generation
  -> artifact adapter
  -> scoped artifact review
```

Research-writing owns document argument and allocation. Presentations owns live sequence and page composition. Neither owns generic prose or domain truth. They share vocabulary, not one schema.

### Repository evidence reviewed

- `AGENTS.md`
- `README.md`
- `TODO.md`
- `scripts/codex_marketplace_config.json`
- `docs/design/READER_FACING_COMMUNICATION_PLUGIN_BOUNDARIES.md`
- `docs/design/PRESENTATIONS_PRODUCTION_REDESIGN_PLAN_V0_1_2026-09-07.md`
- `docs/workflows/CONTINUOUS_REAL_WORLD_SKILL_REFINEMENT.md`
- `docs/PLUGIN_MATURITY.md`
- `docs/plugin-todos/presentations.md`
- `docs/plugin-changelogs/presentations.md`
- `docs/workflows/RESEARCH_PRESENTATION_REFERENCE_LIBRARY.md`
- `docs/audits/RESEARCH_PRESENTATION_EXTERNAL_METHOD_AUDIT.md`
- `docs/audits/research_presentation_external_method_matrix.json`
- `results/RESEARCH_PRESENTATION_CURRENT_CYCLE_FINAL_REPORT.md`
- `automation/reviewed_handoff/tasks/RESEARCH_PRESENTATION_CURRENT_ROUND.md`
- `skills/tools/documents-media/presentations/research-presentations/SKILL.md`
- `skills/tools/documents-media/presentations/business-presentations/SKILL.md`
- `skills/tools/documents-media/presentations/shared/**`
- CAT-TRACE v4–v14 feedback recorded in `docs/plugin-todos/presentations.md`
