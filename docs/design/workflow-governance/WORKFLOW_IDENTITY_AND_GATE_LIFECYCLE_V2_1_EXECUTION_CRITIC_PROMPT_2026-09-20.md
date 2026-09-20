# 工作流命名与插件回归机制完善（AI_Skills + Bridge）— Execution-ready Critic Prompt v2.1 R2

你是 AI Research Stack 的长期独立 Critic thread。

继续同一个 **工作流命名与插件回归机制完善（AI_Skills + Bridge）** execution-package round。

本轮只复核上一轮两个 execution-package blocker 是否关闭，以及这两处小修改是否直接引入回归。不要重开已经 PASS 的 v2.1 design，不重审已关闭 C-WIGL-01/02/03/04，不重新设计 Gate lifecycle、scope precedence、semantic identity、G1–G7、version architecture 或 human-readable naming。

不要实现代码，不创建 task/branch/worktree，不启动 Executor，不运行 paid API，不修改 production，不替用户发送 Kickoff。

## Active Review Context

```text
target_repo = YuukiAS/AI_Skills_Collection
human_readable_name = 工作流命名与插件回归机制完善（AI_Skills + Bridge）
technical_task_key = cross-repo--workflow-identity-gate-lifecycle
design_topic = workflow-identity-and-gate-lifecycle
review_stage = EXECUTION_READY_PACKAGE_REVIEW_R2

approved_proposal =
docs/design/workflow-governance/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V2_PROPOSAL_2026-09-20.md
proposal_version = v2.1
proposal_commit = ba2fc85f9c58b9b332eb07f821d1756b417fe1d1

implementation_plan =
docs/design/workflow-governance/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V2_1_IMPLEMENTATION_PLAN_2026-09-20.md

canonical_goal =
docs/goals/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V2_1_GOAL.md

kickoff_draft =
docs/operations/prompts/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V2_1_KICKOFF.md

revised_package_commit =
1d13a6ebdc81fa8be2c3726d2025165c611ce96b

prior_execution_critic_review =
docs/design/workflow-governance/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V2_1_EXECUTION_CRITIC_REVIEW_2026-09-20.md

prior_execution_critic_review_commit =
9cc8731be314546ae6901e28dd35e17f73670a0c

open_findings =
C-WIGL-E1-REMOTE-IDENTITY-PREFLIGHT
C-WIGL-E2-REPLAY-COUNT-SEMANTICS

execution_branch/worktree = NOT_CREATED
```

设计 blocker 保持：

```text
C-WIGL-01=CLOSED
C-WIGL-02=CLOSED
C-WIGL-03=CLOSED
C-WIGL-04=CLOSED
```

如果没有本轮修改直接产生的新具体 blocker，不要重新打开这些对象。

## 一、必须实际读取

读取 AI_Skills_Collection 最新 main 的：

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- approved Proposal v2.1
- prior execution Critic review @ `9cc8731be314546ae6901e28dd35e17f73670a0c`
- revised Implementation Plan
- revised Canonical Goal
- revised Kickoff Draft

按需要 targeted read Bridge Git/task-key source 或 current version source，只用于检查这次两处修改是否与真实执行入口冲突；不要重新进行上一轮已经完成的完整 execution-package architecture review。

本轮是两个 execution-contract clarification，不引入新的外部技术方案。除非发现新的具体事实冲突，不需要扩展外部 research。

## 二、只复核 C-WIGL-E1-REMOTE-IDENTITY-PREFLIGHT

Plan / Goal / Kickoff 现在都应一致要求：

1. 在两个 repo 的任何 branch/worktree creation，以及任何 fetch/push action 之前，先做 read-only remote identity gate；
2. 确认当前 local Git repo 是 prompt 声明的 canonical repository；
3. 读取 `origin` effective fetch URL；
4. 读取 **all effective push URLs**，包括 configured `pushurl`；
5. 将 GitHub SSH / scp-style SSH / HTTPS 等价 URL 规范到 `owner/repo` identity；
6. AI_Skills fetch/push identity 只能唯一解析到：
   `YuukiAS/AI_Skills_Collection`
7. Bridge fetch/push identity 只能唯一解析到：
   `YuukiAS/GPT_Codex_AI_Bridge_Kit`
8. distinct extra push destination、repo mismatch、missing origin、unsupported/ambiguous identity 必须：

```text
STOP_BEFORE_MUTATION=YES
NEXT_OWNER=GPT_PLANNER
```

9. 不得 branch/worktree creation、fetch 或 push；
10. 禁止 `git remote set-url`、修改 `remote.origin.url` / `remote.origin.pushurl`、增删 push URLs、修改 Git URL rewrite config / Git config 或 remote remap 来让 gate 通过；
11. 不新增 remote registry/state/schema/controller。

请重点判断三份文件语义是否一致，以及这个 preflight 是否足够覆盖“fetch URL 对、pushurl 指向别处”的真实风险。

