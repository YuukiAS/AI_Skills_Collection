# 057 Repo AGENTS Hygiene — Integration Package Critic R2

你是 AI Research Stack 的长期独立 Critic thread。

继续：

TASK_KEY = `057_repo_agents_hygiene`

当前阶段：integration package v0.1 -> narrow R2 review。

本轮只复核一个 stable blocker：

`C057-G1-CLEAN-CANONICAL-WORKTREE-GATE`

不要重新设计 057，不重开 I1-I6/H1-H9，不修改 repo，不执行 merge/push，不创建 branch/worktree，不 release Bridge，不开始 056，不运行 paid API。

## Review objects

- `docs/design/057_REPO_AGENTS_HYGIENE_INTEGRATION_PLAN.md` v0.2
- `docs/goals/057_REPO_AGENTS_HYGIENE_INTEGRATION_GOAL.md` v0.2
- `docs/operations/prompts/057_REPO_AGENTS_HYGIENE_INTEGRATION_KICKOFF.md` v0.2
- `docs/design/057_REPO_AGENTS_HYGIENE_REVIEW_PACKAGE.md`

Prior v0.1 package commit:

`0d84bf541800c1b0bc39d8f15c0a17f72905b1fd`

## Frozen reviewed tuple

- AI_Skills E3: `745281b70322b8508e43e59a5bdef70529749ea5`
- AI_Skills M3: `24051588d13f07e7f71e0edf5a723aca36754ed5`
- Bridge: `e1d6b781ad7e56d567bed419001069baf439d0a5`
- Bobbio: `ab5dccb6b8b87c49671aa097233ce1bcc38be004`
- Lucerna: `41cd1297af6901531d3135593bc9806bffc38829`
- Mica: `e49416f874f633aedc7521734ee5b0f441aae970`
- Asteria: `0ce1d4daca1e410ce551570578dd563d4ef67e90`
- SeminarArc: `74caaa4ecec16f1bc90987979458d1a4e93f52be`
- CUHK Date inspected only: `711fab75f044b7ad31e5ff8610c076f902ccc949`

## Already accepted — do not reopen

Independent v0.1 integration review already accepted:

- Bridge/Bobbio/Mica/Asteria/SeminarArc are exact fast-forward integration cases;
- AI_Skills/Lucerna use clean mechanical merge commits when current non-overlap remains true;
- exact SHA + `--ff-only` candidate preservation;
- no squash/rebase/cherry-pick/force/history rewrite;
- current AI_Skills/Lucerna divergence remains mechanically mergeable;
- all reviewed task-branch heads equal the frozen candidate SHAs;
- push order and truthful partial-integration recovery;
- Bridge `0.8.3` source-only boundary, with no tag/release/publish/deploy/Host install/`0.8.4`;
- no repeated Bridge 363 tests/H1-H9/product tests;
- CUHK Date inspect-only;
- no 056 mutation.

Do not repeat those reviews unless the v0.2 text itself materially contradicts them.

## Mandatory current reads

Read latest AI_Skills main:

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- current integration v0.2 Plan/Goal/Kickoff/Review Package

This is a narrow contract correction. No new external product research is required unless you find a factual Git-semantics conflict in the revised wording.

## R2 questions

### 1. Does C057-G1 close the clean canonical worktree/index gap?

The exact canonical checkout used for integration must now verify before merge:

- intended canonical branch/HEAD;
- no unfinished merge/rebase/cherry-pick/revert/bisect or equivalent Git operation;
- no pre-existing staged changes;
- no pre-existing unstaged tracked changes;
- no untracked path that conflicts with candidate paths, merge outputs, or checkout/merge targets.

The package should require observable evidence such as `git status --porcelain` or an equivalent direct Git check.

### 2. Is dirty user work protected without hidden mutation?

Verify v0.2 explicitly forbids using these merely to make integration proceed:

- `git stash`
- `git reset`
- `git clean`
- committing unrelated work
- moving/overwriting user files
- absorbing unrelated staged/worktree content into a merge commit

Dirty/staged unrelated work must stop that repo and be reported. Conflicting or ambiguous untracked files must also stop rather than being automatically deleted or overwritten.

### 3. Does the gate cover both merge modes and run before the first push?

Check that:

- the same clean-state gate applies to fast-forward repos;
- AI_Skills/Lucerna must pass it before `git merge --no-ff --no-commit`;
- therefore `git merge --abort` begins from a known-clean baseline;
- every mutable repo completes source/drift/identity/clean-state preflight before the first canonical push.

### 4. Did anything else drift?

Compare v0.2 against the frozen v0.1 integration decisions. There must be no substantive change to:

- exact reviewed tuple;
- target canonical branches;
- `FF_ONLY` repos;
- AI_Skills/Lucerna `CLEAN_MERGE` strategy;
- push order;
- partial integration recovery;
- Bridge `0.8.3` source-only boundary;
- no tag/release/publish/deploy/Host install/`0.8.4`;
- no squash/rebase/cherry-pick/force/history rewrite;
- no CUHK Date mutation;
- no 056 changes;
- no repeated tests/H1-H9;
- no H10/state/schema/ledger/controller/watcher;
- no paid API.

If a wording cleanup changes none of those semantics, it is not a blocker.

## Output

If C057-G1 remains open or v0.2 introduces new integration-scope drift:

```text
RESULT = REVISE
TASK_KEY = 057_repo_agents_hygiene
REVIEW_STAGE = INTEGRATION_PACKAGE_R2
C057-G1-CLEAN-CANONICAL-WORKTREE-GATE = OPEN
READY_FOR_INTEGRATION_CODEX = NO
NEXT_HANDOFF = PLANNER
```

Give only blockers directly caused by this narrow revision and, per Critic contract, a complete Planner revision prompt.

If closed:

First explain briefly in normal Chinese:

- how the clean worktree/index gate now works;
- why dirty user work cannot be silently moved or absorbed;
- why AI_Skills/Lucerna now have a credible `merge --abort` baseline;
- that the rest of the integration strategy is unchanged;
- that PASS authorizes only the user to send the integration Kickoff, not the integration itself.

Then give:

```text
RESULT = PASS
TASK_KEY = 057_repo_agents_hygiene
REVIEW_STAGE = INTEGRATION_PACKAGE_R2
C057-G1-CLEAN-CANONICAL-WORKTREE-GATE = CLOSED
PLAN = docs/design/057_REPO_AGENTS_HYGIENE_INTEGRATION_PLAN.md
GOAL = docs/goals/057_REPO_AGENTS_HYGIENE_INTEGRATION_GOAL.md
KICKOFF = docs/operations/prompts/057_REPO_AGENTS_HYGIENE_INTEGRATION_KICKOFF.md
READY_FOR_INTEGRATION_CODEX = YES
NEXT_HANDOFF = USER_SENDS_APPROVED_INTEGRATION_KICKOFF
```

Finally return the exact reviewed `## Kickoff` body verbatim:

```text
=== APPROVED 057 INTEGRATION KICKOFF BEGIN ===
<verbatim current v0.2 kickoff body>
=== APPROVED 057 INTEGRATION KICKOFF END ===
```

Do not create a newer prompt after PASS.
