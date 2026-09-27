# Frontend Design Production Consolidation Proposal v0.1

状态：`DRAFT_FOR_INDEPENDENT_CRITIC`  
日期：2026-09-27  
仓库：`YuukiAS/AI_Skills_Collection`  
规划基线：`main@42e5ea84556db32ffb79eee7fa879317f223409b`  
插件：`web-development` / Frontend Design  
当前插件版本：`0.2`  
当前成熟度：`unclassified`  
本轮范围：`#52–#72`，共 21 个 Frontend Design TODO  
明确延期：`#73`、`writing-style #17`、`writing-style #20`；下一阶段再检查 `writing-style #13` 是否为调用/保真前置依赖。  
本文件仅为 Planner Proposal；不修改 production Skill，不修改 Clear Writing，不 bump version，不关闭 TODO，不创建 Executor Goal。

---

## 1. Current reality

### 1.1 当前 source 已经比输入基线更新

用户给出的已知基线 `93e37ab67e9b4369e8d5e32aaea04836166ac14d` 仍是祖先，但规划开始时最新 `main` 已到：

`42e5ea84556db32ffb79eee7fa879317f223409b`

其前序提交已经加入 CUHK Date Product UI Copy naturalness audit，并把 Frontend Design `#73` 与 writing-style copy TODO 链接到该 evidence。因此，本提案按最新 main，而不是按旧聊天或旧摘要规划。

### 1.2 当前 Frontend Design 已有什么

`web-development 0.2` 已有 F-A/F-B/F-C production gates：

- F-A：存在当前 canonical design source 时，把它当 production visual authority，并要求 shipped state/variant/responsive/interaction coverage；
- F-B：要求 component/tokens/typography/icon/motion/localization 等形成一致系统；
- F-C：要求真实 target surface 收敛，设计存在时做整屏比较，并要求 producer 在 external acceptance 前自行发现明显问题。

056 的真实回放证明了一个重要但较窄的能力：面对 canonical Bobbio handoff 时，当前插件不会自己发明缺失 state，也不会把只读 design evidence 冒充已经完成的 product repair。它并没有证明 #52–#72 所代表的整套视觉成熟度已经成立。

### 1.3 当前 topology

当前相关 production skills：

- `frontend-visual-systems`
- `product-ux-planning`
- `visual-direction`
- `design-system-tokens`
- `figma-design-to-code`
- `motion-interaction`
- `responsive-accessibility-review`
- `webapp-testing`
- `implementation-react-tailwind`

当前 Marketplace 的 Frontend Design `visual` aggregate 已包含：

`frontend-visual-systems + visual-direction + design-system-tokens + figma-design-to-code + motion-interaction`

而 `product-ux-planning` 当前只出现在 `research-product-frontend` aggregate；`responsive-accessibility-review`、`webapp-testing`、`implementation-react-tailwind` 不在主要 visual aggregate 中。

### 1.4 外部现实核查

本轮仅采用与设计结论直接相关的官方资料：

1. Figma Code Connect / Dev Mode：官方把 design component 与 production component 的映射定位为连接设计与代码、减少 handoff drift 的机制；这支持“已有 canonical Figma 时应保持 design-code convergence”，但不支持“所有项目必须使用 Figma 或 Code Connect”。  
   - https://developers.figma.com/docs/code-connect/  
   - https://help.figma.com/hc/en-us/articles/15023124644247-Guide-to-Dev-Mode

2. Playwright actionability：真实 click 不只是最终 DOM 状态，还会检查元素可见、稳定、接收事件、启用等条件；这支持 #69 的核心结论——当多个路径都能得到同一最终状态时，只断言最终状态不足以证明目标控件路径。  
   - https://playwright.dev/docs/actionability

3. Tauri 测试文档：mock runtime 不执行 native WebView；Tauri 另外提供 WebDriver/E2E 对实际应用进行测试，并明确区分快速 renderer-only browser mode 与 app binary 测试。这直接支持 #53：browser fixture 不能替代 desktop-native acceptance。  
   - https://v2.tauri.app/develop/tests/  
   - https://v2.tauri.app/develop/tests/webdriver/

采用结论：借鉴这些边界，不把任何特定工具变成强制依赖。

---

## 2. Exact scope

当前 `docs/plugin-todos/web-development.md` 精确包含 tracking `#52–#73`，共 22 个 open candidates。

本轮只处理：

`#52–#72 = 21 TODOs`

本轮不处理：

- `#73 Product UI copy needs an explicit Frontend Design content-architecture contract`
- `writing-style #17 Product UI microcopy should state user consequence, not internal implementation reassurance`
- `writing-style #20 Product UI copy naturalness needs a dedicated microcopy capability`
- 以及任何其它 writing-style TODO。

注意：这里所谓“下一阶段 natural-language/copy 问题”不只是逐句润色。#73 还包含“这个位置是否应该有文字、相邻文字是否重复、页面级 copy rhythm、内容架构与产品语义如何分流”等 Frontend Design 责任。用户已明确要求把这整块留到下一阶段，因此本轮不偷跑。

---

## 3. 21-item adjudication matrix

