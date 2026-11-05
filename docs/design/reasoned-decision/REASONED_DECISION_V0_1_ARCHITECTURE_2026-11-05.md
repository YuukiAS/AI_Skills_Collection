# Reasoned Decision v0.1 插件架构候选

Status: design candidate  
Date: 2026-11-05  
Planned form: dedicated Marketplace plugin with a minimal internal skill set  
Production status: NOT IMPLEMENTED

## 1. 当前架构裁决

Reasoned Decision 应该是一个**独立插件**，不是 standalone skill，也不应该被塞进 `workflow-core` 变成一个内部 skill。

第一版插件只保留两个真正不同职责的 skill：

1. **Judgment Integrity**
   - 负责“到底该怎么判断”；
   - 负责证据强度、约束优先级、方案淘汰、明确推荐、推翻条件，以及跨轮改口审计；
   - 解决“证据够了还不敢下结论”和“没有新依据却一轮一改”这两个相反失败。

2. **Solution Design**
   - 负责“已经知道要解决什么以后，方案该怎么设计”；
   - 负责复用现成能力、方案最小化、关键假设、有限验证、长期可维护性、回滚与实施边界；
   - 解决“没查现成轮子就开始造”“理论可行被包装成生产可靠”“遇到一个缺口就继续叠新层”。

不新增第三个 `search-first` skill，不新增 `decision-continuity` skill，也不新增默认 council skill。

“先查现成方案”是 Solution Design 的一个条件触发参考流程；“跨轮改口审计”是 Judgment Integrity 的核心机制。它们不各自长成新的顶级能力。

## 2. 为什么不能归 workflow-core

`workflow-core` 的职责是复杂任务如何执行、验证和可靠收尾。它已经拥有：

- Human Decision Gate；
- evidence-surface fidelity；
- repeat-failure circuit breaker；
- should-not-change / accepted-behavior protection；
- source discovery、normal entry、least-privilege recovery。

这些能力解决的是“任务怎样做才可靠”。

Reasoned Decision 解决的是不同问题：

> **面对不完整、冲突或层级不同的证据，到底应该相信什么、淘汰什么、推荐什么，以及以后什么时候有资格改变这个判断。**

如果把 Reasoned Decision 塞进 workflow-core，会产生两个问题：

1. workflow-core 会开始承担购买、账户、基础设施策略、产品路线等通用判断，职责过宽；
2. “执行机制”和“判断质量”混在一起，用户以后很难知道一次失败究竟是 domain facts、decision synthesis 还是 execution workflow 的问题。

因此正确协作是：

```text
domain facts / project evidence
        ↓
Reasoned Decision
  Judgment Integrity
        ↓
  Solution Design（需要方案时）
        ↓
workflow-core（需要复杂执行时）
        ↓
writing-style（最后的表达层）
```

Warm Response 可以在用户因连续失败明显受挫时并行触发，但不参与改变技术判断。

## 3. 插件到底负责什么

Reasoned Decision 不承诺“永远第一次就对”。

它承诺的是一种更严格、可持续的判断行为：

- 当前推荐必须与当前证据相匹配；
- 用户当前明确要求不会被旧报告、旧建议或模型偏好覆盖；
- 已被强证据淘汰的路线不会无理由复活；
- 关键未知如果会翻转选择，就必须暴露出来；
- 如果这个未知能低成本验证，就先验证，不先写一整套生产架构；
- 后续改口必须说明到底什么改变了；
- 能自己查、自己验证的事实，不推给用户；
- 搜到很多资料以后，插件必须替用户收敛，而不是把判断重新丢回用户。

Reasoned Decision 的核心产物不是“更多分析”，而是：

> **一个当前可依赖的选择，以及这个选择的有效边界。**

## 4. 两个 skill 的职责边界

### 4.1 Judgment Integrity

这是插件的默认入口和核心。

负责：

