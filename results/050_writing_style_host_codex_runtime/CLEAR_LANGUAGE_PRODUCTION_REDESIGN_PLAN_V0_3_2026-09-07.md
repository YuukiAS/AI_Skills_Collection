# Clear-language production redesign plan

Plan version: **0.3**

Status: **DRAFT / READY FOR CRITIC REVIEW / NOT EXECUTION AUTHORIZATION**

Supersedes for planning purposes: `CLEAR_LANGUAGE_PRODUCTION_REDESIGN_PLAN_V0_2_2026-09-06.md`.

The earlier v0.1/v0.2 files remain design history. Do not overwrite them.

This document does **not** modify the frozen 050 Reviewed Handoff `PLAN.md`, does not authorize Codex implementation, does not rename `writing-style`, and does not declare 050 PASS.

---

## 0. Why v0.3 exists

The v0.2 architecture direction survived Critic review: the selected four-component model, Meaning Map, Reader Plan, `chinese-prose` realization core, source-aware fidelity audit, targeted repair, and re-verification remain the intended direction.

The Critic identified five execution-readiness gaps and recommended one additional generalization gate. Those findings are largely correct. v0.3 closes them, with one important correction based on current repository state:

> The current 050 task cannot receive another Planner revision. `CURRENT.json` is already `plan_revision=1` with `max_plan_revisions=1` and is in `AWAIT_HUMAN_DECISION`. Therefore an approved v0.3 architecture must **not** be smuggled into the exhausted 050 frozen Plan. The implementation must move to a successor Reviewed Handoff task with a fresh current Plan contract. The old 050 `PLAN.md` and replay task remain historical evidence.

This is not a cosmetic workflow choice. It prevents a new architecture from being implemented under a frozen contract that explicitly requires the old Round-5 execution path.

### Critic resolution summary

| Critic finding | v0.3 decision |
| --- | --- |
| `REALIZE_MEANING` “cannot see source” is not a true context sandbox | **ACCEPT, choose soft isolation.** Do not claim model-context isolation that ordinary plugin runtime cannot prove. |
| Frozen 050 Plan / replay task conflict with v0.2 | **ACCEPT underlying issue, reject in-place revision mechanism.** 050 revision budget is exhausted; use a successor task with a new Plan and new replay contract. |
| Forced `scientific-rewrite` replay does not prove ordinary-user routing | **ACCEPT.** Add black-box natural-user routing gate. |
| `writing-fidelity` may lock headings/order and undo structural rewrite | **ACCEPT.** Define explicit structural-rewrite fidelity override. |
| Meaning Map source-copy and repair/assembly source leakage remain escape paths | **ACCEPT.** Add direct regression and structured repair/assembly input contracts. |
| Add one fresh real holdout | **ACCEPT as final generalization gate.** Keep it small, frozen before evaluation, and do not tune on failure. |

---

## 1. Verified repository reality

### 1.1 Current 050 workflow authority

On `reviewed/050_writing_style_host_codex_runtime`, current `CURRENT.json` is:

```text
state = AWAIT_HUMAN_DECISION
plan_revision = 1
max_plan_revisions = 1
implementation_commit = 590502f5a78b2032f2238380aa68ea8287d50b9c
```

Therefore 050 has no remaining legal Planner revision budget.

The frozen 050 `PLAN.md` still requires the old execution contract:

```text
source
-> document understanding / map
-> argument units
-> Meaning Card + Fidelity Ledger per unit
-> selected positive transformations
-> unit rewrite from meaning + original
-> ...
```

and explicitly says the semantic/writing steps occur in the same plugin task/session.

The current task-local `CLEAN_PRODUCTION_REPLAY_TASK.md` also still requires the old artifact set, including per-unit Meaning Cards, candidate units, Latin-span inventory, Chinese reader PASS, and post-Chinese self-audit.

These are historical 050 source-of-truth artifacts. v0.3 does not pretend they already describe the new architecture.

### 1.2 Current `main`

At the last verified main state used by v0.2, `skills/writing/core/` contains:

- `chinese-prose`
- `scientific-prose`
- `writing-fidelity`

and does not contain `scientific-rewrite`.

The current main `writing-style` Marketplace source likewise packages the three existing skills and not the branch-local heavy route.

