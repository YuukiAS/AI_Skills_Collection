# Presentations TODO — Cumulative Human Feedback, Teaching Sufficiency, and Authoring Authority

Date: 2026-10-06  
Status: ACTIVE TODO / PLANNER INPUT  
Primary evidence source: `YuukiAS/STAT5060-TA` Tutorial 01 revision history, 2026-09-29 through 2026-10-06

This TODO exists because repeated presentation revisions achieved mechanical/evidence PASS while still violating earlier human feedback. The generic problem is not STAT5060-specific: an existing deck can accumulate dozens of human decisions across versions, and a revision system that only reads the latest candidate will repeatedly regress.

The source project now maintains a cumulative human-feedback registry with 193 recovered student-deck feedback objects plus separate instructor-learning annotations. That registry is evidence for the generic requirements below; exact STAT5060 page numbers, statistics, course policy, and model-specific wording must not become plugin runtime special cases.

## P0 — Existing-deck revision must have cumulative human-feedback memory

Problem:
- Historical human feedback is currently easy to lose when page numbers change, a new frozen spec is written, or a later executor/reviewer reports PASS.
- A deck can therefore reintroduce a previously rejected pattern under a different page number or wording.

Required generic behavior:
- Existing-deck revision must discover and load every available human rejection/annotation ledger for the artifact family, not only the immediately previous version.
- Store feedback with stable semantic IDs, source artifact/version, page at time of feedback, colour/type, original comment, normalized intent, and closure state.
- Page number is historical evidence, not the identity of the feedback item.
- Human feedback remains active until explicitly retired with a reason.
- A new candidate must produce a regression matrix: `feedback_id -> semantic guard -> current-page evidence -> ABSENT/PRESENT/NOT_APPLICABLE`.

Promotion gate:
- Replay a deck in which a rejected pattern returns on a different page number. The cumulative guard must catch it even when changed-page review does not.

## P0 — Feedback history must encode supersession, not just accumulate rows

Problem:
- A cumulative ledger can still fail if it stores contradictory historical comments without deciding which instruction is currently effective.
- A later human decision may refine or reject the geometry implied by an earlier comment. Literal accumulation can therefore recreate an old failure while claiming “history was preserved.”

Required generic behavior:
- Every feedback item has lifecycle state: `ACTIVE / SUPERSEDED / RETIRED / INSTRUCTOR_ONLY / RESOLVED_BUT_GUARDED`.
- When a newer human comment conflicts with or refines an older item, record an explicit `supersedes_feedback_id` / `superseded_by_feedback_id` chain.
- Preserve the original comment verbatim; never delete it.
- Candidate planning consumes the **effective active decision set**, not a flat bag of all historical comments.
- Reviewer reports both historical provenance and the currently effective rule.
- If conflict cannot be resolved from human evidence, stop for Planner/human decision; executor must not choose.

Promotion gate:
- Replay a real sequence where an earlier styling request is later rejected/refined. The planner must apply the latest effective rule while preserving the earlier record for provenance.

## P0 — Page PASS requires demonstrated consumption of relevant historical feedback

Problem:
- Merely attaching a master ledger to the review package does not prove the reviewer used it.
- A reviewer can still mark a page PASS while overlooking an earlier human complaint that is visibly present again.

Required generic behavior:
- Before a page can PASS, the reviewer must list the active historical guard IDs relevant to that page/semantic role.
- The page row must state concrete current evidence for each applicable guard.
- `PASS` with an empty/irrelevant guard set is invalid when historical feedback exists for that page role.
- The review system must distinguish:
  - `HISTORY_LOADED=YES`
  - `RELEVANT_GUARDS_RESOLVED=YES`
  These are not the same condition.
- A known historical failure fixture reappearing in final pixels automatically forces REVISE even if the current frozen spec accidentally permits it.

Promotion gate:
- Historical replay where the ledger is present but the reviewer ignores one relevant guard must fail review-spec validation.

## P0 — Human rejection overrides executor/reviewer/evidence PASS

Problem:
- Automated evidence integrity and independent review can be technically correct about files while the audience artifact is still human-rejected.
- Repeated STAT5060 rounds demonstrated that a clean evidence packet cannot override teaching/readability failure.

