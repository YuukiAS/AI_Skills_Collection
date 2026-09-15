# Product Delivery Discipline v5 — Planner Proposal

状态：`DRAFT_FOR_CRITIC_REVIEW`  
日期：2026-09-15  
基线：`main@071fe957d9dce8d5c9528b2d27e1109b8239e7b2`  
替代关系：本提案纠正 v4 对 Lucerna 新事故的归因重点，并在官方 ChatGPT export 审计、当前 repo 规则与用户最新要求基础上重新设计“何时才允许 GPT Work / 用户介入”和“需要用户动作时如何持续阻塞等待”。Critic PASS 前不修改 production skill、Bridge Kit Lite template 或任何产品 AGENTS。

## 1. Active Design Context

```text
target_repo = YuukiAS/AI_Skills_Collection
target_plugin_or_domain = workflow-core + web-development + ai-skills-core; Bridge Kit Lite as distributor; repo-specific consumers
design_topic = complete-before-handoff product delivery discipline + persistent human prompt + design-system convergence
source_branch_or_ref = main@071fe957d9dce8d5c9528b2d27e1109b8239e7b2
proposal_path_and_version = docs/design/PRODUCT_DELIVERY_DISCIPLINE_V5_PROPOSAL_2026-09-15.md / v5 draft
execution_branch/worktree = NOT_CREATED
```

本轮是 Planner 设计轮次。已重新读取最新 Planner/Critic contract、Capability Gate Policy、当前 workflow/frontend/maintainer TODO、Bridge Kit user-input policy，以及重点 repo AGENTS。也进行了外部研究：

- OpenAI `Harness engineering`：人的注意力是稀缺资源；agent 应自行 review/drive application；AGENTS 应是短导航而不是大手册；失败应转化为可执行的工具/guardrail/feedback loop，而不是“再试一次”。
- Figma developer handoff / design process：master components、variants/states、styles/tokens应形成可供开发消费的 source of truth，设计与代码应同步，而不是 handoff 后各自漂移。
- Microsoft `AnimatedIcon`：动画应与真实交互状态转换绑定；没有交互动画需求的图标不应为了“都有动效”而强制动画。这个边界用于避免把用户“图标不能再粗糙、静态、乱画”的要求机械化成所有 status/brand icon 都循环动画。

## 2. 对 Lucerna 新事故的纠正归因

用户明确指出 v4 把两件事混在了一起。

### 2.1 第一件事：不是“用户操作后闭环”本身，而是**在让用户/外部 reviewer 介入前必须尽可能彻底做完**

Lucerna OpenAI Usage Monitor 只是一个新例子：开发方在大量编译/单测/构建 PASS 后让用户去输入 key，用户一操作就暴露 `Not set up` / validation feedback / endpoint diagnostics 等仍未收口的问题，随后又连续返修。

用户真正要求的是：

> 不允许 `做一点 -> 让用户/GPT Work验收 -> 暴露本来开发者自己应该发现的问题 -> 返修 -> 再验收`。

因此必须新增 **Review Admission / Pre-Human Readiness Gate**：只要某项缺陷仍能由 agent 自己通过代码、测试、fixture、真实 target surface、Figma、local native UI、日志、provider-safe probe 或已授权工具发现并修复，就不允许进入 GPT Work 或最终用户验收。

这条与“中途不可替代的用户动作”要分开：用户可能必须输入 secret、完成 OS 授权、网页登录等，但这只是执行 checkpoint，不是“开始验收”的时刻。**所有与该动作无关、以及可以在没有该 secret/点击之前完成的实现、错误处理、UI、设计、测试、diagnostics、状态机和恢复路径，都必须先完成。**

### 2.2 第二件事：Goal 里可预见需要用户操作时，必须是**持续、阻塞、非过期的 prompt**

用户不要“提示一下然后过一会儿消失”的通知式 prompt，也不要后台继续跑到 `BLOCKED`。

目标语义是：

```text
到达 human gate
-> 显示 persistent blocking request-user-input
-> 当前依赖链暂停
-> prompt 保持 pending，直到用户明确回应 / 取消
-> 不因等待时间而自动消失、超时转失败或改成 BLOCKED
-> 收到回复后从 frozen resume point 继续
```

Bridge Kit 当前已经启用 `default_mode_request_user_input = true`，并已有“recoverable question is not terminal BLOCKED”的规则；但当前规则没有证明 **prompt persistence / no-expiry / runner timeout immunity**。因此这是一个真实的 Bridge Kit / host capability verification gap，而不只是文案问题。

