---
name: citation-management
description: Manage bibliography, BibTeX, citation metadata, and reference-library hygiene. Use for DOI/PMID/arXiv-to-BibTeX conversion, metadata extraction, duplicate repair, and style formatting. Route claim support to citation-verification, literature synthesis to literature-review, paper lookup to research-lookup, and Zotero operations to pyzotero.
status: active
provenance: unknown
trusted: false
requires_network: false
writes_files: true
executes_code: false
secrets_needed:
last_reviewed: 2026-05-14
profile_tags:
recommended_scope: project
icon_small: assets/app-facing.svg
icon_large: assets/app-facing.svg
license: MIT License
metadata:
  skill-author: K-Dense Inc.
allowed-tools: Read Write Edit Bash
---
# Citation Management

## Overview

Manage citations systematically throughout the research and writing process. This skill provides tools and strategies for bibliography construction, BibTeX generation, metadata extraction from multiple sources (CrossRef, PubMed, arXiv), duplicate cleanup, and citation-style formatting.

This is a technical reference-management skill, not the final authority on whether a cited source supports a manuscript claim. Use `citation-verification` for source-existence, DOI/PMID consistency, claim-support, and citation-drift verdicts.

## When to Use This Skill

Use this skill when:
- Locating known papers by exact title, author/year, DOI, PMID, arXiv ID, URL, or an existing candidate list so their records can be added to a bibliography
- Converting DOIs, PMIDs, or arXiv IDs to properly formatted BibTeX
- Extracting complete metadata for citations (authors, title, journal, year, etc.)
- Checking metadata consistency for existing bibliography entries
- Cleaning and formatting BibTeX files
- Finding known papers or identifier-backed records needed for a bibliography
- Building a bibliography for a manuscript or thesis
- Checking for duplicate citations
- Ensuring consistent citation formatting

Do not use this skill as the primary route when:
- A sentence, table, figure, or claim must be checked against the cited source; use `citation-verification`.
- The user needs a systematic, scoping, narrative, or related-work synthesis; use `literature-review`.
- The user asks to find papers by topic, find recent papers, discover new candidate sources, expand a bibliography, or scan current evidence; use `research-lookup`.
- The user needs Zotero collection reads, exports, or local library operations; use `pyzotero`.

## Visual and Figure Routing

Citation work should stay focused on source accuracy, metadata, and bibliography hygiene. Do not generate diagrams just because a citation document is being created. Add visuals only when the user asks for a search-method figure, bibliography workflow diagram, citation-style decision tree, or presentation-ready summary.

Use tables for citation audits, duplicate checks, metadata repair plans, and source verification status. Route optional diagrams to `markdown-mermaid-writing`, `drawio-diagrams`, or `d2-diagrams` when a workflow or decision tree is genuinely clearer as a visual.

---

## Core Workflow

Citation management follows a systematic process:

### Phase 1: Bibliography Record Resolution

**Goal**: Resolve known papers or known identifiers into reliable bibliographic records. This phase starts from user-supplied DOIs, PMIDs, arXiv IDs, URLs, exact titles, author/year pairs, or candidate records produced by `research-lookup` or `literature-review`.

Do not use this phase to discover papers by topic. For "find recent papers about X," "search the literature on X," "expand this candidate set," or "what should I cite for X," route to `research-lookup` first and return here only after candidate records or identifiers exist.

#### Known-Record Lookup

Use exact-title, exact-author, or identifier-backed lookups only when metadata is incomplete and the record is already known.

**Google Scholar record lookup examples**:
```bash
# Locate a known paper by exact title for metadata repair
python scripts/search_google_scholar.py '"Attention Is All You Need"' \
  --limit 5 \
  --output known_title_record.json

# Locate a known author/year/title fragment when no DOI was supplied
python scripts/search_google_scholar.py '"Vaswani" "Attention Is All You Need" 2017' \
  --limit 5 \
  --output author_year_record.json
```

**Known-record strategies**:
- Use quotation marks for exact phrases: `"deep learning"`
- Search by author: `author:LeCun`
- Search in title: `intitle:"neural networks"`
- Keep result limits small and inspect matches manually
- Prefer DOI, PMID, arXiv ID, publisher pages, CrossRef, PubMed, or arXiv when available

