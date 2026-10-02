# Project Instructions Editor — Standalone Skill Design v1 Critic Review

Date: 2026-10-02  
Result: `REVISE`  
Repository: `YuukiAS/AI_Skills_Collection`  
Source branch/ref: `main`  
Latest main observed for this review: `7c75515aeeec9e37322a6f60d359a5057fd1d682`  
Reviewed proposal: `docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_STANDALONE_SKILL_DESIGN_V1_PLANNER_PROPOSAL_2026-10-01.md`  
Proposal version: `v1`  
Proposal source blob on current main: `2ff61e1d4799ecfc48425ec8edc065ba55995638`  
Proposal originally introduced: `f915ffc4d9b4d7abb507d95aa2f754cef2e16726`  
Tracking: `#93`  
Review stage: future standalone Skill product/design planning only

```text
CRITIC_RESULT=REVISE
READY_FOR_FUTURE_SKILL_DESIGN=YES
READY_FOR_SKILL_IMPLEMENTATION=NO
```

## 1. 结论

v1 的主方向成立，但还不能 PASS。

独立 standalone Skill 有真实产品价值。现有证据表明问题已经超出“中文润色”或一般写作保真：它需要围绕长期 Project instruction surface 同时处理真实 live setting、相关历史决定、canonical source、有限字符预算、scope 平衡、locator 替代与 mutation radius。这一职责如果直接塞进 `chinese-prose` 或 `writing-fidelity`，会把原本清楚的写作/保真边界扩成 Project authority 与 persistence placement owner，反而增加触发冲突。

v1 对以下方向已经足够清楚，不构成阻塞：

- bounded edit 默认优先；
- full rewrite 需要跨范围的实质原因，而不是“更干净”；
- locator 不能替代必须在 source lookup 之前生效的 ownership / authority / safety / cross-task contract；
- 约 8,000 字符只被当作历史 Project 约束，不是统一产品常数；
- 字符预算按语义密度、实际限制和 Project-specific headroom 判断，不使用固定比例；
- 不建立 history database、ledger、daemon、watcher 或新 state machine；
- A–H 真实回归方向覆盖了 stale candidate、multi-scope、删除项复活、exact identity、source drift、missing baseline、no-op 与 language-independent case；
- qualitative full-output review 已被明确要求，字符数和 diff 只证明机械性质。

仍有四个会直接改变产品正确性的设计缺口，必须由 Planner 修订。

## 2. 独立外部核查

本轮按 Critic Role Contract 独立核对了 OpenAI 当前官方资料：

- OpenAI Help Center, “Projects in ChatGPT”  
  https://help.openai.com/en/articles/10169521-projects-in-chatgpt
- OpenAI Academy, “Using projects in ChatGPT”  
  https://openai.com/academy/projects/
- OpenAI Help Center, “Memory in ChatGPT”  
  https://help.openai.com/en/articles/8590148-memory-in-chatgpt
- OpenAI Help Center, “ChatGPT Custom Instructions”  
  https://help.openai.com/en/articles/8096356-custom-instructions-for-chatgpt
- OpenAI Help Center, “ChatGPT — Release Notes”  
  https://help.openai.com/en/articles/6825453-chatgpt-release-notes

截至 2026-10-02，官方 Projects 文档明确说明：

1. Project instructions 只在对应 Project 内适用，并覆盖 global custom instructions。
2. Project 可以把 chats、files、instructions 作为持续上下文；Project-only memory 可以让同一 Project 内的 chats 相互引用，同时阻断 Project 外对话。
3. 当前官方 Projects 文档没有给出一个可验证的统一 Project-instruction 字符上限。这里的正确结论是“本轮未找到官方统一限制”，不能升级为“证明不存在限制”。
4. 官方目前确实给 global Custom Instructions 单独公布了字符限制；这不能作为 Project instructions 的限制证据。

因此 Planner 拒绝把约 8,000 硬编码为统一官方限制是正确的；但 Project/global instruction 的有效性边界需要在 authority/placement 设计里更明确，见 B2。

