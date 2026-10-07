# Anti-Shortcut Production Contract

Before applying this contract, read `presentation-end-to-end-pre-execution-runbook.md` and then `pre-execution-cumulative-acceptance-contract.md`.

This contract governs non-trivial presentation creation and revision. It is designed for the actual failure mode of an executor that optimizes the easiest observable proxy rather than the intended presentation outcome.

The executor is not assumed to remember prior feedback, preserve accepted work voluntarily, or interpret a prose checklist exactly as the Planner intended. Every important requirement must therefore be represented by authority, scope, a production check, and independent review.

## 1. Shortcut threat model

The workflow must explicitly defend against these recurrent shortcuts.

### Authority shortcuts

- read only the latest version or latest feedback batch;
- count records without consuming their meaning;
- map historical feedback to any globally valid current page;
- silently reinterpret an unresolved or conflicting requirement;
- treat executor summaries as higher authority than raw human feedback.

### Scope shortcuts

- regenerate the whole deck to fix a local page;
- modify a shared component without declaring every consumer page affected;
- touch unlocked-looking files that were not in the explicit allowlist;
- use a broad refactor to hide unrelated visual changes.

### Content shortcuts

- delete difficult teaching content to fix overflow or whitespace;
- replace an explanation with a formula, package name, API table, slogan, or generic diagram;
- add plausible audience-visible prose that was never approved;
- merge distinct estimands or mechanisms into one compressed page;
- move interpretation away from its evidence merely to improve occupancy metrics.

### Layout shortcuts

- use columns because horizontal space exists, even when reasoning is sequential;
- shrink fonts or figures instead of changing composition;
- fill space with cards, boxes, decorative arrows, captions, or repeated labels;
- claim a template/component PASS from source presence without checking the final render;
- repair one page by changing header, footer, typography, or shared macros globally.

### Test and evidence shortcuts

- write tests that recognize fixture IDs, chosen bad values, phrases, or hashes;
- write the validator in the same task and tune it until the candidate passes;
- assert constants instead of passing accepted inputs through production detectors;
- report file/count/schema presence as semantic correctness;
- use clean worktree, executor prose, or self-authored evidence as acceptance;
- review only representative pages and return a global PASS;
- call an inaccessible or unreviewed gate PASS rather than NOT_INDEPENDENTLY_VERIFIED.

## 2. Required authority bundle

Before the executor may edit a presentation, the outer orchestrator freezes an authority bundle containing:

```text
artifact family and exact baseline identity
stable PageIDs and page ancestry
page jobs and required/forbidden objects
exact visible-copy authority when available
layout archetype and shared-component bindings
complete feedback ledger and lifecycle
human locks and explicit unlocks
round allowlist
cumulative acceptance gates
validator/reviewer runtime version
```

The bundle is hashed and read-only to the executor.

If any required field is unresolved, the task stops before candidate editing.

## 3. Proof-carrying patch

Every executor candidate must include a machine-readable patch manifest:

```text
candidate_id
parent_candidate_id
baseline_commit
validator_version
modified_page_ids[]
modified_component_ids[]
addressed_feedback_ids[]
unchanged_locked_page_ids[]
unchanged_locked_component_ids[]
required_object_relocations[]
visible_copy_changes[]
authorised_dependency_invalidations[]
open_items_before[]
open_items_after[]
```

Rules:

- modified IDs are a subset of the round allowlist;
- every source diff maps to one modified page/component ID;
- every addressed feedback ID maps to actual evidence;
- no required object disappears without an explicit approved relocation;
- no audience-visible string appears outside the frozen copy authority or explicit Planner addition;
- unchanged locks are proved by source/body/render identities as appropriate.

The executor does not decide that its evidence is sufficient; it only supplies the candidate and patch manifest.

## 4. Monotone convergence invariants

For existing-deck revision, each accepted round must satisfy:

```text
open_feedback_next ⊆ open_feedback_current
human_locked_pages_next ⊇ human_locked_pages_current
human_locked_components_next ⊇ human_locked_components_current
modified_ids ⊆ explicit_round_allowlist
unrelated_source_changes = 0
unrelated_render_changes = 0
new_P0_or_P1_regressions = 0
previously_closed_guard_recurrences = 0
```

A later round may not reopen an accepted item merely because the physical page number, source file, or layout changed.

If a shared component changes, every consumer page is automatically placed in deterministic regression scope. This does not reopen its semantic or visible-copy lock.

## 5. Change-budget and regeneration rules

The executor receives an explicit change budget.

