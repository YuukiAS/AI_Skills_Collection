# Slurm protected-cancel production closure — Kickoff Draft v0.1

Status: DRAFT / CRITIC_PENDING / DO_NOT_EXECUTE

If and only if an independent Critic gives execution-ready PASS for the exact current package and the user sends the approved text, this message authorizes the bounded actions below.

Task: `hpc--slurm-cancel-production-closure`

Authority:
- `docs/design/slurm-workflows/SLURM_WORKFLOWS_PRODUCTION_CLOSURE_PLAN_V0_1_2026-10-16.md`
- `docs/goals/hpc--slurm-cancel-production-closure-goal-v0_1.md`
- Stage A product commit `acf8bf29681b404a3c107d25ade527ad1dfe0b89`
- Stage A independent Reviewer PASS on `reviewed/hpc--slurm-cancel-human-confirmation`

Expected source identities at package freeze:
- AI Skills main: `APPROVED_COMMIT` from Critic
- DII main: `f5066f5760d707fa85bb326a5716c82026929c25`
- CARE main: `75a40e454de43b64e59a0b0b438ff57ef2bb8345`

Exact bounded branches/worktrees:
- AI Skills:
  - R=`/overflow/htzhu/mingcheng_new/AI_Skills_Collection`
  - branch=`work/hpc--slurm-cancel-production-closure`
  - W=`/overflow/htzhu/mingcheng_new/AI_Skills_Collection-hpc--slurm-cancel-production-closure`
- DII expected:
  - R=`/users/a/e/aereinh/Distributed_Imaging_Inference`
  - branch=`work/hpc--slurm-cancel-production-closure`
  - W=`/users/a/e/aereinh/Distributed_Imaging_Inference-hpc--slurm-cancel-production-closure`
- CARE expected:
  - R=`/users/a/e/aereinh/CARE`
  - branch=`work/hpc--slurm-cancel-production-closure`
  - W=`/users/a/e/aereinh/CARE-hpc--slurm-cancel-production-closure`

## Phase 0 — exact preflight and branch creation

Before writes, for all three repos read-only verify repo root, origin, clean state, source branch SHA, absence of the target branch/worktree and applicable AGENTS rules.

- AI Skills must have `origin/main == APPROVED_COMMIT`.
- DII must have `origin/main == f5066f5760d707fa85bb326a5716c82026929c25`.
- CARE must have `origin/main == 75a40e454de43b64e59a0b0b438ff57ef2bb8345`.

If any expected repo/source has advanced or the path/branch/worktree is occupied/dirty/ambiguous, STOP before creating that branch and report the exact mismatch. Do not absorb new source changes silently.

The user authorizes creation of exactly the three listed `work/hpc--slurm-cancel-production-closure` branches/worktrees and no other branch topology changes. No force/reset/clean/stash/rebase.

The same approved Kickoff also explicitly authorizes **one first remote publication per exact task branch** after its candidate commit is ready and before mandatory Reviewer handoff:

- from AI Skills exact W: one ordinary non-force `git push --set-upstream origin work/hpc--slurm-cancel-production-closure`;
- from DII exact W: the same command, only to that repo's `origin`;
- from CARE exact W: the same command, only to that repo's `origin`.

Each is authorized once solely to create the same-name remote candidate branch and bind upstream. Before each command, verify current repo/origin, exact branch, clean worktree, source lineage and that `origin/work/hpc--slurm-cancel-production-closure` does not already exist. If it exists, source has drifted, worktree is dirty, lineage differs, or another remote/branch would be affected, STOP. No other remote publication, branch, force/force-with-lease, delete, tag, history rewrite or remote mutation is authorized. After first publication, use the existing bounded current-branch publisher for subsequent ordinary same-branch updates.

## Phase 1 — build candidate only, no production deployment

AI Skills:
1. Port only these Stage A product/test paths from `acf8bf29681b404a3c107d25ade527ad1dfe0b89`:
   - `scripts/skills.py`
   - `skills/tools/hpc/slurm-workflows/SKILL.md`
   - `skills/tools/hpc/slurm-workflows/scripts/slurm_routing.py`
   - `tests/test_slurm_workflows.py`
   Do not import Stage A task control files/results as new production state.
2. Implement the Plan’s single safe-cancel normal entry.
3. Preserve existing Slurm behavior and all G1–G6 semantics.

DII:
- sync the exact central final candidate into the repo-local installed slurm-workflows path;
- update only standing race cancellation semantics to use safe-cancel;
- no direct protected cancellation.

CARE:
- adapt all current authority surfaces named in the Plan, including root `AGENTS.md`, the `status: AUTHORIZED` `prompts/tasks/20260801_care_target_domain_race_gap_closure_controller.md`, and its scheduling source `prompts/blueprints/CARE_target_domain_race_gap_closure_20260801.md`;
- adapt the exact reachable direct-cancel implementation paths listed in the Plan to safe-cancel;
- for `REQUIRE_FRESH_HUMAN`, retain the loser / queued lane and emit the short human request;
- no direct `scancel` fallback;
- do not alter model/loss/split, training budget, resource compatibility, lane order, interactive takeover order, candidate gates, atomic claims, or other scientific semantics;
- do not mechanically edit DRAFT prompts, historical result/command logs or provenance-only artifacts.

Do not modify Longleaf private config or Host Policy in Phase 1.

## Phase 2 — validation

Run deterministic local tests first.

