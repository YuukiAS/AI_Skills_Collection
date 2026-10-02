# Frontend Design Production Consolidation Proposal v0.2

状态：DRAFT_FOR_INDEPENDENT_CRITIC_REREVIEW  
日期：2026-09-27  
仓库：YuukiAS/AI_Skills_Collection  
返修基线：main@98e775485461f15229c16f6d1fd7924fbd6b82a5  
目标插件：web-development / Frontend Design  
当前插件版本：0.2  
当前成熟度：unclassified  
本轮范围：Frontend Design TODO #52–#72，共 21 条  
明确延期：Frontend Design 的 Product UI Copy content-architecture 条目、writing-style #17、writing-style #20；writing-style #13 只保留为下一阶段 dependency-to-review。  
本文件仍然只是 Planner Proposal：不实现、不修改 production Skill、不修改 Clear Writing、不 bump version、不关闭 TODO、不创建 Executor Goal、不推进 release。

---

## 1. Current reality

### 1.1 当前 production 路径已有基础，但还不是可靠的默认 Frontend Design owner

web-development 0.2 已通过 056 建立 F-A/F-B/F-C：

- F-A：存在 canonical design source 时，把它当 production visual authority，并要求 shipped states / variants / responsive / interaction coverage；
- F-B：要求 component、tokens、typography、icon、motion 等形成一致系统；
- F-C：要求 actual target surface 收敛，并在 external acceptance 前由 producer 先做 self-QA。

这些规则方向正确，因此 v0.2 不推倒重来。

真正的缺口是：当前 generated payload 并没有把这些能力组织成 coordinator-first 的正常入口。当前 generated `plugins/codex/plugins/web-development/skills/visual/SKILL.md` 明确要求“从多个 source workflow 中选择一个”，因此 `frontend-visual-systems`、`visual-direction`、`design-system-tokens`、`figma-design-to-code`、`motion-interaction` 仍是平级 choose-one 关系；`product-ux-planning` 又只出现在独立的 `research-product-frontend` aggregate；`responsive-accessibility-review` 与 `webapp-testing` 不在主要 production aggregate 中。

所以当前问题不是“规则完全不存在”，而是三类现实同时存在：

1. 已有规则但入口没真正协调；
2. 有 source skill，但 generated plugin 没把它放进正确闭环；
3. 某些真实 failure 本身仍缺 production contract，例如 native evidence、whole-product taste、handoff action reachability。

### 1.2 v0.1 之后新增的 Lucerna 真实失败进一步证明 self-QA 不能只靠声明

2026-09-27 Lucerna 01052 中，Overleaf 修复已经 test、release build、commit 并 push 到 `85e757c287d4ed571636fbdeff6ba1c9cddb6354`，随后直接要求用户在 Lucerna 中点击 `Choose folder`。用户立即指出：开发方连按钮能不能点、长得是否合适都没有先验收。

随后 producer 才开始补真实交互 QA，并发现：

- 第一次真实点击并没有触发原生文件夹选择器；
- 需要重新抓实际 release 界面、处理 DPI/坐标问题；
- UIAutomation 又没有暴露 WebView 内部控件；
- 最终继续回查前端事件绑定，而不是已经拥有“这个按钮可工作”的 evidence。

这不是新的项目特例，而是 #56 + #69 的直接新增证据：**任何交付给用户的操作步骤，如果 producer 自己可以安全触发到 user-only boundary，就必须在 handoff 前实际验证。** 用户不应该成为第一次发现“按钮根本点不了”或“明显视觉粗糙”的人。

Lucerna 当前 repo 自己已经有很强的 `docs/workflows/LUCERNA_VISUAL_ACCEPTANCE.md` 与 AGENTS visual self-review 规则。因此这次 failure 也说明：仅仅再写一条 repo-local 规则不是解法；Frontend Design production normal entry 必须把 interaction reachability、真实 surface、自审 admission 真正纳入统一闭环。

### 1.3 真实 source 与外部现实

本轮重新核查了当前 main 的 Frontend source、Marketplace config、generated payload、Bobbio/Lucerna/Asteria 项目 contract，以及官方资料：

- Figma Code Connect 的定位是连接设计组件与 production code，使设计与代码共享更准确的组件映射；它支持 design-code convergence，但不意味着所有项目必须使用 Figma。
- Playwright 在真实 click 前会检查元素可见、稳定、能接收事件、启用等；普通 browser interaction 不需要机械增加 handler instrumentation。
- Tauri 明确区分 mock runtime 与真实 app：mock runtime 不执行 native WebView；真实 desktop acceptance 可以通过 WebDriver/E2E 等 target-surface 证据完成。

这些现实支持本 Proposal 的两条边界：**有设计 authority 时不能漂移；没有 Figma 也必须能完成。Browser evidence 证明 browser，native claim 必须有 native evidence。**

---

## 2. 对 Critic findings 的逐项回应