- 把用户的问题还原成真正需要决定的问题；
- 区分当前硬约束、历史偏好、项目事实和模型推断；
- 判断证据强度；
- 把决定方案生死的关键前提绑定到证据；
- 淘汰违反硬约束或已被证据否定的路线；
- 在证据足够时给一个明确推荐；
- 在证据不足但存在首选时给“条件性推荐 + 推翻条件”；
- 记录哪些路线已经被淘汰；
- 约束后续改口；
- 在用户质疑时判断是应该维持、补证还是改判，而不是自动摇摆。

它不负责：

- 深入搜索某个专业领域的全部事实；
- 设计具体 Windows/统计/医学/网络实现；
- 执行 Git、部署、配置或代码修改；
- 把输出写得更好看。

### 4.2 Solution Design

只有当问题已经从“该不该/选哪个”进入“怎么做”时才触发。

负责：

- 把 Judgment Integrity 的推荐转成一个最小、可落地的解决方案；
- 先检查是否已有现成实现、原生能力、成熟工具或项目内已有机制；
- 选择 Adopt / Extend / Compose / Build；
- 防止重复造轮子；
- 防止因为一个局部缺口就增加 watcher、daemon、数据库、状态机或新的插件层；
- 区分“理论上可行”“值得试”“已经验证”“可以长期生产使用”；
- 把真正会翻转方案的未知转成有限验证；
- 规定最小回滚和 should-not-change；
- 把方案交给 workflow-core 或领域执行层，而不是自己执行。

它不负责：

- 重新推翻 Judgment Integrity 已冻结的目标和硬约束；
- 没有新证据时重新做一套完全不同的架构；
- 为了“更稳”自动加入第二 reviewer、第三 agent、第四层 orchestrator。

## 5. 插件的主要使用环境

Reasoned Decision 不是只服务一种场景。第一版至少覆盖六类环境，但全部由同两个 skill 处理，不为每类再新增 skill。

### 环境 A：直接选择

用户问：

- “选哪个？”
- “要不要做？”
- “以后还用不用？”
- “A 还是 B？”

主要由 Judgment Integrity 处理。

目标：明确推荐，不退化成对称优缺点列表。

### 环境 B：技术/基础设施策略

例如：

- 是否迁移；
- 更新策略怎么定；
- 长期用主备还是单路；
- 采用哪个远程访问方案。

Judgment Integrity 先冻结目标和淘汰路线；需要具体架构时再进入 Solution Design。

### 环境 C：新建工具 / 插件 / 工作流

这是 prior-art 子流程的主要触发环境。

Solution Design 必须先问：

> “这个能力是不是已经有成熟轮子？”

然后执行 repo → installed capability → native/platform → package/registry → GitHub/open source 的搜索顺序。

没有 prior-art 裁决，不允许直接推荐 Build。

### 环境 D：事故后的方案修复

这次 Edge 就属于这里。

事故环境最容易犯的错是：

- 看到一个症状就急着给长期方案；
- 把旧 workaround 当当前目标；
- 同类失败一再出现还继续扩架构。

这里必须优先：

1. 识别当前事实；
2. 冻结用户当前目标；
3. 标记已经被事实淘汰的路线；
4. 找唯一会改变选择的未知；
5. 先做小验证，再决定长期方案。

### 环境 E：跨轮重新判断

用户可能说：

- “你上次不是说 A 吗？”
- “现在还这么看吗？”
- “你为什么改口？”
- “我给你新证据了。”

Judgment Integrity 必须进入 Decision Delta 模式，不允许从零开始重新生成答案。

### 环境 F：已有方案的生产升级

例如：

- “这个候选可以正式长期用了吗？”
- “可以部署到另一台机器了吗？”
- “能不能从实验变成默认？”

这里的关键不是继续设计，而是判断“证据是否足以把 candidate 升级成 production”。

## 6. 不应触发的环境

为了防止插件变成所有任务都套一层，以下默认不触发：

