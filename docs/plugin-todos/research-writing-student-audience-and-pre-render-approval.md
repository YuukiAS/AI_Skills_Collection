# Research Authoring — Reader Contract, Approval Gate, and Regression-Control TODO

status: NEW / DETAILED_SOLUTION_CANDIDATE
source: `YuukiAS/STAT5060-TA` / STAT5060 2026–27 HW1 and Final Project authoring failures
last updated: 2026-10-06

evidence:
- rejected Final Project student artifact: `YuukiAS/STAT5060-TA/materials/2026-27/final-project/student/release/STAT5060_Project_Guide_2026-27.pdf`
- rejected Final Project candidate commit: `145c7bc265265e4bc266824af8c770d9e3e55014`
- HW1 student-facing redesign and critic history in `YuukiAS/STAT5060-TA`
- HW1 balanced-reader candidate: `reviewed/stat5060--hw1-v3-balanced-reader-final@faa0b2bf194b38778f6ee1c7149b8a463df805b0`
- instructor annotations and thread corrections, 2026-10-06
- related specialization TODO: `docs/skill-todos/course-assessment-authoring.md`

target layer: research-document planning / reader contract / content approval / preservation / bounded revision / semantic and visual QA

## 1. Problem statement

A document can be factually correct, fully rendered, searchable, visually unclipped, hash-stable and heavily validated, yet still be wrong for its intended reader.

The STAT5060 failures exposed two recurring classes of error.

### 1.1 Wrong-audience content selection

The failed Final Project Guide was nominally student-facing, but much of its content was selected from instructor, marker, implementation and QA needs. It exposed or over-explained material that may be valid internally but was not needed by postgraduate students to complete the assessment, including:

- internal publication and approval state;
- machine-style decision labels and grading codes;
- instructor-side atomic rubric detail;
- method-selection scaffolding that pre-solved work expected from lecture notes;
- unapproved consultation requirements and contingency dates;
- internal score-cap exception logic;
- rejected implementation alternatives and QA history.

The central mistake was asking:

> What information exists in the source bundle?

instead of:

> What does this reader need in order to act correctly?

### 1.2 Regression during bounded revision

HW1 and presentation work exposed a second failure mode. A candidate can contain accepted content and layout, but a later local repair can reflow or regenerate the whole artifact and damage unrelated accepted areas.

Typical causes include:

- a local wording change triggering a whole-document rewrite;
- a page-break repair changing unrelated pagination;
- a font, spacing, table or heading change affecting all pages;
- the implementation agent reading only the latest complaint instead of the complete active-decision history;
- a new candidate being treated as authoritative merely because it passed build or automated QA;
- no explicit map of what is locked, editable or rejected.

The general Research Authoring problem is therefore broader than reader selection. It is:

> How do we turn authoritative sources into a reader-appropriate artifact, obtain human approval before rendering, and later revise only the intended scope without damaging accepted content or visual structure?

## 2. Scope and boundary

This TODO proposes a generic Research Authoring capability for substantial reader-facing documents, including:

- advisor and group-meeting reports;
- manuscripts, rebuttals and supplements;
- formal technical reports;
- student-facing assessment documents when routed through the course-specific specialization.

It does not authorize Research Authoring to decide course assessment meaning. The proposed `course-assessment-authoring` specialization should own Homework, Project, Milestone, rubric-publication and course-release specifics.

Course-specific weights, dates, methods, penalties, filenames and oral rules remain in the course repository. Research Authoring owns the general reader contract, content-approval gate, preservation model and revision QA.

## 3. Mandatory audience contract

Every substantial reader-facing artifact must declare an audience contract before drafting.

Minimum schema:

```text
AUDIENCE = <specific reader or reader group>
READER_TASK = <what the reader must understand, decide, approve or do>
INCLUDE = <information required for that task>
EXCLUDE = <material belonging to other audiences>
SOURCE_AUTHORITY = <where facts, rules, claims and terminology come from>
```

The declaration is internal authoring metadata. It does not normally appear in the final document.

