# Research Writing Production Redesign Plan

**Plan version:** 0.1  
**Status:** READY FOR CRITIC REVIEW / NOT EXECUTION AUTHORIZATION  
**Date:** 2026-09-07  
**Repository:** `YuukiAS/AI_Skills_Collection`  
**Repository baseline reviewed:** `abaa8ef522a3a37c0248b5ca3aca72f96ebe1a01`

This is a versioned architecture plan, not an implementation task. A later Critic may require `v0.2`, `v0.3`, or `v0.4`; those revisions must be committed as new versioned design files rather than silently overwriting this document.

The task brief identifies `CLEAR_LANGUAGE_PRODUCTION_REDESIGN_PLAN_V0_2_2026-09-06.md` as a candidate neighboring design. That file was **not present on the inspected repository baseline** under `docs/design/`. This plan therefore defines a provisional generic-language interface and records any tension explicitly. It does not treat the absent document or `READER_FACING_COMMUNICATION_PLUGIN_BOUNDARIES.md` as frozen architecture.

---

## 0. Why this plan exists

The current research-writing plugin is not empty or useless. It contains strong research-reporting guidance, several sensible trigger boundaries, a useful distinction between manuscript planning and paragraph drafting, citation verification, literature synthesis, venue and LaTeX concerns, and reviewer-oriented checks.

The problem is that those capabilities do not yet form a coherent production architecture. Today the plugin is primarily a Marketplace bundle containing three user-visible entries:

- `research-reporting`;
- `research-paper-workflow`;
- `literature-and-citations`.

The two aggregate entries are mostly source-skill routers: they list neighboring skills and tell the agent to choose one. Several source skills are very large instructional documents that describe scripts, references, templates, or executable support not present in their current source trees. Historical routing tests mainly assert configuration membership and keyword boundaries. That architecture can pass CI while still failing to plan and produce a good research document.

The real Distributed Imaging report gives the most useful evidence. The first report was factually rich but organized around execution chronology, internal correction rounds, repeated results, and system-facing terminology. The improved report did not succeed merely because sentences became smoother. It changed the document's scientific architecture: it opened with the real research questions, selected decisive evidence, stated bounded conclusions and limitations, moved detailed settings to appendices, and ended with genuine next decisions. This distinction is essential:

- **research-writing** decides what the document is for, what claims matter, what evidence is decisive, how sections depend on one another, and what belongs in main text, table, figure, supplement, or appendix;
- a **generic language layer** realizes that already-decided meaning in clear, natural, reader-facing prose.

**Core judgment:** the current plugin is a historically assembled skill aggregate rather than a mature production system. Its useful knowledge should be retained, but the flat aggregate should be replaced by **document-type orchestrators built on a shared research-argument and evidence core**, with literature/citation as a companion evidence service, peer review as an independent evaluator, and LaTeX/PDF/Word as artifact adapters.

---

## 1. Verified repository reality

### 1.1 Current plugin composition and maturity

| Item | Verified repository fact |
|---|---|
| Marketplace plugin | `research-writing` |
| Plugin version | `0.1` |
| README maturity | `unclassified` |
| Direct user-visible source skill | `research-reporting` |
| User-visible aggregate | `research-paper-workflow` |
| Source skills in paper aggregate | `scientific-writing`, `paper-workflow-orchestrator`, `nature-manuscript-workflow`, `latex-paper-authoring`, `venue-templates`, `peer-review`, `scholar-evaluation` |
| User-visible aggregate | `literature-and-citations` |
| Source skills in literature aggregate | `literature-review`, `citation-verification`, `citation-management`, `research-lookup`, `pyzotero` |
| Main real-use evidence | Distributed Imaging advisor/group-meeting reports and `docs/provenance/RESEARCH_GROUP_MEETING_WRITING_REVIEW_2026_08_29.md` |
| Historical routing evidence | `automation/reviewed_handoff/tasks/001_research_writing/PLAN.md`, results, and `tests/test_research_writing_routing.py` |

### 1.2 What the current skills actually are

**VERIFIED FACT.** `research-reporting/SKILL.md` is the most coherent current document-type workflow. It addresses source-grounded research reports, reader purpose, claim-evidence architecture, decisive evidence, main-body versus appendix separation, tables and interpretation, advisor decisions, and a later writing-style pass.

**VERIFIED FACT.** `paper-workflow-orchestrator/SKILL.md` describes manuscript planning, a claim-evidence spine, section contracts, result-to-claim gates, figure/text synchronization, pre-submission checks, rebuttal planning, and final QA. Its current source tree contains the skill document and lightweight assets/evals, not an implemented coordinator state or runtime comparable to the behavior it describes.

**VERIFIED FACT.** `scientific-writing/SKILL.md` is a broad manuscript-prose skill. It spans IMRaD drafting, paragraph construction, reporting guidance, citations, figures/tables, style, reports, LaTeX, and adjacent concerns. It therefore overlaps research-reporting, the generic language layer, literature/citation, visualization, and artifact production.

**VERIFIED FACT.** `literature-review/SKILL.md` combines systematic/scoping/narrative review, related work, single-paper evidence cards, discovery, screening, synthesis, verification, and output generation. Its text advertises broader scripts/references/assets than are present in its current source tree.

**VERIFIED FACT.** `citation-verification/SKILL.md` has a clearer specialist boundary: source existence, metadata consistency, DOI/PMID/BibTeX checks, claim support, evidence drift, and handoffs to discovery or bibliography management.

**VERIFIED FACT.** `peer-review/SKILL.md` and `scholar-evaluation/SKILL.md` are packaged in the same authoring aggregate as manuscript planning and drafting. `peer-review` is reviewer-style critique and acceptance-risk analysis; `scholar-evaluation` adds fixed-dimensional quantitative scoring. Neither separation guarantees reviewer independence when invoked inside the same self-authoring run.

**VERIFIED FACT.** `nature-manuscript-workflow` is a venue/positioning policy for broad or high-impact journals. `latex-paper-authoring` concerns source structure and compilation. `venue-templates` describes a large venue-template and helper ecosystem, while its current source tree does not contain the advertised template/reference/script collection.

### 1.3 What the aggregate runtime actually does

**VERIFIED FACT.** The generated `research-paper-workflow` aggregate lists seven source workflows and instructs the agent to select and read the matching source. It does not maintain one shared manuscript state, resolve authority conflicts, or coordinate report/manuscript/rebuttal/supplement production through an observable normal entrypoint.

**VERIFIED FACT.** The generated `literature-and-citations` aggregate similarly lists discovery, review, verification, bibliography, and Zotero workflows. It is a user-facing routing convenience, not a unified evidence architecture.

**INFERENCE.** The current plugin therefore has useful specialized instructions but no single production coordinator whose behavior can be validated end to end. “Aggregate exists” is not equivalent to “workflow is coordinated.”

