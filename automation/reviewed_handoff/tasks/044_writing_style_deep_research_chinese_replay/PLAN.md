---
schema: AI_BRIDGE_REVIEWED_PLAN_V1
task_key: 044_writing_style_deep_research_chinese_replay
decision: PLAN_FROZEN
---

# 044 Writing Style — Deep Research 中文长报告 replay

## Revision 1 note

Human acceptance rejected the Round-1 PASS. The user actually read the private `rewritten_report.md` and found that it still failed the core reader-facing goal: ordinary English abstraction labels and English scientific syntax still carried too much of the Chinese prose structure. This Plan revision tightens acceptance and review ownership before any further production change is made.

The Round-1 output is now a failed baseline under this revised Plan. Its failure is not that protected technical names remained; the failure is that ordinary abstractions such as `provenance`, `estimand`, `scientific gap`, `residual gap`, `state of the art`, `resource contract`, `testbed`, `contract`, `baseline`, `shared initialization`, `local drift`, and `pooled gap` still repeatedly behaved as reader-facing sentence skeletons.

## Objective and value

验证现有 `writing-style` 是否真的能把一份难读的中文科研长报告改成自然、直接、低认知负担的中文，同时保持研究内容完全可信。该任务首先是一次真实 replay，而不是预设“skill 一定有 bug”。如果当前 plugin 已经能把材料改好，就停止修改；如果真实输出仍难读，再做最小、可泛化的能力修正。

用户最终获得的不是更多规则，而是两个可观察结果：

1. 同一份 Deep Research 报告经过 `writing-style` 后，事实、数字、公式、算法/数据集名称、引用、结论强度和证据边界不发生漂移；
2. 正文从英文抽象标签、翻译腔和代理式科研话语，变成中文读者第一次阅读就能理解“谁做了什么、为什么、结果说明什么”的表达。

这份 PDF 是已知 replay/stress case。它可以证明已知问题是否被当前/修改后的 plugin 处理好，不能证明对所有中文报告的 unseen generalization。

## Frozen decisions

- 保留现有顶级 `writing-style` plugin，不新增“说人话”plugin，不拆分新的顶级 skill。
- `chinese-prose` 是本任务主要 owner；`writing-fidelity` 只在其当前合同实际阻碍“保留语义但整句重写”时做最小澄清。
- `research-reporting` 继续负责科研报告的科学结构；本任务不让 style 层重新决定研究问题、方法路线、证据强弱或实验结论。
- 必须先使用**未修改的当前 production plugin**完整处理真实输入。只有 baseline 未达到本 Plan 的验收门槛时才允许修改 production skill/plugin。
- “不改变内容”指不改变语义、事实、数值、公式、变量、算法/数据集名称、引用、归因、条件、限制、不确定性和结论强度；它不等于逐字保留原句、英文语序或段落内部说明顺序。
- 用户明确允许为降低认知负担而拆句、合句、改写句法、把主语和动作提前、调整段落内部解释顺序，并把抽象标签改写为它在当前句子中实际表达的意思。
- 不用禁词表或逐词替换解决问题。`anchor`、`provenance` 等只是这份材料暴露问题的例子，不得成为项目专用 hard-code；合法技术语境中确实需要英文时必须能保留。
- 普通科研抽象词是否保留英文，继续按语义判断：只有删除英文会损失专业识别、精确定位或约定俗成技术含义时才保留；否则优先用自然中文把实际含义说清楚。
- “直白、生动”不得通过新增来源没有的类比、例子、因果解释或研究判断实现。允许更具体的动词、主语、条件和解释顺序；不允许编造内容。
- 完整输入 PDF 和完整重写稿默认保持 repo-untracked，避免把未公开科研内容复制进公开仓库。Executor 从用户提供的本机路径读取，并把完整重写结果写到用户指定的外部输出目录。GitHub 只保存通用实现、测试、Reviewed Handoff 状态和不泄露正文的结果摘要。
- 同一份 PDF 可用于 baseline 与修复后 replay；它不能在调参后再被称为 holdout。
- Round-1 Reviewer 没有读取完整 private rewrite，因此它的 PASS 只能说明执行路径、CI 和公开证据摘要通过；不能作为本任务最终产品质量结论。用户实读结果高于该 Round-1 PASS。

### Baseline-first decision

1. 先用当前 `writing-style` 正常用户入口处理整份报告，不得手写一个只对该 PDF 有效的临时 prompt 冒充 plugin 能力。
2. 如果 baseline 已同时满足“语义/证据零漂移 + 阅读难度明显下降”，不要修改 production skill，只记录当前 plugin 已足以处理该案例，并交付重写结果。
   Round-1 baseline 已经由用户实读判定失败，因此后续实现应把它作为 production `writing-style` 在该真实 replay 上的失败证据处理。
