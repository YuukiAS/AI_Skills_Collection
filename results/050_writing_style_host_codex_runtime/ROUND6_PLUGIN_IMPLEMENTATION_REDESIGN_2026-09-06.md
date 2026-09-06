# 050 Round 6 — plugin implementation redesign

Status: architecture diagnosis / proposal. This file does not revise `PLAN.md`, does not declare PASS, and does not authorize another implementation by itself.

## Product target

`writing-style` is a reusable language-realization layer: make already-fixed content easier to read without changing facts, formulas, evidence boundaries, uncertainty, comparison meaning, or scientific force. It must be usable downstream of research-writing, presentations, statistical-modeling, scientific-visualization, medical-imaging, bioinformatics, and ordinary technical writing.

The remaining 050 problem is not a missing blacklist or another reader score. The current heavy route is over-orchestrated and keeps too much source wording / QA vocabulary inside the generation context, so the model learns to preserve and explain abstractions instead of directly realizing the underlying scientific relation in natural Chinese.

## Verified problems in the current production design

### 1. Planning and realization are not truly separated

`scientific-rewrite` already creates a Document Map, Reader Plan and Meaning Cards, but the writer packet still contains the current original unit alongside the Meaning Card, terminology contract, English-span classification and selected templates. The writer therefore remains strongly anchored to source wording and QA categories.

The intended architecture should separate:

- semantic/content planning: what propositions, relations, caveats and exact identities must survive;
- language realization: how a reader should encounter those meanings in natural Chinese.

This is the classic NLG separation between content/discourse planning and surface realization.

### 2. Local unit rewriting is too dominant for document-level simplification

The current route rewrites local argument units with only a short previous rewritten tail and a short next-source preview. This is safer for local fidelity but encourages source-order/local prose and weakens global discourse realization.

Document-level simplification research repeatedly finds that iterating sentence/local simplification can damage discourse coherence, while document-level planning and access to broader context improve quality.

### 3. The seed library is too template-like and too `formal-technical`

The seed library contains many literal rewrite templates and most early seeds use `register=formal-technical`. The first definition seed itself teaches the pattern:

`术语A -> 它在这里指...`

That is close to the Round-5 failure mode: retain an abstraction and add a definition instead of replacing it with the concrete scientific question/relation when possible.

Production should consume operation labels, not sentence templates that the model can echo.

### 4. English-span classification is in the writer's planning path

The Reader Plan currently decides whether English spans are `exact_identity`, `useful_recognition`, or `ordinary_reasoning` before writing. This makes token preservation a first-class writing objective and can push the model toward bilingual labels and glossary-like repairs.

Exact identities belong to fidelity constraints. Ordinary wording decisions belong to realization. They should not be a central content-planning axis.

### 5. The fidelity layer is correct in purpose but too visible during realization

`writing-fidelity` correctly protects facts, formulas, numbers, citations, comparisons and uncertainty. But realization should receive the smallest necessary exact-identity set, not the entire preservation machinery. Exact inventories, token roles and QA ledgers must stay outside reader-facing prose and should not shape sentence skeletons.

### 6. Same-model self-review is useful for revision, not a reason to complicate generation

Self-refinement can improve a first draft, but it should be a bounded writer-side feedback/revise loop. It must not require a proliferation of reader-facing QA fields or deterministic natural-language proxies.

## External design evidence

The proposed architecture follows mature text-generation and simplification work rather than inventing a repo-local workflow:

1. Reiter & Dale's applied NLG architecture separates content determination, discourse/document planning, microplanning and linguistic realization.
2. Moryossef, Goldberg & Dagan (NAACL 2019), *Step-by-Step: Separating Planning from Realization in Neural Data-to-Text Generation*, reports better reliability/adequacy when faithful planning is separated from realization.
3. Cripwell, Legrand & Gardent (EACL 2023), *Document-Level Planning for Text Simplification*, shows document-level planning improves simplification over sentence-local approaches.
4. Cripwell, Legrand & Gardent (Findings ACL 2023), *Context-Aware Document Simplification*, shows local simplification without enough document context is a quality limitation.
5. Madaan et al. (NeurIPS 2023), *Self-Refine*, shows a bounded feedback -> refine loop can improve model outputs without another trained model; use this as a generation technique, not final authority.
6. Shulman et al. (Journal of Language and Social Psychology 2020) found jargon reduces processing fluency even when definitions are supplied. Therefore `term + parenthetical definition` is not sufficient plain-language realization.
7. CoEdIT (Findings EMNLP 2023) demonstrates that explicit edit operations/instructions can generalize well; this supports a small operation vocabulary rather than a large phrase/template library.

## Selected production architecture

Use a simpler three-stage semantic pipeline:

```text
SOURCE
  -> CONTENT CONTRACT + READER PLAN
  -> READER-FACING REALIZATION
  -> FIDELITY REPAIR
  -> FINAL
```

### Stage A — Content Contract + Reader Plan

Host Codex reads the full authorized source and produces a compact semantic representation. This representation owns content, not prose.

Required concepts:

- reader/audience and purpose;
- reader questions;
- propositions/claims;
- evidence and attribution;
- comparators/conditions;
- caveats/uncertainty/negative findings;
- causal/comparative/temporal relations between propositions;
- epistemic role where relevant;
- exact identities that truly require literal preservation;
- formula objects and what scientific question each formula answers;
- source-span coverage.

Do **not** put these into the Reader Plan as first-class planning fields:

