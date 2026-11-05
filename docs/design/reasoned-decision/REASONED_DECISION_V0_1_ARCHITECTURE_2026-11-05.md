# Reasoned Decision v0.1 架构收敛稿

Status: DESIGN_CONVERGED_FOR_REVIEW  
Date: 2026-11-05  
Planned form: dedicated Marketplace plugin  
Production status: NOT IMPLEMENTED  
Authority: 本文件是下一阶段实现与审查的权威设计入口；同日更早草稿中与本文冲突的表述，以本文为准。

## 1. 冻结结论

Reasoned Decision 的历史三层候选架构恢复并冻结为：

```text
Task State Integrity
        ↓
Judgment Integrity
        ↓
Solution Design
```

这三层是**职责架构**，不是要求模型严格只走一遍的流水线。

它们分别解决：

- **Task State Integrity**：保证没有答错题、忘掉当前状态或复活已关闭问题；
- **Judgment Integrity**：保证证据、淘汰、推荐和改口有稳定依据；
- **Solution Design**：保证方案建立在现实已有解法上，优先采用、组合、扩展，只有真实缺口才自建。

必须明确区分以下三个概念，后续不得再混淆：

1. `Task State Integrity → Judgment Integrity → Solution Design`：Reasoned Decision 自身的三层职责架构；
2. Judgment Integrity 内部“什么可以改变 / 先核证据再改判 / 允许保持未知”的判断原则；
3. `Reasoned Decision → Design Assurance → Delivery Assurance`：更大的跨插件可靠性生命周期。

它们不是同一个“三层”。

### 1.1 插件内部怎么落

第一版仍保持最小内部 skill 数量：

- **Task State Integrity** 是 Reasoned Decision 的强制入口层和状态合同，不单独长成一个新 skill；
- **Judgment Integrity** 是判断 skill；
- **Solution Design** 是方案 skill。

因此：

- 不新增独立 `search-first` skill；
- 不新增 `decision-continuity` skill；
- 不新增默认 council skill；
- 不新增 Reasoned Decision 专属隐藏数据库或长期守护进程。

复杂多轮架构收敛、独立盲区调查和 Architecture Freeze 仍属于 **Design Assurance**；冻结后的真实交付、防降级和防回归仍属于 **Delivery Assurance**。

---

## 2. Reasoned Decision 的核心行为

Reasoned Decision 不应该被理解为：

> 模型理解问题以后，自己设计一套解决方案。

正确行为是：

> **先弄清楚用户真正要解决什么和当前已经有什么；再调查现实世界已经存在的解法、成熟案例和失败经验；从真实解空间里形成候选并判断；优先采用、组合、扩展现成方案；只有明确证明仍有残余缺口，才自己设计那一小块。**

因此第一版的核心不是“让 GPT 更会设计”，而是让 GPT **更晚设计、更少自建、更稳定地沿用已经成立的判断**。

---

## 3. 实际运行主干：采用“正常人解决问题”的顺序

三层是职责边界；实际运行采用下面这条主干：

```text
搞清目标和现状
    ↓
调查现实已有解空间
    ↓
从真实案例归纳成熟路线
    ↓
判断哪些路线真正适合
    ↓
优先 Adopt / Compose / Extend
    ↓
证明仍有残余缺口才 Build
    ↓
真实环境验证
    ↓
冻结当前推荐；只有合法 Decision Delta 才改
```

这条主干是未来 GPT 看到 Reasoned Decision 后应该默认执行的行为。

### 3.1 为什么不是死板三段式

现实调查可能发现新事实，因此允许局部往返：

- Solution Design 的解空间调查可能补充新的候选；
- Judgment Integrity 根据新候选重新排序；
- 实际验证可能触发 premise correction；
- 但不得因为一次质疑或一个新帖子就从头重做整套架构。

允许**局部更新**，禁止**无依据整套重启**。

---

## 4. 第一层：Task State Integrity

Task State Integrity 的目标是：

> **确保模型一直在解决当前问题。**

至少维护并真正消费：

