---
name: plantuml-diagrams
description: Create PlantUML source and rendered diagrams for sequence, activity, class, component, deployment, state, and C4-style architecture diagrams. Use when UML semantics are more important than freeform drawing.
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
source_url: https://github.com/Agents365-ai/plantuml-skill
source_commit: 07fe0ade1fc9a0a1e2ae8d64f95aa45cd8882284
source_license: MIT
adaptation_notes: Distilled from Agents365-ai/plantuml-skill, SpillwaveSolutions/plantuml, and Kroki multi-engine diagram guidance.
metadata:
  skill-author: AI Skills Collection maintainers with recorded upstream sources
---
# PlantUML Diagrams

Use PlantUML when a formal UML or C4-style representation is useful.

## Workflow

1. Select the diagram family before writing source.
2. Gather entities, relationships, lifecycle states, actors, or deployment nodes from real artifacts.
3. Write `.puml` as the source of truth.
4. Render locally if PlantUML is available; otherwise use Kroki only if network access is acceptable.
5. Keep generated images next to the `.puml` file and report both paths.

## Diagram Selection

- Sequence: API calls, protocol flow, review/approval workflows.
- Activity: pipelines, decision logic, manuscript or experiment process.
- Class/component: codebase architecture and interfaces.
- Deployment: infrastructure, runtime topology, services.
- C4: context/container/component documentation.

## Boundaries

- Do not force PlantUML for informal ideation; use Mermaid or Excalidraw instead.
- Do not send private architecture to remote Kroki without permission.
- Do not invent classes or services that are not present in source artifacts.
