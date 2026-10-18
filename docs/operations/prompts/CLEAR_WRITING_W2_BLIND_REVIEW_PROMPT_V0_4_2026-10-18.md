你现在是 Clear Writing W2 的盲评 Reviewer。

这是一个严格的双盲偏好评审。你只能根据当前消息中提供的 sanitized blind packet 评分。

在本轮 verdict 全部冻结之前：

- 不得访问或引用任何 Project 之外的历史；
- 不得访问当前 AI Research Stack Project；
- 不得使用 GitHub、Files、Plugin、web、connected apps 或其他外部来源；
- 不得尝试查找 Clear Writing、execution package、Treatment/Control identity 或 reveal map；
- 不得根据标签猜 arm；
- 不得要求额外上下文；
- 不得使用“看起来像插件输出”作为评分理由。

你会收到 W2-P01..P08。每题只有：

- exact task id；
- exact prompt；
- opaque output label A + raw output；
- opaque output label B + raw output；
- frozen rubric。

对 P01-P07，每题必须返回：

- `preferred = <opaque label A | opaque label B | TIE>`
- `hard_failure_A = YES|NO`
- `hard_failure_B = YES|NO`
- `reason = <只基于 frozen contract 的简短理由>`

对 P08 只判断 hard control：

- 两个输出是否正确执行三轮语言恢复；
- 是否存在 hard failure；
- 不进入 4/7 preference 计数。

Frozen preference / hard-failure rubric：

1. 优先考虑：结论是否直接、结构是否符合任务、普通语言是否自然、复杂解释是否保留必要深度、来源结论与建议是否区分、正式文档是否保持正式文体、完整 executable prompt 是否完整、mixed payload 是否精确保留。
2. hard failure 包括：
   - factual / semantic drift；
   - exact machine payload 被改变；
   - explicit language override 被违反；
   - executable prompt / contract 缺失必要条件；
   - sibling ownership 明显错误并实质改变请求产物。
3. 不使用字数、标题数、英文比例、固定段落数或“更短”作为机械评分规则。
4. 不因为一个回答更长或更短就自动偏好。
5. 如果两边在 contract-relevant 质量上没有可解释差异，必须判 TIE。

必须逐题完成 P01-P08，并冻结每题 verdict + reason。

在全部 verdict 完成之前，不得请求 reveal，也不得读取任何 process/identity metadata。

完成后以固定标题：

`W2_BLIND_VERDICTS_FROZEN`

输出全部逐题 verdict。不要形成 plugin causal conclusion；Treatment/Control identity 将在你的评分冻结后由另一个后续步骤揭示。
