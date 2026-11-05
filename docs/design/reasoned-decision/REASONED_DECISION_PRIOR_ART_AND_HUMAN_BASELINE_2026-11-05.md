# Reasoned Decision：既有 Pro 结论、待补缺口与人类问题解决基线

Status: INCORPORATED_IN_CANONICAL_ARCHITECTURE  
Date: 2026-11-05  
Scope: supporting evidence for Reasoned Decision only  
Not in scope: 新增独立 `search-first` skill、重做 Design Assurance、重做 Delivery Assurance

## 0. 为什么需要这份文档

Reasoned Decision 当前真正需要解决的，不是“再想一套更漂亮的架构”，而是把一种可靠的人类问题解决习惯变成稳定的 Agent 行为：

> 面对一个非平凡现实问题，不要先从模型内部生成一套新方案；先恢复当前任务状态，再调查现实世界已经存在的解法、案例、成熟工具和失败经验，在已有解空间上完成判断、组合与最小补缺。

这份文档只做三件事：

1. 冻结 Pro 已经得出的结论，避免下一轮重新发明；
2. 明确现有结论还缺的执行闭环；
3. 给出一个“正常、有经验的人类遇到问题会怎么一步步做”的行为基线，作为后续 Reasoned Decision 的设计与回归标准。

相关历史材料：

- `YuukiAS/AI_Research_Toolkit/docs/research/reasoned-decision/TODO.md`
- `YuukiAS/AI_Research_Toolkit/docs/research/reasoned-decision/REAL_USE_EVIDENCE.md`
- `docs/design/reasoned-decision/REASONED_DECISION_V0_1_ARCHITECTURE_2026-11-05.md`
- `docs/design/reasoned-decision/evidence/EDGE_WINDOWS_DECISION_FAILURE_2026-11-05.md`
- `docs/skill-todos/reasoned-decision.md`

本文件不是新的 skill 设计，也不是竞争架构。其结论已经并入 `REASONED_DECISION_V0_1_ARCHITECTURE_2026-11-05.md`；后续实现和审查以该权威架构为准，本文件只保留推导依据与人类行为基线。

---

## 1. 先冻结历史三层基线

Reasoned Decision 的既有三层候选架构是：

```text
Task State Integrity
        ↓
Judgment Integrity
        ↓
Solution Design
```

不得再把它与以下结构混为一谈：

- `Judgment Integrity + Solution Design` 两个内部 skill；
- Judgment Integrity 内部“什么可以改变 / 先核证据再改判 / 允许保持未知”的三条判断原则；
- `Reasoned Decision → Design Assurance → Delivery Assurance` 的跨插件可靠性生命周期。

三者都可以继续存在，但它们不是这里所说的 Reasoned Decision 三层。

### 1.1 Task State Integrity

负责保证 AI 仍在解决当前问题，而不是逻辑严谨地回答错题。

至少要持续维护并真正消费：

- 当前问题；
- 当前成功标准；
- 当前硬约束；
- 已确认事实；
- 已完成动作；
- 已关闭问题；
- 已淘汰、不得无理由复活的路线；
- 当前仍开放的关键未知。

BWG/GFW 真实失败已经证明：只做 Judgment Integrity 不够。用户已经付费换 IP 后，“现在要不要换 IP”必须退出当前问题；如果模型下一轮又讨论“先别付钱换”，说明任务状态已经丢失。

### 1.2 Judgment Integrity

负责在正确的问题上形成稳定判断：

- 证据强度与主张强度匹配；
- 先淘汰违反约束或已被事实否定的路线；
- 证据足够时给明确推荐；
- 真正决定性的未知尚未解决时，允许条件性推荐或保持未知；
- 用户质疑本身不是改口理由；
- 改判必须有明确的 Decision Delta：新证据、用户约束变化、前提/逻辑纠错或选项集合变化；
- 没有合法 Decision Delta，默认继承上一轮正式推荐。

### 1.3 Solution Design

负责把已稳定的问题和判断转成可落地方案。

关键要求不是“设计得多完整”，而是：

> 先发现已有解空间，再选择、组合、扩展，最后只补真实缺口。

Solution Design 不应默认等于“模型开始创造方案”。

---

## 2. Pro 已经得出的结论：不新增 search-first skill

