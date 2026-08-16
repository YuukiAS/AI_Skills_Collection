# 002 Writing Style — Planner Review

reviewed_commit: `0ecd81fd82157a4f2dbc53a942b2070b1624c4f6`
current_main_control_commit: `c31fe6f2f6d5d514ce6b77830f7386d31f3a0f1b`
review_round: 1
decision: PASS
next_task_key: `003_presentations`

## 结论

002 已达到冻结计划要求，可以进入 003。当前 `writing-style` 已经形成清楚的三层协作：`writing-fidelity` 负责保住事实、用户纠错、版本身份和受保护内容；`chinese-prose` 负责中文面向读者的自然表达与“说人话”终审；`scientific-prose` 负责英文科研成稿的证据强度、模板腔和过度防御式表达。三者不再把同一种风格修改都写成自己的主职责。

本轮没有新增 humanizer、anti-AI 或检测规避技能，也没有改变当前十插件 Marketplace 拓扑。Planner 未发现需要阻断 002 的调用冲突、生成层不一致或回归问题。

## 冻结要求核查

### 1. `writing-fidelity` 已明确为保真层，而不是通用文风层

当前 source 的 description 和正文都明确把它定位为 preservation layer，保护事实、纠错、标签、结构、公式、引用、版本权威和最终产物身份；中文自然表达交给 `chinese-prose`，英文科研风格交给 `scientific-prose`。同时保留了“Preserve first. Improve second.”这一优先级。

因此以下请求已经可区分：

- “只润色，数字、标题、公式、引用和结构不要动。” → `writing-fidelity` 作为保真门槛；
- “把这段中文写自然一点，别像日志。” → `chinese-prose`；
- “Polish this Results section without overstating the evidence.” → `scientific-prose`。

### 2. 中文“说人话”规则已经落到可泛化语义，而不是单纯禁词

`chinese-prose` 当前明确要求：正文优先用连贯段落，列表只在步骤、比较、清单或确实需要快速扫描时使用；不要为了结构化把每句话拆成 bullet，也不要机械凑三点式、对称排比、重复总结或固定“首先/其次/此外/综上”。

英文保留也采用语义判断：如果去掉英文不会损失准确含义、专业识别或机器定位能力，就优先写中文；模型、指标、代码、路径、配置和精确状态等需要定位的内容继续保留。这符合冻结计划的“中文优先但不损害精确性”。现有常见替换表只是示例，不是触发机制或硬编码禁词器。

### 3. “降低 AI 味”没有越界成检测规避或伪原创

`writing-fidelity`、`chinese-prose` 和 `scientific-prose` 都明确排除了 AI detector evasion、source laundering、隐藏 AI 来源或通过删除真实 limitation 来制造更像人工的文本。允许做的是减少套话、翻译腔、模板腔和无证据的拔高，同时维持原始事实和证据边界。

### 4. 英文科研成稿边界足够清楚

`scientific-prose` 现在明确说明它不是 manuscript planner、citation verifier 或中文终审；它用于证据和目标段落已经明确之后的英文成稿质量 pass，并要求真实 limitation 必须保留且写得准确、成比例。

与 001 的 `scientific-writing` 也能按自然任务区分：

- “把已有实验结果写成完整 Results 正文。” → `scientific-writing`，负责真正的论文段落起草/修改；
- “这版英文 Results 已经写完，帮我去掉模板腔并检查有没有 overclaim。” → `scientific-prose`，负责最终英文表达与证据强度终审。

当前没有证据表明两者仍存在无法由任务阶段和意图区分的同义入口，因此不在 002 重新打开 001。

## Profile、Marketplace 与生成层

`global-baseline` 继续同时包含 `writing-fidelity`、`scientific-prose` 和 `chinese-prose`，因此通用环境仍具备保真 + 中文自然表达 + 英文科研表达三层能力。

`writing-style` Marketplace 插件的描述和默认请求也已同步到新的职责边界。Planner 抽查 generated snapshot，`plugins/codex/plugins/writing-style/skills/fidelity/SKILL.md` 与 source 中的新保真/hand-off 规则一致，没有出现只改 source、生成插件仍保留旧职责的情况。

当前 Marketplace 仍保持 10 个插件与 `marketplacePluginBudget=10`，002 没有删除或新增顶级插件。

## 自然语言验收

Planner 直接按冻结计划的近邻请求做了语义检查：

- “把这个 README 改得像人写的，中文为主，命令和路径别动。” → `chinese-prose` 主处理自然表达，同时由 `writing-fidelity` 保护命令、路径和事实。
- “这份进展报告别像审计日志，先把结论说清楚。” → `chinese-prose`，规则明确要求第一段先给读者判断，机器字段和日志后置。
- “普通英文能翻成中文的就翻掉，模型名和代码保留。” → `chinese-prose`，与当前语义化英文保留规则一致。
- “别每句话一个 bullet，用正常段落写。” → `chinese-prose`，当前正文已有直接验收规则。
- “只润色，数字、标题、公式、引用和结构不要动。” → `writing-fidelity`，不会把保护对象交给纯风格修改自行决定。
- “Remove defensive wording from this rebuttal but keep the real limitation.” → `scientific-prose`，当前规则明确禁止为了更自信而抹掉真实局限。

这些请求不要求用户知道内部 skill 名，且没有发现必须靠关键词硬分流才能解释的明显歧义。

## 验证与远端状态

Executor 报告的完整本地验证链通过：149 个 active skills 校验、全库 audit、registry/catalog/provenance/Marketplace 生成、icon/provenance checks、100 个单元测试以及 `git diff --check` 均成功。

Planner 独立核对了真实 GitHub Actions：

- 实现提交 `0ecd81fd82157a4f2dbc53a942b2070b1624c4f6` 的 `Codex Marketplace` workflow 已由 Executor 记录为 `completed / success`；
- 当前结果提交 `c31fe6f2f6d5d514ce6b77830f7386d31f3a0f1b` 的 `Codex Marketplace` workflow 为 `completed / success`。

没有 CI 等待项需要继续阻断 002。

## 下一步

002 结束。Codex 可以开始 `003_presentations`，严格读取：

`automation/reviewed_handoff/tasks/003_presentations/PLAN.md`

003 重点是返修现有 `presentations` Marketplace 插件与 `presentation-desktop`：取消“科研/学术默认 Beamer”的旧硬默认，按用户实际交付格式决定 editable PPTX/Slides 或 Beamer，并把 render + visual QA 作为完成门槛。不要借 003 重新打开已经通过的 001/002。