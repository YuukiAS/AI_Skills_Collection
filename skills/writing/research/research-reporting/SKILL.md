---
name: research-reporting
description: Create repo-grounded research reports, milestone summaries, experiment reviews, technical notes, and result retrospectives from project evidence. Use for Markdown reports and internal scientific documentation, not for full journal manuscript workflows.
status: active
provenance: user-authored
trusted: false
requires_network: false
writes_files: true
executes_code: false
secrets_needed:
last_reviewed: 2026-07-13
profile_tags:
  - research-writing
recommended_scope: project
icon_small: assets/app-facing.svg
icon_large: assets/app-facing.svg
---
# Research Reporting

Use this skill when the output is a project-grounded report rather than a formal manuscript.

## Boundary

- Use for repo reports, milestone summaries, experiment retrospectives, technical notes, and evidence-backed Markdown documents.
- Do not use for paragraph-level polishing; route that to `writing-style`.
- Do not use for full manuscript planning, rebuttals, supplements, or grants; route those to `research-paper-workflow`.
- Do not implement low-level PDF, DOCX, PPTX, or LaTeX file mechanics here.

## Workflow

1. Identify the source of truth: code, results, logs, figures, tables, notes, prior reports, and open questions.
2. Separate observed results, planned work, assumptions, and speculation.
3. Build a claim-evidence map with explicit file or section anchors.
4. Write the report with enough structure for later review: goal, method, evidence, interpretation, limitations, and next decisions.
5. Ask `writing-style` for final language cleanup only after the evidence structure is stable.

## Acceptance

- Every important claim points to an evidence anchor.
- Missing or weak evidence is named directly.
- The report does not invent results, citations, benchmarks, or reviewer feedback.
