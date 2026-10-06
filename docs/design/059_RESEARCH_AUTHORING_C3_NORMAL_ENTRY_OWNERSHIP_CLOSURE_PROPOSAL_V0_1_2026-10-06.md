# 059 Research Authoring C3 正常入口所有权收口 — Repair Proposal v0.1

日期：2026-10-06  
状态：DRAFT_FOR_EXECUTION_READY_CRITIC_REVIEW / NOT_IMPLEMENTATION_AUTHORIZATION  
Repository：YuukiAS/AI_Skills_Collection  
Task：research-authoring--formal-production-authoring  
Branch：work/research-authoring--formal-production-authoring

## 0. Authority and frozen failure

Current failed candidate：

C2=ac501d988f00cb6672fec105ae5fd51a0679cae0

Final evidence head：

1aa52fb737735443dee40cc205e083a3492204f7

Failure authority：

- results/research-authoring--formal-production-authoring/c2_final/C2_FINAL_GATE_STOP_G1_FAIL.md
- docs/design/059_RESEARCH_AUTHORING_C2_G1_FINAL_FAILURE_CRITIC_REVIEW_V0_1_2026-10-06.md
  @ 15f2009fc4e4d276e7ed5720e92be36fe997f4ed
- docs/design/059_RESEARCH_AUTHORING_C2_G1_FINAL_FAILURE_CLOSURE_REQUIREMENTS_V0_1_2026-10-06.md
  @ 15bba2ff6aa3f65e2301a4e90f2087a25fd95946

Frozen facts：

~~~text
C2_G1=FAIL
C2_G1_FAILURE_IMMUTABLE=YES
C2_RELEASE_ADMISSION=FAILED
C2_G2_G3_G4_FINAL_EXECUTION=NOT_CONTINUED
~~~

This Proposal keeps the same 059 task and the same Research Authoring 0.3 release line. It is not a successor task and does not reopen the approved Research Authoring document architecture.

## 1. ROOT_CAUSE

The exact C2 Research Authoring aggregate was consumed, but the renderer was selected before Research Authoring had granted a downstream production handoff.

The decisive trace is：

~~~text
natural request asks Research Authoring to prepare a formal advisor PDF
-> model announces research-reporting + renderer before reading report aggregate
-> exact C2 report aggregate is read
-> aggregate says standalone/no-renderer must stop at source + handoff
-> global render-chinese-math-pdf is still read
-> Pandoc/XeLaTeX + PDF QA executes
-> G1 FAIL
~~~

Therefore：

~~~text
ROOT_CAUSE=
MISSING_EXECUTABLE_NORMAL_ENTRY_OWNER_ADMISSION_BETWEEN
RESEARCH_AUTHORING_AND_RENDERER
~~~

The failure is not missing renderer mechanics and not missing another prohibition sentence inside the generated report aggregate.

## 2. Actual trigger mechanism

Current OpenAI skill behavior matters here.

Official current documentation states：

1. the model first sees Skill metadata, including name and description;
2. the description tells the model when to consider the Skill;
3. full SKILL.md instructions are loaded after the request matches the Skill;
4. installed Plugins/Skills can be used automatically when relevant.

Sources checked on 2026-10-06：

- https://developers.openai.com/plugins/concepts/skills
- https://developers.openai.com/api/docs/guides/tools-skills
- https://developers.openai.com/plugins/guides/optimize-metadata
- https://help.openai.com/en/articles/20001256-plugins-in-chatgpt

This makes the C2 failure structurally explainable：

- the generated Research Authoring aggregate body contains the standalone stop rule;
- but the global renderer description independently matches “produce a PDF” before that body is loaded;
- the renderer can therefore become a co-owner too early.

A profile installing a Skill means the Skill is available/discoverable. It does not by itself prove that the current request has granted that Skill ownership.

There is no current repository/runtime evidence for a hard conditional ACL such as：

~~~text
if active_owner == Research Authoring standalone:
    renderer capability unavailable
