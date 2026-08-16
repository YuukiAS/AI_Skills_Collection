# 001 Research Writing — Planner Review

reviewed_commit: `ed5508ab6e20be905f9c89de2f928b135f8dc5ed`
current_main_control_commit: `ca005976b523c7cc07aceb557f12b731be1af338`
review_round: 2
decision: PASS
next_task_key: `002_writing_style`

## 结论

001 已达到冻结计划要求，可以进入 002。上一轮唯一阻断问题已经被精确修复：`citation-management` 现在只负责已知论文或已知标识符的书目记录定位、元数据补全、BibTeX 与参考文献整理，不再把按主题发现论文、寻找最新论文或扩展候选集合当作自身正常职责。

这次返修没有扩大范围，也没有破坏上一轮已经通过的论文写作、审稿、量化评价、综述、即时检索和引用核验边界。当前 Marketplace 仍保持 10 个插件与 `marketplacePluginBudget=10`。

## 上一轮 Blocker 的关闭证据

### 1. `citation-management` 已收窄为已知记录处理

当前 source 明确把适用场景限定为：

- exact title / author-year；
- DOI / PMID / arXiv ID / URL；
- 用户或上游流程已经给出的 candidate list；
- 在这些已知记录基础上做 metadata acquisition、BibTeX、去重和 bibliography hygiene。

原来的 `Paper Discovery and Search` 已改为 `Bibliography Record Resolution`。Google Scholar / PubMed 示例也从主题级检索改为 exact-title、author/year 或 identifier-backed record lookup。

### 2. 主题级论文发现已明确交给 `research-lookup`

当前正文明确规定以下请求不得由 `citation-management` 主处理：

- 按主题找论文；
- 找最近论文；
- 发现新的候选来源；
- 扩展 bibliography candidate set；
- 扫描当前证据；
- “what should I cite for X”。

这些任务统一路由到 `research-lookup`，待候选记录或标识符确定后，再回到 `citation-management` 做技术性的参考文献整理。

### 3. 生成层已经同步

`plugins/codex/plugins/research-writing/skills/litcite/_src/cite/source.md` 已包含同样的 `Bibliography Record Resolution` 和 `research-lookup` handoff，没有出现 source 修改而 generated snapshot 仍保留旧论文发现流程的情况。

### 4. 回归测试覆盖了正负边界

`tests/test_research_writing_routing.py` 当前同时检查：

- `known papers or identifier-backed records`；
- `bibliography record resolution`；
- `exact-record lookup`；
- `find papers by topic` 必须指向 `research-lookup`；
- 旧的 `paper discovery and search`、`searching for specific papers on Google Scholar or PubMed`、`search for papers on your topic` 等宽泛入口不得重新出现。

这比只检查几个新关键词存在更能防止原 blocker 回归。

## 自然语言验收

当前边界可以清楚处理以下相邻请求：

- “现在帮我找几篇 2025–2026 年关于 X 的最新论文。” → `research-lookup`，负责论文发现和当前证据检索。
- “把这几个 DOI / PMID 和已知论文整理成规范 BibTeX，补全元数据并去重。” → `citation-management`，负责技术性的书目整理。
- “这个 DOI 是否真实，而且这篇文章真的支持正文这句话吗？” → `citation-verification`，负责存在性、元数据一致性和 claim-support verdict。
- “围绕 X 做相关工作梳理，并按方法路线和研究空白组织。” → `literature-review`，负责综述和证据综合。

因此，上一轮“同一个自然请求仍有两条都合理的论文发现入口”的问题已经关闭。

## 其他已通过边界保持不变

本轮复查没有发现新的阻断问题：

- `scientific-writing` 继续负责论文正文起草与修改；
- `paper-workflow-orchestrator` 继续负责整篇论文结构、主张—证据骨架和流程协调；
- `peer-review` 与 `scholar-evaluation` 继续分别负责 reviewer-style critique / acceptance risk 与固定 rubric / quantitative scoring；
- `literature-review`、`research-lookup`、`citation-verification`、`citation-management` 的职责现在可由正常用户表达区分；
- `research-writing` 用户可见入口仍保持 `research-reporting`、`research-paper-workflow`、`literature-and-citations` 三项；
- 十插件 Marketplace 没有回退。

## 验证与远端状态

Executor 报告的完整本地验证链均通过，包括 149 active skills 校验、全库 audit、marketplace build、provenance/icon checks、99 个单元测试以及 `git diff --check`。

Planner 独立核对了真实 GitHub Actions：

- 实现提交 `ed5508ab6e20be905f9c89de2f928b135f8dc5ed` 的 `Codex Marketplace` workflow：`completed / success`；
- 当前结果提交 `ca005976b523c7cc07aceb557f12b731be1af338` 的同一 workflow：`completed / success`。

没有 CI 等待项需要继续阻断 001。

## 下一步

001 结束。Codex 可以开始 `002_writing_style`，严格读取：

`automation/reviewed_handoff/tasks/002_writing_style/PLAN.md`

002 只处理现有 `writing-style` 的保真、中文自然表达和英文科研成稿边界，不借机重新打开 001 或扩展新的外部能力。
