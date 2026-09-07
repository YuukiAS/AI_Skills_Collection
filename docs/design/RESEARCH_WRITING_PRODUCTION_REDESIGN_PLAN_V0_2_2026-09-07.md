# Research Writing Production Redesign Plan

**Plan version:** 0.2  
**Status:** READY FOR CRITIC REVIEW / NOT EXECUTION AUTHORIZATION  
**Date:** 2026-09-07  
**Repository:** `YuukiAS/AI_Skills_Collection`  
**Repository baseline reviewed:** `c827037b253a18a928103f22936ddb3477c74a73`

This is a complete versioned architecture plan. It revises, but does not overwrite, `RESEARCH_WRITING_PRODUCTION_REDESIGN_PLAN_V0_1_2026-09-07.md`. Later Critic revisions must be recorded as `v0.3`, `v0.4`, and so on rather than silently replacing this file.

The v0.1 Critic verdict was `REVISE — medium revision`. Four corrections are binding in v0.2:

1. merge the front door, argument/evidence reasoning, and document-type planning into one real research-document orchestrator;
2. restrict the scholarly-evidence service to finding, screening, reading, extracting, verifying, and managing evidence records—it does not own literature synthesis;
3. retire `scientific-writing` as an independent broad production owner, retaining only compatibility routing and selected knowledge during migration;
4. define reviewer independence through frozen artifacts, declared scope, separated review context, and no edit-and-certify authority—not through the word reviewer.

`CLEAR_LANGUAGE_PRODUCTION_REDESIGN_PLAN_V0_2_2026-09-06.md` remains absent from the reviewed repository baseline. This plan keeps a provisional interface to a future generic language layer without treating that missing file, or `READER_FACING_COMMUNICATION_PLUGIN_BOUNDARIES.md`, as frozen production truth.

---

## 0. Why this plan exists

The current research-writing plugin contains substantial useful knowledge: advisor-report planning, claim-evidence reasoning, manuscript section guidance, literature review, citation verification, venue and LaTeX concerns, and reviewer-oriented checks. The failure is architectural rather than total.

Today the plugin is mainly a bundle of one direct reporting skill and two aggregates. The aggregates list multiple source skills and ask the agent to choose one. Several source skills are broad instructional documents with overlapping authority. This arrangement can pass routing tests and still fail to produce a coherent report or manuscript.

The Distributed Imaging report is the strongest real evidence. The first report was factually rich but organized around execution chronology, internal correction rounds, repeated result narration, and project-facing labels. The improved report succeeded because it changed what the document was doing: it opened with what was now known, identified the decisive evidence, stated what could not yet be concluded, moved detailed splits and settings later, and ended with genuine research decisions. Sentence polish was necessary but secondary.

V0.1 correctly separated three responsibility levels:

```text
domain science decides what is true
research-writing decides what this document must argue and contain
generic language decides how the fixed meaning is expressed
```

The Critic identified residual overengineering. V0.1 proposed six runtime components, including a front door, an argument/evidence planner, and document-type orchestrators. Those three are not independently valuable production systems. They are one integrated act of document-level reasoning:

```text
what document is needed, for whom
  -> what the supplied evidence supports
  -> how this document type should organize that support
```

Implementing them as separate components would invite `document_contract.json`, `argument_evidence_brief.json`, `document_plan.json`, and `unit_contract.json` to all pass while the final document remained unreadable.

**Core judgment:** the current flat aggregate is not a viable production center. The selected architecture has four true components: one integrated research-document orchestrator, one scholarly-evidence service, one artifact adapter coordinator, and one scoped document reviewer. The shared research-argument model remains an internal logic contract, not a separate runtime, schema, or mandatory packet chain.

---

## 1. Verified repository reality

### 1.1 Current plugin composition

| Item | Verified repository fact |
|---|---|
| Marketplace plugin | `research-writing` |
| Plugin version | `0.1` |
| Capability status | `unclassified` |
| Direct user-visible skill | `research-reporting` |
| User-visible aggregate | `research-paper-workflow` |
| Paper aggregate sources | `scientific-writing`, `paper-workflow-orchestrator`, `nature-manuscript-workflow`, `latex-paper-authoring`, `venue-templates`, `peer-review`, `scholar-evaluation` |
| User-visible aggregate | `literature-and-citations` |
| Literature aggregate sources | `literature-review`, `citation-verification`, `citation-management`, `research-lookup`, `pyzotero` |
| Main real-use evidence | Distributed Imaging advisor/group-meeting report v1/v2 and repository review notes |
| Historical routing evidence | task `001_research_writing`, its results/review, and `tests/test_research_writing_routing.py` |

### 1.2 What the current skills actually do

**VERIFIED FACT.** `research-reporting/SKILL.md` is the clearest current document workflow. It covers audience and decision purpose, source inventory, claim-evidence reasoning, decisive evidence, tables, main-body versus appendix separation, and a later language pass.

**VERIFIED FACT.** `paper-workflow-orchestrator/SKILL.md` describes claim-evidence spines, result-to-claim gates, section contracts, figure/text synchronization, rebuttal planning, and submission checks. Its current source tree does not implement an end-to-end coordinator comparable to those claims.

**VERIFIED FACT.** `scientific-writing/SKILL.md` spans IMRaD, section drafting, paragraph prose, citations, figures/tables, reporting guidelines, style, professional reports, and LaTeX. It overlaps research-reporting, the generic language layer, evidence services, visualization, and artifact production.

**VERIFIED FACT.** `literature-review/SKILL.md` combines systematic/scoping/narrative review, related work, single-paper cards, search, screening, synthesis, verification, and output generation. Its current text also advertises broader scripts/assets than are present in its source tree.

