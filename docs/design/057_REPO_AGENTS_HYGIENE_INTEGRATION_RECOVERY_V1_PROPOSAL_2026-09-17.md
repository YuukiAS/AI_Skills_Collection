# 057 Repo AGENTS Hygiene — Integration Recovery V1 Proposal

- Task key: `057_repo_agents_hygiene`
- Date: 2026-09-17
- Status: `DRAFT_FOR_CRITIC_REVIEW`
- Scope: integration recovery only; no 057 redesign, no candidate mutation, no 056 work

## 1. Why the current integration execution is over-coupled

The reviewed 057 implementation is already complete and independently accepted. The current blocker is not AGENTS quality or H1-H9. It is the integration execution surface.

The approved integration v0.2 required all repositories to use a clean canonical local checkout before the first push. That correctly protected dirty user work, but it coupled unrelated local workstation state to remote integration:

- AI_Skills local `main` is a stale/diverged user checkout with old unrelated 044 commits. It must not be reset/rebased/cleaned for 057.
- Bridge local canonical `main` has a pre-existing `.gitignore` modification. 057 must not stash/reset/clean/commit it.
- Remote reviewed branches and remote canonical refs remain usable.

The result is repeated Goal blocking even though the reviewed commits themselves remain valid.

## 2. Current remote facts rechecked by Planner

At this proposal round:

- AI_Skills remote `main = d73684fe59f2866d551fcbfae750cada4b3fd4ae`; reviewed branch still points exactly to `M3 = 24051588d13f07e7f71e0edf5a723aca36754ed5`. They are diverged, and M3 adds only `results/057_repo_agents_hygiene/*` relative to the 057 base.
- Bridge remote `main = cb77b1cc5a1fce097a38066d2db452291e359852`; reviewed branch = `e1d6b781ad7e56d567bed419001069baf439d0a5`; candidate is still a pure fast-forward.
- Bobbio `develop` -> `ab5dccb6b8b87c49671aa097233ce1bcc38be004`: still pure fast-forward.
- Mica `main` -> `e49416f874f633aedc7521734ee5b0f441aae970`: still pure fast-forward.
- Asteria `main` -> `0ce1d4daca1e410ce551570578dd563d4ef67e90`: still pure fast-forward.
- SeminarArc `main` -> `74caaa4ecec16f1bc90987979458d1a4e93f52be`: still pure fast-forward.
- Lucerna current remote `main` has advanced from the old 057 base, while reviewed branch remains `41cd1297af6901531d3135593bc9806bffc38829`. The current main-side post-base changes still do not touch `AGENTS.md`; a clean mechanical merge remains plausible.
- CUHK Date remains inspect-only and is not part of integration.

## 3. Simpler recovery mechanism

Replace the single cross-repo canonical-checkout orchestration with **independent per-repository integration prompts**, all reviewed together once.

This does not change any reviewed candidate, canonical target branch, H1-H9 result, Bridge version, release boundary, or 056 sequencing. It changes only the local execution surface and removes the global “all canonical checkouts clean before any push” coupling.

### 3.1 Five fast-forward repositories

For Bridge, Bobbio, Mica, Asteria and SeminarArc:

- run from the existing `reviewed/057_repo_agents_hygiene` repository/worktree or any existing checkout that can resolve the exact immutable candidate object;
- do **not** switch to or modify the dirty canonical local checkout;
- `git fetch origin`;
- verify `origin/reviewed/057_repo_agents_hygiene` equals the frozen candidate SHA;
- verify the current remote canonical ref is an ancestor of the candidate;
- push the immutable commit directly to the canonical remote ref:
  - `git push origin <EXACT_SHA>:refs/heads/main`, or Bobbio `...:refs/heads/develop`;
- do not use force.

A direct push of an explicit commit object does not consume the local working tree/index. Git's normal branch update rule rejects a non-fast-forward push unless force is used. Therefore Bridge's unrelated local `.gitignore` modification does not need to be moved, stashed, reset, committed, or inspected as integration input.

If the remote canonical ref advanced so that the update is no longer fast-forward, stop only that repo and return the exact remote state.

### 3.2 Two diverged repositories

AI_Skills and Lucerna need a real merge commit because canonical remote history advanced independently.

