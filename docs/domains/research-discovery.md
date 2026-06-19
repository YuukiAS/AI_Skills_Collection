# research-discovery

Active skills: 8

## Install

Complete domain install:

```bash
python3 scripts/skills.py install --target repo --domain research-discovery --mode symlink --write-agents-md
```

Install a few skills precisely:

```bash
python3 scripts/skills.py install --target repo --skill science/discovery/arxiv-database --skill science/discovery/bgpt-paper-search --skill science/discovery/biorxiv-database --mode symlink --write-agents-md
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
- `citation-management` (`skills/science/discovery/citation-management`): Comprehensive citation management for academic research. Search Google Scholar and PubMed for papers, extract accurate metadata, validate citations, and generate properly formatted BibTeX entries.
- `openalex-database` (`skills/science/discovery/openalex-database`): Query and analyze scholarly literature using the OpenAlex database. Use for literature searches, research output analysis, citation analysis, and academic database queries.
- `pubmed-database` (`skills/science/discovery/pubmed-database`): Direct REST API access to PubMed. Advanced Boolean/MeSH queries, E-utilities API, batch processing, citation management. For Python workflows, prefer biopython (Bio.Entrez). Use this for direct HTTP/REST work or custom API implementations.
- `pyzotero` (`skills/science/discovery/pyzotero`): Interact with Zotero reference management libraries using the pyzotero Python client. Retrieve, create, update, and delete items, collections, tags, and attachments via the Zotero Web API v3.
- `research-lookup` (`skills/science/discovery/research-lookup`): Look up current research information using the Parallel Chat API (primary) or Perplexity sonar-pro-search (academic paper searches). Automatically routes queries to the best backend. Use for finding papers, gathering research data, and verifying scientific information.

## Main References

- No domain references discovered yet. Add `references/source-notes.md`, checklists, or overview notes when the skill carries long-lived domain knowledge.
