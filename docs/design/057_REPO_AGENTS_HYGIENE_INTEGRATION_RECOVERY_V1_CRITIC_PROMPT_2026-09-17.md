# 057 Repo AGENTS Hygiene — Integration Recovery V1 Critic Prompt

你是 AI Research Stack 的长期独立 Critic thread。

继续：

TASK_KEY = `057_repo_agents_hygiene`

当前阶段：approved integration execution blocked -> lighter per-repo recovery review。

本轮不是重新设计 057，也不是重开 I1-I6/H1-H9。只审恢复执行机制是否应从“所有 repo 依赖 clean canonical local checkout”收敛为“按 repo 独立集成”。不要修改任何 repo，不执行 push/merge，不创建 branch/worktree，不开始 056，不运行 paid API。

## Review object

`docs/design/057_REPO_AGENTS_HYGIENE_INTEGRATION_RECOVERY_V1_PROPOSAL_2026-09-17.md`

Planner proposal creation commit:

`893d639e87ec4f1f90adf058a3131b218a4d7ae1`

## 必须读取

最新 AI_Skills main：

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- approved 057 integration v0.2 Plan/Goal/Kickoff
- 本 recovery proposal

并独立核对当前 remote refs / reviewed refs：

- AI_Skills
- Bridge
- Bobbio
- Lucerna
- Mica-for-ChatGPT
- Asteria
- SeminarArc

必要时查 Git 官方 `git push` / `git switch --detach` / `git merge` 文档。

## 已冻结、不重开

- exact reviewed tuple / M3；
- repo AGENTS/Bridge implementation内容；
- I1-I6、Bobbio consolidation、H1-H9；
- Bridge `0.8.3` source-only boundary；
- canonical target branches；
- CUHK Date inspect-only；
- no tag/release/publish/deploy/Host install/0.8.4；
- no force/rebase/squash/cherry-pick/history rewrite；
- no paid API；
- 057 integration完成后才做 bounded 056 source-drift revalidation。

## 背景问题

当前 approved integration v0.2 在本地 preflight 被连续阻塞：

- AI_Skills ordinary local `main` 严重 stale/diverged，含 unrelated old 044 commits；不能为了057 reset/rebase/clean它。
- Bridge ordinary local `main` 有 pre-existing `.gitignore` unstaged change；不能为了057 stash/reset/clean/commit它。

但这些是 local checkout 状态，不等于 reviewed remote candidate失效。

Planner认为当前跨repo统一 clean-canonical-checkout gate 把 unrelated local state 耦合得过重。

## 核心审查问题

### 1. 五个 fast-forward repo 能否直接推 exact immutable SHA？

Proposal 对 Bridge/Bobbio/Mica/Asteria/SeminarArc 要求：

- 从现有 repo/reviewed worktree fetch；
- verify remote reviewed ref == exact candidate；
- verify remote canonical ref is ancestor of candidate；
- `git push origin <EXACT_SHA>:refs/heads/<canonical>`；
- no force；
- push后verify remote canonical == exact candidate。

审：

- 这是否保留 exact reviewed commit identity；
- branch push默认 non-fast-forward rejection是否足以保护 concurrent advancement；
- 因为push source是 explicit commit SHA，本地另一个 canonical checkout 的 dirty working tree/index 是否确实不是输入；
- 是否无需为了integration处理 Bridge `.gitignore` dirty state。

如果认为还需要 clean-state gate，必须解释哪个可观察风险会改变 explicit-SHA push 的实际 remote content，不得只是沿用旧 package 习惯。

### 2. AI_Skills / Lucerna 的 detached reviewed-worktree merge 是否合适？

Proposal 不碰 problematic canonical local checkout，而是：

