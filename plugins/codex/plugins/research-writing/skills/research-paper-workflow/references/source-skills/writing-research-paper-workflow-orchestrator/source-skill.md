---
name: paper-workflow-orchestrator
description: Orchestrate end-to-end research paper work: project bootstrap, claim/evidence spine, section sequencing, figure/text synchronization, submission checks, and rebuttal planning. Use when the user asks how to structure a manuscript workflow rather than only polish a paragraph.
status: active
provenance: external-adapted
source_repo_url: https://github.com/WUBING2023/PaperSpine
source_path: .
source_ref: d4529208cda72aa075767611b0265b95b709b550
source_imported_at: 2026-07-09
source_license: MIT
source_note: Distilled from PaperSpine, academic-research-skills, Nature-Paper-Skills, paper-writing-skill, and Research-Paper-Writing-Skills; see TODO/CLONED_SKILL_SOURCES.md.
trusted: false
requires_network: false
writes_files: true
executes_code: false
secrets_needed:
last_reviewed: 2026-07-09
profile_tags:
  - research-writing
recommended_scope: project
metadata:
  skill-author: AI Skills Collection maintainers with recorded upstream sources
---
# Paper Workflow Orchestrator

Use this skill to plan and coordinate manuscript work. Do not use it as a prose-polishing skill; hand off paragraph-level editing to `scientific-writing`, `scientific-prose`, or `writing-fidelity`.

## Workflow

1. Establish the paper type, venue, audience, artifact state, target outputs, and hard constraints.
2. Create a claim/evidence spine:
   - central contribution;
   - supporting claims;
   - evidence artifacts for each claim;
   - figure/table panels that carry each claim;
   - missing or weak evidence.
3. Choose the next active phase:
   - bootstrap directory and source files;
   - outline and section plan;
   - draft section;
   - revise claim/evidence alignment;
   - audit citations and figures;
   - prepare submission package;
   - respond to reviewers.
4. Keep one source of truth for manuscript state. If the repo already has a paper plan, update or reference it instead of creating a parallel plan.
5. Before final reporting, state what changed, what evidence supports it, what remains unresolved, and which downstream skill should run next.

## Routing

- Use `scientific-writing` for full paragraph scientific prose.
- Use `literature-review` for field synthesis and related-work structure.
- Use `citation-verification` before submission or when claims rely on citations.
- Use `nature-manuscript-workflow` for Nature-family venue fit, data availability, and submission-specific checks.
- Use `latex-paper-authoring` when LaTeX structure, Overleaf readiness, or compilation is the main issue.
- Use `scientific-visualization`, `drawio-diagrams`, or `d2-diagrams` when figures are the main deliverable.

## Quality Gates

- Every major section must have a purpose in the argument.
- Every figure panel must map to a specific claim or method step.
- Every central claim must identify the artifact that supports it.
- Missing evidence must be named explicitly, not hidden by prose.
- Do not invent results, citations, reviewer requests, or venue policies.