Do not repair or use their problematic canonical local checkout. Instead use the **existing reviewed 057 worktree** as the integration surface:

1. verify the reviewed worktree itself is clean enough to switch safely and is on/resolves the exact frozen reviewed branch;
2. fetch `origin`;
3. verify the reviewed remote branch still equals the exact frozen candidate;
4. verify the relevant path non-overlap still holds;
5. `git switch --detach origin/main` — no new branch/worktree;
6. `git merge --no-ff --no-commit <EXACT_REVIEWED_SHA>`;
7. conflict or semantic uncertainty -> `git merge --abort`, switch back to `reviewed/057_repo_agents_hygiene`, stop this repo;
8. otherwise inspect the staged merge, run `git diff --cached --check`, make no manual content edits, commit the mechanical merge;
9. `git push origin HEAD:refs/heads/main` without force;
10. switch the reviewed worktree back to `reviewed/057_repo_agents_hygiene`.

For AI_Skills specifically, the stale/diverged local `main` with old 044 commits is left completely untouched. For Lucerna, current canonical product changes are preserved as the first-parent side of the merge.

If the existing reviewed worktree itself has unrelated dirty changes that make detach/merge unsafe, stop that repo. Do not create another worktree automatically under this recovery.

## 4. Why this is simpler and still safe

The previous package tried to preflight all repositories before the first push to reduce partial integration. But Git cannot make updates across separate repositories/remotes atomic. The approved recovery already required truthful reporting of partial integration.

This proposal therefore prefers **repo-local failure isolation**:

- one dirty checkout cannot block six unrelated repos;
- easy fast-forward integration does not touch a working tree at all;
- only the two repositories that actually need merge commits require a clean integration worktree;
- remote fast-forward rejection remains the safety boundary for concurrent remote advancement;
- exact reviewed commit identity is preserved.

This is a recovery simplification, not a new workflow/state/ledger/controller and not a successor task.

## 5. Frozen boundaries

Remain unchanged:

- exact reviewed tuple and `M3`;
- canonical targets: Bridge/main, Bobbio/develop, Lucerna/main, Mica/main, Asteria/main, SeminarArc/main, AI_Skills/main;
- CUHK Date untouched;
- no candidate content changes;
- no H1-H9 rerun and no Bridge 363-test rerun;
- Bridge stays `0.8.3` source-only: no tag, GitHub Release, package publish, deployment, Host install/update, or `0.8.4`;
- no branch deletion, PR, squash, rebase, cherry-pick, force push, reset/clean/stash of unrelated user work;
- no paid API;
- no 056 modification/execution during 057 integration;
- after successful 057 integration: bounded 056 source-drift revalidation.

## 6. Execution order

After one independent Critic PASS on this recovery package, the user may send the following repo prompts independently.

Recommended order:

1. Bobbio
2. Mica
3. Asteria
4. SeminarArc
5. Bridge
6. Lucerna
7. AI_Skills last

A failure in one prompt does not invalidate already successful repo integrations. Report it and continue only if the user chooses to send another already-approved repo prompt; do not improvise a new recovery for the failed repo.

## 7. Exact per-repo prompts for Critic review

### Prompt A — Bobbio

```text
TASK_KEY = 057_repo_agents_hygiene
MODE = approved per-repo integration recovery
REPO = YuukiAS/Bobbio
TARGET = develop
EXACT_CANDIDATE = ab5dccb6b8b87c49671aa097233ce1bcc38be004

只做这个repo的057 integration。不要修改candidate内容，不创建branch/worktree，不改Figma/product/runtime/version，不开始056。

从现有repo/worktree执行：
1. git fetch origin
2. 验证 origin/reviewed/057_repo_agents_hygiene == EXACT_CANDIDATE
3. 验证 origin/develop 是 EXACT_CANDIDATE 的ancestor；否则停止并报告
4. 不需要checkout/修改本地develop；直接：
   git push origin ab5dccb6b8b87c49671aa097233ce1bcc38be004:refs/heads/develop
5. 禁止force
6. fetch并验证 origin/develop == EXACT_CANDIDATE

本prompt不授权清理/stash/reset任何unrelated local work；也不删除reviewed branch。

返回 old/new remote develop、push结果和exact candidate identity。
```

### Prompt B — Mica

