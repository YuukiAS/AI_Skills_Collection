# 最终用户阅读层：跨 Project 回答终审架构 Proposal

- Proposal version: `v0.1`
- Date: `2026-10-06`
- Planner base main: `36e854fe06779400e2e1279083a34803c7c62a48`
- Tracking: `#13`
- Status: `READY_FOR_CRITIC_REVIEW`
- Architecture decision: `EXTEND_CLEAR_WRITING_WITH_A_DEDICATED_BUNDLED_SKILL`
- Scope: 研究、架构与正式验收设计；不授权实现、不创建 Executor、不修改 live Plugin、不启动 paid API、automation 或发布。

## 0. 结论

这个问题不再属于 Project Instructions Editor（PIE）的规则编辑质量，也不能靠给每个 Project 再加一段同义说明来解决。C5–C11 已经证明：当“领域判断、来源材料、语言规则、自检”全部混在同一次生成里时，模型仍会把来源中的普通英文、内部阶段名、状态字段和日志式结构带进最终回答；再增加规则只会让合同更长，不会产生真正独立的发送前处理阶段。

正式职责应改为：

1. **Clear Writing（plugin slug 仍为 `writing-style`）成为最终用户阅读层的唯一中央负责人。**
2. 在现有 Plugin 内新增一个范围明确的 Skill：`reader-layer-finalization`，用户可见名称建议为“最终用户阅读层终审”。它负责普通聊天回答最后一层的语言、信息组织、机器内容分层和语义保真，不负责科研、工程、统计、权限或事实判断。
3. 不依赖一个 Skill 在运行时调用另一个 Skill。新 Skill 必须在一次被加载后拥有完成终审所需的紧凑合同；它可以复用 `chinese-prose` 与 `writing-fidelity` 的中央规则来源，但不能把“先调用 A、再调用 B”当成平台保证。
4. 普通 ChatGPT Web 的正常入口采用四层防护：安装/预装 Clear Writing、Skill 元数据路由、Project 内一条短激活桥、Project 外的全局 Custom Instructions 兜底。领域 Skill 继续拥有事实和结论，最终阅读层只重写已经形成的语义。
5. 当前平台没有公开支持普通 ChatGPT Web 的通用发送前钩子、强制 Skill 顺序、Skill→Skill 调用接口，或无需额外凭据的独立第二次模型调用。因此本方案不能声称存在真正机械隔离的第二阶段；它追求的是正常使用下显著、可重复提升，并把平台限制写进产品合同和验收门。
6. Codex hook、Workspace Agent、外部模型服务可以提供更强的阶段分离，但都不满足“普通 ChatGPT Web、零额外 API key、零独立托管、无额外操作”的正常入口，故只保留为非默认高保障路线，不进入最小成熟实现。

这不是创建另一个写作插件，也不是把 Clear Writing 变成领域作者。它是在现有语言与保真能力之上，补齐一个此前没有被正式拥有的产品表面：**普通聊天回答的最后阅读层**。

---

## 1. 问题重新定义

### 1.1 用户真正遇到的不是“不会翻译”

当前失败通常发生在模型已经读懂内容之后。来源使用英文仓库、论文、Skill、Plugin、日志或 Planner/Critic 文档时，模型会把以下内容误当成应保留的正式术语：

- 普通工程、科研、统计和流程词；
- 来源标题、阶段名、机制名和设计标签；
- 内部审计角色、状态字段和验收术语；
- 原始日志、路径、哈希和字段名；
- 为模型组织思路而存在的框架，而不是用户需要看到的结论。

结果不仅是中英夹杂，还包括机械换行、单字段成段、状态块堆叠、裸日志代替判断、先讲内部审计再讲用户结论，以及同一结论用多个状态字段重复表达。

因此，产品目标不是“翻译英文词”，而是：

> 在领域判断完成后，把将要发送的内容重新组织成适合当前用户、当前语言和当前任务的完整回答，同时严格保持事实、条件、权限、安全、证据强度、不确定性、时间关系、完成状态和精确标识。

### 1.2 已有需求合同并不缺语义

AI Research Stack 当前 Project instructions 的“0. 面向用户的输出规范”已经覆盖：

