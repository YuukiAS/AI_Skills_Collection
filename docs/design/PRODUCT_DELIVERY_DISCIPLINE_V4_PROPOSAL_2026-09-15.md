# Product Delivery Discipline v4 — Planner Proposal

状态：`DRAFT_FOR_CRITIC_REVIEW`  
日期：2026-09-15  
基线：`main@51342ae205525c53ad2fd589544c6d644a91f393`  
替代关系：本提案在 v3 的官方 ChatGPT export 证据基础上，加入 2026-09-15 Lucerna OpenAI Usage Monitor 的新真实失败，以及用户明确新增的 human-action 要求。Critic PASS 前不修改 production skill、Bridge Kit Lite template 或任何产品 AGENTS。

## 1. Active Design Context

```text
target_repo = YuukiAS/AI_Skills_Collection
target_plugin_or_domain = workflow-core + web-development + ai-skills-core; Bridge Kit Lite as distributor; repo-specific consumers
design_topic = cross-project product delivery discipline and human-gated task closure
source_branch_or_ref = main@51342ae205525c53ad2fd589544c6d644a91f393
proposal_path_and_version = docs/design/PRODUCT_DELIVERY_DISCIPLINE_V4_PROPOSAL_2026-09-15.md / v4 draft
execution_branch/worktree = NOT_CREATED
```

本轮是 Planner 设计轮次。已重新读取最新 Planner/Critic contract、Capability Gate Policy、当前 workflow/frontend/maintainer TODO、重点 repo AGENTS，并做针对性外部检索。OpenAI 自身公开经验强调：AGENTS 应作为短导航而不是巨大手册；复杂反复工作应由更深层文档/skill 承担。这支持“Lite 短底线 + workflow/domain 深规则”的分层，而不是把所有事故都堆进每个 repo 的 AGENTS。

## 2. 新的 Lucerna 事故改变了什么

Lucerna Goal `01033_openai_usage_monitor_shared_vault` 在用户输入前其实正确记录了：

```text
RESULT=NEEDS_HUMAN_ACTION
NEXT_USER_ACTION=Lucerna -> OpenAI API -> Set up -> ... -> Validate & save
OPENAI_VALIDATION=PENDING_USER_LOCAL_INPUT
OPENAI_PROVIDER_LIVE=PENDING_USER_LOCAL_INPUT
```

同时大量编译、单测和 release build 已 PASS。用户随后按要求输入 key，但真实 UI 仍显示 `Not set up`，又进入修复 `show OpenAI validation progress` 与 `split OpenAI validation diagnostics`。这说明：

1. **“已经 prompt 用户”本身仍不等于 workflow 正确。** Human action 是中间 checkpoint，不是完成证据。
2. 用户动作发生后，Executor 必须恢复同一个 Goal，亲自验证 post-action 正向目标：credential 接受、live provider read、持久化/状态映射、正常 UI 从 `Not set up` 转到真实状态，必要时 restart/reopen 后仍成立。
3. pre-human unit/build/screenshot 不能证明 post-human integration；正如 browser fixture 不能证明 native interaction。
4. 如果 task 从 Goal authoring 时就可预见需要用户动作，Goal 必须明确写出 **prompt contract**；Executor 到达该 gate 时必须实际 prompt，不能静默等待，也不能仅因为需要一个用户动作就终止为不可恢复 `BLOCKED`。
5. 用户完成动作后若真实目标失败，责任回到 Executor 继续诊断/修复；不能把同一未经新证据的路径再次端给用户重试。

因此 v4 把 v3 的 “User-interaction ownership” 升级为 **Human-gated action lifecycle**，并新增一个独立的 **Post-user-action closure** 能力要求。

## 3. 最终建议的 9 个通用机制

这些机制是中央规则候选；具体 Lucerna/Bobbio/Mica/Asteria 名词不进入通用规则正文。

### R1. Positive goal fidelity

任务开始时明确用户真正要得到的正向结果、实际对象/版本、正常入口和不可替代条件。代码写完、构建 PASS、测试 PASS、生成截图、写 result 或到达某个流程状态，都只是过程证据，不能替代原始正向结果。

只要求设计/诊断/计划时也不能反向膨胀成必须上线或真人验收。规则约束的是“claim 与原目标一致”，不是一律更重。

### R2. Human-gated action lifecycle — Goal 必须预声明 prompt

如果 Goal 在编写时已经知道某一步只有用户能完成，例如：

