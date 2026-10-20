# Clear Writing 0.6：ChatGPT 单入口与最终产物绑定方案 v0.1

日期：2026-10-20  
状态：DRAFT_FOR_INDEPENDENT_CRITIC  
角色：Planner  
目标仓库：`YuukiAS/AI_Skills_Collection`  
目标插件：`writing-style / Clear Writing`  
设计任务：`clear-writing--single-entry-artifact-finalization`  
设计分支：`design/clear-writing--single-entry-artifact-finalization`  
基线：`main@aa2e6ade13cf6e038a69ec4a2b5fbe318bebed39`  
跟踪：Issue `#13`  
拟议插件版本：`writing-style 0.5 -> 0.6`  
拟议个人插件版本：`0.5.0 -> 0.6.0`  
仓库发布决策：实现与验收完成后走 `PATCH`；具体三段版本在正式发布前按当前 `origin/release` 后绑定。

## 一、本轮结论

本轮不再把问题归结为“用户没有正确调用 Clear Writing”，也不把它简化成“再给 `chinese-prose` 增加几条规则”。用户已经在 ChatGPT Web 中显式选择了 Clear Writing；现有文档路线也已经写明中文技术长文应经过保真、结构重写和中文终审。真实失败说明的是：

> **显式选择当前 Clear Writing 个人插件，仍不能稳定保证正确的子能力被完整消费，也不能保证本轮所有读者产物——尤其是外部文档——都经过对应路线并以终审结果写回。**

Clear Writing 0.6 的正式方向是：

1. 保留现有六项专业能力及其 canonical source；
2. 只对 ChatGPT Personal Plugin 增加一个唯一可见的总入口；
3. 总入口先识别本轮所有交付对象，再为每个对象选择和执行相应路线；
4. 外部文件任务必须把“聊天回复”和“真正要写回的文档”分开验收；
5. 写入后必须回读最终文件，不能用一段清楚的聊天说明冒充文档已经经过 Clear Writing；
6. Codex Marketplace 继续保留六项直接能力，避免破坏既有跨插件调用和回放；
7. 不新增 MCP、外部模型、常驻服务、状态机或第二套写作规则。

这不是先验认定“六个并列 Skill 一定就是唯一根因”。准确结论是：**当前多 Skill 个人插件缺少可观察的总入口合同和最终产物绑定，因此允许本次失败发生。** 单入口方案必须通过真实 Web 回放证明有效；若仍失败，立即停止并回 Planner，不继续堆文字规则。

## 二、用户承诺基线

Clear Writing 0.6 必须稳定提供以下正常使用结果：

1. 用户只需显式选择一次 **Clear Writing**，不需要知道或手工选择 `response-clarity`、`scientific-rewrite`、`chinese-prose` 等内部路线。
2. 插件必须识别用户真正要得到的对象，而不只优化最后一段聊天回复。
3. 一次请求同时包含聊天解释和 GitHub、Drive、文件或其他外部文档时，两者必须分别处理和分别报告状态。
4. 已有技术或科研长文需要重新组织时，必须以全文为输入，保留事实、数字、公式、引用、权限、状态和精确机器字符串。
5. 外部写入只有在候选稿完成终审后才能发生；写入后回读不一致时不得声称完成。
6. 纯 JSON、YAML、代码、命令、逐字日志等精确机器输出继续保持原样。
7. 普通聊天、界面文案、英文科研表达和正式中文文档继续保持职责分离，不把 Clear Writing 变成一个接管领域判断的万能作者。
8. 没有可用写入工具时，输出完整候选稿和准确的待写入状态，不冒充已经修改外部文件。

后续修订可以细化机制，但不能静默删除这些承诺。

## 三、已经核实的事实

### 3.1 这次确实发生了显式调用

用户提供的 ChatGPT Web 截图显示，消息中已经选择：

```text
$clear-writing
```

对应当前 owned personal plugin `writing-style / Clear Writing 0.5.0`。因此“没有调用插件”不是这次失败的正确解释。

### 3.2 当前 Clear Writing 个人插件是六个并列 Skill

Planner 通过 Plugin Creator 回读当前发布包。它包含：

