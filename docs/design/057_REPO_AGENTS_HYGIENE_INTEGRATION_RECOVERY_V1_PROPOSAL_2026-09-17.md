# 057 Repo AGENTS Hygiene — Integration Recovery V1.1 Proposal

- Task key: `057_repo_agents_hygiene`
- Date: 2026-09-17
- Version: `v1.1`
- Status: `DRAFT_FOR_CRITIC_R2`
- Scope: integration recovery only; no 057 redesign, no candidate mutation, no 056 work
- Prior recovery proposal: v1 at `893d639e87ec4f1f90adf058a3131b218a4d7ae1`, Critic `REVISE`

## 0. Critic blocker disposition

### C057-R1-CANONICAL-PUSH-DESTINATION-IDENTITY — ACCEPT

The v1 recovery correctly bound the **source commit identity** through exact reviewed SHAs, but it treated the local remote name `origin` as if that also proved the **destination repository identity**. That is not sufficient: a named remote can have a different fetch URL and one or more configured push URLs.

v1.1 therefore adds the same read-only remote-identity gate to all seven per-repo prompts **before any fetch, push, or merge**:

- verify the local checkout is the intended repository;
- inspect the effective `origin` fetch URL;
- inspect **all** effective `origin` push URLs, including configured `pushurl` values;
- normalize equivalent GitHub SSH/HTTPS URL forms to the repository identity `github.com/<owner>/<repo>` (optional trailing `.git` ignored);
- require the effective fetch destination and every effective push destination to resolve to the prompt's declared canonical `YuukiAS/<repo>`;
- any extra or ambiguous push destination is a stop condition;
- do not run `git remote set-url`, edit Git config, remap remotes, or otherwise mutate remote configuration to make the gate pass.

This is a read-only destination check, not a new controller/state/ledger.

### C057-R2-PARTIAL-INTEGRATION-056-HANDOFF — ACCEPT

Repo-by-repo failure isolation remains correct, but partial integration is **never** 057 integration completion.

v1.1 freezes the completion rule:

- successful repo integrations remain published and are not rolled back merely because another repo is blocked;
- each repo reports exact success/block state independently;
- `PLANNER_BOUNDED_056_SOURCE_DRIFT_REVALIDATION` is legal only after successful integration evidence exists for **all seven mutable canonical targets**: Bridge, Bobbio, Mica, Asteria, SeminarArc, Lucerna, and AI_Skills;
- if any target remains `BLOCKED`, `FAILED`, or `NOT_RUN`, do not start or modify 056; report the exact partial state and hand back to Planner for 057 integration status/recovery.

Prompt G is now conditional and cannot unilaterally advance to 056 merely because AI_Skills itself integrated successfully.

## 1. Why the current integration execution is over-coupled

The reviewed 057 implementation is already complete and independently accepted. The current blocker is not AGENTS quality or H1-H9. It is the integration execution surface.

The approved integration v0.2 required all repositories to use a clean canonical local checkout before the first push. That correctly protected dirty user work, but it coupled unrelated local workstation state to remote integration:

- AI_Skills local `main` is a stale/diverged user checkout with old unrelated 044 commits. It must not be reset/rebased/cleaned for 057.
- Bridge local canonical `main` has a pre-existing `.gitignore` modification. 057 must not stash/reset/clean/commit it.
- Remote reviewed branches and remote canonical refs remain usable.

The result is repeated Goal blocking even though the reviewed commits themselves remain valid.

## 2. Current remote facts rechecked by Planner

At v1.1 revision start:

- AI_Skills remote `main = f0a0738f4104d484e973f3fccc5a11a05d9059a0`; reviewed branch still points exactly to `M3 = 24051588d13f07e7f71e0edf5a723aca36754ed5`. They are diverged, and M3 adds only `results/057_repo_agents_hygiene/*` relative to the 057 base. This proposal commit itself will advance `main`, so execution must fetch current `origin/main` rather than depend on this locator.
- Bridge remote `main = cb77b1cc5a1fce097a38066d2db452291e359852`; reviewed branch = `e1d6b781ad7e56d567bed419001069baf439d0a5`; candidate is still a pure fast-forward.
- Bobbio `develop` -> `ab5dccb6b8b87c49671aa097233ce1bcc38be004`: still pure fast-forward.
- Mica `main` -> `e49416f874f633aedc7521734ee5b0f441aae970`: still pure fast-forward.
- Asteria `main` -> `0ce1d4daca1e410ce551570578dd563d4ef67e90`: still pure fast-forward.
- SeminarArc `main` -> `74caaa4ecec16f1bc90987979458d1a4e93f52be`: still pure fast-forward.
- Lucerna remote `main` has advanced from the old 057 base, while reviewed branch remains `41cd1297af6901531d3135593bc9806bffc38829`. The current main-side post-base changes still do not touch `AGENTS.md`; a clean mechanical merge remains plausible.
- CUHK Date remains inspect-only and is not part of integration.

## 3. Simpler recovery mechanism

Replace the single cross-repo canonical-checkout orchestration with **independent per-repository integration prompts**, all reviewed together once.

This does not change any reviewed candidate, canonical target branch, H1-H9 result, Bridge version, release boundary, or 056 sequencing. It changes only the local execution surface and removes the global “all canonical checkouts clean before any push” coupling.

### 3.1 Remote identity gate shared by all seven prompts

Before **any** `git fetch origin`, `git push origin ...`, detached merge, or other integration mutation, each prompt must first perform a read-only remote identity gate.

Minimum evidence:

```text
git rev-parse --show-toplevel
git remote get-url origin
git remote get-url --all origin
git remote get-url --push --all origin
```

Equivalent direct Git inspection is allowed, but it must establish the same facts.

Interpretation:

- the effective fetch URL must resolve to the declared canonical GitHub repository for that prompt;
- every effective push URL must resolve to that same canonical GitHub repository;
- HTTPS and SSH forms are equivalent when they resolve to `github.com` with the exact declared owner/repository path; an optional trailing `.git` does not change identity;
- if multiple effective push URLs exist, **all** must normalize to that one canonical repository; any additional different destination is a blocker;
- remote aliases, URL rewrite configuration, or push URLs that make the destination ambiguous are a blocker unless the effective URLs above still resolve unambiguously to the declared canonical repo;
- do not change `origin`, `pushurl`, `insteadOf`/`pushInsteadOf`, Git config, or any remote mapping under this task.

This closes destination identity without coupling integration to another local checkout's working-tree state.

### 3.2 Five fast-forward repositories

For Bridge, Bobbio, Mica, Asteria and SeminarArc:

- run from the existing `reviewed/057_repo_agents_hygiene` repository/worktree or any existing checkout that can resolve the exact immutable candidate object;
- do **not** switch to or modify the dirty canonical local checkout;
- pass the remote identity gate in §3.1;
- `git fetch origin`;
- verify `origin/reviewed/057_repo_agents_hygiene` equals the frozen candidate SHA;
- verify the current remote canonical ref is an ancestor of the candidate;
- push the immutable commit directly to the canonical remote ref:
  - `git push origin <EXACT_SHA>:refs/heads/main`, or Bobbio `...:refs/heads/develop`;
- do not use force.

A direct push of an explicit commit object does not consume the local working tree/index. Git's normal branch update rule rejects a non-fast-forward push unless force is used. Therefore Bridge's unrelated local `.gitignore` modification does not need to be moved, stashed, reset, committed, or inspected as integration input.

If the remote canonical ref advanced so that the update is no longer fast-forward, stop only that repo and return the exact remote state.

### 3.3 Two diverged repositories

AI_Skills and Lucerna need a real merge commit because canonical remote history advanced independently.

Do not repair or use their problematic canonical local checkout. Instead use the **existing reviewed 057 worktree** as the integration surface:

1. verify the reviewed worktree itself is clean enough to switch safely and is on/resolves the exact frozen reviewed branch;
2. pass the remote identity gate in §3.1;
3. fetch `origin`;
4. verify the reviewed remote branch still equals the exact frozen candidate;
5. verify the relevant path non-overlap still holds;
6. `git switch --detach origin/main` — no new branch/worktree;
7. `git merge --no-ff --no-commit <EXACT_REVIEWED_SHA>`;
8. conflict or semantic uncertainty -> `git merge --abort`, switch back to `reviewed/057_repo_agents_hygiene`, stop this repo;
9. otherwise inspect the staged merge, run `git diff --cached --check`, make no manual content edits, commit the mechanical merge;
10. `git push origin HEAD:refs/heads/main` without force;
11. switch the reviewed worktree back to `reviewed/057_repo_agents_hygiene`.

For AI_Skills specifically, the stale/diverged local `main` with old 044 commits is left completely untouched. For Lucerna, current canonical product changes are preserved as the first-parent side of the merge.

If the existing reviewed worktree itself has unrelated dirty changes that make detach/merge unsafe, stop that repo. Do not create another worktree automatically under this recovery.

## 4. Why this is simpler and still safe

The previous package tried to preflight all repositories before the first push to reduce partial integration. But Git cannot make updates across separate repositories/remotes atomic. The approved recovery already required truthful reporting of partial integration.

This proposal therefore prefers **repo-local failure isolation**:

- one dirty checkout cannot block six unrelated repos;
- easy fast-forward integration does not touch a working tree at all;
- only the two repositories that actually need merge commits require a clean integration worktree;
- the remote identity gate prevents `origin` from silently pointing pushes at the wrong repository;
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
- no remote remap / `git remote set-url` / Git-config rewrite to make identity checks pass;
- no paid API;
- no 056 modification/execution during partial or complete 057 integration;
- only after all seven mutable canonical targets have successful integration evidence may the workflow advance to bounded 056 source-drift revalidation.

## 6. Execution order, partial integration, and completion

After one independent Critic PASS on this recovery package, the user may send the following repo prompts independently.

Recommended order:

1. Bobbio
2. Mica
3. Asteria
4. SeminarArc
5. Bridge
6. Lucerna
7. AI_Skills last

A failure in one prompt does not invalidate already successful repo integrations. The user may continue by sending another already-approved repo prompt; no failed repo may improvise a new recovery.

However, **partial integration is never 057 integration completion**.

057 integration is complete only when successful integration evidence exists for all seven mutable canonical targets:

- Bobbio
- Mica-for-ChatGPT
- Asteria
- SeminarArc
- GPT_Codex_AI_Bridge_Kit
- Lucerna
- AI_Skills_Collection

Success evidence is the repo prompt's own remote result: the required canonical ref/head or reviewed-candidate ancestry is verified after push, with the exact candidate preserved.

If any target is `BLOCKED`, `FAILED`, or `NOT_RUN`:

- report the exact per-repo partial state;
- do not roll back already-successful integrations merely to simulate atomicity;
- do not start or modify 056;
- hand back to Planner for 057 integration status/recovery.

Only after all seven are confirmed integrated may:

`NEXT_HANDOFF = PLANNER_BOUNDED_056_SOURCE_DRIFT_REVALIDATION`

be emitted.

This is a handoff condition, not a new workflow enum/state machine.

## 7. Exact per-repo prompts for Critic review

### Prompt A — Bobbio

