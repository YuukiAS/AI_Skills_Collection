---
name: data-analysis-python
description: Python data analysis workflows with EDA, Polars, scikit-learn, and symbolic math.
status: active
provenance: generated
trusted: false
requires_network: false
writes_files: true
executes_code: false
secrets_needed:
last_reviewed: 2026-07-10
profile_tags:
recommended_scope: project
source_skills:
  - skills/tools/data-science/exploratory-data-analysis
  - skills/tools/data-science/polars
  - skills/tools/data-science/scikit-learn
  - skills/tools/data-science/sympy
---

# data-analysis-python

## Trigger Boundary

Python data analysis workflows with EDA, Polars, scikit-learn, and symbolic math.

Use this aggregate Codex App skill when the task matches one of the source workflows below.

## Source Workflows

- `exploratory-data-analysis`: Perform comprehensive exploratory data analysis on scientific data files across 200+ file formats. This skill should be used when analyzing any scientific data file to understand its structure, content, quality, and characteristics. Reference: `references/source-skills/tools-data-science-exploratory-data-analysis/source-skill.md`
- `polars`: Fast in-memory DataFrame library for datasets that fit in RAM. Use when pandas is too slow but data still fits in memory. Lazy evaluation, parallel execution, Apache Arrow backend. Best for 1-100GB datasets, ETL pipelines, faster pandas replacement. For larger-than-RAM data use dask or vaex. Reference: `references/source-skills/tools-data-science-polars/source-skill.md`
- `scikit-learn`: Machine learning in Python with scikit-learn. Provides comprehensive reference documentation for algorithms, preprocessing techniques, pipelines, and best practices. Reference: `references/source-skills/tools-data-science-scikit-learn/source-skill.md`
- `sympy`: Use this skill when working with symbolic mathematics in Python. Apply this skill when the user needs exact symbolic results rather than numerical approximations, or when working with mathematical formulas that contain variables and parameters. Reference: `references/source-skills/tools-data-science-sympy/source-skill.md`

## Workflow

1. Choose the source workflow whose trigger boundary best matches the user request.
2. Read that source workflow's `source-skill.md` before acting.
3. Load only the needed files under that workflow's copied references, scripts, assets, or evals.
4. Follow the source workflow unless the current project gives stricter instructions.
