# Canonical Presentation Authoring and Production Workflow

Status: **canonical workflow contract**  
Applies to: non-trivial teaching, research, business, product, and technical presentations  
Primary evidence: STAT5060 Tutorial 01, CAT-TRACE, CUHK Date, Lucerna, Bobbio, and prior presentation-plugin production/review work

**Mandatory first read before any non-trivial execution:**

- `pre-execution-cumulative-acceptance-contract.md`

Then read with:

- `chatgpt-web-authoring-contract.md`
- `anti-shortcut-production-contract.md`
- `independent-review-contract.md`

No later workflow, domain skill, or task-local prompt may weaken the cumulative acceptance and review-ownership rules in the pre-execution contract.

## 1. Objective

Produce a strong audience artifact quickly, then converge through bounded revision without repeatedly breaking accepted work.

The workflow optimizes three things together:

1. **content quality** — claims, teaching, evidence, and audience boundaries are correct;
2. **visual quality** — hierarchy, composition, whitespace, scale, and shared chrome are deliberate;
3. **revision efficiency** — the user is not the first QA pass and normally reviews only two to four shrinking deltas.

Infrastructure is subordinate to the presentation. Once the necessary authority exists, work must move to visible artifacts rather than expanding governance indefinitely.

## 2. Foundations that must never be lost

The following remain mandatory:

- separate new-deck, minor-revision, major-revision, and failed-version-recovery modes;
- stable semantic PageIDs rather than physical page-number identity;
- version lineage and page/component ancestry;
- cumulative human-feedback memory with lifecycle and supersession;
- semantic, visible-copy, layout, page-body, and shared-component locks;
- explicit layout grammar rather than page-local improvisation;
- no executor-authored audience copy;
- cumulative acceptance standards;
- prebuild Critic for major revision/recovery;
- deterministic QA separated from rendered visual/pedagogical review;
- immediate locking after explicit human acceptance;
- two-to-four-round monotone convergence;
- user-facing delta review rather than repeated full-deck annotation;
- final whole-deck regression before delivery.

Later hardening strengthens these rules; it does not replace them.

## 3. Task classification and Critic gate

Classification happens before authoring or production.

### 3.1 New deck

A small, low-risk deck may proceed directly from Planner authority to component/golden proof. A substantial teaching, scientific, high-stakes, or template-defining deck is treated as major and receives a prebuild Critic before broad production.

### 3.2 Minor revision

A revision is minor only when all are true:

- page count and section order are unchanged;
- no page job or scientific/teaching claim changes;
- no shared title/header/footer/navigation/template redesign;
- no new layout archetype, page split, or page merge;
- copy changes are local and source-supported;
- scope is normally at most three pages and at most one already-defined component;
- no closed historical guard has recurred;
- the user has not requested a broad rethink or full-history recovery.

A separate prebuild Critic is optional. ChatGPT Planner may freeze the bounded scope directly.

### 3.3 Major revision

A fresh prebuild Critic is mandatory when any of these holds:

- page count, section order, narrative, or page jobs change;
- substantial visible-copy/content changes span multiple pages;
- shared shell/template/header/footer/navigation changes;
- new archetypes, page splits/merges, or major figure systems are introduced;
- statistical, scientific, pedagogical, or assessment meaning changes;
- repeated regressions suggest the current authority is wrong;
- the user asks to rethink, rebuild, overhaul, or reread all history.

If uncertain, classify as major.

### 3.4 Failed-version recovery

Recovery is always major. Add:

- authoritative version map;
- incident/lineage ledger;
- raw annotation recovery and lifecycle resolution;
- positive and negative visual/content baselines;
- explicit content-recovery decision;
- prebuild Critic before implementation.

### 3.5 Critic consequence

The prebuild Critic reviews the Planner package, not rendered production. It checks:

- historical-feedback consumption;
- page count and teaching/decision sequence;
- page-by-page content sufficiency and audience boundary;
- layout suitability and historical-regression risk;
- Controller workflow and review plan.

Major production is blocked until the Critic returns PASS. A major Planner amendment after Critic review requires a fresh Critic pass. Minor corrections explicitly bounded by the Critic may be amended without reopening unrelated architecture.

## 4. Role division

### 4.1 ChatGPT Web / Planner / Presentation Author

Owns human-level judgment:

- read and reconcile sources;
- define audience, purpose, duration, format, and desired audience change;
- classify the task and decide whether Critic is mandatory;
- decide narrative, section order, page count, and PageIDs;
- assign one page job and primary object per page;
- decide required/forbidden scientific or teaching objects;
- write/freeze audience-visible copy;
- distinguish audience slides, speaker notes, instructor-learning material, and internal planning;
- choose semantic layout relation and approved archetype;
- ingest and normalize feedback;
- decide lifecycle, supersession, locks, and unlocks;
- make statistical, scientific, pedagogical, and assessment judgments;
- prepare Critic and autonomous Codex Controller Goals;
- inspect renders for source/meaning/specification defects;
- present only filtered deltas and genuine decisions to the user.

