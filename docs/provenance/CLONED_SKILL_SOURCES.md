# Cloned Skill Sources

This file records the scratch clones used for integration. Keep this tracked before deleting any local scratch clone directory.

## Summary

- Recorded active scratch sources: 33
- Integration policy: distill and merge; do not bulk-copy upstream repositories.
- Plugin-only repositories are record-only unless converted to normal local skills.

## Sources

| Name | Remote | HEAD | Evidence | Decision | Target |
|---|---|---|---|---|---|
| `academic-research-skills` | https://github.com/Imbad0202/academic-research-skills.git | `ad0a7759cee9` | SKILL.md x4, plugin manifest, README skill/plugin wording | `merge` | paper-workflow-orchestrator; literature-review; peer-review; citation-verification |
| `citation-check-skill` | https://github.com/serenakeyitan/citation-check-skill.git | `b9deb7077099` | SKILL.md x1, README skill/plugin wording | `merge` | citation-verification |
| `claude-d2-diagrams` | https://github.com/heathdutton/claude-d2-diagrams.git | `2694f8d50e03` | plugin manifest | `record-only` | plugin-only; future d2-diagrams reference |
| `claude-drawio-skill` | https://github.com/little-hands/claude-drawio-skill.git | `23b638710f92` | SKILL.md x1, README skill/plugin wording | `merge` | drawio-diagrams |
| `claude-mermaid` | https://github.com/veelenga/claude-mermaid.git | `9c7edc930337` | SKILL.md x1, plugin manifest | `merge` | markdown-mermaid-writing |
| `claude-scholar` | https://github.com/Galaxy-Dawn/claude-scholar.git | `2f7766fd541a` | SKILL.md x45, plugin manifest, README skill/plugin wording | `merge-selected` | nature-manuscript-workflow; citation-verification; latex-paper-authoring; skill-library-analysis |
| `claude-scientific-writer` | https://github.com/K-Dense-AI/claude-scientific-writer.git | `44414bded0ea` | SKILL.md x84, .claude/skills x25, README skill/plugin wording | `merge-selected` | existing scientific/writing/database skills; mostly duplicate provenance source |
| `D2-Diagram-Skill` | https://github.com/RayanAhmed0/D2-Diagram-Skill.git | `5b30a5597f93` | SKILL.md x1, README skill/plugin wording | `merge` | d2-diagrams |
| `design-doc-mermaid` | https://github.com/SpillwaveSolutions/design-doc-mermaid.git | `e13f987306d5` | SKILL.md x1, README skill/plugin wording | `merge` | markdown-mermaid-writing; d2-diagrams |
| `drawio-mcp` | https://github.com/jgraph/drawio-mcp.git | `883b34c8aea7` | SKILL.md x1, README skill/plugin wording | `merge` | drawio-diagrams |
| `drawio-skill` | https://github.com/Agents365-ai/drawio-skill.git | `e740fb2898c0` | SKILL.md x1, README skill/plugin wording | `merge` | drawio-diagrams |
| `excalidraw-diagram-skill` | https://github.com/coleam00/excalidraw-diagram-skill.git | `8646fcc9f74f` | SKILL.md x1, README skill/plugin wording | `merge` | excalidraw-diagrams |
| `experiment-agent` | https://github.com/Imbad0202/experiment-agent.git | `e291e7dc7ca2` | SKILL.md x1, README skill/plugin wording | `merge` | experiment-execution |
| `graph-of-skills` | https://github.com/davidliuk/graph-of-skills.git | `69f2ab2f5e18` | SKILL.md x3, README skill/plugin wording | `merge` | skill-library-analysis |
| `graphify` | https://github.com/safishamsi/graphify.git | `9c27a5244822` | README skill/plugin wording | `record-only` | no SKILL.md; possible future knowledge-graph tooling |
| `kroki-editorial-diagrams` | https://github.com/LabinatorSolutions/kroki-editorial-diagrams.git | `e92889d89e72` | SKILL.md x1, README skill/plugin wording | `merge` | plantuml-diagrams; markdown-mermaid-writing; d2-diagrams |
| `latex-document-skill` | https://github.com/ndpvt-web/latex-document-skill.git | `75fd68be6588` | SKILL.md x1 | `merge-selected` | latex-paper-authoring; render-chinese-math-pdf |
| `latex-paper-skills` | https://github.com/yunshenwuchuxun/latex-paper-skills.git | `d0f106108cb0` | SKILL.md x8, README skill/plugin wording | `merge` | latex-paper-authoring |
| `literature-survey-skill` | https://github.com/SNL-UCSB/literature-survey-skill.git | `18475960526b` | SKILL.md x1, README skill/plugin wording | `merge` | literature-review |
| `markdown-viewer-skills` | https://github.com/markdown-viewer/skills.git | `a3afd455b3ad` | SKILL.md x15, README skill/plugin wording | `merge-selected` | markdown-mermaid-writing; plantuml-diagrams; d2-diagrams |
| `mermaid-skill` | https://github.com/Agents365-ai/mermaid-skill.git | `15d09cfff6cf` | SKILL.md x1, README skill/plugin wording | `merge` | markdown-mermaid-writing |
| `Nature-Paper-Skills` | https://github.com/Boom5426/Nature-Paper-Skills.git | `44cff42ac22a` | SKILL.md x18, README skill/plugin wording | `merge` | nature-manuscript-workflow; paper-workflow-orchestrator; citation-verification; peer-review |
| `nature-skills` | https://github.com/Yuan1z0825/nature-skills.git | `7fcb3f0d03bf` | SKILL.md x17, README skill/plugin wording | `merge` | nature-manuscript-workflow; scientific-visualization; citation-verification |
| `paper-writing-skill` | https://github.com/SNL-UCSB/paper-writing-skill.git | `8c303a75f99a` | SKILL.md x1, README skill/plugin wording | `merge` | scientific-writing; paper-workflow-orchestrator |
| `paperpipe` | https://github.com/hummat/paperpipe.git | `7b9ab07c11f6` | SKILL.md x7 | `merge-selected` | literature-review; citation-verification |
| `PaperSpine` | https://github.com/WUBING2023/PaperSpine.git | `d4529208cda7` | SKILL.md x5, plugin manifest, README skill/plugin wording | `merge` | paper-workflow-orchestrator |
| `plantuml` | https://github.com/SpillwaveSolutions/plantuml.git | `5580ff786015` | SKILL.md x1, README skill/plugin wording | `merge` | plantuml-diagrams |
| `plantuml-skill` | https://github.com/Agents365-ai/plantuml-skill.git | `07fe0ade1fc9` | SKILL.md x1, README skill/plugin wording | `merge` | plantuml-diagrams |
| `Research-Paper-Writing-Skills` | https://github.com/Master-cai/Research-Paper-Writing-Skills.git | `77e7c2c1ba06` | SKILL.md x1, README skill/plugin wording | `merge` | scientific-writing; paper-workflow-orchestrator |
| `scientific-agent-skills` | https://github.com/K-Dense-AI/scientific-agent-skills.git | `4d97e293dc6f` | SKILL.md x149, README skill/plugin wording | `merge-selected` | existing duplicated skills; provenance and selected deltas only |
| `scientific-skills` | https://github.com/yorkeccak/scientific-skills.git | `20b3d5037006` | SKILL.md x13, plugin manifest, README skill/plugin wording | `merge` | valyu-scientific-search |
| `Scientific-Writing-zh` | https://github.com/YuanZHAO321/Scientific-Writing-zh | `df89f35a16f8` | SKILL.md x1, README skill/plugin wording | `merge-selected` | chinese-prose; scientific-writing |
| `scipilot-figure-skill` | https://github.com/Haojae/scipilot-figure-skill.git | `43098ddb9e6a` | SKILL.md x1, README skill/plugin wording | `merge` | scientific-visualization; drawio-diagrams |

## Excluded Or Skipped

| Name | Remote | Decision | Reason |
|---|---|---|---|
| `paper-qa` | https://github.com/Future-House/paper-qa.git | `removed` | Software/RAG library, not a skill source for this integration. |
| `claude-skill-registry` | https://github.com/majiayu000/claude-skill-registry.git | `skipped` | Too large for scratch integration; user accepted skipping it. |

## Cleanup Rule

Do not remove local scratch clones until this file and `docs/provenance/cloned_skill_sources.json` are committed and the user explicitly approves scratch cleanup.