| FINDING | RESPONSE | 依据与 v0.2 修改 |
|---|---|---|
| FD-C01 NORMAL_ENTRY_ORCHESTRATION_UNCLOSED | ACCEPT | 当前 generated visual aggregate 的确是 choose-one source，不是 coordinator-first。v0.2 冻结 `frontend-visual-systems` 为唯一 generic production coordinator；其他设计 skill 只作为按需 delegate。后续 implementation 必须修改 generated routing，而不是只改 source prose。 |
| FD-C02 SCALE_DOWN_AXES_AMBIGUOUS | ACCEPT | A–F 把工作规模、design authority、surface 混成一维分类，确实会让 executor 难判断。v0.2 改为 3 档基础工作规模 + 2 个正交修饰符。 |
| FD-C03 SELF_QA_ADMISSION_UNDEFINED | ACCEPT | 单写 `P1=0/P2=0` 会变成 producer 自签。v0.2 采用 Bobbio 已真实使用的 P1/P2/P3 语义，并要求 verdict 绑定 exact candidate + exact rendered evidence；self-QA 只负责 external-review admission，不代替独立 review。新增 Lucerna 01052 “用户被要求点击一个 producer 尚未验证可用的按钮”作为直接 regression。 |
| FD-C04 TODO_MERGE_LOSSES | ACCEPT | #52、#62、#69 的 maintenance merge 可以保留，但 v0.1 丢了关键 retained semantics。v0.2 明确：merge anchor 不是 sole owner；#52 保留 icon source/registry/provenance；#62 保留无 Figma 也适用的 end-to-end delivery convergence；#69 进入 F-C，browser/native 均适用，只有 competing route 或 control-path claim 才加强 cause proof。 |
| FD-C05 REPLAY_ATTRIBUTION_CONFOUNDED | PARTIAL_ACCEPT | capability attribution 问题完全成立；但 Critic 提到的 `LUCERNA_UI_PRODUCT_SYSTEM_V1` 在当前 Lucerna main 中没有找到对应路径。本轮实际可核实的是 Lucerna AGENTS + `docs/workflows/LUCERNA_VISUAL_ACCEPTANCE.md`，它们已经足够证明 repo-local QA 很强。v0.2 接受 attribution 结论，并按当前真实 locator 重写 replay。 |
| FD-C06 TRACKING_BACKLINK_COLLISION | ACCEPT | 已直接核实 GitHub Issue #73 是 Statistical Modeling 的 “Delegate reader-facing wording without giving away statistical semantics”；`docs/plugin-todos/statistical-modeling.md` 合法使用 `tracking: #73`。Frontend Product UI Copy heading 错误复用了 #73。v0.2 不再用 “Frontend #73” 作为 durable locator，只用 source heading，并给 AI Skills Maintainer exact pending mutation。 |

---

## 3. Exact scope 与延期边界

本轮仍只处理 `docs/plugin-todos/web-development.md` 中 #52–#72 的 21 条 Frontend Design 成熟化 TODO。

下一阶段明确延期：

- source heading：`Product UI copy needs an explicit Frontend Design content-architecture contract`；当前 `tracking: #73` 是错误 locator，必须先由 AI Skills Maintainer 重绑；
- writing-style #17；
- writing-style #20；
- writing-style #13 只在下一阶段检查是否为 routing / fidelity prerequisite。

CUHK Date Product UI Copy naturalness 不属于本轮 completion gate。本轮只允许处理“normal UI 不应泄露 raw implementation state”这种已有 #63 范围，不提前进入文案自然度、页面级 copy rhythm 或跨插件 microcopy 架构。

---

## 4. #52–#72 adjudication matrix

说明：`MERGE_INTO_<tracking>` 只表示 maintenance consolidation anchor，**不表示该 tracking 是唯一 owner**。v0.2 额外写明 retained semantics，防止合并时能力丢失。

