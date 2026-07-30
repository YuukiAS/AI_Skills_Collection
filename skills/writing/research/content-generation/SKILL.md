---
name: content-generation
description: Archived legacy academic content-generation pipeline note. Do not route new writing tasks here; use paper-workflow-orchestrator, scientific-writing, peer-review, writing-fidelity, and chinese-prose for current manuscript drafting and review.
status: archived
provenance: unknown
trusted: false
requires_network: false
writes_files: true
executes_code: false
secrets_needed:
last_reviewed: 2026-07-28
profile_tags:
recommended_scope: project
---
# Archived Content Generation Pipeline

This skill is retained only as a legacy note for older installations that used a standalone academic content-generation pipeline. It is not an active runtime entry and should not be selected for new writing work.

For current tasks, route by capability:

- Manuscript planning, claim-evidence mapping, result-to-claim checks, section contracts, submission readiness, and rebuttal handoff: use `paper-workflow-orchestrator`.
- Section drafting, scientific phrasing, methods/results/abstract writing, and source-faithful revision: use `scientific-writing` and `scientific-prose`.
- Pre-submission review, reviewer-risk analysis, response-to-reviewer assessment, and acceptance-risk triage: use `peer-review`.
- Final Markdown/PDF/DOCX/slides fidelity, version-label checks, and source-preserving edits: use `writing-fidelity`.
- Chinese-first reports, group-meeting notes, and human-readable delivery summaries: use `chinese-prose`.

Legacy anti-patterns intentionally removed from runtime behavior:

- fixed system personas or reviewer personalities;
- hard stops that require a specific unavailable notification tool;
- mandatory Mermaid diagrams, tables, generated figures, or fixed word counts;
- looped expansion until a score threshold is reached;
- source-repository names or old pipeline labels as user-facing trigger terms.