- 默认自然、连续、专业中文；
- 普通概念只要中文准确就应中文化；
- 来源使用英文不构成保留理由；
- 标题、列表、表格、总结和结论同样受约束；
- 只有需要复制、执行、搜索或唯一定位的正式字符串保留；
- 机器内容与解释正文分层；
- 非必要换行、状态块和裸日志属于失败；
- 重写不得改变事实、权限、安全、证据强度、不确定性、强制/可选关系或结论边界。

缺口不是再补一条同义语义，而是让这一合同在普通回答的正常入口中被稳定消费。

### 1.3 本轮不延续 C11

本轮不是：

- C12；
- C11 的修复；
- PIE 的新规则模板；
- Server+VPS 特判；
- 英文关键词清单或比例评分；
- 固定三段式回答模板；
- 旧 MCP/API finalizer 复活。

C5–C11 作为失败证据和回归集保留，但不再作为同一实现路线的下一编号。

---

## 2. 真实历史给出的架构约束

关键历史身份：

- C11 reader-baseline candidate: `187212887bc8f7a339cd43097384df35c1e71baf`
- Gate evidence: `9824d0501dea233442d3f0aca85e319f757bbe27`
- Critic stop: `1325ffba51be6ecbe46cde7e46492f9e69284c4c`

C5–C11 共同建立了以下事实：

1. **规则存在不等于正常入口会执行。** C6、C8、C9、C11 都出现了规则已经写入、局部自检也声称通过，但完整回答仍泄漏普通英文或内部框架。
2. **同轮读取多个 Skill 不等于阶段分离。** C10-B3 只有在三个独立模型轮次中按“冻结语义→读者实现→保真复核”传递时才稳定通过；一次推理中同时读取两个 Skill 仍属于同一生成过程。
3. **语言优化本身可能改变语义。** C7 曾把已删除、已拒绝或仅属历史的内容重新写成长期规则。最终阅读层必须把用户纠正、拒绝、删除、接受和完成状态视为受保护语义。
4. **完整回答才是产品。** 文件存在、fixture PASS、字符串扫描、自检声明和哈希都不能替代真实 ChatGPT Web 完整回答验收。
5. **旧路线应冻结。** C11 Critic 已明确停止继续增加 baseline、自检和 exactness 说明；后续必须转向职责、消费路径和产品入口。

这些结论否定的是“继续强化同一提示词循环”，不是否定所有同次推理中的改进价值。由于普通 ChatGPT Web 当前没有公开的独立发送前模型阶段，最小现实方案仍只能在同一回答内建立逻辑边界；但必须明确这是能力边界，而不是把它包装成真实第二次调用。

---

## 3. 2026-10 官方产品现实核查

本轮只采用 OpenAI 最新官方文档支持产品事实，核查日期为 `2026-10-06`。

### 3.1 Skill 与 Plugin 的正常触发

官方文档说明：

- 安装后，ChatGPT 可以在“有帮助”时自动使用一个或多个 Skills；
- Skill 的名称和描述先被模型看到，完整说明在用户请求匹配或用户直接调用时加载；
- 已安装 Plugin 在“与请求相关”时自动使用，也可通过 `@` 明确选择；
- 工作区可把 Plugin 的安装策略设为 `Installed`，让符合条件的成员自动安装。

这提供了可行的正常入口，但没有提供“每条回答必经”的承诺。预装解决的是可用性，不是强制执行。

### 3.2 Plugin 内多个 Skills 的边界

官方文档说明 Plugin 可以包含多个 Skills，Skill 可以定义工具顺序和最终输出要求；但没有公开一个 Skill 调用另一个 Skill 的接口，也没有公开多个 Skills 的确定顺序、独立上下文或独立模型轮次。

因此，本方案禁止把以下伪架构写成正式合同：

```text
domain skill -> calls finalizer skill -> calls fidelity skill
```

新终审 Skill 必须在自身被加载时具备完整、紧凑、可执行的职责，不把 Skill 链当作平台能力。

### 3.3 不存在可用于普通 ChatGPT Web 的通用发送前 hook

OpenAI Plugin 文档中的 lifecycle hooks 属于 Codex runtime，包括 ChatGPT Work 和 Codex。官方明确说明：网页安装 Plugin 不会部署 hook 脚本，脚本还需要存在于执行环境并通过信任审查；迁移指南也明确要求普通 Chat 不要依赖 hooks。