```text
skills/fidelity/
skills/response-clarity/
skills/product-ui-copy/
skills/sci/
skills/scientific-rewrite/
skills/zh/
```

当前包只有 `.codex-plugin/plugin.json`，其能力声明为 `Skills`，没有 root `plugin.json`，也没有一个名为 `clear-writing` 的唯一总入口 Skill。

### 3.3 PIE 是另一种包装结构

Planner 同时回读了当前 `Project Instructions Editor 0.2.8` 个人插件。它具有：

```text
plugin.json
.codex-plugin/plugin.json
skills/project-instructions-editor/SKILL.md
skills/project-instructions-editor/references/editor-contract.md
```

它只有一个顶层 Skill；该 Skill 自己包含基线门槛、编辑模式、完整候选检查和输出合同。用户显式选择 PIE 后，不需要再进行一次“六条兄弟路线选哪一条”的决定。

PIE 的成功不能单独证明“任何单 Skill 插件都会成功”。PIE 还有三个额外优势：任务范围窄、输出合同明确、主要交付物直接出现在当前回答中。Clear Writing 面向多种任务并可能写外部文档，因此 0.6 不能只复制“一个 Skill”这一表面结构，还必须增加交付对象识别和最终产物绑定。

### 3.4 现有 Clear Writing 规则已经覆盖了本次表面问题

当前 `chinese-prose` 已明确要求：

- 中文文档中文为主；
- 普通工程英文应中文化；
- 不把内部审计、流程和状态语言当成读者主叙事；
- 正式中文技术文档必须做最终终审；
- 需要结构性重写的已有中文技术材料应交给 `scientific-rewrite`。

当前 `scientific-rewrite` 也已经覆盖中文或中文主导的技术材料，不仅限于论文。它要求先建立语义地图和读者计划，再形成最终候选，并禁止把内部任务流程当成正文。

因此继续增加“少用英文”“别像日志”“先说人话”等同义规则不能解释或解决这次失败。

### 3.5 平台公开合同不保证插件级选择会加载全部兄弟 Skill

OpenAI 当前公开资料说明：

- 已安装插件可以在相关时自动使用，也可以由用户直接选择；
- 一个插件可以包含多个 Skill；
- 模型先看到 Skill 的名称和描述，只有请求匹配或直接调用具体 Skill 时才加载完整说明；
- ChatGPT 可以在有帮助时使用一个或多个 Skill。

公开资料没有承诺：用户选择一个包含多个 Skill 的插件后，该插件的所有 Skill 都会被加载、按固定顺序执行，或自动形成一次文档级终审流水线。

### 3.6 当前无法证明失败线程内部究竟选择了哪个 Skill

本轮没有该失败线程的正式 per-skill load trace，因此不能把以下说法写成已证实事实：

```text
模型只加载了 response-clarity
```

用户粘贴的后续回答表明，助手声称自己读取了 `chinese-prose` 和 `response-clarity`，但没有真正调用并消费一个独立输出。这支持“路线和消费合同失效”，但不能精确还原平台内部选择过程。

因此本 Proposal 的根因表述故意停在可证层级：

> 当前个人插件结构不能保证显式插件选择后，正确的完整路线覆盖本轮全部产物。

## 四、失败归因

### 4.1 已证实的产品缺陷

本次请求至少有两个交付对象：

1. GitHub 中的完整 Delivery Assurance Reader Guide；
2. ChatGPT 回给用户的说明。

最终聊天说明经过了某种语言整理，但 GitHub 文档仍大量使用 `Gate`、`adapter`、`owner`、`claim`、`Executor` 等内部流程词组织读者叙事，也没有完成真正的读者模型转换。

因此已证实的缺陷是：

```text
EXPLICIT_PLUGIN_SELECTION
!=
ALL_READER_TARGETS_CORRECTLY_ROUTED_AND_FINALIZED
```

### 4.2 高概率机制

当前六个 Skill 是并列入口，各自通过文字声明“应交给另一个 Skill”。这种 handoff 不是工具调用，也没有一个必经协调者确认：

- 本轮有几个目标；
- 每个目标属于哪条路线；
- 哪些路线需要串联；
- 哪个输出才是最终外部产物；
- 外部文件是否已经写回并回读。

