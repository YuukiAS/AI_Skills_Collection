# Workflow Identity & Capability Gate Lifecycle — Critic Prompt v2

你是 AI Research Stack 的长期独立 Critic thread。

继续同一个 `workflow-identity-and-gate-lifecycle` 设计轮次。不要创建 successor task，不创建 Reviewed Handoff task/branch/worktree，不启动 Executor，不运行 paid API，不修改 production。

## Active Review Context

```text
target_repo = YuukiAS/AI_Skills_Collection
target_plugin_or_domain = AI Skills Maintainer + workflow-core + Bridge Kit Reviewed Handoff
design_topic_or_task_key = workflow-identity-and-gate-lifecycle
review_stage = DESIGN_PROPOSAL_R2
source_branch_or_ref = AI_Skills_Collection main
proposal_path = docs/design/workflow-governance/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V2_PROPOSAL_2026-09-20.md
proposal_version = v2
proposal_commit = 7a01c84c1c7f5a6419f62623cf8edc42199d33a4
prior_proposal_path = docs/design/workflow-governance/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V1_PROPOSAL_2026-09-20.md
prior_critic_review_path = docs/design/workflow-governance/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V1_CRITIC_REVIEW_2026-09-20.md
prior_critic_review_commit = 4ba429ebb510d6088f947468e624a1b043d19022
stable_blockers = C-WIGL-01-SCOPE-PRECEDENCE, C-WIGL-02-IMPACT-FALLBACK-BOUNDARY, C-WIGL-03-IDENTITY-CUTOVER-COVERAGE
execution_branch/worktree = NONE
```

本轮 Planner 对三个 blocker 均为 `ACCEPT`，没有 `REBUT`。请优先复核原 blocker 和 v2 修改影响，不要重新设计已经在 v1 review 中接受的架构；只有真实新证据或 v2 新增风险才可提出新 blocker。

## 一、强制读取

