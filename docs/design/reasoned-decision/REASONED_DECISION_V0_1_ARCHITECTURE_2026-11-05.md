# Reasoned Decision v0.1 架构候选

Status: design candidate  
Owner: `workflow-core` plugin  
Planned runtime form: one skill inside `workflow-core`, not a standalone skill and not a new Marketplace plugin  
Date: 2026-11-05

## 1. 当前裁决

`Reasoned Decision` 不再按 standalone skill 发展，也不新建第 11 个 Marketplace plugin。

第一版应作为 `workflow-core` 内一个按需触发的 decision skill。它不负责 Windows、统计、医学、法律、产品设计等领域事实，也不替代领域 skill；它负责把领域事实、用户约束和不确定性合成为一个能持续执行的判断，并约束后续改口。

这与 `workflow-core` 已有职责相邻但不重复：

- `workflow-core` 现有 W2 负责“什么时候真需要用户决策”；
- W3 负责“证据能证明到什么程度”；
- W4 负责“同类失败不能无信息重跑”；
- Reasoned Decision 负责“在这些事实和边界下到底选什么，以及下一轮什么时候有资格改变选择”。

它不是新的 workflow/state machine，也不建立新的长期数据库、daemon 或全局 ledger。

## 2. 为什么现在需要它

现有系统已经能阻止很多执行层失败，但仍缺少一层稳定的判断纪律。

真实失败主要有两种相反形式。

第一种是过度保守：证据已经足够，却持续列优缺点、反复说“高度疑似”“不能完全排除”，把真正的选择重新丢给用户。BWG/GFW 历史案例属于这一类。

第二种是过度自信和连续改口：证据不足时先把候选路线说成长期方案；用户指出问题或出现新证据后，模型又从头设计另一套，却没有说明上一轮究竟哪条前提被推翻。2026-11-05 Windows Edge thread 是这一类的高信号负例。

Reasoned Decision 的目标不是保证每次第一次就绝对正确。它要保证：

1. 当前推荐与当前证据相匹配；
2. 不把关键未知藏在“方案已经可行”的语气里；
3. 已经被强证据淘汰的路线不会无理由复活；
4. 后续改口必须有可审计的原因；
5. 用户不用承担替 agent 维护事实、提醒旧结论和检查自相矛盾的工作。

## 3. 触发边界

### 应触发

当任务真正包含“选择”而不是单纯执行时触发，包括：

- 用户直接问“选哪个”“要不要”“以后怎么办”“哪个方案更好”；
- 两个或以上真实可行路线需要取舍；
- 基础设施、迁移、软件/服务、购买、账户路径、工作流或架构策略选择；
- 当前执行被一个非平凡决策阻塞；
- 上一轮已经形成正式建议，而当前轮出现可能导致改判的新事实；
- 用户质疑上一轮正式建议，需要判断“维持还是改判”；
- 一个候选方案要从“理论可行”升级成“值得实施”。

### 不应触发

以下情况不应把简单任务升级成决策流程：

- 纯事实查询；
- 明确 bug 且修复路线已由项目合同冻结；
- 已冻结方案的普通执行；
- 拼写、格式、机械重构等低风险可逆动作；
- 领域 skill 已经给出唯一合法路径，Reasoned Decision 没有真实选择可做；
- 用户只要求解释，不要求选择。

## 4. 核心内部状态

Reasoned Decision 每次只维护一个很小的 Decision Snapshot。默认不把整份状态倒给用户看。

建议字段：

- **Decision question**：这轮真正要决定什么；
- **Success condition**：什么结果才算满足用户目标；
- **Hard constraints**：用户明确不可违反的约束；
- **Verified facts**：本轮已直接观察或由高权威来源确认的事实；
- **Reported evidence**：社区经验、二手报告、未完全验证的现场陈述；
- **Decisive assumptions**：如果它错了，会改变推荐的假设；
- **Eliminated options**：已经因硬约束或更强证据淘汰的路线及原因；
- **Current recommendation**：当前首选；
- **Overturn conditions**：什么新事实或约束会改变首选；
- **Validation gate**：若关键未知可低成本验证，先做什么小验证；
- **Decision delta**：相对上一轮正式建议，新增了什么。

这些字段是推理约束，不是用户可见模板。普通用户只应看到经过压缩的结论。

## 5. 事实、约束和历史的优先级

Reasoned Decision 必须先解决“什么才是当前有效输入”。

优先级：

1. 用户当前消息中的明确要求和纠正；
2. 当前真实系统/项目/文件的直接证据；
3. 当前项目已冻结的有效合同；
4. 当前官方或领域权威来源；
5. 历史对话、旧报告、旧方案；
6. 社区经验和推断。