| TRACKING | TITLE | ROOT_FAILURE_CLASS | GENERICITY | EVIDENCE_STRENGTH | OVERLAPS_WITH | DECISION | TARGET_OWNER | RETAINED_SEMANTICS / RATIONALE |
|---|---|---|---|---|---|---|---|---|
| #52 | Production icon sourcing and icon-registry discipline | design-system asset governance | 高；具体图库项目化 | 高 | #55,#68,#72 | MERGE_INTO_#55 | design-system-tokens + coordinator | 必须保留：project/platform canonical icon source；central icon registry/component；generic icon vs brand asset；optical normalization；accessibility/theme behavior；third-party source/license/provenance。不是只写“图标统一”。 |
| #53 | Desktop-native acceptance must not be inferred from browser fixtures | evidence surface mismatch | 高 | 高 | #56,#69 | PROMOTE | coordinator + target-runtime QA | Browser renderer 不能替代 native shell/WebView acceptance。 |
| #54 | Motion, hover grammar, and performance budgets belong to the design system | motion intent / runtime latency 混淆 | 高；固定数字低泛化 | 中高 | #55 | PROMOTE | motion-interaction + builder/runtime | motion intent 归 design；真实 latency/jank 归 runtime；Frontend Design 负责 acceptance boundary；不冻结 universal 数字。 |
| #55 | Component craftsmanship must be part of definition of done | system/component grammar 缺失 | 高 | 高 | #52,#66,#68,#71,#72 | PROMOTE | frontend-visual-systems + design-system-tokens | 作为 component/system grammar 总 owner；覆盖 anatomy、states、hierarchy、spacing、semantic roles。 |
| #56 | External review should confirm quality, not discover obvious local P2 defects | producer self-QA / admission 缺失 | 高 | 很高 | #53,#57,#59,#69 | PROMOTE | coordinator + producer | external reviewer 找 blind spot，不负责第一次发现 producer 自己可见、可操作、可复现的问题。 |
| #57 | Freeze whole-screen visual direction before implementation polish | coding 前整屏方向未冻结 | 高 | 高 | #55,#58,#59 | PROMOTE | product-ux-planning + visual-direction + coordinator | 先解决 dominant task、hierarchy、density、grouping，再 coding；不是 pixel lock。 |
| #58 | Canonical design artifacts must gate production implementation | design authority / state coverage | 高；条件触发 | 高 | #60,#61,#62 | PROMOTE | figma-design-to-code + coordinator | canonical Figma 是 visual authority；无 Figma 时使用 durable non-Figma authority。 |
| #59 | Whole-product taste gate | checklist PASS 但整体仍随意 | 高 | 高 | #56,#57 | PROMOTE | visual-direction + coordinator | 用 observable questions 判断 arbitrary / placeholder-like / incoherent，不用主观“审美不够”。 |
| #60 | Design corrections must round-trip through canonical Figma | repair routing | 高；仅 canonical-design 项目 | 高 | #58,#62 | MERGE_INTO_#58 | figma-design-to-code | design defect 回 authority；implementation drift 直接修 code；product semantics 回 P0；runtime-only 直接修 runtime。 |
| #61 | “Figma complete” needs definition of done | design-source 假完成 | 高；仅 Figma 项目 | 高 | #58 | MERGE_INTO_#58 | figma-design-to-code | 当前 milestone 的 primary states、variants、responsive、interaction intent、density、自审齐全。 |
| #62 | Design-to-code goals must not stop at either Figma or implementation | delivery convergence 断裂 | 高；不只 Figma | 高 | #58,#56,#59 | MERGE_INTO_#58 | coordinator + F-A/F-C/F-D closed loop | **保留独立语义**：design authority（Figma 或其他 durable authority）→ implementation → actual surface → producer self-QA → confirmation。#58 只是 tracking anchor，不把 #62 缩成 Figma rule。 |
| #63 | Normal UI must have a human-readable presentation boundary | raw runtime state 泄露 | 高 | 高 | #67,#64 | PROMOTE | product-ux-planning + presentation layer | normal surface 显示用户状态/动作；raw IDs/debug contract 下沉 details。自然措辞仍延期到 Clear Writing phase。 |
| #64 | Primary surfaces should optimize for actionability | IA 被 implementation completeness 主导 | 高 | 高 | #70,#63 | PROMOTE | product-ux-planning | primary surface 按当前用户任务排序；maintenance/setup 按 lifecycle disclosure。 |
| #65 | Metric labels and rankings must match data semantics | visible semantic claim 与数据不一致 | 高 | 中高 | #63 | PROMOTE | product-ux-planning + domain/data owner | Frontend 不发明 aggregation，但必须拒绝无 denominator/scope/order contract 的强语义标签。 |
| #66 | Comparable resource cards need coherent grammar | sibling component grammar 漂移 | 高 | 中高 | #55,#72 | MERGE_INTO_#55 | design-system-tokens | 同类 resource/status card 共用语义结构，不另立 quota-card workflow。 |
| #67 | Opaque identifiers and formatting artifacts must not leak | machine representation 泄露 | 高 | 高 | #63 | MERGE_INTO_#63 | product-ux-planning + presentation layer | human label、zero normalization、date/time convention 属于 normal presentation boundary。 |
| #68 | Severity colors must encode stable meaning | semantic color 漂移 | 高 | 中高 | #55,#72 | MERGE_INTO_#55 | design-system-tokens | severity token 一义一致，不把 warning 色同时当装饰色。 |
| #69 | Native interaction acceptance must prove intended control path | interaction causality / evidence fidelity | 高；browser/native 都适用 | 很高；新增 Lucerna 01052 | #53,#56 | MERGE_INTO_#53 | **F-C evidence fidelity** + target-runtime QA | **保留独立语义**：只在存在 competing route 或明确 control-path claim 时加强 cause proof。普通 Playwright locator/actionability + postcondition 足够，不机械要求 handler instrumentation。 |
| #70 | Configured surfaces must collapse from setup to status | lifecycle disclosure 缺失 | 高 | 高 | #64 | MERGE_INTO_#64 | product-ux-planning | configured/healthy state 回归 status/action；setup/recovery 按需展开。 |
| #71 | Typography governance must define semantic roles | token 有但 hierarchy 缺失 | 高 | 中高 | #55,#57 | MERGE_INTO_#55 | design-system-tokens + visual-direction | typography role 与 whole-screen hierarchy 联动，不另建字体 workflow。 |
| #72 | Status chrome must follow coherent grammar | sibling status chrome 漂移 | 高 | 中高 | #55,#68 | MERGE_INTO_#55 | design-system-tokens | pill/border/fill/bare label 由 semantic role 决定。 |

汇总仍为：

- PROMOTE_COUNT = 10
- MERGE_COUNT = 11
- DEFER_COUNT = 0
- REJECT_COUNT = 0

---

## 5. Consolidated failure taxonomy

最终仍收敛为 7 类，不新增规则墙：

1. **产品任务 / 状态 / 可见语义未冻结**：#63/#64/#65/#70。
2. **design authority 与 implementation 脱节**：#58/#60/#61/#62。
3. **whole-screen visual direction 未在 coding 前解决**：#57。
4. **component / icon / typography / semantic color / status grammar 漂移**：#52/#55/#66/#68/#71/#72。
5. **motion intent 与真实 performance 混淆**：#54。
6. **evidence surface 或 interaction causality 不可信**：#53/#69。
7. **producer 没有完成第一线 visual/interaction QA 就交 external reviewer 或用户**：#56/#59。

