# 工作流命名与插件回归机制完善（AI_Skills + Bridge）— Integration / Release Planning Critic Review R1

- Date: 2026-09-21
- Review role: independent Critic
- Review stage: INTEGRATION_RELEASE_CRITIC_REVIEW
- Human-readable name: **工作流命名与插件回归机制完善（AI_Skills + Bridge）**
- Technical task key: `cross-repo--workflow-identity-gate-lifecycle`
- Prior implementation Critic PASS:
  `docs/design/workflow-governance/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V2_1_IMPLEMENTATION_CRITIC_REVIEW_R2_2026-09-21.md`
- AI_Skills approved production candidate: `ce63f50238555849a48256068e6fa0d46e21a97b`
- AI_Skills approved evidence tip: `871489ee227dee773c8fff3c161bd5743da739c7`
- Bridge approved production candidate: `7f2707dd4020951650d561303c82a17e22b27317`
- Bridge approved evidence tip: `d09306f180634aa4d4ad4ec3ee46295a8b20945b`
- AI_Skills latest main inspected: `0a38519ed051cf01503ba3ed02b5a33b787b9c99`
- Bridge latest main inspected: `afb2414b6fbe4b2b03292d3b1437d4dd22277fd0`
- Decision: **REVISE**
- Complexity: **APPROPRIATE**
- Scope: integration/release planning only; no merge/release authorization

## 1. Bottom line

The proposed integration direction is correct:

- preserve candidate history rather than rebase/squash it;
- preserve main-only README/refactor/review/TODO work;
- keep the new human-facing README structure while applying the candidate's release/plugin versions;
- Bridge can integrate against unchanged main;
- post-integration parity/install/upgrade smoke is required;
- merge/push, tag/release, publish/deploy, and fresh runtime/API smoke remain separate authorization boundaries.

However, the current plan is not yet complete enough for execution. Current AI_Skills main has materially advanced beyond the candidate base, and the overlap is broader than README alone. In addition, because `main` is itself the normal Marketplace source, the plan needs an explicit post-merge failure/recovery boundary before any merge can be authorized.

## 2. Verified current-source facts

### AI_Skills

Current main is `0a38519e...`, after the human-facing README refactor was actually integrated through PR #3.

The reviewed candidate branch and current main are now diverged:

- candidate branch: 3 commits ahead of their merge base;
- current main: 14 commits ahead of the same merge base;
- merge base: `2b6a5b50...`.

Current canonical release/version slots on main are still unconsumed:

- Repository: `5.0.5`
- workflow-core: `0.1`
- ai-skills-core: `0.2`

The duplicate-approval TODO commit `9d145db...` is an ancestor of current main and therefore must be preserved.

### Bridge

Bridge main remains `afb2414...`, the same baseline used by the candidate. The reviewed branch is ahead of main with no main-side production drift.

## 3. Blocking finding C-WIGL-INT1-MAIN-DRIFT-OVERLAP-COVERAGE

**Requirement**

Integration must preserve both the approved candidate behavior and all valid current-main work.

**Observed source**

Since the common merge base, both AI_Skills main and the candidate branch changed these overlapping paths:

1. `README.md`
2. `docs/workflows/PLANNER_ROLE_CONTRACT.md`
3. `docs/workflows/CRITIC_ROLE_CONTRACT.md`
4. `tests/test_codex_marketplace.py`

The current plan explicitly names only the README conflict.

The test overlap is substantive:

- current main replaced the old README release-dashboard test with the new human-facing plugin-gallery test;
- candidate branch changes plugin-version expectations and adds workflow-identity/Gate-lifecycle contract regression coverage.

The role-contract overlap is also semantically meaningful:

- current main makes Planner/Critic handoff prompts self-contained rather than README-template-dependent;
- candidate adds semantic task-key / Gate-lifecycle rules and advances those contracts to v1.4.

**Causal risk**

A merge that only consciously resolves README can silently lose either:

- the new human-facing README regression;
- candidate version expectations / Gate-lifecycle regression;
- main's self-contained handoff wording;
- candidate semantic task-key / Gate-lifecycle contract.

Tests may also fail after integration even if README itself looks correct.

**Minimum closure**

