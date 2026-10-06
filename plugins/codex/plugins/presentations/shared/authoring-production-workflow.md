# Canonical Presentation Authoring and Production Workflow

Status: **canonical workflow contract**  
Applies to: non-trivial teaching, research, business and technical presentations  
Primary evidence: STAT5060 Tutorial 01, CAT-TRACE, CUHK Date, Lucerna and Bobbio production/review experience

## 1. Objective

Produce a high-quality audience artifact quickly, then converge through bounded revision without repeatedly breaking accepted work.

The workflow is designed for two simultaneous goals:

1. quality: content, pedagogy, visual composition and technical delivery must all be correct;
2. efficiency: the user is not the first QA pass and normally reviews only two to four increasingly small deltas.

Process infrastructure is subordinate to the presentation. After the required planning authority exists, the workflow must move to visible component/golden-page evidence rather than spending open-ended time extending governance machinery.

## 2. Preserve the original convergence architecture

The following foundations remain mandatory:

- separate `NEW_DECK`, `EXISTING_DECK_REVISION` and `FAILED_VERSION_RECOVERY` modes;
- stable semantic PageIDs rather than physical page-number identity;
- version lineage and page/component ancestry;
- cumulative human-feedback memory with lifecycle and supersession;
- semantic, visible-copy and visual locks;
- explicit layout archetypes and shared-component ownership;
- no executor-authored audience copy;
- cumulative acceptance standards;
- deterministic QA before independent visual/pedagogical review;
- immediate locking after explicit human acceptance;
- two-to-four-round monotone convergence;
- user-facing delta review rather than repeated full-deck annotation;
- final full-deck regression before delivery.

Later workflow additions strengthen these rules; they do not replace them.

## 3. Task proportionality

Do not impose failed-version recovery machinery on every presentation.

### 3.1 New deck

Minimum authority:

- audience and purpose;
- source/evidence set;
- narrative and section map;
- page jobs;
- exact visible copy or an explicitly authorised copy-writing stage;
- layout archetypes;
- shared template/components;
- acceptance standard.

### 3.2 Existing deck revision

Add:

- exact reviewer-seen baseline;
- stable PageIDs and ancestry;
- cumulative feedback registry;
- accepted elements and locks;
- current-round modify/freeze scope;
- historical regression guards.

### 3.3 Failed-version recovery

Add only when history is genuinely complex:

- authoritative version map;
- incident/lineage ledger;
- annotation recovery and lifecycle resolution;
- explicit content-recovery baseline;
- rejected-layout inventory;
- recovery-specific proof pages.

Once these exist, do not continue rebuilding the control plane instead of producing the presentation.

## 4. Role division

### 4.1 ChatGPT Web / Planner / Presentation Author

Owns human-level judgment:

- read and reconcile sources;
- define audience, purpose and desired audience change;
- decide narrative, section order and page count;
- assign one page job to every PageID;
- decide required and forbidden scientific/teaching objects;
- write/freeze audience-visible copy;
- distinguish audience slides, speaker notes and instructor-learning material;
- choose semantic layout relations and approved archetypes;
- ingest and normalize human feedback;
- decide lifecycle, supersession, locks and unlocks;
- make statistical, scientific, pedagogical and assessment judgments;
- prepare the autonomous Codex Controller Goal;
- review only subtle/high-level deltas after internal QA.

ChatGPT Web may invoke the presentations capability for authoring and review orchestration, but it does not implement slide source, compile files, manufacture figures or run the production toolchain.

### 4.2 Codex Parent Controller

Owns autonomous production orchestration inside one Goal:

- launch fresh Producer and fresh read-only Auditor contexts;
- maintain exact candidate identity and round scope;
- route ordinary findings back to a new Producer;
- require a new fresh Auditor after every source change;
- continue repair/re-review without user relay;
- stop only for a genuine Planner semantic decision, human-only external action or proven reviewer-runtime failure;
- publish only an independently accepted candidate/delta.

The user must not be asked to copy completion blocks between Producer, Auditor and Planner.

### 4.3 Codex Producer

Owns implementation only:

- typeset approved copy;
- implement approved layout archetypes and shared components;
- create approved figures/assets from frozen specifications;
- build/render/export;
- run deterministic smoke and production checks;
- create a proof-carrying patch manifest;
- fix Auditor findings within the frozen scope;
- commit/push coherent candidates.

Producer may not:

- decide what to teach or claim;
- add/delete/paraphrase visible prose;
- create/merge/delete page jobs;
- choose a new archetype;
- remove difficult content to solve layout pressure;
- edit acceptance rules to make the candidate pass;
- declare final acceptance.

