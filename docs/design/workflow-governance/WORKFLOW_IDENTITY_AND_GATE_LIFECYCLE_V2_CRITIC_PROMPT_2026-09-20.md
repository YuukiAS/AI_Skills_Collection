# Workflow Identity & Capability Gate Lifecycle — Critic Prompt v2.1

你是 AI Research Stack 的长期独立 Critic thread。

继续同一个 `workflow-identity-and-gate-lifecycle` 设计轮次。本轮只审最小 v2.1 naming clarification。不要创建 successor task，不创建 Reviewed Handoff task/branch/worktree，不启动 Executor，不运行 paid API，不修改 production。

## Active Review Context

```text
target_repo = YuukiAS/AI_Skills_Collection
target_plugin_or_domain = AI Skills Maintainer + workflow-core + Bridge Kit Reviewed Handoff
design_topic_or_task_key = workflow-identity-and-gate-lifecycle
review_stage = DESIGN_PROPOSAL_R3
source_branch_or_ref = AI_Skills_Collection main
proposal_path = docs/design/workflow-governance/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V2_PROPOSAL_2026-09-20.md
proposal_version = v2.1
proposal_commit = ba2fc85f9c58b9b332eb07f821d1756b417fe1d1
prior_critic_review_path = docs/design/workflow-governance/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V2_CRITIC_REVIEW_2026-09-20.md
prior_critic_review_commit = c8c349432b2f1343f87c73d6c39553abc874ae93
closed_blockers = C-WIGL-01-SCOPE-PRECEDENCE, C-WIGL-02-IMPACT-FALLBACK-BOUNDARY, C-WIGL-03-IDENTITY-CUTOVER-COVERAGE
active_blocker = C-WIGL-04-HUMAN-READABLE-WORKFLOW-LABEL
execution_branch/worktree = NONE
```

上一轮已经明确：

```text
C-WIGL-01 = CLOSED
C-WIGL-02 = CLOSED
C-WIGL-03 = CLOSED
```

不要重新打开这三项，不重做 Gate lifecycle、scope precedence、Bridge compatibility、G1–G7 或 release fallback 架构。只有 v2.1 这个小改动直接引入了新的具体回归，才允许提出新的 blocker。

## 一、实际读取

