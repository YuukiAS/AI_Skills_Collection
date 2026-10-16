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

This closure does not create another Reviewed Handoff task. It uses exact user-authorized bounded `work/...` branches, then an independent Reviewer before production deployment.

Central:
- repo: `YuukiAS/AI_Skills_Collection`
- source: exact Critic-approved package commit on `main`
- task branch: `work/hpc--slurm-cancel-production-closure`
- R: `/overflow/htzhu/mingcheng_new/AI_Skills_Collection`
- W: `/overflow/htzhu/mingcheng_new/AI_Skills_Collection-hpc--slurm-cancel-production-closure`

DII candidate locator from prior user-provided Longleaf state:
- repo: `YuukiAS/Distributed_Imaging_Inference`
- expected R: `/users/a/e/aereinh/Distributed_Imaging_Inference`
- task branch: `work/hpc--slurm-cancel-production-closure`
- expected W: `/users/a/e/aereinh/Distributed_Imaging_Inference-hpc--slurm-cancel-production-closure`

CARE candidate locator from prior user-provided Longleaf state:
- repo: `YuukiAS/CARE_Challenge`
- expected R: `/users/a/e/aereinh/CARE`
- task branch: `work/hpc--slurm-cancel-production-closure`
- expected W: `/users/a/e/aereinh/CARE-hpc--slurm-cancel-production-closure`

Before any branch/worktree write in a consumer repo, verify the exact existing R, origin, clean state, current `origin/main`, absence of target branch/worktree, and repo identity. A mismatch stops only that consumer and prevents overall DONE.

### First remote publication authority

The three `work/hpc--slurm-cancel-production-closure` branches are new and therefore do not yet have same-name upstream branches. The normal bounded current-branch publisher does not create a first upstream.

Only when the user sends the exact Critic-approved Kickoff, the Executor is authorized once per repository to publish the **exact current task branch** non-force to the same-name branch on `origin` and bind that upstream, solely for candidate / independent Reviewer handoff.

Before that first publication, re-check repo/origin, source lineage, clean worktree, exact branch, and that the same-name remote branch does not exist. Existing remote branch, source drift, dirty state, lineage mismatch or a different remote must fail closed. No other branch/remote, force, force-with-lease, delete, tag, history rewrite or remote mutation is authorized. After the first publication succeeds, later ordinary same-branch publication must use the existing bounded current-branch publisher.

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

The current cancellation contract is authoritative in **three additional active surfaces** and all three must be adapted:

- root `AGENTS.md`: current routing-race rule requires cancelling the still-pending mirror when a compatible route starts;
- `prompts/tasks/20260801_care_target_domain_race_gap_closure_controller.md`: current `status: AUTHORIZED` task, including its pending-lane cancellation contract;
- `prompts/blueprints/CARE_target_domain_race_gap_closure_20260801.md`: scheduling-contract source for that authorized task, including interactive takeover cancellation.

For those three authority surfaces, change only cancellation routing: direct cancellation becomes central safe-cancel. If central decision is `REQUIRE_FRESH_HUMAN`, retain the loser / queued lane and produce the short human request. Do **not** change model/loss/split, training budget, resource compatibility, lane order, interactive takeover order, candidate gates, atomic claims, or other scientific semantics.

Also replace direct `scancel` in the current reachable implementation paths:

- `.agents/skills/slurm-routing-partition/SKILL.md`
- `scripts/route_B_round04/watch_B1_race.py`
- `scripts/evaluation/watch_care_srr_cascade_formal_race.py`
- `scripts/evaluation/watch_srr_v3_m7_routing.py`
- `scripts/evaluation/watch_srr_v3_m8_myops_race.py`
- `scripts/target_domain_gap_closure/monitor_interactive_takeover.py`

For `results/20260711_srr_v3_m10_complete_mechanism_repair/wave2_partition_race_watcher.py`:
- if a current normal entry can still execute it, adapt it;
- otherwise record it as historical/non-entry and ensure current authoritative prompts/scripts do not route to it.

Do not mechanically edit DRAFT prompts, historical result/command logs, or provenance-only artifacts. No direct `scancel` fallback is permitted for a current production consumer path.

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

Before Reviewer handoff, use the user-authorized one-time same-name first-publication authority for each exact task branch if its remote branch is still absent. Publish only the candidate commits needed for review; no production deployment follows from publication.

Freeze exact central/DII/CARE candidate commits and send the full diff, tests, isolation evidence, private-policy template behavior, Host Policy candidate rule, and consumer inventory to an independent Reviewer.

