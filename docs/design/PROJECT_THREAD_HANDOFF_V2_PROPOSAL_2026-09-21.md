# Project Thread Handoff — V2 Proposal

日期：2026-09-21  
阶段：pre-implementation design review  
状态：AWAITING_INDEPENDENT_CRITIC_RECHECK  
Target repo：`YuukiAS/AI_Skills_Collection`  
Source branch：`main`  
Reviewed baseline：`9f1c0d32abf49e674bcc7cab0e7287ed714a1199`  
Bridge reference baseline：`YuukiAS/GPT_Codex_AI_Bridge_Kit main@9d2da9f485f26ca51842a1909a276cb44f73351a`  
Design topic：`project-thread-handoff`  
Prior Critic verdict：`APPROVE_WITH_CHANGES`  
Blockers：`PTH-01`, `PTH-02`, `PTH-03`

本文件是完整 V2 设计，不是 implementation Plan，不授权修改 production source。

## 1. 本轮 source drift 核对

本轮只做 targeted revalidation。AI_Skills 当前 main 仍为
`9f1c0d32abf49e674bcc7cab0e7287ed714a1199`，与 reviewed baseline 完全一致；
Bridge Kit 当前 main 仍为
`9d2da9f485f26ca51842a1909a276cb44f73351a`，与 reference baseline 完全一致。

因此没有与本方案直接相关的 main drift，不重新做 full-repo audit。角色合同继续使用
`PLANNER_ROLE_CONTRACT.md` v1.4、`CRITIC_ROLE_CONTRACT.md` v1.4，并已重新核对
`PLUGIN_CAPABILITY_GATE_POLICY.md`、`AGENTS.md`、`docs/SKILL_AUTHORING.md` 和当前
`skill-creator` 的 `agents/openai.yaml` contract。

## 2. Planner 对 Critic findings 的处理

- `PTH-01 — authority / recency contract`：ACCEPT。
- `PTH-02 — explicit invocation metadata`：ACCEPT。
- `PTH-03 — actual normal-entry regression`：ACCEPT。

本轮没有 REBUT。三个 finding 都能用较小改动关闭，不需要增加 plugin、MCP、数据库、状态机或额外交互。

## 3. 产品目标与 V1 边界

Project Thread Handoff 只解决一个问题：

> 长期项目旧 thread 快到上下文/线程长度边界时，用户显式调用一次 Skill，旧 thread 直接生成一份最小充分的新 thread 初始化 Prompt。

典型项目包括 CAT-TRACE、DII、CardiacNexus。V1 不负责项目知识管理，不复制完整历史，不维护另一份 CURRENT，不自动打开新 thread，不自动写 repo。

用户默认操作只有一次显式调用。正常情况不确认、不问表单、不要求用户重复项目背景。

建议 skill：

`skills/science/communication/project-thread-handoff/`

V1 source 只需要：

```text
SKILL.md
agents/openai.yaml
evals/trigger_queries.json
```

不增加 scripts、references、assets，除非实现时出现目前未知且真实需要的最小理由。

## 4. 核心机制：最小充分认知续接

Handoff 不是“总结旧聊天”，而是从旧 thread 提取那些如果丢失会让新 thread：

- 搞错当前研究目标；
- 搞错关键实体角色；
- 重新打开已经关闭的旧路线；
- 把假设当结果；
- 不知道下一步；
- 不知道应从哪个 canonical source 恢复事实。

能从项目 repo、实验 artifact、正式报告、Deep Research 等可靠恢复的事实，默认只给 locator，不大量复制。

## 5. PTH-01：authority / recency contract

### 5.1 先按 claim type 判断 authority，不使用简单“最后一句赢”

#### A. 当前研究意图 / 决策

优先级：

1. 用户最新明确决定、纠正或明确冻结的决定；
2. 较早仍未被替代的用户/冻结决定；
3. 用户明确采纳的 assistant 建议；
4. assistant 自己的 brainstorming / exploration。

更晚出现的 assistant brainstorming 永远不能仅凭“更晚”覆盖用户已经明确决定的方向。

