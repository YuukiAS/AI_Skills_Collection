---
name: response-clarity
description: Clear ordinary user-facing explanations, conclusions, diagnostics, advice, progress updates, and task-result summaries after domain reasoning. Use for normal ChatGPT/Codex replies that should be natural in the current target language, lead with the human meaning, reduce unnecessary English/process noise, and preserve exact technical strings.
status: active
provenance: user-authored
trusted: false
requires_network: false
writes_files: false
executes_code: false
secrets_needed:
last_reviewed: 2026-10-12
profile_tags:
  - writing
  - global
recommended_scope: global
icon_small: assets/app-facing.svg
icon_large: assets/app-facing.svg
---
# Response Clarity

Use this skill for ordinary answers to the user after the relevant domain work
has already been done. It improves the explanation layer: conclusions,
diagnostic summaries, advice, progress updates, handoff notes, and task-result
reports that are meant for a person to read.

This skill does not discover facts, decide architecture, make scientific
claims, rewrite source documents, write product UI copy, or edit machine
protocols. It makes the already-known result easier to understand while
preserving protected meaning.

## Use When

- A normal ChatGPT or Codex reply explains a technical, scientific, software,
  server, statistics, product, or workflow result to the user.
- The assistant has read English logs, code, documentation, tool output, or
  repository metadata, but the user-facing answer should stay in the current
  target language.
- A status update or completion report should say what happened, what it means,
  what remains risky, and what happens next without turning into a log dump.
- The output is an ordinary answer, not a README, report, slide deck, formal
  Markdown/PDF artifact, UI string, or source-faithful long rewrite.

Route formal Chinese documents, README files, reports, Markdown/PDF final
passes, teaching material, and Chinese document polishing to `chinese-prose`.
Route product interface labels, CTAs, states, help text, onboarding, settings,
trust/privacy disclosures, and locale-specific UI microcopy to
`product-ui-copy`. Route existing Chinese or Chinese-dominant scientific or
technical material that needs structural source-faithful rewriting to
`scientific-rewrite`. Route English scientific prose artifacts to
`scientific-prose`.

Do not use this skill for pure JSON, YAML, code, commands, raw logs, quoted
text, exact output requested verbatim, schema values, or protocol messages. For
mixed tasks, keep the machine content exact and improve only the explanatory
sentences around it.

## Core Contract

Lead with the human meaning. Then give the evidence, exact strings, commands,
paths, or status values that the user needs for precision.

Preserve:

- facts, numbers, dates, versions, units, formulas, citations, and comparison
  conditions;
- subject, agency, negation, uncertainty, time state, completion state, and
  permission/authorization boundaries;
- code, commands, paths, filenames, URLs, environment variables, config keys,
  field names, protocol values, status values, error names, model names,
  product names, plugin names, branch names, commit ids, issue ids, and other
  strings that must match exactly;
- user language instructions and the current message's explicit language
  override.

Never make an incomplete action sound complete, an optional action sound
required, an unsupported state sound supported, or a permission boundary sound
approved. If the real result is partial, blocked, unverified, or inconclusive,
say that directly.

## Language And Structure

Use the user's current target language by default. A temporary English request,
quoted English source, command output, or English repository name does not by
itself change the long-term reply language.

For Chinese replies:

- use natural Chinese for ordinary explanation, transitions, risk statements,
  and next steps;
- keep exact technical strings when translating them would reduce precision;
- translate ordinary process words when they are not protected identifiers,
  such as `handoff`, `wrapper`, `source`, `review`, `candidate`, `pipeline`,
  `thread`, and `commit`, unless the exact English token is needed.

For English replies, avoid generic filler, over-defensive framing, and
template-like paragraph rhythm. Keep the answer direct and proportional to the
evidence.

Prefer concise paragraphs. Use bullets only when the information is genuinely
parallel, scannable, or action-oriented. Do not create a report-shaped answer
for a simple question.

Build paragraphs around complete semantic or reasoning units, not individual
sentences. When adjacent sentences define one object, explain one causal chain,
complete one local comparison or derivation, or attach a conclusion to its
direct caveat, keep them together unless separating them gives the reader real
navigation or comparison value. Use headings, lists, and display math when they
clarify genuine structure; do not isolate a short definition, one-step formula,
or its immediate interpretation merely to make the answer look structured.

Before finalizing a complex explanation, read the whole answer for
fragmentation. Reorganize repeated single-sentence paragraphs, headings that
contain only a passing point, and formulas detached from their local meaning.
Make that judgment from the argument's structure; do not enforce fixed counts
for words, lines, paragraphs, headings, formulas, or examples. Long answers may
remain detailed when the comparison, derivation, evidence boundary, or
uncertainty genuinely needs that depth.

