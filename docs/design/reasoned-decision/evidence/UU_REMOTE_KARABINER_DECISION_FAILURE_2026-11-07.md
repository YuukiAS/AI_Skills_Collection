# UU Remote + Karabiner 体验对齐：连续局部解法导致判断漂移

Date: 2026-11-07  
Source: PC+Server+VPS / Legion Y9000P → UU Remote → Mac mini  
Purpose: Reasoned Decision 真实负例。本文记录判断过程为什么反复，以及应该怎样收敛；不是 Local Compute 的最终实现规格。

## 用户真正要解决的问题

用户不是只想修好 ChatGPT 的 `Ctrl+Enter`。

真实目标是：

- Legion Y9000P 通过 UU 远控 Mac mini 时，键盘体验尽量与直接在 Mac mini 上使用 Dell Windows 键盘一致；
- 普通应用里的 `Ctrl+A/C/V/Z/S` 等保持 Windows 使用习惯；
- ChatGPT 等应用继续使用已有的应用专用语义；
- Terminal / iTerm 中不能因为全局换键而破坏 `Ctrl+C` 等终端控制语义；
- 尽量复用现有 Karabiner canonical，不为了远控再堆一套难维护的快捷键系统；
- 最终需要一个明确答案：这个目标能否实现、能做到什么程度、推荐路线是什么、还有什么必须验证。

## 已确认的现场事实

1. Mac mini 直接连接的 Dell Windows 键盘可以正常使用现有 Karabiner 规则。
2. UU 的 macOS 按键映射截图显示：Windows `Ctrl` 发送为 macOS `Control`，`Alt` 为 `Option`，`Win` 为 `Command`。
3. Legion 经 UU 远控时：
   - `Ctrl+A` 不是全选，而是触发 macOS 原生 `Control+A` 的行首行为；
   - ChatGPT App 的 `Ctrl+Enter` 不能发送；
   - `Win+Enter` 也不能发送。
4. `YuukiAS/Local_Compute_Infrastructure` 的 canonical Karabiner 已经存在：
   - `Ctrl+A -> Cmd+A`；
   - `Ctrl+C/V/X -> Cmd+C/V/X`；
   - ChatGPT / Codex 的 `Ctrl 或 Fn+Enter -> Cmd+Enter`；
   - Terminal / iTerm、Edge、Notion 等应用专用规则。
5. 因此问题不是“缺少这些快捷键规则”，而是 UU 远控输入没有像实体 Dell 键盘一样进入同一条 Karabiner 处理路径。
6. Karabiner 16.3.0 已具备 CGEventTap fallback，可用于接收不经普通 HID 路径的键盘事件；但 CGEventTap 事件没有可靠的物理设备身份。这意味着“能接住远控输入”和“能直接冒充 Dell 设备”是两个不同问题。

## 多轮回答是怎样失控的

### 第一轮：把问题缩成 ChatGPT 的发送键

最初回答根据 UU 截图和已有 ChatGPT 规则，推断远控 `Ctrl+Enter` 没有被转换成 `Cmd+Enter`，然后要求用户额外测试 `Win+Enter`。

这个判断只覆盖了一个症状，没有先确认用户真正要的是“整套远控键盘体验与实体 Dell 一致”。因此测试即使成功，也只能说明某个按键能发送，不能解决整体问题。

用户随后补充 `Ctrl+A` 会跳到行首，证明问题明显超出 ChatGPT。

### 第二轮：直接建议 UU 全局改修饰键

随后回答建议把 UU 设置成：

- `Ctrl -> Command`
- `Alt -> Option`
- `Win -> Control`

这能让普通应用中的部分 Windows 快捷键看起来恢复正常，但它把“普通桌面快捷键”误当成了完整需求。

用户追问后才暴露关键冲突：实体 Dell 的体验并不是简单的全局 `Ctrl -> Command`。现有 Karabiner 会按应用区分语义，例如普通应用和 Terminal / iTerm 的 `Ctrl+C` 需要不同处理。UU 的静态全局修饰键映射不能复刻这种按应用变化的行为。