如果当前 Codex surface 的 request-user-input 不能做到 persistent blocking，Bridge Kit 必须：

1. 明确报告该 host capability 不满足；
2. 保持 repository workflow state 不变；
3. 不用 ephemeral toast/普通进度消息冒充；
4. 不把等待计入 retry/repair budget；
5. 不自动转 terminal BLOCKED；
6. 提供受限、可恢复的替代机制前须经独立 Critic，而不是在项目里临时发明 polling/watchdog。

## 3. 重新收敛后的 10 个通用机制

### R1. Positive-goal fidelity

开始任务时明确用户真正要得到的正向结果、实际对象/版本、normal entry、不可替代条件和完成证据。代码完成、测试 PASS、截图、result、某个内部 state 都不能替代原始正向结果。

只要求设计/研究/诊断时也不能反向膨胀成上线或真人验收；“更严格”不能改变任务本身。

### R2. Pre-human readiness / review admission gate

在进入 GPT Work、独立外部 reviewer 或最终用户验收之前，producer 必须完成当前 scope 内所有能够自行完成的工作，并形成一个 **feature-complete / milestone-complete review candidate**。

进入 review 前至少确认适用项：

- 功能实现完整，不是半成品 checkpoint；
- 新增功能/行为变化/bug fix 的 targeted validation 已完成；
- known regression 已跑；
- actual target surface 已 smoke；
- 明显 loading/error/empty/recovery 路径已处理；
- 设计/Figma/visual system 已收敛；
- component/icon/layout/motion 没有明显局部漂移；
- candidate identity 与待审 build 一致；
- 需要的 diagnostics 已经存在，不靠用户帮忙收日志；
- producer 自己看过最终 artifact/UI，而不是只看测试字段；
- 不存在已知、可由 agent 自己修复的 P1/P2/明显产品缺陷。

**禁止 incremental acceptance**：不能每实现一个小段就让 GPT Work/用户“看看行不行”。中间检查只能是 agent 自己的 development QA；外部/human review 面向收口后的 candidate。

如果 external review 找到缺陷，先回 producer 内部修复和回归。只有修成新的 review-ready candidate 才重新 external review；最终用户不参与这个修复循环。

### R3. Foreseeable human action must be declared in the Goal

Goal / kickoff 若已知存在 agent 无法替代的用户动作，必须提前写清：

```text
HUMAN_ACTION_REQUIRED = YES
PROMPT_REQUIRED = YES
PROMPT_TRIGGER = <exact gate>
PROMPT_MODE = PERSISTENT_BLOCKING
USER_ACTION = <one minimal action>
USER_REPLY = <what unblocks>
DO_NOT = <safety limits if needed>
RESUME_POINT = <where agent continues>
POST_ACTION_AGENT_WORK = <what agent, not user, must do next>
```

这些不要求新增 workflow schema；可以作为 task/Goal human-decision section 的语义合同，由现有模板承载。

### R4. Persistent blocking prompt

到达 R3 的 gate 后必须实际使用当前 host 的 request-user-input / prompt capability，并满足：

- pending until explicit response/cancel；
- dependent execution paused；
- no silent polling；
- no ephemeral notification as substitute；
- no automatic timeout -> terminal failure；
- no automatic timeout -> `BLOCKED`；
- no repeated prompt for the same answered scope；
- user answer resumes from the recorded point rather than restarting the task。

真正不可恢复的 host/tool failure 与“用户还没点”必须严格分开。

### R5. Human action is not acceptance

中途需要用户输入 secret、完成授权、登录、设备确认等，不等于进入用户验收。

在用户完成动作后，agent 自动继续同一 Goal，完成与该动作相关的 integration closure：validation、persistence、runtime consumption、normal UI/state、必要 restart/reopen、failure safety、targeted regression。

只有 R2 的 review-ready gate 也满足后，才允许 external/human acceptance。

这条保留 v4 的 post-action closure，但降为 R2/R3/R4 之后的子闭环，不再把 Lucerna 的根因简化成“用户动作后没测”。

### R6. Exact failure + faithful targeted validation

所有新功能、行为变化和 bug fix 都必须有风险匹配的验证；bug 修复优先证明旧失败被准确捕获。

能自动化时：old-bad -> new-good。  
真实服务/native 场景无法完整自动化时：保留一次真实 failure capture，建立 faithful replay / deterministic assertions，再在最终 actual surface 做必要 smoke。

