# Critic Prompt — Project Instructions Editor Standalone Skill Design v2

你现在负责对 `project-instructions-editor` 候选 standalone Skill 的 v2 产品/架构设计做独立 Critic 复核。

这不是 implementation review。
不要创建 Skill、Plugin、implementation Goal、Kickoff、trigger eval、README/VERSION/registry/catalog/Marketplace/profile/release 产物。

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
standalone Skill product/design v2 review after prior REVISE

reviewed proposal:
docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_STANDALONE_SKILL_DESIGN_V2_PLANNER_PROPOSAL_2026-10-02.md

proposal version:
v2

v2 package commit:
d9a6d782fe3374fe260a276ec06f2c1b206d421a

prior proposal:
docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_STANDALONE_SKILL_DESIGN_V1_PLANNER_PROPOSAL_2026-10-01.md

prior Critic review:
docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_STANDALONE_SKILL_DESIGN_V1_CRITIC_REVIEW_2026-10-02.md

prior Critic review commit:
e6ee48e9c84d5e79803b497e6a5774dc31271465

stable blockers to recheck first:
B1
B2
B3
B4

tracking:
Issue #93

READY_FOR_SKILL_IMPLEMENTATION=NO
```

如果 `d9a6d782fe3374fe260a276ec06f2c1b206d421a` 之后 `main` 只有无关并行提交，使用最新真实 HEAD，不要回退。

## 必须先读取

实际读取最新 main：

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md`
- `docs/SKILL_AUTHORING.md`
- `TODO.md`
- `docs/skill-todos/project-instructions-editor.md`

主要审查对象：

- `docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_STANDALONE_SKILL_DESIGN_V2_PLANNER_PROPOSAL_2026-10-02.md`

上一轮 review：

- `docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_STANDALONE_SKILL_DESIGN_V1_CRITIC_REVIEW_2026-10-02.md`

只在需要判断本轮改动是否破坏既有设计时复核：

- `docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_STANDALONE_SKILL_DESIGN_V1_PLANNER_PROPOSAL_2026-10-01.md`
- `docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_REAL_PROJECT_REGRESSION_LESSONS_2026-10-01.md`
- `docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_READABILITY_DESIGN_HISTORY_2026-10-01.md`
- `docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_V4_1_PLANNER_PROPOSAL_2026-10-01.md`
- `docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_V4_1_CRITIC_REVIEW_2026-10-01.md`

职责边界按需复核：

- `skills/writing/core/chinese-prose/SKILL.md`
- `skills/writing/core/writing-fidelity/SKILL.md`
- `skills/writing/core/scientific-rewrite/SKILL.md`
- `skills/core/codex-system/codex-workflow-protocol/SKILL.md`
- `skills/core/codex-system/ai-skills-repository-maintainer/SKILL.md`

以及 Issue #93 当前真实状态。

不要做无边界 full-repo audit。

## 本轮优先复核 B1–B4

按 Critic Role Contract，先复核旧 blocker。只有新事实、先前遗漏的关键风险或 v2 引入的新回归才新增 blocker；不要移动终点。

### B1 — replacement mode

v2 已接受 B1，并区分：

1. preservation-sensitive replacement：
   - 已有 setting；
   - 用户没有授权丢弃未涉及语义；
   - 声称保留现有语义；
   - 必须取得足够精确、语义完整的 live baseline。

2. greenfield / explicit-reset replacement：
   - Project 已确认 setting 为空；或
   - 用户当前明确要求废弃旧 setting、从零重建且不要求旧语义保真；
   - 可以生成完整 setting；
   - 不得声称保留未知旧规则。

请检查：

- 是否真正关闭 v1 过严门禁；
- 是否仍可能把含糊“重写”误判成 reset；
- explicit reset 是否只解除 Project-setting preservation obligation，而没有越权覆盖更高层安全/权限/当前用户要求；
- future case I 是否足以证明这一边界。

### B2 — semantic ownership vs effective enforcement placement

v2 已接受 B2，并要求每条受影响 durable rule 分开判断：

- canonical / semantic ownership；
- effective enforcement placement。

Project 内可能需要：

- direct resident semantic rule；
- short bridge/trigger + canonical source；
- source-only；
- task-only；
- no placement。

请检查：

- global/user ownership 是否仍可能被错误理解成“可以从 Project 删除”；
- ownership、authority、permission、safety、evidence、user-reading contract 等 lookup-before-action semantics 是否得到保护；
- locator substitution 是否保留必要 Project-local trigger；
- future case J 是否真正验证 Project/global precedence，而不是只验证文字存在。

### B3 — protected absence under partial history

v2 已接受 B3。

当 relevant history partial/unavailable 时，durable rule 如果：

- 不在 live baseline；
- 只出现在旧 Candidate / Reference / summary；

则当前 edit 默认保持 absent。