#### B. 工程、实验、数值与运行事实

当前 canonical repo / artifact / report 是事实 authority。聊天里的记忆、摘要或 assistant 推测不能覆盖当前 artifact。

用户可以改变“接下来做什么”或“如何解释当前问题”，但不能仅靠一句计划把尚未验证的实验结果变成事实。

### 5.2 thread-only delta

如果 thread 中存在**比 canonical repo 更新、但尚未持久化的明确用户决定/冻结决定**：

- 必须带入 handoff；
- 标记为“thread-only delta / 尚未持久化”；
- 对研究意图、当前路线、命名、下一步等决策语义，可明确暂时 supersede repo 中更旧的计划/说明；
- 不用它伪造或覆盖 repo 中的真实实验数字、代码状态或运行事实；
- 新 thread 应在需要时把它与当前 repo 对照，并在正常项目工作流中决定是否持久化。

### 5.3 其他信息类别

- **active working hypothesis**：仅在仍影响当前推理/下一步时保留，并明确“待验证”，不能写成结论。
- **open question / unresolved item**：保留真正仍待解决的事项。
- **assistant exploration**：只有用户已采纳，或仍是明确 open question 且理解下一步必需时才保留；普通 brainstorming 直接删除。
- **rejected route with recurrence risk**：如果新 thread 很可能重新误入，最多保留一行“不要重开 + 当前原因”。
- **stale / naturally superseded history**：不进入 handoff。
- **historical chat noise**：不进入 handoff。

DII/CARE 的正确语义属于“实体角色 + 当前研究意图”，不是把 CARE 历史模型列表迁移过去：
DII 是当前工作；CARE 是当前使用的数据/数据来源；CARE challenge 模型不是当前 DII 方法体系。

### 5.4 canonical locator contract

能从外部 source 恢复的事实，优先使用短 locator。理想形式是：

```text
<repo/source> @ <branch/ref if known> : <path if known> — 用于恢复 <哪类事实>
```

规则：

- 已知 repo、branch/ref、path 时尽量写清；
- exact commit 只在 frozen artifact / result 必须绑定该版本时使用；对需要读“当前状态”的内容优先让新 thread 读取当前绑定 branch；
- 如果只确认 repo 或 source，而不知道精确 path，不得编造路径、SHA、报告名；应写“从当前 AGENTS / README / results index 定位”等真实可执行指引；
- handoff 不为了补齐 locator 自动 full-repo audit；
- 新 thread 负责重新读取 canonical source；
- locator 必须说明它负责恢复什么事实，避免“给了一堆路径但不知道为什么读”。

## 6. 输出 contract

V1 默认只输出**一份可直接作为新 thread 第一条消息的初始化 Prompt**，不附第二份审计报告、不附确认请求。

最小必需内容：

1. 当前项目 / 当前续接目标；
2. 最新有效决定与 thread-only delta（如有）；
3. 当前立即下一步；
4. canonical source locators / fact-recovery guidance。

按需内容：

- 关键实体角色：只有存在误解风险时出现；
- 当前进度：只有理解下一步必需时出现；
- active hypothesis / open question：只有仍活跃时出现；
- recurrence guard：只有被否定路线很可能重新出现时出现。

不强制固定八段模板；结构应服从“最小充分信息”。

长度：
- 800–1800 中文字仅作为常见经验范围；
- 不设机械最低字数；
- 约 2500 字作为默认软上限；
- 对未落盘公式、精确 prompt、不可重新生成的关键约束可合理突破。

## 7. PTH-02：显式 invocation contract

V1 明确选择**只允许显式调用**。

不要把 `allow_implicit_invocation` 写进普通 `SKILL.md` frontmatter。按当前 OpenAI Skill contract，新建：

`agents/openai.yaml`

至少包含：

```yaml
interface:
  display_name: "Project Thread Handoff"
  short_description: "Create a continuation prompt for a long-running project thread."
  default_prompt: "Use $project-thread-handoff to create a continuation prompt for a new thread."

policy:
  allow_implicit_invocation: false
```

