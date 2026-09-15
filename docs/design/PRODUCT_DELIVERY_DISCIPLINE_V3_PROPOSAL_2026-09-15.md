# Product Delivery Discipline v3 — Planner Proposal

状态：`DRAFT_FOR_CRITIC_REVIEW`  
日期：2026-09-15  
Planner source commit：`affdf5957a88ce4c1f96752a968cc58e461c5d97`  
替代关系：这是 `PRODUCT_DELIVERY_DISCIPLINE_V2_2026-09-14.md` 的证据升级提案；在 Critic PASS 和后续正式实现前，不替代任何 active AGENTS、skill、Bridge Kit template 或 repo policy。

## 1. Active Design Context

```text
target_repo = YuukiAS/AI_Skills_Collection
target_plugin_or_domain = workflow-core + web-development + ai-skills-core; with Bridge Kit Lite and repo-specific consumers
design_topic = cross-project product-delivery discipline after official ChatGPT export audit
source_branch_or_ref = main@affdf5957a88ce4c1f96752a968cc58e461c5d97
proposal_path_and_version = docs/design/PRODUCT_DELIVERY_DISCIPLINE_V3_PROPOSAL_2026-09-15.md / v3 draft
execution_branch/worktree = NOT_CREATED
```

本轮只做证据复核、职责划分和提案，不修改 production skill、Bridge Kit template 或各产品 AGENTS，不创建 successor，不运行付费 API。

## 2. 新证据：官方 ChatGPT Data Export 能说明什么、不能说明什么

用户使用 OpenAI 官方 Data Export，在本机对 2026-09-13 至 2026-09-15 的开发对话进行了离线扫描。私有原始 bundle 不提交到公开仓库。本轮 Planner 实际检查了 bundle 的 coverage、thread inventory、incident ledger、deep dive、raw rules 和重点 curated threads。

机器取证覆盖：27 个 `conversations-*.json` shard 全部解析，约 2,626 个 conversation record；识别 23 个时间窗内候选，7 个 primary thread deep-read、10 个 secondary cross-check、5 个 ambiguous；解析失败为 0。bundle 自动抽取了 173 个所谓 incident 和 15 条 raw rule。

但 **173 和 raw rule 的 incident 计数不能直接当统计证据**。人工复核发现明显误分类：例如 SeminarArc thread 被关键词归为 Server+VPS；若干正常 PASS/status 输出被标成 `design source ignored` 或 `missing targeted regression`；Bobbio 最重要的 Figma 失败 thread 被留在 ambiguous/secondary。原因是自动抽取适合做高召回索引，不适合直接判定用户不满的语义类别。

因此本提案采用两层证据：

1. 全 shard inventory 证明“搜索范围没有只挑几个聊天”；
2. curated thread 中可恢复完整前后文的高信号案例，作为规则设计依据。

目前足以支持跨项目机制判断的高信号来源主要是：

- **Mica**：synthetic/E2E 大量 PASS 后真实 ChatGPT 仍复发；用户被反复要求 Atlas/真人验收；诊断能力逐渐变成目标本身；真实 action-bar / stale-composer 结构没有被 faithful fixture 捕获。
- **Bobbio**：功能/性能/本地 QA 绿灯后，整屏仍有无语义装饰、相邻控件两套语法、重复 CTA；已有 canonical Figma 却在 production code 里补设计缺口，用户被迫逐屏做 art direction。
- **Lucerna**：关闭按钮、Refresh、视觉样式反复返修；仓库事实上已经存在“真实 Windows release interaction + matching regression + truthful live values”的规则，说明这里至少部分是 **existing-rule execution regression**，不是继续加同义规则即可解决。
- **Asteria**：箭头终点、card/edge 碰撞、跨层 routing、公式渲染、标签/连接器层级等明显视觉问题到 GPT Work/人工阶段仍未被挡住；后续 repo 已增加 developer visual self-QA 和 canonical scientific graph visual system，说明需要验证这些新增规则是否真实消费，而不是继续堆新的视觉禁令。

## 3. 对 15 条 raw rules 的 Planner 审核

raw rules 不应原样推广。建议合并为 8 个机制候选：

