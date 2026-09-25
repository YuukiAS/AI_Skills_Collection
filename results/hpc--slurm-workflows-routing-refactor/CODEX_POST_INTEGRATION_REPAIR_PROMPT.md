# Slurm Workflows v0.2 — Post-integration Repair Prompt

Repository: `YuukiAS/AI_Skills_Collection`  
Task key: `hpc--slurm-workflows-routing-refactor`  
Audit baseline main: `72690e43664367e95fcca83bb1c72c6fadd8f77f`  
Existing reviewed branch: `reviewed/hpc--slurm-workflows-routing-refactor`  
Existing worktree: `/tmp/ai-skills-hpc-slurm-workflows-routing-refactor`

This is the same task, not a successor and not a new architecture round. Reuse the existing reviewed branch/worktree. Preserve Proposal v0.6 semantics. Do not modify Bridge Kit, Longleaf_Bridge, scientific project logic, Host Policy, central Plugin topology, or any unrelated repository.

## 1. Read first

Fetch latest `origin/main`, `origin/release`, and the reviewed branch. Read current:

- `AGENTS.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md`
- `docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md`
- `docs/design/slurm-workflows/SLURM_WORKFLOWS_ROUTING_REFACTOR_PROPOSAL_V0_6_2026-09-24.md`
- `docs/design/slurm-workflows/SLURM_WORKFLOWS_ROUTING_REFACTOR_CRITIC_REVIEW_V0_6_2026-09-24.md`
- current Slurm production source/tests/result evidence.

If relevant Slurm semantics changed after the audit baseline, stop and report instead of overwriting newer work.

## 2. Repair the missing production capabilities

### A. Persist sticky workload/capacity state

Implement the approved user-local current-state contract:

`~/.config/ai-skills/slurm-workflows.toml`

It must actually load/persist:

- accepted workload-family resource contracts;
- capacity-family current configuration;
- bounded enrollment scope/digest;
- optional evidence locator.

No history database. Historical runtime evidence remains in Slurm accounting.

Prove across independent loads that the same workload reuses the exact accepted CPU/memory/GPU/walltime unless explicit override or approved comparable evidence changes it.

### B. Implement real calendar-aware persistent capacity reconciliation

Current capacity logic must not treat “compatible RUNNING GPU” as sufficient by itself.

Production reconciliation must consume the approved calendar semantics, including:

- recurrence;
- target availability occurrence;
- `target_ready_by`;
- `successor_lead_time`;
- `minimum_useful_duration`;
- latest useful end/cutoff;
- earliest uncovered recurrence.

A running allocation whose remaining lifetime cannot cover the next target window must not satisfy that target.

Maintain at most one lifecycle-owned intended successor. Dated job display names are not capacity identity.

Calendar-bound submission options such as `--deadline` / `--time-min` remain fail-closed unless target-site capability is verified.

### C. Fix enrollment authorization

A mutation-capable enrollment must require an exact valid `scope_digest`.

- missing digest -> invalid/read-only;
- mismatched/stale digest -> invalid/read-only;
- matching digest + bounded submit permission + max successor 1 -> eligible.

Changing resource envelope, recurrence/window, site/family identity, or action scope must invalidate the old authorization.

### D. Restore the approved routing/config contract

Fresh config generation must stop emitting obsolete universal defaults such as:

- `race_after_minutes = "60"`;
- generic `race_cancel_policy`.

Legacy fields may remain readable for compatibility but are not new defaults.

Reconcile current local routing vocabulary with the approved architecture; do not leave obsolete and replacement semantics half-wired.

Doctor requiredness must be site-aware. Remove the generic assumption that every Slurm site requires the same `account / partition / qos / scratch_root / module_init` set. Derive requiredness from live facts, public hard constraints, and explicit local facts; unknown stays unknown.

### E. Make G6 a real installed normal-entry path

The no-profile path must genuinely run:

fake Slurm CLI on PATH
-> environment detect
-> plan
-> apply
-> doctor
-> installed `slurm-workflows`
-> installed live discovery
-> resolved SiteContext
-> local preference
-> routing plan

Do not manually inject a scheduler-partition dictionary after installation.

Required installed scenarios:

1. no committed profile / arbitrary third-party cluster;
2. known public overlay + distinct local site id;
3. no-profile local site + optional public overlay;
4. hidden partition detail / unavailable association -> UNKNOWN, no guessing.

