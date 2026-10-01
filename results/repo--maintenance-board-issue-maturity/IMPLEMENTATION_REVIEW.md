# Independent Stage A Implementation Review

Task: `repo--maintenance-board-issue-maturity`  
Review stage: `STAGE_A_IMPLEMENTATION_REVIEW`  
Result: `REVISE`  
Reviewed functional candidate: `c6202533b7617a4eec95eca60accd4d2c620192f`  
Handoff/evidence-only branch head before this review: `27f0a45c6ae5decf71950157147fc8d00f07744f`

## Conclusion

The Stage A functional implementation is largely faithful to the approved v7 package:

- changed-file scope is within the authorized v7 surfaces;
- canonical board §§14–16 are unchanged, so v6.1 remains independent;
- Issue Forms and blank route match the frozen contracts;
- the pre-admission Action is limited to `issues: opened` + `issues: write`, with no checkout, repository secrets, Issue-body execution, Project mutation, lifecycle mutation, or automatic admission/classification;
- the metadata audit helper is read-only;
- `PRE_MIGRATION_ISSUE_METADATA.json` and `MIGRATION_CLASSIFICATION.csv` each cover all 86 current `maintenance-track` Issues;
- required anchors #4 / #5 / #35 / #63 / #86 are present as frozen;
- current live `maintenance-track` set is still 86 Issues;
- no Stage A live taxonomy migration is evidenced;
- the extra commit after the functional candidate adds only review-handoff/Clear-Writing evidence and does not change functional source.

However, Stage A has exposed one direct execution dead-end that must be resolved before G7.

## Blocker: BOARD-V7-AUDIT-CLOSURE-DEADEND-01

### Requirement

The approved package requires the post-migration live metadata audit to PASS before v7 can close. The same package must therefore provide a legal route to resolve any already-known live metadata violations that the audit will necessarily report.

### Direct evidence

`PRE_MIGRATION_ISSUE_METADATA.json` already proves 21 current lifecycle-integrity violations that are independent of v7 taxonomy labels:

1. Closed `COMPLETED` Issues with Project `DONE` but empty `Resolution commit`:
   - #53, #54, #55, #56, #57, #58, #59, #63, #64, #65

2. Closed `DUPLICATE` Issues still represented as Project `DONE`:
   - #52, #60, #61, #62, #66, #67, #68, #69, #70, #71, #72

The new audit code explicitly reports:

- completed close without non-empty Resolution commit;
- non-completion close represented as DONE.

`RESULT.md` also acknowledges these existing live drifts and states that the future audit will report them unless repaired.

But the current execution package limits existing-Issue migration to v7 taxonomy labels and explicitly forbids changing existing Project Status/Area or Issue lifecycle as part of taxonomy reconciliation. It provides no reviewed mutation route for the above 21 pre-existing violations.

### Causal risk

If G7 is authorized now, the task can successfully publish labels, Forms and the intake Action and migrate taxonomy, but the mandatory live audit is already known to fail for reasons the task is not authorized to repair.

That means the current package has a deterministic closure dead-end:

```text
G7 PASS
-> main publication
-> taxonomy migration
-> live audit
-> known non-zero violations
-> no authorized repair path
-> v7 cannot reach DONE
```

Proceeding to G7 would therefore create external taxonomy mutations while knowingly entering an unrecoverable state under the frozen execution contract.

### Minimum close condition

Return to Planner for a minimal execution-contract amendment. Do not redesign v7 taxonomy/intake architecture.

The amendment must choose and freeze one truthful route for the 21 known pre-existing lifecycle violations before G7:

1. Preferably add a bounded, independently reviewed board-truth reconciliation step that:
   - identifies the exact affected Issues from current live evidence;
   - for completed Issues, resolves and writes a truthful Resolution commit only when directly supported by existing closure evidence;
   - for duplicate/non-completion closes, reconciles Project representation according to the canonical board false-DONE rule;
   - does not reopen/close Issues merely for taxonomy migration;
   - preserves source TODO maturity/evidence/`tracking:#N`;
   - records pre/post Project metadata and rollback.

2. If the Planner believes these historical violations must remain out of v7 scope, it must instead revise the audit/acceptance contract through the required design-review path. The current package may not simply grandfather them silently while still claiming a full live metadata audit PASS.

The repair must be independently reviewed before G7 label cutover. Until then:

```text
G7_LABEL_CUTOVER_AUTHORIZED = NO
```

## Non-blocking observations

The path-scoped v7 tests PASS. The reported full-suite failures are in unrelated existing tests that attempt writes outside the sandbox or require unavailable optional packages; current evidence does not support treating those failures as a v7 product blocker.

The audit GraphQL pagination implementation should be exercised during the reviewed live path before relying on it for closure; no additional blocker is raised here without a direct runtime failure.

## Final fields

```text
RESULT = REVISE
REVIEW_STAGE = STAGE_A_IMPLEMENTATION_REVIEW
REVIEWED_COMMIT = c6202533b7617a4eec95eca60accd4d2c620192f
BLOCKERS = BOARD-V7-AUDIT-CLOSURE-DEADEND-01
G7_LABEL_CUTOVER_AUTHORIZED = NO
NEXT_HANDOFF = PLANNER
```