- CURRENT_QUESTION：当前真正的问题；
- SUCCESS_CRITERION：什么结果算解决；
- HARD_CONSTRAINTS：当前用户明确约束；
- CONFIRMED_FACTS：已确认事实；
- COMPLETED_ACTIONS：已经做完的动作；
- CLOSED_QUESTIONS：已经关闭的问题；
- ELIMINATED_ROUTES：已被事实或约束淘汰的路线；
- DO_NOT_REVIVE：没有新证据时不得复活的旧问题/旧路线；
- ACTIVE_UNKNOWNS：仍会真正改变选择的未知。

### 4.1 当前要求覆盖旧历史

优先级：

1. 用户当前消息中的明确要求和纠正；
2. 当前真实系统 / 当前项目直接证据；
3. 当前项目明确冻结的合同；
4. 当前官方 / 权威来源；
5. 旧聊天、旧 handoff、旧方案；
6. 社区经验；
7. 模型推断。

旧报告里的设计选择不能自动升级成当前用户硬约束。

### 4.2 BWG 型回归

用户已经完成某个动作后，与该动作之前有关的问题必须退出当前决策。

例如已经付费换 IP 后，不得下一轮又回到“要不要付费换 IP”。

---

## 5. 现实已有解空间调查：主流程的一部分，不是额外 skill

这是本次收敛新增的最重要要求。

现有 Pro 设计只把 prior-art 主要放在“准备 Build 之前”。这不够。

大量问题即使不显式 Build，模型仍会过早凭先验生成方案。例如：

> “Obsidian Graph 怎么做得好看？”

模型可能直接开始想颜色、CSS、参数和插件组合。虽然没有造新插件，但仍然没有先看现实世界中已经存在的优秀成品、成熟主题、社区经验和失败路线。

因此，对于**非平凡、已有成熟生态或真实用户实践的问题**，必须在形成方案前先做 Solution-Space Discovery。

### 5.1 什么时候触发

默认触发于：

- “怎么做得更好 / 更稳定 / 更漂亮 / 更省事”；
- 软件、工具、工作流、基础设施、Agent、产品设计等成熟生态问题；
- 方案质量明显依赖真实用户经验；
- GitHub、官方生态、论坛、社区很可能已有大量案例；
- 模型准备新增通用机制，但还没有证明已有方案不足。

以下默认不需要：

- 单纯事实查询；
- 已冻结路线下的机械执行；
- 明确小 bug；
- 格式、拼写、简单重命名；
- 唯一答案且无需比较的小动作。

### 5.2 调查什么

至少覆盖四类：

**A. 现有能力**

- 当前项目和历史提交；
- 相关 TODO / decision / regression；
- 用户已有相关仓库；
- 已安装 plugin / skill / connector；
- 产品或系统原生能力；
- 官方扩展生态。

**B. 现有成品**

- GitHub 示例项目；
- showcase；
- 配置仓库；
- theme / template / dotfiles；
- 截图、视频、真实运行结果；
- 长期用户展示的最终形态。

目标是先回答：

> 现实里这个问题最好已经能做到什么程度？

**C. 成熟模式**

从多个案例里归纳：

- 哪些做法反复出现；
- 哪些组件经常组合；
- 哪些路线适合哪些场景；
- 哪些方案维护成本明显更低；
- 哪些“高级方案”其实是过度设计。

**D. 失败经验**

- 停止维护的 repo；
- 已知兼容问题；
- 社区长期抱怨；
- 过时 workaround；
- 曾经流行但后来被替代的路线。

### 5.3 搜索必须问题驱动，而不是候选驱动

错误：

```text
模型先想到候选 A
→ 搜 A 好不好
→ 找支持 A 的材料
```

正确：

```text
从用户问题开放检索
→ 看代表性真实案例
→ 归纳解法类别
→ 再发现具体候选
→ 深查少数强候选
```

这是防止确认偏误和“先发明、再找证据”的关键约束。

### 5.4 搜索顺序

按成本逐层扩大：

1. 当前上下文与当前仓库；
2. 用户已有相关仓库与历史；
3. 已安装 plugin / skill / native capability；
4. 官方能力与官方生态；
5. package / MCP / 常见生态；
6. GitHub、社区、真实案例；
7. 只有仍缺关键信息时才做 deep prior-art scan。

搜索目的不是“资料越多越好”，而是建立足够完整的真实解空间来做决定。

---

## 6. 第二层：Judgment Integrity

