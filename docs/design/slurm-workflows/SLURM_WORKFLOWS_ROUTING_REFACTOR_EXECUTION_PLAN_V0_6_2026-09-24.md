# Slurm Workflows Routing Refactor — Execution Plan v0.6

日期：2026-09-24  
状态：AWAITING_EXECUTION_READY_CRITIC  
Target: standalone Skill / HPC / `slurm-workflows`  
Task key: `hpc--slurm-workflows-routing-refactor`

## 0. Authority, supersession, and execution identity

Canonical architecture:

- Proposal: `docs/design/slurm-workflows/SLURM_WORKFLOWS_ROUTING_REFACTOR_PROPOSAL_V0_6_2026-09-24.md`
- Proposal commit: `ad3e60988f5581dd0d0c194e13907baaa446c413`
- Architecture Critic PASS: `docs/design/slurm-workflows/SLURM_WORKFLOWS_ROUTING_REFACTOR_CRITIC_REVIEW_V0_6_2026-09-24.md`
- Critic commit: `63a80b33e51c2eaf7fb5bc662a8ef87f3cdeede8`

This v0.6 execution package supersedes the old v0.2 execution Plan/Goal/Kickoff. The old package remains historical evidence only and must not be used to launch implementation.

Exact future execution branch:

`reviewed/hpc--slurm-workflows-routing-refactor`

Exact future task-owned worktree:

`/tmp/ai-skills-hpc-slurm-workflows-routing-refactor`

Neither may be created until an independent Critic gives `READY_FOR_CODEX=YES` for this exact v0.6 execution package and the user then sends the approved v0.6 Kickoff.

At kickoff time, create the branch from the latest compatible `origin/main`. The latest main must still contain this approved package and must not have relevant semantic drift in Slurm Workflows, environment/site handling, capability gates, or version policy. Relevant drift stops execution and returns to Planner/Critic; unrelated docs/review drift does not.

## 1. Product outcome

Ship one portable Slurm Workflows product rather than a Longleaf-specific script.

Normal product composition:

```text
bounded live Slurm discovery
+ optional public hard-policy overlay
+ user-local facts/preferences
        ↓
resolved SiteContext
        ↓
workload mode
        ↓
sticky resource contract
        ↓
persistent capacity lifecycle when applicable
        ↓
safe routing / widening / fail-closed behavior
```

The release must work on:

1. known sites with optional public policy overlays;
2. a normal third-party Slurm site that has no committed repository profile.

The product must never require deployment-specific partition, hostname, GPU-route, node, account, or QOS constants in generic production source.

## 2. Frozen architecture contracts

Implementation must preserve all architecture findings closed by Proposal v0.6.

### 2.1 Fact, policy, preference

```text
live scheduler facts
!=
site hard policy
!=
user/project preference
```

- Live Slurm tells us what is currently visible/available.
- Optional public site profiles may restrict or clarify policy but are not a supported-server registry and cannot invent a live route.
- Local/project preferences choose among legal compatible routes; they cannot weaken hard policy.

### 2.2 Workload modes

- finite unattended compute -> batch mode;
- persistent reusable workspace/capacity -> persistent allocation mode;
- short debugging shell -> debug interactive mode.

Persistent mode reuses a compatible running allocation before requesting a new one. Allocation lifetime and scientific commands stay separate.

### 2.3 Sticky resource contract

For one comparable workload family, accepted CPU/memory/GPU/walltime stays unchanged unless explicit user/project input or approved accounting evidence passes the frozen hysteresis rules.

Routing may not silently shrink resources merely to improve queue placement.

### 2.4 Routing safety

```text
legal candidates
-> local preference
-> advisory probe
-> native single-job widening when appropriate
-> fail closed / optional guarded duplicate fallback
```

- `sbatch --test-only` is advisory only.
- In-place Partition widening requires real target-site/job-class probe evidence.
- cancel+resubmit is only for replaceable pending jobs.
- replacement requires state-safe cancellation and confirmed old-job inactivity.
- array/dependency/external-JobId-sensitive jobs fail closed if identity cannot be preserved.
- duplicate-job race requires explicit site allow plus user/local opt-in; unknown site authority disables it.

### 2.5 Persistent capacity lifecycle

A persistent capacity family is identified by stable family semantics, not calendar job names.

Target invariant:

```text
at most one compatible active allocation
+
at most one lifecycle-owned intended successor
```

Compatible active allocation is reused first. A successor is only maintained for the earliest uncovered target window.

