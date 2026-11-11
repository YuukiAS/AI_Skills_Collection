# macOS CJK 随机错字形：Reasoned Decision 真实负例

Date: 2026-11-11
Source: PC+Server+VPS / macOS Edge + 飞书跨应用随机 CJK 错字形排查
Purpose: Reasoned Decision negative regression evidence
Underlying owner: macOS 字体注册/字形渲染状态与 Chromium/Electron 渲染缓存之间的边界；具体 state owner 尚待现场裁决

## 现场与硬约束

同一天在 Microsoft Edge 与飞书桌面端出现跨应用中文显示异常：原始中文被成片替换成另一批合法但无关的汉字，英文、数字、代码片段、图标大多正常。截图已经能捕获错误字形，因此不是显示器、线材或面板故障；表现也不同于编码损坏产生的 mojibake。

用户的真实目标不是“临时恢复一次”，而是查清故障族并得到低成本、可长期使用的处理路线。用户明确拒绝把 macOS 升级或整机重启当作优先动作；这类高成本、广影响操作只能作为前面更小动作全部不足后的兜底。

当前故障状态本身仍然可观察，因此它是高价值诊断现场，不应在完成最小裁决前先用整机重启、系统升级或大范围字体重置把现场抹掉。

## 失败

Agent 前几轮虽然逐渐识别到“字形映射/渲染状态”而不是普通编码问题，但形成长期建议时仍过早把“更新系统 + 整机重启”排到主路径，并进一步提出广泛字体重置。

这违反了 Reasoned Decision 的几个已有原则：

1. 没有先定位真实 state owner，就用会同时重置多个子系统的动作替代诊断；
2. 没有把 human-time、停机、中断、回滚难度和变更面作为一级成本；
3. 在仍存在两个高概率根因族——字体注册/字体面映射状态与 Chromium/Electron GPU 字形图集/渲染缓存——时，没有收缩到一个能立即裁决的关键未知；
4. 当前故障正在发生，却建议“等下次复发再看”，浪费了现成的真实故障现场；
5. “系统更新可能包含修复”被错误地提升成当前机器的优先方案，但没有 Gap Proof 证明更小动作不足。

## 现实证据

### 1. macOS 上存在同型的 glyph/font-face 状态失配

Mozilla Bugzilla 2085623（2026-10）记录了 macOS ARM64 上“底层文字正确，但屏幕显示成错误字形”的同型问题。报告中重开应用、换 profile、软件渲染、清 Firefox 缓存、移除一个大型用户 TTC、执行用户字体数据库清理均未解决；而终止 `fontd` 后重新启动应用立即恢复，不需要注销或整机重启。

- https://bugzilla.mozilla.org/show_bug.cgi?id=2085623

这证明 `fontd` / CoreText 字体注册状态与应用侧缓存之间的失配是现实存在的故障族，但它不能单独证明当前 Edge + 飞书案例已经由同一个 state owner 引起。

### 2. Chromium 已明确处理过 macOS 字体注册变化无法可靠到达 renderer 的问题

Chromium 2026-05 的相关提交专门处理“registered fonts change”时 renderer 字体缓存失效：由于 sandbox / macOS 通知路径，renderer 进程可能无法可靠获知字体注册变化，因此需要主动让 renderer font cache 失效。相关改动经历回滚后于 2026-05-27 重新落地。

- https://chromium.googlesource.com/chromium/src/+/905d03b3f6c35ec2e6dafd879fa3defe8e10b24c

这说明“macOS 字体状态与 Chromium renderer 的字体缓存不同步”不是臆测，而是 Chromium 已经真实修过的一类问题。Edge 基于 Chromium，飞书桌面端也属于 Electron/Chromium 路线，因此两者同日出现同型 CJK 错字形时，这一共同路径必须优先调查。

### 3. 同期 macOS CJK 错字形还存在 renderer/glyph-atlas 一侧的现实案例

Ghostty 2026-11 的同型报告显示：CJK codepoint 会被绘成另一字体中的同编号 glyph，ASCII 正常；改变一次字号即可让当前渲染面恢复。该证据更接近 shaper/font cache/glyph atlas 或字体 face identity 错配，而不是文本编码损坏。

- https://github.com/ghostty-org/ghostty/discussions/15018

因此不能只凭“`killall fontd` 在另一个案例有效”就把当前故障直接定性成纯 `fontd` 问题；还需要把 Chromium/Electron GPU 字形图集/渲染缓存这一候选与共享字体服务候选现场分开。

### 4. 飞书提供原生硬件加速开关，可用于低成本 A/B 裁决

飞书桌面端设置中提供“使用硬件加速（如果可用）”开关并要求重启应用后生效。它可以只改变一个受影响应用的 renderer 路径，不改系统版本、不改字体文件，也不影响 Edge，因此适合当前故障现场做单变量 A/B。

