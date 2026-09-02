# SNF-CN-TECH-001 Decision

Decision: `NO_DEEP_REWRITE`

The source is already readable Chinese technical prose. The correct behavior is
to preserve it as-is or make only local copyediting if the user explicitly asks.

Critical protected terms preserved:

- `AI_Research_Toolkit`
- R
- Bioconductor
- R library
- `renv`
- `BiocManager`
- DESeq2/PyDESeq2
- Scanpy/Seurat
- `sessionInfo()`

The scientific-rewrite route should not translate package names, collapse
version/release constraints, delete reproducibility requirements, or turn this
technical list into casual prose.
