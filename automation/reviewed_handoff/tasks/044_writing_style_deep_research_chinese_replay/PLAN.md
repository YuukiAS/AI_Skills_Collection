---
schema: AI_BRIDGE_REVIEWED_PLAN_V1
task_key: 044_writing_style_deep_research_chinese_replay
decision: PLAN_FROZEN
---

# 044 Writing Style — Deep Research 中文长报告 replay

## Objective and value

验证并按需完善现有 `writing-style` plugin，使一份难读的中文科研长报告在不改变研究内容、事实、数字、公式、算法/数据集名称、引用、结论强度和证据边界的前提下，真正变成自然、直接、低认知负担的中文。

本任务仍然只处理原始 044 目标：同一份已知 Deep Research 报告的“说人话”重写与保真验证，不新增研究内容，不扩展为新的插件或新的研究报告工作流。该 PDF 仍是 known replay/stress case，不能被称为 unseen/generalization evidence。

Review 1 曾依据摘要、protected-span 和抽查证据判定 baseline 足够，但用户随后实际阅读完整私有重写稿并明确拒绝该 PASS：全文仍有 `provenance`、`estimand`、`scientific gap`、`resource contract`、`state of the art` 等普通英文抽象标签承担中文句子结构，且 Reviewer 当时没有读取完整私有 artifact。该人类反馈推翻了“baseline 已满足 artifact-quality gate”的结论，因此本次唯一 Plan revision 只补上原计划缺失的**完整私有成品审查路径**，并允许在原 044 边界内做最小通用修复。

用户最终需要两个同时成立的可观察结果：

1. 科学内容与来源边界保持可信；
2. 完整重写稿本身经过独立全文审查，普通中文研究者可以连续阅读，不再由英文抽象标签、翻译腔和代理式科研话语承担句子骨架。

## Frozen decisions

- 保留现有顶级 `writing-style` plugin，不新增“说人话”plugin，不拆分新的顶级 skill，不创建新 Reviewed Handoff task。
- `chinese-prose` 是中文读者表达的主要 owner；`writing-fidelity` 只负责事实/证据保真边界；`research-reporting` 继续负责科学结构，不由 style 层重新决定研究问题、方法路线、证据强弱或实验结论。
- Maintenance companion: ai-skills-core
- Domain owner: writing-style
- 用户对 Review-1 PASS 的拒绝已证明原 baseline **没有**同时满足“全文自然中文 + 内容保真”。因此本轮不再允许以旧 baseline 摘要、phrase scan、protected-span 数量或局部抽查直接关闭任务。
- Longleaf 上现有的未提交 candidate repair 与第五次 replay artifact 只能作为候选实现/候选证据；在新的 source implementation、production replay、CI、回归与完整 Text Review 全部闭合前，不得把它们写成已通过结果。
- “不改变内容”继续指不改变语义、事实、数值、公式、变量、算法/数据集名称、引用、归因、条件、限制、不确定性和结论强度；它不等于逐字保留原句、英文语序或段落内部说明顺序。
- 为降低认知负担，可以拆句、合句、改写句法、把主语和动作提前、调整段落内部解释顺序，并把普通抽象标签改写为它在当前句子中实际表达的意思。
- 不使用项目专用禁词表、逐词替换或这份 PDF 的专用 hard-code。`provenance`、`estimand`、`scientific gap`、`resource contract`、`state of the art`、`anchor`、`gap`、`scope` 等仅是已暴露回归的例子，不是 blacklist；合法技术专名或为检索/精确定位必须保留的英文仍可保留。
- “直白、生动”不得通过新增来源没有的类比、例子、因果解释或研究判断实现。
- 完整输入与完整重写稿仍不得以 plaintext 提交到公开仓库；私有全文审查使用现有 `GPT_Codex_AI_Bridge_Kit` Text Review transport，GitHub 只保存加密 payload、manifest、结构化 review evidence 和非泄露摘要。
- 用户本次 recovery instruction 已明确要求完整 Text Review，因此允许通过现有 OpenAI Responses API `store=false` Text Review 路径审查该私有 artifact；不得提交 plaintext、age private identity 或 API key。
- `CURRENT.text_review_required=true`。task-local 路径固定为：
  - encrypted payload: `results/044_writing_style_deep_research_chinese_replay/text_review/payload.age`
  - manifest: `results/044_writing_style_deep_research_chinese_replay/text_review/text_inputs.json`
  - evidence: `results/044_writing_style_deep_research_chinese_replay/text_review/TEXT_REVIEW.json`
- Review 1 历史必须保留；当前 `review_round=1`，最多只剩 Review 2，不得创建 Review 3。

### Revised baseline / repair decision

原 baseline 的 process checks 可以保留为历史证据，但用户完整阅读已证明 artifact-quality gate 失败。因此本轮进入 bounded generic repair：

