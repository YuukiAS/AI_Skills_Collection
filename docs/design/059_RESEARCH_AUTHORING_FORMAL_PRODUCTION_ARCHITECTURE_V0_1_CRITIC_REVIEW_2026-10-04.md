# 059 Research Authoring 正式科研文档生产架构 v0.1 — Critic 审查

日期：2026-10-04  
角色：独立 Critic  
结果：REVISE  
审查阶段：PRE_IMPLEMENTATION_ARCHITECTURE_REVIEW

## Active Review Context

- target_repo: `YuukiAS/AI_Skills_Collection`
- target_plugin_or_domain: `research-writing / Research Authoring`
- design_topic_or_task_key: `research-authoring--formal-production-authoring`
- human workflow number: `059`
- source_branch_or_ref: `main`
- reviewed source main: `5f920ffb76d033485de2958ce0b9fa6de7904442`
- review object: 用户冻结的 “Research Authoring Formal Production Architecture v0.1”
- proposal_path_and_version: 尚未落库；本轮对象来自用户冻结的 v0.1 设计正文

本轮不是实现审查。未修改 production source，未创建或更新 ChatGPT Plugin，未启动 Executor，未调用 paid API。

## 核心判断

方向基本正确，不需要推倒重来。Research Authoring 应继续作为“科研文档语义与生产组织”的领域所有者，而不是泛化成统计方法设计、普通语言层、演示文稿系统或 PDF 渲染器。正式论文、补充材料、回复审稿人、导师书面报告、科研进展、方法说明、研究演变记录和论文级相关工作可以共享同一个科研文档语义核心；具体文档族仍需要各自的专门路线。

ChatGPT 与 Codex 两个使用表面也不应复制两套产品源。当前 OpenAI 官方能力与本账号现有 personal Plugin 先例都证明：PRIVATE / USER-scope / skills-only wrapper 可行，MCP 不是这类写作工作流的必需条件。采用“一个 canonical source + 两个分发表面”比 Codex-only、新建 Chat 专属 canonical Skill、或把中央 Codex plugin 直接强行兼做所有 ChatGPT 分发职责更合适。

但 v0.1 还不能进入实现。当前有四个真实阻塞项。

## RA1 — “所有正式科研文档必须消费 Research Authoring”目前没有唯一可执行的共享入口合同

对应要求：Research Authoring 被定义为科研文档领域所有者，且自然请求不能绕过它；ChatGPT 与 Codex 必须消费同一个 canonical source。

直接证据：当前 production 仍由 `report` / `paper` / `litcite` 三个聚合入口组成；其下层 `research-reporting`、`paper-workflow-orchestrator`、`scientific-writing`、`literature-review` 等职责不同。特别是 `scientific-writing` 明确只是段落/章节级科学写作能力。若 Chat wrapper 直接组合若干现有 skills，一个 “写 Methods” 或 “整理 related work” 请求可以直接命中下层 skill，而没有证据保证先执行 v0.1 所要求的读者、文档目的、科学叙事、claim/evidence、section job、表图公式职责等文档级决策。

因果风险：normal entry 可能“看起来用了 research-writing 中的某个 skill”，但实际绕过 Research Authoring 的领域核心；ChatGPT 与 Codex 也可能因组合方式不同而形成两套行为。这会让“强制消费”退化成关键词/触发器 PASS。

最小关闭条件：v0.2 必须冻结一个跨两表面共享、且所有“产出科研文档”的入口都不能绕过的 canonical authoring core contract。它可以是一个共享 reference/contract 被现有入口强制读取，也可以是一个同时供 ChatGPT/Codex 使用的 canonical orchestration skill；不得新建 Chat-specific canonical skill。v0.2 同时明确 `report` / `paper` / `litcite` 哪些保留为薄路由、哪些调整或退役，以及纯检索/纯 citation verification 与“产出科研文档”如何分流。

owner: Planner

## RA2 — 缺少正式的增量更新合同

对应要求：生产级科研文档不能每次从头生成；本轮审查对象也明确要求检查 incremental update 与 drift。

