# ChatGPT Web Critic 优质审查示例：Delivery Assurance 与 STAT5060

日期：2026-10-20  
性质：Planner/Critic 1.7 的真实审查示例；用于未来复杂任务参考，不新增任务专属硬规则。  
治理基线：Planner Role Contract 1.7、Critic Role Contract 1.7、Plugin Capability Gate Policy 1.2。

## 为什么记录这两个例子

这两个案例都来自用户明确不信任既有“已冻结/已通过”结论的复杂设计。独立 Critic 没有沿用历史 PASS，也没有因为文件齐全、映射数量完整、测试存在或架构被标为 frozen 就放行，而是重新读取当前仓库事实，从用户真正需要的结果反推完整成功链、关键失败链、实施入口和恢复路径。

两个案例最终都给出 `REVISE`。它们之所以是优质示例，不在于结论更严格，而在于审查真正发现了会导致后续实现失败或虚假完成的具体问题，同时保留已经有充分证据支持的设计决定。

详细回归记录：

- `results/chatgpt-web--pass-integrity/DELIVERY_ASSURANCE_FRESH_CRITIC_REGRESSION_2026-10-20.md`
- `results/chatgpt-web--pass-integrity/STAT5060_VALIDATOR_FRESH_CRITIC_REGRESSION_2026-10-20.md`

## 示例一：Delivery Assurance

现有 v0.3 已有较完整的公共架构、Phase 1 证据和历史审查，容易产生“架构主体已经通过，只补实现即可”的错觉。优质 Critic 没有停在公共合同，而是继续追问七个真实 consumer 是否都已经形成可实施的接入合同。

它发现：

- 正式 consumer 证据实际只具体覆盖 Lucerna、CARE、Bobbio，另外四仓仍缺完整接入合同；
- adapter 可能通过遗漏要求、漏 sibling target 或指向过期 authority 来降低验收强度；
- Bobbio 已存在真实 authority 漂移，旧 0.2.0 证据可能与当前 0.3.0 工作混淆；
- DA-G10–DA-G15 仍偏公共能力分类，缺少逐仓正常入口的完整成功链与代表性危险失败链；
- 各仓能自动声明到什么层级、什么必须留给真人判断，还没有逐仓冻结。

审查没有因此推翻公共架构，而是明确保留正确部分，并要求补七仓接入附录、遗漏变异测试、authority freshness、逐仓 claim ceiling 和正常入口 Gate。它还把 Bobbio 的模糊“状态漂移”转成精确恢复任务，而不是永久登记一个 known gap。

这是优质 Critic 的关键特征：**既能阻塞真实风险，也能控制返修范围。**

## 示例二：STAT5060 Validator Architecture

该设计已经有 213/46/32 历史映射、4/5/5 validator 架构、控制矩阵和两份实施 handoff，很容易被“零 orphan”“DESIGN FROZEN”“已经有 Codex prompt”这些表面信号误导。

优质 Critic 继续追到可执行语义链，发现：

- 每条历史要求“有 owner”不等于已经绑定真正的 enforcing validator、规则、控制、正常入口、当前候选证据和 scoped verdict；
- 两份现有 handoff 没有完整冻结三个分支的身份、工作树、允许路径、受保护 rubric/test、恢复方式和 AGENTS 冲突，不能直接作为 GPT Work 安全执行入口；
- 历史三页 Project Guide 并非真正找不到，而是已有明确提交、路径、哈希和失败记录；
- 两页 Guide 仍缺“删内容硬塞”和“不可读压缩”两类独立负控；
- HW1 Q6 的完整协方差统计对象仍缺真实成熟包拟合正控。

同时，Critic 保留了已经冻结且有充分依据的用户决定：Tutorial 的 104 条教师学习包批注明确排除在 student-deck release-history coverage 之外，不要求恢复，也不得变成学生课件要求；4/5/5 validator 数量也没有因为“更保险”而机械增加。

这是另一项重要标准：**Critic 必须区分“当前设计真正缺什么”和“用户已经明确决定、不应重新打开什么”。**

## 未来复杂 Critic 应复制的行为

遇到架构、工作流、能力验收、关键恢复或复杂执行包时，优先采用这两轮体现出的审查方式：

1. 先读当前 source of truth，再看 Planner 结论；历史 PASS、旧提示词和“已冻结”标签只是证据。
2. 从用户真实消费结果反推正常入口、完整成功链、跨组件调用和最高风险失败链。
3. 对“数量齐全、映射无孤儿、测试通过、schema 完整、文件存在”继续追问其是否真的证明用户能力。
4. 检查执行提示词本身；如果它把产品、架构、统计、评分、权限、验收或恢复决定留给 Executor，就不能认为 execution-ready。
5. 对缺失 source、artifact 或历史失败证据，能恢复的就给精确 recovery task；不能恢复的才保留诚实缺口。
6. 保留已经被当前用户明确冻结且有依据的决定，不因一般性“不确定”重新打开。
7. `REVISE` 只阻塞真实问题，并给最小关闭条件；`PROCEED` 也必须说明还有哪些阶段尚未证明。
8. 先给用户一屏能独立理解的中文摘要，再给 finding、locator 和机器 handoff。
9. 最终 execution-ready 审查重新检查完整承诺和执行包，不能被上一轮 blocker 清单缩窄。
10. 只有真正到 execution-ready 时才允许唯一 Critic 级 `PASS`，并同时给 `READY_FOR_CODEX=YES`。

## 不应机械复制的东西

这两个案例中的七仓名称、STAT5060 的 4/5/5 validator、三页 Guide、Bobbio milestone、具体 Gate 编号都属于各自任务证据，不是未来 Critic 的通用模板。

真正应复用的是审查强度和方法：当前事实优先、正常路径优先、完整链优先、关键失败链优先、可执行性优先，以及对用户已冻结决定和审查范围的尊重。

如果未来 Critic 只复述 Proposal、只关闭旧 blocker、只看测试/schema/映射数量，或者用户一句自然追问就能暴露核心设计空白，应视为审查质量回归，而不能因为输出了正确的 verdict token 就接受。
