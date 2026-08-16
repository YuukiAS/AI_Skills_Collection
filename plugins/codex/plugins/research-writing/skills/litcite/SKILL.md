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
  - skills/writing/research/literature-review
  - skills/writing/research/citation-verification
  - skills/science/discovery/citation-management
  - skills/science/discovery/research-lookup
  - skills/science/discovery/pyzotero
icon_small: "assets/codex/app-skill-icons/aggregate.svg"
icon_large: "assets/codex/app-skill-icons/aggregate.svg"
default_prompt:
---

# literature-and-citations

## Trigger Boundary

Current paper lookup, literature synthesis, single-paper evidence cards, citation support checks, BibTeX and reference metadata hygiene, and Zotero-oriented workflows.

Use this aggregate Codex App skill when the task matches one of the source workflows below.

## Source Workflows

- `literature-review`: Synthesize scholarly literature and create single-paper evidence cards. Use for systematic/scoping/narrative reviews, related work, paper精读, paper cards, claim-evidence extraction, method maps, thematic synthesis, and research-gap analysis. Route quick lookup, DOI/claim checks, BibTeX, and Zotero to citation skills. Reference: `_src/lit/source.md`
- `citation-verification`: Verify academic citations, references, BibTeX entries, DOI/PMID metadata, citation claims, and figure/table evidence before manuscript submission, review response, or report delivery. Use when citation existence or claim support matters more than citation formatting alone. Reference: `_src/verify/source.md`
- `citation-management`: Manage bibliography, BibTeX, citation metadata, and reference-library hygiene. Use for DOI/PMID/arXiv-to-BibTeX conversion, metadata extraction, duplicate repair, and style formatting. Route claim support to citation-verification, literature synthesis to literature-review, paper lookup to research-lookup, and Zotero operations to pyzotero. Reference: `_src/cite/source.md`
- `research-lookup`: Find current research information and recent papers quickly. Use for latest papers, targeted evidence gathering, methods/protocol checks, and source-backed facts. Route systematic or related-work synthesis to literature-review, claim-support verdicts to citation-verification, and BibTeX or library cleanup to citation-management or pyzotero. Reference: `_src/lookup/source.md`
- `pyzotero`: Interact with Zotero reference management libraries using the pyzotero Python client. Retrieve, create, update, and delete items, collections, tags, and attachments via the Zotero Web API v3. Reference: `_src/zotero/source.md`

## Workflow

1. Choose the source workflow whose trigger boundary best matches the user request.
2. Read that source workflow's `source.md` before acting.
3. Load only the needed files under that workflow's copied references, scripts, assets, or evals.
4. Follow the source workflow unless the current project gives stricter instructions.