| TRACKING | TITLE | ROOT_FAILURE_CLASS | GENERICITY | EVIDENCE_STRENGTH | OVERLAPS_WITH | DECISION | TARGET_OWNER | RATIONALE |
|---|---|---|---|---|---|---|---|---|
| #52 | Production icon sourcing and icon-registry discipline | 设计系统资产治理 | 高；具体图库选择是项目局部 | 高：Lucerna 反复暴露，且现有 F-B 已有 icon coherence 但执行边界不足 | #55, #68, #72 | MERGE_INTO_#55 | `design-system-tokens` + `frontend-visual-systems` | icon family、来源、registry、optical alignment、brand/generic 分工都应成为统一 component grammar 的一部分，不新增独立 icon stage。 |
| #53 | Desktop-native acceptance must not be inferred from browser fixtures | 证据 surface 与真实运行环境错配 | 高 | 高：Bobbio/Lucerna + Tauri 官方测试边界 | #56, #69 | PROMOTE | Frontend coordinator + target-runtime QA | 这是独立能力边界：browser renderer 能证明布局/DOM，不足以证明 native shell/WebView/系统集成。 |
| #54 | Motion, hover grammar, and performance budgets belong to the design system | 交互意图与运行时性能混淆 | 高（原则）；固定数值阈值泛化性低 | 中高 | #55 | PROMOTE | `motion-interaction` 负责 motion intent；builder/runtime 负责 latency/performance | 保留“motion 不能掩盖 latency”“交互反馈需统一”；拒绝把 160–220ms、50ms 等数字冻结成通用门槛。性能预算必须按产品/硬件定义。 |
| #55 | Component craftsmanship must be part of the definition of done | component/system grammar 缺失 | 高 | 高：Bobbio + Lucerna 独立复现 | #52, #66, #68, #71, #72 | PROMOTE | `frontend-visual-systems` + `design-system-tokens` | 作为 component craftsmanship 总 contract，吸收 icon、typography、semantic color、status chrome、comparable-card grammar，避免五套并行 checklist。 |
| #56 | External review should confirm quality, not discover obvious local P2 defects | producer self-QA / review admission 缺失 | 高 | 高：Bobbio + Lucerna 都让外部 reviewer/用户成为第一视觉 reviewer | #53, #57, #59 | PROMOTE | Frontend coordinator + producer | external reviewer 应找 blind spot，而不是第一次发现巨大空白、明显矛盾、native path 没跑等 producer 自己可见问题。 |
| #57 | Freeze whole-screen visual direction before implementation polish | 缺少 coding 前的整屏构图冻结 | 高 | 高：Bobbio + Lucerna 独立复现 | #55, #58, #59 | PROMOTE | `product-ux-planning` + `visual-direction` + coordinator | 解决“逐个修组件却始终不像一个产品”。冻结的是 hierarchy/composition/grammar，不是要求每个像素永不改变。 |
| #58 | Canonical design artifacts must gate production implementation | design authority / state coverage 缺失 | 高但条件触发 | 高：Bobbio canonical Figma + 当前 F-A + Figma 官方实践 | #60, #61, #62 | PROMOTE | `figma-design-to-code` + coordinator | 作为唯一 design-authority 总 contract，吸收 round-trip、Figma complete、design-to-code closed loop。没有 canonical Figma 时不触发 Figma 要求。 |
| #59 | Visual acceptance must include a whole-product taste gate, not only defect checklists | checklist 通过但整体仍明显随意 | 高 | 高：Bobbio + Lucerna | #56, #57 | PROMOTE | `visual-direction` + coordinator | 保留独立 final taste gate，但必须用可观察问题判定，不允许只写“要有审美”。 |
| #60 | Design corrections must round-trip through the canonical Figma before code changes | design-source repair 路由不清 | 高但仅 canonical-design 项目 | 高 | #58, #62 | MERGE_INTO_#58 | `figma-design-to-code` | design defect / implementation drift / product-semantic defect / runtime-only defect 四分类应进入同一 authority contract，不再另立规则。 |
| #61 | “Figma complete” needs an explicit definition of done | design source state coverage 假完成 | 高但仅 canonical-Figma 项目 | 高 | #58 | MERGE_INTO_#58 | `figma-design-to-code` | “完成”定义应并入 canonical authority：当前 milestone 的 primary states、variants、responsive、interaction intent、density、自审齐全。 |
| #62 | Design-to-code goals must not stop at either Figma or implementation | design 与 implementation 分阶段假完成 | 高但设计型任务条件触发 | 高 | #58, #56 | MERGE_INTO_#58 | coordinator + `figma-design-to-code` | design freeze → implementation → actual-surface comparison → repair loop 属于一个 convergence contract。 |
| #63 | Normal UI must have a human-readable presentation boundary | runtime/internal state 直接泄露到 normal UI | 高 | 高：Lucerna 多次真实 release evidence | #67, #64, #73 | PROMOTE | `product-ux-planning` + coordinator | 本轮只推广“presentation boundary”：正常 UI 显示用户可理解的状态/动作，raw IDs/debug contract 下沉 details。自然措辞本身仍留给下一阶段 Clear Writing。 |
| #64 | Primary surfaces should optimize for actionability, not implementation completeness | information architecture 被实现完整度主导 | 高 | 高：Lucerna 9/17 与 9/24 独立重复 | #70, #63 | PROMOTE | `product-ux-planning` | primary surface 应按用户当前任务排序，而不是“后端有字段就全部展示”。吸收 configured→status lifecycle。 |
| #65 | Metric labels and rankings must be backed by the data semantics they imply | 视觉标签与真实数据语义不一致 | 高 | 中高：直接真实错误，因果明确 | #63 | PROMOTE | `product-ux-planning` + domain/data owner | Frontend 不负责发明后端聚合，但必须拒绝没有 denominator/scope/order contract 的 `Top`、`highest`、`share`、`remaining` 等强语义标签。 |
| #66 | Comparable resource cards need one coherent progress and reset grammar | sibling component 语义/视觉 grammar 漂移 | 高；具体 quota 文案局部 | 中高 | #55, #72 | MERGE_INTO_#55 | `design-system-tokens` | 同类 resource/status cards 属于 component-family consistency，不需要独立 quota-card 规则。 |
| #67 | Opaque identifiers and formatting artifacts must not leak into glanceable UI | presentation boundary / formatting normalization 缺失 | 高 | 高 | #63 | MERGE_INTO_#63 | `product-ux-planning` + presentation layer | raw ID、negative zero、混乱时区是同一“machine representation 不应直出 primary UI”问题。 |
| #68 | Severity colors must encode one stable semantic meaning | semantic color 漂移 | 高 | 中高 | #55, #72 | MERGE_INTO_#55 | `design-system-tokens` | severity color 是 design-system semantic token 的一部分；不单独建立颜色规则墙。 |
| #69 | Native interaction acceptance must prove the intended control path, not only the final window state | interaction causality / evidence fidelity | 高 | 高：Lucerna false positive + Playwright/Tauri 官方边界 | #53, #56 | MERGE_INTO_#53 | target-runtime QA + coordinator | 扩展 #53：真实 surface 不仅要对，还要在存在竞争路径时证明目标 control/event path，而不是只看最终状态。 |
| #70 | Configured surfaces must collapse from setup mode to status mode | lifecycle-aware progressive disclosure 缺失 | 高 | 高：多个 Lucerna configured surfaces 重复 | #64 | MERGE_INTO_#64 | `product-ux-planning` | setup/configured/recovery 是 lifecycle states；配置完成后 primary surface 应回到 status/action，而非永久停在 admin form。 |
| #71 | Typography governance must define semantic roles and hierarchy, not only token values | token 存在但语义层级缺失 | 高 | 中高 | #55, #57 | MERGE_INTO_#55 | `design-system-tokens` + `visual-direction` | typography role 是 component/system grammar，不另开 typography workflow。 |
| #72 | Status chrome must follow one coherent visual grammar | sibling status chrome 漂移 | 高 | 中高 | #55, #68 | MERGE_INTO_#55 | `design-system-tokens` | pill/border/fill/bare label 应按 semantic role 固定 family，作为 #55 的 status-component 子合同。 |

