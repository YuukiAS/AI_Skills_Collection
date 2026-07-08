# Chinese Final Pass Checklist

Use this checklist for Chinese reports, READMEs, documentation, status updates, and Chinese-facing research summaries.

## Protected Spans

Before editing, protect:

- Numbers, dates, versions, units, percentages, ranges.
- Dataset names, model names, method names, package names, project names.
- Commands, code, paths, parameters, fields, config keys, logs, errors.
- Figure/table labels, metric names, experimental conditions, baselines.
- Citations, quoted text, source attribution, responsibility attribution.

During reread, verify protected spans remain unchanged.

## Fact-Preserving Rewrite

Allowed:

- Delete filler around facts.
- Split long translated sentences.
- Replace vague verbs with concrete actions.
- Move the main point earlier when the sentence buries it.
- Convert slogan-like endings into the actual next step or limitation.

Not allowed:

- Add sources, results, certainty, or causal explanations not in the input.
- Turn uncertainty into a conclusion.
- Replace a precise metric with a vague summary.
- Change who did the work or who made the claim.

## README Checks

- The opening explains what the project is.
- The target user is clear.
- Installation and quick start commands are exact.
- Features are concrete, not promotional.
- Limitations or prerequisites are not hidden.

## Report Checks

- The research question is visible.
- Evidence and interpretation are separated.
- Negative or inconclusive results remain visible.
- The next step is an action, not "继续优化".
- The conclusion is bounded by the available evidence.

## Documentation Checks

- Terms are stable across the document.
- Sections are ordered by reader workflow.
- Each paragraph has one topic.
- Lists are used for scanning, not decoration.
- Code and command text is exact.

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

## Chinese Reader Rhythm

Good Chinese technical prose usually:

- Names the subject early.
- Keeps action verbs close to subjects.
- Uses shorter sentences for conditions and caveats.
- Defines abbreviations before relying on them.
- Keeps paragraph endings concrete.
- Avoids decorative transitions.