```text
TASK_KEY = 057_repo_agents_hygiene
MODE = approved per-repo integration recovery
REPO = YuukiAS/Bobbio
TARGET = develop
EXACT_CANDIDATE = ab5dccb6b8b87c49671aa097233ce1bcc38be004
CANONICAL_REPO = YuukiAS/Bobbio

只做这个repo的057 integration。不要修改candidate内容，不创建branch/worktree，不改Figma/product/runtime/version，不开始056。

在任何fetch/push前先做只读remote identity gate：
- 确认当前Git repo就是本prompt声明的repo；
- 读取 `git remote get-url origin`、`git remote get-url --all origin`、`git remote get-url --push --all origin`；
- 将SSH/HTTPS等价形式规范到GitHub owner/repo identity；effective fetch destination和所有effective push destinations都必须只解析到 `YuukiAS/Bobbio`；
- 发现额外push destination、repo不匹配或identity有歧义则停止并报告；
- 禁止 `git remote set-url`、修改pushurl/Git config或任何remote remap。

通过remote identity gate后：
1. git fetch origin
2. 验证 origin/reviewed/057_repo_agents_hygiene == EXACT_CANDIDATE
3. 验证 origin/develop 是 EXACT_CANDIDATE 的ancestor；否则停止并报告
4. 不需要checkout/修改本地develop；直接：
   git push origin ab5dccb6b8b87c49671aa097233ce1bcc38be004:refs/heads/develop
5. 禁止force
6. fetch并验证 origin/develop == EXACT_CANDIDATE

本prompt不授权清理/stash/reset任何unrelated local work；也不删除reviewed branch。

返回remote identity检查结果、old/new remote develop、push结果和exact candidate identity。
```

### Prompt B — Mica

```text
TASK_KEY = 057_repo_agents_hygiene
MODE = approved per-repo integration recovery
REPO = YuukiAS/Mica-for-ChatGPT
TARGET = main
EXACT_CANDIDATE = e49416f874f633aedc7521734ee5b0f441aae970
CANONICAL_REPO = YuukiAS/Mica-for-ChatGPT

只做这个repo的057 integration。不要修改AGENTS/candidate/runtime/version，不创建branch/worktree，不开始056。

在任何fetch/push前先做只读remote identity gate：
- 确认当前Git repo identity；
- 检查origin effective fetch URL和 `git remote get-url --push --all origin` 的全部effective push URLs；
- SSH/HTTPS形式可等价，但全部必须只解析到 `YuukiAS/Mica-for-ChatGPT`；
- 任何额外push destination/不匹配/歧义 => 停止；
- 不得修改/remap remote或Git config。

通过后：
1. git fetch origin
2. 验证 origin/reviewed/057_repo_agents_hygiene == EXACT_CANDIDATE
3. 验证 origin/main 是 EXACT_CANDIDATE 的ancestor；否则停止
4. 不切换或清理canonical local main；直接：
   git push origin e49416f874f633aedc7521734ee5b0f441aae970:refs/heads/main
5. 禁止force
6. fetch并验证 origin/main == EXACT_CANDIDATE

不得stash/reset/clean/commit unrelated local work。返回remote identity检查、old/new remote main和push结果。
```

### Prompt C — Asteria

```text
TASK_KEY = 057_repo_agents_hygiene
MODE = approved per-repo integration recovery
REPO = YuukiAS/Asteria
TARGET = main
EXACT_CANDIDATE = 0ce1d4daca1e410ce551570578dd563d4ef67e90
CANONICAL_REPO = YuukiAS/Asteria

只做这个repo的057 integration，不修改candidate、product/runtime、prompts/AGENT_RULES.md，不创建branch/worktree，不开始056。

在任何fetch/push前先做只读remote identity gate：
- 确认当前repo identity；
- 检查origin effective fetch URL和所有effective push URLs（包括pushurl）；
- 等价SSH/HTTPS可接受，但全部必须只解析到 `YuukiAS/Asteria`；
- extra push destination/不匹配/歧义 => 停止；
- 禁止remote set-url/remap/config修改。

通过后：
1. git fetch origin
2. 验证 origin/reviewed/057_repo_agents_hygiene == EXACT_CANDIDATE
3. 验证 origin/main 是 EXACT_CANDIDATE 的ancestor；否则停止
4. 直接：
   git push origin 0ce1d4daca1e410ce551570578dd563d4ef67e90:refs/heads/main
5. 禁止force
6. fetch并验证 origin/main == EXACT_CANDIDATE

不要清理/移动/提交unrelated local work。返回remote identity检查、old/new remote main和push结果。
```

### Prompt D — SeminarArc

