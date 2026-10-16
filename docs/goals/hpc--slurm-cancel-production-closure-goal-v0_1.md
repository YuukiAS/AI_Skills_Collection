# Slurm protected-cancel production closure — Canonical Goal v0.1

Task: `hpc--slurm-cancel-production-closure`

Status: DRAFT / EXECUTION_NOT_AUTHORIZED

Authority:
- Stage A implementation: `acf8bf29681b404a3c107d25ade527ad1dfe0b89`
- Stage A Reviewer PASS: `results/hpc--slurm-cancel-human-confirmation/REVIEW_1.md`
- Production Plan: `docs/design/slurm-workflows/SLURM_WORKFLOWS_PRODUCTION_CLOSURE_PLAN_V0_1_2026-10-16.md`

This Goal must not be executed until an independent Critic gives execution-ready PASS for the exact package and the user sends the approved Kickoff.

## Product result

Finish the protected-cancellation feature through the normal production paths without claiming an unavailable hard OS isolation guarantee.

The final behavior must be:

- Longleaf private policy protects all jobs in partition `htzhulab`.
- Longleaf private policy separately protects every H100 job on any partition.
- Protected, old, or non-current-run jobs are never cancelled by the agent. The agent returns a short exact-target request; actual protected cancellation is performed only by the user from an independent terminal.
- Long Goal text, standing race opt-in, `auto_review`, Hook output, or model-generated confirmation cannot execute protected cancellation.
- Exact current-run unprotected jobs may still be cancelled automatically through the central safe-cancel entry.
- Raw `scancel` is forbidden in the current Longleaf_Codex Host Policy normal command path.
- DII/CARE known production cancellation paths use the same central safe-cancel entry and have no direct `scancel` fallback.
- The shipped claim is “normal production entry protection enabled”; do not claim arbitrary same-UID Python/Slurm API is OS-level unbypassable.

## Frozen repository identities

Central:
- repo: `YuukiAS/AI_Skills_Collection`
- source: exact Critic-approved package commit on `main`
- task branch: `reviewed/hpc--slurm-cancel-production-closure`
- R: `/overflow/htzhu/mingcheng_new/AI_Skills_Collection`
- W: `/overflow/htzhu/mingcheng_new/AI_Skills_Collection-hpc--slurm-cancel-production-closure`

DII candidate locator from prior user-provided Longleaf state:
- repo: `YuukiAS/Distributed_Imaging_Inference`
- expected R: `/users/a/e/aereinh/Distributed_Imaging_Inference`
- task branch: `reviewed/hpc--slurm-cancel-production-closure`
- expected W: `/users/a/e/aereinh/Distributed_Imaging_Inference-hpc--slurm-cancel-production-closure`

CARE candidate locator from prior user-provided Longleaf state:
- repo: `YuukiAS/CARE_Challenge`
- expected R: `/users/a/e/aereinh/CARE`
- task branch: `reviewed/hpc--slurm-cancel-production-closure`
- expected W: `/users/a/e/aereinh/CARE-hpc--slurm-cancel-production-closure`

Before any branch/worktree write in a consumer repo, verify the exact existing R, origin, clean state, current `origin/main`, absence of target branch/worktree, and repo identity. A mismatch stops only that consumer and prevents overall DONE.

## Phase 1 — build the cross-repo final candidate

### Central candidate

1. Create the exact AI Skills task branch/worktree from the Critic-approved `main` commit.
2. Selectively port Stage A product/test changes from `acf8bf29681b404a3c107d25ade527ad1dfe0b89`; do not import its Reviewed task control files. If the port conflicts semantically with current main, stop and return Planner.
3. Implement one small central safe-cancel executable/CLI inside existing `slurm-workflows`.
4. It must resolve exact target facts read-only, load the private policy, call the Stage A decision, then:
   - `ALLOW_OWNED_UNPROTECTED`: revalidate and internally run `scancel`, then read back state;
   - `REQUIRE_FRESH_HUMAN`: print the short exact-target request and execute nothing;
   - `DENY_UNKNOWN_OR_FORBIDDEN`: execute nothing.
5. There must be no production API that accepts model/chat confirmation and then executes a protected cancellation.
6. Preserve all existing routing/race/sticky/persistent/doctor behavior.

### DII

After read-only locator validation, use its exact task worktree.

- Update the repo-local installed slurm-workflows candidate to the same central final candidate.
- Update only the standing H100/A100 race cancellation semantics so loser cancellation uses central safe-cancel.
- If central decision requests fresh human confirmation, retain the loser and report/request; standing race opt-in is not cancellation approval.
- No change to training/scientific budget, GPU eligibility, data, model, or evaluation.

### CARE

After read-only locator validation, use its exact task worktree.

Replace direct `scancel` in the current reachable consumer paths with the central safe-cancel entry, preserving each watcher’s state machine and scientific semantics:

- `.agents/skills/slurm-routing-partition/SKILL.md`
- `scripts/route_B_round04/watch_B1_race.py`
- `scripts/evaluation/watch_care_srr_cascade_formal_race.py`
- `scripts/evaluation/watch_srr_v3_m7_routing.py`
- `scripts/evaluation/watch_srr_v3_m8_myops_race.py`
- `scripts/target_domain_gap_closure/monitor_interactive_takeover.py`

