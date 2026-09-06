# Presentations Production Redesign Plan

**Plan version:** 0.1  
**Status:** READY FOR CRITIC REVIEW / NOT EXECUTION AUTHORIZATION  
**Date:** 2026-09-07  
**Repository:** `YuukiAS/AI_Skills_Collection`  
**Repository baseline reviewed:** `abaa8ef522a3a37c0248b5ca3aca72f96ebe1a01`

This is a versioned architecture plan, not an implementation task. A later Critic may require `v0.2`, `v0.3`, or `v0.4`; those revisions must be committed as new versioned design files rather than silently overwriting this document.

A file named `CLEAR_LANGUAGE_PRODUCTION_REDESIGN_PLAN_V0_2_2026-09-06.md` was identified in the task brief as an important candidate design. It was **not present on the inspected repository baseline** under `docs/design/`. Therefore this plan preserves interface awareness with a future generic language layer, but does not treat that missing file as production truth. `docs/design/READER_FACING_COMMUNICATION_PLUGIN_BOUNDARIES.md` is used only as a proposal and may need joint revision after Critic review.

---

## 0. Why this plan exists

The current presentations plugin has accumulated several real capabilities: source-fidelity rules, audience-aware planning, page-level scientific objects, exact-template handling, rendered review, scoped repair, and safeguards for existing-deck revision. Those investments should not be discarded casually.

However, current evidence does not support treating the existing architecture as mature. The plugin has gradually fused four different concerns into one control plane:

1. deciding what an audience must understand or decide;
2. constructing a deck-level narrative and page-level visual communication;
3. selecting a file format, template, and renderer;
4. proving completion through schemas, packets, validators, fixtures, and reviewer decisions.

The strongest real-use improvements in CAT-TRACE v8→v14 came from changing the communication problem before generation: audience/page-job briefs, first-use ordering, claim-first figure redesign, transitions, spoken scientific language, preservation of accepted elements, and questions that genuinely help an advisor decide. By contrast, the frozen real holdout cycle recorded four failures out of four even after substantial work on gold compositions, exact CUHK rendering, repair loops, validators, and synthetic fixtures. This is the central architecture signal: the system invested heavily in renderer and control-plane observability without reliably solving semantic storyboard and visual reasoning.

**Core judgment:** the current architecture is **partly correct, but its center of gravity is wrong**. Presentations should remain an orchestrator, but its production core should be a semantic storyboard and page-composition contract. Beamer, PPTX, Google Slides, HTML, templates, reference libraries, and validators should become bounded adapters or services rather than the theory of the product.

---

## 1. Verified repository reality

### 1.1 Current plugin composition and maturity

| Item | Verified repository fact |
|---|---|
| Marketplace plugin | `presentations` |
| Plugin version | `0.3` |
| README maturity | `baseline` |
| User-visible source skills | `research-presentations`, `business-presentations`, plus `shared/**` |
| Research modes named in the source skill | group meeting, supervisor discussion, seminar, conference talk, journal club, defense, existing-deck revision |
| Current research desktop default | exact CUHK Beamer/PDF route |
| Current generic planning artifact | `shared/deck-plan.schema.json`, usually materialized as `deck-plan.yaml` |
| Current prominent runtime entry | `shared/scripts/generate_research_presentation_production_entry.py` |
| Existing-deck completion gate | `shared/scripts/validate_existing_deck_revision_entry.py` |
| Main repository evidence | `docs/plugin-todos/presentations.md`, changelog, external-method audit, current-cycle report, Reviewed Handoff history and results |

### 1.2 Current production path

**VERIFIED FACT.** `research-presentations/SKILL.md` combines task routing, research-state intake, evidence-board construction, slide planning, format routing, exact-template behavior, visual review, reference-library use, writing handoff, and existing-deck revision rules.

**VERIFIED FACT.** `deck-plan.schema.json` combines audience and purpose, slide-level meaning, scientific evidence, layout intent, renderer/template requirements, citations, notes, uncertainty, fallbacks, and QA. It is therefore not merely a lightweight interchange format; it is carrying product intent, scientific traceability, visual design, and completion control in one document.

**VERIFIED FACT.** `generate_research_presentation_production_entry.py` is a one-call **exact-CUHK research presentation** entry. It is a real executable route, but it is not a universal presentations front door. Its default story order, task bundle, Beamer source, render outputs, review artifacts, and repair behavior are strongly coupled to the CUHK group-meeting route.

**VERIFIED FACT.** `validate_existing_deck_revision_entry.py` validates a revision packet containing a baseline review, accepted-element ledger, first-use checks, rendered-object checks, final language pass, and independent review. It does not itself inspect and edit a deck, plan bounded changes, or produce a revised artifact. It is a gate around a revision workflow, not the revision workflow itself.

### 1.3 Real production feedback

**VERIFIED FACT.** CAT-TRACE v8→v14 feedback repeatedly identified failures that are only weakly captured by renderer success:

- the page lacked a clear job for a particular audience;
- a central term, method, dataset, or estimand appeared before explanation;
- transitions did not tell the audience why the next page existed;
- slide language looked like paper prose rather than spoken scientific language;
- a diagram was geometrically valid but had little explanatory utility;
- a figure reported values without first exposing the claim it should support;
- advisor questions existed but had low decision value;
- citations or PDF text layers were mechanically present but visually unusable;
- a scoped review or partial-page review was presented as a global PASS;
- accepted elements were damaged while fixing unrelated pages;
- a deck passed page checks while still imposing excessive whole-deck reader effort.