直接证据：CAT-TRACE 的真实演变文档之所以可靠，是按统计/软件模块重组，并允许后续修改对应模块而不是在末尾不断追加时间流水账；现有 paper workflow 也强调单一正文源与修订一致性。v0.1 把这条经验写进“真实经验”，但没有把它提升为跨文档族的正式更新语义。

因果风险：对论文、导师报告、研究演变记录进行第二次或第三次修改时，模型可能重写未受影响段落、改变符号、引用、claim strength、表图编号或已经接受的内容。首次生成 Gate 即使通过，也不能证明长期 authoring 可用。

最小关闭条件：v0.2 增加最小增量更新合同：先识别现有 canonical artifact 与本次 evidence/decision delta；默认局部修改受影响 section/job；保护未受影响的已接受文本、记号、claim/evidence 绑定、citation key、figure/table identity；只有用户明确要求或原结构已失效时才允许全文重构。不要为此新增 database、ledger 或 state machine，文档源、git diff 和现有 provenance 足够。

owner: Planner

## RA3 — Capability Gate 目前还是候选能力清单，不是可执行 Gate Matrix

对应要求：`PLUGIN_CAPABILITY_GATE_POLICY.md` 要求正式 plugin 行为调整在实现前有最小但充分的 Gate Matrix，包含 normal entry、完整产物、明确 FAIL、should-not-change、必要人工/独立质评与 same-final-candidate 要求。

直接证据：v0.1 目前列出 routing、fidelity、advisor report、formal manuscript、citation、Clear Writing、handoff、long-document consistency、fresh generalization 等十余个候选方向，但没有合并成实际 Gate，也没有绑定真实输入和完整产物。

因果风险：实现阶段很容易把同一个能力拆成大量同义 Gate，或用 trigger match、测试、render success、文件存在、Plugin upload 等机械证据冒充产品能力；最终也无法证明同一 final candidate 在 normal entry 下同时可用。

最小关闭条件：v0.2 必须给出正式 Gate Matrix。建议压缩为四个不同能力：
1. 自然入口与边界：真实自然请求 + near-miss 负例，证明文档任务进入 Research Authoring，而普通问答、单句润色、README/邮件、演示文稿、render-only 不误触发。
2. 科研文档语义保真与增量修订：至少覆盖一份真实导师/科研更新或研究演变文档，直接检查 reader-first、claim/evidence、pending-result 边界、语言层协同和增量修改不漂移。
3. 正式论文生产包：使用一个真实 manuscript task 检查 manuscript/supplement/bibliography/figures/tables/venue-required statements/reporting checklist 的按需选择、主文与补充材料一致性、引用与公式/表图一致性，并禁止文件爆炸。
4. 跨表面生产与最终产物：同一 final candidate 直接通过 ChatGPT wrapper 与 Codex 正常路径，证明 wrapper 只分发 canonical source、Clear Writing 依赖来自同一 canonical commit、Chat→Codex handoff 不丢文档身份与渲染合同、最终文件真实可读。

fresh/generalization、should-not-change、final-candidate identity 应作为上述 Gate 的证据要求与回归银行，不另建同义 Gate。

owner: Planner

## RA4 — 本轮 promotion 没有符合维护看板规则的顶层 tracking owner

对应要求：`AI_SKILLS_MAINTENANCE_BOARD.md` 要求正式 maintenance 在 first substantive Plan/design 时绑定 top-level tracking Issue、source `tracking: #N`、DOING 当前执行锚点与下一步；不得把 Project 生命周期藏在 TODO 文档中，也不得要求用户手工维护。

直接证据：`docs/plugin-todos/research-writing.md` 中 #20–#29 分散绑定多个已有 Issue，另有若干新条目仍为 `tracking: UNASSIGNED`；这些 Issue 分别描述具体问题，没有一个真实等价于本轮“Research Authoring 正式科研文档生产能力整体 promotion”。

因果风险：若复用 #20 或 #21，会把论文生产、ChatGPT 分发、报告演变、渲染边界等不相干的本轮工作错误塞进窄 Issue；若不建 umbrella，本轮 Proposal/implementation 又没有真实生命周期 owner。

