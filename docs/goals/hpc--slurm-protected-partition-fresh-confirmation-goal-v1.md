# Slurm protected-partition fresh-confirmation — Canonical Goal v1

Task: hpc--slurm-cancel-production-closure

Status: EXECUTION_PACKAGE / AUTHORIZED_ONLY_AFTER_CRITIC_PASS_AND_USER_SEND / PHASE_0_TO_3_ONLY

Architecture authority:
- docs/design/slurm-workflows/SLURM_PROTECTED_PARTITION_FRESH_CONFIRMATION_PROPOSAL_V1_2026-10-17.md
- Proposal commit 12fd741a7fb8290ec53027db206fddc5df11fb21
- Proposal blob eddcf4881020518841730e77e8db85b591513a79

Execution authority:
- docs/design/slurm-workflows/SLURM_PROTECTED_PARTITION_FRESH_CONFIRMATION_EXECUTION_PLAN_V1_2026-10-17.md
- execution-package revision base main: 06648df4f2951766c257e19ee035e141a8a1ceb3
- Repository version baseline: 5.4.5
- Next execution-ready Critic must bind APPROVED_COMMIT to the final package commit. Critic PASS alone does not execute anything; Phase 0–3 is authorized only when the user subsequently sends the exact approved Kickoff.

## 1. Product result

Deliver one small protected-partition cancellation guard.

Longleaf private protection:
protected_cancel_partitions = ["htzhulab"]

Required behavior:

- Non-protected exact jobs receive no new protected-partition confirmation requirement. Existing Goal / Host Policy authorization semantics stay unchanged.
- A protected exact job is never cancelled on the first attempt.
- First protected attempt resolves exact JobId / Partition read-only and creates a fresh one-time challenge.
- Current deployable human confirmation is an independent user-shell command.
- The confirmation command only confirms; it never performs Slurm mutation.
- The next ordinary scancel attempt re-resolves JobId / Partition, atomically consumes the matching confirmation once, then performs exact /usr/bin/scancel.
- Replayed, expired, changed-target or changed-Partition confirmation is rejected.
- Initial Goal text, standing race opt-in, auto_review, model output and Hook output cannot confirm a protected cancellation.

Do not implement:
- H100 or accelerator protection;
- current-run ownership;
- owned-job-id;
- three-state safe-cancel architecture;
- confirmation receipt as long-lived authority;
- consumer-specific protected logic;
- database / daemon / broker / approval service;
- fifth Capability Gate.

## 2. Exact execution identities

Central AI Skills:
- base: exact execution-ready Critic APPROVED_COMMIT
- R=/overflow/htzhu/mingcheng_new/AI_Skills_Collection
- branch=work/hpc--slurm-protected-partition-fresh-confirmation
- W=/overflow/htzhu/mingcheng_new/AI_Skills_Collection-hpc--slurm-protected-partition-fresh-confirmation

DII:
- base=747829b957b19e8fcffa6bd5f1bb7ae62ae11f6f
- R=/users/a/e/aereinh/Distributed_Imaging_Inference
- branch=work/hpc--slurm-protected-partition-fresh-confirmation
- W=/users/a/e/aereinh/Distributed_Imaging_Inference-hpc--slurm-protected-partition-fresh-confirmation

CARE:
- base=75a40e454de43b64e59a0b0b438ff57ef2bb8345
- R=/users/a/e/aereinh/CARE
- branch=work/hpc--slurm-protected-partition-fresh-confirmation
- W=/users/a/e/aereinh/CARE-hpc--slurm-protected-partition-fresh-confirmation

Bridge source reference:
- main last verified=a03742ed07d00d36e3436f64a17e92c40a51064e
- repository mutation=FORBIDDEN

The old work/hpc--slurm-cancel-production-closure branches are rejected historical candidates and must not be reused.

Before branch creation, verify exact repo/origin/clean/source/target-branch/target-worktree. Any mismatch stops that repository.

## 3. Central implementation

### 3.1 Guard

Implement ai-slurm-scancel inside existing slurm-workflows.

Supported input:
- one exact normal JobId;
- explicit list of exact normal JobIds;
- exact array element only when unique read-only resolution is proven.

Reject:
- array parent/range;
- heterogeneous leader/component;
- job step;
- dynamic selectors such as --user / --partition / --name / --state;
- federation/cluster-switching;
- non-default signal/batch/full mutations.