历史材料不能自动升级成当前硬约束。

如果旧报告写“WebView2 必须自动更新”，但当前用户没有这样要求，则它只能成为待验证的历史设计选择，而不能直接写入新的诊断 Prompt。2026-11-05 Edge thread 正是这类污染的真实失败。

## 6. 证据—主张绑定

关键规则：

> 推荐强度不能高于支撑该推荐的关键证据强度。

每个会改变选择的关键前提都必须知道由什么支撑。最低要求区分：

- **Direct observation**：当前机器、当前文件、当前运行状态直接观察；
- **Project authority**：当前项目正式配置/合同/测试；
- **Primary authority**：官方文档、规范、产品当前行为说明；
- **Reported evidence**：社区或他人现场经验；
- **Inference**：根据已知事实推导，但没有直接证明；
- **Unknown**。

不要求给每句话打标签；只对决定方案生死的前提做绑定。

如果一个关键前提只是 inference，且它错误会完全改变选择，就不能把方案直接包装成“最终长期方案”。此时只有三种合法行为：

1. 找到更强证据；
2. 做一个能真正裁决该前提的有限验证；
3. 如果验证成本明显高于决策代价，明确按当前最优信息做条件性选择。

## 7. 先淘汰，再推荐

Reasoned Decision 不应把所有方案对称展示后交给用户自己合成。

顺序应是：

1. 违反硬约束的路线先删除；
2. 被更强证据直接否定的路线删除；
3. 与已确认现场事实冲突的路线删除；
4. 剩余路线才比较成本、收益、可逆性和风险；
5. 给一个当前首选。

已淘汰路线需要留下最小原因，防止后续模型“重新想一遍”又把它复活。

允许重新打开淘汰路线的原因只有：

- 环境发生实质变化；
- 原证据被证明错误；
- 用户改变硬约束；
- 出现此前不存在的新机制/选项。

## 8. “先查现成方案”放在哪里

不新增 `search-first` 独立 skill，也不让所有任务强制联网搜索。

Reasoned Decision 自己包含一个**按决策类型触发的 prior-art 子流程**。它只在以下情况自动启用：

- 准备新建通用工具、插件、skill、服务、框架、工作流或 reusable helper；
- 正在做 build-vs-adopt / buy-vs-build / dependency choice；
- 当前方案明显可能已有成熟实现；
- 用户问“要不要自己造”。

子流程吸收 `search-first` 的成熟机制：

1. 先查当前仓库已有能力；
2. 再查已安装 plugin/skill/native capability；
3. 再查包注册表、官方产品能力、GitHub/开源实现；
4. 对真正相关候选读实际实现/正式文档，不只看搜索摘要；
5. 最后必须形成一个裁决：**Adopt / Extend / Compose / Build**；
6. 只有当现成候选都命中明确 stop condition 时，才允许 Build。

这只是 Reasoned Decision 在“是否要造东西”时的一段内部参考流程，不形成新的顶级 skill，不让改一个 bug 也被迫跑 prior-art sweep。

如果任务是判断一个项目本身是否新颖、是否有人已经做得更完整，则可借 `prior-art` 的深扫方法；这不是日常默认路径。

## 9. 主动反证

形成首选后，在发送给用户之前必须做一次简短反证：

- 有没有一个已经知道的事实能直接把首选打死；
- 有没有把“当前能工作”误写成“长期可靠”；
- 有没有用弱证据支持强承诺；
- 有没有遗漏一个更简单、可逆、风险更小的路线；
- 有没有把用户明确禁止的东西偷偷带回来；
- 有没有让用户去验证 agent 自己本可以验证的东西。

这不是默认四角色委员会。

只有在以下情况下才调用独立第二视角：

- 决策代价高且难回滚；
- 两条路线都真正站得住；
- 关键证据互相冲突；
- 首选依赖一个高影响、尚未验证的推断；
- 用户明确要求独立反证。

独立第二视角只做一件事：找出足以推翻当前首选的最强事实或逻辑缺口。不要默认产生四份重复意见。

## 10. 改口协议：Reasoned Decision 的核心差异

上一轮已经形成正式建议后，下一轮不得“重新从零思考”然后悄悄换结论。

任何正式改判必须先生成 Decision Delta。

合法改判原因只有四类：

1. **NEW_EVIDENCE**：出现了上一轮没有的新事实；
2. **USER_CONSTRAINT_CHANGE**：用户改变了目标或硬约束；
3. **PREMISE_CORRECTION**：上一轮把某条证据读错、把推断当事实，或发现明确逻辑错误；
4. **OPTION_SET_CHANGE**：出现了上一轮不存在的可行路线，或原路线失效。

注意：不要求“必须有外部新证据才能改口”。模型发现自己上一轮逻辑错误也可以改，但必须指出具体错误：