## 3. 与现有 Skill 的边界判断

### `chinese-prose`

不重复。它负责已确定语义的中文实现与终审，不负责 Project resident/locator/task-local placement、history reconciliation、budget allocation 或 live-setting replacement safety。

### `writing-fidelity`

这是最接近的现有能力，但仍不足以替代 standalone Skill。它负责编辑过程中不破坏事实、用户纠正、版本 authority 与 artifact identity；它没有 Project-specific 的 resident placement、canonical locator、multi-scope budget 或 live/history/source reconciliation owner。

把这些职责只补成一小段 `writing-fidelity` guardrail 会让“保真层”承担 Project 产品架构判断，触发边界反而更模糊。因此 standalone Skill 方向可继续。

### `scientific-rewrite`

不重复。其单位是 source-faithful scientific/technical document structural rewrite，且有 Meaning Map / Reader Plan 等重路线；Project instructions 的核心不是科学文档重写。

### `workflow-core`

不重复。它拥有复杂任务的 process、routing、gate、evidence 与 completion semantics，不拥有 Project instruction content placement。

### `ai-skills-core`

不重复。它负责 AI_Skills_Collection 的 source/generated/release maintenance；以后实现或发布该 Skill 时会参与维护，但不应成为普通 Project instruction editing 的 runtime domain owner。

## 4. Blocking findings

### B1 — exact live setting 门禁把两类合法完整编辑一起挡住了

**对应要求**

检查 exact live setting 是否真的应该成为 full replacement 的必要条件，以及是否存在无需 exact baseline 仍可合法完整编辑的情形。

**直接证据**

Proposal §4 把 actual live Project setting 写成“Required for exact editing, deletion, full replacement, or safe to paste output”；§7.3 又规定 exact live setting 不可得时 full rewrite 被 blocked。

这对“修改已有 Project 且要保证保留旧语义”是正确的，但没有区分：

- 新建/确认为空的 Project；
- 用户明确要求 reset / discard existing setting，不要求保存旧语义；
- 对已有 setting 做保真替换。

**因果风险**

按照 v1 原文执行，Skill 会在没有旧 baseline 语义需要保护的情况下仍拒绝合法的完整候选，造成不必要的人机往返；反过来，如果实现者为绕过这条硬门槛临时放宽，又容易把真正需要 preservation 的已有 Project 当成 reset。

**最小关闭条件**

v2 必须把“full replacement”拆成至少两类语义：

1. preservation-sensitive replacement：修改已有 setting，并声称保留未授权部分；必须拿到足够精确的 live baseline。
2. greenfield / explicit-reset replacement：Project 已确认为空，或用户当前明确决定丢弃旧 setting 且不要求旧语义保真；允许在无旧 baseline 下生成完整 setting，但不得声称“保留了未知旧规则”。

同时在未来验收方向中加入一个 greenfield 或 explicit-reset 情形，证明不会把 baseline preservation gate 机械套到所有完整候选。

---

### B2 — authority placement 没有区分“语义归属”与“在当前 Project 中实际能约束行为”

**对应要求**

authority 关系与 locator substitution 必须可执行，不能因为内容“更属于 global/user layer”就把当前 Project 仍必须生效的关键语义移出 Project。

**直接证据**

Proposal §2.2、§3.3、§5 允许把规则判定为“global/user-level preference layer”或“leave with another authority layer”。

但 OpenAI 当前官方 Projects 文档明确说明 Project instructions 会覆盖 global custom instructions。仓库自己的 readability design history 也已经记录：只在 account/global 层强化可读性不足以保证 Project 内行为，因此后来才加入 Project-local bridge。

**因果风险**

如果 Skill 只按“谁在语义上拥有这条规则”决定存放位置，就可能把一条必须约束本 Project 的规则移到 global 层；该规则虽然“归属更正确”，在 Project 内却可能失去有效控制。高风险对象包括用户阅读契约、authority/permission/safety 前置规则以及 Project-local 对全局偏好的必要桥接。