### 2.6 Recurring authorization

`auto_maintain_successor=true` is a preference, not authorization.

Automatic recurring mutation requires a one-time bounded capacity-family enrollment containing the frozen site/family/resource/window/action scope. Same-scope occurrences do not re-prompt weekly. Scope expansion reauthorizes. Unenrolled monitor/diagnose remains read-only.

An enrolled GPU family is activated only by explicit family reference or an approved compatible-resource activation rule. A CPU-only task on the same cluster must not accidentally maintain a GPU successor.

### 2.7 Portability

Current scheduler facts come from bounded live discovery. Public `site-profiles/*.json` are optional policy overlays, not the list of supported servers.

A no-profile live Slurm site must be able to pass environment detect/plan/apply/doctor and normal installed Skill routing without repository source changes.

## 3. Production implementation boundary

Allowed implementation areas are bounded to the following.

### 3.1 Slurm Workflows source

- `skills/tools/hpc/slurm-workflows/SKILL.md`
- concise references under `skills/tools/hpc/slurm-workflows/references/`
- at most one small deterministic helper module under `skills/tools/hpc/slurm-workflows/scripts/`

The helper is part of the normal installed production path, not a test-only tool. Prefer one module rather than multiple services. It may own:

- bounded read-only Slurm discovery and SiteContext normalization;
- local contract parsing;
- workload/capacity family normalization;
- accounting normalization;
- resource hysteresis decisions;
- routing/capacity reconciliation planning;
- enrollment-scope normalization/digest.

It must not become a daemon, watcher, server registry, scheduler, queue-history database, or independent workflow engine.

Actual Slurm mutations remain governed by the Skill/action contract and current authorization; the helper must not invent permissions.

### 3.2 Shared environment/install path

- `scripts/skills.py`
- `site-profiles/local-overrides.example.toml`
- `docs/LOCAL_CONFIGURATION.md`
- `schemas/site-profile.schema.json` only if a minimal existing-schema extension is genuinely required

Expected shared behavior changes:

- environment profile matching becomes optional policy-overlay matching rather than the only site identity path;
- an unknown explicit `--site <id>` may be a local site id instead of an automatic error;
- no-profile + live Slurm can plan/apply;
- environment detect/doctor expose local site identity, discovery availability, optional policy overlay, and unknown facts;
- generated site reference becomes a public-safe locator/policy summary, not a private live-facts dump.

Existing Longleaf/CUHK public profiles may be adjusted only for wording/revision/schema parity required by this contract. Do not add deployment partition or GPU-route preferences to them and do not loosen their duplicate-race policy.

### 3.3 User-local current-state contract

Canonical local path:

`~/.config/ai-skills/slurm-workflows.toml`

It stores current declarative state only:

- workload-family accepted resource contracts;
- capacity-family preferences;
- one-time bounded enrollment scope;
- optional last-adjustment evidence locator.

It is not a history database or authorization ledger. Historical resource evidence remains in `sacct`.

The repository may add a public-safe example/template/reference for this file, but must not commit real account, partition, hostname, path, or private site data.

### 3.4 Tests

Prefer existing test infrastructure.

Allowed:

- extend `tests/test_skill_update.py`;
- extend `tests/test_standalone_skill_baselines.py`;
- add at most one focused `tests/test_slurm_workflows.py` if it clearly improves separation/readability;
- add deterministic fake Slurm CLI fixtures under existing test fixture conventions.

Do not create a second test framework.

### 3.5 Docs generated/source parity

Update only directly affected human/source metadata, such as:

- `docs/domains/hpc.md`;
- standalone Skill catalog/registry outputs through existing generators;
- local configuration docs.

Do not turn internal execution evidence into README maintenance prose.

### 3.6 Explicitly forbidden implementation scope

Do not modify:

- `YuukiAS/GPT_Codex_AI_Bridge_Kit`;
- Longleaf_Bridge;
- CAT-TRACE / CARE scientific logic;
- other standalone Skills except unavoidable shared environment install parity;
- central Plugin production behavior/topology;
- Host Policy;
- a central cluster registry;
- SSH host management;
- university-document scraping;
- administrator configuration;
- account/QOS associations;
- scheduler configuration.

## 4. Phase A — kickoff preflight and isolation

After the user sends the approved Kickoff:

1. fetch latest `origin/main`;
2. confirm Proposal v0.6, architecture PASS, and exact execution package are present;
3. compare relevant source against package baseline;
4. if compatible, create exactly:
   - `reviewed/hpc--slurm-workflows-routing-refactor`
   - `/tmp/ai-skills-hpc-slurm-workflows-routing-refactor`