### 3.1 Reader-action test

A source item belongs in the reader-facing artifact only when at least one of the following is true:

1. the reader needs it to take a required action;
2. the reader needs it to interpret a claim correctly;
3. the reader needs it to evaluate evidence or make a requested decision;
4. omission would create a material ambiguity, error or fairness problem.

A source item does not belong merely because it is true, available, internally important or easy to copy.

### 3.2 Audience separation

At minimum distinguish:

1. **reader-facing content** — what the intended reader needs;
2. **author/instructor-facing content** — reasoning, calibration, hidden rubric, solutions or decision history;
3. **implementation-facing content** — file paths, build instructions, rendering contracts and tool details;
4. **QA/release-facing content** — hashes, manifests, contact sheets, validation logs and release states.

No artifact should double as all four layers.

## 4. Source-to-reader inclusion map

Before drafting, classify each source unit.

Recommended fields:

| Field | Meaning |
|---|---|
| Source locator | Canonical file, section, table, figure or decision |
| Source role | fact / rule / claim / evidence / rationale / implementation / QA |
| Intended audience | student / instructor / advisor / reviewer / implementer / QA |
| Reader need | concrete action or interpretation supported |
| Disposition | INCLUDE / SUMMARIZE / MOVE_INTERNAL / EXCLUDE / USER_DECISION |
| Fidelity requirement | verbatim label / semantic preservation / exact number / optional reorganization |

This map prevents source-file order from becoming document order and prevents internal material from leaking into the reader artifact.

## 5. Artifact-family planning

Different document families require different default information structures. Research Authoring should not apply one generic outline to all artifacts.

### 5.1 Student Homework brief

Default priority:

1. course and assignment identity;
2. due date, weight and essential submission information;
3. minimum data/software context required before Question 1;
4. questions and requested outputs;
5. concise reproducibility and assistance policy.

Questions should dominate the artifact. Administrative instructions must not become half of the assignment unless genuinely necessary.

### 5.2 Student Project brief

Default priority:

1. task and required components;
2. dates and milestone/proposal requirements;
3. data and method boundaries without pre-solving method selection;
4. required report contents;
5. broad public mark allocation;
6. templates and submission;
7. necessary format/late/AI/oral rules.

### 5.3 Advisor or research report

Default priority:

1. scientific question or decision;
2. decisive evidence;
3. current conclusion and uncertainty;
4. why it matters;
5. unresolved alternatives, risks and requested input.

Internal experiment chronology, job names, QA gates and repository state normally remain outside the main narrative.

## 6. Human content approval before rendering

A substantial reader-facing artifact must not move directly from internal sources to Codex rendering.

Required sequence:

```text
source and authority review
-> audience contract
-> source-to-reader map
-> complete reader-facing body draft
-> human content approval
-> frozen approved body
-> implementation/rendering
-> semantic and visual QA
-> human artifact acceptance
```

### 6.1 Approval record

The approval record should bind:

```text
STATUS = USER_APPROVED
APPROVED_BODY_PATH = <path>
APPROVED_BODY_SHA = <blob or content hash>
APPROVED_BODY_COMMIT = <commit>
AUDIENCE_CONTRACT_PATH = <path>
FINAL_PUBLICATION_APPROVAL = PENDING | APPROVED
```

Approval of assessment design, scientific analysis or an earlier document version does not automatically approve a new reader-facing body.

### 6.2 Approval invalidation

Any semantic change invalidates the content approval for the changed material, including:

- adding or removing a requirement;
- changing information scope;
- adding an example, exception, contingency or explanation;
- changing public rubric detail;
- changing conclusion strength;
- changing reader-facing terminology or structure in a way that alters interpretation.

Purely mechanical layout changes may remain in the rendering stage only when the approved body is semantically unchanged and the system records that fact.

## 7. Preservation map

Every approved artifact should have a preservation map before later revision.

Recommended statuses:

| Status | Meaning |
|---|---|
| `LOCKED_CONTENT` | Wording, numbers, formulas or meaning must not change |
| `LOCKED_VISUAL` | Accepted layout/composition must not change |
| `EDITABLE_WORDING` | Local wording may change without semantic drift |
| `EDITABLE_LAYOUT` | Local layout may change while content stays fixed |
| `USER_DECISION_REQUIRED` | Any change requires renewed human decision |
| `REJECTED_ROUTE_GUARD` | A previously rejected approach must not recur |

The map may operate at document, section, page, table, figure or component level.

Example:

```text
Page 1 course header = LOCKED_CONTENT + LOCKED_VISUAL
Question 1 text = LOCKED_CONTENT
Numerical-reporting paragraph = EDITABLE_WORDING
Q3/Q4 page-break controls = EDITABLE_LAYOUT
Two-column assignment layout = REJECTED_ROUTE_GUARD
```

## 8. Mandatory change contract for every revision

Every revision must begin with a bounded change contract.

```text
TARGET_ARTIFACT = <exact artifact and version>
TARGET_SCOPE = <files / sections / pages / components>
CHANGE_TYPE = semantic | wording | layout | mechanical
PROBLEM = <specific reader-visible failure>
ALLOWED_CHANGES = <exact permitted changes>
FORBIDDEN_COLLATERAL_CHANGES = <content and visual areas that must remain unchanged>
SOURCE_REFRESH = <authority files and active decisions re-read>
ACCEPTANCE_TESTS = <proof that the problem is closed and accepted material remains intact>
```

A request such as “improve layout” is not sufficiently bounded.

## 9. Full source refresh and annotation closure

Before every revision, re-read in full:

- current canonical sources;
- approved reader-facing body;
- audience contract;
- preservation map;
- active decisions;
- all still-active annotations;
- rejected-route guards;
- current rendered artifact.

A previous generated candidate or successful validation report is not sufficient authority.

User annotations should be tracked as a closure ledger:

| Field | Requirement |
|---|---|
| Annotation ID | Stable identifier |
| Exact target | Page, line, region or component |
| User intent | Meaning of the requested change |
| Implementation | Exact location and method |
| Validation evidence | Render, diff or test |
| Status | OPEN / CLOSED / REGRESSED / SUPERSEDED |

Every new version must revalidate all `CLOSED` active annotations and report any regression.

## 10. Local patch versus global regeneration

Default rule:

> A local problem should be fixed with the narrowest reliable patch, not a whole-artifact regeneration.

Global regeneration or reflow is permitted only when:

- the user explicitly approves a global redesign;
- the content structure itself changes;
- the existing production system cannot perform a safe local repair;
- the whole artifact returns to full content and visual review.

The following are global-risk changes and must trigger full regression review:

- font family or scale;
- page geometry or margins;
- global line/paragraph spacing;
- heading system;
- list/table theme;
- column system;
- template engine;
- automatic pagination or page-break strategy;
- figure sizing macros.

## 11. Semantic diff gate

After implementation, compare the new artifact with the approved body and previous accepted artifact.

The semantic diff should check at least:

- normalized visible text;
- headings and order;
- numbers, dates, weights and limits;
- mathematical formulas and symbols;
- table cells;
- figure/table captions;
- filenames and commands;
- claims and conclusion strength;
- required and prohibited actions.

Required result for a layout-only revision:

```text
SEMANTIC_DIFF_OUTSIDE_SCOPE = NONE
APPROVED_BODY_PARITY = PASS
```

Token-presence testing alone is insufficient. The check must detect additions, omissions and meaning changes.

## 12. Visual regression gate

Every revision must compare the complete artifact, not only changed pages.

Evidence should include:

- before/after PDF;
- per-page renders;
- contact sheets;
- page count and page-break locations;
- table/figure bounding boxes where relevant;
- intended changed pages;
- unintended changed pages.

Required fields:

```text
INTENDED_CHANGED_PAGES = <list>
UNINTENDED_CHANGED_PAGES = NONE | <list and justification>
LOCKED_VISUAL_REGIONS_PRESERVED = YES | NO
```