**VERIFIED FACT.** `citation-verification/SKILL.md` has a comparatively clear specialist boundary: source existence, metadata consistency, DOI/PMID/BibTeX checks, claim support, and citation drift.

**VERIFIED FACT.** `peer-review` and `scholar-evaluation` are currently packaged inside the same aggregate as authoring. Packaging does not create operational independence.

**VERIFIED FACT.** `nature-manuscript-workflow` is a specialized manuscript policy. `latex-paper-authoring` concerns source and compilation. `venue-templates` advertises a broader template/helper ecosystem than its current source tree contains.

### 1.3 What the aggregates actually do

**VERIFIED FACT.** The generated `research-paper-workflow` aggregate lists source workflows and instructs the model to select one. It does not maintain a shared manuscript state, resolve authority conflict, or coordinate report/manuscript/rebuttal/supplement production through one observable entrypoint.

**VERIFIED FACT.** `literature-and-citations` similarly routes among discovery, review, verification, bibliography, and Zotero workflows. It is a routing convenience, not a unified evidence runtime.

**INFERENCE.** Current skills may be individually useful, but the plugin does not yet have one production coordinator whose end-to-end behavior can be validated on real documents.

### 1.4 Meaning of historical PASS

**VERIFIED FACT.** The `001_research_writing` task explicitly froze the top-level aggregates and disallowed merge/delete. Its PASS validly established narrower trigger boundaries, generated parity, and test/CI success.

**VERIFIED FACT.** `tests/test_research_writing_routing.py` mainly checks membership and boundary phrases.

**INFERENCE.** That evidence cannot establish that the current aggregate architecture is optimal or that it produces advisor-ready and submission-ready documents.

### 1.5 Real report evidence

**VERIFIED FACT.** The Distributed Imaging v2 report moved the main narrative toward the scientific question, key evidence, bounded conclusions, limitations, and next decisions, with detailed splits/settings/numbers later. Repository feedback explicitly rejects audit tokens, correction rounds, execution chronology, repeated table narration, invented short scripts, and decorative advisor questions.

**INFERENCE.** The decisive improvement was document architecture and content selection, not local wording alone.

### 1.6 V0.2 revision fact

**VERIFIED FACT.** No production source changed between the v0.1 plan and this v0.2 planning task. The reviewed main adds only the v0.1 design documents.

**PROPOSAL.** V0.2 changes design authority only. It does not authorize implementation, migration, retirement, benchmark execution, or version bumps.

---

## 2. Product target

Research-writing should give a researcher a defensible, source-grounded research document whose purpose, contribution or decision logic, evidence selection, section structure, literature authority, and artifact form are coherent for the intended reader.

It is not a tool for producing academic-sounding paragraphs. Its product is:

> A research argument or decision record in document form, with explicit claim boundaries, sufficient and traceable evidence, deliberate allocation among prose/tables/figures/appendices, and a usable final artifact.

| Task family | Final artifact | Real success | Mechanical PASS can still fail when… |
|---|---|---|---|
| Advisor/group-meeting report | Markdown/Word/PDF plus optional internal appendix | advisor understands question, decisive evidence, uncertainty, and next decision | report remains an execution log |
| Technical research report | structured report and reproducibility appendix | methods, evidence, limitations, and reproduction boundary are clear | every run is listed but the scientific comparison is unclear |
| Manuscript | source, figures/tables/references, rendered output | contribution, claims, evidence, and section jobs are defensible | all IMRaD sections exist but contribution is obscure |
| Literature review | synthesis plus evidence/search records where appropriate | themes, method comparisons, contradictions, and gaps are clear | many valid citations replace synthesis |
| Related work | manuscript-ready section plus evidence map | prior work is fairly synthesized and the paper is positioned honestly | the section becomes a name list or novelty exaggeration |
| Rebuttal | response letter plus manuscript-change map | each concern is answered by evidence, concession, or scoped change | polite wording hides an unresolved scientific objection |
| Supplement/appendix | supporting package | reproducibility/detail is complete without hiding decisive evidence | important support is exiled merely to shorten the main text |
| Pre-submission review | findings ledger and scoped readiness status | major risks are exposed and tracked | the authoring model gives itself a score and PASS |
| Citation workflow | verified/unsupported/unresolved ledger | support status is source-backed | DOI formatting is correct but the source does not support the sentence |

These tasks share research questions, claims, evidence, uncertainty, literature authority, and reader obligations. They do not require one identical stage sequence.

---

## 3. Current architecture map

The current paper route is approximately:

```text
user request
  -> research-paper-workflow aggregate
  -> select one source skill
     scientific-writing / paper-workflow-orchestrator / Nature / LaTeX /
     venue / peer-review / scholar-evaluation
  -> selected skill applies its own instructions
  -> optional handoffs
  -> document or review artifact
```

The current literature route is approximately:

```text
user request
  -> literature-and-citations aggregate
  -> select literature-review / citation-verification /
     citation-management / research-lookup / pyzotero
  -> discovery, synthesis, verification, or library output
```

The reporting route is closer to:

```text
report request
  -> research-reporting
  -> source/audience/purpose reasoning
  -> claim-evidence and content allocation
  -> draft
  -> language and artifact handoffs
```

The reporting route demonstrates the right level of reasoning but is isolated. The aggregates provide routing without coordination, and broad source skills retain overlapping authority.

---

## 4. What currently works