ChatGPT Web may invoke presentations for authoring and review orchestration, but it does not implement slide source, compile, render, or run production tooling.

### 4.2 Independent prebuild Critic

Required for major revision/recovery and substantial high-risk new decks.

The Critic is fresh and read-only. It:

- verifies the exact feedback/source counts consumed;
- independently evaluates page count and sequence;
- audits every planned page for content correctness, student/audience sufficiency, copy boundary, layout suitability, and historical guards;
- audits whether the Codex Controller really follows the workflow;
- returns PASS or a bounded Planner-amendment list.

It does not author slides or repair the specification itself.

### 4.3 Codex Parent Controller

Owns autonomous production orchestration inside one Goal:

- launch fresh Producer and fresh read-only Auditor/Reviewer contexts;
- bind exact candidate identity, authority, and round scope;
- route ordinary findings back to a fresh Producer;
- require a new fresh Auditor after every source change;
- continue repair/re-review without user relay;
- stop only for a genuine Planner semantic decision, human-only external action, or proven reviewer-runtime failure;
- publish only an independently accepted candidate or delta.

### 4.4 Codex Producer

Owns implementation only:

- typeset approved copy;
- implement approved archetypes and components;
- create approved figures/assets from frozen values and labels;
- choose line breaks, spacing, widths, alignment, and responsive fallback **inside the approved archetype and token ranges**;
- crop/scale assets without changing meaning;
- build/render/export;
- run deterministic smoke/production checks;
- create proof-carrying patch manifests;
- fix Auditor findings inside the frozen scope;
- commit/push coherent immutable candidates.

Producer may not:

- decide what to teach, claim, omit, merge, or split;
- add/delete/paraphrase visible prose;
- change page count, section order, or page jobs;
- invent a new layout archetype;
- delete difficult content to fix layout pressure;
- change shared components without an explicit unlock;
- edit acceptance rules to make the candidate pass;
- declare final acceptance.

### 4.5 Independent deterministic Auditor

Runs after Producer stops, in a fresh read-only process/context.

Checks:

- authority coverage and exact copy;
- PageID/ancestry and round scope;
- locks and protected paths;
- required-object preservation;
- component consumers and archetypes;
- fonts, math glyphs, code copyability, PDF structure, and artifact identity;
- historical regression guards;
- versioning and evidence integrity.

### 4.6 Independent rendered-artifact Reviewer

Reviews final renders, not executor claims.

Checks:

- hierarchy and reading path;
- primary scientific/decision object scale;
- whitespace and semantic proximity;
- visual consistency and deck rhythm;
- natural audience language;
- pedagogical or decision sufficiency;
- whole-deck coherence.

### 4.7 GPT Work

GPT Work is the final aesthetic, reader-effort, and pedagogical/communication gate for formal decks.

For a major/new/recovery full candidate, GPT Work reviews all pages and the full contact sheet on the exact immutable artifact.

For a minor bounded revision, GPT Work may review only the changed pages, affected shared-component consumers, and full contact sheet **when** semantics, page count, section order, shell, and archetypes remain locked. Final release still requires one whole-deck regression.

GPT Work does not override deterministic failures, invent course/scientific content, or act as the implementation agent.

### 4.8 User

The user is the final subtle decision-maker, not routine QA.

The user should normally decide only:

- two already acceptable visual alternatives;
- subtle tone or preference;
- whether a page/component is ready to lock;
- final subjective acceptance.

## 5. Freeze ladder

Presentation production proceeds through explicit freezes. A later stage cannot silently reopen an earlier one.

### F0 — Source and baseline freeze

Freeze:

- source/evidence set;
- exact reviewer-seen baseline;
- artifact family/version identity;
- historical-feedback corpus and current locks.

### F1 — Narrative and page-job freeze

Freeze:

- section sequence;
- page count or bounded range;
- stable PageIDs;
- one page job per PageID;
- primary object;
- required/forbidden objects;
- source anchors and transitions;
- audience versus presenter/instructor boundary.

### F2 — Visible-copy freeze

Freeze all audience-visible strings:

- titles/subtitles;
- prose/bullets;
- equations and labels;
- Question/Answer;
- table cells;
- figure labels;
- code shown;
- captions/source lines;
- administrative instructions.

### F3 — Layout-semantics freeze

Freeze:

- semantic relationship;
- layout archetype;
- reading path;
- primary object priority;
- allowed and forbidden fallback;
- shared-component bindings.