这使模型可以只完成其中一部分，例如改进聊天回复，却没有对外部文档完成结构重写和最终终审。

### 4.3 尚未证实的部分

下面三项必须由实现后的真实 Gate 验证，不能在设计阶段当成事实：

1. 只要改成单入口，质量问题就一定消失；
2. `.codex-plugin` 的 `Skills` 与 PIE 的 `Interactive` 声明本身就是决定性原因；
3. 不增加 MCP 也一定能稳定约束所有外部写入。

0.6 采用单入口，是因为它消除一个已经观察到的职责缺口，并且是当前最轻的可验证方案；不是因为 Planner 已经证明平台内部的唯一因果路径。

## 五、替代路线比较

| 路线 | 结论 | 原因 |
|---|---|---|
| 继续给六个 Skill 增加规则 | 拒绝 | 本次违反的规则已经存在；继续堆同义规则不会建立必经入口或产物绑定。 |
| 只改插件描述和默认提示词 | 拒绝作为主方案 | 可以改善发现与粗路由，但仍让六个顶层 Skill 并列，也不能处理多交付对象和写回后回读。 |
| 新增第七个协调 Skill，同时保留六个顶层 Skill | 拒绝 | 仍可能直接选中兄弟 Skill，协调入口不是必经路径。 |
| 要求用户以后手工选择 `scientific-rewrite` | 拒绝 | 用户不应理解内部 Skill；也无法处理同一请求中的聊天回复与外部文档。 |
| 将整个 Codex Marketplace 也折叠成一个 Skill | 拒绝 | 会破坏跨插件直接消费、现有 replay、profile 和职责清晰度，改动面远大于当前失败。 |
| 为 Clear Writing 新建 MCP/外部 finalizer | 0.6 不采用 | 可以提供更强的动作控制，但会引入服务、权限、部署和故障面；当前尚未证明单入口 skills-only 方案不足。 |
| ChatGPT 个人插件改为单入口，Codex 保留六 Skill | 采用 | 最小化解决显式 Web 调用的入口和目标绑定问题，同时保留 canonical 六能力及 Codex 兼容性。 |

## 六、0.6 架构

### 6.1 两层结构

```text
Canonical capability layer
├── writing-fidelity
├── response-clarity
├── product-ui-copy
├── scientific-prose
├── scientific-rewrite
└── chinese-prose

ChatGPT personal wrapper layer
└── clear-writing
    ├── 识别全部交付对象
    ├── 为每个对象选择路线
    ├── 组合需要串联的路线
    ├── 约束写入前终审
    └── 写入后回读最终产物
```

六个现有 Skill 继续是专业语义的 canonical source。新的 `clear-writing` 只负责 ChatGPT 表面的入口、路由、顺序和完成判定，不重新复制一套写作判断。

### 6.2 个人插件包装

0.6 的 USER / PRIVATE Personal Plugin 继续保留：

```text
name = writing-style
displayName = Clear Writing
scope = USER
discoverability = PRIVATE
MCP = NO
existing plugin identity = PRESERVE
```

包结构改成 PIE 已验证的双 manifest + 单 Skill 形态：

```text
plugin.json
.codex-plugin/plugin.json
assets/...
skills/clear-writing/SKILL.md
skills/clear-writing/references/routes/writing-fidelity.md
skills/clear-writing/references/routes/response-clarity.md
skills/clear-writing/references/routes/product-ui-copy.md
skills/clear-writing/references/routes/scientific-prose.md
skills/clear-writing/references/routes/scientific-rewrite.md
skills/clear-writing/references/routes/chinese-prose.md
```

两个 manifest 必须声明同一版本和同一用户入口。个人插件使用唯一顶层 Skill `clear-writing`。旧的六个顶层 Skill 路径必须通过 Plugin Creator `delete_paths` 明确删除；只上传新文件而保留旧路径会使路由歧义继续存在，视为实现失败。

`capabilities` 是否使用与 PIE 相同的 `Interactive`，必须在执行 Plan 中依据当前 Plugin Creator schema 和一个无副作用包装探针冻结。不得仅因 PIE 使用该值就推断语义；但最终个人插件必须采用当前平台正式接受、能稳定显式选择单入口的 manifest 形态。