5. record kickoff-time main SHA under `results/hpc--slurm-workflows-routing-refactor/`;
6. do not touch real Slurm state during branch bootstrap.

## 5. Phase B — implement generic live-site discovery

Implement a bounded SiteContext discovery path.

### 5.1 Bounded command set

Prefer explicit field whitelists and the minimum controller/database RPCs needed.

Use, where available:

- `sinfo` with explicit `-o/-O` fields for visible/default partitions, state, CPU, memory, GRES/features, time limits, and relevant priority tier;
- `scontrol show partition` for detailed current partition constraints;
- `scontrol show config` only for selected routing/capability fields such as ClusterName, select/scheduler/priority/private-data/accounting capability;
- `sacctmgr show assoc user=$USER` only when SlurmDBD/site permission allows, for account/partition/QOS association facts.

Do not use `sinfo --all` merely to discover hidden partitions.

Do not treat raw `sinfo --json/--yaml` as privacy-minimal. If structured output is used at all, immediately project approved fields and never persist the raw dump.

### 5.2 Fact provenance

Normalize facts as at least:

```text
LIVE_KNOWN
LOCAL_EXPLICIT
PROFILE_POLICY
UNKNOWN
```

Unknown fields stay unknown. Do not fill account/QOS/partition policy with invented defaults.

### 5.3 Local site identity

Resolve in order:

1. existing local stable site id;
2. safe Slurm ClusterName-derived local identity;
3. one-time local alias when ClusterName is unavailable/unsuitable.

A private/raw ClusterName must not be written into tracked repo output when a safe local alias is needed.

### 5.4 Environment CLI

No-profile live site must work:

```text
environment detect
-> plan
-> apply
-> doctor
```

without adding a public profile.

Known profiles attach only as optional policy overlays.

No live scheduler plus insufficient local facts must report runtime unavailable and fail closed for routing mutation rather than pretending the site is configured.

### 5.5 Public/private materialization

The generated installed reference may include:

- local-site locator/alias;
- optional policy-overlay id/revision;
- public-safe hard-policy summary;
- local override locator;
- discovery ownership/availability.

It must not persist raw private hostname/account/QOS/controller/database/path facts into tracked project source.

## 6. Phase C — implement sticky resource contracts

### 6.1 Comparable workload family

At minimum:

```text
project identity
+ entrypoint/job family
+ workload class
+ material scale signature
+ accelerator requirement
```

Dates, seeds, output folders, and route choice do not create new families.

Explicit project/user family id wins. Ambiguous comparability means no automatic accounting merge/right-size.

### 6.2 Contract precedence

1. current explicit user/project resource request;
2. project-owned accepted contract;
3. user-local accepted workload-family contract;
4. initial estimate only if no accepted contract exists.

### 6.3 Frozen fields

At least:

- cpus-per-task;
- memory request and semantics;
- GPU count/type/equivalence requirement;
- batch walltime or persistent availability duration.

### 6.4 Accounting evidence

Read existing `sacct` data when semantically comparable. Do not copy history into a new database.

Carry forward:

- OOM -> memory increase candidate;
- trustworthy comparable high-water >= 85% -> increase candidate;
- approximate increase target 1.25x comparable high-water;
- one low run never decreases memory;
- >=3 comparable successful low-memory runs all below ~50% -> decrease candidate;
- approximate decrease target 1.5x recent high-water;
- multi-task/multi-node MaxRSS must not be treated as whole-allocation memory unless semantics are actually comparable;
- CPU stable-first; CPU efficiency ratio is diagnostic only;
- batch TIMEOUT supports walltime increase;
- persistent availability duration is not derived from batch training elapsed history;
- GPU count/type is never silently downgraded for queue convenience.

Mandatory implementation detail: an OOM increase candidate after rounding must be strictly greater than current accepted memory.

If completed-job `sacct Comment` is unavailable, use conservative matching and do not auto-right-size from ambiguous history.

## 7. Phase D — implement workload mode and local routing preference

### 7.1 Mode classification

- finite unattended -> batch;
- persistent reusable capacity -> persistent allocation;
- short debug -> interactive shell.

The Skill must make this decision before choosing the submission frontend.

### 7.2 Local preference

Candidate routing order is:

1. filter by hard workload/resource requirements;
2. filter by current live legality/visibility and site policy;
3. honor explicit local preferred partition tier;
4. among remaining legal compatible routes, apply optional local accelerator-class preference;
5. use scheduler advisory evidence.