- 上一轮依赖了哪条错误前提；
- 为什么它现在被判为错误；
- 这如何改变推荐。

以下都不是合法改判理由：

- 用户只是表达不满；
- 模型“重新想了一遍”；
- 换了一个模型或新开一轮；
- 搜到了更多但不改变任何关键前提的材料；
- 想表现得更谨慎或更果断。

如果没有合法 Decision Delta，默认继承上一轮正式建议。

## 11. 推翻条件不是装饰

每个重要推荐应说明什么会让它不再成立。吸收 `headwork` 的 “OVERTURNED IF” 思想，但不强制使用固定英文格式。

好的推翻条件应：

- 是可观察事实，不是“如果情况变化”；
- 真正会改变方案，而不是一般风险；
- 尽量能由 agent 自动检查；
- 不要求用户承担无意义测试。

例如：

> 当前继续使用 A；如果实测发现 X 仍会发生，则 A 被判失败，切到 B。

如果没有近端可见的推翻条件，也可以明确说“除非用户约束或底层环境发生变化，目前没有已知近端条件会改变选择”，不能为了模板硬造。

## 12. 条件性决定与有限验证

不确定性不等于不能决定。

Reasoned Decision 应区分三种情况：

### 可直接决定

证据足够，剩余未知不会改变选择。直接推荐并执行。

### 条件性决定

已经有首选，但一个关键未知如果为假会改变路线，而且这个未知可以低成本验证。

输出应是：

> 当前选 A。唯一可能推翻它的是 X。先做 Y；Y 通过继续 A，失败切 B。

这是一种 bounded experiment，不是摆烂式“需要更多信息”。

### 暂时不能决定

只有在确实缺一个决定性事实、当前 agent 无法获得、而用户也没有授权继续承担风险时才使用。

这是少数情况，不应成为默认安全话术。

## 13. 用户问题的边界

吸收 `headwork` 的原则：

> 能查到的不要问用户。

只有真正属于用户价值判断、授权或不可代理动作的问题才问。

例如：

- “稳定优先还是最新功能优先”可能是用户价值选择；
- “这台机器是不是 Workgroup”必须自己查；
- “仓库里有没有现成实现”必须自己查；
- “哪个策略当前真实生效”必须自己验证。

便宜、容易回滚的小选择由 agent 自己做并说明，不浪费用户一次交互。

## 14. 与领域 skill 的关系

Reasoned Decision 不成为“万能专家”。

领域 skill 负责：

- Windows/Edge 的真实机制；
- 网络/服务器的拓扑与故障事实；
- 统计模型的数学性质；
- 医学/法律/金融等专业事实；
- 项目自己的科学和产品合同。

Reasoned Decision 只消费这些事实并负责：

- 约束对齐；
- 证据权重；
- 方案淘汰；
- 推荐；
- 不确定性处理；
- 推翻条件；
- 改口连续性。

如果领域事实不够，它应路由回领域来源，不应自己脑补。

## 15. 与 workflow-core 现有能力的关系

Reasoned Decision 不复制现有 W2/W3/W4/W5。

它应复用：

- W2 的 HUMAN_ONLY / AGENT_RESOLVABLE 区分；
- W3 的 evidence-surface fidelity；
- W4 的 repeat-failure circuit breaker；
- W5 的 should-not-change / accepted behavior protection。

新增的是：

1. **decision question framing**；
2. **hard-constraint freeze**；
3. **evidence-to-premise binding for recommendation**；
4. **option elimination memory**；
5. **one clear recommendation**；
6. **overturn conditions**；
7. **Decision Delta / change-of-mind audit**；
8. **build-vs-adopt prior-art subflow**。

## 16. 用户可见输出

普通回答不得把 Decision Snapshot 直接打印给用户。

默认应该只有：

1. 当前建议；
2. 最重要的两三个理由；
3. 当前真正会改变结论的未知；
4. 下一步；
5. 必要时一句推翻条件。

例如：

> 我建议继续 A。B 已被当前实测 X 淘汰，C 违反你明确的 Y 约束。现在唯一可能改变选择的是 Z，所以先做一次小验证；Z 通过就继续 A，失败再切 B。除此之外不重新讨论路线。

只有用户要求审计时，才展开完整证据链和 Decision Delta。

## 17. 外部 prior art 的采用结论

### headwork

**Adopt-part。**

吸收：

- 每轮给明确推荐；
- 推荐必须说明什么会推翻；
- 能查的绝不问用户；
- 便宜可逆的决定直接做；
- 只处理当前真正阻塞的决策。

不直接采用：

- 它明确不保存状态，因此不能解决跨轮无依据改口；
- 它偏向一次一个用户问题，不覆盖我们需要的 agent 自主决策和跨轮连续性。