- 输入或确认 secret，但 secret 不应暴露给 agent；
- OS/app 授权；
- 人工网页登录/OAuth/设备确认；
- 必须由用户做的产品选择；
- agent 工具确实无法完成的一个最小 GUI 动作；

则 Goal / kickoff 必须显式声明：

```text
HUMAN_ACTION_REQUIRED = YES
PROMPT_REQUIRED = YES
PROMPT_TRIGGER = <到达哪个 gate 时>
USER_ACTION = <只做哪一个动作>
USER_REPLY = <完成后怎样回复>
DO_NOT = <必要安全禁区>
RESUME_POINT = <收到回复后从哪里继续>
POST_ACTION_ACCEPTANCE = <agent 必须自己验证什么>
```

Executor 到达该 gate 时必须实际调用当前 host 可用的 request-user-input / prompt 机制。若该工具在当前 surface 不存在，必须在聊天中发出同等清晰的单步可见请求并暂停依赖步骤；不得静默轮询、只写 result 文件、只发普通进度消息后等待。

**仅缺一个可恢复用户动作不能因为方便而直接写成不可恢复 `BLOCKED`。** 应映射到现有 workflow 的合法 waiting/human-decision 语义；不新增状态机。只有确实无法通过现有 prompt/wait/resume 路径恢复，且有证据时，才使用真正不可恢复失败语义。

已经明确授权的同一 artifact/provider/purpose/credential/cost 范围不得重复询问；新范围才重新 gate。

### R3. Post-user-action closure — 用户动作之后必须由 agent 闭环

Human action 只是 checkpoint。收到用户完成回复后，Executor 必须恢复同一个 Goal 并验证其后的真实正向结果，而不是把“用户已输入/已点击”记成 feature complete。

对于 credential/setup/provider 类能力，至少按任务风险检查适用项：

1. 输入被产品真正接受，而不是只关闭 modal；
2. validation 成功，并区分局部权限失败/错误 scope；
3. credential/state 按设计持久化或安全缓存；
4. production provider/runtime 实际消费新状态；
5. 正常用户 UI 显示真实 live/available/auth-error，而不是仍然 `Not set up`、stale 或 placeholder；
6. 必要时 restart/reopen 后仍能复用；
7. 失败不会写入半成品 active state；
8. 相关旧行为没有被破坏。

只有这些属于 Goal completion contract 的正面结果通过，才可完成。用户动作暴露失败后，先修根因并做 targeted replay；没有新证据前不得再次要求同一路径的人类重试。

### R4. Exact failure + faithful regression

Bug/behavior failure 必须先建立准确事实：旧行为是什么、在哪里、预期是什么、哪条证据证明 mismatch。能自动化时，用能抓住旧失败的最窄 regression 证明 old-bad -> new-good；已有测试确实覆盖时复用，不为数量重复造测试。

真实服务/原生环境无法自动化时，保留一次可信 failure capture，再构造 faithful replay。若旧坏实现不会在 fixture/test 中失败，说明测试不忠实，先修证据路径而不是继续改 runtime。

新功能、行为变化也必须有与风险匹配的测试，不只 bug fix 才加测试。

### R5. Evidence-surface fidelity

Claim 的范围不得超过 evidence 的 surface：

- unit/static test 只能证明对应逻辑；
- synthetic/browser fixture 不能证明 native desktop/live authenticated service；
- source 存在不能证明 normal entry 消费；
- screenshot 不能证明 button action；
- helper 能跑不能证明普通用户入口能跑；
- pre-human build 不能证明 post-human setup integration。

最终 candidate 发生 substantive change 后，关键 gate 必须由当前 candidate 自己重新通过，不能拼旧版本证据。

### R6. Producer self-QA before external/human review

用户和独立 reviewer 是最后确认与发现盲区的人，不是第一线 debugger/设计师/测试员。

在请求用户或外部 reviewer 前，producer 必须完成自己现有工具能够安全完成的：

- targeted regression；
- actual-surface smoke；
- 明显视觉/交互自审；
- main-path error/healthy-state consistency；
- 正确 candidate identity；
- 当前所需 evidence 完整性。

若明显问题仍可由 agent 自己观察/修复，不得交给用户发现。人类动作不可避免时，只请求一个最小动作。

### R7. Repeat-failure circuit breaker

以下任一出现时，禁止无信息地继续重跑 full suite、Atlas、GPT Work 或真人验收：

- 相同用户症状再次出现；
- 同一测试/验收无新信息连续失败；
- 用户再次指出同一类别明显缺陷；
- 测试一直绿但真实路径反复失败；
- 规则明明存在但行为仍重复违反。