- 单纯事实查询；
- 明确 bug 且项目合同已冻结修复路线；
- 已冻结方案的机械执行；
- 格式、拼写、简单重命名；
- 用户只要求解释某段材料；
- 领域事实本身有唯一明确答案，不存在真实选择；
- 低成本、可逆、明显无需比较的小动作。

一个很重要的原则：

> **不是所有“怎么做”都需要 Reasoned Decision。**

只有当“选择错路线”的代价明显高于直接执行时才需要。

## 7. Decision Anchor：跨轮连续性的最小状态

Reasoned Decision 不建立新的隐藏全局数据库。

它只维护一个很小的 **Decision Anchor**，可以从当前对话、项目已有 decision/plan/handoff 或当前任务材料中恢复。

Anchor 只包含：

- 这次真正的 decision question；
- 当前 success condition；
- 当前用户硬约束；
- 决定性的已验证事实；
- 决定性的未验证假设；
- 已淘汰路线及淘汰原因；
- 当前推荐；
- 推翻条件；
- 如果需要，当前有限验证。

普通短对话不需要把 Anchor 写进文件。

只有当一个决定会跨 session、影响真实项目或长期基础设施时，才复用项目现有的 decision/plan/handoff 文档保存；不新建一个 Reasoned Decision 专属 ledger。

## 8. 约束优先级

这次 Edge 事故证明，历史内容污染是高风险失败。

默认优先级：

1. 用户当前消息中的明确要求和纠正；
2. 当前真实系统 / 当前项目直接证据；
3. 当前项目明确冻结的合同；
4. 当前官方 / 权威来源；
5. 旧聊天、旧 handoff、旧方案；
6. 社区经验；
7. 模型推断。

旧报告里出现过的选择，不能自动变成当前硬约束。

如果历史写“WebView2 自动更新”，而当前用户没有这样要求，它只能进入“历史设计选择”，不能写成“用户明确要求”。

## 9. 证据与结论强度

Judgment Integrity 必须遵守：

> **结论强度不能高于支撑它的关键证据强度。**

对决定方案生死的关键前提，至少区分：

- 当前直接观察；
- 当前项目权威事实；
- 官方/规范明确保证；
- 官方有限支持 / 有适用条件；
- 社区/真实用户经验；
- 合理推断；
- 未知。

不要求把这些机器标签全部展示给用户。

但如果一个关键前提只是“推断”，而它一旦错了就会让整个方案失效，那么不能把方案叫“稳定长期方案”。

此时只能：

- 补更强证据；
- 做一个真正会裁决它的小实验；
- 或明确给条件性推荐。

## 10. 方案状态：防止 candidate 冒充 production

这次 Edge 最严重的错误之一就是“能写脚本”被说成“能长期稳定做到”。

Reasoned Decision 内部至少区分：

1. **Idea**
   - 只是一个可能方向。

2. **Candidate**
   - 与已知事实不冲突，值得验证。

3. **Conditionally Recommended**
   - 当前首选，但有一个明确关键未知。

4. **Recommended**
   - 当前证据足够支持采取行动。

5. **Production-worthy**
   - 已完成与风险匹配的真实验证，可以长期默认使用。

从 Candidate 到 Production-worthy 不能靠语言升级。

必须有新证据。

## 11. 先淘汰，再比较

Judgment Integrity 不应该把所有路线平铺给用户自己选。

正确顺序：

1. 违反用户硬约束 → 淘汰；
2. 被现场事实直接否定 → 淘汰；
3. 官方适用范围明显不覆盖当前环境，而又无真实证据补强 → 不得作为主方案；
4. 与项目现有成熟能力重复且无新增价值 → 淘汰；
5. 剩余方案才比较成本、可逆性、维护负担和风险。

淘汰路线要保留最小原因。

以后除非出现以下情况，否则不能复活：

- 环境实质变化；
- 原证据被证伪；
- 用户改变硬约束；
- 出现新的机制级证据。

## 12. 主动反证，但不默认多 agent

形成首选后必须做一次轻量反证：