If the query is broad, topical, recent, or exploratory, stop and use `research-lookup`.

#### PubMed Record Lookup

PubMed is used here to resolve known biomedical records, PMIDs, MeSH-backed publication records, and citation metadata.

**Record lookup examples**:
```bash
# Resolve a known PMID or exact title
python scripts/search_pubmed.py '"BNT162b2 mRNA Covid-19 Vaccine in a Nationwide Mass Vaccination Setting"' \
  --limit 5 \
  --output known_pubmed_record.json

# Resolve known biomedical records from an existing candidate list
python scripts/search_pubmed.py \
  --query '"Polack FP"[Author] AND "BNT162b2"[Title/Abstract] AND 2020[Publication Date]' \
  --limit 5 \
  --output candidate_record.json
```

**Record lookup patterns** (see `references/pubmed_search.md`):
- Use MeSH terms: `"Diabetes Mellitus"[MeSH]`
- Field tags: `"cancer"[Title]`, `"Smith J"[Author]`
- Boolean operators: `AND`, `OR`, `NOT`
- Date filters: `2020:2024[Publication Date]`
- Publication types: `"Review"[Publication Type]`
- Combine with E-utilities API for metadata retrieval

**Best Practices**:
- Use MeSH Browser to find correct controlled vocabulary
- Retrieve PMIDs for stable metadata extraction
- Export resolved records to JSON or BibTeX
- Keep lookup queries tied to known papers, known authors, known titles, or known identifiers

### Phase 2: Metadata Extraction

**Goal**: Convert paper identifiers (DOI, PMID, arXiv ID) to complete, accurate metadata.

#### Quick DOI to BibTeX Conversion

For single DOIs, use the quick conversion tool:

```bash
# Convert single DOI
python scripts/doi_to_bibtex.py 10.1038/s41586-021-03819-2

# Convert multiple DOIs from a file
python scripts/doi_to_bibtex.py --input dois.txt --output references.bib

# Different output formats
python scripts/doi_to_bibtex.py 10.1038/nature12345 --format json
```

#### Comprehensive Metadata Extraction

For DOIs, PMIDs, arXiv IDs, or URLs:

```bash
# Extract from DOI
python scripts/extract_metadata.py --doi 10.1038/s41586-021-03819-2

# Extract from PMID
python scripts/extract_metadata.py --pmid 34265844

# Extract from arXiv ID
python scripts/extract_metadata.py --arxiv 2103.14030

# Extract from URL
python scripts/extract_metadata.py --url "https://www.nature.com/articles/s41586-021-03819-2"

# Batch extraction from file (mixed identifiers)
python scripts/extract_metadata.py --input identifiers.txt --output citations.bib
```

**Metadata Sources** (see `references/metadata_extraction.md`):

1. **CrossRef API**: Primary source for DOIs
   - Comprehensive metadata for journal articles
   - Publisher-provided information
   - Includes authors, title, journal, volume, pages, dates
   - Free, no API key required

2. **PubMed E-utilities**: Biomedical literature
   - Official NCBI metadata
   - Includes MeSH terms, abstracts
   - PMID and PMCID identifiers
   - Free, API key recommended for high volume

3. **arXiv API**: Preprints in physics, math, CS, q-bio
   - Complete metadata for preprints
   - Version tracking
   - Author affiliations
   - Free, open access

4. **DataCite API**: Research datasets, software, other resources
   - Metadata for non-traditional scholarly outputs
   - DOIs for datasets and code
   - Free access

**What Gets Extracted**:
- **Required fields**: author, title, year
- **Journal articles**: journal, volume, number, pages, DOI
- **Books**: publisher, ISBN, edition
- **Conference papers**: booktitle, conference location, pages
- **Preprints**: repository (arXiv, bioRxiv), preprint ID
- **Additional**: abstract, keywords, URL

### Phase 3: BibTeX Formatting

**Goal**: Generate clean, properly formatted BibTeX entries.

