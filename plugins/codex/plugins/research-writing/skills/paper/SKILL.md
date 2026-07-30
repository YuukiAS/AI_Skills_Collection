---
name: research-paper-workflow
description: Formal manuscript, supplement, rebuttal, pre-submission review, claim-evidence workflow, result-to-claim gates, grant, citation, and LaTeX authoring coordination.
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
  - skills/writing/research/scientific-writing
  - skills/writing/research/paper-workflow-orchestrator
  - skills/writing/research/nature-manuscript-workflow
  - skills/writing/research/latex-paper-authoring
  - skills/writing/research/venue-templates
  - skills/writing/research/peer-review
icon_small: "assets/codex/app-skill-icons/aggregate.svg"
icon_large: "assets/codex/app-skill-icons/aggregate.svg"
default_prompt:
---

# research-paper-workflow

## Trigger Boundary

Formal manuscript, supplement, rebuttal, pre-submission review, claim-evidence workflow, result-to-claim gates, grant, citation, and LaTeX authoring coordination.

Use this aggregate Codex App skill when the task matches one of the source workflows below.

## Source Workflows

- `scientific-writing`: Draft, revise, and acceptance-check scientific manuscripts and sections. Use for 写论文/改论文, abstracts, introductions, methods, results, discussion, reviewer-response edits, claim-supported prose, reporting-guideline coverage, and final manuscript text in full paragraphs rather than bullet points. Reference: `_src/write/source.md`
- `paper-workflow-orchestrator`: Orchestrate research paper workflows: manuscript plan, claim-evidence spine, result-to-claim gate, section contracts, figure/text sync, pre-submission acceptance checks, rebuttal planning, final artifact QA, and paper-structure rescue rather than paragraph polishing. Reference: `_src/flow/source.md`
- `nature-manuscript-workflow`: Plan, draft, revise, and audit broad-journal or high-impact manuscripts, including claim framing, figure logic, data availability, submission readiness, and reviewer response. Use for story-driven journal strategy, broad-audience manuscript framing, figure-to-claim alignment, and Nature-family targets when explicit. Reference: `_src/nature/source.md`
- `latex-paper-authoring`: Author, organize, repair, and prepare LaTeX research papers for arXiv, Overleaf, conference templates, or journal submission. Use when manuscript structure, LaTeX source hygiene, compilation, figures, bibliography, or template cleanup is central. Reference: `_src/latex/source.md`
- `venue-templates`: This skill should be used when preparing manuscripts for journal submission, conference papers, research posters, or grant proposals and need venue-specific formatting requirements and templates. Reference: `_src/venue/source.md`
- `peer-review`: Structured manuscript/grant review and writing acceptance check. Use for pre-submission self-review, paper验收, reviewer-style critique, likely objections, acceptance-risk diagnosis, rebuttal assessment, claim-evidence audit, methodology/statistical validity, reporting standards, ICLR/top-conference review, and constructive feedback. Reference: `_src/review/source.md`

## Workflow

1. Choose the source workflow whose trigger boundary best matches the user request.
2. Read that source workflow's `source.md` before acting.
3. Load only the needed files under that workflow's copied references, scripts, assets, or evals.
4. Follow the source workflow unless the current project gives stricter instructions.
