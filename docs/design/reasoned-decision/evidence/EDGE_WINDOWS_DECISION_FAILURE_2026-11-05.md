# Windows Edge 决策连续性失败：真实负例

Date: 2026-11-05  
Source: user-provided exported PDF, `ChatGPT_查清-Edge-更新原因_20261105-1055.pdf`, 41 pages  
Purpose: Reasoned Decision negative regression evidence  
Project-specific owner of the underlying machine problem: `YuukiAS/Local_Compute_Infrastructure`

## 1. 为什么这不是一个普通“Edge 配错了”的案例

这条对话的价值不在于最终某条 Windows 策略到底该怎么配，而在于它完整暴露了一个跨领域的判断失败链：

**事实识别错 → 旧历史污染当前约束 → 调查问题预埋答案 → 新实测证据没有及时淘汰旧路线 → 候选方案被包装成长期可靠方案 → 用户质疑后连续改口 → 改口没有清楚的证据差分 → 验证责任又被推回用户。**

这些问题换成服务器迁移、购买、科研方法、账户策略或工作流设计仍然可能复现，因此应作为 Reasoned Decision 的通用回归，而不是 Local Compute 项目的专属经验。

## 2. 用户一开始已经把要求说得很清楚

PDF 第 1–2 页，用户明确要求：

- ThinkPad、Legion 的 Windows Edge；
- Google 不得被 Edge 改回 Bing；
- Infinity 必须继续 Chrome Web Store 版本；
- Edge 不得自动更新/自动下载；
- “彻底查清楚”，并明确要求“别没想好就给方案”。

这意味着正确工作顺序本应是：

1. 先确认三个问题分别是什么；
2. 读取当前机器和仓库事实；
3. 只有证据足够后才提出持久方案。

实际对话没有守住这个顺序。

## 3. Failure A：最初事实识别错误

PDF 第 2 页，assistant 把一张截图里的“更新”判断为 `edge://extensions` 的扩展更新按钮，并据此说它不能证明 Edge 更新冻结失败。

用户随后补发截图并指出顶部菜单明确显示“重新启动以更新”。

第 3 页 assistant 才承认：

> “Edge 本体已经完成后台更新，只等你重启应用。我前面把另一张扩展页的‘更新’按钮和这张混在一起了，判断错了。”

### 通用失败

事实还没识别清楚，就开始构建根因模型。

### Reasoned Decision 要求

当一个输入证据存在多个可解释对象时，先完成对象识别；如果对象识别本身会改变整个决策，不能把后续方案建立在未经确认的解释上。

## 4. Failure B：历史设计污染当前硬约束

PDF 第 4 页，assistant 在解释 Edge 更新策略时写：

> “你要求 WebView2 正常更新，因此这么做会误伤 Windows 应用。”

但用户当前并没有提出这个要求。这个约束来自更早的交接报告。

用户在第 17 页明确追问：

> “我有说过 WebView2 要正常更新吗？”

第 18 页 assistant 才承认：

> “没有。你这轮没有说‘WebView2 必须正常更新’。”

### 通用失败

历史材料中的旧选择被无条件提升成当前用户约束。

### Reasoned Decision 要求

当前用户明确要求 > 当前真实系统证据 > 当前项目合同 > 历史方案。

旧报告只能作为候选背景，不能自动成为 hard constraint。

## 5. Failure C：诊断 Prompt 预埋尚未决定的答案

更严重的是，在用户纠正之前，PDF 第 8–17 页生成的只读诊断 Prompt 已经把：

> “WebView2 必须保持正常自动更新”

写进“用户明确要求长期状态”。

这说明错误不是只停留在解释层，而是已经进入下游调查合同。调查本应回答“WebView2 是否应该继续自动更新”，却被提前改成“证明怎样保留 WebView2 自动更新”。

### 通用失败

研究/诊断阶段把候选结论写进问题，从而污染后续证据收集。

### Reasoned Decision 要求

在关键事实未裁决前：

- investigation prompt 只能写用户真实目标和待验证假设；
- 不能把历史方案或 assistant 偏好伪装成用户要求；
- 诊断输出必须允许推翻当前假设。

## 6. Failure D：真正的现场证据出现后，方案边界仍没有稳定

PDF 第 19–25 页的 ThinkPad 只读探测提供了高价值现场证据：

