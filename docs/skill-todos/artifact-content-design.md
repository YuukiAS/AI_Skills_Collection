# artifact-content-design — Long-Term TODO

Future standalone capability for deciding what a reader-facing artifact should visibly contain before or alongside rendering.

## Open candidates

### Cross-artifact content restraint and whitespace
status: NEW
source: repeated user feedback across DII Notion, generated images and product/UI artifacts, 2026-10-27
evidence: `YuukiAS/AI_Research_Toolkit` branch `research/complex-system-showcase-20261026-r2-comparison`, `docs/history/notion/distributed-imaging-inference-version-history-2026-10-24-to-2026-10-27.md`
problem: Different artifact types repeatedly become over-authored even when the underlying content is correct. The model adds explanatory text, labels, guidance, metadata, sections or decorative structure after the user already has enough information to understand or act. The missing capability is not ordinary prose polishing or low-level rendering; it is deciding what should be visible at all, at what granularity, and when the artifact should stop explaining and leave space.
scope examples: Notion/project pages, UI, generated visual artifacts, documents and presentations where content selection and visual restraint matter before final rendering.
boundary: Clear Writing owns prose quality; product-ui-copy owns interface wording; research-writing owns research-document semantics; presentations and visualization own their domain composition; renderers own faithful layout. This future capability should not silently absorb those responsibilities.
project-specific context: DII page history and current Notion cleanup are evidence only. Do not encode DII sections, prompts or research workflow as generic behavior.
next research step: audit overlap with existing authoring, UI, presentation, visualization and rendering skills; determine whether this becomes one standalone skill, a shared pre-render contract, or a small capability consumed by artifact-producing skills. Do not implement production behavior until that ownership study is complete.