Dangerous fake cancellation replay is allowed only inside a separately proven isolated process/container satisfying ER-02:
- network disabled;
- isolated PID namespace;
- no production SSH credentials/agent;
- no Slurm/MUNGE/controller/socket;
- no host control socket;
- no production writable mounts;
- fake Slurm only.

If no such environment is available, skip those dangerous simulations and report the exact evidence gap; never run them on Longleaf.

No real Slurm mutation, no H100/htzhulab test cancellation, no test allocation.

Freeze exact AI/DII/CARE candidate SHAs and produce a compact cross-repo evidence packet.

## Phase 3 — mandatory independent Reviewer wait

Before Reviewer handoff, use only the one-time same-name first-publication authority above for any exact task branch that still has no remote upstream. Publish the frozen candidate commits needed for review; publication itself does not authorize production deployment.

STOP after candidate publication.

Do not deploy or integrate main yet.

The user will supply an independent Reviewer result bound to the exact three candidate commits. Reviewer must inspect actual diffs, G1–G6 evidence, isolated replay evidence/limitations, raw-scancel Host Policy candidate, and consumer behavior.

If Reviewer is not PASS, only repair its bounded findings. No production deployment.

## Phase 4 — conditional production deployment after Reviewer PASS

This original user-approved Kickoff also authorizes the following actions **only after the user returns with a valid independent Reviewer PASS bound to the exact frozen central/DII/CARE candidate commits**. Do not bump or release versions yet.

1. Back up only the Longleaf user-level AI Skills install/config and current Longleaf_Codex Host Policy/rules files that will be changed. Never print secrets.
2. Deploy the **exact reviewed central candidate** through the existing user-level AI Skills normal install path while leaving repository/slurm-workflows version, README release claims and CHANGELOG release identity unchanged.
3. Read-only detect the real Longleaf cluster identity, then update only its section in `~/.config/ai-skills/local-overrides.toml`, preserving all unrelated content:
   - `cancel_policy_version = "2026-10-16-v1"`
   - `cancel_policy_confirmed = true`
   - `protected_partitions = "htzhulab"`
   - `protected_accelerators = "H100"`
4. Update only current Longleaf_Codex execpolicy/Host Policy so direct `scancel` and confirmed `/usr/bin/scancel` resolution are `forbidden`, while the exact central safe-cancel executable is permitted and existing read-only Slurm commands remain unchanged.
5. Do not deploy a new production Hook unless the existing configuration already requires it.
6. Run read-only production validation only:
   - raw scancel policy evaluation => forbidden;
   - absolute `/usr/bin/scancel` => forbidden;
   - installed central candidate identity => exact reviewed candidate;
   - private policy readback => htzhulab + H100;
   - safe-cancel protected evaluation => REQUIRE_FRESH_HUMAN and no execution, using bounded read-only real target facts only if safely available; otherwise use offline fixture.
7. Integrate the exact reviewed DII/CARE consumer commits using their normal non-force integration process and obtain normal-entry evidence that all current authority/consumer surfaces route cancellation through central safe-cancel with no reachable direct `scancel` fallback.
8. Assemble complete G1–G6 production evidence for the same behavior candidate.
9. If any product behavior, safe-cancel logic, consumer behavior, Host Policy behavior or protection mechanism changes after Reviewer PASS, STOP, freeze new candidate commits and obtain another independent Reviewer PASS before release. Do not hide behavior changes in release metadata.

Never cancel, signal, release, requeue, suspend, kill a real holder, or submit a test job for validation.

## Phase 5 — final release / maintenance closure

Only after Phase 4 proves Longleaf normal-entry protection, DII/CARE consumer integration and complete G1–G6 production evidence may release/version metadata change:

1. `slurm-workflows` 0.4 -> 0.5.
2. Repository -> next PATCH from the actual release-time version; if still 5.4.4, 5.4.5.
3. Central Marketplace Plugins remain NO_BUMP.
4. Bridge Kit remains NO_CHANGE.
5. Check/update README, CHANGELOG, generated/version surfaces and formal release identity according to repository policy.
6. This release closure must not change product behavior. Any behavior change routes back to independent Reviewer before release.

Maintenance lifecycle truth:
- current `docs/skill-todos/slurm-workflows.md` still has `tracking issue: PENDING_CLEAR_WRITING`; no real tracking Issue/Project state exists, so do not claim ADAPTING or DONE yet;
- if a real Clear Writing-capable AI Skills Maintainer is available, first invoke it on Issue copy, create a dedicated maintenance Issue (do not reuse #96), write real `tracking: #N`, set first substantive tracked execution to DOING, then ADAPTING only when central is complete and required Longleaf/DII/CARE consumers remain;
- DONE requires all central/Longleaf/DII/CARE evidence, durable Resolution commit and actual Issue close;
- if Clear Writing is still unavailable, do not fabricate Issue/Project status. Record the exact pending mutation for the next capable maintainer; do not ask the user to maintain it manually.

## Permanent prohibitions for this Kickoff

- Never actually cancel, signal, release, requeue, suspend or kill any real Slurm job/allocation for testing.
- Never touch an existing H100/htzhulab allocation except bounded read-only inspection.
- Never submit a new Slurm job just to test this feature.
- No Slurm admin/MUNGE/Unix identity/SSH key changes.
- No Bridge Kit modification.
- No new daemon/database/broker/control plane.
- No paid model/API call.
- No raw `git push -f`, force, reset/clean, arbitrary branch creation, or silent source drift.
- No fallback from forbidden `scancel` to Python/SSH/API direct cancellation.
- Do not claim hard same-UID unbypassability.

If any required step needs an authority or side effect outside this exact envelope, STOP and return to Planner.
