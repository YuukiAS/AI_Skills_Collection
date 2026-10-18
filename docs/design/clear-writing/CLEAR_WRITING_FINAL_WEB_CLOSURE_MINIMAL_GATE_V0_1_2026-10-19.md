# Clear Writing 最终 Web 收尾最小验收方案 v0.1

日期：2026-10-19  
状态：PLANNER_REVISION_FOR_CRITIC  
对象：`writing-style / Clear Writing`  
任务键：`clear-writing--final-web-closure-minimal-gate`  
source/evidence branch：`reviewed/clear-writing--scientific-explanation-readability-repair`

## 1. 本轮目标

本轮只解决独立 Critic 的一个 blocker：`CW-FWC-01`。

现有广泛证据已经存在：

- frozen production candidate：
  `fd7a1578a5042a46a55c5b638f6d550655b1096b`
- KR-WEB-01..09 PASS；
- 四组 should-not-change PASS；
- focused/full tests 与 required CI PASS；
- source/generated parity PASS；
- 独立 implementation/product Reviewer：
  `PROCESS PASS + PRODUCT / ARTIFACT PASS`；
- 真实 PRIVATE ChatGPT plugin 已存在，并已回读六个核心 Skill 与
  `scientific-rewrite` support script，内容与 frozen candidate 一致；
- invocation-policy proposal v0.2 已独立 Critic PASS；
- Web Gate execution package v0.4 已 execution-ready PASS；
- 旧 strict matched W2 read-only preflight 得到
  `W2=INCONCLUSIVE`，且没有发生 live batch。

因此本轮不再增加样本数量，不重跑旧 W0/W1/W2/W3/G7，也不重新证明已经由
repo/Codex/独立 artifact review 证明过的能力。

最终人工 ChatGPT Web 验收数量严格冻结为：

**4 个真实回答。**

## 2. CW-FWC-01 的接受与关闭方式

Critic 的判断是：问题不在“4 个太少”，而在原 4 个回答没有必然直接覆盖：

1. 一个不同于普通 `response-clarity` 的兄弟写作任务族；
2. frozen candidate 最新修复的复杂科研解释行为。

本方案接受该 finding，不新增第五个回答，而是重新分配原有 4 个回答的信息密度：

- Test 1 保持显式 `@Clear Writing` 普通技术状态解释；
- Project Turn 1 改为新的 `scientific-rewrite` 类型 source-faithful rewrite；
- Project Turn 2 保持 pure exact JSON；
- Project Turn 3 改为新的复杂科研普通解释，并同时验证 exact-only 后恢复。

这样 4 个回答分别直接观察四类互补能力：

1. 显式真实插件入口 + 普通解释 + exact identities；
2. 兄弟写作任务族 + source-faithful 结构重写；
3. exact-only activation exemption；
4. 复杂科研解释 + 多重下标 + 未定义对象 + turn recovery。

## 3. Release claim 重新收窄

本轮将最终 release claim 明确限制在用户可观察层。

四回答全部 PASS 后，只允许声称：

- 显式真实 Clear Writing 入口工作正常；
- 薄 Project policy + 已安装 Clear Writing 下的连续用户行为达到预期；
- pure exact-only 输出不受污染；
- 至少一个非默认兄弟写作任务族在真实 Web 正常入口下行为正确；
- frozen candidate 最新复杂科研解释修复在真实 Web 中得到直接观察。

明确禁止声称：

- `PLUGIN_LOADED_EVERY_TURN=PASS`；
- 已证明每轮后台必然加载 Clear Writing；
- 已证明插件相对于相同 Project setting 有独立因果增量。

因此 strict matched W2 **不再是 release blocker**。

已有 `W2=INCONCLUSIVE` 保留为历史诊断证据，不删除、不改写、不重跑。
这不是把 INCONCLUSIVE 改判 PASS，而是收窄正式产品 claim，使 release gate 与真实
用户承诺一致。

## 4. Capability Gate Matrix

