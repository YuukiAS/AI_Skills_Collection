# Bobbio

> **From discovery to enduring knowledge.**

Bobbio 是给科研人员使用的 **local-first、human-in-the-loop research knowledge workbench**。它要做的不是把某一步工具做得更花哨，而是把科研知识从发现、阅读、整理到后续复用的过程连起来，让每一步都能被人检查、追溯，并在以后继续使用。

这条链路大致是：

```text
Literature Radar
      ↓
Paper Inbox
      ↓
Zotero
      ↓
Interactive Reading + Agent Assistance
      ↓
Human Curation
      ↓
Notion
      ↓
Selective Project Publishing
      ↓
Project Repository / wiki/
      ↓
GPT / Codex / Research Agents
```

Bobbio 不希望 AI 替研究者“读完并总结论文”。它更适合接管低价值、重复性的搬运和整理工作，把真正需要人判断的部分留给研究者：哪篇论文值得读，哪些内容值得留下，应该如何理解和组织，以及哪些知识可以进入后续研究。

## 为什么叫 Bobbio

Bobbio 这个名字来自意大利北部的 Bobbio Abbey。它历史上的 scriptorium 和 library 长期负责文本的收集、抄录、整理与保存。

这个来源对应了产品要解决的问题：知识不应只停留在一次阅读或一次对话里。研究者理解、筛选并整理过的内容，应该变成以后仍然可信、找得到、能复用的研究资产。

这里的历史意象只说明品牌来源，并不表示产品功能会采用宗教或历史主题。

## Bobbio 解决什么问题

现在的科研工具大多只处理工作流中的一小段：

- Semantic Scholar / PubMed / arXiv 帮助发现论文；
- Zotero 管理文献、PDF 和 annotation；
- AI PDF tools 帮助解释或总结论文；
- Notion 等工具保存人的笔记；
- Codex / Claude Code 等 agent 帮助写代码和写作。

真正的损耗发生在这些工具之间。研究者读到不懂的 term 时，常常要离开当前上下文重新搜索；annotation 留在单篇 PDF 里，很难进入后续知识库；AI 给出的解释可能有用，但很快埋在 chat history 中；把 Zotero 内容搬到 Notion 又需要大量复制、重排，并处理公式和图片；已经在 Notion 中整理好的知识，coding/writing agent 也很难稳定复用。反过来，如果直接让 AI 自动总结，又容易把研究者自己的判断一起外包掉。

Bobbio 要处理的是这条完整的知识供应链，而不是其中某一个单点工具。

## 核心模块

### Bobbio Radar

Bobbio Radar 根据 keyword、author、topic、venue、seed paper 等研究方向，使用 OpenAlex、Semantic Scholar、PubMed、arXiv 等来源发现更新。

新论文先进入统一的 Paper Inbox。用户阅读 title / abstract / relevance explanation 后，再决定是否加入 Zotero。AI 可以解释“为什么这篇可能值得读”，但最终筛选仍由用户完成。

### Bobbio Reader
