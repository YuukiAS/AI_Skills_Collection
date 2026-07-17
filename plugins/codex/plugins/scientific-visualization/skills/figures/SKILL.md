---
name: publication-figures
description: Publication figure orchestration with Matplotlib, Seaborn, Plotly, canonical palettes, and export-ready figure layout.
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
  - skills/science/communication/scientific-visualization
  - skills/tools/visualization/matplotlib
  - skills/tools/visualization/seaborn
  - skills/tools/visualization/plotly
icon_small: "assets/codex/app-skill-icons/aggregate.svg"
icon_large: "assets/codex/app-skill-icons/aggregate.svg"
default_prompt:
---

# publication-figures

## Trigger Boundary

Publication figure orchestration with Matplotlib, Seaborn, Plotly, canonical palettes, and export-ready figure layout.

Use this aggregate Codex App skill when the task matches one of the source workflows below.

## Source Workflows

- `scientific-visualization`: Meta-skill for publication-ready figures. Use when creating journal submission figures requiring multi-panel layouts, significance annotations, error bars, colorblind-safe palettes, and specific journal formatting (Nature, Science, Cell). Reference: `_src/publication/source.md`
- `matplotlib`: Low-level plotting library for full customization. Use when you need fine-grained control over every plot element, creating novel plot types, or integrating with specific scientific workflows. Reference: `_src/mpl/source.md`
- `seaborn`: Statistical visualization with pandas integration. Use for quick exploration of distributions, relationships, and categorical comparisons with attractive defaults. Best for box plots, violin plots, pair plots, heatmaps. Built on matplotlib. For interactive plots use plotly; for publication styling use scientific-visualization. Reference: `_src/seaborn/source.md`
- `plotly`: Interactive visualization library. Use when you need hover info, zoom, pan, or web-embeddable charts. Best for dashboards, exploratory analysis, and presentations. For static publication figures use matplotlib or scientific-visualization. Reference: `_src/plotly/source.md`

## Plugin Workflow Notes

- For palette selection, use `publication-figure-palettes` or `../../shared/scripts/palette.py` before choosing raw colors.
- For figure readiness checks, use `scientific-figure-qa` after plotting or layout decisions.
- Venue templates belong to research-writing; this plugin owns figure color, plotting code, visual examples, schematics, and posters.

## Workflow

1. Choose the source workflow whose trigger boundary best matches the user request.
2. Read that source workflow's `source.md` before acting.
3. Load only the needed files under that workflow's copied references, scripts, assets, or evals.
4. Follow the source workflow unless the current project gives stricter instructions.