### 1.4 Historical task and test meaning

**VERIFIED FACT.** The historical `001_research_writing` plan explicitly froze the top-level structure, retained the two aggregates, disallowed merging/deleting skills, and focused on trigger boundaries.

**VERIFIED FACT.** Its Planner PASS established that citation-management had been narrowed, related requests routed more clearly, generated files were synchronized, and CI/tests passed.

**VERIFIED FACT.** `tests/test_research_writing_routing.py` primarily checks plugin membership and the presence or absence of boundary phrases.

**INFERENCE.** That PASS is valid for the bounded routing task but cannot be used as evidence that the plugin's production architecture is optimal or that it produces submission-ready manuscripts and advisor-ready reports.

### 1.5 Real advisor-report evidence

**VERIFIED FACT.** The Distributed Imaging report v1 was longer and organized more heavily around experiment order and internal terminology. The later v2 explicitly kept the main body focused on the scientific problem, key evidence, limitations, and next decisions, moving detailed data splits, settings, and numbers to appendices.

**VERIFIED FACT.** The recorded feedback rejects internal `PASS`, commit, audit, correction-round, and pipeline language in advisor-facing narrative; rejects invented “three-minute version” or speech-coach sections; rejects execution chronology as document structure; and requires real advisor questions rather than decorative discussion prompts.

**INFERENCE.** The main production bottleneck was content selection and document architecture, not local sentence fluency alone.

### 1.6 Current source-of-truth caveat

**VERIFIED FACT.** `docs/design/READER_FACING_COMMUNICATION_PLUGIN_BOUNDARIES.md` is a proposal. The clear-language v0.2 file named in the task was absent from the inspected main.

**PROPOSAL.** The architecture below should be judged independently, then reconciled with a later generic-language design. Existing skills and provenance are evidence, not vetoes against retirement or replacement.

---

## 2. Product target

Research-writing should give an ordinary researcher a defensible, source-grounded research document whose purpose, contribution or decision logic, evidence selection, section structure, citations, and artifact form are coherent for the intended audience.

It is not “a tool that writes academic-sounding paragraphs.” Its product is:

> A research argument or decision record in document form, with explicit claim boundaries, sufficient evidence, appropriate literature authority, deliberate allocation among prose/tables/figures/appendices, and a usable final artifact.

The supported task families have different success conditions.

| Task family | Normal entry | Final artifact | Real success | Mechanical PASS can still fail when… |
|---|---|---|---|---|
| Advisor/group-meeting report | “把本周工作整理成给导师看的报告” | Markdown/Word/PDF plus optional internal appendix | advisor understands the question, decisive evidence, uncertainty, and next decision | report is a complete execution log; internal statuses dominate; question for advisor is fake |
| Technical research report | “整理成可复现的技术报告” | structured report plus evidence/reproducibility appendix | methods, evidence, conclusions, limitations, and reproduction boundary are explicit | every run is listed but the scientific comparison is unclear |
| Manuscript | “从结果做成投稿稿件” | manuscript source plus figures/tables/references and rendered output | contribution hierarchy and evidence are clear, section contracts are fulfilled, claims are bounded | all IMRaD sections exist but novelty and decisive evidence are obscure |
| Literature review | “系统梳理这个方向” | synthesis, evidence table, search/screening record where applicable | literature is organized by concepts/methods/evidence, not paper-by-paper chronology | citations are numerous and valid but synthesis is absent |
| Related work | “重写 related work 并定位我们的工作” | manuscript-ready section plus evidence map | prior work is synthesized and the manuscript's boundary is fair | sources become a name list or are distorted to exaggerate novelty |
| Rebuttal | “根据审稿意见准备回复” | response letter plus manuscript-change map | each concern is understood, answered with evidence or concession, and linked to real changes | tone is polite but the scientific concern is not resolved |
| Supplement | “整理 supplement” | supplement/appendix package | supporting detail is complete without hiding evidence required for main claims | decisive evidence is pushed out merely to shorten the main text |
| Pre-submission review | “投稿前按审稿人检查” | independent findings and readiness status | major scientific/reporting risks are exposed, not self-certified away | the authoring model gives itself a high score |
| Citation workflow | “检查这些引用是否真的支持正文” | verified/unsupported/unresolved citation ledger | claim support is source-backed and traceable | DOI formatting is valid but the source does not support the claim |

These tasks belong to a common research-document domain because they all depend on research questions, claims, evidence, uncertainty, literature authority, and reader obligations. They should not be forced through one identical workflow. The architecture should share a small argument core while using document-type policies for report, manuscript, review, rebuttal, and supplement.

---

## 3. Current architecture map

The present paper route is approximately:

```text
user requests a paper-related task
  ↓
Marketplace routes to research-paper-workflow
  ↓
aggregate chooses one source skill
    ├─ scientific-writing
    ├─ paper-workflow-orchestrator
    ├─ nature-manuscript-workflow
    ├─ latex-paper-authoring
    ├─ venue-templates
    ├─ peer-review
    └─ scholar-evaluation
  ↓
selected skill independently applies its own instructions
  ↓
possibly delegates to literature/citation, language, figures, or LaTeX
  ↓
document or review artifact
```

The literature route is approximately:

```text
user requests papers, synthesis, citation checks, BibTeX, or Zotero work
  ↓
Marketplace routes to literature-and-citations
  ↓
aggregate chooses one source skill
    ├─ literature-review
    ├─ citation-verification
    ├─ citation-management
    ├─ research-lookup
    └─ pyzotero
  ↓
selected workflow produces discovery, synthesis, verification, or library output
```

The direct reporting route is:

```text
user requests research/advisor report
  ↓
research-reporting
  ↓
source intake and purpose/audience reasoning
  ↓
claim-evidence and document plan
  ↓
main-body / table / figure / appendix allocation
  ↓
draft
  ↓
generic writing pass and artifact production
```

The third path is currently closer to a production architecture than the aggregates. The main gap is that report, manuscript, literature synthesis, rebuttal, and evaluation do not share an explicit argument/evidence contract or conflict-resolution policy. They are adjacent instructions rather than coordinated components.

---

## 4. What currently works

### 4.1 Research-reporting's reader and decision orientation

The report workflow correctly prioritizes why the work exists, what evidence changes the current judgment, what remains uncertain, and what the advisor needs to decide. Its main-body/appendix separation addresses a real production failure.

### 4.2 Claim-evidence thinking

The paper orchestrator's claim-evidence spine, result-to-claim gate, section contracts, and figure/text synchronization are valuable concepts. They should be strengthened, not preserved merely as checklist language.

### 4.3 Document-type specialization