Pro 已经收敛的方向应保留：

> 不新增独立的 `search-first` skill。

原因不是“搜索不重要”，而是搜索与 prior-art 本来就是 Solution Design 的组成部分，另起一个 skill 只会继续增加能力层级和调度复杂度。

现有 Pro 设计已经明确了以下内容。

### 2.1 Prior-art 属于 Solution Design

当任务涉及以下情况时，应触发现有方案调查：

- 新建插件、skill、通用工具、服务或工作流；
- 引入新依赖；
- build-vs-buy / build-vs-adopt；
- reusable wrapper / agent infrastructure；
- 用户明确问“是不是要自己造”。

### 2.2 搜索顺序

现有设计已经给出顺序：

1. 当前仓库；
2. 已安装 plugin / skill / native capability；
3. 平台或框架官方能力；
4. package registry / MCP / 常见生态；
5. 维护中的开源实现；
6. 必要时 deep prior-art scan。

### 2.3 最终必须形成复用裁决

```text
Adopt   = 直接采用已有方案
Extend  = 基于成熟方案补一个真实缺口
Compose = 组合多个已有能力
Build   = 现有方案均无法满足
```

### 2.4 Build 不是默认许可

如果最终要 Build，必须说明：

- 实际检查过哪些现成候选；
- 每个候选具体缺什么；
- 为什么 Extend / Compose 不能解决；
- 自建新增的不可替代价值是什么；
- 后续维护成本是什么。

没有这些，不允许 Build。

### 2.5 Edge 负例已经要求自动触发 prior-art

现有 Edge 回归中的 R8 已经明确：当问题转成“要不要做 Reasoned Decision 这种通用插件/skill”时，Agent 必须自动检查当前仓库、已安装能力和外部成熟实现，再形成 Adopt / Extend / Compose / Build 裁决，不能等用户提醒。

以上结论应保留，不需要再造新的 search-first skill。

---

## 3. Pro 结论还缺什么：触发点太晚

现有设计的主要不足不是“搜索顺序不够细”，而是 prior-art 目前主要被描述成：

> 准备造新东西之前，先查有没有现成轮子。

这还不够。

大量现实问题不会显式进入“我要 Build 一个新东西”的状态，但模型仍然会过早从自己的先验里生成方案。

例如用户问：

> Obsidian 怎么把 Graph 做得好看？

模型可能根本没有说“我要造插件”，而是直接开始建议：

- 调颜色；
- 调节点大小；
- 写 CSS；
- 调力导向参数；
- 自己设计 vault 的标签体系。

这依旧可能是在没有调查现实解空间的情况下从头设计。

真正缺的是：

> prior-art 不只做 Build 前检查；对于存在成熟生态、公开案例或真实使用经验的非平凡 Solution Design，必须先做 Solution-Space Discovery。

也就是说，Solution Design 应有两个连续但不同的门。

---

## 4. 第一门：Solution-Space Discovery

这是“产生方案之前”的门。

### 4.1 什么时候自动触发

只要满足以下任一条件，就应默认先调查已有解空间：

- 用户问“怎么做得更好”“怎么配置更好”“有没有稳定方案”；
- 问题属于成熟软件、工具、工作流、基础设施或产品生态；
- 公开世界很可能已经有大量案例、插件、配置、主题、模板、脚本或社区经验；
- 方案质量明显依赖真实使用经验，而不只是形式逻辑；
- 视觉、生产力、开发工具、Agent 工作流、基础设施治理等已有成熟社区；
- 当前任务已经出现“自己设计一套”的冲动，但尚未证明现有解法不足。

低成本、唯一答案、纯机械任务不需要升级成这套流程。

### 4.2 调查什么

Solution-Space Discovery 不等于“搜一个同名 repo”。

至少应主动覆盖四类信息。

#### A. 现有能力

查：

- 当前项目已经有什么；
- 相关历史提交、TODO、decision、regression 已经做过什么；
- 用户已有相关仓库有什么；
- 当前已安装 plugin / skill / connector 有什么；
- 产品或操作系统原生支持什么；
- 官方扩展生态有什么。

#### B. 现有成品

不是只看“功能列表”，而是看别人真正做出来的结果：