### 6.3 canonical source 与生成

不允许人工维护六份 route snapshot。

0.6 必须有一个确定性构建步骤，从以下 canonical source 生成个人插件中的 route references：

```text
skills/writing/core/writing-fidelity/
skills/writing/core/response-clarity/
skills/writing/core/product-ui-copy/
skills/writing/core/scientific-prose/
skills/writing/core/scientific-rewrite/
skills/writing/core/chinese-prose/
```

生成结果至少记录每个 source 的路径和 SHA-256，并通过测试证明：

- 个人插件 route references 与目标 source 一致；
- wrapper 不成为第二份可独立漂移的专业规则来源；
- Codex Marketplace 的六 Skill exposure 保持不变；
- Personal Plugin 只暴露一个 Skill。

具体目录和构建脚本名称在 execution-ready Plan 中冻结，但 source/generated ownership 不再开放给 Executor选择。

## 七、单入口工作合同

### 7.1 第一步：枚举本轮交付对象

`clear-writing` 必须先在内部识别所有用户真正会消费的对象，而不是默认只处理最终聊天消息。

对象类型至少包括：

```text
CHAT_RESPONSE
INLINE_DOCUMENT
EXTERNAL_DOCUMENT
PRODUCT_UI_COPY
MACHINE_PAYLOAD
```

每个对象必须确定：

- 来源；
- 目标读者；
- 用户要求的操作；
- 是否允许结构变化；
- 受保护事实和精确字符串；
- 需要的内部路线；
- 最终交付位置；
- 完成证据。

这是当前回答内的临时工作对象，不新增仓库 schema、数据库或长期 ledger。

### 7.2 第二步：按对象路由

| 对象/任务 | 路线 |
|---|---|
| 普通聊天解释、诊断、建议、进度说明 | `response-clarity` + 必要保真 |
| 已有中文正式文档的局部润色和最终终审 | `writing-fidelity` -> `chinese-prose` |
| 已有中文或中文主导技术/科研长文的结构性重写 | `writing-fidelity` -> `scientific-rewrite` -> `chinese-prose` 最终终审 |
| 英文科研表达 | `writing-fidelity` -> `scientific-prose` |
| 产品界面微文案 | `writing-fidelity` -> `product-ui-copy` |
| 纯精确机器内容 | 原样输出，不为证明调用而改写 |
| 混合自然语言 + 机器内容 | 只处理自然语言层，机器内容保持精确 |

总入口执行的是这些 route contract，不要求平台再次选择兄弟 Skill。

### 7.3 第三步：获取完整目标材料

对外部文档：

- 必须读取实际目标文件全文或足以覆盖本次授权范围的完整区域；
- 必须绑定当前文件身份、版本或 commit；
- 不能只根据标题、摘要、旧聊天或上一版回复生成替代品；
- 若目标文件不可访问，返回准确缺口，不声称已经重写。

### 7.4 第四步：先形成终审候选，再写入

外部文档写入前必须形成一个已经完成以下检查的候选：

- 事实和受保护字符串保真；
- 路线对应的结构与语言要求；
- 用户要求的完整范围；
- 没有把聊天说明、审计过程或执行状态误写入正文；
- 没有只修开头或少量片段却声称整篇完成。

聊天回复和外部文档是两个对象。聊天回复不得作为文档候选或文档验收证据。

### 7.5 第五步：写入后回读

有可用 GitHub、Drive 或文件工具时：

1. 写入已终审候选；
2. 重新读取实际目标；
3. 核对目标身份和内容；
4. 再报告完成。

若回读失败、内容不一致或目标身份改变，状态只能是：

```text
ARTIFACT_FINALIZATION_UNVERIFIED
```

不得声称“已经过 Clear Writing 正式终审”。

这是一项 Skill 工作合同，不冒充平台级事务或不可绕过的系统 Hook。0.6 的验收必须证明该合同在真实 ChatGPT Web 正常入口中实际被遵守；若不能，返回 Planner 再判断是否需要 App/MCP 层，而不是通过文档宣称解决。

## 八、本次真实失败怎样进入回归