Nature/broad-journal framing, venue requirements, LaTeX authoring, rebuttal, and citation verification are genuinely different concerns. The redesign should not collapse them into one generic prose skill.

### 4.4 Literature synthesis versus citation verification

The routing work correctly distinguishes synthesis, current paper discovery, bibliography management, and claim-support verification. This distinction remains useful even if the aggregate packaging changes.

### 4.5 Citation verification as an integrity gate

A citation should be assessed for existence, metadata, and actual support. This is stronger than treating a formatted bibliography as correct.

### 4.6 Source fidelity and bounded claims

The current skills repeatedly prohibit invented data, p-values, citations, or unsupported claims. The real report feedback also supports conditional conclusions rather than dramatic story-making.

### 4.7 Artifact awareness

LaTeX, Word, PDF, venue templates, figures, tables, appendices, and supplements matter. They should remain explicit outputs, although their mechanics should move to adapters.

### 4.8 External provenance

PaperSpine and other external sources are recorded with provenance rather than bulk-vendored. That practice should continue.

---

## 5. What may be a dead end

### 5.1 Flat skill aggregate as production coordinator

Listing source skills and asking the agent to select one does not coordinate a document. It provides routing but no shared state, no authority ordering, and no end-to-end guarantee.

**Proposal:** replace the aggregates as architectural centers. Retain a single user-facing front door, but route into explicit document contracts and shared argument/evidence components.

### 5.2 One broad `scientific-writing` skill owning both meaning and wording

The current skill spans document structure, section drafting, paragraph flow, style, figures/tables, reporting guidance, and artifacts. This makes it easy for a local prose task to silently reframe claims or for a manuscript task to stop at polished paragraphs.

**Proposal:** split its useful content. Research-specific section semantics belong to document-type orchestrators; local reader-facing realization belongs to the generic language layer.

### 5.3 Paper workflow as a checklist without production state

Claim-evidence, section contracts, and final checks are valuable only if they influence the normal authoring path and can be inspected in the actual artifact. A long skill document can describe the right process while the model still writes section-by-section from the source.

**Proposal:** preserve PaperSpine-derived concepts as a shared argument model and observable handoff, not as a docs-only coordinator.

### 5.4 Report and manuscript forced through the same full pipeline

They share claims and evidence but optimize for different reader actions. An advisor report may legitimately foreground uncertainty and a pending decision; a manuscript must establish contribution, relation to literature, reproducible methods, and venue obligations.

**Proposal:** share a core, not a fixed stage sequence.

### 5.5 Literature, citation, bibliography, and authoring treated as one undifferentiated domain

Discovery mechanics, evidence synthesis, claim-support verification, and reference-library hygiene have different authorities and failure modes.

**Proposal:** retain them as a companion scholarly-evidence service with explicit statuses. Research-writing owns why and where evidence is used; provider tools own retrieval; citation verification owns support verdicts.

### 5.6 Author self-review and self-scoring

Embedding peer review and quantitative scholar scoring inside the same aggregate invites “write → score → PASS” behavior. Numeric scores can create false certainty.

**Proposal:** peer review becomes an independent evaluator mode. `scholar-evaluation` is removed from the default authoring path and retained only if Critic identifies a real user need for rubric scoring.

### 5.7 Venue-template claims without real assets or current-source verification

A skill that advertises many venue templates or scripts but does not contain them can produce false confidence and stale requirements.

**Proposal:** retire or replace the current `venue-templates` implementation. Use user-supplied templates and current official venue instructions at runtime, with artifact adapters handling mechanics.

### 5.8 Fixed, heavy workflow borrowed wholesale from an external system

PaperSpine's contribution-first and single-entry ideas are useful. Its current twelve-stage gate system, mandatory artifacts, fixed candidate counts, internal humanize stage, and author-side reviewer audit are not automatically appropriate for every report, short revision, rebuttal, or existing manuscript.

**Proposal:** selectively port concepts, not the whole workflow.

### 5.9 LaTeX/PDF as the architecture

Compilation success is not research-writing success. LaTeX, Word, Quarto, MyST, and Manubot are mature production tools below the information architecture layer.

**Proposal:** use mature renderers and manuscript toolchains rather than recreating them, but never delegate contribution, claim, or evidence decisions to them.

---

## 6. Authority boundaries

The provisional authority chain is:

```text
domain semantics
  ↓
research-writing information and argument architecture
  ↓
generic language realization
  ↓
artifact rendering
  ↓
independent evaluation
```

The arrows are handoffs, not permission for downstream layers to rewrite upstream meaning.

### 6.1 Domain plugins

`statistical-modeling`, `medical-imaging`, `bioinformatics`, and other domain owners decide whether methods, estimands, analyses, results, uncertainty, and scientific interpretations are valid. Research-writing may expose contradictions, missing evidence, or unsupported transitions, but it may not repair them by inventing a model, changing a comparison, or strengthening a conclusion.

The domain handoff should provide validated statements, evidence artifacts, uncertainty/limitations, and unresolved scientific questions. Research-writing decides documentary role and order.

### 6.2 Research-writing

Research-writing owns:

- document purpose and audience;
- research-question framing as represented to the reader;
- contribution hierarchy and novelty positioning for manuscripts;
- claim, counterclaim, limitation, and uncertainty structure;
- evidence sufficiency for the document's declared claims;
- decisive versus supporting evidence selection;
- section jobs and narrative dependencies;
- main text versus table, figure, appendix, supplement, or omission;
- literature synthesis and the role of citations in the argument;
- reviewer-facing argument, rebuttal structure, and change mapping;
- artifact package requirements, without owning renderer mechanics.

It does not own the underlying scientific truth, sentence-level language after meaning is fixed, statistical figure encoding, or file-format implementation.

### 6.3 Generic language layer

The language layer receives a bounded unit whose meaning, evidence, claim strength, terminology constraints, and section job are already specified. It may improve sentences, paragraphs, headings, captions, table notes, transitions, and local explanations.

It may not:

- choose the contribution;
- remove a negative result or caveat because it disrupts flow;
- move decisive evidence to an appendix;
- decide which experiments support the main claim;
- change statistical or domain semantics;
- alter literature positioning;
- convert an unresolved claim into a confident conclusion.

Language can return a conflict—for example, “the requested compression cannot preserve this caveat”—rather than silently changing meaning.

### 6.4 Presentations

Presentations may consume a research-writing output as a source package, but it owns live spatial-temporal communication. Research-writing does not decide slide order, page jobs, deck rhythm, or visual hierarchy. Presentations does not inherit manuscript sections as slides.

The two may share the concepts of audience, question, claim, evidence, and uncertainty, but not one universal runtime schema.

### 6.5 Scientific visualization

Research-writing owns the documentary role of a table or figure:

- what question it answers;
- which claim it supports;
- whether it belongs in main text or supplement;
- what comparison and caption obligations exist.