```text
TASK_KEY = 057_repo_agents_hygiene
MODE = approved per-repo integration recovery
REPO = YuukiAS/Mica-for-ChatGPT
TARGET = main
EXACT_CANDIDATE = e49416f874f633aedc7521734ee5b0f441aae970

只做这个repo的057 integration。不要修改AGENTS/candidate/runtime/version，不创建branch/worktree，不开始056。

1. git fetch origin
2. 验证 origin/reviewed/057_repo_agents_hygiene == EXACT_CANDIDATE
3. 验证 origin/main 是 EXACT_CANDIDATE 的ancestor；否则停止
4. 不切换或清理canonical local main；直接：
   git push origin e49416f874f633aedc7521734ee5b0f441aae970:refs/heads/main
5. 禁止force
6. fetch并验证 origin/main == EXACT_CANDIDATE

不得stash/reset/clean/commit unrelated local work。返回old/new remote main和push结果。
```

### Prompt C — Asteria

```text
TASK_KEY = 057_repo_agents_hygiene
MODE = approved per-repo integration recovery
REPO = YuukiAS/Asteria
TARGET = main
EXACT_CANDIDATE = 0ce1d4daca1e410ce551570578dd563d4ef67e90

只做这个repo的057 integration，不修改candidate、product/runtime、prompts/AGENT_RULES.md，不创建branch/worktree，不开始056。

1. git fetch origin
2. 验证 origin/reviewed/057_repo_agents_hygiene == EXACT_CANDIDATE
3. 验证 origin/main 是 EXACT_CANDIDATE 的ancestor；否则停止
4. 直接：
   git push origin 0ce1d4daca1e410ce551570578dd563d4ef67e90:refs/heads/main
5. 禁止force
6. fetch并验证 origin/main == EXACT_CANDIDATE

不要清理/移动/提交unrelated local work。返回old/new remote main和push结果。
```

### Prompt D — SeminarArc

```text
TASK_KEY = 057_repo_agents_hygiene
MODE = approved per-repo integration recovery
REPO = YuukiAS/SeminarArc
TARGET = main
EXACT_CANDIDATE = 74caaa4ecec16f1bc90987979458d1a4e93f52be

只做这个repo的057 integration。不要修改AGENTS/DEVICE_TESTING或Android/runtime/product，不创建branch/worktree，不开始056。

1. git fetch origin
2. 验证 origin/reviewed/057_repo_agents_hygiene == EXACT_CANDIDATE
3. 验证 origin/main 是 EXACT_CANDIDATE 的ancestor；否则停止
4. 直接：
   git push origin 74caaa4ecec16f1bc90987979458d1a4e93f52be:refs/heads/main
5. 禁止force
6. fetch并验证 origin/main == EXACT_CANDIDATE

不得碰真机/Emulator；这是纯Git integration。返回old/new remote main和push结果。
```

### Prompt E — Bridge

```text
TASK_KEY = 057_repo_agents_hygiene
MODE = approved per-repo integration recovery
REPO = YuukiAS/GPT_Codex_AI_Bridge_Kit
TARGET = main
EXACT_CANDIDATE = e1d6b781ad7e56d567bed419001069baf439d0a5
VERSION = 0.8.3 source candidate

只做Bridge的057 source integration。不要修改candidate，不清理当前canonical checkout里的`.gitignore`或其他dirty work，不创建branch/worktree，不开始056。

1. git fetch origin
2. 验证 origin/reviewed/057_repo_agents_hygiene == EXACT_CANDIDATE
3. 验证 origin/main 是 EXACT_CANDIDATE 的ancestor；否则停止
4. 不checkout/修改dirty canonical main；直接：
   git push origin e1d6b781ad7e56d567bed419001069baf439d0a5:refs/heads/main
5. 禁止force
6. fetch并验证 origin/main == EXACT_CANDIDATE
7. 只读确认main中的version surfaces为0.8.3

明确禁止tag/GitHub Release/package publish/deploy/Host install/update/0.8.4。返回old/new remote main和version identity。
```

### Prompt F — Lucerna

