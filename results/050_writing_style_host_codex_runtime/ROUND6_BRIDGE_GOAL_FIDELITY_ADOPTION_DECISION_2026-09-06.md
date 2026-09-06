# 050 Round 6 — Bridge Goal Fidelity / anti-degradation adoption decision

Status: architecture diagnosis / Planner input. This file does not change production runtime, PLAN.md, workflow schema, or plugin identity.

## Why this note exists

Round 6 exposed a deeper defect than missing style rules. The installed writer can still produce awkward, abstraction-heavy Chinese while its own `chinese_reader_pass.json` reports `PASS` with no findings. Targeted tests also pass because the deterministic verifier checks artifact structure and self-declared decisions rather than independently judging reader quality.

The question is therefore no longer "which extra Chinese rule should be added?". It is whether the current development/evaluation authority model permits false positive completion.

## Bridge Kit evidence

Bridge Kit `0.7.0` Goal Fidelity explicitly separates:

- positive completion from supporting mechanics;
- non-substitutable semantics from weaker substitutes;
- evidence scope from claim scope;
- executor self-assessment from independent audit authority.

The Control role policy further separates Executor, Verifier, Planner and Critic. Executor cannot self-promote; Verifier owns mechanical/independent-oracle evidence but cannot invent qualitative product semantics; Planner/Critic own product/scientific/qualitative judgment. The CARE stress-test postmortem records that false PASS was prevented by exactly these separations, and specifically warns that verifier success, known-bad absence, state movement, or green CI are not positive completion by themselves.

This is directly relevant to 050.

## Current 050 mismatch with Goal Fidelity

The current scientific-rewrite heavy route mixes three authorities inside one host-Codex generation session:

1. writer generates candidate prose;
2. the same session authors semantic self-audit / Chinese reader PASS artifacts;
3. deterministic code validates that those self-authored artifacts are structurally valid.

That is acceptable as an internal self-repair mechanism, but it is not independent product-quality evidence.

Round 6 demonstrated the failure mode: poor prose can coexist with `language_naturalness=PASS`, `abstraction_burden=PASS`, `reader_effort=PASS`, and `findings=[]`.

Therefore `chinese_reader_pass` must not remain release/promotion authority merely because it is more detailed than a boolean PASS.

## External evaluation evidence

Recent LLM-as-a-judge research also argues against treating the writer model's own judgment as authoritative:

- self-preference bias has been measured in LLM judges, including GPT-family judges;
- 2026 work reports that self-preference persists even in rubric-based evaluation;
- position, style and other judgment biases remain relevant;
- multiple judges, blind comparison, order swapping and human calibration can mitigate bias, but do not make a single self-judge infallible.

Implication for 050: a fresh same-family Codex reader is useful, but its PASS should still be evidence rather than final authority.

## Proposed authority model

### A. Writer self-check becomes diagnostic / repair guidance

Keep Meaning Cards, Reader Plan, local semantic self-audit and Chinese self-check if they help generation.

But label them semantically as writer-owned self-check evidence. They cannot alone promote an implementation or candidate.

Do not delete useful internal reasoning stages merely because they are not independent.

### B. Deterministic verifier stays mechanical

Deterministic code should own only observable invariants such as:

- exact literals / formulas / citations / source coverage;
- candidate and artifact identity;
- no raw token/glossary leak when mechanically detectable;
- production-entrypoint binding;
- privacy and dataflow;
- reviewer artifact binding and freshness.

It must not decide natural Chinese, abstraction burden, explanation quality or reader effort by regex/score heuristics.

### C. Independent reader evidence is separate from writer outputs

For development/release evaluation, generate the candidate in one fresh production `plugin-replay` child, then review it in a separate fresh reader context that did not generate the candidate and does not receive writer self-audit, source-repair notes, rejection vocabulary or expected findings.

The reader receives only:

- candidate text;
- audience;
- frozen reader-quality rubric / Goal Fidelity quality bar.

Its output must contain concrete observable findings when returning REVISE; a PASS artifact must be bound to the candidate hash.

The reader artifact must live outside the writer stage package. The writer must not author or overwrite it.

