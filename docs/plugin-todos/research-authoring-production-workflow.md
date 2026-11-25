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


## 18. Information-value-first opening-page composition

The STAT5060 HW1 natural-flow proof showed a useful second-order issue: whole-document pagination can improve substantially while the first page still feels visually light after unnecessary administrative prose has been removed.

The generic response must not be “add more text.”

For the opening page:

1. preserve the reader job and positive document-family baseline;
2. review whether existing context/deliverables are too compressed to scan;
3. recover only high-value source-backed context from earlier/source artifacts;
4. restructure submission/data information before inventing prose;
5. let assessed content flow naturally;
6. accept remaining purposeful whitespace.

A recovered historical sentence is eligible only when it still matches current authority and materially helps interpretation, navigation, action or error prevention.

For Homework briefs, useful opening context is often:

- a one-sentence shared data/story context;
- a causality/provenance fact that affects interpretation;
- a concise mapping from data files to questions;
- a clear two- or three-item submission list.

The workflow should reject both extremes:

- dense paragraph blocks that hide deliverables;
- decorative/filler prose added only to make Page 1 look fuller.

Acceptance:

```text
OPENING_PAGE_INFORMATION_DENSITY = APPROPRIATE
HIGH_VALUE_CONTEXT_ONLY = YES
SUBMISSION_BLOCK_SCANNABLE = YES
FILLER_FOR_WHITESPACE = NO
WHOLE_DOCUMENT_FLOW_PRESERVED = YES
```


## 19. Annotated baselines are positive copy baselines

A rendered artifact returned with instructor annotations should be interpreted as:

```text
accepted/unmarked visible copy
+ explicit strikeout removals
+ explicit highlight/comment changes
+ later direct decisions
```

unless the instructor explicitly says to rewrite the entire body.

The STAT5060 HW1 replay exposed the opposite failure: useful unmarked data-context explanation disappeared during a major revision even though the instructor had not marked it for removal.

Generic rule:

- major revision may reopen structure/assessment meaning where authorized;
- it does not erase the positive copy baseline;
- unmarked useful context is preserved by default;
- every deletion needs a disposition in the feedback/copy registry;
- simplification must be evidence-based, not deletion-by-omission.

This should be enforced before visible-copy freeze and again in the final semantic diff.

## 20. Build the artifact from the reader task, then choose the lightest form that carries the meaning

Research Authoring should not be governed by an expanding blacklist of bad-looking tokens. The content model is positive: start from the reader task and include only material that helps the reader understand the question, evaluate the evidence, interpret the conclusion correctly, or make the requested decision.

Everything else is supporting infrastructure. It may remain in source files, implementation notes, reproducibility records or QA evidence without becoming reader-facing copy.

### 20.1 Main narrative selection

For every candidate detail, ask what job it performs for the reader.

Keep it in the main narrative when it is needed to:

- state the scientific or technical question;
- explain a comparison, result or mechanism;
- preserve a condition, limitation or uncertainty that changes interpretation;
- support a decision or next action the reader is expected to make.

If it performs none of these jobs, omit it from the main narrative. Do not keep material merely because it is exact, available, traceable, difficult to compute, or useful to the implementation team.

Reproducibility is a separate reader task. When the artifact is explicitly meant to support reproduction, include the minimum exact implementation identities needed for reproduction in a dedicated section or companion artifact. Do not turn every research summary into a reproducibility handoff by default.

### 20.2 Form follows information shape

Choose the form that minimizes reader inference:

- prose for judgments, explanations, causal or logical relationships, uncertainty and decisions;
- tables for aligned comparisons across methods, conditions, groups or multiple numeric results;
- inline mathematics for compact relationships that are clearer symbolically than verbally;
- display mathematics only when a central, long, structured or multi-line relationship benefits from independent visual reading;
- code, commands, paths and machine tokens only when the reader must copy, execute, locate or verify that exact object;
- citations and references for source identity, not as a dump of internal evidence locations.

Do not elevate information into a table, equation, code block, appendix or separate section simply because that form is available.

### 20.3 Progressive disclosure

A substantial research artifact may have three layers:

1. the main reader narrative;
2. optional supporting detail needed by this reader for interpretation or reproduction;
3. internal implementation and QA evidence.

The second layer is not a dumping ground. Every appendix item must still have a reader job. Material with no reader job remains internal.

A good main narrative should remain understandable when implementation metadata, repository state, audit state and production history are hidden.

