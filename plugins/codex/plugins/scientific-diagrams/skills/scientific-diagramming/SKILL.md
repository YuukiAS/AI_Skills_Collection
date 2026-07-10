---
name: scientific-diagramming
description: Editable draw.io, D2, PlantUML, Excalidraw, Mermaid, scientific schematic, and publication figure workflows.
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

# scientific-diagramming

## Trigger Boundary

Editable draw.io, D2, PlantUML, Excalidraw, Mermaid, scientific schematic, and publication figure workflows.

Use this aggregate Codex App skill when the task matches one of the source workflows below.

## Source Workflows

- `drawio-diagrams`: Create, edit, validate, and export editable draw.io diagrams for architecture, methods, flowcharts, ER diagrams, and paper method figures. Use when the deliverable should remain editable as .drawio XML or embedded editable SVG/PDF. Reference: `references/source-skills/tools-visualization-drawio-diagrams/source-skill.md`
- `d2-diagrams`: Generate D2 source diagrams and rendered SVG/PNG outputs for architecture, infrastructure, method pipelines, system components, and codebase structure. Use when a text-based diagram DSL is preferable to manual drawing. Reference: `references/source-skills/tools-visualization-d2-diagrams/source-skill.md`
- `plantuml-diagrams`: Create PlantUML source and rendered diagrams for sequence, activity, class, component, deployment, state, and C4-style architecture diagrams. Use when UML semantics are more important than freeform drawing. Reference: `references/source-skills/tools-visualization-plantuml-diagrams/source-skill.md`
- `excalidraw-diagrams`: Create or revise Excalidraw-style sketch diagrams for early architecture, workflow, method, and concept ideation. Use when the user wants informal hand-drawn exploration rather than publication-final figures. Reference: `references/source-skills/tools-visualization-excalidraw-diagrams/source-skill.md`
- `markdown-mermaid-writing`: Comprehensive markdown and Mermaid diagram writing skill. Use when creating any scientific document, report, analysis, or visualization. Establishes text-based diagrams as the default documentation standard with full style guides (markdown + mermaid), 24 diagram type references, and 9 document templates. Reference: `references/source-skills/tools-visualization-markdown-mermaid-writing/source-skill.md`
- `scientific-visualization`: Meta-skill for publication-ready figures. Use when creating journal submission figures requiring multi-panel layouts, significance annotations, error bars, colorblind-safe palettes, and specific journal formatting (Nature, Science, Cell). Reference: `references/source-skills/science-communication-scientific-visualization/source-skill.md`
- `scientific-schematics`: Create publication-quality scientific diagrams using Nano Banana 2 AI with smart iterative refinement. Uses Gemini 3.1 Pro Preview for quality review. Reference: `references/source-skills/science-communication-scientific-schematics/source-skill.md`

## Workflow

1. Choose the source workflow whose trigger boundary best matches the user request.
2. Read that source workflow's `source-skill.md` before acting.
3. Load only the needed files under that workflow's copied references, scripts, assets, or evals.
4. Follow the source workflow unless the current project gives stricter instructions.
