# writing-style — Long-Term TODO

Canonical maintenance inbox for the `writing-style` plugin.

## Incoming real-use feedback

### English scientific slide microcopy and full-deck prose remain cognitively heavy after a nominal final pass
status: NEW
source: TRACE / CAT-TRACE group-meeting deck v4–v8 reviews
evidence: `YuukiAS/TRACE` commits `e36cb5d93fc882ce158d88ac9201fe494b98b69a`, `1de90f2f26b3f787073ecedd7a4df41a985712eb`, `ef08bc25673fb33b639e523504676c0f333d93f4` and `26fd2ad0f042f0a8d7c7dc2154392e3f9460760d`. Earlier rounds exposed `Failure prevented`, mechanical `Example.` language, `What it measures`, `Focal method`, `Backbone` and `Rare fit`. The 33-page v8 deck still contains first-use domain terms that are expanded but not placed in enough context for a statistics audience (`COI`, `Metabarcoding`, `VicFlora`, `MGP`), source-note-like wording such as `That threshold is an implementation choice, not a CAT-TRACE theoretical constant.`, and dense table/slide language that is grammatically valid but unnecessarily hard to parse. The v8 English-final-pass record explicitly says that it only reviewed visible wording touched in v8, so untouched but still difficult language could survive.
problem: `scientific-prose` / presentation handoff needs to distinguish grammatical correctness from reader effort. A research slide should let a first-time expert reader understand what an unfamiliar term is, why it appears here, and what the sentence is asking them to retain. Expanding an acronym alone is insufficient when the term remains contextless. Final slide prose review also cannot be limited only to source lines modified in the current round: layout changes alter wrapping and old wording may still be cognitively heavy. The desired behavior is a full-deck audience-facing pass after scientific freeze: direct sentences, explicit local context for unfamiliar terms, natural action labels, short explanatory bridges where needed, and removal of internal/defensive/meta wording. This is not detector evasion and must not weaken scientific precision.
project-specific context: CAT-TRACE, TRACE, CORAL, VicFlora, COI, OTU, GBIF, MGP, catalogue/open-tail and the specific slide sentences belong to this project. Do not create a CAT-TRACE-specific banned-word list, and do not let writing-style alter equations, scientific claims, dataset values, theorem status, citations or slide layout.

## Open candidates

### Audit `academic-humanizer` only for genuinely missing academic-writing capabilities
status: CANDIDATE_GENERIC
source: external resource discovery, 2026-09-02
evidence: `AIScientists-Dev/academic-humanizer` at commit `94b88b23703bed7df507acae7d6d5876209a0cdf` (`SKILL.md` v0.3.3), MIT. The inspected public skill focuses on English academic editing: AI-assisted paper/thesis/rebuttal/proposal cleanup, claim-evidence calibration, author-voice matching, and paper-vs-NSF/NIH proposal register. It has useful before/after academic examples, but much of its claim-strength and anti-template guidance overlaps the current `scientific-prose`; it also contains team-specific stylistic preferences such as broad AI-tell lists and a blanket em-dash removal rule.
target layer: writing
problem: this source may contain a few capabilities that are genuinely missing from the current `writing-style` / `research-writing` stack, especially author-reference voice matching and paper-vs-grant register separation. It is not part of the active 048 scientific-rewrite cutover and its AI-tell catalog must not become another phrase wall.
candidate_action: keep `academic-humanizer` as `REFERENCE_ONLY` during 048. After 048 closes, run a bounded source-vs-current-capability audit against `scientific-prose`, `writing-fidelity`, and relevant `research-writing` skills. Selectively port only a concrete capability that is absent, non-duplicative, license-compatible, and supported by a real task. Do not wholesale vendor the repo, create a new top-level humanizer plugin, copy broad banned-word/AI-tell lists, import author-specific house-style rules as universal rules, or duplicate claim-evidence behavior already implemented.
promotion_gate: promote only if the later audit identifies a specific missing production capability and a real replay shows that current skills fail without it. Otherwise record `REVIEWED_NOT_ADOPTED` / `REFERENCE_ONLY` and leave production behavior unchanged.

### Keep style cleanup downstream of scientific structure
status: CANDIDATE_GENERIC
source: real Presentation and advisor-report revisions
evidence: repeated user feedback on AI-like internal language, rhetorical templates and unnatural Chinese
target layer: writing
problem: style rules can accidentally take ownership of scientific structure or artifact mechanics.
candidate_action: preserve the boundary that research-reporting/presentation layers decide scientific structure while writing-style owns source-faithful reader-facing rewriting and final prose quality. For a supplied long scientific source that explicitly needs deep rewriting, use the 048 scientific-rewrite route rather than asking `chinese-prose` to invent scientific structure.
promotion_gate: only add new style rules when repeated across independent real artifacts; do not duplicate research-reporting/presentation structural rules.

### 中文科研长文需要从 instruction-only 转为 meaning-first scientific rewrite
status: PROMOTE_NOW
source: 044 Deep Research production replay + TRACE v8-v9 real revision evidence + user-approved 048 architecture decision
evidence: `reviewed/044_writing_style_deep_research_chinese_replay` established that production `writing-style` could preserve many exact spans yet the complete private rewrite still retained reader-facing English abstractions such as `provenance`, `estimand`, `scientific gap`, `resource contract`, `state of the art`, `baseline`, `shared initialization`, `local drift` and related workflow labels as Chinese sentence/heading structure. This was an artifact-quality failure, not a missing-word-list problem. Separately, `YuukiAS/TRACE` v8-v9 improved language without a new writing-style runtime: the successful change was audience/purpose/meaning/role/first-use context/reader-takeaway guidance plus positive wording direction and a full-artifact language pass. Task 048 freezes additional public positive regressions and should-not-fix controls before implementation.
target layer: writing
problem: current `chinese-prose` is overloaded as global Chinese final pass, rule catalogue and de-AI cleanup, while current `writing-fidelity` blanket-protects titles/headings/labels/structure alongside exact scientific invariants. The combination biases deep rewriting toward source surface structure. Repeatedly adding phrase rules, English scans or protected spans increases local constraints without teaching the model how to reconstruct a scientific argument in natural Chinese.
project-specific context: CARE/M&Ms/FedFisher/FedLPA, the specific 044 English expressions, CAT-TRACE/VicFlora/COI/MGP and page numbers are evidence examples only. They must not become permanent project-specific rewrite rules or blacklist entries.
candidate_action: implement bounded task `048_writing_style_product_cutover_and_readable_report` inside the existing `writing-style` plugin. Add an internal scientific-rewrite orchestrator using document/argument mapping, Meaning Cards, literal-vs-semantic fidelity, small positive transformation examples, bounded argument-unit rewriting, deterministic exact checks, semantic fidelity audit, targeted repair, Chinese language review and whole-document coherence review. Keep `chinese-prose` as positive-style/classification/language-review and `writing-fidelity` as exact/semantic preservation + post-rewrite audit. No new top-level plugin, no embedding/vector database, no model-vendor dependency, no fine-tuning.
promotion_gate: satisfied for bounded implementation by the severe 044 production failure, 047 architecture evidence, revised 048 Plan, and explicit user request for a long-term cross-project capability. Final `PROMOTED` status requires 048 technical gates, private full-report Text Review PASS, Scheduled Reviewer PASS, and user ACCEPT.

## Do not do

- Do not create detector-evasion or generic humanizer behavior.
- Do not let style rewriting change equations, claims, labels, versions or citation meaning.
- Do not turn 044/TRACE vocabulary into a banned-word list.
- Do not use 047 public regression outputs as seed examples for the same scientific-rewrite capability.