Required generic behavior:
- Human `REJECTED` is a higher-priority artifact state than executor PASS, independent-review PASS, evidence PASS, or hash closure.
- Once human rejection occurs, prior PASS artifacts remain historical evidence only.
- Any audience-visible byte change after rejection creates the next artifact version; do not continue evidence-only closure on a human-rejected artifact.

Promotion gate:
- Inject a human rejection after an evidence PASS and verify the workflow routes to a new content version rather than another release-evidence loop.

## P0 — Authoring authority lock: executors must not invent audience-facing prose

Problem:
- Layout/execution agents frequently fill whitespace, repair overflow, add transitions, add captions, or explain code by inventing new visible sentences.
- In a teaching deck this silently changes pedagogy.

Required generic behavior:
- Support an `EXACT_COPY_LOCK` mode.
- When active, every audience-visible string must trace to an approved copy registry.
- Executor-allowed changes: escaping, line wrapping, font/layout binding, source-path substitution, and explicitly approved symbol-equivalent TeX.
- Executor-forbidden changes: adding/deleting sentences, paraphrasing, inserting transitions, captions, warnings, prerequisites, API explanations, package caveats, labels, or filler.
- If approved text does not fit, executor must fail with page/object diagnostics. It must not solve fit by authoring.
- Reviewer must compare rendered visible text to the approved registry, not only source-file diffs.

Promotion gate:
- A fixture with deliberately insufficient space must STOP rather than invent a shorter sentence or delete a line.

## P0 — Teaching decks need a pedagogical-sufficiency gate before visual/evidence closure

Problem:
- A slide can have correct formulas, no overflow, good hashes, and still fail because the audience is never told why the method is needed or how to interpret it.
- The failure is especially common on first-introduction slides.

Required generic behavior for a first introduction of a substantive method:
- Verify the page/mini-sequence answers, as appropriate:
  1. what problem/data structure motivates the method;
  2. what changes in the model or estimand;
  3. what the central parameter/device means;
  4. how to interpret the displayed result;
  5. what assumption/failure mode matters at the current course level.
- These are semantic checks, not mandatory section labels.
- Do not accept a formula/result page merely because later slides eventually supply the missing intuition.

Promotion gate:
- Historical replay where formula + estimate is mechanically clean but under-explained must fail; a repaired mini-sequence must pass.

## P0 — Whitespace is conditional teaching budget, not an unconditional cleanliness metric

Problem:
- Two opposite failure modes recur:
  - fill empty space with slogans/meta prose;
  - protect large empty regions even though the core concept is under-explained or the primary scientific object is too small.

Required generic behavior:
- Evaluate whitespace only after pedagogical sufficiency.
- If the concept is complete and visual hierarchy is strong, intentional whitespace is allowed.
- If natural audience questions remain unanswered, large unused space is a signal to improve teaching content, scientific-object scale, or example structure.
- Never satisfy occupancy by pushing a conclusion away from its evidence.
- Never fill space with provenance, QA language, prerequisites, package notes, decorative diagrams, or generic takeaways.

Promotion gate:
- One sparse-but-complete slide passes.
- One under-explained slide with similar whitespace fails.
- One artificially filled slide also fails.

## P0 — Student-facing software-plumbing firewall

Problem:
- Code/reference pages tend to accumulate object dependencies, `Prerequisite:` lines, backend caveats, API parameterization differences, file names, implementation provenance, and validation language.
- These details displace statistical teaching even when technically true.

Required generic behavior:
- Classify visible technical text as one of:
  - core statistical interpretation;
  - runnable code needed for the learning objective;
  - reference-only implementation detail;
  - instructor/developer provenance.
- Reference-only details default to speaker notes, companion notebook, appendix, or instructor material.
- Student body must not contain dependency narration such as `Prerequisite: object from P03` unless dependency itself is the learning target.
- Package/API differences appear visibly only when they change statistical meaning or prevent correct interpretation.
- The deck-wide code-page ratio and code-area share should trigger reviewer inspection when code/reference content begins to dominate teaching content; no fixed universal percentage is proposed yet.