Resolution:
- scontrol show job -o exact-id primary;
- optional bounded squeue cross-check;
- resolve current state + Partition / candidate Partition set;
- one protected target makes the whole explicit group protected;
- repeat resolution immediately before mutation;
- clear SCANCEL_* before exact /usr/bin/scancel.

### 3.2 Challenge state

Implement minimal user-private local files:
- random 128-bit challenge;
- exact target list;
- resolved partition set;
- operation;
- create/expiry times;
- pending / confirmed / consumed.

Use safe file permissions and atomic state transitions. No database.

### 3.3 Human confirmer

Implement ai-slurm-confirm-cancel.

Input must include exact challenge state file and challenge value.

It may only:
pending -> confirmed.

It must never run scancel.

### 3.4 Private config

Extend existing local override with exactly:
protected_cancel_partitions

Do not keep the rejected protected_accelerators / current-run policy as production semantics.

### 3.5 Automation shim

Provide a reviewed automation-only scancel shim that execs ai-slurm-scancel.

Do not replace /usr/bin/scancel.
Do not put the shim into the user's ordinary interactive shell PATH globally.

## 4. Consumer adaptation

### DII

- install/sync exact central candidate;
- prove actual automation launcher resolves scancel to reviewed shim;
- modify only launcher / executable resolution if necessary;
- no protected-partition/challenge/confirmation logic in DII;
- no current-run/three-state old candidate semantics.

### CARE

All current automation cancellation continues to express ordinary scancel intent and must resolve to the guard.

Outcome contract:
- returncode 0 => actual real scancel invocation succeeded;
- nonzero => cancellation did not successfully execute; retain target and continue the existing monitoring/retry path.

Apply exact minimal control-flow fixes:

B1:
- add to cancelled only on returncode 0;
- nonzero keeps target eligible for next existing while poll.

M7:
- return 0 only on cancel returncode 0;
- nonzero continues existing for-loop.

M8:
- exit only on code 0;
- nonzero continues existing check loop.

interactive takeover:
- enter sacct CANCELLED wait / launch only on cancel returncode 0;
- nonzero returns to existing outer poll.

cascade formal race:
- preserve current interval re-entry;
- nonzero must not be logged as successful cancellation.

Consumers must not parse challenge, Partition protection or confirmation.

If new source scanning reveals absolute /usr/bin/scancel, SSH scancel or Slurm API cancel, stop and return Planner rather than inventing another adapter.

## 5. Host Policy candidate, no production install yet

Bridge Kit source stays unchanged.

Candidate production rule is a separate user-layer Codex rules file:
$CODEX_HOME/rules/slurm-protected-cancel.rules

It must forbid Codex normal entry:
- scancel
- /usr/bin/scancel
- exact ai-slurm-confirm-cancel executable

It must recommend ai-slurm-scancel as the safe path.

Do not blanket-allow ai-slurm-scancel; existing Goal / approval semantics still govern unprotected cancellation.

Longleaf currently has two persistent Codex config homes that must be reverified before production:
- /users/a/e/aereinh/.codex
- /overflow/htzhu/mingcheng_new/.codex

Full Longleaf normal-entry claim requires the same reviewed rule in all currently active Longleaf Codex config layers.

This candidate is only built/tested in implementation. The Implementation Kickoff does not authorize writing either production CODEX_HOME.

## 6. PreToolUse

Optional auxiliary only.

Do not make Hook necessary for Gate PASS.
Do not use Hook as human confirmer.
Do not claim it catches Python subprocess scancel.
Do not deploy production Hook in this Goal unless a later production authorization explicitly includes it; default is no production Hook.

## 7. Capability Gate A-D

Gate A — protected partition routing:
- non-protected exact job keeps normal cancellation path;
- htzhulab first attempt cannot mutate;
- multi-partition candidate containing htzhulab is protected;
- long initial blanket authorization cannot skip first block.

Gate B — fresh human:
- only independent shell confirmer can change pending -> confirmed;
- confirmer itself cannot cancel;
- auto_review/model text/Hook cannot confirm;
- unconfirmed retries remain non-mutating;
- confirmed next retry executes at most once;
- replay/expiry/target/Partition/operation mismatch rejects.

Gate C — normal entry and consumers:
- raw / absolute scancel candidate rules are forbidden;
- confirmer is forbidden to Codex normal entry;
- user ordinary /usr/bin/scancel remains available;
- every required DII/CARE automation consumer resolves reviewed shim;
- B1/M7/M8/takeover obey nonzero re-entry;
- cascade retains interval re-entry;
- no current reachable absolute/SSH/API bypass.

