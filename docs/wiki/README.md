# Research Wiki

`docs/wiki/` 是项目内可长期复用的研究知识层。它用于沉淀论文摘要、报告摘要、概念页、方法对比、研究空白和讨论结论。

它不是 Codex 默认任务入口。需要 Codex 执行时，先把 wiki 中的方向提炼成 `prompts/tasks/<task_key>.md`。

## 目录

- `index.md`：所有 wiki 页面目录和一句话摘要。
- `log.md`：append-only 操作日志。
- `papers/`：单篇论文或报告的结构化摘要。
- `concepts/`：方法、理论、概念页面。
- `entities/`：作者组、数据集、系统、benchmark。
- `comparisons/`：跨方法、跨论文对比。
- `gaps/`：研究空白、假设、开放问题。
- `synthesis/`：领域综合理解、多轮讨论结论。

## 原始材料

原始论文 PDF、OCR 文本、报告和实验记录可以保存在项目已有位置。wiki 页面必须在 frontmatter 的 `source` 字段中引用原始材料路径。

## 使用规则

- ChatGPT/GitHub MCP 写 wiki 前应先读 `prompts/CHATGPT_RULES.md`。
- Codex 只在 task 显式引用时读取 wiki 页面。
- 不要把 wiki 页面直接当 task 执行。
- 不确定结论必须标注 `confidence: low` 或在正文说明。