- existing reviewed 057 worktree 必须自身 clean；
- fetch；
- verify exact reviewed ref；
- verify relevant path non-overlap；
- `git switch --detach origin/main`；
- `git merge --no-ff --no-commit <EXACT_CANDIDATE>`；
- no conflict/manual edit；
- inspect + `git diff --cached --check`；
- commit mechanical merge；
- `git push origin HEAD:refs/heads/main` without force；
- switch back reviewed branch。

审：

- 是否无需新branch/worktree；
- 是否保留 reviewed candidate ancestry；
- 是否足够保护 stale AI_Skills local main 的 old 044 commits；
- 是否保留 Lucerna current main product commits；
- push rejection / conflict recovery 是否明确。

### 3. Repo-by-repo execution 是否比全局 preflight 更合适？

Proposal 不再要求“所有repo clean后才能第一次push”。原因：不同repo/remote本身不能形成单一原子Git transaction，旧合同也已经允许 truthful partial integration。

审：

- 这种失败隔离是否合理降低 complexity / human time；
- 一个repo blocked时，其他已独立满足前提的repo是否可以继续；
- 是否仍然诚实报告 partial integration；
- 是否会让 candidate identity / evidence provenance 失真。

### 4. 七个 exact prompt 是否 execution-safe？

逐个检查 Proposal §7 的 Bobbio、Mica、Asteria、SeminarArc、Bridge、Lucerna、AI_Skills prompt。

必须确认没有：

- candidate content mutation；
- local user-work cleanup；
- force push；
- new branch/worktree；
- PR；
- release/tag/deployment；
- paid API；
- 056 work；
- CUHK Date mutation；
- H10/state/schema/ledger/controller/watcher。

如果某一个 prompt 有局部问题，要求最小修订，不要因此重开整个057架构。

## 复杂度审查

主动判断当前旧恢复方案是否已经“为了集成几个已PASS的AGENTS/docs commit而过重”。

优先选择能保持 exact candidate、安全边界和用户工作，同时减少：

- 跨repo耦合；
- 对无关 dirty canonical checkout 的依赖；
- 重复 Planner/Critic 往返；
- 用户手动清理/选择。

不要为了延续旧 package 而保留没有直接风险依据的 ceremony。

## 输出

若需要修订：

```text
RESULT = REVISE
TASK_KEY = 057_repo_agents_hygiene
REVIEW_OBJECT = docs/design/057_REPO_AGENTS_HYGIENE_INTEGRATION_RECOVERY_V1_PROPOSAL_2026-09-17.md
READY_FOR_PER_REPO_INTEGRATION = NO
NEXT_HANDOFF = PLANNER
```

只列本 recovery proposal 自己的 stable blockers，并自动给完整 Planner 修订 prompt。

若通过：

先用正常中文解释：

- 为什么当前 blocker 是 local integration surface，不是057 product/AGENTS failure；
- 为什么五个 FF repo 可以用 explicit-SHA push而不用碰dirty canonical checkout；
- 为什么 AI_Skills/Lucerna 只需要各自 reviewed worktree 的 clean detached merge；
- 为什么 repo-by-repo failure isolation比全局clean gate更轻且没有降低关键安全边界；
- PASS证明什么、不证明什么。

然后给：

```text
RESULT = PASS
TASK_KEY = 057_repo_agents_hygiene
REVIEW_OBJECT = docs/design/057_REPO_AGENTS_HYGIENE_INTEGRATION_RECOVERY_V1_PROPOSAL_2026-09-17.md
READY_FOR_PER_REPO_INTEGRATION = YES
NEXT_HANDOFF = USER_SENDS_APPROVED_PER_REPO_PROMPTS
```

最后逐字返回 Proposal §7 的七个 prompt，分别标记：

- APPROVED BOBBIO PROMPT
- APPROVED MICA PROMPT
- APPROVED ASTERIA PROMPT
- APPROVED SEMINARARC PROMPT
- APPROVED BRIDGE PROMPT
- APPROVED LUCERNA PROMPT
- APPROVED AI_SKILLS PROMPT

不要 PASS 后重写一个“更完善”的版本。