else:
    renderer capability available
~~~

Do not invent one.

The strongest existing mechanism is therefore：

~~~text
metadata discovery boundary
+ canonical owner/handoff boundary
+ profile-scoped routing authority
+ real normal-entry replay
~~~

## 3. Three required user-entry modes

The repair must establish one coherent rule across all three modes.

### Mode A — standalone Research Authoring

Natural shape：

> 把这份研究更新整理成正式 PDF。

Expected：

~~~text
Research Authoring owner
-> scientific semantics
-> stable Markdown/LaTeX source
-> complete renderer-production handoff
-> STOP
~~~

Global renderer discovery is not renderer authorization.

No PDF compile, preview, extraction or PDF-derived QA is allowed in this surface.

### Mode B — research-main integrated production

Expected：

~~~text
Research Authoring owner
-> stable semantics/source
-> explicit production handoff
-> render-chinese-math-pdf
-> PDF
-> renderer QA
-> Research Authoring final scientific QA
~~~

The renderer is installed and explicitly admitted by the profile, but only after the document owner finishes the authoring stage.

### Mode C — true render-only

Natural shape：

> 把这个已经最终定稿的 Markdown 渲染成 PDF。

or finalized LaTeX.

Expected：

~~~text
render-chinese-math-pdf direct owner
-> compile/render/QA
~~~

Research Authoring must not force a new document brief or rewrite frozen content.

## 4. Reality-based repair-layer comparison

### Option 1 — generated aggregate only

REJECTED.

C2 final evidence directly falsifies this layer as sufficient.

The report aggregate already said：

- standalone -> source + handoff only;
- no compile/render/preview/QA;
- generic runtime is not a renderer substitute.

The model still selected the renderer before/alongside the aggregate.

Adding more equivalent workflow-note prose would be another symptom patch.

### Option 2 — renderer only

INSUFFICIENT.

Narrowing renderer metadata is necessary to prevent premature selection, but renderer alone cannot decide：

- whether the current Research Authoring surface is standalone;
- whether research-main explicitly authorizes the next production phase;
- what constitutes a complete Research Authoring handoff;
- when final scientific QA returns to Research Authoring.

### Option 3 — Research Authoring canonical core/report only

INSUFFICIENT.

The canonical body can define owner semantics, but C2 proves body instructions can arrive after a competing Skill has already been selected by metadata.

### Option 4 — profile routing only

INSUFFICIENT.

research-main profile notes can sequence an integrated production route and have historical normal-entry evidence, but standalone Marketplace Research Authoring has no such profile authority. Profile notes also cannot repair a globally broad renderer description that is independently selected for a research-document PDF request.

### Option 5 — Research Authoring + renderer + existing profile routing

SELECTED.

This is the minimum combination that acts at all three real control points without adding a routing framework.

It uses only existing mechanisms：

- Skill descriptions / Trigger Boundaries;
- Research Authoring core/delegate owner model;
- profile routing_notes;
- existing aggregate generation;
- normal runtime consumption evidence.

No daemon, routing service, state machine, database or Bridge change is needed.

## 5. Selected mechanism — two-stage owner admission

### 5.1 Discovery stage

The renderer's metadata must stop matching ordinary research-document authoring merely because the requested eventual artifact is PDF.

The renderer should be discoverable as a direct owner when：

1. the input content/source is already final and the task is render-only; or
2. the current workflow has reached an explicit downstream document-owner handoff.

Its metadata must explicitly exclude：

> creating, materially revising, or organizing a research report/manuscript where Research Authoring still owns document semantics, even if the eventual deliverable is PDF.

This is not a command blacklist. It is the user-goal trigger boundary used during Skill discovery.

### 5.2 Research Authoring stage

The canonical core must define an artifact handoff admission rule：

> Renderer discoverability or installation is not renderer authorization.

For a Research Authoring-owned document task, renderer admission requires an explicit current-surface production route.

