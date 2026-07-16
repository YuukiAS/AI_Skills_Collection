---
name: scientific-visualization
description: Publication-ready figures, canonical scientific palettes, Matplotlib/Seaborn/Plotly snippets, schematics, posters, and venue figure QA for papers and top conferences.
status: active
provenance: generated
trusted: false
requires_network: true
writes_files: true
executes_code: true
secrets_needed:
  - OPENROUTER_API_KEY
last_reviewed: 2026-07-10
profile_tags:
recommended_scope: project
source_skills:
  - skills/science/communication/scientific-visualization
  - skills/tools/visualization/matplotlib
  - skills/tools/visualization/seaborn
  - skills/tools/visualization/plotly
  - skills/science/communication/scientific-schematics
  - skills/science/communication/latex-posters
  - skills/writing/research/venue-templates
icon_small: "assets/codex/app-skill-icons/aggregate.svg"
icon_large: "assets/codex/app-skill-icons/aggregate.svg"
default_prompt:
---

# scientific-visualization

## Trigger Boundary

Publication-ready figures, canonical scientific palettes, Matplotlib/Seaborn/Plotly snippets, schematics, posters, and venue figure QA for papers and top conferences.

Use this aggregate Codex App skill when the task matches one of the source workflows below.

## Source Workflows

- `scientific-visualization`: Meta-skill for publication-ready figures. Use when creating journal submission figures requiring multi-panel layouts, significance annotations, error bars, colorblind-safe palettes, and specific journal formatting (Nature, Science, Cell). Reference: `_src/publication/source.md`
- `matplotlib`: Low-level plotting library for full customization. Use when you need fine-grained control over every plot element, creating novel plot types, or integrating with specific scientific workflows. Reference: `_src/mpl/source.md`
- `seaborn`: Statistical visualization with pandas integration. Use for quick exploration of distributions, relationships, and categorical comparisons with attractive defaults. Best for box plots, violin plots, pair plots, heatmaps. Built on matplotlib. For interactive plots use plotly; for publication styling use scientific-visualization. Reference: `_src/seaborn/source.md`
- `plotly`: Interactive visualization library. Use when you need hover info, zoom, pan, or web-embeddable charts. Best for dashboards, exploratory analysis, and presentations. For static publication figures use matplotlib or scientific-visualization. Reference: `_src/plotly/source.md`
- `scientific-schematics`: Create publication-quality scientific diagrams using Nano Banana 2 AI with smart iterative refinement. Uses Gemini 3.1 Pro Preview for quality review. Reference: `_src/schematics/source.md`
- `latex-posters`: Create professional research posters in LaTeX using beamerposter, tikzposter, or baposter. Support for conference presentations, academic posters, and scientific communication. Includes layout design, color schemes, multi-column formats, figure integration, and poster-specific best practices for visual communication. Reference: `_src/posters/source.md`
- `venue-templates`: This skill should be used when preparing manuscripts for journal submission, conference papers, research posters, or grant proposals and need venue-specific formatting requirements and templates. Reference: `_src/venue/source.md`

## Plugin Workflow Notes

- For palette selection, first read `../../shared/palette/scientific-figure-palettes.json` and `../../shared/palette/ROUTING.md` when running inside this plugin.
- In the source repository, use `palette/scientific-figure-palettes.json` and the read-only CLI `python scripts/palette.py`.
- Use journal-inspired palettes only as non-official visual inspiration and preserve the disclaimer in figure guidance.
- Route manuscript-level figure policy to research-writing, but route figure color, plot code, and visual QA here.

## Workflow

1. Choose the source workflow whose trigger boundary best matches the user request.
2. Read that source workflow's `source.md` before acting.
3. Load only the needed files under that workflow's copied references, scripts, assets, or evals.
4. Follow the source workflow unless the current project gives stricter instructions.
