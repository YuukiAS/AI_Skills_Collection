# 053 Fresh Holdout H1 Rewrite Task

请把随附的 Karatsuba 算法 raw wiki 技术条目整理成自然、连贯、读者能直接理解的简体中文说明。

要求：

- 保留算法名称、提出年份、作者归因、复杂度、递归关系、示例数量级、与普通乘法/Toom-Cook/Schönhage-Strassen 的比较边界。
- `<math>...</math>`、wiki 模板、`[[...]]`、`<ref>...</ref>`、外部链接模板等源平台语法不得出现在读者正文中；其公式、引用和归因含义要保留。
- 公式必须使用可渲染的 Markdown/LaTeX 数学表达；不要把公式写成 fenced `text` code block。
- 代码或伪代码只在有助于说明算法时保留；若保留，必须简短、可读，并解释它在递归分解中的作用。
- 普通正文用简体中文；必要英文专名、算法名、作者名和引用身份可以保留。
- 不要写成“根据给定材料”“原文指出”这类改写说明，也不要输出 workflow、candidate、commit、hash、Reviewer、Executor 等过程信息。
- 不新增来源不支持的解释，不改变结论强度。

请写入：

```text
outputs/h1_karatsuba.md
```
