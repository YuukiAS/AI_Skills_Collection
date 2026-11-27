# Student Assessment Research Authoring — Semantic Pagination Amendment V1

Status: **CANONICAL COMPANION / BINDING FOR PAGE-FLOW DECISIONS**  
Date: 2026-10-07  
Applies to: Homework briefs, Project Guides, policy sheets, forms, templates, reports and other reader-facing fixed-page documents

This amendment defines how Research Authoring decides whether a paragraph, table, list, quotation, question or other block should remain on the current page, move as a whole to the next page, or split across pages.

The objective is not to maximize page fill. The objective is to preserve the reader's unit of understanding and action while using whitespace deliberately.

---

## 1. Start from semantic blocks, not page coordinates

Before choosing a page break, assign stable BlockIDs and relations.

Required fields:

```text
BLOCK_ID
BLOCK_ROLE
BLOCK_RELATION_TO_PREVIOUS
BLOCK_RELATION_TO_NEXT
READER_ACTION
ATOMICITY = ATOMIC | CONTINUABLE | INDEPENDENT
LEGAL_INTERNAL_BREAKPOINTS
PAGE_START_CONTEXT_REQUIRED = YES | NO
```

Useful relations include:

```text
INTRODUCES
EXPLAINS
QUALIFIES
CONSEQUENCE_OF
TABLE_FOR
CAPTION_FOR
ATTRIBUTION_FOR
SCORE_SUMMARY_FOR
SUBPART_OF
CONTINUATION_OF
INDEPENDENT_AFTER
```

Pagination is decided from these relations. It is not decided by whichever page happens to have unused space.

---

## 2. Atomic semantic blocks

An atomic block should remain on one page whenever it fits on one page under frozen typography and geometry.

Typical atomic blocks:

- heading + first substantive lines;
- rule paragraph + table that operationalizes the rule + consequence sentence;
- quotation + attribution;
- figure/table + caption or immediately required explanation;
- warning + required action/consequence;
- question heading + opening statement + first subpart;
- form label + input area;
- scoring heading + scoring table.

A block is atomic when one or more are true:

1. the later element cannot be interpreted correctly without the earlier element;
2. the earlier element explicitly promises, introduces or labels the later element;
3. the reader must use the elements together to make one decision or take one action;
4. placing a page turn between them would force backtracking;
5. the next page would begin with a dependent child lacking context.

Do not split an atomic block merely to fill the preceding page.

---

## 3. Continuable and independent blocks

A block may split naturally when:

- it is longer than one page;
- each paragraph remains independently understandable;
- an approved internal breakpoint exists;
- continuation is obvious or explicitly labelled;
- no heading, label, table, consequence or attribution is stranded.

An independent block may move between pages without carrying adjacent blocks when it starts a new reader action and has its own visible context.

Examples:

- a long explanation may continue across pages;
- a multi-page table may continue only with repeated headers and a continuation treatment;
- an independent new section may start on the next page;
- a short rule paragraph that introduces a deduction table is not independent.

---

## 4. Page-boundary decision algorithm

For every proposed break:

### Case A — atomic block fits in remaining space

Keep it on the current page when:

- the complete block fits;
- minimum post-block/footer reserve is respected;
- keeping it does not create an orphan immediately after it.

### Case B — atomic block does not fit

Move the **entire block** to the next page.

Accept purposeful whitespace on the previous page rather than splitting the block.

### Case C — block is larger than a page

Split only at pre-approved internal semantic breakpoints.

Use continuation labels or repeated headers where needed. Never let a page begin with an unlabeled dependent fragment.

### Case D — both keeping and moving are semantically legal

Render at most two proofs:

1. keep/split at the legal boundary;
2. move the complete block.

Both must pass objective checks. A fresh rendered Reviewer compares:

- semantic continuity;
- page-turn cost;
- page-start context;
- hierarchy;
- whitespace quality;
- whole-sequence rhythm.

Do not search dozens of micro-spacing combinations before resolving this structural choice.

---

## 5. Page-start context rule

A page must not begin with a dependent child unless continuation is explicit.

Normally forbidden page starts:

- a deduction table without the rule paragraph that introduces it;
- an attribution without its quotation;
- a consequence sentence without the rule it qualifies;
- a subpart label separated from its question context;
- a figure/table caption separated from the figure/table;
- a list that is visibly the continuation of an unlabeled previous-page lead-in.

Required check:

```text
DEPENDENT_CHILD_AT_PAGE_START = NO
```

---

## 6. Purposeful versus accidental whitespace

Whitespace is purposeful when it results from preserving an atomic semantic boundary and the next page begins with a complete, clearly labelled reader action.

Whitespace is accidental when it is created by:

- stale `Needspace` or keep-together values;
- an unnecessary manual break;
- a detached child block;
- a residual line/page;
- a block moved without semantic reason;
- inconsistent spacing tokens.

Do not fill purposeful whitespace by splitting an atomic block.

To reduce purposeful whitespace, consider only:

1. moving another **complete independent block** across the boundary;
2. choosing a different approved semantic breakpoint;
3. adjusting already-approved global rhythm within its valid range;
4. revisiting page-count mode through Planner authority.

Do not move half of a semantic unit.

---

## 7. Implementation rule for keep-together controls

Raw pagination controls are implementation state, not semantic authority.

- derive `Needspace`, keep-with-next and keep-together values from the actual block and current typography;
- prefer a block wrapper or measured content height over copied magic numbers;
- global typography/geometry changes invalidate these controls;
- inspect actual generated source when an unexpected residual page appears;
- do not preserve an old guard merely because it existed in the positive baseline.

