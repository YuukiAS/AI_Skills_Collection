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
- adapt the exact direct-cancel consumer paths listed in the Plan to safe-cancel;
- no direct `scancel` fallback;
- preserve existing scientific/routing state machines.

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

STOP after candidate publication.

Do not deploy or integrate main yet.

The user will supply an independent Reviewer result bound to the exact three candidate commits. Reviewer must inspect actual diffs, G1–G6 evidence, isolated replay evidence/limitations, raw-scancel Host Policy candidate, and consumer behavior.

If Reviewer is not PASS, only repair its bounded findings. No production deployment.

## Phase 4 — conditional production deployment after Reviewer PASS

This original user-approved Kickoff also authorizes the following actions **only after the user returns with a valid independent Reviewer PASS for the frozen candidate**. A new architecture approval is not required if scope is unchanged.

1. Back up only the Longleaf user-level AI Skills install/config and the current Longleaf_Codex Host Policy/rules files to be changed.
2. Integrate/release the exact reviewed central candidate according to repository policy:
   - slurm-workflows 0.4 -> 0.5;
   - repository PATCH from actual release-time version;
   - central Plugins NO_BUMP;
   - Bridge Kit NO_CHANGE.
3. Install exact released candidate through existing user-level AI Skills normal install path.
4. Read-only detect the real Longleaf cluster identity, then update only its section in `~/.config/ai-skills/local-overrides.toml`, preserving all unrelated content:
   - `cancel_policy_version = "2026-10-16-v1"`
   - `cancel_policy_confirmed = true`
   - `protected_partitions = "htzhulab"`
   - `protected_accelerators = "H100"`
5. Update only current Longleaf_Codex execpolicy/Host Policy so direct `scancel` and confirmed `/usr/bin/scancel` resolution are `forbidden`, while the exact central safe-cancel executable is permitted and existing read-only Slurm commands remain unchanged.
6. Do not deploy a new production Hook unless the existing configuration already requires it.
7. Run read-only production validation only:
   - raw scancel policy evaluation => forbidden;
   - absolute `/usr/bin/scancel` => forbidden;
   - installed skill identity => exact released candidate;
   - private policy readback => htzhulab + H100;
   - safe-cancel protected evaluation => REQUIRE_FRESH_HUMAN and no execution, using read-only real target facts only if safely available; otherwise use offline fixture.
8. Integrate DII/CARE exact reviewed consumer commits using normal non-force integration.
9. Verify current consumers contain no reachable direct `scancel` fallback.
10. Complete version/README/CHANGELOG/maintenance closure only after all above evidence is true.

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