Accepted current-surface authority：

- integrated research-main routing note explicitly authorizes Research Authoring -> renderer after stable source; or
- a later downstream task explicitly consumes a frozen Research Authoring handoff.

Not accepted：

- renderer exists globally;
- renderer is merely listed in a skill inventory;
- generic runtime can execute XeLaTeX;
- the user mentioned “PDF” while still asking to author/revise the research document.

The handoff remains lightweight, not a new persistent schema. It contains the already-approved fields：

- stable source locator/artifact;
- document family;
- audience/purpose;
- evidence/citation authority;
- table/figure/formula roles;
- formatting/venue/project authority;
- requested artifact;
- downstream renderer owner;
- final Research Authoring scientific-QA callback.

### 5.3 Integrated profile stage

research-main becomes the explicit integrated production composition.

Its routing notes must cover both report and manuscript families：

~~~text
research document + PDF
-> Research Authoring core/family route first
-> stable source + explicit handoff
-> renderer
-> artifact QA
-> document-level scientific QA
~~~

It must also define：

~~~text
finalized source + render-only
-> renderer direct
~~~

and clarify that the generic pdf helper is not the primary owner for creating a new formal research document.

### 5.4 Authoring-only profile

codex-research-writing currently does not include render-chinese-math-pdf, but its description mentions PDFs without an explicit route contract.

It should be clarified as an authoring/source profile：

- manuscript/research source work is allowed;
- formal artifact requests stop at source/package + downstream handoff;
- global renderer discoverability does not upgrade this profile into research-main;
- use research-main for integrated formal-PDF production.

This prevents the same ambiguity outside Marketplace standalone.

### 5.5 Manuscript-specific early-trigger protection

latex-paper-authoring currently has broad discovery metadata and its body says to compile after edits.

For a new/substantially revised manuscript + PDF request, it can otherwise become another premature artifact owner inside research-main.

Its trigger boundary must distinguish：

- direct existing-LaTeX compile/debug/template/source-hygiene work -> direct LaTeX owner;
- Research Authoring manuscript production -> paper/core first; LaTeX skill is a source/package delegate;
- final formal PDF mechanics for the Research Authoring workflow -> renderer after handoff.

The paper aggregate/config should point to this canonical boundary rather than duplicating a new renderer rule.

## 6. Why the generic pdf Skill is not modified now

skills/tools/documents-media/pdf has broad metadata and remains an adjacent routing risk, especially inside research-main.

However：

- the C2 final failure directly names render-chinese-math-pdf, not the generic PDF Skill;
- historical research-main production replays successfully used Research Authoring then the canonical renderer while the generic PDF Skill was installed;
- changing the generic PDF tool has much broader non-research blast radius.

Therefore this Proposal does not preemptively modify the generic PDF Skill.

Instead it is a mandatory should-not-change/negative owner in the C3 development matrix.

If a C3 development replay shows generic pdf actually stealing new research-document production, C3 is not frozen. That would be new direct evidence requiring Planner/Critic before widening scope.

This is a stop condition, not an adaptive hidden patch.

## 7. Exact expected production scope

### Canonical Research Authoring

- skills/writing/research/research-authoring-core/SKILL.md
- skills/writing/research/research-reporting/SKILL.md
- skills/writing/research/paper-workflow-orchestrator/SKILL.md
- skills/writing/research/latex-paper-authoring/SKILL.md

### Renderer

- skills/tools/documents-media/render-chinese-math-pdf/SKILL.md

Renderer scripts/QA implementation are expected to remain unchanged. The failure is entry ownership, not PDF mechanics.

### Profiles / routing source

- profiles/research-main.json
- profiles/codex-research-writing.json
- scripts/codex_marketplace_config.json

The Marketplace config may update report/paper workflow notes only to point at the canonical owner-admission rule. It is not the architecture center.

### Tests

- tests/test_research_writing_routing.py
- tests/test_render_chinese_math_pdf.py