裁决汇总：

- `PROMOTE = 10`
- `MERGE = 11`
- `DEFER_MORE_EVIDENCE = 0`
- `REJECT_AS_GENERIC_RULE = 0`

这里的 PROMOTE 不等于把十条 TODO 原文复制进 Skill。十个被提升的 tracking 只作为证据锚点；production contract 最终收敛成下面七类 failure taxonomy、五阶段 workflow 和四个 capability gates。

---

## 4. Consolidated failure taxonomy

### T1. Product/state/semantic contract 缺失

覆盖 #63、#64、#65、#70。

问题不是“页面不够漂亮”，而是系统没有先决定：

- 用户此刻要完成什么；
- 哪些状态是 primary；
- 哪些信息应该进 normal surface；
- 哪些是 setup / maintenance / diagnostics；
- metric/ranking/status 标签到底意味着什么。

### T2. Design authority 与 design-source convergence 失效

覆盖 #58、#60、#61、#62。

典型失败：明明有 canonical Figma，却在 code 里发明缺失 state；被拒绝后又直接改 CSS，导致 Figma 与生产两套真值。

### T3. Whole-screen direction 缺失

覆盖 #57。

典型失败：局部按钮越修越精细，但完整屏幕仍然没有 dominant task、合理 density、控制分组和视觉重心。

### T4. Design-system / component grammar 漂移

覆盖 #52、#55、#66、#68、#71、#72。

包括 icon、typography role、spacing、control hierarchy、semantic color、status chrome、同类 resource grammar。目标不是增加 token 数量，而是让正常 production path 真正消费一套语义系统。

### T5. Motion 与 runtime performance 混淆

覆盖 #54。

motion 是状态反馈和连续性的设计意图；latency/jank 是运行时质量。动画不能用来遮住慢，也不能把某个硬件上的数值阈值做成通用设计法则。

### T6. Evidence surface / interaction causality 不可信

覆盖 #53、#69。

browser fixture、static screenshot、native release、interaction recording 各自只能支持相应 claim。native 产品不能用 renderer-only fixture 代替 native acceptance；当多条路径都能产生同一 final state 时，必须证明目标控件路径。

### T7. Producer 没有先完成第一线视觉 QA

覆盖 #56、#59。

producer 必须先看真实 rendered product、清掉明显 P1/P2，并做 whole-product taste review；external reviewer 用于独立发现 blind spot，而不是第一次指出“巨大空白、状态矛盾、控件完全不像一套系统”。

---

## 5. Proposed production workflow

不建立 14 个 stage。建议将 Frontend Design normal production path 收敛为五阶段。

| 阶段 | OWNER | INPUT | OUTPUT | HARD_GATE | WHEN_APPLICABLE | WHEN_SKIPPED |
|---|---|---|---|---|---|---|
| P0 产品与状态合同 | `frontend-visual-systems` 协调；调用 `product-ux-planning` | 用户目标、产品/数据合同、现有页面与状态、当前 milestone | UI task brief；primary-state matrix；actionability/lifecycle 规则；metric/status semantic contract；design-authority locator；任务类型 A–F；evidence plan | 不知道用户任务/状态/数据语义时，不允许用视觉样式掩盖；先确认是否已有 canonical design authority | 所有用户可见 UI 任务；tiny fix 走最小版本 | 纯 backend/docs/nonvisual |
| P1 Design authority + whole-screen freeze | coordinator；`visual-direction`、`design-system-tokens`；按需 `figma-design-to-code`、`motion-interaction`、`responsive-accessibility-review` | P0 contract + canonical design/reference/现有 UI | 当前 milestone 的 whole-screen direction；component grammar；semantic typography/icon/color/status；responsive behavior；motion intent；Figma frames 或非 Figma durable design brief | 大型/设计型实现开始前，不能还需要 builder 自己决定 hierarchy、component family 或 primary-state layout | 新页面、redesign、design-heavy、canonical-Figma | 纯 implementation drift 直接使用已有 frozen authority；tiny fix 只检查受影响 grammar |
| P2 Implementation handoff | coordinator；downstream builder 实现 | frozen state/design target、tokens/components、responsive/motion intent、evidence plan | 可执行 handoff：state→component→token/asset 映射，design constraints，known platform constraints | builder 不得静默改 product semantics、design hierarchy 或 data semantics；发现 design gap 要返回 P0/P1 | 有代码实现的 UI 任务 | 纯 planning/design-only |
| P3 Actual-surface convergence + producer self-QA | producer + coordinator；browser 时可用 `webapp-testing`；native 使用 target-runtime evidence | exact implementation candidate + frozen design | claim-to-evidence matrix；真实 screenshot/recording/state evidence；design/render diff；performance/interaction evidence；producer P1/P2 ledger | exact candidate、正确 surface、primary states 覆盖；明显 P1/P2=0；证据无自相矛盾；native claim 不得只靠 browser fixture | 所有准备 release/user/external review 的 UI candidate | 纯设计稿且本轮不实现 |
| P4 Whole-product taste + external confirmation | coordinator 先做 taste gate；之后才是 independent reviewer | P3 已通过 candidate | whole-product verdict；remaining P3；必要的 design/implementation repair classification | 功能正确仍可因 arbitrary / placeholder-like / visually incoherent / hierarchy confused 而失败；external reviewer 只能在 P3 local gate 通过后进入 | 所有实质 UI candidate；D/E/F 默认完整执行 | tiny/local A/B 可只做受影响 surface 的本地 taste check；无高风险时可不调用 external reviewer |

### Repair loop

P3/P4 发现问题后先分类，而不是“哪里不好看就改哪里”：

