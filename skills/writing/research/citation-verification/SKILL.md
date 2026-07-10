---
name: citation-verification
description: Verify academic citations, references, BibTeX entries, DOI/PMID metadata, citation claims, and figure/table evidence before manuscript submission, review response, or report delivery. Use when citation existence or claim support matters more than citation formatting alone.
status: active
provenance: adapted
trusted: false
requires_network: true
writes_files: true
executes_code: false
secrets_needed:
last_reviewed: 2026-07-09
profile_tags:
  - research-writing
  - citations
recommended_scope: project
source_url: https://github.com/serenakeyitan/citation-check-skill
source_commit: b9deb7077099f56b05c9b6ecea744c2ca0a6d324
source_license: MIT
adaptation_notes: Distilled from citation-check-skill, Nature-Paper-Skills citation-verifier/reference-audit, claude-scholar citation-verification, and paperpipe verification workflows.
metadata:
  skill-author: AI Skills Collection maintainers with recorded upstream sources
---
# Citation Verification

Use this as a verification gate. Formatting a bibliography is not enough; check whether the cited source exists and supports the claim being made.

## Workflow

1. Inventory all citation-bearing artifacts: manuscript, slides, figures, tables, BibTeX, references, captions, and supplementary files.
2. Classify citation checks:
   - existence: DOI, PMID, arXiv ID, URL, title, authors, year;
   - metadata consistency: BibTeX fields match authoritative metadata;
   - claim support: the cited source actually supports the sentence or panel;
   - placeholder risk: missing references, `TODO`, fake-looking DOIs, malformed keys;
   - citation drift: cited paper supports a narrower or different claim.
3. Prefer authoritative sources when available: publisher page, Crossref, PubMed, OpenAlex, arXiv, official repository, or the source PDF.
4. Record uncertainty. If online verification is unavailable, mark the citation `unverified`, not `valid`.
5. Output a table with `citation`, `location`, `check_type`, `status`, `evidence`, and `fix`.

## Boundaries

- Do not fabricate missing metadata.
- Do not silently replace citations with unrelated papers.
- Do not claim a citation supports a method/result unless the relevant passage was checked.
- If an API key or network access is unavailable, run structural checks and report the limitation.

## Hand Off

- Use `citation-management` for search, BibTeX generation, and reference-library operations.
- Use `paper-workflow-orchestrator` when citation issues imply a larger manuscript-claim problem.
- Use `literature-review` when a missing citation requires field-level source discovery.