Implementation must re-read the latest `origin/main` when the successor task is created. This plan does not freeze a stale main SHA as the future implementation base.

### 1.3 Current `writing-fidelity` conflict is real

Current main `writing-fidelity` marks titles, headings, section order and labels as protected spans in its general workflow. That is appropriate for polish/layout/source-faithful reconstruction, but it conflicts with an explicitly authorized structural rewrite where source ordering is not reader-facing authority.

Therefore v0.3 requires a task-mode-dependent fidelity contract instead of leaving this to Executor interpretation.

### 1.4 Historical heavy-route source

The historical heavy-route implementation baseline remains:

`590502f5a78b2032f2238380aa68ea8287d50b9c`

Use it as a selective port/reference source only. Do not treat later failed local Round-6 work as production authority.

---

## 2. Product target

The product remains:

> Take already-established technical/scientific meaning and express it in lower-burden reader-facing language without changing what the source/domain owner actually established.

For a heavy Chinese rewrite, the reader should encounter the actual scientific question, comparison, mechanism, result, limitation or decision directly. Avoidable source abstractions should not remain the sentence skeleton merely because they appeared in the source.

This is not summarization. Unless the user explicitly authorizes deletion/compression, substantive source propositions remain represented somewhere in the final artifact.

---

## 3. Selected runtime architecture: four logical owners

### A. `scientific-rewrite` — heavy document orchestrator

Owns:

- reading the raw source for heavy rewrite;
- source anchors;
- Meaning Map construction;
- Reader Plan construction;
- semantic bundle sizing;
- calling `chinese-prose` realization mode;
- document assembly/coherence;
- invoking source-aware fidelity audit;
- targeted repair routing;
- final re-verification orchestration;
- heavy-route evidence receipt.

Does not own:

- generic Chinese wording rules;
- domain scientific decisions;
- research-writing content selection;
- deterministic language-quality scores.

### B. `chinese-prose` — reusable Chinese realization core

Keeps the current existing-text polish/review path and gains a separate meaning-realization path.

Owns:

- turning already-fixed meaning into natural Chinese;
- local sentence/paragraph realization;
- bounded reader-facing bridges that add no new scientific claim;
- terminology realization where exact external identity is not required.

Does not own:

- source authority;
- content selection;
- semantic fidelity certification;
- document-wide research architecture.

### C. `writing-fidelity` — preservation contract

Owns the semantic/literal preservation rules for the requested edit mode.

For structural rewrite it protects content/evidence authority, not source organization by default.

### D. `rewrite_support.py` — mechanical support only

Owns:

- stable source anchors/hashes;
- Meaning Map/source coverage bookkeeping;
- Reader Plan/meaning ownership validation;
- exact literals/formulas/citations/identifiers;
- current artifact hashes;
- privacy/path/dataflow checks;
- receipt validation.

It must not decide naturalness, reader burden, semantic equivalence or scientific quality.

### Seed/template status

`seed-transformations.json` is **not** a production realization input.

It may remain historical/provenance material. Production writing must not dynamically select literal rewrite templates from it.

---

## 4. End-to-end heavy rewrite pipeline

```text
RAW SOURCE
  ↓
SOURCE ANCHORS
  ↓
MEANING MAP
  ↓
READER PLAN
  ↓
REALIZE_MEANING
  ↓
DOCUMENT ASSEMBLY
  ↓
EXACT + SEMANTIC FIDELITY AUDIT
  ↓
STRUCTURED TARGETED REPAIR (only if needed)
  ↓
RE-ASSEMBLE IF NEEDED
  ↓
RE-VERIFY
  ↓
FINAL
```

The main architectural invariant is:

> Reader-facing drafting is governed by the semantic packet and Reader Plan, not by a source-paragraph editing prompt.

This is a **soft isolation** contract in the selected runtime, not a claim of context sandboxing.

---

## 5. Source isolation: select soft isolation, do not invent nested Codex

### 5.1 Production reality

The current product architecture uses the host Codex model inside one plugin task/session. If that host model has already read the source to build the Meaning Map, switching skills does not erase prior model context.

Therefore v0.3 explicitly rejects the false statement:

> “The realization model cannot see the source.”

Unless a future production runtime provides a real fresh-context stage, that statement cannot be verified.

