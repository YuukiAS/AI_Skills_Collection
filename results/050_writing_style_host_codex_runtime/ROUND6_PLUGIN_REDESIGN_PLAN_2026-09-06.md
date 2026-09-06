# 050 Round 6 — clear-language production redesign plan

Status: **DESIGN PLAN / READY FOR USER CONFIRMATION / NOT EXECUTION AUTHORIZATION**.

This document is the current architecture plan for repairing the `writing-style` production implementation after the Round-6 failure. It supersedes `ROUND6_PLUGIN_IMPLEMENTATION_REDESIGN_2026-09-06.md` as the implementation-planning source, but it does **not** edit the frozen Reviewed Handoff `PLAN.md`, does not authorize Codex execution, and does not rename the plugin.

The problem being solved is simple to state:

> The plugin must take already-established technical/scientific content and explain it in natural reader-facing language without changing what the content means.

For Chinese, this means more than translating English terms or polishing sentences. The reader should normally encounter the actual question, comparison, mechanism, result, limitation, or decision directly, instead of first decoding an avoidable abstract label.

---

## 1. Product decision

Keep the current top-level plugin and skill split for now:

- `writing-style` — current plugin identity during 050;
- `writing-fidelity` — preservation guardrail;
- `chinese-prose` — generic Chinese reader-facing realization layer;
- `scientific-prose` — English scientific prose;
- `scientific-rewrite` — heavy long-document orchestrator.

Do **not** create another humanizer/simplifier plugin.

After 050 closes, the preferred top-level rename remains `writing-style -> clear-language`; the rename is not part of this redesign because current replay evidence is bound to `writing-style@yuukias-ai-skills`.

### Selected production architecture

The heavy Chinese route should become:

```text
SOURCE
  -> MEANING MAP
  -> READER PLAN
  -> READER-FACING REALIZATION
  -> FIDELITY CHECK + TARGETED REPAIR
  -> FINAL
```

The key change is not another quality gate. It is that **reader-facing prose is generated from an explicit meaning representation and reader plan, instead of being produced by locally paraphrasing the original paragraphs while QA/token metadata remains in the writer context**.

`chinese-prose` becomes the reusable realization behavior. `scientific-rewrite` becomes a thinner long-document coordinator around it.

---

## 2. Verified current implementation

### 2.1 Plugin packaging is already broadly correct

Current marketplace source packages four writing skills in `writing-style`:

- `writing-fidelity`
- `scientific-prose`
- `scientific-rewrite`
- `chinese-prose`

The current profile also activates those four skills. This composition is suitable for the intended product and does not need another top-level skill merely to solve Round 6.

### 2.2 The heavy route is much more complicated than the user-facing task

Current `scientific-rewrite/SKILL.md` requires or describes:

1. Document Map;
2. Reader Plan;
3. reader-oriented argument units;
4. Meaning Card per unit;
5. Fidelity Ledger;
6. selected positive transformations;
7. candidate unit per unit;
8. unit semantic audit;
9. self-audit;
10. final assembly;
11. Latin-span inventory / English classification;
12. Chinese reader pass;
13. post-Chinese self-audit;
14. final candidate.

The clean production replay task makes this concrete by requiring many separate stage artifacts, including `candidate_units`, `semantic_audits`, `latin_span_inventory`, `chinese_reader_pass`, and `post_chinese_self_audit` before the result is considered a valid replay.

That orchestration is now shaping the writing task instead of merely supporting it.

### 2.3 The current writer is still anchored to source wording

Current writer instructions explicitly combine:

- current original unit;
- current Meaning Card;
- Fidelity Ledger;
- Reader Plan bundle;
- terminology contract;
- English-span classification;
- previous rewritten tail;
- next-source preview;
- 2–4 selected rewrite examples.

The skill then tells Codex to “rewrite the unit from the Meaning Card and original unit together.”

This is not a clean separation between understanding and expression. The model is still looking directly at the source sentence while deciding how to say it, so source abstractions remain highly salient.

That matches the observed failure mode: instead of replacing an avoidable abstraction with the concrete scientific relation, the writer frequently preserves the abstraction and adds a definition or Chinese gloss around it.

### 2.4 Local chunking is stronger than the documentation suggests