- A local repair may not become a full-deck rewrite.
- Full regeneration requires an explicit Planner decision that names why local preservation is impossible.
- When fewer than one third of pages remain open, full-deck regeneration is forbidden by default.
- A shared-component repair is completed and locked before unrelated page composition continues.
- Page deletion, page merge, content compression, and layout-archetype replacement each require an explicit authority record.
- Overflow, whitespace, or build difficulty never authorizes semantic deletion.

## 6. Dependency-aware locks

Locks are layered:

```text
semantic lock
visible-copy lock
layout-archetype lock
page-body visual lock
shared-component lock
```

A change invalidates only dependent lock layers.

Examples:

- correcting a footer invalidates footer geometry review for all consumers but not page semantics or copy;
- changing page copy invalidates page layout/body review but not the approved shared header;
- changing a shared font invalidates typography/render checks for all pages and requires explicit Planner authorization;
- a page-body repair cannot alter the title, header, footer, or other shared component unless that component is separately unlocked.

## 7. Independent acceptance pipeline

Apply `independent-review-contract.md`.

The executor stops at the candidate commit and reports only readiness for independent validation.

Authoritative deterministic validation:

- runs in a fresh process/CI or strictly isolated read-only subagent;
- uses a version-pinned validator fixed before candidate execution;
- consumes the exact authority bundle, candidate commit, and patch manifest;
- executes production detectors, accepted controls, property mutations, historical regression guards, protected-path checks, and lock comparisons;
- cannot edit candidate, authority, tests, thresholds, or fixtures.

Rendered review is separate and blind to executor narratives and expected answer keys.

## 8. Review-scope integrity

A review verdict has an explicit scope:

```text
reviewed_pages[]
reviewed_components[]
reviewed_requirements[]
unreviewed_requirements[]
artifact_hashes[]
```

A scoped review cannot emit a global PASS while mandatory global requirements are unreviewed.

Changed-page delta review does not replace final full-deck regression review. It reduces user workload during convergence; the final release still checks the complete artifact.

## 9. Hidden historical regression corpus

Human-rejected artifacts and known regressions are retained as a versioned corpus.

- The executor receives the guard schema but not all expected findings.
- A small sentinel set may be exposed for capability calibration.
- A holdout set remains unavailable to the executor and is used by independent validation/review.
- Prompt tuning against one rejected artifact does not count as reviewer maturity.
- Promotion requires at least one unrelated deck to pass under the same runtime.

## 10. Recurrence and escalation rules

The workflow does not allow infinite local patching.

### Same-guard recurrence

If one closed guard reappears in a later candidate:

1. reject the candidate;
2. identify the shared primitive, source-of-truth, or missing production detector responsible;
3. repair that root cause before another candidate round;
4. add the recurrence to the historical regression corpus.

If the same guard recurs twice after claimed repair, project-local page patching stops.

### Repeated control-plane failure

If a new P0 self-certification class appears after the current bounded repair:

```text
PROJECT_LOCAL_CONTROL_PATCHING = STOP
CANDIDATE_PRODUCTION = FROZEN
```

Rebuild the generic validator/reviewer runtime in the presentations plugin, independently review and version it, replay historical and unrelated decks, then rerun the frozen candidate.

### Human-round budget

A normal deck should converge in two to four human review rounds.

If open issues do not strictly decrease after a round, or accepted items are reopened, the next action is not another full candidate. Perform a root-cause review of authority, component primitive, copy freeze, or validator coverage.

## 11. Completion semantics

Executor statuses:

- `CANDIDATE_MATERIALIZED`
- `READY_FOR_INDEPENDENT_VALIDATION`
- `STOP_PLANNER_DECISION_REQUIRED`
- `BLOCKED_DEPENDENCY`

Independent validator statuses:

- `PASS`
- `FAIL`
- `NOT_INDEPENDENTLY_VERIFIED`
- `BLOCKED`

Rendered reviewer statuses:

- `PASS`
- `REVISE`
- `NOT_INDEPENDENTLY_VERIFIED`
- `BLOCKED`

Only the acceptance aggregator, after required human decisions, may declare the round accepted and create new locks.

## 12. Minimum promotion evidence

The generic workflow is not mature until it demonstrates on a real existing deck:

- exact authority and baseline binding;
- bounded allowlist-only candidate edits;
- proof-carrying patch manifest;
- production detectors shared by validation and mutation tests;
- independent validator runtime immutable during candidate execution;
- blind rendered review;
- hidden historical regression replay;
- monotonically shrinking open scope and growing locks;
- two-to-four-round user convergence;
- final full-deck regression without template, content, whitespace, footer/header, or page-order recurrence.