必须先重新检查：

```text
candidate/runtime identity
actual rule/plugin loading
failure hypothesis
fixture fidelity
evidence surface
data/environment differences
whether repair touched root cause
whether accepted behavior regressed
```

下一次昂贵/人工重试必须检验新的假设或新的修复；否则停止失败路线并回 Planner，而不是把用户时间当循环资源。

### R8. Protect accepted behavior

修改共享 UI/state/runtime/design mechanism 时，先识别本轮会影响的既有接受行为，并做相邻回归。修一个按钮不能让此前 close/tray/refresh/provider/typing/performance/annotation 等已接受行为退化。

用户主动改变产品要求时，旧行为当然可以废弃；此时要明确这是新决策，不是假装无回归。

### R9. Design source + whole-product closure（只在视觉/UI任务触发）

如果存在 canonical Figma/design artifact，它是 production visual source of truth，不是 moodboard。

- 缺 production state/interaction 时先补 design，再实现；
- design 正确但代码偏离时固定 design、修实现；
- 禁止直接在代码里发明未设计的按钮、箭头、卡片、装饰图形、重复 CTA 或新的 component grammar；
- 实现后从实际 target surface 做 full-screen 对照，不只看 component crop；
- 检查 hierarchy、component family、spacing、interaction states、motion、responsive、empty/error/loading/recovery；
- 外部 visual review 只在 producer-local obvious defects 已清零后进入。

这条由 Frontend Design 负责具体专业标准。Scientific schematic 中具有模型/统计语义的 connector、endpoint、uncertainty、math encoding 等，再路由 Scientific Visualization；workflow-core 只负责正确调用 owner 和 gate。

## 4. 各层应该放什么

### Lite Handoff / project-installed baseline

Lite 必须短，因为每个普通 repo 都会消费；它只放不依赖专业插件触发的底线：

1. 保持原始目标与不可替代条件；不静默降级。
2. **Goal 中可预见的用户动作必须写 prompt contract；到点实际 prompt，不静默等待，不因单个可恢复用户动作直接不可恢复 BLOCK。**
3. 用户完成动作后，agent 继续同一 Goal 做 post-action closure；human step 不是 completion。
4. feature/behavior/bug fix 有风险匹配的 validation；proxy evidence 不冒充实际 surface。
5. 同类失败无新信息时停止 blind rerun / repeated human QA，先重新诊断。
6. final report 区分完成、部分完成、等待用户/外部、未验证，并给 resume point。

Lite 不复制 Figma checklist、按钮 anatomy、Mica DOM、Lucerna provider 或 Asteria arrow 规则。

### Verified Workflow / workflow-core — 主要 owner

把 R1–R8 变成 normal execution contract：

- Goal authoring 时识别 foreseeable human gates；
- human gate prompt/resume；
- post-user-action closure；
- exact failure/faithful regression；
- evidence surface/candidate identity；
- producer self-QA 与 human QA budget；
- repeat-failure circuit breaker；
- protected behavior；
- truthful final status；
- domain routing。

不新增第二套 state/schema/ledger；使用现有合法 workflow 状态。

### Frontend Design / web-development

当前 TODO 已有大量正确候选，不继续平行加口号。下一轮 production refinement 应把它们收敛为少量真实 gates：

1. canonical design + state coverage；
2. component/interaction grammar；
3. implementation -> actual-surface whole-screen comparison；
4. producer visual self-QA；
5. external confirmation after local convergence。

Lucerna/Bobbio/Asteria 的具体视觉风格只作为 evidence，不成为通用默认样式。

### Scientific Visualization

Asteria 的 scientific schematic case 已作为 `status: NEW` evidence 记录。未来只把跨项目仍成立的科学图示语义质量（routing/endpoint/label/math/encoding）提升为 capability；普通 frontend composition 仍归 Frontend Design。

### AI Skills Maintainer

已有规则仍失败时，优先核实 actual installed version、plugin invocation、task entry、generated/consumer parity、current-session loading 与 normal production replay。不能靠再写一条同义 TODO 证明问题解决。

### Bridge Kit

Bridge Kit 只负责：

- 向 Lite 安装面分发短 baseline；
- 确保已有 request-user-input / wait / resume 机制真实可用；
- 对这些机制做必要测试。

不新增 controller、watcher、ledger、状态机。当前 Host Policy 已有 `default_mode_request_user_input = true`，所以新事故首先要验证“为什么没有被正确使用”，而不是先造新 prompt 系统。

## 5. Repo-specific 建议

### Lucerna