1. 先检查并实际消费 production `ai-skills-core` maintenance preflight，再由 `writing-style` domain owner处理写作质量。
2. 优先复用 Longleaf 上未提交 candidate repair，但必须独立检查其 diff；不得因为它已经存在就视为 frozen implementation。
3. 只允许在既有层内做最小通用修复：
   - `chinese-prose` 的整句/段落中文化与普通抽象英文标签处理；
   - `writing-fidelity` 的 rewrite 保真边界，仅当它实际阻碍语义不变的自然重述；
   - `writing-style` routing/front-door，仅当正常自然语言请求没有稳定触发中文终审；
   - 对应 checklist/tests/generated parity。
4. 修复后用 fresh production `writing-style` 对完整已知报告重新 replay；不能把手写临时 prompt、局部重写或第五次候选产物本身冒充 production plugin evidence。
5. 将最终完整重写稿加密进入 Text Review。Text Review 必须读取**完整成品**，并依据 manifest 中的 source/artifact identity 与 rubric 同时审查科学/来源保真和中文读者表达。
6. 若最终 artifact 仍不满足 revised acceptance，Review 2 必须按当前合同处理；不得再开第三轮自动返修。

## Implementation scope

允许在原 044 边界内选择性修改：

- `skills/writing/core/chinese-prose/SKILL.md`
- `skills/writing/core/chinese-prose/references/*`
- `skills/writing/core/writing-fidelity/SKILL.md`（仅在确认 literal/structural protection 阻碍自然重述时）
- `scripts/codex_marketplace_config.json`（routing/front-door 或正式版本 closure 所需）
- 与 `writing-style` / `chinese-prose` / `writing-fidelity` 直接相关的现有 tests
- `docs/plugin-todos/writing-style.md`
- `docs/plugin-changelogs/writing-style.md`、README/root changelog/repository version metadata，仅用于本轮形成正式 production improvement 后的 canonical version closure
- generated `plugins/codex/plugins/writing-style/` 与 Marketplace layer，只能从 source regenerate，禁止手改 generated mirror
- `results/044_writing_style_deep_research_chinese_replay/` 下非泄露执行摘要，以及 task-local encrypted Text Review payload/manifest/evidence

不得提交完整用户 PDF、完整 plaintext 原文抽取、完整 plaintext 重写稿或项目专用 phrase list。

### Expected generic improvement

本轮只解决原任务已暴露的通用问题：

- **从翻译词升级为解释意思**：普通英文抽象标签不能仅换一个中文同义词后继续承担句法骨架，而要根据当前句子直接说明它实际指什么。
- **从逐句润色升级为语义保真的整句重述**：保留全部事实与证据，同时允许按自然中文主谓和因果/条件顺序重组句子。
- **区分语义保真与表面结构保真**：保护内容、证据和判断强度，不保护原句英文语序、机械名词堆叠或不必要的段落内部次序。
- **术语分层**：算法、数据集、公式、变量、正式指标、论文/会议名称等需要精确定位的专名继续保留；普通研究工作流/抽象判断标签若无需英文即可准确表达，则优先直接说中文含义。
- **不靠删内容变简单**：限制、反例、负结果、条件、停止规则和未决问题必须留下。

## Acceptance and regression gates

### A. PROCESS PASS：实现与保真辅助检查

以下均是必要 process evidence，但单独不能构成最终 PASS：

- source/generated plugin parity 正确；
- relevant unit/regression tests、repository validate/audit、Marketplace build 与真实 GitHub CI 通过；
- production `ai-skills-core` maintenance preflight 已实际运行并被 Executor 消费，不能只读取 source `SKILL.md`；
- fresh production `writing-style` replay 通过正常用户入口完成整份报告；
- 数字、年份、样本量、指标值、公式、变量、算法名、数据集名、引用、路径/代码等 protected spans 的机械核查；
- claim-level 辅助检查没有发现新增/删除科学主张、改变归因、删 caveat/STOP 条件或改变结论强度；
- phrase scan/英文抽象词扫描只能帮助定位疑点，永远不能作为 artifact-quality PASS。

### B. PRODUCT / ARTIFACT PASS：完整私有 Text Review

最终 Reviewer PASS 必须建立在 fresh、identity-matched 的 `TEXT_REVIEW.json` 上，而不是 Executor 摘要或局部抽查上。Text Review rubric 必须要求审查完整最终重写稿，并同时覆盖：

**科学与来源保真**

- 不新增或删除科学主张、证据、限制、停止条件、下一步条件；
- 不把“可能/推断/条件性”改成“证明/确定”，也不反向弱化原有明确结论；
- 不改变谁做了什么、哪些是项目事实、哪些是文献事实、哪些是研究判断；
- 数字、公式、变量、算法/数据集/指标名称、引用与精确定位内容保持一致；
- 不通过删段、压缩信息量或总结替代完整重写。

**中文读者表达**