Promotion gate:
- Replay a teaching deck in which package/API prose is removed from visible body while statistical meaning remains complete and copyable reference code remains available elsewhere.

## P0 — Every visible prose object must have a semantic role

Problem:
- Explanatory sentences are often placed below code/figures as visually orphaned prose: neither clear body text, caption, note, Question/Answer, nor source.

Required generic behavior:
- Every visible text object must declare one role:
  - title/subtitle;
  - body teaching prose;
  - bullet/list item;
  - Question;
  - Answer;
  - figure/table caption;
  - annotation/callout;
  - source/credit;
  - code/output;
  - administrative instruction.
- Layout and typography are role-driven.
- Orphan prose without a role is a review failure.
- Caption text must describe the scientific object; body interpretation must not masquerade as a tiny caption.
- Source/provenance must not carry teaching conclusions.

Promotion gate:
- Historical orphan-prose fixtures fail; repaired body/caption/note versions pass.

## P0 — Question and Answer must be a paired semantic grammar

Problem:
- Question blocks can receive a deliberate accent rule while answers are left as ordinary prose, producing inconsistent reading roles.

Required generic behavior:
- Shared `Question` and `Answer` primitives with matched rule geometry, label hierarchy, line spacing, and natural ragged-right text.
- The answer role must not be simulated by bolding the word “Answer” inside ordinary body text.
- The same primitives must work for one-line and multi-line content without full-justification rivers or rule overshoot.

Promotion gate:
- One-line and multi-line Q/A fixtures pass; mismatched answer styling and rule overshoot fail.

## P0 — Review order for teaching presentations must prioritize audience quality

Required order:
1. cumulative human-feedback regression;
2. pedagogical/content sufficiency;
3. whole-slide reading path and scientific-object scale;
4. natural audience language and visible-text roles;
5. template/geometry regression;
6. code copyability/reproducibility;
7. release/evidence identity closure.

Rules:
- Failure in stages 1–4 blocks spending review effort on release-evidence closure except minimal diagnostics.
- Evidence completeness cannot upgrade a failed audience artifact.
- Final human acceptance always occurs after these gates.

Promotion gate:
- Workflow refuses to enter evidence-closure mode while a human/pedagogical guard is open.

## P0 — Acceptance standards are cumulative, not substitutive

Problem:
- A later review standard can accidentally “simplify” the process and drop hardening that was added because of an earlier false PASS.
- This is itself a regression. A new pedagogical gate must not silently remove artifact binding, whole-slide review, role separation, first-use checks, template regression, figure provenance, or other already-proven gates.

Required generic behavior:
- Every new/revised acceptance contract must declare its parent review standards and produce a carry-forward matrix:
  `prior_gate -> current_gate -> PRESERVED / STRENGTHENED / EXPLICITLY_RETIRED_WITH_REASON`.
- Missing prior gates are automatic review-spec failure.
- A gate may be retired only by an explicit Planner/human decision with rationale and replacement coverage; silence is not retirement.
- New requirements are additive unless they explicitly supersede an older requirement.
- Historical known-failure fixtures remain part of regression testing after new gates are added.

Minimum carry-forward set for mature presentation review:
- exact artifact/commit/hash binding;
- all-page whole-slide review before zoomed diagnostics;
- contact-sheet/deck-rhythm review;
- role-separated independent review where enabled;
- reviewer calibration / known-failure replay where enabled;
- concrete page-level PASS/REVISE observations;
- template/header/footer/navigation behavior;
- projection readability and typography;
- figure/source provenance;
- first-use/narrative-order checks across all visible text layers;
- natural audience language;
- assessment/instructor-vs-audience boundary;
- cumulative human-feedback regression;
- pedagogical sufficiency;
- exact-copy compliance when locked;
- code copyability/reproducibility;
- evidence identity only after audience-facing gates;
- final human authority.

Promotion gate:
- Start from a previously hardened review contract, add one new gate, and verify that the generated successor contract still contains every unretired predecessor gate. A deliberately omitted predecessor gate must fail spec validation.

## P0 — Review-role isolation and calibration must survive later workflow upgrades

Problem:
- Past false PASS events required two independent reviewer roles, verdict isolation, and blind known-failure calibration. A later “single comprehensive review” can lose that protection while appearing more modern.