Gate D — target integrity and claim:
- explicit multiple IDs are evaluated as one set;
- complex selectors fail closed;
- target is re-resolved before mutation;
- dangerous mutation replay only isolated fake Slurm;
- production Longleaf validation later is read-only;
- never claim same-UID OS-level unbypassability.

Do not add a fifth Gate or reuse rejected three-state G1-G6 as final proof.

## 8. Testing

Ordinary deterministic tests may cover:
- parser;
- challenge state machine;
- local config;
- consumer return-code behavior;
- execpolicy candidate matching;
- fake read-only Slurm fixtures.

Any test that really invokes fake scancel/subprocess mutation path requires an isolated environment with:
- network disabled;
- isolated PID namespace;
- no production credentials;
- no real Slurm/MUNGE/controller/socket;
- no host control socket;
- no production writable mount;
- fake Slurm only.

If unavailable, mark those destructive replays BLOCKED_BY_ISOLATION. Do not use Longleaf.

Never cancel a real htzhulab/H100/other Slurm job for this task.

## 9. Candidate publication and independent review

After central + DII + CARE candidate implementation and tests:

1. freeze exact commit in each repo;
2. perform at most one user-authorized same-name non-force first push for each new task branch if remote is absent;
3. create evidence under the central task result path;
4. stop for independent Reviewer.

Reviewer must inspect Proposal, Plan, Goal, three repo diffs, Gate A-D, isolation evidence, candidate rules/private config, rollback, and old-candidate non-reuse.

No production deployment before Reviewer PASS.

## 10. Production activation is a second, short authorization

This Goal defines but does not itself authorize production activation.

After exact Reviewer PASS, Planner/user gets a short production action request bound to exact candidate commits. Only that later authorization may permit:

- backups of task-owned user-local production files;
- exact reviewed central install;
- protected_cancel_partitions=["htzhulab"] in the actual Longleaf local override(s);
- slurm-protected-cancel.rules in each actual active Longleaf CODEX_HOME;
- reviewed automation PATH shim deployment;
- read-only production validation;
- exact reviewed DII/CARE integration after central normal-entry validation.

No production authorization may include real cancellation testing.

Existing running Codex process/session that does not reload new rules is not covered by the protection claim. Do not kill app-server/session automatically; validate using a fresh process/session and report stale sessions explicitly.

## 11. Rollback

Before production activation, capture backup/hash of only changed user-local files.

Rollback restores:
- previous central installed candidate;
- previous local override;
- previous additional slurm-protected-cancel.rules state;
- previous automation launcher/PATH state.

Rollback must not mutate Slurm, kill holders, alter MUNGE/SSH/Unix identities, run ai-bridge host install, or change Bridge source.

## 12. Version and release

Implementation candidate:
- Repository NO_BUMP
- slurm-workflows NO_BUMP
- central Plugins NO_BUMP
- Bridge Kit NO_CHANGE

After reviewed production activation + DII/CARE integration + complete Gate A-D:
- slurm-workflows 0.4 -> 0.5
- Repository release-time next PATCH; if the actual release-time version is still 5.4.5, the next PATCH is 5.4.6
- central Plugins NO_BUMP
- Bridge Kit NO_CHANGE
- README/CHANGELOG/version/generated release closure last

Release metadata cannot change behavior. Behavior change after Reviewer requires another independent review.

## 13. Maintenance truth

Current source remains PENDING_CLEAR_WRITING.

Do not invent a tracking Issue/Project state.

Next real Clear Writing + Project-capable Maintainer:
- create dedicated Issue, not #96;
- write real tracking: #N;
- first tracked execution -> DOING;
- central complete / required consumers pending -> ADAPTING;
- all required consumer evidence + Resolution commit + Issue close -> DONE.

If unavailable at technical closure, emit exact pending mutation; user does not manually maintain the board.

## 14. Forbidden

- deploy rejected old Phase 3 product candidate;
- cherry-pick/merge rejected candidates as new implementation;
- H100 protection or ownership logic;
- daemon/database/broker/control service;
- real Slurm cancellation/requeue/signal/release test;
- real htzhulab cancellation test;
- new Slurm allocation for testing;
- Bridge Kit source change;
- production Host Policy/private config write before separate production authorization;
- production Hook deployment by default;
- paid model/API call;
- force/history rewrite/remote deletion;
- fifth Capability Gate;
- same-UID hard-isolation claim.