### F4 — Shared-component freeze

After real-content proof and internal review, lock:

- title;
- header/navigation;
- footer/source/buttons/page number;
- typography;
- Question/Answer;
- table/code/caption/figure grammar;
- closing.

### F5 — Golden-page composition freeze

Lock representative composition, density, scale, and archetype behavior across six to ten real high-risk pages.

### F6 — Full-candidate freeze

Freeze the exact candidate commit, source, render, hashes, page map, and review bundle for independent full review.

### F7 — Human locks

Explicit user acceptance locks the page/component until a named unlock states reason and scope.

## 6. Historical-feedback consumption

Historical feedback is cumulative, but not every agent rereads every raw sentence in every minor round.

### 6.1 Major revision/recovery

ChatGPT Planner and prebuild Critic reread:

- the complete raw feedback history;
- direct human decisions;
- actual rendered lineage;
- lifecycle/supersession records;
- positive and rejected baselines.

They report exact counts, unresolved conflicts, and affected PageIDs/components before production.

### 6.2 Every Codex round

Codex must consume a read-only compiled authority bundle containing:

- all active global guards;
- all guards for modified PageIDs/components;
- current human locks and round-frozen scope;
- current-round feedback;
- ancestry and component consumers;
- unresolved conflicts, if any.

The deterministic Auditor verifies that the bundle covers the cumulative registry. Codex may not reinterpret raw human comments or resolve conflicts.

### 6.3 Minor revision

ChatGPT reads:

- current feedback;
- exact baseline;
- active global guards;
- full affected-page/component history;
- current locks and dependencies.

A recurrence, ambiguity, or shared-root change escalates the task to major and triggers full-history Critic review.

### 6.4 Authority precedence

Use:

```text
latest explicit human decision
> active raw feedback and named Planner amendment
> lifecycle/supersession decisions
> compiled guard registry
> latest candidate
> executor preference
```

A normalized guard organizes history; it cannot reverse an active human decision.

## 7. Layout grammar

Layout is chosen from the semantic relationship, not from available space.

### 7.1 When columns are appropriate

Columns are appropriate when regions are true peers or a stable object/explanation pair:

- R versus Python code;
- before versus after;
- model A versus model B;
- written analysis versus oral defense;
- figure plus interpretation;
- image pair or two-panel evidence;
- independent peer concepts that can be read in either order.

Required conditions:

- neither side depends on reading the other first;
- both sides can remain legible at normal slide scale;
- headings/formulas share optical anchors;
- the primary object is not shrunk merely to preserve symmetry;
- interpretation remains adjacent to the corresponding evidence.

### 7.2 When columns are forbidden

Use a vertical path for:

- derivations;
- algorithms and ordered updates;
- cause/mechanism chains;
- Question -> evidence -> Answer;
- count -> exposure -> rate reasoning;
- stepwise model interpretation;
- any page where the right side depends on the left side;
- prose split into columns only to fill horizontal space.

A useful test:

> If the audience must finish the left region before the right region makes sense, the page is sequential and should normally be vertical.

### 7.3 Responsive fallback

Codex may use only frozen fallbacks, such as:

- widen the primary object;
- reduce non-primary spacing;
- move a short interpretation directly below evidence;
- use a single vertical sequence;
- regenerate a figure for slide scale;
- split only when Planner authority explicitly permits it.

Shrinking fonts, deleting copy, inventing captions, or switching to arbitrary cards/columns are not valid fallbacks.

## 8. Whitespace and density rules

Whitespace is judged **after** content sufficiency.

### 8.1 Intentional whitespace

Whitespace is acceptable when:

- the page job is complete;
- the primary object is already at a useful, readable scale;
- the reading path is clear;
- the space creates deliberate breathing room;
- title/closing identity benefits from restraint.

### 8.2 Meaningless whitespace

A page fails when a large unused region coexists with any of:

- an undersized primary figure/table/formula/code block;
- interpretation stranded far from its evidence;
- a result artificially pushed to the bottom;
- copy compressed into tiny type;
- columns that create empty lower regions;
- missing explanation or deleted content;
- a composition that appears unfinished.

Do not fill space with slogans, cards, decorative arrows, repeated labels, or generic takeaways. Use available body space to enlarge the primary object, improve grouping, or restore needed explanation.

A geometric detector may flag a large contiguous unused body region, but final judgment remains semantic: empty area alone is not a failure; empty area caused by weak composition or incomplete teaching is.

### 8.3 Whole-slide review

Whitespace must be reviewed at whole-slide scale and in the contact-sheet sequence. Crops cannot establish page balance.

## 9. End-to-end workflow

### Stage 0 — Mode, severity, and source intake

Classify the task and identify exact sources, baseline, format, template, and audience outcome.

