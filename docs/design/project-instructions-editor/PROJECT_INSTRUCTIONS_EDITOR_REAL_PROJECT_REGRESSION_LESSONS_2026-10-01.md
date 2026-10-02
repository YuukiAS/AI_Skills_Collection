# Project Instructions Editor — 真实 Project 回归经验

日期：2026-10-01  
状态：PLANNING_EVIDENCE_ONLY  
跟踪：#93  
候选未来 standalone Skill：`project-instructions-editor`

本文记录 AI Research Stack Project settings 多轮真实修改与回归得到的经验，供后续 Planner 设计 `project-instructions-editor` 时使用。

本文不是 Skill 实现规范，不授权创建 Skill、Plugin、README card、VERSION、registry/catalog、Marketplace、profile、release 或安装入口。

## 1. 这轮真实工作证明了什么

这轮工作的直接目标只是改善一个真实 ChatGPT Project 中的中文可读性：减少普通英文工程/统计/管理术语泄漏，避免一句一行、状态字段堆砌和简单公式块，同时保留真正需要精确定位的产品名、角色、代码、路径、字段和机器协议。

真实回归表明：

- Project-level 用户阅读层规则有实际效果，能明显改善开头、段落连续性和部分术语中文化；
- 仅靠一条“中文优先”不够，Project 内长期治理文本、旧 thread、Project files、source documents 与模型既有表达习惯都可能继续影响最终输出；
- source-heavy 技术任务尤其容易把来源中的描述性英文标签继续带进用户正文；
- 多轮继续收紧同一 Project setting 后，边际改善会变小，不能因为某个测试仍有残余英文就无限扩写设置。

当前用户决定：现有 Project setting 暂时停止继续调参，把经验固化到仓库，后续由新的 Planner 从更广的 `project-instructions-editor` 目标继续设计。

## 2. 最重要的新经验：真实 live setting 必须是编辑基线

本轮曾出现一个直接流程错误：仓库中的 Project-instruction candidate / Reference B 已经落后于用户实际保存在 ChatGPT Project Settings 中的 live text。

如果直接拿仓库旧 candidate 覆盖 live setting，会丢掉用户后来已经加入并接受的更强治理规则，例如自动接手条件或角色接手前置条件。

因此未来编辑 Project instructions 时，必须优先取得并比较：

1. 用户当前真实 Project setting；
2. 该 Project 中与本次修改直接相关的历史 thread / 用户纠正；
3. 对应 canonical repo 的当前规则、README/AGENTS/policy/Goal/TODO 等真实来源；
4. 当前用户请求。

仓库中的历史 candidate、Reference、旧 thread 摘要只能作为证据，不能自动冒充当前 live setting。

如果无法取得当前 Project setting，不应做“完整替换版”并声称安全；最多输出明确标注基线缺失的建议或请求取得 live text。

## 3. 中文化经验只是未来 Skill 的一个维度

这几轮主要验证的是“用户阅读层中文化与可读性”，不能把它误写成未来 standalone Skill 的全部能力。

未来 `project-instructions-editor` 应解决的是更大的 Project-instruction 编辑问题，包括：

- 在有限字符预算下保存真正长期有效的规则；
- 读取 Project 历史 thread，理解用户已经接受、拒绝和反复纠正过什么；
- 读取对应 repo 的当前事实来源，不把可检索细节重复复制进 Project settings；
- 在多个 scope 共存时维持长期权重和平衡，不能让最近一次局部需求吞掉整个 Project；
- 默认做 bounded edit，保护已有正确规则；
- 区分稳定的 Project-level 治理、可通过 locator 读取的详细工作流程、临时任务信息和用户阅读层规则；
- 保留精确机器标识和正式身份；
- 对完整替换候选做语义保真检查；
- 必要时提供清楚的前后差异与修改理由，让用户能快速判断到底改了什么。

中文可读性是其中一个真实要求，不是 Skill 的产品定义。

## 4. 有限字符预算必须是核心约束

真实 Project 编辑曾以约 8,000 字符作为该 Project 的实际使用预算。这个数字是用户当前 Project 的经验基线，不应被宣称为所有 ChatGPT Project 的统一产品上限。

可复用要求是：

- 编辑前先检查当前文本长度和剩余空间；
- 不以“把所有有用规则都塞进去”为成功；
- 优先保留稳定 ownership、routing、authority、安全、证据、决策和长期产品哲学；
- 详细 SOP、课程细节、构建步骤、评审清单和易变化事实优先留在 canonical repo / document 后，通过 locator 按需读取；
- 为未来局部修改留出合理余量，不把设置填到无法维护；
- 评价的是语义密度和长期稳定性，不是单纯追求字符越少越好。

## 5. 用户阅读层与来源语言必须分开

真实测试反复暴露一个重要边界：

模型为了读取、搜索、比较和核对英文 repo / design proposal 而需要接触原文，不等于用户最终需要看到这些原文。

因此未来编辑器需要区分：

- **内部取证语言**：为了理解 repo、论文、日志、规则而读取的原文；
- **用户阅读语言**：最终用户真正需要直接理解的解释；
- **精确身份 / 机器层**：必须凭原字符串复制、执行、唯一定位或机器匹配的内容。

正式产品、仓库、Skill、固定角色、文件名、路径、命令、字段、状态值、版本和协议字符串可以因稳定身份或机器匹配需要保留。