### 4.4 Independent deterministic Auditor

Runs in a fresh read-only context/process after Producer stops.

Checks:

- authority coverage and exact copy;
- PageID/ancestry and round scope;
- locks and protected paths;
- required-object preservation;
- component consumers and layout archetypes;
- fonts, math glyphs, code copyability and PDF structure;
- historical regression guards;
- evidence and artifact identity.

### 4.5 Independent rendered-artifact Reviewer

Reviews final renders, not executor claims.

Checks:

- hierarchy and reading path;
- scientific-object scale;
- whitespace and semantic proximity;
- visual consistency and rhythm;
- natural audience language;
- pedagogical or decision sufficiency;
- whole-deck coherence.

It remains read-only and blind to expected human-rejection answers.

### 4.6 User

The user is the final subtle decision-maker, not routine QA.

The user should normally decide only matters such as:

- two acceptable visual alternatives;
- subtle tone/preference;
- whether a page/component is ready to lock;
- final subjective acceptance.

## 5. End-to-end workflow

### Stage 0 — Mode and source intake

1. classify the task as new deck, revision or recovery;
2. identify exact sources and baseline artifacts;
3. separate source material from derived presentation content;
4. identify presentation format and canonical template;
5. define what success means for the audience.

Output: `DECK_BRIEF`.

### Stage 1 — Narrative and semantic page plan

ChatGPT freezes:

- section sequence;
- target page count or bounded range;
- stable PageIDs;
- one page job per PageID;
- primary scientific/teaching object;
- prerequisite/transition relationship;
- required and forbidden objects;
- source anchors;
- student/audience versus presenter/instructor boundary.

Output: `PAGE_AUTHORITY`.

No slide implementation starts while substantive page jobs remain unresolved.

### Stage 2 — Exact visible copy

ChatGPT freezes all audience-visible strings:

- titles and subtitles;
- body prose/bullets;
- equations and mathematical labels;
- Question/Answer text;
- table cells;
- figure/diagram labels;
- code shown to the audience;
- captions and source lines;
- administrative instructions.

Every text object has a semantic role. Instructor-learning needs route to notes/study material unless there is a specific pedagogical reason to alter the audience slide.

Output: `VISIBLE_COPY_AUTHORITY`.

If exact wording is intentionally delegated, that delegation is a bounded authoring stage owned by ChatGPT/writing skills, not by the layout executor.

### Stage 3 — Layout semantics and archetypes

ChatGPT records the semantic relationship before choosing composition:

- `VERTICAL_EXPLANATION`;
- `SEQUENTIAL_DEPENDENCY`;
- `PEER_COMPARE`;
- `FIGURE_PLUS_INTERPRETATION`;
- `QUESTION_TABLE_ANSWER_VERTICAL`;
- `DERIVATION`;
- `CODE_PEER`;
- `LARGE_FIGURE`;
- `ADMIN_TABLE`;
- `TITLE`;
- `CLOSE`.

Columns are allowed for peer relationships, not merely because horizontal space exists. Each archetype defines fallback and forbidden fallback.

Output: `LAYOUT_AUTHORITY`.

### Stage 4 — Shared-component proof sheet

Before a full deck, Codex Controller produces proofs for the actual deck's:

- title page;
- header/section navigation;
- footer/source/navigation/page number;
- typography hierarchy;
- Question/Answer;
- table;
- code;
- caption;
- scientific figure/diagram treatment;
- closing page.

Use real deck content, not lorem ipsum.

Internal loop:

```text
Producer -> deterministic checks -> fresh Reviewer -> repair -> fresh Reviewer
```

The user sees only independently filtered proof alternatives. Explicit acceptance locks the component.

### Stage 5 — Golden-page proof pack

Select a small representative set, normally six to ten pages, covering:

- the highest-risk content;
- every major layout archetype;
- pages with repeated historical failures;
- dense and sparse pages;
- code/table/figure/formula/Q&A pages;
- opening and closing.

Do not build the entire deck as the first visual prototype.

The same autonomous Producer/Reviewer loop runs. User acceptance locks the golden pages and establishes the deck's density/composition floor.

### Stage 6 — Full candidate production

Only after content, copy, components and golden pages are sufficiently frozen:

1. Producer assembles the full deck;
2. deterministic Auditor checks exact copy, locks, archetypes, code/math/PDF and historical guards;
3. rendered Reviewer checks every page and the contact-sheet sequence;
4. Parent routes all ordinary P0/P1/P2 findings through automatic repair and a new fresh review;
5. only an internally accepted candidate reaches the user.

