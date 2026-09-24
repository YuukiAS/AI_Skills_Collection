# Slurm Workflows Routing Refactor — Execution-Ready Critic Prompt v0.2

你继续作为 AI Research Stack 的独立 Critic。

这是 `hpc--slurm-workflows-routing-refactor` 的 **EXECUTION_READY** review。

本轮不是重新审 architecture。Proposal v0.2 已经获得独立架构 PASS；你要审查的是 Planner 是否把该已批准设计正确、完整且不过度地冻结成可交给 Codex Executor 的 Plan / Goal / Kickoff。

## Active Review Context

Target repository:

`YuukiAS/AI_Skills_Collection`

Target:

standalone Skill / HPC / `slurm-workflows`

Design topic / task key:

`hpc--slurm-workflows-routing-refactor`

Review stage:

`EXECUTION_READY`

Approved architecture Proposal:

`docs/design/slurm-workflows/SLURM_WORKFLOWS_ROUTING_REFACTOR_PROPOSAL_V0_2_2026-09-24.md`

Proposal commit:

`b1d516c173ce838fd5eb9f39ae0a117bcb7f517e`

Architecture Critic PASS:

`docs/design/slurm-workflows/SLURM_WORKFLOWS_ROUTING_REFACTOR_CRITIC_REVIEW_V0_2_2026-09-24.md`

Architecture Critic commit:

`08c598f748903ec48c07b96fd1b35dc96561699d`

Execution package:

- Plan: `docs/design/slurm-workflows/SLURM_WORKFLOWS_ROUTING_REFACTOR_EXECUTION_PLAN_V0_2_2026-09-24.md`
- Goal: `docs/goals/SLURM_WORKFLOWS_ROUTING_REFACTOR_GOAL_V0_2.md`
- Kickoff: `docs/operations/prompts/SLURM_WORKFLOWS_ROUTING_REFACTOR_KICKOFF_V0_2.md`

Execution package commits:

- Plan: `1309628e5a6fd7be4f81cbd9997b18720244983b`
- Goal: `aeec366f95dd59e24a760444d1413a91f2583eaa`
- Kickoff / package tip: `8a489d1cf21298eada472e185d820efdac83671c`

Exact future execution branch:

`reviewed/hpc--slurm-workflows-routing-refactor`

Exact future task-owned worktree:

`/tmp/ai-skills-hpc-slurm-workflows-routing-refactor`

No execution branch/worktree has been created yet.

## 1. Required read

First actually read current latest main:

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md`

Then read:

- approved Proposal v0.2;
- architecture Critic PASS v0.2;
- exact Execution Plan v0.2;
- exact Goal v0.2;
- exact Kickoff v0.2.

Read current production source only as needed to verify the execution package still points to real files and current version identities. Do not reopen already-approved Slurm architecture merely because you can imagine an alternative.

If main advanced after the package only because of unrelated docs/review commits, do not mechanically REVISE. Only relevant semantic drift matters.

## 2. Architecture equivalence check

Verify that Plan / Goal / Kickoff preserve, without weakening or expanding, the approved architecture:

- generic Skill + site hard authority + local preference + generated site reference;
- generic source contains no Longleaf-specific partition constants;
- ordered preference -> advisory probe -> native single-job widening;
- `--test-only` remains advisory and parse failure fails closed;
- in-place Partition widening is only automatically enabled after real target-site/job-class probe evidence;
- cancel+resubmit is only for replaceable pending jobs;
- replacement requires state-safe cancellation and old-job inactive confirmation;
- identity-sensitive array/dependency/external-JobId workflows fail closed;
- duplicate race requires **site explicit allow + user/local opt-in**;
- current Longleaf/CUHK `disabled_by_default` is not reinterpreted as allow;
- G1-G6 semantics match approved Proposal;
- duplicate fallback may remain disabled;
- future resource-feasibility / pending-reason / restartability-preemption / deadline-aware routing remain NON_GOALS;
- no daemon/watcher/database/control plane is introduced.

If any package text materially changes those semantics, REVISE.

## 3. Execution identity and authorization check

Check that the package correctly freezes:

```text
branch:
reviewed/hpc--slurm-workflows-routing-refactor

