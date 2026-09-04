# 050 round-2 source audit — why the plugin still underperforms the manual rewrite

This is a privacy-safe source audit. It records generic production-contract findings only; no private smoke plaintext is included.

## 1. Marketplace/plugin entrypoint bias

Current marketplace source describes `writing-style` as a writing-quality/polishing layer and says it operates without `research-structure decisions`.

For light polish this boundary is correct. For explicit heavy `scientific-rewrite`, the wording is too broad: the plugin must not change **scientific decisions**, but it must be allowed to change **reader-facing document structure** while preserving the same evidence graph.

The profile description is also framed as lightweight polishing. The installed entrypoint therefore does not strongly advertise the structural-rewrite capability that the successful manual baseline demonstrates.

Repair target: marketplace source + profile/default heavy-rewrite prompt, followed by normal generated-parity rebuild. Do not hand-edit generated plugin files as the source of truth.

## 2. `scientific-rewrite` workflow bias

The heavy route has Document Map, argument units, Meaning Cards, selected transformations, per-unit writer packets, exact/semantic audit and assembly. Those concepts are useful, but the contract still centers the `current argument unit` and a compact bounded packet.

That architecture can satisfy fidelity while still producing locally polished research-memo prose. The missing global object is a host-owned **Reader Plan** that decides the final explanatory order before prose generation.

A valid Reader Plan needs only observable behavior, not a new central workflow schema:

- reader questions / bounded section purpose;
- ordered source-span/proposition bundles, including non-contiguous spans;
- epistemic role where it matters;
- planned information form: prose, short list, table, formula walkthrough, trace;
- expansion/compression decision based on reader effort;
- proper-name vs ordinary-reasoning English classification.

Unit/bundle writing and final assembly must consume this plan.

## 3. Unit-local fidelity can become a structural bottleneck

A structural rewrite must preserve the document-level evidence graph, not force every original source chunk to retain every exact item in the same local candidate block.

If exact/semantic gates run against source-order units before a reader-oriented bundle is established, they can unintentionally prevent cross-section consolidation. The correct order is:

source spans/propositions
-> host Reader Plan / logical bundles
-> bundle-level rewrite + fidelity
-> global assembly
-> document-level fidelity

Inline-critical items must remain in meaningful reader context, but that context may be a new reader-oriented bundle rather than the original paragraph location.

Do not loosen factual fidelity; change the ownership/location unit used for checking.

## 4. Positive transformation library is too formal-memo oriented

The current seed library is small, which is good, but many examples use `formal-technical` register and dense template-like sentences. They teach correctness but not enough explanatory expansion or information-shape transformation.

Add only a small number of operation-centered generic transformations:

- scattered evidence -> one reader question;
- dense contrast -> two-step explanation;
- formula -> intuition / exact formula / symbol meaning / implication;
- flat method list -> decision question / mechanism groups;
- parallel values -> table/list;
- bounded conclusion -> nearby caveat;
- ordinary English scaffold -> natural Chinese relation.

Do not turn these into canned prose templates or project-specific phrases.

## 5. `chinese-prose` contains the right Chinese-first rule but also a potential long-form tension

The skill correctly says ordinary English should be translated when exact identity is not needed, and every remaining English span should be classified by semantic purpose.

Round 2 still contains substantial ordinary English reasoning language, so this rule is not functioning as a terminal production gate for the heavy route.

At the same time, `chinese-prose` prefers continuous paragraphs and warns against too many bullets/headings. That rule is useful against AI listicles, but for a long structural scientific rewrite it must not prevent a five-condition GO/STOP rule, parallel center counts, or a method family comparison from becoming a short list/table/subsection when that is genuinely easier to read.

Repair target: add a heavy-structural-rewrite exception based on reader effort, not a blanket preference for bullets.

## 6. `writing-fidelity` must remain conditional on task type

For polish/layout/source-faithful reconstruction, headings and order should remain protected.

For explicit heavy structural rewrite, reader-facing heading/paragraph/section order must not be protected by default. Preserve claim/evidence/condition/caveat/attribution/uncertainty identity instead.

Do not regress the round-1 fixes around `inline-critical`, relocatable trace, formula atomicity or raw token restoration.

## 7. Candidate-only review needs two dimensions

Answerability alone is insufficient. Round 2 shows a candidate can answer all frozen scientific questions and still impose too much decoding work.

The host final reader pass should separately judge:

- answerability;
- reader effort.

Reader-effort failure includes contextual, non-metric judgments such as:

- ordinary English carries the logical skeleton;
- a dense paragraph forces the reader to reconstruct parallel conditions;
- a formula lacks enough local intuition/implication;
- fact / literature / interpretation / proposal boundaries blur;
- the main conclusion is delayed by process/provenance framing;
- the output is shorter only because explanatory bridges were compressed away.

No score, detector or phrase blacklist is required.

## 8. Why direct GPT succeeds more easily

The manual rewrite has four freedoms that the production route must deliberately recover without sacrificing fidelity:

1. full-document global context and a single reader objective;
2. freedom to regroup non-contiguous evidence around the same question;
3. freedom to spend more words or change information form when that reduces cognitive load;
4. natural-language judgment over which English terms are identities and which are merely reasoning scaffolds.

The production plugin currently invests more structure in proving coverage than in explicitly optimizing those four reader freedoms. The repair should rebalance the contract, not remove the coverage checks.

## 9. Acceptance consequence

Round 3 should not be handed to the user if it is merely a shorter/cleaner memo. Before human handoff, production must demonstrate:

- host-owned Reader Plan consumed by drafting and assembly;
- non-contiguous grouping available;
- meaningful table/list/heading transformation when warranted;
- Chinese-first terminal pass actually executed;
- exact names preserved while ordinary reasoning is natural Chinese;
- fidelity checks bound to reader-oriented bundles/document, not positional source order;
- no raw token/source-copy fallback;
- same frozen A/B/C, one implementation identity, no paid model call.