1. **design defect**：hierarchy/composition/component family/typography role/semantic color/responsive/motion intent 本身错误 → 回 P1，先改 design authority；
2. **implementation drift**：frozen design 正确但 code 偏离 → 保持 design 不变，修 code，再 P3；
3. **product/interaction semantic defect**：状态、action、metric meaning 错 → 回 P0 更新 product contract，再同步 P1；
4. **runtime-only defect**：race、stale state、integration、性能 bug，而 visual intent 不变 → 直接修 runtime，再做 P3 regression。

---

## 6. Capability gates

本轮不建议再堆十多个新命名 gate。保留并扩展现有 F-A/F-B/F-C，仅新增一个 F-D：

| Gate | Capability / claim | Normal entry | Evidence | Failure | Regression boundary | Final-candidate requirement |
|---|---|---|---|---|---|---|
| F-A | Product/state + design-authority correctness | 普通新页面、redesign、状态变更、canonical design 项目 | task/state matrix、authority locator、data/metric semantics、当前 milestone design coverage | builder 需要自己猜 primary state；有 Figma 却缺 shipped state；UI 标签没有真实语义合同 | 不强迫无 Figma 项目创建 Figma；纯 drift 不重做产品规划 | design-heavy/canonical-design candidate 必须由当前 authority 支持 |
| F-B | Whole-screen + design-system coherence | 实质视觉改动 | full-screen design/render；component families；semantic typography/icon/color/status；responsive/motion intent | sibling controls/status 不像同一系统；arbitrary geometry；placeholder icon；token 有但 hierarchy 乱 | tiny fix 只检查受影响 family；不固定某图库/字体/颜色/动效数字 | final rendered candidate 使用同一 frozen grammar |
| F-C | Actual-surface + evidence fidelity | implementation candidate | browser/native 适配的 screenshot、recording、state trace、design diff、必要性能证据 | browser fixture 冒充 native；截图冒充 click；最终状态冒充目标 control path；旧 candidate 证据拼给新 candidate | browser product 不强迫 native；native renderer-only regression 仍可用 browser 作辅助 | release/user-ready claim 必须来自 exact candidate 的正确 surface |
| F-D | Producer self-QA + whole-product taste + review admission | external reviewer / user acceptance 前 | producer full-screen review、P1/P2 ledger、observable taste questions、evidence completeness | external reviewer/用户第一次发现明显 P2；功能全绿但整屏仍像 placeholder/拼装 UI | tiny fix 不强迫 GPT Work；外部 review 只按风险/里程碑触发 | external/user handoff 前 producer 必须 local P1=0/P2=0 |

---

## 7. Skill topology / ownership

### 7.1 Production coordinator

推荐继续使用现有 `frontend-visual-systems` 作为 Frontend Design production coordinator。

原因：

- 它已经承载 F-A/F-B/F-C；
- 边界已经明确“定义设计系统，不自行实现 app”；
- 已经连接 visual direction、tokens、Figma handoff、motion；
- 这次缺的是 workflow ownership 与 evidence/taste closure，不是缺一个新名字。

因此：

`NEW_ORCHESTRATOR_RECOMMENDED = NO`

### 7.2 `product-ux-planning`

应该进入主要 production aggregate，而不是只作为 `research-product-frontend` 的附属来源。

它负责 P0：产品任务、信息架构、navigation/flow/states、actionability、lifecycle、visible semantic contract。Frontend Design 如果没有这层，后面的视觉系统会继续美化错误的信息架构。

未来实现应避免同一 `product-ux-planning` 在两个 aggregate 中制造模糊触发；优先让 generic planning 归 production coordinator，`research-product-frontend` 保持专业研究产品的附加规划能力。

### 7.3 `responsive-accessibility-review`

应该进入闭环，角色是：

- P1 给出 responsive/accessibility constraints；
- P3 在真实 rendered surface 验证 text fitting、keyboard/focus、contrast、narrow viewport 等。

它不是独立 orchestrator。

### 7.4 `webapp-testing`

它是 production workflow 的**证据工具**，不是设计 owner。

- Web/browser 产品：用于真实浏览器 interaction、state、screenshot、console 等；
- Tauri/Electron/native-WebView：可做 renderer-only 辅助回归，但不能替代 native evidence；
- 不应该因为 Playwright available 就把 every UI task 机械升级为大型 E2E。

未来 packaging 可以让 coordinator 在需要 browser evidence 时能调用/读取它，但其职责必须保持“测试工具”。

### 7.5 `implementation-react-tailwind`

保持 downstream builder，不进入 Frontend Design 的设计所有权。

原因：

- Frontend Design 必须能服务 React/Tailwind 以外的栈；
- Tauri/Electron 也可能使用不同 renderer；
- design coordinator 若把 builder 合并进自身，会重新产生“实现便利性决定视觉方向”的问题。

### 7.6 推荐 aggregate 逻辑

主要 coordinator 应可按需路由：

`product-ux-planning → frontend-visual-systems → visual-direction / design-system-tokens / figma-design-to-code / motion-interaction / responsive-accessibility-review → evidence tool`

其中 `webapp-testing` 是证据 helper；`implementation-react-tailwind` 或项目自有 builder 在 handoff 后执行。

当前 aggregate 不是错误，而是**不完整**：它已有视觉系统核心，但缺 generic product/state planning、responsive/accessibility closure 与明确的 browser/native evidence/review-admission contract。

---

## 8. Figma / design-authority contract

### 8.1 有 canonical Figma 时

Figma 是**视觉设计 source of truth**，不是所有产品事实的 source of truth。

- 产品语义、数据语义、业务约束仍来自相应 product/domain contract；
- Figma 定义当前 milestone 的 visual hierarchy、screen composition、component family、tokens/variables、responsive states、interaction/motion intent；
- code 定义 runtime implementation，但不能静默重新发明 visual/product semantics。

### 8.2 没有 Figma 时

不失败，也不要求补 Figma。

可接受的 design authority 可以是：

- durable screen-level design brief；
- approved reference frames/design board；
- 已接受的 rendered baseline + component/token system；
- 对 tiny fix，现有 production screen + frozen component grammar 即可。

核心要求是：实现前必须有足够明确的设计决策，builder 不需要临场发明 hierarchy/system；不是“必须有某个工具”。

### 8.3 Design freeze

Design freeze 不等于 pixel lock。

它表示当前 milestone 至少已经冻结：

- primary user task；
- shipped primary states；
- whole-screen hierarchy/composition；
- component families；
- semantic typography/icon/color/status roles；
- responsive behavior；
- important interaction/motion intent；
- intentional omissions。

