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

Use this skill to select, organize, write, and revise ordinary answers from
supported domain work: explanations, comparisons, advice, progress updates,
handoffs, and task-result reports. Start with the user's question and the
reader's understanding needs before drafting, not with a prewritten result
whose wording alone can be polished.

This skill does not discover facts, decide architecture, make scientific
claims, rewrite source documents, write product UI copy, or edit machine
protocols. Domain owners establish facts and decisions; this skill owns which
supported material belongs in the answer and how the reader can understand it.

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

1. Read the latest user question. Identify the questions to answer, audience,
   target language, requested depth and output type, and any actual action or
   verbatim output required. A short status and a full proof require different
   depths; neither inherits its length from how much material was inspected.
2. Separate the evidence pool from the answer's content. Keep domain-verified
   facts available for reasoning, but select for the answer only what answers
   the question, establishes a necessary mechanism or mathematical intuition,
   affects confidence/completion/risk, supports action or reproduction, or is
   explicitly requested. Preserve protected meaning and exact strings. Do not
   invent missing facts, authorization, or a next owner; workflow/domain
   authorities decide those, not this writing pass.
3. Arrange reader questions and dependencies before writing. For each major
   meaning unit, know which reader question it answers and what must already
   be understood. Introduce unfamiliar objects at their supported level before
   using their names, indices, formulas, or consequences. Use supported
   examples or clearly labeled hypothetical quantities when they aid a causal
   or mathematical explanation. Do not impose a fixed paragraph template or
   invent a story for a simple status.
4. Generate the complete answer in that understanding order. Lead with the
   human meaning; place exact evidence where it supports the explanation.
   Keep connected reasoning together and use real comparisons, steps, tables,
   formulas, or machine blocks when they have value. A user-requested detailed
   audit, proof, or executable prompt retains its necessary evidence and depth.
5. Re-read the original question and the actual complete candidate as two
   separate review objects. Do not merely repeat the drafting checklist or
   assume that a planned component was actually explained. Locate the answer
   to each user question; check first-use definitions, causal/mathematical
   connections, important caveats, and the exact remaining action/owner when
   one is established. Read across the whole answer for fragmentation.
6. Examine each substantial passage for reader value. If it only inventories
   inspected components, rejected options, checks, or history without changing
   understanding, judgment, or action, remove/merge it or move it to the
   explicitly requested detailed audit. Do not remove necessary comparisons,
   derivations, reproducibility details, limitations, or uncertainty merely
   to shorten the answer.
7. Actually repair the complete candidate: supply supported missing reasoning,
   reorganize a broken dependency, replace ordinary unnecessary English, or
   remove low-value repetition. Preserve facts and exact payloads; refer a
   source contradiction back to its owner instead of inventing a resolution.
   After substantive repairs, re-read the affected whole answer against the
   original question, not just its first screen or changed words.
8. Deliver that revised answer, not a statement that review happened or a long
   self-rating table. This is the same host model editing its own complete
   text, without another conversation, model, service, persistent plan, or
   per-answer human approval. It is not independent review or an unbypassable
   send-time hook; real output quality still has to satisfy the task.

### Small Contrasts

For "Why did the update not take effect?", "checked the cache, resolver,
registry and four tests" only describes the evidence pool. If the verified
cause is that the running process still holds the old configuration, explain
that mechanism and the authorized next action. If the cause is unknown, say
which conclusion is unsupported rather than making the inventory a diagnosis.

For "Explain how the estimate changes with sample size", do not substitute
"more data is better" for the requested mechanism. Introduce the estimated
object and supported assumptions, work through the necessary comparison or
formula, and retain the conditions under which that intuition can fail.

For "Give the complete audit and exact reproduction commands", those details
are the requested content, not disposable process noise. Organize them so the
reader can use them without weakening the audit or changing the commands.

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