如果旧坏实现不会让新 fixture/test 失败，说明证据不 faithful；先修测试，不继续靠 broad suite PASS 自证。

### R7. Evidence-surface fidelity

Claim 不能超过证据：unit/static/synthetic/browser/native/live/user acceptance 各自只证明其 surface。

特别禁止：

- synthetic E2E 冒充 real authenticated app；
- browser fixture 冒充 native desktop；
- screenshot 冒充 click/action；
- source/handler 存在冒充 normal entry；
- helper-only path 冒充 product path；
- pre-human gate PASS 冒充 post-human integration；
- 旧 candidate 的关键 PASS 拼给新 candidate。

### R8. Repeat-failure circuit breaker + human-time budget

相同症状再次出现、测试一直绿但真实路径再次失败、同一 reviewer/user 再次指出同类问题、或已有规则再次被违反时，停止盲目 rerun / re-review。

下一轮前必须获得至少一种新信息：新的 failure hypothesis、faithful fixture、root-cause repair、candidate correction、rule-loading evidence 或 environment explanation。

没有新信息不得再次调用：full suite、Atlas、GPT Work、真人验收。人的注意力不是调试循环资源。

### R9. Protect accepted behavior + system-wide consistency

修改共享 UI/state/runtime/design mechanism 前，识别受影响的已接受行为和同族组件。局部修复不仅要防回归，还要检查同一 visual/component family 是否因此出现不一致。

例如：改一个按钮 family、icon family、radius、spacing、motion、status treatment 时，不允许只修截图里那一个实例而把同级 sibling / 其他主要 screen 留成另一套设计语法。

这条是 workflow 的 should-not-change 责任；具体视觉一致性由 Frontend Design 定义。

### R10. Design-source authority + design-system convergence（仅视觉/UI任务触发）

存在 canonical Figma/design artifact 时：

1. Figma/design 是 production source of truth，不是 moodboard；
2. production 所需 state/variant/responsive/interaction 缺失 -> **先改设计**；
3. 设计正确而实现偏离 -> **固定设计，修代码**；
4. 禁止 implementation agent 在代码里临时发明按钮、圆、箭头、card、pill、CTA、spacing grammar、icon style；
5. 设计变更先在 source-of-truth 中完成、自审、freeze，再实现；
6. implementation 完成后做 actual-surface full-screen comparison；
7. unrecorded visual deviation 是 defect；必要的 platform/accessibility deviation 应先反馈到设计源并形成一致决定，而不是静默漂移。

## 4. Frontend Design 的详细 production gates

当前 `web-development` TODO 已经有大量正确候选；问题是过于分散。下一轮 production refinement 应 **合并而不是继续平行堆条目**，最终形成以下几组 capability gates。

### F1. Canonical Design Gate

- 找到并读取 canonical Figma / design file；
- 确认当前里程碑所有要发布的 primary states/variants；
- 缺 state 先修改 Figma/design；
- freeze 后才 coding；
- design revision 后旧 implementation screenshot 不再算最终依据。

Figma 官方 handoff 实践强调 master component + variants/states + styles/tokens 是 source of truth；这正对应 Bobbio/类似项目的失败。

### F2. Design System Consistency Gate

整个 screen/product 要统一：

- component families；
- control hierarchy；
- typography scale；
- spacing rhythm；
- radius/border/surface；
- semantic colors；
- hover/pressed/focus/selected/disabled/loading/destructive states；
- motion grammar；
- density；
- empty/error/recovery composition。

改一个 shared family 时应检查所有同级主要实例，不允许“这里修漂亮了、那里还是旧样式”。现有 `design-system-tokens` 已有 primitive/semantic/component tokens、motion/state tokens，TODO 应优先推动正常入口真正消费它，而不是新增第二套 token 概念。

### F3. Mature Icon / Asset Gate

用户要求的本质是：不再让 agent 随手画粗糙 SVG/圆点/占位图标。

建议通用规则：

- generic UI/action/status icons 默认来自项目既有 canonical icon library、platform-native system 或成熟维护库；
- 若项目未选，设计阶段必须先选一个 coherent family；
- 不混用多套 generic icon family；
- brand/provider mark 优先官方资产或成熟 brand set；
- custom SVG 仅用于 product identity、真正 domain-specific symbol、或成熟库确实没有的 gap，并记录理由；
- 所有图标通过中央 registry/component 管 source、size、optical alignment、state、theme、accessibility；
- placeholder emoji/random dots/ad-hoc SVG 不得进入 production candidate。