- GitHub 示例项目；
- 社区 showcase；
- 配置分享；
- theme / template / dotfiles；
- 有截图、视频或真实运行结果的案例；
- 长期使用者展示的最终形态。

这一步回答：

> 现实里这个问题最好已经能做到什么程度？

#### C. 成熟模式

从多个案例中提炼：

- 哪些做法反复出现；
- 哪些组件经常被组合；
- 哪些选择只适合特定场景；
- 哪些方案维护负担大；
- 哪些看似高级，实际是过度设计。

这一步回答：

> 成功案例背后的共同模式是什么？

#### D. 失败经验

查：

- 停止维护的 repo；
- 已知兼容性问题；
- 社区长期抱怨；
- 过时 workaround；
- 曾经流行但后来被替代的路线；
- “功能能做”但长期维护不值得的方案。

这一步避免只看正面宣传。

### 4.3 检索必须问题驱动，而不是候选驱动

错误顺序：

```text
模型先想到候选 X
→ 搜“X 好不好”
→ 找证据支持 X
```

正确顺序：

```text
从用户问题本身开放检索
→ 收集代表性案例
→ 归纳解法类别
→ 再发现具体候选
```

这是现有 macOS Finder 右键软件回归已经暴露过的问题：先锁定一个项目再做支持性搜索，会把“功能看起来很合适”误当成“默认最值得推荐”。

### 4.4 什么时候停止查

不要求每次做 Deep Research。

按成本逐层扩大：

```text
当前上下文 / 当前项目
→ 用户已有仓库与能力
→ 已安装 skill / plugin / native capability
→ 官方生态
→ 高价值社区 / GitHub
→ 必要时 deep prior-art
```

当已经找到足以覆盖用户目标、且主要替代方案不会改变决策的成熟解法时就停止。

搜索的目的不是“资料越多越好”，而是建立足够完整的解空间来做决定。

---

## 5. 第二门：Reuse / Build Gate

Solution-Space Discovery 完成后，才允许进入真正的方案构造。

### 5.1 先做需求—能力映射

内部至少形成：

```text
需求 A → 已有能力 X：完整覆盖
需求 B → 已有能力 Y：部分覆盖
需求 C → X + Z：组合后覆盖
需求 D → 现有候选都无法覆盖
```

不要求把整张表暴露给用户，但内部必须有足够证据证明：

> “真正的缺口到底是什么？”

### 5.2 默认顺序

```text
Adopt
  ↓
Compose
  ↓
Extend
  ↓
Build
```

Build 是最后一种、异常情况，不是模型最自然的默认行为。

### 5.3 Gap Proof

如果选择 Build，必须能回答：

1. 现有解法有哪些？
2. 哪些已经完整覆盖？
3. 哪些只能部分覆盖？
4. 具体哪一条用户硬约束仍然没人满足？
5. 为什么组合已有能力还不够？
6. 最小需要自建的部分是什么？

无法回答，说明还没有证明存在真实 gap，不得 Build。

---

## 6. 还需要补的执行保证

仅在文档里写“先查”仍然不够。后续实现必须让“先查”成为可验证义务，而不是模型自觉。

### 6.1 必须有实际来源证据

Agent 不能只说“我检查过了”。

对决定方案的关键既有能力，至少应知道来源：

- 哪个仓库 / 文件；
- 哪个已安装 skill / plugin；
- 哪个官方能力；
- 哪个成熟外部项目；
- 哪个社区长期实践。

### 6.2 无法调查时不能脑补“没有现成方案”

如果当前环境没有能力访问相关仓库、插件目录、外部搜索或官方资料，不能直接说：

> “看来没有，所以我们自己做。”

正确状态是：

> prior-art / solution-space discovery 未完成，因此当前没有资格判断需要 Build。

### 6.3 新增机制必须自动触发检查

只要准备新增以下对象，就应立即检查是否已经存在：

- skill；
- plugin；
- agent；
- watcher；
- daemon；
- guardian；
- wrapper；
- 服务；
-数据库；
- 状态机；
- 通用工作流；
- 新依赖。

这是硬触发器，不依赖用户提醒。

### 6.4 回归不能只检查最终有没有写 Adopt / Extend / Compose / Build

真正的回归要验证：

> Agent 能不能在用户没有告诉它名字的情况下，自己发现预先存在的高价值能力。

