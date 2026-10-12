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
7. Check that the final answer still matches the actual result and the user's
   latest instruction.

## Red Flags

- The first sentence is a path, branch, status token, log line, or tool output
  instead of the answer.
- The reply says "done" when tests, install, review, upload, publish, or
  permission are still pending.
- Ordinary English words are left in a Chinese answer merely because the source
  material was English.
- A pure machine-output request is paraphrased or decorated.
- A document/report/README task stays here instead of going to `chinese-prose`
  or `scientific-rewrite`.
- Product interface copy stays here instead of going to `product-ui-copy`.
- A scientific claim is made stronger, broader, or more certain for readability.

## Output

Usually return the improved answer directly. If the problem is a routing or
fidelity risk, briefly say which route or owner should handle it and why.