A contact sheet is useful for global rhythm but does not replace individual-page inspection for small text, clipping, formulas, footers or local composition.

## 13. Release-state model

Do not collapse all PASS states into one.

Recommended state model:

```text
CONTENT_DRAFTED
CONTENT_USER_APPROVED
IMPLEMENTED
TECHNICAL_QA_PASS
SEMANTIC_QA_PASS
READY_FOR_USER_REVIEW
USER_ACCEPTED
RELEASE_READY
RELEASED
```

Rules:

- build success does not imply semantic correctness;
- critic PASS does not imply user acceptance;
- `READY_FOR_USER_REVIEW` does not imply release readiness;
- administrative publication is separate from artifact readiness;
- a regression in any active annotation or locked region returns the artifact to the appropriate earlier state.

## 14. QA matrix

### 14.1 Source and correctness QA

- authoritative facts, numbers and labels are correct;
- no unsupported additions;
- formulas, tables and references are faithful;
- required content is complete.

### 14.2 Audience QA

- intended reader and task are explicit internally;
- reader can identify the purpose and required action quickly;
- no material belonging to another audience is exposed;
- no method, decision or reasoning expected from the reader is pre-solved without approval;
- document density and information order match the reader task.

### 14.3 Visual QA

- layout, equations, tables and figures are readable;
- document-family identity is preserved;
- no clipping, overlap, missing glyph or raw markup;
- accepted pages and visual regions remain unchanged outside scope.

### 14.4 Release QA

- student/reader, instructor/author, implementation and QA deliverables are separated;
- no solutions, keys, internal notes, logs or validation evidence leak into the reader package;
- manifest and hashes bind the actual release artifacts.

## 15. Implementation-agent boundary

Codex or another implementation agent may:

- materialize a frozen approved body;
- apply the approved visual system;
- build and render files;
- perform bounded local layout repairs;
- generate technical and regression evidence;
- package the appropriate release set.

It may not independently decide:

- what the reader should know;
- what rubric detail is public;
- what examples, exceptions or contingencies to add;
- how to reinterpret source terminology;
- whether accepted content may be deleted or reorganized;
- whether a local repair justifies a global redesign.

If the implementation agent discovers a semantic problem, it must stop and return a precise content decision request.

## 16. Human-review packaging

Human review packages should be audience- and stage-specific.

For student-facing content review, provide only the actual student artifacts needed for the current decision. Do not mix in instructor forms, manifests, QA JSON, contact sheets and internal prompts unless the reviewer explicitly asks for them.

The review package should begin with a short instruction stating:

- what is being reviewed now;
- what is not being reviewed yet;
- what decision the human should make;
- which later layers remain pending.

## 17. Course-assessment specialization

The proposed `course-assessment-authoring` skill should specialize this generic contract for:

- Homework briefs;
- Project briefs;
- milestone/proposal forms;
- student submission checklists;
- oral-defense briefs;
- instructor solutions, rubrics and calibration materials;
- student/instructor release packaging.

It should add course-specific checks for workload, assessment validity, question/deliverable counts, progression, grading burden and alignment with lecture/tutorial preparation.

Research Authoring should retain the generic reader-contract, content-approval and regression-control mechanisms so the same discipline applies to advisor reports, manuscripts and other formal documents.

## 18. Proposed end-to-end workflow

```text
canonical sources and frozen decisions
-> audience contract
-> artifact-family classification
-> source-to-reader inclusion map
-> complete reader-facing body
-> human content approval
-> approved-body freeze
-> preservation map and rejected-route guards
-> bounded implementation handoff
-> build/render
-> semantic diff
-> full visual regression
-> audience QA
-> human artifact acceptance
-> release QA
-> publication
```

For later revision:

```text
full source refresh
-> restate audience
-> read approved body + preservation map + all annotations
-> bounded change contract
-> narrow patch
-> semantic diff
-> full visual regression
-> annotation revalidation
-> human acceptance when required
```

## 19. Promotion and replay plan

