---
name: valyu-scientific-search
description: Search scientific literature and biomedical databases through Valyu-backed semantic search when available, including PubMed, arXiv, bioRxiv, medRxiv, patents, ChEMBL, DrugBank, Open Targets, FDA labels, and clinical trials.
status: active
provenance: external-adapted
source_repo_url: https://github.com/yorkeccak/scientific-skills
source_path: .
source_ref: 20b3d503700656f847e6de873753335bf90e63e3
source_imported_at: 2026-07-09
source_license: MIT
source_note: Distilled from scientific-skills search skills; kept optional because it depends on external semantic-search infrastructure.
trusted: false
requires_network: true
writes_files: false
executes_code: false
secrets_needed:
  - VALYU_API_KEY
last_reviewed: 2026-07-09
profile_tags:
  - research-discovery
recommended_scope: project
metadata:
  skill-author: AI Skills Collection maintainers with recorded upstream sources
---
# Valyu Scientific Search

Use this only when a Valyu-backed semantic search service is configured. If it is not configured, route to existing database skills such as `pubmed-database`, `arxiv-database`, `biorxiv-database`, `openalex-database`, or `research-lookup`.

## Routing

- Literature across PubMed/arXiv/bioRxiv/medRxiv: use a broad literature query.
- Biomedical and drug discovery questions: search biomedical, DrugBank, ChEMBL, Open Targets, clinical trials, and FDA labels as separate evidence channels.
- Patent or prior-art questions: search patents separately from papers.
- Clinical questions: use this only for literature retrieval, not medical advice.

## Workflow

1. State the search scope and databases.
2. Use natural-language semantic queries, then refine with entities, methods, populations, and outcomes.
3. Deduplicate results by DOI, PMID, title, or trial identifier.
4. Separate preprints, peer-reviewed papers, labels, patents, and trials in the output.
5. Report source database, date searched, key metadata, and confidence limitations.

## Boundaries

- Do not treat semantic-search results as authoritative without source inspection.
- Do not merge regulatory labels, patents, trials, and papers into one evidence level.
- If `VALYU_API_KEY` is missing, explain the fallback path and use available local skills.
