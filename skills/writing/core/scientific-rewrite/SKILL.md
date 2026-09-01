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
- Section map.
- Terminology glossary.
- Cross-section definitions and dependencies.
- Claim dependencies.
- Important caveats, uncertainty, negative findings, and scope limits.
- Major conclusions.
- Literal-protected inventory.

The Document Map is not a new fact source. It only helps the local writer keep
terminology, dependencies, and reader orientation stable.

### 2. Split Into Argument Units

Rewrite by complete argument or discourse units, not by fixed token chunks.

Default unit choices:

- One complete subsection.
- Or 2-5 logically connected paragraphs.

Do not split a definition, experimental condition, result, comparison, caveat,
or conclusion in the middle merely to equalize length.

### 3. Create Meaning Card And Fidelity Ledger

For each unit, create a Meaning Card with at least:

- Audience.
- Purpose.
- Claims.
- Evidence/results.
- Conditions/comparators.
- Caveats/uncertainty/negative findings.
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

### 4. Prepare The Local Writer Packet

Each local rewrite packet should contain only bounded context:

- Compact Document Map.
- Global terminology contract.
- Relevant cross-section claims.
- Short previous rewritten tail as read-only continuity.
- Current original unit.
- Small next-source preview.
- Current Meaning Card and Fidelity Ledger.
- 3-5 selected positive transformations.

Do not put the full document, all rules, and every example into each local
writer packet.

### 5. Select Positive Transformations

Select examples by transformation metadata, not topic similarity:

- `scene`
- `discourse_function`
- `rewrite_problem`
- `fidelity_risk`
- `register`

Choose 3-5 examples that are relevant and diverse. The examples teach rewrite
operations such as "workflow label -> concrete subject/action/relation"; they
do not provide facts.

Use `references/seed-transformations.json` as the P0 seed library. Do not add
047 frozen holdout outputs, private 044 text, or project-specific 044 phrases to
this library.

### 6. Rewrite From Meaning Plus Original

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

### 7. Verify Exact Items

Run deterministic exact checks for literal invariants:

- Numbers, dates, ranges, percentages, and units.
- Citations, DOI-like strings, formulas, code spans, commands, paths, config
  keys, and identifiers.
- Formal algorithm, dataset, metric, package, product, or benchmark names when
  exact naming matters.

The helper can report exact drift, but it cannot prove semantic equivalence.

### 8. Audit Semantic Fidelity

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

### 9. Targeted Repair Only

If exact or semantic audit finds a problem, repair the affected unit only. Do
not freely rewrite the whole document again. Whole-document review may identify
terminology drift, repeated definitions, weak transitions, unclear references,
or local style outliers; fixes must return to the relevant local unit.

### 10. Chinese Language Review

Use `chinese-prose` as the language-quality review layer after fidelity gates:

- Concrete actors and actions.
- Direct relations.
- Chinese sentence skeleton rather than English workflow scaffolding.
- Natural rhythm without forced smoothness.
- Register matching for scientific or technical readers.
- Lower reader effort without weakening evidence.

The review should judge context, not blacklist hits. It must not introduce
044-specific phrase rules.

## Helper

The optional helper at `scripts/rewrite_support.py` only performs deterministic
outer-layer work:

- `prepare`: split Markdown/text into section-aware rewrite units and extract
  literal invariants.
- `select-examples`: choose seed transformations by metadata.
- `verify-exact`: compare literal invariants between source and candidate.

It does not judge naturalness, semantic equivalence, causality, uncertainty,
or claim quality.

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
