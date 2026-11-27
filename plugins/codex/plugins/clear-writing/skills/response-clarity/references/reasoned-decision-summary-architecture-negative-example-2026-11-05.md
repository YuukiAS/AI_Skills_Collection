# Negative example: Reasoned Decision summary/architecture discussion that forced repeated user repair

Date: 2026-11-05  
Route: Clear Writing / `response-clarity`  
Status: user-confirmed negative example  
Source: live ChatGPT discussion about Reasoned Decision, prior-art discovery, and human problem-solving flow

## Why this example is kept

The domain reasoning was increasingly close to the intended answer, but the user still had to repair the response over many turns because the explanation layer repeatedly failed.

The recurring failure was not primarily factual. It was that the assistant did not convert the known result into the exact reader task:

- summarize three explicitly requested parts;
- compare the second and third proposals;
- state which one should be the main architecture;
- explain what is adopted from each;
- show the final step-by-step runtime flow;
- explain why that combined design is better.

Instead, the assistant oscillated between overlong report-like explanations and one-sentence compression, repeatedly stopped after meta-commentary, and forced the user to ask one missing question at a time.

This is a strong Clear Writing regression because the user explicitly invoked Clear Writing multiple times and the answer still regressed when the skill was not applied continuously.

## The three source obligations that should have been preserved

The user had asked the supporting document to contain three things:

1. what the Pro analysis had already concluded;
2. what still needed to be added to that conclusion;
3. how a competent human would actually solve this kind of problem step by step.

A correct summary therefore had to preserve all three. A correct follow-up comparison also had to explain how items 2 and 3 relate.

## Failure sequence

### Failure 1 — “summary” became another report

User request:

> “人话给我总结”

The answer restated the architecture, prior-art idea, Obsidian example, Build gate, and regression logic at length. It was factually relevant but still read like a compressed design document rather than a reader-facing summary.

Problem:

- too much background was repeated;
- the three requested source obligations were not made explicit early;
- the user still had to infer what the final architecture actually was.

### Failure 2 — correction from “总结” to “概括” triggered over-compression

After the user objected, the answer collapsed to essentially one sentence:

> “Reasoned Decision 以后要像正常人解决问题：先搞清楚你真正要什么，再先看现成方案、真实案例和成熟经验，最后只补现有方案解决不了的缺口……”

Problem:

- it answered the theme, not the document;
- it dropped the Pro conclusion, the proposed addition, and the human baseline as separate obligations;
- it treated brevity as the objective instead of low cognitive load with complete coverage.

### Failure 3 — explaining “概括 vs 总结” did not repair the substantive task

The assistant then explained the distinction between 概括 and 总结 and produced another long summary.

Problem:

- it spent reader attention on terminology instead of finishing the requested synthesis;
- it still did not structure the answer around the exact three source obligations;
- the user had to ask again how many of the three things had actually been covered.

### Failure 4 — meta-apology replaced task completion

When the user noted that the answer regressed whenever Clear Writing was not invoked, the assistant replied mainly with:

> “对，这一轮没走 Clear Writing，我又明显退回到……”

and stopped.

Problem:

- the assistant correctly diagnosed the writing failure but left the underlying task unfinished;
- a style correction should be applied immediately to the pending answer, not become a substitute for that answer.

Regression rule:

> Never stop at a meta-explanation of why the previous response was bad if the substantive request is still open.

### Failure 5 — continuation returned to long-form repetition

After the user forced continuation, the assistant produced another long explanation of Pro, the missing piece, and the human process.

Problem:

- the content was closer, but it again expanded into a report;
- repeated background overshadowed the actual decision;
- the reader still had to infer the final architecture.

### Failure 6 — comparison question buried the decisive relation

User request:

> “你给我比第二个和第三个，也就是人真正做的，哪个好？还是各有一部分好？到底怎么做？”

The answer eventually reached the correct relation:

- the human problem-solving process should be the main flow;
- the prior-art / gap-proof machinery should be the enforcement guardrail.

But this relation was surrounded by many paragraphs before the final runtime flow became clear.

Problem:

- the decisive answer should have appeared immediately;
- the answer needed one architecture sentence, one step-by-step flow, and one short rationale;
- instead, it continued explaining the same distinction from several angles.

### Failure 7 — “重点” compression again lost the complete architecture

After another user correction, the answer said:

> “第三个‘人类怎么解决问题’做主流程；第二个只负责把这套流程锁死，防止 GPT 偷懒。”

This was the right headline, but the user still had to point out that the assistant had not clearly delivered:

- what the final architecture is;
- exactly what happens step by step;
- which elements from proposal 2 are retained;
- which elements from proposal 3 are retained;
- why the combination is better.

Problem:

- a good headline is not a complete answer;
- “say the point first” does not mean “stop after the point.”