| Audited candidate | 吸收的 raw rule | 判断 |
|---|---|---|
| A1 User-interaction ownership | USER_USED_AS_DEBUGGER / MISSING_USER_PROMPT / REPEATED_AUTHORIZATION | 通用。能自己观察/测试的先自己做；只有用户能完成的动作才显式最小询问；同范围授权不重复问。底层 prompt 能力由 Bridge Kit/host 提供。 |
| A2 Exact failure + faithful regression | MISSING_TARGETED_REGRESSION / UNFAITHFUL_TEST_FIXTURE | 通用。修复必须绑定原失败；能自动化时让旧实现失败、新实现通过；真实服务无法自动化时保留一次真实 failure capture 并构造 faithful replay。 |
| A3 Evidence-surface fidelity | PROXY_EVIDENCE_TREATED_AS_REAL / TOOL_LIMITATION_MISHANDLED / WEAK_IMPLEMENTATION | 通用。证据 claim 不得超出被观察 surface；browser fixture 不能冒充 native/live，代码存在不能冒充交互结果。 |
| A4 Repeat-failure circuit breaker | EXCESSIVE_PROCESS_TOKEN_WASTE + Mica repeated-live loops | 通用。相同症状重复、同测试无新信息、或用户再次拒绝同类结果后，停止盲目重跑/真人验收，先重查 hypothesis、candidate identity、fixture fidelity、规则是否实际加载。 |
| A5 Protect accepted behavior | REGRESSION_OF_ACCEPTED_BEHAVIOR | 通用。修改共享 surface 时列出受影响的已接受行为并做相邻回归；用户主动改变要求除外。 |
| A6 Design source + whole-product loop | DESIGN_SOURCE_IGNORED | 通用到 UI/visual domain，但不应塞入所有任务的详细 Lite 规则。若存在 canonical design，缺 state 先回 design；实现后做 full-screen actual-surface comparison。 |
| A7 Producer self-QA before external/human review | Bobbio/Asteria evidence，raw rules 未单列 | 通用到视觉/交互 artifact。外部 Reviewer 和用户用于独立确认，不应承担第一轮明显缺陷发现。 |
| A8 Goal/status fidelity | REQUIREMENT_MISUNDERSTANDING / PREMATURE_COMPLETION / WORKFLOW_STATUS_MISUSE | 通用。原始正向目标、当前 owner、剩余 gate 和实际状态一致；不能因过程通过就提前完成，也不能把可恢复等待写成不可恢复失败。 |

以下 raw rule **不单独保留**：

- `REQUIREMENT_MISUNDERSTANDING` 太宽，容易把普通产品讨论都变成流程违规；归并 A8，并依赖具体 source/acceptance。
- `MISSING_USER_PROMPT`、`REPEATED_AUTHORIZATION` 不是新顶级规则；已有授权/交互机制应先验证是否真实生效。
- `WEAK_IMPLEMENTATION` 只是 A2/A3/A6 的结果，不值得新增抽象层。
- 自动 bundle 的 raw incident 频次不用于决定 promotion 优先级。

## 4. 推荐职责划分

### 4.1 Lite Handoff / AGENTS：只保留短底线

Lite 不能依赖某个 plugin 恰好被触发，所以需要一个短、稳定、跨项目 baseline；但不能复制完整 workflow。官方 Codex harness 经验也强调 AGENTS 应作为简短导航而不是巨大手册。

建议 Lite baseline 最终只覆盖：

1. 保持原始正向目标、task-declared source of truth 和已接受不变量；禁止静默降级。
2. 先使用 agent 已有观察/测试能力；只有用户能完成的步骤才明确发最小 prompt；同范围授权不重复询问。
3. 新增功能、行为变化和 bug fix 必须有与风险匹配的 regression/validation；已有充分覆盖可复用，不为数量新增测试。
4. completion claim 必须绑定正确 candidate 和正确 surface；proxy/synthetic 只能证明自身范围。
5. 同类失败重复且没有新信息时停止 blind rerun / repeated human QA，先重新诊断。
6. 最终回复区分完成、部分完成、等待用户/外部、未验证，并说明恢复点。

Lite 中不写 Figma 具体状态表、按钮 anatomy、Mica Atlas、Lucerna close、Asteria arrow 等领域内容。

### 4.2 Verified Workflow / workflow-core：本轮主要 owner

workflow-core 应把上面的短底线转成可执行流程，而不是新增 state/schema：

