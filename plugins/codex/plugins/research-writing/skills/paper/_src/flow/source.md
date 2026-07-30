---
name: paper-workflow-orchestrator
description: Orchestrate research paper workflows: manuscript plan, claim-evidence spine, result-to-claim gate, section contracts, figure/text sync, pre-submission acceptance checks, rebuttal planning, final artifact QA, and paper-structure rescue rather than paragraph polishing.
status: active
provenance: external-adapted
source_repo_url: https://github.com/WUBING2023/PaperSpine
source_path: .
source_ref: d4529208cda72aa075767611b0265b95b709b550
source_imported_at: 2026-07-09
source_license: MIT
source_note: Distilled from recorded paper-workflow sources; see docs/provenance/INTEGRATION_HISTORY.md.
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

## Research Paper Production Workbench

Use this skill when the user needs the paper process itself organized, not just
a paragraph rewritten. Route by task shape:

1. Intake and scoping: identify the research question, target audience, current
   artifact state, available evidence, missing evidence, and deadline pressure.
2. Argument spine: turn scattered notes, experiments, or conclusions into a
   problem -> gap -> method -> evidence -> claim -> limitation structure.
3. Section contracts: define what each manuscript section must prove, which
   figures/tables carry the proof, and which claims must be removed or narrowed.
4. Draft production: sequence the writing so methods, results, figures, and
   claims stay synchronized; do not generate a polished paper that outruns the
   evidence ledger.
5. Revision loop: audit reviewer attack surfaces, unsupported superiority or
   robustness claims, missing comparisons, stale numbers, and inconsistent
   terminology before prose polishing.
6. Submission/rebuttal handoff: create venue checklist, reviewer concern matrix,
   required experiments or text fixes, and final artifact QA tasks for the
   downstream writing, citation, LaTeX, PDF, or review skills.
7. Result-to-claim gate: after experiments or audits finish, decide which claims are supported, which must be narrowed, which are draft-only, and which require new evidence before writing.
8. Final artifact gate: before treating a manuscript, Markdown, PDF, response, or report as final, identify the selected artifact, evidence authority, unresolved checks, and the downstream style/fidelity skill that must run.

Use `literature-review` for single-paper cards or field synthesis. Use
`peer-review` for reviewer scoring, acceptance risk, and rebuttal assessment.
Use `writing-fidelity` before final Markdown/PDF delivery when version labels,
headings, numbers, or evidence boundaries have been corrected before.

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
5. Run a result-to-claim check before drafting or accepting results prose: each number, table row, leaderboard entry, audit result, and qualitative example must be classified as supported, bounded, draft-only, historical, or not verifiable.
6. Before final reporting, state what changed, what evidence supports it, what remains unresolved, and which downstream skill should run next.

## Routing

- Use `scientific-writing` for full paragraph scientific prose.
- Use `literature-review` for field synthesis and related-work structure.
- Use `citation-verification` before submission or when claims rely on citations.
- Use `nature-manuscript-workflow` for broad-journal/high-impact framing, figure-to-claim logic, data availability, and Nature-family checks when relevant.
- Use `latex-paper-authoring` when LaTeX structure, Overleaf readiness, or compilation is the main issue.
- Use `scientific-visualization` for manuscript figure palettes, plotting snippets,
  figure export QA, top-conference figure presets, and publication-ready visual
  checks. Use `drawio-diagrams` or `d2-diagrams` when editable diagrams are the
  main deliverable.

## Quality Gates

- Every major section must have a purpose in the argument.
- Every figure panel must map to a specific claim or method step.
- Every central claim must identify the artifact that supports it.
- Missing evidence must be named explicitly, not hidden by prose.
- Do not invent results, citations, reviewer requests, or venue policies.
- Do not let an audit report, old draft, month label, or candidate row substitute for the author-approved best result or the requested final artifact.