### F4. Interaction Motion Gate

不建议把“所有图标必须动画”机械写成全局规则。成熟平台实践更合理的是：

- interactive icon/control 必须有清晰 hover/pressed/focus/selected/busy feedback；
- 若图标本身适合状态转换动画，使用成熟/一致的 animation grammar 或库；
- static brand/status/informational icon 在没有交互状态转换时不强制动画；
- 禁止为了显得“高级”而循环、无意义、影响扫描效率的 motion；
- respect reduced-motion；
- motion 不能掩盖 latency 或逻辑失败。

Microsoft `AnimatedIcon` 官方也明确只建议在与 control interaction/state transition 绑定时使用；无需要时用普通 static icon。这个边界比“每个 icon 都动”更成熟，也更符合用户真正想避免粗糙静态占位符的目标。

### F5. Actual-Surface Whole-Product Gate

实现后必须在真实 target surface 查看完整界面，不只 component crop：

- native app 看 native；
- web app 看真实 browser/runtime；
- mobile 看 emulator/真机中与本轮风险相称的 surface；
- 比较 canonical design 与 actual result；
- 检查整个窗口/viewport 的 hierarchy、balance、density、cross-component consistency、motion 和 states；
- producer local obvious P1/P2 清零后才允许 external visual review。

## 5. Lite Handoff 最终建议：只保留 8 条短底线

Lite 必须在 plugin 未触发时仍有效，但不能成为百科全书。

1. **原始目标**：保持 positive goal、normal entry、不可替代条件；不静默降级。
2. **Review admission**：能由 agent 自己完成/发现/修复的工作全部完成后，才允许 GPT Work/外部 reviewer/最终用户验收；禁止 incremental acceptance。
3. **Foreseeable human gate**：Goal 中已知需要用户动作就必须预声明 persistent prompt + resume point；到点实际 prompt。
4. **Persistent wait**：用户未回应时保持 waiting；不静默轮询、不因时间到自动消失/失败/terminal BLOCKED。
5. **Human action != acceptance**：用户动作后 agent 自己继续闭环；不把用户输入/点击当 feature completion。
6. **Matching validation**：feature/behavior/bug fix 有风险匹配的 targeted validation；proxy evidence 不冒充 real surface。
7. **No blind rerun**：同类失败没有新信息时停止重复 heavy test/reviewer/human QA，先重新诊断；保护已接受行为。
8. **Truthful handoff**：final report 说明当前真实能力、未验证边界和 resume point；不只报 tests/logs。

详细 Figma/icon/motion/testing checklist 不复制进 Lite。

## 6. Verified Workflow / workflow-core — 本轮主要 owner

下一轮正式 refinement 应把 R1–R9 变成 normal execution contract，重点不是新增状态/schema，而是增加 **admission gates 与 transition semantics**：

1. **Goal authoring preflight**：识别 foreseeable human action、external review、final human acceptance；写明谁在什么时候介入。
2. **Pre-Human Readiness Gate**：任何 external/human review 前，producer-owned implementation/tests/actual-surface/design/diagnostics 全部先收口。
3. **Human Action Gate**：persistent blocking prompt；不 response 不继续依赖链；waiting 不消耗 repair/retry budget。
4. **Action vs Acceptance split**：中途 human action 与最终 user acceptance 是两个不同 gate。
5. **Post-action executor closure**：human action 后 executor 自动恢复并自己验证相关 integration。
6. **Exact failure / faithful replay**：旧失败必须被针对性证据抓住；broad suite 不替代。
7. **Evidence-surface / final-candidate identity**：claim 与 evidence 对齐，关键 gate 由 final candidate 通过。
8. **Producer self-QA / external review admission**：external reviewer 用来独立确认，不用于发现 producer 可见的明显缺陷。
9. **Repeat-failure circuit breaker**：无新信息不重复 full suite/GPT Work/human QA。
10. **Protected behavior / adjacent regression**：修复共享机制必须保护既有能力。
11. **Domain routing**：视觉/Figma -> Frontend Design；科学图示语义 -> Scientific Visualization；workflow-core 不决定具体 icon/style。
12. **Final report**：以“用户现在真正能做什么”为中心，不以测试数量为中心。

### Capability gates for this workflow refinement