因此这轮把局部可行方案过早升级成了长期方案。

### 第三轮：从一个局部解法跳到另一个局部解法

在认识到全局换键不够后，回答又很快转向 Karabiner 的 `CGEventTap fallback`，认为可以让 UU 注入事件进入现有规则。

方向比上一轮更接近真实需求，但仍然没有先完成两个关键检查：

1. 现有 canonical 里哪些 Windows 语义规则对“无设备身份事件”已经可复用；
2. 哪些规则严格依赖 Dell / Xiaomi 的设备身份，fallback 即使接到事件也不会自动获得与实体键盘完全相同的行为。

因此“打开 fallback”本身仍不能直接升级成最终长期方案。

### 第四轮：用户显式要求按 Reasoned Decision 重做

这时才按 Reasoned Decision 的冻结设计重新执行：

- 先冻结当前问题：目标是“Legion 远控体验尽量等同实体 Dell”，而不是修某个快捷键；
- 读取 Local Compute canonical，而不是根据单个症状继续猜；
- 调查 Karabiner 当前原生能力及其限制；
- 检查现有规则对有设备身份和无设备身份输入的覆盖；
- 淘汰“UU 全局换键”作为完整方案；
- 淘汰“只开 fallback 就结束”作为完整方案；
- 收敛出一个更符合现有架构的候选方向：让 UU 输入进入 Karabiner，再用一个明确的远控会话状态区分 UU 输入，尽量复用现有 Windows 语义，只为真正依赖实体设备身份的少量规则补远控入口。

这个方向目前仍是 Candidate / Conditionally Recommended，而不是 Production-worthy，因为还缺两个现场验证：

1. 当前 UU 版本注入的键盘事件是否能被 Karabiner fallback 稳定捕获；
2. Mac mini 上能否得到一个稳定、低维护的“UU 远控会话正在进行”信号。

只有这两个前提通过，才有资格把该方向升级为长期实现。

## 这个案例对 Reasoned Decision 暴露的问题

### Task State Integrity

当前问题必须保存为用户的整体成功标准，而不是被最新一个症状替换。

本案中，`Ctrl+Enter`、`Ctrl+A` 都只是证据。真正的问题始终是：

> Legion 远控是否能获得与 Mac mini 实体 Windows 键盘近似一致、且不破坏现有 Karabiner 维护结构的体验？

如果一开始冻结这个成功标准，就不会把“Win+Enter 能不能发送”误当成主要裁决。

### Judgment Integrity

连续两次方案被新事实推翻后，应该停止生成下一套完整方案，回到唯一会改变选择的关键未知。

本案应尽早收缩到：

- UU 输入到底有没有进入 Karabiner；
- 如果通过 fallback 进入，缺失设备身份会实际影响哪些现有规则。

在这两个问题没有回答前，不应把任何一套映射或 fallback 设置称为“最终方案”。

### Solution Design

成熟产品问题必须先检查现有能力和当前 canonical，再决定是否扩展。

本案已有大量 Windows 键盘语义已经存在于 Local Compute。正确方向不是重新设计一套 UU 快捷键，而是先判断现有体系能否复用，再只补远控输入与实体 HID 输入之间的真实差距。

### 用户可见回答

即使内部已经完成规则覆盖分析，也不能把设备条件、fallback、变量和规则数量直接堆给用户。

用户真正需要先看到的是：

- 这个目标能不能实现；
- 能做到多接近；
- 为什么 Dell 正常而 UU 不正常；
- 推荐路线是不是要改动现有 Karabiner；
- 哪两个事实还没验证；
- 验证失败时意味着什么。

如果用户读完仍要追问“所以到底能不能做到和实体键盘一样”，说明 reader-facing decision 仍未完成。

## 当前应保留的决策状态

- “UU 静态全局 `Ctrl -> Command`”只能解决部分普通快捷键，不满足完整目标，不能作为长期主方案。
- “只打开 Karabiner CGEventTap fallback”也不足以证明完整体验一致。
- 当前最有希望的方向是复用现有 Karabiner Windows 语义，让远控输入进入同一处理体系，并只补远控输入缺少实体设备身份造成的残余差距。
- 在 fallback 捕获和稳定 UU 会话信号完成真实验证前，该方向仍是候选，不得报告为已经解决。