- `useful_recognition` / `ordinary_reasoning` token classification;
- phrase-level translation decisions;
- literal rewrite templates;
- source sentences copied as `normalized meaning`.

The Reader Plan decides only:

- question/order;
- which propositions belong together;
- prose/list/table/formula-walkthrough information shape;
- where a concrete explanation or bridge is required.

For existing-document heavy rewrite, all source propositions remain owned somewhere. The plan may regroup/reorder but may not perform research-writing's content selection/deletion role.

### Stage B — Reader-facing realization

Generate prose from the Content Contract + Reader Plan as the primary instruction surface.

The original source is authority for later fidelity comparison, but source sentence wording should not be the realization template.

Preferred realization unit:

- whole document when it fits comfortably;
- otherwise one reader-question section / large discourse bundle at a time;
- avoid 8+ small local units followed by concatenation unless the source itself is naturally modular.

Every realization bundle receives the full compact Reader Plan and relevant neighboring bundle purposes, not just a 600-character tail/preview.

Use a small set of **operations**, not literal seed sentences:

1. `DIRECT_RELATION`: replace an avoidable abstract label with the actual comparison/action/condition/consequence.
2. `QUESTION_FIRST`: state the reader's concrete scientific question before technical terminology.
3. `METHOD_MENTAL_MODEL`: explain what each method observes/sends/optimizes before dense notation.
4. `FORMULA_WALKTHROUGH`: question/intuition -> exact formula -> symbol meaning -> implication/boundary.
5. `CLAIM_WITH_BOUNDARY`: bounded conclusion -> evidence -> nearby caveat.
6. `DECOMPRESS_NOUN_STACK`: convert stacked labels into subject + action + relation.
7. `PARALLEL_TO_STRUCTURE`: use list/table only when relations are genuinely parallel.
8. `REMOVE_INTERNAL_FRAME`: replace workflow/audit/status language with the scientific fact/relation it represents.

No operation contains project-specific words. No operation contains a canned final sentence.

For a term that is a real formal name, preserve it. For a technical concept that is not an external identity, realization decides whether the English term is useful; default is to express the scientific relation directly in Chinese. A definition does not by itself justify retaining the jargon.

### Stage C — Fidelity repair

Now compare the candidate against the source/content contract.

Deterministic helpers own only mechanically safe invariants:

- numbers/dates/units;
- formulas;
- citations;
- code/paths/config identifiers;
- exact externally identifying names;
- source proposition coverage/ownership;
- candidate/source hashes and privacy boundaries.

Host semantic fidelity audit owns:

- omitted/invented claims;
- changed comparator;
- reversed relation;
- changed uncertainty;
- moved caveat that changes interpretation;
- wrong attribution;
- conclusion-strength drift.

Repair only the affected reader bundle. Do not append exact-token/glossary inventories into the document.

## Bounded writer refinement

One writer-side refinement cycle is allowed:

```text
initial realization
-> writer feedback on concrete reader problems
-> one rewrite
```

Feedback should point to concrete transformations (e.g. `this paragraph requires decoding an abstraction before the comparison is stated`) rather than return generic PASS fields. This is a writing technique, not completion authority.

## What to remove or demote from the current heavy production route

1. Demote `english_span_classification` from Reader Plan/writer input to optional diagnostic evidence; it must not drive sentence construction.
2. Replace template-heavy `seed-transformations.json` consumption with a small operation catalog. Keep provenance/reference history, but production selection should return operation IDs + short semantic descriptions, not sentence templates.
3. Stop making `original unit + Meaning Card` equal co-primary drafting inputs. The content contract/plan is the realization input; source prose is primarily fidelity authority.
4. Replace many local `candidate_units` with larger reader-question bundles or whole-document realization when context permits.
5. Remove glossary/token-inventory appendices as a legal preservation strategy.
6. Keep `chinese_reader_pass` as writer-side diagnostic if useful, but it must not force the writer to construct prose around QA field categories.
7. Do not add deterministic Chinese-naturalness regexes, jargon counts, sentence-length thresholds or English-density targets.

## Mode design for a reusable future `clear-language` plugin

The generic plugin should expose three internal rewrite modes without creating three new plugins:

### LIGHT

Use for captions, labels, short conclusions, slide microcopy and local prose. No document plan. Domain semantics are already fixed by the caller.

### STANDARD

Use for several connected paragraphs / one section. Build a compact local content contract, realize the section, then fidelity-check.

### HEAVY

Use for a long existing document requiring structural rewrite. Full Content Contract + Reader Plan -> large-bundle/whole-document realization -> fidelity repair.

`research-writing` remains responsible for deciding what a new report/paper should contain. `presentations` remains responsible for deck sequence/page jobs. Statistical/visual/domain plugins own their scientific semantics and hand stable reader-facing jobs to this language layer.

## Implementation consequence for 050

The next implementation should simplify the heavy route rather than add more gates:

- keep `writing-fidelity` as the preservation layer;
- make `chinese-prose` the reusable realization contract;
- make `scientific-rewrite` a thin heavy-rewrite orchestrator around Content Contract -> Reader Plan -> realization -> fidelity repair;
- reduce `rewrite_support.py` to mechanical coverage/exact/privacy/dataflow support;
- reduce template-heavy seed influence;
- increase realization context from small local units to reader-question bundles / whole-document when feasible.

If this architecture cannot be implemented inside the existing 050 frozen authority without changing the frozen Plan, return to Planner. Do not disguise the change as another regex or reader-gate patch.