新增 Lucerna 01052 不创建第 8 类；它归入第 6+7 类，并成为“handoff action reachability”回归。

---

## 6. Normal-entry orchestration contract

### 6.1 唯一 generic production coordinator

`frontend-visual-systems` 是 Frontend Design 的 production coordinator。

定义“正常 production Frontend Design 入口”为：用户要求设计、重构、视觉返修、界面收敛、Figma-to-code、产品 UI review、release/UI acceptance，而不是显式只调用某个 specialist 工具。

正常入口必须：

1. 先读取 coordinator；
2. coordinator 先判定工作规模、design authority、target surface、product/state risk；
3. coordinator 决定需要哪些 delegate；
4. delegate 结果必须返回 coordinator 做 convergence/admission；
5. specialist 单独运行不能直接产生 `production-ready` / `user-ready` Frontend Design completion claim。

### 6.2 Delegates

coordinator 按需调用：

- `product-ux-planning`：产品任务、信息架构、state、actionability、lifecycle；
- `visual-direction`：whole-screen direction、composition、taste；
- `design-system-tokens`：component grammar、semantic typography/icon/color/status；
- `figma-design-to-code`：canonical Figma authority、handoff、round-trip；
- `motion-interaction`：interaction/motion intent；
- `responsive-accessibility-review`：responsive / accessibility constraints 与 closure；
- `webapp-testing`：narrow browser evidence companion；
- `research-product-frontend`：只有高密度 research product 确有领域 UI 特性时作为 specialist，不再拥有 generic product-ux routing。

`implementation-react-tailwind` 继续是 downstream builder，不是 design owner。若 builder 发现缺 state、需要改变 hierarchy/component grammar、或实现约束会改变产品语义，必须回 P0/P1，不能在 code 里自行决策。

### 6.3 generated payload 必须真正表达 coordinator-first

v0.2 不接受“只在 source skill 加一句 coordinator”的伪修复。当前 aggregate generator 固定生成 choose-one workflow，因此 implementation 必须改变 generated routing。

推荐的最小做法：

- 保留现有 aggregate 机制；
- 给 aggregate generator 增加一个**仅按需启用**的 coordinator-first routing mode；
- web-development 的 main Frontend aggregate 显式指定 `frontend-visual-systems` 为 coordinator source；
- generated `visual/SKILL.md` 必须先读 coordinator，再按 coordinator 决定读取 delegated `_src/*`；
- 没有启用该 mode 的其他 plugin aggregate 保持现有 choose-one 语义不变。

为什么不采用两个更简单的表面方案：

- 只加 `workflow_notes`：不够，因为 generated `## Workflow` 仍明确说 choose-one，语义互相冲突；
- 把所有 delegate 做成平级 top-level copy：会扩大 implicit routing ambiguity，仍不能保证 normal Frontend entry 先 coordinator。

这不是新增 orchestrator Skill，也不是新状态机；是让现有 aggregate 能表达当前已明确需要的 ownership。因为会触及 shared generator / Marketplace，未来 implementation 必须按 Capability Gate Policy 升级为 broad regression，验证其他 aggregates should-not-change。

### 6.4 `product-ux-planning` 的 routing ambiguity

当前 `research-product-frontend` aggregate 同时包含 `product-ux-planning`，会允许 generic UX planning 绕过 coordinator。

v0.2 冻结：

- generic `product-ux-planning` 只由 main Frontend coordinator 委派；
- `research-product-frontend` 只保留 research-product-specific specialist role；
- 普通“设计一个研究产品 UI”仍先进入 coordinator，由 coordinator 再决定是否调用 research specialist。

### 6.5 `webapp-testing`

`webapp-testing` 是 evidence companion，不是 design owner。

它必须在 production plugin payload 中对 coordinator **真实可达**，以便 browser evidence 需要时被调用；但：

- 不拥有 P0/P1 design decision；
- 不因为 Playwright 可用就要求每个 UI task 跑 full E2E；
- Tauri/Electron 任务只能把它当 renderer/browser 辅助 evidence，不能替代 native evidence。

---

## 7. Proposed production workflow

仍保留 P0–P4 五阶段，但允许小任务合并阶段。

| 阶段 | OWNER | INPUT | OUTPUT | HARD GATE |
|---|---|---|---|---|
| P0 产品与状态合同 | coordinator + product-ux-planning | 用户目标、业务/data contract、现有 UI | primary task/state；actionability/lifecycle；metric/status semantics；工作规模；authority/surface 修饰符 | 不知道用户要做什么、state/metric 意义不清时，不允许用视觉层掩盖。 |
| P1 Design authority + whole-screen freeze | coordinator + visual-direction/tokens；按需 Figma/motion/a11y | P0 + canonical/durable design source | whole-screen hierarchy；component grammar；responsive/motion intent；design freeze | design-heavy work 开始 coding 前，builder 不应再需要自己发明 hierarchy/system。 |
| P2 Implementation handoff | coordinator → downstream builder | frozen design decisions | state→component→token/asset/interaction handoff；平台约束 | builder 发现 design gap 必须回 P0/P1。 |
| P3 Actual-surface convergence + producer self-QA | producer + coordinator；按需 webapp-testing/native QA | exact implementation candidate | claim→evidence mapping；render/interaction evidence；design diff；P1/P2/P3 ledger | exact candidate、正确 surface、关键 state/action 实际可达；无 unresolved P1/P2。 |
| P4 Whole-product taste + independent confirmation | coordinator taste gate → independent reviewer when required | P3 PASS candidate | independent verdict / remaining P3 / repair classification | substantive redesign、baseline/release capability gate、重大 design/native milestone 必须 independent review；local fix 可跳过。 |

