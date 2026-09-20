# 工作流命名与插件回归机制完善（AI_Skills + Bridge）— Execution-ready Critic Prompt v2.1

你是 AI Research Stack 的长期独立 Critic thread。

继续同一个 `workflow-identity-and-gate-lifecycle` 设计轮次。设计 v2.1 已 PASS；本轮只审 execution package 是否忠实、可执行、不过重也不过简。

不要实现代码，不创建 task/branch/worktree，不启动 Executor，不运行 paid API，不修改 production，不替用户发送 Kickoff。

## Active Review Context

```text
target_repo = YuukiAS/AI_Skills_Collection
human_readable_name = 工作流命名与插件回归机制完善（AI_Skills + Bridge）
technical_task_key = cross-repo--workflow-identity-gate-lifecycle
target_plugin_or_domain = AI Skills Maintainer + workflow-core + Bridge Kit Reviewed Handoff
design_topic = workflow-identity-and-gate-lifecycle
review_stage = EXECUTION_READY_PACKAGE_REVIEW
source_branch_or_ref = AI_Skills_Collection main

approved_proposal =
docs/design/workflow-governance/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V2_PROPOSAL_2026-09-20.md
proposal_version = v2.1
proposal_commit = ba2fc85f9c58b9b332eb07f821d1756b417fe1d1

design_critic_pass =
docs/design/workflow-governance/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V2_1_CRITIC_REVIEW_2026-09-20.md
design_critic_pass_commit = 1427c7060776719e2e1ae191b681ab2e1a608705

implementation_plan =
docs/design/workflow-governance/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V2_1_IMPLEMENTATION_PLAN_2026-09-20.md
plan_version = v2.1

canonical_goal =
docs/goals/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V2_1_GOAL.md
goal_version = v2.1

kickoff_draft =
docs/operations/prompts/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V2_1_KICKOFF.md
kickoff_version = v2.1

package_content_commit = 0f2b9adb3f00e520ca18c941c37c20a04e2111e8

execution_branch/worktree = NOT_CREATED
```

设计 blocker 已全部关闭：

```text
C-WIGL-01-SCOPE-PRECEDENCE = CLOSED
C-WIGL-02-IMPACT-FALLBACK-BOUNDARY = CLOSED
C-WIGL-03-IDENTITY-CUTOVER-COVERAGE = CLOSED
C-WIGL-04-HUMAN-READABLE-WORKFLOW-LABEL = CLOSED
```

不要重新打开设计架构。只有 execution package 明显违背已批准 v2.1、授权不安全、验收不能证明能力、version/recovery 不成立，才 REVISE。

## 一、强制读取