飞书桌面端 bundle / 安装信息也显示 Electron 体系标识（如 `com.electron.lark`），与 Chromium/Electron 共同渲染路径判断一致。

### 5. 字体数据库破坏性操作不应前置

macOS `atsutil` 文档明确表明，移除字体数据库会影响激活状态，而 server shutdown 也不是推荐的常规操作。因此 `atsutil databases -remove*`、字体数据库全清、系统字体大重置都不能在 state owner 尚未定位时充当默认修复。

## 重做后的判断

当前证据支持以下排序：

1. **高概率候选 A：macOS 字体注册 / font face identity 与 Chromium/Electron renderer font cache 的状态失配。**
2. **高概率候选 B：Chromium/Electron GPU 字形图集或 renderer 侧 glyph cache 状态损坏。**
3. **次级候选：用户字体、重复字体、旧版 CJK 字体或 fallback 配置触发了上面两类缓存错误。**
4. **低概率：单个字体文件本身永久损坏。** 如果字体文件真正系统性损坏，通常应更稳定、更广泛复现，而不是在 Edge 与飞书里随机出现不同合法汉字。
5. **淘汰：普通文本编码错误、显示器/线材问题、单个应用内容数据损坏。** 当前现场模式与这些解释不符。

当前唯一真正会改变长期处理路线的未知是：

> **错误主要由 Chromium/Electron renderer/GPU 路径持有，还是由共享的 macOS 字体注册/字体面状态持有？**

在这个未知被裁决前，系统升级、整机重启、清全局字体数据库、重置所有字体都只能是 fallback，不能叫“长期修复”。

## 当前故障现场的最小裁决

不需要等待再次复发。应利用当前仍然存在的故障态按以下顺序裁决：

1. 在 Safari 或 TextEdit 中显示/粘贴同一段中文。
   - 如果原生应用也错：优先进入共享字体服务/字体环境路线，跳过“两个 Chromium 应用共同坏”的假设。
   - 如果原生应用正确、Edge + 飞书错误：字体文件本体和系统级文本内容基本可以降权，重点留在 Chromium/Electron 与共享字体服务边界。

2. 只在一个受影响应用里切换 renderer 条件。优先用飞书的原生“硬件加速”开关，关闭后只重启飞书，Edge 保持原状。
   - 飞书恢复而 Edge 仍错：GPU/renderer 路径得到强支持，可继续验证把硬件加速关闭作为低成本长期规避。
   - 飞书仍错：不要顺手关闭 Edge 硬件加速，进入下一裁决。

3. 在 GPU 单变量测试未解决时，执行低成本共享状态重置：`killall fontd`，随后只重开受影响应用。
   - 两个应用同时恢复：共享字体服务 / renderer font cache 状态失配得到强支持；无需整机重启。
   - 仍不恢复：再进入只读字体环境审计（Font Book 验证、`atsutil fonts -verify`、用户字体/重复字体/legacy CJK 字体），而不是直接删除数据库或重置字体。

这套顺序的目标不是“多试几个 workaround”，而是每一步只改变一个高价值变量，让当前故障现场直接裁决根因族。

## 高成本兜底的正确位置

只有以下情况之一成立，才允许升级到高成本动作：

- 最小现场裁决无法区分根因，且低成本状态重置无效；
- 字体验证发现系统级、无法局部修复的异常；
- 上游已明确证明当前系统版本存在已修复且无法规避的缺陷；
- 或用户明确接受停机/大范围变更成本。

因此 macOS 升级、整机重启、安全模式、大范围字体重置、字体数据库删除都必须保持在 fallback，而不是主路径。

## 回归断言

- **广影响 reset 不能替代 state-owner diagnosis。** “重启/升级大概率能好”不构成优先推荐的理由。
- **disruption cost 是一级排序维度。** 系统升级、整机重启、重新登录、全局数据库重建都必须显式计入人时、中断、回滚和潜在回归成本。
- **正在发生的故障是诊断资产。** 若当前现场可观察，应先用最小单变量测试裁决，不得先把现场重置掉再要求用户等待复发。
- **多个高概率根因并存时先找唯一关键未知。** 不要在没有裁决的情况下任选一个根因并给“永久修复”。
- **同型外部案例只能提升候选概率，不能替代当前机器验证。** Firefox 的 `fontd` 修复证据不能直接升级成 Edge + 飞书的确定根因。
- **用户明确的变更成本约束必须进入 Task State。** “不把系统升级/整机重启作为优先动作”是当前硬约束，不得被通用排障模板覆盖。
- **fallback 需要 Gap Proof。** 只有更小、可逆、局部动作已经证明不足，才能升级到系统级恢复。
