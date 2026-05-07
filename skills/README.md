# Skills Directory

This directory is organized by reuse scope and workflow importance. Keep
callable skills under one of the top-level buckets below.

## Top-Level Buckets

- `reusable/`: Cross-project skills that are useful on most servers and repos.
- `research/`: High-value research workflow skills for writing, discovery, ideation, and communication.
- `domain/`: Domain-specific skills that are reusable within a field but not universally needed.
- `project/`: Repo-specific or project-specific skills that depend on local codebase conventions.
- `system/`: Agent, Codex, plugin, MCP, and skill-management skills.

## Current Groups

### Reusable

- `reusable/frontend/`: Frontend design, implementation, accessibility, motion, Figma, and web app testing.
- `reusable/documents-media/`: PDF, Word, PowerPoint, spreadsheet, conversion, notebook, and web utilities.
- `reusable/visualization/`: Plotting, image generation, slides, infographics, canvas design, themes, and diagrams.
- `reusable/data-science/`: General analysis, modeling, graph, tabular, geospatial, and optimization skills.
- `reusable/ai-ml/`: Machine learning, deep learning, forecasting, reinforcement learning, and model tooling.
- `reusable/notion/`: Notion workspace automation, task planning, search, database, and page skills.
- `reusable/cursor/`: Cursor rule, skill, subagent, migration, and settings helpers.

### Research

- `research/writing/`: Manuscript drafting, literature review, peer review, grants, venue templates, and academic paper pipelines.
- `research/discovery/`: Academic search, citation management, paper databases, Zotero, and research lookup skills.
- `research/ideation/`: Hypothesis generation, scientific brainstorming, critical thinking, and structured scenario exploration.
- `research/communication/`: Research posters, scientific slides, schematics, paper-to-web, and publication-ready communication assets.

### Domain

- `domain/bayesian/`: Bayesian diagnostics and probabilistic programming support.
- `domain/bioinformatics/`: Genomics, transcriptomics, single-cell, protein, pathway, and biological database skills.
- `domain/medical-imaging/`: General medical imaging, DICOM, radiomics, MONAI/deep learning, IDC, and pathology imaging skills.
- `domain/medicine-clinical/`: Clinical reports, treatment planning, decision support, clinical trials, and medical ML skills.

### Project

- `project/CMR/`: CardiacNexus-specific docs, phenotype contracts, pipeline refactors, strain, and registration skills.

### System

- `system/codex-system/`: Codex/OpenAI system skills plus MCP and skill-authoring helpers.

## Layout Convention

Each skill lives in its own directory with a `SKILL.md`. Optional `assets/`,
`references/`, `scripts/`, templates, and other bundles sit beside that file.

Use `../bundles/` to define deployable subsets for each server or workflow.