`scientific-visualization` owns valid encoding, plot construction, uncertainty display, visual accessibility, and export. Domain owners validate the data and statistical meaning. Research-writing may request a redesign but cannot silently change axes, estimands, or preprocessing.

### 6.6 Citation and literature services

Research-writing owns the literature question, inclusion purpose, synthesis, novelty positioning, and placement in the argument.

Discovery services own retrieval from current sources. Citation verification owns existence, metadata, and claim-support status. Bibliography/Zotero services own record hygiene and library operations. An authoring component may not mark a citation verified merely because it generated the citation.

### 6.7 Documents and rendering

LaTeX, PDF, Word, Quarto, MyST, Manubot, Pandoc, and venue templates are artifact systems. They own source assembly, cross-references, bibliography rendering, template mechanics, compilation, and output checks. They do not decide contribution, evidence, or section logic.

### 6.8 Peer review and evaluation

Peer review is an independent evaluator. It may identify scientific, reporting, evidence, clarity, or venue risks and return findings. It may not quietly rewrite the document and then certify its own rewrite. It cannot declare submission-ready solely from a rubric score.

---

## 7. Alternative architectures

| Architecture | Description | Strengths | Main failure risk | Decision |
|---|---|---|---|---|
| A. Current skill aggregate | three user-visible entries route among many broad source skills | preserves specialist names and low implementation cost | routing is not coordination; overlapping authority; docs-only behavior; self-review loop | reject as production center |
| B. Document-type orchestrators + shared argument core | one front door creates a task contract; report, manuscript, literature synthesis, rebuttal, and supplement use different policies over a shared claim/evidence model | matches real report evidence; avoids forcing one workflow; clear authority and artifact allocation | shared core may become an over-designed schema or fail to capture document-specific logic | **selected** |
| C. Claim-evidence graph core + thin adapters | all documents are generated from a formal graph of questions, claims, evidence, citations, counterclaims, and sections | strong traceability, reuse, citation and figure alignment | graph construction can dominate work; nuanced narrative may not fit; easy to optimize completeness instead of readability | use as conceptual model, not mandatory graph runtime in v0.1 |
| D. Single mature external workflow dependency | adopt PaperSpine or a comparable end-to-end system as the runtime | real orchestrator, one entry, gates, artifacts, current development | fixed stages and policies may overfit manuscript production; integration/authority mismatch; reports and local revisions become too heavy | selectively port concepts; no wholesale adoption |
| E. Lightweight router + mature artifact tools | keep only routing and rely on Quarto/Manubot/MyST/Pandoc plus model judgment | minimal repo-specific machinery; strong rendering/citation ecosystem | mature tools do not solve contribution, evidence selection, or advisor decision architecture | adopt tools below the selected semantic architecture |

Architecture B is selected, with C used as the reasoning model and E used for artifact production. The decision is not based on preserving current skill count. It is based on the real distinction between advisor report, manuscript, review, rebuttal, and literature synthesis, while retaining a shared scientific-argument contract.

---

## 8. Selected architecture

### 8.1 Core domain

The core domain of research-writing is **research argument and evidence architecture for documents**. It converts validated scientific material into a document-specific structure that a reader can evaluate, act on, reproduce, or review.

The core is not prose style, literature search alone, LaTeX, or reviewer scoring.

### 8.2 Shared research-argument model

The shared logical model should include only concepts needed across document types:

- purpose and audience;
- research question or decision question;
- contribution hierarchy where applicable;
- claims and claim strength;
- evidence items and their validity/status;
- evidence sufficiency and gaps;
- counterclaims, alternative explanations, and limitations;
- literature authority and novelty/relationship;
- figure/table roles;
- section jobs and narrative dependencies;
- main/appendix/supplement allocation;
- unresolved decisions and required human/domain input.

This is a **logical contract**, not authorization to create a large schema. A Markdown evidence/argument brief may be more appropriate than JSON for early production. Formalization is justified only when it prevents a demonstrated failure.

### 8.3 Document-type orchestrators

#### Advisor and technical report

The report orchestrator prioritizes current scientific question, what changed, decisive evidence, bounded interpretation, uncertainty, and next decision. It suppresses execution chronology unless chronology itself is scientifically relevant. Reproducibility details and internal status move to an appendix or separate evidence package.

#### Manuscript package

The manuscript orchestrator adds contribution hierarchy, novelty positioning, section contracts, figure-to-claim mapping, reporting obligations, venue constraints, rebuttal readiness, supplement logic, and a submission package. It must not begin from “fill IMRaD sections.” It begins from the contribution and evidence that justify a manuscript.

#### Literature synthesis and related work

This orchestrator turns a research question and source set into themes, method/evidence comparisons, contradictions, gaps, and fair positioning. Discovery and screening may be delegated; synthesis remains a research-writing responsibility. Related work is not merely a shortened literature review: it serves the manuscript's argument while preserving fairness.

#### Rebuttal and revision

This mode maps each reviewer concern to interpretation, required evidence, response strategy, manuscript change, and unresolved risk. Polite wording is downstream. A rebuttal must be able to concede or narrow a claim rather than defend automatically.

#### Supplement and appendix

This mode ensures that material supporting reproducibility, secondary analyses, derivations, full tables, and robustness checks is complete. It must prevent the main document from hiding evidence essential to its principal claims.

### 8.4 Scholarly-evidence companion service

The current literature-and-citations area should remain accessible to the user but be reconceived as a companion service with distinct operations:

1. **discovery** — locate current candidate sources;
2. **screening and evidence extraction** — identify relevant records and extract claims/methods/evidence;
3. **synthesis** — organize evidence for the document question;
4. **citation verification** — verify existence, metadata, and claim support;
5. **bibliography/library management** — produce clean records and manage Zotero/BibTeX.

The authoring runtime consumes explicit statuses such as `verified`, `unsupported`, `unresolved`, or `not checked`. It cannot infer verification from citation formatting.

### 8.5 Independent evaluation

Peer review is invoked after an artifact or sufficiently complete draft exists, or earlier for an explicit adversarial design review. It returns findings to the user/authoring orchestrator. It does not share the final PASS authority with the authoring run.

Quantitative `scholar-evaluation` is optional and outside the default path. A score may summarize a requested rubric; it is not evidence of publishability.

### 8.6 Language timing

Language realization may occur iteratively, but only after the relevant semantic unit is stable enough:

1. research-writing fixes the unit's purpose, claim, evidence, caveat, terminology, and relation to neighboring units;
2. generic language realizes clear reader-facing prose;
3. research-writing checks that the realization still serves the section/document contract;
4. domain/citation checks remain authoritative for science and support.

This avoids both extremes: writing an entire document before any language feedback, and letting sentence-by-sentence rewriting determine the document architecture.