来源中的章节标题、设计标签、阶段标签和普通技术短语，即使反复出现或能够搜索，也不应仅凭这一点进入最终用户正文。

真实回归里出现过的英文词只是 failure evidence，用来证明边界问题存在；**不得把这些例子转成禁词表、替换词典或硬编码列表。**

## 6. 不要用“禁止 XX”堆规则解决问题

本轮多次证明：继续叠加“禁止某词”“连续几个英文词失败”“英文比例”“固定几段”“固定几个标题”“固定几个公式块”这类规则，很容易产生两个问题：

- 模型针对表面形式过拟合，却没有真正理解信息层级；
- Project settings 自身越来越长，反过来挤压真正重要的治理语义。

未来 Skill 不应以以下机制为核心：

- 英文禁词表或大型中英替换表；
- 英文数量、比例或连续词阈值；
- 固定段落、标题、列表、公式数量；
- “禁止 XX”墙；
- 仅靠关键词扫描判断语义保真；
- 为了可量化而建立评分器、daemon、watcher 或新状态机。

需要的是语义判断：这条内容属于什么层、为什么长期留在 Project setting、删改后是否改变治理含义、原字符串是否真的承担稳定身份或机器匹配功能。

例子只能作为回归样本，不能变成实现词典。

## 7. Bounded edit 比“重新写一份更漂亮的 Project setting”更重要

真实用户经常只要求增加或修正一个局部规则。

未来编辑器默认应：

1. 先恢复当前 setting 的结构和已有有效语义；
2. 判断本次请求影响哪个局部范围；
3. 优先做最小充分修改；
4. 检查相邻 scope 是否被挤压、重复或意外删除；
5. 只有存在跨全局的真实冲突时，才提出更大范围重构。

最近讨论的 scope 不应因为“刚刚谈得最详细”就自动获得最多字符预算。

用户明确删除、拒绝或纠正过的规则不得在后续“优化”中被复活。

## 8. 完整候选必须能让用户看懂“到底改了什么”

本轮另一个真实失败是：即使生成了更好的 Project setting，如果对照基线选错、或者只给完整新稿而不说明变化，用户仍然需要自己逐行找差异。

未来编辑器在涉及现有 Project setting 修改时，应优先提供：

- 基于真实 live setting 的修改候选；
- 清楚的差异视图；
- 删除内容与新增内容分别可见；
- 每个实质修改给简短理由；
- 明确指出哪些治理语义保持不变；
- 再给一份可直接复制使用的干净完整版。

差异视图是帮助用户审查的交付形式，不应反向变成机器 patch 协议，也不要求所有小修改都制造复杂报告。

## 9. 回归测试的经验：固定来源，避免把内容变化误算成设置改善

本轮多次使用“比较 workflow-core 0.4 与 0.5”作为真实 Project 回归题。

期间 `workflow-core 0.5` Proposal 自身也在继续演进，因此不同回归回答的内容变化不能全部归因于 Project setting 修改。

未来要比较两版 Project instructions 的效果时，应尽量：

- 固定同一个 source commit / repo state；
- 使用相同或等价任务；
- 区分来源变化与 Project-setting 变化；
- 观察自然输出，而不是在测试 prompt 里提示“少英文”“少列表”等目标答案；
- 使用多个性质不同的真实任务验证，避免对一个问题过拟合。

单个 regression 可以发现失败，但不应因为一条输出残留几个术语就无限追加规则。

## 10. 当前中文回归的阶段性结论

截至本轮结束：

- 一句话一行、状态字段堆砌和简单数学块问题已经明显改善；
- 普通工程英文泄漏明显减少，但 source-heavy 技术问答仍可能保留部分来源描述性标签；
- 继续微调 Project setting 的收益已经不确定；
- 当前选择是停止继续调参，把残余问题作为未来 Skill / 输出终审设计的真实证据。

这不表示 Project-level 用户阅读层无效；它表示 Project setting 不是无限精细控制模型表面的理想位置。

后续若再次修改当前 AI Research Stack Project setting，应有新的真实失败或新的项目需求作为依据，不因“还能再润色一点”继续膨胀。

## 11. 给未来 Planner 的设计边界

下一轮 Planner 可以继续完善 `project-instructions-editor` 的产品设计，但应从整个 Project 管理问题出发，而不是继续围绕中文术语做局部补丁。

至少要回答：

- 输入如何取得真实 live Project setting，而不是旧 candidate；
- 怎样读取相关 Project 历史 thread 并识别用户最新有效决定；
- 怎样读取对应 repo 的 canonical sources；
- 怎样在字符预算下区分必须常驻、应该使用 locator、应该留在 task prompt 的内容；
- 怎样保护已有治理语义、scope 平衡和用户明确删除项；
- 怎样输出 bounded edit、完整候选和可审差异；
- 怎样用真实 Project 回归验证，而不是靠禁词或格式计数；
- 与现有中文写作 / fidelity Skill 的职责边界是什么；
- 什么时候只应更新 Project setting，什么时候应该更新 repo source，什么时候两者都不该改。

当前仍然：

```text
READY_FOR_FUTURE_SKILL_DESIGN=YES
READY_FOR_SKILL_IMPLEMENTATION=NO
```

standalone Skill 的实现、包装、触发、发布和安装仍需后续用户明确开启。
