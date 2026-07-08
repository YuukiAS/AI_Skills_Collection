---
name: frontend-visual-assets
description: Generate images and apply coherent visual themes for frontend surfaces and artifacts.
status: active
provenance: generated-codex-marketplace
trusted: false
requires_network: false
writes_files: true
executes_code: false
secrets_needed:
profile_tags:
recommended_scope: project
---

# frontend-visual-assets

## Trigger Boundary

Generate images and apply coherent visual themes for frontend surfaces and artifacts.

Use this aggregate Codex App skill when the task matches one of the source workflows below.

## Source Workflows

- `generate-image`: Generate or edit images using AI models (FLUX, Nano Banana 2). Use for general-purpose image generation including photos, illustrations, artwork, visual assets, concept art, and any image that is not a technical diagram or schematic. For flowcharts, circuits, pathways, and technical diagrams, use the scientific-schematics skill instead. Reference: `references/source-skills/tools-visualization-generate-image/source-skill.md`
- `theme-factory`: Toolkit for styling artifacts with a theme. These artifacts can be slides, docs, reportings, HTML landing pages, etc. There are 10 pre-set themes with colors/fonts that you can apply to any artifact that has been creating, or can generate a new theme on-the-fly. Reference: `references/source-skills/tools-visualization-theme-factory/source-skill.md`

## Workflow

1. Choose the source workflow whose trigger boundary best matches the user request.
2. Read that source workflow's `source-skill.md` before acting.
3. Load only the needed files under that workflow's copied references, scripts, assets, or evals.
4. Follow the source workflow unless the current project gives stricter instructions.
