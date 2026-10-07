# Presentation End-to-End Pre-Execution Runbook

Status: **CANONICAL / MUST READ IN FULL BEFORE EVERY NON-TRIVIAL PRESENTATION TASK**  
Applies to: teaching, research, business, product, technical, decision, seminar, group-meeting, defense, and course presentations  
Mandatory companion contracts:

1. `pre-execution-cumulative-acceptance-contract.md`
2. `rendered-artifact-positive-ancestry-acceptance-contract.md`

This runbook is the complete operating procedure for presentation work.

It exists because repeated real-world failures showed that isolated rules are not enough. A deck can have correct page count, correct copy, correct formulas, a passing build, and even a prebuild Critic PASS while the rendered artifact is still visibly poor: tiny objects, half-empty pages, deleted diagrams, unreadable tables, broken visual ancestry, or a suspicious figure that was never validated against the underlying quantity.

The governing rule is:

> **Before any non-trivial presentation work begins, read this runbook in full, then read both companion contracts. Only then may planning, Critic review, production, revision, or release work start.**

No task-local prompt, domain skill, later workflow, or executor preference may weaken this runbook. Domain-specific skills may add requirements.

---

# 1. Core objective

The workflow must optimize four things simultaneously:

1. **content quality** — what is taught, claimed, or shown is correct, sufficient, audience-appropriate, and source-grounded;
2. **visual quality** — hierarchy, composition, object scale, whitespace, typography, navigation, evidence proximity, and rhythm are deliberate;
3. **historical fidelity** — accepted content, visual objects, and solved failure modes do not silently disappear or regress;
4. **revision efficiency** — obvious defects are solved internally and the user normally sees only two to four shrinking review deltas.

The user is never the first QA pass.

Infrastructure exists to support a good presentation. Once sufficient authority is frozen, the process must move to visible artifacts. Do not spend open-ended time extending governance while no useful render appears.

---

# 2. Mandatory pre-execution declaration

Before substantive work, the Planner or Controller must determine and record:

```text
RUNBOOK_READ = YES
CUMULATIVE_ACCEPTANCE_CONTRACT_READ = YES
RENDERED_ARTIFACT_CONTRACT_READ = YES
TASK_CLASSIFICATION =
CRITIC_REQUIRED =
INTERNAL_COMPONENT_PROOF_REQUIRED =
INTERNAL_HIGH_RISK_PAGE_PROOF_REQUIRED =
GPT_WORK_REQUIRED =
DELIVERABLE_FORMAT =
AUDIENCE =
PURPOSE =
EXACT_BASELINE =
SOURCE_SET =
HISTORY_SCOPE =
CURRENT_FREEZE_LEVEL =
ACTIVE_GLOBAL_GUARDS =
RENDER_PENDING_GUARDS =
LOCKED_PAGEIDS =
LOCKED_COMPONENTS =
POSITIVE_VISUAL_ANCESTRY_READY = YES | NO
IN_SCOPE_PAGEIDS =
IN_SCOPE_COMPONENTS =
ROUND_ALLOWLIST =
USER_IS_FIRST_QA = NO
```

If these cannot be determined, implementation does not start.

---

# 3. Task classification

## 3.1 NEW_SMALL

Use only when:

- the deck is small and low-risk;
- source and audience are clear;
- no complex history exists;
- no major scientific, statistical, pedagogical, or template decision is introduced;
- the visual system is already established or simple.

A separate prebuild Critic may be optional. Rendered review is still required.

## 3.2 NEW_MAJOR

Use when a new deck is substantial, high-stakes, teaching-heavy, scientific, template-defining, or likely to require non-trivial page-count, content-depth, or layout judgments.

A prebuild Critic is required before broad production.

## 3.3 MINOR_REVISION

A revision is minor only if **all** are true:

- page count unchanged;
- section order unchanged;
- no page-job changes;
- no scientific/statistical/pedagogical claim changes;
- no shell/header/footer/navigation/template redesign;
- no new archetype;
- no page split or merge;
- visible-copy changes are local and source-supported;
- scope is normally no more than about three pages and one already-defined shared component;
- no closed historical guard has recurred;
- no shared-root failure is suspected.

