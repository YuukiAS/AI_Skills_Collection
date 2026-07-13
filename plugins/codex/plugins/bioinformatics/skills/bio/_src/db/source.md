---
name: bioinformatics-database-retrieval
description: Use for gene, protein, pathway, variant, expression, disease, and structure database lookups. Prefer workflow-specific skills for scanpy, scvi-tools, pysam, or DICOM work.
status: active
provenance: local
trusted: true
requires_network: true
writes_files: false
executes_code: false
secrets_needed:
last_reviewed: 2026-05-14
profile_tags:
recommended_scope: project
---
# Bioinformatics Database Retrieval

Use this umbrella skill for targeted retrieval from common biological databases
when the task is primarily a lookup, ID mapping, or small data extraction rather
than a full analysis workflow.

## Provider Routing

- Genes and annotations: Ensembl, NCBI Gene/gget, GTEx, gnomAD.
- Proteins and domains: UniProt, AlphaFold DB, InterPro, STRING.
- Pathways and regulatory data: KEGG, Reactome, JASPAR.
- Studies and cohorts: GEO, ENA, GWAS Catalog, OpenTargets, DepMap.
- GWAS summary statistics: start with `references/providers/gwas-summary-statistics-databases.md`, then choose the smallest official source that fits the trait, population, access, and downstream analysis.
- Phenotype and disease graphs: Monarch, OpenTargets.

Provider details live in `references/providers/`. Read only the relevant
provider note before making network calls.

## Workflow

1. Clarify entity type, organism, genome build, ID namespace, and desired output.
2. Pick the smallest provider set that can answer the question.
3. Prefer official REST APIs or stable package clients.
4. For GWAS summary statistics, record genome build, ancestry/population, sample size, endpoint/trait definition, file version or release, harmonization status, and access conditions.
5. Record query URLs, access dates, and version/build metadata in the response.
6. For batch retrieval, write reproducible scripts rather than manual browser steps.

## Boundaries

- Use `scanpy`, `scvi-tools`, or `anndata` for single-cell analysis workflows.
- Use `pysam`, `tiledbvcf`, or `polars-bio` for local genomic files.
- Use `pydicom` or medical-imaging skills for DICOM/NIfTI imaging.