应专门设计“隐藏已有轮子”测试：

- 仓库里已经有 70%–90% 的实现；
- Prompt 不告诉 Agent 文件名；
- 相关 skill / plugin 已存在；
- 外部世界存在明显成熟方案。

合格行为：

> 自己发现 → 正确归类覆盖范围 → 只补剩余缺口。

失败行为：

> 直接设计新的 watcher / plugin / framework / workflow，即使新方案本身逻辑完整，也判 FAIL。

---

## 7. 如果是一个正常、有经验的人类，他会怎么做

这部分不是新的系统架构，而是 Reasoned Decision 应逼近的行为基线。

### 第一步：搞清楚自己到底想解决什么

人不会看到一个模糊问题就直接写代码。

例如：

> “Obsidian Graph 不好看。”

会先拆成真实目标：

- 是视觉太乱？
- 聚类不明显？
- 色彩不好？
- 标签太多？
- 是想做展示图，还是想做真正可导航的项目地图？
- 希望配置长期稳定、可 Git 管理吗？

这一阶段对应 Task State Integrity。

### 第二步：看看自己已经有什么

先检查当前环境：

- Obsidian 原生 Graph 已经能做什么；
- 当前 vault 的 folder / tag / link 结构；
- 当前 theme；
- 当前已装插件；
- 现在具体哪里不好。

正常人不会假设自己从空白系统开始。

### 第三步：看别人已经做到什么程度

这是模型最容易跳过、但人类很自然会做的一步。

围绕问题本身去找：

- 官方文档；
- GitHub；
- Reddit；
- Obsidian Forum；
- showcase；
- 博客 / 视频；
- 配置仓库。

目标不是马上找一个插件，而是先回答：

> 别人已经把这个问题做到什么程度？好看的结果长什么样？

### 第四步：从案例反推出解法类别

看多个案例以后，可能发现不同路线：

- 原生 Graph + 分组 / 过滤 / force 参数；
- theme + CSS；
- 增强 Graph 插件；
- 固定布局插件；
- 其实目标不适合 Global Graph，而更适合 Canvas / Bases / 局部地图。

这时才形成“解法类别”。

顺序应是：

```text
案例
→ 规律
→ 解法类别
→ 具体候选
```

而不是：

```text
模型先想到一个候选
→ 再找资料证明它不错
```

### 第五步：深查少数强候选

此时再看：

- 是否仍维护；
- issue / release 状态；
- 真实用户是否长期使用；
- 和当前版本是否兼容；
- 权限、副作用和迁移成本；
- 配置能不能被保存和恢复；
- 是否会引入明显维护负担。

这一阶段主要属于 Judgment Integrity。

### 第六步：把候选映射回自己的需求

例如最终得到：

```text
原生 Graph → 已解决聚类、过滤和基础颜色
成熟 theme → 已解决大部分视觉
现成插件 X → 只补固定布局
项目自己的 CSS → 只需补一个小视觉细节
```

那么合理方案自然是：

> 原生能力 + theme + 一个成熟插件 + 很少量项目配置。

而不是重新实现 Graph、布局、主题、筛选和状态管理。

### 第七步：只补真正没人解决的部分

如果调查后发现：

> Project Atlas 有一项特殊状态映射，现有插件都不支持。

那就只实现这一小块适配。

不是以这个小缺口为理由重做整套系统。

### 第八步：用自己的真实环境验证

人不会因为 README 写得好就宣布长期方案成立。

至少会：

- 在自己的数据上试；
- 看真实结果；
- 对照强案例；
- 看维护成本；
- 判断是否真的比当前状态好。

只有验证以后，才把候选升级成长期默认。

### 第九步：形成稳定结论

一旦正式选择，不因为下一次看到一个新帖子就整套推翻。

新证据先判断：

- 是否真的改变用户目标；
- 是否推翻原关键前提；
- 是否出现了明显更优的新方案；
- 还是只是多了一个可选项。

只有真正改变排序，才更新推荐。

---

## 8. Obsidian Graph：Reasoned Decision 应该怎样实际回答

用户问：

> “Obsidian 怎么做出好看的 Graph？”

错误行为：

