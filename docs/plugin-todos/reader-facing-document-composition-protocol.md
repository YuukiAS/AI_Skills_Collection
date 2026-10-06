# Research Authoring — Reader-Facing Document Composition Protocol Candidate

status: DETAILED_SOLUTION_CANDIDATE / NOT YET PROMOTED TO SKILL
source: STAT5060 HW1, Final Project and presentation regressions, 2026-10-06
scope: generic reader-facing document composition; applies beyond course materials

## 1. Why this protocol exists

A document can be factually correct, semantically approved, unclipped and searchable, yet still be visually poor because page count, line spacing, block spacing and semantic structure were left to the renderer.

Two recurring failures motivated this protocol:

1. a dense first page followed by a mostly empty second page;
2. a one-page document produced by arbitrary local compression, with inconsistent heading, paragraph, list and quotation spacing.

The renderer should not be asked to "make it fit". Page count and vertical rhythm are authoring decisions.

## 2. Responsibility model

### Author / planner owns

- intended reader and reader task;
- semantic zones and information order;
- which blocks are scored / required / contextual / quoted;
- page-count mode;
- document-family typography and spacing tokens;
- legal page-break positions;
- preservation map and accepted baseline.

### Renderer / Codex owns

- faithful implementation of the frozen content and composition contract;
- deterministic build and render;
- no unapproved content or spacing invention;
- reporting a layout conflict when the frozen contract cannot be met.

### Reviewer owns

- actual pixel-level judgement at realistic reading / print scale;
- semantic and visual regression review;
- rejecting technically valid but compositionally poor output.

### User / document owner owns

- content approval;
- final visual acceptance;
- publication approval.

No one role may silently take over another role's decisions.

## 3. Semantic zoning before layout

Every document is decomposed into semantic zones before any page planning.

Recommended zone schema:

| Zone | Purpose | Examples |
|---|---|---|
| `IDENTITY` | identify the artifact | title, version, date, due date, weight |
| `RULES` | tell the reader how to act | submission, format, deadlines, permitted tools |
| `ASSESSED_OR_DECISION_CONTENT` | content that is scored or used for a formal decision | questions, rubric dimensions, required deliverables |
| `EVIDENCE_OR_ARGUMENT` | substantive claims and support | results, figures, reasoning, literature |
| `SOURCE_QUOTE` | exact external source text | policy quote, legal/institutional wording |
| `REFERENCE` | supporting lookup material | links, definitions, references |
| `INTERNAL_ONLY` | author / marker / QA material | hashes, atomic rubric, build notes |

A block may not be placed merely because it exists in the source bundle. It must have a reader-facing purpose.

### Mandatory separation rule

Blocks that imply different reader actions must not be visually or structurally collapsed.

Examples:

- scored material does not sit inside ordinary ungraded rules prose;
- penalties do not look like optional context;
- direct quotations do not look like course-authored prose;
- internal QA material does not enter the reader-facing document.

For assessment documents, front matter contains rules; scored components belong in the assessed section so that totals are transparent.

## 4. Block inventory

Before rendering, create a block inventory.

Each block records:

```text
BLOCK_ID
SEMANTIC_ZONE
SEMANTIC_CLASS = identity | rule | task | assessed | warning | quote | context | reference
CONTENT_AUTHORITY
CONTENT_LOCK = locked | editable
VISUAL_ROLE = title | metadata | heading | paragraph | list | table | quote | note
KEEP_TOGETHER = hard | preferred | no
BREAK_BEFORE_ALLOWED = yes | no
BREAK_AFTER_ALLOWED = yes | no
ESTIMATED_HEIGHT
```

The block inventory is the basis of page planning. File order is not page order.

## 5. Page-count declaration

Every document declares:

```text
PAGE_COUNT_MODE = HARD | PREFERRED | FREE
PAGE_COUNT_TARGET = <number / range / NONE>
CONTENT_MUTABLE = YES | NO
FONT_MUTABLE = YES | NO
MARGINS_MUTABLE = YES | NO
RHYTHM_MINIMUMS = <frozen spacing floor>
```

Interpretation:

- `HARD`: page count is a real requirement. If the frozen content cannot fit above the readability floor, return a layout conflict.
- `PREFERRED`: aim for the target only if readability and semantic integrity are preserved.
- `FREE`: semantic structure and visual rhythm determine page count.

The mode is chosen before rendering. The renderer cannot promote a preference into a hard requirement or vice versa.

## 6. Document-family rhythm tokens

Each document family defines one stable set of vertical-rhythm tokens.

Minimum token set:

```text
BODY_SIZE
BODY_LEADING
PARAGRAPH_GAP
TITLE_GAP_AFTER
HEADING_GAP_BEFORE
HEADING_GAP_AFTER
LIST_GAP_BEFORE_AFTER
LIST_ITEM_GAP
NESTED_LIST_ITEM_GAP
QUOTE_GAP_BEFORE
QUOTE_GAP_AFTER
ATTRIBUTION_GAP_AFTER
TABLE_GAP_BEFORE_AFTER
TABLE_ROW_PADDING
FOOTER_RESERVE
```

### Rules

1. Use one body leading throughout the document unless an explicitly approved role uses another size.
2. Do not add local `setstretch`, `parskip`, list or heading overrides to make one page fit.
3. Exact units may differ between LaTeX, Word and HTML, but the rendered rhythm must be equivalent.
4. A family contract is inherited by related documents; do not invent a new rhythm for every artifact.
5. Any exception is recorded as a bounded override with a reason and visual evidence.