### 20.4 Scientific limitations stay; workflow limitations stay internal

Do not remove real scientific limitations in the name of readability. Keep boundaries such as dataset scope, extrapolation range, approximation error, missing uncertainty, incomplete external validation or unresolved alternative explanations when they constrain the claim.

By contrast, production state such as who ran a task, which branch contains it, whether a validator has passed, or which correction round produced it is normally not a scientific limitation. Use that information internally to establish authority, but do not substitute it for the scientific boundary.

### 20.5 Actual rendering is part of artifact acceptance

The target surface is part of the artifact definition. A Markdown, PDF, slide deck or document is not accepted merely because its source syntax is valid.

For GitHub-facing Markdown, use a GitHub-specific authoring profile rather than copying chat or TeX notation into the file:

- write ordinary explanation as normal paragraphs;
- use headings only for real sections, not every short thought;
- use bullets only for genuine parallel items or steps;
- use tables for aligned numeric or method comparisons;
- use fenced code only for real code, commands, configuration or literal machine text;
- keep short mathematical quantities and one-step relations inline when they remain readable;
- treat display equations as exceptional: use them only when the relationship is central, long, structured or multi-line enough to benefit from independent visual reading;
- never move a scalar, short parameter tuple, short asymptotic statement or numeric sequence into a display equation merely to emphasize it;
- do not assume chat-style or TeX-style delimiters will render correctly on GitHub; if mathematical rendering is needed, verify the exact syntax on the actual GitHub page;
- if a simple expression does not render reliably, prefer a directly readable Unicode/plain-text form over exposing raw markup.

Before delivery, inspect the actual reader-facing rendering and confirm that the chosen forms still perform their intended jobs: prose reads as prose, comparisons scan correctly, mathematics renders cleanly, tables remain legible, and no source or implementation syntax leaks into the reading experience.

If a representation fails on the target surface, reconsider whether that representation is needed before trying alternative syntax.

### 20.6 Regression checks are guards, not the writing model

Known failures should become automated or manual QA checks, but they should not expand into the primary authoring policy.

For example, scans for repository paths, workflow labels, raw math markup, audit tokens, stray code fences, isolated numeric paragraphs or unnecessary display equations are useful after those failures have occurred. They catch recurrence.

They do not answer the authoring question: what should the reader see?

The governing rule remains the reader-task test plus information-shape choice. A new form of irrelevant internal material must still be removed even if no existing regression check knows its token pattern.

### 20.7 Final reader test

Before surfacing a substantial artifact, answer these questions from the intended reader's perspective:

- Can the reader identify the question or decision quickly?
- Is the decisive evidence visible without reconstructing the implementation history?
- Are the necessary conditions and uncertainty attached to the claims they constrain?
- Does every visible section, table, formula, appendix item and technical token have a reader-facing job?
- If internal workflow and repository metadata are hidden, does the scientific or technical argument remain complete?
- Is any visible element present mainly because the author had access to it rather than because the reader needs it?

If the last answer is yes, the artifact is not ready for reader review.
## 21. Technical-explanation continuity for mathematically capable readers

Status: **TODO / promote into the Research Authoring reader model after regression review**

Evidence: repeated user-facing rewrites of the CAT-TRACE numerical-method notes on 2026-11-24--25. The mathematics was often correct, but the reader repeatedly had to ask what a method was for, how it connected to the previous method, what a new symbol meant, or why an implementation detail appeared before the statistical object was understood.

This section does not replace Section 20. It specializes the existing reader-task and information-shape rules for technical learning notes aimed at a mathematically capable reader who does not need elementary prerequisites re-taught, but does need every new conceptual bridge made explicit.

### 21.1 Explain the job before the machinery

Before introducing a new method, acronym, operator or family of symbols, state in ordinary prose what problem it solves in the current story.

Preferred order:

1. what object or computation is currently needed;
2. why the previous method or naive extension becomes insufficient;
3. what the new method changes operationally;
4. one concrete low-dimensional example when the mechanism is abstract;
5. only then the general notation or formula;
6. implementation constants and code details last.

Do not open an explanatory subsection with notation such as `Q_l`, `\Delta_l`, `Q_{\mathrm{high}}`, a Hessian, or a transformed coordinate unless the reader already knows the role of that object from the immediately preceding text.

### 21.2 Preserve causal bridges between neighboring methods