A separate prebuild Critic may be skipped. A bounded render review is still mandatory.

## 3.4 MAJOR_REVISION

Major when any of the following holds:

- page count, section order, narrative, or page jobs change;
- broad copy/content changes span multiple pages;
- shell/template/header/footer/navigation changes;
- a new layout archetype or major figure system is introduced;
- a page is split or merged;
- scientific/statistical/pedagogical/assessment meaning changes;
- repeated regression suggests the Planner authority is wrong;
- the user asks to rethink, rebuild, overhaul, or reread all history.

If uncertain, classify as major.

## 3.5 FAILED_VERSION_RECOVERY

Always major.

Required additions:

- authoritative version map;
- exact reviewer-seen historical renders;
- raw annotation recovery;
- lifecycle and supersession;
- positive visual ancestors;
- rejected/negative ancestors;
- explicit recovery decisions;
- prebuild Critic;
- mandatory internal component proof;
- mandatory internal high-risk-page proof;
- full rendered-artifact review before user delivery.

**A failed-version recovery may not skip internal proof merely because the user does not want to review intermediate artifacts.** The proof may remain internal, but it must exist and pass.

---

# 4. Role separation

## 4.1 ChatGPT Web / Planner / Presentation Author

Owns human-level judgment:

- source reading and reconciliation;
- audience, purpose, duration, format, and desired audience change;
- task classification and Critic routing;
- narrative, section sequence, and page count;
- stable PageIDs and one job per page;
- primary scientific/teaching/decision object;
- required and forbidden content;
- source anchors;
- audience vs speaker/instructor/internal boundary;
- exact visible copy;
- semantic relationship and layout archetype;
- historical-feedback interpretation, lifecycle, and supersession;
- positive and negative visual ancestry;
- locks and unlocks;
- Planner amendments;
- Critic prompt;
- autonomous Codex Controller Goal;
- deciding whether a finding is a specification defect or implementation defect.

ChatGPT Web must not be reduced to “write a prompt telling Codex to make it better.”

It does not own TeX/PPTX implementation, compilation, final rendering, or repository production mechanics.

## 4.2 Prebuild Specification Critic

Fresh, read-only, and independent.

It verifies the **specification before production**:

- actual source/history consumption;
- exact feedback counts;
- page count and sequence;
- every page job;
- content correctness and sufficiency;
- audience boundary;
- exact-copy completeness;
- layout/archetype suitability;
- positive/negative visual ancestry completeness;
- historical guard coverage;
- Controller review/repair plan.

It does **not** certify final visual quality because no final render exists yet.

Its allowed outcomes are:

- `PASS` — production may begin;
- `REVISE` — Planner authority only;
- `BLOCKED_HISTORY_NOT_CONSUMED` or source-equivalent block.

A major Planner amendment after Critic review requires a new fresh Critic.

## 4.3 Codex Parent Controller

Owns the autonomous production/review loop:

```text
fresh Producer
-> Producer self-QA
-> mandatory internal component/high-risk proof when applicable
-> fresh deterministic Auditor
-> fresh rendered-artifact Auditor
-> fresh Producer repair
-> new immutable candidate if bytes change
-> new fresh complete review
-> GPT Work final gate
-> repeat until independently accepted
```

The Parent:

- binds exact candidate, authority, history, and round scope;
- makes no new semantic decisions;
- does not ask the user to relay intermediate completion blocks;
- routes routine findings to fresh Producer contexts;
- stops only for a genuine Planner decision, human-only external action, or proven reviewer-runtime failure.

## 4.4 Codex Producer

Owns implementation only.

Allowed:

- typeset approved copy;
- implement approved archetypes;
- choose line breaks, widths, spacing, crop, and alignment within frozen bounds;
- use approved responsive fallbacks;
- regenerate approved figures from frozen data, labels, and semantics;
- build, render, export, and run code;
- prepare proof-carrying patch manifests;
- repair findings inside frozen scope.

Forbidden:

- decide what to teach, claim, omit, merge, split, or rewrite;
- add/delete/paraphrase visible copy;
- change page count or section order;
- invent a new archetype;
- shrink below approved typography floors;
- delete a difficult figure/diagram/table and replace it with prose unless Planner authority explicitly retires that object;
- change shared components without explicit unlock;
- edit gates or acceptance rules to make a candidate pass;
- declare final acceptance.

