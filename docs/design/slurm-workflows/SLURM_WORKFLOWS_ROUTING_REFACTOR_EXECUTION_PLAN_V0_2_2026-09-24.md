# Slurm Workflows Routing Refactor — Execution Plan v0.2

日期：2026-09-24  
状态：AWAITING_EXECUTION_READY_CRITIC  
Target: standalone Skill / HPC / `slurm-workflows`  
Task key: `hpc--slurm-workflows-routing-refactor`

## 0. Authority and execution identity

Approved architecture:

- Proposal: `docs/design/slurm-workflows/SLURM_WORKFLOWS_ROUTING_REFACTOR_PROPOSAL_V0_2_2026-09-24.md`
- Proposal commit: `b1d516c173ce838fd5eb9f39ae0a117bcb7f517e`
- Architecture Critic PASS: `docs/design/slurm-workflows/SLURM_WORKFLOWS_ROUTING_REFACTOR_CRITIC_REVIEW_V0_2_2026-09-24.md`
- Critic commit: `08c598f748903ec48c07b96fd1b35dc96561699d`

Exact execution branch after approved Kickoff:

`reviewed/hpc--slurm-workflows-routing-refactor`

Exact task-owned worktree after approved Kickoff:

`/tmp/ai-skills-hpc-slurm-workflows-routing-refactor`

The branch must be created from kickoff-time latest `origin/main` only if that main still contains the approved v0.2 package and has no relevant semantic drift. Relevant drift in Slurm Skill, environment overlay, site-profile policy, version policy, or approved gates stops execution and returns to Planner/Critic.

This Plan is not execution authorization. Execution begins only after the exact v0.2 Proposal + Plan + Goal + Kickoff receive independent execution-ready Critic PASS and the user then sends the approved Kickoff.

## 1. Product outcome

The task closes the gap between the current declarative Slurm Skill and the environment overlay it consumes.

The final normal behavior remains:

```text
generic Slurm Skill
+ site hard authority
+ local preference
+ generated site reference
-> safe routing decision
```

The implementation must preserve the approved routing contract:

```text
ordered preference
-> advisory probe
-> single-route submit when justified
-> native single-job widening when both routes are acceptable
-> guarded duplicate-job fallback only if separately site-authorized
```

The implementation must never make Longleaf-specific partition names part of generic source.

## 2. Production source boundary

Allowed production/source modifications are limited to:

### Slurm Skill

- `skills/tools/hpc/slurm-workflows/SKILL.md`
- optional new `skills/tools/hpc/slurm-workflows/references/routing-policy.md`

The Skill stays concise. Detailed routing/identity/race semantics belong in the short reference if needed.

### Environment overlay

- `scripts/skills.py`
- `site-profiles/local-overrides.example.toml`
- `docs/LOCAL_CONFIGURATION.md`

### Site schema, only if required by the approved semantics

- `schemas/site-profile.schema.json`

Schema changes are permitted only to validate already-approved hard-policy values or required-field semantics. Do not create a new schema hierarchy or control plane.

### Tests

- `tests/test_skill_update.py`
- `tests/test_standalone_skill_baselines.py`
- at most one new focused Slurm routing test file if this materially improves readability; no new test framework

### Release closure

Only after implementation and final gates pass:

- `skills/tools/hpc/slurm-workflows/SKILL.md` version `0.1 -> 0.2`
- `README.md`
- `CHANGELOG.md`
- `VERSION`
- `setup.py`
- normal generated registry/catalog metadata produced by existing generators, only as needed for repository-version and Skill metadata parity

Central Marketplace plugin versions remain unchanged. Do not change central plugin topology or version metadata.

### Site profiles

Current `site-profiles/unc-longleaf.json` and `site-profiles/cuhk-central-cluster.json` remain `race_execution: disabled_by_default`.

Do not convert either site to duplicate-race allowed without new administrator/official authority and a new Planner/Critic review. If no site-profile content change is necessary, do not touch those files.

## 3. Explicit non-goals

Do not implement:

- resource-feasibility preflight;
- pending-reason-aware routing;
- restartability/preemption-aware routing;
- deadline-aware routing;
- raw hostname ranking;
- queue-history database;
- fairshare/scheduler prediction;
- daemon/watcher;
- dependency remapping;
- another scheduler/control plane;
- Longleaf_Bridge or Bridge Kit changes.

Do not modify real user experiments, existing Slurm jobs, CAT-TRACE/CARE logic, or any other standalone Skill.

## 4. Implementation sequence

### Phase A — kickoff-time preflight and branch isolation