1. **Research-reporting's decision orientation.** It starts from what the reader must understand or decide rather than from run chronology.
2. **Claim-evidence concepts.** Contribution hierarchy, result-to-claim gates, section jobs, and figure-to-claim mapping are valuable when they change the artifact.
3. **Document-type specialization.** Report, manuscript, literature synthesis, rebuttal, supplement, and review have different reader obligations.
4. **Discovery/verification/bibliography distinctions.** The earlier routing work usefully separated these operations.
5. **Citation verification.** Existence, metadata, and support are distinct checks.
6. **Source fidelity and bounded claims.** The current skills repeatedly prohibit invented data, results, citations, and overclaiming.
7. **Artifact awareness.** LaTeX, Word, PDF, figures, tables, appendices, and venue requirements matter, but mechanics should remain adapters.
8. **External provenance.** Mature systems are recorded rather than bulk-vendored.

---

## 5. What may be a dead end

### 5.1 Flat aggregate as production coordinator

A source-skill list is routing, not document production.

**Proposal:** replace the current aggregate as architectural center with one real research-document orchestrator.

### 5.2 Three semantic components producing packet chains

Separating front door, argument planner, and document-type orchestrator invites multiple schemas and handoff files without independent user value.

**Proposal:** combine them into one component. A shared research-argument model remains internal reasoning. A compact working brief may be written when traceability is needed, but no chain of mandatory JSON artifacts is part of the product architecture.

### 5.3 Broad `scientific-writing` authority

It currently owns too much: section purpose, prose, citations, figures/tables, reporting guidance, reports, and artifacts.

**Proposal:** retire it as an independent production owner. Port section-semantic knowledge to the research-document orchestrator, route wording to the generic language layer, route evidence to the evidence service, route figures to visualization/domain owners, and route LaTeX/Word/PDF to artifact adapters.

### 5.4 Scholarly-evidence service owning synthesis

The phrase `synthesis support` is too broad. It allows an evidence service to decide themes, comparability, contradictions, gaps, and novelty positioning.

**Proposal:** evidence service supplies inspected evidence records and status. The research-document orchestrator alone owns literature synthesis in the document argument.

### 5.5 Reviewer independence by role name

The same model/context writing, switching persona, rewriting, and giving itself PASS is not independent review.

**Proposal:** independence must be evidenced by a frozen artifact, declared scope, separated review execution/context, artifact identity, and prohibition on editing the reviewed version.

### 5.6 Quantitative score as readiness

`scholar-evaluation` can produce a requested rubric. It cannot establish publishability and should leave the default production route.

### 5.7 Paper workflow as mandatory stage machinery

PaperSpine-like gates can be useful, but a fixed full pipeline can overburden advisor reports, scoped revisions, and mature manuscripts.

### 5.8 Ghost venue/template capability

A skill should not claim current templates, scripts, or venue rules that are absent or stale.

### 5.9 Artifact success as document success

A compiled PDF, correct bibliography, or valid cross-reference does not prove good contribution/evidence architecture.

---

## 6. Authority boundaries

The shared order is:

```text
domain semantics
  -> research-document information architecture
  -> generic language and domain-valid figure handoffs
  -> artifact adapter
  -> scoped review
```

### 6.1 Domain plugins

`statistical-modeling`, `medical-imaging`, `bioinformatics`, and other domain owners decide whether methods, estimands, analyses, results, uncertainty, and scientific interpretations are valid. Research-writing may expose contradiction or missing support but cannot repair science by changing a model, comparator, or conclusion.

### 6.2 Research-document orchestrator

It owns:

- user front door and bounded task scope;
- document purpose and audience;
- research/decision question as presented to the reader;
- contribution hierarchy and novelty positioning for manuscripts;
- claims, caveats, counterclaims, alternative explanations, and limitations;
- decisive versus supporting evidence selection;
- evidence sufficiency for declared document claims;
- document-type policy and section/unit jobs;
- narrative dependency and reader order;
- main text versus table, figure, appendix, supplement, notes, or omission;
- literature synthesis, method comparison, contradiction, gap analysis, and related-work positioning;
- reviewer-facing argument and rebuttal/change mapping;
- artifact package requirements, without renderer mechanics.

It does not own underlying scientific truth, citation support verdicts, generic sentence style, statistical visual encoding, or file-format implementation.

### 6.3 Scholarly-evidence service

| Evidence service owns | Evidence service does not own |
|---|---|
| find candidate literature and authoritative sources | final themes or narrative structure |
| execute/document search and screening protocols | decide which methods are scientifically comparable |
| read sources and extract claims, methods, samples, evidence, limitations | reconcile contradictions into the document argument |
| record source pointers and provenance | define the research gap or novelty claim |
| verify citation existence, metadata, and sentence/panel support | write Related Work positioning |
| manage DOI/PMID/arXiv/BibTeX/Zotero records | choose contribution hierarchy or section order |
| return `verified`, `unsupported`, `unresolved`, `not checked` | treat formatted metadata as evidence support |

For a systematic review, this service may operate search, deduplication, screening, and extraction. The research-document orchestrator owns the review question, synthesis categories, interpretation, and written argument. Statistical meta-analysis remains with the statistical domain owner.

### 6.4 Generic language layer

After a document unit's purpose, claim, evidence, caveat, terminology, and relation to neighboring units are stable, the language layer may realize sentences, paragraphs, headings, captions, table notes, and transitions. It may return a conflict when requested compression would delete necessary meaning.

It may not choose the contribution, remove negative evidence, move decisive evidence to the supplement, change claim strength, alter literature positioning, or resolve domain uncertainty.

### 6.5 Scientific visualization

Research-writing owns why a figure/table belongs, what claim or comparison it must support, and whether it belongs in the main text or supplement. `scientific-visualization` owns valid encoding, plot construction, uncertainty display, accessibility, and export. Domain owners validate data and statistical meaning.

