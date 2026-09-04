# 050 STYLE_REJECT — round-2 artifact diagnosis

## Decision

`STYLE_REJECT` remains the product decision for the second A/B/C smoke.

This rejection is narrower than round 1. The second smoke shows that the selected 050 architecture is now directionally correct: structural reorganization is visible, formulas are back in scientific context, the raw exact-literal/token-dump appendix failure is no longer the dominant artifact, and the three smoke roles expose the intended research questions more directly.

The remaining product failure is reader effort. The output still reads like a compressed bilingual research memo rather than the successful manual readability rewrite used as reference. Do not redesign 050 or reopen paid-review infrastructure. Repair the reader-facing writing contract and the host-Codex stage responsibilities.

No private smoke plaintext is recorded here.

## Why the manual rewrite is materially better

The successful manual rewrite did not merely replace awkward words. It changed the information architecture and the amount of explanation supplied to the reader.

Generic capabilities demonstrated by the manual baseline:

1. **Reader-question organization.** Scattered source material that jointly answers one scientific question is regrouped even when it originally appears in different sections.
2. **Fidelity of the evidence graph, not source order.** Claims, evidence, caveats, uncertainty, attribution, formulas, numbers and decision boundaries remain stable while headings, paragraph grouping, table organization and section order may change.
3. **Epistemic boundaries are visible.** Project facts, literature facts, research interpretation, candidate methods and still-unverified items remain distinguishable in the prose.
4. **Formula narrative.** The reader gets the intuition/question first, then the exact formula, then an explanation of the important symbols and what conclusion/comparison follows.
5. **Decision-centered literature organization.** A large method catalog is reorganized around the decision the document must make, rather than preserved as a flat source-order table/list.
6. **Proper names stay recognizable; ordinary reasoning becomes Chinese.** Algorithm/dataset/package names remain exact, while ordinary organizational and inferential language is expressed in natural Chinese when English adds no identification value.
7. **Bounded conclusion before qualification.** The scientific judgment appears early; the caveat that limits it stays nearby instead of making the reader decode audit/provenance language before learning the point.
8. **Readability is not compression.** The manual rewrite is allowed to become longer locally when explanation, grouping, a table, a short list, or an extra heading reduces cognitive load. Shorter is not an acceptance metric.
9. **Information morphology may change.** Dense parallel counts become a table; GO/STOP conditions become a list; method families may become grouped subsections; repeated facts may be consolidated once without losing coverage.

## Why round 2 still fails

### 1. The plugin-level product description still biases toward polishing, not structural explanation

The generated `writing-style` plugin describes itself as a writing-quality/polishing layer and explicitly says it operates without research-structure decisions. That is appropriate for ordinary polishing but too restrictive for an explicitly requested heavy scientific rewrite.

For heavy `scientific-rewrite`, the plugin must distinguish:

- changing scientific claims/research decisions: **not allowed**;
- changing reader-facing document structure to explain the same evidence graph: **allowed and required when it lowers reader effort**.

The profile/default prompts should expose that distinction so the installed entrypoint is not semantically biased toward local polish.

### 2. `scientific-rewrite` still needs an explicit global Reader Plan

A Document Map is not enough. The host needs to decide before drafting:

- which reader questions the document must answer;
- the order in which those questions should be answered;
- which source spans/propositions belong to each reader question, including non-contiguous spans;
- which material should be expanded, collapsed, tabulated, listed, or moved to trace;
- which formulas require an intuition/variable/implication wrapper;
- which terms are exact proper names and which are ordinary reasoning language that should be natural Chinese.

This must be a host-Codex semantic artifact consumed by unit writing and final assembly. It must not be synthesized by deterministic code.

### 3. Unit writing is still too strongly optimized for compressed `formal-technical` prose

The current seed transformations and writer contract favor concise formal-technical rewrites. That produces grammatically valid but cognitively dense prose.

Heavy say-it-plain scientific rewriting needs a reader-facing scientific register: rigorous but explanatory. The writer must be allowed to add connective explanation, split a dense paragraph, introduce a useful subheading/list/table, and repeat a small amount of local context when that lowers inference burden.

The model must not be rewarded for minimizing character count.

### 4. `chinese-prose` has the right principles, but they are not an observable terminal gate

`chinese-prose` already says Chinese final output should be Chinese-first and that ordinary English concepts should be translated when removal loses no precision/identification value. Round 2 still contains many ordinary English reasoning/scaffolding phrases, which proves those rules are not reliably governing the heavy production output.

The heavy route therefore needs a real host-Codex Chinese reader pass after global assembly. It should consume the assembled candidate and a compact Chinese-language contract, then repair only reader-facing language/organization while leaving exact proper names and evidence semantics unchanged.

This is not a phrase blacklist and not a separate paid model call.

### 5. Proper-name preservation and English-reasoning preservation are currently conflated

Formal method/dataset/package names must remain exact. Ordinary concepts do not gain scientific authority by remaining English.

The host should classify remaining English spans by function:

- exact identity/proper name -> preserve;
- useful first-use recognition -> explain in Chinese and optionally keep English once;
- ordinary reasoning/organization -> express naturally in Chinese.

Do not use a fixed banned-word list. The classification is semantic and contextual.

### 6. Evidence boundaries need a local prose contract

The manual baseline makes it easy to tell whether a statement is a project fact, literature fact, research interpretation, candidate method, or unverified item. Round 2 preserves many caveats but often places literature description, project interpretation and future-method judgment in the same dense paragraph.