Required generic behavior:
- If an artifact family has activated role-separated review, later review standards keep that architecture unless a human explicitly retires it.
- Visual/presentation and teaching/language reviewers inspect the same immutable artifact but freeze verdicts independently.
- Neither sees executor PASS labels or the other reviewer verdict before its own freeze.
- Calibration uses a known rejected artifact without giving the reviewer the human answer key; expected minimum hits remain with the aggregator.
- Repair closure is role-scoped; the aggregator can only union/verify findings, never override a reviewer.
- A final human rejection invalidates both reviewer PASS results as acceptance authority for successor versions.

Promotion gate:
- Replay one historical false-PASS deck; a shallow reviewer must fail calibration or candidate review, while role-separated reviewers detect distinct visual and teaching defects.

## P1 — Human annotation colour semantics should be configurable and persistent

Evidence from real workflows shows colour is meaningful but project-specific.

Required generic capability:
- Allow a project to register colour -> semantic meaning, e.g. local revision, AI-like language, instructor-learning need, generic plugin issue, open teaching decision.
- Extraction preserves exact annotation type, colour, comment, page, coordinates, source PDF hash, and author when available.
- Colour meaning is stored with the feedback registry and survives later version remapping.
- Do not hard-code STAT5060 colours into the plugin.

Promotion gate:
- Two projects with different colour contracts can ingest annotations without semantic collision.

## P1 — Instructor-learning annotations must not automatically inflate student slides

Problem:
- “I do not understand this well enough to teach it” is different from “the student slide needs more text.”

Required generic behavior:
- Separate audience artifact feedback from instructor/speaker learning feedback.
- Blue/instructor-learning-equivalent items can route to speaker notes, instructor study packs, or teaching scripts.
- Promotion to visible slide content requires an explicit pedagogical reason.

Promotion gate:
- Instructor-only explanation closes the feedback without changing the student slide.

## P1 — Revision planning must produce a page-level semantic map before execution

For each candidate page record:
- teaching job;
- primary scientific object;
- required visible copy IDs;
- layout archetype;
- reading order;
- historical feedback guards applying to the page;
- permitted implementation freedom;
- forbidden regressions.

Codex/executor consumes this map; it does not invent page purpose.

Promotion gate:
- Executor can materialize a deck using only the frozen page map + approved copy without creating new prose.

## P1 — Full-deck human-feedback closure must be machine-queryable

Required artifacts:
- master CSV/JSON feedback registry;
- human-readable master ledger;
- candidate regression matrix;
- page-level review notes;
- unresolved guard count.

A candidate cannot report `READY_FOR_HUMAN_ACCEPTANCE=YES` when an active human-feedback item lacks closure evidence.

Promotion gate:
- Deliberately omit one historical feedback item and ensure readiness fails.

## P1 — Evidence/QA tooling must distinguish “proof of review” from “proof of quality”

- Unique page observations prove that a reviewer looked at each page; they do not prove the judgment was good.
- Hash/tree closure proves reviewed identity; it does not prove pedagogy.
- Geometry metrics are diagnostic evidence; they do not substitute for audience judgment.
- The review UI/report should keep these concepts separate.

## Do not encode project-specific content

Do not promote into generic plugin runtime:
- STAT5060 page numbers;
- horseshoe crab/alligator/Ohio examples;
- the specific offset example;
- exact homework/project wording;
- exact model formulas;
- CUHK course policy;
- exact 193-item registry.

Those remain evidence in the course repository. The generic promotion target is the workflow discipline above.


## P0 — Default existing-deck revision workflow

User-approved default for long-running presentation revision:

1. historical-feedback preflight with explicit counts;
2. lifecycle/supersession resolution;
3. explicit current-round modify scope plus human-locked and round-frozen scope;
4. bounded high-risk proof pack before broad rebuilds when material visual/pedagogical changes are involved;
5. direct proof review against historical guard IDs;
6. immediate page/component locking after explicit human PASS;
7. full candidate only after proof approval;
8. full-candidate review repeats complete-history consumption;
9. evidence/release closure last.

A future workflow may strengthen this sequence but must not silently replace it with a latest-version-only or full-deck-first revision path.