```text
TASK_KEY = 057_repo_agents_hygiene
MODE = approved per-repo integration recovery
REPO = YuukiAS/SeminarArc
TARGET = main
EXACT_CANDIDATE = 74caaa4ecec16f1bc90987979458d1a4e93f52be
CANONICAL_REPO = YuukiAS/SeminarArc

只做这个repo的057 integration。不要修改AGENTS/DEVICE_TESTING或Android/runtime/product，不创建branch/worktree，不开始056。

在任何fetch/push前先做只读remote identity gate：
- 确认当前repo identity；
- 检查origin effective fetch URL和所有effective push URLs；
- SSH/HTTPS等价形式可以接受，但全部必须只解析到 `YuukiAS/SeminarArc`；
- 额外push destination/identity mismatch/ambiguity => 停止；
- 不得修改remote/Git config。

通过后：
1. git fetch origin
2. 验证 origin/reviewed/057_repo_agents_hygiene == EXACT_CANDIDATE
3. 验证 origin/main 是 EXACT_CANDIDATE 的ancestor；否则停止
4. 直接：
   git push origin 74caaa4ecec16f1bc90987979458d1a4e93f52be:refs/heads/main
5. 禁止force
6. fetch并验证 origin/main == EXACT_CANDIDATE

不得碰真机/Emulator；这是纯Git integration。返回remote identity检查、old/new remote main和push结果。
```

### Prompt E — Bridge

```text
TASK_KEY = 057_repo_agents_hygiene
MODE = approved per-repo integration recovery
REPO = YuukiAS/GPT_Codex_AI_Bridge_Kit
TARGET = main
EXACT_CANDIDATE = e1d6b781ad7e56d567bed419001069baf439d0a5
VERSION = 0.8.3 source candidate
CANONICAL_REPO = YuukiAS/GPT_Codex_AI_Bridge_Kit

只做Bridge的057 source integration。不要修改candidate，不清理当前canonical checkout里的`.gitignore`或其他dirty work，不创建branch/worktree，不开始056。

在任何fetch/push前先做只读remote identity gate：
- 确认当前repo identity；
- 检查origin effective fetch URL、全部fetch URLs和全部effective push URLs（包括pushurl）；
- SSH/HTTPS等价形式可接受，但effective fetch destination和所有effective push destinations必须只解析到 `YuukiAS/GPT_Codex_AI_Bridge_Kit`；
- 任何额外push destination/不匹配/歧义 => 停止；
- 禁止remote set-url/remap/config修改。

通过后：
1. git fetch origin
2. 验证 origin/reviewed/057_repo_agents_hygiene == EXACT_CANDIDATE
3. 验证 origin/main 是 EXACT_CANDIDATE 的ancestor；否则停止
4. 不checkout/修改dirty canonical main；直接：
   git push origin e1d6b781ad7e56d567bed419001069baf439d0a5:refs/heads/main
5. 禁止force
6. fetch并验证 origin/main == EXACT_CANDIDATE
7. 只读确认main中的version surfaces为0.8.3

明确禁止tag/GitHub Release/package publish/deploy/Host install/update/0.8.4。返回remote identity检查、old/new remote main和version identity。
```

### Prompt F — Lucerna

```text
TASK_KEY = 057_repo_agents_hygiene
MODE = approved per-repo integration recovery
REPO = YuukiAS/Lucerna
TARGET = main
EXACT_CANDIDATE = 41cd1297af6901531d3135593bc9806bffc38829
REVIEWED_BASE = 760931ae8a1f0edffefe41c83c1667c7190c3014
CANONICAL_REPO = YuukiAS/Lucerna

只做Lucerna的057 integration。保留当前main上的后续product/closure commits；不得修改057 candidate或产品/runtime。

使用现有 reviewed/057_repo_agents_hygiene worktree，不使用/清理别的canonical checkout，不创建新branch/worktree。

在任何fetch/push/merge前先做只读remote identity gate：
- 确认当前repo identity；
- 检查origin effective fetch URL和所有effective push URLs；
- SSH/HTTPS等价形式可接受，但全部必须只解析到 `YuukiAS/Lucerna`；
- 额外push destination/不匹配/歧义 => 停止；
- 禁止修改/remap remote或Git config。

通过remote identity gate后：
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

返回remote identity检查、old/new remote main、merge commit SHA、candidate reachability。若push因remote再次前进被拒绝，禁止force，切回reviewed branch并报告。
```