## 4.5 Fresh deterministic Auditor

Fresh, read-only, independent from Producer.

Checks objective conformance:

- exact copy, PageIDs, order, and count;
- allowlist and locks;
- complete history/guard coverage;
- required-object preservation;
- positive-visual-ancestor object preservation;
- component bindings and consumers;
- code execution and copyability;
- formulas, numerical results, mathematical glyphs, figure labels;
- PDF/PPTX structure and artifact identity;
- forbidden strings and roles;
- recurrence of deterministic historical failures.

## 4.6 Fresh rendered-artifact Auditor

Fresh, read-only, and bound to the exact candidate bytes.

Checks the actual page images, not only source or extracted text:

- page hierarchy and reading path;
- primary-object scale;
- typography at projection scale;
- whitespace and density;
- evidence-interpretation proximity;
- table/code/figure readability;
- Q/A geometry;
- shared-component optical consistency;
- positive visual ancestry;
- every render-dependent historical guard;
- suspicious charts, traces, or numerical visualizations against underlying variables and summaries;
- page rhythm and whole-deck rhythm.

For major/full-deck work it must inspect every page and the full contact sheet.

## 4.7 GPT Work

Final independent aesthetic, reader-effort, pedagogical, and communication gate.

For major/new/recovery candidates it reviews:

- all pages at whole-slide scale;
- full contact sheet;
- high-risk pages at high resolution;
- cumulative visual/pedagogical guards;
- positive visual ancestry and deleted-object regressions;
- whole-deck rhythm, density, and natural language;
- whether the audience can actually follow the page;
- whether whitespace feels intentional;
- whether evidence and interpretation remain visually connected.

GPT Work does not implement fixes and cannot override deterministic or statistical failures.

## 4.8 User

Owns only:

- genuine subjective preference between already acceptable options;
- new semantic/course/research decisions not determined by source;
- explicit page/component locks;
- final subjective acceptance.

The user is never routine QA.

---

# 5. Freeze ladder

Later stages cannot silently reopen earlier freezes.

## F0 — source/baseline/history freeze

Freeze:

- source set;
- exact reviewer-seen baseline;
- artifact/version identity;
- raw historical feedback;
- positive and negative baselines;
- current locks.

## F1 — narrative/page-job freeze

Freeze:

- section sequence;
- page count or bounded range;
- stable PageIDs;
- one job per PageID;
- primary object;
- required and forbidden objects;
- source anchors;
- transitions;
- audience vs speaker/instructor boundary.

## F2 — visible-copy freeze

Freeze every audience-visible string:

- title/subtitle;
- prose/bullets;
- equations and labels;
- Question/Answer;
- table cells;
- figure labels;
- code;
- captions/sources;
- administrative instructions.

## F3 — layout-semantics freeze

Freeze:

- semantic relationship;
- reading path;
- approved archetype;
- primary-object priority;
- typography floors;
- allowed fallback;
- forbidden fallback;
- shared-component bindings.

## F3V — positive visual ancestry freeze

For every non-trivial page/component, freeze:

```text
page_or_component_id
best_content_ancestor
best_visual_ancestor
negative_ancestors
mandatory_visual_objects
mandatory_relationships
minimum_scale_or_readability_expectation
preserve_geometry_or_composition_features
allowed_changes
forbidden_deletions_or_substitutions
retirement_authority_if_any
```

A visual object that previously worked is not merely “reference material.” It is a protected asset until explicitly retired.

## F4 — shared-component proof freeze

Using real deck content, prove and lock:

- title shell;
- header/navigation;
- footer/source/buttons/page number;
- typography;
- Question/Answer grammar;
- table/code/caption/figure grammar;
- closing shell.

## F5 — internal high-risk-page composition freeze

Internally prove representative high-risk pages covering:

- opening and closing;
- dense and sparse layouts;
- every major archetype;
- figures, tables, formulas, code, and Q/A;
- historically recurrent failures;
- pages with positive visual ancestors that must be preserved.

The user need not review this proof. The proof still must exist and pass.

## F6 — full-candidate freeze

Freeze exact:

- source commit;
- PDF/PPTX;
- per-page renders;
- hashes;
- page map;
- history-to-render closure matrix;
- review bundle.

## F7 — human locks

Explicit user acceptance creates immutable page/component locks until a named unlock states reason and scope.

---

# 6. How historical feedback is actually consumed

“History consumed” means more than counting rows.

Every raw human annotation must pass through this chain:

```text
raw annotation
-> exact historical artifact/page
-> stable PageID/component
-> normalized requirement
-> semantic / copy / visual / component / process classification
-> lifecycle and supersession
-> positive ancestor and negative example where applicable
-> Planner field that encodes the requirement
-> responsible verification layer
-> exact evidence required for closure
-> current resolution state
```

The mandatory row schema is:

```text
feedback_id
historical_artifact
historical_physical_page
historical_feedback_text
historical_type_or_batch_type
stable_page_id
current_physical_page
component_id_if_any
requirement_class
normalized_requirement
positive_visual_ancestor_if_any
negative_ancestor_if_any
planner_authority_locator
verification_owner
required_evidence
resolution_state
resolution_reason
```

Allowed states:

- `UNRESOLVED`
- `PARTIAL`
- `RESOLVED_IN_SPEC`
- `RENDER_PENDING`
- `RESOLVED_IN_RENDER`
- `RETIRED_BY_PAGE_CHANGE`
- `SUPERSEDED`
- `ROUTED_INSTRUCTOR_ONLY` / audience-equivalent
- `SOURCE_GAP_UNVERIFIABLE`

Rules:

1. `RENDER_PENDING` remains open.
2. A visual guard can become `RESOLVED_IN_RENDER` only after the exact candidate image is inspected.
3. A page deletion/merge does not erase history.
4. A visual object cannot be deleted merely because it is difficult to implement.
5. A later version inherits every active or resolved-but-guarded requirement.
6. Every major Critic and every final render review updates the same cumulative ledger.
7. Final release is blocked while mandatory visual items remain `RENDER_PENDING`.

For each production candidate, generate two matrices:

### 6.1 History-to-authority matrix

Proves every human item is represented by current Planner authority.

### 6.2 History-to-render closure matrix

Proves every render-dependent item was checked against the exact page image and records:

```text
feedback_id
candidate_id
page_id
page_png_sha256
render_evidence_locator
verdict
reviewer
review_date
```

A report saying “all history consumed” without these mappings is insufficient.

---

# 7. Positive and negative ancestry

## 7.1 Positive ancestry

For each page, identify the best prior content and visual ancestors independently.

Examples of protected positive assets include:

- a useful teaching diagram;
- a readable prior table;
- a strong figure-plus-interpretation composition;
- code output placed beside the correct code block;
- an accepted title/closing shell;
- an aligned Q/A pattern.

The Producer may improve them, but cannot silently remove them.

## 7.2 Negative ancestry

Rejected versions remain regression fixtures. Their failure modes must be named and replayed against each new candidate.

## 7.3 No deletion-as-repair

If historical feedback says “repair the diagram,” deleting the diagram and replacing it with prose is not compliance.

Deletion requires explicit Planner retirement authority stating:

- why the object no longer serves the page job;
- what replaces its teaching function;
- why the old failure cannot recur;
- which historical guards are retired or remapped.

---

# 8. Page planning

Every page must have:

- one primary job;
- one primary audience action;
- one primary object or object group;
- explicit required objects;
- explicit forbidden objects;
- source anchor;
- transition in/out;
- audience boundary;
- semantic relationship;
- approved archetype;
- typography floor;
- positive visual ancestor or explicit “new composition” authority;
- render-level acceptance tests.

Pages are split or merged for semantic reasons, never merely to fit content.

---

# 9. Layout grammar

## 9.1 Columns are for true peers

Appropriate examples:

- R vs Python;
- before vs after;
- model A vs model B;
- two independent evidence panels;
- stable figure + adjacent interpretation.

Conditions:

- either side can be understood without finishing the other first;
- both remain readable at slide scale;
- headings/formulas share anchors;
- the primary object is not shrunk for symmetry;
- interpretation stays next to its evidence.

## 9.2 Sequential logic stays vertical

Vertical flow is default for:

- derivations;
- algorithms;
- mechanism chains;
- Question -> evidence -> Answer;
- count -> exposure -> rate;
- any page where the right region depends on the left.

Test:

> If the audience must finish the left region before the right region makes sense, the relationship is sequential and should normally be vertical.

## 9.3 Codex freedom

Codex may adjust widths, spacing, line breaks, crop, and alignment within the approved archetype.

Codex may not change archetype, shrink below typography floors, delete content, split/merge pages, or replace visual explanation with generic cards/prose.

---

# 10. Whitespace and density

Whitespace is judged **after content sufficiency**.

Accept when:

- page job is complete;
- primary object is already large/readable;
- reading path is clear;
- space supports grouping or deliberate restraint.

Fail when large unused space coexists with:

- undersized figures, tables, formulas, or code;
- missing explanation;
- result pushed far from evidence;
- tiny text;
- a lower void caused by columns;
- deleted/compressed content;
- an unfinished-looking composition.

Do not fill space with slogans, decorative cards, generic arrows, repeated labels, filler captions, or generic takeaway boxes.

Use space first to improve:

- primary-object scale;
- typography;
- evidence-interpretation proximity;
- grouping;
- needed explanation.

### 10.1 Objective warning rule

Automated geometry is a warning, not the sole aesthetic judge. However, the following combination is a hard review trigger:

```text
large unused body region
+ primary object below its page-specific scale floor
or
+ text below approved typography floor
```

A reviewer must explain why the whitespace is intentional or fail the page.

---

# 11. Shared components

Shared components must be centralized and independently reviewable:

- title shell;
- header/navigation;
- footer/source/buttons/page number;
- typography;
- Question;
- Answer;
- table;
- code;
- caption;
- figure/diagram treatment;
- closing shell.

If a shared component changes:

- unlock only that component;
- automatically revalidate every consumer page;
- do not reopen semantic/copy locks on those pages;
- rerender and review all affected consumers.

---

# 12. Question/Answer grammar

- Question and Answer are paired semantic components.
- Both use the intended aligned accent rule.
- One continuous answer uses one continuous rule.
- Sequential Q -> evidence -> A stays vertical.
- A key conclusion must not fall outside the Answer block.
- Q/A must not become arbitrary cards.

---

# 13. Figure, chart, caption, and numerical validation

A figure is not decoration.

Rules:

- it must encode data, mechanism, model, uncertainty, or evidence;
- mathematical variables use actual mathematical glyphs;
- captions are captions, not hidden paragraphs;
- interpretation stays adjacent to evidence;
- primary figures are not shrunk while large empty regions remain;
- paper/export figures may be regenerated for slide scale;
- suspicious traces, posterior plots, diagnostic values, axes, legends, and labels must be checked against the exact underlying variable and numerical summaries.

A chart can fail even if it renders cleanly. The Auditor must confirm that the plotted quantity, scale, filtering stage, and label agree with the source data and surrounding claims.

---

# 14. Code-page rules

- code must be copyable;
- shown code is actually run;
- visible output stays near the code that produces it;
- code syntax is subordinate to the scientific/statistical job;
- package/API inventory is not the teaching purpose unless explicitly authorized;
- peer code blocks use aligned roles and readable scale;
- one short column may not create a large lower void while another is dense;
- no curly quotes or broken text extraction.

---

# 15. Prebuild Critic workflow

Required for major/recovery and major new decks.

The Critic must:

1. prove source/history consumption;
2. independently evaluate page count and sequence;
3. review every planned PageID;
4. check content correctness and sufficiency;
5. check audience boundary;
6. check visible-copy completeness;
7. check layout/archetype suitability;
8. check positive and negative visual ancestry;
9. list relevant historical guards;
10. audit the Controller;
11. update the cumulative historical ledger item by item.

A prebuild Critic PASS means only:

> the specification is coherent enough to produce.

It does **not** mean:

> the future rendered deck is visually accepted.

---

# 16. Mandatory internal proof before broad production

## 16.1 Component proof

Required for:

- new or materially changed visual systems;
- failed-version recovery;
- shell/component redesign;
- repeated component regression.

Use real deck content, not placeholder text.

## 16.2 High-risk-page proof