### decision-council-plus

**Adopt-part。**

吸收：

- 先标事实、猜测、用户目标、硬约束；
- 先淘汰违反硬约束的路线；
- 保留 strongest dissent；
- 检查问题框架是否错误；
- 要求 change trigger。

不直接采用：

- 四角色 council 不作为默认路径；
- 多视角不能替代真实证据；
- 默认多代理会增加成本和文字噪音。

### decision-coach

**Adopt-part，非底座。**

吸收：

- pre-mortem；
- reverse course；
- retrospective；
- 高代价决策的 margin-of-safety 思想。

不直接采用：

- “Ask, don't tell” 与本系统目标冲突；
- 它面向人类自我决策 coaching，不适合要求 agent 自己查、自己裁决的技术和基础设施任务。

### search-first

**Adopt-part，作为本 skill 的 conditional prior-art reference，不新增 skill。**

吸收：

- repo first；
- established tool 默认优先；
- Adopt / Extend / Compose / Build 裁决；
- Build 必须说明为何候选都不够；
- 搜索要有停止条件。

不直接采用：

- 不对所有任务强制 prior-art；
- 不让普通 bug fix、事实查询、已冻结执行都先跑搜索；
- 不引入新的独立 search-first skill。

### prior-art

**仅作为深度模式方法参考。**

适用于“我们这个通用能力是否真的新”“现有项目有哪些机制值得移植”这类问题。日常 dependency/tool choice 不需要完整 novelty scan。

## 18. 2026-11-05 Edge 负例暴露出的必测失败

完整证据见：

`docs/design/reasoned-decision/evidence/EDGE_WINDOWS_DECISION_FAILURE_2026-11-05.md`

必须覆盖：

1. 截图/事实识别错误不能在未纠正前扩成方案；
2. 历史报告不能覆盖当前用户约束；
3. 只读调查 Prompt 不得预埋尚未决定的结论；
4. 新实测证据必须立即更新淘汰集合；
5. “能写脚本”不能升级成“长期可靠可实现”；
6. 未公开定义的内部状态不能被过度解释；
7. 用户质疑不能触发无差分改口；
8. 改口时必须指出具体 premise correction；
9. agent 可验证的内容不能转嫁给用户做 regression suite；
10. 连续失败后不能用“再设计一套”“再加一个 reviewer”代替收敛。

## 19. v0.1 回归集

至少包含四类真实案例。

### 正例 A：Claude/Persona KYC

应输出单一首选、证据边界和一次尝试的停止条件，不退化成对称优缺点列表。

### 正例 B：BWG/GFW

证据足够时必须敢于明确判断；用户质疑但没有新证据时不能从一个极端跳到另一个极端。

### 负例 A：Windows Edge 2026-11-05

重点测：

- 当前用户约束能否覆盖旧报告；
- 实测 evidence 能否淘汰理论路线；
- 是否把 candidate 当 production；
- 是否无依据连续改口；
- 是否识别自身 premise correction；
- 是否避免把验证成本甩回用户。

### 对照例：普通低风险选择

例如小型依赖/工具选择。应快速决定，不启动完整 council，不产生长报告，不为了“严谨”阻塞执行。

## 20. 发布前的最低验收

v0.1 不能只靠 prompt review 宣布完成。

至少需要：

1. **trigger positives**：真实策略/迁移/工具选择能自动触发；
2. **trigger negatives**：事实查询、明确 bug、冻结执行不误触发；
3. **constraint preservation**：用户当前硬约束不会被旧历史覆盖；
4. **evidence update**：新强证据到来后淘汰集合真实更新；
5. **no-churn**：无 Decision Delta 时不得改变正式建议；
6. **premise-correction**：发现上一轮逻辑错误时允许改判，但必须指出具体错误；
7. **bounded validation**：关键未知可低成本验证时，输出能裁决方案的小验证，而不是泛化“继续研究”；
8. **prior-art trigger**：build-vs-adopt 类任务自动先查现成能力；
9. **prior-art hard negative**：普通 bug fix 不跑 prior-art；
10. **human output**：最终回答保持短、明确、能执行，不暴露内部状态机。

## 21. 本轮明确不做的事情

本设计阶段不：

- 新建 Marketplace plugin；
- 新建 standalone `reasoned-decision` skill；
- 新建独立 `search-first` skill；
- 默认创建多 agent council；
- 创建隐藏全局 decision database；
- 修改任何 production skill；
- bump plugin/repository version。

下一步应该是独立 Planner/Critic 对本设计做 ownership、trigger、overlap 和回归充分性审查；只有设计通过后，才在 `workflow-core` 内实现对应 skill。