### 5.2 Selected contract: soft isolation

`REALIZE_MEANING` means:

> Raw source prose must not be part of the realization **instruction/input surface**. The realization step drafts from the semantic packet and Reader Plan. The host model may have seen source material earlier in the same task/session, but the production workflow must not re-present source paragraphs, tails/previews, source excerpts, source quotations, or source-shaped rewrite templates as drafting inputs.

The realization packet contains only:

```text
audience / register
bundle purpose / reader question
relevant meaning records
relevant relation records
required exact item identities/formulas
neighboring bundle purposes/dependencies
information shape
optional structured repair instruction
```

No component may claim that this equals a fresh model context.

### 5.3 Why v0.3 does not choose true isolation now

Do not add ad-hoc nested `codex exec` merely to satisfy an architectural sentence.

`ai-bridge plugin-replay` remains the approved outer production replay mechanism for testing an installed plugin. It is not automatically an internal recursive stage runner.

If real artifacts show that soft isolation is insufficient, return to Planner. A future true-isolation design may be evaluated only through an existing supported fresh-child/runtime mechanism, with cost/privacy/entrypoint behavior understood first.

### 5.4 Acceptance consequence

Because soft isolation is weaker than a true context sandbox, it must earn acceptance through real output. If the new writer still systematically mirrors source syntax/abstraction despite the semantic input surface, do not claim the architecture succeeded because packet fields looked clean.

---

## 6. Source anchors and Meaning Map

### 6.1 Source anchors

Mechanical source anchors are audit locators only:

```text
source_anchor_id
source_sha256
start/end range
anchor_text_sha256
```

Raw anchor prose is available to semantic extraction/audit, but must not be copied into the realization packet.

### 6.2 Meaning Map minimum contract

```text
schema
source_sha256
audience
purpose
reader_questions[]

meanings[]
  meaning_id
  kind
  normalized_meaning
  authority_class
  claim_strength/modality where relevant
  source_anchor_ids[]
  exact_item_ids[] where relevant

relations[]
  relation_id
  relation_type
  from_meaning_ids[]
  to_meaning_ids[]

exact_items[]
  exact_item_id
  literal/hash
  category
  location_role
  source_anchor_ids[]

formula_objects[]
  formula_id
  exact_item_id
  scientific_question
  symbol_meaning_ids[]
  supported_meaning_ids[]

coverage
  source_anchor -> meaning ids
  meaning id -> source anchors
```

`kind` must preserve distinctions when relevant: claim/conclusion, evidence/result, definition/object, condition, comparator, caveat/limitation, uncertainty, negative finding, attribution, next-decision/future-method status.

### 6.3 Source-copy is a known regression, not just prose guidance

The helper must have **no production fallback that synthesizes `normalized_meaning` or equivalent semantic content from source excerpts**.

If semantic extraction is missing/malformed/incomplete:

```text
FAIL / REPAIR SEMANTIC EXTRACTION
```

not:

```text
copy source excerpt -> normalized_meaning -> continue
```

Mechanical regression requirements:

- a fixture where the semantic field is absent must fail rather than be helper-filled;
- a fixture where `normalized_meaning` is exactly a source-anchor excerpt may be rejected as the known direct-copy fallback pattern;
- this exact-copy guard is a regression check only, not a semantic-quality score;
- do not invent similarity/readability thresholds to judge whether a valid semantic abstraction is “different enough.”

The host semantic extractor still owns actual understanding.

### 6.4 Bidirectional authority

Every substantive source anchor maps to at least one meaning ID; every meaning ID maps to a source anchor or explicitly authorized factual source.

Do not force one paragraph = one meaning.

---

## 7. Reader Plan contract

Reader Plan owns reading order and information shape, not wording.

Minimum contract:

```text
schema
meaning_map_sha256
reader_question_order[]

bundles[]
  bundle_id
  reader_question_id
  owned_meaning_ids[]
  required_exact_item_ids[]
  purpose / intended_takeaway
  information_shape
  dependency_bundle_ids[]
  bridge_required
  formula_ids[] where relevant

bundle_order[]
```

It must not contain raw source paragraph text, English-span QA classes, sentence templates, validator language or target sentences.

### Long-document sizing