### 8.7 Artifact adapters

LaTeX, PDF, Word, Quarto, MyST, Manubot/Pandoc, and venue templates are adapters. The selected adapter must preserve cross-references, citations, figures, tables, equations, appendices, and source editability. Current official venue instructions and user-supplied templates override stale internal claims.

### 8.8 Required decisions

1. **Core domain:** research argument and evidence architecture for scholarly documents.
2. **Report and manuscript:** share the argument/evidence core, not one fixed workflow.
3. **`research-paper-workflow` aggregate:** not adequate as production architecture; replace with a true document front door and orchestrators.
4. **`literature-and-citations` aggregate:** retain as a companion user-facing evidence domain only after separating discovery, synthesis, verification, and library authority.
5. **Literature discovery:** not the core responsibility of research-writing; research-writing owns the search question and use of evidence, while discovery providers retrieve candidates.
6. **Citation verification:** belongs in the plugin's companion evidence service and acts as an independent integrity gate, not as prose or bibliography formatting.
7. **Peer review / scholar evaluation:** peer review is an independent evaluator; scholar scoring is optional and removed from default authoring.
8. **Main/table/figure/appendix decisions:** research-writing owns documentary allocation based on claim importance, comparison needs, reader burden, and reproducibility; domain and visualization owners retain scientific/encoding authority.
9. **Contribution/claim hierarchy:** manuscript orchestrator owns its documentary construction, using domain-validated science and user confirmation where strategic judgment is unresolved.
10. **Language layer timing:** after meaning and unit role are fixed, before final artifact review; it may return conflicts but cannot alter scientific architecture.
11. **Domain knowledge:** domain plugins provide validated semantics and uncertainty through explicit handoff; research-writing organizes but does not recompute or overrule.
12. **LaTeX/PDF:** artifact renderers/adapters, not the research-writing core.
13. **PaperSpine-derived orchestrator:** its contribution-first, results-to-claim, one-front-door, and resumable concepts are worth selective porting; the current repo-local docs-only orchestrator should not remain the core.
14. **Mature external architecture:** Manubot/Rootstock, Quarto, and MyST are more mature for artifact/citation/build concerns; PaperSpine is a stronger reference for orchestrated workflow. None replaces the selected research-argument architecture wholesale.

---

## 9. Runtime components

The proposed architecture has **six** production components. Generic language, domain plugins, visualization, and specific renderers are explicit dependencies.

### 9.1 Research-document front door

**Owns:** task-family routing, document purpose, audience, source inventory, existing-draft versus build-from-materials, target venue/output, scope, and blockers.  
**Does not own:** scientific conclusions, contribution selection without evidence/user input, prose, citation support verdicts.  
**Input:** natural-language request, source material, draft, venue/template constraints, available evidence.  
**Forbidden input:** invented deadlines, target journals, word limits, or contribution claims.  
**Output:** document contract and selected orchestrator.  
**Failure behavior:** ask or block on genuinely unresolved strategic constraints; do not launch a full manuscript workflow for a local report revision.

### 9.2 Research argument and evidence planner

**Owns:** research/decision question, contribution hierarchy, claim boundaries, evidence-to-claim mapping, alternative explanations, limitations, evidence sufficiency, and unresolved gaps.  
**Does not own:** domain validity, literature retrieval mechanics, local prose, formatting.  
**Input:** document contract plus domain-validated results, source artifacts, and evidence-service outputs.  
**Forbidden input:** internal process statuses treated as scientific evidence; unverified citations presented as support.  
**Output:** argument/evidence brief and escalation requests.  
**Failure behavior:** mark gaps and return to domain/user; never invent a bridge claim.

### 9.3 Document-type orchestrator

**Owns:** report/manuscript/literature-synthesis/rebuttal/supplement policy; section jobs; narrative dependency; decisive/supporting evidence selection; main/table/figure/appendix allocation; requested reader action.  
**Does not own:** raw scientific computation, figure encoding, sentence style, renderer mechanics.  
**Input:** document contract and argument/evidence brief.  
**Forbidden input:** a universal IMRaD template applied when inappropriate; execution chronology as default narrative.  
**Output:** document plan, unit contracts, artifact package plan, and explicit language/visualization requests.  
**Failure behavior:** block when decisive evidence or section purpose is unresolved; do not fill the document with generic background.

### 9.4 Scholarly-evidence service

**Owns:** discovery delegation, source inventory, evidence extraction, synthesis support, citation verification, metadata/BibTeX/Zotero operations, provenance and status.  
**Does not own:** manuscript contribution, section order, scientific truth beyond what sources support.  
**Input:** research/literature question, candidate sources, claims requiring verification, library records.  
**Forbidden input:** model memory as citation proof; formatted metadata as support proof.  
**Output:** source set, evidence cards/tables, verified/unsupported/unresolved ledger, bibliography artifacts.  
**Failure behavior:** preserve uncertainty and unavailable sources; never fabricate or silently replace evidence.

### 9.5 Artifact coordinator

**Owns:** choose and invoke LaTeX/Word/Quarto/MyST/Manubot/Pandoc or venue/template adapters; assemble figures, tables, references, appendices; render and perform mechanical artifact checks.  
**Does not own:** argument, claim strength, peer-review verdict.  
**Input:** approved document units, artifact package plan, user template, citations/assets.  
**Forbidden input:** stale venue rules treated as current; screenshots or flattened images substituted for editable/source artifacts without authorization.  
**Output:** source package and rendered artifacts with traceable references.  
**Failure behavior:** fail closed on compilation, missing citations, unavailable templates, or unsupported output requirements.

### 9.6 Independent research-document evaluator

**Owns:** reviewer-style critique, claim/evidence and reporting risks, venue fit when explicitly requested, readability at document level, missing limitations, rebuttal adequacy, and declared readiness status.  
**Does not own:** rewriting followed by self-certification, domain computation, numeric publishability prediction.  
**Input:** frozen or versioned draft/artifact, argument brief, source/evidence ledger, declared review scope.  
**Forbidden input:** authoring model's self-reported PASS as evidence; incomplete document presented as globally reviewed.  
**Output:** findings ledger with scope, severity, evidence, and required owner.  
**Failure behavior:** unresolved major findings remain open; no automatic PASS from rubric averages.

---

## 10. Production entrypoint

A normal user should enter through one research-writing front door using ordinary language:

- “把这两天实验整理成给老师看的组会报告。”
- “从现有结果和图表规划并写成一篇论文。”
- “只重构 Discussion，不要改变结果和引用。”
- “围绕这个问题做 related work，说明我们和现有方法的边界。”
- “核验这段话的引用是否真的支持。”
- “根据审稿意见准备 rebuttal，并标出正文要改哪里。”
- “把 supplement 和 main text 的内容重新分配。”
- “投稿前请独立审查，不要替我直接改完再给自己 PASS。”

