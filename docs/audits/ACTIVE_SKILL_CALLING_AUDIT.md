# Active Skill Calling Audit
## Scope And Baseline
- Frozen baseline: `main @ 157552aae0d4871a4a333ed14fd1e56a000472ee`; `origin/main` verified at that SHA after `git fetch origin main`.
- Source active skill count: `149` from `registry.json`; generated plugin copies are excluded.
- Audit purpose: capability discovery, calling boundary, entrance, and marketplace/profile exposure. No code changes or topology changes are proposed here.

## Duplicate Capability And Calling Conflict Clusters
| Cluster | Involved source skills | Conflict type | Current evidence | Possible calling consequence |
|---|---|---|---|---|
| Research paper workflow overlap | `scientific-writing`, `paper-workflow-orchestrator`, `nature-manuscript-workflow`, `peer-review`, `scholar-evaluation` | Broad-vs-specific / duplicate boundary | All describe manuscript drafting, claim-evidence, acceptance/reviewer checks, or broad-journal readiness under research-writing. | A broad manuscript request may be caught by several source skills unless the aggregate decides route precisely. |
| Literature and citation provider overlap | `literature-review`, `citation-verification`, `citation-management`, `research-lookup`, `arxiv-database`, `biorxiv-database`, `pubmed-database`, `openalex-database`, `valyu-scientific-search`, `bgpt-paper-search`, `pyzotero` | Tool/provider competition | The aggregate includes literature-review, citation-verification, citation-management, research-lookup, and pyzotero; provider/database skills also expose direct search tasks. | A natural paper search request could route to a provider skill before the evidence/citation workflow is chosen. |
| OCR academic document recovery overlap | `academic-paper-writer-pro`, `ocr-kb`, `markitdown`, `pdf` | Duplicate/adjacent task boundary | academic-paper-writer-pro and ocr-kb both cover scanned PDF/OCR recovery and DOCX/Markdown delivery; markitdown/pdf also trigger on PDF conversion. | Scanned paper cleanup may start as generic PDF conversion instead of OCR recovery or manuscript artifact repair. |
| Visualization and diagram entry spread | `markdown-mermaid-writing`, `drawio-diagrams`, `d2-diagrams`, `plantuml-diagrams`, `excalidraw-diagrams`, `scientific-schematics`, `scientific-visualization`, `scientific-figure-qa`, `generate-image`, `imagegen`, `canvas-design`, `infographics` | Multiple front doors / medium competition | Diagram DSL, scientific figure, image generation, infographic, and canvas-design skills all respond to visual artifact requests. | Users asking for a diagram/figure may need to know desired medium before routing is clear. |
| Frontend planning/build/QA chain lacks marketplace front door | `product-ux-planning`, `visual-direction`, `design-system-tokens`, `implementation-react-tailwind`, `responsive-accessibility-review`, `webapp-testing`, `research-product-frontend`, `frontend-reference-research`, `frontend-visual-systems`, `figma-design-to-code`, `motion-interaction` | No marketplace front door / broad-vs-specific | Frontend skills exist in profiles and direct skills, but none of six marketplace plugins exposes them. | A user-visible marketplace install path does not advertise frontend design/build capability. |
| Bioinformatics provider granularity | `bioinformatics-database-retrieval`, `biopython`, `pubmed-database`, `pysam`, `tiledbvcf`, `zarr-python`, `polars-bio`, `gtars`, `geniml`, `deeptools`, `arboreto`, `scanpy`, `scvi-tools`, `anndata`, `scvelo` | Aggregate versus named-library boundary | Bioinformatics aggregate exposes 10 core source skills, while many specialized active provider/tool skills remain direct/profile only. | Common bioinformatics tasks are covered, but specialized requests may require naming the specific library/platform. |
| Medical imaging aggregate coverage gap | `cardiac-mri`, `pydicom`, `medical-imaging-classical-features`, `medical-imaging-deep-learning`, `pathml`, `medical-imaging-terminology-measurement` | Aggregate coverage gap | Medical Imaging aggregate source list covers CMR/DICOM/features/deep learning/pathology source skills, while terminology-measurement is active but not in the plugin aggregate. | Terminology/measurement caveat requests may miss the marketplace medical-imaging front door. |
| Clinical medicine has no marketplace front door | `clinical-guideline-checking`, `medical-literature-evidence-review`, `clinical-reports`, `clinical-decision-support`, `treatment-plans`, `medical-safety-boundaries` | No front door / safety boundary risk | Clinical skills are active direct/profile skills but not in the six marketplace plugins. | Clinical evidence/report requests may route through generic research-writing or web search without clinical safety boundary skill. |
| Data-science library direct-name dependence | `polars`, `dask`, `vaex`, `geopandas`, `networkx`, `scikit-learn`, `shap`, `umap-learn`, `aeon`, `pymoo`, `sympy`, `matlab`, `exploratory-data-analysis` | Internal/library name dependent | Most data-science skills are active source skills in profiles or direct selectors; no marketplace data-science aggregate. | Users with natural analytics tasks may need to name the library or profile to discover the skill. |
| AI/ML framework exposure is partial | `pytorch-lightning`, `transformers`, `torch-geometric`, `langchain`, `llamaindex`, `opencv`, `fastai`, `timesfm-forecasting` | Plugin/profile exposure mismatch | Medical Imaging plugin exposes PyTorch Lightning and Transformers via ai-ml-imaging; other AI/ML framework skills remain direct/profile only. | General AI/ML implementation tasks may be incorrectly perceived as medical-imaging-only or not discoverable through marketplace. |
| Presentation and poster skills split by audience/format | `research-presentations`, `business-presentations`, `latex-posters`, `pptx-posters`, `paper-2-web` | Adjacent task boundary / no marketplace front door | Presentation profile exposes research/business decks; poster and paper-to-media skills are active but outside marketplace. | A request for slides/poster/web summary may require route choice by output format and audience. |
| OpenAI docs/system helpers depend on exact capability names | `openai-docs`, `mcp-builder`, `skill-creator`, `plugin-creator` | Internal-name dependent | Descriptions are concrete but direct/profile exposed; no user-facing marketplace front door groups OpenAI docs, MCP, skill, and plugin authoring together. | Users may ask for API help or a plugin/skill vaguely and miss the correct helper unless the runtime already has system routing. |

