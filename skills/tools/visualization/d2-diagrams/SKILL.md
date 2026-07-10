---
name: d2-diagrams
description: Generate D2 source diagrams and rendered SVG/PNG outputs for architecture, infrastructure, method pipelines, system components, and codebase structure. Use when a text-based diagram DSL is preferable to manual drawing.
status: active
provenance: adapted
trusted: false
requires_network: false
writes_files: true
executes_code: true
secrets_needed:
last_reviewed: 2026-07-09
profile_tags:
  - visualization
  - diagrams
recommended_scope: project
source_url: https://github.com/RayanAhmed0/D2-Diagram-Skill
source_commit: 5b30a5597f93876295b1ae9567c0e97e87543aa4
source_license: MIT
adaptation_notes: Distilled from D2-Diagram-Skill and heathdutton/claude-d2-diagrams plugin notes; plugin-only repo recorded but not imported.
metadata:
  skill-author: AI Skills Collection maintainers with recorded upstream sources
---
# D2 Diagrams

Use D2 for clean source-controlled diagrams. Keep the `.d2` file as the authoritative artifact.

## Workflow

1. Determine diagram type: architecture, infrastructure, sequence-like flow, ERD, state machine, or method pipeline.
2. Inspect source files or paper notes before diagramming. Do not infer architecture from names alone.
3. Draft `.d2` with stable node names and short labels.
4. Use clusters for subsystems, stages, datasets, or infrastructure boundaries.
5. Render to SVG/PNG only after the source is syntactically valid.
6. Report the `.d2` source path and rendered path.

## Style

- Prefer readable hierarchy over decorative complexity.
- Use color sparingly to encode ownership, stage, or risk.
- Keep long explanations in captions or Markdown, not node labels.
- For paper method figures, choose semantic stages and data transformations over implementation minutiae.

## Boundaries

- If D2 is not installed, create valid `.d2` source and state rendering was not run.
- Do not use D2 when the user explicitly needs editable draw.io output.
- Do not replace Mermaid in README contexts unless D2 gives a clear advantage.