```text
TASK_KEY = 057_repo_agents_hygiene
MODE = approved per-repo integration recovery
REPO = YuukiAS/Lucerna
TARGET = main
EXACT_CANDIDATE = 41cd1297af6901531d3135593bc9806bffc38829
REVIEWED_BASE = 760931ae8a1f0edffefe41c83c1667c7190c3014

只做Lucerna的057 integration。保留当前main上的后续product/closure commits；不得修改057 candidate或产品/runtime。

使用现有 reviewed/057_repo_agents_hygiene worktree，不使用/清理别的canonical checkout，不创建新branch/worktree。

1. 确认当前这个reviewed worktree没有uncommitted/staged changes，也没有unfinished Git operation；不干净就停止
2. git fetch origin
3. 验证 origin/reviewed/057_repo_agents_hygiene == EXACT_CANDIDATE
4. 验证从 REVIEWED_BASE 到 origin/main 的main-side变化仍未修改 AGENTS.md；若已修改或语义不确定则停止
5. git switch --detach origin/main
6. git merge --no-ff --no-commit 41cd1297af6901531d3135593bc9806bffc38829
7. conflict/任何手工reconciliation需求 => git merge --abort；git switch reviewed/057_repo_agents_hygiene；停止
8. 检查staged merge和 git diff --cached --check；不得手工编辑内容
9. commit纯机械merge
10. git push origin HEAD:refs/heads/main；禁止force
11. fetch并验证EXACT_CANDIDATE在origin/main ancestry中
12. git switch reviewed/057_repo_agents_hygiene

返回old/new remote main、merge commit SHA、candidate reachability。若push因remote再次前进被拒绝，禁止force，切回reviewed branch并报告。
```

### Prompt G — AI_Skills last

```text
TASK_KEY = 057_repo_agents_hygiene
MODE = approved per-repo integration recovery
REPO = YuukiAS/AI_Skills_Collection
TARGET = main
EXACT_CANDIDATE_M3 = 24051588d13f07e7f71e0edf5a723aca36754ed5
REVIEWED_BASE = e8ba751561c9e61a5b0bbd094d2c280ff0b00b59

只做AI_Skills的057 evidence integration。不要修改057 candidate、current main docs/TODO、任何plugin production或056。

本机普通local main含旧044 commits且严重diverged；不要reset/rebase/clean/stash/merge/修复该local main。使用现有 reviewed/057_repo_agents_hygiene worktree 作为独立integration surface，不创建新branch/worktree。

1. 确认这个reviewed worktree自身没有uncommitted/staged changes，也没有unfinished Git operation；不干净就停止
2. git fetch origin
3. 验证 origin/reviewed/057_repo_agents_hygiene == EXACT_CANDIDATE_M3
4. 验证从 REVIEWED_BASE 到 origin/main 没有修改 results/057_repo_agents_hygiene/*；若已有重叠或语义不确定则停止
5. git switch --detach origin/main
6. git merge --no-ff --no-commit 24051588d13f07e7f71e0edf5a723aca36754ed5
7. conflict/需要手工内容修改 => git merge --abort；git switch reviewed/057_repo_agents_hygiene；停止
8. 检查staged merge和 git diff --cached --check；M3侧应只带入reviewed results/057_repo_agents_hygiene evidence；不得手工编辑
9. commit纯机械merge
10. git push origin HEAD:refs/heads/main；禁止force
11. fetch并验证M3在origin/main ancestry中
12. git switch reviewed/057_repo_agents_hygiene

绝对不要触碰本机旧local main的044 commits。返回old/new remote main、merge commit SHA、M3 reachability。

成功后：NEXT_HANDOFF = PLANNER_BOUNDED_056_SOURCE_DRIFT_REVALIDATION
```

## 8. Critic decision requested

Critic should judge whether this lighter recovery is actually safer/simpler than continuing to repair canonical local checkouts, especially:

- whether explicit-SHA direct push is sufficient for the five current fast-forward repos;
- whether local dirty canonical checkout can safely be treated as irrelevant to such a push;
- whether the existing reviewed worktree + detached current `origin/main` is an acceptable clean integration surface for AI_Skills/Lucerna;
- whether repo-by-repo execution and truthful partial integration are preferable to the current globally coupled preflight;
- whether any prompt accidentally authorizes candidate mutation, force push, release, 056, or user-work cleanup.

If PASS, return the seven prompt blocks verbatim as approved execution prompts. No additional integration package round should be required unless a repo's remote state changes enough to invalidate its prompt preconditions.

`NEXT_HANDOFF = CRITIC`