### Delivery convergence

#62 的 retained contract 是整个闭环：

`P0/P1 authority → P2 implementation → P3 actual surface → F-D admission → P4 confirmation`

这个闭环对 Figma 和非 Figma durable authority 都适用。

---

## 8. Capability gates

### F-A — Product / state / authority

证明：

- user task / primary state / visible semantics 被正确冻结；
- design authority 被发现并按条件使用；
- 有 Figma 时不漂移；无 Figma 时不失败；
- design-heavy coding 前有足够 whole-screen direction。

### F-B — Visual-system coherence

证明：

- component family、typography role、icon source/registry、semantic color、status chrome、spacing/density、responsive/motion grammar 一致；
- #52 的 icon source / registry / provenance 语义完整保留；
- “token 存在”不等于 hierarchy coherent。

### F-C — Actual-surface evidence fidelity

证明：

- browser claim 使用真实 browser evidence；
- native claim 使用真实 native candidate evidence；
- screenshot 只证明静态 state；
- interaction claim 使用能证明该 interaction 的 evidence；
- 普通 Playwright locator/actionability + expected postcondition 通常足够；
- 只有在 competing route、坐标点击、focus-loss、outside-click 等可能产生同一 final state，或 claim 明确是“这个 control 导致了结果”时，才要求额外 cause/path proof；
- 不机械要求 handler instrumentation。

### F-D — Producer self-QA 与 review admission

证明：

- producer 已在 exact rendered candidate 上先完成第一线 QA；
- 用户不会第一次发现 routine P1/P2；
- independent reviewer 进入时面对的是收敛 candidate，而不是 debug checkpoint；
- handoff 中要求用户执行的 UI action，若可以安全预演，producer 已经先验证到 user-only boundary。

---

## 9. Figma / design-authority contract

### 9.1 Authority 层级

Frontend Design 先发现 design authority：

1. canonical Figma；
2. 其他 durable design authority（approved frames/design board/screen-level brief）；
3. 对 targeted fix，可使用当前 production grammar + existing component/token system。

Figma 只拥有 visual design authority，不拥有 business/data/scientific truth。

### 9.2 Design freeze

freeze 的是当前 milestone：

- primary task/state；
- whole-screen hierarchy；
- component family；
- semantic typography/icon/color/status；
- responsive behavior；
- important interaction/motion intent；
- intentional omissions。

不是 2px pixel lock，也不是未来 roadmap 全部完成。

### 9.3 Figma complete

对当前 milestone 必须覆盖：

- shipped primary states；
- material component variants；
- materially different responsive layouts；
- important interaction/motion intent；
- long/dense/error/loading 等会改变布局的 representative content；
- desktop shell constraint（若影响 composition）；
- producer design self-review。

### 9.4 Repair loop

- **design defect**：hierarchy/composition/component grammar/responsive/motion intent 错 → 回 design authority；
- **implementation drift**：authority 正确、code 偏离 → authority 不动，修 code；
- **product semantic defect**：user task/state/metric meaning 错 → 回 P0，再同步 design；
- **runtime-only defect**：race/stale state/integration/performance bug且 visual intent 不变 → 直接修 runtime，再跑 P3。

---

## 10. Visual-system / taste contract

### 10.1 Component/system grammar

#55 吸收相关 tracking，但不丢子语义：

- component anatomy 与 applicable states；
- sibling hierarchy；
- spacing/grouping；
- semantic typography roles；
- icon canonical source / central registry / optical normalization / brand-vs-generic / accessibility / theme / provenance；
- semantic severity color；
- status chrome family；
- comparable resource/status card grammar。

### 10.2 Motion 与 performance

- design 决定 feedback、continuity、transition intent；
- builder/runtime 负责真实 latency、jank、remount、polling、layout cost；
- Frontend Design 在 P3 负责 acceptance boundary：不能把慢响应用动画包装成“感觉流畅”；
- 不冻结 universal p95、long-task 或 animation duration 阈值；
- 项目可以按硬件和交互重要性定义 budget。

### 10.3 Whole-product taste 的可观察问题

对 primary screen 至少回答：

1. 第一眼能否看出 dominant task / primary action？
2. 高显著性 shape/card/pill/icon 是否有语义或交互作用？
3. sibling controls/status 是否像同一系统？
4. typography 是否真正形成 semantic hierarchy？
5. icon 是否统一且没有 placeholder 感？
6. semantic colors 是否一义一致？
7. normal state 是否被 setup/maintenance/diagnostics 抢占？
8. configured state 是否仍像 onboarding/admin form？
9. 是否有 over-carded、over-pill、巨大无解释空白或局部拥挤？
10. screen 间是否保持同一 component grammar？
11. 若一眼像 AI/placeholder，能否指出 random decoration、generic nested cards、fake metric、组件家族混杂、重复状态等可观察原因？

不能只写“审美不好”。

---

## 11. Browser / native evidence contract

### 11.1 Evidence classes