1. 模型直接凭先验列几个参数；
2. 自己设计一套颜色；
3. 建议写 CSS；
4. 甚至开始提新的插件 / Atlas Graph Engine；
5. 用户再提醒“别人没有现成的吗”。

正确行为：

### A. Task State Integrity

先理解“好看”的实际目标，并结合用户当前 vault / 项目用途。

### B. Solution-Space Discovery

主动调查：

- Obsidian 原生 Graph 的真实能力；
- 社区高质量 Graph showcase；
- GitHub 上成熟的 Graph 相关插件和配置；
- theme / CSS 方案；
- Reddit / Forum 的长期经验；
- 哪些插件已停止维护；
- 哪些案例实际上不是 Global Graph，而是其他 Obsidian 表达方式。

先看结果，再看实现。

### C. Judgment Integrity

从多个案例里判断：

- 哪些模式真正重复出现；
- 哪些只是个人审美；
- 哪些方案维护稳定；
- 哪些会破坏当前工作流；
- 哪条路线最符合用户的真实目标。

### D. Solution Design

优先组合已有能力，例如：

```text
原生 Graph
+ 已有 theme
+ 现成成熟插件（如果真的需要）
+ 最小量项目配置
```

只有调查证明某个 Project Atlas 特殊需求没有成熟方案，才针对该小缺口自己实现。

这个案例应成为 Reasoned Decision 的正式回归之一：

> 如果用户只问“怎么把 Obsidian Graph 做得好看”，Agent 在没有调查公开案例、现有插件、原生能力和真实社区实践前就直接开始设计新的 CSS 系统、插件或工作流，则判 FAIL。

---

## 9. Edge 为什么也是同一问题

Edge thread 的关键失败并不只是“某条微软策略看错”。

它还暴露了同一种设计习惯：

1. 看到问题；
2. 很快进入“我可以设计一个长期方案”；
3. 提出 updater 产品隔离、guardian、恢复机制等新结构；
4. 后面才逐步核对现有官方能力、真实平台限制和已有工具；
5. 新证据出现以后再撤回。

正确顺序应该相反：

```text
当前真实状态
→ 现有仓库能力
→ 官方支持边界
→ 已有成熟工具 / 社区经验
→ 已淘汰路线
→ 真实剩余 gap
→ 最小方案
```

这也是为什么 Edge 应继续作为 Solution-Space Discovery + Reuse Gate 的负回归案例。

---

## 10. 最终需要冻结的原则

Reasoned Decision 的 Solution Design 不应该被理解为：

> “根据目标设计一个解决方案。”

应改成：

> **“先发现现实世界已经存在的解空间，理解成熟模式和失败经验，再根据用户当前约束完成 Adopt / Compose / Extend；只有 gap 被证明以后，才允许 Build。”**

更短地说：

> **不是先想方案，再查有没有轮子；而是先看这个世界已经怎么解决，再决定还需要设计什么。**

Build 应是异常状态。

对公开软件、工具、Agent、工作流、基础设施、产品和视觉设计问题，默认假设应该是：

> **大概率已经存在完整解法、部分解法、成熟案例或可复用模式。先发现它们。**

只有现实调查之后仍然存在明确缺口，模型才有资格创造新的部分。

---

## 11. 下一轮修改 Reasoned Decision 时应做什么

只做 Reasoned Decision，不新增其他 skill。

需要修改的重点：

1. 恢复并明确 `Task State Integrity → Judgment Integrity → Solution Design` 三层边界；
2. 保留 Pro 已有的 prior-art 与 `Adopt / Extend / Compose / Build` 结论；
3. 把 prior-art 从“Build 前检查”前移为非平凡 Solution Design 的默认 `Solution-Space Discovery`；
4. 建立 Reuse / Build Gate 与 Gap Proof；
5. 要求关键既有能力有真实来源证据；
6. 无法完成调查时禁止脑补“没有现成方案”；
7. 新增 watcher / agent / plugin / daemon / wrapper 等机制时自动触发已有能力检查；
8. 增加“隐藏已有轮子”的发现型回归；
9. 把 Obsidian Graph 加成正向设计回归，把 Edge 继续作为负向回归；
10. 最终实现仍保持一个 Reasoned Decision 插件，不因为这些机制再新增 `search-first` 或其他辅助 skill。

这就是下一轮真正需要收敛的设计问题。