Priority:

1. whole document if semantic packet + intended output comfortably fit;
2. otherwise one complete reader-question bundle;
3. if still too large, split by semantic sub-question/dependency;
4. mechanical size limits may only raise `NEEDS_SEMANTIC_SPLIT`.

No silent fallback to 4-paragraph / 2800-character chunking.

---

## 8. `chinese-prose` modes

### 8.1 `POLISH_EXISTING`

Preserve existing behavior for already-written text.

It may read the existing reader-facing text because editing that text is the task.

### 8.2 `REALIZE_MEANING`

The writer receives the bounded semantic input surface defined in Section 5.

Forbidden explicit realization inputs:

- raw source paragraph/sentence;
- source tail/preview;
- source quotation;
- source excerpt embedded in finding text;
- Latin-span inventories;
- `exact_identity/useful_recognition/ordinary_reasoning` QA classification;
- QA ledgers/checklists;
- literal seed rewrite templates;
- previous rejected candidate;
- manual GPT reference output.

Output is reader-facing Chinese for one bundle or whole document.

The machine record is minimal:

```text
bundle_id
consumed_meaning_ids[]
output_sha256
```

No self-declared `language_pass=true` field.

### Realization operations

Use semantic operations, not canned sentences:

- `DIRECT_RELATION`
- `QUESTION_FIRST`
- `METHOD_MENTAL_MODEL`
- `FORMULA_WALKTHROUGH`
- `CLAIM_WITH_BOUNDARY`
- `DECOMPRESS_NOUN_STACK`
- `PARALLEL_TO_STRUCTURE`
- `REMOVE_INTERNAL_FRAME`

---

## 9. Assembly contract: no second hidden source-conditioned writer

When multiple bundles are realized, `scientific-rewrite` owns assembly.

### Assembly may receive

- Reader Plan;
- realized bundle text;
- bundle order/dependencies;
- meaning ownership IDs;
- bundle purpose/takeaway;
- required exact objects needed for placement;
- terminology choices already established by realized bundles.

### Assembly must not receive as drafting material

- raw source paragraphs;
- source quotations;
- source tails/previews;
- full source document for a second global rewrite;
- seed templates;
- rejected reference outputs.

### Assembly may do

- order bundles according to Reader Plan;
- add headings/transitions that introduce no new scientific claim;
- remove duplicate definitions when meaning ownership remains intact;
- normalize terminology established by realization;
- fix unresolved local references;
- position formulas/tables/lists.

### Assembly may not do

- re-author scientific claims from raw source;
- silently delete meanings;
- change conclusion strength;
- merge meanings in a way that changes conditions/caveats;
- become an alternative whole-document writer that bypasses `REALIZE_MEANING`.

If assembly reveals a scientific-content problem, route back to Meaning Map / Reader Plan / realization rather than solving it from source prose inside assembly.

---

## 10. Structural rewrite fidelity override

This is a required production contract, not an optional adjustment.

`writing-fidelity` must distinguish at least:

### Ordinary polish / edit / source-faithful reconstruction

Default structural protection may include headings, section order, paragraph organization and labels where the task did not authorize restructuring.

### `STRUCTURAL_REWRITE` / heavy meaning-preserving rewrite

Default protected authority is:

- facts/claims and polarity;
- evidence and attribution;
- comparator and comparison direction;
- conditions/scope/exceptions;
- caveats/limitations;
- uncertainty/modality;
- negative findings;
- conclusion strength;
- numbers/dates/units;
- formulas/notation;
- citations;
- exact formal identities required by the source/user;
- user-explicit no-touch structure/spans.

The following are **not automatically protected** in structural rewrite mode:

- source headings;
- paragraph boundaries;
- paragraph order;
- section order;
- source-local explanatory sentence order;
- internal workflow labels.

If the user explicitly says “keep this heading/order/table position”, that user constraint overrides the default structural freedom.

### Required regression

A source and candidate containing the same facts/claims/numbers/formulas/citations/conditions/caveats but intentionally improved headings and section order must **not** fail fidelity solely because source structure moved.

A candidate that changes a comparator, drops a caveat or strengthens uncertainty must fail.

This override must be encoded in the active `writing-fidelity` contract, not left as an informal assumption in `scientific-rewrite`.