Existing Marketplace/profile tests may change only if current parity generation truthfully requires it.

### Generated layer

Source-first regeneration only：

- plugins/codex/plugins/research-writing/**;
- .agents/plugins/marketplace.json;
- registry/catalog/provenance artifacts only where the existing generators actually change them.

Never hand-edit generated Research Authoring plugin files.

## 8. Version decision

This remains the same 059 Research Authoring 0.3 candidate line.

~~~text
research-writing:
remains 0.3 candidate
NOT 0.4

Repository VERSION:
unchanged during bounded implementation/final gates

maturity:
unchanged
~~~

The standalone renderer currently reports version 0.2.

If the selected renderer trigger behavior is implemented and the full C3 development matrix passes, it is a real user-visible standalone behavior change. Before C3 freeze, the release-candidate metadata should therefore become：

~~~text
render-chinese-math-pdf:
0.2 -> 0.3 candidate
~~~

This does not make a formal repository release. Repository PATCH/version integration remains a later release-closure step after final G1-G4 PASS.

Research Authoring's existing 0.3 candidate changelog is amended, not bumped again.

Any README version/card change requires actual Clear Writing use under repository policy. If that legal writing surface is unavailable during candidate closure, stop before C3 freeze rather than ship mismatched release metadata.

## 9. Development evidence before C3

No new final Gate is consumed until the complete development matrix passes.

The matrix is defined in the Implementation Plan and covers：

- standalone report/formal PDF;
- standalone ordinary advisor report;
- standalone manuscript/formal PDF;
- integrated research-main report/PDF;
- integrated research-main manuscript/PDF;
- render-only finalized Markdown;
- render-only finalized LaTeX;
- neighboring owners;
- global-renderer counterexample;
- unrelated-global-skill counterexample.

Static unit/config tests are supporting evidence only.

## 10. Capability Gate impact

No G5.

The current G1-G4 taxonomy remains intact：

- G1：normal entry / owner boundary;
- G2：research-document semantic organization + incremental update;
- G3：real manuscript/package;
- G4：ChatGPT + Codex final production.

The C3 development matrix is a pre-final regression/admission requirement, not a new release Gate.

C2 G1 FAIL is permanent regression evidence.

After C3 exists, all final G1-G4 evidence must be newly bound to the same C3.

## 11. Rejected architecture expansion

Do not add：

- routing daemon/service;
- database/ledger/state machine;
- new top-level coordinator;
- successor task;
- Bridge workflow;
- renderer install/uninstall tricks;
- prompt command blacklist;
- G1 fixture/path/hash special cases;
- test-only renderer hiding.

If the existing metadata + canonical owner + profile routing mechanisms fail the complete development matrix after this repair, stop and report that the current Skill/Profile platform cannot reliably express the required conditional ownership. Do not manufacture PASS with another wording patch.

## 12. Planner decision

~~~text
ROOT_CAUSE=
MISSING_EXECUTABLE_NORMAL_ENTRY_OWNER_ADMISSION

SELECTED_REPAIR=
RESEARCH_AUTHORING_CANONICAL_BOUNDARY
+ RENDERER_DISCOVERY_BOUNDARY
+ PROFILE_ROUTING_COORDINATION

AGGREGATE_ONLY_REPAIR=REJECTED
RENDERER_ONLY_REPAIR=REJECTED
PROFILE_ONLY_REPAIR=REJECTED

C2=PERMANENT_G1_FAIL
C3=NOT_CREATED

RESEARCH_WRITING_TARGET_VERSION=0.3_CANDIDATE
RENDER_CHINESE_MATH_PDF_TARGET_VERSION=0.3_CANDIDATE_IF_MATRIX_PASSES

FINAL_GATES_NOT_STARTED=YES
LIVE_PLUGIN_MUTATION_AUTHORIZED=NO
READY_FOR_IMPLEMENTATION=NO
NEXT_HANDOFF=CRITIC
~~~