#### Understanding BibTeX Entry Types

See `references/bibtex_formatting.md` for complete guide.

**Common Entry Types**:
- `@article`: Journal articles (most common)
- `@book`: Books
- `@inproceedings`: Conference papers
- `@incollection`: Book chapters
- `@phdthesis`: Dissertations
- `@misc`: Preprints, software, datasets

**Required Fields by Type**:

```bibtex
@article{citationkey,
  author  = {Last1, First1 and Last2, First2},
  title   = {Article Title},
  journal = {Journal Name},
  year    = {2024},
  volume  = {10},
  number  = {3},
  pages   = {123--145},
  doi     = {10.1234/example}
}

@inproceedings{citationkey,
  author    = {Last, First},
  title     = {Paper Title},
  booktitle = {Conference Name},
  year      = {2024},
  pages     = {1--10}
}

@book{citationkey,
  author    = {Last, First},
  title     = {Book Title},
  publisher = {Publisher Name},
  year      = {2024}
}
```

#### Formatting and Cleaning

Use the formatter to standardize BibTeX files:

```bash
# Format and clean BibTeX file
python scripts/format_bibtex.py references.bib \
  --output formatted_references.bib

# Sort entries by citation key
python scripts/format_bibtex.py references.bib \
  --sort key \
  --output sorted_references.bib

# Sort by year (newest first)
python scripts/format_bibtex.py references.bib \
  --sort year \
  --descending \
  --output sorted_references.bib

# Remove duplicates
python scripts/format_bibtex.py references.bib \
  --deduplicate \
  --output clean_references.bib

# Validate and report issues
python scripts/format_bibtex.py references.bib \
  --validate \
  --report validation_report.txt
```

**Formatting Operations**:
- Standardize field order
- Consistent indentation and spacing
- Proper capitalization in titles (protected with {})
- Standardized author name format
- Consistent citation key format
- Remove unnecessary fields
- Fix common errors (missing commas, braces)

### Phase 4: Citation Validation

**Goal**: Verify all citations are accurate and complete.

#### Comprehensive Validation

```bash
# Validate BibTeX file
python scripts/validate_citations.py references.bib

# Validate and fix common issues
python scripts/validate_citations.py references.bib \
  --auto-fix \
  --output validated_references.bib

# Generate detailed validation report
python scripts/validate_citations.py references.bib \
  --report validation_report.json \
  --verbose
```

**Validation Checks** (see `references/citation_validation.md`):

1. **DOI Verification**:
   - DOI resolves correctly via doi.org
   - Metadata matches between BibTeX and CrossRef
   - No broken or invalid DOIs

2. **Required Fields**:
   - All required fields present for entry type
   - No empty or missing critical information
   - Author names properly formatted

3. **Data Consistency**:
   - Year is valid (4 digits, reasonable range)
   - Volume/number are numeric
   - Pages formatted correctly (e.g., 123--145)
   - URLs are accessible

4. **Duplicate Detection**:
   - Same DOI used multiple times
   - Similar titles (possible duplicates)
   - Same author/year/title combinations

5. **Format Compliance**:
   - Valid BibTeX syntax
   - Proper bracing and quoting
   - Citation keys are unique
   - Special characters handled correctly

**Validation Output**:
```json
{
  "total_entries": 150,
  "valid_entries": 145,
  "errors": [
    {
      "citation_key": "Smith2023",
      "error_type": "missing_field",
      "field": "journal",
      "severity": "high"
    },
    {
      "citation_key": "Jones2022",
      "error_type": "invalid_doi",
      "doi": "10.1234/broken",
      "severity": "high"
    }
  ],
  "warnings": [
    {
      "citation_key": "Brown2021",
      "warning_type": "possible_duplicate",
      "duplicate_of": "Brown2021a",
      "severity": "medium"
    }
  ]
}
```

### Phase 5: Integration with Writing Workflow

#### Building References for Manuscripts

Complete workflow for creating a bibliography:

```bash
# 1. Start from known records or candidates supplied by the user,
# research-lookup, or literature-review.
# candidate_ids.txt may contain DOI, PMID, arXiv ID, URL, or exact title lines.
cat candidate_ids.txt

# 2. Resolve metadata and convert candidate records to BibTeX
python scripts/extract_metadata.py \
  --input candidate_ids.txt \
  --output crispr_refs.bib

# 3. Add specific papers by DOI
python scripts/doi_to_bibtex.py 10.1038/nature12345 >> crispr_refs.bib
python scripts/doi_to_bibtex.py 10.1126/science.abcd1234 >> crispr_refs.bib

# 4. Format and clean the BibTeX file
python scripts/format_bibtex.py crispr_refs.bib \
  --deduplicate \
  --sort year \
  --descending \
  --output references.bib

# 5. Validate all citations
python scripts/validate_citations.py references.bib \
  --auto-fix \
  --report validation.json \
  --output final_references.bib

# 6. Review validation report and fix any remaining issues
cat validation.json

# 7. Use in your LaTeX document
# \bibliography{final_references}
```

#### Integration with Literature Review Skill

This skill complements the `literature-review` skill:

**Literature Review Skill** → Systematic search and synthesis
**Citation Management Skill** → Technical citation handling

**Combined Workflow**:
1. Use `literature-review` for comprehensive multi-database search
2. Use `citation-management` to extract metadata, generate BibTeX, and clean duplicate references
3. Use `literature-review` to synthesize findings thematically
4. Use `citation-verification` for final source-existence and claim-support checks
5. Use `citation-management` to apply final bibliography formatting

```bash
# After completing literature review
# Verify all citations in the review document
python scripts/validate_citations.py my_review_references.bib --report review_validation.json

# Format for specific citation style if needed
python scripts/format_bibtex.py my_review_references.bib \
  --style nature \
  --output formatted_refs.bib
```

## Record Location Strategies

### Known-Record Lookup Best Practices

This skill may use Google Scholar or PubMed only to locate records that are already known from a title, author/year pair, identifier, source URL, or upstream candidate list.

Do not use this section to choose what the user should cite. For topic-level discovery, recent-paper lookup, seminal-paper discovery, citation chasing, or candidate expansion, use `research-lookup` first.

**Record quality signals:**
- DOI, PMID, PMCID, arXiv ID, ISBN, or publisher URL is present.
- Title and author order match the source supplied by the user or upstream lookup.
- Journal/conference name, year, volume, pages, and DOI match authoritative metadata.
- Preprint and published versions are not mixed unless explicitly documented.

**Exact lookup operators** (full list in `references/google_scholar_search.md`):
```
"exact phrase"           # Exact phrase matching
author:lastname          # Search by author
intitle:keyword          # Search in title only
source:journal           # Search specific journal
```

**Example Searches**:
```
# Locate a known record by exact title
"Attention Is All You Need"

# Locate a known record by author and title fragment
author:Vaswani intitle:"Attention"

# Locate a known journal record when a citation is incomplete
"BNT162b2" "Polack" "New England Journal of Medicine"
```

### PubMed Record Lookup Best Practices

**Using MeSH Terms for record resolution**:
MeSH (Medical Subject Headings) provides controlled vocabulary for precise searching.

1. **Find MeSH terms** at https://meshb.nlm.nih.gov/search
2. **Use in known-record queries**: `"Diabetes Mellitus, Type 2"[MeSH]`
3. **Combine with exact title, author, year, PMID, or DOI information when available.**

**Field Tags**:
```
[Title]              # Search in title only
[Title/Abstract]     # Search in title or abstract
[Author]             # Search by author name
[Journal]            # Search specific journal
[Publication Date]   # Date range
[Publication Type]   # Article type
[MeSH]              # MeSH term
```

**Building Complex Queries**:
```bash
# Known author/title/year record
"Polack FP"[Author] AND "BNT162b2"[Title/Abstract] AND 2020[Publication Date]

# Known journal/title fragment record
"NEJM"[Journal] AND "BNT162b2"[Title/Abstract]
```

**E-utilities for Automation**:
The scripts use NCBI E-utilities API for programmatic access:
- **ESearch**: Search and retrieve PMIDs
- **EFetch**: Retrieve full metadata
- **ESummary**: Get summary information
- **ELink**: Find related articles

