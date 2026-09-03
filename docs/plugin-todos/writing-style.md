# writing-style — Long-Term TODO

Canonical maintenance inbox for the `writing-style` plugin.

## Incoming real-use feedback

### English scientific slide microcopy remains formulaic without an explicit writing pass
status: NEW
source: TRACE / CAT-TRACE group-meeting deck v4 review
evidence: `YuukiAS/TRACE` commit `e36cb5d93fc882ce158d88ac9201fe494b98b69a`; v4 P2–P19；presentation task读取了 `scientific-prose`，但没有把 dedicated writing-style replay 作为独立完成步骤
problem: 最终英文 slide 仍出现反复的 `Failure prevented`、机械 `Example.` 标签、`as new samples arrive` 一类不自然微文案，以及把结构化事实压成 noun-stack/table-contract 语言的情况。当前证据说明 presentation production 只“读写作规则”仍不足以保证自然科研英语；需要先用现有 `scientific-prose` 对已经冻结科学结构的可见英文做一次真实 replay，确认问题来自 routing 未执行，还是 skill 本身仍缺 slide-specific microcopy 能力。
project-specific context: CAT-TRACE、TRACE、CORAL、catalogue/open-tail 等科学术语和具体句子属于项目；不能为这个 deck 建专用禁词表，也不能让 writing-style 改动公式、模型结构、页面布局或科学 claim。

## Open candidates

### Keep style cleanup downstream of scientific structure
status: CANDIDATE_GENERIC
source: real Presentation and advisor-report revisions
evidence: repeated user feedback on AI-like internal language, rhetorical templates and unnatural Chinese
target layer: writing
problem: style rules can accidentally take ownership of scientific structure or artifact mechanics.
candidate action: preserve the current boundary: `writing-fidelity` protects facts, `scientific-prose` / `chinese-prose` polish reader-facing language after evidence/structure are stable.
promotion gate: only add new style rules when repeated across independent real artifacts; do not duplicate research-reporting/presentation structural rules.

### Deep Research 中文报告语义化重述仍保留英文抽象骨架
status: CANDIDATE_GENERIC
source: ChatGPT Deep Research 中文科研报告，2026-08-31；该 PDF 由 Deep Research 直接生成，**没有经过 `writing-style` plugin**。
evidence: 用户提供的 22 页 PDF《共享预训练医学分割模型下的极低通信联邦适应：项目事实审计、算法前沿与下一轮实验决策》；正文反复出现 `anchor`、`provenance`、`estimand`、`scientific gap`、`method gap`、`residual gap`、`resource contract`、`strict one-shot contract`、`testbed`、`axis`、`comparator`、`correction/stability run` 等表达，并存在“法律意义上证明”“forensic-level exact provenance proof”一类不必要的法律/取证腔。Reviewed Handoff 044 已通过 production `writing-style@yuukias-ai-skills` baseline replay 补齐证据：`ai-bridge plugin-replay` run `20260831T124239Z-b8734d927221`，完整改写稿保存在本机 `.ai-bridge/plugin-replay/.../outputs/044_writing_style_deep_research_chinese_replay/`，未提交私有正文。
target layer: writing
problem: Round-1 human acceptance 已确认 production replay 仍失败：完整 `rewritten_report.md` 仍大量让 `provenance`、`estimand`、`scientific gap`、`residual gap`、`state of the art`、`resource contract`、`testbed`、`contract`、`baseline`、`shared initialization`、`local drift`、`pooled gap` 等普通英文抽象标签承担中文句子的骨架。问题不是禁掉某个词，也不是 `provenance -> 来源追踪` 一类词表替换，而是 `chinese-prose` / `writing-fidelity` 需要更明确地允许在保真前提下整句重述，把这些标签按当前语境讲成自然中文。
project-specific context: PDF 的具体研究对象是 one-shot federated medical segmentation、CARE、M&Ms、FedFisher/FedLPA 等；这些算法、数据集、公式和研究判断属于项目内容，不应被写成通用风格规则。该 PDF 只能作为已知 replay/stress case，不能在反复迭代后再冒充 unseen/generalization holdout。
candidate action: 在不新增顶级 skill/plugin、不创建项目专用禁词表的前提下，强化 `chinese-prose` 的“语义化重述”规则、全稿残留英文扫描和科研专名/普通抽象概念分层；同时澄清 `writing-fidelity` 在 rewrite 模式保护的是语义、事实和证据边界，不是英文语序、段落表面结构或普通英文抽象标签本身。
promotion gate: 044 修复后必须通过完整 replay、内容保真检查和真实可读性检查；最终 Reviewer 必须读取完整本地最终稿，不能只看公开摘要、CI 或 protected-span 计数。

## Do not do

- Do not create detector-evasion or generic humanizer behavior.
- Do not let style rewriting change equations, claims, labels, versions or citation meaning.
