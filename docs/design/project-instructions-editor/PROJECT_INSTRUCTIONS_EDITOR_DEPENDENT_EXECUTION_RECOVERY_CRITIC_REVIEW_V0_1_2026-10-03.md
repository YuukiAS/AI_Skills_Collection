# Project Instructions Editor — Dependent Execution Recovery Critic Review v0.1

Date: 2026-10-03  
Result: `PASS`  
Repository: `YuukiAS/AI_Skills_Collection`  
Source branch/ref: `main`  
Latest main observed: `c4018d25c98c85611321c59246ace2979c6c1cf4`  
Execution branch: `work/project-instructions-editor--standalone-skill-implementation`  
Execution branch observed head: `ebbebee0c42f93d362811594a829bc336a481e8f`  
Review stage: dependent-execution recovery after current-main drift  
Tracking: `#93`

Reviewed recovery package:

- Plan: `docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_DEPENDENT_EXECUTION_RECOVERY_PLAN_V0_1_2026-10-02.md`
- Resume: `docs/operations/prompts/PROJECT_INSTRUCTIONS_EDITOR_DEPENDENT_EXECUTION_RESUME_V0_1.md`
- Package commit: `0cc2abb061ab95655b95bc22846f3aef8877f40c`

The Plan and Resume blobs on latest main are byte-identical to the package commit.

Current facts independently rechecked:

```text
main VERSION = 5.4.1
main workflow-core = 0.5
main shared replay timeout = 3
task branch merge base = 98721a202bc557c0b9c0800e66e50cab466bfba2
task branch is diverged from current main
```

```text
CRITIC_RESULT=PASS
R3_SUPERSEDE_DECISION=PASS
VERSION_DRIFT_RECOVERY=PASS
MAIN_SYNC_ROUTE=PASS
C2_FORMATION_CONTRACT=PASS
R1=OPEN
R2=OPEN
RECOVERY_EXECUTION_APPROVED=YES
READY_FOR_CODEX=YES
READY_FOR_GATES=NO
READY_FOR_INTEGRATION=NO
READY_FOR_RELEASE=NO
NEXT_HANDOFF=EXECUTOR
```

## 1. Closure of the prior dependent blocker

The Executor stopped correctly when the previous R3 repair could no longer satisfy the current-main condition.

The old R3 finding was about task ownership, not about proving that `0.5` was permanently correct. Current main now owns the shared replay timeout at `3`, introduced outside the Project Instructions Editor task.

The recovery correctly reframes the requirement:

- this task must not own a special replay-timeout value;
- after synchronization, the task inherits the latest current-main shared replay behavior;
- the Executor must not decide `0.5` versus `2` versus `3` inside this task.

Therefore:

```text
R3_SUPERSEDE_DECISION=PASS
```

This does not close R1/R2 and is not an implementation PASS.

## 2. VERSION drift recovery

The previously accepted release classification remains valid:

```text
Repository bump decision = MINOR
project-instructions-editor standalone = 0.1
central plugins = NO_BUMP for this task
```

Current main is now `5.4.1`, so if it remains `5.4.1` when recovery execution starts, the correct candidate remains `5.5.0`, with release delta `5.4.1 -> 5.5.0`.

The recovery explicitly preserves:

- the `5.4.1` release history;
- workflow-core `0.5`;
- all current-main central plugin versions;
- current-main shared tests and source/generated facts.

It also stops and returns to Planner if the main repository version changes again before candidate reconciliation.

Therefore:

```text
VERSION_DRIFT_RECOVERY=PASS
```

## 3. Branch synchronization route

The exact task branch is already published and has diverged from current main.

The proposed recovery:

```text
same exact branch/worktree
-> git fetch origin main
-> optional fast-forward to the same remote task branch if needed
-> git merge origin/main
-> bounded conflict resolution
-> normal non-force exact-branch publication
```

is the smallest history-preserving route that does not rewrite the existing remote task history.

It explicitly forbids rebase, force push, successor branches, a second clone, remote remapping, destructive reset/clean/restore, and merging the task branch back into main.

Current Bridge Kit Host policy also requires dirty-tree ownership checks and bounded same-branch publication behavior. The Resume's authorization envelope is narrow enough for those existing rules to choose the canonical bounded publisher; it does not authorize a wider raw publication fallback.

Official Git documentation independently confirms that a true merge joins diverged histories with a merge commit rather than rewriting the existing branch history, and warns against beginning a merge with non-trivial uncommitted changes. The recovery's clean-worktree preflight is therefore appropriate.

```text
MAIN_SYNC_ROUTE=PASS
```

## 4. Conflict-resolution boundary

The ownership split is sufficient and not overbuilt.

Current main owns unrelated/shared state:

- workflow-core source/version/generated payload;
- central plugin versions;
- shared replay tests;
- current-main release history;
- unrelated main changes.

The Project Instructions Editor task owns its bounded addition:

- standalone Skill source;
- focused tests;
- standalone baseline entry;
- card/icon identity;
- generated registry/catalog/provenance identity;
- `5.5.0` candidate addition;
- task evidence history.

Generated conflicts are resolved source-first and regenerated with the current generator rather than by selecting a stale generated side.

This is enough to prevent both failure directions:

1. stale task state overwriting workflow-core `0.5`, `5.4.1`, or other current-main facts;
2. blindly taking main and dropping the Project Instructions Editor candidate.