因此：

- Codex 的 `Stop` 等 hook 不能冒充普通 ChatGPT Web 发送前钩子；
- 新 Plugin 也不能强制所有聊天回答先经过脚本；
- Plugin 扩展提供侧栏、输入框、文件查看器或交互界面，不等于回复拦截器。

### 3.4 Project instructions 与 Custom Instructions

官方说明 Project instructions 只在该 Project 内生效，并覆盖全局 Custom Instructions；在部分工作区 Project 模式中，项目内甚至只提供 Project instructions。

因此：

- 全局 Custom Instructions 可以作为非 Project 聊天的兜底；
- 它不能替代 Project 内的一条短激活桥；
- 也不能靠一份全局长模板覆盖所有 Project 的语言和机器输出边界。

### 3.5 独立第二次模型调用

本轮未在官方文档中找到以下原生能力：

- 普通 ChatGPT Web 在回复发送前自动启动独立第二次模型调用；
- Plugin 无条件把草稿交给另一个模型阶段；
- 不使用外部服务、API key、Workspace Agent access token 或用户额外操作的独立 finalization。

Workspace Agents 可从外部系统通过 ChatGPT API channel 异步触发，并需要专用访问令牌；这不是普通聊天中的透明第二阶段。远程 MCP 或外部模型服务同样需要托管、凭据、成本和工具选择，不能作为本产品的默认入口。

### 3.6 官方产品资料