| Gate | 能力 / claim | 正常入口 | 证据 | 失败 | final candidate |
| --- | --- | --- | --- | --- | --- |
| FWC-1 | 显式真实插件入口下普通解释、中文自然度、事实强度和 exact identity 保护 | 新普通 ChatGPT 对话 + 显式选择真实 PRIVATE `@Clear Writing` | Test 1 完整回答 | 任一 hard failure | 必须是当前真实 PRIVATE plugin，且 release 内容与 `fd7a1578...` parity |
| FWC-2 | 非默认兄弟任务族在 Project normal entry 下正确工作 | 测试 Project，不手工 @ | Project Turn 1 source-faithful rewrite | claim/formula/未验证状态漂移，猜未定义对象，机器身份被改，机械压短 | 同上 |
| FWC-3 | exact-only 输出不被 Project policy / 已安装插件污染 | 同一 Project conversation Turn 2 | exact JSON 字符级相等 | 任意多余/缺失/重排字符 | 同上 |
| FWC-4 | 复杂科研普通解释的 reader-model 修复真实生效，并能从 exact-only 恢复 | 同一 Project conversation Turn 3 | 复杂科研解释完整回答 | 下标/层级不清、猜未知对象、机械压短、中文/结构未恢复 | 同上 |

现有 KR-WEB-01..09、四组 should-not-change、repo/full CI、artifact review 和
plugin parity 继续作为 supporting regression evidence，不要求用户重复执行。

## 5. 冻结 Project policy

Project 测试只使用已经批准的薄调用策略，不复制 Clear Writing 内部写作规则：

> 对每条面向用户的自然语言最终回答，以及自然语言与机器内容混合的最终回答，如果当前 Clear Writing 可用，则使用其最合适的现有写作能力；纯 JSON、YAML、代码、命令、原始日志、逐字引用或其他要求精确机器输出的请求不为此强制调用 Clear Writing，直接保持精确原样。不要模拟、重建或复制 Clear Writing 内部规则。

本轮不修改用户真实 Project setting。测试时只用于专门测试 Project。

## 6. 四个最终真实 Web 回答

完整逐字测试输入和检查规则冻结在：

`docs/operations/prompts/CLEAR_WRITING_FINAL_WEB_CLOSURE_TEST_PROTOCOL_V0_1_2026-10-19.md`

总数固定为 4。

### Test 1 — 显式 `@Clear Writing`

保持此前方案原样，验证：

- 真实 PRIVATE plugin 可显式使用；
- 普通技术状态解释；
- 结论优先；
- 自然中文；
- 不机械逐条翻译；
- exact branch/status/command；
- 不拔高 release readiness。

### Project Turn 1 — 新的 scientific-rewrite 用户任务

不手工 `@Clear Writing`。

输入是一段新的中文科研技术材料，要求 source-faithful 结构重写，并同时包含：

- 小型多重下标公式链；
- 一个明确未定义的数学对象；
- 一个“仍未验证”的科学限制；
- 必须逐字保留的机器身份；
- 允许重组段落；
- 禁止改变 claim strength、公式、变量含义与未验证状态；
- 禁止猜未定义下标；
- 禁止机械压短必要解释。

这里只判断用户侧兄弟任务行为，不声称后台具体 Skill load 已被观察。

### Project Turn 2 — pure exact JSON

同一 conversation：

`{"status":"PENDING","retry":false,"count":2}`

assistant message 必须逐字符只有该 JSON。

### Project Turn 3 — 新的复杂科研普通解释

不手工 `@Clear Writing`。

新的普通解释任务必须包含：

- 多重下标对象；
- 后续用途；
- 一个信息不足、不能可靠解释的对象；
- 要求先建立对象/层级/用途的 reader model，再进入公式或术语；
- 信息不足必须明确说缺什么；
- 禁止按符号形状猜含义；
- 不能机械压短必要解释。

同时直接观察 Turn 2 exact-only 后普通自然中文和正常解释结构是否恢复。

## 7. 冻结 PASS / FAIL 标准

### Hard fail：一次即失败

任一回答出现以下任一项，最终 Web Gate 直接 FAIL：

- 事实或 claim strength 漂移；
- exact machine string / JSON / code 被改；
- 未定义科学对象被自行猜成事实；
- explicit language requirement 被违反；
- source-faithful rewrite 删除/改变必要公式、变量含义或“仍未验证”边界；
- sibling route 错误到实质改变请求产物；
- exact-only 输出增加前言、解释、代码围栏或其他字符。

