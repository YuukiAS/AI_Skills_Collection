# Student Assessment Research Authoring — Delivery Closure Amendment V1

Status: **CANONICAL COMPANION / BINDING FOR STUDENT-ASSESSMENT PRODUCTION**  
Date: 2026-10-07  
Applies to: all non-trivial student-facing Homework, Project, milestone, policy, template and oral-brief work

This amendment exists because the STAT5060 HW1 replay demonstrated a second class of failure after the original non-recurrence rules were added:

> the control system itself can prevent delivery when it keeps reopening a nearly accepted artifact, treats optional experiments as blockers, or accumulates more local authorities than the document requires.

The objective is not “more governance”. The objective is a usable student artifact with the smallest reliable control system.

---

## 1. Delivery is the product

Every production milestone must name the next visible artifact:

~~~text
PRIMARY_DELIVERABLE =
PRIMARY_CANDIDATE =
NEXT_VISIBLE_PROOF =
USER_DECISION_NEEDED =
~~~

If a new governance file, validator, critic, or prompt does not directly enable the next visible artifact, do not create it.

For a small Homework handout, the control plane must remain smaller than the artifact problem it governs.

---

## 2. One active route only

At any point there may be only one active:

~~~text
ACTIVE_PLANNER_AUTHORITY
ACTIVE_ACCEPTANCE_STANDARD
ACTIVE_CONTROLLER_GOAL
ACTIVE_POSITIVE_BASELINE
~~~

Older local routes must be explicitly marked:

~~~text
SUPERSEDED
HISTORICAL_EVIDENCE_ONLY
DO_NOT_EXECUTE
~~~

A Producer must not choose among multiple V1/V2/V3/V4 prompts.

A new active route is allowed only when the previous route is retired with:

- exact root cause;
- exact superseding file;
- what remains locked;
- what new decision is being made.

---

## 3. Positive candidate cannot be invalidated by an optional experiment

When a user asks to compare an accepted or nearly accepted candidate with an exploratory alternative:

~~~text
PRIMARY_CANDIDATE = preserved
EXPLORATORY_OPTION = independent
~~~

Rules:

1. evaluate each option independently;
2. failure of the exploratory option does not invalidate the primary candidate;
3. if the primary candidate passes and the exploratory option fails, the task may still proceed with the primary candidate;
4. another production round is not required merely to manufacture a second acceptable option;
5. the user sees the failed alternative only if seeing it is itself useful and safe;
6. no exploratory alternative may consume the primary candidate's acceptance or locks.

Required outcomes:

~~~text
BOTH_VALID
PRIMARY_ONLY_VALID
BOTH_INVALID
~~~

'PRIMARY_ONLY_VALID' is a normal successful comparison outcome.

---

## 4. “Basically good” creates a preservation baseline

When the user says an artifact is broadly acceptable and gives bounded remaining findings, immediately freeze that exact artifact as:

~~~text
CURRENT_POSITIVE_BASELINE
~~~

Then classify every requested change:

~~~text
SEMANTIC_DELTA
COPY_DELTA
VISUAL_DELTA
DEPENDENT_LAYOUT_DELTA
~~~

Everything not named by those deltas is frozen.

A later experiment must start from the positive baseline and may not silently reopen unrelated content, layout, typography, or packaging.

---

## 5. Layout dependencies must be explicit

Global layout variables create dependent state. Examples:

- font size;
- body leading;
- page geometry;
- column width;
- heading size;
- table width.

Dependent pagination controls include:

- Needspace;
- keep-with-next;
- keep-together;
- widow/orphan controls;
- manual break hints;
- minimum-space guards.

If a global layout variable changes, all dependent pagination controls are automatically reopened for validation.

Do not carry a Needspace threshold tuned under one font size into another font size and then blame the new font size for the resulting blank page.

---

## 6. Prove the composition before tuning micro-spacing

For any page-flow problem:

~~~text
semantic blocks
-> legal breakpoint
-> composition archetype
-> feasibility render
-> rendered review
-> only then micro-spacing
~~~

Default maximum for a simple handout repair:

- up to 3 meaningful composition archetypes;
- up to 3 spacing variants per archetype.

More than 9 visual candidates requires an explicit explanation of why the problem cannot be isolated more directly.

Do not run 54 or 72 near-identical candidates to discover a semantic or pagination-control error.

---