**VERIFIED FACT.** The CAT-TRACE v9 improvement was attributed to task-level audience/page-job briefs and a first-use registry prepared before language realization, while the production runtime itself remained unchanged.

**VERIFIED FACT.** The current-cycle record reports that the frozen four-paper real batch failed 4/4: two cases did not render because no compatible gold composition was found; two rendered cases did not receive effective pixel-changing repair, and citation/body collisions or contact-sheet review still failed.

**INFERENCE.** These outcomes do not prove that schemas, gold compositions, or validators are useless. They do show that none should remain the architectural center or a mandatory universal gate without evidence that it improves real decks across modes.

### 1.4 Current source-of-truth caveat

**VERIFIED FACT.** The repository boundary document is labeled as a proposal. The current skill source is the production implementation but not proof that the architecture is correct. Historical Reviewed Handoff PASS decisions certify bounded task contracts, not the global product architecture.

**PROPOSAL.** All architectural claims below should therefore be evaluated against real deck behavior rather than protected by historical investment or current file structure.

---

## 2. Product target

A user does not primarily call presentations to “obtain a PPTX or PDF.” The user wants a bounded audience, in a finite amount of time, to undergo the intended belief or decision update while preserving scientific truth and receiving a usable rendered artifact.

The shared product target is:

> Turn source-grounded research or business material into a coherent spatial-temporal communication artifact whose sequence, page jobs, visual objects, wording, notes, template use, and rendered behavior jointly serve a defined audience purpose.

The artifact differs by scenario:

| Scenario | Normal entry | Final artifact | Real success | Render/tests can pass while product fails when… |
|---|---|---|---|---|
| Research group meeting | “把本周结果做成组会汇报” | editable source plus rendered deck, optional notes | advisor understands the scientific question, evidence, uncertainty, and next decision | slides follow execution chronology, advisor question is fake, evidence density hides the decision |
| Supervisor discussion | “整理三页让我和老师讨论路线” | small scoped deck or revised pages | unresolved choices and consequences are explicit | system redesigns the whole deck, damages accepted pages, or buries the decision |
| Research seminar | “做一个面向统计/医学听众的 seminar” | full talk with notes and references | prerequisites arrive before use; argument survives a longer arc | every page is individually sound but the audience loses the dependency chain |
| Conference talk | “做 12 分钟 conference talk” | time-bounded deck | contribution and decisive evidence are memorable and supportable | manuscript sections are compressed into slides without a talk narrative |
| Journal club | “讲这篇论文并评价它” | paper-centered deck | paper question, method, evidence, limits, and discussion prompts are clear | screenshots or summaries replace critical interpretation |
| Defense | “准备答辩 deck” | thesis-level deck with backup | contribution hierarchy, evidence, limitations, and anticipated challenges are navigable | a generic seminar template omits contribution ownership or backup logic |
| Business presentation | “给决策者讲方案” | decision deck | options, trade-offs, evidence, and requested decision are explicit | research-heavy schemas and CUHK defaults contaminate a business task |
| Existing-deck revision | “只改第 8、11、12 页” | revised deck plus change record | targeted problems are fixed while accepted material and style remain stable | revision mode silently regenerates the whole deck or self-certifies |
| Template-constrained deck | “严格使用这个模板” | source and render that use the template itself | required master/layout/branding and editable semantics are preserved | the system extracts colors and imitates the template rather than using it |

These scenarios share a lifecycle but not a fixed storyline. Group meeting, conference talk, and defense can share intake, storyboard, composition, rendering, and review interfaces; they must not share a single page sequence or evidence policy.

---

## 3. Current architecture map

The present path is approximately:

```text
user request
  ↓
Marketplace routes to research-presentations or business-presentations
  ↓
skill-level intake and mode rules
  ↓
research mode may build Research State + Evidence Board
  ↓
deck-plan.yaml validated against deck-plan.schema.json
  ↓
page archetypes + scientific objects + layout/fallback/QA fields
  ↓
format/template routing
    ├─ exact CUHK Beamer/PDF for the dominant research desktop route
    └─ editable PPTX / other application path for other cases
  ↓
renderer or production entry
  ↓
rendered artifact + contact sheet + trace/manifest
  ↓
quality loop / bounded repair
  ↓
independent visual review and completion gate
```

The existing-deck path is closer to:

```text
existing artifact + targeted feedback
  ↓
revision packet assembled elsewhere
  ↓
accepted-element / first-use / rendered-QA / language / reviewer fields
  ↓
validate_existing_deck_revision_entry.py
  ↓
PASS_REVIEWED, REVISE, or BLOCKED
```

This map reveals three structural gaps.

First, semantic planning is encoded as many fields but is not a distinct production component with a stable input/output contract. Second, visual intelligence is split among page archetypes, scientific objects, gold compositions, renderer code, reference lessons, and review scripts, so no component clearly owns the transformation from “what must be understood” to “what should occupy the page.” Third, revision has a strong gate but no equally explicit production runtime.

---

## 4. What currently works

The redesign should preserve the following capabilities unless later evidence disproves them.

### 4.1 Source and scientific fidelity

The evidence-board and source-anchor concepts correctly prevent a renderer or language pass from inventing results, changing uncertainty, or presenting unsupported claims. This is a real production requirement, not schema decoration.

### 4.2 Audience, purpose, and page-job reasoning