### 6.6 Presentations

Presentations may consume a report/manuscript/evidence package, but it owns live spatial-temporal communication. Research-writing does not decide slide order, page job, page composition, or deck rhythm. Manuscript sections are not slide archetypes.

### 6.7 Artifact adapters

LaTeX, Word, PDF, Quarto, MyST, Manubot/Pandoc, venue templates, cross-references, bibliography rendering, compilation, and source packaging are artifact concerns. They do not decide contribution or evidence order.

### 6.8 Review authority and independence levels

Independence is an evidence property, not a role label.

| Review class | Meaning | Verdict authority |
|---|---|---|
| `AUTHORING_SELF_CHECK` | same authoring context checks its own draft | may suggest repairs; no independent PASS |
| `SEPARATED_SCOPED_REVIEW` | separate review execution reads a frozen artifact and declared evidence/scope; reviewer identity/context recorded | may issue scoped findings; call it independent only when separation is evidenced |
| `INDEPENDENT_REVIEW` | fresh separate context, human reviewer, external reviewer, or Text Review process reads a frozen artifact and cannot edit the reviewed version | may issue scoped `PASS`, `REVISE`, or `BLOCKED` |

A reviewer cannot rewrite the same artifact version and certify that rewrite. Findings return to the authoring orchestrator. A new artifact version must be produced and reviewed again. Unresolved major findings block completion for the reviewed scope. Review of selected sections cannot certify the whole manuscript.

---

## 7. Alternative architectures

| Architecture | Strength | Failure risk | Decision |
|---|---|---|---|
| A. Current skill aggregate | low implementation cost and many specialist names | routing without coordination; overlapping authority | reject as center |
| B. V0.1 six-component architecture | explicit responsibilities and traceability | front door/planner/orchestrator become packet-producing bureaucracy | revise, not selected |
| C. Four components with one integrated research-document orchestrator | matches real report behavior and minimizes control-plane artifacts | orchestrator can become too broad unless boundaries are enforced | **selected** |
| D. Formal claim-evidence graph as mandatory core | strong traceability | graph completeness can dominate readability and workflow cost | conceptual model only |
| E. One external end-to-end workflow such as PaperSpine | real orchestrator and gates | fixed stages overfit some document types; authority mismatch | selectively port concepts |
| F. Lightweight router plus Quarto/Manubot/MyST | mature artifact and citation mechanics | does not solve content selection or argument architecture | use beneath selected architecture |

Architecture C is selected. The shared argument model is internal to the orchestrator, while mature external systems handle bounded artifact/evidence mechanics.

---

## 8. Selected architecture

### 8.1 Core domain

Research-writing owns **research argument and evidence architecture for documents**. It turns validated scientific material into a document-specific structure that a reader can evaluate, act on, reproduce, or review.

The core is not prose style, literature retrieval, LaTeX, or reviewer scoring.

### 8.2 Four-component overview

```text
research-document orchestrator
  <-> scholarly-evidence service
  -> generic language / scientific visualization handoffs
  -> artifact adapter coordinator
  -> frozen artifact
  -> scoped document reviewer
```

The orchestrator may call the evidence service iteratively. The reviewer is outside authoring authority.

### 8.3 Integrated research-document orchestrator

This component integrates three questions in one reasoning loop:

1. what document or bounded revision is requested, for whom, and to what end;
2. what claims the supplied domain evidence and literature actually support;
3. how the chosen document type should organize claims, evidence, caveats, and reader action.

It uses an internal research-argument model containing only:

- purpose and audience;
- research or decision question;
- contribution hierarchy where applicable;
- claims and claim strength;
- evidence items, gaps, alternative explanations, and limitations;
- literature relationships and support status;
- section/unit jobs and narrative dependencies;
- prose/table/figure/appendix/supplement allocation;
- unresolved decisions and required owner.

This is a logical contract, not a fifth component. It does not require `document_contract.json`, `argument_evidence_brief.json`, `document_plan.json`, or `unit_contract.json`. A single compact working brief may be persisted when needed for long tasks, collaboration, review traceability, or restart. Its existence is never a completion criterion by itself.

### 8.4 Document modes inside the orchestrator

#### Advisor and technical report

Prioritize the current question, what changed, decisive evidence, bounded interpretation, uncertainty, and next decision. Suppress execution chronology unless it is scientifically relevant. Put reproducibility and internal state later.

#### Manuscript

Add contribution hierarchy, novelty positioning, section contracts, figure-to-claim mapping, reporting obligations, venue constraints, supplement logic, and submission package requirements. Do not begin by filling IMRaD headings.

#### Literature review and related work

The orchestrator defines synthesis themes, method/evidence comparisons, contradictions, gaps, and fair positioning. It consumes inspected evidence records from the evidence service. Related Work serves the manuscript argument but may not distort sources to enlarge novelty.

#### Rebuttal and manuscript revision

Map each reviewer concern to interpretation, evidence need, concession or defense, manuscript change, and unresolved risk. Polite language is downstream. A valid concern may require narrowing a claim.

#### Supplement and appendix

Preserve reproducibility, full derivations, robustness checks, extended tables, and secondary analyses without hiding evidence essential to the main claim.

#### Bounded existing-unit revision

A request to revise one section or paragraph should not launch the full manuscript workflow. The orchestrator establishes the local semantic contract and protected claims, then routes wording to the language layer and performs a bounded document-level regression check.

### 8.5 Scholarly-evidence service

The service exposes distinct operations:

1. candidate discovery;
2. search/screening protocol execution;
3. source reading and evidence extraction;
4. citation existence/metadata/support verification;
5. bibliography and library operations.

