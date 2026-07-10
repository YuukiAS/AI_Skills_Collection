# Integration Conflicts And Deferred Decisions

These items require explicit handling instead of silent merging.

| Topic | Source(s) | Decision |
|---|---|---|
| Plugin-only D2 workflow | `heathdutton/claude-d2-diagrams` | Record only; `d2-diagrams` distills the workflow without importing plugin structure. |
| Large registry clone | `majiayu000/claude-skill-registry` | Skipped because the repo is too large for this integration pass. |
| Software library, not skill | `Future-House/paper-qa` | Removed from scratch sources; do not integrate as a skill. |
| Multiple overlapping paper-writing workflows | PaperSpine, Nature-Paper-Skills, academic-research-skills, paper-writing-skill, Research-Paper-Writing-Skills | Distill into local workflow skills; do not keep competing active orchestrators. |
| External search service dependency | `yorkeccak/scientific-skills` | Add `valyu-scientific-search` as optional; fallback to existing database/search skills if `VALYU_API_KEY` is unavailable. |
| Remote rendering services | Kroki/PlantUML/Mermaid sources | Treat remote rendering as optional; do not send private diagrams to remote renderers without user approval. |
| Editable method figures | draw.io vs D2 vs PlantUML vs Excalidraw | Route by deliverable: draw.io for editable XML, D2 for source-controlled architecture/method diagrams, PlantUML for UML semantics, Excalidraw for ideation sketches. |
