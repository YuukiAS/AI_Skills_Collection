# Clear Writing 真实网页回归与 CI 恢复 Goal v0.1

Status: DRAFT_FOR_CRITIC_REVIEW  
Task: `clear-writing--cross-surface-language-layer`  
Branch: `reviewed/clear-writing--cross-surface-language-layer`

Resume the existing Clear Writing task without redesigning it.

Required outcome:

1. Freeze and use `results/clear-writing--cross-surface-language-layer/REAL_WEB_REGRESSION_BANK_V1.md` as the development known-regression bank.
2. Before any product edit, replay the existing candidate represented by implementation commit `cac70c3bfcce6aeeba9c3e80adfa317235b54ee9` on public-safe derived fixtures for RW-WEB-01..05 and preserve baseline outputs.
3. Merge current `origin/main` normally into the same reviewed branch after the baseline packet is frozen.
4. Repair `response-clarity` only if the frozen known regressions demonstrate a real generic failure. Preserve the RW-WEB-03 positive control and explicit should-not-change cases. Do not use keyword bans, English ratios, fixed length/heading rules, sample-specific project logic or a new skill/router.
5. Close the already-identified full-CI baseline defects without weakening CI:
   - stale repository-version assertion;
   - central-plugin TODO/changelog directory assumption;
   - generated parity/mirror drift.
6. Generated-only synchronization of Presentations / Research Authoring is allowed only if current canonical source mechanically determines the generated result and no source semantics, routing, version or professional behavior changes. Any semantic choice stops and returns to Planner.
7. Run affected focused tests, the five known regressions, should-not-change controls, generator/parity checks, full repository tests and required GitHub CI.
8. Do not perform ChatGPT personal plugin/account mutation, paid review, PIE 0.2, release/version bump, main merge or G7 fresh evaluation in this recovery execution.
9. When the reviewed branch has a full-CI PASS and complete known-regression evidence, stop for the existing independent review path. Do not spend the last Reviewer round on a branch whose full CI still fails.

Success means the task has a clean, reviewable candidate that no longer reproduces the frozen known response-clarity failures and is no longer blocked by the five preexisting CI categories. It does not yet mean ChatGPT Web automatic activation or final product release has passed.