已知失败固定为 release-critical regression：

```text
显式选择 Clear Writing
+ 提供 GitHub Reader Guide 链接
+ 要求把整套架构讲清楚并修改文档
+ 同时需要聊天说明
```

回放必须检查：

1. 插件识别两个交付对象，而不是一个；
2. GitHub 文档走结构重写 + 中文终审；
3. 聊天回复走普通解释路线；
4. 最终文档不再由普通内部流程英文承担句子骨架；
5. 正式名称、路径、版本和必要机器字符串仍保持精确；
6. 写入后回读的文档与终审候选一致；
7. 不能仅凭聊天回复清楚就给 PASS。

该案例从现在起是 known regression，不能再作为 fresh generalization 样本。

## 九、Capability Gate Matrix

| Gate | Capability / claim | Normal entry | 必须看到的证据 | 明确失败 | 既有能力保护 | 最终候选要求 |
|---|---|---|---|---|---|---|
| `CW06-G1` 单入口身份 | 显式选择 Clear Writing 后进入唯一 `clear-writing` 工作合同 | 当前 USER / PRIVATE 插件，ChatGPT Web 中直接选择 Clear Writing | Plugin Creator 回读只有一个顶层 Skill；两个 manifest、版本、scope、discoverability 与现有身份一致；旧顶层 Skill 路径已删除 | 仍暴露多个顶层 Skill、旧文件残留、创建第二个同名插件或身份漂移 | PIE、其他个人插件和 Codex Marketplace 不受影响 | 是 |
| `CW06-G2` 路线覆盖 | 单入口能区分普通回复、正式中文文档、结构重写、英文科研、UI 文案和精确机器内容 | 自然用户请求，不出现内部 Skill 名 | 每个代表任务进入正确合同并产出对应质量；exact-only 不被污染 | 需要用户手工指定内部路线、错误路线接管或纯机器内容被改写 | 现有六项职责和四类 should-not-change | 是 |
| `CW06-G3` 多产物绑定 | 同一请求中的聊天回复与外部文档分别处理，最终文档真实写回 | 真实 GitHub/Drive/文件任务，显式选择 Clear Writing | 已知 Reader Guide 回放；目标枚举、完整源读取、候选、写入、回读、最终文档和聊天回复均可定位 | 只改善聊天回复、文档未改/改错目标、未回读却声称完成 | 只读审查不得误写；单一聊天任务不得制造外部产物 | 是，release-critical |
| `CW06-G4` 保真与权限 | 清晰表达不改变事实、公式、引用、权限、状态或机器字符串 | 包含正式名称、路径、状态和混合内容的真实任务 | source 与 final artifact 对照；受保护内容保持，普通解释自然化 | 删除/增强主张、改权限或状态、翻译机器 token、遗漏限制 | 现有 writing-fidelity 和 exact bypass | 是 |
| `CW06-G5` source/generated parity | ChatGPT wrapper 不形成第二份专业规则来源，Codex 六 Skill 继续可用 | 构建、安装和正常回放 | route reference hash 对齐 canonical source；Codex profile/Marketplace direct routes 回归通过 | 人工复制漂移、Codex route 被折叠或跨插件 handoff 失效 | Research Authoring、Presentations、统计和科研图等下游不被接管 | 是 |
| `CW06-G6` 完整产物定性与泛化 | 修复不是针对 Reader Guide 的一次性特判 | 一个冻结后的 fresh 长技术文档任务，由独立线程评审 source 与完整 final artifact | Reviewer 可访问全文，先判保真再判可读性；同一最终候选通过 | 只看摘要/截图/聊天回复，或看过样本后继续调候选 | 已知正例不能因追求简短而退化 | 是 |

Gate 数量不以越多越稳为目标。实现阶段先跑确定性 source/parity 和 known regression，再运行真实 Web 和 fresh 定性验收。不得把 schema、文件数、receipt 或 Skill load 自述冒充 `CW06-G3/G6`。

## 十、实施顺序

本 Proposal 获得 `PROCEED` 后，Planner 才准备 execution-ready Plan。预计顺序为：

