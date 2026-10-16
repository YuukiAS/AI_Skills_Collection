# Project Instructions Editor C7 G4 replay Critic review

Date: 2026-10-05
Result: `REVISE`

Active review context:

```text
target_repo=YuukiAS/AI_Skills_Collection
target_plugin_or_domain=standalone Skill / project-instructions-editor
design_topic_or_task_key=project-instructions-editor--standalone-skill-implementation
source_branch_or_ref=work/project-instructions-editor--standalone-skill-implementation
review_stage=C7 final fresh replay / G4 regression adjudication
FINAL_CANDIDATE_COMMIT=C7=263df60b1ffd76704c33b5ddee014168a21057b2
BLOCKER_EVIDENCE_HEAD=a01c77df6b1e33e9aa129bfed1908443cbdcbc44
```

Reviewed directly:

- latest main Planner/Critic role contracts, Capability Gate policy and maintenance-board contract;
- exact C7 `SKILL.md` and `references/editor-contract.md`;
- exact C7 G4 blocker evidence;
- prior frozen protected-absence contract and Gate taxonomy;
- Issue #93 lifecycle/source scope.

No new external product fact is needed for this adjudication: the blocker is an internal contradiction between exact C7 output and the already-frozen protected-absence contract. Previously verified ChatGPT Project/Skill product behavior is unchanged and not the disputed fact.

## Judgment

The Executor stopped correctly.

The raw nested Codex transport is no longer the blocker. It executed successfully and produced fresh exact-C7 evidence.

R7's language/exactness repair also worked in the public-safe Server/VPS replay: the prior ordinary-English self-exemption no longer appears.

However, C7 G4 exposes a real product regression in protected absence:

```text
保留已接受的用户决定。不要恢复用户已删除或拒绝的规则。
```

The second sentence is not merely a harmless restatement. It converts targeted deletion/rejection history that should only constrain the current edit into a new durable Project-resident meta-rule.

That violates the already-frozen protected-absence contract:

- deletion/rejection evidence may suppress reintroduction during the current edit;
- an absent deleted/rejected rule remains absent;
- the final long-lived setting should normally contain neither the deleted rule nor its deletion history;
- a durable prohibition/history marker is allowed only when the current user explicitly asks to store it as long-lived Project state.

The output does not name the deleted nightly-build rule, but genericizing the deletion history into “do not restore deleted/rejected rules” still preserves the history mechanism as durable Project policy. The Executor was therefore correct to mark G4 failed and stop.

## Stable blocker

```text
R5=REOPENED_BY_C7_G4
```

This is not a new architecture blocker and does not justify a fifth Gate.

### Root cause

C7 has a strong local Protected Absence rule, but its final whole-candidate pass is still centered on reading/language consistency. Targeted history can therefore leak back into the completed setting as a generalized meta-rule.

The missing operational invariant is:

```text
targeted history is edit-control evidence,
not an independent source of new durable Project rules
```

History may:

- preserve an already-live/current durable rule;
- prevent an absent deleted/rejected rule from being reintroduced;
- justify a current-edit omission.

History may not, by itself:

- create a new generic “do not restore deleted/rejected rules” policy;
- create tombstones or deletion-history commentary;
- turn old rejection/deletion process into durable Project state.

Exception: the current user explicitly asks to adopt such a prohibition/history marker as a durable Project rule.

### Minimum closure

Keep the frozen architecture, modes, no-op semantics, R6 repair, R7 exactness repair, Gate taxonomy, routing, wrapper architecture, and release plan unchanged.

Make one bounded implementation repair:

1. strengthen the final whole-candidate semantic consistency pass so it checks protected absence/history residue in addition to reading/language consistency;
2. explicitly treat targeted deletion/rejection history as current-edit control evidence rather than a source of new durable rules;
3. after drafting any bounded edit/consolidation/full replacement, remove any rule whose only semantic support comes from deletion/rejection history unless the current user explicitly requested that rule as durable state;
4. preserve valid current/live durable rules such as “preserve accepted user decisions” when independently supported by the live setting/current request;
5. do not implement a phrase blacklist, tombstone regex, or nightly-build special case.

Add a focused regression using the same structural failure: a user explicitly says one historical rule was deleted and must not be restored; the final setting must omit that rule and must not generalize the deletion history into a new long-lived prohibition.

Because candidate-owned source must change after a final Gate failure, C7 remains failed. Freeze a new C8 and rerun fresh affected evidence from exact C8; do not stitch C7 Gate results into C8.

## Gate judgment

```text
RAW_NESTED_CODEX_REPLAY_AUTHORIZED=YES
RAW_NESTED_CODEX_REPLAY_USED=YES
RAW_NESTED_CODEX_REPLAY_EXECUTABLE=YES

R6=CLOSED
R7=FIXED_FOR_OBSERVED_LANGUAGE_FAILURE
R5=REOPENED_BY_C7_G4

G1=C7_FRESH_COMPLETED_NOT_REUSABLE_FOR_C8
G2=C7_FRESH_COMPLETED_NOT_REUSABLE_FOR_C8
G3=C7_FRESH_COMPLETED_NOT_REUSABLE_FOR_C8
G4=FAIL

IMPLEMENTATION_OVERALL=REVISE
E7=NOT_FORMED

READY_FOR_INTEGRATION=NO
READY_FOR_RELEASE=NO
```

Issue #93 remains `DOING`. This review does not imply a Project status mutation or release authorization.

## Next handoff

Per the Critic role contract, this REVISE returns to Planner for a bounded recovery package. The Planner should not reopen product architecture; it should formalize only the minimal C8 repair described above and return a Critic prompt for execution approval.
