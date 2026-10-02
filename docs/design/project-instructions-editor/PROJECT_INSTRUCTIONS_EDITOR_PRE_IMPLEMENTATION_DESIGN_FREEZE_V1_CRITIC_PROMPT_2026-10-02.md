# Critic Prompt — Project Instructions Editor 实现前最终设计冻结 v1

你现在负责对 `project-instructions-editor` 候选 standalone Skill 的“实现前最终设计冻结”做独立 Critic 审查。

这不是 implementation review。
不要创建 Skill、Plugin、implementation Goal、Kickoff、trigger eval、README/VERSION/registry/catalog/Marketplace/profile/release 产物，也不要启动 Codex。

## Active Review Context

```text
target_repo:
YuukiAS/AI_Skills_Collection

target_plugin_or_domain:
candidate standalone Skill / project-instructions-editor

design_topic_or_task_key:
project-instructions-editor--standalone-skill-design

source_branch_or_ref:
main

review_stage:
pre-implementation final design freeze review

approved architecture:
docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_STANDALONE_SKILL_DESIGN_V2_PLANNER_PROPOSAL_2026-10-02.md

approved architecture package commit:
d9a6d782fe3374fe260a276ec06f2c1b206d421a

approved architecture Critic review:
docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_STANDALONE_SKILL_DESIGN_V2_CRITIC_REVIEW_2026-10-02.md

architecture Critic review commit:
b2da311519bf29713f0681245a7aab62fa81dadd

current review object:
docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_PRE_IMPLEMENTATION_DESIGN_FREEZE_V1_PLANNER_PROPOSAL_2026-10-02.md

freeze version:
v1

freeze proposal + canonical TODO package commit:
f1cace3d44870ff98d352698b8e9aa23621655df

tracking:
Issue #93

prior blockers:
B1 CLOSED
B2 CLOSED
B3 CLOSED
B4 CLOSED

DESIGN_FREEZE_CANDIDATE=YES
READY_FOR_SKILL_IMPLEMENTATION=NO
```

如果 `f1cace3d44870ff98d352698b8e9aa23621655df` 之后 main 只有无关并行提交，使用最新真实 HEAD，不要回退。

## 必须读取

