---
name: bioinformatics-workflows
description: Common bioinformatics workflows across databases, single-cell analysis, genomics I/O, and omics analysis.
status: active
provenance: generated
trusted: false
requires_network: true
writes_files: true
executes_code: false
secrets_needed:
  - TILEDB_REST_TOKEN
last_reviewed: 2026-07-10
profile_tags:
recommended_scope: project
source_skills:
  - skills/domains/bioinformatics/databases/bioinformatics-database-retrieval
  - skills/domains/bioinformatics/single-cell/scanpy
  - skills/domains/bioinformatics/single-cell/scvi-tools
  - skills/domains/bioinformatics/single-cell/anndata
  - skills/domains/bioinformatics/genomics-io/pysam
  - skills/domains/bioinformatics/omics-analysis/pydeseq2
  - skills/domains/bioinformatics/biology-toolkits/biopython
  - skills/domains/bioinformatics/biology-toolkits/scikit-bio
  - skills/domains/bioinformatics/omics-analysis/polars-bio
  - skills/domains/bioinformatics/genomics-io/tiledbvcf
default_prompt:
---

# bioinformatics-workflows

## Trigger Boundary

Common bioinformatics workflows across databases, single-cell analysis, genomics I/O, and omics analysis.

Use this aggregate Codex App skill when the task matches one of the source workflows below.

## Source Workflows

- `bioinformatics-database-retrieval`: Use for gene, protein, pathway, variant, expression, disease, and structure database lookups. Prefer workflow-specific skills for scanpy, scvi-tools, pysam, or DICOM work. Reference: `_src/db/source.md`
- `scanpy`: Standard single-cell RNA-seq analysis pipeline. Use for QC, normalization, dimensionality reduction (PCA/UMAP/t-SNE), clustering, differential expression, and visualization. Best for exploratory scRNA-seq analysis with established workflows. For deep learning models use scvi-tools; for data format questions use anndata. Reference: `_src/scanpy/source.md`
- `scvi-tools`: Deep generative models for single-cell omics. Use when you need probabilistic batch correction (scVI), transfer learning, differential expression with uncertainty, or multi-modal integration (TOTALVI, MultiVI). Best for advanced modeling, batch effects, multimodal data. For standard analysis pipelines use scanpy. Reference: `_src/scvi/source.md`
- `anndata`: Data structure for annotated matrices in single-cell analysis. Use when working with .h5ad files or integrating with the scverse ecosystem. This is the data format skill—for analysis workflows use scanpy; for probabilistic models use scvi-tools; for population-scale queries use cellxgene-census. Reference: `_src/anndata/source.md`
- `pysam`: Genomic file toolkit. Read/write SAM/BAM/CRAM alignments, VCF/BCF variants, FASTA/FASTQ sequences, extract regions, calculate coverage, for NGS data processing pipelines. Reference: `_src/pysam/source.md`
- `pydeseq2`: Differential gene expression analysis (Python DESeq2). Identify DE genes from bulk RNA-seq counts, Wald tests, FDR correction, volcano/MA plots, for RNA-seq analysis. Reference: `_src/deseq/source.md`
- `biopython`: Comprehensive molecular biology toolkit. Use for sequence manipulation, file parsing (FASTA/GenBank/PDB), phylogenetics, and programmatic NCBI/PubMed access (Bio.Entrez). Best for batch processing, custom bioinformatics pipelines, BLAST automation. For quick lookups use gget; for multi-service integration use bioservices. Reference: `_src/biopy/source.md`
- `scikit-bio`: Biological data toolkit. Sequence analysis, alignments, phylogenetic trees, diversity metrics (alpha/beta, UniFrac), ordination (PCoA), PERMANOVA, FASTA/Newick I/O, for microbiome analysis. Reference: `_src/skbio/source.md`
- `polars-bio`: High-performance genomic interval operations and bioinformatics file I/O on Polars DataFrames. Overlap, nearest, merge, coverage, complement, subtract for BED/VCF/BAM/GFF intervals. Streaming, cloud-native, faster bioframe alternative. Reference: `_src/polars/source.md`
- `tiledbvcf`: Efficient storage and retrieval of genomic variant data using TileDB. Scalable VCF/BCF ingestion, incremental sample addition, compressed storage, parallel queries, and export capabilities for population genomics. Reference: `_src/vcf/source.md`

## Workflow

1. Choose the source workflow whose trigger boundary best matches the user request.
2. Read that source workflow's `source.md` before acting.
3. Load only the needed files under that workflow's copied references, scripts, assets, or evals.
4. Follow the source workflow unless the current project gives stricter instructions.
