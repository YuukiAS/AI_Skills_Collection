# writing-style — Long-Term TODO

Canonical maintenance inbox for the `writing-style` plugin.

## Incoming real-use feedback

### English scientific slide microcopy and full-deck prose remain cognitively heavy after a nominal final pass
status: NEW
source: TRACE / CAT-TRACE group-meeting deck v4–v8 reviews
evidence: `YuukiAS/TRACE` commits `e36cb5d93fc882ce158d88ac9201fe494b98b69a`, `1de90f2f26b3f787073ecedd7a4df41a985712eb`, `ef08bc25673fb33b639e523504676c0f333d93f4` and `26fd2ad0f042f0a8d7c7dc2154392e3f9460760d`. Earlier rounds exposed `Failure prevented`, mechanical `Example.` language, `What it measures`, `Focal method`, `Backbone` and `Rare fit`. The 33-page v8 deck still contains first-use domain terms that are expanded but not placed in enough context for a statistics audience (`COI`, `Metabarcoding`, `VicFlora`, `MGP`), source-note-like wording such as `That threshold is an implementation choice, not a CAT-TRACE theoretical constant.`, and dense table/slide language that is grammatically valid but unnecessarily hard to parse. The v8 English-final-pass record explicitly says the pass was limited to visible wording touched by v8, so untouched but still difficult language could survive.
problem: `scientific-prose` / presentation handoff needs to distinguish grammatical correctness from reader effort. A research slide should let a first-time expert reader understand what an unfamiliar term is, why it appears here, and what the sentence is asking them to retain. Expanding an acronym alone is insufficient when the term remains contextless. Final slide prose review also cannot be limited only to source lines modified in the current round: layout changes alter wrapping and old wording may still be cognitively heavy. The desired behavior is a full-deck audience-facing pass after scientific freeze: direct sentences, explicit local context for unfamiliar terms, natural action labels, short explanatory bridges where needed, and removal of internal/defensive/meta wording. This is not detector evasion and must not weaken scientific precision.
project-specific context: CAT-TRACE, TRACE, CORAL, VicFlora, COI, OTU, GBIF, MGP, catalogue/open-tail and the specific slide sentences belong to this project. Do not create a CAT-TRACE-specific banned-word list, and do not let writing-style alter equations, scientific claims, dataset values, theorem status, citations or slide layout.

## Open candidates

### Keep style cleanup downstream of scientific structure
status: CANDIDATE_GENERIC
source: real Presentation and advisor-report revisions
evidence: repeated user feedback on AI-like internal language, rhetorical templates and unnatural Chinese
target layer: writing
problem: style rules can accidentally take ownership of scientific structure or artifact mechanics.
candidate_action: preserve the boundary that research-reporting/presentation layers decide scientific structure while writing-style owns source-faithful reader-facing rewriting and final prose quality. For a supplied long scientific source that explicitly needs deep rewriting, use the 047 scientific-rewrite route rather than asking chinese-prose to invent scientific structure.
promotion_gate: only change this boundary if real routing evidence shows research-reporting and scientific-rewrite collide; do not duplicate research-reporting/presentation structural rules.

### 中文科研长文需要从 instruction-only 转为 meaning-first scientific rewrite
status: PROMOTE_NOW
source: 044 Deep Research production replay + TRACE v8→v9 real revision evidence + user-approved 047 architecture decision
evidence: `reviewed/044_writing_style_deep_research_chinese_replay` established that production `writing-style` could preserve many exact spans yet the complete private rewrite still retained reader-facing English abstractions such as `provenance`, `estimand`, `scientific gap`, `resource contract`, `state of the art`, `baseline`, `shared initialization`, `local drift` and related workflow labels as Chinese sentence/heading structure. This was an artifact-quality failure, not a missing-word-list problem. Separately, `YuukiAS/TRACE` v8→v9 improved language without a new writing-style runtime: the successful change was audience/purpose/meaning/role/first-use context/reader-takeaway guidance plus positive wording direction and a full-artifact language pass. Task 047 freezes additional public positive holdouts and should-not-fix controls before implementation.
target layer: writing
problem: current `chinese-prose` is overloaded as global Chinese final pass, rule catalogue and de-AI cleanup, while current `writing-fidelity` blanket-protects titles/headings/labels/structure alongside exact scientific invariants. The combination biases deep rewriting toward source surface structure. Repeatedly adding phrase rules, English scans or protected spans increases local constraints without teaching the model how to reconstruct a scientific argument in natural Chinese.
project-specific context: CARE/M&Ms/FedFisher/FedLPA, the specific 044 English expressions, CAT-TRACE/VicFlora/COI/MGP and page numbers are evidence examples only. They must not become permanent project-specific rewrite rules or blacklist entries.
candidate_action: implement bounded task `047_writing_style_scientific_rewrite_architecture` inside the existing `writing-style` plugin. Add an internal scientific-rewrite orchestrator using document/argument mapping, Meaning Cards, literal-vs-semantic fidelity, small positive transformation examples, bounded argument-unit rewriting, deterministic exact checks, semantic fidelity audit, targeted repair, Chinese language review and whole-document coherence review. Keep chinese-prose as positive-style/classification/language-review and writing-fidelity as exact/semantic preservation + post-rewrite audit. No new top-level plugin, no embedding/vector database, no model-vendor dependency, no fine-tuning.
promotion_gate: satisfied for bounded experimental implementation by the severe 044 production failure and explicit user request for a long-term cross-project capability. Task 047 still must pass its pre-frozen positive holdout and should-not-fix batch before any production release decision; 044 success alone cannot prove generalization.

## Do not do

- Do not create detector-evasion or generic humanizer behavior.
- Do not let style rewriting change equations, claims, labels, versions or citation meaning.
- Do not turn 044/TRACE vocabulary into a banned-word list.
- Do not use frozen 047 holdout outputs as seed examples in the same experiment.