只有：

- current user explicit add/re-adopt；
- current task explicit canonical-source synchronization，且 source authority 支持；

才允许引入。

请检查：

- 是否足以防止历史删除规则通过旧 Candidate 复活；
- 是否仍然保持 targeted history，而没有隐式变成 tombstone registry / exhaustive history audit；
- canonical-sync exception 是否过宽；
- bounded edit 是否没有因此扩大到无关 scope；
- future case K 是否能直接揭示失败。

### B4 — normal entry / near-miss

v2 已接受 B4。

未来验收方向 L 需要证明：

- 普通用户自然请求 Project-instruction 编辑时，不点名 Skill，也能进入正确能力；
- ordinary Chinese polish -> `chinese-prose`；
- ordinary writing fidelity -> `writing-fidelity`；
- scientific/technical structural rewrite -> `scientific-rewrite`；
- AI_Skills repo maintenance -> `ai-skills-core`；
- complex task process/control -> `workflow-core`。

请检查：

- 这是否足以证明 standalone trigger surface 值得存在；
- near-miss 是否覆盖真正高风险邻近 owner；
- 是否需要新增别的任务族，还是当前范围已经足够；
- 是否仍有 route receipt / chars / diff / keywords 冒充 normal-entry quality 的漏洞。

当前不要创建 trigger eval，不要规定固定 sample count，不要建立正式 Capability Gate Matrix。

## 独立外部核查

按 Critic Role Contract 做针对性官方核查，优先 OpenAI 官方资料。

至少重新确认：

- Project instructions 在当前 Project 内的作用与 global custom instructions 的关系；
- 当前 Projects 文档是否给出可验证的统一 Project-instruction 字符上限；
- global Custom Instructions 的限制不能被当成 Project instructions 限制；
- Project history/memory availability 是否支持“targeted history + honest degradation”，而不是假定可穷尽枚举。

若官方没有给出统一 Project instruction limit，只能写“未找到可验证统一限制”，不能写“证明不存在限制”。

## 检查 v1 已通过方向有没有回归

除 B1–B4 外，v1 以下方向应保持，除非你发现新的直接证据：

- standalone Skill 有独立产品价值；
- bounded edit 默认；
- full rewrite 只有真实跨范围原因；
- recent thread 不因 recency 获取更多 budget；
- exact identifier 与 ordinary language 分层；
- locator 不能移走 lookup 前必须生效的关键治理语义；
- 约 8,000 不是统一产品常数；
- budget 按实际限制、semantic density、Project-specific headroom；
- 不设固定 reserve 百分比；
- qualitative full-output review；
- no-op 合法；
- 不建 database / ledger / daemon / watcher / history state machine；
- `chinese-prose` / `writing-fidelity` 是辅助和 guardrail；
- `scientific-rewrite` 不承担 Project-setting architecture；
- `workflow-core` 只管复杂任务过程；
- `ai-skills-core` 只管以后 AI_Skills repo 实现/发布维护。

A–L 当前只是 future regression/task-family directions，不是固定 Gate 数。

## 维护状态

canonical TODO 应继续含：

```text
tracking: #93
```

Issue #93 应继续：

```text
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
docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_STANDALONE_SKILL_DESIGN_V2_PLANNER_PROPOSAL_2026-10-02.md
```

若当前 surface 没有 GitHub Project field mutation，输出 exact pending mutation，不能声称已同步，也不要让用户手工拖卡片。

Issue #93 reader-facing body 仍落后于当前设计。根据 `AI_SKILLS_MAINTENANCE_BOARD.md`，实质修改 Issue copy 前必须真实调用当前安装的 Clear Writing（`writing-style`）。

如果当前环境没有可验证 invocation surface：

```text
CLEAR_WRITING_UNAVAILABLE
```

不要绕过 policy 改 Issue。

## 输出要求

对明确的 v2 Proposal 给：

```text
CRITIC_RESULT=PASS
```

或：

```text
CRITIC_RESULT=REVISE
```

如果 REVISE：

- stable blocker ID；
- 对应要求；
- 直接证据；
- 因果风险；
- 最小关闭条件；
- 优先说明是 B1–B4 未关闭，还是 v2 引入了新的真实风险。

如果 PASS：

- 明确逐项关闭 B1–B4；
- 说明 v2 的 PASS 只批准当前 standalone Skill 产品/架构设计继续向下一 Planner 阶段推进；
- 不授权 Skill implementation；
- 不创建 implementation Goal / Kickoff；
- 下一 handoff 仍回 Planner，由 Planner 决定是否已经足够成熟进入“实现前冻结设计”阶段，并另经用户授权。

始终保持：

```text
READY_FOR_FUTURE_SKILL_DESIGN=YES/NO
READY_FOR_SKILL_IMPLEMENTATION=NO
```

按 Critic Role Contract 自动生成下一角色 prompt。