---

## 11. Semantic fidelity audit

`writing-fidelity` owns the contract; `scientific-rewrite` orchestrates a source-aware host semantic audit.

The auditor may see:

- raw source;
- source anchors;
- Meaning Map;
- Reader Plan;
- current candidate.

It checks at least:

- omitted/invented meaning;
- changed comparator;
- condition/scope drift;
- reversed relation;
- lost negative finding;
- lost/strengthened uncertainty;
- wrong attribution;
- caveat placement that changes interpretation;
- conclusion-strength drift.

Findings bind to meaning IDs/source anchors.

The audit is allowed to know the source. The realization writer is not allowed to receive the audit's source prose.

---

## 12. Structured repair contract: close the source-leak backdoor

### 12.1 Repair packet sent to `REALIZE_MEANING`

A repair packet may contain only structured information such as:

```text
bundle_id
affected_meaning_ids[]
finding_type
required_semantic_correction
required_exact_item_ids[]
allowed_realization_operations[] where useful
```

Examples of `required_semantic_correction`:

- restore comparator meaning `meaning-021`;
- keep modality at “suggests/possible”, not established;
- restore caveat meaning `meaning-034` near conclusion `meaning-031`;
- remove candidate sentence not owned by any meaning ID;
- make the relation between `meaning-011` and `meaning-012` explicit.

### 12.2 Forbidden repair payload content

Do not send:

- source quotations;
- source paragraph prose;
- source excerpt fields;
- “原文说：……” blocks;
- a manually rewritten target sentence;
- manual GPT reference text.

Exact formal literals may be referenced through `exact_item_ids`; the realization packet receives only the exact identities actually required.

### 12.3 Meaning Map repair is separate

If the auditor determines the Meaning Map itself is wrong/incomplete, repair the Meaning Map from source first. Then update Reader Plan bindings and re-run realization.

Do not use prose repair to hide a broken semantic representation.

### 12.4 Re-verification

After every repair:

1. affected mechanical exact/coverage checks;
2. affected semantic re-audit;
3. assembly/coherence check if cross-boundary text changed.

Default maximum remains two targeted repair passes for the same unresolved bundle. Then fail closed.

---

## 13. Production evidence: small and architecture-specific

The successor heavy-route replay should require approximately:

```text
meaning_map.json
reader_plan.json
realization/<bundle>.md    # or whole-document realization
assembly.json              # only if multiple bundles
fidelity_audit.json
repair/<round>.json        # only if repair happened
final_candidate.md
stage_receipt.json
```

No required production artifacts for:

- per-tiny-unit Meaning Cards;
- selected sentence templates;
- Latin-span classification;
- Chinese reader self-PASS;
- post-Chinese self-PASS.

Receipt = dataflow evidence only.

---

## 14. Workflow authority: do not mutate exhausted 050 into the new architecture

The Critic is correct that implementation under the current 050 frozen Plan would be contradictory. The mechanism proposed by the Critic—another 050 Planner revision—is not available because 050 already exhausted `max_plan_revisions=1`.

Therefore v0.3 selects this workflow route:

### 14.1 050 remains historical

Do not rewrite:

- `automation/reviewed_handoff/tasks/050_writing_style_host_codex_runtime/PLAN.md`;
- 050 `CURRENT.json` to invent extra revision budget;
- historical 050 result/replay evidence merely to make it look like the new architecture existed there.

The old `CLEAN_PRODUCTION_REPLAY_TASK.md` remains evidence of the Round-5/old-contract replay. It is **not** the replay task for the successor architecture.

### 14.2 User approval of v0.3 authorizes planning, not implementation

If the user later accepts this architecture and asks to implement it, first create a **successor Reviewed Handoff task** with a fresh current Plan contract.

The successor task identifier is chosen at task creation time; do not hard-code it in this design Plan.

Prefer Bridge Kit 0.7.1 / AI_Skills current Plan V2 Goal Fidelity once the repository adaptation is complete.

### 14.3 Successor Plan must explicitly replace the old execution contract

It must freeze:

- four-component runtime model;
- soft-isolation semantics;
- Meaning Map / Reader Plan contracts;
- `REALIZE_MEANING` input surface;
- assembly restrictions;
- structural-rewrite fidelity override;
- structured repair packet;
- ordinary-user routing gate;
- new minimal replay artifacts;
- known regression + fresh holdout acceptance.