3. 如果 baseline 失败，Executor 只允许在下述既有层中做最小通用修正，并在同一份报告上重跑：
   - `chinese-prose` 的整句/段落中文化与可读性规则；
   - `writing-fidelity` 对 `rewrite` 模式的保真边界，如果其当前结构保护导致模型不敢正常重述；
   - `writing-style` routing/description，仅当正常自然语言请求没有稳定触发中文终审时；
   - 对应 checklist、tests、generated plugin parity。
4. 若失败原因超出这些冻结边界，进入 `NEEDS_GPT_PLANNER`，不得自行扩展到新 plugin、新 schema 或研究报告结构重做。

## Implementation scope

允许按 baseline 证据选择性修改：

- `skills/writing/core/chinese-prose/SKILL.md`
- `skills/writing/core/chinese-prose/references/*`
- `skills/writing/core/writing-fidelity/SKILL.md`（仅当确认 literal/structural protection 阻碍本任务）
- `scripts/codex_marketplace_config.json`（仅当 routing/front-door 描述确有缺口）
- 与 `writing-style` / `chinese-prose` / `writing-fidelity` 直接相关的现有 tests
- `docs/plugin-todos/writing-style.md`：根据 replay 证据更新该条目的状态
- generated `plugins/codex/plugins/writing-style/` 与 Marketplace layer：只能通过现有 generator 重建，不手改
- `results/044_writing_style_deep_research_chinese_replay/`：只提交不泄露原报告正文的执行/评审摘要

不得把完整用户 PDF、完整原文抽取、完整重写稿或项目专用 phrase list 提交到 repository。

### Expected generic improvement if baseline fails

优先解决以下能力，而不是记忆单词：

- **从“翻译词”升级为“解释意思”**：普通英文抽象名词不机械找中文同义词，而是根据句子说明它实际指什么。
- **从“逐句润色”升级为“语义保真的整句重述”**：保留所有信息，但允许把长句重新组织成正常中文主谓结构。
- **区分语义保真与表面结构保真**：用户明确要求 rewrite 时，保护的是内容和证据，不是原句英文语序、每个段落边界或内部说明顺序。
- **科研术语分层**：FedFisher、M&Ms、Dice、公式变量等精确技术名继续保留；`gap`、`contract`、`scope` 等普通抽象标签只有在确有不可替代含义时才保留英文。
- **不靠删内容变简单**：限制、反例、负结果、条件和未决问题都必须留下。

## Acceptance and regression gates

### A. 真实 replay：内容保真

对 baseline 和修复后输出都建立 protected-span / claim-level 核查。最终通过至少要求：

- 数字、年份、样本量、指标值、通信量、公式、变量、算法名、数据集名和引用不被改写成别的内容；
- 不新增或删除科学主张、证据、限制、停止条件、下一步条件；
- 不把“可能/推断/条件性”改成“证明/确定”，也不反向弱化原有明确结论；
- 不改变谁做了什么、哪些内容来自项目事实、哪些是研究判断；
- 不通过总结、删段或压缩信息量来假装“更易读”。

机械 protected-span 检查只能辅助，不能替代 claim-level 人工/模型审阅。

### B. 真实 replay：阅读难度

最终完整重写稿必须达到：

- 普通中文研究者无需先理解内部代理/工作流语言就能读懂；
- 大量普通英文抽象标签不再充当句子骨架；保留下来的英文有明确专业或定位理由；
- 不是把 `anchor -> 锚点`、`provenance -> 来源追踪` 逐词替换后原句照搬，而是直接解释当前句子真正要说的区别、证据或限制；
- 长句在不丢条件的情况下拆成可追踪的逻辑关系，主语、动作、原因、结果更靠近；
- 标题和段落直接描述科学内容，不使用代理式元话语制造专业感；
- 用户能明显感到比原 Deep Research PDF 更容易连续阅读。用户的真实阅读反馈高于机械 style score。

### B2. Artifact-aware review

最终 Reviewer 必须实际读取完整 `rewritten_report.md`。完整用户材料仍不得提交公共 GitHub，但必须通过 task-local private path、host-local review、或其他不公开材料正文的真实 review path 让 Reviewer 读取最终产物。

如果 Reviewer 无法读取完整最终产物，只能返回 `REVISE` 或等待证据；不能因为 CI、摘要、protected-span 计数或 Executor 自述通过就判 `PASS`。

Reviewer 需要明确记录它读取的是哪一个最终稿路径，以及它如何检查 reader-facing 可读性、普通英文抽象标签、用户明确禁用的表达和内容保真之间的平衡。

### B3. Chinese-first reader-facing gate

最终正文必须让中文研究者直接理解。普通英文抽象标签不得承担中文句子的主要语义结构；保留下来的英文必须是算法名、数据集名、模型名、指标名、公式/代码标识、论文题名、引用原文，或确有检索/定位价值的正式术语。

不能靠逐词翻译解决问题。修改应按当前句子的实际意思整句或整段重述，例如把 provenance 类表达改成“这个 checkpoint 当初用过哪些病例，目前能确认到什么程度”，而不是把 `provenance` 机械换成“来源追踪”。