**最小关闭条件**

v2 必须明确分开：

- canonical/semantic ownership：这条规则详细真相由哪个 layer/source 拥有；
- effective enforcement placement：为了让当前 Project 真正受约束，Project setting 是否仍需直接常驻语义或短 bridge/trigger。

只有当规则不需要在当前 Project 生效，或当前产品行为已验证另一个 layer 仍会有效约束该 Project 时，才可仅“leave with another authority layer”。

增加一个未来验收情形：global preference 与 Project instruction 冲突/覆盖时，编辑器不得把当前 Project 需要的控制语义误移出 Project。

---

### B3 — “targeted history”原则正确，但 partial/unavailable history 下还缺一条保护“历史删除的未知缺席”的默认规则

**对应要求**

history 设计既不能要求 exhaustive audit，也必须避免用户明确删除/拒绝的规则因为旧 candidate、summary 或 canonical material 再次复活；工具拿不到完整历史时要能诚实降级。

**直接证据**

Proposal §4.2 规定只搜索与当前编辑有关的 history；缺失时不声称 exhaustive，默认保留 unrelated live rules；若“requested edit could revive/delete a disputed rule”则停止该 mutation。

问题在于：如果历史恰好不可达，Skill 可能根本不知道某条规则曾被明确拒绝。Proposal 仍允许 old candidate / references 作为 evidence，也允许 full rewrite 做全局 relocation/deduplication。

**因果风险**

已被用户删除、因此在 live setting 中“缺席”的规则，可能从旧候选或旧总结重新进入完整候选。此时实现表面上完全符合“没有发现 disputed rule”，却重现本项目最明确的真实失败之一。

**最小关闭条件**

不需要 exhaustive history。v2 只需增加一个保守的 provenance/diff 原则：

- 当 relevant history 不可得或只部分可得时，凡“live baseline 中不存在、但只出现在旧 candidate/reference/summary”的 durable rule，默认视为 protected absence，不得仅凭旧 evidence 加回。
- 只有当前用户明确要求/重新决定加入，或当前任务明确是对某 canonical source 做同步且该 source 确实拥有这项当前事实/规则，才可引入。
- bounded edit 的未涉及部分继续保持，不扩大 history 搜索。

增加一个“history unavailable + old candidate contains previously removed rule”的未来验收情形；不规定固定样本数。

---

### B4 — A–H 测了“Skill 已经被调用以后做得对不对”，还没证明 standalone Skill 的普通入口真的可用且不会抢错任务

**对应要求**

未来验收方向必须覆盖真实用户能力，并检查 normal entry、should-not-change、完整 artifact 与 qualitative review；Standalone Skill 还必须证明它值得作为独立触发面存在。

**直接证据**

`docs/SKILL_AUTHORING.md` 明确把 Skill description 作为 trigger surface，并要求避免与邻近 Skills 高度重叠。Capability Gate policy 也要求正常入口而不是 helper/forced route 冒充产品能力。

Proposal §10 的 A–H 都从“Project editor 已经在处理这个任务”开始，没有一项证明：

- 普通用户只说“帮我改这个 Project setting”时会自然进入该 Skill；
- 普通中文润色不会被它抢走；
- 一般 writing fidelity、scientific rewrite、AI_Skills repo maintenance 不会误路由到它。

**因果风险**

后续实现可能在显式强制调用下 A–H 全部 PASS，但普通用户根本触发不到；或者因 trigger surface 过宽，把大量普通写作任务吸入 Project governance reasoning。这样 standalone 产品价值并未被真实证明。

**最小关闭条件**

当前仍不写 trigger eval，也不建立正式 Capability Gate Matrix。v2 只需把未来验收方向补成：

- 至少一种普通、未点名 Skill 的 Project-instruction 编辑请求必须能走正常入口；
- 邻近任务族作为 near-miss/should-not-change：普通中文润色、普通写作保真、科学文档结构重写、AI_Skills repo maintenance 继续由现有 owner 处理；
- 未来 Reviewer 要看到相关完整输入和完整输出，并做定性判断；不能只看 route receipt、字符数或 diff。