### 14.4 Successor task gets its own clean replay task

Create a new task-local replay prompt/evidence contract for the successor task.

Do **not** reuse the historical 050 replay file as if it were current.

This resolves the source-of-truth conflict without falsifying 050 history or exceeding its Planner revision budget.

---

## 15. Production routing: add a real black-box user-entry gate

A forced subskill replay is insufficient.

### 15.1 What forced replay proves

A task that says:

> “Use `writing-style:scientific-rewrite`”

proves only that the heavy route works when the internal route is named.

It does not prove normal plugin discovery/routing.

### 15.2 Required black-box gate

The final acceptance must include a production replay where:

- the installed plugin selected is only `writing-style@yuukias-ai-skills` (or its then-current exact installed id);
- the user task is natural and contains no internal subskill/runtime names;
- the task does not mention `scientific-rewrite`, `REALIZE_MEANING`, Meaning Map, Reader Plan, stage packets or internal evidence files;
- the task asks for a realistic heavy rewrite, e.g. “把这份较长的中文科研报告重新组织成自然、连贯、第一次看的研究者也能读懂的中文，数字、公式、引用、比较条件和结论强度都不能改，不要总结掉内容。”

The resulting heavy-route receipt must prove that the installed plugin internally selected/executed the new heavy route.

### 15.3 Routing regression set

Also verify:

- short/local Chinese polish does **not** unnecessarily enter heavy document orchestration;
- fidelity-only requests remain fidelity-only;
- English scientific prose remains on the English route;
- heavy Chinese source-faithful rewrite naturally enters the heavy route.

The normal-user black-box task is part of Product PASS, not only a unit test.

---

## 16. Mechanical tests and anti-degradation regressions

Tests should prove only observable contracts.

At minimum:

### Meaning / source boundary

- missing semantic extraction fails; helper does not synthesize it from source;
- direct source-excerpt copy fallback is rejected as a known regression;
- every meaning has source authority;
- every substantive source anchor is covered;
- realization packet schema has no raw-source/source-quote fields;
- repair packet schema has no raw-source/source-quote fields;
- assembly input does not include raw source as drafting material.

### Reader Plan / bundling

- Reader Plan owns valid meaning IDs only;
- every reader-facing meaning is owned;
- fixed-size splitter cannot silently choose the final heavy bundles;
- oversized bundle requests semantic split rather than character-cut fallback.

### Fidelity

- exact literals/formulas/citations preserved;
- structural rewrite can change headings/order without fidelity failure;
- changed comparator/caveat/uncertainty fails;
- semantic audit artifact binds current source/map/candidate.

### Production routing

- heavy natural-language request routes to heavy skill;
- short polish does not;
- heavy route uses minimal new stage artifacts;
- source/generated Marketplace parity remains correct.

### Cost/privacy

- no external paid generation dependency;
- private replay commits no plaintext;
- ordinary push does not trigger paid review.

Tests must not claim to prove natural Chinese or reader burden.

---

## 17. Real acceptance: known regression, full report, and fresh holdout

### 17.1 Gate A — known A/B/C regression

A/B/C remain known regression inputs, not unseen evidence.

Run through the installed production plugin architecture, with no plan/failure/reference leakage into the writer.

Human comparison occurs only after generation.

Goal:

- preserve/improve Round-5 factual fidelity;
- materially reduce abstraction decoding / bilingual scaffolding / memo-style burden;
- remaining difference from the human-approved/manual reference is mainly wording preference, not systematic reader-effort gap.

### 17.2 Gate B — full private report

After the known style regression is accepted, run the complete private report through the same installed route.

No alternate writer architecture.

### 17.3 Gate C — fresh real holdout

Before final evaluation begins, freeze a small **different real scientific/technical source** from another document family.

Requirements:

- real source, not synthetic prose;
- different document/project vocabulary from the known A/B/C report;
- enough connected material to require at least a meaningful section-level rewrite (roughly one to several pages; do not choose a single trivial sentence);
- source hash/range frozen before evaluation;
- implementation is frozen before the holdout run;
- the holdout source is not used to add new phrase rules, templates, special cases or validator logic.