## 2026-11-07 follow-up：在宣布 BLOCKED 前漏查了已经存在的 UU 会话检测实现

后续执行又暴露了同一类问题。

Codex 已经实测确认：启用临时 CGEventTap 捕获后，Legion 经 UU 的 `Ctrl+A` 可以进入 Karabiner 并命中现有规则。这证明“UU 输入完全进不了 Karabiner”已经被淘汰。

随后 Codex 发现 CGEventTap 事件在 Karabiner 16.3.0 和当前上游都会以 `device_id(0)` 进入规则匹配，无法保留真实物理来源。这个事实本身成立，但 Codex 立即把 Goal 标为“阻塞”，并多次要求用户断开/重连 UU、继续按键探测，以寻找“来源”。

这里再次把“不能区分每个事件来自哪一把键盘”误当成了“不能完成用户目标”。用户当前真实场景是：人在广州，通过 Legion 的 UU 会话操作香港 Mac mini；当前连接本身就是唯一可用的人机入口。要求断开会直接破坏当前操作路径，而且并不能恢复 CGEventTap 已经丢失的设备身份。

更重要的是，开放式现实解空间调查很快找到已有开源项目 `aoyamashou/UUyc-companion`。该项目已经在 macOS 被控端实现 UU 真实会话检测，不需要用户断开连接：

- `UUMonitor.overlayPresent()` 通过 `CGWindowListCopyWindowInfo` 检查屏幕上是否存在 owner 为 `UURemoteServer` 的覆盖窗口；
- `UUReader.readControllers()` 通过 macOS Accessibility API 读取 UU 主界面，在表格行中查找“远程控制”标记并取得当前控制端设备名；
- `UUConnectionState` 将两类信号合并，并使用短防抖判断 connected / disconnected；
- 项目 UI 能直接显示“等待其它设备连接中”或“某设备已连接”。

因此，“Mac 端无法可靠知道 UU 是否正在被控”并不是已经证明的 blocker。至少存在一个现实、已实现、可检查源码的检测路线，应先在当前 Mac mini 上验证和最小复用，再决定是否需要自建。

这次 follow-up 对 Reasoned Decision 的新增要求是：

1. **BLOCKED 也是一个需要 Gap Proof 的结论。** 发现底层限制后，不能直接把整个 Goal 标阻塞；必须先证明该限制确实击中了用户成功标准，而且现实生态中没有旁路。
2. **不要把实现内部要求升级成用户要求。** 用户需要“远控时获得与实体 Windows 键盘近似一致的体验”，并没有要求 Karabiner 必须为每个 CGEventTap 事件恢复硬件 VID/PID。
3. **当前操作通道本身属于 Task State。** 当用户正在通过唯一远控链路与 Agent 交互时，默认不得要求断开该链路做诊断，除非已证明没有无损替代。
4. **连续失败后应扩大现实解空间，而不是扩大用户探测负担。** 本案应该先查 UU 生态、GitHub、现成 companion/monitor，再决定是否需要用户提供新输入。

## 2026-11-07 follow-up：从“来源识别困难”升级到自编译 Karabiner，属于未经 Gap Proof 的过度设计

后续执行在已经确认 stock Karabiner 的 CGEventTap fallback 能接住 UU 按键后，为了恢复/验证软件事件来源，继续设计了 Karabiner 源码补丁，并把完整上线前置条件升级为：在 Mac mini 安装完整 Xcode 26 或更新版本、配置 Apple Development 证书、构建并签名整套 Karabiner 安装包。

这条路线在技术上可能可行，但没有先证明它是满足用户成功标准所必需的，因此不能升级为主方案。

用户的成功标准仍然是：Legion 经 UU 远控 Mac mini 时获得与本机 Dell Windows 键盘尽量一致的日常体验，同时保持一份清晰、低维护的 Karabiner canonical。用户没有要求恢复每个 CGEventTap 事件的原始硬件身份，也没有要求维护自编译 Karabiner 分叉。

