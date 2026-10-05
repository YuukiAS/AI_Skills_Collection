---
name: research-paper-workflow
description: Formal manuscript planning, drafting, revision, reviewer-style critique, rubric scoring, rebuttal, supplement, venue, and LaTeX coordination; route literature discovery and citation checks to literature-and-citations.
status: active
provenance: generated
trusted: false
requires_network: true
writes_files: true
executes_code: true
secrets_needed:
last_reviewed: 2026-07-10
profile_tags:
recommended_scope: project
source_skills:
  - skills/writing/research/research-authoring-core
  - skills/writing/research/scientific-writing
  - skills/writing/research/paper-workflow-orchestrator
  - skills/writing/research/nature-manuscript-workflow
  - skills/writing/research/latex-paper-authoring
  - skills/writing/research/venue-templates
  - skills/writing/research/peer-review
  - skills/writing/research/scholar-evaluation
icon_small: "assets/codex/app-skill-icons/aggregate.svg"
icon_large: "assets/codex/app-skill-icons/aggregate.svg"
routing_mode: "coordinator-first"
coordinator_artifact_id: "core"
default_prompt:
---

# research-paper-workflow

## Trigger Boundary

Formal manuscript planning, drafting, revision, reviewer-style critique, rubric scoring, rebuttal, supplement, venue, and LaTeX coordination; route literature discovery and citation checks to literature-and-citations.

Use this aggregate Codex App skill by entering the coordinator source first.

## Source Workflows

- `research-authoring-core` (coordinator): Canonical document-level coordinator for Research Authoring. Use before producing or substantially revising research reports, manuscripts, related-work documents, research updates, reviewer responses, or supplements; route support-only lookup, citation/BibTeX/Zotero, local prose polishing, render-only, PPT/Beamer, and ordinary Q&A to their owners. Reference: `_src/core/source.md`
- `scientific-writing` (delegate): Draft and revise scientific manuscript prose: abstracts, IMRaD sections, reviewer-response wording, claim-supported paragraphs, and reporting-guideline text. Route whole-paper planning, reviewer-risk critique, literature discovery, citation verification, BibTeX, figures, venue formatting, and LaTeX issues to neighboring skills. Reference: `_src/write/source.md`
- `paper-workflow-orchestrator` (delegate): Orchestrate research paper workflows: manuscript plan, claim-evidence spine, result-to-claim gate, section contracts, figure/text sync, pre-submission acceptance checks, rebuttal planning, final artifact QA, and paper-structure rescue rather than paragraph polishing. Reference: `_src/flow/source.md`
- `nature-manuscript-workflow` (delegate): Plan, draft, revise, and audit broad-journal or high-impact manuscripts, including claim framing, figure logic, data availability, submission readiness, and reviewer response. Use for story-driven journal strategy, broad-audience manuscript framing, figure-to-claim alignment, and Nature-family targets when explicit. Reference: `_src/nature/source.md`
- `latex-paper-authoring` (delegate): Author, organize, repair, and prepare LaTeX research papers for arXiv, Overleaf, conference templates, or journal submission. Use when manuscript structure, LaTeX source hygiene, compilation, figures, bibliography, or template cleanup is central. Reference: `_src/latex/source.md`
- `venue-templates` (delegate): This skill should be used when preparing manuscripts for journal submission, conference papers, research posters, or grant proposals and need venue-specific formatting requirements and templates. Reference: `_src/venue/source.md`
- `peer-review` (delegate): Reviewer-style manuscript or grant critique and acceptance-risk assessment. Use for pre-submission self-review, paper验收, likely objections, rebuttal assessment, claim-evidence audit, methods/statistics critique, reporting standards, and concern ledgers. Route prose drafting to scientific-writing and scoring to scholar-evaluation. Reference: `_src/review/source.md`
- `scholar-evaluation` (delegate): Quantitatively evaluate scholarly work with a fixed rubric or ScholarEval-style dimensions. Use for rubric assessment, benchmarked quality scoring, numbered ratings, and dimension-by-dimension evaluation. Route ordinary reviewer-style critique to peer-review and prose revision to scientific-writing. Reference: `_src/score/source.md`

## Plugin Workflow Notes

- For document-producing manuscript, supplement, reviewer-response, cover-letter, thesis-chapter, or submission-package work, read `_src/core/source.md` first, then delegate paper-family planning, prose, review, venue, LaTeX, and citation work to the relevant source workflow.
- Do not use paper-family delegates as bypasses around the document-level Research Authoring core.

## Workflow

1. Read the coordinator source `_src/core/source.md` first.
2. Let the coordinator classify the task, authority, surface, risk, and required delegates.
3. Load delegate sources only after the coordinator selects them.
4. Return delegate findings to the coordinator for convergence, admission, and final handoff.
5. Follow stricter current-project instructions when they apply.