See `references/pubmed_search.md` for complete API documentation.

## Tools and Scripts

### search_google_scholar.py

Locate known Google Scholar records and export candidate metadata. Do not use this tool here for topic discovery; route topic discovery to `research-lookup`.

**Features**:
- Automated searching with rate limiting
- Small-result exact-record lookup
- Exact title and author/year filtering
- Export to JSON or BibTeX
- Metadata candidates for manual confirmation

**Usage**:
```bash
# Exact-title record lookup
python scripts/search_google_scholar.py '"Attention Is All You Need"'

# Known author/title fragment lookup
python scripts/search_google_scholar.py '"Vaswani" "Attention Is All You Need"' \
  --limit 5 \
  --output known_record.json

# Export a resolved record directly to BibTeX
python scripts/search_google_scholar.py '"Attention Is All You Need"' \
  --limit 5 \
  --format bibtex \
  --output known_record.bib
```

### search_pubmed.py

Resolve known PubMed records using E-utilities API. Do not use this tool here for topic-level biomedical discovery; route discovery to `research-lookup`.

**Features**:
- Complex query support (MeSH, field tags, Boolean)
- Date, author, title, PMID, and publication type filtering
- Batch retrieval for known candidate records
- Export to JSON or BibTeX

**Usage**:
```bash
# Exact-title or title-fragment lookup
python scripts/search_pubmed.py '"BNT162b2 mRNA Covid-19 Vaccine"' \
  --limit 5

# Known author/title/year lookup
python scripts/search_pubmed.py \
  --query '"Polack FP"[Author] AND "BNT162b2"[Title/Abstract] AND 2020[Publication Date]' \
  --limit 5 \
  --output known_pubmed_record.json

# Export to BibTeX
python scripts/search_pubmed.py '"BNT162b2 mRNA Covid-19 Vaccine"' \
  --limit 5 \
  --format bibtex \
  --output known_pubmed_record.bib
```

### extract_metadata.py

Extract complete metadata from paper identifiers.

**Features**:
- Supports DOI, PMID, arXiv ID, URL
- Queries CrossRef, PubMed, arXiv APIs
- Handles multiple identifier types
- Batch processing
- Multiple output formats

**Usage**:
```bash
# Single DOI
python scripts/extract_metadata.py --doi 10.1038/s41586-021-03819-2

# Single PMID
python scripts/extract_metadata.py --pmid 34265844

# Single arXiv ID
python scripts/extract_metadata.py --arxiv 2103.14030

# From URL
python scripts/extract_metadata.py \
  --url "https://www.nature.com/articles/s41586-021-03819-2"

# Batch processing (file with one identifier per line)
python scripts/extract_metadata.py \
  --input paper_ids.txt \
  --output references.bib

# Different output formats
python scripts/extract_metadata.py \
  --doi 10.1038/nature12345 \
  --format json  # or bibtex, yaml
```

### validate_citations.py

Validate BibTeX entries for accuracy and completeness.

**Features**:
- DOI verification via doi.org and CrossRef
- Required field checking
- Duplicate detection
- Format validation
- Auto-fix common issues
- Detailed reporting

**Usage**:
```bash
# Basic validation
python scripts/validate_citations.py references.bib

# With auto-fix
python scripts/validate_citations.py references.bib \
  --auto-fix \
  --output fixed_references.bib

# Detailed validation report
python scripts/validate_citations.py references.bib \
  --report validation_report.json \
  --verbose

# Only check DOIs
python scripts/validate_citations.py references.bib \
  --check-dois-only
```

### format_bibtex.py

Format and clean BibTeX files.

**Features**:
- Standardize formatting
- Sort entries (by key, year, author)
- Remove duplicates
- Validate syntax
- Fix common errors
- Enforce citation key conventions