Required internally for failed-version recovery and substantial major revision.

Select pages covering:

- every major archetype;
- opening and closing;
- dense and sparse pages;
- figures, tables, code, formulas, and Q/A;
- historical recurrent failures;
- pages whose positive visual ancestors must be preserved;
- pages with numerical figures requiring validation.

## 16.3 User boundary

The user does not have to review these proofs. The internal Controller must complete them.

The following shortcut is forbidden:

```text
user does not want an intermediate proof
-> skip proof
-> generate full deck immediately
```

The correct route is:

```text
internal proof
-> internal review/repair
-> full deck
-> final review
-> user sees only the accepted candidate
```

---

# 17. Full-candidate production

```text
Producer builds exact candidate
-> Producer self-QA
-> deterministic Auditor
-> rendered-artifact Auditor over all pages
-> repair all P0/P1/P2
-> new immutable candidate if bytes change
-> fresh full re-review
-> GPT Work final gate
```

The user does not receive intermediate defects.

---

# 18. Producer self-QA

Before independent review, Producer must remove obvious defects:

- clean build;
- exact page count/order/copy;
- required objects present;
- positive-ancestor mandatory objects preserved;
- forbidden strings/roles absent;
- code and numerical outputs verified;
- formulas/labels correct;
- no clipping/overlap;
- no page-local font shrinking;
- shell/components render;
- page images/contact sheet exist;
- obvious whitespace/tiny-object problems fixed;
- bad columns, footer/header, Q/A, caption, and crop issues fixed;
- patch manifest matches actual changes.

Producer self-QA cannot issue final PASS.

---

# 19. Deterministic Auditor

For every candidate, verify:

- source/commit/artifact identity;
- copy/PageID/order/count;
- allowlist and locks;
- history bundle coverage;
- positive visual object preservation;
- code execution/copyability;
- mathematical and numerical fidelity;
- component consumer regression;
- no unauthorized object deletion;
- no stale or fake review evidence.

A source change after audit creates a new candidate identity.

---

# 20. Rendered-artifact Auditor

For major/full-deck work, review every page and the contact sheet.

Per page record:

```text
page_id
physical_page
page_png_sha256
active_historical_guards
positive_visual_ancestor
mandatory_visual_objects
preserved_or_missing_objects
page_job
primary_object
copy_fidelity
component_fidelity
reading_path
object_scale
typography
whitespace
semantic_proximity
numerical_visual_validation
audience_boundary
observed_issue_or_pass_reason
verdict
```

The Auditor must also update every `RENDER_PENDING` historical row against the exact candidate image.

Global PASS is forbidden unless:

- every page has a row;
- every mandatory render-dependent guard has a verdict;
- all page image hashes bind to the reviewed candidate;
- no required visual object was silently deleted;
- no unexplained suspicious numerical figure remains;
- P0=P1=P2=0.

---

# 21. GPT Work gate

For major/recovery decks, GPT Work reviews all pages and the full contact sheet.

It judges:

- true projection-scale readability;
- hierarchy and audience effort;
- whitespace and density;
- positive visual ancestry;
- natural language;
- evidence proximity;
- deck rhythm;
- whether a page feels complete rather than technically populated.

If GPT Work finds a defect that should have been caught earlier, two actions are required:

1. repair the candidate;
2. strengthen the upstream guard/reviewer so the failure becomes a permanent regression test.

---

# 22. User review

The user receives:

- the internally accepted candidate or bounded delta;
- resolved feedback IDs;
- before/after where useful;
- genuine remaining subjective choices;
- proof unrelated locks remained unchanged.

The user does not receive routine defect lists, build logs, reviewer relay tasks, or obviously unfinished pages.

---

# 23. Bounded revision

Every revision round freezes:

- exact baseline;
- allowlisted PageIDs/components;
- addressed feedback IDs;
- locks;
- round-frozen scope;
- component consumers;
- explicit unlocks;
- change budget;
- positive visual ancestor expectations.

Producer supplies:

```text
candidate_id
parent_candidate_id
baseline_commit
modified_page_ids
modified_component_ids
addressed_feedback_ids
unchanged_locked_page_ids
unchanged_locked_component_ids
preserved_positive_visual_objects
retired_visual_objects_with_authority
required_object_relocations
visible_copy_changes
dependency_invalidations
open_items_before
open_items_after
```