The front door should:

1. identify the document task and scope;
2. inventory sources and ask domain owners to resolve scientific gaps;
3. build or reuse the argument/evidence brief;
4. apply the relevant document-type policy;
5. call scholarly-evidence services for discovery, synthesis, or verification as needed;
6. hand bounded units to the generic language layer;
7. delegate figures and tables through domain/visualization contracts;
8. render through a mature artifact adapter;
9. invoke an independent evaluator only when requested or required by the document contract;
10. return the artifact, source/evidence status, unresolved risks, and review scope.

Provider-specific database tools, bibliography scripts, LaTeX helpers, and evaluation rubrics are subordinate services. They are not alternative user front doors for a complete research document.

---

## 11. Existing implementation disposition

| Current implementation | Disposition | Reason |
|---|---|---|
| `research-reporting/SKILL.md` | **KEEP / SIMPLIFY / PROMOTE INTO REPORT ORCHESTRATOR** | strongest real-use architecture; remove generic language and renderer overreach |
| generated `research-paper-workflow` aggregate | **REPLACE** | source list/router is not a production coordinator |
| `paper-workflow-orchestrator/SKILL.md` | **PORT CONCEPTS / REPLACE CURRENT CORE** | claim-evidence and section contracts are useful; current docs-only coordinator does not provide end-to-end production behavior |
| `scientific-writing/SKILL.md` | **MERGE / SPLIT / RETIRE AS BROAD STANDALONE AUTHORITY** | retain research-specific unit contracts in orchestrators; move expression to generic language |
| `nature-manuscript-workflow/SKILL.md` | **MERGE AS MANUSCRIPT POLICY PACK** | valuable specialization, but not a separate architectural center |
| `latex-paper-authoring/SKILL.md` | **KEEP AS ARTIFACT ADAPTER POLICY** | real file/source concern; remove authority over contribution and document architecture |
| `venue-templates/SKILL.md` | **RETIRE / REPLACE** | advertised assets and current venue requirements are not backed by its present source tree; use official/current templates |
| `peer-review/SKILL.md` | **KEEP / MOVE TO INDEPENDENT EVALUATOR** | valuable critique, but should not self-certify authoring |
| `scholar-evaluation/SKILL.md` | **REFERENCE_ONLY / OPTIONAL; CRITIC REVIEW FOR RETIREMENT** | fixed scores can create false authority; no default authoring role demonstrated |
| generated `literature-and-citations` aggregate | **REPLACE WITH EVIDENCE-SERVICE FRONT DOOR** | retain convenience but expose operation and authority boundaries |
| `literature-review/SKILL.md` | **SPLIT / SIMPLIFY** | keep synthesis, review methodology, related work, and evidence cards; remove ghost resources/provider/artifact overreach |
| `citation-verification/SKILL.md` | **KEEP / STRENGTHEN AS INDEPENDENT GATE** | clear production value and authority |
| `citation-management` | **KEEP AS BIBLIOGRAPHY SERVICE** | technical record hygiene, not discovery or support verdict |
| `research-lookup` | **KEEP AS DISCOVERY PROVIDER** | current-source retrieval, not synthesis or authoring |
| `pyzotero` | **KEEP AS LIBRARY ADAPTER** | user-library operations, not research-writing logic |
| routing keyword tests | **KEEP FOR REGRESSION, NOT MATURITY** | useful boundary tests; do not prove production behavior |
| historical 001 plan/review | **REFERENCE_ONLY** | valid bounded routing evidence; architecture was frozen by design and must not constrain redesign |

---

## 12. External resources / mature implementations

### 12.1 Evaluated sources

| Source | Version / commit | License | Inspected files | Capability | Decision |
|---|---|---|---|---|---|
| `WUBING2023/PaperSpine` current upstream | `1fe46f0e76aab800db381b0a0c392cebe14d86bf` | MIT | `README.md`, `LICENSE`, `src/skill/SKILL.md` | one front door, document scenes, contribution-first planning, results-to-contribution gate, resumable stages, artifact checks | **SELECTIVELY_PORTED (proposed)**; do not adopt the fixed twelve-stage runtime wholesale |
| PaperSpine version historically integrated locally | `d4529208cda72aa075767611b0265b95b709b550` | MIT | provenance record plus current `paper-workflow-orchestrator/SKILL.md` | claim-evidence spine and manuscript workflow concepts | **MERGED (historical concepts); REPLACE current wrapper** |
| `manubot/manubot` | `859dd15850d7e89184e75c3a63e9d9e3f9ab9873` | BSD-2-Clause Plus Patent | `README.md`, `LICENSE.md`; package entry behavior described for `process`, `cite`, `webpage`, `ai-revision` | citation-by-identifier, manuscript preprocessing, Pandoc integration, reproducible scholarly build | **RUNTIME_DEPENDENCY (proposed)** for citation/artifact mechanics; not argument planning |
| `manubot/rootstock` | `f44f9bbe35441a8acd51a5898e6e739acaf54c1c` | CC BY 4.0; selected code/data dual licensed CC0 1.0 | `README.md`, repository layout and CI/build description | source/output separation, Git versioning, collaborative manuscript build, HTML/PDF artifacts, citation/build CI | **REFERENCE_ONLY** as an artifact/build pattern |
| `quarto-dev/quarto-cli` | `fdf5a968509bc5903b328d9f99bc5d99bc53b149` | MIT | `README.md`, `src/project/types/manuscript/manuscript-types.ts`, manuscript project implementation paths | scientific/technical publishing, executable content, cross-references, citations, multi-format project/manuscript output | **RUNTIME_DEPENDENCY (proposed)** for report/manuscript rendering |
| `jupyter-book/mystmd` | `55d3c9a4045a64857e13532c95bd8897ac61972a` | MIT | `README.md`, license declaration and AST/rendering capabilities | structured scientific Markdown AST, citations/cross-references, HTML/PDF/LaTeX/Word, journal templates | **REVIEWED_NOT_ADOPTED for the first implementation**; reconsider when structured AST/export is required |
| `asreview/asreview` | `79d568212b2b0a78f9fd7be3c5117dfb890489f9` | Apache-2.0 | `README.md` | transparent active-learning screening for systematic reviews, duplicate handling, labels, export | **RUNTIME_DEPENDENCY (conditional proposal)** for large systematic-screening tasks only |
| `docs/provenance/RESEARCH_SKILL_REPOS_2026_07_28.md` sources | exact commits recorded there | licenses recorded there | source-specific inspection recorded in provenance | Academic Research Skills, Nature Skills, research-paper-writing skills, other catalogs | **REVIEWED_NOT_ADOPTED or SELECTIVELY_PORTED as already recorded**; no bulk import |