**Usage**:
```bash
# Basic formatting
python scripts/format_bibtex.py references.bib

# Sort by year (newest first)
python scripts/format_bibtex.py references.bib \
  --sort year \
  --descending \
  --output sorted_refs.bib

# Remove duplicates
python scripts/format_bibtex.py references.bib \
  --deduplicate \
  --output clean_refs.bib

# Complete cleanup
python scripts/format_bibtex.py references.bib \
  --deduplicate \
  --sort year \
  --validate \
  --auto-fix \
  --output final_refs.bib
```

### doi_to_bibtex.py

Quick DOI to BibTeX conversion.

**Features**:
- Fast single DOI conversion
- Batch processing
- Multiple output formats
- Clipboard support

**Usage**:
```bash
# Single DOI
python scripts/doi_to_bibtex.py 10.1038/s41586-021-03819-2

# Multiple DOIs
python scripts/doi_to_bibtex.py \
  10.1038/nature12345 \
  10.1126/science.abc1234 \
  10.1016/j.cell.2023.01.001

# From file (one DOI per line)
python scripts/doi_to_bibtex.py --input dois.txt --output references.bib

# Copy to clipboard
python scripts/doi_to_bibtex.py 10.1038/nature12345 --clipboard
```

## Best Practices

### Record Resolution Strategy

1. **Start from identifiers or known records**:
   - Prefer DOI, PMID, PMCID, arXiv ID, ISBN, publisher URL, exact title, or author/year pairs
   - Treat topic-only requests as discovery requests and route them to `research-lookup`
   - Return to citation-management only after candidate records exist

2. **Use authoritative metadata sources**:
   - CrossRef for DOI-backed journal records
   - PubMed for biomedical PMIDs and PMCIDs
   - arXiv for preprints
   - Publisher pages when automated metadata conflicts

3. **Resolve ambiguity explicitly**:
   - Compare exact title, authors, venue, year, DOI, and pages
   - Keep preprint and published versions separate until the user chooses one
   - Mark ambiguous matches instead of silently picking the first result

4. **Document record provenance**:
   - Record identifier source and lookup date
   - Note metadata source used for each repair
   - Flag records that need citation-verification for source existence or claim support

### Metadata Extraction

1. **Always use DOIs when available**:
   - Most reliable identifier
   - Permanent link to the publication
   - Best metadata source via CrossRef

2. **Verify extracted metadata**:
   - Check author names are correct
   - Verify journal/conference names
   - Confirm publication year
   - Validate page numbers and volume

3. **Handle edge cases**:
   - Preprints: Include repository and ID
   - Preprints later published: Use published version
   - Conference papers: Include conference name and location
   - Book chapters: Include book title and editors

4. **Maintain consistency**:
   - Use consistent author name format
   - Standardize journal abbreviations
   - Use same DOI format (URL preferred)

### BibTeX Quality

1. **Follow conventions**:
   - Use meaningful citation keys (FirstAuthor2024keyword)
   - Protect capitalization in titles with {}
   - Use -- for page ranges (not single dash)
   - Include DOI field for all modern publications

2. **Keep it clean**:
   - Remove unnecessary fields
   - No redundant information
   - Consistent formatting
   - Validate syntax regularly

3. **Organize systematically**:
   - Sort by year, author, or citation key
   - Group entries by manuscript section or source list when useful
   - Use separate files for different projects
   - Merge carefully to avoid duplicates

### Validation

1. **Validate early and often**:
   - Check citations when adding them
   - Validate complete bibliography before submission
   - Re-validate after any manual edits

2. **Fix issues promptly**:
   - Broken DOIs: Find correct identifier
   - Missing fields: Extract from original source
   - Duplicates: Choose best version, remove others
   - Format errors: Use auto-fix when safe

3. **Manual review for critical citations**:
   - Verify key papers cited correctly
   - Check author names match publication
   - Confirm page numbers and volume
   - Ensure URLs are current

## Common Pitfalls to Avoid

1. **Using citation-management for discovery**: Asking this skill to find new papers by topic
   - **Solution**: Use `research-lookup` for topic discovery and return here only after candidate records or identifiers exist

2. **Accepting metadata blindly**: Not verifying extracted information
   - **Solution**: Spot-check extracted metadata against original sources