同步最新 main，并实际读取：

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md`
- `docs/SKILL_AUTHORING.md`
- `TODO.md`
- `docs/skill-todos/project-instructions-editor.md`

主要审查对象：

- `docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_PRE_IMPLEMENTATION_DESIGN_FREEZE_V1_PLANNER_PROPOSAL_2026-10-02.md`

已批准架构与 review：

- `docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_STANDALONE_SKILL_DESIGN_V2_PLANNER_PROPOSAL_2026-10-02.md`
- `docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_STANDALONE_SKILL_DESIGN_V2_CRITIC_REVIEW_2026-10-02.md`

核对 Issue #93 当前真实状态。

除非发现一个具体未知项，不要重新做 v1/v4.1 全历史审计，也不要重新打开 B1–B4。

## 本轮审查问题

本轮不是再问“standalone Skill 是否成立”。v2 已经 PASS。

你要判断的是：当前 freeze candidate 是否已经把以后 implementation 不应再自行决定的产品合同冻结清楚。

### 1. 最终职责与非职责

检查 Skill 是否只拥有：

- 长期 ChatGPT Project instructions 的 semantic placement / editing；
- live/history/canonical source/budget 协调；
- bounded/full edit；
- effective enforcement；
- safe delivery。

检查它是否明确排除：

- generic prompt optimization；
- global Custom Instructions；
- ordinary prose；
- scientific document rewrite；
- AI_Skills repo maintenance；
- workflow execution/control；
- background history/state services。

如果 implementation 仍可能合理地问“这个能力到底是不是 Project editor 的职责”，说明 freeze 还不够。

### 2. normal entry / near-miss

检查普通用户不点名 Skill 时能否有清楚触发边界。

重点检查混合请求：

- Project setting semantic edit + 中文润色：Project editor 应主导，writing Skill 辅助；
- 只润色一两句已有 instruction，不改变 placement/budget/history/authority：不应强行启用完整 Project editor reasoning；
- generic agent/system prompt 与 global Custom Instructions 不应被误吸入。

不要现在写 trigger eval，也不要为了安全增加无限 near-miss 列表。

### 3. 三种 edit mode

检查：

- preservation-sensitive；
- greenfield；
- explicit reset；

是否已经能直接作为未来 implementation contract。

特别确认：

- preservation-sensitive 没有 baseline 时不能 false-safe full replacement；
- greenfield/reset 不被机械 baseline gate 阻止；
- 模糊“重写”不会被当成 reset。

### 4. 输入与降级

检查：

- live setting；
- targeted Project history；
- canonical project sources；
- current edit request；
- character budget；

缺失时的降级是否局部、诚实、不会为了“完整”制造假事实或不必要用户往返。

不要要求 exhaustive Project history。

### 5. semantic ownership vs effective enforcement

检查 freeze 是否真正固定：

- semantic owner 在哪里；
- 当前 Project 为了实际生效需要 resident rule、bridge/trigger 还是 source-only；

并防止：

- 因 global/repo ownership 就错误删除 Project-local hard control；
- locator 在 lookup 发生前无法约束行为。

### 6. protected absence

检查：

- old-only absent rule 在 partial history 下默认不恢复；
- explicit re-adopt / explicit canonical sync exception 边界够窄；
- 不产生 tombstone registry/history database；
- bounded edit 无关区域保持不动。

### 7. bounded edit / full rewrite

检查：

- bounded edit 真的是默认；
- full rewrite 的理由是 cross-cutting contradiction、pervasive copied detail、multi-scope imbalance、budget impossibility、systemic source drift 或 explicit user request/reset；
- recent thread /“更整齐”不是 full rewrite 理由。

### 8. 最终用户交付合同

检查交付是否比例化：

- small bounded edit；
- medium edit；
- full replacement；
- missing-input advice；
- no-op。

不能让每次小修改都生成大型审计包；也不能只给完整新稿让用户自己找差异。

### 9. 实现后必须证明的用户能力

检查 freeze 是否已经覆盖：

1. normal entry / routing boundary；
2. core Project editing semantics；
3. fidelity / authority / should-not-change；
4. representative complete task；
5. qualitative full user artifact。

这些是 capability claims，不是现在的测试脚本。

### 10. Capability Gate family

freeze candidate 把 A–L regression/task-family bank 收敛为四个 Gate family：

1. Normal entry / routing boundary；
2. Core Project editing semantics；
3. Fidelity / authority / should-not-change；
4. Representative complete task + qualitative final artifact。

请独立判断：

- 四个 Gate family 是否过多或过少；
- 是否两个 Gate 其实证明同一 capability；
- 是否漏掉 production normal entry、final-candidate identity、完整 artifact 或 qualitative review；
- Gate 4 是否足够承担 complete/long/multi-scope + final candidate + fresh generalization；
- A–L 是否仍只是 regression bank，而不是暗中变成 12 个 Gate；
- 是否需要正式实现阶段再根据 blast radius split，而不是现在继续增加 Gate。

不要为了“更稳”机械要求第五、第六 Gate；只有 capability/evidence/failure semantics 真正不同才增加。

## 外部事实核查

按 Critic Role Contract 做最小针对性官方核查。

本轮 Planner 已重新核对 OpenAI 当前官方 Projects / Memory 文档，未发现需要修改 v2 的新事实。

你至少确认：

- Project instructions 仍只在对应 Project 内生效并覆盖 global custom instructions；
- Project memory/context 可用性仍不能被解释成“Skill 可以穷尽枚举全部 Project history”；
- 当前官方 Projects 文档是否出现可验证统一 Project-instruction 字符上限。

如果没有，只能写“当前未核实到统一上限”，不能写“证明不存在上限”。

## 不要重新打开已经批准的设计

除非 freeze candidate 引入真实回归或你发现新直接证据，否则继续保持：

- standalone Skill 独立成立；
- bounded edit 默认；
- B1–B4 CLOSED；
- 约 8,000 不是统一产品常数；
- 无固定 reserve 百分比；
- locator 不移走 lookup-before-action 语义；
- protected absence 不持久化；
- no-op 合法；
- qualitative full-output review 必需；
- 不建 database / ledger / daemon / watcher / state machine。

## Maintenance state

canonical TODO 应继续含：

```text
tracking: #93
```

Issue #93 应继续：

```text
state=open
maintenance-track
kind:new-capability
scope:standalone-skill
area:standalone-skill
```

目标 Project lifecycle：

```text
Project = AI Skills Maintenance
Issue = #93
Status = DOING
Area = standalone-skill
current design anchor =
docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_PRE_IMPLEMENTATION_DESIGN_FREEZE_V1_PLANNER_PROPOSAL_2026-10-02.md
```

如果当前 surface 没有 GitHub Project field mutation，输出 exact pending mutation，不声称已同步，也不要让用户手工拖卡片。

Issue reader-facing copy 只有在真实调用当前安装的 Clear Writing 后才能实质修改。

若没有可验证 invocation surface：

```text
CLEAR_WRITING_UNAVAILABLE
```

不要绕过 policy 改 Issue。

## PASS / REVISE

如果 freeze contract 足够让未来 implementation 不再自行做产品架构选择：

```text
CRITIC_RESULT=PASS
DESIGN_FREEZE=PASS
READY_FOR_SKILL_IMPLEMENTATION=NO
```

这里的 PASS 只表示：

- 产品/架构设计已冻结；
- 等待用户未来明确授权 implementation planning / implementation。

它不授权：

- 创建 Skill；
- Goal/Kickoff；
- trigger eval；
- Plugin；
- release/package；
- 安装；
- Codex execution。

如果 REVISE：

每个 blocker 必须包含：

- stable ID；
- 对应冻结要求；
- 直接证据；
- 因果风险；
- 最小关闭条件。

不要用“还可以更详细”或实现期自然会决定的问题阻塞设计冻结。

## 下一 handoff

无论 PASS/REVISE，都按 Critic Role Contract 自动生成下一角色 prompt。

PASS 后 NEXT_HANDOFF 仍应为 PLANNER。
Planner 只负责记录 freeze closure 并等待用户未来是否明确开启 implementation；不得因为 PASS 自动创建 Goal/Kickoff。