新 OpenAI incident 说明已有 AGENTS 的“真实 release UI + truthful provider + matching regression”仍不足以保证 **human-gated setup closure**。但这个机制首先是 workflow-core 通用问题，不应在 Lucerna 复制中央规则全文。

Critic PASS 后，Lucerna repo-specific 最多补一条很短的 product invariant：任何 provider/credential onboarding 只有在用户完成必要本地输入后，由 agent 从当前 release 验证 `accepted -> stored -> provider live -> normal UI configured/live -> restart reuse if applicable` 才算完成；否则保持当前 Goal active。具体 OpenAI scope/Costs/Usage 语义仍留 Lucerna provider docs/tests。

更重要的是补/检查能抓住 `Validate & save 后仍 Not set up` 类别的 targeted integration/smoke，而不是只加文字。

### Mica

保留真实 ChatGPT 最终手工边界，但正式要求：一次 live failure capture -> faithful fixture 能抓住旧失败 -> 本地修复 -> candidate gate -> 最后一次真人确认。真实同症状复发且没有新 replay 证据时禁止再次真人循环。

### Bobbio

不再加重复“不要让用户帮忙看 UI”的段落。去重现有 section；把 canonical Figma/design source 接到 normal frontend entry：missing state -> design first -> implementation -> native full-screen comparison。

### Asteria

已有 developer visual self-QA 与 scientific graph visual system。重点验证规则真实消费并把视觉 repair 锁进 generic regression；不继续给 AGENTS 增加重复视觉条款。

### Lucerna 之外的 server/research task 反例

纯后端/server、纯文档、只读诊断没有视觉 surface 时，不触发 Figma/whole-product gate；没有 human action 时不制造 prompt。规则必须减少而不是增加无关仪式。

## 6. workflow-core Capability Gate Matrix（待 Critic 审）

| Gate | Capability / normal entry | Evidence / failure | Final candidate |
|---|---|---|---|
| G1 Human prompt/resume | Goal 预声明一个真实必须用户操作的 gate | 到点实际 prompt；不静默轮询；用户回复后从同一 resume point 继续。仅写 result 或不可恢复 block = FAIL | YES |
| G2 Post-human closure | credential/setup 类真实任务 | 用户动作后 agent 自己验证 normal surface 的 configured/live 正向结果；把“用户已操作”当 complete 或仍 `Not set up` 却交付 = FAIL | YES |
| G3 Faithful regression | 一个 deterministic bug + 一个 live-only bug | old-bad/new-good 或可信 live failure capture + faithful replay；broad suite 代替原失败 = FAIL | YES |
| G4 Evidence-surface fidelity | synthetic/browser/native/live 混合案例 | claim 不超 surface；旧 candidate/proxy 冒充 production = FAIL | YES |
| G5 Repeat-failure stop | 同一症状二次出现的 replay | 第二次不 blind rerun/human QA；先产生新 attribution/hypothesis/replay evidence | YES |
| G6 Protected behavior | 共享 mechanism 修复 | 原问题通过且 adjacent accepted behavior 保持 | YES |
| G7 Should-not-change | docs-only/server task、无需 human/visual 的普通任务 | 不被强行升级为 Figma、human QA、paid review 或重 workflow | YES |
| G8 Production consumption | 实际安装/正常入口调用 workflow-core | active skill/rule 真被 consumer 使用；只检查 source 文本存在 = FAIL | YES |

## 7. 外部资料采用决定

本轮采用 OpenAI 官方 Codex 资料的两点：

- AGENTS 是持久 repo context，但大型单体 AGENTS 会挤占任务/代码上下文，适合“map, not manual”；因此坚持 Lite baseline 短、详细流程由 skill/reference 承担。
- Codex 的实际行为来自 instructions + tools + user input 的组合，AGENTS 只是其中一层；因此“文件写了 prompt 规则”不能证明 runtime 会真的 prompt，必须做 production consumption replay。

不采用“再增加更多角色/控制器”作为解决方案；当前失败是基本交付纪律、真实证据和消费路径没有闭环，不是缺一个新 orchestration framework。

## 8. 现在不做什么

Critic PASS 前：

- 不改 Bridge Kit Lite template；
- 不改 workflow-core production skill；
- 不改 Frontend Design production；
- 不改 Lucerna/Mica/Bobbio/Asteria AGENTS；
- 不创建 successor / Executor task；
- 不调用 paid review。

允许继续完善 Proposal、TODO evidence 和 Critic prompt。当前用户已明确表示希望先把这套规则彻底收口，再继续其他开发。