1. 冻结 0.6 ChatGPT wrapper package shape、旧路径删除清单和构建 source ownership；
2. 用 Plugin Creator 当前 release 做只读清单和可逆包装探针，不修改正式插件；
3. 冻结完整 Gate 输入、评审标准、回读方式和停止条件；
4. 独立 Critic 做 execution-ready 审查；
5. 用户批准 Kickoff 后由 Codex 使用 `workflow-core + ai-skills-core + writing-style` 实现；
6. 先完成 repository source/generated、tests、known regression 和 Codex compatibility；
7. 更新现有 Personal Plugin，保留同一 plugin identity，并删除旧顶层 Skill 路径；
8. 在真实 ChatGPT Web 运行 `CW06-G1..G5`；
9. 冻结后运行 `CW06-G6`；
10. 独立实现/产物审查、版本和 changelog 收口；
11. 形成 repository PATCH release，并更新现有个人插件到 `0.6.0`；
12. Issue `#13` 只有在其原有其他 required consumers 也满足时才可 DONE；0.6 成功不自动关闭 #13。

当前 Proposal 不创建 Goal/Kickoff，不修改 production source，不更新个人插件，也不执行真实 Gate。

## 十一、版本与兼容性

如果 0.6 最终改变正式用户行为并完成发布：

```text
Repository bump decision: PATCH
Reason: existing Clear Writing plugin receives a compatible normal-entry and artifact-finalization improvement.

Affected plugins:
- writing-style: 0.5 -> 0.6
- all other central plugins: NO_BUMP
```

个人插件使用三段平台版本：`0.5.0 -> 0.6.0`。中央插件仍按仓库规范使用两段版本 `0.6`。

不改：

- plugin slug `writing-style`；
- display name `Clear Writing`；
- 现有 Personal Plugin ID；
- Research Authoring、Presentations、PIE 和其他插件版本；
- maturity；
- 当前 Project setting；
- 现有 automatic-every-turn claim boundary。

## 十二、风险、反证和恢复

### 风险 1：单入口仍不能稳定执行外部文档终审

若唯一入口已真实加载，但 `CW06-G3` 仍失败，则“多 Skill 并列”不是充分解释。立即停止；不得继续给入口 Skill 增加更多同义规则。Planner 必须重新判断是否需要受控 App/MCP 写入层、宿主 connector 工作流或更窄的产品承诺。

### 风险 2：包装迁移留下旧 Skill 文件

Plugin Creator 更新采用 overlay 语义。旧六路径若未显式删除，单入口架构只是表面变化。执行 Plan 必须冻结当前 release 文件清单和 exact `delete_paths`，更新后逐文件回读。

### 风险 3：个人插件与 canonical 六 Skill 漂移

通过确定性构建、source hash、generated parity 和正式 release closure 处理。不要靠人工复制或 27/27 手工比对作为长期维护机制。

### 风险 4：把 Clear Writing 扩成文档作者或领域裁判

总入口只拥有交付对象、路线和最终化。报告信息架构、幻灯片叙事、统计结论、科研图编码和医学/生物解释继续属于相应领域插件。

### 风险 5：为了修长文而破坏短答和精确输出

`CW06-G2/G4/G5` 必须保留普通短答、必要长答、正式结构和 exact-only should-not-change。不得使用固定长度、英文比例、标题数量或禁词表。

### 风险 6：误把工作合同说成平台硬 Hook

0.6 是 skills-only 工作流改进，不是平台发送前 finalizer。所有对“写入必经”“回读必经”的主张必须由真实 Web 正常入口证据支持；做不到就降低 claim，不通过文字宣布强制性。

## 十三、Planner 对此前归因的修正

此前回答中以下两点成立：

- PIE 的单 Skill 入口明显减少了二次路由不确定性；
- Clear Writing 当前多 Skill 包装缺少一个负责整轮结果的入口。

但“因此只要加一个 coordinator 就能修好”过度简化。PIE 与 Clear Writing 的差异还包括：

- PIE 是窄任务，Clear Writing 是多任务族；
- PIE 主要返回一个当前回答，Clear Writing 可能修改外部产物；
- PIE 的唯一 Skill 拥有从输入门槛到最终输出的完整合同；
- Clear Writing 需要按交付对象组合多条专业路线。