Before promotion into an active Research Authoring rule set, replay this workflow on at least:

1. one student Homework brief;
2. one open-ended student Project brief;
3. one fillable milestone/proposal form;
4. one instructor grading package;
5. one advisor-facing research report;
6. one manuscript, rebuttal or reviewer-facing artifact;
7. one bounded revision where previously accepted pages must remain unchanged.

Promotion evidence must show:

- reader usability improved;
- internal material did not leak;
- approved content remained stable through rendering;
- local revision did not change unrelated content or pages;
- technical QA and human acceptance remained distinct;
- domain-specific meaning remained owned by the appropriate course or research authority.

## 20. Non-goals

- no universal document template;
- no automatic decision about what to teach, assess or publish;
- no replacement for statistical/scientific review;
- no assumption that all source material belongs in the final artifact;
- no claim that automated tests can replace human reader review;
- no permission for implementation agents to broaden semantic scope.


## 15. Quoted-source integrity and citation presentation

Direct quotation is a separate authoring mode from paraphrase and must be protected as source content.

Required rules:

1. A direct quote must be copied exactly from the cited source. Do not silently modernize, simplify, normalize, or improve its wording.
2. A substantive direct quote should use a visibly distinct quotation treatment, such as a block quote with a left rule or equivalent publication-appropriate quotation style. Do not hide a substantive quotation inside ordinary prose merely by adding quotation marks.
3. Attribution belongs immediately with the quote. Record the exact source title and, where relevant, section / policy / page locator.
4. Paraphrase must remain visually and semantically distinct from direct quotation. Do not place a paraphrase in quotation marks.
5. The approved body must contain the exact quotation, attribution text, link labels, link destinations and desired presentation role before implementation.
6. Codex or another renderer may style an approved quotation but may not invent, extend, shorten, reword, merge, or source a quotation on its own.
7. If the source does not support the desired sentence exactly, return to the author/content stage; do not manufacture a quote that sounds plausible.
8. Later revisions must verify quotation text parity and citation-target parity in addition to general semantic parity.

Recommended source map fields for quoted content:

```text
QUOTE_TEXT = <exact approved source text>
QUOTE_SOURCE = <canonical source>
QUOTE_LOCATOR = <section/page/heading>
QUOTE_STYLE = <block quote / pull quote / inline short quote>
ATTRIBUTION_TEXT = <exact approved attribution>
LINK_LABEL = <exact approved label if any>
LINK_TARGET = <exact approved target if any>
```

## 16. Document-family identity across related artifacts

A group of related artifacts should share a stable document-family identity unless a deliberate redesign is approved.

For related Homework / Project / technical-report families, explicitly freeze:

- title hierarchy;
- title wording conventions;
- course/project identity placement;
- academic-year / version placement;
- due-date or document-date label and placement;
- weight/status metadata placement when applicable;
- typeface and math family;
- page geometry;
- heading hierarchy;
- footer / page-number behavior;
- hyperlink and quotation style.

Artifact-specific values remain source-controlled; family consistency governs presentation and label structure, not the invention of missing values.

A renderer must not redesign one member of the family merely because another template is available. A later artifact should first recover the accepted family contract and then change only what its own reader task requires.



## 17. Visual rhythm and composition must be specified, not delegated to renderer taste

A renderer can satisfy clipping, overflow, page-count and token-presence checks while still producing a visibly cramped or compositionally poor document. Visual quality therefore cannot be treated as an emergent property of successful compilation.

### Failure pattern

The STAT5060 HW1 AI-policy artifact reproduced this failure:

- all required text was present;
- the quotation and links were technically correct;
- the PDF fit on one page;
- automated checks passed;
- yet body leading, paragraph spacing, section spacing and list spacing were inconsistent and too compressed for comfortable reading.

The error was not only an implementation defect. The authoring contract had failed to define a visual-rhythm target, so the implementation optimized for fitting content rather than for reading.

### Required visual-composition contract

Before rendering a substantial document, freeze a composition contract covering at least:

```text
BODY_SIZE = <size>
BODY_LEADING = <line-height / line-spacing target>
PARAGRAPH_SPACING = <target>
HEADING_SPACING_BEFORE = <target>
HEADING_SPACING_AFTER = <target>
LIST_TOP_BOTTOM_SPACING = <target>
LIST_ITEM_SPACING = <target>
QUOTE_SPACING = <target>
TABLE_ROW_SPACING = <target>
BLOCK_KEEP_TOGETHER_RULE = <rule>
PAGE_BREAK_POLICY = <rule>
PAGE_COUNT_TARGET = NONE | <actual requirement>
```

Exact implementation units may differ across LaTeX / Word / HTML, but the rendered visual rhythm must be equivalent.

### Readability over page minimization

Unless a page count is itself an approved requirement:

- do not compress line spacing or vertical whitespace merely to keep a document on one page;
- a two-page readable policy is preferable to a one-page cramped policy;
- if a short semantic block cannot fit comfortably in the remaining page space, move the whole block to the next page;
- do not leave only one or two lines of a named instruction block at the bottom of a page;
- do not use global spacing reduction as a local overflow fix.

### Semantic-block pagination

Treat short titled or labeled units as semantic blocks, for example:

- a policy subsection;
- a numerical-reporting instruction;
- a warning/caution block;
- a short numbered alternative;
- a quotation plus attribution.

For blocks short enough to fit on one page, keep the block together. If insufficient space remains, start the block on the next page rather than splitting it into a narrow fragment.

### Pixel-level visual QA

Visual QA must review the rendered pages at realistic reading/print scale, not only text extraction or bounding-box overflow.

The reviewer must explicitly judge:

- body line spacing;
- paragraph rhythm;
- heading-to-body spacing;
- list hierarchy;
- quote separation;
- density at top/middle/bottom of page;
- whether a page is cramped merely to avoid another page;
- whether a semantic block is awkwardly split;
- whether white space is purposeful rather than accidental.

A report that says only `NO_OVERFLOW = PASS` is insufficient.

### Implementation boundary

Codex may implement a frozen visual-composition contract. It must not choose its own global spacing system merely to make content fit.

If approved content does not fit under the visual contract, Codex should add a page or return a layout conflict. It should not silently tighten leading, paragraph spacing, list spacing, margins or font size.

## 18. Metadata adjacency and compact identity blocks

Metadata rows that are conceptually one block (for example Due date and Weight/Total) must be authored and rendered as one compact unit.

A blank paragraph, section-like gap or unrelated metadata field must not be inserted between adjacent rows unless explicitly approved.

The authoring contract should specify both:

- content order;
- visual adjacency.

This prevents a renderer from preserving the correct words while introducing a misleading visual hierarchy.



## 19. Page budgeting is a constrained composition problem, not a page-count reflex

A document should not oscillate between a cramped one-page version and a sparse two-page version. Page count must be decided only after content, typography and visual rhythm are treated as explicit constraints.

### Hard constraint versus soft preference

Every document should declare:

```text
PAGE_COUNT_MODE = HARD | PREFERRED | FREE
PAGE_COUNT_TARGET = <n or range or NONE>
CONTENT_MUTABLE = YES | NO
FONT_MUTABLE = YES | NO
MARGINS_MUTABLE = YES | NO
RHYTHM_MINIMUMS = <frozen spacing floor>
```

Interpretation:

- `HARD`: page count itself is a requirement; if content cannot fit without violating frozen readability constraints, return a conflict instead of silently compressing.
- `PREFERRED`: aim for the target only if it fits above the minimum readability floor.
- `FREE`: let semantic blocks and visual rhythm determine the page count.

### Compaction ladder

When a shorter document is desired, apply changes in this order:

1. remove accidental / duplicated vertical whitespace;
2. rebalance semantic-block placement and keep-together rules;
3. use the approved normal line-spacing target rather than locally enlarged spacing;
4. reduce paragraph / heading / list spacing only within the frozen acceptable range;
5. only if explicitly allowed, reconsider margins or font size;
6. never delete, paraphrase or weaken content merely to hit a page target.