No per-file conflict ledger is needed before a real conflict exists.

## 5. C2 and same-final-candidate contract

The recovery preserves the approved identity sequence:

```text
main synchronization
-> candidate-owned reconciliation
-> deterministic/full validation
-> FINAL_CANDIDATE_COMMIT=C2
-> install from C2
-> G1
-> G2
-> G3
-> G4 full packet
-> zip from C2
-> evidence-only commits
-> EVIDENCE_HEAD=E2
-> prove C2..E2 contains no candidate-owned changes
-> independent Reviewer
```

The old candidate is historical only. Old Gate PASS cannot be stitched into C2.

Any candidate-owned mutation after C2 still invalidates affected Gate evidence and requires a new candidate plus risk-matched rerun.

```text
C2_FORMATION_CONTRACT=PASS
```

## 6. R1 continuity

`R1=OPEN`.

The recovery does not weaken G4. The new public-safe G4 packet must preserve the full review surface, including:

- exact natural request;
- full live Project-setting baseline;
- targeted history;
- deletion/rejection evidence including the nightly-build deletion;
- exact budget/headroom;
- every canonical source;
- actual AGENTS.md content or exact safe copy plus stable identity;
- source hashes;
- fresh runtime/session identity;
- complete output and actual length;
- explicit non-independent self-check boundary.

Executor still cannot claim G4 PASS.

## 7. R2 continuity

`R2=OPEN`.

G1 must still test real normal-entry ownership with the relevant neighboring Skills actually discoverable.

The required families remain:

- ordinary Chinese prose -> `chinese-prose`;
- writing fidelity -> `writing-fidelity`;
- scientific structural rewrite -> `scientific-rewrite`;
- AI_Skills maintenance -> `ai-skills-core`;
- complex workflow/control -> `workflow-core`;
- generic agent/system prompt -> not the editor;
- global Custom Instructions -> not the editor.

Static trigger JSON, descriptions, or routing receipts still do not substitute for runtime routing evidence.

## 8. Capability taxonomy

No new capability risk was introduced by the synchronization recovery.

The four approved Gate families remain unchanged:

1. normal entry / routing boundary;
2. core Project editing semantics;
3. fidelity / authority / should-not-change;
4. representative complete task + qualitative final artifact.

No fifth Gate or new workflow layer is justified.

## 9. Authorization boundary

The Resume becomes authorization only when the user actually sends it to the Executor.

It authorizes only:

- the exact existing task branch/worktree;
- ordinary non-force main synchronization into that exact branch;
- bounded conflict resolution;
- candidate-owned reconciliation;
- deterministic/full tests;
- task-local install and fresh Codex Gate runs;
- public-safe evidence;
- portable package;
- task-owned commits;
- ordinary non-force exact-branch publication.

It does not authorize task-branch integration into main, release/tag/publication, paid review, private-data external transmission, live ChatGPT mutation, central Plugin redesign, Bridge Kit writes, rebase/force push, remote remapping, destructive Git, or new long-running control infrastructure.

No new branch/worktree authorization is needed because the Resume binds the already-authorized exact task identity.

## 10. Maintenance state

Issue #93 remains open with the expected labels:

- `maintenance-track`
- `kind:new-capability`
- `scope:standalone-skill`
- `area:standalone-skill`

The lifecycle remains `DOING`; the recovery is not completion.

Current expected Project state:

```text
Project = AI Skills Maintenance
Issue = #93
Status = DOING
Area = standalone-skill
current execution anchor =
docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_DEPENDENT_EXECUTION_RECOVERY_PLAN_V0_1_2026-10-02.md
```

No GitHub Project-field mutation surface is available in this Critic runtime, so this remains a pending mutation, not a synchronization claim.

The Issue reader-facing body is stale, but current runtime does not expose a verifiable installed Clear Writing invocation surface:

```text
CLEAR_WRITING_UNAVAILABLE
```

Therefore this review does not mutate the Issue body.

## 11. PASS boundary

This PASS approves only execution of the recovery Plan + exact Resume.

It does not mean:

- C2 already exists;
- Gates have rerun;
- R1 or R2 are closed;
- implementation overall is accepted;
- integration is approved;
- repository `5.5.0` is released.

Accordingly:

```text
CRITIC_RESULT=PASS
R3_SUPERSEDE_DECISION=PASS
VERSION_DRIFT_RECOVERY=PASS
MAIN_SYNC_ROUTE=PASS
C2_FORMATION_CONTRACT=PASS

R1=OPEN
R2=OPEN

APPROVED_RECOVERY_PLAN_PATH=docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_DEPENDENT_EXECUTION_RECOVERY_PLAN_V0_1_2026-10-02.md
APPROVED_RESUME_PATH=docs/operations/prompts/PROJECT_INSTRUCTIONS_EDITOR_DEPENDENT_EXECUTION_RESUME_V0_1.md
APPROVED_PACKAGE_COMMIT=0cc2abb061ab95655b95bc22846f3aef8877f40c

RECOVERY_EXECUTION_APPROVED=YES
READY_FOR_CODEX=YES
READY_FOR_GATES=NO
READY_FOR_INTEGRATION=NO
READY_FOR_RELEASE=NO
NEXT_HANDOFF=EXECUTOR
```
