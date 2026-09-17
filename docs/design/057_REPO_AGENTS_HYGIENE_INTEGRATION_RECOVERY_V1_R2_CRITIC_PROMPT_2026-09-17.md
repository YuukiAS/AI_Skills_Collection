# 057 Repo AGENTS Hygiene — Integration Recovery V1.1 Critic R2

继续：

TASK_KEY = `057_repo_agents_hygiene`

当前阶段：lighter per-repo integration recovery v1 -> narrow R2。

本轮只复核两个 stable blockers：

- `C057-R1-CANONICAL-PUSH-DESTINATION-IDENTITY`
- `C057-R2-PARTIAL-INTEGRATION-056-HANDOFF`

不要重新设计 057，不重开 I1-I6/H1-H9，不恢复旧全局 clean-canonical-checkout 方案，不修改 repo/candidate，不执行 integration，不开始 056，不运行 paid API。

## Review object

`docs/design/057_REPO_AGENTS_HYGIENE_INTEGRATION_RECOVERY_V1_PROPOSAL_2026-09-17.md`

Revised proposal version: `v1.1`

Revised proposal commit:

`e85c435ada79e580f81ee487e6f41625e5bc00c2`

## 已接受，不重开

保持 Critic 已接受的 recovery direction：

- Bridge/Bobbio/Mica/Asteria/SeminarArc 使用 exact reviewed SHA + remote ancestry + non-force explicit-SHA push；
- dirty canonical local checkout 不是 explicit-SHA push 输入；
- AI_Skills/Lucerna 使用 existing reviewed worktree -> detach current origin/main -> no-manual-edit mechanical merge -> push HEAD:main -> switch back；
- repo-by-repo failure isolation；
- truthful partial integration；
- no force/rebase/squash/cherry-pick；
- Bridge `0.8.3` source-only；
- no release/deploy/Host install/paid API/056；
- exact reviewed tuple/canonical targets/path-overlap stop conditions全部不变。

## 只检查三件事

### 1. C057-R1 是否关闭

逐条检查 Proposal §7 的七个 exact prompts。

每个 prompt 必须在任何 fetch/push/merge 前：

- 验证当前 local repo identity；
- 检查 `origin` effective fetch URL；
- 检查 **所有** effective push URLs，包括 `pushurl`；
- 允许等价 SSH/HTTPS URL，但归一化后必须只指向该 prompt 明确声明的 `YuukiAS/<repo>` canonical GitHub repository；
- 不得存在额外的不同 push destination；
- mismatch / ambiguity 必须只停止该 repo 并报告；
- 禁止 `git remote set-url`、pushurl/remap/Git config 修改来“修好”remote。

重点确认 source exact SHA 和 destination identity 都被独立证明。

### 2. C057-R2 是否关闭

Proposal §6 必须明确：partial integration 永远不等于 057 integration complete。

Prompt G 必须满足：

- AI_Skills 自己成功并不足以进入 056；
- 只有 Bridge/Bobbio/Mica/Asteria/SeminarArc/Lucerna/AI_Skills 七个 mutable canonical targets 全部已有成功 integration evidence，才可：
  `NEXT_HANDOFF = PLANNER_BOUNDED_056_SOURCE_DRIFT_REVALIDATION`；
- 任一 repo `BLOCKED` / `FAILED` / `NOT_RUN` 时，必须报告 exact partial state、不回滚成功 repo、不开始/修改 056，并保持在 057 integration Planner status/recovery handoff。

不要因为允许 partial integration 而重新要求全局原子执行。

### 3. 是否没有其它语义漂移

对比已接受的 v1 recovery direction，确认 v1.1 没有实质改变：

- exact reviewed tuple/M3；
- target canonical branches；
- 五个 FF repo explicit-SHA non-force push；
- AI_Skills/Lucerna detached reviewed-worktree merge；
- path-overlap/conflict stop conditions；
- no manual reconciliation；
- no new branch/worktree；
- no user-work stash/reset/clean；
- CUHK Date inspect-only；
- Bridge source-only boundary；
- no repeated tests/H1-H9；
- no paid API；
- no 056 until all 057 canonical integrations are complete。

## Output

若仍有 blocker：

```text
RESULT = REVISE
TASK_KEY = 057_repo_agents_hygiene
REVIEW_OBJECT = docs/design/057_REPO_AGENTS_HYGIENE_INTEGRATION_RECOVERY_V1_PROPOSAL_2026-09-17.md
RECOVERY_VERSION = v1.1
C057-R1 = OPEN | CLOSED
C057-R2 = OPEN | CLOSED
READY_FOR_PER_REPO_INTEGRATION = NO
NEXT_HANDOFF = PLANNER
```

只给与 R1/R2 或本次修订直接造成的 scope drift 有关的 blocker，并按 Critic contract 给完整 Planner revision prompt。

若关闭：

先用正常中文简短解释：

- remote identity gate 如何防止 named `origin` 指向错误 push destination；
- 为什么不需要 remap remote；
- partial integration 为什么可以保留，但为什么不能提前进入 056；
- 其它 recovery strategy 没有变化；
- PASS 只批准用户发送七个 per-repo prompts，并不表示任何 integration 已发生。

然后给：

```text
RESULT = PASS
TASK_KEY = 057_repo_agents_hygiene
REVIEW_OBJECT = docs/design/057_REPO_AGENTS_HYGIENE_INTEGRATION_RECOVERY_V1_PROPOSAL_2026-09-17.md
RECOVERY_VERSION = v1.1
C057-R1-CANONICAL-PUSH-DESTINATION-IDENTITY = CLOSED
C057-R2-PARTIAL-INTEGRATION-056-HANDOFF = CLOSED
READY_FOR_PER_REPO_INTEGRATION = YES
NEXT_HANDOFF = USER_SENDS_APPROVED_PER_REPO_PROMPTS
```

最后逐字返回 Proposal §7 的七个 prompt：

- APPROVED BOBBIO PROMPT
- APPROVED MICA PROMPT
- APPROVED ASTERIA PROMPT
- APPROVED SEMINARARC PROMPT
- APPROVED BRIDGE PROMPT
- APPROVED LUCERNA PROMPT
- APPROVED AI_SKILLS PROMPT

不要 PASS 后再写新的“改进版”。
