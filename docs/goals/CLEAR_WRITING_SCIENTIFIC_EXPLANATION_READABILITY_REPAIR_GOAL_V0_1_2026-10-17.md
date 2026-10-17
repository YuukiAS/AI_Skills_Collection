# Goal — Clear Writing 普通科研解释可读性最小修复 v0.1

Status: DRAFT_FOR_CRITIC_REVIEW  
Task: `clear-writing--scientific-explanation-readability-repair`

继续现有 Clear Writing，不重做架构。

只修第二轮独立 Reviewer 已确认的两个通用缺口：

1. 普通复杂科研解释按完整语义/推理单元组织自然段，避免一句一段、过密标题和无价值公式碎片化；
2. 陌生方法、术语和多重下标对象首次出现时，先建立不越权的 reader mental model，再进入正式术语/公式；上游信息不足时明确缺定义，不得猜科学含义。

必须使用：
`results/clear-writing--scientific-explanation-readability-repair/REAL_WEB_KNOWN_REGRESSION_BANK_V2.md`

该 bank 冻结全部 9 组已记录真实 Web 正反例的可迁移特征，不复制私人原文。全部 9 组都要进入最终回归；它们全部是 known evidence，不得作为 G7 fresh。

执行要求：

- 复用上一任务的当前 `response-clarity` 候选和成果；
- merge latest main 后再实现，确保 2026-10-16/17 feedback 被消费；
- 修改 source 前，只为新增 KR-WEB-06..09 建 public-safe 泛化 fixtures 并跑 baseline；
- production change 只允许落在 `response-clarity` 与直接相关 eval/tests/generated mirror；
- 不修改其他 writing skills 的 production semantics；
- 不修改 Research Authoring / Presentations；
- 不新增 skill/router/model/API；
- 不使用固定字数/段落/标题/英文比例/公式数量/关键词 grep 做质量 oracle；
- 修复后完整跑 KR-WEB-01..09、四组 should-not-change、focused tests、full tests、Marketplace generator/check、required GitHub CI；
- CI PASS 后交独立 Reviewer，Reviewer 必须实际读 9 组最终输出。

成功只表示 known-regression successor candidate 可以进入后续真实 ChatGPT Web 验收；不代表 A/E、B/C、G7、PIE 0.2 或正式 release 已完成。