Meaning Cards / Reader Plan should carry an epistemic role for claims where relevant, and assembly should preserve that role in natural prose or compact labels. The exact visible labels are optional; the distinction is not.

### 7. Candidate-only review currently overvalues answerability

The smoke questions can be answerable while the prose is still unpleasant to read. A reader should not need to mentally translate ordinary English scaffolding, unpack noun stacks, or reconstruct a five-condition decision from one dense paragraph.

The host-Codex reader pass must judge both:

- **answerability**: can the reader recover the scientific answer?
- **reader effort**: does a normal first read present that answer directly, with enough local explanation and useful visual/text structure?

No automatic numeric readability metric is needed. Human style acceptance remains final authority.

## Layer-by-layer repair target

### A. Plugin metadata / profile / default prompt

Repair the heavy-rewrite description so it explicitly allows reader-facing structural reorganization without giving writing-style authority to change scientific claims or research decisions.

Do not broaden light polishing behavior.

### B. `scientific-rewrite/SKILL.md`

Add/strengthen these production contracts:

- global Reader Plan before drafting;
- non-contiguous source grouping when one reader question requires it;
- readability != compression;
- information morphology may change (paragraph/list/table/subheading) when fidelity is preserved;
- formula narrative;
- semantic classification of English proper names vs ordinary reasoning;
- epistemic-role preservation;
- mandatory final Chinese reader pass after global assembly.

### C. Meaning Card / Fidelity Ledger reference

Keep claim/evidence/caveat/uncertainty/attribution protection. Add only the minimum semantics needed to prevent the observed failures:

- reader question / local reader job;
- epistemic role where relevant;
- whether a formula requires explanation in reader core;
- whether dense parallel information is better represented as prose/list/table;
- expansion/compression permission driven by reader effort, not target length.

Do not make this a second document-planning system.

### D. Positive style contract / seed transformations

Keep the library small. Add generic transformation classes demonstrated by the manual baseline:

- scattered evidence -> one reader-question bundle;
- dense logical paragraph -> bounded explanatory sequence;
- formula -> intuition + formula + variable/implication;
- flat method catalog -> decision question + mechanism groups + complete detail;
- parallel numeric/entity facts -> table/list when that lowers lookup effort;
- ordinary English reasoning scaffold -> precise Chinese relation;
- bounded conclusion -> nearby caveat.

Prefer operation examples over polished slogans/templates that encourage formal memo prose.

### E. `chinese-prose`

Do not duplicate the entire skill. Define an explicit heavy-route handoff/terminal pass so its existing Chinese-first/reader-facing principles are actually consumed by `scientific-rewrite` production.

The terminal pass must preserve exact names and factual authority while being allowed to split/reorder reader-facing sentences/paragraphs within the already approved Reader Plan.

### F. `writing-fidelity`

Preserve the round-1 fixes: structural rewrite is allowed when explicitly authorized, inline-critical cannot be satisfied only in an appendix, and exact preservation is not positional preservation.

Do not reopen the raw token restoration path.

Add no new restriction that forces the repaired output back toward source order or sentence-local paraphrase.

### G. deterministic helper

Keep deterministic responsibilities mechanical only. It may validate the Reader Plan/Meaning Cards/coverage and exact items, but must not write semantic content or Chinese repair prose.

Preserve the removal of raw literal token-dump repair and project-specific phrase hacks.

Where practical, validate that the final host-produced Reader Plan/assembly really differs from source order when it claims structural reorganization, but do not require reordering on every document.

### H. final host-Codex assembly + Chinese reader pass

Final assembly must consume the Reader Plan rather than merely concatenate unit candidates.

After assembly, perform one host-Codex candidate-only Chinese reader pass that asks:

- what is the bounded point of each section?
- are ordinary logical relations natural Chinese?
- are exact proper names preserved?
- does every important formula have enough local interpretation?
- are long parallel conditions better expressed as a list/table?
- are evidence classes/uncertainty distinguishable?
- is a conclusion buried behind process/provenance language?
- is text overly compressed even though technically answerable?

Repairs return to affected blocks, then exact/semantic verification runs again.

## Do not do

- no new architecture task / no 051;
- no Terra/OpenAI generation;
- no phrase blacklist;
- no CARE/ODAL/FedFisher-specific production rule;
- no AI-detector/readability score optimization;
- no character-count compression target;
- no reopening the token-dump appendix behavior;
- no source-copy semantic fallback;
- no hand-editing smoke candidates;
- no weakening of formulas, claims, uncertainty or decision boundaries.

## Round-3 human acceptance target

The next A/B/C should be rejected before user handoff if any of these are still true:

1. ordinary English reasoning vocabulary still carries the sentence skeleton;
2. a dense five-part decision remains a single paragraph when a list/table would be substantially easier to read;
3. formulas appear without enough local intuition/meaning;
4. literature fact, project fact, interpretation and candidate method blur into one voice;
5. the final assembly is materially just source-order/unit-order concatenation despite a structural-rewrite claim;
6. the text is shorter but harder to read because explanatory bridges were removed;
7. any raw literal inventory/token dump reappears;
8. any private smoke plaintext enters Git;
9. automated PASS is used to override human style judgment.

Round 3 remains the same fixed A/B/C regression input. If this bounded reader-facing repair still fails, return to Planner with evidence rather than adding another project-specific rule layer.
