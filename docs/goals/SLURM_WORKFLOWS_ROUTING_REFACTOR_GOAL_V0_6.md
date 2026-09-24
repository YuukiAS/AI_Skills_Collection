# Slurm Workflows Routing Refactor — Canonical Goal v0.6

Target repository: `YuukiAS/AI_Skills_Collection`  
Task key: `hpc--slurm-workflows-routing-refactor`  
Approved architecture: `docs/design/slurm-workflows/SLURM_WORKFLOWS_ROUTING_REFACTOR_PROPOSAL_V0_6_2026-09-24.md`  
Architecture Critic PASS: `docs/design/slurm-workflows/SLURM_WORKFLOWS_ROUTING_REFACTOR_CRITIC_REVIEW_V0_6_2026-09-24.md`  
Execution Plan: `docs/design/slurm-workflows/SLURM_WORKFLOWS_ROUTING_REFACTOR_EXECUTION_PLAN_V0_6_2026-09-24.md`

Exact future branch:

`reviewed/hpc--slurm-workflows-routing-refactor`

Exact future worktree:

`/tmp/ai-skills-hpc-slurm-workflows-routing-refactor`

This Goal is not execution authorization until the exact v0.6 execution package receives independent `READY_FOR_CODEX=YES` and the user then sends the approved v0.6 Kickoff.

## Goal

Release a portable `slurm-workflows 0.2` and corresponding repository MINOR release whose normal installed path can safely operate on known or unknown Slurm clusters without deployment-specific routing constants.

The final product must implement:

```text
live Slurm facts
+ optional public hard-policy overlay
+ user-local facts/preferences
-> SiteContext
-> workload mode
-> sticky resource contract
-> reusable capacity lifecycle when applicable
-> safe routing/widening
```

## Required product capabilities

1. A third-party Slurm site with no committed profile can use environment detect/plan/apply/doctor and the installed normal `slurm-workflows` path.
2. Public site profiles are optional policy overlays, not a supported-server registry.
3. `local_site_id` and optional `policy_overlay_id` remain separate.
4. Generic source contains no deployment-specific partition/host/node/account/QOS/GPU-route constants.
5. Discovery uses bounded read-only Slurm inspection; hidden facts remain UNKNOWN rather than guessed.
6. Fact, policy and preference remain separate.
7. Sticky workload resource contracts remain stable unless explicit override or approved comparable accounting evidence justifies change.
8. OOM right-sizing strictly increases accepted memory after rounding; ambiguous accounting history cannot auto-resize.
9. Finite unattended work routes to batch; persistent reusable capacity routes to persistent allocation mode; short debugging routes to interactive mode.
10. Compatible running persistent allocation is reused before requesting another.
11. Persistent capacity lifecycle maintains at most one intended successor for the earliest uncovered target.
12. `auto_maintain_successor=true` is not mutation authority by itself.
13. One-time bounded family enrollment authorizes same-scope recurring maintenance without weekly re-prompt.
14. Unenrolled monitor/diagnose remains read-only.
15. An unrelated CPU-only workload on the same site does not activate an enrolled GPU family.
16. JobId/dependency/array/running-transition safety remains fail-closed.
17. Duplicate-job race requires explicit site allow plus user/local opt-in; unknown authority disables it.
18. Local partition and accelerator preferences may order legal compatible routes; hard accelerator requirements cannot be downgraded as preferences.
19. G1-G8 pass on one exact final candidate, including no-profile installed normal-entry portability.
20. Bridge Kit remains unchanged.

## Longleaf-specific validation boundary

Longleaf is a current deployment used to validate site behavior, not a generic source of constants.

The final product may use local Longleaf preferences from user-local configuration and live discovery, but may not commit those deployment values as generic defaults.

Real capability probes are bounded by the approved Kickoff and must be minimized/combined. They may not touch existing user jobs or perform research computation.

## Authorization boundary

Before the user sends the approved Kickoff, no reviewed branch/worktree or real Slurm mutation is authorized.

After the approved Kickoff:

- create/use only the exact reviewed branch/worktree;
- modify only Plan-approved source/tests/docs/release files;
- run deterministic tests and read-only scheduler inspection;
- execute only the bounded real probes explicitly authorized by the Kickoff, if still necessary;
- never touch pre-existing user jobs;
- never enroll or maintain the user's real weekly capacity family as part of implementation testing;
- ordinary non-force push only.

## Release contract

Architecture/package docs: `NO BUMP`.

If the complete capability ships:

```text
Repository bump decision: MINOR

If actual release-time VERSION is still 5.1.0:
5.1.0 -> 5.2.0

Otherwise:
next MINOR from actual release-time VERSION

Standalone:
slurm-workflows 0.1 -> 0.2

Central Plugins:
all NO_BUMP

Bridge Kit:
NO CHANGE
```

No new version infrastructure is allowed.

## Completion

This Goal is complete only when:

- approved v0.6 architecture is implemented;
- required deterministic and installed-normal-entry evidence passes;
- G1-G8 pass on the exact versioned final candidate;
- any authorized real site probe is cleaned up and truthfully recorded;
- final independent Critic PASS exists for that candidate;
- README/CHANGELOG/version/registry/catalog/generated parity is correct;
- the exact reviewed final candidate is integrated to main without semantic drift;
- remote main is verified.

Passing unit tests, creating a branch, materializing an environment, or obtaining a Slurm allocation is not completion.