- 启动时明确 positive completion target、实际 surface/candidate、protected behaviors、用户唯一能做的动作。
- bug fix / behavior change 先建立 exact failure evidence；能自动化时要求 narrow regression，不能自动化时定义可信替代证据。
- 将 proxy evidence 与 production/native/live evidence 分级，claim scope 不能超出 evidence scope。
- human QA 前要求 producer-local evidence 已绿；人类失败后，下一次请求前必须有新 hypothesis/repair/replay evidence。
- repeated-failure circuit breaker：相同症状或同一无信息检查再次失败时，不继续 full-suite/Atlas/GPT Work/真人循环；先检查 candidate identity、fixture fidelity、实际 plugin/rule loading 和失败归因。
- 任何修复都保护 adjacent accepted behavior；真正互斥的新产品决定才交用户。
- 设计/视觉任务路由给 Frontend Design；科学图示语义路由给 Scientific Visualization；workflow-core 不自己决定按钮样式或箭头造型。
- final report 解释“用户现在能做什么”，而不是只报 tests/logs。

当前 `docs/plugin-todos/workflow-core.md` 已有高度重合的 NEW candidate；正式实现应 **修订/合并该条，而不是再建一条平行 TODO**。

### 4.3 Frontend Design / web-development：已有 TODO 足够，重点是收敛与真正执行

当前 TODO 已经覆盖 icon system、native-vs-browser evidence、motion/performance、component craftsmanship、producer self-review、whole-screen visual freeze、canonical design source、Figma completion、design-to-code closed loop 和 whole-product taste。官方 export 的 Bobbio/Lucerna/Asteria/Mica 证据主要是 **强化这些候选，而不是要求再增加一批同义规则**。

下一轮正式 refinement 应优先合并为少量 production gates：

- canonical design/state coverage；
- implementation-to-actual-surface full-screen comparison；
- component/interaction consistency；
- obvious-defect producer self-QA；
- external confirmation only after local visual gate。

不要把某个 Bobbio 圆、某套 Fluent icon、某种箭头造型推广为全局风格。

### 4.4 Scientific Visualization：只记录 Asteria 新事实，暂不设计生产改动

Asteria 暴露的是 interactive scientific schematic 的真实 QA 缺口：connector routing、arrow endpoint、label/card overlap、数学渲染和视觉层级具有科学表达含义，不能只靠 DOM/bbox/机械测试证明质量。

建议先作为 `status: NEW` 真实反馈进入 `scientific-visualization` TODO；未来 Planner 再判断它应由 Scientific Visualization、Frontend Design，还是两者的边界负责。不要把 Asteria 当前 open-chevron/具体 spacing 数值写成通用科学图规范。

### 4.5 AI Skills Maintainer：验证“规则有没有真的被消费”

当前 `ai-skills-core` TODO 已有正确候选：已有规则仍失败时，先核实实际安装版本、plugin invocation、生成层/消费层、task entry 和 rule loading，再判断是缺规则还是 execution regression。

官方 export 更支持这条：Lucerna、Mica、Asteria 在失败前后都出现过已经写下来的相似规则。正式 refinement 不应继续靠文档数量制造“治理完成”。

### 4.6 Bridge Kit：分发 baseline + 提供真实 prompt 能力，不新增控制体系

Bridge Kit 当前 host profile 已管理 `default_mode_request_user_input = true`。因此“需要用户时不询问”不能先假定是底层没有 prompt 能力；要区分 task 没调用、运行 surface 不支持、或规则没有要求。

Bridge Kit 后续若经 Critic PASS 修改，范围应限于：

- Lite template/AGENT_RULES 分发短 baseline；
- 现有合法 wait/resume/user-input 语义的文档/测试；
- 不新增 state、ledger、watcher、controller 或审批体系。

## 5. Repo-specific 处理建议

### Bobbio

当前 `develop` 的 AGENTS 已经有大量“先自行 native UI inspection、只有真需要才 prompt 用户”的规则，不应再复制同义段落。真正缺口是 frontend read-list / normal path 应明确包含当前 canonical Figma handoff 和 production UI source-of-truth，并把“design missing state -> update design first -> implement -> native compare”接到当前 milestone。

正式修改时应顺带 **去重** section 8 中重复的 user-prompt/UI-self-inspection文字，而不是让 AGENTS 越来越长。

### Lucerna

当前 AGENTS 已明确要求：真实 Windows release interaction、close/hide-to-tray、matching regression、truthful provider values、bounded screenshot helper。9 月 14 日 close incident 属于这些规则没有在候选交付前挡住问题。**默认不新增 repo policy。** 后续应检查实际 regression 是否能对旧坏行为 FAIL，以及生产候选是否真的执行该 test/real release smoke。

### Mica

已有 focused-test budget、Tier 1/2/3、real-site diagnostic UX 和“不要反复用 authenticated ChatGPT 做自动回归”的规则，但缺少一个足够硬的 real-site bug closure contract。