在已有事实下，更小的现实路线仍未被排除：stock Karabiner 已能接收这类事件；物理 Dell/Xiaomi 仍走 HID 路径并保留真实 device id；UU 软件输入走 CGEventTap 的 device_id(0)。如果能可靠识别“当前 UU 被控会话”，就可以仅在该状态下为 device_id(0) 应用现有公共 Windows 语义，并保持实体设备分支不变。即使需要为少量 device_if-only 行为增加变量门控分支，其维护成本也远低于维护自定义 Karabiner 二进制和代码签名链。

因此在要求 Xcode、开发者证书、自定义构建和长期维护分叉之前，必须先完成 Gap Proof：

1. stock Karabiner + UU 会话状态门控是否已经足够覆盖真实成功标准；
2. device_id(0) 在 UU 会话期间是否会与用户当前机器上的其他软件注入事件产生实际冲突；
3. 这些冲突是否无法通过现有条件、最小规则分支或自动生成避免；
4. 只有上述路线真实失败，才有资格把“修改 Karabiner 源码并自签名发行”升级为必要方案。

该 follow-up 进一步说明：Reasoned Decision 不只要防止过早 BLOCK，也要防止为了绕过一个底层限制直接跳到高维护 Build。发现内部能力缺口后，仍必须先走 Adopt / Compose / Extend；Xcode、开发证书、自维护 fork、系统级 helper 等明显增加长期维护面的方案，在没有 Gap Proof 前只能是远端 fallback，不能成为当前执行主线。

## 2026-11-07 follow-up：用户一追问就改口，说明 Recommendation Delta 仍未被实际守住

在后续对话中，用户没有提供新的现场证据，只是连续追问：

- “最新的 prompt 到底能不能发？”
- “这个 prompt 到底要做什么？”
- “是不是又自己加了莫名其妙的前提？”

回答却再次发生实质性改口：上一轮刚把“UU 会话检测 + CGEventTap fallback + `uu_remote_active` + 少量规则补齐”说成已经按 Reasoned Decision 收敛的推荐，下一轮又改成“上一版方向对，但不建议原样发”，并重新调整实现合同和强调重点。

这正是冻结架构已经明确禁止的行为：**用户质疑本身不是 Decision Delta。** 如果现场事实、用户硬约束、关键前提和候选集合都没有变化，就不应该因为用户问“你确定吗”而重新生成一套推荐或 prompt。

本案中真正允许变化的只有表达质量和执行合同中暴露出的错误前提，例如：
- 删除此前擅自加入的“必须恢复物理设备来源”；
- 删除未经 Gap Proof 的 Xcode / 自编译 Karabiner 路线；
- 把已确认的事实和淘汰路线写得更清楚。

这些属于修正错误或澄清边界，可以形成合法 Decision Delta。

但如果没有新的技术证据，就不应继续从：
“会话检测 + fallback + 变量”
改写成另一套结构，
也不应每次都重新包装成“这次才是真正最终方案”。

该 follow-up 对 Reasoned Decision 的要求是：

1. **用户追问不能自动触发重新决策。** 先检查是否真的出现了新证据、约束变化、逻辑纠错或候选集合变化。
2. **如果只是表达失败，改写表达，不改技术推荐。** Clear Writing 可以重组语言，但不能借机重做架构。
3. **如果发现上一轮推荐本身含有未经授权的新前提，只撤销那个前提和受影响部分。** 不得把局部纠错扩成整套方案重启。
4. **每次改口必须能说出 Recommendation Delta。** 说不出“哪条新事实导致哪部分排序变化”，就默认保持原推荐。
5. **Prompt 也是 recommendation 的一部分。** 不能正文说方案已冻结，下一轮又因为用户质疑而把执行 prompt 改成另一套隐含架构。

这次用户反馈的核心不是某个技术细节，而是对 Agent 决策稳定性的直接否定：用户已经明确感受到“一问就改口”。这应当作为 Judgment Integrity 的真实回归样本保留。

