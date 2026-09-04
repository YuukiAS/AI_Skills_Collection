---
name: scientific-rewrite
description: Internal Writing Style route for high-fidelity Chinese scientific and technical long-form rewriting from existing source text, with meaning cards, literal/semantic fidelity ledgers, exact checks, and Chinese language review.
status: active
provenance: local
trusted: false
requires_network: false
writes_files: true
executes_code: true
secrets_needed:
last_reviewed: 2026-09-01
profile_tags:
  - writing
  - global
recommended_scope: global
icon_small: assets/app-facing.svg
icon_large: assets/app-facing.svg
license: MIT-compatible local synthesis; selective architecture patterns distilled from MIT sources recorded in docs/provenance/INTEGRATION_HISTORY.md
---
# Scientific Rewrite

This skill is the heavy Chinese scientific rewrite route inside `writing-style`.
It rewrites an existing scientific or technical document into clearer Chinese
without changing the document's meaning, facts, evidence boundaries, or
scientific force.

It is not a generic humanizer, AI detector workaround, summarizer, manuscript
planner, or research-report generator. Use `research-reporting` when the user
wants a new report from project evidence. Use `chinese-prose` for short or
light Chinese polishing. Use `scientific-prose` for English scientific prose.
Use `writing-fidelity` alone when the task is only to audit numbers, formulas,
versions, citations, or protected spans.

For an explicit heavy scientific rewrite or "说人话重写", this route carries
`STRUCTURAL_REWRITE_AUTHORIZED_BY_TASK` to `writing-fidelity`. That handoff
means content fidelity is not source-order fidelity: preserve the
content/evidence graph, not the original reader-facing headings, paragraph
grouping, paragraph order, section order, or table order unless the user
explicitly protected that structure.

## When To Use

Use this route when all of these are true:

- The source is an existing Chinese or Chinese-dominant scientific/technical
  document, report, Markdown file, README section, or long explanation.
- The user wants meaning-preserving rewriting, not a summary or a new document.
- The request mentions natural Chinese, "说人话", easier reader effort, less
  log-like wording, less translationese, or removing internal workflow language.
- The user also requires scientific fidelity: numbers, formulas, citations,
  formal names, caveats, uncertainty, attribution, comparisons, and conclusion
  strength must not drift.
- The text is more than a small local polish; a full subsection or multiple
  connected paragraphs need rewriting.

Typical trigger requests include:

- "把这份中文科研长报告重新讲得自然一点，但数字、公式、引用和结论都不能变。"
- "这篇技术报告内容是对的，但太像运行日志了，按原意重新写成人能连续读的中文。"
- "不要总结，也不要删限制条件；把这几节科研说明说人话。"
- "保留算法名和数据集名，把其余中英混杂的内部工作流语言改成正常科研中文。"
- "这份结果报告事实不能动，但标题、句法和解释顺序可以重写，让第一次看的研究者能直接理解。"
- "按原文逐条保留 claim/caveat，把长段落重新组织得更清楚。"
- "把整份 Markdown 科研报告做一次高保真自然重写，不是局部润色。"

Do not trigger this route for:

- "帮我从这些实验结果新写一份组会报告。" Route to `research-reporting`.
- "把这两句中文润色一下/改顺一点。" Route to `chinese-prose`.
- "润色这段英文 Results/caption。" Route to `scientific-prose`.
- "帮我规划整篇论文结构/写 rebuttal。" Route to `research-paper-workflow`.
- "只检查数字、版本、公式有没有被改。" Route to `writing-fidelity`.

## Authority Order

The original source text is the highest authority. A Meaning Card, reader
takeaway, Document Map, seed example, or rewritten draft cannot introduce facts
that are not present in the original source or an explicitly authorized factual
source.

Use this authority order:

1. User's latest instruction and explicit no-touch spans.
2. Original source unit being rewritten.
3. Authorized factual sources supplied by the user.
4. Document Map and terminology contract derived from the source.
5. Meaning Card and Fidelity Ledger derived from the current unit.
6. Seed transformations as style-operation examples only.

