# Slurm Workflows Routing Refactor — Critic Review v0.2

日期：2026-09-24  
角色：AI Research Stack Independent Critic  
审查阶段：PRE_IMPLEMENTATION_DESIGN_RECHECK

## Active Review Context

- target_repo: `YuukiAS/AI_Skills_Collection`
- target_plugin_or_domain: standalone Skill / HPC / `slurm-workflows`
- design_topic_or_task_key: `hpc--slurm-workflows-routing-refactor`
- source_branch_or_ref: `main@b1d516c173ce838fd5eb9f39ae0a117bcb7f517e`
- proposal_path_and_version: `docs/design/slurm-workflows/SLURM_WORKFLOWS_ROUTING_REFACTOR_PROPOSAL_V0_2_2026-09-24.md` / v0.2
- proposal_commit: `b1d516c173ce838fd5eb9f39ae0a117bcb7f517e`
- previous_proposal: `docs/design/slurm-workflows/SLURM_WORKFLOWS_ROUTING_REFACTOR_PROPOSAL_V0_1_2026-09-24.md` @ `14158d1f11f8b005c40d0e943dddffbe2052a76c`
- previous_critic_review: `docs/design/slurm-workflows/SLURM_WORKFLOWS_ROUTING_REFACTOR_CRITIC_REVIEW_V0_1_2026-09-24.md` @ `723c7097004df7def7d739b0e8b1a037ad3fe950`
- review_stage: `PRE_IMPLEMENTATION_DESIGN_RECHECK`
- execution_branch/worktree: none

Preflight: current `main` is exactly `b1d516c173ce838fd5eb9f39ae0a117bcb7f517e`; there is no post-v0.2 main drift to assess.

## Result

```text
RESULT = PASS
SWR-B1 = CLOSED
SWR-B2 = CLOSED
```

```text
PASS_OBJECT =
SLURM_WORKFLOWS_ROUTING_REFACTOR_PROPOSAL_V0_2

PASS_SCOPE =
pre-implementation architecture/design only; not execution authorization
```

This PASS closes only the architecture/design review for Proposal v0.2. It does not authorize production changes, real Slurm submission/hold/update/cancel operations, an execution branch/worktree, an Executor, paid API use, release, or merge of future production changes.

---

## Closure of previous blockers

### SWR-B1 = CLOSED — pending widening JobId / dependency / running-transition safety

v0.2 closes the original causal risk without introducing a dependency-remapping system or new scheduler state machine.

The approved contract is now:

1. In-place `Partition` widening is preferred because it can preserve the existing JobId.
2. It is only enabled automatically for a job class after a real target-site probe has confirmed the relevant update behavior.
3. cancel + resubmit is limited to a narrowly defined **replaceable pending job** created by the current routing invocation, whose JobId has not become an external/workflow contract, has no downstream dependency already pointing to it, is not an identity-sensitive array/dependency workflow, and has no other JobId-preservation requirement.
4. Pre-existing jobs fail closed as identity-sensitive unless direct evidence proves they are replaceable.
5. Replacement must use a state-safe cancellation path, with target-site/version-confirmed `scancel --state=PENDING <JobId>` preferred, or an already validated hold -> recheck -> cancel equivalent.
6. A replacement is submitted only after the old job is confirmed no longer active.
7. If the job becomes RUNNING/CONFIGURING, or cancellation outcome is uncertain, widening stops; the running workload is not killed and no replacement is submitted.
8. Identity-sensitive jobs that cannot widen safely in place are not auto cancel+resubmitted.
9. G3/G5 now include downstream dependency, array/dependency identity, and PENDING -> RUNNING negative cases.

Independent SchedMD recheck supports this contract:

- `scontrol hold` prevents a pending job from starting; attempting to hold a running job does not suspend or cancel it.
- SchedMD documents that an existing job's partition(s) can be updated with `scontrol update JobId=<jobid> Partition=<partition(s)>`, while partition/QOS/reservation changes belong to the pending-job path.
- `sbatch --dependency` binds dependency conditions to job IDs, and a dependency that has failed due to a predecessor termination state does not later recover merely because that predecessor is requeued.
- Job arrays have explicit `ArrayJobID` / `ArrayTaskID` identity and dependency semantics.
- `scancel --state=PENDING` restricts cancellation to jobs that are in PENDING state.

These facts are enough to support the fail-closed design. The Proposal correctly does **not** infer from generic Slurm documentation that Longleaf already supports every desired in-place multi-partition update; that remains a target-site probe before production use.

### SWR-B2 = CLOSED — duplicate race site authority

v0.2 now uses a fail-closed authority boundary:

- explicitly forbidden -> duplicate race prohibited;
- explicitly allowed with user opt-in -> duplicate race may be enabled only after user/local opt-in;
- unknown / disabled-by-default / missing -> duplicate race prohibited.

Current Longleaf and CUHK profiles remain `race_execution = disabled_by_default`. v0.2 explicitly refuses to reinterpret those values as “allowed if the user opts in.” A local `duplicate_race_opt_in=true` therefore cannot create duplicate submissions on either current profile.

Single-job multi-partition remains separate because it is one Slurm job, not a duplicate-job race.

This closes the original authority escalation risk without requiring new site-policy infrastructure.

---

## Independent source and Slurm review

### Repository source re-read