Out-of-allowlist changes fail.

---

# 24. Monotone convergence

Each accepted round must satisfy:

```text
open_feedback_next is a strict subset of open_feedback_current
human_locked_pages_next is a superset of human_locked_pages_current
human_locked_components_next is a superset of human_locked_components_current
modified_ids are a subset of explicit_allowlist
unrelated_source_changes = 0
unrelated_render_changes = 0
closed_guard_recurrences = 0
positive_visual_object_losses = 0
```

Normal user review target: two to four rounds.

If open issues do not decrease or accepted work reopens, stop broad generation and diagnose the authority, copy, archetype, component, positive ancestry, or reviewer-coverage root cause.

---

# 25. Failure escalation

## Planner/specification failure

Return to Planner; amend F1/F2/F3/F3V; fresh Critic if major.

## Producer implementation failure

Fresh Producer repair -> fresh deterministic/rendered review.

## Shared-component failure

Unlock named component only -> repair root primitive -> revalidate all consumers.

## Positive-ancestry failure

Restore or explicitly re-authorize the protected visual object. Do not accept a prose substitution as repair.

## Review-coverage failure

Add a permanent guard, strengthen the responsible layer, and replay the rejected artifact.

## Self-certification/control-plane failure

Stop project-local patching and repair/version the generic validator/reviewer runtime.

---

# 26. Severe rendered-deck failure rule

A candidate is a severe workflow failure when several of the following occur together:

- technically correct content but widespread tiny-object / large-void composition;
- historically protected diagrams or visual structures disappear;
- multiple `RENDER_PENDING` guards remain visibly violated;
- suspicious numerical plots are not validated;
- all-page review is claimed without page-level evidence;
- GPT Work PASS is absent, scoped incorrectly, or not bound to the exact artifact;
- the user is the first person to identify obvious full-deck visual problems.

Consequence:

```text
CANDIDATE = HUMAN_REJECTED
MINOR_PATCH = FORBIDDEN
RETURN_TO = HISTORY + POSITIVE_VISUAL_ANCESTRY + RENDER_ACCEPTANCE_REPAIR
```

Do not continue page-local polishing on top of an invalid visual system.

---

# 27. Final full-deck regression

Before release, review the exact delivery artifact for:

- all pages/order;
- all active and resolved-but-guarded historical requirements;
- semantic/copy/layout/component/positive-visual locks;
- header/footer/navigation/bookmarks;
- typography;
- formulas and numerical figures;
- figures/tables/code;
- code copyability;
- PDF/PPTX text quality;
- whitespace and object scale;
- semantic proximity;
- deck rhythm;
- source fidelity;
- artifact identity and reproducibility.

Delta review never replaces final full-deck regression.

---

# 28. Completion rule

A presentation is complete only when all applicable layers agree:

- runbook read;
- cumulative acceptance contract read;
- rendered-artifact contract read;
- required prebuild Critic PASS;
- Planner freezes intact;
- internal component/high-risk proof PASS;
- Producer self-QA complete;
- fresh deterministic Auditor PASS;
- fresh rendered-artifact Auditor PASS;
- all `RENDER_PENDING` guards closed on the exact render;
- GPT Work PASS where required;
- positive visual ancestry preserved or explicitly retired;
- prior locks preserved;
- final full-deck regression PASS;
- artifact identity/reproducibility PASS;
- user final subjective acceptance when required.

A file existing, compiling, or looking acceptable on representative pages is never sufficient.

---

# 29. Mandatory read order

Before every non-trivial presentation task, read in this order:

1. `presentation-end-to-end-pre-execution-runbook.md`;
2. `pre-execution-cumulative-acceptance-contract.md`;
3. `rendered-artifact-positive-ancestry-acceptance-contract.md`;
4. `authoring-production-workflow.md`;
5. `chatgpt-web-authoring-contract.md` when ChatGPT Web is planning;
6. `anti-shortcut-production-contract.md`;
7. `independent-review-contract.md`;
8. domain skill / project-specific authority;
9. task-local source, baseline, history, ancestry, and locks.

Do not begin execution until steps 1–3 are complete.