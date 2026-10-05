---
name: research-reporting
description: Report-family Research Authoring route for advisor reports, group-meeting written reports, milestones, research updates, methods notes, experiment retrospectives, and evidence-backed technical notes; enter the document-level core first, then delegate report semantics to research-reporting.
status: active
provenance: generated
trusted: false
requires_network: false
writes_files: true
executes_code: false
secrets_needed:
last_reviewed: 2026-07-10
profile_tags:
recommended_scope: project
source_skills:
  - skills/writing/research/research-authoring-core
  - skills/writing/research/research-reporting
icon_small: "assets/codex/app-skill-icons/aggregate.svg"
icon_large: "assets/codex/app-skill-icons/aggregate.svg"
routing_mode: "coordinator-first"
coordinator_artifact_id: "core"
default_prompt:
---

# research-reporting

## Trigger Boundary

Report-family Research Authoring route for advisor reports, group-meeting written reports, milestones, research updates, methods notes, experiment retrospectives, and evidence-backed technical notes; enter the document-level core first, then delegate report semantics to research-reporting.

Use this aggregate Codex App skill by entering the coordinator source first.

## Source Workflows

- `research-authoring-core` (coordinator): Canonical document-level coordinator for Research Authoring. Use before producing or substantially revising research reports, manuscripts, related-work documents, research updates, reviewer responses, or supplements; route support-only lookup, citation/BibTeX/Zotero, local prose polishing, render-only, PPT/Beamer, and ordinary Q&A to their owners. Reference: `_src/core/source.md`
- `research-reporting` (delegate): Create repo-grounded research reports, milestone summaries, experiment reviews, technical notes, advisor/group-meeting reports, and result retrospectives from project evidence. Use for report semantics even when the final deliverable is a formal PDF; rendering mechanics belong to companion document skills. Reference: `_src/report/source.md`

## Plugin Workflow Notes

- For document-producing report-family requests, read `_src/core/source.md` first to freeze audience, purpose, source authority, claim-evidence spine, section jobs, table/figure/formula roles, citation authority, incremental-edit scope, downstream route, and final document-level QA.
- For explicit formal PDF delivery, keep report semantics in Research Authoring and delegate only rendering mechanics to `render-chinese-math-pdf` when that companion is installed through the active profile; standalone Marketplace Research Authoring must fail closed when the renderer companion is missing.

## Workflow

1. Read the coordinator source `_src/core/source.md` first.
2. Let the coordinator classify the task, authority, surface, risk, and required delegates.
3. Load delegate sources only after the coordinator selects them.
4. Return delegate findings to the coordinator for convergence, admission, and final handoff.
5. Follow stricter current-project instructions when they apply.