3. **Ignoring DOI errors**: Broken or incorrect DOIs in bibliography
   - **Solution**: Run validation before final submission

4. **Inconsistent formatting**: Mixed citation key styles, formatting
   - **Solution**: Use format_bibtex.py to standardize

5. **Duplicate entries**: Same paper cited multiple times with different keys
   - **Solution**: Use duplicate detection in validation

6. **Missing required fields**: Incomplete BibTeX entries
   - **Solution**: Validate and ensure all required fields present

7. **Outdated preprints**: Citing preprint when published version exists
   - **Solution**: Check if preprints have been published, update to journal version

8. **Special character issues**: Broken LaTeX compilation due to characters
   - **Solution**: Use proper escaping or Unicode in BibTeX

9. **No validation before submission**: Submitting with citation errors
   - **Solution**: Always run validation as final check

10. **Manual BibTeX entry**: Typing entries by hand
    - **Solution**: Always extract from metadata sources using scripts

## Example Workflows

### Example 1: Building a Bibliography for a Paper

```bash
# Step 1: Start from candidate records supplied by the user,
# research-lookup, or literature-review.
# candidate_ids.txt contains DOI, PMID, arXiv ID, URL, or exact title lines.
cat candidate_ids.txt

# Step 2: Extract metadata from candidate records
python scripts/extract_metadata.py \
  --input candidate_ids.txt \
  --output candidate_records.bib

# Step 3: Add specific papers you already know
python scripts/doi_to_bibtex.py 10.1038/s41586-021-03819-2 >> specific.bib
python scripts/doi_to_bibtex.py 10.1126/science.aam9317 >> specific.bib

# Step 4: Combine all BibTeX files
cat candidate_records.bib specific.bib > combined.bib

# Step 5: Format and deduplicate
python scripts/format_bibtex.py combined.bib \
  --deduplicate \
  --sort year \
  --descending \
  --output formatted.bib

# Step 6: Validate
python scripts/validate_citations.py formatted.bib \
  --auto-fix \
  --report validation.json \
  --output final_references.bib

# Step 7: Review any issues
cat validation.json | grep -A 3 '"errors"'

# Step 8: Use in LaTeX
# \bibliography{final_references}
```

### Example 2: Converting a List of DOIs

```bash
# You have a text file with DOIs (one per line)
# dois.txt contains:
# 10.1038/s41586-021-03819-2
# 10.1126/science.aam9317
# 10.1016/j.cell.2023.01.001

# Convert all to BibTeX
python scripts/doi_to_bibtex.py --input dois.txt --output references.bib

# Validate the result
python scripts/validate_citations.py references.bib --verbose
```

### Example 3: Cleaning an Existing BibTeX File

```bash
# You have a messy BibTeX file from various sources
# Clean it up systematically

# Step 1: Format and standardize
python scripts/format_bibtex.py messy_references.bib \
  --output step1_formatted.bib

# Step 2: Remove duplicates
python scripts/format_bibtex.py step1_formatted.bib \
  --deduplicate \
  --output step2_deduplicated.bib

# Step 3: Validate and auto-fix
python scripts/validate_citations.py step2_deduplicated.bib \
  --auto-fix \
  --output step3_validated.bib

# Step 4: Sort by year
python scripts/format_bibtex.py step3_validated.bib \
  --sort year \
  --descending \
  --output clean_references.bib

# Step 5: Final validation report
python scripts/validate_citations.py clean_references.bib \
  --report final_validation.json \
  --verbose

# Review report
cat final_validation.json
```

### Example 4: Resolving Known Records Without DOIs

```bash
# Locate known papers when the user supplied exact titles but no DOI
python scripts/search_google_scholar.py '"Attention Is All You Need"' \
  --limit 5 \
  --output attention_record.json

python scripts/search_pubmed.py '"BNT162b2 mRNA Covid-19 Vaccine"' \
  --limit 5 \
  --output vaccine_record.json

# Convert to BibTeX
python scripts/extract_metadata.py \
  --input attention_record.json \
  --output attention_refs.bib

python scripts/extract_metadata.py \
  --input vaccine_record.json \
  --output vaccine_refs.bib

# The BibTeX files now contain resolved metadata for known records
```