`one-shot` 可以在首次定义后按语境保留；`pooled`、`client`、`checkpoint`、`baseline` 等词不能因为领域里常见就自动保留。若它们在当前句子里只是普通概念，应优先写成自然中文。

### B4. Explicit user-constraint gate

本次实际最终稿的 reader-facing prose 不得继续出现 `provenance`，除非它是必须逐字保留的正式标题、代码标识、路径、引用原文或论文/软件专名。

Production skill 的通用修复不得 hard-code 一个项目专用 `provenance` 禁词表；应解决“普通英文抽象标签没有被语义化重述”的一般问题。

### B5. Reviewer ownership

明显违反 frozen Plan 或用户明确长期要求的问题必须由 Planner/Reviewer 判 `REVISE`。Human gate 只保留真正需要主观取舍的最终偏好，不得把普通英文抽象标签残留、未读完整 artifact、或 reader-facing 中文不达标这类可检查质量问题外包给用户。

### C. 通用回归

至少加入/更新少量**非项目专用**回归，覆盖：

1. 中文科研段落含多个普通英文抽象标签，要求按语义重述而非词表替换；
2. 同一段同时包含必须保留的算法/数据集/指标英文名，不能“全翻译”；
3. 有明确限制与不确定性的段落，简化后不能删 caveat；
4. 用户只要求轻度润色时，不得擅自结构性重写；用户明确要求“重新讲清楚”时，允许在语义不变的前提下做更大幅度句法重构；
5. README/状态说明等相邻场景不能因为本次科研报告修正而退化。

不要把这份 PDF 的完整句子或专有研究结论做成 tuning fixture。

### D. Production entry point

Reviewer 必须验证正常用户请求能够经 `writing-style` front-door 到达正确能力，而不是只有测试 helper 会：

- “把这份中文科研报告说人话重写一遍，内容、公式和引用不要动。”
- “这份 Deep Research 太难读了，保留全部信息，用正常中文重新讲清楚。”
- “不要只替换英文术语，按中文逻辑把每句话说直白，但别改研究结论。”

### E. Build / repository

- source / generated plugin parity 正确；
- relevant tests、完整 validate/audit、Marketplace build 按仓库现行要求通过；
- 不新增顶级 skill/plugin/schema/state；
- 不把完整用户研究材料提交到公开仓库；
- CI 若该任务要求则必须真实通过，不能用本地 PASS 代替。

### Version decision

Repository bump decision: NONE
Reason: 本轮是 `writing-style` 的真实 replay 与 bounded refinement，不直接打 repository release。
Affected plugins:
- `writing-style`: NO_BUMP
  Reason: 先证明真实行为改善并由用户验收；若形成值得正式发布的 improvement batch，后续单独按 canonical version policy 决定 `0.1 -> 0.2` 与 repository patch release，不在本任务中顺手 bump。

## Natural-language usage / routing expectations

### should-trigger

- “把这份中文科研报告说人话重写一遍，内容一个都别丢。”
- “这份 Deep Research 太像机器写的了，用正常中文重新讲清楚。”
- “保留公式、数字、引用和结论，只把表达改得直白好读。”
- “不要一堆 anchor / gap / contract 这种抽象标签，直接告诉我每句话到底什么意思。”
- “把这份技术报告按中文逻辑重写，不要逐词翻译英文术语。”
- “可以大幅改句子，但不能改研究内容和证据边界。”
- “帮我做中文最终审校，读起来像正常科研人员写的报告。”

### should-not-trigger

- “核查这份报告引用的论文到底存不存在。” → citation / research-writing
- “把这 22 页压缩成一页摘要。” → summarization，允许删减信息，不属于纯 style rewrite
- “重排这个 PDF 的字体、页边距和表格。” → PDF/document mechanics
- “Polish this English Results section.” → `scientific-prose`
- “重新设计这个研究方向并补几个新实验。” → research reasoning，不属于 writing-style

### neighbor skills

- `writing-fidelity`：保护事实、证据和用户纠错；不是中文自然表达 front-door。
- `research-reporting`：决定科研报告的科学叙事与决策结构；不负责中文最终“说人话”。
- `scientific-prose`：英文科研成稿，不处理中文终审。

### front-door

`writing-style` plugin → `chinese-prose` (`zh`)；用户不需要知道内部 skill 名。

## Out of scope

- 不重新研究、核查或扩展这份 Deep Research 的联邦学习科学内容。
- 不新增或修正文献引用；发现疑点只能记录，不得趁 style rewrite 改科学事实。
- 不把 style plugin 变成摘要器、翻译器、PDF 排版器或 research-reporting 替代品。
- 不为了这份报告新增 FedFisher/CARE/M&Ms 等项目专用规则。
- 不在本任务中声称 unseen/generalization PASS。
- 不在本任务中发布 `writing-style 0.2` 或 repository patch release。
- 不在本任务中解决 ChatGPT/Deep Research 对自定义 plugin 的产品集成；该分发路径在 plugin 质量稳定后单独验证。
