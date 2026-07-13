---
name: scientific-visualization
description: Scientific plotting and visualization with Matplotlib and Plotly.
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
  - skills/tools/visualization/matplotlib
  - skills/tools/visualization/plotly
default_prompt:
---

# scientific-visualization

## Trigger Boundary

Scientific plotting and visualization with Matplotlib and Plotly.

Use this aggregate Codex App skill when the task matches one of the source workflows below.

## Source Workflows

- `matplotlib`: Low-level plotting library for full customization. Use when you need fine-grained control over every plot element, creating novel plot types, or integrating with specific scientific workflows. Reference: `_src/mpl/source.md`
- `plotly`: Interactive visualization library. Use when you need hover info, zoom, pan, or web-embeddable charts. Best for dashboards, exploratory analysis, and presentations. For static publication figures use matplotlib or scientific-visualization. Reference: `_src/plotly/source.md`

## Workflow

1. Choose the source workflow whose trigger boundary best matches the user request.
2. Read that source workflow's `source.md` before acting.
3. Load only the needed files under that workflow's copied references, scripts, assets, or evals.
4. Follow the source workflow unless the current project gives stricter instructions.
