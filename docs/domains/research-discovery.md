# research-discovery

Active skills: 9

## Install

Complete domain install:

```bash
ai-skills install --target repo --domain research-discovery --mode symlink --write-agents-md
```

Install a few skills precisely:

```bash
ai-skills install --target repo --skill science/discovery/arxiv-database --skill science/discovery/bgpt-paper-search --skill science/discovery/biorxiv-database --mode symlink --write-agents-md
```

Complete domain installs are supported. If an audit reports high description length or many active skills, treat it as a context-budget warning, not an installation error.

## Common Uses

- Install the whole domain for a project where most tasks are in this area.
- Use precise skill selectors when only one tool or workflow is needed.
- Combine with profiles when a project needs a curated cross-domain set.

## Skills

- `arxiv-database` (`skills/science/discovery/arxiv-database`): Search and retrieve preprints from arXiv via the Atom API. Use this skill when searching for papers in physics, mathematics, computer science, quantitative biology, quantitative finance, statistics, electrical engineering, or economics by keywords, authors, arXiv IDs, date ranges, or categories.
- `bgpt-paper-search` (`skills/science/discovery/bgpt-paper-search`): Search scientific papers and retrieve structured experimental data extracted from full-text studies via the BGPT MCP server. Returns 25+ fields per paper including methods, results, sample sizes, quality scores, and conclusions.
- `biorxiv-database` (`skills/science/discovery/biorxiv-database`): Efficient database search tool for bioRxiv preprint server. Use this skill when searching for life sciences preprints by keywords, authors, date ranges, or categories, retrieving paper metadata, downloading PDFs, or conducting literature reviews.
- `citation-management` (`skills/science/discovery/citation-management`): Manage bibliography, BibTeX, citation metadata, and reference-library hygiene. Use for DOI/PMID/arXiv-to-BibTeX conversion, metadata extraction, duplicate repair, and style formatting. Route claim support to citation-verification, literature synthesis to literature-review, paper lookup to research-lookup, and Zotero operations to pyzotero.
- `openalex-database` (`skills/science/discovery/openalex-database`): Query and analyze scholarly literature using the OpenAlex database. Use for literature searches, research output analysis, citation analysis, and academic database queries.
- `pubmed-database` (`skills/science/discovery/pubmed-database`): Direct REST API access to PubMed. Advanced Boolean/MeSH queries, E-utilities API, batch processing, citation management. For Python workflows, prefer biopython (Bio.Entrez). Use this for direct HTTP/REST work or custom API implementations.
- `pyzotero` (`skills/science/discovery/pyzotero`): Interact with Zotero reference management libraries using the pyzotero Python client. Retrieve, create, update, and delete items, collections, tags, and attachments via the Zotero Web API v3.
- `research-lookup` (`skills/science/discovery/research-lookup`): Find current research information and recent papers quickly. Use for latest papers, targeted evidence gathering, methods/protocol checks, and source-backed facts. Route systematic or related-work synthesis to literature-review, claim-support verdicts to citation-verification, and BibTeX or library cleanup to citation-management or pyzotero.
- `valyu-scientific-search` (`skills/science/discovery/valyu-scientific-search`): Search scientific literature and biomedical databases through Valyu-backed semantic search when available, including PubMed, arXiv, bioRxiv, medRxiv, patents, ChEMBL, DrugBank, Open Targets, FDA labels, and clinical trials.

## Main References

- No domain references discovered yet. Add `references/source-notes.md`, checklists, or overview notes when the skill carries long-lived domain knowledge.