Never borrow facts, entities, numbers, datasets, algorithms, or scientific
claims from examples.

## Workflow

### 1. Build A Compact Document Map

Before local rewriting, build a compact map for the whole document:

- Audience.
- Document purpose.
- Reader questions the document must answer.
- Section map.
- Terminology glossary.
- Cross-section definitions and dependencies.
- Claim dependencies.
- Evidence classes: project facts, literature facts, research interpretation,
  candidate methods, and still-unverified items.
- Important caveats, uncertainty, negative findings, and scope limits.
- Major conclusions.
- Literal-protected inventory.

The Document Map is not a new fact source. It only helps the local writer keep
terminology, dependencies, and reader orientation stable.

### 2. Build A Host Reader Plan

For heavy structural rewrite, the host Codex session must turn the Document Map
into a Reader Plan before drafting. The plan is not a new research plan and does
not change claims; it decides how a reader should encounter the existing
evidence graph.

The Reader Plan should record:

- the reader questions the final document must answer;
- the order in which those questions should be answered;
- the source spans or propositions that answer each question, including
  non-contiguous spans when needed;
- whether each bundle should become prose, a short list, a table, a formula
  walkthrough, or technical trace;
- where explanation should expand, split, or move because reader effort would
  otherwise be high;
- which English spans are exact identities, useful first-use recognition, or
  ordinary reasoning language that should become Chinese;
- epistemic roles when they matter: project fact, literature fact, research
  interpretation, candidate method, or still-unverified item.

Deterministic code may validate that this host-authored plan exists, binds the
current Document Map, covers source spans exactly once, and is consumed by final
assembly. It must not synthesize the plan.

### 3. Split Into Reader-Oriented Argument Bundles

Rewrite by complete argument or discourse units, not by fixed token chunks.

Default unit choices:

- One complete subsection.
- Or 2-5 logically connected paragraphs.
- Or non-contiguous bounded spans when they answer the same scientific reader
  question and the argument plan records exact source-span ownership.

Do not split a definition, experimental condition, result, comparison, caveat,
or conclusion in the middle merely to equalize length.

The output order of argument units may differ from source order. Every source
span must still be accounted for exactly once, unless a duplicate is explicitly
marked as a cross-reference rather than new ownership.

### 4. Create Meaning Card And Fidelity Ledger

For each unit, create a Meaning Card with at least:

- Audience.
- Purpose.
- Claims.
- Evidence/results.
- Conditions/comparators.
- Caveats/uncertainty/negative findings.
- Evidence class for each semantic item: project fact, literature fact,
  research interpretation, candidate method, or still-unverified item.
- Literal-protected items.
- Terminology.
- Relation to previous/next argument.
- Reader takeaway.

Then create a Fidelity Ledger:

- Literal preservation: exact tokens that must stay unchanged.
- Semantic preservation: relations and claims that may be rephrased completely
  but cannot change meaning.
- Claim/relation status after rewriting: `preserved`, `narrowed`,
  `broadened`, `reversed`, `invented`, `omitted`, or `reattributed`.

Run a source-to-Meaning-Card coverage check before rewriting. If an important
proposition appears in the source but cannot be found in the Meaning Card, stop
and repair the Meaning Card before writing.

Do not create a production Meaning Card by copying source excerpts into
`normalized_meaning`, `plain_meaning`, claims, evidence, or reader takeaway.
If host-produced semantic artifacts are absent, malformed, or source-copy
fallbacks, fail and repair them in the current host-Codex workflow.

### 5. Execute The Host-Codex Stage Workflow

For long-form production rewrites, the current host Codex session performs the
semantic and writing work. Create observable stage artifacts as the work
proceeds, then validate them with the deterministic helper before treating the
route as complete:

```bash
python3 skills/writing/core/scientific-rewrite/scripts/rewrite_support.py validate-host-stage \
  --source SOURCE.md \
  --stage-dir stage_packets \
  --candidate stage_packets/final_candidate.md \
  --receipt stage_packets/stage_receipt.json
```