### 12.2 Architectural conclusions from external systems

Mature systems already solve many artifact and workflow mechanics:

- Manubot handles scholarly source processing and citation-by-identifier;
- Rootstock separates editable content from generated output and uses CI;
- Quarto and MyST provide cross-references, citations, executable content, templates, and multi-format rendering;
- ASReview provides a specialized systematic-screening workflow;
- PaperSpine offers a real single-entry staged orchestrator with contribution-first gates.

AI_Skills_Collection should not rebuild lower-quality citation processors, manuscript renderers, or systematic-screening engines. Its distinctive value should be the research-argument architecture and the routing/authority layer that decides when to use these tools.

PaperSpine is not adopted wholesale because its fixed stage sequence, mandatory research and artifact ledgers, internal humanize stage, and self-contained reviewer audit may overburden advisor reports, scoped revisions, rebuttals, or already-mature manuscripts. Its useful mechanisms should be ported only where they prevent observed failures.

---

## 13. Real-artifact validation strategy

### 13.1 Minimum real task set

A future implementation should be validated on real, held-out artifacts:

1. the Distributed Imaging advisor report family, with v1/v2 comparison available but not used as the only test;
2. a second advisor or technical report from another project;
3. a manuscript built from real results and figures;
4. an existing manuscript revision with a bounded scope;
5. a related-work or literature-synthesis task with verified sources;
6. a rebuttal that requires at least one concession or claim narrowing;
7. a supplement/main-text allocation task;
8. a citation-support audit containing both supported and unsupported claims;
9. at least two artifact routes, such as Markdown→PDF/Word and LaTeX or Quarto/MyST.

### 13.2 Evaluation dimensions

For reports:

- does the document begin from the scientific/decision problem rather than the execution log;
- is decisive evidence selected and interpreted without repetition;
- are claims bounded by the actual data;
- are internal statuses and implementation history appropriately separated;
- does the reader know what remains uncertain and what decision is requested;
- are appendices used for detail without hiding necessary evidence.

For manuscripts:

- is the contribution hierarchy explicit and defensible;
- does each major result support a declared claim;
- are alternative explanations and limitations visible;
- do figures/tables have clear claim roles;
- do sections fulfill distinct contracts and form a coherent dependency chain;
- is literature positioning fair and source-backed;
- are main text, supplement, and appendix allocations justified;
- are venue and reporting requirements current and traceable.

For literature and citations:

- is discovery separated from synthesis;
- can each substantive literature claim be traced;
- are citation support verdicts based on inspected sources;
- are unresolved or unavailable sources marked rather than guessed;
- does related work synthesize rather than enumerate.

### 13.3 Comparative evidence

The selected architecture should be compared with the current aggregate route on the same source package. Human or independent model reviewers must see the actual document and source/evidence map, not only generated planning artifacts.

A good argument brief that does not change the final document is not success. A clean PDF with incorrect content selection is not success. A valid bibliography with poor synthesis is not success. Reviewer PASS is not sufficient when item-level findings remain blocking.

### 13.4 Maturity threshold

Promotion from `unclassified` should require repeated success on at least two report families and one manuscript family, plus evidence that the normal user front door invokes the shared argument core and appropriate document orchestrator. The Critic should set exact thresholds, but no promotion should rely only on routing tests or the existing Distributed Imaging example.

---

## 14. Non-substitutable semantics

The following cannot be silently simplified, inferred, or replaced:

- the research question and document purpose;
- domain-validated methods, data, estimands, results, and uncertainty;
- contribution hierarchy and novelty boundary;
- claim strength and caveats;
- decisive versus supporting evidence;
- negative results that affect interpretation;
- literature inclusion and source-support status;
- main text versus appendix/supplement placement when it affects claim visibility;
- figure/table scientific meaning;
- reviewer concerns and whether they are actually resolved;
- user-specified venue/template/output requirements;
- citation support verdicts;
- independence and scope of evaluation.

If these cannot be resolved, the system must expose the gap. It must not fabricate citations, delete caveats to improve flow, hide a weak result in an appendix, invent a contribution, generate a fake reviewer score, or substitute a polished artifact for scientific adequacy.

---

## 15. Red-team failure paths

1. A claim-evidence map exists, but the document still follows execution chronology.
2. Every claim has some evidence, but the main text includes all evidence instead of the decisive subset.
3. The contribution is named, but the results do not actually validate it.
4. Every IMRaD section exists, but their jobs overlap and the narrative is repetitive.
5. A report is comprehensive, but the advisor cannot tell what decision is needed.
6. The language is natural, but the scientific information architecture is wrong.
7. A compression pass deletes a negative result, limitation, or uncertainty that changes the conclusion.
8. A table is formatted correctly, but the comparison itself is scientifically invalid.
9. A figure is beautiful, but it does not support the stated claim.
10. Citations are real and metadata-valid, but related work is a paper-by-paper list.
11. A citation is formatted through BibTeX, but it does not support the sentence.
12. Literature discovery is extensive, but inclusion criteria and synthesis purpose are undefined.
13. The same model writes, reviews, scores, revises, and declares the manuscript ready.
14. `scholar-evaluation` gives high numeric scores that mask a fatal unsupported claim.
15. A venue template compiles, but the requirements were stale or the wrong article type was used.
16. LaTeX/PDF/Word generation succeeds while cross-references, citations, or appendices are semantically incomplete.
17. PaperSpine-style gates all pass because required files exist, while their content is generic or circular.
18. A report workflow automatically performs a full literature review and manuscript pipeline that the user did not request.
19. A local paragraph revision silently changes contribution or claim strength.
20. Domain plugins are bypassed because the writing system “makes the story coherent.”
21. A manuscript hides decisive robustness evidence in supplement to fit a word count.
22. A rebuttal is rhetorically defensive instead of conceding a valid concern.
23. A systematic review uses AI-ranked screening without preserving human decisions or stopping rationale.
24. A renderer fallback produces a flat image or uneditable artifact without disclosure.
25. A routing test passes because keywords are present while the normal user entry never invokes the intended component.

Future implementation evidence should explicitly show how the normal production path blocks these failures.

---

## 16. Proposed future implementation phases

These are bounded design phases, not Executor prompts and not authorization to begin.

### Phase 1 — Real document front door and document contracts

**New user capability:** ordinary requests for report, manuscript, related work, rebuttal, supplement, citation audit, or independent review enter the correct path without knowing internal skill names, and scoped revisions do not launch an unnecessary full workflow.

### Phase 2 — Shared argument/evidence core on real reports and manuscripts

**New user capability:** reports and manuscripts derive from explicit research questions, claims, evidence sufficiency, caveats, and unresolved decisions rather than execution logs or section templates.

The phase must change real artifacts; creating a schema alone does not count.

