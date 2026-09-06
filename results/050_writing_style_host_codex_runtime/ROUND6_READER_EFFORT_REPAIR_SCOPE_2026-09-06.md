# 050 Round 6 — reader-effort repair scope

Status: task-local source-of-truth repair note for `050_writing_style_host_codex_runtime`.

This note records the bounded human rejection after Round 5 Final3. It does not revise `PLAN.md`, rename the plugin, create a new workflow state, or authorize a new architecture.

## Human decision

Round 5 Final3 is **STYLE_REJECT**, but it is materially better than Round 4.

The remaining blocker is no longer primarily English density. The main gap versus the manually polished GPT reference is **reader inference burden**: Round 5 often defines or translates an abstraction, while the better reference rewrites the abstraction into the concrete scientific question, comparison, mechanism, or consequence that the reader actually needs.

Examples of the generic pattern:

- weaker: keep an abstract label and add a parenthetical definition;
- stronger: state directly what the experiment is comparing or what question the term stands for;
- weaker: explain that two methods differ in an `anchor`;
- stronger: explain that one method describes all sites around the same reference point while the other first lets each site move to its own local solution;
- weaker: list `information objects`;
- stronger: ask what each client sends and what scientific failure each information type is meant to fix.

These examples are explanatory patterns, not a phrase blacklist.

## What Round 6 must improve

### 1. Concept restatement over glossary-style definition

For non-identity abstractions, first ask whether the concept can be replaced by the concrete scientific relation it represents in the current sentence or paragraph.

A construction like `术语（English，指的是……）` is not automatically a good final answer. It is acceptable only when retaining the term materially helps recognition. If the reader can understand the argument better by stating the underlying question/comparison directly, prefer that direct restatement.

### 2. Reader question before abstraction

When a paragraph is organized around an abstract label, rewrite toward the reader question:

- what is being compared;
- what changed;
- why the difference matters;
- what the evidence can and cannot support;
- what decision follows.

Do not require the reader to learn an internal abstraction before understanding the scientific point.

### 3. Intuition before technical compression

For method contrasts and formulas, use the pattern:

`concrete question / intuition -> exact technical object -> implication / boundary`.

The technical object remains exact where required, but it should not be the entry point when a simpler scientific description is available.

### 4. No reader-facing classification appendix

Round 5 Candidate C ends with a reader-facing glossary/classification section (`复合标识的语义位置`) that exists to explain retained compound English identifiers. This is not acceptable as a final reader artifact.

Latin-span classification, protected-name ledgers, recognition rationales, and similar evidence belong in private stage artifacts. They must not be appended to the final candidate to satisfy preservation or language gates.

If an English identifier cannot be explained naturally in its scientific context, translate/rewrite it there rather than appending a final glossary generated from the validator inventory.

### 5. Candidate-only reader-effort review must judge abstraction burden

The terminal reader review should ask a new question beyond `is this English span explained?`:

> Can a technically trained reader understand the scientific point without first decoding an avoidable abstract label or mentally translating a bilingual noun stack?

A passage fails reader-effort review when it is technically correct but still makes the reader perform an avoidable intermediate translation step.

This is semantic judgment owned by the host Codex reader pass. Do not replace it with sentence-length metrics, English-density thresholds, phrase blacklists, or a numeric readability score.

### 6. Keep Round 5 gains

Do not regress:

- exact formal names remain recognizable;
- ordinary English reasoning is not allowed to survive through `useful_recognition` escape hatches;
- useful recognition remains narrow and locally explained;
- source facts, formulas, numbers, citations, conditions, uncertainty, attribution, evidence class and conclusion strength remain intact;
- clean isolated `ai-bridge plugin-replay` is mandatory for final A/B/C;
- no application-level OpenAI/Terra generation;
- no raw literal/token dump;
- no source-copy Meaning Card fallback;
- no report-planning responsibilities from `research-writing` are imported into 050.

## What Round 6 must NOT do

- do not redesign Reader Plan / Reviewed Handoff / Bridge Kit;
- do not add project-specific vocabulary rules;
- do not optimize for fewer English tokens as a proxy for quality;
- do not force global reordering when not needed;
- do not hand-edit smoke outputs;
- do not append a glossary or token inventory to the reader-facing candidate;
- do not rename `writing-style` to `clear-language` before 050 closes;
- do not modify `research-writing`, `presentations`, `statistical-modeling`, `scientific-visualization`, `medical-imaging`, or `bioinformatics` runtime in this task.

## Acceptance target

The next clean A/B/C should preserve Round 5 fidelity while materially lowering reader inference burden toward the manually polished GPT reference.

The practical target is not stylistic imitation. The target is that the remaining difference from the manual reference is mostly personal wording preference, not a systematic difference in how much abstract decoding the reader must do.

If the same abstraction-heavy failure remains after this bounded repair, stop adding style rules and return to Planner with the real clean artifacts and stage evidence. Treat the host writer/reader contract itself as the likely bottleneck.