| Capability | Normal entry | Evidence | Failure |
|---|---|---|---|
| Pre-human readiness | ordinary feature task with external/human final review | agent finishes implementation, targeted tests, actual-surface smoke and local QA before emitting review-ready handoff | GPT Work/user receives obvious unfinished state or first discovers locally observable defect |
| Persistent prompt | Goal with one foreseeable human-only action | request remains pending until explicit response/cancel; workflow state preserved; no timeout->BLOCKED | prompt disappears/times out or task terminates while answerable |
| Action/acceptance separation | credential/OS-auth/manual click task | user action resumes same Goal; acceptance not requested until final candidate is locally ready | user input itself counted as completion or user immediately asked to debug unfinished integration |
| Faithful regression | reproduced bug | old candidate fails focused regression; repaired candidate passes; actual surface confirms | broad tests pass but original failure is not exercised |
| Repeat-failure stop | repeated real failure after green tests | second attempt changes hypothesis/fixture/root-cause evidence before any new expensive/human replay | same test/reviewer/user loop repeated with no new information |
| Should-not-change | shared UI/runtime fix | targeted adjacent regression for affected accepted behavior | new fix silently regresses accepted behavior |
| Non-overreach | docs-only/server/simple task | no Figma/GPT Work/extra human gate unless relevant | new workflow forces irrelevant heavy gates |

## 7. Repo-specific AGENTS：只加本项目真正独有的东西

### 7.1 Lucerna

**需要新增/强化一个 provider onboarding invariant，而不是再复制通用 workflow：**

- 任何 provider/credential onboarding 在请求用户输入前，必须完成所有不依赖 secret 的实现、validation logic、failure diagnostics、no-write-on-failure、UI states、runtime wiring、targeted tests 和 actual release smoke；
- 用户只负责不可替代的 credential/account action；不是产品 QA；
- 用户完成后，Codex 自动继续并验证 provider live、normal UI state、persistence/reopen/restart（若设计要求）和 failure safety；
- 只有整个 onboarding candidate 进入 review-ready 状态后才交 GPT Work/用户做最终验收；
- 同一 provider flow 应有 reusable integration smoke，不能每加一个 provider 都靠用户第一次操作来发现 glue code 没接通。

这次 `OpenAI key -> UI 仍 Not set up -> 连续补 validation progress/diagnostics` 应作为该 invariant 的 regression evidence。

### 7.2 Bobbio

Bobbio `develop` 已有大量 native UI self-inspection / prompt 规则，当前问题不是再加更多同义段落，而是 **去重并把 design source 接到 normal entry**：

- frontend/Product Design task mandatory read：canonical Figma handoff + Product Design Brief + current milestone design states；
- design 缺 state -> 修改 canonical design -> self-review/freeze -> implementation；禁止 code-only improvisation；
- implementation -> native full-window comparison；
- shared component/icon/motion 必须走 Bobbio canonical component/design system；
- external GPT Work only after native local visual/product QA has no obvious must-fix issue；
- 顺带删除 AGENTS 中重复的“不要把用户当截图工具”段落，改成短规则 + 指向唯一 contract，避免 AGENTS 继续膨胀。

### 7.3 Mica for ChatGPT

Mica 已有很强的 test budget / real-site safety，但要加一个 **live failure conversion contract**：

- 真实 ChatGPT 人工验证第一次失败后，下一次请求用户前必须先把该 failure 转化成 faithful fixture/replay 或明确证明无法 fixture 化；
- old candidate 应在该 replay 中失败；new candidate local gates 通过后才允许下一次 real-site confirmation；
- 不允许 Atlas/diagnostic harness 自己膨胀成目标；诊断只为捕获真实 failure semantics 服务；
- final authenticated-user check 应尽量一次完成一组已本地收口的风险，而不是一 patch 一真人验收；
- 同一症状第二次失败立即触发 repeat-failure circuit breaker。

### 7.4 Asteria

Asteria 已经有 developer visual self-QA、canonical scientific graph visual system、generic-fix rule、GPT Work-before-human gate。**默认不再加同义 AGENTS。**

下一步应验证这些 rules 是否从 normal task entry 真实被读取/执行；若未执行，修 task routing/consumer path。只有出现新项目不变量才补 AGENTS。

### 7.5 SeminarArc

SeminarArc 已有大量 emulator/physical-device safety。若用户确认存在 canonical Figma/design source，但 repo 当前没有明确 locator，则应新增 **唯一 design source locator** 和 Android design-to-Compose handoff入口；不要在 AGENTS 复制一套 Frontend Design checklist。

否则先保持现状，不根据聊天记忆臆造 Figma path。

### 7.6 CUHK Date / Server+VPS / CARE Challenge / EAT Research

