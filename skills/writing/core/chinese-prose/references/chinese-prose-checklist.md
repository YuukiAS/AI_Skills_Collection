# Chinese Final Pass Checklist

Use this checklist for Chinese reports, READMEs, documentation, status updates, and Chinese-facing research summaries.

## Automatic Final Pass

Run this checklist whenever the deliverable is a Chinese Markdown, PDF, report,
README, slide text, status note, or user-facing explanation. The user does not
need to explicitly ask for "说人话".

Before accepting the artifact as final, confirm:

- The first visible paragraph gives a reader-facing conclusion in Chinese.
- Paths, commands, branch names, status tokens, audit trails, and machine fields
  are evidence after the conclusion, not the conclusion itself.
- Mixed English process labels are either protected exact tokens or translated.
- Ordinary English abstraction labels do not carry the main semantic structure
  of Chinese sentences; the sentence explains the actual meaning in Chinese.
- A nontechnical reader from the intended audience can tell what happened, why,
  what comes next, and what should not be done yet.

## Protected Spans

Before editing, protect:

- Numbers, dates, versions, units, percentages, ranges.
- Dataset names, model names, method names, package names, project names.
- Commands, code, paths, parameters, fields, config keys, logs, errors.
- Figure/table labels, metric names, experimental conditions, baselines.
- Citations, quoted text, source attribution, responsibility attribution.
- English paper titles, formulas, variables, method names, software names,
  commands, API names, metric names, and dataset names.

During reread, verify protected spans remain unchanged.

## Fact-Preserving Rewrite

Allowed:

- Delete filler around facts.
- Split long translated sentences.
- Replace vague verbs with concrete actions.
- Move the main point earlier when the sentence buries it.
- Convert slogan-like endings into the actual next step or limitation.
- Rewrite a whole sentence or the local order of explanations when the user
  asked to make the text understandable and the facts, conditions, caveats, and
  evidence boundaries remain unchanged.
- Replace ordinary English abstractions with their actual contextual meaning in
  Chinese, not with a mechanical one-word translation.

Not allowed:

- Add sources, results, certainty, or causal explanations not in the input.
- Turn uncertainty into a conclusion.
- Replace a precise metric with a vague summary.
- Change who did the work or who made the claim.
- Preserve English sentence order or abstract labels merely because the source
  used them, when the requested output is reader-facing Chinese.

## Chinese-First Research Rewrite

For Chinese research reports, especially long Deep Research-style drafts, check
whether remaining English belongs to a protected class. Keep algorithm names,
dataset names, metric names, formulas, variables, code identifiers, paths,
paper titles, citations, and formal searchable terms. Do not automatically keep
ordinary concepts such as baseline, client, checkpoint, pooled, gap, contract,
axis, anchor, testbed, drift, estimand, or provenance when they are only
shorthand for ideas that can be stated directly in Chinese.

The rewrite should answer the meaning directly. For example, a provenance-like
phrase should become a concrete statement about which data or model state can
be confirmed and what remains unknown, not a surface translation such as
"来源追踪". A gap-like phrase should name the question the evidence has not
answered yet. A contract-like phrase should name the actual constraint. An
estimand-like phrase should name what the experiment is estimating or asking. An
anchor-like phrase should name the actual reference point, such as a shared
initial model, a common parameter value, or a jointly agreed comparison point.

If the user explicitly named an ordinary English abstraction as unwanted in
reader-facing prose, treat it as protected-negative text. It may remain only as
code, path, quoted source, paper title, table field, or truly necessary formal
term. Otherwise, rewrite the containing sentence into Chinese facts and
relationships.

Before final acceptance, scan the whole artifact, not only samples. If repeated
ordinary English abstractions still form the skeleton of reader-facing Chinese
sentences, classify the artifact as not ready even when protected spans and
style-score checks look acceptable.

Also scan for hyphenated English noun chains, slash-stacked labels, and
sentences whose grammar still says "`X aggregation` and `Y approximation` are
different". These should usually become Chinese explanations of the reference
point, information being aggregated, target being approximated, and real
difference between the two approaches. Keep such English only when it is a
paper title, algorithm name, code token, table field that must align with
external labels, or a necessary searchable formal term.

## README Checks

- The opening explains what the project is.
- The target user is clear.
- The current status is visible when the project is experimental, deprecated,
  internal, or not ready for general use.
- The opening points to more detailed documentation when quick start is not
  enough.
- Installation and quick start commands are exact.
- Features are concrete, not promotional.
- Limitations or prerequisites are not hidden.

## Report Checks

- The research question is visible.
- The first paragraph says the actual judgment before evidence paths or logs.
- Evidence and interpretation are separated.
- Negative or inconclusive results remain visible.
- The next step is an action, not "继续优化".
- The conclusion is bounded by the available evidence.
- Scientific claims distinguish existing data, user-confirmed decisions,
  contextual inference, and suggested next steps.
- Words such as "显著", "先进", "有效", and "鲁棒" have conditions, baselines,
  ranges, or are removed.

## Documentation Checks

- Terms are stable across the document.
- Sections are ordered by reader workflow.
- Each paragraph has one topic.
- Lists are used for scanning, not decoration.
- Code and command text is exact.
- Ordinary English words such as audit, pipeline, candidate, reviewer, final
  artifact, and status are translated unless they are exact machine tokens.

## Markdown/PDF Checks

- The visible title and first paragraph are useful to a reader, not only to an
  execution log.
- Evidence paths, commands, tables, and machine-readable fields are grouped
  after the conclusion.
- The PDF or rendered Markdown does not expose scratch notes, checklist
  fragments, or internal task-contract language as the main message.
- Remaining English spans are classified as protected exact tokens, recognized
  technical names, or text that should be translated.

## AI-Taste Audit

Flag and fix:

- Empty openings and closing summaries.
- Vague significance claims.
- Slogan-like phrases.
- Mechanical "首先/其次/最后" when not needed.
- Forced three-part lists.
- Unsupported "研究表明" or "专家认为".
- Long translated clauses that start with "基于/通过/为了".
- Mixed formal, internet, and marketing voice in the same paragraph.
- Machine-process openings such as "audit result", "candidate output",
  "pipeline status", or "final artifact" when a Chinese conclusion is needed.

## Chinese Reader Rhythm

Good Chinese technical prose usually:

- Names the subject early.
- Keeps action verbs close to subjects.
- Uses shorter sentences for conditions and caveats.
- Defines abbreviations before relying on them.
- Keeps paragraph endings concrete.
- Avoids decorative transitions.
