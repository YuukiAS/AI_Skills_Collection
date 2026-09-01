# writing-style — Long-Term TODO

Canonical maintenance inbox for the `writing-style` plugin.

## Incoming real-use feedback

### English scientific slide microcopy remains formulaic without an explicit writing pass
status: NEW
source: TRACE / CAT-TRACE group-meeting deck v4, v5 and v6 reviews
evidence: `YuukiAS/TRACE` commits `e36cb5d93fc882ce158d88ac9201fe494b98b69a`, `1de90f2f26b3f787073ecedd7a4df41a985712eb` and `ef08bc25673fb33b639e523504676c0f333d93f4`; v4 exposed repeated `Failure prevented` / mechanical `Example.` language, v5 still contained labels such as `What it measures` and `Focal method`, and v6 still used audience-facing stage labels such as `Backbone`, `Rare-species prior` and `Rare fit` even after the presentation English final-pass step
problem: 最终英文 scientific slide 仍可能保留模板化标签、内部分类腔和不自然 microcopy。v5/v6 说明即使 presentations 已要求 scientific-prose final pass，也不能只检查语法和明显 AI 模板句；还要判断一个 label 是否真的是研究者会对听众使用的最直接说法。尤其是方法流程的 subheading 应尽量说明“这一步做什么”，而不是只给内部对象名或短促工程标签。需要后续判断这是 current `scientific-prose` 本身的 slide-microcopy coverage 缺口，还是 presentation handoff 提供的上下文/验收不够。
project-specific context: CAT-TRACE、TRACE、CORAL、catalogue/open-tail、具体 metric、公式和具体 slide 句子属于当前项目；不能为这个 deck 建专用禁词表，也不能让 writing-style 改动公式、模型结构、页面布局或科学 claim。

## Open candidates

### Keep style cleanup downstream of scientific structure
status: CANDIDATE_GENERIC
source: real Presentation and advisor-report revisions
evidence: repeated user feedback on AI-like internal language, rhetorical templates and unnatural Chinese
target layer: writing
problem: style rules can accidentally take ownership of scientific structure or artifact mechanics.
candidate action: preserve the current boundary: `writing-fidelity` protects facts, `scientific-prose` / `chinese-prose` polish reader-facing language after evidence/structure are stable.
promotion gate: only add new style rules when repeated across independent real artifacts; do not duplicate research-reporting/presentation structural rules.

### Deep Research 中文报告作为 `writing-style` 的真实压力测试输入
status: BLOCKED_NEEDS_EVIDENCE
source: ChatGPT Deep Research 中文科研报告，2026-08-31；该 PDF 由 Deep Research 直接生成，**没有经过 `writing-style` plugin**。
evidence: 用户提供的 22 页 PDF《共享预训练医学分割模型下的极低通信联邦适应：项目事实审计、算法前沿与下一轮实验决策》；正文反复出现 `anchor`、`provenance`、`estimand`、`scientific gap`、`method gap`、`residual gap`、`resource contract`、`strict one-shot contract`、`testbed`、`axis`、`comparator`、`correction/stability run` 等表达，并存在“法律意义上证明”“forensic-level exact provenance proof”一类不必要的法律/取证腔。
target layer: writing
problem: 这份 PDF 证明的是一个真实的中文科研写作痛点，不是当前 `writing-style` 的 production failure，因为插件尚未实际处理过它。用户要求“说人话”层在不改变任何事实、数字、公式、算法名、数据集名、引用、结论强度和证据边界的前提下，大幅降低阅读难度；不能只做逐词翻译，而要在语义完全保真的前提下按中文逻辑重新组织句子和段落，让读者直接知道“谁做了什么、为什么、结果说明什么”。现有 `chinese-prose` 已有中文优先、非必要英文清理、报告终审等规则，因此下一步应先用**当前 production plugin**完整 replay 这份材料，再判断是已有规则已经足够、只是以前没有调用，还是确实需要修改 skill / fidelity contract / routing。
project-specific context: PDF 的具体研究对象是 one-shot federated medical segmentation、CARE、M&Ms、FedFisher/FedLPA 等；这些算法、数据集、公式和研究判断属于项目内容，不应被写成通用风格规则。该 PDF 只能作为已知 replay/stress case，不能在反复迭代后再冒充 unseen/generalization holdout。
candidate_action: baseline-first：先用未修改的 `writing-style` 对同一材料做一次完整、保真、中文优先的重写；若真实输出仍存在抽象英文标签、英文科研语序、逐词翻译、过强 `writing-fidelity` 导致不敢整句重写，或可读性明显不足，再由 Reviewed Handoff Planner 冻结最小通用修改。禁止为了这一个 PDF 增加项目词汇禁表或专门规则。
promotion_gate: 当前 `writing-style` 在该真实 replay 上无法同时满足“内容/证据零漂移”和“阅读难度显著下降”，或随后另一个独立真实中文科研材料复现同类问题；若当前 plugin 已经能把该 PDF 改好，则不为了制造 diff 修改 production skill。

## Do not do

- Do not create detector-evasion or generic humanizer behavior.
- Do not let style rewriting change equations, claims, labels, versions or citation meaning.