The recent real feedback strongly supports asking what the audience knows, what belief should change, and what each page must accomplish. A page job is more useful than a generic title or content type.

### 4.3 First-use ordering

First-use is valuable when treated as a narrative dependency: a central object must be introduced before the audience is asked to reason with it. It should not be reduced to a post-hoc checklist.

### 4.4 Scientific and decision objects

Equations, result figures, comparison tables, diagrams, decision matrices, and annotated images are valid page-level communication objects. Requiring an object is not enough, but explicitly choosing its role is useful.

### 4.5 Render-and-look behavior

Compiling a file or checking object coordinates is insufficient. Whole-deck rendering, high-resolution review of problem pages, contact sheets, text-layer checks, and re-rendering after repair are essential.

### 4.6 Existing-deck preservation

Reviewer-seen baselines, targeted scope, accepted-element ledgers, and regression checks address a real failure mode: fixing three pages by unintentionally rewriting thirty.

### 4.7 Bounded repair and fail-closed behavior

One or a small number of evidence-driven repair cycles is safer than an unbounded “keep improving” loop. When the required renderer, source, template, or evidence is unavailable, the system should block rather than silently emit generic cards or a screenshot-only artifact.

### 4.8 Exact template support

Exact CUHK Beamer support is useful for the user's actual environment. Its value is as a reliable template adapter, not as the universal theory of research presentations.

---

## 5. What may be a dead end

### 5.1 Universal schema-first planning

The current schema is overloaded. It mixes stable semantic requirements with transient implementation details, template choices, renderer fields, fallbacks, and QA evidence. Adding more fields would make it easier to assert that planning occurred without proving that the deck communicates well.

**Proposal:** retire `deck-plan.yaml` as the universal production intermediate representation. Preserve a compatibility reader during migration, but center production on a smaller logical storyboard whose serialization is optional.

### 5.2 Exact CUHK Beamer as the general research architecture

The exact CUHK route is a user-specific and template-specific production path. Treating it as the default for all research tasks confuses a successful local adapter with the general product architecture.

**Proposal:** keep the exact CUHK implementation only as one renderer/template adapter. Beamer-first is not a product principle.

### 5.3 Gold-composition compatibility as a hard gate

Reference-calibrated composition can improve a deck when a relevant pattern exists. The real batch demonstrated that a hard “compatible gold record” requirement can prevent generation or force brittle matches.

**Proposal:** references may supply optional priors, examples, or candidate compositions. Absence of a match must not block a semantically valid deck; presence of a match must not authorize copying it without evidence of suitability.

### 5.4 Validator proliferation as substitute for capability

Validators are valuable when they prevent a demonstrated regression. They become a dead end when every new real failure produces another packet field while the planner and composer remain unchanged.

**Proposal:** every retained validator must name a concrete failure, operate on evidence produced by the normal entrypoint, and be removable if it does not change user-visible outcomes.

### 5.5 Existing-deck gate as a revision runtime

A packet can show that somebody supplied a ledger and review decision. It cannot itself guarantee that the artifact was revised intelligently.

**Proposal:** build a true revision mode before treating the current gate as mature production behavior.

### 5.6 Independent reviewer as final scientific authority

An independent reviewer is useful for detecting visual or reader-facing failure. It should not be allowed to invent scientific claims, approve unsupported content, or issue a global product PASS after inspecting only selected pages.

**Proposal:** narrow reviewer authority to the artifact and declared scope; unresolved scientific semantics return to the domain owner or user.

### 5.7 Synthetic benchmark success as maturity evidence

Synthetic fixtures are appropriate for regression and repair mechanics. They do not validate audience understanding, deck rhythm, scientific judgment, or template-constrained revision.

**Proposal:** no future maturity promotion should rely on synthetic decks alone.

---

## 6. Authority boundaries

The selected boundary is a dependency chain with explicit return paths, not a hierarchy in which presentations can overrule every other plugin.

```text
domain semantics
  ↓
presentations communication architecture
  ↓
generic language realization
  ↓
artifact-specific rendering
  ↓
rendered review and bounded repair
```

### 6.1 Domain plugins

`statistical-modeling`, `medical-imaging`, `bioinformatics`, and other research-domain owners decide whether the estimand, comparison, model, metric, uncertainty, imaging interpretation, and scientific conclusion are valid. Presentations may ask for clarification or flag a communication gap; it may not “simplify” by changing the science.

### 6.2 Research writing

Research-writing may provide an existing research-question map, contribution hierarchy, claim-evidence relations, literature synthesis, or report/manuscript structure. Presentations is not a renderer for manuscript sections. It owns the transformation into a time-bounded spatial sequence: what the audience must know first, what belongs on a page, what can be omitted, what should be shown rather than said, and what discussion or decision is sought.

The two plugins may share a small vocabulary—audience, research question, claim, evidence, uncertainty, limitation—but should **not** share a universal runtime schema. Document argument and live visual communication have different dependency, density, repetition, and timing requirements.

### 6.3 Generic language layer

The language layer acts after page meaning is fixed enough to be expressed. It may produce or revise titles, labels, captions, concise slide copy, result explanations, transitions, and speaker notes while preserving the page brief.

It may not decide slide order, page job, scientific object, evidence selection, visual encoding, or advisor decision. Presentations must recheck whether the realized language fits the spatial and temporal artifact.

Because the named clear-language v0.2 file was absent from the inspected main, this handoff is a proposal to be jointly reviewed, not a frozen API.

### 6.4 Scientific visualization