Generic source never contains the user's real deployment partition names or GPU->partition mapping.

If accelerator type is a hard requirement, it cannot be downgraded as a preference. Only user/project-approved equivalence/preference classes may be ordered.

### 7.3 Existing routing safety

Preserve v0.2/v0.6 JobId, dependency, array, transition, native widening, and duplicate-race authority contracts exactly.

## 8. Phase E — implement persistent capacity lifecycle and enrollment

### 8.1 Capacity family

A capacity family binds at least:

- local_site_id;
- stable family id;
- persistent workload mode;
- accepted resource contract / allowed envelope;
- recurrence/timezone/target availability window;
- successor lead time;
- minimum useful duration;
- latest useful end/cutoff;
- activation scope;
- max intended successor = 1;
- auto-maintain preference;
- enrollment scope/actions.

### 8.2 Reconciliation

For a current invocation that activates an enrolled family:

1. discover compatible running allocation;
2. reuse it when it covers the target window sufficiently;
3. discover lifecycle-owned pending successor;
4. if one exists, do not duplicate;
5. find earliest uncovered target;
6. if no successor covers it and enrollment authorizes it, plan/execute exactly one successor;
7. never maintain more than one intended successor.

An unrelated workload on the same site must not activate a GPU family merely because the family is enrolled.

### 8.3 Enrollment authority

`auto_maintain_successor=true` without valid enrollment is read-only proposal mode.

One-time enrollment freezes:

- site/family identity;
- activation scope;
- accepted resource contract / allowed envelope;
- recurrence/window;
- max successor;
- submit-successor permission;
- optional lifecycle-owned stale-successor state-safe cancel/retarget permission.

Same-scope future occurrence does not re-prompt. Material scope expansion invalidates enrollment.

Scope mismatch/stale enrollment fails closed.

Pre-existing jobs are outside lifecycle-owned mutation unless separately proven replaceable and separately authorized.

### 8.4 Calendar semantics

Maintain BEST_EFFORT truth:

- `--begin` is earliest eligibility, not reservation;
- future BeginTime is not claimed to accumulate age unless site configuration actually says so;
- calendar-bounded candidate `--begin + --deadline + --time + --time-min` is used only after target-site capability validation;
- unsupported/ambiguous behavior fails closed rather than returning to drifting fixed-duration weekly jobs;
- no admin reservation path is introduced.

## 9. Phase F — development-local deterministic tests

No real Slurm mutation is allowed merely because these tests pass.

### G1 bank — site isolation + portability

Cover at least:

- generic production source contains no deployment-specific routing constant;
- fake no-profile third-party site derives/accepts local_site_id;
- fake live `sinfo/scontrol` facts produce SiteContext;
- environment plan/apply works without committed profile;
- hidden `scontrol` detail -> UNKNOWN, not guessed;
- missing `sacctmgr` -> association UNKNOWN, not global failure;
- optional policy overlay restricts but does not invent a route;
- public profile list is not required for support;
- private/raw site identity is not written to tracked project output.

### G2 bank — preference routing

Cover:

- P1 immediate;
- P1 delayed/P2 immediate;
- test-only parse failure fail closed;
- fixed partition means no unrequested widening;
- representative fictional PI-like preferred partition ranks before remaining legal routes;
- remaining arbitrary discovered GPU routes may follow local accelerator preference;
- hard accelerator requirement cannot be downgraded;
- route preference never changes resource contract.

Use fictional partition/GPU fixture names rather than current deployment names.

### G3 bank — native widening / JobId

Cover:

- compatible delayed candidates -> one native multi-partition plan;
- in-place update unavailable/unverified -> do not use it for identity-sensitive job;
- downstream dependency -> no unsafe replacement;
- array/dependency/external JobId -> preserve/fail closed;
- PENDING->RUNNING transition -> no cancellation/replacement;
- uncertain old-job cancellation -> no replacement.

### G4 bank — duplicate race authority

Cover:

- unknown/disabled site + local opt-in -> no duplicate;
- explicit site allow + user opt-in is required;
- if duplicate fallback is not implemented for this release, keep capability disabled and record G4 as disabled/NOT_APPLICABLE rather than implementing it for form.

### G5 bank — bounded monitoring/replacement

Cover:

- no tight polling;
- no blind resubmit;
- old-job uncertainty blocks replacement;
- existing triage behavior is not regressed.

