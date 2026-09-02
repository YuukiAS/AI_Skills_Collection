# Bobbio

> **From discovery to enduring knowledge.**

Bobbio 面向科研人员，核心目标是把论文发现、阅读、整理和后续写作连接起来。它采用 **local-first** 的使用方式，把关键判断留给研究者本人，同时让 AI 处理重复的检索、搬运、整理和解释工作。换句话说，Bobbio 不是替研究者读论文，而是帮助研究者把一次阅读中形成的判断沉淀成以后还能找到、还能复用的研究知识。

这条知识链从论文发现开始，经过收件箱筛选、Zotero 文献管理、带 AI 辅助的交互式阅读、人工整理、Notion 笔记，再进入项目仓库或 `wiki/`，最后供 GPT、Codex 和其他 Research Agents 在后续研究中调用：

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

Bobbio 保留 human-in-the-loop 的原因很直接：科研里最重要的不是把所有论文都自动总结一遍，而是判断什么值得读、哪些内容应该留下、这些内容应当怎样理解和组织，以及哪些知识已经可靠到可以进入后续研究。

## 名字从哪里来

Bobbio 的名字来自意大利北部的 Bobbio Abbey。历史上，Bobbio Abbey 的 scriptorium 和 library 长期承担文本收集、抄录、整理与保存的工作。

这个来源对应的是产品想解决的问题：科研知识不应停在一次 PDF 阅读或一次 chat history 里。它需要经过理解、筛选和整理，变成可信、可查、可复用的研究资产。

这里的历史意象只解释品牌来源，不代表产品会采用宗教或历史主题的功能设计。

## Bobbio 想解决的问题

现有科研工具往往各自处理一段流程。Semantic Scholar、PubMed 和 arXiv 更擅长发现论文；Zotero 管理文献、PDF 和 annotation；AI PDF tools 可以解释或总结论文；Notion 保存研究者自己的笔记；Codex、Claude Code 等 agent 则更多参与代码和写作。

问题出在这些环节之间。研究者读到不懂的 term 时，常常要离开当前上下文重新搜索；annotation 往往留在单篇 PDF 内部；AI 解释也可能很有用，但很快被埋在 chat history 里；把 Zotero 里的内容搬到 Notion，又会消耗大量复制、重排、公式和图片处理时间；而 Notion 中已经整理好的知识，也很难被 coding/writing agent 稳定复用。

如果直接把总结交给 AI，另一个问题会出现：研究者自己的判断也被一起外包。Bobbio 要处理的不是某个单点工具缺口，而是让整条研究知识供应链少丢信息、少重复劳动，并且仍由研究者掌握最终判断。

## 核心模块

### Bobbio Radar

Bobbio Radar 订阅 keyword、author、topic、venue 和 seed paper 等研究方向，并通过 OpenAlex、Semantic Scholar、PubMed、arXiv 等来源发现新论文。

新论文先进入统一的 Paper Inbox。用户阅读 title、abstract 和 relevance explanation 后，再决定是否加入 Zotero。AI 可以解释“为什么这篇论文可能值得读”，但不替用户做最终筛选。

### Bobbio Reader