It returns evidence records and support states. It does not output the final thematic synthesis, research gap, contribution positioning, or section narrative. Those remain with the research-document orchestrator.

The current `literature-and-citations` user entry may remain temporarily for evidence-only requests. A request for a literature review, related work, or field synthesis enters the research-document orchestrator because synthesis is a document-argument task.

### 8.6 Retirement of broad `scientific-writing`

V0.2 makes a definite decision:

> `scientific-writing` should be retired as an independent broad production owner after a compatibility migration.

Its useful knowledge is redistributed:

- manuscript section jobs and reporting obligations -> research-document orchestrator;
- sentence/paragraph realization -> generic language layer;
- citation support -> scholarly-evidence service;
- figure role -> orchestrator, with encoding by scientific visualization/domain owners;
- LaTeX/Word/PDF mechanics -> artifact adapters.

During migration, the old skill may remain as a thin compatibility route for natural requests such as `rewrite my Results section`. It must delegate rather than retain parallel authority, and it must not remain a second front door indefinitely.

### 8.7 Language timing

Language work may be iterative, but each unit receives a bounded semantic contract first. The language layer returns prose or a conflict. The orchestrator then checks that the result still fulfills the unit and document job. Domain and citation authority remain external.

### 8.8 Artifact adapters

Artifact adapters assemble the approved units, figures, tables, citations, appendices, and templates into source-editable and rendered outputs. Current official venue instructions and user-supplied templates override stale internal claims.

### 8.9 Scoped reviewer contract

A reviewer receives:

- one frozen/versioned artifact identity;
- declared scope and unreviewed scope;
- the relevant claim/evidence/source ledger;
- the target audience/venue requirements;
- no authority to modify the reviewed version.

It returns findings with location, severity, evidence, required owner, and scope. The authoring orchestrator produces a new version. Re-review is required for closure. Numeric rubric scores cannot cancel a major evidence or soundness blocker.

### 8.10 Explicit answers to the required product questions

1. **Core domain:** research argument and evidence architecture for documents.
2. **Report and manuscript:** share one internal reasoning model, not one fixed pipeline or separate runtime core.
3. **`research-paper-workflow`:** not a sufficient production architecture; replace with the integrated orchestrator.
4. **`literature-and-citations`:** may remain temporarily as an evidence-service compatibility entry, not as owner of literature synthesis.
5. **Literature discovery:** scholarly-evidence service.
6. **Citation verification:** scholarly-evidence service as an integrity operation independent of authoring claims.
7. **Peer review / scholar evaluation:** peer review is a separate scoped evaluator; scholar scoring is explicit-only and outside the default production route.
8. **Main body/table/figure/appendix:** research-document orchestrator decides documentary allocation; domain/visualization owners retain scientific and encoding authority.
9. **Contribution and claim hierarchy:** research-document orchestrator, based on domain-validated evidence and user confirmation where strategic judgment is unresolved.
10. **Language layer:** after the unit's meaning and role are stable, before final artifact review; it may not change the document architecture.
11. **Domain knowledge:** enters as validated facts, evidence, uncertainty, and unresolved questions; research-writing organizes but does not recompute or overrule.
12. **LaTeX/PDF/Word:** artifact adapters.
13. **PaperSpine-derived orchestrator:** selectively port contribution-first, result-to-claim, one-front-door, and resumability concepts; replace the current docs-only wrapper as core.
14. **Mature external architecture:** use Manubot/Quarto/MyST/ASReview for bounded mechanics where appropriate; none replaces the research-argument orchestrator wholesale.

---

## 9. Runtime components

The proposed architecture has four production components. Generic language, scientific visualization, and domain plugins are explicit dependencies, not hidden components.

### 9.1 Research-document orchestrator

**Owns:** normal user front door; task scope; purpose/audience; source inventory; research/decision question; contribution/claim/evidence reasoning; document-type policy; section/unit jobs; narrative dependency; decisive/supporting evidence; literature synthesis; main/table/figure/appendix/supplement allocation; bounded language/visualization requests; unresolved-owner routing.  
**Does not own:** domain truth, citation support verdict, generic prose style, figure encoding, renderer mechanics, reviewer PASS.  
**Input:** request, source material/draft, domain-validated evidence, venue/output constraints, evidence-service records.  
**Forbidden input:** internal execution status as scientific evidence; mandatory packet chains; invented contribution, venue, deadline, or result.  
**Output:** document architecture, bounded unit contracts or draft, evidence/asset requests, unresolved questions. A persisted brief is optional and never sufficient evidence of quality.  
**Failure behavior:** expose gaps and return to the correct owner; do not fill sections with generic background or execution chronology.

### 9.2 Scholarly-evidence service

**Owns:** source discovery; search/screening records; source reading; claim/method/evidence/limitation extraction; provenance; citation existence/metadata/support verification; DOI/PMID/arXiv/BibTeX/Zotero operations; support status.  
**Does not own:** themes, comparability, contradiction resolution, research gap, novelty positioning, contribution, section order, or final synthesis prose.  
**Input:** research/evidence question, candidate sources, claims requiring verification, library records.  
**Forbidden input:** model memory as proof; bibliography formatting as support; uninspected abstracts presented as full-text evidence.  
**Output:** source set, evidence records/cards/tables, support ledger, bibliography/library artifacts.  
**Failure behavior:** mark unavailable, partial, unresolved, or unsupported; never fabricate, silently replace, or synthesize beyond inspected evidence.

### 9.3 Artifact adapter coordinator

