# Clear-language production redesign plan

Plan version: **0.2**

Status: **DRAFT / READY FOR USER REVIEW / NOT EXECUTION AUTHORIZATION**

Supersedes for planning purposes: `ROUND6_PLUGIN_REDESIGN_PLAN_2026-09-06.md` (treat that earlier document as v0.1 design history).

This file does not modify the frozen Reviewed Handoff `PLAN.md`, does not authorize Codex implementation, does not rename `writing-style`, and does not declare 050 PASS.

## 0. Why v0.2 exists

The v0.1 direction was broadly correct: reduce the heavy rewrite path to semantic understanding → reader plan → natural Chinese realization → fidelity repair. The external critique correctly identified that v0.1 was not yet execution-ready because it did not fully reassign every responsibility from the old Round-5 pipeline, did not define component contracts tightly enough, and did not account for the fact that current `main` does not contain `scientific-rewrite` at all.

This v0.2 keeps the architecture direction but closes those gaps.

One clarification to the critique: `seed-transformations.json` being a separate file does not by itself make it a fifth architectural component. The relevant question is whether production realization consumes it as an independent conditioning source. v0.2 resolves that ambiguity by removing the seed library from the production realization path entirely. It may remain as provenance/development history, but production writing does not read literal rewrite templates from it.

---

## 1. Verified repository reality

### 1.1 Current `main`

At the time of this plan, `AI_Skills_Collection/main` is `50963b7d0dd6a723b3589460e1023f20d429dfb1`.

Current `main` under `skills/writing/core/` contains only:

- `chinese-prose`
- `scientific-prose`
- `writing-fidelity`

It does **not** contain `scientific-rewrite`.

Current `main` marketplace `writing-style` likewise packages only:

- `writing-fidelity`
- `scientific-prose`
- `chinese-prose`

Therefore the next implementation cannot assume the branch-local 050 heavy route already exists on `main`.

### 1.2 Historical heavy-route source

The stable historical source baseline for the heavy route is the 050 implementation commit:

`590502f5a78b2032f2238380aa68ea8287d50b9c`

That implementation produced the materially improved Round-5 output and contains the branch-local `scientific-rewrite` skill, helper, references, tests and generated `writing-style` payload needed to understand the old production path.

Do not treat the later failed local Round-6 implementation as the port base. The failed local Round-6 work is diagnostic evidence, not a production source of truth.

### 1.3 Current generic communication boundary

`main` already has a design proposal that separates:

- generic reader-facing language layer;
- `research-writing` document authoring;
- `presentations` deck information architecture;
- domain plugins such as statistical-modeling / visualization / imaging / bioinformatics.

This redesign follows that boundary: the language layer expresses already-decided meaning; it does not take over domain scientific decisions.

---

## 2. Product target

The plugin should do one thing reliably:

> Take already-established technical/scientific meaning and express it in lower-burden reader-facing language without changing what the source/domain owner actually established.

For Chinese scientific writing, success means the reader encounters the actual scientific question, comparison, mechanism, result, limitation or decision directly. The reader should not have to decode an avoidable abstract label first merely because that label existed in the source.

This is not a summarizer. For a source-faithful heavy rewrite, all substantive source propositions remain represented somewhere unless the user explicitly authorizes deletion/summarization.

---

## 3. Final runtime component model: four components

Production should have four logical owners.

### A. `scientific-rewrite` — heavy document orchestrator

Owns:

- raw source reading for heavy rewrite;
- Meaning Map construction;
- Reader Plan construction;
- long-document semantic bundling;
- document-level assembly and coherence;
- calling `chinese-prose` realization mode;
- invoking source-aware fidelity audit;
- routing targeted repair;
- final re-verification orchestration.

Does not own:

- generic Chinese sentence style rules;
- domain scientific decisions;
- deterministic “naturalness” scoring;
- research-writing content selection.

### B. `chinese-prose` — Chinese realization core

Keeps its existing polish/review capability and gains a distinct meaning-realization capability.

It owns how fixed meaning becomes natural Chinese.

It does not own factual/source authority and cannot certify fidelity by itself.

### C. `writing-fidelity` — preservation contract

Owns the preservation semantics:

- facts/claims;
- polarity;
- comparator;
- condition/scope;
- caveat/uncertainty;
- attribution;
- conclusion strength;
- formulas/numbers/citations/exact identity.

It defines both literal and semantic fidelity requirements. The host model performs semantic audit under this contract; deterministic code only handles mechanically safe checks.