不声明 MCP/tool dependency。

`SKILL.md` 保留 AI_Skills_Collection 自己要求的 source/provenance 等 metadata，但 invocation policy 只由 `agents/openai.yaml` 的 `policy` 表达。

正常入口：
- 用户通过 skill picker / 显式 `$project-thread-handoff` 调用；
- bare “总结项目”“继续项目”“handoff 是什么”不应触发；
- bare “handoff”也不作为 V1 隐式触发入口，避免在普通长项目对话中意外注入。

正常 handoff 不向用户确认。用户若只显式调用 skill 而不指定 target，则选择当前 thread 最近持续工作的主线；若用户希望指定目标，可以在同一调用中写明项目/目标，不增加第二轮确认。

## 8. Repo 与 Bridge Kit 边界

V1 完全 read-only：

- 不写当前科研 repo；
- 不写 `docs/wiki/`；
- 不写 `docs/notes/`；
- 不写 `prompts/tasks/`；
- 不 commit / push；
- 不提供 opt-in repo-write mode。

如果旧 thread 有重要且未落盘的最新判断，直接作为 thread-only delta 带入 Prompt。

Bridge Kit 不是依赖，只是已安装项目可利用的 source-role convention。如果 handoff 已知目标项目使用 Bridge Kit，可让新 thread：

1. 先读取项目自己的 `AGENTS.md` 与 `prompts/CHATGPT_RULES.md`；
2. 再按项目既有约定使用 `docs/wiki/`、`docs/notes/`、`prompts/tasks/`、`results/`。

不得假设这些文件一定存在；没有已确认 Bridge Kit 时不写这些 locator。不得复制 Reviewed Handoff / Agent Flow 的状态机。

## 9. 测试与 V1 Capability Gates

本 Skill 很小，因此只保留三个 capability gates，不创建新 Gate framework。

### G1 — Explicit Invocation Boundary

证明：
- 正式 metadata 使用 `agents/openai.yaml -> policy.allow_implicit_invocation: false`；
- 显式 `$project-thread-handoff` 可进入 Skill；
- 普通 summary / project chat / near-miss 不隐式触发。

证据：
- `evals/trigger_queries.json` 的 explicit positive、negative、near-miss；
- metadata contract test；
- 同一 final candidate 的正常安装/发现证据。

失败：
- 需要自然语言猜测才能调用；
- 未显式调用也自动进入；
- invocation policy 放错位置。

### G2 — Core Handoff Semantics / DII Normal Entry

证明：
- 真实正常入口能把旧 thread 的最新研究状态压成正确的新 thread Prompt；
- authority/recency、实体角色、locator、read-only 边界实际生效。

必须做一个真实 DII/CARE normal-entry replay：

1. 使用最终候选 Skill 的真实安装/加载身份；
2. 用显式 `$project-thread-handoff` 进入；
3. 输入采用真实失败语义：较早有 CARE challenge / CARE models 讨论，后续明确转为 DII，且 CARE 当前只是 DII 使用的数据/数据来源；
4. 输出必须：
   - 把 DII 写成当前工作；
   - 把 CARE 写成数据/数据来源，而不是当前方法体系；
   - 不恢复、不推荐 CARE 模型路线；
   - 让最新明确决定覆盖早期 exploration；
   - 对 repo 可恢复事实主要给 locator，不大段复制；
   - 最终只给一份新 thread 初始化 Prompt；
   - 不产生 repo write side effect。
5. replay 前后检查目标项目 repo 与 skill source repo 的 tracked/untracked write scope，确认没有 handoff 写入。

该 replay 不是大型 benchmark，不调用付费 evaluator，不新增独立 grader framework。

### G3 — Generalization / Should-not-change

CAT-TRACE acceptance：
- 后期明确冻结的模型、符号或数据决定覆盖早期探索；
- 不把已过时路线重新并列成当前选项。

CardiacNexus acceptance：
- pipeline、实验数字、代码状态主要指向当前 repo 恢复；
- handoff 只携带 repo 无法替代的最近研究判断、未解决问题和下一步。