**Owns:** select and invoke LaTeX/Word/Quarto/MyST/Manubot/Pandoc or venue/template adapters; assemble approved units, figures, tables, references, appendices; compile/render; perform mechanical checks; preserve source editability.  
**Does not own:** argument, claim strength, literature synthesis, reviewer verdict.  
**Input:** approved document architecture/draft, artifact requirements, templates, verified citations, assets.  
**Forbidden input:** stale venue rules treated as current; flattened images replacing editable/source documents without authorization.  
**Output:** source package and rendered artifacts with traceable references and build status.  
**Failure behavior:** fail closed on compilation, missing resources, unresolved citations, unavailable templates, or unsupported output requirements.

### 9.4 Scoped research-document reviewer

**Owns:** declared-scope critique of claim/evidence, contribution clarity, section logic, reporting, literature fairness, limitations, readability, venue fit when requested, rebuttal adequacy, and readiness for that scope.  
**Does not own:** editing and certifying the same version, domain computation, authoring strategy, numeric publishability prediction, global PASS outside reviewed scope.  
**Input:** frozen artifact identity, review scope, target audience/venue, source/evidence ledger, unreviewed-scope declaration.  
**Forbidden input:** authoring self-PASS; mutable draft; partial review presented as whole-document review.  
**Output:** scoped `PASS`, `REVISE`, or `BLOCKED`; findings ledger with location, severity, evidence, and responsible owner.  
**Failure behavior:** unresolved major findings remain open; revised artifacts require fresh review. Same-context self-check is labeled self-review and has no independent PASS authority.

---

## 10. Production entrypoint

One research-writing front door should accept ordinary requests such as:

- `把这两天实验整理成给老师看的组会报告。`
- `从现有结果和图表规划并写成一篇论文。`
- `只重构 Discussion，不要改变结果和引用。`
- `围绕这个问题做 related work，公平说明我们和现有方法的边界。`
- `找几篇最新论文并核验这些引用。`
- `根据审稿意见准备 rebuttal，并标出正文要改哪里。`
- `把 supplement 和 main text 重新分配。`
- `投稿前做一次真正独立、限定范围的审查。`

Normal routing:

```text
evidence-only request
  -> scholarly-evidence service

document/synthesis/revision request
  -> research-document orchestrator
     <-> evidence service as needed
     -> generic language / visualization handoffs
     -> artifact adapter
     -> optional separated scoped review of frozen artifact
```

The user should not need to know internal skill names. A local paragraph or section revision uses a bounded orchestrator mode, not a full manuscript pipeline. A review request does not grant the reviewer edit-and-certify authority.

---

## 11. Existing implementation disposition

| Current implementation | Disposition | Reason |
|---|---|---|
| `research-reporting/SKILL.md` | **KEEP / PORT INTO RESEARCH-DOCUMENT ORCHESTRATOR** | strongest real-use document architecture |
| generated `research-paper-workflow` aggregate | **REPLACE** | routing list is not production coordination |
| `paper-workflow-orchestrator/SKILL.md` | **PORT SELECTED CONCEPTS; RETIRE AS SEPARATE CORE** | useful claim/evidence logic, but no independent runtime value |
| `scientific-writing/SKILL.md` | **RETIRE AS INDEPENDENT PRODUCTION OWNER; TEMPORARY THIN COMPATIBILITY ROUTE** | broad authority conflicts with orchestrator, language, evidence, visualization, and artifact layers |
| `nature-manuscript-workflow/SKILL.md` | **MERGE AS MANUSCRIPT POLICY PACK** | valid specialization, not an architectural center |
| `latex-paper-authoring/SKILL.md` | **KEEP AS ARTIFACT ADAPTER POLICY** | real source/compile concern |
| `venue-templates/SKILL.md` | **RETIRE / REPLACE WITH CURRENT OFFICIAL TEMPLATE ADAPTERS** | advertised resources and currency are not backed by current source |
| `peer-review/SKILL.md` | **KEEP / MOVE TO SCOPED REVIEWER CONTRACT** | valuable critique; remove edit-and-self-certify path |
| `scholar-evaluation/SKILL.md` | **REMOVE FROM DEFAULT ROUTE; EXPLICIT-ONLY OR FUTURE SEPARATE EVALUATION ENTRY** | score is not readiness evidence |
| generated `literature-and-citations` aggregate | **TEMPORARY COMPATIBILITY; REPLACE WITH EVIDENCE-SERVICE ENTRY** | useful access point, but must not own synthesis |
| `literature-review/SKILL.md` | **SPLIT / SIMPLIFY** | search/screen/read/extract operations to evidence service; synthesis/document logic to orchestrator; remove ghost resources |
| `citation-verification/SKILL.md` | **KEEP / STRENGTHEN** | clear support-integrity role |
| `citation-management` | **KEEP AS BIBLIOGRAPHY OPERATION** | record hygiene only |
| `research-lookup` | **KEEP AS DISCOVERY OPERATION** | retrieval only |
| `pyzotero` | **KEEP AS LIBRARY ADAPTER** | library operations only |
| routing keyword tests | **KEEP FOR REGRESSION, NOT MATURITY** | useful boundaries, insufficient product evidence |
| historical task 001 | **REFERENCE_ONLY** | valid bounded routing evidence; top-level architecture was frozen by task design |

---

## 12. External resources / mature implementations

No external system is adopted wholesale.