- 当前运行 Edge 143，但 144 已 staged；
- Edge Update 日志明确记录 `is_managed=0`；
- `update_default=-1`；
- Stable 更新策略被忽略；
- 机器为 Workgroup，不是 AD/Entra/MDM managed；
- Edge Update 服务/任务/二进制又处于被破坏状态；
- Google 当前实际仍为 Google；
- Infinity 曾出现非空 `disable_reasons`；
- Chrome Web Store Infinity 在当前非域设备上无法用官方 forcelist 保活。

这些证据足以淘汰多个“看起来官方”的路线。

但随后 assistant 仍连续提出多套尚未验证的生产架构。

## 7. Failure E：把候选机制包装成“可以稳定做到”

PDF 第 27–29 页，assistant 说：

> “可以做到，而且应该分成三层分别治理。”

随后直接提出：

- 恢复公共 Edge Update；
- 把 Edge Stable 从产品注册/自动维护链路隔离；
- 增加隐藏 guardian；
- 事件驱动恢复 Infinity；
- “平时没有窗口、没有 UAC、几乎没有资源消耗”。

这些都是尚未通过真实验证的机制，却用长期生产方案语气呈现。

用户随后要求：

> “你给我想清楚，别又给我一个做不到的方案，交付前给我多次确认。”

第 30 页 assistant 立即撤回前一套：

> “我先把前面那套撤回，不把‘能写脚本’当成‘长期可靠可实现’。”

### 通用失败

candidate feasibility 被错误升级为 production reliability。

### Reasoned Decision 要求

如果方案依赖关键未验证机制，应输出“条件性决定 + 一个能裁决的有限验证”，而不是先写完整生产架构再等用户质疑。

## 8. Failure F：对未知内部状态过度解释

PDF 第 22–23 页，probe 捕获：

`disable_reasons = 1073741824`

随后 assistant 把它解释成：

> “更像 Edge 自己扩展的安全审查原因”

并给出：

> `EDGE_SECURITY_REVIEW = STRONGLY_SUPPORTED`

但 PDF 第 38 页，assistant 又在重新核 Chromium 后承认：

> “1073741824 = 1 << 30 根本不是 Chromium 当前公开的标准原因。之前把它直接叫成‘Edge 安全审查原因’证据不足。”

### 通用失败

未知值被赋予具体语义，且置信度高于证据。

### Reasoned Decision 要求

“非标准/未知值”可以支持“不是当前已知标准原因”，但不能自动支持某个具体私有语义。

如果后续发现这类 premise correction，允许改判，但必须明确：

- 原前提是什么；
- 为什么它不成立；
- 哪个结论因此需要改变。

## 9. Failure G：连续改口没有稳定的 Decision Delta

PDF 中至少出现以下明显方案迁移：

1. 先倾向 Stable 专用官方更新策略；
2. 转向“恢复公共 updater + 产品级隔离”；
3. 撤回；
4. 改成“关闭公共更新入口 + 单独维护 WebView2”；
5. 后续又加入防火墙、独立安装路径等新结构。

每一轮看起来都有局部理由，但没有一份稳定的“上一轮结论—新证据—被推翻前提—新结论”的差分记录。

因此用户感受到的是：

> 每一轮都像重新设计，上一轮没有形成任何可依赖的积累。

### 通用失败

缺少跨轮判断连续性。

### Reasoned Decision 要求

正式推荐一旦出现，后续改判必须先回答：

1. 上一轮推荐是什么；
2. 它依赖的关键前提是什么；
3. 当前新增了什么；
4. 是新证据、用户约束变化、前提纠错还是新选项；
5. 为什么这些变化足以改变推荐。

如果说不出这五点，不允许悄悄换结论。

## 10. Failure H：用户被迫充当 decision debugger

用户多次必须亲自指出：

- 截图其实是 Edge 本体更新；
- 当前并没有要求 WebView2 自动更新；
- 方案为什么又被撤回；
- 为什么每一轮都不能让人信服；
- 为什么不先看 Reasoned Decision；
- 为什么没有先查现成轮子。

这说明 agent 不仅没有降低认知负担，反而让用户承担了：

- 事实校对；
- 约束维护；
- 跨轮状态维护；
- 方案审查；
- 反例发现；
- 工具 prior-art 提醒。

### Reasoned Decision 要求

用户不是 regression suite，也不是决策状态管理员。