A sequence of individually correct method descriptions is still hard to read when the transition is missing.

When method B appears because method A hits a limitation, say so explicitly. The reader should be able to answer:

- what worked in the previous method;
- what new difficulty appeared;
- why that difficulty motivates the next method;
- what part of the previous construction is retained.

Example from CAT-TRACE:

- Gauss--Hermite works naturally for low-dimensional Gaussian expectations;
- tensor products require `K^d` node combinations;
- that growth motivates sparse-grid or RQMC alternatives at higher dimension.

Without this bridge, later methods look like an unrelated catalogue.

### 21.3 Expand unfamiliar names and reconnect them to known objects

On first substantive use, expand an acronym or specialist name when the expansion helps the reader place the method.

Do not merely write “AGHQ”. Write **Adaptive Gauss--Hermite Quadrature** once, then explain that it starts from ordinary Gauss--Hermite and relocates/rescales its nodes using the target's mode and local curvature.

Likewise, when a later method reuses an earlier object, reconnect it explicitly:

- the 7-point “Gauss” rule inside a 7/15 Gauss--Kronrod pair is the earlier Gauss--Legendre rule on the standard interval;
- Golub--Welsch is the computational route that produced those Gauss--Legendre nodes and weights;
- Kronrod augments that existing Gauss node set rather than introducing an unrelated quadrature family.

A new section should not force the reader to rediscover these identities.

### 21.4 Use a concrete mechanism example before abstract multidimensional notation

When the difficulty is combinatorial, geometric or hierarchical, a small example is part of the explanation, not optional decoration.

Example: before defining Smolyak increments `\Delta_l=Q_l-Q_{l-1}`, show a two-dimensional, three-level picture:

- each coordinate can use levels 1, 2 or 3;
- a full tensor rule includes combinations up to `(3,3)`;
- a sparse construction can first keep combinations such as `(1,1),(1,2),(2,1),(1,3),(2,2),(3,1)`;
- only after the reader sees what is being omitted should `Q_l`, `\Delta_l` and multi-index notation be introduced.

The example must run the same object through the whole mechanism. Do not substitute an unrelated analogy that creates a second thing to understand.

### 21.5 Translate symbols into actions immediately

A mathematical definition is incomplete as explanation when the reader still cannot say what the symbol does.

After introducing a symbol, give its operational meaning in the same paragraph when that meaning is not obvious.

Examples:

- `Q_l`: the integral approximation produced by the level-`l` one-dimensional rule;
- `\Delta_l=Q_l-Q_{l-1}`: the new integral contribution obtained by upgrading from level `l-1` to `l`;
- `Q_{\mathrm{high}}-Q_{\mathrm{low}}`: a local disagreement used as an error/refinement signal;
- `H=-\nabla^2 h(\hat\theta)`: local curvature that determines the width and correlation of the Gaussian approximation.

Do not leave a formula standing as a vocabulary definition when its role is the actual missing conceptual link.

### 21.6 Separate the mathematical story from implementation tuning

Reader-facing technical notes should first establish what is being integrated, approximated or optimized. Numerical constants, code paths and tuning settings come only after that object is clear.

CAT-TRACE regression case:

Bad sequence:
- finite interval constants;
- segment width;
- node count;
- `log_mass`;
- mixed Gauss--Legendre/Gauss--Hermite weights;
- only later the meaning of the integral.

Preferred sequence:
- continuous species intensity;
- probability of one occurrence history conditional on `(a,\beta)`;
- integrate their product over intercept `a`;
- explain why a finite numerical interval is introduced;
- explain why Gauss--Legendre fits that finite ordinary integral;
- put `[-12,14]`-style coverage constants, segment width, node count and code expressions in optional implementation detail.

This rule is an application of Section 20.3 progressive disclosure; the new requirement is to preserve the mathematical object before exposing the tuning.

### 21.7 Use asymptotic notation at the precision actually justified

Do not use a loose “approximately equal” sign when the omitted terms matter to the next derivation.

Distinguish:

- exact equality;
- asymptotic equivalence `\sim`;
- same leading logarithmic/exponential order;
- informal intuition.

CAT-TRACE regression case: from Mills' ratio, `\Phi(-z_p)\sim\phi(z_p)/z_p` and `q_p\sim\gamma/p`. It is acceptable to use these facts to obtain the leading scale `z_p\sim\sqrt{2\log p}`. It is not acceptable to write `e^{-z_p^2/2}\sim1/p` as a strict asymptotic equivalence, because the fixed `\gamma` and the `z_p` factor were dropped. Those factors are needed later to recover `A_p\to\gamma e^{-1/2}`.

