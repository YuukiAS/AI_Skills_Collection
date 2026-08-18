---
schema: AI_BRIDGE_REVIEWED_PLAN_V1
task_key: 002_writing_style
decision: PLAN_FROZEN
---

# 002 Writing Style — Plan

## 目标

把现有 `writing-style` 从“已有三个写作 skill”整理成一个边界清楚、默认可用的成稿质量层。用户不需要记住内部 skill 名，只需说明“改自然一点”“中文说人话”“不要 AI 味”“保留事实”“科研英文别写得像模板”，系统就能稳定分派。

## 冻结决定

- 保留现有 `writing-style` plugin，不新增顶级 plugin。
- 保留 `writing-fidelity`、`chinese-prose`、`scientific-prose` 三个现有 skill，不新增 humanizer / anti-AI / detector-evasion skill。
- `writing-fidelity` 是保真底线：保护事实、数字、标签、结构、公式、引用、用户纠错和最终产物身份；它不负责把所有文字改成某种文风。
- `chinese-prose` 是中文面向读者的默认终审：中文报告、README、Markdown/PDF、幻灯片文案、技术说明等，默认在不损伤事实的前提下改成自然中文。
- `scientific-prose` 是英文科研成稿终审：英文论文、报告、rebuttal、caption、slide text 等，重点处理证据强度、模板腔和过度防御式写法。
- 中文任务中普通英文概念是否保留，采用语义判断而不是硬编码禁词表：**如果去掉英文不会损失准确含义、专业识别或机器定位能力，就优先写中文；只有专名、模型/指标、路径、代码、配置、精确状态等需要保留英文。**
- 面向人的正文默认使用连贯段落；列表只在步骤、并列比较、清单或需要快速扫描时使用。不要为了“结构化”把每句话拆成 bullet，也不要一两句就另起小标题。
- 不机械追求三点式、对称排比、重复总结或固定“首先/其次/此外/综上”结构。结构由内容决定。
- 不把“去 AI 味”理解成随意口语化或伪装人工来源；目标是具体、自然、少套话、少翻译腔，并保持事实边界。

## 允许修改

主要检查并按需要修改：

- `skills/writing/core/writing-fidelity/SKILL.md`
- `skills/writing/core/chinese-prose/SKILL.md`
- `skills/writing/core/chinese-prose/references/*`
- `skills/writing/core/scientific-prose/SKILL.md`
- `skills/writing/core/scientific-prose/references/*`
- `scripts/codex_marketplace_config.json`
- `profiles/global-baseline.json`
- `profiles/presentation-desktop.json`
- 与 writing-style routing / generated plugin 相关的现有测试和生成层

如果已有内容已经满足标准，不为了制造 diff 强行改。

## 调用边界

### `writing-fidelity`

应处理：
- “只润色，数字、标题、公式、引用和结构不要动。”
- “按我最新纠错改这份报告，不要又恢复旧版本。”
- “这是最终 PDF，不要把 audit/preview 当成交付物。”

不应单独承担：
- “把这段中文写得更自然、更像人写的。” → `chinese-prose`
- “把英文 Results 改得更像科研论文，别过度防御。” → `scientific-prose`

### `chinese-prose`

应处理：
- “把这个 README 改得像人写的，中文为主，命令和路径别动。”
- “这份进展报告别像审计日志，先把结论说清楚。”
- “普通英文术语能翻成中文的就翻掉，模型名和代码保留。”
- “别每句话一个 bullet，用正常段落写。”
- “去掉模板腔和 AI 味，但不要拔高结论。”

不应处理：
- 事实核查、文献搜索、代码修改、纯文件格式转换。

### `scientific-prose`

应处理：
- “Polish this Results section without overstating the evidence.”
- “Remove defensive/self-undermining wording from this rebuttal but keep the real limitation.”
- “Make this English slide text sound like a researcher, not a generic AI summary.”

不应承担：
- 中文“说人话”终审；
- 整篇论文结构规划；
- 引用真实性核验。

## 验收门槛

- `writing-style` 三个 skill 的 description 和正文边界不互相吞噬。
- `global-baseline` 继续默认包含三者，使通用环境具备保真 + 中文自然表达 + 英文科研表达。
- 中文自然表达规则明确覆盖：普通概念中文化、段落优先、避免日志式正文、避免机械三件套/重复总结、先结论后证据。
- 不能通过大规模硬编码“禁词列表”实现；应是可泛化语义规则。
- 必须保留“先保真，再自然”的优先级。
- 不得引入 AI detector evasion、伪原创或隐藏 AI 来源的目标。
- 更新后生成层一致，完整 `validate`、`audit --all`、marketplace build、unittest 通过。
- Planner/Reviewer 必须用上述自然语言样例和近邻反例直接检查，不得只看测试绿灯。

## 用户可见示例

最终报告至少展示 3 组“以前容易出现的问题 → 新规则如何处理”的简短 before/after 或行为对比，例如：

- 中文技术报告从英文流程词堆叠变成中文结论优先，但保留 `CURRENT.json`、`PASS` 等精确 token。
- 原来每句话一个 bullet 的说明改成连贯段落，仅在真正需要扫描时保留列表。
- 英文科研段落去掉空泛价值拔高和 defensive wording，但没有把真实 limitation 删除。

## Frozen decisions

对应本计划中的 `## 冻结决定`、`## 调用边界` 和 `## 不在本任务范围`。本节为 Reviewed Handoff v0.5 validator 的英文标准章节别名，不改变原冻结合同。

## Implementation scope

对应本计划中的 `## 允许修改`。执行范围仍以原中文章节为准。

## Acceptance and regression gates

对应本计划中的 `## 验收门槛` 和 `## 用户可见示例`。验收语义不变。

## Out of scope

对应本计划中的 `## 不在本任务范围`。

## 不在本任务范围

- 不处理科研论文各阶段 routing；001 单独负责。
- 不处理 PPT 文件生成和视觉 QA；003 单独负责。
- 不新增 Notion/外部资源。
- 不把用户整份私人个性化原样复制进公共 skill，只提炼可泛化写作规则。