本轮不建议新增 repo-specific workflow rules。先让 Lite baseline + Verified Workflow 提供通用约束；只有项目特有数据、安全、发布或业务不变量才进入各自 AGENTS。

## 8. AI Skills Maintainer 的作用

`ai-skills-core` 当前“已有规则仍失败时先核实实际调用”的 TODO 方向正确。本轮进一步强调：

- rule text existence != production consumption；
- 检查 installed version、plugin invocation、task entry、current-session loading、generated/source parity；
- active rule 已存在但真实任务违反 -> execution/consumer regression，不再新增同义条目；
- production refinement 最终必须通过真实 installed normal-entry replay。

## 9. Bridge Kit 范围

Bridge Kit 只承担：

1. 分发 Lite baseline；
2. 提供/验证 persistent request-user-input + wait/resume 行为；
3. 把 answerable user wait 与真正 terminal BLOCKED 分开；
4. 等待用户不消耗 retry/repair budget；
5. 保持状态可恢复。

不新增 Control、watcher、ledger、新状态机或“持续提醒 daemon”。用户要求的是 **一个不消失、阻塞依赖链的 prompt**，不是周期性通知。

正式修改前必须用当前 Codex host 做真实 capability probe：确认 request-user-input 是否真的可以 pending 到用户回应，以及外围 runner 是否会因为 turn/stall timeout 把合法 waiting 错误终止。若当前产品能力做不到，应报告 capability gap，再由 Planner/Critic决定最小 fallback。

## 10. Alternatives considered

### 方案 A：把所有规则都塞进 Lite / 每个 AGENTS

拒绝。优点是“到处都能看到”，但会快速变成大手册，挤占 context、重复、腐烂；OpenAI 自身 agent-first repo 经验也明确反对 monolithic AGENTS。

### 方案 B：全部放 workflow-core，AGENTS 几乎不写

也拒绝。plugin 未触发或旧安装时，最基本的“别半成品交用户、需要用户就 persistent prompt、别盲重跑”仍必须存在。

### 方案 C：短 Lite baseline + workflow admission gates + domain plugin 专业规则 + repo-specific invariant

推荐。它让规则在正确层生效，又不把同一套 checklist 复制到所有项目。

## 11. Red-team: 这套方案仍可能怎么失败

- Goal 写了 prompt contract，但实际 host prompt 是 ephemeral；因此必须做真实 capability probe。
- agent 把“pre-human readiness”机械化成每个任务都跑全套 heavy tests；因此 capability gate 必须按 risk/surface 触发。
- agent 为了“都做完”无限开发不敢交付；因此 review admission 看 frozen scope，不允许 scope creep。
- Frontend Design 把“成熟 icon library”变成固定 Lucide/Fluent 宗教；因此 library choice 由项目/platform决定。
- “交互图标应有 feedback”被误写成“所有 icon 都循环动画”；因此 motion 只跟状态/interaction绑定。
- Figma 被当成不可更改圣经；正确逻辑是设计问题先改 Figma、implementation drift 才固定 Figma 修代码。
- producer self-QA 变成同一模型自我吹捧；因此关键视觉/语言/科研质量仍保留独立 review，但只在 producer 完成第一线 QA 之后。
- 已有规则继续不消费；因此 AI Skills Maintainer 要验证 actual invocation/normal entry，而不是只看文件存在。

## 12. 执行顺序（Critic PASS 后）

1. Bridge Kit / Lite：实现短 baseline 与 persistent prompt capability probe/tests。
2. workflow-core：实现 Review Admission、human gate、repeat-failure、evidence/targeted regression 等通用能力，并 production replay。
3. Frontend Design：把当前分散 TODO 收敛为 F1–F5 production gates，真实 Bobbio/Lucerna/Asteria replay。
4. AI Skills Maintainer：验证安装/调用/consumer path。
5. repo-specific：只落必要 invariant：Lucerna provider onboarding；Bobbio design normal entry + AGENTS 去重；Mica live-failure conversion；Asteria优先 consumer replay；SeminarArc 仅在确认 canonical design source 后补 locator。
6. 最后用至少一个非视觉 server/simple task 做 should-not-change，确认没有被强制 Figma/GPT Work/human QA。

## 13. 当前权限边界

本 v5 是 Planner Proposal。允许将本提案和 Critic 审查 prompt 写入 AI_Skills_Collection，并把最新真实证据补入 source-only TODO；不允许在 Critic PASS 前修改 production skill、Bridge Kit template、任何产品 AGENTS 或启动 Codex implementation。