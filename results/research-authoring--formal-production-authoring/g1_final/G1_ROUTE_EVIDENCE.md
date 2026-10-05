# G1 候选运行时路由证据

## 运行身份与证据边界

- 冻结输入：`inputs/01-G1_CASES.md`（内容标题为 `G1 Frozen Routing Cases`）。
- 输入声明的最终候选提交：`1c37c0715aca0096606f24e56192b7857e72bbd6`。
- 本会话可见且实际使用的安装：`ai-skills-candidate/research-writing/0.3`；安装清单中的名称为 `research-writing`，版本为 `0.3`，显示名称为 `Research Authoring`。
- 安装根目录：`/users/a/e/aereinh/.codex/plugins/cache/ai-skills-candidate/research-writing/0.3`。
- 当前安装清单未包含候选提交字段，因此不能仅凭版本和路径独立证明安装内容与上述提交完全一致。精确提交绑定仍需外围 replay 的 provenance 证据。

本次通过会话暴露的正常 skill 入口执行路由判断：先使用 `research-writing:research-reporting`，按其 coordinator-first 工作流读取 `skills/report/_src/core/source.md`；再读取 `research-writing:research-paper-workflow` 和 `research-writing:literature-and-citations` 的入口，以及已选中的 report、paper、literature 家族 delegate 边界。本表是当前候选会话对全部冻结请求的实际分类与处理决定，不是依据描述关键词、安装成功或测试结果推定路由成功。

本轮只执行路由。表内箭头表示若执行该请求应采用的归属链，不表示已生成对应内容，也不表示已调用外部支持工具。没有执行论文检索、引用核查、改写、排版或文档生产。

## 全部冻结案例的路由决定

下表中 `core` 指 `research-authoring-core`。`support_only` 表示该请求只需辅助能力，Research Authoring 不拥有其主产出；`out_of_scope` 表示主任务由其他领域或普通问答负责。

| 案例 | 冻结请求 | 分类 | 正常入口或控制边界 | 判断理由 |
|---|---|---|---|---|
| P1 Methods section | Please turn these experiment notes into a Methods section for the manuscript. | `document_production_primary` | `research-paper-workflow` → core → `paper-workflow-orchestrator` / `scientific-writing`；core 的 Trigger Boundary 与 Family Routing | 请求把实验笔记组织成论文 Methods 章节，属于新的学术章节生产。先由 core 固定来源、方法表述与章节职责，再交论文家族处理，不能降为段落润色。 |
| P2 Research update | 把这几天研究整理成给老师看的报告。 | `document_production_primary` | `research-reporting` → core → `research-reporting`；core 的报告家族路由及 report 的 Boundary | 明确要求面向老师的研究报告。Research Authoring 负责读者、科学问题、证据和报告结构；中文和口语化请求不改变文档生产归属。 |
| P3 Related work | Write a related-work section from these paper notes. | `document_production_primary` | `literature-and-citations` → core → `literature-review`；core 的 literature-document 路由与 lit 的 Overview | 交付物是 related-work 章节，需要跨论文组织论点与证据，已经超出文献查找或元数据支持。使用已给笔记作为来源，不凭空补充文献。 |
| P4 Incremental report update | Update this existing research report using the new evidence without rewriting unrelated sections. | `document_production_primary` | `research-reporting` → core → `research-reporting`；core 的 Incremental Authoring Contract | 新证据改变既有研究报告，仍属于文档生产。以现有报告为权威，仅修改受影响的主张、章节及依赖的图表和引用，保留无关内容。 |
| N1 Citation verify | Check whether these citation keys and DOIs are plausible and flag missing metadata only. | `support_only` | `literature-and-citations` → `citation-verification` / `citation-management`；core 的 support-only citation/metadata 边界 | 请求限于标识符与元数据检查，没有要求写文档或重建论证。不强制建立文档计划，也不扩大为全文引用支持审计。 |
| N2 Paper lookup | Find recent papers about federated cardiac MRI segmentation and summarize why they might be relevant. | `support_only` | `literature-and-citations` → `research-lookup`；core 的 recent-paper discovery 边界与 lit 的 fast-lookup 排除项 | 找近期论文并说明相关性是定向发现支持；简短相关性摘要本身不构成正式 related-work 或综述文档生产。 |
| N3 Local prose polish | Polish this single paragraph for clarity without changing the document structure or adding evidence. | `support_only` | Clear Writing / 局部 prose 支持；core 的 content-preserving local prose polishing 与 Writing And Owner Boundaries | 语义、证据和结构均已冻结，只改一个段落的表达，不进入文档级生产规划。 |
| N4 README/email | Rewrite this README announcement email to sound clearer for users. | `out_of_scope` | 通用 Clear Writing；core 的 scholarly-document 归属及 generic style cleanup 排除边界 | 用户公告邮件或 README 面向用户的表达改写，不是研究文档。文件名和 rewrite 动词不能使其成为 Research Authoring 主任务。 |
| N5 PPT/Beamer | Turn these notes into a 6-slide Beamer deck. | `out_of_scope` | Presentations；core 的 Family Routing 和 slide/deck/Beamer 排除边界 | 交付物为六页演示文稿，主叙事与版式归 Presentations。Beamer 使用 LaTeX 不意味着它属于论文生产。 |
| N6 Render-only | Render this already-final Markdown report to PDF without changing the text. | `support_only` | renderer / `render-chinese-math-pdf` 等文档渲染能力；core 的 render-only 排除边界 | 内容已定稿且禁止改文，所需工作只有输出格式转换。Research Authoring 不接管研究语义或重新生产报告。 |
| N7 Ordinary Q&A | What is the difference between a systematic review and a narrative review? | `out_of_scope` | 普通研究问答；core 的 ordinary research Q&A 排除边界 | 请求解释两个概念的区别，没有要求撰写综述或其他学术文档。术语涉及 review 不足以触发文档生产。 |

## 归属依据

以下路径均相对于上述实际安装根目录：

- `skills/report/SKILL.md`：报告入口要求先进入 coordinator。
- `skills/report/_src/core/source.md`：Trigger Boundary、Family Routing、Incremental Authoring Contract、Writing And Owner Boundaries，控制全部案例的文档生产与支持边界。
- `skills/report/_src/report/source.md`：报告家族与面向导师的报告归属。
- `skills/paper/SKILL.md`、`skills/paper/_src/flow/source.md`：论文家族先进入 core，再处理章节规划与写作。
- `skills/litcite/SKILL.md`、`skills/litcite/_src/lit/source.md`：related-work 文档生产进入 core；快速查找、引用与元数据任务保留支持路由。

## 本轮结果

实际路由结果：四个正例全部为 `document_production_primary`；七个近似案例中四个为 `support_only`，三个为 `out_of_scope`，没有一个被接管为 Research Authoring 主产出。11/11 案例均已给出明确决策。

行为分类满足 G1 的路由要求。精确最终候选提交的身份绑定未由本会话可见安装清单独立验证，因此本文件不单独宣称整个 exact-candidate G1 gate 已无条件 PASS。未生成任何案例要求的报告、论文、PDF、引用、幻灯片或改写文本。