## Broad-Vs-Specific Risks
- **Research paper workflow overlap**: All describe manuscript drafting, claim-evidence, acceptance/reviewer checks, or broad-journal readiness under research-writing. Consequence: A broad manuscript request may be caught by several source skills unless the aggregate decides route precisely.
- **Visualization and diagram entry spread**: Diagram DSL, scientific figure, image generation, infographic, and canvas-design skills all respond to visual artifact requests. Consequence: Users asking for a diagram/figure may need to know desired medium before routing is clear.
- **Frontend planning/build/QA chain lacks marketplace front door**: Frontend skills exist in profiles and direct skills, but none of six marketplace plugins exposes them. Consequence: A user-visible marketplace install path does not advertise frontend design/build capability.
- **Bioinformatics provider granularity**: Bioinformatics aggregate exposes 10 core source skills, while many specialized active provider/tool skills remain direct/profile only. Consequence: Common bioinformatics tasks are covered, but specialized requests may require naming the specific library/platform.
- **Medical imaging aggregate coverage gap**: Medical Imaging aggregate source list covers CMR/DICOM/features/deep learning/pathology source skills, while terminology-measurement is active but not in the plugin aggregate. Consequence: Terminology/measurement caveat requests may miss the marketplace medical-imaging front door.
- **Clinical medicine has no marketplace front door**: Clinical skills are active direct/profile skills but not in the six marketplace plugins. Consequence: Clinical evidence/report requests may route through generic research-writing or web search without clinical safety boundary skill.
- **AI/ML framework exposure is partial**: Medical Imaging plugin exposes PyTorch Lightning and Transformers via ai-ml-imaging; other AI/ML framework skills remain direct/profile only. Consequence: General AI/ML implementation tasks may be incorrectly perceived as medical-imaging-only or not discoverable through marketplace.
- **Presentation and poster skills split by audience/format**: Presentation profile exposes research/business decks; poster and paper-to-media skills are active but outside marketplace. Consequence: A request for slides/poster/web summary may require route choice by output format and audience.

