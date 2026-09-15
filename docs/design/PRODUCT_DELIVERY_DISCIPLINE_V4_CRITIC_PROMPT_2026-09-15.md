# Critic Prompt — Product Delivery Discipline v4

你是 AI Research Stack 的长期独立 Critic thread。

本轮只审方案，不实现代码，不修改任何 product repo，不创建 successor，不启动 Executor，不调用 paid API。

Repository:

`YuukiAS/AI_Skills_Collection`

审查对象：

`docs/design/PRODUCT_DELIVERY_DISCIPLINE_V4_PROPOSAL_2026-09-15.md`

本轮 Proposal 是对 v3 的实质修订，因为新增了 2026-09-15 Lucerna OpenAI Usage Monitor 的真实失败，以及用户明确要求：**凡 Goal 预见需要用户操作，必须在 Goal 里声明 prompt contract；执行到该 gate 时必须实际 prompt，不能静默等待，也不能仅因一个可恢复用户动作直接标为不可恢复 BLOCK；用户完成动作后，agent 必须继续同一 Goal 自己验证真实 post-action completion。**

## 1. 强制先读

先实际读取最新 main：

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/design/PRODUCT_DELIVERY_DISCIPLINE_V4_PROPOSAL_2026-09-15.md`
- `docs/plugin-todos/workflow-core.md`
- `docs/plugin-todos/web-development.md`
- `docs/plugin-todos/ai-skills-core.md`
- `docs/plugin-todos/scientific-visualization.md`
- `skills/core/codex-system/codex-workflow-protocol/SKILL.md`

再读取必要的真实 consumer evidence：

- `YuukiAS/Lucerna` 当前 `AGENTS.md`
- Lucerna Goal `01033_openai_usage_monitor_shared_vault` 相关 result/manifest 和以下 commits：
  - `bc887917572bf29adf57761e52fc1aa3cebbc1c0`
  - `843376e8e40b30287a72a5cd26f9d54fe001f0d0`
  - `7f0d1a15bc777ac1baffa40115955c770d489ba0`
- `YuukiAS/Mica-for-ChatGPT` 当前 `AGENTS.md`
- `YuukiAS/Bobbio` 当前 active development branch `AGENTS.md`
- `YuukiAS/Asteria` 当前 `AGENTS.md` 与 `prompts/AGENT_RULES.md`
- `YuukiAS/GPT_Codex_AI_Bridge_Kit` 当前 `templates/host/CODEX_CONFIG_PROFILE.md`、Lite/AGENT_RULES 相关模板

如果 private ChatGPT export bundle 在当前 Critic thread 不可访问，不得声称亲自读过 raw thread；但可以审 Planner 已公开记录的 evidence boundary，并独立核验 repo 侧事实。若缺 raw bundle 足以影响关键 PASS，请给出最小补证要求。

## 2. 必须独立核查的核心问题

### A. 新 Lucerna 事故到底证明什么

区分：

- user prompt 本身是否缺失；
- prompt 已发生但 post-action closure 缺失；
- live provider validation/permissions 错误；
- UI state 映射错误；
- test fixture 不忠实；
- 已有 Lucerna AGENTS 规则没有实际消费。

不得把“用户输入后仍 Not set up”简单包装成“再加一条要测试”。判断 Proposal 的 human-action lifecycle 与 post-action closure 是否抓住了真正根因。

### B. Goal-level prompt contract 是否过重或不够强

用户明确要求：如果 Goal 从一开始可预见需要用户操作，Goal 本身必须要求 prompt，而不是把动作埋在 result/普通消息里。

请审：

- `HUMAN_ACTION_REQUIRED / PROMPT_REQUIRED / PROMPT_TRIGGER / USER_ACTION / USER_REPLY / DO_NOT / RESUME_POINT / POST_ACTION_ACCEPTANCE` 这组语义是否应该全部强制，还是可更简化；
- 是否会让每个普通 task 都膨胀；
- 是否正确复用现有 state/wait/resume，而不是创造新状态机；
- 在 prompt tool 不存在时的 visible-message fallback 是否合理；
- “不能仅因一个可恢复用户动作直接不可恢复 BLOCK”如何与已有合法 `blocked` 语义兼容。

### C. Lite baseline 是否太长/太短

Proposal 给 Lite 6 条。请独立判断：

- 哪些必须常驻，不能依赖 workflow-core 触发；
- 哪些应只在 workflow-core/reference 中按需加载；
- 是否应该把 post-user-action closure 常驻 Lite；
- 是否会对纯 docs/server/read-only task 造成不必要流程。

优先保证“最轻入口也不会再静默等用户、提前完成、拿 proxy 冒充真实结果”，但不要把 Lite 变成大手册。

### D. workflow-core 是否拥有正确职责

检查 R1–R8：

- positive goal fidelity
- human-gated action lifecycle
- post-user-action closure
- exact failure + faithful regression
- evidence-surface fidelity
- producer self-QA
- repeat-failure circuit breaker
- protect accepted behavior

判断是否有重复、遗漏或放错层。尤其不要让 workflow-core 接管 Figma/视觉专业判断。

### E. Frontend Design 与 Scientific Visualization 边界

审 Proposal 是否正确：

- Frontend Design 管 canonical design/state coverage、component/interaction grammar、whole-screen actual-surface comparison、producer visual self-QA；
- Scientific Visualization 只管科学示意图中具有科学/统计语义的 encoding/routing/endpoint/label/math 等质量；
- Bobbio 圆、Lucerna Fluent icon、Asteria 当前 arrow style 不应成为中央默认风格。

### F. Repo-specific 是否克制

特别审：

- Lucerna 是否只需要短 product invariant + targeted integration/smoke，而不是再复制整个中央 workflow；
- Mica 是否应该固化“一次 live failure -> faithful fixture -> local repair -> candidate gate -> 最后一轮 human confirmation”；
- Bobbio 是否应去重现有 AGENTS，并把 canonical Figma 接到 normal frontend entry；
- Asteria 是否主要验证现有 visual rules 真消费，而不是继续堆条款。

### G. AI Skills Maintainer / Bridge Kit 边界

- Maintainer 是否正确负责“规则存在但失败时先核实 actual invocation/install/consumer”；
- Bridge Kit 是否只负责 Lite baseline 分发和现有 prompt/wait/resume 机制；
- 是否有任何证据需要真正改 Bridge Kit runtime，而不仅是模板/测试；
- 禁止为本问题新增 controller/watcher/ledger/state machine。

## 3. Capability Gate Matrix 审查

逐项审 G1–G8：

- 是否证明不同真实能力；
- 是否缺 normal entry；
- 是否能被只检查文档字符串、mock 或 synthetic PASS 钻空子；
- G1 prompt/resume 与 G2 post-human closure 是否应该独立；
- 是否有 should-not-change 反例证明纯 docs/server task 不被升级；
- 是否所有关键 gate 都要求 final production candidate；
- production consumption 是否真正证明 installed workflow 被调用，而不是 source 文件存在。

Gate 过重就删/合，过简就补；不要追求固定数量。

## 4. 外部研究要求

本轮 Critic 自己做针对性网络检索，至少独立核查：

- Codex / AGENTS persistent instruction 的官方建议；
- human-in-the-loop / tool interaction 的现实边界，若有官方 source；
- 不要只复述 Planner 引用。

说明采用/不采用什么，以及为什么。

## 5. 输出

对明确版本给：

`PASS` 或 `REVISE`

若 REVISE，每条 blocker 必须给：

- 稳定编号；
- 对应用户要求/合同；
- 证据；
- 因果风险；
- 最小关闭条件；
- owner。

非阻塞建议分开。

如果 REVISE，按 Critic contract 自动附完整 Planner follow-up prompt。

如果 PASS，也要明确：

- PASS 只批准 v4 proposal 的职责/机制设计；
- 不等于 production 修改已完成；
- 不代替用户授权；
- 下一步若准备执行，必须再审 Proposal/Plan + Canonical Goal + Kickoff Draft 的 execution-ready package。
