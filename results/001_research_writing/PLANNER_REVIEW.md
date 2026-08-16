# 001 Research Writing — Planner Review

reviewed_commit: `6354ea48753368b2c5c4738d005abcee34c65491`
current_main_control_commit: `f05721d1db7bd886d14c7fedd5f3f478ae91e34f`
decision: REVISE

## 结论

这一轮已经把大部分核心边界整理正确：论文正文、整篇论文流程、审稿式风险检查、量化评分，以及综述、即时检索、引用核验、BibTeX/Zotero 的上游入口已经明显比基线清楚；十插件 Marketplace 也没有被再次删回六个。实现提交与当前控制提交对应的 `Codex Marketplace` GitHub Actions 都已成功。

目前只保留 1 个阻断问题。它属于 001 冻结计划本身要求解决的调用边界，不是额外扩展。

## Blocker 1 — `citation-management` 仍保留通用论文发现职责

### 冻结依据

001 的冻结计划明确规定：

- `citation-management` 应收窄为 bibliography / BibTeX / metadata / reference-library hygiene；
- 一般论文发现、尤其“找论文 / 查最近论文”应交给 `research-lookup`；
- 本阶段应通过 description、When-to-Use、Hand Off / Routing 等位置把边界写清，而不是只改聚合入口的一句话。

### 真实证据

当前 `citation-management` 的 frontmatter 已经改得比较清楚，但正文仍把下面内容列为自身正常职责：

- `When to Use` 中仍有 “Searching for specific papers on Google Scholar or PubMed”；
- `Core Workflow` 的第一阶段仍是 `Paper Discovery and Search`；
- 该阶段继续提供按主题搜索 Google Scholar / PubMed 的完整工作流和示例。

这与同轮 `research-lookup` 的“current research information and recent papers / paper discovery”边界形成实质重叠。对于“帮我搜几篇某主题的论文并整理进参考文献”这类自然请求，当前 skill 正文仍给出两条都合理的入口，未完全达到冻结计划要求。

### 最小修复

只修 `citation-management` 的这一条边界，不重做整个文献系统：

1. 将 `When to Use` 中的通用论文搜索改成“已知论文、已知标题或 identifier-backed record 的定位/元数据补全，用于 bibliography 构建”；
2. 将 `Phase 1: Paper Discovery and Search` 收窄或改名为 bibliography record resolution / metadata acquisition，避免继续把主题级 Google Scholar / PubMed discovery 写成该 skill 的主工作流；
3. 明确写出：按主题找新论文、找最近论文、扩展候选文献集合 → `research-lookup`；
4. 保留 DOI / PMID / arXiv → BibTeX、元数据提取、去重、格式化、bibliography hygiene 等现有能力；
5. 重新生成 `research-writing` 的 `litcite` source snapshot，并保持十插件 Marketplace 不变。

如增加回归测试，测试应覆盖这个负边界，而不只是检查几个关键词存在。

### 修复后验收

Planner 下一轮需要看到：

- 用户说“找几篇最近关于 X 的论文”时，`research-lookup` 是唯一自然的论文发现入口；
- 用户说“把这几个 DOI/PMID/已知论文整理成规范 BibTeX，补元数据并去重”时，`citation-management` 是自然入口；
- `citation-verification` 仍独占“这个引用是否真实 / 是否支持这句话”的最终核验职责；
- `literature-review` 仍负责综述与单篇深读；
- source 与生成后的 `literature-and-citations` snapshot 一致；
- 完整测试与 GitHub Actions 继续通过。

## 已通过的部分

以下部分本轮没有发现阻断问题：

- `scientific-writing` 已明确成为论文正文起草/修改能力，并把整篇规划、审稿风险、检索、引用核验、BibTeX、图像、venue 和 LaTeX 路由给邻接能力；
- `paper-workflow-orchestrator` 保持整篇论文结构、主张—证据骨架和流程协调职责；
- `peer-review` 与 `scholar-evaluation` 已分别收敛为 reviewer-style critique / acceptance risk 与固定 rubric / quantitative scoring；
- `research-paper-workflow` 仍是单一用户可见聚合入口，并已包含 `scholar-evaluation` 作为内部 source workflow；
- `literature-review`、`research-lookup`、`citation-verification` 的主要边界已经清楚；
- `research-writing` 仍只有 `research-reporting`、`research-paper-workflow`、`literature-and-citations` 三个用户可见能力；
- Marketplace 保持十插件、`marketplacePluginBudget=10`；
- 实现提交 `6354ea4` 与当前控制提交 `f05721d` 的远端 `Codex Marketplace` workflow 均为 `completed / success`。

修复以上单一 blocker 后重新提交 `RESULT.md`，再进行 001 第二次 Planner 复核。不要提前进入 002。