## Hard-To-Call Capabilities
- Skills with `NO_FRONT_DOOR` or `INTERNAL_NAME_DEPENDENT`: `58`.
- `INTERNAL_NAME_DEPENDENT` `timesfm-forecasting` (`skills/tools/ai-ml/timesfm-forecasting`): primary task AI/ML frameworks, experiments, and model engineering; exposure direct-only; evidence description “Zero-shot time series forecasting with Google's TimesFM foundation model. Use for any univariate time series (sales, sensors, energy, vitals, weather) without training a custom mod”.
- `INTERNAL_NAME_DEPENDENT` `torch-geometric` (`skills/tools/ai-ml/torch-geometric`): primary task AI/ML frameworks, experiments, and model engineering; exposure direct-only; evidence description “Graph Neural Networks (PyG). Node/graph classification, link prediction, GCN, GAT, GraphSAGE, heterogeneous graphs, molecular property prediction, for geometric deep learning.”.
- `INTERNAL_NAME_DEPENDENT` `arboreto` (`skills/domains/bioinformatics/omics-analysis/arboreto`): primary task Bioinformatics databases, single-cell, genomics I/O, and omics workflows; exposure direct-only; evidence description “Infer gene regulatory networks (GRNs) from gene expression data using scalable algorithms (GRNBoost2, GENIE3). Use when analyzing transcriptomics data (bulk RNA-seq, single-cell RN”.
- `INTERNAL_NAME_DEPENDENT` `dnanexus-integration` (`skills/domains/bioinformatics/platforms/dnanexus-integration`): primary task Bioinformatics databases, single-cell, genomics I/O, and omics workflows; exposure direct-only; evidence description “DNAnexus cloud genomics platform. Build apps/applets, manage data (upload/download), dxpy Python SDK, run workflows, FASTQ/BAM/VCF, for genomics pipeline development and execution.”.
- `INTERNAL_NAME_DEPENDENT` `flowio` (`skills/domains/bioinformatics/omics-analysis/flowio`): primary task Bioinformatics databases, single-cell, genomics I/O, and omics workflows; exposure direct-only; evidence description “Parse FCS (Flow Cytometry Standard) files v2.0-3.1. Extract events as NumPy arrays, read metadata/channels, convert to CSV/DataFrame, for flow cytometry data preprocessing.”.
- `INTERNAL_NAME_DEPENDENT` `gtars` (`skills/domains/bioinformatics/omics-analysis/gtars`): primary task Bioinformatics databases, single-cell, genomics I/O, and omics workflows; exposure direct-only; evidence description “High-performance toolkit for genomic interval analysis in Rust with Python bindings. Use when working with genomic regions, BED files, coverage tracks, overlap detection, tokenizat”.
- `INTERNAL_NAME_DEPENDENT` `lamindb` (`skills/domains/bioinformatics/platforms/lamindb`): primary task Bioinformatics databases, single-cell, genomics I/O, and omics workflows; exposure direct-only; evidence description “This skill should be used when working with LaminDB, an open-source data framework for biology that makes data queryable, traceable, reproducible, and FAIR.”.
- `INTERNAL_NAME_DEPENDENT` `latchbio-integration` (`skills/domains/bioinformatics/platforms/latchbio-integration`): primary task Bioinformatics databases, single-cell, genomics I/O, and omics workflows; exposure direct-only; evidence description “Latch platform for bioinformatics workflows. Build pipelines with Latch SDK, @workflow/@task decorators, deploy serverless workflows, LatchFile/LatchDir, Nextflow/Snakemake integra”.
- `INTERNAL_NAME_DEPENDENT` `zarr-python` (`skills/domains/bioinformatics/genomics-io/zarr-python`): primary task Bioinformatics databases, single-cell, genomics I/O, and omics workflows; exposure direct-only; evidence description “Chunked N-D arrays for cloud storage. Compressed arrays, parallel I/O, S3/GCS integration, NumPy/Dask/Xarray compatible, for large-scale scientific computing pipelines.”.
- `INTERNAL_NAME_DEPENDENT` `neurokit2` (`skills/domains/medicine-clinical/neurokit2`): primary task Clinical medicine evidence, reporting, and safety-bounded documents; exposure direct-only; evidence description “Comprehensive biosignal processing toolkit for analyzing physiological data including ECG, EEG, EDA, RSP, PPG, EMG, and EOG signals.”.
- `INTERNAL_NAME_DEPENDENT` `pyhealth` (`skills/domains/medicine-clinical/pyhealth`): primary task Clinical medicine evidence, reporting, and safety-bounded documents; exposure direct-only; evidence description “Comprehensive healthcare AI toolkit for developing, testing, and deploying machine learning models with clinical data.”.
- `INTERNAL_NAME_DEPENDENT` `scikit-survival` (`skills/domains/medicine-clinical/scikit-survival`): primary task Clinical medicine evidence, reporting, and safety-bounded documents; exposure direct-only; evidence description “Comprehensive toolkit for survival analysis and time-to-event modeling in Python using scikit-survival.”.
- `INTERNAL_NAME_DEPENDENT` `aeon` (`skills/tools/data-science/aeon`): primary task Data science, tabular analytics, geospatial, time series, and optimization; exposure direct-only; evidence description “This skill should be used for time series machine learning tasks including classification, regression, clustering, forecasting, anomaly detection, segmentation, and similarity sear”.
- `INTERNAL_NAME_DEPENDENT` `geopandas` (`skills/tools/data-science/geopandas`): primary task Data science, tabular analytics, geospatial, time series, and optimization; exposure direct-only; evidence description “Python library for working with geospatial vector data including shapefiles, GeoJSON, and GeoPackage files. Supports PostGIS databases, interactive maps, and integration with matpl”.
- `INTERNAL_NAME_DEPENDENT` `networkx` (`skills/tools/data-science/networkx`): primary task Data science, tabular analytics, geospatial, time series, and optimization; exposure direct-only; evidence description “Comprehensive toolkit for creating, analyzing, and visualizing complex networks and graphs in Python. Applicable to social networks, biological networks, transportation systems, ci”.
- `INTERNAL_NAME_DEPENDENT` `pymoo` (`skills/tools/data-science/pymoo`): primary task Data science, tabular analytics, geospatial, time series, and optimization; exposure direct-only; evidence description “Multi-objective optimization framework. NSGA-II, NSGA-III, MOEA/D, Pareto fronts, constraint handling, benchmarks (ZDT, DTLZ), for engineering design and optimization problems.”.
- `INTERNAL_NAME_DEPENDENT` `shap` (`skills/tools/data-science/shap`): primary task Data science, tabular analytics, geospatial, time series, and optimization; exposure direct-only; evidence description “Model interpretability and explainability using SHAP (SHapley Additive exPlanations). Works with tree-based models (XGBoost, LightGBM, Random Forest), deep learning (TensorFlow, Py”.
- `INTERNAL_NAME_DEPENDENT` `vaex` (`skills/tools/data-science/vaex`): primary task Data science, tabular analytics, geospatial, time series, and optimization; exposure direct-only; evidence description “Use this skill for processing and analyzing large tabular datasets (billions of rows) that exceed available RAM.”.
- `INTERNAL_NAME_DEPENDENT` `seaborn` (`skills/tools/visualization/seaborn`): primary task Figures, diagrams, visualization, and visual assets; exposure direct-only; evidence description “Statistical visualization with pandas integration. Use for quick exploration of distributions, relationships, and categorical comparisons with attractive defaults. Best for box plo”.
- `INTERNAL_NAME_DEPENDENT` `biorxiv-database` (`skills/science/discovery/biorxiv-database`): primary task Literature search, citations, and reference management; exposure direct-only; evidence description “Efficient database search tool for bioRxiv preprint server. Use this skill when searching for life sciences preprints by keywords, authors, date ranges, or categories, retrieving p”.
- `NO_FRONT_DOOR` `modal` (`skills/tools/ai-ml/modal`): primary task AI/ML frameworks, experiments, and model engineering; exposure direct-only; evidence description “Run Python code in the cloud with serverless containers, GPUs, and autoscaling. Use when deploying ML models, running batch processing jobs, scheduling compute-intensive tasks, or ”.
- `NO_FRONT_DOOR` `pufferlib` (`skills/tools/ai-ml/pufferlib`): primary task AI/ML frameworks, experiments, and model engineering; exposure direct-only; evidence description “High-performance reinforcement learning framework optimized for speed and scale. Use when you need fast parallel training, vectorized environments, multi-agent systems, or integrat”.
- `NO_FRONT_DOOR` `stable-baselines3` (`skills/tools/ai-ml/stable-baselines3`): primary task AI/ML frameworks, experiments, and model engineering; exposure direct-only; evidence description “Production-ready reinforcement learning algorithms (PPO, SAC, DQN, TD3, DDPG, A2C) with scikit-learn-like API. Use for standard RL experiments, quick prototyping, and well-document”.
- `NO_FRONT_DOOR` `esm` (`skills/domains/bioinformatics/biology-toolkits/esm`): primary task Bioinformatics databases, single-cell, genomics I/O, and omics workflows; exposure direct-only; evidence description “Comprehensive toolkit for protein language models including ESM3 (generative multimodal protein design across sequence, structure, and function) and ESM C (efficient protein embedd”.
- `NO_FRONT_DOOR` `etetoolkit` (`skills/domains/bioinformatics/biology-toolkits/etetoolkit`): primary task Bioinformatics databases, single-cell, genomics I/O, and omics workflows; exposure direct-only; evidence description “Phylogenetic tree toolkit (ETE). Tree manipulation (Newick/NHX), evolutionary event detection, orthology/paralogy, NCBI taxonomy, visualization (PDF/SVG), for phylogenomics.”.
- `NO_FRONT_DOOR` `geniml` (`skills/domains/bioinformatics/omics-analysis/geniml`): primary task Bioinformatics databases, single-cell, genomics I/O, and omics workflows; exposure direct-only; evidence description “This skill should be used when working with genomic interval data (BED files) for machine learning tasks. Applies to BED file collections, scATAC-seq data, chromatin accessibility ”.
- `NO_FRONT_DOOR` `neuropixels-analysis` (`skills/domains/bioinformatics/specialized/neuropixels-analysis`): primary task Bioinformatics databases, single-cell, genomics I/O, and omics workflows; exposure direct-only; evidence description “Neuropixels neural recording analysis. Load SpikeGLX/OpenEphys data, preprocess, motion correction, Kilosort4 spike sorting, quality metrics, Allen/IBL curation, AI-assisted visual”.
- `NO_FRONT_DOOR` `phylogenetics` (`skills/domains/bioinformatics/biology-toolkits/phylogenetics`): primary task Bioinformatics databases, single-cell, genomics I/O, and omics workflows; exposure direct-only; evidence description “Build and analyze phylogenetic trees using MAFFT (multiple alignment), IQ-TREE 2 (maximum likelihood), and FastTree (fast NJ/ML). Visualize with ETE3 or FigTree. For evolutionary a”.
- `NO_FRONT_DOOR` `clinical-decision-support` (`skills/domains/medicine-clinical/clinical-decision-support`): primary task Clinical medicine evidence, reporting, and safety-bounded documents; exposure direct-only; evidence description “Produce group-level clinical decision support, cohort evidence summaries, biomarker-stratified analyses, and guideline-style recommendation documents. Use for research, pharmaceuti”.
- `NO_FRONT_DOOR` `clinical-guideline-checking` (`skills/domains/medicine-clinical/clinical-guideline-checking`): primary task Clinical medicine evidence, reporting, and safety-bounded documents; exposure direct-only; evidence description “Check clinical guideline claims against current authoritative sources, jurisdictions, population boundaries, recommendation strength, and update dates before using them in medical ”.
- `NO_FRONT_DOOR` `clinical-reports` (`skills/domains/medicine-clinical/clinical-reports`): primary task Clinical medicine evidence, reporting, and safety-bounded documents; exposure direct-only; evidence description “Draft clinical case reports, diagnostic summaries, trial reports, SOAP/H&P/discharge-style documentation, and de-identified medical report templates with privacy, source, and guide”.
- `NO_FRONT_DOOR` `medical-literature-evidence-review` (`skills/domains/medicine-clinical/medical-literature-evidence-review`): primary task Clinical medicine evidence, reporting, and safety-bounded documents; exposure direct-only; evidence description “Review medical literature evidence with dated source notes, evidence hierarchy, population applicability, uncertainty, and safety boundaries. Use for medical evidence summaries, no”.
- `NO_FRONT_DOOR` `medical-safety-boundaries` (`skills/domains/medicine-clinical/medical-safety-boundaries`): primary task Clinical medicine evidence, reporting, and safety-bounded documents; exposure direct-only; evidence description “Apply safety boundaries for medical tasks: no autonomous diagnosis or prescribing, current-source verification, privacy checks, missing-data caveats, emergency escalation, and clin”.
- `NO_FRONT_DOOR` `treatment-plans` (`skills/domains/medicine-clinical/treatment-plans`): primary task Clinical medicine evidence, reporting, and safety-bounded documents; exposure direct-only; evidence description “Draft concise, clinician-reviewed treatment plan documents with goals, interventions, monitoring, and follow-up. Use only as documentation support with current-source verification,”.
- `NO_FRONT_DOOR` `matlab` (`skills/tools/data-science/matlab`): primary task Data science, tabular analytics, geospatial, time series, and optimization; exposure direct-only; evidence description “MATLAB and GNU Octave numerical computing for matrix operations, data analysis, visualization, and scientific computing. Also use when the user needs help with MATLAB syntax, funct”.
- `NO_FRONT_DOOR` `umap-learn` (`skills/tools/data-science/umap-learn`): primary task Data science, tabular analytics, geospatial, time series, and optimization; exposure direct-only; evidence description “UMAP dimensionality reduction. Fast nonlinear manifold learning for 2D/3D visualization, clustering preprocessing (HDBSCAN), supervised/parametric UMAP, for high-dimensional data.”.
- `NO_FRONT_DOOR` `open-notebook` (`skills/tools/documents-media/open-notebook`): primary task Document/media conversion, office files, PDFs, and web extraction; exposure direct-only; evidence description “Self-hosted, open-source alternative to Google NotebookLM for AI-powered research and document analysis. Supports 16+ AI providers including OpenAI, Anthropic, Google, Ollama, Groq”.
- `NO_FRONT_DOOR` `parallel-web` (`skills/tools/documents-media/parallel-web`): primary task Document/media conversion, office files, PDFs, and web extraction; exposure direct-only; evidence description “Web search and content extraction through Parallel Search API when this provider is requested or when research results must be saved with reproducible source files. Follow host bro”.
- `NO_FRONT_DOOR` `perplexity-search` (`skills/tools/documents-media/perplexity-search`): primary task Document/media conversion, office files, PDFs, and web extraction; exposure direct-only; evidence description “Perform AI-powered web searches with real-time information using Perplexity models via LiteLLM and OpenRouter.”.
- `NO_FRONT_DOOR` `canvas-design` (`skills/tools/visualization/canvas-design`): primary task Figures, diagrams, visualization, and visual assets; exposure direct-only; evidence description “Create beautiful visual art in .png and .pdf documents using design philosophy. You should use this skill when the user asks to create a poster, piece of art, design, or other stat”.
- `NO_FRONT_DOOR` `infographics` (`skills/tools/visualization/infographics`): primary task Figures, diagrams, visualization, and visual assets; exposure direct-only; evidence description “Create professional infographics from text, data, or research using configured research, image-generation, and quality-review providers. Produces polished, source-faithful visual e”.
- `NO_FRONT_DOOR` `publication-figure-palettes` (`skills/science/communication/publication-figure-palettes`): primary task Figures, diagrams, visualization, and visual assets; exposure direct-only; evidence description “Choose publication figure palettes, contextual Notion-derived style candidates, presets, and snippets with provenance and experimental gates.”.
- `NO_FRONT_DOOR` `scientific-figure-qa` (`skills/science/communication/scientific-figure-qa`): primary task Figures, diagrams, visualization, and visual assets; exposure direct-only; evidence description “Audit scientific figures for publication readiness, accessibility, grayscale readability, export quality, and venue visual constraints.”.
- `NO_FRONT_DOOR` `brand-creative-assets` (`skills/tools/frontend/brand-creative-assets`): primary task Frontend product design, implementation, and QA; exposure direct-only; evidence description “Create and review brand-related frontend assets: brand identity, visual guidelines, banners, hero visuals, slides, social images, icons, and marketing creative. Use for branded cam”.
- `NO_FRONT_DOOR` `get-available-resources` (`skills/tools/documents-media/get-available-resources`): primary task HPC resources and Slurm workflows; exposure direct-only; evidence description “This skill should be used at the start of any computationally intensive scientific task to detect and report available system resources (CPU cores, GPUs, memory, disk space).”.
- `NO_FRONT_DOOR` `bgpt-paper-search` (`skills/science/discovery/bgpt-paper-search`): primary task Literature search, citations, and reference management; exposure direct-only; evidence description “Search scientific papers and retrieve structured experimental data extracted from full-text studies via the BGPT MCP server. Returns 25+ fields per paper including methods, results”.
- `NO_FRONT_DOOR` `scholar-evaluation` (`skills/writing/research/scholar-evaluation`): primary task Manuscript, grant, review, and submission workflows; exposure direct-only; evidence description “Systematically evaluate scholarly work using the ScholarEval framework, providing structured assessment across research quality dimensions including problem formulation, methodolog”.
- `NO_FRONT_DOOR` `medical-imaging-terminology-measurement` (`skills/domains/medical-imaging/medical-imaging-terminology-measurement`): primary task Medical imaging, CMR, DICOM, pathology, and imaging ML; exposure direct-only; evidence description “Use medical imaging terminology and measurement conventions with source checks, modality-specific caveats, structured reporting boundaries, and uncertainty language.”.
- `NO_FRONT_DOOR` `ocr-kb` (`skills/writing/research/ocr-kb`): primary task OCR and scanned academic document recovery; exposure direct-only; evidence description “长文档 OCR、扫描 PDF 恢复、公式/表格/图注提取、断点续跑和 DOCX/Markdown 交付工作流。用于把 PDF 页面安全转成可编辑文本并做质量核查；内部处理模式可记录为 OCR，但用户不需要说旧 pipeline 名。”.
- `NO_FRONT_DOOR` `paper-2-web` (`skills/science/communication/paper-2-web`): primary task Presentations, posters, and paper-to-media communication; exposure direct-only; evidence description “This skill should be used when converting academic papers into promotional and presentation formats including interactive websites (Paper2Web), presentation videos (Paper2Video), a”.
- `NO_FRONT_DOOR` `pptx-posters` (`skills/science/communication/pptx-posters`): primary task Presentations, posters, and paper-to-media communication; exposure direct-only; evidence description “Create research posters using HTML/CSS that can be exported to PDF or PPTX. Use this skill ONLY when the user explicitly requests PowerPoint/PPTX poster format. For standard resear”.
- `NO_FRONT_DOOR` `imagegen` (`skills/core/codex-system/system-skills/imagegen`): primary task Raster image generation and editing; exposure direct-only; evidence description “Generate or edit raster images when the task benefits from AI-created bitmap visuals such as photos, illustrations, textures, sprites, mockups, or transparent-background cutouts.”.
- `NO_FRONT_DOOR` `consciousness-council` (`skills/science/ideation/consciousness-council`): primary task Research ideation, experiment planning, and strategic reasoning; exposure direct-only; evidence description “Run a multi-perspective Mind Council deliberation on any question, decision, or creative challenge. Also trigger when the user faces a dilemma, trade-off, or complex choice with no”.
- `NO_FRONT_DOOR` `hypogenic` (`skills/science/ideation/hypogenic`): primary task Research ideation, experiment planning, and strategic reasoning; exposure direct-only; evidence description “Automated LLM-driven hypothesis generation and testing on tabular datasets. Use when you want to systematically explore hypotheses about patterns in empirical data (e.g., deception”.
- `NO_FRONT_DOOR` `hypothesis-generation` (`skills/science/ideation/hypothesis-generation`): primary task Research ideation, experiment planning, and strategic reasoning; exposure direct-only; evidence description “Structured hypothesis formulation from observations. Use when you have experimental observations or data and need to formulate testable hypotheses with predictions, propose mechani”.
- `NO_FRONT_DOOR` `scientific-brainstorming` (`skills/science/ideation/scientific-brainstorming`): primary task Research ideation, experiment planning, and strategic reasoning; exposure direct-only; evidence description “Creative research ideation and exploration. Use for open-ended brainstorming sessions, exploring interdisciplinary connections, challenging assumptions, or identifying research gap”.
- `NO_FRONT_DOOR` `scientific-critical-thinking` (`skills/science/ideation/scientific-critical-thinking`): primary task Research ideation, experiment planning, and strategic reasoning; exposure direct-only; evidence description “Evaluate scientific claims and evidence quality. Use for assessing experimental design validity, identifying biases and confounders, applying evidence grading frameworks (GRADE, Co”.
- `NO_FRONT_DOOR` `what-if-oracle` (`skills/science/ideation/what-if-oracle`): primary task Research ideation, experiment planning, and strategic reasoning; exposure direct-only; evidence description “Run structured What-If scenario analysis with multi-branch possibility exploration. Also trigger when the user faces a fork-in-the-road decision, wants to stress-test an idea, or n”.

## Ambiguous Main Entrance Problems
- Skills with `AMBIGUOUS` entry status: `55`.
- **AI_Skills_Collection maintenance and skill intake**: 1 ambiguous skills: `skill-library-analysis`.
- **Bioinformatics databases, single-cell, genomics I/O, and omics workflows**: 2 ambiguous skills: `deeptools`, `scvelo`.
- **Build MCP servers**: 1 ambiguous skills: `mcp-builder`.
- **Create Codex plugins**: 1 ambiguous skills: `plugin-creator`.
- **Create or update Codex skills**: 1 ambiguous skills: `skill-creator`.
- **Data science, tabular analytics, geospatial, time series, and optimization**: 5 ambiguous skills: `dask`, `exploratory-data-analysis`, `polars`, `scikit-learn`, `sympy`.
- **Document/media conversion, office files, PDFs, and web extraction**: 5 ambiguous skills: `docx`, `markitdown`, `pdf`, `render-chinese-math-pdf`, `xlsx`.
- **Figures, diagrams, visualization, and visual assets**: 11 ambiguous skills: `scientific-schematics`, `scientific-visualization`, `d2-diagrams`, `drawio-diagrams`, `excalidraw-diagrams`, `generate-image`, `markdown-mermaid-writing`, `matplotlib`, `plantuml-diagrams`, `plotly`, `theme-factory`.
- **Frontend product design, implementation, and QA**: 11 ambiguous skills: `design-system-tokens`, `figma-design-to-code`, `frontend-reference-research`, `frontend-visual-systems`, `implementation-react-tailwind`, `motion-interaction`, `product-ux-planning`, `research-product-frontend`, `responsive-accessibility-review`, `visual-direction`, `webapp-testing`.
- **Literature search, citations, and reference management**: 4 ambiguous skills: `arxiv-database`, `openalex-database`, `pubmed-database`, `valyu-scientific-search`.
- **Manuscript, grant, review, and submission workflows**: 1 ambiguous skills: `research-grants`.
- **OCR and scanned academic document recovery**: 1 ambiguous skills: `academic-paper-writer-pro`.
- **OpenAI API/product documentation**: 1 ambiguous skills: `openai-docs`.
- **Presentations, posters, and paper-to-media communication**: 3 ambiguous skills: `latex-posters`, `business-presentations`, `research-presentations`.
- **Research ideation, experiment planning, and strategic reasoning**: 1 ambiguous skills: `experiment-execution`.
- **Skill installation and profile setup**: 1 ambiguous skills: `skill-installer`.
- **Statistical modeling, Bayesian analysis, and simulation**: 5 ambiguous skills: `bayesian-ppl-diagnostics`, `pymc`, `simpy`, `statistical-analysis`, `statsmodels`.

## Plugin Boundary Audit
| Plugin boundary | Current evidence | Issue type |
|---|---|---|
| `workflow-core` | Name and description align with single exposed workflow skill; broad enough to catch complex tasks. Boundary with general coding remains broad but intentional. | plugin-level boundary/coverage observation |
| `ai-skills-core` | Name may look like general AI-skill usage but description is repository infrastructure only; includes project installer and repository maintainer, not skill-library-analysis in marketplace. | plugin-level boundary/coverage observation |
| `writing-style` | Description matches three child skills; overlaps with research-writing for scientific prose in manuscripts and reports. | plugin-level boundary/coverage observation |
| `research-writing` | Description matches report/paper/literature aggregates; broad enough that peer review, grants, LaTeX authoring, and venue templates rely on aggregate routing. | plugin-level boundary/coverage observation |
| `bioinformatics` | Description names broad workflows; aggregate source list covers 10 core skills but specialized active bioinformatics tools/platforms are not all included. | plugin-level boundary/coverage observation |
| `medical-imaging` | Description names CMR/DICOM/segmentation/registration/features/ML; aggregate omits medical-imaging-terminology-measurement while exposing two AI/ML framework skills. | plugin-level boundary/coverage observation |
| `marketplace-global` | No top-level marketplace front door for frontend, data-science, visualization, documents/PDF/OCR, presentations, Bayesian/statistics, clinical medicine, HPC, or research ideation skills; these rely on profiles/direct selectors. | plugin-level boundary/coverage observation |

## Second-Phase Questions Worth Judging
- Whether marketplace-visible aggregate descriptions should be judged against natural requests rather than source package names.
- Whether manuscript/review/grant skills need a sharper routing contract inside the research-paper aggregate.
- Whether OCR/PDF/DOCX requests should enter through document conversion first or through academic document recovery when scanned evidence is central.
- Whether visualization/diagram/image tasks need medium-first routing tests to prevent image generation from swallowing technical diagrams.
- Whether profile-only domains such as frontend, data science/statistics, clinical medicine, and presentations are acceptable without marketplace front doors.
- Whether specialized bioinformatics and AI/ML framework skills should remain direct/provider-name dependent or be reachable from existing aggregates.

## Phase-Two Calling Test Corpus
### workflow-core
should-trigger:
- Implement this repo change with a source-of-truth check and tell me when verification passes.
- Audit this risky migration in phases and stop if the evidence does not support proceeding.
- Coordinate planner/executor/reviewer work for this release and give me completion gates.
should-not-trigger:
- Polish this paragraph so it sounds less stiff.
- Convert this DOCX to Markdown and keep the tables.

### ai-skills-core
should-trigger:
- Audit which skills in this collection are exposed through marketplace plugins.
- Install the research-main profile into this project and verify the installed SKILL.md files.
- Update the AI Skills registry and marketplace generated layer after source skill edits.
should-not-trigger:
- Build a React dashboard for these experiment results.
- Summarize this Nature paper and check the references.

### writing-style
should-trigger:
- Final-check this Chinese Markdown report so it reads naturally and preserves every fact.
- Make this scientific paragraph clearer without changing the claim strength.
- Fix version labels and headings in this report without dropping evidence.
should-not-trigger:
- Plan the whole manuscript structure from these results.
- Search for recent papers about diffusion MRI segmentation.

### research-writing
should-trigger:
- Write a repo-grounded experiment report from these logs and figures.
- Plan a manuscript claim-evidence workflow for these results.
- Check whether the references support every claim in this draft.
should-not-trigger:
- Fix keyboard accessibility bugs in this web app.
- Render this Chinese LaTeX file to PDF and debug fonts.

### bioinformatics
should-trigger:
- Analyze this single-cell RNA-seq dataset with QC, clustering, and marker genes.
- Look up gene and pathway information for these variants and summarize the evidence.
- Process BAM and VCF files for coverage and variant queries.
should-not-trigger:
- Review DICOM geometry and segmentation provenance.
- Design a PowerPoint pitch deck for investors.

### medical-imaging
should-trigger:
- Audit this CMR segmentation pipeline for ED/ES timing and LV/RV measurements.
- Read these DICOM files and preserve spacing/orientation metadata.
- Compare MONAI and nnU-Net baselines for medical image segmentation.
should-not-trigger:
- Run differential expression analysis on RNA-seq counts.
- Create a brand identity and hero image for this product.

### frontend-profile
should-trigger:
- Build a responsive React/Tailwind dashboard for these model comparisons.
- Review this app for mobile layout, keyboard access, and contrast issues.
- Turn these product requirements into navigation, states, and UI flows.
should-not-trigger:
- Check whether these citations exist and match the DOI metadata.
- Run a Slurm job array for this training sweep.

### document-pdf-ocr
should-trigger:
- Convert this scanned paper PDF into clean Markdown with tables and equations checked.
- Edit this DOCX report and preserve headings, citations, and tables.
- Render this Chinese math Markdown to PDF and verify fonts.
should-not-trigger:
- Infer a gene regulatory network from expression data.
- Plan a DICOM segmentation validation protocol.

### data-science-statistics
should-trigger:
- Choose and run an appropriate statistical model for this outcome and report effect sizes.
- Make this pandas workflow faster on a 50GB parquet dataset.
- Build a time-series forecasting baseline for these sensor readings.
should-not-trigger:
- Create an editable draw.io architecture diagram.
- Write a reviewer response letter for this manuscript.

### visualization-diagrams
should-trigger:
- Create an editable architecture diagram for this pipeline.
- Make publication-ready multi-panel plots with colorblind-safe palettes.
- Generate an infographic explaining these study results from the source text.
should-not-trigger:
- Install the medical-imaging project profile into this repo.
- Draft a clinician-reviewed treatment plan document.

### clinical-medicine
should-trigger:
- Check this clinical guideline claim against current authoritative sources.
- Draft a de-identified case report summary with privacy caveats.
- Summarize medical evidence for a cohort-level decision-support document.
should-not-trigger:
- Tune a PyTorch Lightning training loop.
- Convert an academic paper into a promotional website.

## Audit Guardrails Checked
- Active source coverage: `149/149`.
- Generated copies under `plugins/codex/plugins/`: counted only as `12` user-visible generated snapshots, not as source skills.
- Marketplace plugins audited: `6` named plugins plus one global marketplace coverage row.
- Conflict clusters recorded: `12`.
- No deletion, merge, description edit, profile edit, generation command, or plugin topology change was performed.
