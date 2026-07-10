---
name: excalidraw-diagrams
description: Create or revise Excalidraw-style sketch diagrams for early architecture, workflow, method, and concept ideation. Use when the user wants informal hand-drawn exploration rather than publication-final figures.
status: active
provenance: external-adapted
source_repo_url: https://github.com/coleam00/excalidraw-diagram-skill
source_path: .
source_ref: 8646fcc9f74f38539c6cdb4c969723336a96ddcd
source_imported_at: 2026-07-09
source_license: MIT
source_note: Distilled from excalidraw-diagram-skill and kept separate from publication-final diagram workflows.
trusted: false
requires_network: false
writes_files: true
executes_code: false
secrets_needed:
last_reviewed: 2026-07-09
profile_tags:
  - visualization
  - diagrams
recommended_scope: project
metadata:
  skill-author: AI Skills Collection maintainers with recorded upstream sources
---
# Excalidraw Diagrams

Use this for fast visual thinking. Do not use it as the final route for journal figures unless the user explicitly wants hand-drawn style.

## Workflow

1. Identify the core idea, audience, and stage of work.
2. Sketch the smallest useful diagram: actors, stages, flows, dependencies, or uncertainties.
3. Keep text sparse and readable.
4. Use visual grouping to show alternatives, open questions, and next decisions.
5. Export or save the editable Excalidraw artifact when possible.

## Best Uses

- Early system architecture.
- Research plan brainstorming.
- Method alternatives before committing to a formal figure.
- Meeting explanation diagrams.
- Visual comparison of competing workflows.

## Boundaries

- For editable method figures, prefer `drawio-diagrams`.
- For source-controlled architecture diagrams, prefer `d2-diagrams` or `plantuml-diagrams`.
- For README flowcharts, prefer `markdown-mermaid-writing`.
