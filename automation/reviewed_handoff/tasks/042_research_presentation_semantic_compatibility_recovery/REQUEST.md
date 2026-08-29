# Request — 042_research_presentation_semantic_compatibility_recovery

## Objective

在 041 frozen four-paper batch 真实失败后，建立一个**独立于失败 holdout 内容**的 bounded generic recovery，修复当前 presentation production path 中同一类通用语义兼容性断层：成熟构图选择器与 bounded quality-loop repair mapper 都直接依赖过于具体/自由文本化的 scientific-object label，导致本来属于系统已支持科学页面类型的输入在 selector 阶段无匹配，或在 visual finding 已经清楚时仍无法安全映射到已有 repair family。

本 task 不是重新修 041 的 TMB、DESeq2、cardiac-ultrasound 或 RETFound，也不允许用这四篇的正文、图像、标题、DOI、page-specific rendered content 作为 fixture。目标是在完全独立的 non-holdout / synthetic / public-safe regression 上，引入最小、通用、可验证的 scientific-object semantic compatibility mechanism，并证明它能让已有成熟 gold 与已有 bounded repair vocabulary 对等价科学对象标签保持稳定，同时继续对真正未知/不兼容输入 fail closed。

041 的全部失败历史必须原样保留。042 PASS 也不构成 Stage 5 PASS；根据 Program Goal，042 若完成 generic recovery，在冻结下一组 fresh four-paper holdout 之前仍必须进入用户人工门，报告上一批失败原因、通用机制修复和新增证据，由用户决定是否继续消耗下一批。

## User-provided inputs

- 041 Round 1 / Round 2 review、FINAL_REPORT、真实 production failure logs、quality-loop state 与 task-local Terra evidence仅作为**问题类型和边界证据**，不得把失败论文的具体内容变成 tuning material。
- Stage 2–4 已通过的 mature gold composition、exact CUHK layout、normal production entry 与 single-cycle bounded quality-loop contract继续作为必须保护的现有能力。

## User constraints

- 最高冻结质量门保持不变；不得为了减少 selector no-match 而放宽 mature gold compatibility 或强制从垃圾候选中挑赢家。
- 不新增第二套视觉状态机；继续使用 Bridge Kit task-local Visual Review contract。
- 不得添加 TMB、RETFound、DESeq2、cardiac-ultrasound 的标题、DOI、作者、数据集、page-specific object 名称或其他 holdout-specific关键词作为 selector/repair 特例。
- 不得修改或重新生成 041 holdout artifacts来证明恢复成功。
- task 必须有有限实现范围、真实 CI、真实 render identity变化（若触发 repair）和 fresh item/page-level + contact-sheet Terra evidence。
- 042 完成后不得自动冻结下一批 fresh Stage 5 papers；必须先进入用户 human gate。