Presentations owns the role of a figure in the deck: the audience question, claim to expose, needed comparison, crop/annotation request, page placement, and relationship to surrounding pages.

`scientific-visualization` owns scientifically valid encoding, plot construction, uncertainty display, color/accessibility choices, and figure export. Presentations may annotate or compose a validated figure but must not silently recompute or redesign its statistical semantics.

### 6.5 Documents, PDF, and rendering

Renderer services own file mechanics: Beamer, LaTeX, PPTX object construction, Google Slides, HTML/reveal.js, PDF generation, font embedding, text layers, crop boxes, and editability. They consume a presentation artifact contract and do not choose the scientific story.

### 6.6 Citations and literature

Citation/literature services own source discovery, metadata, and support verification. Presentations owns whether a source is needed on a page, whether the citation placement is readable, and whether the talk should expose or defer literature detail. A citation that is visually present but illegible still fails presentations QA; a readable citation that does not support the claim fails citation verification.

### 6.7 Business presentations

Business mode shares the front door, storyboard lifecycle, composition, rendering, and review interfaces. It does not inherit research-state, evidence-board, CUHK, or scientific-object requirements by default. Its evidence semantics and decision objects should remain an isolated policy pack with separate maturity evidence.

---

## 7. Alternative architectures

| Architecture | Description | Strengths | Main failure risk | Decision |
|---|---|---|---|---|
| A. Current schema-heavy orchestrator | A broad skill populates `deck-plan.yaml`, routes format/template, invokes render/QA/repair, and relies on validators and independent review | observable, testable, preserves many historical checks | completed schema can masquerade as communication quality; exact CUHK and gold compatibility dominate; revision remains gate-heavy | reject as center; retain selected safeguards |
| B. Semantic storyboard + renderer adapters | Build a deck brief, narrative dependencies, and page briefs first; then language/visual services and renderer adapters; review actual artifact | directly targets real CAT-TRACE failures; format-neutral; keeps scientific meaning separate from mechanics | storyboard can become another checklist unless grounded in real audience decisions and artifacts | **selected** |
| C. Slide-object compiler / artifact-first | Compile typed objects into editable slides using a constraint solver and renderer-specific object model | strong editability, geometry, responsiveness, and deterministic QA | can create polished but semantically wrong decks; object vocabulary may overfit one renderer | adopt selected mechanisms as adapter/composition layer |
| D. Direct whole-deck LLM planner + bounded renderer | Give the model the full source and task, generate the deck directly, then perform limited artifact review | low control-plane overhead; preserves global context | difficult traceability, unstable revisions, hidden fallback, weak preservation and source fidelity | keep as experimental baseline, not production architecture |

The selected architecture is B with bounded mechanisms from C. The decision is based on real failures, not on sunk cost. Architecture A is easier to continue because most code already exists, but it has not demonstrated robust generalization on the frozen real batch. Architecture C is valuable below the semantic layer. Architecture D is useful as a comparative baseline but lacks the safeguards required for reliable production.

---

## 8. Selected architecture

### 8.1 Architectural center: semantic storyboard

The production center is a **semantic storyboard**, not a renderer and not a mandatory YAML schema. It contains five logical artifacts:

1. **Deck brief** — audience, occasion, duration, purpose, desired belief/decision update, scientific/business constraints, output and template contract.
2. **Narrative sequence map** — the dependencies and transitions that explain why each page follows the previous one; it is not a list of section names.
3. **Page briefs** — one bounded communication contract per page.
4. **Artifact contract** — renderer, editability, template, citation, notes, accessibility, and export requirements.
5. **Review scope** — which pages and whole-deck properties must be reviewed, what is preserved, and what authority the reviewer has.

A page brief should contain only information that materially guides output:

- audience question or confusion addressed;
- page job;
- intended takeaway or decision contribution;
- source/evidence anchors and uncertainty;
- scientific or decision object;
- prerequisites and first-use dependencies;
- incoming and outgoing transition;
- visible content versus speaker notes;
- composition intent and density budget;
- preservation constraints for revision mode.

This logical representation may later be serialized as JSON, YAML, Markdown, or typed objects. The architecture does not authorize a new schema merely to mirror these bullets.

### 8.2 Page job is central but not sufficient

Page job should be the central **per-page** representation because it forces the system to answer why the page exists. It must not become the sole deck representation. A sequence of locally valid page jobs can still produce poor rhythm, missing prerequisites, repeated conclusions, or abrupt transitions. The deck brief and narrative sequence map remain first-class.

### 8.3 Visual intelligence location

Visual intelligence belongs between the page brief and renderer. It converts “what the audience must understand” into a page morphology:

- evidence figure;
- comparison table;
- equation with interpretation;
- mechanism diagram;
- annotated image;
- decision matrix;
- claim-and-proof sequence;
- intentionally sparse transition or conclusion page.

This component chooses the communication form and delegates domain-valid figure generation to `scientific-visualization`. It does not merely select an archetype label or a stored gold geometry.

### 8.4 New deck and revision are separate modes

Both modes share intake, semantic representation vocabulary, renderer adapters, and review infrastructure. They require different runtime contracts.

**New-deck mode**

```text
source package
  → deck brief
  → narrative sequence
  → page briefs
  → language and visual-object realization
  → renderer adapter
  → full-deck review
  → bounded repair
```

**Existing-deck revision mode**