最小关闭条件：Planner 新建一个自然命名的 top-level `maintenance-track` Issue，例如“Research Authoring 正式科研文档生产收口”，Area=`research-writing`，进入 DOING，当前执行锚点指向 v0.2 Proposal，下一步指向 Critic 复审；在 `docs/plugin-todos/research-writing.md` 增加一个对应 promotion 顶层条目并写真实 `tracking: #N`。现有 #20–#29 的独立 backlink 保持不变；真正属于本轮同一 maintenance action 且当前 UNASSIGNED 的条目可以合并绑定 umbrella。不要“一 TODO 一 Gate”，也不要要求用户手工拖 Project。

owner: Planner

## 已接受的关键架构选择

这些不是 blocker，不要求 Planner 推倒重写：

- Research Authoring 负责科研文档的 audience/purpose/scientific story/claim-evidence/section jobs/main-vs-appendix/table-figure-formula scientific role/citation authority/final package selection；不负责新统计方法或实验结论。
- 书面的 advisor/group-meeting report 属于 Research Authoring；PPT/Beamer/slide-deck 导出的 PDF 属于 Presentations。当前 `research-presentations` production skill 已把 group meeting deck 明确归入 Presentations，因此边界可执行。
- Clear Writing 继续是语言层。Research Authoring 可以在分发层组合 canonical `writing-fidelity` + 对应中文/英文 scientific prose support，但不得复制语言规则。与其依赖两个独立 ChatGPT Plugin 每次自动串联，最小 canonical support snapshot 更可靠；版本必须绑定同一 source commit。
- renderer 继续拥有字体、页面、LaTeX/Pandoc/XeLaTeX 与 PDF QA。Chat wrapper 不带 PDF runtime 是合理的；Chat 需要最终 PDF 时交付稳定 source + 有约束的 Codex production handoff。
- PRIVATE / USER-scope / skills-only ChatGPT wrapper 是当前最低复杂度的双表面方案。当前本账号的 Project Thread Handoff 与 Project Instructions Editor wrapper 已证明该分发形态可行；Plugin Creator 的 update 为 overlay 语义并使用 `expected_release_id` 防止并发覆盖。
- 不新增 MCP、connector、database、watcher、state machine。
- 版本目标维持 `research-writing 0.2 -> 0.3`，不升 1.0。

## 论文交付范围核查

现实投稿要求支持 v0.1 的“按 venue/task 选择文件”方向，而不支持固定生成所有 sidecar。ICMJE、Nature Portfolio 与 EQUATOR 都表明：正文之外，实际要求会因期刊和研究类型变化，常见还包括 data/code availability、funding、competing interests、author contributions、ethics/permissions、reporting checklist、cover letter 或 submission forms。

因此 v0.2 不需要继续增加固定文件列表，只需把 `declarations` 明确解释为 venue-required statements/forms 类别，并让 venue/project authority 决定具体集合。Quarto/DOCX/LaTeX 应作为 source/production route，而不是再造一个科研语义核心。

## 外部核查

实际核查了：
- OpenAI Help / Developers：Skills in ChatGPT；Plugins in ChatGPT and Codex；Package your plugin；Plugin architecture。
- ICMJE 2026 Recommendations：manuscript preparation 与 submission。
- EQUATOR reporting guideline guidance。
- Nature Portfolio author/submission/reporting guidance。
- Quarto citation/manuscript authoring guidance。

这些来源支持：skills-only Plugin 成立；已安装 Plugin/Skill 可在相关请求中自动使用，但 surface availability 与路由仍需真实 normal-entry 验收；MCP 只在需要外部服务/工具时才有必要；正式稿件包应由期刊/研究类型要求驱动，而不是固定文件爆炸。

## 审查边界

本 REVISE 只针对 v0.1 架构对象。没有批准 implementation、Plugin Creator mutation、release、merge、paid API 或外部数据发送。RA1–RA4 关闭后，应对同一 v0.2 Proposal 重新进行设计阶段 Critic 审查；只有之后的 execution-ready review 才能审 Goal/Kickoff 并决定是否可以交给 Codex。