- [Skills in ChatGPT](https://help.openai.com/en/articles/20001066-skills-in-chatgpt/)
- [Skills – Plugins](https://developers.openai.com/plugins/concepts/skills)
- [Plugins in ChatGPT](https://help.openai.com/en/articles/20001256-plugins-in-chatgpt)
- [Connect and test your plugin](https://developers.openai.com/plugins/deploy/connect-chatgpt)
- [Package your plugin](https://developers.openai.com/plugins/build/plugins)
- [Plugin architecture](https://developers.openai.com/plugins/concepts/plugins)
- [Submit your Claude Code plugin to OpenAI](https://developers.openai.com/plugins/guides/submit-claude-plugin)
- [Projects in ChatGPT](https://help.openai.com/en/articles/10169521-projects-in-chatgpt)
- [Workspace Agents](https://developers.openai.com/workspace-agents)

---

## 4. 职责归属方案比较

| 路线 | 判断 | 原因 |
|---|---|---|
| A. PIE 继续负责 | **拒绝作为负责人** | PIE 负责编辑 Project instructions，不拥有每次回答的最终表达；C5–C11 已证明继续强化同一规则层不能解决运行时消费。以后它最多作为一次性部署消费者，保留或写入短激活桥。 |
| B. Clear Writing 扩展 | **推荐** | 现有 `chinese-prose` 已拥有自然中文、去日志腔和读者结构，`writing-fidelity` 已拥有语义保真；TODO #13 已将它定位为通用内容保真语言层。缺的是聊天回答终审产品面。 |
| C. 新 standalone Skill | **拒绝顶级独立身份；接受 Clear Writing 内新增 Skill** | 单独安装的新 Skill 会与 Clear Writing 重复职责、产生两个中央来源和路由竞争。作为 Clear Writing 内的窄 Skill，则能获得清晰触发和独立验收，而不新增产品身份。 |
| D. 新 Plugin | **拒绝** | 新 Plugin 不能获得更强 hook，反而增加安装、路由、版本和边界成本。平台限制不会因换壳消失。 |
| E. 顶部短硬门 | **保留为防御与激活桥** | 它仍然是自然语言指令，不能成为主机制；但引用具体已安装 Skill 后，可以把“风格偏好”改成“必须消费某能力”的路由合同，并为 Project 提供语言/绕过上下文。 |
| F. ChatGPT Web Plugin/Skill 正常入口 | **采用，但不夸大** | 安装、自动相关性路由和 `@` 调试入口是真实存在的；没有每条回答强制触发保证，必须通过真实 Web 验收衡量可靠性。 |
| G. Codex hook / Workspace Agent / 外部第二次调用 | **不作为正常入口** | 能提供更强分离，但只适用于特定表面，或需要脚本、信任、令牌、API、托管和额外成本。可保留为未来高保障路线。 |
| H. 不新增 Skill，只改调用架构 | **不足以单独成立** | 平台没有 Skill 依赖/顺序合同；只在每个领域 Skill 中写“记得润色”会重复 C11。调用架构必须与一个明确、可安装、可验收的终审 Skill 结合。 |

---

## 5. 推荐架构

### 5.1 中央负责人

中央负责人：

```text
Plugin: writing-style
Display name: Clear Writing
New bundled Skill: reader-layer-finalization
User-facing capability: 最终用户阅读层终审
```

现有职责保持：

- `chinese-prose`：中文成稿、解释与长文的具体表达方法；
- `writing-fidelity`：事实、条件、证据、归因、精确标识和用户决定的保真；
- `scientific-rewrite`：已有长文的结构化重写；
- `reader-layer-finalization`：普通聊天回答在发送前的最终阅读层。

新 Skill 不接管：

- Research Authoring 的证据选择、文献整合和科研文档结构；
- statistical-modeling 的模型、假设、推断和结论；
- Server+VPS 的权限、网络、机器状态和执行决定；
- frontend / Figma / code 的产品逻辑与精确实现；
- Planner / Critic 的治理判断；
- 外部事实核查。

### 5.2 单次回答中的逻辑边界

在当前平台约束下，运行合同采用逻辑三步，而不谎称三个独立模型调用：

```text
领域任务形成语义结果
    -> 冻结本次回答的受保护语义
    -> reader-layer-finalization 组织最终可见回答
    -> 对受保护语义做发送前核对
```

“受保护语义”不是新的大型 schema，也不允许输出成状态块。它只要求在重写前识别本次不能漂移的内容，包括：

- 事实、数字、公式和引用；
- 结论强度、条件、比较和因果方向；
- 必须/可选、允许/禁止、已授权/未授权；
- 安全、隐私和权限边界；
- 证据强度、不确定性和已知未知；
- 当前/过去/未来、已完成/未完成；
- 精确标识；
- 用户明确纠正、删除、拒绝、接受的决定。

实现可以使用内部最小记录帮助核对，但不得把它变成用户可见表格、固定字段协议或新的内部日志泄漏。

### 5.3 最终阅读层的具体职责

终审 Skill 同时处理：

1. **语言层**：普通概念使用当前目标语言；来源为英文不构成保留理由；同一概念一旦中文化，后文保持一致。
2. **正式字符串层**：代码、命令、路径、文件名、分支、提交、配置键、枚举、端口、主机名、正式产品/方法/数据集名等，在需要复制、执行、搜索或唯一定位时原样保留。
3. **来源框架层**：来源标题、阶段名、机制标签和 Planner/Critic 字段只有在用户任务本身讨论这些对象时才保留；否则转化为已经消化的判断。
4. **结构层**：先给用户结论、是否需要动作和下一步，再给必要证据；段落按真实信息结构形成，不按内部字段换行。
5. **机器内容层**：必须原样提供的日志、JSON、代码和命令与解释正文分层，不用裸机器内容替代结论。
6. **去重复层**：同一结论不以多套状态块重复；列表只在存在真实并列关系时使用。
7. **跨语言层**：默认服从 Project 的持久语言合同；当前消息明确要求英文、双语或其他语言时只覆盖当前回复，不永久改变 Project。
8. **绕过层**：纯 JSON、纯日志、纯代码、逐字引用、严格协议输出等任务不做自然语言改写；混合任务只改解释层，不改机器块。

### 5.4 不采用禁词表或英文比例

验收不能通过以下方式完成：

- 把 `canonical`、`validation`、`artifact` 等列成固定禁词；
- 规定英文字符比例；
- 规定每个回答固定三段；
- 用关键词 scorer 代替阅读判断；
- 因出现路径或产品名就判失败。

同一个字符串是否保留取决于它在当前回答中的语义角色：正式身份、机器接口或可搜索原文可以保留；普通推理、连接语和内部流程标签应改写。

### 5.5 正常入口

正常使用的最小入口为：

1. Clear Writing Plugin 已安装；工作区允许时可设为自动安装。
2. `reader-layer-finalization` 的 metadata 明确：当 Project / Custom Instructions 声明最终阅读层合同，或用户要求面向读者解释、总结、判断时应加载；纯机器输出和明确语言覆盖属于边界情况。
3. 每个需要稳定生效的 Project 只加入一条短激活桥，不复制整套语言规则。
4. Project 外普通聊天可在 Custom Instructions 放同一意图的短兜底；Project 内仍以 Project instructions 为准。
5. `@Clear Writing` 只用于安装验证、调试和失败诊断，不作为日常前置动作。

建议的 Project 激活桥：

```text
发送面向用户的解释性正文前，必须实际使用已安装的 Clear Writing `reader-layer-finalization`，按本 Project 当前语言合同完成最后阅读层；本条消息明确要求其他语言、双语或纯机器内容时，仅对本次切换或跳过。该终审只改表达和信息组织，不改事实、数值、条件、权限、安全、证据强度、不确定性、完成状态、时间关系或精确标识。未消费即未完成。
```

这段文字不是主能力，也不证明能力已执行；它只负责让已安装 Skill 在相关回答中更容易被真实路由。若当前表面无法加载该 Skill，不得声称已调用；可按 Project 已有紧凑规则尽力完成，但验收记录必须标为降级路径。

### 5.6 PIE 的后续位置

PIE 不再是本能力负责人。若核心能力经实现和验收成立，PIE 可以作为后续消费者适配：

- 在用户明确要求建立/完善 Project instructions，且该 Project 需要阅读层时，插入或保留短激活桥；
- 不复制 Clear Writing 的完整合同；
- 不重新实现语言判断；
- 不声称短桥本身等于终审能力；
- 不产生 C12 编号或继续 C11 路线。

该适配不是最小核心实现的前置条件，也不得与核心 Skill 同时无界扩张。

---

## 6. 跨 Project 与语言行为

### 6.1 AI Research Stack

默认中文；保留公式、路径、提交、Plugin/Skill slug 等必要精确字符串；科研与工程判断由对应领域能力完成。终审负责把来源英文和内部状态消化成自然解释。

### 6.2 Server+VPS

自然中文解释必须与机器身份严格分层。主机名、端口、路径、服务名、命令和状态 token 在需要执行或核对时原样保留；不得为了中文自然把“未授权”“仅备份”“当前离线”等强边界弱化。

### 6.3 CAT-TRACE

模型、定理、符号、数据集和引用保持精确；中文解释不把公式名词、结论强度或“待证明/已证明”状态改写错。短数学表达和正文按 Project 现有排版合同处理。

### 6.4 前端 / Figma / 代码项目

组件名、设计节点、文件、函数和代码身份保持精确；普通产品判断、交互解释和验收结论使用自然目标语言。不得把 Figma 或代码中的英文标签自动升级为用户叙述术语。

### 6.5 英文 Project

终审仍生效，但目标是自然英文、清晰结构和去内部日志，不强制中文。正式中文专名按 Project 合同处理。

### 6.6 双语 Project

服从 Project 已声明的双语边界，例如中文解释、英文正式术语或双语标题。终审不能自行扩大双语范围，也不能把所有精确字符串翻译掉。

### 6.7 当前消息覆盖

“这次请用英文”“只给 JSON”“原样贴日志”等要求只影响当前回复。下一轮恢复 Project 的持久语言和阅读层合同，除非用户明确要求修改长期设置。

---

## 7. 语义保真反例

以下任一变化均为阻断性失败，即使文字更自然：

| 原语义 | 错误终审 |
|---|---|
| “尚未完成真实 Web 验收” | “已经验证可用” |
| “可选的回退路线” | “必须执行的步骤” |
| “当前证据支持，但仍有不确定性” | “问题已经确定” |
| “用户拒绝恢复旧 MCP finalizer” | 把旧路线重新列为默认方案 |
| “只授权读取，不授权写入” | 省略权限边界或写成可修改 |
| “未来实现时再决定版本” | 写成当前已经发布某版本 |
| `g1807htzh01.ll.unc.edu` | 翻译、缩写或改写主机名 |
| source author 的 future work | 改成 assistant 当前要求执行的任务 |
| 原始 JSON-only 请求 | 添加解释段落或改变字段 |
| 安全/隐私警告 | 为了简洁而删除或弱化 |

反过来，下列内容通常应改写而不是机械保留：

- 来源中的普通 `candidate`、`validation`、`routing`、`rollback`；
- 与用户判断无关的 `Gate B3`、内部阶段标题、结果字段；
- 多个重复的 PASS/FAIL 状态块；
- 已经可以概括成一句判断的原始日志；
- 仅用于内部定位、但用户不需要复制或核对的路径和哈希。

---

## 8. 五遍预检

### 8.1 产品

**谁用：** 长期在多个 Project 中使用 ChatGPT Web，要求默认自然中文或 Project 指定语言，同时需要保留科研、工程和机器身份精度的用户。

**正常入口：** 安装的 Clear Writing + Project 短激活桥；用户直接提出领域问题，不需要每次加“说中文”“不要英文”或 `@Clear Writing`。

**最终得到：** 第一条完整回答已经是可直接阅读的结论，而不是需要第二轮纠正的内部备忘录。

结论：产品目标具体、可观察，且与现有 Clear Writing 的语言层身份一致。

### 8.2 现实

官方产品支持相关性自动路由和明确选择，不支持普通 Chat 的通用发送前 hook、确定 Skill 链或无凭据独立第二次调用。

结论：真实可做的是同一回答内的专门终审 Skill + 多层激活和真实验收；不能承诺机械 100% 保证。

### 8.3 替代

**更简单路线：** 只在 Project 顶部放短硬门。成本最低，但 C5–C11 已证明同类规则会漂移，只能作为防御层。

**更成熟、强分离路线：** 外部第二次模型调用、Workspace Agent 或 Codex hook。阶段隔离更强，但需要不同产品表面、令牌、脚本、托管或额外成本，不满足正常入口。

结论：推荐路线是在用户约束下可靠性与负担最平衡的方案。

### 8.4 反证

方案必须主动尝试推翻以下假设：

- Skill 安装了但普通领域问题没有触发；
- Project 写了短桥但模型只口头声称调用；
- 多个 Skills 同轮读取被误报为独立阶段；
- fixture、字符串测试和 direct mention 通过，普通 Web 第一条回答仍失败；
- 英文减少了，但事实、状态或权限发生漂移；
- 当前消息英文覆盖污染后续轮次；
- JSON/log-only 被强行润色；
- 用户仍需要第二轮提醒才得到正常表达。

任何一项成立，都不能把能力宣称为正式可用。

### 8.5 执行合同

只有以下条件同时满足后才允许进入 production implementation：

- 独立 Critic 对本 Proposal、Plan 和 Gate Matrix 的同一版本给出 PASS；
- owner、正常入口、平台边界和回退均被冻结；
- 实现任务只修改获批范围；
- 真实 ChatGPT Web 完整回答验收不可被本地 fixture 替代；
- 版本、changelog、候选身份和回退按现有仓库政策执行。

本轮不满足实现授权条件，仅提交设计供 Critic 审查。

---

## 9. 最小成熟实现

若 Critic PASS，最小成熟实现应只包含：

1. Clear Writing 中一个新的 `reader-layer-finalization` Skill；
2. 紧凑、跨语言、语义保真的运行合同与边界样例；
3. 正确打包进现有 `writing-style` Plugin；
4. 一条可由 Project 使用的短激活桥和 Project 外兜底说明；
5. 直接、间接、跟进、负例和边界激活测试；
6. 跨 Project 的真实 ChatGPT Web 完整回答验收；
7. 独立保真与阅读质量审查；
8. 候选版本、changelog 和可回退安装身份。

明确不在最小实现中：

- 新顶级 Plugin；
- 新 MCP server；
- OpenAI API key；
- 外部模型托管；
- Workspace Agent；
- Codex hooks；
- PIE C12；
- 修改所有领域 Skills；
- 大型中间 schema；
- 关键词/比例评分器；
- 自动改写所有 Project instructions；
- 自动发布。

---

## 10. 发布、版本与回退

### 10.1 当前设计轮次

```text
Repository bump decision: NONE
Reason: 仅提交未实现、未发布的设计与验收合同。
Affected plugins:
- writing-style: NO_BUMP
  Reason: 本轮不修改 production behavior。
- all other plugins: NO_BUMP
```

### 10.2 后续实现轮次

若当前 canonical `writing-style` 版本在实现开始时仍为 `0.4`，完成全部 Gate 后的正式发布候选应评估 `0.4 -> 0.5`；若期间已有其他正式发布，则按版本政策使用下一个两段版本，不在本 Proposal 中硬编码过期版本。Repository 只在真正形成可安装 release 时按政策决定 patch/minor，不能因设计文档或测试数量提前 bump。

### 10.3 回退

最小回退单位为：

- 禁用或卸载候选 Clear Writing 版本；
- 恢复上一正式 Plugin 版本；
- 从试点 Project 删除短激活桥；
- 保留原 Project 语言合同，不删除用户已有规则；
- 不恢复 C11、旧 MCP/API finalizer 或新的临时长提示词。

若真实 Web 证明自动触发不稳定但 direct mention 可用，结果应标为“显式调用工具”，不能冒充正常入口通过。

---

## 11. 风险与停止条件

### 11.1 主要风险

- 终审 Skill 过于宽泛，抢占领域职责；
- metadata 过窄，普通领域问题不触发；
- metadata 过宽，机器输出或英文 Project 被误改；
- 同次推理仍被来源框架污染；
- 为了自然表达而弱化权限、状态或不确定性；
- Plugin 安装/工作区策略在不同表面不一致；
- 测试人员通过 `@` 强制调用，掩盖正常入口失败。

### 11.2 必须停止并返回 Planner 的情况

- 普通 Web 无法在不显式 `@` 的情况下稳定触发；
- 完整回答仍系统性重现 C11 的来源英文和状态块泄漏；
- 语义漂移无法通过 bounded repair 消除；
- 方案需要外部 API key、额外模型费用或独立托管才能成立；
- 实现者试图用禁词、英文比例、固定段数或 synthetic-only PASS 代替产品验收；
- 平台能力与官方文档不一致，关键前提无法验证。

停止后应重新评估产品表面或等待平台提供真实 finalization primitive，而不是继续加提示词。

---

## 12. 待 Critic 判断的核心问题

Critic 应重点判断：

1. Clear Writing 是否确实是唯一合理 owner，还是仍存在职责冲突；
2. 新 bundled Skill 是否比扩写 `chinese-prose` 更清楚、更可触发；
3. Project 短激活桥是否属于必要分发合同，而不是换名的 C11；
4. 对 ChatGPT Web 平台限制的表述是否准确、没有伪造 hook 或第二次调用；
5. 最小实现是否足以产生用户可观察改善，又没有无界扩张；
6. Gate Matrix 是否真正能发现“安装但未消费”“同轮伪分离”“Web 第一条回答失败”和“中文化造成语义漂移”。

若 Critic 认为 owner 或正常入口不成立，应返回 `REVISE`；不要让 Executor 用实现试错替代架构决策。

---

## 13. Planner 决议

```text
PROPOSAL_RESULT = READY_FOR_CRITIC_REVIEW
PRIMARY_OWNER = writing-style / Clear Writing
NEW_TOP_LEVEL_PLUGIN = NO
NEW_STANDALONE_SKILL = NO
NEW_BUNDLED_SKILL = YES (`reader-layer-finalization`)
PIE_PRIMARY_OWNER = NO
PROJECT_SHORT_ACTIVATION_BRIDGE = YES, DEFENSE_AND_ROUTING_ONLY
GLOBAL_CUSTOM_INSTRUCTIONS = OPTIONAL_FALLBACK_OUTSIDE_PROJECTS
GUARANTEED_INDEPENDENT_SECOND_CALL = NO
EXTERNAL_API_OR_HOSTING_IN_MINIMUM_PATH = NO
CODEX_HOOK_IN_NORMAL_WEB_PATH = NO
PRODUCTION_IMPLEMENTATION_AUTHORIZED = NO
TRACKING_ISSUE = #13
NEXT_ACTION = INDEPENDENT_CRITIC_REVIEW_OF_V0_1_PACKAGE
```
