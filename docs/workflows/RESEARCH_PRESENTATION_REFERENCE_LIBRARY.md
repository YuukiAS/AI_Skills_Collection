# Research Presentation Reference Library

This workflow maintains a long-lived local reference cache for research, statistics, biostatistics, and medical-imaging presentation patterns.

## Storage Boundary

- Downloaded public PDFs, PPTX files, extracted text, rendered pages, and cache inventories live under `.cache/research-presentation-reference-library/`.
- `.cache/` is ignored and must stay out of git.
- Commit metadata only: source URLs, expected filenames, source family, rights notes, page-level lessons, and verification status.
- Do not commit whole-slide screenshots, public decks, clinical images, private project figures, or copied source styling.

## Committed Metadata

The rebuildable source-of-truth files are:

- `skills/tools/documents-media/presentations/shared/references/build_reference_metadata.py`
- `skills/tools/documents-media/presentations/shared/references/reference_sources_manifest.json`
- `skills/tools/documents-media/presentations/shared/references/reference_source_search_matrix.csv`
- `skills/tools/documents-media/presentations/shared/references/research_slide_reference_index.csv`

Regenerate metadata after source changes:

```bash
python skills/tools/documents-media/presentations/shared/references/build_reference_metadata.py
```

## Local Cache Manifest

Keep a local, untracked cache manifest at:

```text
.cache/research-presentation-reference-library/manifest.jsonl
```

Each row should record filename, local path, source URL, download date if known, institution, speaker, talk type, domain, file type, size, slide/page count when available, checksum, rights note, and page-level review status.

## Adding Sources

1. Add candidate sources to `build_reference_metadata.py`.
2. Prefer official university, lab, personal academic, society, or conference sources.
3. Record rejected or lower-value sources in `reference_source_search_matrix.csv` rather than silently dropping them.
4. Download assets only into `.cache/research-presentation-reference-library/sources/`.
5. Compute checksum and update the local cache manifest.
6. Add page-level records only after reviewing the actual page or slide function.

## Retrieval Rule

Retrieve references by:

- `page_function`
- `scientific_domain`
- `statistical_subdomain`
- `evidence_type`

Do not retrieve by speaker name alone. Speaker and institution are credibility/provenance fields, not layout templates.

## Rights Rule

The index teaches organization, evidence adjacency, and QA criteria. Generated decks should redraw the organization with owned or synthetic data. They must not copy full slides, third-party visual identity, public figures, private clinical images, or unclear-license assets.