### D. `rewrite_support.py` — mechanical support only

Owns only deterministic, observable behavior:

- source anchor creation/hashes;
- schema/dataflow validation;
- Meaning Map ↔ source anchor coverage bookkeeping;
- Reader Plan ↔ meaning-ID ownership checks;
- exact literals/formulas/citations/identifiers;
- candidate hashes;
- privacy/path checks;
- production stage receipt.

It must not judge whether prose is natural, simple, elegant or low-burden.

### `seed-transformations.json`

Not a production component in v0.2.

Production realization must not load literal `rewrite_template` examples from this file. Existing seed/provenance material may remain for history, offline analysis or future research, but it is not an input to the production writer.

A small operation vocabulary belongs inside the canonical `chinese-prose` realization contract (or one reference packaged as part of that skill), not in a separately selected sentence-template library.

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
CHINESE REALIZATION
  ↓
DOCUMENT ASSEMBLY
  ↓
EXACT + SEMANTIC FIDELITY AUDIT
  ↓
TARGETED REPAIR (only if needed)
  ↓
RE-VERIFY
  ↓
FINAL
```

The major behavioral change is between Reader Plan and Chinese realization: realization no longer uses the original source paragraph as a co-primary drafting input.

---

## 5. Stage 1 — source anchors

Before semantic abstraction, deterministic support creates stable task-local source anchors.

An anchor is not a sentence template. It is only an audit locator.

Each anchor contains at minimum:

```text
source_anchor_id
source_sha256
start_line / end_line or equivalent stable source range
anchor_text_sha256
```

The raw source text remains available to `scientific-rewrite` and later fidelity audit, but it is not copied into the realization packet.

Anchors solve two requirements simultaneously:

1. Meaning representation is not forced to carry source wording.
2. Every abstracted meaning can still be traced back to actual source evidence during audit/repair.

---

## 6. Stage 2 — Meaning Map contract

The Meaning Map replaces the current combination of Document Map + many local Meaning Cards as the **primary semantic representation**.

It is document-level and meaning-centric.

Minimum contract:

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
  claim_strength / modality where relevant
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

### `kind`

The representation must distinguish at least when relevant:

- claim / conclusion;
- evidence/result;
- definition/object;
- condition;
- comparator;
- caveat/limitation;
- uncertainty;
- negative finding;
- attribution;
- next-decision / future-method status.

Do not create a giant ontology. These classes exist only to stop meaning from collapsing during rewrite.

### `authority_class`

Use the smallest useful set already established in 050, for example:

- project fact;
- literature fact;
- research interpretation;
- candidate method;
- still-unverified.

### `claim_strength / modality`

The Map must preserve distinctions such as:

- observed vs proved;
- possible vs established;
- suggests vs demonstrates;
- planned/candidate vs already executed.

This may be a compact field or structured annotation; do not invent numeric certainty scores.

### Coverage rule

Bidirectional traceability is mandatory:

- every substantive source anchor must map to at least one meaning ID;
- every meaning ID must cite at least one source anchor or explicitly authorized factual source;
- a source anchor may support multiple meanings;
- final reader bundle ownership is over `meaning_id`, not raw paragraph position.

Do not require artificial one-to-one paragraph mapping.

### Forbidden content in Meaning Map

Do not include as writer-facing fields:

- raw source paragraph prose;
- `useful_recognition` / `ordinary_reasoning` token classes;
- sentence-level translation decisions;
- literal rewrite templates;
- QA PASS fields;
- project-specific wording copied from reference outputs.

`normalized_meaning` must state meaning, not paraphrase the original sentence with the same syntax.

---

## 7. Stage 3 — Reader Plan contract

The Reader Plan decides how a reader should encounter the Meaning Map.

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

Allowed information shapes remain small and practical:

- prose;
- short list;
- table;
- formula walkthrough;
- technical trace where genuinely reader-relevant.

### What Reader Plan must not contain

- raw source paragraph text;
- English-span QA classification;
- rewrite templates;
- validator vocabulary;
- sentence-level target wording.

### Bundle sizing / long-document policy

Semantic structure decides bundles.

Priority:

1. whole-document realization if Meaning Map + Reader Plan + intended output comfortably fit the active context;
2. otherwise one complete reader-question bundle at a time;
3. if one reader question is still too large, split it by semantic sub-question/dependency into child bundles;
4. mechanical size limits may signal `NEEDS_SEMANTIC_SPLIT`, but they must not choose an arbitrary character boundary as the final split point.

The old `4 paragraphs / ~2800 chars -> flush` behavior must not remain the default production realization structure.

No silent fallback from semantic bundling to fixed-size chunking.

---

## 8. Stage 4 — `chinese-prose` must support two modes

This is the largest contract change.

### Mode 1: `POLISH_EXISTING`

Preserve current `chinese-prose` behavior for short/local existing text.

Input may include:

- existing reader-facing text;
- protected exact spans;
- audience/register;
- requested edit depth.

Use cases:

- sentence/paragraph polishing;
- README/status cleanup;
- caption/slide copy already drafted;
- light de-translation.

This mode must not regress.

### Mode 2: `REALIZE_MEANING`

New behavior for heavy/structured generation from fixed meaning.

Input is strictly bounded to:

```text
audience
reader-question / bundle purpose
relevant meaning records
relevant relation records
required exact identities/formulas
neighboring bundle purposes / dependencies
information shape
```

Forbidden writer inputs:

- raw source paragraph/sentence text;
- source-local wording preview/tail as a drafting template;
- `exact_identity/useful_recognition/ordinary_reasoning` classification;
- Latin-span inventories;
- QA ledger prose;
- literal rewrite templates from seed library;
- previous rejected candidate;
- manual GPT reference text.

The writer can know the exact formal identities that must appear; it must not see the full preservation machinery that classified them.

### Output

The output is reader-facing Chinese for one bundle (or the whole document).

A minimal machine-side realization record may contain:

```text
bundle_id
consumed_meaning_ids[]
output_sha256
```

It must not contain self-declared language PASS fields.

### Canonical realization operations

`chinese-prose` should encode a small operation vocabulary as guidance, not canned sentences:

- `DIRECT_RELATION` — state the actual comparison/action/condition/consequence instead of an avoidable abstract label;
- `QUESTION_FIRST` — state the concrete reader question before dense terminology when helpful;
- `METHOD_MENTAL_MODEL` — explain what each method sees/sends/optimizes and the key difference before notation;
- `FORMULA_WALKTHROUGH` — why this formula matters → exact formula → symbols → implication/boundary;
- `CLAIM_WITH_BOUNDARY` — bounded conclusion with nearby evidence/caveat;
- `DECOMPRESS_NOUN_STACK` — turn stacked labels into subject/action/relation;
- `PARALLEL_TO_STRUCTURE` — table/list only for genuine parallel structure;
- `REMOVE_INTERNAL_FRAME` — replace audit/status/workflow framing with the actual reader-facing fact.

These operations contain no project-specific phrase and no final sentence template.

---

## 9. Stage 5 — document assembly and coherence owner

If realization happens in multiple bundles, `scientific-rewrite` owns assembly.

Assembly must handle:

- final bundle order from Reader Plan;
- duplicate definitions;
- terminology drift;
- cross-section transitions;
- unresolved references (“上述/该方法/这里”);
- heading consistency;
- formula placement;
- repeated caveats;
- local table/list/prose integration.

Assembly may add reader-facing connective language and headings that introduce no new scientific claim.

Assembly must not silently delete, strengthen, weaken or merge meanings merely for smoothness.

Final candidate must retain a machine mapping from final section/bundle to owned meaning IDs so later audit knows what should be present.

---

## 10. Stage 6 — fidelity audit ownership

The critique correctly identified that semantic audit cannot disappear.

### Literal/mechanical fidelity

`rewrite_support.py` checks:

- numbers/dates/units;
- formulas;
- citations;
- code/commands/paths/config ids;
- exact formal identities;
- meaning/source coverage bookkeeping;
- Reader Plan ownership;
- hashes/privacy/dataflow.

### Semantic fidelity

`writing-fidelity` owns the contract; `scientific-rewrite` orchestrates a source-aware host semantic audit after realization/assembly.

The audit sees:

- raw source;
- source anchors;
- Meaning Map;
- Reader Plan;
- final candidate.

It checks at least:

- omitted meaning;
- invented meaning;
- changed comparator;
- condition/scope drift;
- reversed causal/comparative relation;
- lost negative finding;
- lost/strengthened uncertainty;
- wrong attribution;
- caveat moved so far that interpretation changes;
- conclusion-strength change.

Findings must bind to `meaning_id` and source anchor(s), not vague “tone” comments.

Deterministic helpers cannot declare semantic equivalence.

---

## 11. Stage 7 — targeted repair and re-verification

Repair is explicit and bounded.

### If Meaning Map is wrong/incomplete

`scientific-rewrite` repairs the Meaning Map from the raw source first, updates affected Reader Plan bindings if needed, then re-realizes the affected bundle.

Do not patch prose around a broken semantic representation.

### If Meaning Map is correct but prose is unclear or semantically drifts

Re-run `chinese-prose REALIZE_MEANING` for the affected bundle with:

- same fixed meaning records;
- same Reader Plan intent;
- concrete fidelity/reader finding;
- still no raw source wording.

### Re-verification

After every targeted repair:

1. mechanical exact/coverage check on affected bundle;
2. semantic fidelity re-audit on affected meanings;
3. document-level assembly/coherence check if the bundle changed cross-boundary text.

No glossary/token append fallback.

No raw literal append.

No “source-copy Meaning Card” fallback.

No fixed-size chunk fallback.

### Repair budget

Default maximum: two targeted repair passes for the same unresolved bundle in one production attempt.

If the same substantive problem remains, return `qa_failed / needs higher-level repair` rather than entering an unbounded self-refinement loop or weakening fidelity.

This is a stop condition, not a quality score.

---

## 12. Production dataflow evidence — keep it small

Old Round 5 required many stage artifacts. v0.2 keeps only evidence needed to prove the new architecture actually ran.

A heavy replay should need approximately:

```text
meaning_map.json
reader_plan.json
realization/<bundle>.md   # or one whole-document realization
assembly.json             # only when multiple bundles
fidelity_audit.json
final_candidate.md
stage_receipt.json
```

Optional repair artifacts exist only when repair actually occurs.

Do not require production-only artifacts such as:

- Latin-span classification report;
- selected sentence templates;
- per-unit Meaning Cards for every tiny chunk;
- reader PASS self-certification;
- post-Chinese PASS self-certification.

The receipt proves dataflow and identity, not prose quality.

---

## 13. Tests: what they should and should not prove

### Mechanical tests should prove

- Meaning Map schema and bidirectional source-anchor coverage;
- every meaning has source authority;
- Reader Plan only owns valid meaning IDs;
- every meaning intended for reader-facing output is owned by a bundle;
- realization packet contains no raw source text field / English QA classification / seed template;
- production path does not load `seed-transformations.json` as writer conditioning;
- exact literals/formulas/citations are preserved;
- semantic audit artifact binds current source/map/candidate identities;
- repair changes only affected bundle unless plan changes;
- re-verification is required after repair;
- fixed-size splitter cannot silently become heavy production bundle planner;
- source/generated marketplace parity;
- no external paid generation dependency;
- private replay does not commit plaintext.

### Tests must not pretend to prove

- “natural Chinese” via regex;
- low reader burden via English percentage;
- language quality via a self-filled `PASS` JSON fixture;
- Product PASS via schema/dataflow alone.

---

## 14. Real production acceptance for this redesign

This redesign is not accepted because unit tests pass.

### First gate: fixed A/B/C replay

Use the same frozen 050 A/B/C sources through the actual installed production plugin route.

Writer input must not include:

- v0.2 plan;
- failure diagnoses;
- previous candidates;
- manual GPT polished reference;
- expected bad vocabulary.

Human review should compare reader burden with Round 5 and the manually polished reference only **after generation**.

Target:

- preserve or improve Round-5 factual fidelity;
- remove the systematic abstraction-decoding gap;
- difference from the manual GPT reference is mostly wording preference rather than obvious cognitive-load difference.

### Second gate: complete private report

Only after style smoke acceptance, produce the complete private report through the same installed production path.

The full report must not use a different writer architecture.

### Final authority

User artifact judgment remains final for 050.

Automated process PASS cannot override a user rejection.

---

## 15. Main integration plan

This is a major missing piece from v0.1 and is now explicit.

Implementation must start from **current `origin/main` at execution time**, not merge the entire 050 branch.

Use two source bases:

```text
Integration base:
current AI_Skills origin/main