- 有没有现成事实能直接打死它；
- 有没有已被淘汰的路线偷偷复活；
- 有没有更简单路线；
- 有没有“当前可行”冒充“长期可靠”；
- 有没有把用户明确禁止的东西重新带回来；
- 有没有把 agent 自己能验证的事情推给用户。

默认单模型完成。

只有在以下情况才请求独立第二视角：

- 决策高代价且难回滚；
- 两个方案都真正成立；
- 关键证据冲突；
- 当前首选依赖一个高影响推断；
- 用户明确要求独立判断。

第二视角的任务不是“重新设计”，而是：

> **找出当前首选最可能被推翻的点。**

## 13. Decision Delta：改口协议

这是 Judgment Integrity 的核心。

上一轮已经正式推荐 A，下一轮不得重新从零设计然后直接给 B。

每次改判必须归入四类之一：

1. **新证据**
2. **用户约束变化**
3. **前提/逻辑纠错**
4. **选项集合变化**

前提/逻辑纠错非常重要。

不要求必须有外部新证据才能改口。

如果模型发现自己上一轮把未知值解释成了某个具体语义，它可以改，但必须明确：

- 上一轮用了哪条错误前提；
- 为什么现在认为它错；
- 它推翻了哪部分结论；
- 新推荐为什么因此改变。

以下不是合法改口原因：

- 用户只是质疑；
- 用户变生气；
- 模型换了；
- “重新想了一遍”；
- 搜到更多背景但没有改变关键前提。

如果没有合法 Decision Delta，默认继承上一轮推荐。

## 14. 推翻条件

吸收 headwork 最值得借的一点：

> 每个重要推荐都应该知道“什么事实会让我改变选择”。

推翻条件必须：

- 可观察；
- 真正会改变路线；
- 尽量能由 agent 自己检查；
- 不是泛泛的“如果情况变化”。

例如：

> 当前推荐 A；如果实测出现 X，则 A 失败，切 B。

推翻条件不是为了显得谨慎，而是为了约束未来改口。

## 15. 有限验证

当一个关键未知真的会翻转选择，而且可以低成本验证时：

**不要再写第五套完整方案。**

输出应该变成：

> 当前首选 A。唯一会推翻它的是 X。先验证 Y；Y 通过继续 A，失败切 B。

有限验证必须：

- 能裁决一个具体关键前提；
- 成本明显低于完整实施；
- 不主动破坏健康系统；
- 不把用户当 regression suite；
- 不继续扩大 scope。

## 16. Solution Design 的 prior-art 子流程

“先查轮子”不独立成 skill。

它只在以下任务触发：

- 新建插件 / skill / 通用工具 / 服务 / 工作流；
- 引入新依赖；
- build-vs-buy / build-vs-adopt；
- 新建 reusable wrapper / agent infrastructure；
- 用户问“我们是不是要自己造”。

搜索顺序：

1. 当前仓库是否已经有；
2. 当前已安装 plugin / skill / native capability 是否已有；
3. 平台/框架官方是否已经提供；
4. 包注册表 / MCP / 常见生态；
5. 维护中的开源实现；
6. 必要时 deep prior-art scan。

最终必须形成一个四选一：

- **Adopt**：直接采用；
- **Extend**：以一个现有方案为底座扩展；
- **Compose**：组合现有能力；
- **Build**：现有方案都不满足。

Build 必须写清：

- 哪些现成候选被看过；
- 每个为什么不够；
- 自建真正新增的价值是什么；
- 以后维护成本是什么。

没有这些，不允许 Build。

## 17. 外部轮子的采用位置

### headwork → Judgment Integrity

采用：

- 明确推荐优先；
- 不把菜单重新丢给用户；
- “能查的不要问”；
- 推翻条件；
- 小而可逆的决定不要浪费用户一次交互。

不直接采用它的无状态设计。

### decision-council-plus → Judgment Integrity 的可选反证参考

采用：

- 硬约束过滤；
- premise check；
- strongest dissent；
- change trigger。