| Source | Version / commit | License | Capability | Decision |
|---|---|---|---|---|
| `WUBING2023/PaperSpine` current upstream | `1fe46f0e76aab800db381b0a0c392cebe14d86bf` | MIT | one front door, contribution-first, result validation, resumable stages, artifact gates | **SELECTIVELY_PORTED proposed**; no fixed twelve-stage adoption |
| PaperSpine historically integrated locally | `d4529208cda72aa075767611b0265b95b709b550` | MIT | claim-evidence and manuscript concepts | **MERGED concepts; replace wrapper** |
| `manubot/manubot` | `859dd15850d7e89184e75c3a63e9d9e3f9ab9873` | BSD-2-Clause Plus Patent | citation-by-identifier, preprocessing, Pandoc integration | **RUNTIME_DEPENDENCY proposed** for bounded citation/artifact mechanics |
| `manubot/rootstock` | `f44f9bbe35441a8acd51a5898e6e739acaf54c1c` | CC BY 4.0; selected code/data CC0 | source/output separation, CI, collaborative builds | **REFERENCE_ONLY** |
| `quarto-dev/quarto-cli` | `fdf5a968509bc5903b328d9f99bc5d99bc53b149` | MIT | executable scientific publishing, citations, cross-references, multi-format output | **RUNTIME_DEPENDENCY proposed** for selected artifact routes |
| `jupyter-book/mystmd` | `55d3c9a4045a64857e13532c95bd8897ac61972a` | MIT | structured scientific Markdown, citations, HTML/PDF/LaTeX/Word | **REVIEWED_NOT_ADOPTED initially** |
| `asreview/asreview` | `79d568212b2b0a78f9fd7be3c5117dfb890489f9` | Apache-2.0 | transparent systematic-review screening | **CONDITIONAL RUNTIME_DEPENDENCY** for large screening tasks |
| research-skill provenance sources | commits/licenses recorded in repository | recorded per source | overlapping writing/review/research workflows | **existing dispositions retained; no bulk import** |

Mature systems already solve many mechanics. AI_Skills_Collection should not rebuild inferior citation processors, renderers, or screening engines. Its distinctive value is the authority and document-argument layer.

---

## 13. Real-artifact validation strategy

### 13.1 Minimum real task set

1. Distributed Imaging report v1/v2 replay as known evidence, not sole validation;
2. a second independent advisor/technical report;
3. a manuscript from real results and figures;
4. a bounded existing-manuscript revision;
5. related work or literature synthesis with verified sources;
6. rebuttal requiring concession or claim narrowing;
7. supplement/main-text allocation;
8. citation audit containing supported and unsupported claims;
9. at least two artifact routes;
10. a scoped review with deliberately unreviewed sections.

### 13.2 Architecture-specific validation

The implementation must demonstrate:

- one orchestrator performs task, argument, and document-type reasoning without mandatory packet chains;
- evidence service outputs records/status but does not author themes, gaps, or Related Work positioning;
- broad `scientific-writing` no longer independently intercepts and owns full manuscript work;
- same-context authoring self-check cannot become independent PASS;
- reviewer reads a frozen artifact, records scope, cannot edit it, and requires a new version for closure.

### 13.3 Product evaluation

For reports: scientific question before chronology, decisive evidence without repeated narration, bounded claims, clear uncertainty/decision, and appendices that support rather than hide.

For manuscripts: contribution hierarchy, result-to-claim support, visible alternatives/limitations, distinct section jobs, fair literature positioning, justified main/supplement allocation, and current venue obligations.

For literature: inspected sources, traceable claims, explicit unresolved evidence, thematic/method synthesis rather than enumeration.

For review: frozen artifact identity, scope integrity, item-level findings, and no self-edit/self-PASS loop.

### 13.4 Comparative evidence

Compare the current aggregate route, a six-component packet-heavy prototype, and the selected four-component route on the same source package. Intermediate artifacts count only when they visibly improve the final document.

### 13.5 Maturity threshold

Promotion requires repeated real success on at least two report families and one manuscript family, plus evidence that the normal front door invokes the selected orchestrator and authority boundaries. Routing tests, one successful report, or a clean build are insufficient.

---

## 14. Non-substitutable semantics

The following cannot be silently simplified or replaced:

- research question, document purpose, and audience;
- domain-validated methods, data, estimands, results, and uncertainty;
- contribution hierarchy and novelty boundary;
- claim strength, negative results, caveats, and alternative explanations;
- decisive versus supporting evidence;
- source-support status and unresolved literature;
- thematic synthesis, method comparability, contradiction, and gap reasoning;
- main/table/figure/appendix/supplement placement when it affects claim visibility;
- figure/table scientific meaning;
- reviewer findings, review scope, artifact identity, and resolution status;
- user-specified venue/template/output requirements;
- the retirement boundary of broad `scientific-writing`;
- the evidence-service prohibition on owning synthesis.

Unresolved semantics must remain visible. The system must not invent citations, delete caveats, hide weak evidence, manufacture a contribution, or substitute polished prose/compiled PDF for scientific adequacy.

---

## 15. Red-team failure paths

1. `document_contract.json`, `argument_evidence_brief.json`, `document_plan.json`, and `unit_contract.json` all pass while the report remains a log.
2. The four-component design quietly recreates three internal sub-runtimes inside the orchestrator.
3. A claim-evidence map exists but every experiment still enters the main text.
4. Evidence service labels its output `synthesis support` and starts deciding themes, gaps, and novelty.
5. Evidence service finds many papers but none are inspected deeply enough for support claims.
6. `scientific-writing` remains installed as a parallel owner and intercepts manuscript tasks.
7. A compatibility wrapper becomes permanent and preserves the old authority conflict.
8. Every IMRaD section exists but contribution and section jobs remain unclear.
9. Literature citations are valid but Related Work is a paper-by-paper list.
10. Related Work exaggerates difference from prior work despite correct source records.
11. A natural-language pass removes a negative result or caveat.
12. A table is polished but compares scientifically non-comparable conditions.
13. A figure is attractive but does not support its claim.
14. The same model/context writes, changes role name, reviews, revises, and declares PASS.
15. A reviewer edits the draft and certifies the edited version without fresh review.
16. A review of Abstract and Results claims whole-manuscript readiness.
17. `scholar-evaluation` returns 87/100 and masks an unsupported central claim.
18. PaperSpine-style gates pass because files exist while their content is generic.
19. A local Discussion revision launches a full research and artifact pipeline.
20. A compiled PDF uses stale venue rules.
21. Main text hides decisive robustness evidence in the supplement to meet length.
22. A rebuttal defends automatically instead of conceding a valid concern.
23. Systematic screening uses AI ranking without preserving human decisions/stopping rationale.
24. Artifact fallback produces flattened or uneditable output without disclosure.
25. Routing tests pass while the normal user entry still chooses the old aggregate.

