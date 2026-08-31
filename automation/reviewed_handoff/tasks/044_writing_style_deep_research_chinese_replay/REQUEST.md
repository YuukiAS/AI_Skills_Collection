# Reviewed Handoff Request — 044_writing_style_deep_research_chinese_replay

## Objective

用一份真实的 ChatGPT Deep Research 中文长报告作为压力测试，验证并按需完善现有 `writing-style` plugin，重点是 `chinese-prose` 的“说人话”能力：在不改变研究内容、事实、数字、公式、算法/数据集名称、引用、结论强度和证据边界的前提下，大幅降低阅读难度，用符合中文逻辑、直接、具体的语言重新讲清同一内容。

本轮必须先跑当前 production plugin 的 baseline。只有 baseline 真实不够好时才修改 skill/plugin；如果当前实现已经能把材料改好，不为了制造 diff 强行修改。

## User-provided inputs

- 真实输入：2026-08-31 由 ChatGPT Deep Research 直接生成的 22 页中文 PDF《共享预训练医学分割模型下的极低通信联邦适应：项目事实审计、算法前沿与下一轮实验决策》。
- 重要澄清：该 PDF **没有经过 `writing-style` plugin**，因此它目前是 replay/stress input，不是 `writing-style` 已知 production failure。
- 用户反馈：原报告大量使用 `anchor`、`provenance`、`estimand`、`scientific gap`、`residual gap`、`resource contract` 等可直接解释的英文抽象标签，整句也经常按英文科研代理/工作流语法组织，阅读负担很高。
- 完整 PDF 不应默认提交到公开仓库。Executor 使用用户在本机提供的外部路径读取，原文件和完整重写稿默认保持 repo-untracked；仓库只保存必要的通用规则、测试、非泄露型评审摘要和 Reviewed Handoff 状态。

## User constraints

- `writing-style` 已经是现有顶级 plugin；不要创建新的“说人话”plugin。
- `chinese-prose` 继续作为中文“说人话”具体 skill；`writing-fidelity` 负责保护事实，但不能把“保真”误解为必须保留原句语序或所有段落结构。
- “不改内容”指不改变语义、事实、证据、结论边界和受保护内容；允许为了可读性重写句法、拆并句子、调整段落内部的解释顺序。
- 不通过项目专用禁词表、逐词替换或针对这份 PDF 的 hard-code 来通过验收。
- 不新增事实、类比、例子、因果解释或研究判断来换取“生动”；直白具体来自更好的中文解释，不来自编造内容。
- 算法名、数据集名、公式、变量、指标、路径、代码、论文标题等需要精确定位的内容继续保留。
- 该 PDF 是已知 replay，不能在迭代后被当成 unseen/generalization 证据。
- 用户最终需要看到一份可实际阅读的完整重写结果，并亲自判断是否真的“能看懂”；测试绿灯不能替代真实阅读验收。
- 后续若 ChatGPT 产品支持该 GitHub Marketplace plugin 在 ChatGPT 中安装，可再单独验证 ChatGPT/Deep Research 使用路径；本轮不要为了未来分发改变当前 skill/plugin 边界。