When a coarse relation is used only for scale intuition, label it as such in prose.

### 21.8 Prefer affirmative explanation over repeated contrastive correction

Technical prose should normally state what an object is, what it does and why it is used.

Use “not X but Y” only when the reader is likely to hold the specific X misconception and the correction materially prevents an error. Repeated contrastive sentences create defensive prose and force the reader to track rejected alternatives.

Example: for Laplace, first state that it uses the posterior mode and local Hessian to form a Gaussian approximation and to approximate the corresponding marginal integral. Mention prior/posterior distinctions only where that distinction changes interpretation; do not repeat negative contrasts as filler.

### 21.9 Regression cases from the CAT-TRACE numerical-method notes

These cases should be retained as positive/negative authoring fixtures when the plugin gains explanatory-writing tests.

**Gauss--Kronrod**

Failure:
- opens with `Q_7,Q_{15}` without explaining that `Q` is a generic quadrature result;
- does not reconnect the 7-point Gauss rule to the previously learned Gauss--Legendre/Golub--Welsch construction;
- says “shared nodes” without showing what is shared.

Repair:
- identify the 7-point rule as Gauss--Legendre;
- state that Kronrod keeps those 7 nodes and adds 8 new ones;
- give a concrete standard-interval node example before returning to generic notation.

**Genz--Malik**

Failure:
- opens with a multidimensional integral and `Q_{\mathrm{high}},Q_{\mathrm{low}}`;
- the reader has not yet been told that the method is multidimensional adaptive integration.

Repair:
- first say that it is the multidimensional analogue of adaptive interval refinement;
- use a two-dimensional rectangle: evaluate two rules, compare them, then split the difficult region along the direction with stronger variation;
- introduce the high/low cubature notation afterward.

**Smolyak**

Failure:
- opens with `Q_l`, `\Delta_l` and multi-indices;
- “lower total level” has no concrete meaning yet.

Repair:
- start from the already-known `K^d` tensor-product explosion;
- use a two-dimensional three-level combination example;
- then define `Q_l` and `\Delta_l` as the level rule and its incremental contribution.

**AGHQ**

Failure:
- acronym appears unexplained;
- mode, Hessian and node mapping appear before the reader knows why ordinary Gauss--Hermite wastes nodes.

Repair:
- expand Adaptive Gauss--Hermite Quadrature;
- state the ordinary-rule mismatch first;
- explain “mode chooses center, curvature chooses width, then the Hermite nodes are moved/rescaled”;
- give the formula only after that story.

**Infinite TRACE intercept integration**

Failure:
- theoretical intensity, finite numerical truncation, node count, segment width and code-level log weights appear in the same layer.

Repair:
- first establish “species intensity × occurrence-history probability, integrated over intercept”;
- then explain finite numerical coverage and Gauss--Legendre;
- move tuning constants and code expressions to optional implementation detail.

**Laplace**

Failure:
- formula-first prose plus repeated English labels and repeated “not X but Y” corrections.

Repair:
- state the object, mode, curvature and resulting Gaussian approximation in natural prose;
- use the marginal-integral formula only where it adds new information;
- keep short relations inline and avoid display equations used only for emphasis, consistent with Section 20.2/20.5.

### 21.10 Reader-side acceptance check for technical explanations

Before surfacing a technical-learning section, ask:

- Can the intended reader say what the method is for before seeing its first nontrivial formula?
- Is the reason for moving from the previous method to this one explicit?
- Are unfamiliar acronyms and reused objects connected to what the reader already learned?
- If the mechanism is abstract, has one small concrete example run through the complete mechanism?
- Does each new symbol have an operational meaning, not only a definition?
- Are mathematical objects explained before code constants and implementation tuning?
- Are exact, asymptotic and heuristic relations distinguished at the precision needed downstream?
- Could the section still be understood if code paths, node counts, tolerances and repository details were hidden?
- Is contrastive correction used only where it prevents a real misconception?
- Are display equations reserved for relationships that genuinely benefit from independent visual reading?

If the reader repeatedly has to ask “what is this for?”, “is this the same object as before?”, “why did this method suddenly appear?”, or “can you give me one concrete example before the symbols?”, the section has failed even when every formula is mathematically correct.