```text
existing source + rendered baseline + user feedback
  → revision scope and accepted-element map
  → diagnosis by page and deck-level consequence
  → bounded change plan
  → source edit through matching renderer adapter
  → re-render
  → targeted-page review + whole-deck regression review
```

Revision must never silently fall back to regeneration. If editable source is unavailable or a requested template cannot be preserved, the system must state the limitation and block or seek authorization for a different deliverable.

### 8.5 Renderer neutrality

Beamer, PPTX, Google Slides, reveal.js/HTML, and future renderers are adapters. The adapter may reject an unsupported contract. It may not rewrite the story to fit its convenience. Exact CUHK Beamer remains a supported adapter for the user's environment, not the default universal route.

### 8.6 Reference-library role

The reference library becomes an optional advisory service. It may retrieve examples by page job, scientific object, audience, or evidence form and suggest composition candidates. A reference is mature only when the normal runtime selected it, actually consumed it, changed the output, and the changed artifact passed qualitative review. “Downloaded,” “inspected,” or “structured” is not enough.

### 8.7 Required decisions

1. **Core identity:** presentations is the orchestrator of communication planning, visual storytelling, artifact production, and rendered review; slide generation alone is an adapter-level capability.
2. **Page job:** central per-page representation, but not a substitute for deck-level narrative dependencies.
3. **`deck-plan.yaml`:** should not remain the universal production IR; retain only temporary compatibility/export support.
4. **Current schema:** over-designed because it mixes semantic, renderer, fallback, and QA concerns.
5. **Reference library:** useful only as optional prior; current evidence does not justify a universal hard dependency.
6. **Visual review:** after a real render, with whole-deck checks plus declared high-resolution page scope; it may also provide early composition feedback but cannot close the task before rendering.
7. **Independent reviewer authority:** currently too broad when partial review can lead to global PASS; restrict it to declared artifact scope and reader-facing evidence.
8. **New versus revision:** share interfaces and adapters, but use distinct production modes and failure contracts.
9. **Beamer/PPTX/Slides:** renderer adapters, not product architecture.
10. **Boundary with scientific visualization:** presentations owns figure purpose and page role; scientific visualization owns valid encoding and figure generation.
11. **Handoff with generic language:** presentations freezes page meaning and constraints; language realizes copy/notes without changing meaning; presentations then validates fit in the artifact.
12. **Shared core with research-writing:** share vocabulary and explicit handoff artifacts, not a universal runtime or schema.
13. **Group meeting/conference/defense:** share lifecycle architecture; each has a separate mode policy for audience, time, evidence, repetition, and backup material.
14. **Business presentations:** remain in the plugin for now as an isolated sibling policy pack; Critic should test whether its different evidence and maturity justify a later split.

---

## 9. Runtime components

The proposed production architecture has **five** true components. Domain, language, literature, visualization, and file-rendering tools are dependencies or adapters, not hidden stages counted as components.

### 9.1 Entry router and task contract

**Owns:** mode selection, normal user entry, new versus revision, audience/occasion/output/template constraints, available source inventory, review scope.  
**Does not own:** scientific conclusions, slide sequence, prose, figure encoding.  
**Input:** natural-language request, source files, existing deck when applicable, explicit template/output requirements.  
**Forbidden input:** invented audience, duration, or template constraints presented as user facts.  
**Output:** deck task contract and resolvable blockers.  
**Failure behavior:** ask only for genuinely missing non-inferable constraints or block; never choose exact CUHK merely because the task is “research.”

### 9.2 Semantic storyboard planner

**Owns:** deck brief, belief/decision update, narrative dependencies, page jobs, first-use order, evidence allocation, visible-versus-notes decisions, transitions, advisor/discussion value.  
**Does not own:** domain truth, sentence-level polish, plot validity, renderer mechanics.  
**Input:** task contract plus domain-validated evidence and source map.  
**Forbidden input:** internal execution chronology treated as audience narrative; unsupported claims.  
**Output:** semantic storyboard and evidence gaps.  
**Failure behavior:** return unresolved scientific or audience questions; do not fill gaps with generic background pages.

### 9.3 Page composition planner

**Owns:** page morphology, scientific/decision object role, hierarchy, density, relationship among text/equation/figure/table/diagram, requests to visualization or language services.  
**Does not own:** recomputing statistics, changing claims, drawing invalid figures, final file geometry.  
**Input:** page briefs, validated source assets, optional reference candidates.  
**Forbidden input:** a gold composition used only because it is available; decorative diagrams with no informational job.  
**Output:** renderer-neutral page composition contracts and asset requests.  
**Failure behavior:** block or simplify honestly when no suitable visual object exists; do not emit generic cards as a silent fallback.

### 9.4 Artifact adapter orchestrator

**Owns:** selecting and invoking the matching renderer/template adapter, mapping composition contracts to editable objects or source, preserving exact templates, producing renderable artifacts and traceable source.  
**Does not own:** story, scientific semantics, or reviewer verdict.  
**Input:** artifact contract, page composition contracts, realized copy/assets, template/source.  
**Forbidden input:** screenshots pretending to be editable slides; token extraction pretending to use an exact template.  
**Output:** editable source where required, rendered deck, text layer, notes, asset/source manifest.  
**Failure behavior:** fail closed if editability, template fidelity, or required rendering cannot be met.

### 9.5 Artifact review and bounded repair controller

