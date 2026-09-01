# writing-style — Long-Term TODO

Canonical maintenance inbox for the `writing-style` plugin.

## Incoming real-use feedback

### English scientific slide microcopy remains formulaic without an explicit writing pass
status: NEW
source: TRACE / CAT-TRACE group-meeting deck v4–v7 reviews
evidence: `YuukiAS/TRACE` commits `e36cb5d93fc882ce158d88ac9201fe494b98b69a`, `1de90f2f26b3f787073ecedd7a4df41a985712eb`, `ef08bc25673fb33b639e523504676c0f333d93f4` and `e5bce0c0b8d24b33aa6930a2ea8f9a8a9c86e252`; v4 exposed repeated `Failure prevented` / mechanical `Example.` language, v5 still contained `What it measures` and `Focal method`, v6 still used terse internal stage labels such as `Backbone` / `Rare fit`, and v7 still contains unnecessary comparison microcopy such as `Methods compared` followed by `CAT-TRACE decomposition`, where the main method is already obvious from the slide and `decomposition` adds abstraction rather than clarity
problem: 最终英文 scientific slide 仍可能保留模板化标签、内部分类腔和不自然 microcopy。连续多轮说明即使 presentations 已要求 scientific-prose final pass，也不能只检查语法和明显 AI 模板句；还要判断一个 label 是否真的是研究者会对听众使用的最直接说法。方法流程 subheading 应说明“这一步做什么”；比较页如果真正需要的是 baseline，就直接写 `Baselines` 并说明每个 baseline 承担什么角色，不要为了结构化额外创造 `Focal method`、`Methods compared`、`decomposition` 等抽象层。
project-specific context: CAT-TRACE、TRACE、CORAL、catalogue/open-tail、具体 metric、公式和具体 slide 句子属于当前项目；不能为这个 deck 建专用禁词表，也不能让 writing-style 改动公式、模型结构、页面布局或科学 claim。

## Open candidates

### Keep style cleanup downstream of scientific structure
status: CANDIDATE_GENERIC
source: real Presentation and advisor-report revisions
evidence: repeated user feedback on AI-like internal language, rhetorical templates and unnatural Chinese
target layer: writing
problem: style rules can accidentally take ownership of scientific structure or artifact mechanics.
candidate_action: preserve the current boundary: `writing-fidelity` protects facts, `scientific-prose` / `chinese-prose` polish reader-facing language after evidence/structure are stable.
promotion_gate: only add new style rules when repeated across independent real artifacts; do not duplicate research-reporting/presentation structural rules.

### Deep Research 中文报告语义化重述仍保留英文抽象骨架
status: PROMOTE_NOW
source: ChatGPT Deep Research 中文科研报告，2026-08-31；该 PDF 由 Deep Research 直接生成，**没有经过 `writing-style` plugin**。
evidence: 用户提供的 22 页 PDF《共享预训练医学分割模型下的极低通信联邦适应：项目事实审计、算法前沿与下一轮实验决策》；正文反复出现 `anchor`、`provenance`、`estimand`、`scientific gap`、`method gap`、`residual gap`、`resource contract`、`strict one-shot contract`、`testbed`、`axis`、`comparator`、`correction/stability run` 等表达，并存在“法律意义上证明”“forensic-level exact provenance proof”一类不必要的法律/取证腔。Reviewed Handoff 044 已通过 production `writing-style@yuukias-ai-skills` baseline replay 补齐证据：`ai-bridge plugin-replay` run `20260831T124239Z-b8734d927221`，完整改写稿保存在本机 `.ai-bridge/plugin-replay/.../outputs/044_writing_style_deep_research_chinese_replay/`，未提交私有正文。
target_layer: writing
problem: Round-1 human acceptance 和后续 Text Review 已确认 production replay 仍失败：完整 `rewritten_report.md` 仍反复让普通英文抽象标签、英文关系链、noun-stack 和内部仓库/审计元话语承担中文标题、段落骨架或论证关系。问题不是禁掉某个词，也不是做中英词表替换，而是 `chinese-prose` / `writing-fidelity` 需要更明确地区分受保护专名与普通英文工作流标签，并允许在保真前提下整句重述，把这些标签按当前语境讲成自然中文。
project-specific context: PDF 的具体研究对象是 one-shot federated medical segmentation、CARE、M&Ms、FedFisher/FedLPA 等；这些算法、数据集、公式和研究判断属于项目内容，不应被写成通用风格规则。该 PDF 只能作为已知 replay/stress case，不能在反复迭代后再冒充 unseen/generalization holdout。
candidate_action: 在不新增顶级 skill/plugin、不创建项目专用禁词表的前提下，强化 `chinese-prose` 的“语义化重述”规则、全稿残留英文扫描、科研专名/普通抽象概念分层，以及 reader-facing 正文与 repo/audit evidence locator 的叙述边界；同时澄清 `writing-fidelity` 在 rewrite 模式保护的是语义、事实和证据边界，不是英文语序、段落表面结构或普通英文抽象标签本身。
promotion_gate: 044 修复后必须通过 fresh production replay、内容保真检查、真实可读性检查、完整 Text Review、unrelated regression 和 CI；最终 Reviewer 必须消费完整 Text Review evidence，不能只看公开摘要、CI 或 protected-span 计数。

## Do not do

- Do not create detector-evasion or generic humanizer behavior.
- Do not let style rewriting change equations, claims, labels, versions or citation meaning.