不默认四角色 council。

### decision-coach → 两个 skill 的参考

Judgment Integrity 借：

- reverse course；
- retrospective；
- confidence/assumption probing。

Solution Design 借：

- pre-mortem；
- margin of safety；
- implementation intention。

不采用“Ask, don't tell”作为默认交互。

### search-first → Solution Design 的 prior-art reference

采用：

- repo first；
- adopt by default；
- 搜索实际实现/官方资料；
- 必须有 reuse/build 裁决；
- Build 需要 stop condition。

不独立成 skill。

### prior-art → Solution Design 的深度模式参考

只用于：

- 插件/产品/通用能力是否真的新；
- 哪些已有机制值得移植；
- novelty / differentiation 判断。

不用于普通 bug 或小型依赖选择。

## 18. Edge 41 页真实负例对插件提出的要求

完整负例：

`docs/design/reasoned-decision/evidence/EDGE_WINDOWS_DECISION_FAILURE_2026-11-05.md`

它不是“Edge 知识不足”的案例，而是插件必须防住的完整 failure chain：

1. 证据对象识别错；
2. 旧报告污染当前硬约束；
3. 诊断 Prompt 把未决定的结论写成用户要求；
4. 新现场证据没有立即淘汰旧路线；
5. Candidate 被包装成 production；
6. 未知内部值被过度解释；
7. 用户一质疑就重新设计；
8. 改口没有 Decision Delta；
9. agent 可做的验证被推给用户；
10. 连续失败后继续新增 reviewer / guardian / 流程，而不是收缩问题。

PDF 里的关键历史事实必须作为真实 replay 输入，而不是只写一句摘要。

## 19. Edge 负例要求的行为变化

### 19.1 事实识别错误

如果截图/日志本身还有歧义，而且这个歧义会改变整个问题定义：

- 先解决对象识别；
- 不基于猜测扩成方案。

### 19.2 当前约束覆盖历史

用户当前没说 WebView2 必须自动更新，就不能因为旧报告里写过而继续把它当硬约束。

### 19.3 调查必须保持中立

调查 Prompt 不允许把“待判断问题”写成“用户明确要求”。

### 19.4 新证据必须改变淘汰集合

一旦实测证明某策略在当前环境被忽略，依赖该机制的主方案应被淘汰，除非后来出现真正的新机制证据。

### 19.5 未知就是未知

没有公开语义的内部值，不能为了给出“完整原因”而强行命名。

### 19.6 用户质疑不是改口证据

“你想清楚”应该触发内部反证，不应该自动产生另一套架构。

### 19.7 连续失败后收缩

如果已经出现两次以上同类改口：

- 停止继续扩方案；
- 回到 Decision Anchor；
- 列出现已确认事实、已淘汰路线、唯一关键未知；
- 只做一次最小裁决动作。

## 20. 与 workflow-core 的接口

Reasoned Decision 输出给 workflow-core 的不是完整思维过程，而是一个小合同：

- 当前目标；
- 当前硬约束；
- 推荐路线；
- 不允许重新打开的已淘汰路线；
- 必须验证的关键假设；
- 推翻条件；
- should-not-change。

workflow-core 负责：

- 执行；
- 验证；
- 失败后回到正确 owner；
- 不越权改决策。

如果执行阶段发现满足推翻条件的新证据，返回 Judgment Integrity 重新裁决，而不是 executor 自己改架构。

## 21. 与 writing-style 的接口

Reasoned Decision 决定：

> “到底应该告诉用户什么判断。”

writing-style 决定：

> “怎样把这个已经正确的判断讲得清楚、自然、少英文、少碎片。”

writing-style 不能为了语气更果断而改变不确定性；
Reasoned Decision 也不能把一整份 Decision Anchor 倒给用户，然后让 writing-style 帮忙压缩成“看起来像人话”。

## 22. 与 Warm Response 的接口

当用户因为模型连续失败而明显愤怒：