### 8.4 “Figma complete”

只针对当前 milestone，不要求把未来 roadmap 全画完。

必须具备：

- shipped primary-state coverage；
- material component variants/states；
- materially different responsive layouts；
- interaction/motion intent；
- long/dense/error/loading 等会改变布局的代表性内容；
- platform-shell constraint（若 desktop shell 影响 composition）；
- producer design self-review。

### 8.5 Round-trip rule

必须先回 design authority 的变化：

- hierarchy/composition；
- component family；
- typography role；
- spacing rhythm；
- semantic color/status grammar；
- responsive layout；
- interaction/motion intent；
- primary-state content placement；
- product/interaction semantics。

可直接改 code：

- implementation drift；
- runtime/performance bug；
- 在 frozen grammar 内的明显实现错误；
- 不改变设计意图的 accessibility fix；
- 小的 token-consistent visual bug。

如果一个“直接 code fix”实质改变了上述设计决定，它就不再是 direct fix，必须 round-trip。

### 8.6 Final convergence

每个适用的 primary state 用真实 target surface 与对应 design target 比较：

- whole-screen hierarchy；
- component family；
- typography；
- spacing/density；
- semantic color/status；
- responsive state；
- interaction/motion intent。

platform/accessibility constraint 导致合理偏差时可以接受，但必须记录；若偏差成为长期设计事实，应回写 design authority，而不是让两边永久不同。

---

## 9. Visual-system / component / taste contract

### 9.1 Ownership

- `product-ux-planning`：用户任务、actionability、信息优先级、lifecycle、visible data semantics；
- `visual-direction`：whole-screen composition、视觉方向、density/重心、anti-generic judgment；
- `design-system-tokens`：component family、semantic typography、icon、color、status chrome、spacing/radius/surface/state；
- `motion-interaction`：interaction feedback、transition intent、reduced-motion；
- builder/runtime：真实 latency、render performance、state correctness；
- `frontend-visual-systems` coordinator：把这些约束合并并做 final convergence/taste gate。

### 9.2 Component craftsmanship

适用组件必须覆盖其真实需要的状态，而不是强迫所有组件拥有同一固定状态清单。

review 关注：

- 同语义 sibling 是否共享 anatomy/height/padding/radius/icon treatment；
- primary / secondary / destructive / maintenance hierarchy 是否清楚；
- interactive states 是否可辨认；
- status component family 是否由语义决定，而不是由实现历史决定；
- comparable resource/status cards 是否共享同一信息语法；
- icon 是否来自既有/canonical family，brand marks 与 generic controls 是否角色分离；
- 不把临时 emoji、随机圆点、手写 placeholder SVG 留进 production candidate。

### 9.3 Typography / semantic color / status

仅有 token 不算完成。

必须能回答：

- heading / metric / body / label / help / status / diagnostic 各是什么 semantic role；
- 同一 role 在 screen 间是否稳定；
- severity color 是否始终表达同一语义；
- pill/border/fill/bare label 的选择是否有 semantic reason；
- 不得用 warning color 作为普通装饰，又同时用它表示 warning。

### 9.4 Motion vs performance

motion 负责“状态如何被感知”；performance 负责“状态多久真实到达”。

因此：

- input 后实际响应慢，不能用 200ms 动画掩盖；
- hover/press/focus feedback 可以有统一 motion grammar；
- runtime jank 要 profile/render/runtime 修复；
- 不冻结跨项目统一的 p95、long-task 或 animation 数字；
- 每个项目可以基于硬件、交互重要性定义自己的 budget。

### 9.5 Whole-product taste：必须可观察

最终 taste gate 不允许只写“好看”“有审美”。

对每个 primary screen，producer 必须回答：

1. 2–5 秒 first glance 能否看出 dominant task / primary action？
2. 每个高显著性 shape/card/pill/icon 是否有实际语义或交互作用？有没有“只是填空”的装饰？
3. 同级 sibling control/status 是否像同一个产品？
4. typography 是否形成清楚 semantic hierarchy，而不是只满足 token？
5. icon 是否统一、对齐、没有 placeholder feeling？
6. semantic colors 是否一义一致？
7. normal state 是否被 setup/maintenance/diagnostics 抢占？
8. configured state 是否仍像 onboarding/admin form？
9. density 是否过卡片化、过 pill 化、存在无解释巨大空白或局部拥挤？
10. screen 间是否保持同一 component grammar？
11. 如果第一眼觉得“AI-generated/placeholder-like”，能否指出可观察原因：random decoration、generic nested cards、fake metric、arbitrary gradient、组件家族混杂、重复状态、无层级等，而不是只下主观标签？

只要这些问题暴露出明显 P2，即使 tests PASS、按钮能点、没有 overflow，也不能判定 Frontend Design 完成。

---

## 10. Browser/native evidence contract

### 10.1 Evidence classes

**Browser evidence**  
真实 browser runtime 的 DOM/layout/interaction evidence。适合正常 web product；对 desktop native 只能证明 renderer 层。

**Native evidence**  
实际 Tauri/Electron/native-WebView candidate 的真实应用 surface，包括需要时的 titlebar/taskbar/native integration。

**Static screenshot**  
只能证明该时刻的单一 rendered state、layout、visible content；不能证明 click cause、motion、persistence、provider call。

**Interaction recording / trace**  
证明一段真实操作序列、state transition、motion/latency；当 claim 涉及交互过程时优先。

**State evidence**  
明确 candidate identity、precondition、target state 和 capture/trace 对应关系；不能只靠文件名猜。

**Claim-to-evidence mapping**  
每一个 production/review claim 都指向足够强的 evidence class。

### 10.2 Causal interaction proof

当多个事件都能产生相同 final state 时：

- 不接受“window hidden，所以 X button 有效”这类推断；
- 应识别真实 rendered target；
- 用 role/locator/native hit target、受控 precondition、event/handler evidence 或等价方法证明目标 path；
- 坐标脚本只有在目标与竞争路径被排除时才能支持 cause claim。

### 10.3 Producer self-QA

external review 前必须：

- 使用 exact current candidate；
- 看完整正常 scale 的 primary surfaces；
- 覆盖当前 milestone 的关键 state；
- 检查 contradictory state / duplicated state / clipped control / placeholder / raw debug leakage；
- 对交互 claim 使用正确 evidence；
- 记录 producer `P1=0, P2=0`；
- evidence complete。