`rewrite_support.py` contains a default `split_markdown_units()` implementation that flushes a unit after roughly four paragraphs or when character count exceeds 2800. The skill text allows non-contiguous reader bundles, but the available deterministic segmentation path still strongly encourages relatively small contiguous units.

This is a poor default for a 20+ page scientific explanation whose main readability gain may require carrying one reader question across several source sections.

### 2.5 English QA has become part of the writing representation

Current Reader Plan includes an English-span policy with:

- `exact_identity`
- `useful_recognition`
- `ordinary_reasoning`

The helper also mechanically inventories Latin spans, and current validation expects a host-authored Chinese reader-pass classification over those occurrences.

This machinery was introduced to stop ordinary English from surviving in Chinese prose. It fixed a real earlier problem, but it also makes English-token ownership unusually prominent in the writer’s thinking. The failure has moved from “leave English untouched” to “retain an abstract English/technical label and explain it.”

### 2.6 The seed library teaches sentence shapes, not only operations

`seed-transformations.json` contains literal `original_template` / `rewrite_template` pairs, with many early entries using `register=formal-technical`.

The first definition seed explicitly teaches a pattern equivalent to:

```text
术语 -> 它在这里指某个定义/角色 -> 决定后续判断
```

This is too close to the Round-5/6 failure pattern. The examples are supposed to teach operations, but their literal sentence shapes are available for imitation.

### 2.7 `chinese-prose` is currently downstream review, not the main realization engine

The current skill is titled “中文自然表达终审”. In the heavy route it reads the final candidate and Reader Plan after scientific-rewrite has already written the prose.

That means the most general “说人话” behavior is applied after the heavy writer has already chosen its vocabulary, sentence skeleton and paragraph logic.

This is backwards for the long-term plugin role. `chinese-prose` should define how already-fixed meaning becomes natural Chinese; it should not mainly act as a cleanup pass after a separate scientific writer has produced formal memo prose.

### 2.8 `writing-fidelity` is mostly on the correct side of the boundary

Current `writing-fidelity` already allows explicit structural rewriting to preserve the **content/evidence graph rather than source order**. It protects claims, evidence, conditions, comparators, caveats, uncertainty, formulas, numbers and exact identities while allowing reader-facing headings/paragraphs/order to change.

This should be preserved. The main redesign is not a relaxation of fidelity.

### 2.9 Current unit tests mostly validate plumbing, not the quality behavior

`tests/test_scientific_rewrite.py` builds stage fixtures where candidate units can simply equal the source unit, then constructs a `chinese_reader_pass` shell with `decision=PASS` and PASS subfields.

Those tests are useful for schema/dataflow/privacy/exact-regression checks. They do not prove that the production writer has learned to produce lower-burden prose. This explains why the relevant tests can all be green while the real Round-6 artifact is still visibly poor.

This is not itself a test bug; it is a reminder that the production implementation must be fixed rather than trying to make unit tests act as a language model.

---

## 3. What the real failures say about the generator

The private Deep Research manual rewrite and Round-5/6 production candidates are not committed to Git. Their privacy-safe lessons are already recorded in the task branch.

The repeated generic differences are:

### A. The better rewrite replaces abstractions with their actual scientific role

Weak pattern:

```text
abstract term -> translation/definition -> scientific point
```

Lower-burden pattern:

```text
scientific question/comparison/mechanism -> exact term only if recognition still matters
```

A definition is not equivalent to removing the decoding step.

### B. The better rewrite uses more information-shape changes

Human/GPT rewriting is willing to:

- ask the reader question explicitly;
- add a short explanatory bridge;
- split one dense paragraph into a sequence;
- move a formula after the reason for looking at it;
- regroup related evidence;
- use a table/list when the comparison is genuinely parallel.

The current system has rules allowing these operations, but local source-anchored drafting makes them secondary to paragraph-by-paragraph preservation.

### C. The failed system optimizes locally

Round 6 still produced bilingual noun stacks, unnatural literal relations, repeated words and technical-label compression. These are consistent with a model trying to satisfy many local constraints simultaneously rather than first deciding how a reader should understand the argument.

### D. QA artifacts are leaking conceptually into prose

Earlier rounds produced literal/token appendices. Round 5 produced a reader-facing section explaining compound identifiers. Round 6 continued to show label-like prose even when the explicit glossary leak was reduced.