worktree:
/tmp/ai-skills-hpc-slurm-workflows-routing-refactor
```

The package should allow branch/worktree creation only after the user sends the approved Kickoff.

Check that routine implementation authorization is bounded to the approved task and does not become generic authorization for arbitrary `reviewed/*`, arbitrary Slurm mutations, or unrelated repos.

## 4. Production source boundary check

Verify that the allowed files are sufficient but not unnecessarily broad.

Expected main implementation layers:

- `skills/tools/hpc/slurm-workflows/SKILL.md`
- optional short routing reference under the same Skill
- `scripts/skills.py`
- `site-profiles/local-overrides.example.toml`
- `docs/LOCAL_CONFIGURATION.md`
- minimal existing schema changes only if needed
- focused existing tests / at most one clear new routing test file
- release/version/generated-parity files only at final closure

Current Longleaf/CUHK site profiles should remain duplicate-race `disabled_by_default` unless new site-authority evidence exists. The package must not quietly authorize changing them to allowed.

Do not require a new routing service/helper merely for testability unless current source makes the normal Skill route impossible without one.

## 5. Real Slurm probe authorization — high-priority review

This is the highest-risk part of the execution package.

The user specifically required any real Slurm submit/hold/update/cancel to be explicitly authorized only when they later send the approved Kickoff.

The Kickoff currently contains a conditional one-probe authorization.

Check whether that scope is least-privilege and executable:

- at most one newly submitted test job;
- held from submission;
- no business/research payload;
- trivial no-op;
- minimal common resource contract;
- walltime <= five minutes;
- inspect/update/cancel only that probe JobId;
- never intentionally release it to RUNNING;
- no existing user job may be modified;
- no duplicate-job race;
- ambiguous update or cleanup failure stops further Slurm mutation;
- no second probe without new user authorization;
- raw site-specific evidence remains under repo `private/exports/`;
- public evidence is redacted.

Also check that the probe is **conditional**, not a mandatory release ritual. If Longleaf in-place widening can remain unverified/fail-closed, the Executor must be allowed to skip the probe.

If the probe authorization could accidentally permit touching existing research jobs or running real workloads, REVISE.

## 6. Development vs final gates

Verify the execution package clearly separates:

### Development-local evidence

- deterministic fixtures;
- focused tests;
- current full repository validation;
- no real Slurm side effect merely because tests pass.

### Production/normal-entry evidence

- installed `slurm-workflows` consumes generated site reference;
- G2/G3 core routing branches are exercised through normal installed entry;
- G6 is not satisfied by helper/unit tests alone.

### Pre-final independent review

Before release closure, implementation diff + gate evidence + installed artifact + optional probe evidence must be independently reviewed.

The package should not use version bump or integration to hide an unreviewed behavior change.

## 7. Capability Gate review

Review the frozen G1-G6 execution semantics, not a new taxonomy.

Pay special attention:

- G1: site isolation + authority propagation;
- G2: installed normal entry for P1/P2/probe parse cases;
- G3: native widening + JobId/dependency/array/RUNNING-transition safety;
- G4: optional duplicate fallback; current disabled sites must not duplicate;
- G5: uncertain old-job state -> no replacement;
- G6: final installed production identity.

Do not add more gates unless a genuinely distinct user capability is missing.

## 8. Version/release closure check

The package proposes:

- design/execution package itself: no bump;
- after implementation + same-final-candidate gates + pre-final Critic PASS:
  - `slurm-workflows 0.1 -> 0.2`;
  - repository = next PATCH from actual release-time VERSION;
  - current `5.1.0` baseline would therefore become `5.1.1`;
  - all central Plugins = `NO_BUMP`.

Check that release metadata is updated only after product gates, and that repository parity uses existing generators/validation rather than new version infrastructure.

## 9. Integration boundary

The package allows ordinary non-force push to the exact reviewed branch during development.

Only after required final Critic/gates does the Kickoff authorize ordinary non-force integration of the exact reviewed final candidate to main, and only if there is no relevant conflicting main drift.

Check that this does not allow force push, silent conflict resolution, or unreviewed production byte changes.

## 10. Result standard

Return:

`RESULT = PASS`

or

`RESULT = REVISE`

Also return:

`READY_FOR_CODEX = YES | NO`

PASS requires both:

```text
RESULT = PASS
READY_FOR_CODEX = YES
```

If REVISE, every blocker must include:

- exact requirement;
- direct package/source evidence;
- concrete causal risk;
- minimal closure condition.

Do not reopen architecture findings already closed unless the execution package actually violates them.

If PASS, explicitly bind:

```text
PASS_OBJECT =
SLURM_WORKFLOWS_ROUTING_REFACTOR_EXECUTION_PACKAGE_V0_2

PASS_SCOPE =
execution-ready Plan + Goal + Kickoff only; execution begins only after user sends approved Kickoff
```

## 11. Review record

You are authorized only to write your own execution-ready Critic review document to current main.

Save as:

`docs/design/slurm-workflows/SLURM_WORKFLOWS_ROUTING_REFACTOR_EXECUTION_CRITIC_REVIEW_V0_2_2026-09-24.md`

Commit and ordinary non-force push only that review document.

Do not:

- create the execution branch/worktree;
- modify production Skill/source/tests;
- modify site profiles;
- run any real Slurm command that mutates state;
- start Executor;
- bump versions;
- modify Longleaf_Bridge or Bridge Kit;
- call paid APIs.

Finally report:

```text
RESULT =
READY_FOR_CODEX =
REVIEW_PATH =
REVIEW_COMMIT =
PACKAGE_TIP =
EXECUTION_BRANCH =
EXECUTION_WORKTREE =
REAL_SLURM_AUTH_BOUNDARY = PASS | FAIL
VERSION_CLOSURE = PASS | FAIL
```