`environment detect` itself must recognize usable live Slurm even when no committed profile matches.

### F. Enforce public-safe generated artifacts

Repo-targeted generated references/manifests must not expose:

- private hostname/controller/db host;
- account/QOS;
- arbitrary absolute private paths;
- raw private ClusterName when it should remain local.

Use public-safe logical locators/aliases. Add regression tests with obviously private fake values.

## 3. Formal release closure

At audit time:

- `main` claims repository `5.3.0` / `slurm-workflows 0.2`;
- formal `release` still points to repository `5.2.2` / `slurm-workflows 0.1`.

Do **not** advance `release` before the repaired final candidate passes G1-G8 and independent final Critic review.

Keep repository version at the correct current formal target; do not invent another bump merely because this pre-release implementation needs repair. If canonical VERSION has changed since the audit, stop and recompute under the version policy.

After final Critic PASS, only then integrate the exact reviewed candidate if needed and fast-forward `release` to the exact formally closed release commit. Verify remote `release`.

## 4. Durable result / tracking truth

Current `results/hpc--slurm-workflows-routing-refactor/RESULT.md` still records a pre-final state. Replace that with truthful durable evidence as the repair proceeds.

Before final review, record the exact candidate SHA and G1-G8 evidence.

After actual closure, durable evidence must truthfully include:

- final Critic PASS;
- exact integrated main SHA;
- exact formal release SHA;
- repository release version;
- standalone `slurm-workflows` version;
- real-probe status.

Read `AI_SKILLS_MAINTENANCE_BOARD.md`. Reuse an existing top-level maintenance tracking Issue if present; otherwise create/bind one top-level Slurm Workflows item, not one Issue per blocker. Keep the source backlink / Project lifecycle truthful. If Project mutation is unavailable, report the exact pending Project mutation rather than claiming sync.

## 5. Real Slurm boundary

This repair authorizes **no new real Slurm mutation**.

Do not run real `sbatch`, `salloc`, `scancel`, modify existing jobs, or enroll the user's real weekly GPU family.

Use deterministic fake Slurm fixtures and read-only inspection. If a real mutation becomes genuinely unavoidable, stop and request exact bounded authorization.

## 6. Required validation

At minimum rerun:

- `python -m unittest tests.test_slurm_workflows`
- `python -m unittest tests.test_skill_update`
- `python scripts/skills.py validate`
- `python scripts/skills.py audit --all`
- `python scripts/build_codex_marketplace.py --write --validate --check --path-report`
- `python -m unittest discover -s tests`

Rebuild G1-G8 evidence on **one exact repaired candidate**.

Extra required proofs:

- G6 is true installed end-to-end normal entry;
- G7 proves persisted sticky contracts across independent loads;
- G8 proves calendar-aware coverage + exact-digest enrollment fail-closed behavior.

## 7. Git / final handoff

Use only the existing:

- branch: `reviewed/hpc--slurm-workflows-routing-refactor`
- worktree: `/tmp/ai-skills-hpc-slurm-workflows-routing-refactor`

Ordinary non-force push only. Do not delete the reviewed branch.

Before independent final review:

1. finish repair;
2. commit/push exact reviewed branch;
3. verify remote branch tip;
4. freeze one exact candidate SHA;
5. write durable evidence;
6. stop and request independent Critic review.

Do not self-approve or advance `release` before that review.

Final pre-Critic report must include at least:

```text
RESULT = READY_FOR_FINAL_CRITIC | REVISE
FINAL_CANDIDATE =
STICKY_STATE_PERSISTENCE =
CALENDAR_CAPACITY_COVERAGE =
ENROLLMENT_DIGEST_FAIL_CLOSED =
LEGACY_CONFIG_CLEANUP =
DOCTOR_SITE_AWARE =
G6_TRUE_NORMAL_ENTRY =
PUBLIC_SAFE_GENERATED_REFERENCE =
G1 =
G2 =
G3 =
G4 =
G5 =
G6 =
G7 =
G8 =
REAL_SLURM_MUTATION = NO
REPOSITORY_VERSION =
SLURM_WORKFLOWS_VERSION =
FULL_TEST_SUITE =
TRACKING_ISSUE =
PROJECT_STATUS =
FINAL_CRITIC = PENDING
INTEGRATED_TO_MAIN = NO
FORMAL_RELEASE_ADVANCED = NO
```

Then provide the exact independent Critic review prompt for that candidate.
