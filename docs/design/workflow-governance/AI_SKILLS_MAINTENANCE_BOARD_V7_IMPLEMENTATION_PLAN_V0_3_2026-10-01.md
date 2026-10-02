# AI Skills Maintenance Board — Issue Maturity Implementation Plan v0.3

Date: 2026-10-01
Task: repo--maintenance-board-issue-maturity
Repository: YuukiAS/AI_Skills_Collection
Package version: v0.3
Approved design: docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V7_MATURITY_PROPOSAL_2026-10-01.md
Approved design commit: 3d091421c7afe8d4f90687ef6e0ce2686bcaf426
Previous package: v0.2
Stage A reviewed functional candidate: c6202533b7617a4eec95eca60accd4d2c620192f
Stage A review: results/repo--maintenance-board-issue-maturity/IMPLEMENTATION_REVIEW.md
Stage A review commit: 78bb326a73aaa1cd44aeb17414648ae0b89c90bc
Stable blocker addressed: BOARD-V7-AUDIT-CLOSURE-DEADEND-01
Execution branch: reviewed/repo--maintenance-board-issue-maturity
Worktree: ../AI_Skills_Collection-repo--maintenance-board-issue-maturity
Primary environment: Longleaf_Codex
Status: READY_FOR_EXECUTION_CRITIC_REVIEW

## 1. Planner disposition

BOARD-V7-AUDIT-CLOSURE-DEADEND-01 = ACCEPT

This amendment does not redesign taxonomy, Forms, the intake Action, the audit, hierarchy, label cutover, Longleaf routing, v6.1 independence, or version policy.

It adds one bounded lifecycle-metadata reconciliation stage before G7 because Stage A evidence already proves that the final live audit would otherwise fail deterministically.

G7 remains unauthorized until the repair itself has passed independent review.

## 2. Inherited v7 contract

All accepted v0.2 semantics remain unchanged:

- canonical TODO owns problem/evidence/maturity/tracking:#N;
- Project Status owns lifecycle;
- Project Area owns primary ownership;
- kind/scope/area labels are searchable taxonomy only;
- two Issue Forms + blank route;
- tiny issues:opened / issues:write pre-admission Action;
- complete classification before taxonomy mutation;
- ambiguous kind fails closed;
- metadata audit remains read-only and its acceptance contract is unchanged;
- native sub-issues/dependencies only;
- v0.2 pre-publication label cutover and provenance-aware label rollback;
- stale auto-close forbidden;
- v6.1 remains independent;
- Repository bump NONE; all plugins NO_BUMP;
- Workstation / CUHK_Workstation_WSL_Codex availability is not required.

## 3. Frozen known lifecycle-drift cohort

Stage A snapshot and independent review identify exactly 21 known pre-existing violations.

Closed COMPLETED + Project DONE + missing Resolution commit:

#53, #54, #55, #56, #57, #58, #59, #63, #64, #65

Closed DUPLICATE + Project DONE:

#52, #60, #61, #62, #66, #67, #68, #69, #70, #71, #72

The current audit contract remains unchanged. These violations must be truthfully reconciled; they are not grandfathered.

## 4. New pre-G7 gate: lifecycle truth reconciliation

Execution sequence becomes:

Stage A candidate
-> Stage A review exposes blocker
-> v0.3 execution amendment approved
-> prepare reconciliation evidence without mutation
-> independent reconciliation-plan review PASS
-> execute bounded lifecycle metadata repair
-> post-repair readback
-> independent lifecycle-repair review PASS
-> G7 label cutover
-> normal v7 publication / taxonomy migration / audit / acceptance

No G7 label mutation may begin before lifecycle-repair review PASS.

## 5. Required pre-repair evidence

Create under results/repo--maintenance-board-issue-maturity/:

- LIFECYCLE_DRIFT_PRE_REPAIR.json
- LIFECYCLE_DRIFT_RECONCILIATION_PLAN.json

For every exact affected Issue, PRE_REPAIR records:

- Issue number/title;
- state + state reason;
- Project item id;
- Project Status;
- Project Area;
- current Resolution commit;
- current labels;
- canonical source locators;
- closure-evidence locators examined.

The live state must still match the frozen cohort. Material drift stops the repair and returns Planner/Reviewer.

For every Issue, RECONCILIATION_PLAN contains exactly one proposed action:

- SET_RESOLUTION_COMMIT
- REMOVE_FROM_PROJECT_AS_NON_COMPLETION
- BLOCKED_NO_TRUTHFUL_REPAIR

No live repair occurs until the full plan is independently reviewed.

## 6. Direct evidence rule for completed Issues

For #53–#59 and #63–#65, a Resolution commit may be written only when existing durable closure evidence directly identifies an exact owner-repo commit as the closure/evidence anchor for that same tracked work.

Acceptable support must contain an exact commit SHA plus an explicit connection to the tracked Issue, its exact canonical maintenance entry, or its exact closure task.

Acceptable sources include:

- an existing Issue body/comment explicitly naming that Resolution/closure commit;
- an existing RESULT / FINAL_REPORT / closure artifact explicitly naming the same Issue or exact canonical source entry and the Resolution/closure commit;
- another existing canonical closure record with the same explicit identity and commit.

Not sufficient by itself:

- nearest commit by date;
- latest commit before Issue close;
- a commit merely touching related files;
- source status PROMOTED;
- title similarity;
- a release/tag without direct mapping to this tracked work;
- another Issue's Resolution commit.

Each completed row must record:

issue_number
proposed_resolution_commit
closure_evidence_locators
direct_support_explanation

If any of the ten Issues lacks direct support, mark BLOCKED_NO_TRUTHFUL_REPAIR and stop before all lifecycle repair mutation. Return Planner. Do not guess to make the audit pass.

## 7. Duplicate / non-completion repair

For #52, #60–#62 and #66–#72, proposed action is REMOVE_FROM_PROJECT_AS_NON_COMPLETION.

Required behavior:

- keep Issue CLOSED / DUPLICATE exactly as-is;
- do not reopen or re-close;
- do not modify source TODO maturity/evidence/tracking:#N;
- do not create Resolution commit;
- remove the Issue item from AI Skills Maintenance so it no longer appears as DONE/History;
- verify the Project item is absent afterward.

If GitHub automation re-adds a closed duplicate or recreates false DONE, stop and return Planner. Do not remove maintenance-track or change Issue state without a separately reviewed amendment.

## 8. Independent reconciliation-plan review

Before live lifecycle repair, an independent Reviewer must inspect:

- exact 21-Issue cohort;
- PRE_REPAIR snapshot;
- every proposed Resolution commit;
- every direct evidence locator;
- every duplicate removal action;
- rollback plan;
- confirmation that no Issue state, source TODO, tracking:#N or taxonomy mutation is proposed.

Required PASS fields:

LIFECYCLE_RECONCILIATION_PLAN = PASS
LIVE_LIFECYCLE_REPAIR_AUTHORIZED = YES

REVISE means repair the plan/evidence and re-review. G7 remains blocked.

## 9. Bounded live repair

Only after reconciliation-plan PASS:

Completed cohort:
- leave Issue CLOSED / COMPLETED;
- leave Project Status DONE;
- leave Project Area unchanged;
- set exactly the independently reviewed Resolution commit;
- read back exact value.

Duplicate cohort:
- leave Issue CLOSED / DUPLICATE;
- remove its Project item;
- verify Project absence;
- leave source TODO and tracking:#N unchanged.

No other Issue/Project mutation is authorized by this repair.

## 10. Post-repair evidence and independent repair review

Create:

- LIFECYCLE_DRIFT_POST_REPAIR.json
- LIFECYCLE_DRIFT_ROLLBACK.json
- LIFECYCLE_DRIFT_REVIEW.md

POST_REPAIR must prove:

- all ten completed Issues remain CLOSED/COMPLETED;
- all ten remain Project DONE;
- all ten have the exact independently reviewed Resolution commit;
- all eleven duplicate Issues remain CLOSED/DUPLICATE;
- all eleven are absent from AI Skills Maintenance;
- no source TODO maturity/evidence/tracking:#N changed;
- no unrelated Issue or Project field changed.

An independent Reviewer must inspect the executed repair and return:

LIFECYCLE_DRIFT_REPAIR = PASS
G7_LABEL_CUTOVER_AUTHORIZED = YES

Without this PASS, G7 remains unauthorized.

## 11. Rollback

Before repair, snapshot enough metadata to restore exact pre-repair state if a repair mutation partially fails.

Completed Issues:
- restore exact pre-repair Resolution commit value, including empty;
- do not change Issue state / Project Status / Area.

Duplicate Issues:
- re-add the same Issue to the same Project;
- restore exact pre-repair Area / Status / Resolution values;
- do not change Issue state/reason or source data.

Rollback intentionally restores the known pre-repair drift only to avoid a partial mutation set. That restored state remains audit-invalid and keeps G7 blocked.

maintenance-track is never changed.

Any rollback residual drift is a hard blocker.

## 12. Interaction with taxonomy migration and audit

This repair is board lifecycle truth reconciliation, not taxonomy migration.

It does not change:

- kind/scope/area classification;
- migration classification table;
- Forms;
- intake Action;
- audit logic;
- source-of-truth architecture.

After lifecycle-repair Reviewer PASS, resume the existing v0.2 flow:

G7 pre-publication label snapshot/cutover
-> labels ready
-> main integration
-> taxonomy migration
-> full live metadata audit
-> Forms / Action / search acceptance
-> closure

The final audit must genuinely PASS. No grandfathering or exception suppression is allowed.

## 13. G7 prerequisite amendment

All BOARD-V7-LABEL-CUTOVER-01 fixes remain unchanged.

G7 prerequisites now additionally require:

- reconciliation-plan independent review PASS;
- lifecycle repair executed;
- post-repair readback complete;
- lifecycle-repair independent review PASS.

Only then may G7 snapshot/reconcile v7 label definitions.

## 14. Failure recovery

Add to the existing v0.2 recovery contract:

- completed Issue lacks direct closure evidence -> no repair mutation; return Planner;
- Resolution commit evidence is inferential or ambiguous -> no mutation;
- live cohort materially differs from frozen 21 -> return Planner/Reviewer;
- repair partially fails -> rollback repair batch from PRE_REPAIR;
- duplicate Project item reappears -> stop; do not change maintenance-track or Issue state;
- repair rollback has residual drift -> hard blocker;
- post-repair independent review REVISE -> G7 remains unauthorized;
- full live audit still fails later -> no grandfathering; only another separately reviewed truthful reconciliation may proceed.

Existing label cutover, Longleaf routing and chooser-UI recovery remain unchanged.

## 15. Environment / version boundary

Primary execution remains Longleaf_Codex.

This is GitHub Project metadata reconciliation, not machine-consumer adaptation. Workstation / CUHK_Workstation_WSL_Codex outage does not block this repair or later v7 GitHub work.

Repository bump decision: NONE
Affected plugins: all NO_BUMP
Production Plugin Capability Gate Matrix: NOT REQUIRED

## 16. Planner result

BOARD-V7-AUDIT-CLOSURE-DEADEND-01 = ACCEPTED_AND_REVISED
KNOWN_COMPLETED_MISSING_RESOLUTION = #53,#54,#55,#56,#57,#58,#59,#63,#64,#65
KNOWN_DUPLICATE_FALSE_DONE = #52,#60,#61,#62,#66,#67,#68,#69,#70,#71,#72
AUDIT_CONTRACT_CHANGED = NO
GRANDFATHERING = NO
G7_LABEL_CUTOVER_AUTHORIZED = NO_UNTIL_LIFECYCLE_REPAIR_REVIEW_PASS
V7_ARCHITECTURE_CHANGED = NO
V6_1_IMPLEMENTED = NO
NEW_BLOCKERS_FOUND_BY_PLANNER = NONE