Historical heavy-route implementation source:
590502f5a78b2032f2238380aa68ea8287d50b9c
```

Selective port only the heavy-route capabilities needed by v0.2.

Do not wholesale merge:

- 050 workflow history;
- result artifacts;
- rejected candidates;
- local failed Round-6 implementation;
- temporary validator experiments.

Expected source changes when implementation is eventually authorized:

- add/port `skills/writing/core/scientific-rewrite/` into current main, but rewrite its contract to v0.2 rather than copying Round-5 behavior unchanged;
- extend `skills/writing/core/chinese-prose/SKILL.md` with `REALIZE_MEANING` while preserving existing polish/review behavior;
- retain/adjust `skills/writing/core/writing-fidelity/SKILL.md` only as required for the explicit semantic-audit handoff;
- add a simplified mechanical `rewrite_support.py` under `scientific-rewrite`;
- keep seed templates out of production conditioning;
- update source marketplace config so `writing-style` packages `scientific-rewrite` again;
- regenerate `plugins/codex/plugins/writing-style/` from source, never hand-edit generated files;
- update profile/source docs/tests only where real production routing requires it.

Do not rename `writing-style` during this implementation. `clear-language` remains a later migration after 050 closes.

---

## 16. Consumer scope in this task

v0.2 deliberately chooses the narrow option:

> Build the reusable `chinese-prose` realization core now; do **not** wire every domain consumer in this same task.

Therefore this task does **not** modify production paths of:

- `research-writing`;
- `presentations`;
- `statistical-modeling`;
- `scientific-visualization`;
- `medical-imaging`;
- `bioinformatics`.

Those consumers may adopt the language layer in later bounded tasks after the core behavior is accepted.

This prevents the redesign from becoming a multi-plugin migration before the core writer is proven.

---

## 17. What is removed from Round-5 production behavior

The following are intentionally removed/demoted:

- raw source paragraph as a co-primary realization input;
- 4-paragraph / ~2800-char splitting as default heavy realization structure;
- English-span classification as a Reader Plan/writer axis;
- literal seed rewrite templates as writer conditioning;
- many tiny candidate-unit rewrites followed by concatenation as the default;
- Latin-span inventory as a reader-facing writing driver;
- `chinese_reader_pass=PASS` as production quality authority;
- glossary/token appendix as preservation strategy.

These are not dropped because they are “too many stages”; they are dropped because repeated real output shows they actively bias the model toward local source-conditioned memo writing.

---

## 18. What is preserved from Round 5

Keep the real gains:

- host Codex owns generation; no application-level OpenAI/Terra generation dependency;
- source-faithful structural rewrite is allowed;
- numbers/formulas/citations/exact names stay protected;
- content/evidence graph matters more than source paragraph order;
- no source-copy semantic fallback;
- no raw literal dump;
- no paid per-stage workflow;
- clean isolated production plugin replay;
- private plaintext stays local;
- user rejection overrides mechanical/process PASS.

---

## 19. Failure / no-degradation policy

If v0.2 cannot produce materially lower-burden prose without weakening fidelity:

- do not reintroduce the old local source-conditioned writer;
- do not reintroduce sentence-template selection;
- do not add English-density thresholds;
- do not add phrase blacklists;
- do not make fixed-size chunking the silent fallback;
- do not switch back to paid per-stage generation;
- do not append source literals/glossaries to make checks pass.

Return to Planner with the real candidate and identify which of these failed:

- Meaning Map extraction;
- Reader Plan;
- realization;
- semantic fidelity audit;
- assembly.

---

## 20. Version history

### v0.1

File: `ROUND6_PLUGIN_REDESIGN_PLAN_2026-09-06.md`

Main decision: move from source-conditioned local rewrite toward semantic planning → realization → fidelity repair.

Known gaps: incomplete component contracts, seed ambiguity, semantic audit/repair owner unclear, main integration absent.

### v0.2 — current

Changes:

- freezes exactly four production logical owners;
- removes seed templates from production conditioning;
- defines Source Anchor / Meaning Map / Reader Plan contracts;
- defines `chinese-prose` `POLISH_EXISTING` and `REALIZE_MEANING` modes;
- makes raw source forbidden in realization mode;
- defines document assembly/coherence owner;
- explicitly assigns semantic fidelity audit ownership;
- defines targeted repair + re-verification;
- defines semantic long-document split policy and forbids silent fixed-size fallback;
- shrinks production evidence to a small real dataflow;
- separates mechanical tests from language-quality acceptance;
- defines selective port from `590502f5...` onto current `main`;
- defers other domain consumer wiring to later tasks.

---

## 21. Current readiness decision

**READY FOR NEXT HUMAN/CRITIC REVIEW, NOT READY FOR EXECUTION YET.**

The architecture and contracts are now specific enough for another review pass. Do not produce a Codex implementation prompt until the user explicitly asks for it after reviewing this version.