### Prompt G — AI_Skills last

```text
TASK_KEY = 057_repo_agents_hygiene
MODE = approved per-repo integration recovery
REPO = YuukiAS/AI_Skills_Collection
TARGET = main
EXACT_CANDIDATE_M3 = 24051588d13f07e7f71e0edf5a723aca36754ed5
REVIEWED_BASE = e8ba751561c9e61a5b0bbd094d2c280ff0b00b59
CANONICAL_REPO = YuukiAS/AI_Skills_Collection

只做AI_Skills的057 evidence integration。不要修改057 candidate、current main docs/TODO、任何plugin production或056。

本机普通local main含旧044 commits且严重diverged；不要reset/rebase/clean/stash/merge/修复该local main。使用现有 reviewed/057_repo_agents_hygiene worktree 作为独立integration surface，不创建新branch/worktree。

在任何fetch/push/merge前先做只读remote identity gate：
- 确认当前repo identity；
- 检查origin effective fetch URL和所有effective push URLs；
- SSH/HTTPS等价形式可接受，但全部必须只解析到 `YuukiAS/AI_Skills_Collection`；
- 额外push destination/不匹配/歧义 => 停止；
- 禁止修改/remap remote、pushurl或Git config。

通过remote identity gate后：
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

绝对不要触碰本机旧local main的044 commits。返回remote identity检查、old/new remote main、merge commit SHA、M3 reachability。

完成AI_Skills自身integration后，不得仅因为本repo成功就宣布057 integration complete或进入056。

只有当前交接上下文中已经有以下七个mutable canonical targets全部成功integration evidence：
- Bridge
- Bobbio
- Mica-for-ChatGPT
- Asteria
- SeminarArc
- Lucerna
- AI_Skills_Collection

才允许：
NEXT_HANDOFF = PLANNER_BOUNDED_056_SOURCE_DRIFT_REVALIDATION

如果任何repo仍是BLOCKED / FAILED / NOT_RUN：
- 汇总并报告exact partial integration state；
- 不回滚已经成功的repo；
- 不开始或修改056；
- NEXT_HANDOFF = PLANNER_057_INTEGRATION_STATUS_RECOVERY

上述NEXT_HANDOFF只是Planner交接标签，不新增workflow enum/state machine。
```

## 8. External Git basis for this narrow revision

Current official Git documentation confirms the relevant mechanics:

- `git remote get-url [--push] [--all] <name>` reports effective remote URLs and expands URL rewrite configuration;
- a configured remote can have multiple push URLs, and Git pushes to all configured push destinations;
- fetch and push URLs may be configured separately, so checking the source SHA alone cannot establish the destination identity;
- an explicit non-force branch push remains subject to Git's normal fast-forward update rules.

These facts support the read-only destination-identity gate without adding any remote-rewrite mechanism.

## 9. Critic decision requested

Critic should perform a narrow R2 review only:

1. Do all seven prompts verify effective canonical fetch/push destination identity before any fetch/push/merge, including all push URLs, while forbidding remote remap?
2. Does Prompt G now prevent partial integration from advancing to 056 unless all seven mutable canonical targets have successful integration evidence?
3. Did any other per-repo recovery semantics drift from the already-accepted v1 direction?

Do not reopen the accepted recovery architecture, 057 implementation, I1-I6/H1-H9, or the old globally coupled integration package unless this v1.1 text directly contradicts them.

If PASS, return the seven prompt blocks verbatim as approved execution prompts. No additional integration package round should be required unless a repo's remote state changes enough to invalidate its prompt preconditions.

`NEXT_HANDOFF = CRITIC`
