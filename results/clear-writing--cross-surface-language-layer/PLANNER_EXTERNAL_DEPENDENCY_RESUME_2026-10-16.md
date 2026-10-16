# Planner external-dependency resume decision — 2026-10-16

Task: `clear-writing--cross-surface-language-layer`
Reviewed branch: `reviewed/clear-writing--cross-surface-language-layer`
Current Plan: revision `1 / 1`
Review round: `1 / 2`

## Verified external repair

The repository-level source-authority blocker identified in
`GEN_PARITY_SEMANTIC_BLOCKER_2026-10-15.md` has been resolved on main.

Verified main:

`3c3a1a393dd99c40dc641d6b1abc478f14e65a19`

The repair reports and repository state establish:

- the four known repository failures are closed;
- the Marketplace generator is clean and idempotent;
- full repository tests are `338 / 338 PASS`;
- no remaining source-authority blocker is reported.

## Planner decision

No second Clear Writing re-plan is required.

The already-frozen revision-1 Plan explicitly requires the Executor, after the
external source-authority issue is resolved, to consume current main, rerun the
known Web regression bank, preserve the should-not-change controls, run the
full generator/repository checks, and then enter the existing CI/review path.

The Clear Writing product scope, G0-G7 taxonomy, known-regression rubric,
response-clarity repair boundary, account/paid/release boundaries, and
Presentations / Research Authoring semantic ownership are unchanged.

Therefore this is an **external-dependency resume under the unchanged frozen
Plan**, not another material Plan revision.

## Remaining execution

Executor must now:

1. merge `main@3c3a1a393dd99c40dc641d6b1abc478f14e65a19` into the same reviewed branch by ordinary non-force merge;
2. preserve the already committed `response-clarity` repair at
   `0284bb264b56a218a60deb4dfbe56fb66f6b1e6e`;
3. run the post-repair RW-WEB-01..05 batch and all frozen should-not-change controls;
4. require RW-WEB-01,02,04,05 PASS and RW-WEB-03 positive-control preservation;
5. run focused tests, source/generated parity, full Marketplace generation/check, full repository tests and `git diff --check`;
6. publish the resulting implementation candidate and enter
   `WAITING_FOR_CI / ci_status=PENDING`;
7. consume no second Reviewer round until required GitHub CI actually passes.

No PIE 0.2, ChatGPT account mutation, paid review, G7 fresh evaluation,
release/main integration, new skill/router, or adjacent domain redesign is
authorized.

## Control-plane note

The task had already consumed its single material Plan revision before the
external repository dependency was discovered. The current resume does not
change `PLAN.md` or consume another revision; it restores execution of the
same frozen revision-1 contract after the dependency named by that contract was
resolved.

`plan_revision` therefore remains `1`, and `review_round` remains `1`.