The private stage package should include `document_map.json`,
`reader_plan.json`, `argument_units.json`, `meaning_cards/<unit>.json`,
`fidelity_ledger.json`, `selected_transformations.json`,
`candidate_units/<unit>.md`, `self_audit.json`,
`chinese_reader_pass.json`, and `final_candidate.md`. The receipt must show
that document mapping, Reader Plan, argument bundles, Meaning Cards, selected
transformations, unit candidates, self-audit, final assembly, and the Chinese
reader pass form a real dataflow. A single whole-document writer call is not
valid production execution for this route.

The host-authored self-audit must include global assembly evidence showing how
the final reader order was chosen from the document map, reader priorities,
argument plan, unit cards, unit candidates, and cross-section dependencies. The
final assembly may merge or move units, introduce reader-facing headings, place
formulas near their explanation, convert repeated method prose into a table, and
move only relocatable trace into a meaningful appendix.

Do not call OpenAI/Terra or `text-transform` for document mapping, Reader Plan,
Meaning Cards, writing, semantic audit, repair, assembly, or Chinese reader
pass. Optional external review, when a frozen task explicitly authorizes it, is
candidate-only QA after local generation and is not a production generation
dependency.

### 6. Prepare The Local Writer Packet

Each local rewrite packet should contain only bounded context:

- Compact Document Map.
- Global terminology contract.
- Relevant cross-section claims.
- Short previous rewritten tail as read-only continuity.
- Current original unit.
- Small next-source preview.
- Current Meaning Card and Fidelity Ledger.
- The Reader Plan bundle that owns this unit, including reader question,
  information shape, expansion policy, and English-span classification.
- 2-4 selected positive transformations.

Do not put the full document, all rules, and every example into each local
writer packet.

### 7. Select Positive Transformations

Select examples by transformation metadata, not topic similarity:

- `scene`
- `discourse_function`
- `rewrite_problem`
- `fidelity_risk`
- `register`

Choose 2-4 examples that are relevant and diverse. The examples teach rewrite
operations such as "workflow label -> concrete subject/action/relation"; they
do not provide facts.

Use `references/seed-transformations.json` as the P0 seed library. Do not add
047 frozen holdout outputs, private 044 text, or project-specific 044 phrases to
this library.

### 8. Rewrite From Meaning Plus Original

Rewrite the unit from the Meaning Card and original unit together. The output
should read as normal Chinese scientific prose:

- Put the real subject and action early.
- Explain why a term matters before relying on it.
- Replace internal workflow labels with reader-facing relations where meaning
  allows.
- Keep formal names, datasets, methods, metrics, citations, code, paths, and
  exact identifiers unchanged when exact naming matters.
- Preserve caveats, uncertainty, negative findings, comparators, attribution,
  and conclusion strength.
- Prefer ordinary sentences over slogans, posture, or decorative structure.
- State the bounded research judgment before the caveat when the source permits
  it, then keep the caveat nearby so the claim is not strengthened.
- For ordinary reasoning and organization language, use natural precise Chinese
  when English adds no external identification value. Keep exact formal names
  when they identify a method, dataset, metric, package, API, citation, command,
  path, or statistical term.
- For reader-facing formulas, normally write: what question or intuition the
  formula captures -> the exact protected formula -> what the important symbols
  mean -> what comparison or conclusion the formula supports.
- For large method comparisons, first identify the decision question, then group
  methods by the relevant mechanism, communicated information, statistical
  object, or resource assumption. Keep complete facts in prose or a table.
- Optimize for minimum reader inference burden, not minimum characters. A local
  section may become longer when it adds necessary explanation, splits parallel
  conditions, introduces a formula, or turns dense comparisons into a table or
  list.

### 9. Verify Exact Items

Run deterministic exact checks for literal invariants:

- Numbers, dates, ranges, percentages, and units.
- Citations, DOI-like strings, formulas, code spans, commands, paths, config
  keys, and identifiers.
- Formal algorithm, dataset, metric, package, product, or benchmark names when
  exact naming matters.

The helper can report exact drift, but it cannot prove semantic equivalence.

