# 050 Style Rejection — root-cause analysis and bounded repair contract

Status: `STYLE_REJECT`

This note contains no private source or candidate plaintext. It records only generic failure modes observed from SMOKE-A/B/C, the manually rewritten readability baseline, and the current branch implementation.

## What the manual rewrite demonstrated

The successful manual rewrite did more than replace awkward words. Its reusable behavior was:

1. **Paragraph/document-level restructuring, not sentence-local paraphrase.** Material spread across several source sections was regrouped by the reader's question: what is known -> what it means -> what it does not prove -> what should happen next.
2. **Content fidelity is not source-order fidelity.** Claims, evidence, caveats, formulas, numbers and attribution remain, but paragraph order, headings, grouping and table organization may change when the user requested a structural rewrite.
3. **Evidence class becomes a reader-facing narrative boundary.** Project facts, literature facts, research interpretation, candidate methods and still-unverified items remain distinguishable without letting internal audit/workflow language dominate the prose.
4. **Formulas use `intuition/question -> formula -> symbol/meaning/implication`.** Exact math is preserved, but readers are told what the equation is for before and after seeing it.
5. **Method surveys are organized around one decision question.** A large method table is first grouped by the scientific distinction that matters for the decision, then detailed evidence is retained.
6. **Keep proper names; translate ordinary logic.** Canonical method/dataset/model names remain exact. Ordinary organizational/reasoning vocabulary should use natural Chinese when English adds no identifying precision.
7. **Conclusion first, evidence boundary nearby.** A cautious qualification should limit the conclusion, not bury the conclusion behind audit/provenance-style setup.

The existing `docs/plugin-todos/writing-style.md` already records these manual-rewrite lessons. This repair should promote the generic capabilities into production behavior rather than add project-specific banned words.

## Why the first 050 smoke is rejected

SMOKE-A/B/C are materially better organized than the rejected 048/049 outputs, but they still read like compressed research memos with English conceptual scaffolding. They also expose a more serious fidelity/runtime failure: exact items can be appended as a token list instead of being restored to their scientifically meaningful location.

The human style gate therefore rejects the first 050 smoke even if reader questions or mechanical checks can PASS.

## Verified implementation problems on the current remote 050 branch

### 1. `writing-fidelity` still protects structure too broadly

`skills/writing/core/writing-fidelity/SKILL.md` says protected content includes headings and section order and broadly prohibits reordering protected content. That is appropriate for polish/layout tasks but conflicts with an explicitly structural scientific rewrite. For `scientific-rewrite`, fidelity must preserve the content/evidence graph while allowing reader-facing headings, paragraph grouping and section order to change unless the user explicitly protected them.

### 2. `scientific-rewrite` still contains the superseded external-generation contract

The current remote `scientific-rewrite/SKILL.md` still lists OpenAI transform/review keys in `secrets_needed` and documents `run-staged` with an `openai-responses` driver. Normal 050 production must instead be host-Codex generation with no external API key. External Terra is optional final QA only.

### 3. Deterministic semantic fallback copies source excerpts

In `rewrite_support.py`, the deterministic `meaning_card()` populates `normalized_meaning` from `source_excerpt`. This is not semantic understanding and cannot be used as a production Meaning Card fallback in 050.

### 4. Project-specific phrase repair remains in generic runtime

`deterministic_reader_review()` and `apply_textual_repair()` contain hard-coded handling for terms such as `provenance`, `estimand`, `resource contract` and `controlled-drift axis`. This is exactly the phrase-list behavior 050 is meant to avoid. Generic style behavior must come from reader effort, role, and discourse structure rather than task vocabulary.

### 5. Exact-literal restoration can create token dumps

`restore_exact_literals()` repairs missing literals by appending a `保留原文精确项：...` list to `reader_core` or `technical_trace`. The unit and final assembly paths call this restoration after exact checks. This can mechanically PASS while producing a scientifically meaningless appendix or tail.

This must be removed from production completion semantics. A missing `inline-critical` item requires host-Codex contextual repair in the reader-facing argument. A missing `relocatable-trace` item requires a meaningful host-written trace entry, not a raw literal bag. Deterministic code may report missing items but must not write reader-facing repair text.