**Owns:** review scope, contact-sheet whole-deck checks, high-resolution page checks, overflow/collision/text-layer/accessibility checks, transition/rhythm audit, preservation regression, issue-to-change mapping, bounded re-rendered repair.  
**Does not own:** self-generated scientific approval, unbounded redesign, global PASS outside reviewed scope.  
**Input:** rendered artifact, source, storyboard, baseline/revision constraints, reviewer evidence.  
**Forbidden input:** only validator summaries when the render is available; synthetic proxy as final evidence.  
**Output:** PASS for declared scope, REVISE with artifact-grounded findings, or BLOCKED.  
**Failure behavior:** unresolved findings remain open; repair must change the real source and be confirmed in a new render.

---

## 10. Production entrypoint

A normal user should call one presentations front door using ordinary task language. The front door should not require users to know `deck-plan.yaml`, gold composition identifiers, Beamer scripts, or internal reviewer packets.

Examples:

- “把这些结果做成周三组会汇报，老师需要决定下一步做理论还是扩实验。”
- “按这个 CUHK 模板做 15 分钟 seminar。”
- “只修现有 deck 的第 4、9、10 页，其他页不要动。”
- “把这篇论文做成 journal club，最后保留两个真正值得讨论的问题。”
- “做一个给非技术负责人决策的商业方案 deck。”

The entrypoint should:

1. determine mode and collect the minimum task contract;
2. invoke domain owners for unresolved scientific meaning rather than infer it;
3. construct a semantic storyboard;
4. realize language and visual requests through explicit handoffs;
5. select the renderer/template adapter from actual user requirements;
6. render and inspect the real artifact;
7. repair only evidence-grounded issues within a bounded scope;
8. return source, render, review status, and unresolved limitations.

Benchmark helpers, exact-CUHK generators, and validators may call the same components, but none is itself the production front door.

---

## 11. Existing implementation disposition

| Current implementation | Disposition | Reason |
|---|---|---|
| `research-presentations/SKILL.md` | **REPLACE / SIMPLIFY** | preserve its strongest policies, but split the current all-in-one authority into the five components and mode packs |
| `business-presentations/SKILL.md` | **KEEP AS ISOLATED POLICY PACK, THEN REVIEW** | useful sibling mode, but currently lacks comparable real validation and must not inherit research/CUHK machinery |
| `shared/deck-plan.schema.json` | **RETIRE AS UNIVERSAL IR; KEEP TEMPORARY COMPATIBILITY** | overloaded and schema-first; serialization should follow architecture rather than define it |
| `generate_research_presentation_production_entry.py` | **REPLACE AS UNIVERSAL ENTRY; KEEP CUHK ROUTE AS ADAPTER/REFERENCE** | executable but tightly coupled to exact-CUHK group-meeting behavior |
| exact CUHK template and layout code | **KEEP / PORT INTO TEMPLATE ADAPTER** | real user value, but environment-specific |
| gold composition store, selector, and compatibility gate | **SIMPLIFY / REFERENCE_ONLY BY DEFAULT** | demonstrated some output influence but failed to generalize in the frozen real batch |
| reference-library metadata and retrieval | **KEEP AS OPTIONAL ADVISORY SERVICE** | valuable when actual consumption and output effect are proven |
| `deck_quality_loop.py` and bounded repair concepts | **SIMPLIFY / PORT** | bounded artifact-grounded repair is sound; current issue mapping and hard assumptions are brittle |
| `validate_existing_deck_revision_entry.py` | **KEEP SELECTED CHECKS; REPLACE AS SOLE REVISION ENTRY** | preservation and scope checks are valuable, but the script is a gate rather than a production reviser |
| `visual-qa.md` | **KEEP / NARROW AUTHORITY** | render inspection is essential; reviewer scope and global verdict semantics need revision |
| source-fidelity and template-routing guidance | **KEEP / SPLIT** | source fidelity belongs to storyboard/evidence interface; template routing belongs to artifact adapter |
| validators without a demonstrated production failure | **CRITIC REVIEW FOR RETIREMENT** | control-plane cost is not justified by existence alone |
| synthetic benchmark fixtures | **KEEP FOR REGRESSION ONLY** | not valid evidence of production maturity |
| current independent reviewer self-certification path | **REPLACE** | reviewer must inspect declared real artifacts and cannot self-authorize outside scope |

---

## 12. External resources / mature implementations

No external repository is adopted wholesale. Exact provenance remains mandatory.

