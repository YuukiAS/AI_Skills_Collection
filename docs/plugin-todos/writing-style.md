# writing-style — Long-Term TODO

Canonical maintenance inbox for the `writing-style` plugin.

## Open candidates

### Keep style cleanup downstream of scientific structure
status: CANDIDATE_GENERIC
source: real Presentation and advisor-report revisions
evidence: repeated user feedback on AI-like internal language, rhetorical templates and unnatural Chinese
target layer: writing
problem: style rules can accidentally take ownership of scientific structure or artifact mechanics.
candidate action: preserve the current boundary: `writing-fidelity` protects facts, `scientific-prose` / `chinese-prose` polish reader-facing language after evidence/structure are stable.
promotion gate: only add new style rules when repeated across independent real artifacts; do not duplicate research-reporting/presentation structural rules.

### Deep Research 中文报告仍大量使用抽象英文和代理式科研话语
status: NEW
source: ChatGPT Deep Research 中文科研报告，2026-08-31
evidence: 用户提供的 22 页 PDF《共享预训练医学分割模型下的极低通信联邦适应：项目事实审计、算法前沿与下一轮实验决策》；正文反复出现 `anchor`、`provenance`、`estimand`、`scientific gap`、`method gap`、`residual gap`、`resource contract`、`strict one-shot contract`、`testbed`、`axis`、`comparator`、`correction/stability run` 等表达，并存在“法律意义上证明”“forensic-level exact provenance proof”一类不必要的法律/取证腔。
problem: 面向中文研究者的正式报告虽然事实、算法名、数据和证据边界需要保持不变，但当前成稿仍把大量可直接解释的普通科研概念写成英文抽象标签或代理内部语言，整句按英文科研写作和工作流语法组织。问题不只是“英文太多”：即使逐词翻译，句子仍可能难读。用户要求“说人话”层在不改变任何事实、数字、公式、算法名、数据集名、引用、结论强度和证据边界的前提下，大幅降低阅读难度，用符合中文逻辑、直白且具体的语言重新讲清同一内容。当前 `chinese-prose` 已有中文优先、非必要英文清理、报告终审等规则，因此该真实失败还需要检查这些规则是否足以覆盖科研抽象名词、整句重述和 Deep Research/最终报告消费路径，不能只新增同义禁词表。
project-specific context: PDF 的具体研究对象是 one-shot federated medical segmentation、CARE、M&Ms、FedFisher/FedLPA 等；这些算法、数据集、公式和研究判断属于项目内容，不应被写成通用风格规则。可复用问题仅限于中文科研报告的可读性、英文抽象标签、代理式元话语、整句中文化和保真改写。

## Do not do

- Do not create detector-evasion or generic humanizer behavior.
- Do not let style rewriting change equations, claims, labels, versions or citation meaning.
