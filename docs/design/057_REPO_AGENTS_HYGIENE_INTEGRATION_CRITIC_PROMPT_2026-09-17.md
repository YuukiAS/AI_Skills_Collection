# 057 Repo AGENTS Hygiene — Integration Package Critic Review

你是 AI Research Stack 的长期独立 Critic thread。

继续：

TASK_KEY = `057_repo_agents_hygiene`

当前阶段：implementation review PASS -> separately approved integration package review。

本轮只审 integration Plan/Goal/Kickoff 是否允许把 exact reviewed 057 tuple 机械集成到 canonical branches。不要重新设计 057，不修改 repo，不执行 merge/push，不创建 branch/worktree，不 release Bridge，不开始 056，不运行 paid API。

## Review objects

- `docs/design/057_REPO_AGENTS_HYGIENE_INTEGRATION_PLAN.md` v0.1
- `docs/goals/057_REPO_AGENTS_HYGIENE_INTEGRATION_GOAL.md` v0.1
- `docs/operations/prompts/057_REPO_AGENTS_HYGIENE_INTEGRATION_KICKOFF.md` v0.1
- `docs/design/057_REPO_AGENTS_HYGIENE_REVIEW_PACKAGE.md`

## Frozen reviewed tuple

- AI_Skills E3: `745281b70322b8508e43e59a5bdef70529749ea5`
- AI_Skills M3: `24051588d13f07e7f71e0edf5a723aca36754ed5`
- Bridge: `e1d6b781ad7e56d567bed419001069baf439d0a5`
- Bobbio: `ab5dccb6b8b87c49671aa097233ce1bcc38be004`
- Lucerna: `41cd1297af6901531d3135593bc9806bffc38829`
- Mica: `e49416f874f633aedc7521734ee5b0f441aae970`
- Asteria: `0ce1d4daca1e410ce551570578dd563d4ef67e90`
- SeminarArc: `74caaa4ecec16f1bc90987979458d1a4e93f52be`
- CUHK Date inspected-only ref: `711fab75f044b7ad31e5ff8610c076f902ccc949`

Do not reopen I1-I6, Bobbio consolidation or H1-H9 unless this integration package itself contradicts the already-reviewed tuple.

## Mandatory reads

Read latest AI_Skills main:

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- approved 057 v0.2 Plan/Goal and Lite versioning amendment
- current integration Plan/Goal/Kickoff/Review Package

Read current canonical branch heads and exact reviewed commits in:

- AI_Skills_Collection main
- GPT_Codex_AI_Bridge_Kit main
- Bobbio develop
- Lucerna main
- Mica-for-ChatGPT main
- Asteria main
- SeminarArc main

Independently recheck current Git merge behavior from official Git/GitHub documentation where needed. This is a merge/integration review, not a new product architecture round.

## Key questions

### 1. Exact-candidate preservation

Confirm package never rewrites reviewed candidates:

- fast-forward cases use exact reviewed SHA with `--ff-only`;
- no squash/rebase/cherry-pick;
- divergent cases preserve exact candidate as parent/ancestor of a mechanical merge commit;
- no manual content reconciliation is authorized.

### 2. Current canonical reality

Planner observed:

- Bridge/Bobbio/Mica/Asteria/SeminarArc are currently fast-forwardable;
- AI_Skills and Lucerna have diverged only because canonical history advanced independently;
- current AI_Skills canonical changes are outside `results/057_repo_agents_hygiene/`;
- current Lucerna post-base changes do not touch candidate `AGENTS.md`.

Independently verify these facts. If current source has changed again, judge the current state rather than Planner's snapshot.

### 3. Drift stop condition

Check that execution-time preflight is strong enough:

- reviewed task-branch head must equal exact reviewed SHA;
- canonical advancement touching candidate paths or relevant instruction/version/release authority stops integration;
- merge conflict stops integration;
- no candidate repair or new integration branch is allowed;
- disjoint unrelated advancement may remain a mechanical integration only when semantics are still clear.

### 4. Merge method

Judge whether the split is minimal and safe:

- fast-forward exact SHA for non-diverged repos;
- AI_Skills/Lucerna: `--no-ff --no-commit`, inspect staged result / `git diff --cached --check`, commit only if fully mechanical;
- conflict => `git merge --abort` and stop.

Reject if cherry-pick/squash/rebase would be safer under the user's exact-candidate requirement; otherwise confirm the chosen method preserves reviewed history as intended.

### 5. Cross-repo partial integration

Check that package does not pretend multi-repo integration is atomic. It preflights all before first push, then uses normal pushes, never rewrites successful history if a later push fails, and reports partial state honestly.

### 6. Bridge release boundary

Confirm integrating Bridge exact `0.8.3` candidate to main does not silently authorize:

- tag;
- GitHub Release;
- package publish;
- deployment;
- Host Policy install/update;
- `0.8.4` bump.

### 7. No unnecessary re-validation

Implementation/H1-H9 already passed. Confirm integration package appropriately avoids rerunning Bridge 363 tests/product suites merely for ceremony, while still verifying canonical head, exact-candidate reachability, merge tree and diff cleanliness.

If relevant source drift invalidates reviewed evidence, package must stop rather than silently restart development.

### 8. 056 boundary

Confirm integration does not modify or execute 056. Its only next handoff after successful integration is bounded 056 source-drift revalidation/package amendment.

### 9. No scope expansion

Reject any hidden authorization for:

- CUHK Date mutation;
- branch deletion;
- PR creation;
- force push/history rewrite;
- release/deployment;
- new workflow/state/schema/ledger/controller/watcher;
- paid APIs;
- product/runtime edits beyond the exact reviewed commits.

## Output

If integration package has a blocker:

```text
RESULT = REVISE
TASK_KEY = 057_repo_agents_hygiene
REVIEW_STAGE = INTEGRATION_PACKAGE
READY_FOR_INTEGRATION_CODEX = NO
NEXT_HANDOFF = PLANNER
```

Give stable blocker IDs and a complete Planner revision prompt per Critic contract.

If integration package is ready, first explain in normal Chinese:

- which repos can fast-forward;
- why AI_Skills/Lucerna need clean merge commits rather than rewritten candidates;
- what drift/conflict causes a stop;
- what Bridge 0.8.3 integration does and does not authorize;
- why implementation tests/H1-H9 are not rerun by default;
- PASS proves only integration package readiness, not that integration has happened.

Then give:

```text
RESULT = PASS
TASK_KEY = 057_repo_agents_hygiene
REVIEW_STAGE = INTEGRATION_PACKAGE
PLAN = docs/design/057_REPO_AGENTS_HYGIENE_INTEGRATION_PLAN.md
GOAL = docs/goals/057_REPO_AGENTS_HYGIENE_INTEGRATION_GOAL.md
KICKOFF = docs/operations/prompts/057_REPO_AGENTS_HYGIENE_INTEGRATION_KICKOFF.md
READY_FOR_INTEGRATION_CODEX = YES
NEXT_HANDOFF = USER_SENDS_APPROVED_INTEGRATION_KICKOFF
```

Finally return the exact reviewed `## Kickoff` body verbatim:

```text
=== APPROVED 057 INTEGRATION KICKOFF BEGIN ===
<verbatim current kickoff body>
=== APPROVED 057 INTEGRATION KICKOFF END ===
```

Do not create a newer prompt after PASS.