样本数由未来风险决定，不固定数量。

## 5. 非阻塞判断

### 字符预算

当前设计合理。继续保留“current length + known/user/product-exposed budget + delta + margin/headroom”的事实性输出；不要添加固定 reserve 百分比或统一预算器。

### locator substitution

v1 已明确：如果规则必须在任何 lookup 之前约束行为，尤其 ownership、authority、safety 与 cross-task response contract，就要直接常驻。这个方向不需要推翻。B2 只是补齐“global ownership 不等于 Project 内有效”的跨层边界。

### bounded edit / full rewrite

总体足够严格，没有发现需要再增加新的 rewrite 触发条件。B1 只是区分 preservation-sensitive 与 explicit reset / greenfield。

### 验收用例

A–H 不是机械重复：

- D 主要验证 exact identity 与 ordinary language 的分离；
- E 主要验证 setting effect 与 source drift 的因果归因。

两者可以同时保留。未来正式 Gate Matrix 不应机械沿用“必须八个 gate”；这些现在只是 task families / regression directions。

### 整体复杂度

当前核心仍然可以归结为一个短 reasoning sequence：

```text
取得真实基线/确认 reset 语义
-> 只找与当前变更有关的 history/source
-> 判断 authority + effective placement
-> 选择最小 mutation radius
-> 保护 invariants
-> 在真实 budget 下去重/locator 化
-> 给可审修改与完整候选（仅在安全时）
```

不需要新 schema、ledger、database、daemon、watcher 或 history state machine。

## 6. Maintenance state

当前 main 已确认：

- canonical source TODO 含 `tracking: #93`；
- Issue #93 为 open；
- labels 为 `maintenance-track`、`kind:new-capability`、`scope:standalone-skill`、`area:standalone-skill`；
- Issue reader-facing body 仍落后于 standalone Skill v1 设计轮次。

Planner 没有在无法验证 Clear Writing 调用的环境里实质改写 Issue body，符合 `AI_SKILLS_MAINTENANCE_BOARD.md` §6。当前 Critic surface 同样没有可验证的已安装 Clear Writing invocation，因此本轮不实质改写 Issue body：

```text
CLEAR_WRITING_UNAVAILABLE
```

当前环境也没有 GitHub Project field mutation surface，因此 Project 同步状态不能声称已验证。

Exact pending Project mutation：

```text
Project = AI Skills Maintenance
Issue = #93
Status = DOING
Area = standalone-skill
current design anchor =
docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_STANDALONE_SKILL_DESIGN_V1_PLANNER_PROPOSAL_2026-10-01.md
```

由于本轮为 REVISE，Issue 的“下一步”语义在下次可调用 Clear Writing 的 maintenance action 中应更新为：Planner 修订 B1–B4，并提交完整 v2 后返回 Critic。不要要求用户手工维护 Project 卡片。

## 7. 本次结论的边界

本轮 `REVISE` 不否定 standalone Skill 方向，也不要求回到 manual checklist 或扩展现有 writing Skill。

它证明的是：v1 还缺四个会影响真实产品行为的边界，必须先设计清楚。

它不授权：

- 创建 `skills/.../project-instructions-editor/`；
- 写 `SKILL.md`、`agents/openai.yaml`、trigger eval；
- 创建 Plugin；
- 修改 README / VERSION / registry / catalog / Marketplace / profile / release；
- 创建 implementation Goal / Kickoff；
- 启动 Codex implementation。

下一步只能回 Planner，提交完整 v2 设计修订并逐项回应 B1–B4。

```text
CRITIC_RESULT=REVISE
BLOCKERS=B1,B2,B3,B4
READY_FOR_FUTURE_SKILL_DESIGN=YES
READY_FOR_SKILL_IMPLEMENTATION=NO
NEXT_HANDOFF=PLANNER
```