The user must not be the first person to discover obvious whitespace, header/footer, typo, clipping, code, content-deletion or reading-path defects.

### Stage 7 — First user review and locking

User feedback is converted to structured records:

```text
feedback_id
source candidate/page/region
target PageID/component
category: semantic/copy/layout/component/visual
required change
verification method
lifecycle state
```

Rules:

- explicit acceptance creates a human lock;
- pages without requested changes are round-frozen;
- unresolved ambiguity returns to ChatGPT Planner, not Codex improvisation.

### Stage 8 — Bounded revision

Every revision round declares:

- exact baseline candidate;
- pages/components allowed to change;
- human-locked scope;
- round-frozen scope;
- shared-component dependency consumers;
- addressed feedback IDs;
- explicit unlocks;
- change budget.

Producer supplies a proof-carrying patch manifest. Source/render changes outside the allowlist fail.

Parent runs repair and fresh review autonomously. The user receives only before/after deltas for changed pages plus minimum context.

### Stage 9 — Monotone convergence

Every accepted round satisfies:

```text
open_feedback_next is a strict subset of open_feedback_current
human_locked_pages_next is a superset of human_locked_pages_current
human_locked_components_next is a superset of human_locked_components_current
unrelated_source_changes = 0
unrelated_render_changes = 0
closed_guard_recurrences = 0
```

Normal target: two to four user review rounds.

If open issues do not decrease or accepted work reopens, do not generate another broad version. Diagnose the root authority, copy, archetype, component or review-coverage failure first.

### Stage 10 — Final full-deck regression and delivery

Run complete final checks over the exact delivery artifact:

- all pages and ordering;
- all active historical guards;
- semantic/copy/layout/component locks;
- header/footer/navigation/outline;
- fonts and mathematical glyphs;
- figure/table/code/source fidelity;
- whitespace and semantic proximity;
- code/PDF text copyability;
- final contact-sheet rhythm;
- artifact hashes and editable-source reproducibility.

Delta review never replaces final whole-deck regression.

## 6. Anti-shortcut rules retained from later hardening

The workflow also retains:

- immutable authority bundle before execution;
- explicit round allowlist and change budget;
- proof-carrying patch manifest;
- dependency-aware layered locks;
- required-object relocation records;
- independent validator/reviewer trust domains;
- no fixture-ID or magic-value detector logic;
- hidden historical regression holdouts where appropriate;
- honest `NOT_INDEPENDENTLY_VERIFIED` states;
- recurrence escalation to shared-root repair;
- no infinite project-local patch chain.

These controls support production; they must not postpone visible proof pages once the necessary authority is already frozen.

## 7. Artifact-first progress rule

A presentation task is failing operationally when it produces expanding governance documents but no visible audience artifact after content authority is ready.

Required progress sequence:

```text
content/page authority
-> visible copy
-> component proof sheet
-> golden-page proof pack
-> full candidate
```

Generic plugin/validator development may proceed in parallel, but it is not a prerequisite for ChatGPT authoring, component proofs or project-local golden pages when the project already has adequate bounded review controls.

## 8. Review and repair inside one Goal

A non-trivial Codex production Goal should normally be a controller task:

```text
Parent Controller
├─ fresh Producer
├─ fresh read-only deterministic/visual Auditor
├─ fresh Producer repair
├─ new fresh Auditor
└─ final independently accepted candidate/delta
```

Ordinary implementation, build, layout, copy-fidelity, visual and reviewer findings are internal engineering work. Do not return intermediate completion blocks to the user or require the user to launch reviewers manually.

## 9. User-facing review package

Each user review contains only:

- changed/proof pages and affected shared components;
- before/after comparison where applicable;
- resolved feedback IDs;
- remaining genuine decisions;
- proof that unrelated locks remain unchanged;
- concise statement of what is ready to lock.

Do not expose internal QA logs, fixture tables, hashes or controller chatter unless the user asks.

## 10. Immediate project adoption

A project may adopt this workflow before the generic presentations runtime is fully implemented.

Required minimum:

- ChatGPT freezes page/copy/layout authority;
- one Codex Controller Goal performs Producer/Reviewer/repair loops;
- accepted components/pages are recorded as locks;
- later revisions use an explicit allowlist and delta review;
- final release runs whole-deck regression.

The generic plugin should encode and automate this workflow over time, but plugin maturity must not block a currently needed presentation.
