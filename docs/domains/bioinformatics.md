# bioinformatics

Active skills: 24

## Install

Complete domain install:

```bash
python3 scripts/skills.py install --target repo --domain bioinformatics --mode symlink --write-agents-md
```

Install a few skills precisely:

```bash
python3 scripts/skills.py install --target repo --skill domain/bioinformatics/anndata --skill domain/bioinformatics/arboreto --skill domain/bioinformatics/bioinformatics-database-retrieval --mode symlink --write-agents-md
```

Complete domain installs are supported. If an audit reports high description length or many active skills, treat it as a context-budget warning, not an installation error.

## Common Uses

- Install the whole domain for a project where most tasks are in this area.
- Use precise skill selectors when only one tool or workflow is needed.
- Combine with profiles when a project needs a curated cross-domain set.

## Skills

- `anndata` (`skills/domains/bioinformatics/single-cell/anndata`): Data structure for annotated matrices in single-cell analysis. Use when working with .h5ad files or integrating with the scverse ecosystem. This is the data format skill—for analysis workflows use scanpy; for probabilistic models use scvi-tools; for population-scale queries use cellxgene-census.
- `arboreto` (`skills/domains/bioinformatics/omics-analysis/arboreto`): Infer gene regulatory networks (GRNs) from gene expression data using scalable algorithms (GRNBoost2, GENIE3). Use when analyzing transcriptomics data (bulk RNA-seq, single-cell RNA-seq) to identify transcription factor-target gene relationships and regulatory interactions. Supports distributed computation for large-scale datasets.
- `bioinformatics-database-retrieval` (`skills/domains/bioinformatics/databases/bioinformatics-database-retrieval`): Use for gene, protein, pathway, variant, expression, disease, and structure database lookups. Prefer workflow-specific skills for scanpy, scvi-tools, pysam, or DICOM work.
- `biopython` (`skills/domains/bioinformatics/biology-toolkits/biopython`): Comprehensive molecular biology toolkit. Use for sequence manipulation, file parsing (FASTA/GenBank/PDB), phylogenetics, and programmatic NCBI/PubMed access (Bio.Entrez). Best for batch processing, custom bioinformatics pipelines, BLAST automation. For quick lookups use gget; for multi-service integration use bioservices.
- `deeptools` (`skills/domains/bioinformatics/omics-analysis/deeptools`): NGS analysis toolkit. BAM to bigWig conversion, QC (correlation, PCA, fingerprints), heatmaps/profiles (TSS, peaks), for ChIP-seq, RNA-seq, ATAC-seq visualization.
- `dnanexus-integration` (`skills/domains/bioinformatics/platforms/dnanexus-integration`): DNAnexus cloud genomics platform. Build apps/applets, manage data (upload/download), dxpy Python SDK, run workflows, FASTQ/BAM/VCF, for genomics pipeline development and execution.
- `esm` (`skills/domains/bioinformatics/biology-toolkits/esm`): Comprehensive toolkit for protein language models including ESM3 (generative multimodal protein design across sequence, structure, and function) and ESM C (efficient protein embeddings and representations).
- `etetoolkit` (`skills/domains/bioinformatics/biology-toolkits/etetoolkit`): Phylogenetic tree toolkit (ETE). Tree manipulation (Newick/NHX), evolutionary event detection, orthology/paralogy, NCBI taxonomy, visualization (PDF/SVG), for phylogenomics.
- `flowio` (`skills/domains/bioinformatics/omics-analysis/flowio`): Parse FCS (Flow Cytometry Standard) files v2.0-3.1. Extract events as NumPy arrays, read metadata/channels, convert to CSV/DataFrame, for flow cytometry data preprocessing.
- `geniml` (`skills/domains/bioinformatics/omics-analysis/geniml`): This skill should be used when working with genomic interval data (BED files) for machine learning tasks. Applies to BED file collections, scATAC-seq data, chromatin accessibility datasets, and region-based genomic feature learning.
- `gtars` (`skills/domains/bioinformatics/omics-analysis/gtars`): High-performance toolkit for genomic interval analysis in Rust with Python bindings. Use when working with genomic regions, BED files, coverage tracks, overlap detection, tokenization for ML models, or fragment analysis in computational genomics and machine learning applications.
- `lamindb` (`skills/domains/bioinformatics/platforms/lamindb`): This skill should be used when working with LaminDB, an open-source data framework for biology that makes data queryable, traceable, reproducible, and FAIR.
- `latchbio-integration` (`skills/domains/bioinformatics/platforms/latchbio-integration`): Latch platform for bioinformatics workflows. Build pipelines with Latch SDK, @workflow/@task decorators, deploy serverless workflows, LatchFile/LatchDir, Nextflow/Snakemake integration.
- `neuropixels-analysis` (`skills/domains/bioinformatics/specialized/neuropixels-analysis`): Neuropixels neural recording analysis. Load SpikeGLX/OpenEphys data, preprocess, motion correction, Kilosort4 spike sorting, quality metrics, Allen/IBL curation, AI-assisted visual analysis, for Neuropixels 1.0/2.0 extracellular electrophysiology.
- `phylogenetics` (`skills/domains/bioinformatics/biology-toolkits/phylogenetics`): Build and analyze phylogenetic trees using MAFFT (multiple alignment), IQ-TREE 2 (maximum likelihood), and FastTree (fast NJ/ML). Visualize with ETE3 or FigTree. For evolutionary analysis, microbial genomics, viral phylodynamics, protein family analysis, and molecular clock studies.
- `polars-bio` (`skills/domains/bioinformatics/omics-analysis/polars-bio`): High-performance genomic interval operations and bioinformatics file I/O on Polars DataFrames. Overlap, nearest, merge, coverage, complement, subtract for BED/VCF/BAM/GFF intervals. Streaming, cloud-native, faster bioframe alternative.
- `pydeseq2` (`skills/domains/bioinformatics/omics-analysis/pydeseq2`): Differential gene expression analysis (Python DESeq2). Identify DE genes from bulk RNA-seq counts, Wald tests, FDR correction, volcano/MA plots, for RNA-seq analysis.
- `pysam` (`skills/domains/bioinformatics/genomics-io/pysam`): Genomic file toolkit. Read/write SAM/BAM/CRAM alignments, VCF/BCF variants, FASTA/FASTQ sequences, extract regions, calculate coverage, for NGS data processing pipelines.
- `scanpy` (`skills/domains/bioinformatics/single-cell/scanpy`): Standard single-cell RNA-seq analysis pipeline. Use for QC, normalization, dimensionality reduction (PCA/UMAP/t-SNE), clustering, differential expression, and visualization. Best for exploratory scRNA-seq analysis with established workflows. For deep learning models use scvi-tools; for data format questions use anndata.
- `scikit-bio` (`skills/domains/bioinformatics/biology-toolkits/scikit-bio`): Biological data toolkit. Sequence analysis, alignments, phylogenetic trees, diversity metrics (alpha/beta, UniFrac), ordination (PCoA), PERMANOVA, FASTA/Newick I/O, for microbiome analysis.
- `scvelo` (`skills/domains/bioinformatics/single-cell/scvelo`): RNA velocity analysis with scVelo. Estimate cell state transitions from unspliced/spliced mRNA dynamics, infer trajectory directions, compute latent time, and identify driver genes in single-cell RNA-seq data. Complements Scanpy/scVI-tools for trajectory inference.
- `scvi-tools` (`skills/domains/bioinformatics/single-cell/scvi-tools`): Deep generative models for single-cell omics. Use when you need probabilistic batch correction (scVI), transfer learning, differential expression with uncertainty, or multi-modal integration (TOTALVI, MultiVI). Best for advanced modeling, batch effects, multimodal data. For standard analysis pipelines use scanpy.
- `tiledbvcf` (`skills/domains/bioinformatics/genomics-io/tiledbvcf`): Efficient storage and retrieval of genomic variant data using TileDB. Scalable VCF/BCF ingestion, incremental sample addition, compressed storage, parallel queries, and export capabilities for population genomics.
- `zarr-python` (`skills/domains/bioinformatics/genomics-io/zarr-python`): Chunked N-D arrays for cloud storage. Compressed arrays, parallel I/O, S3/GCS integration, NumPy/Dask/Xarray compatible, for large-scale scientific computing pipelines.

## Main References

- No domain references discovered yet. Add `references/source-notes.md`, checklists, or overview notes when the skill carries long-lived domain knowledge.
