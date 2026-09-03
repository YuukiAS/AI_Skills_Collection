# writing-style — Long-Term TODO

Canonical maintenance inbox for the `writing-style` plugin.

## Incoming real-use feedback

### English scientific slide microcopy and full-deck prose remain cognitively heavy after a nominal final pass
status: NEW
source: TRACE / CAT-TRACE group-meeting deck v4–v8 reviews
evidence: `YuukiAS/TRACE` commits `e36cb5d93fc882ce158d88ac9201fe494b98b69a`, `1de90f2f26b3f787073ecedd7a4df41a985712eb`, `ef08bc25673fb33b639e523504676c0f333d93f4` and `26fd2ad0f042f0a8d7c7dc2154392e3f9460760d`. Earlier rounds exposed `Failure prevented`, mechanical `Example.` language, `What it measures`, `Focal method`, `Backbone` and `Rare fit`. The 33-page v8 deck still contains first-use domain terms that are expanded but not placed in enough context for a statistics audience (`COI`, `Metabarcoding`, `VicFlora`, `MGP`), source-note-like wording such as `That threshold is an implementation choice, not a CAT-TRACE theoretical constant.`, and dense table/slide language that is grammatically valid but unnecessarily hard to parse. The v8 English-final-pass record explicitly says that it only reviewed visible wording touched in v8, so untouched but still difficult language could survive.
problem: `scientific-prose` / presentation handoff needs to distinguish grammatical correctness from reader effort. A research slide should let a first-time expert reader understand what an unfamiliar term is, why it appears here, and what the sentence is asking them to retain. Expanding an acronym alone is insufficient when the term remains contextless. Final slide prose review also cannot be limited only to source lines modified in the current round: layout changes alter wrapping and old wording may still be cognitively heavy. The desired behavior is a full-deck audience-facing pass after scientific freeze: direct sentences, explicit local context for unfamiliar terms, natural action labels, short explanatory bridges where needed, and removal of internal/defensive/meta wording. This is not detector evasion and must not weaken scientific precision.
project-specific context: CAT-TRACE, TRACE, CORAL, VicFlora, COI, OTU, GBIF, MGP, catalogue/open-tail and the specific slide sentences belong to this project. Do not create a CAT-TRACE-specific banned-word list, and do not let writing-style alter equations, scientific claims, dataset values, theorem status, citations or slide layout.

## Active refinement

### Deep Research long-form rewrite: host Codex must own generation; external Terra is bounded final QA only
status: PROMOTE_NOW
active_task: `050_writing_style_host_codex_runtime`
source: 044/047/048/049 Deep Research rewrite series. 048 showed a one-shot production failure despite automated PASS; 049 then showed that making every semantic stage a paid Terra/OpenAI call was both the wrong plugin architecture and an unacceptable cost regression.
evidence: 048 implementation `928de2325d781ca630883d03e0f381092675b269`; 049 historical branch tip `19d7ba6f1a2a8752adfa4e7c11d3ebe9ed318070`; user rejected the first 049 A/B/C outputs as showing no perceptible improvement, and 049's paid per-stage pipeline later exhausted the API credit balance. 049 also produced useful engineering work around argument units, Meaning Cards, literal roles, reader-core/technical-trace separation, isolated replay and dataflow evidence, but that work is not Product PASS.
target layer: writing
problem: the remaining issue is architectural, not a missing vocabulary rule. `writing-style` is a Codex plugin and should guide the current host Codex model to perform document understanding, argument segmentation, Meaning Cards, rewriting, semantic self-audit, targeted repair and assembly in the normal task/session. Local deterministic helpers may verify exact literals and stage/evidence contracts, but must not fabricate semantic understanding or source-copy missing meaning. External Terra should not be a hidden generation dependency and should not be called for intermediate stages.
candidate_action: task 050 inherits useful 049 work but replaces the production owner model. Use isolated installed `writing-style` + current host Codex for generation/intermediate semantic work; use local deterministic exact/privacy/dataflow checks; keep the same fixed private A/B/C regression inputs; optionally run at most one combined candidate-only Terra reader QA for A/B/C and one final candidate-only Terra QA after style acceptance. Normal released plugin use keeps Terra/API off by default. Paid QA must be manual-only, hard-budgeted, and never triggered by ordinary push.
promotion_gate: 050 final cutover requires real installed host-Codex production behavior, fixed A/B/C user `STYLE_ACCEPT`, full private report user `ACCEPT`, and release/integration closure. Automated QA cannot override human rejection.

## Open candidates

### Audit `academic-humanizer` only for genuinely missing academic-writing capabilities
status: CANDIDATE_GENERIC
source: external resource discovery, 2026-09-02
evidence: `AIScientists-Dev/academic-humanizer` at commit `94b88b23703bed7df507acae7d6d5876209a0cdf` (`SKILL.md` v0.3.3), MIT. The inspected public skill focuses on English academic editing: AI-assisted paper/thesis/rebuttal/proposal cleanup, claim-evidence calibration, author-voice matching, and paper-vs-NSF/NIH proposal register. It has useful before/after academic examples, but much of its claim-strength and anti-template guidance overlaps the current `scientific-prose`; it also contains team-specific stylistic preferences such as broad AI-tell lists and a blanket em-dash removal rule.
target layer: writing
problem: this source may contain a few capabilities that are genuinely missing from the current `writing-style` / `research-writing` stack, especially author-reference voice matching and paper-vs-grant register separation. It should not be added to the active scientific-rewrite architecture merely because it is popular, and its AI-tell catalog must not become another phrase wall.
candidate_action: keep `academic-humanizer` as `REFERENCE_ONLY` during 050. Later run a bounded source-vs-current-capability audit against `scientific-prose`, `writing-fidelity`, and relevant `research-writing` skills. Selectively port only a concrete capability that is absent, non-duplicative, license-compatible, and supported by a real task.
promotion_gate: promote only if a later audit identifies a specific missing production capability and a real replay shows that current skills fail without it. Otherwise leave production behavior unchanged.

### Keep style cleanup downstream of scientific structure
status: CANDIDATE_GENERIC
source: real Presentation and advisor-report revisions
evidence: repeated user feedback on AI-like internal language, rhetorical templates and unnatural Chinese
target layer: writing
problem: style rules can accidentally take ownership of scientific structure or artifact mechanics.
candidate_action: preserve the current boundary: `writing-fidelity` protects facts, `scientific-prose` / `chinese-prose` polish reader-facing language after evidence/structure are stable.
promotion_gate: only add new style rules when repeated across independent real artifacts; do not duplicate research-reporting/presentation structural rules.

## Do not do

- Do not create detector-evasion or generic humanizer behavior.
- Do not let style rewriting change equations, claims, labels, versions or citation meaning.
- Do not treat a documented multistage workflow as implemented unless the normal production path actually executes it.
- Do not use automated readability PASS to override explicit human rejection of the real artifact.
- Do not make normal `writing-style` use depend on an external paid model when the current host Codex can perform the semantic/writing work itself.
- Do not let ordinary Git pushes trigger paid model QA.
