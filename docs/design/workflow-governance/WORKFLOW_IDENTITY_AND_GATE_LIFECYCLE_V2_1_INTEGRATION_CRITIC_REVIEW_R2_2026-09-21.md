# 工作流命名与插件回归机制完善（AI_Skills + Bridge）— Integration / Release Planning Critic Review R2

- Date: 2026-09-21
- Review role: independent Critic
- Review stage: INTEGRATION_RELEASE_CRITIC_REVIEW_R2
- Human-readable name: **工作流命名与插件回归机制完善（AI_Skills + Bridge）**
- Technical task key: `cross-repo--workflow-identity-gate-lifecycle`
- Reviewed planning commit: `0c3bfe964fac9e14d263e527ba9a41cbb035b179`
- Integration Plan: `docs/design/workflow-governance/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V2_1_INTEGRATION_PLAN_R2_2026-09-21.md`
- Canonical Goal: `docs/goals/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V2_1_INTEGRATION_GOAL_R2.md`
- Kickoff Draft: `docs/operations/prompts/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V2_1_INTEGRATION_KICKOFF_R2.md`
- Prior integration Critic R1: `docs/design/workflow-governance/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V2_1_INTEGRATION_CRITIC_REVIEW_R1_2026-09-21.md`
- Latest AI_Skills main inspected before this review write: `a30eec22b0337008ebde6075bf4d558e989e9cd4`
- Bridge main inspected: `afb2414b6fbe4b2b03292d3b1437d4dd22277fd0`
- Decision: **REVISE**
- Complexity: **APPROPRIATE**
- Scope: integration/release execution package only; implementation PASS remains intact

## 1. Overall judgment

R2 fixes most of the R1 integration concerns correctly.

The four known AI_Skills overlap files are now explicitly covered, with the right intended three-way resolutions:

- keep current main's human-facing README/gallery while applying repository/plugin release values;
- preserve both main's self-contained Planner/Critic handoff wording and candidate v1.4 semantic-task-key/Gate-lifecycle rules;
- preserve the human-facing README gallery regression while also retaining candidate version expectations and workflow-identity/Gate-lifecycle regressions.

The package also adds the right non-destructive release structure:

- clean temporary integration rehearsal;
- real merge history, no rebase/squash/cherry-pick rewrite;
- pre-push source/generated/version/changelog parity and full tests;
- exact integrated commit/tree freeze;
- bounded corrective/revert recovery;
- no force/reset/history rewrite;
- tag/release/publish/deploy kept outside the merge authorization.

Two narrow execution-contract inconsistencies remain. They do not reopen v2.1 or the implementation PASS.

## 2. C-WIGL-INT1-MAIN-DRIFT-OVERLAP-COVERAGE — OPEN

### What R2 fixed

The overlap resolution itself is now adequate. README, Planner contract, Critic contract and marketplace tests are all handled explicitly, and the duplicate-approval TODO is protected.

### Remaining inconsistency

The Plan correctly records two different facts:

- `0a38519...` is the production-source main used for the drift/overlap audit;
- latest main already also contains the R1 Critic review `a30eec22...`.

But Stage 1 still states:

```text
AI_Skills expected base:
0a38519ed051cf01503ba3ed02b5a33b787b9c99
```

and the Goal/Kickoff tuple still presents `0a38519...` as the current main for integration purposes.

That is already stale at review time. More importantly, committing Critic reviews to main naturally advances main with control/docs-only commits. Hard-pinning the integration base to the earlier production-drift SHA would either omit valid main-only review history or cause a pointless re-review loop after every review commit.

### Causal risk

A rehearsal starting from `0a38519...` rather than the actual latest main would not preserve all current-main history, contradicting the package's own preservation requirement.

### Minimum closure

Do not merely replace `0a38519...` with today's latest SHA, because this review itself will advance main again.

Instead distinguish two identities consistently in Plan + Goal + Kickoff:

```text
AI_SKILLS_PRODUCTION_DRIFT_BASE=0a38519ed051cf01503ba3ed02b5a33b787b9c99
AI_SKILLS_INTEGRATION_BASE=<exact latest main resolved at Phase-1 preflight>
```

Required behavior:

1. Phase 1 begins with a read-only fetch/read of actual latest `origin/main`;
2. record that exact SHA as `AI_SKILLS_INTEGRATION_BASE`;
3. preserve all commits on that main ancestry;
4. compare changes since the already-audited production drift base:
   - if they are review/control/planning/TODO/evidence-only and do not alter production/version/release surfaces or the known overlap semantics, carry them forward without reopening architecture;
   - if they touch production/version/release surfaces or materially change one of the overlap resolutions, stop and return to Planner/Critic;
5. build the clean integration worktree from the resolved `AI_SKILLS_INTEGRATION_BASE`, not from hardcoded `0a38519...`.

The same rule should apply generically to Bridge if its main advances before execution.

This closes the real drift problem without creating an infinite “Critic writes a review -> main moved -> plan stale” loop.

## 3. C-WIGL-INT2-MAIN-AS-PRODUCTION-RECOVERY — OPEN

### What R2 fixed

The smoke definition itself is now sufficiently concrete:

- target repo/ref;
- expected versions;
- isolated Codex/Python identity;
- install/upgrade path;
- network and side effects;
- cleanup/restoration;
- no private data / paid review / live-global mutation;
- failure -> no release/publish/deploy + bounded corrective/revert or Planner/Critic return.

### Remaining inconsistency

The Kickoff currently says:

1. obtain authorization for main push;
2. push main;
3. **after main push**, ask for a second authorization for production-identity smoke.

That conflicts with the reason INT2 exists: `main` is already the normal user-consumed Marketplace source. R1 required the smoke to run immediately after main changes. If smoke authorization is only requested after push, main can sit in an unverified state while waiting for another user interaction.

### Causal risk

The user may approve the merge but be unavailable for the subsequent smoke prompt. The normal production source has then changed without the required production-identity check and without a bounded time-to-recovery.

### Minimum closure

Keep merge/push authorization and smoke authorization **separate in scope**, but obtain both before changing main.

After Phase 1 freezes the exact integrated commits/trees, the user request should contain two separately stated approvals:

- **A. Main merge/push**: exact repos, current main SHAs, exact integrated commits/trees, merge/FF method, no release/publish.
- **B. Immediate post-push smoke**: exact AI_Skills/Bridge targets, identities, network/runtime side effects, expected versions and cleanup boundary.

Rules:

- user may approve/deny A and B independently;
- do **not** execute A unless B is also approved for the immediate smoke required by this release contract;
- after A succeeds, execute B immediately without asking the same authorization again;
- if B fails, use the already-defined no-release + corrective/revert recovery;
- tag/GitHub Release/package publish/deploy remains a later separate authorization.

This preserves separate authorization semantics while preventing an avoidable unverified-production window and another duplicate-approval loop.

## 4. Direct regression check

No R2 amendment reviewed here reopens:

- the approved implementation tuple;
- semantic task-key architecture;
- Gate lifecycle;
- G1–G7;
- duplicate-approval TODO ownership;
- 056 isolation;
- no-paid/private/live-global boundaries;
- non-destructive Git requirement.

Bridge's no-drift integration direction remains valid, subject to resolving actual latest main at execution preflight.

Official Git documentation supports the chosen history-preserving direction: a true merge joins diverged histories and records a merge commit, while rebase rewrites history and is risky for already-published branches. citeturn441554search0turn441554search2

## 5. Decision

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

This REVISE is limited to the two execution-contract details above. It does not reopen architecture or implementation acceptance.