- Warm Response 负责自然承认具体负担；
- Reasoned Decision 负责立即恢复正确的目标、事实和当前选择。

不能只道歉不继续做事；
也不能只技术复盘，完全不回应用户为什么已经被折腾得很烦。

## 23. 用户可见输出

默认不展示内部框架。

普通回答应该像：

> 我建议 A。B 已被 X 这条事实淘汰，C 违反你明确的 Y 约束。现在唯一会改变结论的是 Z，所以先做一次小验证；通过就继续 A，失败再切 B。除此之外不重新讨论路线。

如果证据已经足够：

> 我建议 A。关键原因是 X 和 Y，B 已经不成立。现在直接做下一步 N。

如果发生改口：

> 我上一轮推荐 A。现在改成 B，不是因为重新想了一遍，而是新证据 X 证明上一轮依赖的前提 Y 不成立；因此 A 被淘汰。

只有用户要求审计时，才展开完整证据链。

## 24. 插件自身的回归集

第一版至少使用五类真实 replay。

### A. Claude/Persona KYC 正例

必须：

- 给一个首选；
- 区分官方要求与社区经验；
- 给一次尝试的 stop condition；
- 不把三个选项重新丢给用户。

### B. BWG/GFW 正例/负例

必须：

- 证据够时敢于明确判断；
- 用户质疑但没有新证据时不从一个极端跳另一个极端；
- 不重复讨论已经完成的动作。

### C. Windows Edge 2026-11-05 主负例

必须覆盖：

- 当前约束优先；
- investigation neutrality；
- evidence-driven elimination；
- candidate/production distinction；
- unknown value discipline；
- Decision Delta；
- human-time budget；
- repeated-failure contraction；
- prior-art reflex。

### D. Build-vs-adopt 自举测试

给模型一个“做新的 decision skill”的任务。

预期：

- 自动找到 headwork / council / coach / search-first / prior-art 等现成实现；
- 先决定 Adopt / Extend / Compose / Build；
- 不直接从零设计。

这个 replay 直接防止 Reasoned Decision 自己重复本次“先造轮子后搜索”的错误。

### E. 低风险 hard negative

例如一个明确的小 bug 或机械配置修改。

预期：

- Reasoned Decision 不触发；
- 不做 council；
- 不跑 prior-art sweep；
- 不制造额外文档。

## 25. 第一版发布门槛

Reasoned Decision v0.1 不能只靠设计文档通过。

至少证明：

1. 正确触发非平凡选择；
2. 不误触发普通执行；
3. 当前用户约束不会被旧历史覆盖；
4. 新证据会更新淘汰集合；
5. 没有合法 Decision Delta 时不会改正式推荐；
6. 自我纠错可以发生，但必须说清 premise correction；
7. 关键未知会被转成 bounded validation，而不是无限研究；
8. build-vs-adopt 会自动走 prior-art 子流程；
9. user-facing 输出不是审计日志；
10. Edge 完整负例 replay 不再复现“连续五套方案”行为。

## 26. 明确不做

第一版不做：

- 第三个核心 skill；
- 独立 search-first skill；
- 独立 decision journal 服务；
- 全局隐藏 decision database；
- 默认多 agent council；
- 独立 reviewer plugin；
- 把 workflow-core 复制一遍；
- 把 domain facts 搬进 Reasoned Decision；
- 每个问题都生成 Markdown 决策记录。

## 27. 下一步

下一步不是继续扩架构，而是对这份插件设计做一次独立架构审查，重点只问：

1. `Judgment Integrity` 与 `Solution Design` 是否已经覆盖所有必要职责，有没有真正需要第三个 skill；
2. Reasoned Decision 与 workflow-core / writing-style / domain plugin 的边界是否清楚；
3. Edge 负例是否足够严格，能不能真实阻止无依据改口；
4. prior-art 子流程是否会误触发太多普通任务；
5. Decision Anchor 是否足够轻，不会演变成新的状态系统。

只有这五点通过，才进入实现。
