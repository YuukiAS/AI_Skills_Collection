# Slurm Workflows Routing Refactor — EXECUTION_READY Critic Prompt v0.6

你继续作为 AI Research Stack 的独立 Critic。

这是同一个 task key 的 **EXECUTION_READY** review。

本轮不是重新审 architecture。Proposal v0.6 已获得独立 Critic PASS；你要审查的是 Planner 是否把已批准架构完整、可执行、不过度地冻结成新的 v0.6 Plan / Goal / Kickoff。

## Active Review Context

Target repository:

`YuukiAS/AI_Skills_Collection`

Target:

standalone Skill / HPC / `slurm-workflows`

Design topic / task key:

`hpc--slurm-workflows-routing-refactor`

Review stage:

`EXECUTION_READY`

Approved architecture:

`docs/design/slurm-workflows/SLURM_WORKFLOWS_ROUTING_REFACTOR_PROPOSAL_V0_6_2026-09-24.md`

Proposal commit:

`ad3e60988f5581dd0d0c194e13907baaa446c413`

Architecture Critic PASS:

`docs/design/slurm-workflows/SLURM_WORKFLOWS_ROUTING_REFACTOR_CRITIC_REVIEW_V0_6_2026-09-24.md`

Architecture PASS commit:

`63a80b33e51c2eaf7fb5bc662a8ef87f3cdeede8`

Execution Plan v0.6:

`docs/design/slurm-workflows/SLURM_WORKFLOWS_ROUTING_REFACTOR_EXECUTION_PLAN_V0_6_2026-09-24.md`

Plan commit:

`8a73c8edd82b2a02749a1cff884d06122874fac3`

Canonical Goal v0.6:

`docs/goals/SLURM_WORKFLOWS_ROUTING_REFACTOR_GOAL_V0_6.md`

Goal commit:

`f44f8b09004019222dbd1dc649ca14db04202bb9`

Kickoff Draft v0.6:

`docs/operations/prompts/SLURM_WORKFLOWS_ROUTING_REFACTOR_KICKOFF_V0_6.md`

Kickoff/package-tip commit:

`c4df32fd1778b216aaa459a80c117283ad318ad8`

Future execution branch:

`reviewed/hpc--slurm-workflows-routing-refactor`

Future execution worktree:

`/tmp/ai-skills-hpc-slurm-workflows-routing-refactor`

Neither exists yet.

The old v0.2 execution package is obsolete historical evidence and MUST NOT be treated as execution authority.

## 1. Required read

First actually read current latest main:

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md`

Then read:

- approved Proposal v0.6;
- architecture Critic PASS v0.6;
- exact Execution Plan v0.6;
- exact Goal v0.6;
- exact Kickoff v0.6.

Read current production source only as needed to check that package file boundaries/version assumptions are real.

Do not reopen already-closed architecture findings unless the v0.6 execution package itself weakens or contradicts them.

## 2. Architecture equivalence check

Confirm the package faithfully preserves all approved capabilities:

- generic bounded live Slurm discovery;
- optional public hard-policy overlays, not a supported-server registry;
- local_site_id / optional policy_overlay_id split;
- no-profile site environment detect/plan/apply/doctor;
- fact != policy != preference;
- no deployment-specific generic constants;
- sticky workload resource contracts + accepted G7 hysteresis;
- batch / persistent allocation / debug interactive modes;
- persistent reusable capacity lifecycle;
- one active / one intended successor;
- one-time bounded family enrollment;
- same-scope recurring maintenance without weekly re-prompt;
- unrelated CPU-only workload does not activate enrolled GPU family;
- JobId/dependency/array/running-transition safety;
- duplicate-race explicit site authority;
- G1-G8 including G1/G6 portability extensions;
- Bridge Kit NO CHANGE.

Any package text that materially changes those semantics is a blocker.

## 3. Execution identity and authorization

Verify exact future execution identity:

```text
branch:
reviewed/hpc--slurm-workflows-routing-refactor

