# Slurm Workflows Routing Refactor — Kickoff v0.2

直接执行已获架构 Critic PASS、且待 execution-ready Critic 最终放行的 Slurm Workflows routing refactor。不要重新设计 routing architecture。

Repository:

`YuukiAS/AI_Skills_Collection`

Exact task:

`hpc--slurm-workflows-routing-refactor`

Exact branch to create/use:

`reviewed/hpc--slurm-workflows-routing-refactor`

Exact task-owned worktree:

`/tmp/ai-skills-hpc-slurm-workflows-routing-refactor`

Canonical authority:

- Proposal: `docs/design/slurm-workflows/SLURM_WORKFLOWS_ROUTING_REFACTOR_PROPOSAL_V0_2_2026-09-24.md`
- Architecture Critic PASS: `docs/design/slurm-workflows/SLURM_WORKFLOWS_ROUTING_REFACTOR_CRITIC_REVIEW_V0_2_2026-09-24.md`
- Execution Plan: `docs/design/slurm-workflows/SLURM_WORKFLOWS_ROUTING_REFACTOR_EXECUTION_PLAN_V0_2_2026-09-24.md`
- Canonical Goal: `docs/goals/SLURM_WORKFLOWS_ROUTING_REFACTOR_GOAL_V0_2.md`

Start from kickoff-time latest compatible `origin/main`. It must still contain the approved package and have no relevant semantic drift. If relevant Slurm/environment/version-policy drift exists, stop and return to Planner/Critic.

## Authorized implementation scope

Implement only the approved Goal/Plan.

Keep the approved architecture:

```text
generic Skill
+ site hard authority
+ local preference
+ generated site reference
```

and the approved routing semantics:

```text
prefer
-> advisory probe
-> native single-job widening
-> duplicate fallback only when explicit site allow + user/local opt-in
```

In particular:

- remove generic Longleaf-specific partition/race defaults;
- propagate site hard policy into the installed generated reference;
- make doctor requiredness site-aware;
- keep `--test-only` advisory/fail-closed;
- in-place widening only after site/job-class probe evidence;
- cancel+resubmit only for replaceable pending jobs with state-safe cancellation and old-job inactive confirmation;
- identity-sensitive array/dependency/external-JobId workflows fail closed;
- Longleaf/CUHK `disabled_by_default` must not be widened by local duplicate-race opt-in;
- duplicate fallback may remain disabled; do not implement it just to make G4 look complete;
- do not implement the future NON_GOALS listed in the Plan.

## Real Slurm authorization in this Kickoff

By sending this exact approved Kickoff, I authorize **one conditional bounded Longleaf probe only if the implementation genuinely needs it to decide whether automatic in-place Partition widening can be enabled**.

That probe is limited to:

- at most one newly submitted probe job;
- obvious probe-only name;
- submitted held from the start;
- no business/research computation;
- trivial no-op payload;
- minimal common resources;
- requested walltime at most five minutes;
- inspect/update only that probe JobId;
- attempt only the approved pending/held Partition update;
- never intentionally release it to RUNNING;
- cancel it and verify it is inactive before completion.

If no common safe resource contract exists, the probe becomes RUNNING/CONFIGURING, update semantics are ambiguous, or cleanup cannot be confirmed:

- stop further real Slurm mutations;
- do not submit a second probe;
- leave in-place widening unverified/fail-closed;
- report the probe JobId if cleanup remains unresolved.

This authorization does **not** permit touching any pre-existing Slurm job, changing an existing research job, running duplicate-job race, or submitting any business workload.

Site-specific/private raw probe output must remain in the Plan-approved `private/exports/` path; public results must redact actual partition/account/path values.

## Tests and gates

Run focused deterministic regression first, then current repository full validation.

G1-G6 must follow the approved matrix.

G2/G3 core branches and G6 must exercise the actually installed `slurm-workflows` normal entry consuming generated site reference; helper-only tests are insufficient.

After implementation evidence is ready, freeze the candidate and obtain the Plan-required independent pre-final Critic review before release closure.

## Release closure

After required gates and pre-final Critic PASS:

- bump `slurm-workflows 0.1 -> 0.2` exactly once;
- compute repository next PATCH from actual release-time `VERSION`;
- central Plugins all remain `NO_BUMP`;
- update README/CHANGELOG/version/generated parity as defined by the Plan;
- rerun release validation.

Ordinary non-force push to the exact reviewed branch is authorized.

After final gates and Critic approval, ordinary non-force integration of the exact reviewed final candidate to `main` is authorized only if main has no relevant conflicting semantic drift. No force push.

Do not modify Longleaf_Bridge, Bridge Kit, CAT-TRACE/CARE product logic, other standalone Skills, or central Plugin topology.

Final report must include:

```text
RESULT = PASS | REVISE
TASK = hpc--slurm-workflows-routing-refactor
BRANCH =
WORKTREE =
START_MAIN =
FINAL_CANDIDATE =
G1 =
G2 =
G3 =
G4 =
G5 =
G6 =
LONGLEAF_PROBE = NOT_NEEDED | PASS | FAIL | BLOCKED
PROBE_CLEANUP = NOT_APPLICABLE | PASS | BLOCKED
SLURM_WORKFLOWS_VERSION =
REPOSITORY_VERSION =
CENTRAL_PLUGIN_BUMPS = NONE
README_CHECK =
FULL_TEST_SUITE =
FINAL_CRITIC =
INTEGRATED_TO_MAIN = YES | NO
REMOTE_MAIN =
```