| Source | Version / commit | License | Inspected files / evidence | Capability | Decision |
|---|---|---|---|---|---|
| `RFYoung/slideweaver` | `8735c40d5c7bfe647f35f293a902fc02cc81c9a4` | MIT | `LICENSE`, `README.md`, `SKILL.md`, `assets/smart_layout.py`, `assets/deck_profile.py`, `assets/render_qa.py`, `assets/shape_cookbook.py` | native editable PPTX, smart layout, deck profile, render QA | **SELECTIVELY_PORTED (proposed)** for adapter/composition mechanics only; not semantic planning |
| `wmyung/manuscript-to-editable-slides` | `2b7c9b5b234384d69ee0c153aa98107fc3f037bc` | MIT | `LICENSE`, `README.md`, `SKILL.md`, `references/layout_families.md`, `references/layout_rhythm.md`, `references/acceptance_tests.md`, `references/render_repair_loop.md`, `scripts/render_pptx.js`, `scripts/render_slide_previews.py` | source coverage, editable slide production, layout rhythm, render-repair loop | **SELECTIVELY_PORTED (proposed)** for renderer-neutral coverage and repair contracts |
| `andyqiu847-ai/high-quality-slides` | `30a90be3561e61580cd52800a43f867513a8b144` | MIT | `LICENSE`, `README.md`, `plugin/skills/high-quality-slides/SKILL.md`, `layouts.md`, `html-template.md` | staged assertion/evidence/visual planning and layout guidance | **REFERENCE_ONLY**; any later concept port requires a bounded intake |
| `zarazhangrui/frontend-slides` | `9906a34d640d2111f724544cbc50f7f130569ae1` | MIT | `LICENSE`, `SKILL.md`, `plugins/frontend-slides/skills/frontend-slides/SKILL.md`, `html-template.md`, selected `bold-template-pack/templates/*/design.md` | same-content visual auditions and style discovery | **REFERENCE_ONLY** until real deck A/B evidence shows value |
| Assertion–Evidence approach | repository audit record | source-specific terms recorded in audit | official materials listed in the audit | message assertion plus visual evidence | **REFERENCE_ONLY**; useful page principle, not universal deck architecture |
| MIT Communication Lab presentation guidance | repository audit record | CC BY-NC 4.0 | official guidance inspected in the audit | audience, message, visual communication guidance | **REFERENCE_ONLY**, no code port |
| PLOS “Ten Simple Rules for Effective Presentation Slides” | 2021 publication | CC BY | publication recorded in the audit | one idea per slide, message headings, reduction | **REFERENCE_ONLY** |
| Task-supplied CUHK Beamer template and repository copy | current project material | project/template terms | seven-page template and current adapter code | exact institutional rendering | **MERGED (existing project adapter)**, not general architecture |

The adoption rule is unchanged: `DISCOVERED → DOWNLOADED → INSPECTED → STRUCTURED → RUNTIME_SELECTED → ACTUALLY_CONSUMED → OUTPUT_AFFECTED → QUALITY_REVIEWED`. Only the final three stages justify claiming production integration.

---

## 13. Real-artifact validation strategy

Validation must use real decks and rendered artifacts, not only schema validity.

### 13.1 Minimum real task set

At least the following should be held out from implementation tuning:

1. a CAT-TRACE research group-meeting deck with advisor decisions;
2. a conference-length research talk from a manuscript;
3. a defense or long seminar with prerequisites and backup material;
4. a bounded existing-deck revision with accepted pages;
5. a strict template-constrained CUHK Beamer deck;
6. a native editable PPTX task;
7. a business decision deck.

### 13.2 Review dimensions

Each task should be reviewed on:

- audience and purpose fidelity;
- scientific/source fidelity;
- narrative dependency and first-use;
- page job clarity;
- visual object utility rather than mere presence;
- figure/table/equation claim alignment;
- slide-to-slide transitions and whole-deck rhythm;
- spoken readability and notes separation;
- template fidelity and editability;
- rendered layout, text layer, citations, accessibility;
- scope preservation in revision mode;
- whether the final discussion question or call to action has real decision value.

### 13.3 Evidence design

A candidate architecture should be compared against the current production route on the same source package. The review must include the whole deck and high-resolution problem pages. Page-level findings must be linked to visible evidence and, after repair, to actual source and pixel changes.

A successful validator run is supporting evidence only. A task fails if the artifact is unusable, misleading, visually incoherent, or outside the requested scope even when every mechanical check passes.

### 13.4 Maturity threshold

Promotion beyond baseline requires repeated real success across at least three research modes and one revision mode, with no silent fallback, plus one renderer other than exact CUHK Beamer. The Critic should decide the exact count; this plan rejects any threshold based solely on fixtures.

---

## 14. Non-substitutable semantics

The following cannot be replaced by a generic fallback:

- user-specified audience, duration, purpose, and template;
- source-grounded scientific claims, numbers, equations, uncertainty, and citations;
- page job and deck-level dependency order;
- first-use explanation for central terms and objects;
- requested editability and exact-template use;
- accepted-element preservation in revision mode;
- the distinction between visible slide content and speaker notes;
- a figure's scientific meaning and encoding;
- review scope and reviewer authority;
- a real rendered artifact for final visual judgment.

When any of these is unavailable, the correct result is an explicit blocker or narrower deliverable—not generic cards, paragraph dumps, screenshots pretending to be editable, fake charts, or synthetic evidence.

---

## 15. Red-team failure paths

1. The storyboard file is complete, but the deck is visually dull or confusing because page briefs were treated as form fields rather than design reasoning.
2. Every page has a job, but the jobs do not form a coherent belief update.
3. First-use records pass numerically, but the explanation is too brief or appears on a page the audience cannot parse.
4. Every page contains a scientific object, but the selected object is the wrong representation for the claim.
5. A diagram is technically correct but merely decorates a process already obvious from text.
6. A figure is valid as a paper figure but fails in a talk because the decisive comparison is not visible at presentation distance.
7. Slide copy becomes natural and concise while the page job, transition, or evidence selection remains wrong.
8. The reference library is queried and logged but does not alter the artifact.
9. A gold composition alters the artifact but imposes an irrelevant structure.
10. Beamer compiles and the text layer passes, yet the audience cannot follow the story.
11. Page QA passes while the contact sheet reveals monotonous rhythm or excessive cumulative density.
12. A visual reviewer inspects four pages and issues a global PASS.
13. The authoring model writes the deck and then acts as an “independent” reviewer.
14. A revision fixes the requested pages but changes accepted typography, citations, or diagrams elsewhere.
15. The exact template is imitated through colors and boxes instead of loaded and used.
16. A missing native renderer silently degrades to image-only slides.
17. A synthetic deck benchmark passes while a real group meeting remains unusable.
18. Business mode receives research-specific evidence-board or CUHK defaults.
19. The language handoff changes a cautious claim into a stronger assertion.
20. The presentation layer redraws a statistical figure and changes the estimand or uncertainty encoding.