同时验证：
- ordinary summary request 不触发 Skill；
- no repo-write；
- 不依赖 Bridge Kit 才能工作；
- 不 hardcode “DII/CARE” 为通用逻辑。

G1–G3 的 release-critical evidence 必须来自同一个 final candidate。机械 tests 是支撑证据，不替代 G2 的 normal-entry 行为。

## 10. 实现范围（仅在 Critic PASS 后进入 execution package）

预计 source change：

```text
skills/science/communication/project-thread-handoff/SKILL.md
skills/science/communication/project-thread-handoff/agents/openai.yaml
skills/science/communication/project-thread-handoff/evals/trigger_queries.json
tests/test_project_thread_handoff_contract.py
tests/fixtures/project_thread_handoff/...   # 仅保存最小 acceptance fixture，如实现需要
```

以及当前仓库已有的 registry/catalog/provenance/generated parity 更新。

不新增：
- plugin；
- MCP；
- database；
- CURRENT；
- handoff history；
- state machine；
- browser extension；
- automation/watchers；
- Bridge Kit production change；
- 目标科研 repo production change。

README closure：
- implementation/release closure 必须显式检查根 README 和 skills README；
- 若 standalone skill 的加入不改变中央 plugin 表格/用户安装入口，则记录 `README checked: no update required`，不为了留痕硬改 README。

版本：
- 本设计不提前指定 repository bump；
- implementation/release Plan 必须按当前版本政策读取真实 source 后给出版本决策；
- 本 Skill 不对应任何现有中央 plugin version bump；
- Bridge Kit version 不变。

## 11. 失败恢复与停止条件

如果实现发现需要以下任一项才能让 V1工作，停止并返回 Planner/Critic，不得临时扩 scope：

- 必须新增 plugin/MCP；
- 必须写用户项目 repo；
- 必须引入持久状态；
- 必须依赖 Bridge Kit；
- 必须加入自动触发才能实现核心 UX；
- normal-entry replay 只能靠测试脚本 hardcode 而正式入口不成立。

普通 wording、fixture、contract test 修复属于已批准范围内的实现调整，不因小修重新设计。

## 12. 当前产品可用性边界

当前 OpenAI 官方文档显示：ChatGPT 中“个人 Skills”的创建/安装目前面向符合条件的
Business、Enterprise、Healthcare、Edu 用户；Codex 等其他产品也可支持 Skills。

因此本 V2 **不声称 ChatGPT Pro Web 目前已经可以原生安装并调用这个 standalone Skill**。
用户当前是 Pro，这一点属于产品 surface 可用性约束，而不是 Skill 本身需要加数据库/Plugin 的理由。

V1 可继续作为正确的 standalone Skill source/behavior 设计，并在支持 standalone Skill 的真实 runtime 做 G1/G2 normal-entry 验证；但最终交付时必须区分：

- `SKILL_BEHAVIOR_READY`：standalone Skill 本身已通过；
- `CHATGPT_PRO_NATIVE_ENTRY_VERIFIED`：只有实际 Pro ChatGPT surface 真能安装/调用后才能声称。

如果用户以后要求“现在就在 Pro Web 原生一键调用”，而产品仍不提供 personal Skill entry，那将是新的 distribution/packaging 决策；本 V1 不擅自改成 Plugin。

## 13. V1 完成定义

V1 只有在同一 final candidate 满足以下条件时才可称 standalone Skill capability ready：

- 显式 invocation metadata 正确；
- contract/trigger tests 通过；
- DII/CARE 真实 normal-entry replay 通过；
- CAT-TRACE、CardiacNexus acceptance 不暴露过拟合/角色误判；
- output 是一份最小充分初始化 Prompt；
- no repo-write side effect；
- source/generated/provenance/registry/catalog parity 通过；
- README closure 已检查；
- 版本决策按当前 policy 完成。

这不自动等于 ChatGPT Pro Web native entry 已可用，也不等于任何 plugin release。
