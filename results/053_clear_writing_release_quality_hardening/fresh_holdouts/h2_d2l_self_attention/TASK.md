# 053 Fresh Holdout H2 Rewrite Task

请把随附的《动手学深度学习》自注意力和位置编码章节整理成能直接给中文技术读者阅读的简体中文成稿。

要求：

- 保留自注意力定义、CNN/RNN/自注意力比较、计算复杂度、顺序操作、最大路径长度、位置编码公式、相对位置信息解释、小结和练习范围。
- Sphinx/Markdown 标签、`:cite:`、`:label:`、`:numref:`、`:eqref:`、notebook tab 标记、图片路径、训练代码 scaffolding 等源格式标记不得出现在读者正文中；其引用、公式和说明含义要保留。
- 公式必须使用可渲染的 Markdown/LaTeX 数学表达；不要把公式写成 fenced `text` code block。
- 源中的多段代码可以改写成简短的实现说明；只有确实帮助读者理解时才保留代码块，并避免让代码块主导正文。
- 普通正文用简体中文；必要英文术语如 CNN、RNN、self-attention、positional encoding、PyTorch 可保留。
- 开头直接说明主题和结论，不要写成“根据给定材料”的改写说明。
- 不新增来源不支持的解释，不改变结论强度。

请写入：

```text
outputs/h2_d2l_self_attention.md
```