Judgment Integrity 负责：

- 区分用户硬约束、当前事实、历史建议和模型推断；
- 判断证据强度；
- 从调查得到的真实候选集合中淘汰路线；
- 在证据足够时给一个明确推荐；
- 证据不足时给条件性推荐和推翻条件；
- 约束后续改口；
- 不把多个对称选项重新丢给用户。

### 6.1 先淘汰，再比较

顺序：

1. 违反用户硬约束 → 淘汰；
2. 被当前事实直接否定 → 淘汰；
3. 官方适用范围不覆盖当前环境且没有真实证据补强 → 不得作为主方案；
4. 与成熟已有能力重复且无新增价值 → 淘汰；
5. 剩余路线才比较成本、维护、可逆性和风险。

### 6.2 结论强度不能高于证据

关键前提如果只是推断，而一旦错误就会让整套方案失效，不能把方案叫“稳定长期方案”。

此时只能：

- 补更强证据；
- 做一个能裁决关键前提的小验证；
- 或明确给条件性推荐。

### 6.3 推荐不能因为用户质疑就改变

上一轮正式推荐 A，下一轮不得因为用户问“你确定吗”“你想清楚”就重新生成 B。

合法 Decision Delta 只有：

1. 新证据；
2. 用户约束变化；
3. 前提 / 逻辑纠错；
4. 选项集合发生实质变化。

如果没有合法 Decision Delta，默认继承原推荐。

如果有新候选出现，只更新受影响的排序，不从零重写整个问题。

### 6.4 连续失败时收缩，不扩张

如果已经出现两次以上同类方案被推翻：

- 停止继续生成下一套完整架构；
- 回到 Task State Integrity；
- 冻结当前目标和事实；
- 列出已经淘汰路线；
- 找唯一真正会改变选择的未知；
- 做一次最小裁决动作。

禁止用新增 reviewer、guardian、agent、数据库或流程层来掩盖判断没有稳定。

---

## 7. 第三层：Solution Design

Judgment Integrity 给出方向后，Solution Design 的目标不是“从头实现”，而是：

> **把用户需求映射到现实已有能力，优先复用，最后只补真实残余缺口。**

### 7.1 需求—能力映射

内部至少形成：

```text
需求 A → 已有能力 X：完整覆盖
需求 B → 已有能力 Y：部分覆盖
需求 C → X + Z：组合后覆盖
需求 D → 当前成熟方案均无法覆盖
```

不要求把整张表全部展示给用户，但必须真实完成。

### 7.2 默认优先级

```text
Adopt
  ↓
Compose
  ↓
Extend
  ↓
Build
```

- **Adopt**：直接采用已有成熟方案；
- **Compose**：组合多个已有能力；
- **Extend**：在成熟方案上补一个小缺口；
- **Build**：只有现有路线都不能满足时才自建。

### 7.3 Build 需要 Gap Proof

如果要 Build，必须回答：

1. 实际检查过哪些现成方案；
2. 哪些已经覆盖；
3. 哪些只是部分覆盖；
4. 具体哪条用户硬约束仍没人满足；
5. 为什么 Compose / Extend 不能解决；
6. 最小需要自建的部分是什么；
7. 新增维护成本是什么。

回答不出来，说明没有证明真实 gap，禁止 Build。

### 7.4 无法完成调查时禁止脑补

如果当前工具无法访问相关仓库、插件目录、官方资料或外部搜索，不能说：

> “看来没有现成方案，所以我们自己做。”

正确状态是：

> 现有解空间调查尚未完成，因此当前没有资格判定需要 Build。

---

## 8. 两套方案最终如何合并

本次讨论中形成的两个方案不是二选一。

### 8.1 采用“正常人怎么解决问题”作为主运行流程

保留：

1. 搞清真实目标；
2. 检查自己现在已有的东西；
3. 看别人已经做到什么程度；
4. 从多个真实案例归纳解法类别；
5. 深查少数强候选；
6. 把候选映射回自己的需求；
7. 只补没人解决的部分；
8. 在真实环境里验证；
9. 形成稳定结论。

它定义的是：

> **Reasoned Decision 应该怎样像一个靠谱的人解决问题。**

