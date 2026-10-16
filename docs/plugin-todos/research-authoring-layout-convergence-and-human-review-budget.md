# Research Authoring — Layout Convergence and Human-Review Budget TODO

status: NEW / IMMEDIATE PRACTICE CANDIDATE
source: STAT5060 HW1 repeated student-PDF layout regressions, 2026-10-06

## 1. Problem

A reader should not be used as the layout-debugging loop.

The STAT5060 HW1 sequence repeatedly sent technically valid PDFs to the instructor even though the pages still had obvious density imbalance, artificial whitespace, broken semantic grouping, or inconsistent reader-facing text. Each individual change was bounded, but the production system still generated one speculative layout at a time and asked the human to discover whether it worked.

This is not an acceptable Research Authoring workflow.

## 2. Human-review budget

Before implementation, declare:

```text
HUMAN_REVIEW_BUDGET = <number and type of expected reviews>
```

Default for a bounded visual revision:

```text
HUMAN_REVIEW_BUDGET = one final acceptance review
```

The intended reader/instructor should not receive a candidate merely because it compiled or because the implementation agent labelled it visually acceptable.

Repeated obvious failures mean the authoring/render pipeline has failed. They do not justify consuming additional human review cycles.

## 3. Pre-user layout-convergence gate

A substantial or repeatedly failing visual task must include an internal convergence stage before `READY_FOR_USER_REVIEW`.

Required sequence:

```text
approved content and semantic zones
-> frozen preservation map
-> bounded layout parameter space
-> render all allowed candidates
-> machine rejection of invalid candidates
-> independent pixel-level review of survivors
-> select one candidate
-> only then expose it to the user
```

`READY_FOR_USER_REVIEW` is forbidden until this sequence closes.

## 4. Bounded candidate search

Do not make one untested spacing guess at a time.

Freeze an allowed parameter set, for example:

```text
BODY_LEADING in <approved finite set>
PARAGRAPH_GAP in <approved finite set>
BLOCK_GAP in <approved finite set>
LIST_ITEM_GAP in <approved finite set>
KEEP_TOGETHER_RULE in <approved variants>
```

Then render every allowed combination with the real production engine.

The implementation agent may select only among these approved values. It may not invent a new value after seeing the result.

## 5. Hard candidate rejection

Reject a candidate before human review when any of the following occurs:

- content, number, formula, title, filename, or link drift;
- a required semantic block is split;
- a forbidden hard break or effective hard break remains;
- an orphaned heading or stranded label appears;
- page-count contract fails;
- font, margins, or other locked visual properties change;
- any active annotation regresses;
- any visual trigger remains unresolved;
- visible instructions contradict the actual artifact structure, such as referring to Questions 1–4 after a fifth scored section has been added.

## 6. Layout objective

For valid candidates, select by a declared objective rather than taste.

Recommended ordering:

1. semantic integrity;
2. preservation of locked content and visuals;
3. no awkward block splits;
4. no page-count-driven compression;
5. balanced adjacent-page density;
6. consistent vertical rhythm;
7. minimal deviation from the established document family.

Example density objective:

```text
MIN_PAGE_OCCUPANCY >= approved floor
MAX_ADJACENT_OCCUPANCY_DELTA <= approved ceiling
```

The exact thresholds are review triggers, not universal aesthetics, but a triggered candidate cannot auto-pass.

## 7. Independent pre-user review

The implementation agent's own `VISUAL_REVIEW = PASS` is not sufficient.

Before surfacing a candidate:

- render every page at realistic reading/print scale;
- inspect actual pixels, not only extracted text;
- inspect the whole artifact, not only changed pages;
- verify all semantic and numerical consistency checks;
- record unresolved concerns;
- require an independent reviewer/planner decision.

The same agent may generate evidence, but cannot grant the final pre-user visual acceptance to itself after repeated failures.

## 8. User-facing delivery gate

A candidate may be shown to the user only when:

```text
CONTENT_PARITY = PASS
LOCKED_REGIONS_PRESERVED = PASS
VISUAL_TRIGGER_COUNT = 0
INDEPENDENT_PRE_USER_REVIEW = PASS
READY_FOR_USER_REVIEW = YES
```

Otherwise the output remains an internal candidate.

## 9. General applicability

This rule is not limited to Homework or students. It applies to:

- research reports;
- manuscripts and supplements;
- advisor updates;
- rebuttals;
- policy sheets;
- course handouts;
- slide decks and other fixed-layout artifacts.

The general principle is:

> Human attention is a limited review resource. Research Authoring must converge internally before asking the human to inspect the artifact.