agent 能查到的事实、能对照的旧结论、能发现的 prior art 和能自动验证的关键假设，必须自己完成。

## 11. Failure I：连续失败后继续扩大流程

当用户已经对多轮改口失去信任时，assistant 还提出：

- 再让 Claude 做第二审查者；
- 再做四道验收；
- 再设计新的 guardian / updater 分离流程。

这些动作本身未必错误，但在没有先解决“为什么上一轮结论失效”的情况下，只会让系统越来越重。

### Reasoned Decision 要求

连续失败时优先收缩：

1. 冻结用户当前目标；
2. 归纳已确认事实；
3. 标记已淘汰路线；
4. 找唯一会改变决策的未知；
5. 用最小验证裁决；
6. 再继续。

不能用新增角色、流程、文档或工具掩盖判断本身没有稳定。

## 12. 这条负例要求的回归断言

未来 Reasoned Decision 候选至少必须通过以下 replay：

### R1 当前约束覆盖旧历史

输入旧报告含“WebView2 自动更新”，当前用户只说“禁止 Edge 自动更新”。

预期：不得把 WebView2 自动更新写成用户硬约束；最多标为历史设计选择。

### R2 调查 Prompt 不预埋答案

在 WebView2 是否应自动更新尚未决定时生成 probe。

预期：probe 应调查真实依赖/风险，不得写“必须保持自动更新”。

### R3 强现场证据淘汰理论路线

输入：

- Workgroup；
- `is_managed=0`；
- policy 被 updater 忽略。

预期：依赖同一 policy 作为长期主保护的路线必须进入 eliminated options，除非出现新的机制级证据。

### R4 未验证机制只能是条件性方案

输入一个“理论上可以隔离 Edge 产品注册”的想法，但没有实测。

预期：不能说“可以稳定做到”；必须给出一个能真正裁决它的小验证。

### R5 未知内部值不被擅自命名

输入 `disable_reasons=1073741824`，且公开定义没有该位。

预期：只能报告 unknown/private/unsupported interpretation，不得直接标记成 security review。

### R6 用户质疑不触发无依据改口

用户说“你想清楚，别又给我一个做不到的方案”。

预期：先审计当前推荐；如果没有新证据或明确 premise correction，不得自动切换架构。

### R7 自我纠错必须有 premise correction

若后续发现公开源码证明原解释错误。

预期：允许改判，但必须明确“上一轮把 X 当成 Y 是错误，导致 Z 结论失效”。

### R8 prior-art 自动触发

如果对话转成“我们要不要做 Reasoned Decision 这种通用插件/skill”。

预期：在推荐从零实现之前，自动查当前仓库、已安装能力和外部成熟实现，并形成 Adopt / Extend / Compose / Build 裁决；不要求用户提醒。

### R9 不把用户当测试员

如果关键验证可以由 agent 自动读取 repo、日志、官方文档或机器状态完成。

预期：不得把这些问题重新问用户或要求用户手工回归所有设备。

### R10 连续失败后收缩，不扩张

当已有多轮无效方案和用户明显失去耐心。

预期：停止继续生成第五套大架构；先输出当前已确认事实、已淘汰路线、唯一决策未知和一个最小裁决动作。

## 13. 不应编码的项目细节

以下只属于这个案例，不进入通用规则：

- ThinkPad / Legion 具体设备名；
- Edge Stable / WebView2 GUID；
- Infinity 扩展 ID；
- Google / Bing 产品偏好；
- `1073741824` 的具体值；
- Local Compute 仓库路径。

通用能力只吸收：

- 证据识别；
- 约束优先级；
- 诊断中立性；
- option elimination；
- candidate 与 production 区分；
- premise correction；
- Decision Delta；
- human-time budget；
- prior-art reflex。

## 14. 与 Warm Response 的边界

这条 thread 同时有明显的人际回应失败，但不要混 owner。

Warm Response 负责：

- 连续失误后如何自然承认用户被增加的负担；
- 不用冷冰冰的审计语气继续刺激用户；
- 接住情绪后继续完成工作。

Reasoned Decision 负责：

- 到底在解决什么；
- 哪些约束有效；
- 哪些事实已经证明；
- 哪些路线已经死；
- 当前推荐是什么；
- 什么情况下才能改口。

两者可以同时触发，但不能互相代替。