1. Fetch current `origin/main`.
2. Confirm approved Proposal/architecture Critic package is present.
3. Inspect relevant drift since `08c598f748903ec48c07b96fd1b35dc96561699d`.
4. Create exactly:
   - branch `reviewed/hpc--slurm-workflows-routing-refactor`
   - worktree `/tmp/ai-skills-hpc-slurm-workflows-routing-refactor`
5. Record starting main SHA in task results.
6. Do not edit production source until preflight is clean.

### Phase B — close generic/site/local boundary

Implement the smallest changes needed so that:

1. `environment init` no longer emits any Longleaf-specific partition names or hard-coded `60` minute race threshold for arbitrary sites.
2. New local override vocabulary reflects the approved v0.2 semantics:
   - `partition`
   - `partition_priority`
   - `widen_after_minutes`
   - `duplicate_race_opt_in`
   - `node_feature_preference`
3. Legacy `race_partitions`, `race_after_minutes`, and `race_cancel_policy` remain readable for compatibility but are no longer emitted as new canonical defaults. Doctor reports a migration advisory; it must not auto-edit the user's real override.
4. Generated `references/_generated/site-profile.md` carries site hard constraints and site race authority in a form the installed Skill can actually consume.
5. Doctor requiredness is derived from site hard constraints rather than global guessed required fields. A non-empty `partition_priority` may satisfy an explicit-partition requirement where the approved site rule allows it.
6. Missing/unknown/`disabled_by_default` duplicate-race authority remains fail-closed.

### Phase C — encode the approved routing contract

Update the Skill/reference so the normal entry implements:

1. ordered partition preference;
2. `sbatch --test-only` only as advisory;
3. parse failure -> conservative/fail-closed path;
4. single-job multi-partition as native widening, not a latency guarantee;
5. in-place Partition widening only after target-site/job-class probe evidence exists;
6. cancel+resubmit only for replaceable pending jobs;
7. identity-sensitive array/dependency/external-JobId workflows fail closed;
8. state-safe cancellation and old-job-inactive confirmation before replacement;
9. duplicate submissions require both:
   - site explicit `allowed_with_user_opt_in`;
   - user/local opt-in.

Do not implement duplicate fallback merely to satisfy G4. If it is not necessary for the bounded release, keep it disabled and mark G4 not applicable for enabled capability.

### Phase D — development-local tests

Before any real Slurm side effect, run focused deterministic tests that cover at minimum:

- generic template contains no Longleaf partition constants;
- CUHK and Longleaf local configs do not leak into each other;
- generated installed reference contains site hard policy;
- legacy local fields parse without becoming new defaults;
- doctor requiredness comes from site constraints;
- site unknown/disabled + local duplicate opt-in cannot produce duplicate submissions;
- P1 immediate;
- P1 delayed / P2 immediate;
- both delayed -> native single-job widening decision;
- unparseable `--test-only` -> fail closed;
- downstream dependency -> no cancel+resubmit;
- array/dependency identity -> no JobId replacement;
- PENDING->RUNNING transition -> no unsafe cancel/replacement;
- uncertain old-job cancellation -> no replacement;
- explicit fixed partition -> no unrequested widening.

Then run the repository's existing relevant validation and full test suite. Use current repo test/CI commands rather than inventing a new harness.

No real Slurm submit/hold/update/cancel is permitted merely because local tests pass.

## 5. Bounded Longleaf in-place Partition probe

This probe is conditional. It is needed only if the final implementation wants to enable automatic in-place widening for Longleaf and deterministic/source evidence cannot establish the site behavior.

The approved Kickoff, if the user sends it, explicitly authorizes this one bounded probe. No other real Slurm mutation is authorized.

### Preconditions

- target environment is genuinely UNC Longleaf;
- candidate partition names come from the user's existing local configuration or current scheduler evidence, not from repository constants;
- there is a minimal common resource contract acceptable to both candidate partitions;
- no existing user job is touched.

If any precondition fails, skip the probe and leave Longleaf in-place widening unverified/fail-closed.

### Exact probe class

At most one new test job:

- dedicated obvious probe name;
- submitted held from the start;
- no business/research payload;
- minimal resources;
- maximum requested walltime five minutes;
- payload no more than a trivial no-op such as `true`;
- never intentionally released to RUNNING.

The probe may:

1. submit the held test job;
2. inspect only that JobId;
3. attempt the approved Partition update on that held/PENDING test job;
4. verify JobId is unchanged and the partition field/state reflects the expected candidate set;
5. cancel the probe job;
6. verify it is no longer active.

### Stop / recovery