## 7. Validator must prove both rejection and admission

Before a deterministic validator controls a real candidate:

~~~text
KNOWN_BAD_CONTROL = REJECTED
KNOWN_GOOD_OR_SYNTHETIC_VALID_CONTROL = ACCEPTED
~~~

If it can reject bad artifacts but cannot accept a valid control, it is not production-ready.

If all real candidates fail the same class:

1. stop;
2. inspect the validator;
3. inspect gate ownership;
4. inspect stale dependent layout controls;
5. do not widen the candidate grid until the failure class is explained.

---

## 8. Objective and aesthetic gates remain separate

Deterministic gates answer questions such as:

- is the text correct?
- do totals and references agree?
- did a protected block change?
- is there clipping/overflow?
- did a forbidden break occur?
- are the required files present?

Rendered review answers:

- is the spacing comfortable?
- is a page awkwardly sparse?
- is hierarchy clear?
- is the page visually balanced enough?
- is a larger font worth an extra page?

Aesthetic metrics may inform review. They do not become hard gates without calibration.

---

## 9. User-review budget is a hard resource

The user must not receive:

- speculative spacing candidates;
- a candidate known to have routine visual defects;
- a candidate that has not passed the required independent rendered review;
- a new full artifact when only one bounded region changed.

For a bounded final repair:

~~~text
HUMAN_REVIEW_BUDGET = 1
~~~

The one review should be a final acceptance decision or a preference between already acceptable options.

If the same routine defect reaches the user twice, stop local repair and perform incident/root-cause review before any further candidate.

---

## 10. Incident trigger for process failure

Enter incident mode when any occurs:

- the same visible defect reaches the user twice;
- two broad rounds fail to reduce open issues;
- a closed guard reopens;
- all candidates fail one unexplained gate;
- governance files grow while the visible artifact does not improve;
- an exploratory alternative blocks an already valid primary candidate;
- a typography experiment fails because of stale pagination guards;
- more than one active authority/controller remains live.

Incident mode requires:

~~~text
CURRENT_POSITIVE_BASELINE
ROOT_CAUSE
ACTIVE_ROUTE_AFTER_INCIDENT
SUPERSEDED_ROUTES
UNCHANGED_LOCKS
NEXT_VISIBLE_ARTIFACT
~~~

Do not create another ordinary “V+1” local patch until those fields are resolved.

---

## 11. Completion discipline

Once the user accepts the student artifact:

1. freeze exact source, artifact hash and visual lock;
2. do not reopen it while finishing instructor solution/rubric/package work;
3. later work may reveal a genuine substantive defect, but that requires a new explicit semantic revision;
4. package/release QA cannot silently rewrite the accepted student artifact.

For a Homework, acceptance should end the student-PDF design loop.

---

## 12. Minimal closure topology

For a bounded repair on an established Homework family, the default topology is:

~~~text
positive baseline
-> bounded Planner delta
-> fresh Critic only if semantics/scoring changes
-> Producer
-> deterministic objective QA
-> fresh rendered review
-> optional GPT Work if major/recovery
-> one user acceptance
-> lock
~~~

Do not add component-proof, golden-page, large candidate-grid, or recovery machinery when the bounded task does not need them.

---

## 13. Mandatory preflight additions

Before production report:

~~~text
CURRENT_POSITIVE_BASELINE =
PRIMARY_CANDIDATE =
EXPLORATORY_OPTIONS =
ACTIVE_PLANNER_AUTHORITY =
ACTIVE_ACCEPTANCE_STANDARD =
ACTIVE_CONTROLLER_GOAL =
SUPERSEDED_ROUTE_COUNT =
DEPENDENT_LAYOUT_CONTROLS_REOPENED = YES | NO | N/A
KNOWN_GOOD_VALIDATOR_CONTROL = PASS | N/A
CANDIDATE_BUDGET =
NEXT_VISIBLE_ARTIFACT =
USER_REVIEW_BUDGET =
~~~

If these fields show that the process is larger than the remaining artifact problem, simplify before implementation.

---

## 14. HW1 lesson in one sentence

The HW1 failure was not that a four-page PDF was intrinsically difficult.

The failure was repeatedly allowing process machinery, unproved hard constraints, stale pagination guards, and optional experiments to outrank the simple goal:

> preserve the good Homework, make the bounded requested changes, independently verify them, and deliver one usable artifact.