等价 raw SSH/HTTPS URL 如果规范后仍是同一个声明 GitHub repo，可以视为同一个 repository identity；任何 distinct normalized push destination 必须失败。

如果 E1 已经关闭，不要为了更复杂的 Git provenance 系统继续加 gate。

## 三、只复核 C-WIGL-E2-REPLAY-COUNT-SEMANTICS

Plan / Goal / Kickoff 现在都应一致表达：

### Approved scenario set 固定为两个

1. Verified Workflow
2. AI Skills Maintainer

“两种/两个”限制的是 **replay scenarios/cases**，不是总 invocation 数。

### 合法 rerun

如果某个固定 scenario 第一次 FAIL：

- 先归因 concrete root cause；
- root cause 可以在 frozen architecture 内 bounded repair 时，允许修复后重跑**同一个 frozen scenario**；
- rerun 不属于 paid-call budget；
- scenario 的输入/意图不能因为看过 FAIL 就换成新的赢家输入。

### 禁止

- 不得新增第三种 replay scenario；
- 不得追加新输入/variant 来找 PASS；
- 不得 run-until-PASS；
- 不得把 rerun 理解为 Terra/OpenAI Responses paid-call budget；
- repeated failure 没有新的具体 in-scope causal repair 时，应停止/归因而不是 blind rerun；
- repeated failure 如果表明必须改变 Gate taxonomy、ownership、parser responsibility、state/recovery semantics，则停止并回 Planner/Critic。

请确认三份文件里已经没有“总调用最多两次”与“允许重跑”并存的冲突文字。

如果 E2 已关闭，不要新增任意 retry counter、replay ledger 或固定调用次数。

## 四、只做直接 regression check

检查这两处 amendment 是否直接破坏以下已经批准的 package boundary：

- technical task key 仍是 `cross-repo--workflow-identity-gate-lifecycle`;
- human-readable name 仍是 `工作流命名与插件回归机制完善（AI_Skills + Bridge）`;
- cutover bootstrap不变；
- exact two repo scope不变；
- G1–G7不变；
- `BROAD_FULL_FALLBACK`不变；
- final candidate tuple不变；
- version slots不变；
- 056 non-concurrency / stale-slot rule不变；
- no paid API/private data/Host mutation；
- no PR/main merge/tag/release/publish/deploy；
- no registry/database/ledger/controller/watcher/state machine；
- no docs directory migration；
- plugin TODO 不因本轮纯 contract amendment 机械修改。

如果没有由 E1/E2 amendment 直接产生的新具体回归，不要重新审上一轮已接受的 replay sufficiency、版本架构、bootstrap 或 G1–G7设计。

## 五、PASS / REVISE

优先逐项写：

```text
C-WIGL-E1-REMOTE-IDENTITY-PREFLIGHT=CLOSED|OPEN
C-WIGL-E2-REPLAY-COUNT-SEMANTICS=CLOSED|OPEN
```

若仍 OPEN，必须用原 finding ID 说明：

- 具体仍不一致的文件/文字；
- causal execution risk；
- 最小关闭条件。

只有本轮修改确实引入新的具体 blocker 才允许新增 finding；不要移动终点。

如果两个 finding 均 CLOSED 且无直接回归，应收敛为 execution-ready PASS。

## 六、execution-ready PASS 输出

因为本 execution-package round 已经出现正式 REVISE，如果最终 PASS，先用正常中文说明：

- E1 怎样把 fetch/push destination identity 纳入授权边界；
- E2 怎样把“两个 scenario”与“同 scenario bounded rerun”区分开；
- 哪些原 design/package部分保持不变；
- PASS 仍不等于已经执行/merge/release。

然后输出：

```text
APPROVED_PROPOSAL_PATH=docs/design/workflow-governance/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V2_PROPOSAL_2026-09-20.md
APPROVED_PLAN_PATH=docs/design/workflow-governance/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V2_1_IMPLEMENTATION_PLAN_2026-09-20.md
APPROVED_GOAL_PATH=docs/goals/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V2_1_GOAL.md
APPROVED_KICKOFF_PATH=docs/operations/prompts/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V2_1_KICKOFF.md
APPROVED_PACKAGE_COMMIT=1d13a6ebdc81fa8be2c3726d2025165c611ce96b
DECISION=PASS
COMPLEXITY=APPROPRIATE
C-WIGL-E1-REMOTE-IDENTITY-PREFLIGHT=CLOSED
C-WIGL-E2-REPLAY-COUNT-SEMANTICS=CLOSED
READY_FOR_CODEX=YES
NEXT_HANDOFF=CODEX
```

并按照 `CRITIC_ROLE_CONTRACT.md`，逐字输出 revised package commit 中已经审过的 `## Kickoff` 正文：

```text
=== APPROVED CODEX KICKOFF BEGIN ===
<verbatim revised Kickoff正文>
=== APPROVED CODEX KICKOFF END ===
```

不要 PASS 后重写或扩权。Critic PASS 本身不执行；只有用户真正发送 approved Kickoff，才形成 execution authorization。