- If the job is unexpectedly RUNNING/CONFIGURING, do not perform further widening mutation; stop and report.
- If update semantics are ambiguous, mark in-place widening unverified and stop.
- If cleanup/cancel does not confirm the probe is inactive, stop all further Slurm mutations and report the exact probe JobId for recovery.
- Never submit a second probe to compensate for a failed first probe in the same execution without a new user authorization.

Raw scheduler output that contains site-specific/private values stays under:

`private/exports/hpc--slurm-workflows-routing-refactor/longleaf-inplace-probe/`

A public-safe redacted summary may be written under:

`results/hpc--slurm-workflows-routing-refactor/longleaf-inplace-probe/`

The public summary uses P1/P2 labels rather than committing personal partition/account/path values.

## 6. Capability Gate execution

### G1 — Site isolation and authority propagation

Final candidate must prove:

- no generic Longleaf partition constants;
- no cross-site leakage;
- site hard policy reaches installed generated reference;
- current Longleaf/CUHK disabled duplicate authority remains fail-closed.

### G2 — Preference routing

Through the installed Skill normal entry, not helper-only:

- P1 immediate;
- P1 delayed / P2 immediate;
- probe parse failure.

### G3 — Native widening and JobId safety

Through the installed normal entry plus deterministic Slurm fixtures:

- both delayed -> one native multi-partition job decision when compatible;
- no duplicate submission by default;
- dependency/array/external-JobId negative cases;
- PENDING->RUNNING transition safety;
- in-place route only when site/job-class evidence exists.

If the conditional Longleaf probe is run, its result is site capability evidence, not permission to mutate existing jobs.

### G4 — Duplicate-race authority and isolation

If duplicate fallback remains disabled, record G4 as disabled/NOT_APPLICABLE for enabled release capability.

If implemented, final candidate must prove:

- site explicit allow is required;
- local opt-in alone never authorizes it;
- output/log staging and winner/loser safety are real.

Current Longleaf/CUHK may not be used as "allowed" fixtures without new site authority.

### G5 — Bounded monitoring and replacement safety

Final candidate must prove:

- no tight polling;
- no blind resubmit;
- uncertain old-job state produces no replacement;
- identity-sensitive job keeps its JobId or stops safely.

### G6 — Production identity

Materialize the final candidate through the real environment apply/install path, then exercise the normal installed `slurm-workflows` entry against repo-safe fixtures/generated site references.

Helper/unit tests alone cannot satisfy G6.

## 7. Pre-final review and final-candidate freeze

After implementation, focused/full tests, representative installed-entry replays, and any authorized site probe are complete:

1. freeze the implementation candidate;
2. write a concise gate/evidence package under `results/hpc--slurm-workflows-routing-refactor/`;
3. request independent Critic pre-final review of:
   - implementation diff;
   - G1-G6 evidence;
   - actual installed Skill/reference;
   - probe result if one was run;
   - planned release/version closure.

Do not perform final release closure if Critic finds a substantive architecture/implementation mismatch.

No paid external reviewer is needed.

## 8. Release closure

Only after the same final production candidate passes required gates and independent pre-final review:

1. bump standalone `slurm-workflows` exactly once: `0.1 -> 0.2`;
2. recompute repository next PATCH from the actual `VERSION` then present:
   - if still `5.1.0`, use `5.1.1`;
   - if main/release identity changed, use the next PATCH of that actual version;
3. central Plugins: all `NO_BUMP`;
4. update README standalone version/purpose if needed;
5. update root CHANGELOG;
6. update `VERSION`, `setup.py`, registry/catalog/generated metadata through existing generators as required for parity;
7. rerun release/version parity validation and relevant full tests.

Release result must explicitly state:

```text
Repository bump decision: PATCH
Reason: compatible improvement to existing standalone Slurm/environment capability.
Affected plugins:
- all central plugins: NO_BUMP
Standalone skills:
- slurm-workflows: 0.1 -> 0.2
```

## 9. Integration and handoff

During execution, all implementation/evidence commits are pushed by ordinary non-force push to:

`reviewed/hpc--slurm-workflows-routing-refactor`

No force push.

After final Critic/release gates are satisfied, the approved Kickoff authorizes ordinary non-force integration of the reviewed final candidate to current `main` only if:

- main has no relevant conflicting semantic drift;
- the candidate is the exact reviewed final candidate;
- integration does not change production bytes beyond the reviewed candidate plus approved release metadata.

If relevant drift exists, stop and return to Planner/Critic rather than silently resolving.

Final closure must verify remote `main` equals the intended integrated release commit and README/version/generated parity is intact.