Semantic rule first; TeX/DOCX pagination control second.

---

## 8. Deterministic and rendered-review ownership

Deterministic validation checks:

- atomic block split/no-split according to authority;
- dependent child at page start;
- required repeated header/continuation marker;
- page count when hard;
- clipping/overflow;
- locked copy and content.

Rendered review checks:

- whether whitespace looks intentional;
- whether the page turn feels natural;
- whether a page is visually calm or looks unfinished;
- whether hierarchy remains clear;
- whether the full page sequence reads better with the chosen break.

Page occupancy is diagnostic only unless calibrated to an accepted baseline or tied to objective usability.

---

## 9. Required decision log

For every non-trivial page-boundary decision, record:

```text
BOUNDARY_ID
BLOCKS_BEFORE
BLOCKS_AFTER
ATOMIC_BLOCKS_AFFECTED
LEGAL_OPTIONS
SELECTED_OPTION
SEMANTIC_REASON
PAGE_START_CONTEXT_CHECK
PURPOSEFUL_WHITESPACE_JUSTIFICATION
RENDERED_REVIEW_RESULT
```

This log should be short. It exists to preserve the decision, not to create another large governance layer.

---

## 10. Acceptance fields

Before user review:

```text
ATOMIC_BLOCK_MAP = COMPLETE
PAGE_BOUNDARY_DECISION_LOG = COMPLETE
ATOMIC_BLOCK_SPLITS = 0 | APPROVED_CONTINUATIONS_ONLY
DEPENDENT_CHILD_AT_PAGE_START = NO
PAGE_START_CONTEXT = PASS
PURPOSEFUL_WHITESPACE = PASS
STALE_PAGINATION_GUARDS = NONE
RENDERED_PAGE_FLOW_REVIEW = PASS
```

---

## 11. STAT5060 HW1 calibration example

For the HW1 page-limit material:

```text
RULE-PAGELIMIT =
  page-limit paragraph
  + deduction table
  + post-subtotal consequence sentence
```

Relations:

```text
paragraph INTRODUCES table
table OPERATIONALIZES paragraph
consequence QUALIFIES table/rule
```

Therefore `RULE-PAGELIMIT` is an atomic semantic block.

The version that leaves the explanatory paragraph on Page 1 and begins Page 2 with the deduction table is semantically weaker because Page 2 begins with a dependent child and the student must turn back to recover the rule context.

The preferred version moves the complete page-limit paragraph, table and consequence sentence to Page 2. The extra whitespace at the end of Page 1 is purposeful because it preserves a complete rule unit and creates a clear boundary between submission/report-format instructions and page-limit/workflow instructions.


## 12. Heading plus first-body spacing is a component relation

A heading and its first substantive paragraph/subpart are an atomic visual relation.

The semantic rule is not only “do not orphan the heading”; it also requires a stable, readable gap after the heading.

For repeated question headings:

- define one shared heading-to-body gap token;
- do not allow one question to have a noticeably tighter first-body gap than another;
- a typography or heading-size change reopens this token for validation;
- fix the shared question-heading component rather than inserting local skips.

Required:

```text
HEADING_FIRST_BODY_ATOMICITY = PASS
QUESTION_HEADING_BODY_GAP_CONSISTENCY = PASS
LOCAL_HEADING_SPACING_HACKS = ZERO
```


## 13. Assessment question-flow rule

For Homework and exam-style handouts, a **major question is not automatically an atomic page block**.

Default classification:

```text
QUESTION_HEADING + opening context = ATOMIC
EACH_SUBPART_LABEL + first substantive line = ATOMIC
MAJOR_QUESTION_BODY = CONTINUABLE
BETWEEN_SUBPARTS = PREFERRED_LEGAL_BREAKPOINT
BETWEEN_PARAGRAPHS_INSIDE_LONG_SUBPART = SECONDARY_LEGAL_BREAKPOINT
```

Do not impose layout rules such as:

- one question per page;
- two questions per page;
- start every major question at the top of a page;
- keep an entire multi-subpart question together

unless there is a reader/pedagogical reason and the resulting composition has been rendered and accepted.

When consecutive questions are short, paginate the **whole question sequence** rather than pairing questions with pages. The preferred sequence is:

```text
frozen copy
-> natural continuous flow
-> semantic orphan/continuation protection
-> whole-sequence rendered review
-> only then bounded rhythm tuning
```

A sparse lower half of a page is a diagnostic trigger to inspect:

1. explicit hard breaks;
2. stale `Needspace` / keep-together guards;
3. unnecessary whole-question atomicity;
4. fixed page/question grouping.

Do not solve sparse pages by adding filler prose, decoration, oversized local gaps, or arbitrary font/margin changes.

If a page break occurs between subparts of the same major question, the next page may begin with the next labelled subpart when the previous subpart ended cleanly and the continuation is unambiguous. If ambiguity remains, use a restrained continuation treatment rather than moving an otherwise valid full question to a new page.

Required:

```text
FIXED_QUESTION_PER_PAGE_RULE = NONE | EXPLICITLY_JUSTIFIED
MAJOR_QUESTION_ATOMICITY = CONTINUABLE_BY_DEFAULT
LEGAL_SUBPART_BREAKPOINTS = DEFINED
WHOLE_SEQUENCE_PAGE_FLOW_REVIEW = PASS
SPARSE_PAGE_ROOT_CAUSE = EXPLAINED
FILLER_ADDED_TO_BALANCE_PAGES = NO
```