### Phase 3 — Document-type orchestrators and content allocation

**New user capability:** advisor reports, manuscripts, literature synthesis, rebuttals, and supplements share evidence but make document-specific decisions about section jobs, main/table/figure/appendix placement, and reader action.

### Phase 4 — Scholarly-evidence authority separation

**New user capability:** discovery, synthesis, citation verification, bibliography management, and Zotero operations return distinct traceable statuses; an authoring run can no longer treat formatted references as verified support.

Where mature tools such as ASReview or Manubot solve a bounded subproblem, use an adapter rather than reimplementing it.

### Phase 5 — Generic-language and visualization handoffs

**New user capability:** research-writing can request clear prose or scientific figures while preserving frozen claims, caveats, terminology, section roles, and evidence. Conflicts return to the correct owner instead of being silently “fixed.”

### Phase 6 — Mature artifact adapters

**New user capability:** the same approved document architecture can be rendered through appropriate LaTeX/Word/Quarto/MyST/Manubot/Pandoc routes with current venue templates, traceable citations, and source editability.

### Phase 7 — Independent evaluator mode

**New user capability:** users can obtain artifact-grounded peer review whose findings remain separate from authoring and cannot be converted into self-certified readiness by a rubric average.

### Phase 8 — Retire obsolete aggregates and ghost claims

**New user capability:** the plugin exposes fewer, clearer, truthful production entries; skills that advertise nonexistent assets or duplicate authority no longer intercept normal tasks.

Retirement should occur only after the new front door and compatibility migration are proven.

---

## 17. What is deliberately NOT being implemented yet

- no production skill, plugin, profile, generated layer, runtime, test, or workflow changes;
- no plugin or repository version bump;
- no new argument/evidence schema;
- no Reviewed Handoff implementation task;
- no migration or deletion of current aggregates;
- no adoption of PaperSpine, Quarto, MyST, Manubot, or ASReview as a dependency;
- no venue-template download;
- no literature search or paid review benchmark;
- no claim that the clear-language v0.2 interface is frozen;
- no automatic peer-review or self-scoring loop;
- no attempt to solve domain scientific validity inside research-writing;
- no rewriting of the Distributed Imaging reports;
- no assertion that current routing tests are obsolete; they remain useful but insufficient;
- no implementation prompt for Codex.

---

## 18. Questions for Critic

1. Is “research argument and evidence architecture” a sufficiently precise core domain, or does it still absorb too much scientific judgment?
2. Can report and manuscript genuinely share one logical core without forcing manuscript contribution logic onto advisor reports?
3. Should literature synthesis be a document-type orchestrator inside research-writing, while discovery and screening are moved to a separate plugin?
4. Is retaining a user-facing `literature-and-citations` companion service still historical bundling rather than coherent product design?
5. Does citation verification need operational independence from both authoring and bibliography management?
6. Is six production components minimal, or can the front door, argument planner, and document orchestrator be safely combined?
7. Should `scientific-writing` be retired entirely, or retain a narrow research-unit realization role distinct from generic language?
8. Does the proposed language handoff happen late enough to protect meaning but early enough to avoid structurally correct, unreadable drafts?
9. Is `peer-review` sufficiently independent if it remains in the same Marketplace plugin?
10. Should `scholar-evaluation` be removed from the plugin rather than retained as optional?
11. Which PaperSpine mechanisms prevent observed failures, and which merely create more mandatory artifacts?
12. Are Quarto/MyST/Manubot best treated as runtime dependencies, optional adapters, or reference implementations?
13. Does research-writing have enough authority to choose main text versus figure/table/appendix without trespassing on domain or visualization owners?
14. How should the system handle disagreement between domain evidence, manuscript strategy, and a target venue's space constraints?
15. What evidence is required before retiring `venue-templates` and the current paper aggregate?
16. Does the current plan understate collaboration/version-control needs for long manuscripts?
17. How should existing manuscripts with a strong author voice bypass unnecessary planning without degrading into local paraphrase?
18. What real second report and manuscript should be held out for validation?
19. Should report and manuscript maturity be tracked separately inside one plugin?
20. Does the proposed boundary conflict with the absent clear-language v0.2 plan in ways that require a joint v0.3 design?

---

### Cross-plan consistency with presentations

This plan and `PRESENTATIONS_PRODUCTION_REDESIGN_PLAN_V0_1_2026-09-07.md` use the same provisional authority order:

```text
domain semantics
  → medium-specific information architecture
  → generic language realization
  → artifact rendering
  → scoped review
```

Research-writing owns document argument, section logic, and documentary evidence allocation. Presentations owns live-deck sequence, page jobs, visual storytelling, and deck rhythm. Neither owns generic sentence style or domain truth. They may exchange audience/question/claim/evidence/uncertainty briefs, but they do not share one universal schema or orchestrator.

### Repository evidence reviewed

- `AGENTS.md`
- `README.md`
- `TODO.md`
- `scripts/codex_marketplace_config.json`
- `docs/design/READER_FACING_COMMUNICATION_PLUGIN_BOUNDARIES.md`
- `docs/workflows/CONTINUOUS_REAL_WORLD_SKILL_REFINEMENT.md`
- `docs/PLUGIN_MATURITY.md`
- `docs/plugin-todos/research-writing.md`
- `docs/plugin-changelogs/research-writing.md`
- `docs/provenance/RESEARCH_GROUP_MEETING_WRITING_REVIEW_2026_08_29.md`
- `docs/provenance/RESEARCH_SKILL_REPOS_2026_07_28.md`
- `automation/reviewed_handoff/tasks/001_research_writing/PLAN.md`
- `results/001_research_writing/RESULT.md`
- `results/001_research_writing/REVIEW_1.md`
- `results/001_research_writing/PLANNER_REVIEW.md`
- `tests/test_research_writing_routing.py`
- `skills/writing/research/research-reporting/SKILL.md`
- `skills/writing/research/paper-workflow-orchestrator/SKILL.md`
- `skills/writing/research/scientific-writing/SKILL.md`
- `skills/writing/research/literature-review/SKILL.md`
- `skills/writing/research/citation-verification/SKILL.md`
- `skills/writing/research/peer-review/SKILL.md`
- `skills/writing/research/scholar-evaluation/SKILL.md`
- `skills/writing/research/nature-manuscript-workflow/SKILL.md`
- `skills/writing/research/latex-paper-authoring/SKILL.md`
- `skills/writing/research/venue-templates/SKILL.md`
- generated `plugins/codex/plugins/research-writing/skills/paper/SKILL.md`
- generated `plugins/codex/plugins/research-writing/skills/litcite/SKILL.md`
- `YuukiAS/Distributed_Imaging_Inference` real report v1, v2, manifest, figures/tables/notes inventory