The problem is not only a missing “no glossary” rule. The generation context itself gives QA/token categories too much importance.

---

## 4. External evidence used for this redesign

This plan uses outside research only for architecture choices; it does not treat those papers as proof that one exact repository implementation will work.

### 4.1 Separate planning from realization

Reiter & Dale’s applied NLG architecture separates document planning (what to say and how to structure it), microplanning and surface realization. Moryossef, Goldberg & Dagan (NAACL 2019) explicitly separate faithful text planning from neural realization and report improved reliability/adequacy while maintaining fluency.

References:

- Reiter, E. & Dale, R. *Building Natural Language Generation Systems*, Cambridge University Press. Document Planning / Microplanning / Surface Realisation chapters.
- Moryossef, A., Goldberg, Y., Dagan, I. 2019. “Step-by-Step: Separating Planning from Realization in Neural Data-to-Text Generation.” NAACL-HLT. DOI: `10.18653/v1/N19-1236`.

Repository implication: the semantic representation handed to the writer should be substantially more important than the source sentence wording.

### 4.2 Long documents need document context, not repeated sentence/local editing

Cripwell, Legrand & Gardent show that sentence-level simplification applied repeatedly at document level can fail to preserve discourse structure; document-level planning improves simplification, and access to broader document context improves realization.

References:

- Cripwell, L., Legrand, J., Gardent, C. 2023. “Document-Level Planning for Text Simplification.” EACL. DOI: `10.18653/v1/2023.eacl-main.70`.
- Cripwell, L., Legrand, J., Gardent, C. 2023. “Context-Aware Document Simplification.” Findings ACL. DOI: `10.18653/v1/2023.findings-acl.834`.

Repository implication: the current 4-paragraph / ~2800-character default segmentation should not determine the realization structure of heavy rewrites.

### 4.3 Human simplification is not only substitution/deletion

Yamaguchi et al. compared professional human simplification with neural systems and found systems over-rely on deletion/local substitution and struggle with content-level operations, including adding explanatory material needed for simplification.

Reference:

- Yamaguchi, D., Miyata, R., Shimada, S., Sato, S. 2023. “Gauging the Gap Between Human and Machine Text Simplification Through Analytical Evaluation of Simplification Strategies and Errors.” Findings EACL. DOI: `10.18653/v1/2023.findings-eacl.27`.

Repository implication: “reader effort is not compression” must be an actual drafting behavior; the writer must be allowed to add bounded explanatory bridges that introduce no new scientific claim.

### 4.4 Defining jargon is not the same as removing its processing burden

Shulman et al. experimentally found that jargon reduced processing fluency even when definitions were supplied.

Reference:

- Shulman, H. C., Dixon, G. N., Bullock, O. M., Colón Amill, D. 2020. “The Effects of Jargon on Processing Fluency, Self-Perceptions, and Scientific Engagement.” *Journal of Language and Social Psychology*. DOI: `10.1177/0261927X20902177`.

Repository implication: `technical term + parenthetical definition` cannot be the default success pattern when the same scientific relation can be stated directly.

### 4.5 Explicit edit operations are useful; canned target sentences are not required

CoEdIT and explicit-edit simplification work support giving a model clear edit operations/instructions. This is evidence for retaining a small operation vocabulary while removing literal rewrite templates from the primary production context.

References:

- Raheja, V., Kumar, D., Koo, R., Kang, D. 2023. “CoEdIT: Text Editing by Task-Specific Instruction Tuning.” Findings EMNLP. DOI: `10.18653/v1/2023.findings-emnlp.350`.
- Dong, Y., Li, Z., Rezagholizadeh, M., Cheung, J. C. K. 2019. “EditNTS: A Neural Programmer-Interpreter Model for Sentence Simplification through Explicit Editing.” ACL. DOI: `10.18653/v1/P19-1331`.

Repository implication: production guidance should name the transformation to perform, not provide a sentence shell that the model can imitate.

---

## 5. Alternatives considered

### Alternative A — keep the current route and add more Chinese rules

Examples: more term classes, more anti-patterns, more regexes, more reader-pass fields.

**Reject.** Six rounds show diminishing returns and new proxy behavior. The current problem is how prose is generated, not a shortage of rules describing bad output.

### Alternative B — one direct whole-document rewrite from the raw source