## 7. Deterministic page-planning algorithm

The author / planner performs these steps before Codex renders the final artifact.

### Step 1 — freeze content and zones

Approve exact reader-facing text and semantic zones.

### Step 2 — choose rhythm tokens

Apply the document-family defaults and any approved artifact-specific overrides.

### Step 3 — render a measurement draft

Use the actual production engine to measure each block under the frozen tokens. Do not optimise yet.

### Step 4 — enumerate legal breakpoints

Page breaks may occur only at approved semantic boundaries.

Hard keep-together blocks include, when short enough to fit on one page:

- a heading plus the first meaningful content;
- a short instruction block;
- a numbered alternative plus its immediate explanation;
- a quotation plus attribution;
- a compact table and its explanatory line;
- a scored block heading plus its mark table.

### Step 5 — select the page plan

Choose the page plan that minimises this ordered set of costs:

1. overflow or clipping;
2. violation of content / semantic separation;
3. splitting a hard keep-together block;
4. orphaned heading or stranded label;
5. page-count contract violation;
6. large density imbalance between adjacent pages;
7. excessive accidental whitespace;
8. unnecessary deviation from family rhythm tokens.

This order matters. A shorter document is never preferred over semantic integrity or readability.

### Step 6 — compaction or expansion

If the draft is too long, apply only this order:

1. remove accidental duplicate whitespace;
2. move breaks to better semantic boundaries;
3. use the normal approved family tokens consistently;
4. adjust spacing only within the pre-approved acceptable range;
5. reconsider page count if it is not hard;
6. change geometry / font only if explicitly reopened by the owner.

Never delete, paraphrase or weaken content to hit a page target without new content approval.

If the draft is too sparse:

1. remove unnecessary hard breaks;
2. rebalance complete semantic blocks across pages;
3. do not invent filler content;
4. do not enlarge arbitrary gaps solely to fill the page.

## 8. Density audit heuristics

Use page occupancy as an audit signal, not as an automatic design objective.

Let:

```text
O_p = occupied vertical content height / usable page height
```

Soft review triggers:

- `O_p < 0.55` on an interior page without an approved semantic reason;
- adjacent pages differ by more than roughly 0.25 in occupancy;
- one page is near full while the next contains only one residual block;
- the bottom of one page is crowded while the next page is largely blank;
- a short block is split even though it could fit whole on the next page.

These are review triggers, not automatic failures. Title pages, deliberate chapter openings and final pages may be sparse for valid reasons.

## 9. One-page versus two-page decision

For a short policy / brief with frozen content:

1. render with the family font, geometry and standard rhythm tokens;
2. if all blocks fit on one page without local compression, semantic splits or excessive density, choose one page;
3. if one page requires violating the rhythm floor, choose two pages;
4. if two pages are used, rebalance complete sections so the second page is not a residual fragment;
5. do not alternate between one and two pages by random spacing changes.

A one-page document is better only when it is comfortably readable. A two-page document is better only when both pages have intentional composition.

## 10. Scored / unscored / policy separation

For assessment documents:

- rules and operational instructions belong in front matter;
- questions and all scored components belong in the assessed section;
- the displayed points in the assessed section must sum transparently to the stated total;
- a scored process / presentation component must not be hidden inside rules prose;
- page-limit deductions may remain in rules because they are submission consequences, but the scored component itself belongs with other scored items.

This is a semantic rule, not merely a formatting preference.

## 11. Visual QA protocol

Visual QA reviews every page at realistic reading / print scale.

Mandatory judgements:

- body line spacing is consistent;
- paragraph gaps are consistent;
- heading hierarchy is clear;
- list levels are visibly distinct without compression;
- quotations and attributions are separated correctly;
- tables have adequate row spacing and surrounding space;
- adjacent pages are balanced unless a semantic boundary justifies otherwise;
- no semantic block is awkwardly split;
- no page is compressed simply to avoid another page;
- no accepted unrelated region changed during a bounded revision.

The following are necessary but insufficient:

- no clipping;
- no overlap;
- no missing glyph;
- no overflow;
- searchable text;
- passing unit tests.

## 12. Regression and acceptance evidence

Every bounded revision records:

```text
AUDIENCE_PREFLIGHT
CONTENT_APPROVAL_GATE
SEMANTIC_ZONE_MAP
PAGE_COUNT_MODE
RHYTHM_TOKEN_SOURCE
INTENDED_CHANGED_BLOCKS
UNINTENDED_SEMANTIC_CHANGES
UNINTENDED_VISUAL_CHANGES
SEMANTIC_BLOCK_SPLITS
ADJACENT_PAGE_DENSITY_REVIEW
LOCKED_CONTENT_PRESERVED
LOCKED_VISUAL_REGIONS_PRESERVED
READY_FOR_HUMAN_REVIEW
```

Codex's own `VISUAL_REVIEW = PASS` is evidence, not final authority. The actual rendered pages remain authoritative.

## 13. Promotion evidence

Before promotion into Research Authoring, replay this protocol on at least:

- one one-page policy sheet;
- one two-page rules/front-matter section;
- one multi-page research report;
- one presentation or slide deck;
- one bounded revision where accepted pages must not regress.

Success requires repeatable page composition, not just successful compilation.
