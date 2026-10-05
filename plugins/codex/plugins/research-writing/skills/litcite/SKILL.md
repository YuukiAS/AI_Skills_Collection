---
name: literature-and-citations
description: Current paper lookup, literature synthesis, single-paper evidence cards, citation support checks, BibTeX and reference metadata hygiene, and Zotero-oriented workflows.
status: active
provenance: generated
trusted: false
requires_network: true
writes_files: true
executes_code: true
secrets_needed:
  - OPENROUTER_API_KEY
  - PARALLEL_API_KEY
  - ZOTERO_API_KEY
last_reviewed: 2026-07-10
profile_tags:
recommended_scope: project
source_skills:
  - skills/writing/research/research-authoring-core
  - skills/writing/research/literature-review
  - skills/writing/research/citation-verification
  - skills/science/discovery/citation-management
  - skills/science/discovery/research-lookup
  - skills/science/discovery/pyzotero
icon_small: "assets/codex/app-skill-icons/aggregate.svg"
icon_large: "assets/codex/app-skill-icons/aggregate.svg"
routing_mode: "coordinator-first"
coordinator_artifact_id: "core"
default_prompt:
---

# literature-and-citations

## Trigger Boundary

Current paper lookup, literature synthesis, single-paper evidence cards, citation support checks, BibTeX and reference metadata hygiene, and Zotero-oriented workflows.

Use this aggregate Codex App skill by entering the coordinator source first.

## Source Workflows

- `research-authoring-core` (coordinator): Canonical document-level coordinator for Research Authoring. Use before producing or substantially revising research reports, manuscripts, related-work documents, research updates, reviewer responses, or supplements; route support-only lookup, citation/BibTeX/Zotero, local prose polishing, render-only, PPT/Beamer, and ordinary Q&A to their owners. Reference: `_src/core/source.md`
- `literature-review` (delegate): Synthesize scholarly literature and create single-paper evidence cards. Use for systematic/scoping/narrative reviews, related work, paper精读, paper cards, claim-evidence extraction, method maps, thematic synthesis, and research-gap analysis. Route quick lookup, DOI/claim checks, BibTeX, and Zotero to citation skills. Reference: `_src/lit/source.md`
- `citation-verification` (delegate): Verify academic citations, references, BibTeX entries, DOI/PMID metadata, citation claims, and figure/table evidence before manuscript submission, review response, or report delivery. Use when citation existence or claim support matters more than citation formatting alone. Reference: `_src/verify/source.md`
- `citation-management` (delegate): Manage bibliography, BibTeX, citation metadata, and reference-library hygiene. Use for DOI/PMID/arXiv-to-BibTeX conversion, metadata extraction, duplicate repair, and style formatting. Route claim support to citation-verification, literature synthesis to literature-review, paper lookup to research-lookup, and Zotero operations to pyzotero. Reference: `_src/cite/source.md`
- `research-lookup` (delegate): Find current research information and recent papers quickly. Use for latest papers, targeted evidence gathering, methods/protocol checks, and source-backed facts. Route systematic or related-work synthesis to literature-review, claim-support verdicts to citation-verification, and BibTeX or library cleanup to citation-management or pyzotero. Reference: `_src/lookup/source.md`
- `pyzotero` (delegate): Interact with Zotero reference management libraries using the pyzotero Python client. Retrieve, create, update, and delete items, collections, tags, and attachments via the Zotero Web API v3. Reference: `_src/zotero/source.md`

## Plugin Workflow Notes

- For document-producing literature reviews, related-work sections, evidence syntheses, paper-card synthesis artifacts, or scholarly field summaries, read `_src/core/source.md` first and then delegate literature/citation work.
- For support-only lookup, citation verification, BibTeX, metadata, or Zotero/library hygiene, the core should explicitly route to the appropriate delegate without forcing a full document plan.

## Workflow

1. Read the coordinator source `_src/core/source.md` first.
2. Let the coordinator classify the task, authority, surface, risk, and required delegates.
3. Load delegate sources only after the coordinator selects them.
4. Return delegate findings to the coordinator for convergence, admission, and final handoff.
5. Follow stricter current-project instructions when they apply.