This resembles the successful manual GPT rewrite and maximizes global context.

**Not selected as the only production route.** It is attractive for moderate documents, but it weakens observability and makes high-fidelity repair harder on long/dense material. It also risks omission or silent claim drift when a document exceeds a comfortable single-pass working size.

Whole-document realization should nevertheless be allowed inside the selected architecture when the source and output comfortably fit the active model context.

### Alternative C — semantic planning -> realization -> fidelity repair

**Selected.** It preserves the main benefit of the successful manual rewrite (meaning-first global explanation) while retaining explicit source coverage and fidelity repair.

The realization unit becomes a whole document or a large reader-question section, not a mechanically fixed paragraph chunk.

### Alternative D — external model/API for every semantic stage

**Reject.** 049 already demonstrated the cost/complexity failure. Normal plugin use must remain host-Codex based without a separate API bill.

---

## 6. Target implementation in detail

## Stage 1 — Meaning Map

Replace the current stack of Document Map + argument segmentation + many per-unit Meaning Cards as the primary semantic representation with one compact document-level **Meaning Map**.

The Meaning Map is not reader prose. It records what must survive.

Minimum contents:

```text
audience
purpose
reader questions
propositions
  - proposition id
  - normalized meaning
  - source span ids / source hashes
  - evidence/authority class
  - condition/comparator
  - caveat/uncertainty when applicable
relations
  - supports
  - contrasts
  - conditions
  - limits
  - explains
  - leads-to / next-decision
formula objects
  - exact formula identity
  - what question the formula answers
  - key symbol meanings already present in source
exact identities
  - true algorithm/dataset/metric/package/API/code/path/citation identities
coverage map
```

Important constraints:

- normalized meaning must not be a source-copy fallback;
- no phrase-level English retention policy here;
- no `useful_recognition` / `ordinary_reasoning` ownership here;
- no target sentence templates;
- no research-writing content selection: every source proposition remains owned somewhere.

The existing `document_map.json` name may be retained for compatibility if necessary, but semantically it must become this meaning-centric representation. Do not create an extra layer merely to preserve old names.

## Stage 2 — Reader Plan

The Reader Plan answers only **how the reader should encounter the meanings**.

It contains:

```text
reader-question order
bundle ids
proposition ids owned by each bundle
bundle purpose / intended takeaway
information shape
  - prose
  - short list
  - table
  - formula walkthrough
where a short explanation/bridge is required
neighboring bundle relationship
```

It does **not** contain:

- English token classification;
- literal rewrite templates;
- raw source paragraph text as drafting material;
- test/QA vocabulary.

Bundle size is semantic, not character-count driven.

Preferred realization size:

1. whole document when it comfortably fits current context;
2. otherwise one complete reader question / major section at a time;
3. only use small local units when the source itself is naturally modular.

Every bundle receives the **full compact Reader Plan** and the purposes of neighboring bundles, not only a short previous tail and next-source preview.

## Stage 3 — Reader-facing realization

This is where `chinese-prose` becomes the actual reusable language layer.

Primary drafting input:

```text
Meaning Map
+ Reader Plan
+ exact identities/formulas needed by the current bundle
```

The raw source remains available as factual authority and later fidelity reference, but its sentence wording must no longer be a co-primary drafting template.

The realization instruction should be simple:

> Explain the planned meanings to this reader in natural Chinese. State the actual scientific relation before introducing avoidable labels. Keep exact external identities when needed. Add only explanatory bridges that do not add scientific claims.

### Production operation vocabulary

Replace literal sentence templates with a small operation catalog:

1. **直接说关系** — replace an avoidable abstract label with the actual comparison/action/condition/consequence.
2. **先说问题** — state what the reader needs to understand before introducing technical terminology.
3. **把方法讲成“拿到什么、做什么、差在哪里”** — give a mental model before dense notation.
4. **公式先讲为什么看它** — question/intuition -> exact formula -> important symbols -> implication/boundary.
5. **结论和限制放在一起** — bounded claim -> evidence -> nearby caveat.
6. **拆开名词堆** — turn stacked labels into subject + action + relation.
7. **并列信息换形态** — use list/table only when the content is genuinely parallel.
8. **去掉内部流程外壳** — replace audit/status/workflow framing with the scientific fact/relation it represents.