Output: `DECK_BRIEF` and `SOURCE_AND_BASELINE_MANIFEST`.

### Stage 1 — Narrative and semantic page plan

ChatGPT freezes F1.

Output: `PAGE_AUTHORITY`.

### Stage 2 — Exact visible copy

ChatGPT freezes F2.

Output: `VISIBLE_COPY_AUTHORITY`.

### Stage 3 — Layout semantics and archetypes

ChatGPT freezes F3 using the grammar above.

Output: `LAYOUT_AUTHORITY`.

### Stage 4 — Prebuild Critic when required

Major/new-high-risk/recovery tasks receive an independent Critic.

The Critic must PASS before broad production. Minor bounded revisions may skip this stage when the classification conditions are met.

### Stage 5 — Shared-component proof

Codex Controller produces real-content component proofs and internally closes ordinary findings.

User acceptance creates F4 locks.

### Stage 6 — Golden-page proof

Select six to ten high-risk/representative pages. Internal Producer/Reviewer repair precedes user review.

User acceptance creates F5 locks.

For an urgent recovery where the user explicitly rejects another proof round, a major Critic may authorize direct full-deck production only when the shell, copy, archetypes, historical guards, and full review route are sufficiently frozen. This is an exception, not the default.

### Stage 7 — Full candidate production

Producer builds the full deck. Deterministic Auditor and rendered Reviewer inspect the complete artifact. Parent automatically repairs P0/P1/P2 and launches fresh re-review.

Only an internally accepted candidate reaches GPT Work or the user.

### Stage 8 — GPT Work gate

Major/full candidate: all pages plus full contact sheet.  
Minor bounded revision: changed pages + affected consumers + full contact sheet, provided global structure remains locked.

### Stage 9 — User review and locks

User feedback becomes structured records. Explicit acceptance creates F7 locks; unchanged out-of-scope pages are round-frozen.

### Stage 10 — Bounded revision

Every round declares exact baseline, allowlist, locks, dependencies, feedback IDs, unlocks, and change budget. Producer supplies a proof-carrying patch manifest. Parent performs autonomous repair/re-review.

### Stage 11 — Final whole-deck regression and delivery

Run complete checks over the exact delivery artifact. Delta review never replaces final full-deck regression.

## 10. Minor-revision route

A minor route is intentionally lighter:

```text
Planner classifies minor
-> freeze exact baseline and <=3-page / <=1-component allowlist
-> read affected history + active global guards
-> Codex Producer
-> deterministic delta audit
-> rendered delta review + full contact-sheet glance
-> automatic repair and fresh review
-> Planner/user subtle acceptance
-> update locks
```

Escalate to major immediately if page jobs, shell, archetypes, page count, broad copy, or closed guards change.

## 11. Major-revision/recovery route

```text
full raw history/source reread
-> Planner freezes F0-F3
-> independent prebuild Critic
-> amend and rerun Critic until PASS
-> component/golden proof unless specifically waived by Critic/Planner
-> autonomous full production
-> deterministic + rendered full review
-> GPT Work all-page final gate
-> user final subtle acceptance
```

The user is not asked to inspect intermediate candidates or perform routine QA.

## 12. Monotone convergence

Each accepted revision round satisfies:

```text
open_feedback_next is a strict subset of open_feedback_current
human_locked_pages_next is a superset of human_locked_pages_current
human_locked_components_next is a superset of human_locked_components_current
modified_ids are a subset of the explicit allowlist
unrelated_source_changes = 0
unrelated_render_changes = 0
closed_guard_recurrences = 0
```

Normal target: two to four user review rounds.

If open issues do not decrease or accepted work reopens, stop producing broad candidates. Diagnose the root authority, copy, archetype, component, or review-coverage failure.

## 13. Artifact-first progress rule

A presentation task is failing operationally when it produces expanding governance documents but no visible audience artifact after content authority is ready.

Required sequence:

```text
source/baseline
-> page authority
-> visible copy
-> layout authority
-> Critic when required
-> component/golden evidence
-> full candidate
-> bounded revisions
-> final delivery
```

Generic validator/plugin development may proceed in parallel; it is not automatically a blocker for project-local authoring and visible production.

## 14. User-facing review package

Each user review contains only:

- changed/proof pages and affected components;
- before/after comparison where applicable;
- resolved feedback IDs;
- remaining genuine decisions;
- proof that unrelated locks remain unchanged;
- concise statement of what is ready to lock.

Do not expose internal QA logs, fixture tables, hashes, or controller chatter unless requested.

## 15. Completion principle

A deck is complete only when content authority, rendered quality, historical guards, independent review, and final artifact identity agree.

A file existing, compiling, or passing executor self-tests is never sufficient by itself.