The Reviewer must PASS before production install.

Do not deploy while review is pending.

## Phase 4 — conditional production deployment after Reviewer PASS

This original user-approved Kickoff authorizes the following actions **only after the user returns with a valid independent Reviewer PASS bound to the frozen central/DII/CARE candidate commits**. Do not release or bump versions yet.

1. Back up only the Longleaf user-local AI Skills install/config and the current Longleaf_Codex Host Policy/rules files that will be changed. Never print secrets.
2. Deploy the **exact reviewed central candidate** through the existing user-level AI Skills normal install path **without changing repository version, slurm-workflows version, README release claims or CHANGELOG release identity**.
3. Read-only detect the real Longleaf cluster identity.
4. Update only that site section in `~/.config/ai-skills/local-overrides.toml`, preserving all unrelated fields:
   - `cancel_policy_version = "2026-10-16-v1"` unless the reviewed candidate freezes a different exact value;
   - `cancel_policy_confirmed = true`;
   - `protected_partitions = "htzhulab"`;
   - `protected_accelerators = "H100"`.
5. Update only the current Longleaf_Codex Host Policy/rules:
   - raw `scancel` => `forbidden`;
   - confirmed host executable path `/usr/bin/scancel` resolves to the same forbidden decision;
   - central safe-cancel entry remains permitted through its exact bounded executable;
   - normal read-only Slurm commands remain unchanged.
6. Do not deploy a production Hook unless already required by the existing Host Policy. Hook is not a completion dependency.
7. Run only read-only Longleaf production validation:
   - raw / absolute scancel policy evaluation => forbidden;
   - installed central candidate identity => exact Reviewer-approved commit;
   - private policy readback => `htzhulab` + H100;
   - safe-cancel protected evaluation => `REQUIRE_FRESH_HUMAN` and no execution, using safe read-only real target facts only when appropriate, otherwise an offline exact-target fixture.
8. Integrate the exact reviewed DII and CARE consumer commits through their normal non-force integration path and obtain normal-entry evidence that they use central safe-cancel and have no reachable direct `scancel` fallback.
9. Re-run / assemble the complete production G1–G6 evidence on the same product behavior candidate.
10. If any product behavior, safe-cancel logic, consumer behavior, Host Policy behavior or protection mechanism changes after the independent Reviewer PASS, freeze new candidate commits and obtain a new independent Reviewer PASS before continuing. Release metadata may not hide behavior changes.

Never cancel, signal, requeue, suspend, release, kill a holder, or submit a test job for validation.

## Phase 5 — final version / release closure

Only after Phase 4 has established Longleaf normal-entry protection, DII/CARE consumer integration, and complete G1–G6 production evidence may release metadata advance:

- `slurm-workflows`: 0.4 -> 0.5;
- Repository: next PATCH from the actual release-time version; if still 5.4.4, release 5.4.5;
- central Marketplace Plugins: NO_BUMP;
- Bridge Kit: NO_CHANGE.

Then check/update README, CHANGELOG, generated/version surfaces and formal release identity according to repository policy. This final release closure must not introduce product behavior changes; if it does, return to Reviewer before release.

Do not claim hard same-UID unbypassability.

## Maintenance lifecycle truth

Current canonical source still says `tracking issue: PENDING_CLEAR_WRITING`. There is no real dedicated tracking Issue and the Project lifecycle has **not** been synchronized; therefore this task is not truthfully ADAPTING or DONE yet.

When a real Clear Writing-capable AI Skills Maintainer is available:

1. invoke Clear Writing on the reader-facing Issue copy;
2. create a dedicated maintenance Issue “防止 AI 未经本人确认取消受保护 Slurm 作业”; do not reuse closed #96;
3. apply the then-current maintenance taxonomy, with `maintenance-track`, regression semantics, and cross-repo / standalone-skill ownership consistent with the current board;
4. replace the pending source text with the real durable `tracking: #N`;
5. set the first substantive tracked execution to DOING with this production Plan/Goal/Kickoff and exact task branches as current anchor;
6. move to ADAPTING only when central production implementation is complete while required Longleaf/DII/CARE consumers remain pending;
7. move to DONE only after central + Longleaf + DII + CARE all pass, durable evidence and Resolution commit exist, and the tracking Issue is actually closed.

If Clear Writing is still unavailable at technical closure, do not invent an Issue or Project DONE. Emit this exact pending mutation for the next capable maintainer; the user is not required to maintain the board manually.

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