### 6. Formula/literal extraction is too token-oriented

The smoke evidence shows formulas and numbers can appear as fragmented exact items. Math must be treated as atomic protected spans where possible. Bare numbers extracted from inside an already protected formula/table/code span must not become independent restoration tokens that later get dumped into an appendix.

### 7. Assembly still favors source/unit order

The current staged helper builds `reader_core` by concatenating rewritten unit cores, with later assembly repair layered on top. The manual baseline shows that the needed operation is often a reader-order reorganization across source sections. The host-Codex argument-unit plan must be allowed to bind non-contiguous source spans and order units by the scientific decision path rather than source chronology, while preserving one-to-one source coverage.

## Bounded repair contract for 050

Do not change the selected 050 architecture. Repair it so the real production path behaves as follows:

```text
source
-> host-Codex document understanding
-> host-Codex reader-order / argument plan (may regroup non-contiguous source spans)
-> host-Codex Meaning Cards + evidence class + fidelity ledger
-> positive transformation selection
-> host-Codex unit rewrite from meaning + original
-> deterministic exact check only
-> host-Codex contextual repair when exact/semantic findings exist
-> host-Codex global assembly/reorganization
-> chinese-prose final reader pass
-> final candidate
```

Deterministic helpers must never generate semantic content or reader-facing fallback prose.

### Required production capabilities to promote

- Structural rewrite may reorder/merge paragraphs and reader-facing sections while preserving all source claims/evidence/caveats/attribution.
- Argument units may bind non-contiguous source spans when they answer the same reader question; every source span must still be covered exactly once or explicitly accounted for.
- Preserve evidence classes as semantics, not necessarily fixed labels.
- Canonical method/dataset/model/metric names stay exact; ordinary logic defaults to natural Chinese.
- Formula-bearing explanations follow intuition/question -> exact formula -> variable/implication.
- Comparative tables/sections may be regrouped around a decision-relevant mechanism or information type without dropping facts.
- `inline-critical` exact items must remain in contextual reader-facing prose/math/table; appendix presence alone cannot satisfy them.
- Only `relocatable-trace` may move to a technical appendix, and the appendix must be meaningful prose/table context, not a raw token list.
- Missing literals/semantic findings must route back to host Codex for targeted contextual repair. No deterministic source-copy or token-restoration fallback.
- Final assembly must be allowed to reorganize globally instead of merely concatenating locally polished source-order units.

## Regression tests that should fail before the repair and pass after it

1. A structural-rewrite request may change headings/paragraph order without fidelity failure while preserving source proposition coverage.
2. Non-contiguous source spans can form one bounded argument unit; duplicate/omitted spans fail validation.
3. Meaning Card validation rejects deterministic source-copy fallback as production semantic evidence.
4. Generic runtime contains no task-specific repair list for CARE/ODAL/FedFisher/provenance/estimand/etc.
5. `inline-critical` literal found only in `technical_trace` remains a failure.
6. No helper function may satisfy exact failure by appending a raw list of missing literals to reader-facing text.
7. Formula blocks are atomic protected spans; numbers inside them are not separately restored as token fragments.
8. A method-comparison fixture can be reorganized by decision axis while preserving all methods/claims/caveats.
9. Normal heavy `writing-style` production requires no OpenAI API key and does not call `/v1/responses`.
10. A/B/C are regenerated from one frozen implementation identity through the installed host-Codex route and remain at the human `STYLE_ACCEPT/STYLE_REJECT` gate.

## What not to do

- Do not add a CARE/ODAL/FedFisher word blacklist.
- Do not copy the manual rewritten report into the repository or use it as factual authority.
- Do not reactivate Terra/OpenAI per-stage generation.
- Do not lower fidelity by deleting caveats or conditions.
- Do not accept a mechanical exact PASS if the visible output contains a token-dump appendix.
- Do not open a new 051 task merely to avoid repairing 050; these failures are within the frozen 050 architecture and are suitable for one bounded generic `STYLE_REJECT` repair.
