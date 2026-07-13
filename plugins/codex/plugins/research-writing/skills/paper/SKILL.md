---
name: research-paper-workflow
description: Formal manuscript, supplement, rebuttal, grant, claim-evidence, citation, and LaTeX authoring workflow coordination.
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
default_prompt:
---

# research-paper-workflow

## Trigger Boundary

Formal manuscript, supplement, rebuttal, grant, claim-evidence, citation, and LaTeX authoring workflow coordination.

Use this aggregate Codex App skill when the task matches one of the source workflows below.

## Source Workflows

- `scientific-writing`: Core skill for the deep research and writing tool. Write scientific manuscripts in full paragraphs (never bullet points). Reference: `_src/write/source.md`
- `paper-workflow-orchestrator`: Orchestrate end-to-end research paper work: project bootstrap, claim/evidence spine, section sequencing, figure/text synchronization, submission checks, and rebuttal planning. Use when the user asks how to structure a manuscript workflow rather than only polish a paragraph. Reference: `_src/flow/source.md`
- `nature-manuscript-workflow`: Plan, draft, revise, and audit Nature-style manuscripts, including claim framing, figure logic, data availability, submission readiness, and reviewer response. Use when the user targets Nature-family journals or asks for Nature-style scientific writing. Reference: `_src/nature/source.md`
- `latex-paper-authoring`: Author, organize, repair, and prepare LaTeX research papers for arXiv, Overleaf, conference templates, or journal submission. Use when manuscript structure, LaTeX source hygiene, compilation, figures, bibliography, or template cleanup is central. Reference: `_src/latex/source.md`

## Workflow

1. Choose the source workflow whose trigger boundary best matches the user request.
2. Read that source workflow's `source.md` before acting.
3. Load only the needed files under that workflow's copied references, scripts, assets, or evals.
4. Follow the source workflow unless the current project gives stricter instructions.