### G7 bank — resource stability/right-sizing

Cover:

- same family/no evidence -> exactly same request;
- explicit user/project override wins;
- OOM candidate strictly increases;
- trustworthy high-memory case may increase;
- one low run cannot decrease;
- >=3 comparable low runs may form decrease candidate;
- incomparable MaxRSS -> no automatic resize;
- GPU/IO-bound low CPU efficiency -> no automatic CPU cut;
- TIMEOUT -> walltime increase evidence;
- unavailable Comment/ambiguous family history -> no automatic right-size.

### G8 bank — workload mode/capacity/enrollment

Cover:

- batch vs persistent vs debug classification;
- compatible running allocation reuse;
- current active allocation may satisfy next recurrence regardless of dated job name;
- at most one intended successor;
- existing successor -> no duplicate;
- unenrolled auto-maintain -> read-only;
- enrolled same scope -> one successor mutation allowed without weekly re-prompt;
- unrelated CPU-only task does not activate enrolled GPU family;
- material enrollment scope change -> reauthorize;
- stale scope digest -> read-only;
- BeginTime != reservation;
- calendar-bound unsupported site -> fail closed;
- Bridge intent can be consumed without Bridge changes;
- allocation mode does not claim queue bypass.

Then run current repository validation/full test suite using existing commands.

## 10. G6 — normal installed production identity

G6 is not satisfied by helper/unit tests alone.

Materialize the exact candidate through the real environment/install path and invoke the installed Skill/helper as normal production code.

Required installed scenarios:

### 10.1 Known-profile site fixture

Prove policy overlay + live facts + local preference merge correctly.

### 10.2 No-profile third-party site fixture

Use deterministic fake Slurm CLI executables on PATH:

```text
no committed profile
+ fake live Slurm
+ local site id / local override
-> environment detect/plan/apply/doctor
-> installed slurm-workflows
-> live SiteContext
-> workload/resource contract
-> local preference
-> routing plan
```

This must not require a repository source change for the fake site.

### 10.3 Persistent capacity normal entry

Installed Skill/helper consumes a user-local enrolled capacity fixture, reuses compatible capacity, and plans exactly one missing successor only for a matching workload.

No real third-party cluster is required for G6.

## 11. Real Longleaf validation — bounded, minimized, conditional

No real mutation is authorized while this package is merely being reviewed.

If the user later sends the approved v0.6 Kickoff, it authorizes only the bounded capability probes below, and only after deterministic tests/read-only discovery show they are still needed.

First perform read-only Longleaf discovery with the minimum RPC set. Do not modify any existing job.

Conceptual questions:

- P-A: calendar-bound request semantics;
- P-B: persistent allocation backend/caller lifecycle;
- P-C: pending in-place Partition update.

These are not automatically three jobs.

### 11.1 Combine P-A and P-C when safe

Prefer one held/no-op probe job to answer both:

- controller accepts and exposes the bounded calendar fields needed by the candidate;
- held/PENDING job can safely demonstrate the desired Partition update semantics while preserving JobId.

Probe constraints:

- at most one newly created held batch probe;
- obvious task-owned probe name;
- no scientific payload;
- trivial no-op command;
- minimal request;
- requested walltime <= 5 minutes;
- never intentionally released to RUNNING;
- inspect/update/cancel only this probe JobId;
- cancel and verify inactive before proceeding.

If read-only `sbatch --test-only` is enough to close P-A, do not add extra mutation merely to duplicate evidence.

### 11.2 P-B persistent allocation probe only if still required

At most one additional minimal allocation probe may be used to validate the actual caller/attach/cleanup lifecycle for the candidate persistent backend.

Constraints:

- use the cheapest live legal resource contract sufficient to test allocation lifecycle; prefer CPU-only, not GPU;
- no scientific payload;
- one trivial `srun --jobid` step at most;
- requested walltime <= 5 minutes;
- use a verified bounded wait/immediate mechanism if available; never wait indefinitely;
- cleanup only the task-owned probe allocation;
- verify inactive after cleanup.

If the site cannot provide a cheap bounded probe or the allocation would wait unbounded, skip and leave that backend unverified/fail-closed rather than escalating resources.

### 11.3 Global real-probe limits

For the entire task:

- maximum one held batch probe plus one minimal allocation probe;
- combine questions when one probe safely answers more than one;
- no repeated probe after ambiguous/failing result without new user authorization;
- no existing user job touched;
- no weekly successor submitted;
- no capacity-family enrollment performed on behalf of the user;
- no duplicate race;
- no research GPU computation;
- no account/QOS/association/admin mutation.