Current latest main was re-read for:

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md`
- Proposal v0.2
- Proposal v0.1
- previous Critic review v0.1
- `skills/tools/hpc/slurm-workflows/SKILL.md`
- relevant `scripts/skills.py` environment/template/doctor/generated-reference paths
- `site-profiles/unc-longleaf.json`
- `site-profiles/cuhk-central-cluster.json`
- `site-profiles/local-overrides.example.toml`
- `docs/LOCAL_CONFIGURATION.md`
- `schemas/site-profile.schema.json`
- relevant `tests/test_skill_update.py`
- `VERSION` and current standalone Skill version for version-boundary confirmation

Current production source is still unchanged from the design baseline: generic `environment_blank_site_override()` still contains Longleaf-specific partition defaults, generated references still omit public site policy, doctor still uses global required fields, and current site profiles remain `disabled_by_default`. These are therefore still real implementation targets rather than already-fixed assumptions.

### External SchedMD sources checked

Checked on 2026-09-24:

1. SchedMD — `scontrol`  
   https://slurm.schedmd.com/scontrol.html  
   Relevant result: hold semantics; user/job update boundaries.

2. SchedMD — `sbatch`  
   https://slurm.schedmd.com/sbatch.html  
   Relevant result: dependency binds to JobId and failed dependency semantics remain identity-sensitive.

3. SchedMD — Job Array Support  
   https://slurm.schedmd.com/job_array.html  
   Relevant result: `ArrayJobID` / `ArrayTaskID` identity and array dependency semantics.

4. SchedMD — `scancel`  
   https://slurm.schedmd.com/scancel.html  
   Relevant result: `--state=PENDING` is an explicit cancellation state filter; array cancellation semantics are distinct.

5. SchedMD — FAQ / Managing Jobs  
   https://slurm.schedmd.com/faq.html  
   Relevant result: existing job partition(s) can be updated; partition/QOS/reservation changes are pending-job operations.

No official source requires using any of these mechanisms on Longleaf merely because Slurm supports them generally. v0.2 correctly keeps site-specific in-place widening behind a real target-site probe.

---

## Non-blocking items from v0.1 review

All previous non-blocking items were absorbed sufficiently:

- Multi-partition is now described as Slurm-native widening, **not** a latency guarantee.
- Unparseable `sbatch --test-only` fails closed instead of guessing route delay.
- Doctor requiredness is explicitly derived from public site hard constraints rather than a global guessed field list.
- G2/G3 require the installed Skill normal entry to consume the generated site reference for core routing branches.
- No daemon, watcher, database, scheduler score service, or new control plane is introduced.
- Resource-feasibility preflight, pending-reason-aware routing, restartability/preemption-aware routing, and deadline-aware routing are explicitly future-only NON_GOALS.

These future ideas should remain outside the current implementation unless later direct evidence justifies a separate design round.

---

## Complexity check

### Is v0.2 too complex?

No.

The implementation architecture remains four existing layers/objects:

```text
generic Skill
+ site authority / hard constraints
+ local preference
+ generated site reference
```

The revision does not add a service, persistent watcher, database, dependency graph, remapping engine, scheduler predictor, or second state machine. The additional safety contract is conditional logic around a real destructive boundary that already exists: whether a pending job may be replaced.

The simplification from v0.1 is also material: the free-form `routing_strategy` proposal is removed; duplicate-race permission is not inferred; and duplicate fallback may remain disabled without blocking the core release.

### Has v0.2 become too simple or unsafe?

No.

The previously missing safety boundaries are now explicit: JobId preservation, array/dependency identity, PENDING -> RUNNING transition protection, old-job-state confirmation before replacement, and fail-closed site authority. These close the concrete execution risks identified in v0.1 without requiring the future routing capabilities listed as NON_GOALS.

---

## Capability Gate Matrix review

The revised G1–G6 matrix is sufficient and not overbuilt.

- **G1** proves site isolation and site-authority propagation into the installed reference.
- **G2** proves ordered preference through the installed normal entry, including probe parse failure.
- **G3** proves native widening and JobId safety, including downstream dependency, array/dependency identity, and RUNNING-transition negative cases.
- **G4** proves duplicate-race authority/isolation only if that optional fallback is actually implemented. If duplicate fallback remains disabled, G4 may remain NOT_APPLICABLE / disabled capability rather than forcing implementation.
- **G5** proves bounded monitoring and, critically, that uncertain old-job state cannot create a replacement submission.
- **G6** proves final production identity: environment apply -> installed Skill/generated reference -> normal routing invocation.

No additional gate is required for this design stage. The matrix already covers the distinct high-risk capabilities, normal installed entry, should-not-change cases, site isolation, and final-candidate identity.

---

## Version and scope review

Current source confirms:

- Repository version: `5.1.0`
- standalone `slurm-workflows`: `0.1`

Design review itself correctly performs no version bump.

If the approved behavior is later implemented, validated on the same final candidate, and formally released:

- standalone `slurm-workflows`: `0.1 -> 0.2`
- Repository: recompute the next PATCH from the actual current repository version at release time; with the current `5.1.0` baseline, that would be `5.1.1`
- Central Plugins: `NO_BUMP`

This is consistent with the current version policy because the proposed change improves an existing collection capability rather than adding a new repository-level workflow or central plugin.

---

## What this PASS proves and does not prove

This PASS proves that Proposal v0.2 is sufficiently correct, bounded, simple, and safe to serve as the approved **pre-implementation architecture** for the next Planner execution-package step.

It does **not** prove:

- that Longleaf supports the desired in-place partition widening;
- that any real Slurm command has been safely executed;
- that the future implementation correctly realizes this contract;
- that capability gates have passed;
- that `slurm-workflows 0.2` is ready to release.

No production file was modified by this review. No real Slurm state was touched.

The next role is Planner, which may now convert this approved design into the same-version execution package (Plan/Goal/Kickoff) required by the Planner/Critic contracts. That execution package still requires its own Critic execution-ready review before Codex/Executor may start.
