# Bobbio

> **From discovery to enduring knowledge.**

Bobbio 是一个面向科研人员的 **local-first、human-in-the-loop research knowledge workbench**，用于把科研过程中分散的工作连接成一条连续、可审核、可追溯的知识链。

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

Bobbio 的目标不是让 AI 替研究者“读完并总结论文”，而是让 AI 接管低价值的机械工作，同时保留最重要的人类判断：什么值得读、什么值得留下、如何理解、如何组织，以及哪些知识可以进入后续研究。

## 为什么叫 Bobbio

Bobbio 得名于意大利北部的 Bobbio Abbey。它历史上的 scriptorium 与 library 长期承担文本的收集、抄录、整理与保存。

这个名字对应 Bobbio 想解决的核心问题：知识不应该停留在一次阅读或一次对话里，而应该经过理解、筛选和整理，成为以后仍然可信、可找到、可复用的研究资产。

这里的历史意象只是品牌来源，不意味着产品会采用宗教或历史主题的功能设计。

## Bobbio 解决什么问题

今天的科研工具通常分别解决某一小段工作：

- Semantic Scholar / PubMed / arXiv 帮助发现论文；
- Zotero 管理文献、PDF 与 annotation；
- AI PDF tools 帮助解释或总结论文；
- Notion 等工具保存人的笔记；
- Codex / Claude Code 等 agent 帮助写代码和写作。

真正困难的是这些环节之间的知识不断丢失：

- 读到不懂的 term，需要离开当前上下文重新搜索；
- annotation 被困在单篇 PDF 里；
- AI 给出的解释很有用，但很快消失在 chat history 中；
- 把 Zotero 内容搬到 Notion 需要大量复制、重排、公式和图片处理；
- Notion 中已经整理好的知识，coding/writing agent 又很难稳定复用；
- 直接让 AI 自动总结，则容易把研究者自己的判断一起外包掉。

Bobbio 要处理的不是其中某一个点，而是这条完整的知识供应链。

## 核心模块

### Bobbio Radar

订阅 keyword、author、topic、venue、seed paper 等研究方向，通过 OpenAlex、Semantic Scholar、PubMed、arXiv 等来源发现更新。

新论文进入统一 Paper Inbox。用户阅读 title / abstract / relevance explanation 后，再决定是否加入 Zotero。

AI 可以回答“为什么这篇可能值得读”，但不替用户做最终筛选。

### Bobbio Reader