Raw site-specific evidence goes only to:

`private/exports/hpc--slurm-workflows-routing-refactor/real-site-probes/`

Public-safe redacted summaries go to:

`results/hpc--slurm-workflows-routing-refactor/real-site-probes/`

Cleanup failure is a blocker and must report the exact task-owned probe JobId.

## 12. Evidence and final-candidate freeze

All task evidence needed by later Critic must remain in repo:

- public-safe evidence: `results/hpc--slurm-workflows-routing-refactor/`
- sensitive/raw site evidence: `private/exports/hpc--slurm-workflows-routing-refactor/`

Before final release validation:

1. finish implementation;
2. run development tests;
3. perform any authorized bounded site probes;
4. fetch current `origin/main`;
5. if relevant semantic drift exists, stop;
6. if only compatible version/docs drift exists, reconcile it before final freeze;
7. compute release versions from actual current release baseline;
8. update release metadata;
9. freeze one exact final candidate SHA.

No production behavior may change after freeze without invalidating final-candidate gates.

## 13. Release metadata before final gates

Because Proposal v0.6 classifies the complete capability as repository MINOR, the frozen release candidate must contain the intended release metadata before G1-G8 final pass.

If release-time actual repository baseline remains `5.1.0`:

`5.1.0 -> 5.2.0`

If it changed:

> compute the next MINOR from the actual release-time VERSION.

Standalone:

`slurm-workflows 0.1 -> 0.2`

Central Plugins:

all `NO_BUMP`

Bridge Kit:

`NO CHANGE`

Use existing version infrastructure only:

- `VERSION`;
- package/setup version parity;
- README repository release;
- README standalone Skill version/description;
- root `CHANGELOG.md`;
- existing registry/catalog/generated validation.

No new version service/schema is allowed.

## 14. Final capability gates on the exact release candidate

Run G1-G8 on the exact versioned/frozen candidate.

Final gate meanings:

- G1: site isolation + generic live discovery/privacy/fail-closed portability;
- G2: local preference routing without resource mutation;
- G3: native widening + JobId/dependency/array/transition safety;
- G4: duplicate-race authority or explicitly disabled/NOT_APPLICABLE capability;
- G5: bounded monitoring/replacement safety;
- G6: real installed normal entry, including no-profile third-party fixture;
- G7: sticky resource contract/right-sizing;
- G8: workload mode + persistent capacity lifecycle + one-time enrollment authority.

Run the repository full suite and version/generated parity after final metadata is present.

## 15. Independent pre-final Critic review

After final candidate freeze and G1-G8 evidence:

Request an independent Critic review of:

- exact final candidate SHA;
- production diff;
- installed final Skill/helper/reference;
- G1-G8 evidence;
- public/private evidence separation;
- any real site probe result and cleanup;
- release/version metadata;
- README/CHANGELOG/generated parity.

Critic must explicitly return final PASS for that candidate before integration to main.

Do not treat architecture PASS or execution-ready PASS as product/release PASS.

## 16. Integration boundary

Development commits/evidence are ordinary non-force pushed only to:

`reviewed/hpc--slurm-workflows-routing-refactor`

After final Critic PASS, the approved Kickoff authorizes ordinary non-force integration of the exact reviewed final candidate to current `main` only when:

- main has no relevant conflicting semantic drift;
- integration does not introduce unreviewed production bytes;
- release version remains the correct next MINOR from the actual baseline.

If main changes in a way that changes the required MINOR target or production semantics, reconcile and rerun affected final gates/review rather than silently merging stale metadata.

No force push.

Final closure verifies remote `main`, repository version, standalone Skill version, README, CHANGELOG, registry/catalog/generated parity, and central Plugin versions.

## 17. Completion contract

The task is complete only when all are true:

- approved v0.6 architecture is implemented;
- generic no-profile Slurm install/environment use works;
- no deployment-specific constants leak into generic production source;
- G1-G8 required gates pass on one exact release candidate;
- any authorized real probe is fully cleaned up;
- final Critic PASS is recorded;
- `slurm-workflows` is released as `0.2`;
- repository is released as the correct next MINOR from actual release-time VERSION;
- all central Plugins remain unchanged in version;
- Bridge Kit remains unchanged;
- exact reviewed candidate is integrated to main;
- remote main/version/README/generated parity is verified.

A local branch, helper test, environment apply, live allocation, or submitted probe is not completion.