先读取 AI_Skills_Collection 最新 main：

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md`
- approved Proposal v2.1
- design Critic PASS v2.1
- Implementation Plan v2.1
- Canonical Goal v2.1
- Kickoff Draft v2.1
- current `VERSION`
- current `scripts/codex_marketplace_config.json`
- current workflow-core / ai-skills-core changelogs
- current `skills/core/codex-system/codex-workflow-protocol/`
- current `skills/core/codex-system/ai-skills-repository-maintainer/SKILL.md`
- current 056 review package / Plan / Goal，仅用于核对 overlap/source-drift 事实，不重审 056 架构。

再读取 GPT_Codex_AI_Bridge_Kit 当前 latest main：

- `AGENTS.md`
- `pyproject.toml`
- `CHANGELOG.md`
- `ai_bridge_kit/reviewed_handoff.py`
- `ai_bridge_kit/cli.py`
- `scripts/validate_handoff_workspace.py`
- `ai_bridge_kit/reviewed_runner.py`
- `ai_bridge_kit/text_review.py`
- `ai_bridge_kit/visual_review.py`
- relevant reviewed-handoff / repo-cli / text-review / visual-review tests
- relevant task-authoring templates/docs still using numbered examples.

只 targeted read必要 source，不做无关全仓审计。

## 二、先审 execution package 是否忠实于 v2.1

逐项确认 Plan/Goal/Kickoff 没有偷偷改变设计：

- Bridge 只负责 lexical syntax / legacy compatibility / canonical creation / generic validation / identity propagation；
- AI_Skills负责 scope semantics、Gate lifecycle、regression-bank/release-selection policy与最小 consumers；
- workflow-core 不实现第二 parser；
- domain plugin 不被 maintenance/workflow吞掉专业判断；
- 001–057 不 rename/migrate；
- canonical new creation semantic-only；
- generic validation legacy + semantic；
- repair/review/integration 同 technical key；
- G1–G7，不新增 G8；
- same-final-candidate；
- narrow/broad-full fallback 完整保留；
- no registry/database/ledger/controller/watcher/state machine；
- no docs directory reorganization；
- technical key != human-readable label；
- no task display-name schema/registry/title service；
- 不声称控制 client auto title。

如果包内任何一处实质偏离 approved design，应 REVISE；不要由 Critic 临场改写 Kickoff。

## 三、审 cutover bootstrap 是否真实可执行

当前 Bridge main 的 canonical task init 仍拒绝 semantic key。Execution package 采用一次性 cutover boundary：

- 不新建 numeric successor；
- 不手写 semantic CURRENT；
- 使用 approved Plan/Goal/Kickoff + exact semantic Git branches 执行实现；
- candidate 支持 semantic creation 后，在 isolated fixture repo 通过正式 CLI 验证 normal entry。

请独立判断这是否是最小、诚实的 bootstrap。

重点攻击：

1. 是否存在循环依赖，导致 Executor 实际上仍需要预先伪造新 contract；
2. exact semantic branch 本身是否能在普通 Git ref 规则下合法使用；
3. 是否应该创建另一个临时 task/state/registry——默认答案应是“不需要”，除非你找到真实不可执行证据；
4. 是否清楚说明“第一条普通 production semantic task 在 integration/release 后才创建”，没有 retroactive self-certification。

如果 cutover 可以靠现有 Goal/Kickoff + branch 正常执行，不要为了形式强迫创建 legacy successor。

## 四、审真实修改范围

### Bridge

检查 Plan 是否漏掉或过度扩大：

- one canonical lexical authority/helper；
- `reviewed_handoff.py` new creation；
- `cli.py` generic validation；
- `scripts/validate_handoff_workspace.py`；
- reviewed runner / Text Review / Visual Review 只做必要 propagation；
- normal authoring docs/templates从 numeric new-task default转为 semantic；
- legacy examples/history保留；
- tests覆盖G1/G2/G4。

拒绝：

- Bridge读取AI_Skills registry；
- Bridge判断 `cross-repo` 语义；
- second identity field；
- Review state/schema/role改造；
- unrelated Lite/Control redesign。

### AI_Skills

检查最小 consumer alignment 是否足够：

- `PLUGIN_CAPABILITY_GATE_POLICY.md`；
- root `AGENTS.md`；
- Planner/Critic contracts必要 naming/scope locator规则；
- workflow-core source/references；
- AI Skills Maintainer source；
- generated parity；
- version/changelog/tests。

Critic 要特别判断：

- 是否真的需要修改 Planner/Critic contracts，还是某处已有同义规则只需最小补充；
- 是否应该修改 plugin TODO，还是当前已有设计 authority/changelog 已足够，避免为“留痕”制造重复 TODO；
- 是否存在漏掉的 actual production consumer，导致 policy只写在 docs里没进 plugin runtime。

## 五、审 G1–G7 normal-entry acceptance

不能只审“有测试”。

### G1

必须能通过 candidate Bridge 的 canonical CLI normal entry 创建 semantic task，并拒绝 malformed/collision/new numeric。

### G2

必须覆盖 exact semantic key 传播到：

- task dir
- result dir
- `reviewed/<task_key>`
- CURRENT
- PLAN
- RESULT
- REVIEW
- FINAL_REPORT
- task-bound Planner/Reviewer/Executor
- Text Review manifest/evidence
- Visual Review manifest/evidence。

### G3

AI Skills Maintainer实际 consumer/replay必须证明：

- single plugin
- one-repo multi-plugin
- repo-wide non-plugin
- multi-mutable-repo
- read-only refs不计入
- 056-like -> cross-repo。

Bridge不应判断这些。

### G4

同一 isolated workspace 必须 coexist：

- legacy numbered task仍validation合法；
- semantic task通过canonical new creation；
- new numeric canonical creation失败。

### G5

实际 maintenance consumer/replay要区分：

- existing capability regression -> existing Gate；
- genuinely new capability -> Gate redesign consideration。

不能只靠关键词 assertion。

### G6

本任务应当是 `BROAD_FULL_FALLBACK`。核对：

- full cheap deterministic applicable bank；
-所有 G1–G7 same final tuple direct evidence；
- workflow-core replay能区分合法 narrow与mandatory broad/full；
- no fixed paid/fresh count；
- no old-candidate stitching。

### G7

直接审真实 diff/计划边界，不允许出现新 control system、parser duplication、display-name service、docs migration。

## 六、审 candidate plugin replay 设计

Package 只授权最多两次 public-safe candidate plugin replay：

1. Verified Workflow
2. AI Skills Maintainer

检查：

- 是否足够证明 actual generated/installed production consumer，而不只是 source prose；
- 是否可以在不调用 Terra/OpenAI Responses/private data 的情况下完成；
- 是否没有把同一个 candidate失败后变成“追加更多样本直到 PASS”；
- failure recovery是否只允许修 approved architecture 内 defect；
- domain judgment是否仍不由这两个 plugin越权判断。

如果两次 replay 太少以至于无法覆盖 package claim，应指出具体漏掉哪项独立 capability；不要机械加样本数。

## 七、审版本与 056 overlap

当前 package冻结的 planning baseline：

```text
AI_Skills:
Repository 5.0.5
workflow-core 0.1
ai-skills-core 0.2