---

## 16. Proposed future implementation phases

These are bounded planning units, not implementation authorization and not Codex prompts.

### Phase 1 — Integrated research-document orchestrator

**New user capability:** report, manuscript, literature synthesis, rebuttal, supplement, and bounded revision requests enter one coherent document-level reasoning path without multiple mandatory planning packets.

Real reports and a manuscript must visibly change; a new schema alone does not complete this phase.

### Phase 2 — Scholarly-evidence authority separation

**New user capability:** discovery, screening, reading, extraction, citation verification, and bibliography/library operations return traceable records while synthesis remains with the document orchestrator.

### Phase 3 — Generic-language and visualization handoffs plus `scientific-writing` migration

**New user capability:** research documents receive natural prose and valid figures without parallel ownership of contribution, evidence, or section logic. The broad `scientific-writing` entry becomes a thin compatibility route and is prepared for retirement.

### Phase 4 — Mature artifact adapters

**New user capability:** approved document architecture can render through appropriate Markdown/Word/LaTeX/Quarto/Manubot/MyST routes with current templates, citations, cross-references, appendices, and source editability.

### Phase 5 — Scoped reviewer contract

**New user capability:** frozen artifacts receive scope-correct review whose findings cannot be converted into authoring self-PASS; revised versions require rereview.

### Phase 6 — Compatibility retirement and truthful plugin surface

**New user capability:** obsolete aggregates, ghost resource claims, broad `scientific-writing` authority, and default scholar scoring no longer intercept normal tasks. Compatibility is removed only after real entrypoint replay.

---

## 17. What is deliberately NOT being implemented yet

- no production skill, plugin, profile, generated layer, test, runtime, or workflow change;
- no plugin or repository version bump;
- no new argument/evidence schema;
- no mandatory document packet chain;
- no Reviewed Handoff implementation task;
- no deletion or migration of current skills;
- no adoption of PaperSpine, Quarto, MyST, Manubot, or ASReview as a dependency;
- no venue-template download;
- no paid review or benchmark;
- no claim that the absent clear-language design is frozen;
- no automatic peer-review or scoring loop;
- no domain-science repair inside research-writing;
- no rewriting of the Distributed Imaging reports;
- no implementation prompt.

---

## 18. Questions for Critic

1. Is one integrated research-document orchestrator now the correct minimum, or does it retain hidden overreach?
2. Is the internal research-argument model sufficiently lightweight to avoid becoming a mandatory graph/schema?
3. Does the evidence-service boundary now fully exclude thematic synthesis, comparability, contradiction resolution, gaps, and novelty positioning?
4. Should evidence-only requests remain a user-visible entry inside `research-writing`, or eventually become a separate plugin?
5. Is the retirement decision for broad `scientific-writing` strong enough, and what compatibility period is justified?
6. Are any valuable research-specific prose responsibilities lost by moving realization to a generic language layer?
7. Does the reviewer-independence taxonomy set a sufficiently high bar without making practical review impossible?
8. Can a fresh separate context using the same model count as independent when artifact identity and no-edit authority are proven, or should that be labeled separately?
9. Should `scholar-evaluation` remain explicit-only inside the plugin or move out entirely?
10. Which PaperSpine mechanisms prevent observed failures, and which only create artifacts?
11. Are Quarto/Manubot/MyST best treated as dependencies, adapters, or references for the first implementation?
12. Does the orchestrator have the correct authority over main text versus table/figure/appendix without trespassing on domain science?
13. How should venue space limits be resolved when they conflict with evidence visibility?
14. What second advisor report and manuscript should remain held out for validation?
15. Should report and manuscript maturity be tracked separately within the same plugin?
16. What evidence is required before retiring the old aggregates and compatibility wrapper?

---

### Cross-plan consistency

This plan is consistent with `PRESENTATIONS_PRODUCTION_REDESIGN_PLAN_V0_2_2026-09-07.md`:

```text
domain semantics
  -> medium-specific information architecture
  -> generic language realization and domain-valid visual generation
  -> artifact adapter
  -> scoped artifact review
```

Research-writing owns document argument, literature synthesis, section logic, and documentary allocation. Presentations owns live sequence and page composition. The scholarly-evidence service owns inspected records and support status, not synthesis. Neither plugin owns generic prose or domain truth.

### Repository evidence reviewed

- `AGENTS.md`
- `README.md`
- `TODO.md`
- `scripts/codex_marketplace_config.json`
- `docs/design/READER_FACING_COMMUNICATION_PLUGIN_BOUNDARIES.md`
- `docs/design/RESEARCH_WRITING_PRODUCTION_REDESIGN_PLAN_V0_1_2026-09-07.md`
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
- `YuukiAS/Distributed_Imaging_Inference` report v1, v2, manifest, figures/tables/notes inventory
