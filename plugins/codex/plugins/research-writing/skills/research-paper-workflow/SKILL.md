---
name: research-paper-workflow
description: Scientific writing, paper workflow orchestration, Nature-style manuscripts, citation verification, LaTeX authoring, and optional semantic literature search.
status: active
provenance: generated-codex-marketplace
trusted: false
requires_network: false
writes_files: true
executes_code: false
secrets_needed:
profile_tags:
recommended_scope: project
---

# research-paper-workflow

## Trigger Boundary

Scientific writing, paper workflow orchestration, Nature-style manuscripts, citation verification, LaTeX authoring, and optional semantic literature search.

Use this aggregate Codex App skill when the task matches one of the source workflows below.

## Source Workflows

- `scientific-writing`: Core skill for the deep research and writing tool. Write scientific manuscripts in full paragraphs (never bullet points). Reference: `references/source-skills/writing-research-scientific-writing/source-skill.md`
- `paper-workflow-orchestrator`: Orchestrate end-to-end research paper work: project bootstrap, claim/evidence spine, section sequencing, figure/text synchronization, submission checks, and rebuttal planning. Use when the user asks how to structure a manuscript workflow rather than only polish a paragraph. Reference: `references/source-skills/writing-research-paper-workflow-orchestrator/source-skill.md`
- `nature-manuscript-workflow`: Plan, draft, revise, and audit Nature-style manuscripts, including claim framing, figure logic, data availability, submission readiness, and reviewer response. Use when the user targets Nature-family journals or asks for Nature-style scientific writing. Reference: `references/source-skills/writing-research-nature-manuscript-workflow/source-skill.md`
- `citation-verification`: Verify academic citations, references, BibTeX entries, DOI/PMID metadata, citation claims, and figure/table evidence before manuscript submission, review response, or report delivery. Use when citation existence or claim support matters more than citation formatting alone. Reference: `references/source-skills/writing-research-citation-verification/source-skill.md`
- `latex-paper-authoring`: Author, organize, repair, and prepare LaTeX research papers for arXiv, Overleaf, conference templates, or journal submission. Use when manuscript structure, LaTeX source hygiene, compilation, figures, bibliography, or template cleanup is central. Reference: `references/source-skills/writing-research-latex-paper-authoring/source-skill.md`
- `valyu-scientific-search`: Search scientific literature and biomedical databases through Valyu-backed semantic search when available, including PubMed, arXiv, bioRxiv, medRxiv, patents, ChEMBL, DrugBank, Open Targets, FDA labels, and clinical trials. Reference: `references/source-skills/science-discovery-valyu-scientific-search/source-skill.md`

## Workflow

1. Choose the source workflow whose trigger boundary best matches the user request.
2. Read that source workflow's `source-skill.md` before acting.
3. Load only the needed files under that workflow's copied references, scripts, assets, or evals.
4. Follow the source workflow unless the current project gives stricter instructions.