- **Browser evidence**：真实 browser runtime 的布局/DOM/interaction；
- **Native evidence**：实际 Tauri/Electron/native-WebView candidate；
- **Static screenshot**：证明单一 rendered state；
- **Interaction recording/trace**：证明操作序列、状态变化、motion/latency；
- **State evidence**：candidate identity + precondition + target state；
- **Claim-to-evidence mapping**：每个 production claim 对应足够强的 evidence。

### 11.2 Handoff action reachability

新增为 Lucerna 01052 regression：

如果 handoff 明确要求用户点击、选择、展开、保存、授权某个 UI control，则在安全且不需要用户私有决定的范围内，producer 必须先在 exact candidate 验证：

- control 可见；
- control enabled；
- 真实 pointer/keyboard/locator 能触发；
- 到达预期 next state 或 user-only boundary；
- 当前状态下视觉没有明显 P2。

例：文件夹选择要求用户最终选自己的 repo，但 producer 完全可以先打开原生 picker 再取消。若连 picker 都打不开，就不能把“请点击 Choose folder”交给用户。

如果动作本身不可安全预演（例如 destructive confirmation、真实 credential、不可替代的人类选择），producer 只验证到最后一个安全边界，并明确剩余 user-only action。

---

## 12. Producer self-QA / reviewer admission

采用 Bobbio 已实际使用的最小 severity：

- **P1**：阻塞或危及核心用户流程、状态正确性或 evidence truth；不能交用户测试。
- **P2**：正常用户可直接看到的实质困惑、摩擦、视觉/层级/一致性缺陷；应在用户或 independent reviewer 前修掉。
- **P3**：不破坏 acceptance 的 polish，可延期。

### 12.1 Producer verdict 绑定 evidence

producer 不能只写 `P1=0/P2=0`。

至少绑定：

- exact candidate identity；
- exact target surface；
- reviewed primary states；
- screenshot / interaction trace / state evidence；
- 本轮实际发现并修掉的问题；
- remaining P3。

### 12.2 self-QA 的法律地位

self-QA 只证明“可以进入独立 review”，不证明 independent quality。

以下情况强制 independent review：

- substantive redesign；
- baseline / release capability gate；
- major canonical-design convergence milestone；
- major native user-flow milestone；
- 本轮新增/修改会改变 whole-product hierarchy 或关键 interaction model 的工作。

以下情况可以只做 producer self-QA：

- targeted/local fix；
- 已有 frozen design 的明确 implementation drift；
- 不改变 product semantics / hierarchy / component family；
- exact surface regression + neighboring sibling check 已通过；
- 没有新增高风险 native/user flow。

用户职责：

- 最终产品判断；
- 无法推导的偏好；
- 必须由用户完成的私有/授权动作。

用户不负责 routine P1/P2 discovery。

---

## 13. Revised scale-down model

不再使用 A/B/C/D/E/F 六个同级类别。

### 13.1 基础工作规模

**S1 — targeted/local fix**

例如：一个已知 button spacing、icon alignment、token-consistent visual drift。

默认：

- P0/P1 使用已有 product/design grammar；
- P1/P2 可合并；
- P3 exact surface + neighboring sibling check；
- P4 independent review 通常跳过。

**S2 — bounded UI change**

例如：新增一个 panel/state、局部 flow、若干 component family 变化。

默认：

- P0–P3；
- 同一 producer 且 design decision 已冻结时，P1/P2 可作为一次 handoff 完成；
- 是否 P4 independent review 由 hierarchy/native/user-flow 风险决定。

**S3 — product/redesign**

例如：新产品、whole-screen redesign、多个 primary states、design-system 重构。

默认完整 P0–P4，independent review 必须。

### 13.2 正交修饰符

**Design authority**

- canonical Figma；
- other durable authority；
- current production grammar（只适合 S1/部分 S2）。

它只决定 authority/round-trip 要求，不决定任务大小。

**Surface**

- browser；
- native-WebView。

native 只增加与 native claim 相称的 evidence；不把 S1 自动升级成 full redesign ceremony。

### 13.3 Repair classification 仍独立

design defect / implementation drift / product semantic defect / runtime-only defect 只决定 repair loop 回哪里，不再当 scale category。

---

## 14. Real-project replay + capability attribution

继续只用 Bobbio、Lucerna、Asteria，不为了“更保险”现在强行增加第四个项目。

### 14.1 统一 attribution rule

任何 replay 想证明 **Frontend Design plugin capability**，必须同时满足：

1. 使用正式 production plugin identity；
2. 从 normal Frontend Design entry 进入 coordinator；
3. replay prompt 只写真实目标/项目约束，不复述待测 generic rule；
4. 记录 coordinator → delegate 的实际 route/source consumption；
5. project-local contract 已经完整规定的行为，只能算 regression compatibility，不能单独算 plugin 新能力；
6. 对每个要计入 baseline 的 capability，至少观察一个由 Frontend Design normal entry 自己做出的 P0/P1/P3/F-D generic decision；
7. final evidence 来自同一 final candidate。

### 14.2 Bobbio

**已存在的 repo-local contract**

- canonical Figma；
- BLACKBOX_REVIEW_POLICY 的 P1/P2；
- native self-QA。

**因此 replay 主要证明**

- coordinator 能正确发现 canonical Figma，而不复制 prompt rule；
- coordinator 能区分 design defect vs implementation drift；
- generator routing、delegate consumption、Figma round-trip 没有破坏 Bobbio；
- whole-screen/component/taste gate 与既有 repo contract 兼容。

如果所有行为都只是 Bobbio policy 已明文规定，则只能计为 regression compatibility。