- 普通中文研究者无需理解内部代理/工作流语言即可连续阅读；
- 普通英文抽象标签不得继续承担中文句子的主干、标题骨架或反复出现的逻辑标签；
- `provenance`、`estimand`、`scientific gap`、`resource contract`、`state of the art` 等只是 regression examples：Text Review 应判断它们在具体语境中是否确有不可替代的专业/定位意义，而不是按 blacklist 机械判分；
- 不允许 `anchor -> 锚点`、`provenance -> 来源追踪` 一类逐词翻译后仍保留原机器句法；应直接说明当前句子真正要表达的证据、对象、差距、约束或比较关系；
- 长句在不丢条件的前提下有可追踪的主语、动作、原因、结果和限制；
- 标题与段落直接描述科学内容，不用代理式元话语、法律/取证腔或英文 noun-stack 制造专业感；
- 保留下来的英文必须属于算法/数据集/公式变量/正式名称/检索定位等确实有理由保留的内容。

Text Review 只有 `overall_decision=PASS` 且 evidence 绑定当前 `task_key`、`workflow_type=reviewed_handoff`、当前 implementation commit、manifest identity 与最终 plaintext SHA 时，才能支持 Review 2 的 PRODUCT / ARTIFACT PASS。缺失、malformed、stale、plaintext-SHA mismatch、manifest mismatch 或 non-PASS 都不能支持 Reviewer PASS。

当 encrypted payload 与 manifest 已存在但 fresh `TEXT_REVIEW.json` 仍在等待 GitHub workflow 时，这是 `WAITING_FOR_EVIDENCE / NEEDS_REVIEW`，不得消费 Review 2，也不得写 `BLOCKED`。

### C. 通用回归

至少保留/加入少量**非项目专用**回归，覆盖：

1. 中文科研段落含多个普通英文抽象标签，要求按语义重述而非词表替换；
2. 同段含必须保留的算法/数据集/指标英文名，不能“全翻译”；
3. 有明确限制与不确定性的段落，简化后不能删除 caveat；
4. 用户只要求轻度润色时不得擅自结构性重写；用户明确要求“重新讲清楚”时允许在语义不变前提下做更大句法重构；
5. README/状态说明等相邻场景不能因本轮科研长报告修正而退化。

不得把这份 PDF 的完整句子、专有研究结论，或上述英文 regression examples 变成项目专用 tuning fixture/禁词表。

### D. Production entry point

Reviewer 必须验证正常用户请求能经 `writing-style` front-door 到达正确能力，而不是只有测试 helper 会：

- “把这份中文科研报告说人话重写一遍，内容、公式和引用不要动。”
- “这份 Deep Research 太难读了，保留全部信息，用正常中文重新讲清楚。”
- “不要只替换英文术语，按中文逻辑把每句话说直白，但别改研究结论。”

### E. Version / release closure

当前 canonical source：repository `5.0.2`，`writing-style` `0.1`。

本 Plan 已由用户完整阅读失败证明需要 production behavior improvement；如果 Executor 最终确实修改 production `writing-style`，且 fresh real replay、unrelated regression、CI 与 full Text Review 全部 PASS，则这就是 completed compatible plugin improvement，必须在本 task 内完成版本闭环：

Repository bump decision: PATCH (`5.0.2 -> 5.0.3`)
Reason: 单个中央 plugin 的兼容 user-facing quality improvement，未增加 repository-level 新任务能力，也无 breaking contract。
Affected plugins:
- `writing-style`: `0.1 -> 0.2`
  Reason: 真实 044 artifact failure 导致通用 production 中文重写行为发生变化，并经完整 replay/Text Review 与 unrelated regression 验证。

若最终没有任何 production behavior 改动，则不得伪造 release，必须保持 `NO_BUMP` 并由 Reviewer 判断为何仍能满足本次已确认的 artifact failure；不能仅靠旧 baseline 证据得出该结论。

版本闭环必须同步 Marketplace config、plugin changelog、generated manifest、README release dashboard、root changelog 与 repository canonical version metadata，并通过 parity/regression checks。

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
- `ai-skills-core`：只负责 AI_Skills maintenance closure，不替代 `writing-style` 的中文表达判断。

### front-door

`writing-style` plugin → `chinese-prose` (`zh`)；用户不需要知道内部 skill 名。

## Out of scope

- 不重新研究、核查或扩展这份 Deep Research 的联邦学习科学内容。
- 不新增或修正文献引用；发现疑点只能记录，不得趁 style rewrite 改科学事实。
- 不把 style plugin 变成摘要器、翻译器、PDF 排版器或 `research-reporting` 替代品。
- 不为了这份报告新增 FedFisher/CARE/M&Ms 等项目专用规则。
- 不把 `provenance`、`estimand`、`scientific gap`、`resource contract`、`state of the art` 等示例固化成项目专用 blacklist。
- 不在本任务声称 unseen/generalization PASS。
- 不创建 Review 3；第二轮 Reviewer 是最后一轮自动 semantic review。
- 不在本任务解决 ChatGPT/Deep Research 对自定义 plugin 的产品集成。
- 不把 Longleaf 上未提交 candidate repair 的存在本身当作 acceptance evidence。
- 不在 Reviewer PASS 前把 dedicated 044 branch 集成回 `main`；integration 是独立的 post-acceptance step。