Any future implementation should include explicit evidence showing how these paths are blocked in the normal user entrypoint.

---

## 16. Proposed future implementation phases

These are bounded architectural phases, not Executor prompts and not authorization to start.

### Phase 1 — Real front door with separated new-deck and revision contracts

**New user capability:** ordinary requests enter the correct mode without knowing internal schemas; a three-page revision cannot silently become a full regeneration.

Work would consolidate routing, task contracts, source inventory, blockers, and scope preservation while continuing to use existing renderers where suitable.

### Phase 2 — Storyboard-centered research communication on real decks

**New user capability:** group meeting, conference, and defense tasks receive explicit audience belief updates, narrative dependencies, page jobs, first-use order, transitions, and decision-valued endings before slide copy or geometry is produced.

Acceptance must use CAT-TRACE and at least one independent real research deck.

### Phase 3 — Renderer and template adapters

**New user capability:** the same semantic storyboard can produce exact CUHK Beamer, editable PPTX, or another declared format without changing the scientific story or silently degrading editability.

This phase should reuse mature external layout/render mechanisms rather than rebuild inferior ones.

### Phase 4 — Artifact-grounded review and bounded repair

**New user capability:** the normal entrypoint reviews the whole rendered deck, reports scope-correct findings, maps them to real source edits, and confirms visible repair while preserving accepted content.

### Phase 5 — Optional reference intelligence proven by output effect

**New user capability:** when relevant, the system can use inspected references to improve composition choices without blocking unfamiliar content or copying style blindly.

This phase is justified only by real A/B evidence that reference consumption improves artifacts. A new metadata catalog alone is not a milestone.

### Phase 6 — Business-mode validation or split decision

**New user capability:** business presentation tasks either gain a validated decision-deck route sharing only the appropriate core, or are intentionally separated into a distinct plugin if shared architecture creates routing or quality failures.

---

## 17. What is deliberately NOT being implemented yet

- no production source changes;
- no new storyboard schema;
- no migration of `deck-plan.yaml`;
- no renderer rewrite;
- no plugin or repository version bump;
- no Reviewed Handoff task;
- no new gold composition corpus;
- no template download or bulk vendor;
- no paid review or benchmark;
- no automatic choice between Beamer and PPTX beyond the current system;
- no claim that the reference library is mature;
- no claim that business mode belongs permanently in the same plugin;
- no attempt to freeze the absent clear-language v0.2 interface;
- no deprecation removal before Critic review and migration evidence.

---

## 18. Questions for Critic

1. Is the semantic storyboard sufficiently different from the current deck plan, or will it become the same schema with fewer fields?
2. Does making page job central still underweight deck-level pacing, repetition, and live audience recovery?
3. Should visual composition be one component, or should scientific-object selection and spatial layout be separated?
4. Is five production components the smallest architecture that preserves real behavior?
5. Can exact CUHK remain a well-supported adapter without continuing to distort generic routing?
6. Which current validators prevent real regressions, and which mainly make synthetic tasks observable?
7. Is the proposed reviewer authority too narrow to catch scientific communication failures, or still too broad?
8. Should business presentations remain in this plugin after v0.1, or is a split already justified?
9. Are group meeting, conference, and defense genuinely compatible mode policies, or do any require a separate orchestrator?
10. How should a future generic language layer return conflicts when concise wording cannot preserve a page's scientific meaning?
11. Should the reference library remain optional forever, or can real evidence justify making it mandatory for selected task classes?
12. What real holdout and human-review threshold is sufficient before retiring the current route?
13. Which parts of SlideWeaver or other mature renderers are better used as runtime dependencies rather than selectively ported?
14. Does the proposed presentation/research-writing shared vocabulary create useful interoperability, or a new abstraction that will erase medium-specific reasoning?
15. Which current components should be retired immediately after approval, and which require a compatibility period?

---

### Repository evidence reviewed

- `AGENTS.md`
- `README.md`
- `TODO.md`
- `scripts/codex_marketplace_config.json`
- `docs/design/READER_FACING_COMMUNICATION_PLUGIN_BOUNDARIES.md`
- `docs/workflows/CONTINUOUS_REAL_WORLD_SKILL_REFINEMENT.md`
- `docs/PLUGIN_MATURITY.md`
- `docs/plugin-todos/presentations.md`
- `docs/plugin-changelogs/presentations.md`
- `docs/workflows/RESEARCH_PRESENTATION_REFERENCE_LIBRARY.md`
- `docs/audits/RESEARCH_PRESENTATION_EXTERNAL_METHOD_AUDIT.md`
- `docs/audits/research_presentation_external_method_matrix.json`
- `results/RESEARCH_PRESENTATION_CURRENT_CYCLE_FINAL_REPORT.md`
- `automation/reviewed_handoff/tasks/RESEARCH_PRESENTATION_CURRENT_ROUND.md`
- `results/003_presentations/RESULT.md`
- `skills/tools/documents-media/presentations/research-presentations/SKILL.md`
- `skills/tools/documents-media/presentations/business-presentations/SKILL.md`
- `skills/tools/documents-media/presentations/shared/**`
