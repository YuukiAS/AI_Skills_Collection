---
name: literature-and-citations
description: Literature search, review synthesis, citation verification, BibTeX hygiene, and Zotero-oriented citation workflows.
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
default_prompt:
---

# literature-and-citations

## Trigger Boundary

Literature search, review synthesis, citation verification, BibTeX hygiene, and Zotero-oriented citation workflows.

Use this aggregate Codex App skill when the task matches one of the source workflows below.

## Source Workflows

- `literature-review`: Conduct comprehensive, systematic literature reviews using multiple academic databases (PubMed, arXiv, bioRxiv, Semantic Scholar, etc.). Reference: `_src/lit/source.md`
- `citation-verification`: Verify academic citations, references, BibTeX entries, DOI/PMID metadata, citation claims, and figure/table evidence before manuscript submission, review response, or report delivery. Use when citation existence or claim support matters more than citation formatting alone. Reference: `_src/verify/source.md`
- `citation-management`: Comprehensive citation management for academic research. Search Google Scholar and PubMed for papers, extract accurate metadata, validate citations, and generate properly formatted BibTeX entries. Reference: `_src/cite/source.md`
- `research-lookup`: Look up current research information using the Parallel Chat API (primary) or Perplexity sonar-pro-search (academic paper searches). Automatically routes queries to the best backend. Use for finding papers, gathering research data, and verifying scientific information. Reference: `_src/lookup/source.md`
- `pyzotero`: Interact with Zotero reference management libraries using the pyzotero Python client. Retrieve, create, update, and delete items, collections, tags, and attachments via the Zotero Web API v3. Reference: `_src/zotero/source.md`

## Workflow

1. Choose the source workflow whose trigger boundary best matches the user request.
2. Read that source workflow's `source.md` before acting.
3. Load only the needed files under that workflow's copied references, scripts, assets, or evals.
4. Follow the source workflow unless the current project gives stricter instructions.