An `inline-critical` item must appear in the reader-facing scientific context.
Presence only in technical trace, token inventory, receipt, or appendix is still
a failure. Only `relocatable-trace` items may live in a technical/evidence
appendix, and that appendix must contain host-written contextual meaning rather
than a raw literal list.

### 10. Audit Semantic Fidelity

Independently audit claims and relations. Report exact source and candidate
evidence for every issue. The audit must distinguish:

- `preserved`
- `narrowed`
- `broadened`
- `reversed`
- `invented`
- `omitted`
- `reattributed`

Critical violations must be zero before judging naturalness. Critical examples:
wrong number, formula or citation corruption, claim polarity reversal, omitted
caveat, changed comparator, erased uncertainty, conclusion-strength upgrade,
wrong attribution, or invented scientific fact.

### 11. Targeted Repair Only

If exact or semantic audit finds a problem, repair the affected unit only. Do
not freely rewrite the whole document again. Whole-document review may identify
terminology drift, repeated definitions, weak transitions, unclear references,
or local style outliers; fixes must return to the relevant local unit.

Deterministic helper code must not append missing literals into reader-facing
text, create a "保留原文精确项" list, or write semantic repair prose. Missing
inline-critical or relocatable-trace findings go back to host Codex for
contextual repair, then exact verification runs again.

### 12. Candidate-Only Reader Review

Run a reader review that sees only the candidate and audience description, not
the original source. It must answer whether a technically trained reader can
state the research problem, current evidence, remaining uncertainty, next
comparison or experiment, and GO/STOP consequence without decoding internal
audit vocabulary.

The review has two dimensions:

- `answerability`: can the reader recover the intended scientific answer?
- `reader_effort`: does a normal first read present that answer directly, with
  enough local explanation and the right information shape?

Do not let source-aware fidelity review substitute for this reader review.

### 13. Chinese Language Review

Use `chinese-prose` as the language-quality review layer after fidelity gates:

- Concrete actors and actions.
- Direct relations.
- Chinese sentence skeleton rather than English workflow scaffolding.
- Natural rhythm without forced smoothness.
- Register matching for scientific or technical readers.
- Lower reader effort without weakening evidence.

The review should judge context, not blacklist hits. It must not introduce
044-specific phrase rules.

For heavy structural rewrite this is an observable terminal pass. The host
Codex session writes a candidate-only Chinese reader pass that classifies
remaining English spans as exact identity, useful first-use recognition, or
ordinary reasoning; checks that reader effort was not optimized as compression;
checks formula context and evidence-role boundaries; then repairs affected
reader-facing blocks before exact and semantic verification run again.

## Helper

The optional helper at `scripts/rewrite_support.py` only performs deterministic
outer-layer work:

- `split_markdown_units` / `proposition_inventory`: mechanically prepare
  bounded argument-unit and proposition identifiers for the host Codex workflow.
- `select-examples`: choose seed transformations by metadata.
- `verify-exact`: compare literal invariants between source and candidate.
- `validate-host-stage`: validate host-authored private stage artifacts and
  write a privacy-safe receipt.

It does not judge naturalness, semantic equivalence, causality, uncertainty,
claim quality, or reader effort, and it never writes reader-facing Chinese prose
or source-copy semantic fallback content.

Example:

```bash
python3 skills/writing/core/scientific-rewrite/scripts/rewrite_support.py select-examples \
  --scene scientific-report \
  --discourse-function result-interpretation \
  --rewrite-problem workflow-language \
  --fidelity-risk high \
  --register formal-technical
```

## Completion Standard

A scientific rewrite is acceptable only when:

- Source-to-Meaning-Card coverage is complete for important propositions.
- Literal exact checks pass or every drift is explicitly authorized.
- Semantic audit has zero critical violations.
- Candidate-only facts, numbers, entities, datasets, algorithms, and claims all
  trace back to the source or authorized factual sources.
- The rewritten text is easier for the intended reader without deleting
  constraints, uncertainty, negative findings, or conclusion boundaries.
- The whole-document pass finds no terminology drift, repeated-definition
  confusion, or late conclusion-strength changes.