先读取 AI_Skills_Collection 最新 main：

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/PLUGIN_MATURITY.md`
- `docs/design/workflow-governance/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V1_PROPOSAL_2026-09-20.md`
- `docs/design/workflow-governance/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V1_CRITIC_REVIEW_2026-09-20.md`
- `docs/design/workflow-governance/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V2_PROPOSAL_2026-09-20.md`
- 当前 `docs/design/056_PRODUCT_DELIVERY_DISCIPLINE_IMPLEMENTATION_PLAN.md`
- 当前 `docs/goals/056_PRODUCT_DELIVERY_DISCIPLINE_GOAL.md`

再读取 GPT_Codex_AI_Bridge_Kit 当前最新 main 与 task-key 直接相关的最小 source：

- `ai_bridge_kit/reviewed_handoff.py`
- `ai_bridge_kit/cli.py` 中 task-key validation
- `scripts/validate_handoff_workspace.py`
- text/visual review 与 `task_key` identity 直接相关的必要 source/tests
- task/result/branch propagation 直接相关的必要 source/tests

不要用旧聊天替代真实 source。

## 二、只复核三个原 blocker

### C-WIGL-01-SCOPE-PRECEDENCE

检查 v2 是否已经形成真正互斥的 precedence：

1. 多于一个 mutable canonical repo -> `cross-repo`
2. 恰好一个 mutable AI_Skills repo且多个中央 plugin production behavior 在 scope -> `cross-plugin`
3. 恰好一个 plugin -> `plugin-<canonical-plugin-slug>`
4. 单 repo、非 plugin-wide -> `repo`

Read-only references 不计入。

重点确认：

- 当前 056 的 Plan/Goal 确实需要 AI_Skills + Bridge 两个 mutable repos；
- 因此示例改成 `cross-repo--product-delivery-discipline` 是否正确；
- workflow-core / web-development / ai-skills-core 的 ownership 是否仍在 frozen Plan 内明确表达；
- companion plugin、generated parity、release metadata 是否不会错误把单插件 task 升级成 cross-plugin/repo；
- Bridge 是否只做 lexical validation，而没有开始判断 AI_Skills semantic scope。

如果以上已经关闭，不要仅为“还能有别的命名偏好”继续阻塞。

### C-WIGL-02-IMPACT-FALLBACK-BOUNDARY

检查 v2 是否真正把 narrow/broad 的边界变成可执行规则，而不是换一组抽象词。

至少核对强制 broad/full fallback 是否覆盖：

- shared generation / prompt assembly；
- model / runtime / provider / router；
- normal-entry / install / invocation；
- 被多个 release-critical Gate 消费的 shared layer；
- impact 无法可靠追踪；
- 新 failure 未归因或 multi-gate attribution；
- grader/eval semantics 实质变化；
- maturity promotion。

同时核对：

- narrow 只有在 isolation 可解释、applicable cheap deterministic known-regression bank 全 PASS 时才合法；
- 所有 release-critical Gate 仍有同一 final candidate 的 direct evidence；
- unaffected Gate canary 不能是文件/schema proxy；
- broad/full 不等于每个历史 qualitative/paid case 重跑；
- 没有固定 fresh/manual/paid 样本数；
- 没有 impact registry、dependency database、ledger；
- grader/eval semantics change 的校准与历史 evidence 处理不会伪造 fresh/PASS。

Critic 可以要求文字精确化，但只有仍存在真实 regression hole 才保持 blocker。

### C-WIGL-03-IDENTITY-CUTOVER-COVERAGE

不要新增 G8。逐项检查 G1/G2/G4 是否覆盖：

- canonical Reviewed Handoff task creation；
- generic workspace validation；
- `automation/reviewed_handoff/tasks/<task_key>/`；
- `results/<task_key>/`；
- `reviewed/<task_key>`；
- CURRENT / PLAN / RESULT / REVIEW / FINAL_REPORT；
- text-review manifest/evidence；
- visual-review manifest/evidence；
- current task-bound Planner/Reviewer/Executor path consumers；
- legacy numbered + semantic task 同 workspace coexistence；
- cutover 后 canonical new numeric creation 被拒绝；
- legacy numeric validation 继续合法。

特别审 v2 的这条边界是否合理：

> 不新增 registry 时，generic validator 不根据时间猜 numeric task 是历史还是新建；canonical creation 负责拒绝新的 numeric key，而 validator 为历史兼容继续 dual-format。

如果你认为这仍存在可利用的 production hole，请说明具体 normal entry 和最小解决条件；不要通过新增 creation ledger/timestamp registry 来“解决”。

## 三、确认 v1 已接受方向没有回归

v2 不应重新打开这些已接受方向：

- stable Gate taxonomy + growing regression bank；
- same-final-candidate；
- Gate merge/split/retirement 不删除历史 obligation；
- 001–057 完全不 rename/migrate；
- repair/review/integration 同 task key；
- semantic collision fail-closed + semantic disambiguation；不加 UUID/date/sequence；
- Bridge 只管 lexical syntax / compatibility / propagation；
- AI Skills Maintainer 管 AI_Skills scope semantics、regression maintenance、release closure；
- workflow-core 不成为第二 parser；
- domain plugin 保留专业 judgment；
- 不新增 controller/watcher/database/registry/ledger/state machine；
- task-local docs directory grouping 已 defer，不进入 implementation scope。

若 v2 意外破坏其中一项，可作为新证据指出；否则不要重新争论。

## 四、Capability Gate Matrix v2

审 G1–G7 是否比例合适，尤其：

- G1：semantic canonical creation + numeric creation rejection + collision fail-closed；
- G2：identity propagation 的完整 consumer coverage；
- G3：scope precedence；
- G4：legacy coexistence/cutover；
- G5：Gate lifecycle；
- G6：narrow vs broad/full release safety；
- G7：无治理膨胀。

不要因为 G1/G2/G4 更具体就机械新增 G8，也不要把 text/visual review 拆成多个重复 Gate。

## 五、外部研究

v2 仅针对原 blocker 做小修。可以复用/独立核查 v1 已用的官方原则，但仍需确认关键现实依据没有被 Planner误用：

- Anthropic: capability vs regression eval、saturated capability eval -> regression suite；
- Microsoft TIA: impacted selection + safe full fallback when impact cannot be understood。

不需要为了本轮小修扩展成新的框架调研。

## 六、复杂度审查

明确判断 v2：

```text
TOO_SIMPLE | APPROPRIATE | TOO_COMPLEX
```

重点检查 v2 是否：

- 已关闭三个真实 blocker；
- 没有借修 blocker 增加新 registry/schema/state；
- 没有把 semantic naming 做成另一个复杂 taxonomy；
- 没有把成熟 plugin 的 regression protection 简化成 weak canary；
- 没有让每个小 patch 都必须做 broad/full expensive review。

## 七、输出与保存

如果保存 review，只写 Critic review 文档，不修改 v2 Proposal、不修改 production、不修改 Bridge。

建议路径：

`docs/design/workflow-governance/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V2_CRITIC_REVIEW_2026-09-20.md`

最终先用正常中文给 closure explanation，因为 v1 已正式 REVISE。至少说明：

- C-WIGL-01/02/03 各自是否关闭以及依据；
- 056 为什么现在归 `cross-repo`；
- narrow/broad fallback 如何防 regression 又不导致 Gate/paid review 无限增长；
- identity cutover 如何同时支持 legacy + semantic；
- 哪些层明确没有新增复杂机制；
- PASS 证明什么、不证明什么。

然后给：

```text
REVIEWED_PROPOSAL_PATH=docs/design/workflow-governance/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V2_PROPOSAL_2026-09-20.md
REVIEWED_PROPOSAL_VERSION=v2
REVIEWED_PROPOSAL_COMMIT=7a01c84c1c7f5a6419f62623cf8edc42199d33a4
DECISION=PASS|REVISE
COMPLEXITY=TOO_SIMPLE|APPROPRIATE|TOO_COMPLEX
C-WIGL-01=OPEN|CLOSED
C-WIGL-02=OPEN|CLOSED
C-WIGL-03=OPEN|CLOSED
BLOCKERS=...
NON_BLOCKING=...
READY_FOR_EXECUTION_PLAN=YES|NO
```

即使 PASS，本轮也只允许回 Planner 进入 execution-package planning。不要生成 executable Codex Kickoff，不授权 production、paid API、branch/worktree、merge/release。

按 `CRITIC_ROLE_CONTRACT.md` 结尾自动生成下一条 Planner prompt：

```text
NEXT_HANDOFF=PLANNER
=== COPY TO PLANNER BEGIN ===
...
=== COPY TO PLANNER END ===
```
