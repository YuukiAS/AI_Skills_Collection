# Research Authoring — Canonical Production, Review, and Convergence Workflow

Status: **PROMOTE_NOW / CANONICAL WORKFLOW CANDIDATE**  
Date: 2026-10-06  
Primary evidence: repeated STAT5060 HW1 / Final Project document failures and the mature Presentations convergence workflow

Related inputs:

- `docs/plugin-todos/research-writing-student-audience-and-pre-render-approval.md`
- `docs/plugin-todos/research-authoring-layout-convergence-and-human-review-budget.md`
- `docs/plugin-todos/presentations-authoring-production-workflow.md`
- `plugins/codex/plugins/presentations/shared/authoring-production-workflow.md`
- `plugins/codex/plugins/presentations/shared/anti-shortcut-production-contract.md`
- `plugins/codex/plugins/presentations/shared/independent-review-contract.md`

## 1. Objective

Produce a high-quality reader-facing document quickly, then converge through bounded revision without repeatedly breaking accepted content or asking the user to perform routine QA.

The workflow optimizes two goals simultaneously:

1. **quality** — content, audience fit, information architecture, visual composition and technical delivery must all be correct;
2. **efficiency** — the user is not the first QA pass and normally receives only independently filtered proof/delta artifacts and one final acceptance candidate.

A technically valid PDF can still be wrong. Compilation, searchable text, no clipping, a clean worktree, test PASS or executor self-review do not establish reader acceptance.

## 2. Production modes

Classify every task before authoring.

### 2.1 `NEW_DOCUMENT`

Use when no accepted reader artifact exists.

Required authority:

- audience and reader task;
- source/evidence set;
- document job and section map;
- exact visible copy or an explicitly authorised copy-writing stage;
- information architecture;
- document-family and visual-rhythm contract;
- acceptance standard.

### 2.2 `EXISTING_DOCUMENT_REVISION`

Add:

- exact reviewer-seen baseline;
- stable semantic BlockIDs;
- block ancestry;
- cumulative feedback registry;
- accepted semantic/copy/visual locks;
- round allowlist;
- historical regression guards.

Do not fall back to “read the latest PDF and improve it.”

### 2.3 `FAILED_VERSION_RECOVERY`

Use when repeated versions reintroduce closed defects, user review is becoming the debugging loop, or the candidate history contains contradictory authorities.

Add:

- authoritative version lineage;
- incident ledger;
- complete feedback recovery and lifecycle resolution;
- explicit good/bad baseline mapping;
- rejected-layout inventory;
- proof-page/component pack;
- independent validation/review topology;
- root-cause stop rules;
- explicit human-review budget.

Once the control plane is sufficient, move to visible proof artifacts. Do not continue expanding governance while postponing the document.

## 3. Canonical artifact graph

Every substantial document family should maintain:

```text
ArtifactFamily
  ├── VersionLineage
  ├── BlockRegistry
  │     ├── StableBlockID
  │     ├── semantic job
  │     ├── semantic class
  │     ├── visible-copy version
  │     ├── visual role
  │     ├── ancestors
  │     └── locks
  ├── SharedComponentRegistry
  ├── HumanFeedbackRegistry
  ├── AcceptanceStandard
  ├── ValidatorRuntime
  └── CandidateEvidence
```

Physical page number is presentation order, not semantic identity. A block may move pages without losing its feedback history or lock state.

## 4. Layered locks

Maintain separate locks.

### 4.1 Semantic lock

Freezes purpose, claims, requirements, numbers, formulas, conclusions, sources and required/forbidden content.

### 4.2 Visible-copy lock

Freezes every reader-visible string, including titles, labels, table cells, captions, quotations, attribution and links.

### 4.3 Information-architecture lock

Freezes semantic zones, block order, scored/unscored or evidence/context separation, and reader flow.

### 4.4 Visual-role lock

Freezes each block's role: title, metadata, paragraph, list, table, quote, warning, assessed block, caption or reference.

### 4.5 Page-body visual lock

Freezes accepted composition after explicit human PASS.

### 4.6 Shared-component lock

Freezes document-family title metadata, typography, footer/page number, table, quotation, code, figure and other shared components.

A later change unlocks only dependent layers. A copy correction does not authorise a new layout system. A page-break repair does not authorise text changes.

## 5. Human-feedback registry

Every annotation, direct rejection and accepted preference is retained with:

- immutable raw comment;
- source artifact/page/region/type;
- normalized intent;
- stable BlockID/component target;
- lifecycle state;
- supersession relation;
- verification method;
- current-candidate verdict.

Lifecycle:

```text
ACTIVE
SUPERSEDED
RETIRED
AUTHOR_ONLY
RESOLVED_BUT_GUARDED
CURRENT_ROUND_OPEN
```

A new version, page renumbering, build PASS or executor claim never closes feedback by itself.

## 6. Role division

### 6.1 ChatGPT / Planner / Research Author

Owns human-level judgment:

- read and reconcile sources;
- define audience, purpose and reader action;
- decide what belongs and what must remain outside;
- classify semantic zones and BlockIDs;
- write/freeze exact visible copy;
- decide page-count mode and legal flow/break rules;
- define visual-rhythm tokens and shared components;
- ingest feedback and manage locks;
- create the acceptance standard;
- prepare the autonomous Codex Controller Goal;
- review only independently filtered subtle deltas.

### 6.2 Codex Parent Controller

Owns autonomous orchestration inside one Goal:

- launch fresh Producer and fresh read-only validator/reviewer contexts;
- bind every round to exact artifact/authority identities;
- route ordinary findings to a fresh Producer repair;
- require a new fresh validator/reviewer after every source change;
- stop only for a genuine semantic decision, external human-only action or proven reviewer-runtime failure;
- expose only an independently accepted candidate/delta.

The user must not relay completion blocks between Producer and Reviewer.

### 6.3 Codex Producer

May:

- materialize approved copy;
- implement approved information architecture and visual grammar;
- build/render/export;
- generate bounded layout candidates from an approved finite parameter space;
- run non-authoritative smoke checks;
- create a proof-carrying patch manifest;
- repair independent findings within the frozen allowlist.

May not:

- decide what the reader should know;
- add/delete/paraphrase visible prose;
- create/delete/merge semantic jobs;
- change page-count mode;
- invent spacing values outside the approved set;
- remove difficult content to solve layout pressure;
- edit acceptance rules, validator thresholds or fixtures;
- declare final PASS.

### 6.4 Independent deterministic Validator

Runs after Producer stops, in a fresh read-only process/context.

Must:

- bind to exact repository, commit, artifact and authority hashes;
- use a version-pinned validator fixed before execution;
- treat candidate and authority as read-only;
- have no permission to change candidate, tests, thresholds or fixtures;
- check exact copy, values, formulas, links, allowlist, locks, protected paths, page count, PDF structure and historical guards;
- run accepted controls and known-bad negative controls;
- persist machine-readable evidence.

The same executor process is debugging evidence only, never authoritative validation.

### 6.5 Independent rendered-artifact Reviewer

Runs after deterministic validation passes.

Receives:

- final render;
- BlockIDs/page map;
- frozen copy/layout contract;
- relevant source anchors;
- review rubric.

Does not receive:

- executor completion prose;
- expected rejection answer key;
- permission to edit candidate or standards.

Judges:

- hierarchy and reading path;
- whitespace and vertical rhythm;
- semantic proximity;
- table/list/quote composition;
- audience effort;
- visual consistency;
- whether the document performs its reader job.

### 6.6 User

The user is the final subtle decision-maker, not routine QA.

The user should normally decide only:

- two genuinely acceptable alternatives;
- subtle tone or preference;
- whether a component/page/document is ready to lock;
- final subjective acceptance.

## 7. End-to-end workflow

### Stage 0 — Mode and source intake

1. classify mode;
2. bind exact source/authority and baseline artifacts;
3. separate source material from derived artifact content;
4. define success for the reader;
5. declare human-review budget.

Output: `DOCUMENT_BRIEF`.

### Stage 1 — Audience and source-to-reader map

Freeze:

```text
AUDIENCE
READER_TASK
INCLUDE
EXCLUDE
SOURCE_AUTHORITY
```

Classify each source unit:

```text
Source locator
Source role
Intended audience
Reader need
Disposition: INCLUDE / SUMMARIZE / MOVE_INTERNAL / EXCLUDE / USER_DECISION
Fidelity requirement
```

Output: `READER_AUTHORITY`.

### Stage 2 — Semantic block authority

Assign stable BlockIDs and freeze:

- semantic zone;
- semantic class;
- reader action;
- required/forbidden content;
- order and dependencies;
- keep-together and legal break rules.

Output: `BLOCK_AUTHORITY`.

### Stage 3 — Exact visible-copy authority

Freeze all reader-visible strings:

- titles, metadata and prose;
- equations and labels;
- lists and table cells;
- warnings/penalties;
- quotation and attribution;
- filenames, commands and links;
- captions and references.

No implementation begins while visible copy remains unresolved.

Output: `VISIBLE_COPY_AUTHORITY`.

### Stage 4 — Composition authority

Freeze:

- page-count mode and target;
- document-family typography and geometry;
- vertical-rhythm tokens;
- flow zones;
- legal/forbidden hard breaks;
- visual roles;
- table/list/quote grammar;
- density/readability floors;
- fallback when content does not fit.

Output: `COMPOSITION_AUTHORITY`.

### Stage 5 — Component proof pack

Before full production, prove high-risk shared components with real content:

- title/metadata block;
- body paragraph rhythm;
- list hierarchy;
- table and surrounding spacing;
- quotation + attribution;
- warning/penalty block;
- footer/page number;
- code/math/figure treatment where applicable.

Internal loop:

```text
Producer -> deterministic checks -> fresh rendered Reviewer -> repair -> fresh Reviewer
```

Accepted components are locked.

### Stage 6 — Representative/golden-page proof pack

Select the smallest representative set covering:

- densest page;
- sparsest page;
- every major semantic/composition archetype;
- every historical failure class;
- opening and closing;
- tables/lists/quotes/formulas/figures where applicable.

A full document must not be the first visual prototype.

### Stage 7 — Full candidate through one Controller Goal

1. Producer assembles candidate from frozen copy/components;
2. deterministic Validator runs on exact commit;
3. rendered Reviewer checks every page and sequence/contact sheet;
4. Parent routes ordinary findings to fresh Producer repair;
5. every source change receives a new fresh Validator and Reviewer;
6. only an independently accepted candidate reaches the user.

### Stage 8 — User review and immediate locking

User feedback becomes structured records.

- accepted blocks/pages/components lock immediately;
- unmentioned locked regions remain frozen;
- ambiguity returns to Planner, not renderer improvisation.

### Stage 9 — Bounded revision

Every round declares:

- exact baseline;
- allowed BlockIDs/components;
- semantic/copy/visual locks;
- addressed feedback IDs;
- dependency invalidations;
- change budget;
- open items before/after.

The user receives only changed pages/components plus minimal context.

### Stage 10 — Final whole-document regression

Check the exact delivery artifact:

- page order and document identity;
- all active historical guards;
- semantic/copy/information-architecture/visual/component locks;
- fonts, mathematical glyphs, tables, figures, quotations and links;
- PDF text/searchability and editable-source reproducibility;
- whole-document rhythm and adjacency;
- release package boundaries and hashes.

Delta review never replaces final full-document regression.

## 8. Proof-carrying patch manifest

Every Producer candidate records:

```text
candidate_id
parent_candidate_id
baseline_commit
validator_version
modified_block_ids[]
modified_component_ids[]
addressed_feedback_ids[]
unchanged_locked_block_ids[]
unchanged_locked_component_ids[]
visible_copy_changes[]
required_object_relocations[]
authorised_dependency_invalidations[]
open_items_before[]
open_items_after[]
```

Rules:

- modified IDs are a subset of the round allowlist;
- every source diff maps to an allowed BlockID/component;
- no visible string appears outside frozen copy authority;
- unchanged locks are proven by source/body/render identities;
- Producer supplies evidence but does not accept it.

## 9. Monotone convergence

Every accepted round satisfies:

```text
open_feedback_next is a strict subset of open_feedback_current
human_locked_blocks_next is a superset of human_locked_blocks_current
human_locked_components_next is a superset of human_locked_components_current
modified_ids are a subset of the explicit allowlist
unrelated_source_changes = 0
unrelated_render_changes = 0
new_P0_or_P1_regressions = 0
closed_guard_recurrences = 0
```

If issues do not decrease or accepted work reopens, do not generate another broad candidate. Diagnose authority, shared component, copy, composition or review-coverage failure.

## 10. Anti-shortcut rules

The workflow explicitly rejects:

- reading only the latest version/feedback;
- regenerating the whole document for a local repair;
- deleting content to solve layout pressure;
- adding plausible prose without approval;
- shrinking fonts/margins/leading outside authority;
- filling whitespace with decoration or filler copy;
- changing shared macros to repair one page without declaring all consumers;
- writing/tuning validators during candidate implementation;
- declaring semantic correctness from token presence;
- using executor self-review as acceptance;
- reviewing representative pages and emitting an unscoped global PASS.

## 11. Acceptance pipeline and states

Executor states:

```text
CANDIDATE_MATERIALIZED
READY_FOR_INDEPENDENT_VALIDATION
STOP_PLANNER_DECISION_REQUIRED
BLOCKED_DEPENDENCY
```

Validator states:

```text
PASS
FAIL
NOT_INDEPENDENTLY_VERIFIED
BLOCKED
```

Rendered Reviewer states:

```text
PASS
REVISE
NOT_INDEPENDENTLY_VERIFIED
BLOCKED
```

Only the acceptance aggregator, after required human decisions, may declare:

```text
READY_FOR_USER_REVIEW
USER_ACCEPTED
RELEASE_READY
RELEASED
```

Final acceptance is the conjunction of:

- deterministic validation PASS;
- rendered-artifact review PASS;
- no unresolved mandatory `NOT_INDEPENDENTLY_VERIFIED` gate;
- all previously locked blocks/components preserved;
- required user decisions PASS.

## 12. Human-review budget and escalation

Default for a bounded revision:

```text
HUMAN_REVIEW_BUDGET = one final acceptance review
```

The user must not receive obvious spacing, whitespace, copy, numbering, clipping or consistency defects.

If a closed guard returns:

1. reject candidate;
2. identify shared primitive/authority/review root cause;
3. repair root cause;
4. add persistent regression guard;
5. rerun from frozen candidate.

If the same guard recurs twice after claimed repair, stop project-local patching and repair the generic authoring/validator/reviewer layer.

A fifth broad human repair round triggers incident review rather than routine continuation.

## 13. User-facing review package

Each review contains only:

- artifact(s) needed for the current decision;
- changed/proof pages or full final candidate as appropriate;
- concise resolved-feedback summary;
- genuine remaining decisions;
- proof that unrelated locks remain unchanged.

Do not expose QA logs, fixtures, manifests, hashes or Controller chatter unless requested.

## 14. Acceptance-standard requirements

Before production, freeze an acceptance standard covering:

### Source/copy

- exact authority identity;
- exact visible copy and permitted deltas;
- numerical/formula/link parity;
- no executor-authored prose.

### Audience/information architecture

- reader task visible quickly;
- semantic zones correctly separated;
- no material belonging to another audience;
- required relationships remain proximate.

### Composition

- page-count mode;
- typography/geometry/rhythm tokens;
- legal flow and break rules;
- semantic-block integrity;
- density/readability floors;
- no page-count-driven compression.

### Regression

- allowlist-only source changes;
- locked source/body/render identities;
- shared-component consumer coverage;
- all active feedback guards;
- whole-document final review.

### Trust

- immutable pre-existing validator;
- fresh read-only deterministic validation;
- fresh blind rendered review;
- honest `NOT_INDEPENDENTLY_VERIFIED` state;
- user not first QA.

## 15. Immediate adoption

Projects should use this workflow before the generic Research Authoring plugin is complete.

Minimum immediate adoption:

- ChatGPT freezes audience/block/copy/composition authority;
- a Controller Goal runs Producer/Validator/Reviewer/repair loops internally;
- accepted elements become explicit locks;
- revisions use allowlists and proof-carrying patches;
- final release runs full-document regression.

## 16. First mandatory real experiment — STAT5060 HW1

The STAT5060 HW1 student PDF is the first mandatory recovery experiment.

Success requires:

- `FAILED_VERSION_RECOVERY` mode;
- exact V9 baseline and lineage;
- stable BlockIDs for identity/rules/Q1-Q5;
- cumulative feedback and rejection guards;
- exact visible-copy authority;
- component/golden-page proof for front matter and AI policy;
- one autonomous Controller Goal;
- immutable deterministic validator;
- fresh blind rendered review;
- Q1-Q5 and supporting-asset locks;
- one final user acceptance review;
- complete release-layer regression before HW1 closure.

The experiment fails if the user must again discover obvious spacing, whitespace, block-split, numbering or cross-reference defects.


## 17. Whole-sequence composition for short assessment handouts

The STAT5060 HW1 replay exposed a composition failure not captured by ordinary no-overflow checks: consecutive short questions were effectively assigned to fixed pages, producing visually underfilled pages even though the document had ample total content.

Generic lesson:

- optimize the full semantic sequence, not one page at a time;
- major questions are continuable unless explicitly frozen as atomic;
- page starts should follow legal semantic breakpoints, not a fixed “N questions per page” template;
- remove unnecessary hard breaks / stale keep-together guards before changing typography;
- a short final question should normally follow preceding content if semantic flow and orphan rules permit;
- do not fill white space with prose or decoration merely to make the page look occupied.

For a short Homework proof, the Planner should normally request one **natural-flow composition proof** before authorizing page-specific micro-adjustments.

Acceptance should ask:

```text
WHOLE_SEQUENCE_RHYTHM = PASS
QUESTION_FLOW_NOT_PAGE_PAIRING = PASS
PURPOSEFUL_WHITESPACE_ONLY = PASS
NO_FILLER_FOR_DENSITY = PASS
NO_UNNECESSARY_HARD_BREAKS = PASS
```

This is a rendered-review judgment. Page occupancy remains diagnostic rather than a universal hard threshold.