These operations have descriptions and applicability conditions only. They do not contain project-specific vocabulary or canned final sentences.

### Jargon / English rule

The decision sequence becomes:

1. Is this an exact external identity the reader may need to recognize? If yes, preserve it.
2. If not, can the underlying scientific relation be expressed directly in Chinese? If yes, do that.
3. If an English technical label still materially helps recognition, introduce it only after the Chinese meaning/role is already clear.

A parenthetical definition is an available form, not the target behavior.

## Stage 4 — Fidelity check and targeted repair

Run fidelity **after** natural realization, not as a sentence-construction template.

### Deterministic helper owns only mechanically safe checks

Keep:

- numbers, dates, units;
- exact formulas/notation objects where literal preservation is required;
- citations;
- code/commands/paths/config identifiers;
- exact external identities;
- source span/proposition coverage ids;
- hashes, privacy and generated/source parity.

Do not use deterministic code to judge:

- natural Chinese;
- abstraction burden;
- whether an explanation is “good enough”;
- whether a technical term sounds reader-friendly.

Latin-span enumeration may remain as an **optional diagnostic tool**, but it is removed from the writer’s required semantic plan and from any mechanism that forces prose to be built around classification categories.

### Host semantic fidelity check owns meaning drift

Check only:

- omitted or invented proposition;
- changed comparator/condition;
- reversed relation;
- changed attribution;
- erased uncertainty/caveat;
- conclusion-strength drift.

Repair the affected reader bundle in context.

Never append a literal list, token glossary, classification appendix or QA explanation to satisfy fidelity.

## Stage 5 — final coherence pass

After targeted fidelity repair, do one short document-level pass for:

- duplicated definitions;
- broken references/transitions introduced by repair;
- accidental repetition;
- heading/paragraph continuity;
- formula explanation still adjacent to the formula.

This pass may edit language but may not introduce/delete scientific propositions.

The final artifact is then returned.

---

## 7. Three task sizes for the reusable language layer

The same source behavior should support other plugins without forcing a long-document workflow on every caption.

### LIGHT

Examples: caption, figure annotation, slide copy, short conclusion, table heading.

Flow:

```text
caller-provided fixed meaning
-> chinese-prose realization
-> minimal fidelity check
```

No Document/Reader Plan.

### STANDARD

Examples: several connected paragraphs or one technical section.

Flow:

```text
source
-> compact Meaning Map
-> realization
-> fidelity repair
```

Reader Plan optional when order is already clear.

### HEAVY

Examples: long existing report requiring structural rewrite.

Flow:

```text
source
-> full Meaning Map
-> Reader Plan
-> whole-document or large-bundle realization
-> fidelity repair
-> coherence pass
```

This mode is `scientific-rewrite`.

`research-writing` still decides what belongs in a new report/paper. `presentations` still decides slide jobs and deck sequence. Domain plugins still own statistical/visual/medical/biological semantics.

---

## 8. Exact source files to change

This section defines implementation ownership; it is not a Codex prompt.

### 8.1 `skills/writing/core/scientific-rewrite/SKILL.md`

**Major rewrite required.**

Keep:

- trigger boundary;
- source authority;
- structural rewrite authorization;
- no external API generation;
- exact/semantic fidelity distinction;
- long-document role.

Remove/demote from production flow:

- English-span classification inside Reader Plan;
- current small local writer-packet design;
- mandatory 2–4 literal rewrite examples per unit;
- original source unit as equal co-primary realization input;
- “single whole-document writer call is invalid” blanket rule;
- many-unit candidate generation as the default;
- self-review artifact proliferation as part of writing semantics.

Replace workflow with the 5 stages above.

### 8.2 `skills/writing/core/chinese-prose/SKILL.md`

**Promote from terminal cleanup to canonical Chinese realization behavior.**

Keep:

- Chinese-first principle;
- preserve exact names/facts;
- avoid internal workflow language;
- reader effort != compression;
- lists/tables allowed when structurally useful.

Add/strengthen:

- realize from already-fixed meaning, not from source wording;
- direct scientific relation before abstract label;
- bounded explanatory bridges;
- method mental model before dense terminology;
- LIGHT/STANDARD/HEAVY applicability;
- distinction between exact identity and ordinary conceptual language.

Demote/move out of the core instruction:

- long phrase-by-phrase replacement catalogs;
- any wording that makes English scanning the primary writing operation.

The skill should read like a generator’s language policy, not a post-hoc checklist.

### 8.3 `skills/writing/core/scientific-rewrite/references/meaning-card-and-fidelity-ledger.md`

**Simplify/replace the semantic intermediate design.**

Preferred change:

- replace per-unit Meaning Card emphasis with document-level Meaning Map;
- keep source proposition/span ownership and fidelity rules;
- remove English-span policy from semantic planning;
- keep formula meaning objects and evidence-class boundaries.

A new reference filename is optional; do not create another layer just to rename the concept.

### 8.4 `skills/writing/core/scientific-rewrite/references/seed-transformations.json`

**Stop using literal rewrite templates as production writer input.**

Preserve this file as provenance/reference if useful.

Add one small production operation catalog (or convert the existing file) containing only:

- operation id;
- short description;
- when to use;
- fidelity risk / guardrail.

No `original_template` / `rewrite_template` is consumed during production realization.

### 8.5 `skills/writing/core/scientific-rewrite/scripts/rewrite_support.py`

**Reduce to mechanical support.**

Keep or refactor:

- literal extraction where mechanically valid;
- exact verification;
- source span/proposition ids;
- coverage/id/hash validation;
- privacy/dataflow receipts;
- stage schema validation.

Remove from the required production-quality path:

- `select_examples()` template selection;
- deterministic local chunking as the authoritative reader segmentation;
- `ENGLISH_SPAN_CLASSES` as writer-plan semantics;
- Latin classification as a mandatory quality PASS;
- `validate_chinese_reader_pass()` as proof of naturalness;
- any CJK/readability regex introduced by failed local Round-6 work.

Optional diagnostics may remain callable if they are clearly non-authoritative and do not shape final prose.

### 8.6 `results/050.../CLEAN_PRODUCTION_REPLAY_TASK.md`

**Reduce replay-induced orchestration pressure.**

The replay should no longer force the writer to manufacture a large QA packet.

Preferred private outputs:

```text
rewritten_report.md
stage_receipt.json
stage_packets/meaning_map.json
stage_packets/reader_plan.json          # HEAVY only
stage_packets/initial_draft.md
stage_packets/fidelity_report.json
stage_packets/final_candidate.md
```

Optional debug artifacts may exist, but are not required writer work and are not reader content.

The clean child still receives only TASK + SOURCE.

### 8.7 `tests/test_scientific_rewrite.py`

**Reframe tests around real deterministic responsibilities.**

Keep tests for:

- plugin replay isolation;
- private data not committed;
- exact literals/formulas/citations;
- coverage ids;
- no source-copy semantic fallback;
- no raw literal/token appendix;
- no external API generation;
- generated/source parity;
- stage dataflow.

Remove/replace tests that imply language quality is proven because a fixture can self-write `reader_effort=PASS`.

Do not make unit tests judge natural Chinese.

Add boundary tests proving:

- the heavy writer plan no longer requires English-span classification;
- production operation data contain no sentence templates;
- small mechanical chunking is not required as the final reader bundle structure;
- the reduced stage package is accepted;
- old glossary/token appendices remain rejected;
- exact/formula repair still fails closed when content is actually missing.

### 8.8 Marketplace/profile/generated plugin

Update source config only if descriptions/routing need to reflect the new heavy path. Keep the same plugin slug/version until 050 acceptance.

Regenerate `plugins/codex/plugins/writing-style/**` from canonical source; never hand-edit generated copies as the source of truth.

---

## 9. What not to change

Do not change in this redesign:

- `research-writing` scientific/document-authoring responsibilities;
- `presentations` page/deck responsibilities;
- statistical/visual/medical/bioinformatics domain semantics;
- Bridge Kit workflow architecture;
- paid Terra/OpenAI review architecture;
- plugin slug/version;
- the user’s source facts or scientific claims;
- the existing human authority over final style acceptance.

Do not add:

- another top-level plugin;
- a new generic verifier role;
- a phrase blacklist;
- English-density/readability scores;
- sentence-length targets;
- project-specific CARE/ODAL vocabulary rules.

---

## 10. Red-team: how this redesign could still fail

### Failure 1 — Meaning Map becomes another verbose memo

