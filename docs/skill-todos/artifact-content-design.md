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


## Preliminary concept sketch — Artifact Director / artifact-level editorial judgment

**Status of this section: PRELIMINARY ONLY.** This is an early working hypothesis captured before formal architecture research. It is deliberately non-binding: future Planner/Critic work may revise individual parts, choose a different ownership model, rename the capability, split it across existing domains, or reject and replace this concept entirely. Nothing below authorizes production implementation.

### Working problem statement

The recurring failure is broader than bad prose or bad rendering. A generated artifact may be factually correct and locally well written, yet still be a poor finished work because it contains too much: unnecessary explanation, labels, process narration, metadata, decorative structure, internal terminology, redundant guidance, or information that is true but irrelevant to the audience's immediate task.

The working hypothesis is that artifact production needs an editorial judgment layer whose first question is not "how should this be phrased?" but **"should this be visible at all?"**

A useful default principle to investigate is:

> Absence does not need justification; added visible content does.

Whitespace and silence are therefore valid design resources rather than empty regions that a model should automatically fill.

### Tentative boundary with Clear Writing

This concept is intended to complement, not compete with, Clear Writing.

A provisional distinction is:

- domain capabilities decide whether the underlying scientific, product, statistical, visual or interaction semantics are correct;
- this artifact-level layer decides what deserves visible space in the final artifact, how much emphasis it deserves, and whether it should instead be compressed, moved, visualized or omitted;
- Clear Writing decides how approved reader-facing language should be expressed clearly and naturally without changing established meaning;
- the artifact-specific producer still owns medium-specific realization, such as interaction design, slide composition, document structure, visualization encoding or image composition.

Under this model, a sentence can be factually correct and well written but still be removed because the audience does not need it. Clear Writing should not be expected to solve that problem by polishing the sentence.

### Tentative editorial actions

A minimal artifact-content decision vocabulary worth researching is:

- **KEEP** — visible content is necessary at its current level;
- **COMPRESS** — the idea matters, but the current granularity is excessive;
- **VISUALIZE** — the information matters, but prose is the wrong carrier;
- **DEMOTE** — useful supporting material belongs in a secondary location, appendix, detail view, note or lower visual hierarchy;
- **REMOVE** — the artifact is stronger without it.

Deletion should be a first-class outcome, not only a correction for factual error.

### Tentative pre-production questions

Before a reader-facing artifact is realized, the layer may need to answer a very small set of questions rather than create a large control schema:

1. Who is the artifact for?
2. What is the reader/viewer trying to understand, decide or do?
3. If only one to three things are remembered, what should they be?
4. Which candidate elements directly support that purpose?
5. Which elements are merely available in the source material but do not earn visible space?
6. What deserves primary, secondary or background attention?
7. Is any prose better represented as a visual object, control, table, figure or progressive disclosure?
8. Has the artifact reached the point where adding more would reduce clarity or restraint?

The desired behavior is the opposite of "the model knows this, therefore it should display this."

### Tentative cross-artifact role

The capability should be generic only where the judgment is genuinely generic. It should not become a universal artifact generator.

A provisional architecture to research is:

```text
user goal / domain truth
        |
        v
artifact-level editorial judgment
(audience, visible-content admission, restraint,
priority, density, medium choice)
        |
        +-----------------------+
        |                       |
        v                       v
artifact/domain producer    Clear Writing
(UI, presentations,         approved visible
documents, images,          wording and fidelity
visualization, Notion)
        |                       |
        +-----------+-----------+
                    |
                    v
             rendered artifact
                    |
                    v
artifact-level final review
(whole-work judgment on the real consumption object)
```

The artifact-specific producer keeps medium expertise. Examples:

- UI/product design owns navigation, components, interaction states and responsive behavior;
- presentations owns deck story, page jobs, slide archetypes, spatial hierarchy and rhythm;
- research-writing owns research-document argument/evidence structure;
- visualization owns encoding and graphical semantics;
- image generation owns image composition and rendering mechanics;
- Notion/project systems own database/view/workspace mechanics.

The shared layer should ask whether a visible element has earned its place, not reimplement those domains.

### Tentative post-render responsibility

A pre-render plan is insufficient. Many failures appear only after individually defensible elements are combined.

The final review should inspect the actual consumption object — rendered UI, slide deck, image, PDF, Notion page, chart, README or other finished artifact — and judge the work as a whole.

Questions worth testing include:

- Is the focal point obvious?
- Is there visible content whose removal would improve the artifact without harming the reader's task?
- Is internal process language leaking into the audience-facing work?
- Does the artifact explain beyond the point of usefulness?
- Is hierarchy being replaced by accumulation?
- Is empty space being respected?
- Would a mature human editor/designer regard any element as unnecessary, defensive, decorative or self-explanatory clutter?

This should be works-level judgment, not merely token scanning, schema validation or render-success checking.

### Tentative integration model

If this idea survives research, it should probably be consumed implicitly by artifact-producing capabilities rather than exposed as another step the user must remember to invoke manually.

Possible consumers include UI/product design, presentations, research authoring, visualization, image generation, documents, Notion/project-page generation and other reader-facing delivery paths.

The important unresolved question is whether the best implementation is:

1. one standalone shared skill;
2. a shared artifact-content contract invoked by several existing plugins;
3. a lightweight common decision kernel plus domain-specific adapters;
4. or no new top-level capability at all, with the useful principles distributed into existing artifact owners.

Formal architecture research should decide this rather than treating the present sketch as the answer.

### Open research questions

Before promotion, investigate at least:

- exact ownership boundaries versus `writing-style`, `research-writing`, `presentations`, product/UI, visualization, documents and image-generation paths;
- whether a shared content-admission decision can remain lightweight instead of becoming another workflow/state/schema layer;
- how to make restraint and deletion reliable without causing silent loss of required information;
- how to represent audience purpose and visible-content priority with minimal overhead;
- whether "whitespace is a valid output" can be operationalized without crude density thresholds;
- how final whole-artifact review should differ across UI, slides, documents, images, charts and workspace pages;
- how to ensure the capability is exercised in normal production paths rather than existing only as a written guideline;
- which mature editorial/design systems or existing repositories provide reusable concepts instead of rebuilding a lower-quality framework from scratch.

Again, this section is only a starting hypothesis. It may be substantially revised or fully replaced after overlap analysis and formal architecture review.