external reviewer 的任务是独立寻找 blind spot、fidelity/taste regression，而不是第一次发现 producer 同样能看见的问题。

---

## 11. Scale-down rules

| 类型 | 最小要求 | 明确不要求 |
|---|---|---|
| A. tiny visual fix | 确认受影响 component/semantic role；遵守现有 tokens/grammar；看 exact rendered surface；做受影响区域 + 邻近 sibling 的轻量 taste check | 不自动开 Figma；不跑 whole-product external review；不重做 IA |
| B. existing-design implementation drift | 读取既有 authority；确认是 drift 而非 design defect；修 code；比较受影响 primary state；必要 regression | 不重新设计；不改 Figma；除非发现 design source 本身有问题 |
| C. normal browser product design | P0–P4；可无 Figma；需要 durable visual direction、responsive/accessibility、真实 browser evidence、producer self-QA | 不要求 native evidence；不要求 Code Connect；小里程碑不强制 external reviewer |
| D. design-heavy product/redesign | 完整 P0–P4；primary-state coverage；whole-screen freeze；component/system grammar；full taste gate；通常 independent review | 不规定必须 Figma，但必须有足够 durable 的 design authority |
| E. canonical-Figma project | 完整 P0–P4；Figma authority；missing state 先补 design；material visual correction round-trip；full-screen design/render convergence | 不允许 implementation 自行发明新 visual system；但 runtime-only bug 不强制改 Figma |
| F. Tauri/Electron/native-WebView | 在相应 A–E 基础上加入 native evidence；browser 只作辅助；native shell/control claim 证明真实 path；motion-sensitive flow 用 recording/trace | 不允许 browser fixture 冒充 native acceptance；也不要求每个 renderer-only小修都跑完整 shell 大验收 |

规则可叠加，例如 Bobbio = D + E + F；Lucerna 的普通 panel polish 可是 B/F 或 D/F；Asteria 是 C/D 的 browser product。

---

## 12. Real-project replay plan

### Replay 1 — Bobbio：canonical Figma + design-heavy native product

**KNOWN_FAILURE**

- canonical Figma 已存在，但 production 曾直接在 code 中补 state / visual correction；
- local functional/performance green 后仍出现 arbitrary geometry、sibling controls 不一致、重复 CTA、整屏不成系统；
- 用户被迫逐截图做 art direction。

**GENERIC_RULE_BEING_TESTED**

- F-A design authority/state coverage；
- whole-screen freeze；
- #58 authority/round-trip；
- #55 component grammar；
- #59 taste gate；
- #56 producer self-QA；
- native actual-surface convergence。

**PASS_CRITERIA**

- 当前 replay milestone 的 primary states 在 authority 中先覆盖；
- material design correction 不出现 code-only drift；
- exact native candidate 与 design 做整屏 comparison；
- producer 在 external review 前 `P1=0/P2=0`；
- independent reviewer 不再第一次发现明显 component/hierarchy/design-source mismatch。

**PROJECT_SPECIFIC_DETAIL_NOT_TO_GENERALIZE**

- Reading Focus、Reader + Right Inspector、1440×920 尺寸、紫/金色品牌、Zotero/PDF flow、具体 Figma file/node。

### Replay 2 — Lucerna：Tauri/native compact utility

**KNOWN_FAILURE**

- browser/static evidence 曾产生 native false confidence；
- titlebar close 曾因其他 hide route 得到 false positive；
- configured surface 仍长期停留在 setup/admin mode；
- raw runtime identifiers/diagnostics 泄露 primary UI；
- severity/status chrome/typography/component family 不一致；
- producer 没先看完整 panel，用户/GPT reviewer 成为第一线视觉 QA。

**GENERIC_RULE_BEING_TESTED**

- browser/native evidence boundary；
- intended control-path proof；
- presentation boundary；
- actionability/lifecycle；
- component/status/typography grammar；
- producer full-surface self-QA；
- whole-product taste。

**PASS_CRITERIA**

- exact release candidate 的 native evidence 支持 native claims；
- competing hide routes 不再能冒充目标 control path；
- configured healthy state 以 compact status/action 为主；
- diagnostics/raw IDs 下沉；
- sibling status/controls 使用一致 grammar；
- producer 在 external handoff 前完成完整 surface review，零明显 P1/P2。

**PROJECT_SPECIFIC_DETAIL_NOT_TO_GENERALIZE**

- Windows tray、Longleaf/OpenAI/Zotero/Overleaf、具体 screenshot helper、具体绿色/琥珀/红色 palette、hide-to-tray 语义。

### Replay 3 — Asteria：正常 browser product / should-not-overreach

**KNOWN_FAILURE / EXISTING RISK**

Asteria 已经明确要求 build 通过不能替代 browser QA，并有 accepted concepts、real browser mismatch ledger、responsive checks；它不需要 desktop/native/Figma ceremony。它适合作为“这套 Frontend Design 能否在正常 browser 产品上工作而不过重”的独立 replay。

**GENERIC_RULE_BEING_TESTED**

- 无 canonical Figma 时仍能完成；
- accepted visual direction → real browser convergence；
- responsive/accessibility + interaction evidence；
- performance 与 motion 分开；
- scale-down/non-overreach；
- 不把 desktop-native gate 误施加到 browser-only product。

**PASS_CRITERIA**

- 正常 Frontend Design entry 能识别 browser-only surface；
- 使用 accepted concepts/现有 design source，不额外强制 Figma；
- real browser primary states 与 responsive viewport 通过；
- browser evidence 足够时不要求 native smoke；
- coordinator 没有把 React/Tailwind builder 变成 design owner。

**PROJECT_SPECIFIC_DETAIL_NOT_TO_GENERALIZE**

- TRACE/CAT-TRACE semantics、React Flow graph、具体 node/edge relation、A/B/C/D/E1/E2 concept 内容、Asteria 性能 fixture 数量。

### 明确不作为本轮 baseline replay

CUHK Date Product UI Copy naturalness **不**是本轮 Frontend baseline 的完成条件。它留给：

`Frontend #73 + writing-style #17/#20 (+ review #13 prerequisite)`

的下一阶段 cross-plugin replay。

---

## 13. Implementation surface after Critic PASS

本轮不实施。Critic PASS 后，Executor 的最小 implementation surface 应优先复用现有 Skill：

