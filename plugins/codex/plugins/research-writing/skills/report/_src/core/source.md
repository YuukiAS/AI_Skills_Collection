---
name: research-authoring-core
description: Canonical document-level coordinator for Research Authoring. Use before producing or substantially revising reports, manuscripts, related work, research updates, responses, or supplements, including formal-PDF intent. Stabilize source/handoff before admitted rendering; route render-only and support-only work to owners.
status: active
provenance: user-authored
trusted: false
requires_network: false
writes_files: true
executes_code: false
secrets_needed:
last_reviewed: 2026-10-05
profile_tags:
  - research-writing
recommended_scope: project
icon_small: assets/app-facing.svg
icon_large: assets/app-facing.svg
---
# Research Authoring Core

This is the canonical Research Authoring coordinator for reader-facing scholarly documents. It is the document-level owner for research semantics and production organization, not a renderer, statistics engine, generic prose style layer, presentation system, database, or state machine.

## Trigger Boundary

Use this core first when the user is creating, rebuilding, or substantially updating a research document, including:

- advisor, supervisor, group-meeting, milestone, experiment-review, technical-note, research-update, meeting-minutes, preregistration, or analysis-plan reports;
- manuscript sections, full manuscripts, thesis chapters, supplements, submission packages, cover letters, reviewer responses, and rebuttals;
- literature reviews, related-work sections, paper-card syntheses, evidence syntheses, and field summaries that become a reader-facing scholarly document;
- incremental updates to an existing canonical research document after new evidence, decisions, reviewer comments, results, figures, tables, formulas, or citation changes arrive.

Do not force this core for support-only work:

- exact paper lookup, recent-paper discovery, DOI/PMID/arXiv metadata resolution, BibTeX cleanup, Zotero/library hygiene, or citation-support checks;
- content-preserving local prose polishing after the document meaning is already frozen;
- render-only PDF/DOCX/LaTeX mechanics;
- PPT, Beamer, slide-deck, poster, or presentation authoring;
- ordinary research Q&A, model explanation, statistics/method design, or experiment design that does not produce a research document.

If a support-only task later becomes "write these findings into a report, manuscript section, or related-work document", enter this core from that point onward.

## Artifact And Renderer Admission Contract

Research Authoring is the first owner for creating, rebuilding, or substantively revising a research report or manuscript even when the requested final artifact is a formal PDF. A renderer being globally installed, discoverable, or mentioned by another profile is not renderer admission for the current Research Authoring task.

Use this owner sequence:

- Standalone or authoring-only surfaces: produce stable Markdown/LaTeX/source package plus a complete downstream production handoff, then stop. Do not create, compile, open, preview, render, visually inspect, or PDF-QA the artifact by substituting generic runtime/file/compute capability for an admitted renderer.
- Integrated `research-main` production: Research Authoring first stabilizes the source/package and handoff; an admitted renderer then owns PDF mechanics and renderer QA; Research Authoring resumes after rendering for final scientific QA of claims, evidence, citations, figures, tables, formulas, and limitations.
- Render-only finalized source: if the user provides already-final Markdown/LaTeX and asks only for rendering or PDF QA, route directly to the renderer and do not run full Research Authoring planning.

A complete downstream production handoff names the audience, purpose, source authority, claim/evidence boundaries, table/figure/formula roles, citation/bibliography authority, intended format, renderer/route expectations when known, and scientific QA checks that must be revisited after rendering.

## Document Brief

Before drafting or delegating, freeze a compact document brief:

- task intent and requested artifact;
- audience and document purpose;
- document family: `report`, `paper`, `literature-document`, `review-response`, `submission-package`, or another explicit family;
- source authority and evidence boundary: current files, results, notes, figures, tables, citations, user corrections, missing evidence, and facts not to infer;
- claim-evidence spine: main question, supported claims, weak/conditional claims, limitations, and decisions requested from the reader;
- section jobs: what each section must prove or explain;
- main text vs appendix/provenance boundary;
- table, figure, and formula scientific roles;
- citation and bibliography authority;
- incremental-edit scope when an existing document is present;
- downstream owner route and final artifact route.

The brief can live in the current reasoning, task-local evidence, or an implementation packet. Do not create a mandatory persistent schema, database, ledger, or sidecar unless a project or reviewer explicitly requires one.

## Family Routing

After the brief:

- Use `research-reporting` for report-family documents: advisor reports, group-meeting written reports, milestones, research updates, methods notes, experiment retrospectives, research-evolution records, and decision notes.
- Use `paper-workflow-orchestrator` and its paper-family delegates for manuscripts, supplements, submission packages, reviewer responses, rebuttals, and thesis chapters.
- Use `literature-review` for document-producing literature reviews, related-work sections, paper-card synthesis, evidence maps, and thematic syntheses.
- Use `citation-verification`, `citation-management`, `research-lookup`, or `pyzotero` directly when the task is support-only citation, bibliography, lookup, or library work.
- Use Clear Writing support only after Research Authoring has frozen audience, purpose, claim/evidence, allowed structural freedom, and table/figure/formula roles.
- Use `render-chinese-math-pdf`, LaTeX, DOCX, Quarto, or PDF skills only for artifact mechanics after the document semantics are stable and the active profile/surface explicitly admits that downstream production route.
- Use Presentations for PPT/PPTX, Google Slides, Beamer/slide decks, posters, and slide-export PDFs.

## Incremental Authoring Contract

When a canonical document already exists, default to a minimal dependency-closure update:

```text
existing canonical document
+ evidence / decision / reviewer delta
-> affected claims
-> affected section jobs
-> dependent figures / tables / formulas / citations
-> minimal dependency closure
-> local patch
-> diff QA
```

Protect unchanged material by default:

- accepted text outside the dependency closure;
- notation and symbol meanings;
- claim strength, uncertainty, limitation, and evidence boundaries;
- citation keys, attribution, and bibliography authority;
- equation, theorem, figure, table, and cross-reference labels;
- figure/table identity and captions;
- venue or project front matter, macros, and template identity.

Only expand into broad restructuring when the user asks for it, the new evidence invalidates the document spine, the current source has a systemic structure failure, or the venue/project authority changes. When expanding scope, explain why a local patch is insufficient.

## Writing And Owner Boundaries

Research Authoring owns document semantics:

- audience, purpose, document family, section jobs, claim/evidence spine;
- table, figure, and formula roles;
- citation authority and source/provenance boundary;
- incremental edit scope and document-level scientific QA.

Research Authoring does not own:

- statistical method choice, estimands, models, experiments, or mathematical correctness beyond faithful presentation;
- generic style cleanup, de-translation, or local wording after meaning is frozen;
- fonts, pagination, Pandoc/XeLaTeX, PDF QA, Office packing, or renderer implementation;
- slide/deck narrative, deck layout, PPTX, Google Slides, Beamer presentation ownership, or poster design;
- Plugin Creator live mutation, MCP, connector, database, watcher, or long-lived state.

## Final Document-Level QA

Before calling a document done, check:

- every important claim has an evidence anchor or an explicit uncertainty;
- the document answers the reader's scientific question before internal process details;
- source facts, numbers, formulas, citations, labels, and limitations are preserved;
- tables, figures, and formulas have visible scientific roles;
- reader-facing references are separated from author-only provenance;
- incremental updates did not drift outside the dependency closure;
- downstream language, citation, rendering, or artifact skills did not change scientific meaning;
- final deliverables are actual user-openable artifacts when the user requested a finished file, with canonical path/hash as provenance rather than a substitute for delivery.

If the QA fails because another owner is needed, stop at the correct handoff instead of silently lowering quality or rerouting around Research Authoring.