候选 repo-specific 补充：对依赖真实 ChatGPT DOM/lifecycle 的复发 bug，采用 `一次真实 failure capture -> sanitized faithful fixture/contract -> old code fails -> local repair + focused replay -> candidate full gate once -> one final human confirmation`；若相同 live symptom 再失败，不得直接要求下一次真人 retry，先证明 fixture/candidate/hypothesis 发生了实质变化。诊断 Atlas 是取证手段，不是产品 milestone。

### Asteria

当前 `prompts/AGENT_RULES.md` 已经新增 Developer visual self-QA、canonical scientific graph visual system、generic-fix-not-fixture-hardcode；root AGENTS 也要求每个 code fix 对应 regression。9 月 14 日事件因此主要作为这些 **新规则需要 normal-entry replay** 的证据，不建议继续添加同义 AGENTS。

后续验证重点：真实 UI 截图是否确实被 agent 读取并用于整屏判断；GPT Work 是否在明显 connector/card/KaTeX 缺陷仍存在时被阻止；generic layout mechanism 是否替代 fixture-specific magic numbers。

## 6. Alternatives

### 方案 A：把 20+ 条规则全部塞进 Lite/AGENTS

拒绝。优点是永远可见；缺点是 context 膨胀、项目无关规则干扰、重复和腐化。OpenAI 的 harness 实践明确报告 one-big-AGENTS 方案会挤占上下文，并采用短 AGENTS + deeper docs。

### 方案 B：全部交给 workflow-core

拒绝。优点是集中；缺点是 plugin 未触发或安装过旧时底线失效，也会让 workflow-core 越权负责视觉专业判断。

### 方案 C：短 baseline + workflow mechanism + domain quality + repo-specific invariants

推荐。它能保证基本执行纪律始终存在，又把复杂规则只在相关任务加载；也与 Skill 用作可重复工作流、repo AGENTS 用作 persistent scoped context 的官方定位一致。

## 7. Capability Gate Matrix（供 Critic 审，不代表已批准执行）

### Gate W1 — Lite baseline normal entry
- Capability/claim：普通 Lite 项目在没有显式调用 domain plugin 时仍遵守最小 completion/user-input/regression/evidence discipline。
- Why distinct：证明 baseline 分发，不证明 workflow-core 深度机制。
- Normal entry：安装/更新 Lite 到一个测试 repo 后启动普通 bounded feature/bug task。
- Evidence：实际生成的 AGENT_RULES/AGENTS 消费到 baseline；缺用户动作会主动 prompt；同范围授权不重复询问。
- Failure：只存在 source template、实际 project 未加载；或静默等待/重复索权。
- Regression boundary：纯 docs/只读任务不能被迫新增 runtime tests/人工 QA。
- Final candidate：YES。

### Gate W2 — Exact failure and faithful replay
- Capability/claim：workflow-core 能把真实 complaint 转成与失败相符的 regression，而非 broad suite PASS。
- Normal entry：Mica-like live failure 与普通 deterministic bug 各一例。
- Evidence：deterministic case old-fail/new-pass；live case 有一次 failure capture + faithful local replay，proxy scope 明确。
- Failure：fixture 在旧坏实现也 PASS，或只有 broad test logs。
- Regression boundary：不能为了制造 old-fail 危险回退真实数据/生产环境。
- Final candidate：YES。

### Gate W3 — Repeat-failure circuit breaker
- Capability/claim：同类失败重复时停止无信息重跑/真人循环并重新诊断。
- Evidence：回放两次相同失败后，next action 转为 candidate/fixture/rule-loading/root-cause inspection；不会自动再次 full E2E/GPT Work/human test。
- Failure：同一无新信息操作继续重复。
- Regression boundary：一次普通 transient failure 仍允许 bounded retry。
- Final candidate：YES。

### Gate W4 — Evidence surface and completion fidelity
- Capability/claim：native/live/visual claim 只由对应 surface final candidate 支持。
- Evidence：browser/synthetic PASS 被正确标成局部证据；真实 surface 未验证时不写整体完成。
- Failure：proxy PASS 提升为 product PASS。
- Regression boundary：用户只要求 unit/helper/docs 结果时不擅自增加 live gate。
- Final candidate：YES。