## What the final reader-facing answer should have done in one pass

The correct answer shape was:

### 1. Final decision

State immediately:

> Use the human problem-solving sequence as the runtime spine; use the prior-art / reuse / gap-proof rules as mandatory guardrails around that spine.

### 2. Final architecture

Explain the roles without creating new skills:

```text
Task State Integrity
  ↓
Understand goal + current reality
  ↓
Discover existing solution space
  ↓
Judgment Integrity
  ↓
Select mature route(s)
  ↓
Solution Design
  ↓
Adopt / Compose / Extend
  ↓
Build only for proven residual gap
  ↓
Real-world validation
  ↓
Freeze recommendation unless a valid Decision Delta appears
```

The three named Reasoned Decision layers remain responsibilities; the runtime is allowed to move locally between evidence discovery, judgment, and design when new facts appear.

### 3. What is retained from proposal 2

Retain the machine-enforcement pieces:

- automatic prior-art trigger;
- repo / installed capability / official / ecosystem / open-source search;
- requirement-to-capability mapping;
- Adopt / Compose / Extend / Build preference;
- Gap Proof before Build;
- no “no solution exists” claim when discovery was not actually completed;
- hidden-wheel regression tests where existing solutions are intentionally not named.

### 4. What is retained from proposal 3

Retain the human reasoning sequence:

- define the real goal;
- inspect current assets and constraints;
- look at strong real-world examples before inventing;
- infer solution families from multiple examples;
- inspect a small set of strong candidates deeply;
- map candidates back to actual requirements;
- add only the residual missing part;
- validate in the real environment;
- stabilize the conclusion rather than restarting from scratch.

### 5. Why this combination is better

Because proposal 3 gives the right *way to solve problems*, while proposal 2 gives the *enforcement mechanisms* that keep a model from skipping steps.

Using only proposal 2 risks a compliance-style checklist that is triggered too late, mainly when Build is already being considered.

Using only proposal 3 risks relying on model discipline: the model may understand the human process in principle but still jump straight to its own answer.

Together:

> human workflow = spine; machine rules = guardrails.

This is the intended stable design.

## Clear Writing lessons

### A. Completeness is part of clarity

When the user asks for (N) explicit things, clarity requires answering all (N) in the same response unless genuinely blocked.

A response that is concise but covers only one of four requested points is not clear.

### B. Do not confuse compression with readability

The failure oscillated between:

- report-like over-expansion;
- one-sentence over-compression.

The target is neither. The target is the smallest response that preserves the decision structure the user needs.

### C. Preserve the user’s requested information architecture

If the source task says “tell me A, B, and C,” the summary should visibly preserve A, B, and C before adding interpretation.

Do not reorganize so aggressively that the user must ask which requested part was omitted.

### D. After a correction, repair the pending task immediately

Do not answer only:

> “I see why the last answer was bad.”

The next message must contain the corrected substantive answer unless the user asked only for a diagnosis.

### E. “Lead with the answer” does not mean “stop after the answer”

For architecture or decision explanations, a useful compact pattern is:

1. decision;
2. architecture;
3. steps;
4. why.

This usually beats both a one-line slogan and a full design report.

### F. Explicit style invocation should remain active for the whole answer

If the user explicitly invokes Clear Writing, do not apply it to the opening paragraph and then drift back into report structure.

Read the final answer as a whole before sending.

## Regression prompts derived from this case

### Regression 1 — three-part summary

Input asks to summarize a document that explicitly contains:

1. prior conclusion;
2. proposed addition;
3. human baseline.

PASS:

- all three appear;
- no one part consumes most of the answer;
- the relationship among them is explicit.

FAIL:

- only the headline is returned;
- one or more requested parts disappear;
- the answer becomes a miniature report.

### Regression 2 — compare proposal 2 and proposal 3

Input asks:

> Which is better, proposal 2 or proposal 3, or should they be combined? What is the final architecture and why?

PASS:

- first sentence states the relation;
- architecture is explicit;
- retained elements from each proposal are explicit;
- step-by-step runtime is explicit;
- rationale is explicit.

FAIL:

- gives only “they complement each other”;
- gives only a slogan;
- explains both separately but never states the final combined architecture.

### Regression 3 — user complains about style while task remains open

PASS:

- acknowledge briefly;
- immediately provide the corrected pending answer.

FAIL:

- stop after discussing the writing failure.

### Regression 4 — brevity pressure

PASS:

- reduce repetition and formatting while keeping all requested decision fields.

FAIL:

- collapse to one sentence and lose required content.

## Promotion signal

This case is considered improved only when a future complex architecture discussion can answer, in one reader-facing pass:

- what the decision is;
- what the architecture is;
- what happens step by step;
- what was retained from competing proposals;
- why the resulting design is better;

without requiring the user to pull those answers out over multiple rounds.