### D. Calibrate the reader instead of trusting it blindly

A reader/judge must demonstrate competence on protected generic challenge cases before its judgment is used as promotion evidence.

Use a small cross-domain calibration set that the writer does not see, with human-approved preference/labels. It should include generic failure families such as:

- bilingual noun-stack reasoning;
- abstract-label-plus-definition that still has higher reader burden than direct restatement;
- QA/glossary/classification leak;
- duplicated/awkward Chinese relation;
- formula-first presentation lacking reason/intuition;
- false simplification that improves readability by dropping caveats.

The calibration set should be cross-domain (for example report prose, statistical conclusion/caption, figure annotation or slide microcopy) so 050 cannot overfit CARE wording.

Calibration failure means the reader's judgment is non-authoritative evidence for that run; it does not mean the writer candidate automatically fails for the same reason.

### E. Use pairwise human-anchored comparison for the known A/B/C stress case

The A/B/C sources are no longer holdouts. For this known stress case, the manually polished GPT rewrite is a human-approved readability floor/reference, not writer input.

The writer must never see the reference.

For evaluation, an independent reader may compare aligned candidate/reference passages blindly under a fixed rubric. To reduce judge-position bias, compare both presentation orders and require order-consistent judgment. Do not optimize candidate text against exact reference wording.

Separate fidelity checking remains source-aware; reader comparison is candidate/reference readability only.

The user remains final style authority.

### F. Do not require expensive independent review on every future small use

This architecture is primarily a plugin development/release gate.

Normal `writing-style` / future `clear-language` use for a caption or short conclusion should not automatically spawn multiple reviewer models.

For heavy source-faithful rewrites, a separate reader pass may be offered/used when the runtime supports it, but the plugin's basic quality should first be established by release-time protected evaluation.

## 050 Goal Fidelity mechanism gate

### Positive completion

The installed production plugin produces source-faithful Chinese scientific prose whose reader burden is close enough to the human-approved reference that remaining differences are mainly wording preference, not systematic abstraction decoding, bilingual scaffolding, QA leakage or unnatural literal relations.

### Non-substitutable semantics

Must preserve:

- original facts, formulas, numbers, citations, uncertainty, attribution, comparison logic and conclusion strength;
- actual installed production entry;
- no hand editing;
- Chinese reader-facing quality bar;
- private-source boundary.

### Supporting evidence only — never positive completion by itself

- unit tests;
- schema/dataflow PASS;
- exact-token inventory;
- `chinese_reader_pass` self-assessment;
- absence of banned strings;
- successful PDF/render;
- helper path success.

### Forbidden substitutes

- regex/readability scores as natural-language authority;
- writer-authored PASS promoted as independent review;
- glossary/token appendix used to preserve awkward English;
- reduced/synthetic candidate presented as the real A/B/C artifact;
- hand-edited smoke;
- reference text fed to the writer;
- dropping scientific content to improve readability.

### Required evidence

- real installed-plugin candidate;
- independent source-aware fidelity verification;
- separate candidate-only reader evidence bound to candidate identity;
- protected reader calibration result;
- for known A/B/C, blind pairwise comparison against the human-approved readability reference with swapped order;
- final human `STYLE_ACCEPT` / `STYLE_REJECT`.

## Consequence for current workflow

The existing 050 frozen Plan explicitly says to stop and return to Planner if the host-Codex architecture cannot produce materially better A/B/C without task-specific hacks. It also fixes the semantic self-audit in the same plugin session. The task has already used its one Plan revision.

Therefore the next step should not be another Executor patch round under the same interpretation.

Recommended workflow decision:

1. preserve the local Round-6 failed implementation/diff as diagnostic evidence;
2. do not push or promote it as 050 implementation success;
3. route 050 to Planner/human architecture decision;
4. if the independent-evaluation authority model above is accepted, implement it as a successor bounded task rather than silently mutating the exhausted 050 Plan;
5. reuse 050 A/B/C and human-approved reference as regression evidence, but add at least one protected cross-domain reader calibration/holdout set.

This is an architecture change in evaluation authority, not another style-rule increment.