### Reader-quality repeat fail

以下问题若在不同回答中重复出现至少 2 次，则 FAIL：

- 不必要中英夹杂；
- 一句话一段；
- 内部流程词/状态字段主导正文；
- 真正结论埋在后面；
- 必要复杂解释被机械压短；
- 简单问题被膨胀成报告。

单个轻微措辞偏好不构成 release blocker。

### 防挑样本

- 四个输入在第一次运行前全部冻结；
- 每个回答只取一次有效模型回答；
- 只有完全没有 usable answer 的基础设施中断才允许一次技术 retry；
- 低质量、答错、格式错都是真实结果，不重跑到成功；
- 不在看到结果后改 prompt、rubric 或 threshold。

## 8. W2 的新地位

历史 strict matched W2：

`W2=INCONCLUSIVE`

继续保存。

它只说明：当前控制面无法严格证明“plugin 相对于完全相同 Project setting
的独立因果增量”。

本轮 release 不再声称该因果增量，因此不再要求这个研究性对照作为发布条件。

禁止：

- 重跑 matched experiment；
- 构造 control arm；
- 新增盲评；
- 用这 4 个回答反向声称 W2 PASS。

## 9. Release closure 冻结条件

如果且仅如果四个回答全部按上述标准 PASS，则立即进入 release closure。

之后 release-critical 工作只允许：

- repository/plugin version；
- README；
- changelog；
- release branch；
- source/generated/release identity；
- final CI；
- actual released plugin identity/parity。

不得再因为“也许还可以多测”增加新的 Web release Gate。

唯一例外：四回答真实执行中暴露一个**此前合同没有覆盖的新产品失败**。
这时停止 closure，回 Planner/Critic 处理该具体失败；不得把轻微风格偏好包装成新 blocker。

## 10. 五遍预检

### 产品

最终用户关心的是：真实插件是否可用、Project normal entry 是否产生正确用户行为、
exact-only 是否安全、兄弟任务和复杂科研解释是否真实工作。4 个回答现在直接覆盖这些 claim。

### 现实

严格 matched W2 已证明当前 surface 无法安全构造，不是产品输出失败。继续追 W2
会增加用户成本，却不对应本轮收窄后的 release claim。

### 替代

- 继续旧 W2：过重，且当前环境无法证明。
- 只测一个显式 @：过简，不能观察 Project normal entry、exact exemption、兄弟 route、
  复杂科研解释。
- 4 个高信息密度回答：保留真实 Web 证据，同时利用已有广泛 repo evidence。

采用第三种。

### 反证

最容易出现的假 PASS 是：普通解释正常，但 sibling task 或复杂科研解释在真实 Web
runtime 失效。CW-FWC-01 正是通过 Turn 1 / Turn 3 直接补这两个观测缺口。

### 执行

本轮只冻结方案与测试合同，不执行任何回答，不修改 production candidate、
真实 Project setting、真实 PRIVATE plugin，也不启动 Codex。

## 11. 本轮不做什么

- 不修改 `fd7a157...`；
- 不修改六技能架构；
- 不修改真实 PRIVATE plugin；
- 不修改真实 Project setting；
- 不执行四回答测试；
- 不执行旧 W0/W1/W2/W3/G7；
- 不启动 Codex；
- 不做 release/version bump；
- 不实施 PIE、Mica、Research Authoring、Presentations；
- 不创建新 tracking Issue。

## 12. Critic 只需复核

下一轮独立 Critic 只需判断：

1. `CW-FWC-01` 是否被“同样 4 个回答、但 Turn 1/3 改为 sibling + complex scientific”完整关闭；
2. 4 个回答是否与已有广泛证据组合后足以支撑**收窄后的用户可观察 release claim**；
3. W2 从 release blocker 退为历史诊断是否与新的 claim boundary 一致；
4. 四回答 PASS 后直接进入 release closure，且不再追加 Web Gate，是否边界清楚。

Critic PASS 只批准这套最终人工 Web 验收方案；不代表四回答已经实际 PASS，也不代表 release 已完成。
