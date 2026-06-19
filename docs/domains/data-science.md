# data-science

Active skills: 13

## Install

Complete domain install:

```bash
python3 scripts/skills.py install --target repo --domain data-science --mode symlink --write-agents-md
```

Install a few skills precisely:

```bash
python3 scripts/skills.py install --target repo --skill aeon --skill dask --skill exploratory-data-analysis --mode symlink --write-agents-md
```

Complete domain installs are supported. If an audit reports high description length or many active skills, treat it as a context-budget warning, not an installation error.

## Common Uses

- Install the whole domain for a project where most tasks are in this area.
- Use precise skill selectors when only one tool or workflow is needed.
- Combine with profiles when a project needs a curated cross-domain set.

## Skills

- `aeon` (`skills/reusable/data-science/aeon`): This skill should be used for time series machine learning tasks including classification, regression, clustering, forecasting, anomaly detection, segmentation, and similarity search.
- `dask` (`skills/reusable/data-science/dask`): Distributed computing for larger-than-RAM pandas/NumPy workflows. Use when you need to scale existing pandas/NumPy code beyond memory or across clusters. Best for parallel file processing, distributed ML, integration with existing pandas code. For out-of-core analytics on single machine use vaex; for in-memory speed use polars.
- `exploratory-data-analysis` (`skills/reusable/data-science/exploratory-data-analysis`): Perform comprehensive exploratory data analysis on scientific data files across 200+ file formats. This skill should be used when analyzing any scientific data file to understand its structure, content, quality, and characteristics.
- `geopandas` (`skills/reusable/data-science/geopandas`): Python library for working with geospatial vector data including shapefiles, GeoJSON, and GeoPackage files. Supports PostGIS databases, interactive maps, and integration with matplotlib/folium/cartopy.
- `matlab` (`skills/reusable/data-science/matlab`): MATLAB and GNU Octave numerical computing for matrix operations, data analysis, visualization, and scientific computing. Also use when the user needs help with MATLAB syntax, functions, or wants to convert between MATLAB and Python code.
- `networkx` (`skills/reusable/data-science/networkx`): Comprehensive toolkit for creating, analyzing, and visualizing complex networks and graphs in Python. Applicable to social networks, biological networks, transportation systems, citation networks, and any domain involving pairwise relationships.
- `polars` (`skills/reusable/data-science/polars`): Fast in-memory DataFrame library for datasets that fit in RAM. Use when pandas is too slow but data still fits in memory. Lazy evaluation, parallel execution, Apache Arrow backend. Best for 1-100GB datasets, ETL pipelines, faster pandas replacement. For larger-than-RAM data use dask or vaex.
- `pymoo` (`skills/reusable/data-science/pymoo`): Multi-objective optimization framework. NSGA-II, NSGA-III, MOEA/D, Pareto fronts, constraint handling, benchmarks (ZDT, DTLZ), for engineering design and optimization problems.
- `scikit-learn` (`skills/reusable/data-science/scikit-learn`): Machine learning in Python with scikit-learn. Provides comprehensive reference documentation for algorithms, preprocessing techniques, pipelines, and best practices.
- `shap` (`skills/reusable/data-science/shap`): Model interpretability and explainability using SHAP (SHapley Additive exPlanations). Works with tree-based models (XGBoost, LightGBM, Random Forest), deep learning (TensorFlow, PyTorch), linear models, and any black-box model.
- `sympy` (`skills/reusable/data-science/sympy`): Use this skill when working with symbolic mathematics in Python. Apply this skill when the user needs exact symbolic results rather than numerical approximations, or when working with mathematical formulas that contain variables and parameters.
- `umap-learn` (`skills/reusable/data-science/umap-learn`): UMAP dimensionality reduction. Fast nonlinear manifold learning for 2D/3D visualization, clustering preprocessing (HDBSCAN), supervised/parametric UMAP, for high-dimensional data.
- `vaex` (`skills/reusable/data-science/vaex`): Use this skill for processing and analyzing large tabular datasets (billions of rows) that exceed available RAM.

## Main References

- No domain references discovered yet. Add `references/source-notes.md`, checklists, or overview notes when the skill carries long-lived domain knowledge.