### Gate F1 — Canonical design consumption
- Capability/claim：Frontend Design 在存在 canonical Figma/design source 时先补齐要发布的 primary states，再实施。
- Evidence：设计 state 缺失触发 design update；production implementation 引用 frozen target；不在 CSS 中临时发明主要状态。
- Failure：设计只作为灵感，代码直接 invent hierarchy/components。
- Regression boundary：无 canonical design 的小型 UI task 不被强制创建 Figma。
- Final candidate：YES。

### Gate F2 — Whole-screen actual-surface QA
- Capability/claim：producer 自己发现明显 composition/component/interaction defects，再交 external/user。
- Evidence：同一 final candidate 的 actual native/browser full-screen states 被直接观察；明显 P2 阶段内修掉；external review 不再承担第一轮 basic defect discovery。
- Failure：只看 DOM/CSS/test/bbox 或 component crop。
- Regression boundary：非视觉任务不触发 visual gate。
- Final candidate：YES。

### Gate M1 — Rule consumption diagnosis
- Capability/claim：AI Skills Maintainer 能区分 missing rule、not invoked、stale install、consumer not wired、execution noncompliance、rule conflict。
- Evidence：至少一例“已有规则仍失败”真实 replay，最终归因基于 installed runtime/task entry，而非 source SKILL 存在。
- Failure：再加同义 TODO 就称已解决。
- Regression boundary：真实 project bug 不被误搬到中央 plugin。
- Final candidate：YES。

## 8. 失败恢复与停止条件

- 如果 Critic 认为职责划分过重或规则仍重叠，先收敛 Proposal，不创建 implementation task。
- 如果 Bridge Kit 与 workflow-core 对 user-input/status owner 冲突，先核对真实 runtime contract，不静默复制两份机制。
- 如果 repo-specific AGENTS 已完整覆盖 incident，默认判 execution regression；不因用户再次生气就新增同义文字。
- 不使用本轮官方 export 私有原话做 public fixture；后续回归使用 synthetic/minimal task 或公开 repo-safe evidence。
- 本轮无 paid API、无 production install、无用户账户/设备操作。

## 9. 通过后用户新增的真实能力

若后续实现并通过 gates，用户得到的不是“又多了一套规则”，而是：

- agent 真需要用户时会及时问，不需要用户时先自己观察和测试；
- 同一个真实 bug 不再靠一轮轮真人试错推进；
- broad tests/fixture PASS 不能掩盖真实 native/live failure；
- UI 有设计源时不会由 implementation 临场乱设计；
- obvious visual defects 在交 GPT Work/用户前先由 producer 自己发现；
- 已经写进 repo/plugin 的规则如果仍失效，会追查真实消费路径，而不是继续堆文档。

## 10. 外部参考（本轮实际核查）

- OpenAI, *Harness engineering: leveraging Codex in an agent-first world*: https://openai.com/index/harness-engineering/ — 明确反对巨大单体 AGENTS；建议短 AGENTS 作为导航、结构化 docs 作为 system of record；把用户反馈转成 acceptance criteria，并把缺失工具/guardrail/docs 反馈回 repo。
- OpenAI, *Unrolling the Codex agent loop*: https://openai.com/index/unrolling-the-codex-agent-loop/ — Codex 会按 scope 聚合 AGENTS 指令，且项目文档受上下文上限约束，支持“短 baseline + 更深专项规则”的分层。
- OpenAI Academy, *Using skills*: https://openai.com/academy/skills/ — Skill 的定位是可复用的重复工作流，适合承载详细流程而不是每个 repo 重复粘贴。
- OpenAI, *Running Codex safely at OpenAI*: https://openai.com/index/running-codex-safely/ — 强调明确边界、低风险动作快速推进、高风险动作显式化，支持“不要把所有事都变成人工 gate”。

## 11. Critic 审查请求

请独立审查：

1. 8 个 audited candidate 是否仍有重复或遗漏；
2. Lite baseline 是否仍过长/过重，或缺少必须 always-on 的底线；
3. workflow-core 是否越权进入 domain/frontend；
4. Frontend Design 的现有 TODO 是否应先合并而不是继续新增；
5. Scientific Visualization 是否应该接收 Asteria raw feedback，边界如何划；
6. Bobbio/Lucerna/Mica/Asteria 的 repo-specific 建议是否确实最小；
7. Capability Gate Matrix 是否能防止“文件里写了规则 = 实际能力已完成”；
8. 是否应在 Critic PASS 前仅更新 status: NEW evidence，而不碰 production AGENTS/skills/templates。

Critic PASS 前：`READY_FOR_CODEX = NO`。
