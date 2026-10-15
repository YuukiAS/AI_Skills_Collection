# Clear Writing 真实 ChatGPT Web 已知回归库 v1

- Date: 2026-10-15
- Task: `clear-writing--cross-surface-language-layer`
- Purpose: development / known regression only
- Source anchor: `docs/plugin-todos/writing-style.md` on `main@1c59199f88c7527f2bd853e606f20146134fda47`
- Freshness rule: every case below is already exposed to development and therefore MUST NOT be counted as G7 unseen/fresh evidence.

This file freezes the transferable failure semantics from five user-observed ChatGPT Web examples. It intentionally does not commit private full transcripts. Executor may create public-safe derived fixtures that preserve the failure structure, but those fixtures are development regressions, not substitutes for later real Web acceptance.

## RW-WEB-01 — Long answer buries the decision

Polarity: NEGATIVE.

Observed failure:
- the opening states the useful fact, then the answer expands into many headings, bullets, repeated constraints and machine-facing detail;
- reader-facing explanation and machine-delivery content are mixed;
- repeated boundary statements force the reader to keep re-checking whether new information has appeared.

PASS requires:
- the first screen gives the decision, practical meaning and any required action;
- later detail adds genuinely new evidence or decisions instead of reclassifying the same conclusion;
- machine strings, paths, status fields and executable payloads are separated from explanatory prose when they are needed;
- length is driven by information need, not by a fixed short-answer rule.

Should-not-change:
- when the user explicitly requests a complete executable prompt, report, contract or machine payload, preserve the required completeness and exact machine content.

## RW-WEB-02 — Pseudo-clarification and self-critique replace the answer

Polarity: NEGATIVE.

Observed failure:
- the response first rejects interpretations the user did not propose;
- recommendations change without explaining why the previous recommendation was withdrawn;
- when the user criticizes the wording, the answer launches into domain analysis or long self-critique instead of locating the actual bad sentence and replacing it with useful information.

PASS requires:
- define the actual object and answer the user’s question directly before excluding edge interpretations;
- if the recommendation changes, state what new evidence or corrected premise caused the change;
- when the user is reviewing writing quality, diagnose the supplied text itself and show the missing information or better formulation;
- do not psychologize the user or substitute apology/meta-reflection for the requested analysis.

Should-not-change:
- a genuine ambiguity, safety exclusion or materially plausible misconception may still need a concise negative clarification.

## RW-WEB-03 — Concrete explanation with examples is a positive baseline

Polarity: POSITIVE.

Observed success:
- starts with a concrete choice or answer;
- uses ordinary scenarios/examples to explain an abstract concept;
- separates the recommended direction from facts that still need verification.

PASS requires preserving these strengths:
- do not over-compress away a necessary example, causal explanation or uncertainty boundary;
- do not replace a reader-friendly explanation with terse status language;
- do not interpret “clear writing” as “always three sentences”.

This case is a should-not-change positive control for all repairs below.

## RW-WEB-04 — Pseudo-structure lowers information density

Polarity: NEGATIVE.

Observed failure:
- a simple linear flow is expanded into a large fenced text block with one arrow/step per line and large empty visual area;
- a second code-style block lists internal names only to say the user does not need to know them;
- ordinary Chinese explanation repeatedly switches into unnecessary English labels.

PASS requires:
- use ordinary prose or a compact inline flow when the relationship is simple and linear;
- use code fences only for code, machine/exact content, or material where monospace/verbatim treatment has real value;
- expose internal development names only when the current answer needs them for locating, comparing or acting;
- preserve official product names and exact machine strings when precision requires them;
- choose lists, tables, arrows or diagrams only when the structure reduces reader effort.

Should-not-change:
- genuinely branched processes, step-by-step execution, commands, machine output and copyable protocols may use structured blocks.

## RW-WEB-05 — Research synthesis expands into a mini architecture memo

Polarity: NEGATIVE.

Observed failure:
- the useful synthesis is already complete near the beginning;
- the answer then repeats the same central conclusion through “common points”, “differences”, a new product name, component breakdown, location table, experiments and a final re-summary;
- source consensus and the assistant’s further design recommendation are visually blended.

PASS requires:
- first state what all sources agree on, where they materially differ and whether the user needs to act;
- clearly separate “the sources establish” from “my additional recommendation”;
- do not automatically convert a synthesis request into a new architecture/implementation document;
- every new section after the core answer must add a new decision, evidence class or requested implementation detail;
- stop when the user’s question is answered unless the user requested deeper design.

Should-not-change:
- if the user explicitly asks for a complete architecture, implementation plan, component allocation or experiment design, the response may legitimately expand.

## Cross-case development rubric

A known-regression batch passes only when all five cases satisfy their individual criteria.

The grader must not use:
- banned-word counts;
- English percentages;
- heading counts;
- line counts;
- arrow/code-fence bans;
- fixed answer length;
- keyword grep as the qualitative PASS oracle.

The grader should judge:
1. decision visibility;
2. incremental information value after the core answer;
3. reader-effort proportionality of formatting;
4. source fact vs assistant recommendation separation;
5. feedback-intent alignment;
6. preservation of necessary explanation, uncertainty and exact machine strings.

Any production change made after seeing these cases may be tuned on them; therefore these cases remain known regressions permanently and cannot become G7 fresh evidence.