Mitigation: keep it compact, proposition/relation based, and non-reader-facing. Do not fill it with source prose or QA commentary.

### Failure 2 — Writer still copies raw source style because source is in context

Mitigation: realization instructions explicitly make Meaning Map + Reader Plan the drafting surface; raw source is consulted only for factual/exact retrieval and later fidelity. Do not paste the current original paragraph beside every realization bundle.

### Failure 3 — Whole-document generation silently omits details

Mitigation: preserve proposition/span ownership in the Meaning Map and run post-draft coverage/fidelity repair. If full document is too large, use reader-question bundles rather than paragraph chunks.

### Failure 4 — Exact formulas/names again distort prose

Mitigation: give the realization bundle only exact identities/formulas that belong there, then repair missing exact items contextually after drafting. Never append a catch-all exact-item section.

### Failure 5 — Operation catalog becomes another template library

Mitigation: operations describe actions only. No canned target sentences.

### Failure 6 — `chinese-prose` takes over scientific decisions

Mitigation: it receives fixed meaning/constraints from the source/domain owner. It may improve expression and bounded explanation only; it may not choose a different comparison, estimand, uncertainty, or claim.

### Failure 7 — Heavy mode is used for every small text

Mitigation: explicit LIGHT / STANDARD / HEAVY routing. Captions and slide copy should not build a document plan.

### Failure 8 — Unit tests become another false quality proxy

Mitigation: tests certify deterministic boundaries; real output quality remains an artifact-level check. Do not write a fake numeric Chinese quality metric just to automate the gate.

---

## 11. Implementation order

When the user later authorizes execution, use this order.

### Phase 0 — reconcile local Round-6 failure evidence

The execution host previously reported a local-only Round-6 implementation (`faa288e`) plus uncommitted recovery changes and diagnostics. Before implementation, preserve that evidence and identify which changes are reusable versus proxy/failed work. Do not overwrite it with the remote branch.

### Phase 1 — simplify the source contracts first

Edit canonical source skills/references:

1. `scientific-rewrite/SKILL.md`;
2. `chinese-prose/SKILL.md`;
3. semantic intermediate reference;
4. operation catalog.

Do not touch Python until the intended production behavior is expressible cleanly in those sources.

### Phase 2 — reduce the helper to the new boundary

Refactor `rewrite_support.py` only after the skill contract is clear.

Goal: mechanical support, not natural-language authorship or semantic scoring.

### Phase 3 — rewrite tests to match the new mechanical contract

Tests should fail if the implementation reintroduces old required stage clutter, source-copy fallback, template-driven writer inputs, exact-token appendix repair, external generation, or privacy violations.

### Phase 4 — rebuild generated plugin parity

Run canonical marketplace generation/validation and skill audit.

### Phase 5 — production replay

Refresh the installed plugin canonically and run fresh A/B/C from one frozen implementation. Each replay child still receives only the clean task + exact source.

Primary review artifact: Markdown. Do not spend time on PDF for this style gate.

### Phase 6 — only after A/B/C are acceptable

Run the full private report through the exact same heavy path. Do not rename the plugin until 050 closes.

---

## 12. Success criteria for the redesign

The redesign is successful only if the production behavior changes in the intended way, not merely the stage schemas.

For the known A/B/C stress cases, the expected qualitative change is:

- technical identities remain intact;
- avoidable abstractions are more often replaced by the concrete scientific question/relation;
- formulas are introduced by why the reader needs them;
- method comparisons build a mental model before notation;
- no QA/glossary/token inventory leaks into reader prose;
- the writer is willing to add a short explanatory bridge when that lowers reader effort;
- source facts, caveats, uncertainty and conclusion strength remain intact;
- the final result is materially closer to the human-approved manual rewrite in reading burden, without copying that reference.

Unit tests, stage receipts and exact checks are necessary regression evidence, but they are not themselves this success criterion.

---

## 13. Decision required before a Codex prompt

The implementation decision that needs user confirmation is now narrow:

> Accept or reject the architecture change from **local source-anchored unit paraphrasing** to **Meaning Map -> Reader Plan -> whole-document/large-bundle Chinese realization -> post-draft fidelity repair**.

If accepted, the next Codex prompt should implement this plan in a bounded task. If rejected, do not continue adding reader gates or phrase rules; choose a different generation architecture first.