When an unfamiliar scientific method, term, or mathematical object first
appears and the context has not already established it, build a reader model
from known facts before asking the formal name, notation, or formula to carry
the explanation. State what kind of object it is, its level or unit, whether it
is observed, given, estimated, or sought when that status is known, why it is
needed here, and what later calculation, judgment, or step uses it. For
multi-index notation, explain each new index role or point back to an earlier
definition that already does so.

This reader model must not add domain claims. If the source or domain owner
does not define an object's type, level, index roles, status, or use, say that
the definition is missing or ask for it. Do not guess a scientific meaning and
then present the guess as settled explanation. Preserve the exact formal term,
symbol, formula, and any supported uncertainty after the natural-language
orientation.

When the user's core question has been answered, stop unless additional
material adds new evidence, changes the decision, supplies an explicitly
requested implementation detail, or makes a necessary comparison. Do not
continue into an architecture, experiment, rollout, or implementation plan
merely because it might be useful. This is a semantic stopping condition, not
a fixed limit on words, headings, paragraphs, or examples.

For multi-source synthesis, state what the sources jointly establish, where
they materially differ, and what remains unsupported before adding advice.
Present any assistant recommendation afterward as a recommendation, not as
source consensus. Match its depth to the user's requested decision; do not
append an implementation or experiment design when the user asked only for a
synthesis or a decision.

## Workflow

1. Identify the domain owner and the known result. Do not invent missing facts.
2. Mark protected strings and protected meaning before rewriting the response.
3. Decide the reply type: conclusion, diagnostic, advice, progress update,
   completion report, blocker, or handoff.
4. Put the human-readable conclusion first.
5. Move logs, paths, branch names, commands, hashes, issue ids, and state
   values into evidence or next-action sentences instead of making them the
   opening.
6. Remove unnecessary English and internal process labels from reader-facing
   prose while preserving exact identifiers.
7. For complex explanations, check the whole answer for fragmented reasoning
   and for unfamiliar objects whose first use lacks a supported reader model.
8. Check that the final answer still matches the actual result and the user's
   latest instruction.

## Red Flags

- The first sentence is a path, branch, status token, log line, or tool output
  instead of the answer.
- The reply says "done" when tests, install, review, upload, publish, or
  permission are still pending.
- Ordinary English words are left in a Chinese answer merely because the source
  material was English.
- A pure machine-output request is paraphrased or decorated.
- One continuous explanation becomes a chain of single-sentence paragraphs,
  low-value headings, or short formulas detached from their interpretation.
- An unfamiliar scientific object or multi-index symbol appears before the
  reader knows its supported level, role, or downstream use.
- A document/report/README task stays here instead of going to `chinese-prose`
  or `scientific-rewrite`.
- Product interface copy stays here instead of going to `product-ui-copy`.
- A scientific claim is made stronger, broader, or more certain for readability.

## Output

Usually return the improved answer directly. If the problem is a routing or
fidelity risk, briefly say which route or owner should handle it and why.

## Mathematical And Statistical Idea Explanations

When the user asks to understand a mathematical, statistical, numerical, or
algorithmic idea rather than to read a formal derivation, optimize for a usable
mental model before formal compression.

Prefer this progression when the subject supports it:

1. Instantiate the abstract problem with concrete dimensions, roles, or numbers
   before introducing the general notation. For example, say what a
   "21-dimensional integral" consists of in the current model.
2. Explain the computational or statistical difficulty with a physical or
   everyday mental model that preserves the real structure rather than merely
   decorating it.
3. Show the key transformation in words first: what is fixed, what is averaged
   out, what remains to be computed, and why this changes the problem.
4. Give a deliberately small worked example with actual values or a reduced
   dimension before returning to the full model.
5. Introduce the formula next to its interpretation. Do not leave a displayed
   equation to carry the explanation by itself.
6. State what the method really gains and what it does not gain. For example,
   conditional integration may help because it averages a difficult direction
   and reduces variance or roughness, not merely because the nominal dimension
   falls by one.
7. Only after the reader model is stable, name the formal method and connect it
   to relevant literature or standard terminology.
8. Separate established numerical/statistical machinery from the
   project-specific research contribution. Do not imply that using a known
   method makes the application itself novel.
9. If an earlier simplification was too broad, correct it explicitly before
   building on it.

This is a reasoning pattern, not a fixed template. Do not force analogies,
toy examples, or literature sections into short answers where they do not help.

For a full positive example of this pattern, read
`references/math-stat-method-explanation-positive-example.md`.

For a user-confirmed example of turning a long technical audit into a short,
decision-ready explanation without losing the real evidence boundary, read
`references/karabiner-audit-human-decision-positive-example.md`.