先读取 AI_Skills_Collection 最新 main：

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/design/workflow-governance/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V2_PROPOSAL_2026-09-20.md`
- `docs/design/workflow-governance/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V2_CRITIC_REVIEW_2026-09-20.md`

按需 targeted read 当前 056 Plan/Goal 与 Bridge task-key source，只用于确认 v2.1 没有破坏已关闭结论；不要再次完整重审 C-WIGL-01/02/03。

本轮是用户直接提出的命名可读性澄清，不引入新的外部技术假设。除非发现具体事实歧义，不需要为了形式再次扩展外部框架研究。

## 二、只复核 C-WIGL-04

### C-WIGL-04-HUMAN-READABLE-WORKFLOW-LABEL

检查 v2.1 是否清楚分开两层：

#### A. technical task_key

technical task_key 只承担稳定机器 locator，例如：

```text
reviewed/<task_key>
automation/reviewed_handoff/tasks/<task_key>/
results/<task_key>/
CURRENT / PLAN / RESULT / REVIEW / FINAL_REPORT 中必要 locator
text-review / visual-review manifest 与 evidence identity
```

例如：

```text
cross-repo--product-delivery-discipline
```

它不应被当作普通用户 thread title，也不应在普通正文里反复替代工作名称。

确认这个澄清没有削弱：

- semantic task-key lexical stability；
- scope precedence；
- legacy compatibility；
- branch/result/evidence identity；
- collision fail-closed。

#### B. human-readable short label

确认 v2.1 将面向人的短名称定义为**文字表面的命名约定**，而不是新的机器身份。

它可以用于我们实际能控制的：

- Planner/Critic prompt title 与开头；
- Goal 人类可读标题；
- review/report heading；
- Codex kickoff/repair/resume prompt 中给用户看的名称；
- 普通聊天、交接与状态说明。

必须确认没有新增：

- `display_name` schema field；
- registry；
- title service；
- database/ledger；
- 第二 identity mapping system；
- Bridge human-label parser。

## 三、检查命名例子是否符合用户要求

### 单插件 release

当正式 target version 已冻结时，优先人类名称：

```text
Clear Writing 0.4
Presentations 0.3
```

版本尚未冻结时：

```text
Clear Writing 发布收口
Presentations 视觉质量完善
```

Critic 只需判断这是否降低用户认知负担；不要要求把所有内部 scope/owner 拼进标题。

### cross-repo / broad workflow

当前 056 的技术 identity 示例仍可为：

```text
cross-repo--product-delivery-discipline
```

但普通用户名称应类似：

```text
开发交付流程完善（AI_Skills + Bridge）
```

历史 056 不 rename。过渡期可写：

```text
开发交付流程完善（原 056）
```

确认“原 056”只是 transition locator，而不是长期 primary label。

## 四、version 与 collision 边界

检查 v2.1 是否保持：

- version **不是**所有 technical task_key 的强制组成；
- 只有 release target 已冻结，且 version 是区分两个真实独立 workflow 最自然的语义时，才可进入 goal token，例如 `plugin-writing-style--release-0-4`；
- candidate/未冻结版本不能过早固化进 identity；
- collision 不自动追加 UUID/date/sequence；
- 同一 objective 的 repair/review/integration 继续复用原 task key；
- 不为了可读性引入新的 successor task。

如果这里已经足够，不要要求额外唯一性系统。

## 五、客户端自动标题边界

确认 v2.1 明确：

- 规则只约束 repo/workflow 能控制的 prompts、Goal、review/report heading 和普通交流；
- 不声称能控制 ChatGPT/Codex 客户端自动生成的 conversation/sidebar title；
- 客户端自动 title 与建议短名称不同，不应被误判为 repo workflow failure。

不要为了解决平台自动 title 新增 service、API、title registry 或客户端 hack。

## 六、回归检查

只检查这个小修改是否意外破坏已经通过的架构：

- C-WIGL-01 scope precedence；
- C-WIGL-02 narrow/broad fallback；
- C-WIGL-03 identity cutover；
- G1–G7；
- 001–057 no migration；
- same-final-candidate；
- stable Gate taxonomy + growing regression bank；
- Bridge lexical-only ownership；
- AI Skills Maintainer / workflow-core / domain plugin 分权；
- no controller/watcher/database/registry/ledger/state machine；
- docs directory reorganization remains deferred。

没有具体回归证据时，不要重新展开这些已关闭对象。

## 七、结论要求

明确给：

```text
REVIEWED_PROPOSAL_PATH=docs/design/workflow-governance/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V2_PROPOSAL_2026-09-20.md
REVIEWED_PROPOSAL_VERSION=v2.1
REVIEWED_PROPOSAL_COMMIT=ba2fc85f9c58b9b332eb07f821d1756b417fe1d1
DECISION=PASS|REVISE
COMPLEXITY=TOO_SIMPLE|APPROPRIATE|TOO_COMPLEX
C-WIGL-01=CLOSED
C-WIGL-02=CLOSED
C-WIGL-03=CLOSED
C-WIGL-04=OPEN|CLOSED
BLOCKERS=...
NON_BLOCKING=...
READY_FOR_EXECUTION_PLAN=YES|NO
```

由于同一设计轮次此前已经 REVISE，若本轮 PASS，先用自然中文给 closure explanation，重点说明：

- technical task_key 与 human-readable short label 如何分层；
- 用户普通交流里实际会看到什么；
- 为什么没有新增 display_name/schema/registry/title service；
- 版本什么时候能进入人类名称或 task goal token；
- 为什么历史 056/001–057 不需要 rename；
- 本次 PASS 证明什么、不证明什么。

如果 `C-WIGL-04` 已关闭且没有由 v2.1 直接引入的新 blocker，应收敛为 design PASS。不要以“还能更好”为理由移动终点。

即使 PASS，本轮也只允许返回 Planner 进入 execution-package planning。不要生成 executable Codex Kickoff，不授权 production、branch/worktree、paid API、merge/release。

按照 `CRITIC_ROLE_CONTRACT.md`，结尾自动生成下一条 Planner prompt：

```text
NEXT_HANDOFF=PLANNER
=== COPY TO PLANNER BEGIN ===
...
=== COPY TO PLANNER END ===
```
