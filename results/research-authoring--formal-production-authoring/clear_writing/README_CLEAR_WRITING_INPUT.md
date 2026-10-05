# README Excerpt For Clear Writing

Current repository release shown elsewhere in README: `5.4.4`

Research Authoring plugin table row:

```markdown
| <img src="./assets/codex/plugin-icons/research-writing/composer.svg" width="40" alt="Research Authoring 图标"> | <strong>Research Authoring</strong><br><code>research-writing</code> · v`0.3`<br>通过共享文档核心组织研究报告、论文、文献综述、引用证据和增量修订；正式 PDF 仍交给配套渲染器处理。 |
```

Nearby reader-facing context:

```markdown
如果要从研究报告生成正式 PDF，优先安装 [research-main](profiles/research-main.json) profile。它同时包含 Research Authoring 和 `render-chinese-math-pdf`，可以先整理研究内容，再用 Pandoc/XeLaTeX 渲染中文、英文和数学公式。

单独安装 Marketplace 里的 Research Authoring 插件时，它只负责研究文档的内容和结构，不会假装自带 PDF 渲染器。遇到正式 PDF 请求而缺少 `render-chinese-math-pdf` 时，应先安装这个配套技能，而不是静默改用浏览器导出。
```