Revise the integration plan to require an explicit three-way overlap audit from the real merge base before mutation.

At minimum, specify resolution for all four overlapping files:

- `README.md`: keep current main human-facing structure; apply repository `5.0.6`, workflow-core `0.2`, ai-skills-core `0.3` values and any required release wording.
- `PLANNER_ROLE_CONTRACT.md`: preserve current main self-contained handoff wording **and** candidate v1.4 semantic task-key / Gate-lifecycle additions.
- `CRITIC_ROLE_CONTRACT.md`: preserve current main self-contained handoff wording **and** candidate v1.4 semantic task-key / Gate-lifecycle additions.
- `tests/test_codex_marketplace.py`: preserve the current human-facing plugin-gallery test while applying candidate version expectations and retaining the workflow-identity/Gate-lifecycle regression test.

After conflict resolution, run the affected focused tests plus the full AI_Skills suite on the integrated tree.

Do not assume README is the only conflict just because it is the most visible one.

## 4. Blocking finding C-WIGL-INT2-MAIN-AS-PRODUCTION-RECOVERY

**Requirement**

The release contract requires post-integration production-identity install/upgrade smoke. The normal Marketplace source itself points to `main`.

**Observed source**

Current README instructs consumers to use:

`Source: https://github.com/YuukiAS/AI_Skills_Collection.git`
`Ref: main`

The version policy says repository version identifies the formal installable release, and candidate replay policy says final closure still requires a real released/production-identity install or upgrade smoke.

The proposed plan says “merge to main, then post-integration parity and install/upgrade smoke before release,” but it does not define the failure/recovery semantics once `main` has already changed.

**Causal risk**

Pushing the merge changes the normal user-consumed source before the final production-identity smoke is known to pass. A failed smoke would otherwise leave a known-bad candidate on main while the plan has no defined recovery path.

**Minimum closure**

Keep the separate-authorization model, but make the integration sequence explicit:

1. **Pre-push integration rehearsal:** on a clean temporary integration worktree based on exact latest main, merge the approved candidate history without rebase/squash, resolve all overlaps, and run full source/generated/version/changelog parity plus full tests.
2. **Critic-reviewed exact merge result / integration commit:** identify the exact integrated tree/commit intended for main.
3. **User authorization for merge/push** only after that rehearsal is green.
4. **Push/merge to main.**
5. **Immediately run the explicitly authorized production-identity install/upgrade smoke** against the new main.
6. If smoke fails:
   - no tag/release/publish/deploy;
   - preserve failure evidence;
   - recover with a bounded corrective/revert commit or return to Planner/Critic;
   - no force/reset/history rewrite.
7. Only after smoke PASS may a separate tag/GitHub Release/package publish/deploy authorization be considered.

The exact smoke target, Codex identity, install/upgrade path, expected versions, and restoration boundary must be written into the integration Goal/Kickoff. A fresh runtime/API smoke is not implicitly authorized by the planning review.

Git's official merge documentation supports this direction: a true merge combines both diverged histories in a merge commit, while rebase rewrites published history; conflict resolution should happen explicitly on a clean tree.

## 5. Bridge disposition

The Bridge side of the plan is directionally sufficient:

- current main has not drifted;
- candidate history can be integrated without rebase/squash;
- `0.8.3 -> 0.8.4` remains the current slot;
- post-integration full tests/version/changelog/install smoke remain required.

The execution package should still name the exact merge/fast-forward method and post-main smoke/recovery boundary, but no new Bridge architecture work is needed.

## 6. Decision

```text
DECISION=REVISE
COMPLEXITY=APPROPRIATE
C-WIGL-INT1-MAIN-DRIFT-OVERLAP-COVERAGE=OPEN
C-WIGL-INT2-MAIN-AS-PRODUCTION-RECOVERY=OPEN
READY_FOR_INTEGRATION_EXECUTION_PACKAGE=NO
READY_FOR_MAIN_MERGE=NO
READY_FOR_RELEASE=NO
START_056_NOW=NO
NEXT_HANDOFF=PLANNER
```

This REVISE does not reopen v2.1 architecture or the implementation PASS. It only requires the integration/release Plan + Goal + Kickoff to reflect the current main drift and the real main-as-production recovery boundary.