所以 0.6 的正确修改不是简单新增第七个兄弟 Skill，而是：

> **把 ChatGPT Personal Plugin 改为唯一总入口，并把六项能力作为该入口的受控 route references；同时增加交付对象枚举、候选先于写入、写入后回读和逐对象完成声明。**

这项归因是否充分、单入口是否过重或仍然过简、是否应该改 manifest/包装而不是 Skill 语义，必须由独立 Critic 重新审查。本 Proposal 不自行批准。

## 十四、维护看板

复用 Issue `#13`，不创建新的 top-level tracking Issue。当前开始新的实质设计轮次后，正确 lifecycle 应回到：

```text
Status = DOING
Area = writing-style
Execution anchor = 本 Proposal 的最终提交
Next action = independent design Critic review of Clear Writing 0.6 proposal v0.1
Resolution commit = empty
```

当前 ChatGPT surface 没有 GitHub Project 字段修改能力，因此以上为待下一次 Project-capable AI Skills Maintainer 同步的准确 mutation；不得声称 Project 已同步，也不要求用户手工拖卡片。

## 十五、独立 Critic 必须回答的问题

1. 本 Proposal 是否正确区分了“显式插件选择已发生”和“正确 Skill/产物路线未被可靠消费”？
2. 六个并列 Skill 是否确实构成必须修复的产品架构缺口，还是仅需更小的 metadata/提示词修复？
3. PIE 是否只是相关先例，还是被 Planner错误类比？
4. 单入口 + route references 是否能在不复制专业规则的前提下工作？
5. `clear-writing` 是否变成了多余的第七领域 Skill，还是合理的 ChatGPT surface adapter？
6. 外部写入前终审、写入后回读是否在 skills-only 平台上有真实可执行路径，还是未经证实的纸面合同？
7. 个人插件与 Codex 插件采用不同 exposure 是否会形成不可接受的双重产品语义或维护漂移？
8. `CW06-G1..G6` 是否覆盖了本次真实失败、正常入口、完整产物、保真、兼容和泛化，同时没有重复过重？
9. 是否需要在 0.6 就引入 MCP/App，还是应先验证最轻的单入口 wrapper？
10. 哪些决定仍未冻结，是否足以阻止进入 execution-ready Plan？

## 参考资料

仓库来源：

- `AGENTS.md@aa2e6ade13cf6e038a69ec4a2b5fbe318bebed39`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md` v1.7
- `docs/workflows/CRITIC_ROLE_CONTRACT.md` v1.7
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md` v1.2
- `docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md`
- `docs/workflows/CONTINUOUS_REAL_WORLD_SKILL_REFINEMENT.md`
- `docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md`
- `docs/plugin-todos/writing-style.md`
- `docs/design/READER_FACING_COMMUNICATION_PLUGIN_BOUNDARIES.md`
- `skills/writing/core/{writing-fidelity,response-clarity,product-ui-copy,scientific-prose,scientific-rewrite,chinese-prose}/`
- `plugins/codex/plugins/writing-style/.codex-plugin/plugin.json`
- Issue `#13`
- `YuukiAS/AI_Research_Toolkit@0ff0f43f3b04286273490e4c4870975f4aa7a7f8` 的 Delivery Assurance Reader Guide

当前运行时证据：

- Plugin Creator 回读：Clear Writing `0.5.0`，六个顶层 Skill，仅 `.codex-plugin/plugin.json`；
- Plugin Creator 回读：Project Instructions Editor `0.2.8`，一个顶层 Skill，双 manifest，带 reference；
- 用户提供的显式 `$clear-writing` 调用截图及后续失败对话。

外部官方资料：

- OpenAI, “Plugins in ChatGPT”: https://help.openai.com/en/articles/20001256-plugins-in-chatgpt
- OpenAI, “Skills in ChatGPT”: https://help.openai.com/en/articles/20001066-skills-in-chatgpt
- OpenAI Developers, “Skills”: https://developers.openai.com/plugins/concepts/skills
- OpenAI Developers, “Build skills”: https://developers.openai.com/plugins/build/skills
- OpenAI Developers, “Package your plugin”: https://developers.openai.com/plugins/build/plugins