1. `skills/tools/frontend/frontend-visual-systems/SKILL.md`  
   - coordinator workflow；
   - 扩展 F-A/F-B/F-C；
   - 新增 F-D；
   - scale-down / evidence / reviewer admission 总路由。

2. `skills/tools/frontend/product-ux-planning/SKILL.md`  
   - product/state/actionability/lifecycle；
   - normal-vs-diagnostic presentation boundary；
   - metric/ranking visible semantic contract。

3. `skills/tools/frontend/visual-direction/SKILL.md`  
   - whole-screen freeze；
   - observable whole-product taste questions。

4. `skills/tools/frontend/design-system-tokens/SKILL.md`  
   - component craftsmanship；
   - icon source/registry role；
   - semantic typography；
   - semantic severity color；
   - status chrome / sibling grammar。

5. `skills/tools/frontend/figma-design-to-code/SKILL.md`  
   - canonical authority；
   - design freeze / Figma complete；
   - repair classification / round-trip；
   - design-render convergence。

6. `skills/tools/frontend/motion-interaction/SKILL.md`  
   - motion intent 与 runtime performance 边界；
   - 不冻结 universal timing budgets。

7. `skills/tools/frontend/responsive-accessibility-review/SKILL.md`  
   - 进入 production closure。

8. `skills/tools/frontend/webapp-testing/SKILL.md`  
   - 仅在必要处补 claim/evidence 与 browser/native boundary；保持工具身份。

9. `scripts/codex_marketplace_config.json` 与生成的 plugin snapshot  
   - 让主要 aggregate 真实消费 generic product planning 与 responsive/accessibility/evidence capability；
   - 避免 `product-ux-planning` 重复路由造成 ambiguity。

10. tests / replay harness / evidence  
    - 必须有 normal-entry trigger/wiring regression；
    - Bobbio/Lucerna/Asteria 使用真实 production identity/final candidate；
    - browser/native 证据必须匹配 claim。

11. closure docs  
    - README 是显式检查项；如果 Frontend Design 用户入口/描述/能力发生变化，应同步；
    - `docs/PLUGIN_MATURITY.md` 只有真实 replay 达到 baseline 后才允许更新；
    - `docs/plugin-todos/web-development.md` 的 #52–#72 只有在 implementation + replay + Critic closure 后才讨论关闭；
    - 本提案阶段不 bump plugin version；未来若形成正式 user-facing production behavior release，再按 versioning policy 决定版本。

不推荐创建新的 orchestrator Skill。

---

## 14. Regression risks / red team

1. **把 coordinator 变成规则墙**  
   防线：21 TODO 只收敛成 7 类 failure、5 stages、4 gates；source skills 继续各司其职。

2. **任何 UI 改动都被迫跑 Figma + GPT Work**  
   防线：A–F scale-down；tiny fix、pure drift 有明确 fast path；没有 Figma 不失败。

3. **Figma 被当成不可修改圣经**  
   防线：design defect 先改 Figma，implementation drift 才固定 Figma 修 code；product semantics 由 product/domain contract 决定。

4. **Browser QA 再次冒充 native acceptance**  
   防线：claim-to-evidence mapping；Tauri/Electron/native claim 必须实际 native evidence。

5. **native gate 反过来污染 browser-only 项目**  
   防线：Asteria should-not-overreach replay。

6. **Taste gate 变成无限主观返修**  
   防线：只允许用 observable questions 与 P1/P2/P3 consequence；不允许“我觉得不好看”单独当 blocker。

7. **performance 被视觉规则硬编码**  
   防线：design owns motion intent；runtime owns latency；数值 budget 项目化。

8. **icon discipline 变成指定 Fluent/Lucide 宗教**  
   防线：优先项目现有/platform system；固定的是 coherent source/registry，不是固定图库。

9. **#63 偷吃 Clear Writing scope**  
   防线：本轮只处理 normal UI 与 raw/internal data 的 presentation boundary；自然语言 realization、copy rhythm、locale naturalness 留给 #73/#17/#20。

10. **#65 让 Frontend Design 接管 backend analytics**  
    防线：Frontend 只阻止无语义依据的 label；真实 aggregation/denominator 仍由 domain/data owner 定义。

11. **self-QA 变成自我认证**  
    防线：高风险/design-heavy/release 仍保留 independent reviewer，只是 reviewer 在 producer 完成第一线 QA 后进入。

12. **user 再次成为第一视觉 reviewer**  
    防线：P3 producer self-QA + F-D review admission 是硬门槛；user 只在收敛 candidate 后做最终产品判断。

---

## 15. USABLE_FRONTEND_DESIGN_BASELINE

定义如下：

`USABLE_FRONTEND_DESIGN_BASELINE` 成立时，必须同时满足：

1. 正常 UI 项目从用户/产品需求进入后，能先形成 product/state contract，而不是直接写 CSS；
2. 有 canonical design authority 时不会静默漂移；
3. 没有 Figma 时也能用 durable brief/reference/current design system 正常完成；
4. design-heavy work 在 coding 前处理 whole-screen hierarchy/composition；
5. component/typography/icon/color/status/motion grammar 不再临时拼装；
6. metric/ranking/status 强语义不会由前端凭数组顺序或方便字段自行发明；
7. implementation 后会检查真实 rendered surface；
8. Tauri/Electron/native-WebView 不会用 browser fixture 冒充 native acceptance；
9. interaction claim 在存在竞争 route 时能证明 intended path，而不是只证明 final state；
10. producer 会先自行发现明显 P1/P2，external reviewer 不再承担 routine first-line QA；
11. whole-product taste 可以拒绝“功能正确但明显 arbitrary / placeholder-like / visually incoherent”的产品，并能指出可观察原因；
12. scale-down 有效，tiny fix 不被升级成 Figma + external review 大流程；
13. Bobbio、Lucerna、Asteria 三类真实 replay 均由同一 final production candidate/normal entry 通过适用 gate；
14. 用户不需要逐张截图充当第一视觉 reviewer。

### Maturity 决策

当前仍保持：

`web-development = unclassified`

不因本 Proposal、synthetic tests 或未来代码 merge 自动升 status。

当上述 baseline **连同真实 replay** 成立后，建议：

`unclassified -> baseline`

不直接进入 `alpha` 或 `stable`。进入 baseline 的意义是：Frontend Design 已可作为日常真实项目的基础生产路径继续 refinement，但还需要更多长期独立真实项目证明稳定性。