Bridge:
0.8.3
```

candidate slots：

```text
AI_Skills repository 5.0.5 -> 5.0.6 PATCH
workflow-core 0.1 -> 0.2
ai-skills-core 0.2 -> 0.3
all other plugins NO_BUMP
Bridge 0.8.3 -> 0.8.4
```

请按 version policy 独立判断这些 bump 是否成立。

同时核对 current 056：

- 当前是否仍 `READY_FOR_CODEX=NO`；
- 是否确实与 workflow-core / ai-skills-core / Bridge重叠；
- package要求两者不得并发修改shared source；
- kickoff preflight若发现056或其他任务已经消耗source/version slot，必须 mutation前回Planner；
- Executor不得自行变成 5.0.7 / 0.3 / 0.4 / 0.8.5。

如果 current source 已经发生变化，以你实际读取到的最新 source为准，不使用本 prompt中的旧值硬判。

## 八、审同一 final candidate tuple

Package用：

```text
AI_SKILLS_FINAL_CANDIDATE_COMMIT
BRIDGE_FINAL_CANDIDATE_COMMIT
```

组成 cross-repo final candidate tuple。

检查：

- production/source/generated/version在tuple freeze前完成；
- G1–G7绑定exact tuple；
- tuple freeze后production变更会invalidate相关evidence；
- control/evidence-only write不会被误当新product candidate；
- 不允许 Bridge旧candidate + AI_Skills新candidate拼PASS。

## 九、审授权边界

Kickoff如果 PASS，用户发送后将授权：

- 两个 exact semantic task branches；
- 两个 exact /tmp task-owned worktrees；
- Goal列出的 source/tests/docs/generated/version metadata；
- focused/full tests；
- 最多两次 public-safe candidate plugin replay；
- GitHub fetch/check 与 ordinary non-force push exact task branches。

检查授权是否**足够执行但不过宽**。

必须保持未授权：

- paid Responses/Terra；
- private data replay；
- real Host Policy mutation；
- PR/main merge/tag/release/publish/deploy；
- remote/upstream mutation；
- force/destructive Git；
- domain product changes；
- 056 mutation；
- arbitrary new branch。

如果 Kickoff需要实质语义修改，必须 REVISE；不要 PASS 后自己重写一个更宽的 prompt。

## 十、审恢复路径

确认 package 能区分：

- source/version drift before mutation；
- ordinary implementation bug；
- G2 propagation defect；
- G4 legacy regression；
- candidate replay failure；
- architecture/ownership/parser/state change requirement；
- unrelated suite failure；
- waiting for independent review。

不要允许：

- blind retry；
- adaptive sample chasing；
- silent version bump；
- silent merge with 056；
- successor链；
- 为解决一个consumer失败新增registry/state machine。

## 十一、复杂度判断

明确输出：

```text
COMPLEXITY=TOO_SIMPLE|APPROPRIATE|TOO_COMPLEX
```

同时攻击：

- 是否太简单：只改regex/docs，未接通normal entry/generated plugin；
- 是否太复杂：为了 semantic key 新建 control/identity infrastructure；
- 是否版本/replay/全量测试过重；
- 是否反而漏掉 shared normal-entry regression。

## 十二、PASS 条件与输出

只有同一 package commit 下：

1. Proposal v2.1；
2. Implementation Plan v2.1；
3. Canonical Goal v2.1；
4. Kickoff Draft v2.1

全部一致且无 blocker，才能 execution-ready PASS。

若 REVISE：
- stable finding IDs；
- evidence / causal risk / minimum closure / owner；
- 自动输出下一条 Planner prompt。

若 PASS：
先用正常中文说明：

- 这个 execution package 实际将改什么；
- 为什么 cutover bootstrap 不需要旧 0xx successor；
- G1–G7 怎样证明 normal entry；
- 为什么本任务必须 broad/full；
- version decision为什么成立；
- human label如何降低用户认知负担；
- 哪些高影响动作仍未授权。

然后严格输出：

```text
APPROVED_PROPOSAL_PATH=docs/design/workflow-governance/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V2_PROPOSAL_2026-09-20.md
APPROVED_PLAN_PATH=docs/design/workflow-governance/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V2_1_IMPLEMENTATION_PLAN_2026-09-20.md
APPROVED_GOAL_PATH=docs/goals/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V2_1_GOAL.md
APPROVED_KICKOFF_PATH=docs/operations/prompts/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V2_1_KICKOFF.md
APPROVED_PACKAGE_COMMIT=0f2b9adb3f00e520ca18c941c37c20a04e2111e8
DECISION=PASS
COMPLEXITY=...
READY_FOR_CODEX=YES
NEXT_HANDOFF=CODEX
```

并逐字输出已审过的 `## Kickoff` 正文：

```text
=== APPROVED CODEX KICKOFF BEGIN ===
<verbatim approved Kickoff正文>
=== APPROVED CODEX KICKOFF END ===
```

不要 PASS 后重新设计、扩权或另写一个语义不同的 prompt。

本 Critic PASS 本身仍不执行。只有用户真正发送 approved Kickoff，才形成本轮 Codex execution authorization。
