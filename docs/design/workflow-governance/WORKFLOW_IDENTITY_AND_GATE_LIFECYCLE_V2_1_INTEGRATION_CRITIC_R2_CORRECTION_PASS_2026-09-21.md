# 工作流命名与插件回归机制完善（AI_Skills + Bridge）— Integration Critic R2 Correction

- Date: 2026-09-21
- Review role: independent Critic
- Reviewed planning commit: `0c3bfe964fac9e14d263e527ba9a41cbb035b179`
- Supersedes: `WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V2_1_INTEGRATION_CRITIC_REVIEW_R2_2026-09-21.md`
- Decision: **PASS**

## Correction

The prior R2 REVISE over-classified two coordination details as blocking.

The reviewed Integration Plan R2 already provides the mechanisms required to protect product correctness:

- actual latest-main preflight before integration;
- explicit preservation of main-only work;
- four-file overlap resolution;
- pre-push parity, focused tests and full tests;
- non-rewriting merge history;
- exact integrated result freeze;
- post-main production-identity smoke;
- bounded corrective/revert recovery;
- no force/reset/history rewrite;
- release/publish/deploy kept outside this integration closure.

The previously raised concerns about review-only main SHA movement and the preferred timing of smoke authorization do not introduce a new user-visible capability defect, invalidate the implementation evidence, or create an unbounded/irreversible safety risk. They are therefore non-blocking execution details, not grounds for another planning round.

## Closed findings

```text
C-WIGL-INT1-MAIN-DRIFT-OVERLAP-COVERAGE=CLOSED
C-WIGL-INT2-MAIN-AS-PRODUCTION-RECOVERY=CLOSED
```

The four known overlap surfaces are explicitly covered, and the recovery path is sufficient.

## Approved execution scope

The user may now authorize one bounded closure run covering:

1. clean temporary integration rehearsal from actual latest main;
2. merge approved candidate history without rebase/squash/history rewrite;
3. resolve only the reviewed overlaps and preserve current-main docs/TODO/review work;
4. run required parity/focused/full tests;
5. if green, ordinary non-force push exact integrated commits to both `main` branches;
6. immediately run isolated production-identity smoke for AI_Skills and Bridge;
7. if smoke fails, no release/publish/deploy; preserve evidence and use bounded corrective/revert handling;
8. no tag/GitHub Release/package publish/deploy, no paid review, no private data, no live-global plugin mutation, no 056 execution.

After both main integrations and production-identity smoke PASS, this task's functional integration closure is complete. The next substantive task is **开发交付流程完善（原 056）**, starting with bounded source/version revalidation against the newly integrated mains.

## Decision

```text
DECISION=PASS
COMPLEXITY=APPROPRIATE
C-WIGL-INT1-MAIN-DRIFT-OVERLAP-COVERAGE=CLOSED
C-WIGL-INT2-MAIN-AS-PRODUCTION-RECOVERY=CLOSED
READY_FOR_INTEGRATION_EXECUTION_PACKAGE=YES
READY_FOR_MAIN_MERGE=YES_IF_REHEARSAL_GREEN_AND_USER_SENDS_APPROVED_KICKOFF
READY_FOR_RELEASE_PUBLISH=NO
START_056_NOW=NO
NEXT_HANDOFF=EXECUTOR
```