---

## 16. Explicitly deferred cross-plugin phase

`DEFERRED_TO_NEXT_CROSS_PLUGIN_PHASE`

- Frontend Design `#73`
- writing-style `#17`
- writing-style `#20`

下一阶段首先检查：

`writing-style #13`

是否是 prerequisite。

当前判断：**需要检查，但不能预先假定必须先完成 #13 全部 promotion。**

原因：

- #13 定义 Clear Writing 作为通用 content-preserving reader-facing language layer，方向上与 #17/#20 的 production handoff 有直接关系；
- 但 UI microcopy 不能被迫走 heavy long-form rewrite path；
- 下一阶段需要证明的是：当前 Clear Writing packaging/routing 是否已经能提供“短 microcopy + strong fidelity + domain semantics 不漂移”的正常 production entry；
- 若现有入口已足够，#13 可能只是 routing/fidelity dependency，而不需要先完成其所有跨领域 maturity replay；
- 若现有入口无法被 Frontend Design 稳定调用，再把该缺口纳入下一阶段，而不是本轮提前改 Clear Writing。

CUHK Date audit 中 150 条字符串的自然度结果和 page-level copy-rhythm/content-architecture 问题，仅作为下一阶段 evidence。本轮 baseline 不以其修复为成功条件。

---

## 17. Independent Critic prompt

你是 YuukiAS/AI_Skills_Collection 的 Frontend Design 成熟化独立 Critic。

这是 READ-ONLY architecture review。不要实现，不要修改 production Skill，不要 bump version，不要关闭 TODO，不要创建 Executor Goal。

Repository:
`YuukiAS/AI_Skills_Collection`

Review target:
`docs/design/frontend-design/FRONTEND_DESIGN_PRODUCTION_CONSOLIDATION_PROPOSAL_V0_1_2026-09-27.md`

先同步最新 `origin/main`，并实际读取：

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md`
- `docs/PLUGIN_MATURITY.md`
- `docs/plugin-todos/web-development.md`
- 上述 Proposal
- 当前相关 production skills：
  - `frontend-visual-systems`
  - `product-ux-planning`
  - `visual-direction`
  - `design-system-tokens`
  - `figma-design-to-code`
  - `motion-interaction`
  - `responsive-accessibility-review`
  - `webapp-testing`
  - `implementation-react-tailwind`

再独立抽查 Bobbio、Lucerna、Asteria 的真实 evidence，不要只复述 Planner。

你必须独立做针对性外部核查，至少验证：

- Figma design/code handoff / Code Connect 的真实边界；
- Playwright interaction/actionability evidence；
- Tauri browser/mock vs actual app/WebDriver testing 边界。

重点攻击以下问题：

1. Proposal 是否真的逐条覆盖 #52–#72 的 21 个 TODO，是否漏项或重复算数；
2. 10 PROMOTE + 11 MERGE 的裁决是否过重或过简，是否存在应 DEFER/REJECT 的项目特例；
3. 是否把 #52/#66/#68/#71/#72 正确收敛进一个 component/system grammar，而不是仍然形成规则墙；
4. #53/#69 的 native/interaction evidence contract 是否既能防 false positive，又不会把 browser-only 产品变成 native 重流程；
5. #54 是否正确分开 motion intent 与 runtime latency/performance，而没有冻结硬件依赖的 universal budgets；
6. #58/#60/#61/#62 是否真正形成一套一致 Figma/design-authority contract；是否正确允许“无 Figma 也能完成”；
7. product-ux-planning 进入主要 aggregate 是否必要；是否会与 research aggregate 产生重复 trigger；
8. responsive-accessibility-review / webapp-testing / implementation-react-tailwind 的 ownership 是否合理；
9. `frontend-visual-systems` 是否足以作为 coordinator，还是确有证据必须新增 orchestrator；不要因为“更清晰”就新建 Skill；
10. whole-product taste gate 是否有可观察标准，还是仍然主观；
11. producer self-QA 是否能阻止用户/GPT Work成为第一视觉 reviewer，同时仍保留必要独立 review；
12. scale-down A–F 是否足以避免 tiny fix 被迫 Figma + large acceptance；
13. replay 是否覆盖 canonical-Figma native、native utility、normal browser 三种关键类型；
14. Asteria replay 是否真的属于 should-not-overreach，而不是人为多加项目；
15. `USABLE_FRONTEND_DESIGN_BASELINE` 是否只能由真实 normal-entry final-candidate replay证明，而不是 synthetic/CI；
16. Proposal 是否严格 deferred #73 / writing-style #17/#20，并且只把 #13 标为下一阶段 dependency-to-review；
17. 是否存在任何规则会静默把 Product UI Copy naturalness/content-architecture 提前塞进本轮；
18. implementation surface 是否优先复用现有 skills，避免重复 source 和重复 aggregate；
19. README/maturity/TODO closure 是否被正确放在未来 implementation/replay closure，而不是本 Proposal 伪完成；
20. 这套架构是否真实解决 Bobbio/Lucerna 暴露的失败，还是只换了术语。

Critic blocker 必须满足 contract：指出直接证据、因果风险和最小关闭条件；不能因为“再保险”或个人偏好移动终点。

最终只返回：

`RESULT = PASS | REVISE`

若 REVISE：
- 列出真正 blocker；
- 每个 blocker 给最小修改条件；
- 区分 architecture blocker 与 non-blocking note。

若 PASS：
- 明确批准对象为 Proposal v0.1；
- 明确 PASS 仅批准后续 Executor Goal 的架构基础，不等于授权实现；
- 明确 #73 / writing-style #17/#20 仍 deferred；
- 明确当前 web-development maturity 仍为 `unclassified`，直到真实 baseline replay 完成。

---

## 18. Planner conclusion

本轮不是把 21 条 TODO 搬进 Skill，而是把它们压成：

- 7 个真实 failure classes；
- 5 个可执行 production stages；
- 4 个 capability gates；
- 1 个 existing coordinator；
- 0 个新 orchestrator；
- 3 个互补真实 replay。

这套结构覆盖 #52–#72 的所有已知 Frontend Design mature-workflow 缺口，同时明确把 #73 / UI copy naturalness/content architecture 留到下一阶段。

当前仍是 Proposal；只有 independent Critic PASS 后，才允许冻结 Executor implementation Goal。