### 14.3 Lucerna

**已存在的 repo-local contract**

- `docs/workflows/LUCERNA_VISUAL_ACCEPTANCE.md`；
- AGENTS 的 real release / full-panel / visual self-review 规则。

**新增真实 failure**

01052 在已经 test/build/push 后仍要求用户点击一个尚未被 producer 证明能打开 picker 的按钮。

**因此 replay 重点证明**

- normal coordinator 会主动要求 handoff action reachability；
- browser evidence 不冒充 Tauri/native；
- interaction causality按需增强；
- producer handoff 前先看 exact control 的视觉与实际可操作性；
- 不再让用户第一次发现“按钮点不了”。

如果这些 decision 只是直接复述 Lucerna AGENTS，也不能单独计 plugin capability；必须记录 coordinator 自己的 route/admission decision。

### 14.4 Asteria

Asteria 已有：

- accepted concepts；
- browser mismatch / responsive contract；
- `docs/operations/development/DEVELOPER_VISUAL_SELF_QA_CONTRACT.md`；
- explicit no-Figma default。

因此它最适合作为 should-not-overreach / compatibility replay：

- coordinator 识别 browser surface；
- 不增加 native gate；
- 不因为 S2/S3 自动强迫 Figma；
- 正确复用现有 accepted authority；
- browser evidence route 可达。

Asteria 很可能主要贡献 regression/compatibility evidence，而不是 maturity attribution。

### 14.5 maturity attribution

如果三个 replay 最终都只能证明“没有破坏各 repo 已经写好的规则”，则 implementation/release closure 仍可完成，但：

`web-development maturity = unclassified`

保持不变。

等下一次自然出现、没有同义 repo-local QA contract 的真实 Frontend task，再观察 Frontend Design normal entry 是否独立提供 P0/P1/P3/F-D decision，之后才判断 baseline。

---

## 15. USABLE_FRONTEND_DESIGN_BASELINE

能力定义仍保留，但 maturity 结论比 v0.1 更严格。

一个真正 usable 的 Frontend Design 至少意味着：

1. normal UI request 先进入 coordinator，而不是随机 specialist；
2. coordinator 能识别 task size / authority / surface；
3. 有 canonical design 时不 drift；
4. 无 Figma 也能完成；
5. design-heavy coding 前 whole-screen hierarchy 已冻结；
6. component/icon/typography/color/status/motion grammar 不临时拼；
7. visible metric/ranking 有真实语义合同；
8. implementation 后检查 exact rendered surface；
9. browser-only 不被强迫 native；
10. native claim 不由 browser fixture 代替；
11. competing route 时 interaction claim 能证明 intended path；
12. producer 会先清掉 P1/P2；
13. handoff 给用户的 action 已验证 reachability 到 user-only boundary；
14. whole-product taste 可以用 observable reasons 拒绝 functional-but-placeholder 产品；
15. tiny fix 不跑 full ceremony；
16. 用户不需要逐张截图、逐个按钮充当第一线 QA。

但 maturity 从 `unclassified` 升 `baseline` 还必须满足 attribution：至少一个真实 normal-entry task 的关键能力不是 repo-local contract 预先把答案写给插件。

因此本轮 Proposal 不承诺“三个 replay PASS 后必升 baseline”。

---

## 16. Implementation surface after Critic PASS

仍不实现。若 v0.2 获 Critic PASS，后续 execution package 应覆盖：

1. `frontend-visual-systems`
   - coordinator-first P0–P4；
   - F-A/F-B/F-C/F-D；
   - scale-down；
   - reviewer admission；
   - repair routing。

2. `product-ux-planning`
   - task/state/actionability/lifecycle；
   - visible semantic contract；
   - normal-vs-diagnostic boundary。

3. `visual-direction`
   - whole-screen freeze；
   - observable taste questions。

4. `design-system-tokens`
   - component craftsmanship；
   - #52 icon registry/source/provenance；
   - semantic typography/color/status grammar。

5. `figma-design-to-code`
   - authority；
   - Figma complete；
   - round-trip；
   - final convergence。

6. `motion-interaction`
   - motion intent / latency boundary。

7. `responsive-accessibility-review`
   - P1 constraints + P3 closure。

8. `webapp-testing`
   - narrow browser evidence companion；
   - F-C boundary；
   - 不成为 design owner。

9. Marketplace/generator
   - coordinator-first generated aggregate mode；
   - main Frontend aggregate 改为 coordinator + delegates；
   - generic product-ux 不再由 research aggregate 平级拥有；
   - research-product-frontend 改为 coordinator delegate；
   - generated parity tests；
   - 由于触及 shared generator，必须 broad should-not-change 回归其他 aggregates。

10. `implementation-react-tailwind`
   - 不并入 Frontend Design owner；
   - 只需要 handoff boundary：发现 design gap 回 P0/P1。

11. regression/evidence
   - Bobbio/Lucerna/Asteria；
   - 新增 Lucerna 01052 handoff-action-reachability regression；
   - exact production identity；
   - normal-entry route/source consumption evidence；
   - capability attribution 与 compatibility 分开报告。

12. closure
   - README 显式检查；
   - TODO 只在 implementation/replay/Critic closure 后处理；
   - maturity 独立判断；
   - 版本只按正式 release policy 决定，本 Proposal 不 bump。

---

## 17. Regression risks / red team