Use a normal black-box user prompt, not internal route names.

If the holdout fails the frozen acceptance bar:

- the generalization gate fails;
- do not patch production using holdout-specific wording;
- record the generic failure class;
- any recovery occurs on non-holdout/public-safe regression material;
- a new fresh holdout requires a later explicit decision, following the repository holdout policy.

This gate is intentionally small. It is not a new benchmark program.

### 17.4 Final authority

Human artifact judgment remains final for qualitative writing quality.

Process/schema/receipt PASS cannot override rejection.

---

## 18. Main integration / affected implementation surfaces

When a successor implementation is authorized, start from current `origin/main` at execution time.

Historical heavy-route reference:

`590502f5a78b2032f2238380aa68ea8287d50b9c`

Selective port only.

Expected implementation surfaces include:

- `skills/writing/core/scientific-rewrite/` — selectively port/rewrite heavy orchestrator;
- `skills/writing/core/chinese-prose/SKILL.md` — preserve `POLISH_EXISTING`, add `REALIZE_MEANING`;
- `skills/writing/core/writing-fidelity/SKILL.md` — add explicit structural-rewrite fidelity override and audit handoff;
- `skills/writing/core/scientific-rewrite/scripts/rewrite_support.py` — mechanical-only helper;
- source Marketplace config — package heavy route again;
- generated `plugins/codex/plugins/writing-style/` — regenerate from source, never hand-edit;
- routing/profile docs/tests where required by the real installed path;
- successor task's own clean production replay task/evidence contract.

Do not mutate historical 050 `PLAN.md`/replay task to pretend they are the successor contract.

Do not rename `writing-style` in the same implementation.

Do not wire presentations/research-writing/statistics/visualization/imaging/bioinformatics in the same task.

---

## 19. Non-substitutable semantics / no-degradation policy

The successor implementation must not substitute:

- source-conditioned local paraphrase for semantic realization;
- fixed-size chunks for semantic bundles;
- raw source quotations in repair packets for structured semantic corrections;
- assembly-from-source for bundle assembly;
- helper-generated source-copy meanings for semantic extraction;
- phrase blacklists / English-density scores / readability regexes for natural-language quality;
- tests/receipts for human artifact quality;
- forced subskill invocation for ordinary-user routing;
- paid per-stage generation for host-Codex generation;
- glossary/token dumps for contextual fidelity repair.

If soft isolation plus semantic packet still fails to produce materially better prose, report architecture failure rather than quietly reintroducing the old writer.

---

## 20. Version history

### v0.1

Direction: move away from source-conditioned local rewrite toward semantic planning → realization → fidelity repair.

Main gap: architecture idea without complete component contracts.

### v0.2

Added:

- four owners;
- Meaning Map / Reader Plan contracts;
- two `chinese-prose` modes;
- assembly owner;
- semantic fidelity owner;
- targeted repair/reverify;
- long-document semantic split;
- minimal stage evidence;
- selective port from Round 5 to current main.

Critic result: architecture direction PASS, execution readiness REVISE.

### v0.3 — current

Adds/fixes:

- explicitly chooses **soft isolation** and stops claiming a fresh model context;
- forbids ad-hoc nested Codex as a fake isolation fix;
- recognizes 050's exhausted Planner revision budget and requires a **successor task**, not an illegal in-place Plan revision;
- leaves historical 050 Plan/replay evidence unchanged and requires a new successor replay contract;
- adds black-box ordinary-user routing acceptance;
- writes the `writing-fidelity` structural-rewrite override as a mandatory production contract;
- adds direct source-copy regression behavior for Meaning Map helpers;
- constrains repair packets so source prose cannot leak back into realization;
- constrains assembly so it cannot become a second raw-source writer;
- adds a small frozen fresh real holdout after known regression/full-report gates.

---

## 21. Current readiness decision

**READY FOR CRITIC REVIEW. NOT EXECUTION AUTHORIZATION.**

If Critic accepts v0.3 and the user later asks for implementation planning, the next artifact should be a **new successor Reviewed Handoff Plan** built from current main and current Bridge Kit/AI_Skills workflow contracts.

Do not produce an Executor prompt or modify production code until the user explicitly requests that next step.