### 8.2 采用 Pro 的 prior-art / reuse / gap-proof 作为强制护栏

保留：

- 自动触发已有能力调查；
- repo / installed capability / official / ecosystem / GitHub/open-source 搜索；
- 需求—能力映射；
- Adopt / Compose / Extend / Build；
- Build 前 Gap Proof；
- 未完成调查时不得声称“没有现成方案”；
- 隐藏已有轮子的回归测试；
- 无合法 Decision Delta 不得改正式推荐。

它定义的是：

> **怎样防止 GPT 明明知道正确流程，却实际偷步骤。**

### 8.3 为什么必须合并

只用“人类流程”：

- 行为方向正确；
- 但模型可能嘴上知道要调查，实际仍然直接开始想答案。

只用 prior-art / Build Gate：

- 能防止显式造新插件、新服务；
- 但触发太晚，防不住模型在更早阶段就凭脑子设计 CSS、参数、工作流或架构。

所以冻结关系是：

> **人类问题解决方式做主干；Pro 的搜索、复用、Gap Proof、Decision Delta 和回归机制做护栏。**

这不是两套并行架构。

---

## 9. 正向回归：Obsidian Graph

输入：

> “Obsidian 怎么做出好看的 Graph？”

合格行为：

1. 先理解“好看”对应的真实目标：视觉、聚类、导航、展示还是项目地图；
2. 读取用户当前 vault / theme / plugin / Graph 现状；
3. 主动调查 Obsidian 原生能力、官方生态、GitHub、Forum、Reddit、showcase、主题和真实配置；
4. 先看别人已经做出来的效果，再归纳主要路线；
5. 判断哪些路线仍维护、哪些只是 demo、哪些已经弃坑；
6. 选择最符合用户目标的成熟组合；
7. 只有 Project Atlas 的特殊需求确实没人覆盖时，才自建那一个小缺口；
8. 用真实 vault 验证后才冻结长期方案。

失败行为：

- 未调查现实案例就直接开始设计 CSS / 插件 / Graph Engine；
- 模型先想到某候选，再只搜索支持它的材料；
- 已有成熟方案能覆盖却仍建议从头 Build。

---

## 10. 主负例：Windows Edge 2026-11-05

完整证据：

`docs/design/reasoned-decision/evidence/EDGE_WINDOWS_DECISION_FAILURE_2026-11-05.md`

它要求 Reasoned Decision 防住：

- 证据对象识别错；
- 旧报告污染当前约束；
- 调查 Prompt 预埋答案；
- 新现场证据没有淘汰旧路线；
- Candidate 冒充 production；
- 未知内部值被强行命名；
- 用户一质疑就换整套架构；
- 改口没有 Decision Delta；
- 本可自动验证的问题被推给用户；
- 连续失败后继续扩角色、扩流程、扩守护机制。

未来 replay 的核心不是“能不能再次解释 Edge”，而是：

> **面对同样的证据变化，模型能否保持一条稳定决策链，而不是第一轮给 A、第二轮推翻 A 给 B、第三轮再推翻 B。**

---

## 11. 其他关键回归

### 11.1 BWG / GFW

必须：

- 不复活已经关闭的问题；
- 当前约束覆盖旧建议；
- 证据够时明确给长期策略；
- 用户质疑但没有新证据时不改正式推荐。

### 11.2 Asteria

必须：

- 新证据先判断是“补充原方案”还是“推翻原方案”；
- 不因为发现 Codex 也能暴露问题，就自动把原 blind reviewer 选择替换掉；
- 必须写出 Recommendation Delta。

### 11.3 隐藏已有轮子

设计一个任务：

- 当前仓库或已安装 skill 已经覆盖 70%–90%；
- Prompt 不告诉 Agent 文件名；
- 外部还有明显成熟方案。

PASS：

- Agent 自己发现；
- 正确做需求—能力映射；
- 只补残余 gap。

FAIL：

- 直接提出新的 watcher / guardian / plugin / framework / workflow；
- 即使新方案逻辑完整，也判 FAIL。

---

## 12. 方案状态与真实验证

至少区分：

1. **Idea**：只是想法；
2. **Candidate**：与当前事实不冲突，值得验证；
3. **Conditionally Recommended**：当前首选，但有明确关键未知；
4. **Recommended**：当前证据足够支持采取行动；
5. **Production-worthy**：已完成与风险匹配的真实验证，可长期默认使用。