For `results/20260711_srr_v3_m10_complete_mechanism_repair/wave2_partition_race_watcher.py`:
- if a current normal entry can still execute it, adapt it;
- otherwise record it as historical/non-entry and ensure current prompts/scripts do not route to it.

No direct `scancel` fallback is permitted for a production consumer path.

## Phase 2 — isolated validation

Dangerous replay must not run on the Longleaf host.

Use an actually isolated container/VM/runner process with:
- no production SSH credentials/agent;
- no Longleaf/Slurm/MUNGE socket or config mount;
- no production repo write mount except explicit disposable test input;
- isolated PID namespace;
- no host control socket;
- network disabled for the dangerous replay;
- fake Slurm binaries/controller only.

Replay direct safe-cancel, absolute-path/raw-scancel rejection, Python/shell consumer invocation, arrays/batches, state changes, and holder-equivalent simulations only there.

If this isolation cannot be proven, skip dangerous replay and mark the corresponding evidence incomplete. Never substitute real Longleaf mutation.

## Phase 3 — independent implementation review

Freeze exact central/DII/CARE candidate commits and send the full diff, tests, isolation evidence, private-policy template behavior, Host Policy candidate rule, and consumer inventory to an independent Reviewer.

The Reviewer must PASS before production install.

Do not deploy while review is pending.

## Phase 4 — production deployment, authorized only by the approved Kickoff

After Reviewer PASS, the same user-approved Kickoff may continue without a new architectural round.

Longleaf only:

1. Back up current user-local AI Skills installation manifest/config and the current Longleaf_Codex Host Policy files that will be touched. Never print secrets.
2. Install the exact reviewed central candidate through the existing user-level AI Skills normal install path.
3. Read-only detect the real Longleaf cluster identity.
4. Update only that site section in `~/.config/ai-skills/local-overrides.toml`, preserving all unrelated fields:
   - `cancel_policy_version = "2026-10-16-v1"` unless Reviewer freezes a different exact value;
   - `cancel_policy_confirmed = true`;
   - `protected_partitions = "htzhulab"`;
   - `protected_accelerators = "H100"`.
5. Update only the current Longleaf_Codex Host Policy/rules:
   - raw `scancel` => `forbidden`;
   - confirmed host executable path `/usr/bin/scancel` must resolve to the same forbidden rule;
   - central safe-cancel entry remains permitted through its exact bounded executable;
   - normal read-only Slurm commands remain unchanged.
6. Do not deploy a production Hook unless already required by the existing Host Policy. Hook is not a completion dependency.
7. Run only read-only production validation:
   - execpolicy evaluation proves raw/absolute scancel forbidden;
   - installed skill identity equals reviewed candidate;
   - private policy readback contains the exact protected scope;
   - safe-cancel read-only/evaluation path returns `REQUIRE_FRESH_HUMAN` for a protected exact target if a suitable existing target can be inspected without mutation; otherwise use an offline exact-target fixture and do not invent a live test.
8. Never cancel, signal, requeue, suspend, release, kill a holder, or submit a test job for validation.

Consumer integration after central production identity is verified:
- integrate DII/CARE reviewed consumer branches by their normal non-force integration process;
- no real cancellation smoke.

## Phase 5 — release / closure

Only after central + Longleaf + DII + CARE evidence passes:

- `slurm-workflows`: 0.4 -> 0.5;
- Repository: PATCH from the actual release-time version; if still 5.4.4, release 5.4.5;
- central Marketplace Plugins: NO_BUMP;
- Bridge Kit: NO_CHANGE.

Check README/CHANGELOG/version according to repository policy. Do not claim hard same-UID unbypassability.

Maintenance item remains ADAPTING until all required consumers are integrated and production identity is verified.

## Capability gates

Keep the existing six gates only:

- G1: real policy / target identity and protection union.
- G2: protected normal entry never executes cancellation; independent-terminal human action is the only protected execution path.
- G3: isolated fake-Slurm dangerous replay + Longleaf raw scancel forbidden + consumers no direct fallback; still no hard same-UID claim.
- G4: state/target/policy revalidation.
- G5: normal Slurm behavior and DII/CARE workflows preserved.
- G6: exact final candidate, production installation identity, consumer commits, version/release truth and conservative claim.

## Stop conditions

Stop rather than expand scope if:
- central Stage A port conflicts semantically with current main;
- consumer root/remote/worktree identity is not exact;
- Host Policy cannot actually express/load `forbidden` for raw scancel;
- private override cannot be updated without preserving unrelated configuration;
- any reachable DII/CARE production path still directly calls scancel;
- isolated dangerous replay requires Longleaf credentials/network/host PID;
- deployment would require Slurm admin, new Unix identity, MUNGE changes, SSH key changes, daemon or Bridge Kit redesign.

## Explicitly forbidden

- real H100/htzhulab cancellation test;
- any real Slurm cancellation/requeue/suspend/release for validation;
- new allocation just to test this feature;
- production Hook redesign;
- Bridge Kit modification;
- paid API/model calls;
- new daemon/database/control service;
- silent fallback from forbidden raw scancel to another shell/Python/API form;
- automatic merge/release before independent Reviewer PASS.
