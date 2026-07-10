---
name: drawio-diagrams
description: Create, edit, validate, and export editable draw.io diagrams for architecture, methods, flowcharts, ER diagrams, and paper method figures. Use when the deliverable should remain editable as .drawio XML or embedded editable SVG/PDF.
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
source_url: https://github.com/jgraph/drawio-mcp
source_commit: 883b34c8aea72ca7bc978a281061c411bc3e3745
source_license: Apache-2.0
adaptation_notes: Distilled from drawio-mcp, Agents365-ai/drawio-skill, and little-hands/claude-drawio-skill.
metadata:
  skill-author: AI Skills Collection maintainers with recorded upstream sources
---
# draw.io Diagrams

Use this when editability matters. The canonical source should be `.drawio`, not only a rendered PNG.

## Workflow

1. Clarify diagram type, audience, paper/report context, and required output formats.
2. Create or edit `.drawio` XML as the source artifact.
3. Keep labels short and domain-specific.
4. Use stable layout: left-to-right for pipelines, top-to-bottom for stages, grouped regions for modules.
5. If exporting is requested, prefer SVG or PDF with embedded draw.io XML when supported so the figure remains editable.
6. Validate by reopening or inspecting XML structure when possible.

## Output Policy

- For manuscripts: deliver `.drawio` plus SVG/PDF export.
- For README/docs: deliver `.drawio` plus SVG or PNG.
- For early brainstorming: consider `excalidraw-diagrams` instead.
- For DSL-native architecture diagrams: consider `d2-diagrams`, `plantuml-diagrams`, or `markdown-mermaid-writing`.

## Boundaries

- Do not make only a screenshot when the user asked for editable diagrams.
- Do not rely on draw.io desktop CLI unless it is installed or the user accepts that dependency.
- Do not embed hidden assumptions in diagram labels; use notes or captions for uncertainty.