1. **coordinator 只是文案，generated payload 仍 choose-one**  
   → F-A normal-entry gate 必须验证真实 generated routing/source consumption。

2. **为 coordinator-first 新增过重 orchestration framework**  
   → 只允许最小 aggregate generation extension，不新增 Skill/state/ledger。

3. **delegate 全部平级暴露导致 routing 反而更乱**  
   → normal generic entry 只认 coordinator；specialist 仅 explicit/narrow use。

4. **S1 tiny fix 也跑 P0–P4 大流程**  
   → 3 档规模 + authority/surface 修饰符；P1/P2 可合并。

5. **self-QA 变成 producer 自签**  
   → exact evidence + P1/P2/P3 + independent review 条件。

6. **每个 click 都要求 event instrumentation**  
   → 只有 competing route/control-path claim 才升级 cause proof。

7. **native gate 污染 browser-only**  
   → surface modifier 独立。

8. **有 Figma 就任何微调都 round-trip**  
   → implementation drift / token-consistent tiny fix 可以直接 code；material design change 才回 authority。

9. **icon rule变成固定图库宗教**  
   → 固定 source/registry/provenance 原则，不固定 Fluent/Lucide。

10. **Lucerna 又把用户当第一交互 tester**  
    → F-D 新增 handoff action reachability；用户 action 前先验证到 safe user-only boundary。

11. **三个强 repo-local contract replay 被误报成 plugin maturity**  
    → attribution rule；必要时 maturity 保持 unclassified。

12. **Product UI Copy 被本轮偷跑**  
    → deferred heading 使用 source title，不使用错误 #73 locator；不改 Clear Writing。

---

## 18. Deferred cross-plugin phase

明确继续延期：

- source heading：`Product UI copy needs an explicit Frontend Design content-architecture contract`；
- writing-style #17；
- writing-style #20。

下一阶段检查 writing-style #13 是否是 routing/fidelity prerequisite，但不预先要求其全部 promotion。

CUHK Date copy-naturalness audit 只作为下一阶段 evidence；本轮不把自然语言修复纳入 Frontend baseline。

---

## 19. Maintenance Board / tracking truth

### 19.1 已核实 collision

GitHub Issue #73 的真实 owner 是：

- Area: statistical-modeling
- Title: `Delegate reader-facing wording without giving away statistical semantics`
- source: `docs/plugin-todos/statistical-modeling.md`
- source locator: `tracking: #73`

Frontend Design source heading：

`Product UI copy needs an explicit Frontend Design content-architecture contract`

当前错误地也写了 `tracking: #73`，这是非法 backlink collision。

### 19.2 本 Planner 当前不直接 mutation

当前 surface 没有 GitHub Project field mutation 能力；同时 Board policy 要求任何 reader-facing Issue/Project copy mutation 前真实调用 Clear Writing。本轮又明确禁止开始 Clear Writing 工作，因此不在这里创建/改写 tracking Issue，不声称已同步。

### 19.3 Exact pending mutation for AI Skills Maintainer

下一次 Project-capable AI Skills Maintainer 必须先：

1. 读取最新 `docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md`；
2. 真实调用当前安装的 Clear Writing，仅用于 reader-facing Issue copy；
3. 保留 Statistical Modeling Issue #73 与其 source backlink 不变；
4. 对 Frontend source heading `Product UI copy needs an explicit Frontend Design content-architecture contract`：
   - 若该条目继续正式进入 central tracking：创建或复用一个**唯一且属于 web-development 的 tracking Issue**，Project Status 保持 TODO，因为本轮明确 deferred；
   - 然后只做 locator-only source edit，把错误 `tracking: #73` 改成真实新 Issue number；
   - 不改变其 `status: NEW`、problem、evidence、candidate_action、promotion_gate；
   - 若 Maintainer 发现它尚不应 admission，则删除错误 locator，而不是复用不相干 #73。
5. 对 #52–#72：
   - 如果 Project Status 仍为 TODO，推进到 DOING；
   - 如果已经 DOING，不重复推进；
   - CURRENT_ANCHOR = `docs/design/frontend-design/FRONTEND_DESIGN_PRODUCTION_CONSOLIDATION_PROPOSAL_V0_2_2026-09-27.md`
   - NEXT_STEP = independent Critic re-review
   - 不关闭任何 TODO；
   - 不设置 Resolution commit。

Project 尚未由本 Planner surface 同步。

---

## 20. Planner conclusion

v0.2 保留 v0.1 的正确主骨架，但关闭 Critic 指出的六个真实缺口：

- normal entry 从平级 choose-one 改成 coordinator-first；
- scale-down 改成“工作规模 + authority/surface 修饰符”；
- self-QA 有明确 P1/P2/P3 admission semantics；
- #52/#62/#69 的关键能力不再因 merge 丢失；
- replay 只在有真实 plugin-originated decision 时计 capability；
- tracking #73 collision 被确认并交给 Maintainer 按真实 issue truth 修复。

新增 Lucerna 01052 进一步把本轮成功标准说清楚：

> Frontend Design 做好之后，正常 UI 任务在交给用户前，开发者必须已经自己看过真实界面、验证过准备让用户点击的控件确实可用，并修掉肉眼可见的 P1/P2。用户不再负责替开发者第一次发现“按钮点不了、界面明显粗糙、状态不对”。

当前仍然只是 Proposal。只有 independent Critic 对 v0.2 PASS 后，Planner 才能准备 execution package。