A renderer must not jump directly to font reduction or ultra-tight list spacing.

### Density balance across pages

For multi-page documents, do not optimize each page independently. Review the document as a sequence.

Reject:

- a dense Page 1 followed by a mostly empty Page 2;
- a semantic block split only to fill Page 1;
- a whole section moved to Page 2 when modest spacing rebalance would keep a coherent one-page artifact;
- a page whose bottom is visually crowded while the next page is largely blank.

Prefer:

- comparable reading density across adjacent pages;
- semantic boundaries as page boundaries;
- purposeful white space;
- a single page when content comfortably fits without violating rhythm;
- two pages when one page would require compression below the readability floor.

### One-page policy / brief heuristic

For a short policy or brief whose content is frozen:

- first determine whether all semantic blocks can fit on one page using the normal family font, geometry and standard single-reading leading;
- if yes, use one page and distribute spacing consistently;
- if no, use two pages and rebalance the whole artifact rather than letting the second page contain one tiny residual block.

The page-count decision belongs to the authoring/composition stage and should be approved before rendering.

## 20. Semantic classes should not be visually mixed

Reader-facing documents often contain materially different information classes, such as:

- required task;
- ungraded instructions;
- graded assessment criteria;
- warnings / penalties;
- source quotation;
- contextual explanation.

If two classes imply different reader actions, give them distinct visual hierarchy.

A scored component should not appear as an ordinary prose paragraph between ungraded instructions. If a reader must treat it as part of assessment, use an explicit heading, compact table, or otherwise distinct block.

Likewise, warnings, quotations and optional context should not borrow the same hierarchy as required tasks.

The source-to-reader map should therefore add:

```text
SEMANTIC_CLASS = task | instruction | assessed | warning | source_quote | context
VISUAL_ROLE = body | heading | table | quote | note
```

Visual distinction must clarify meaning without turning the document into cards/dashboard UI.



## 21. Continuous-flow zones and explicit break authority

A page break is not a neutral rendering detail. It changes reading flow, grouping and emphasis.

### Continuous-flow contract

When the author or reviewer states that a sequence of blocks should “follow” one another, treat that sequence as a **continuous-flow zone**.

Example:

```text
FLOW_ZONE = Submission -> Report format -> Page limit -> Analysis workflow -> Numerical reporting -> AI assistance
INTERNAL_HARD_BREAKS = FORBIDDEN
HARD_BREAK_AFTER = AI assistance
```

Within a continuous-flow zone:

- the renderer may allow the typesetting engine to break naturally between blocks;
- short blocks may use bounded keep-together / needspace rules to avoid awkward splits;
- the renderer may not insert a fixed hard page break merely to “balance” pages;
- the authoring planner may not later introduce a hard break that contradicts an earlier explicit flow instruction unless the user re-approves the change.

### Explicit negative constraints outrank later layout optimization

If a user has said:

- “do not break here”;
- “these sections should follow one another”;
- “only break after X”;
- “do not move Y”;

that instruction becomes an active rejection/recurrence guard.

A later planner or renderer cannot override it because a different page composition appears cleaner.

Required field:

```text
FLOW_GUARDS:
- <exact user-approved continuity / break constraint>
```

Every revision must revalidate all flow guards before proposing a new page plan.

### Hard-break authorization

A fixed hard break may be introduced only when one of these is true:

1. the user explicitly approved the break;
2. the document-family contract makes the break structural (for example, a new chapter/section artifact);
3. a hard page-count requirement and frozen block integrity leave no legal natural solution, in which case the break is returned for approval before rendering.

“Page balance” alone is not sufficient authority.

### Natural flow versus block integrity

The default mechanism for ordinary prose/rules is:

1. continuous natural flow;
2. bounded keep-together for short semantic blocks;
3. hard break only at an explicitly approved boundary.

This prevents the common failure in which a large blank lower half is created by a planner-selected hard break while the next page begins with content that could have flowed naturally.