## Integration with Other Skills

### Literature Review Skill

**Citation Management** provides the technical infrastructure for **Literature Review**:

- **Literature Review**: Multi-database systematic search and synthesis
- **Citation Management**: Metadata extraction and validation

**Combined workflow**:
1. Use literature-review for systematic search methodology
2. Use citation-management to extract metadata, generate BibTeX, and clean duplicate references
3. Use literature-review to synthesize findings
4. Use citation-verification to confirm source existence and claim support
5. Use citation-management to apply final bibliography formatting

### Scientific Writing Skill

**Citation Management** ensures accurate references for **Scientific Writing**:

- Export validated BibTeX for use in LaTeX manuscripts
- Keep citation metadata and bibliography formatting consistent with publication standards
- Format references according to journal requirements

### Venue Templates Skill

**Citation Management** works with **Venue Templates** for submission-ready manuscripts:

- Different venues require different citation styles
- Generate properly formatted references
- Validate citations meet venue requirements

## Resources

### Bundled Resources

**References** (in `references/`):
- `google_scholar_search.md`: Google Scholar exact-record lookup guide
- `pubmed_search.md`: PubMed and E-utilities metadata lookup documentation
- `metadata_extraction.md`: Metadata sources and field requirements
- `citation_validation.md`: Validation criteria and quality checks
- `bibtex_formatting.md`: BibTeX entry types and formatting rules

**Scripts** (in `scripts/`):
- `search_google_scholar.py`: Google Scholar known-record lookup automation
- `search_pubmed.py`: PubMed E-utilities metadata lookup client
- `extract_metadata.py`: Universal metadata extractor
- `validate_citations.py`: Citation validation and verification
- `format_bibtex.py`: BibTeX formatter and cleaner
- `doi_to_bibtex.py`: Quick DOI to BibTeX converter

**Assets** (in `assets/`):
- `bibtex_template.bib`: Example BibTeX entries for all types
- `citation_checklist.md`: Quality assurance checklist

### External Resources

**Record Lookup Services**:
- Google Scholar: https://scholar.google.com/
- PubMed: https://pubmed.ncbi.nlm.nih.gov/
- PubMed Advanced Search: https://pubmed.ncbi.nlm.nih.gov/advanced/

**Metadata APIs**:
- CrossRef API: https://api.crossref.org/
- PubMed E-utilities: https://www.ncbi.nlm.nih.gov/books/NBK25501/
- arXiv API: https://arxiv.org/help/api/
- DataCite API: https://api.datacite.org/

**Tools and Validators**:
- MeSH Browser: https://meshb.nlm.nih.gov/search
- DOI Resolver: https://doi.org/
- BibTeX Format: http://www.bibtex.org/Format/

**Citation Styles**:
- BibTeX documentation: http://www.bibtex.org/
- LaTeX bibliography management: https://www.overleaf.com/learn/latex/Bibliography_management

## Dependencies

### Required Python Packages

```bash
# Core dependencies
pip install requests  # HTTP requests for APIs
pip install bibtexparser  # BibTeX parsing and formatting
pip install biopython  # PubMed E-utilities access

# Optional (for Google Scholar)
pip install scholarly  # Google Scholar API wrapper
# or
pip install selenium  # For more robust Scholar scraping
```

### Optional Tools

```bash
# For advanced validation
pip install crossref-commons  # Enhanced CrossRef API access
pip install pylatexenc  # LaTeX special character handling
```

## Summary

The citation-management skill provides:

1. **Known-record lookup** for exact titles, author/year pairs, and identifier-backed records
2. **Automated metadata extraction** from DOI, PMID, arXiv ID, URLs
3. **Citation validation** with DOI verification and completeness checking
4. **BibTeX formatting** with standardization and cleaning tools
5. **Quality assurance** through validation and reporting
6. **Integration** with scientific writing workflow
7. **Reproducibility** through documented search and extraction methods

Use this skill to maintain accurate, complete citations throughout your research and ensure publication-ready bibliographies.