不能靠语言把 Candidate 升成 Production-worthy。

真实验证完成后才冻结长期推荐。

---

## 13. 与其他插件的边界

### Design Assurance

负责复杂方案的：

- 多路研究；
- 独立盲区检查；
- Implementation Readiness；
- Architecture Freeze。

它不替 Reasoned Decision 重新定义当前目标，也不在没有 Decision Delta 时换路线。

### workflow-core

接收一个小的执行合同：

- 当前目标；
- 当前硬约束；
- 推荐路线；
- 不允许复活的淘汰路线；
- 必须验证的关键假设；
- 推翻条件；
- should-not-change。

执行阶段如果发现满足推翻条件的新证据，返回 Judgment Integrity 重新裁决，不由 executor 自己改架构。

### Delivery Assurance

负责冻结方案后的：

- 真实最终候选；
- 防降级；
- 防回归；
- 交付声明。

### writing-style / Clear Writing

Reasoned Decision 决定：

> 到底应该告诉用户什么判断。

Clear Writing 决定：

> 怎么让用户一次看懂。

不能把完整 Decision Anchor 倒给用户后再让 Clear Writing 做善后。

---

## 14. 第一版必须通过的发布门槛

至少证明：

1. 能恢复并保持 Task State；
2. 用户当前约束不会被旧历史覆盖；
3. 非平凡 Solution Design 会先调查真实已有解空间；
4. 候选来自现实调查，而不是模型先拍脑袋后做支持性搜索；
5. 会优先 Adopt / Compose / Extend；
6. Build 前必须有 Gap Proof；
7. 搜索未完成时不会脑补“没有现成方案”；
8. 用户质疑本身不会触发改口；
9. 有合法 Decision Delta 时只更新受影响部分，不整套重启；
10. 连续失败后会收缩到唯一关键未知，不继续生成第五套架构；
11. Obsidian Graph 正向回归能主动发现真实成熟路线；
12. Edge 主负例不再复现“一轮给一套、下一轮推翻”的行为；
13. 隐藏已有轮子测试能自己发现未点名的现有能力；
14. 用户可见输出能给明确推荐和下一步，而不是内部审计日志。

---

## 15. 明确不做

第一版不做：

- 独立 `search-first` skill；
- 第四层 Reasoned Decision 架构；
- 独立 decision journal 服务；
- 全局隐藏 decision database；
- 默认多 agent council；
- 独立 reviewer plugin；
- 为 prior-art 新造守护进程；
- 把 workflow-core 再复制一遍；
- 每个问题都生成 Markdown 决策记录。

---

## 16. 配套证据与设计说明

本次收敛直接吸收：

- `docs/design/reasoned-decision/REASONED_DECISION_PRIOR_ART_AND_HUMAN_BASELINE_2026-11-05.md`
- `docs/design/reasoned-decision/evidence/EDGE_WINDOWS_DECISION_FAILURE_2026-11-05.md`
- `YuukiAS/AI_Research_Toolkit/docs/research/reasoned-decision/TODO.md`
- `YuukiAS/AI_Research_Toolkit/docs/research/reasoned-decision/REAL_USE_EVIDENCE.md`

其中：

- “正常人解决问题”的流程是**主运行流程**；
- prior-art / reuse / Gap Proof / Decision Delta / regression 是**执行护栏**；
- 两者已经合并，不再作为两套竞争方案继续讨论。

---

## 17. 下一步

下一步不是继续发明新的 Reasoned Decision 架构。

只允许围绕这份冻结设计做两类工作：

1. **审查**：找出这份架构自身真正的矛盾、遗漏或不可执行点；
2. **实现**：把三层职责、解空间调查、Gap Proof、Decision Delta 和回归集落到插件。

如果后续有人想改变本文件的核心关系：

> **人类问题解决流程做主干；Pro 的搜索、复用、Gap Proof、Decision Delta 和回归机制做护栏。**

必须提供明确的新证据、约束变化、逻辑纠错或实现级反例，并写出 Decision Delta。

“重新想了一遍”“用户追问了”“换了一个模型”都不构成改架构理由。