worktree:
/tmp/ai-skills-hpc-slurm-workflows-routing-refactor
```

Creation is authorized only after:

1. this execution-ready review returns `READY_FOR_CODEX=YES`;
2. the user sends the approved v0.6 Kickoff.

Check that no authorization expands to arbitrary `reviewed/*`, arbitrary repos, force push, or unrelated Slurm mutation.

## 4. Production source boundary

Check that allowed source scope is sufficient but bounded:

- `skills/tools/hpc/slurm-workflows/SKILL.md`;
- concise Skill references;
- at most one small deterministic skill-local helper;
- `scripts/skills.py`;
- local override example/docs;
- minimal existing site-profile/schema changes only when actually required;
- focused existing tests / at most one focused Slurm test file;
- direct domain/catalog/registry/generated parity;
- release files only at final closure.

The helper may normalize discovery/contracts/planning but must not become daemon, watcher, server registry, scheduler, history DB or new workflow engine.

Bridge Kit, Longleaf_Bridge, scientific project logic and central Plugin behavior/topology remain out of scope.

## 5. Generic discovery implementation check

The package requires:

- bounded read-only discovery;
- prefer explicit `sinfo -o/-O` field whitelists;
- raw `sinfo --json/--yaml` not treated as privacy-minimal;
- raw discovery dumps never persisted to tracked project source;
- minimum controller/database RPCs only;
- optional `sacctmgr` association query fail-soft to UNKNOWN;
- private/raw ClusterName replaced by a safe local alias where necessary;
- no-profile live Slurm site can complete environment plan/apply.

Check whether this is concrete enough for Executor without inventing a site registry or leaking private infrastructure.

## 6. Resource-contract implementation check

Verify the package correctly freezes:

- comparable workload family;
- explicit/user/project contract precedence;
- exact reuse when no new evidence;
- approved memory hysteresis;
- OOM increase after rounding strictly greater than current;
- MaxRSS comparability guard;
- CPU stable-first;
- timeout walltime evidence;
- persistent availability duration separate from batch elapsed;
- GPU type/count never silently downgraded;
- missing `sacct Comment` -> conservative matching.

Check that routing cannot mutate resources merely to make a route look schedulable.

## 7. Local partition / accelerator preference

The package carries a user-local preference model without generic deployment constants:

1. hard resource requirements filter first;
2. live/site legality filters next;
3. explicit local preferred partition tier may rank first;
4. remaining legal compatible routes may follow a user-local accelerator-class preference;
5. scheduler advisory evidence follows.

If accelerator type is a hard requirement, it cannot be downgraded.

Check that the package keeps exact deployment partition/GPU mappings out of generic source and uses fictional names for tests.

## 8. Persistent capacity and enrollment authority

Check:

- compatible active capacity is reused first;
- at most one intended successor;
- missing successor is only mutable for valid enrolled same-scope family;
- `auto_maintain_successor=true` without enrollment is read-only;
- unrelated CPU-only task does not activate enrolled GPU family;
- material scope change reauthorizes;
- stale enrollment fails closed;
- pre-existing jobs remain outside lifecycle mutation scope unless separately authorized/replaceable.

The implementation task itself must NOT enroll or maintain the user's real weekly GPU capacity family.

## 9. Existing routing safety

Verify the Plan/Kickoff preserve:

- `--test-only` advisory only;
- parse failure fail closed;
- native single-job widening;
- in-place Partition update only after target-site/job-class evidence;
- cancel+resubmit only replaceable pending jobs;
- state-safe cancellation and old-job inactivity confirmation;
- identity-sensitive arrays/dependencies/external JobIds fail closed;
- duplicate race requires explicit site allow + user/local opt-in;
- unknown site authority disables duplicate race.

Do not reopen the old architecture findings unless package text regresses them.

## 10. Development tests vs production gates

Confirm deterministic development tests cover G1-G5/G7/G8 behavior without real Slurm mutation.

Confirm G6 requires the actually installed production path, including:

- known-profile site fixture;
- no-profile fake third-party Slurm site;
- installed Skill/helper consumes live fake SiteContext/local preference;
- persistent capacity normal entry.

Helper-only unit tests must not satisfy G6.

## 11. Real Slurm probe authorization — high priority

The user has not yet sent the Kickoff. This review itself authorizes NO mutation.

If the user later sends the exact approved Kickoff, it conditionally authorizes no more than:

### Probe A
maximum one held/no-op batch probe, combining calendar-bound and pending Partition-update questions where safe.

### Probe B
maximum one minimal persistent-allocation lifecycle probe, only if still necessary.

Check all boundaries:

- no existing user job touched;
- no real weekly successor;
- no real family enrollment;
- no duplicate race;
- no scientific/research payload;
- no research GPU computation;
- no account/QOS/association/reservation/admin mutation;
- each probe walltime <= 5 minutes;
- Probe B prefers CPU-only;
- no indefinite wait;
- no retry after ambiguous/failing probe without new user authorization;
- cleanup must be confirmed;
- raw private evidence stays under `private/exports/`;
- public evidence is redacted.

Check that conceptual P-A/P-B/P-C questions do not mechanically cause three jobs and that read-only/test-only evidence is used first.

If this boundary is too permissive or not executable, REVISE.

## 12. Evidence and final-candidate freeze

Check that the Plan requires:

- task evidence in repo;
- raw sensitive evidence under `private/exports/`;
- fetch/reconcile compatible main drift before final freeze;
- compute release version before freeze;
- one exact final candidate SHA;
- no production changes after freeze without invalidating final gates.

## 13. Release/version contract

Architecture/package docs: no bump.

If complete capability ships:

```text
Repository release class: MINOR

Current baseline if unchanged:
5.1.0 -> 5.2.0

If release-time VERSION changed:
next MINOR from actual VERSION

Standalone:
slurm-workflows 0.1 -> 0.2

Central Plugins:
all NO_BUMP

Bridge Kit:
NO CHANGE
```

Check that release metadata is applied before final-candidate gates so the exact versioned candidate receives G1-G8/full-test/final-Critic validation.

No new version infrastructure may be introduced.

## 14. G1-G8 review

Do not invent G9 without a genuinely distinct missing capability.

Check the frozen gate meanings:

- G1 site isolation + live discovery/privacy/unknown fail-closed;
- G2 local preference routing without resource mutation;
- G3 native widening + JobId/dependency/array/transition safety;
- G4 duplicate-race authority or disabled/NOT_APPLICABLE release capability;
- G5 bounded monitoring/replacement;
- G6 real installed normal entry including no-profile site;
- G7 resource-contract stability/right-sizing;
- G8 workload mode + reusable capacity lifecycle + enrollment authority.

Check whether the final candidate is the same candidate used for the meaningful gate evidence.

## 15. Pre-final review and integration

The package requires an independent pre-final Critic review after the exact release candidate is frozen and G1-G8 evidence exists.

Only after that PASS may the exact reviewed candidate be ordinary non-force integrated to main.

Check that:

- no force push is authorized;
- relevant main drift stops/reconciles before integration;
- a changed required MINOR target causes affected gates/review to rerun;
- no unreviewed production bytes are introduced during integration.

## 16. Result standard

Return:

`RESULT = PASS`

or

`RESULT = REVISE`

Also return:

`READY_FOR_CODEX = YES | NO`

PASS requires:

```text
RESULT = PASS
READY_FOR_CODEX = YES
```

If REVISE, each blocker must state:

- requirement;
- direct package/source evidence;
- concrete execution/resource/release risk;
- minimum closure condition.

Do not create a new architecture round unless the package actually changes architecture.

If PASS, bind:

```text
PASS_OBJECT =
SLURM_WORKFLOWS_ROUTING_REFACTOR_EXECUTION_PACKAGE_V0_6

PASS_SCOPE =
execution-ready Plan + Goal + Kickoff only; actual execution begins only after user sends approved v0.6 Kickoff
```

## 17. Review record

You are authorized only to write:

`docs/design/slurm-workflows/SLURM_WORKFLOWS_ROUTING_REFACTOR_EXECUTION_CRITIC_REVIEW_V0_6_2026-09-24.md`

to current main.

Commit + ordinary non-force push only that review document.

Do NOT:

- create execution branch/worktree;
- modify production source/tests;
- execute any real Slurm mutation;
- enroll a real capacity family;
- modify Bridge Kit;
- bump version;
- start Executor;
- call paid API.

Finally report:

```text
RESULT =
READY_FOR_CODEX =
REVIEW_PATH =
REVIEW_COMMIT =

PROPOSAL_COMMIT = ad3e60988f5581dd0d0c194e13907baaa446c413
ARCHITECTURE_PASS_COMMIT = 63a80b33e51c2eaf7fb5bc662a8ef87f3cdeede8
PLAN_COMMIT = 8a73c8edd82b2a02749a1cff884d06122874fac3
GOAL_COMMIT = f44f8b09004019222dbd1dc649ca14db04202bb9
KICKOFF_PACKAGE_TIP = c4df32fd1778b216aaa459a80c117283ad318ad8

EXECUTION_BRANCH =
reviewed/hpc--slurm-workflows-routing-refactor

EXECUTION_WORKTREE =
/tmp/ai-skills-hpc-slurm-workflows-routing-refactor

REAL_SLURM_AUTH_BOUNDARY = PASS | FAIL
NO_PROFILE_PORTABILITY = PASS | FAIL
RESOURCE_CONTRACT = PASS | FAIL
CAPACITY_ENROLLMENT = PASS | FAIL
VERSION_CLOSURE = PASS | FAIL
REPOSITORY_RELEASE_CLASS = MINOR | OTHER
STANDALONE_SLURM_WORKFLOWS_RELEASE = 0.1 -> 0.2 | OTHER
CENTRAL_PLUGIN_BUMPS = NONE | OTHER
BRIDGE_CHANGE_REQUIRED = NO
```
