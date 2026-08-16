---
schema: AI_BRIDGE_REVIEWED_PLAN_V1
task_key: 001_research_writing
decision: PLAN_FROZEN
---

# Reviewed Handoff Plan

## Objective and value

本任务只处理当前技能库中“科研论文写作”和“文献检索/引用”两组高频能力。现有审计已经证明这些能力总体完整，但相邻技能的触发范围存在明显重叠。目标不是增加更多技能，而是让已经安装的技能根据用户正常表达更稳定地选择正确入口，并让 `research-writing` 插件的两个聚合入口承担清晰的上游分流职责。

本任务是现有库整理的第一批落地，不处理其他 10 个冲突组。

## Frozen decisions

### 1. 顶层结构保持不变

- 保留现有 `research-writing` plugin。
- 保留 `research-paper-workflow` 与 `literature-and-citations` 两个 aggregate。
- 不新增 plugin、skill、profile 或新的顶级入口。
- 不删除、不停用、不归档任何现有 skill。本轮如果发现内容仍高度重复，只通过调用边界和明确委派解决；真正的 merge/delete 必须另开任务。
- `marketplacePluginBudget` 保持 `6`。

### 2. 论文写作组的职责边界

- `research-paper-workflow`：用户面对完整论文任务时的主要入口，负责把请求分派到下列具体能力。
- `paper-workflow-orchestrator`：只负责整篇论文的过程与结构，例如主张-证据骨架、章节职责、结果到主张的门槛、图文同步、论文结构救援和投稿前流程组织；不是段落润色器。
- `scientific-writing`：负责真正的论文正文起草与修改，包括 abstract/introduction/methods/results/discussion、基于已有证据的 reviewer-response 文本修改和报告规范落实。它不再把“整篇论文流程规划、接受风险评审、文献发现、BibTeX 管理、图像制作、期刊格式检查”作为自身主要触发范围。
- `peer-review`：负责 reviewer-style critique、投稿前验收、拒稿/接受风险、方法与证据质疑、rebuttal 评估。普通论文写作或段落修改不应进入这里。
- `scholar-evaluation`：保留为“明确要求多维度量化评分、rubric/benchmark 式学术质量评价”的专门能力。不得再与普通 peer review 或投稿 readiness 争夺宽泛的“帮我评价这篇论文”入口；description 和 `When to Use` 应据此收窄。
- `nature-manuscript-workflow`：继续只负责 Nature-family / broad-journal / high-impact framing 等明确场景，不扩大为普通论文入口。
- `venue-templates`：负责具体期刊/会议投稿格式、模板和 venue 要求。
- `latex-paper-authoring`：负责 LaTeX 结构、编译、Overleaf/投稿源文件问题。

### 3. 文献与引用组的职责边界

- `literature-and-citations`：文献与引用工作的主要聚合入口。
- `literature-review`：负责 field-level synthesis、systematic/scoping/narrative review、related work，以及单篇论文精读/evidence card/method map。它可以组织检索，但不应吞掉“快速查几篇最新论文”“仅核验一个 DOI/引用”“清理 BibTeX”这类更具体任务。
- `research-lookup`：负责面向当前研究信息和论文发现的快速外部检索，尤其是“现在查”“找几篇最新论文”“补充当前证据”等目标。它是检索提供能力，不负责系统综述结构，也不负责最终 citation support verdict。description 应以自然研究任务为主，不把 backend/API 名作为用户必须知道的入口。
- `citation-verification`：负责 citation existence、DOI/PMID/metadata consistency、claim-support、citation drift 和交付前核验。它是 verification gate，不负责一般文献综述。
- `citation-management`：收窄为 bibliography/BibTeX/metadata/reference-library hygiene，包括生成和清理 BibTeX、去重、补全元数据、维护文献表。若需要判断“某引用是否真的支持一句话”，必须委派给 `citation-verification`；若需要领域综述，委派给 `literature-review`。
- `pyzotero`：继续负责 Zotero-oriented library operations，不扩大范围。
- `arxiv-database`、`pubmed-database`、`openalex-database` 等 provider-specific skills 本任务不修改。用户明确点名 provider 时可由已安装环境直接调用；是否把它们进一步纳入 aggregate 是后续独立任务。

### 4. 不用“合并技能”解决第一批问题

第一批的结论是：上述技能虽然相邻，但仍有可解释的独立用户任务。先通过 description、When-to-Use、Hand Off/Routing 和 aggregate 分流把边界写清。Reviewer 只有在改完后仍出现实质同义触发时，才能把“未来考虑 merge”写成非阻断建议，不得在本任务要求删除技能。

## Implementation scope

允许修改的 source layer 主要包括：

- `skills/writing/research/scientific-writing/SKILL.md`
- `skills/writing/research/paper-workflow-orchestrator/SKILL.md`
- `skills/writing/research/peer-review/SKILL.md`
- `skills/writing/research/scholar-evaluation/SKILL.md`
- `skills/writing/research/literature-review/SKILL.md`
- `skills/writing/research/citation-verification/SKILL.md`
- `skills/science/discovery/research-lookup/SKILL.md`
- `skills/science/discovery/citation-management/SKILL.md`
- `scripts/codex_marketplace_config.json`
- 与现有测试体系一致的必要 routing regression fixture/test。

如果某个文件已经满足冻结边界，不要求为了“有改动”而修改它。

修改 source layer 后按仓库既有流程重新生成 registry/catalog/marketplace/plugin generated layer；生成层不得手工设计。

现有三份 `docs/audits/ACTIVE_SKILL_*` 是本任务前的基线证据，不要把它们改写成“事后证明自己正确”的报告。需要记录变更时使用 Reviewed Handoff 的 `RESULT.md` / `FINAL_REPORT.md` 或新增一个简短的本轮验证产物，但不要建立新的审计体系。

## Acceptance and regression gates

### A. 结构门槛

- active skill 总体结构不因本任务新增/删除而改变；不得创建新 skill/plugin/profile。
- `marketplacePluginBudget=6` 保持不变。
- `research-writing` 仍只有现有三个用户可见能力：`research-reporting`、`research-paper-workflow`、`literature-and-citations`。
- generated marketplace/plugin 文件只由既有生成流程产生。

### B. 论文写作边界必须可区分

以下请求应在语义上形成清晰分流：

1. “把 Results 第一节改写成完整论文段落，保留统计量和图号。” -> `scientific-writing`
2. “先把这篇论文的主张-证据骨架、章节职责和图文关系理清楚。” -> `paper-workflow-orchestrator`
3. “按审稿人视角指出主要拒稿风险和 rebuttal 要处理的问题。” -> `peer-review`
4. “按固定维度给这篇工作做量化评分，并逐项解释研究质量。” -> `scholar-evaluation`
5. “这篇准备投 Nature Methods，检查高影响期刊 framing 和 figure-to-claim 逻辑。” -> `nature-manuscript-workflow`
6. “按 TMI/某目标 venue 的投稿要求检查格式和材料。” -> `venue-templates`
7. “把这份 LaTeX 稿件整理到可编译、可提交的状态。” -> `latex-paper-authoring`

不应出现：

- 普通段落润色被 `peer-review` 或 `paper-workflow-orchestrator` 抢走。
- 投稿风险检查被 `scientific-writing` 抢走。
- 普通 reviewer-style critique 被 `scholar-evaluation` 抢走，除非用户明确要 rubric/量化评分。
- 仅因为“论文”两个字就触发 Nature/venue/LaTeX 专门能力。

### C. 文献与引用边界必须可区分

以下请求应形成清晰分流：

1. “围绕这个问题做相关工作梳理，按方法路线和研究空白组织。” -> `literature-review`
2. “深读这篇 PDF，给我 claim-evidence card、方法图和局限。” -> `literature-review`
3. “现在帮我找几篇 2025–2026 年关于这个方法的最新论文。” -> `research-lookup`
4. “检查这个 DOI/PMID 是否真实，并确认这句话是否真的被该文献支持。” -> `citation-verification`
5. “清理这个 `.bib`，补全元数据、去重并生成规范 BibTeX。” -> `citation-management`
6. “把这批文献加入/整理到 Zotero collection。” -> `pyzotero`

不应出现：

- `research-lookup` 把系统综述/related-work synthesis 当成自己的完整任务。
- `citation-management` 对 claim support 给最终结论。
- `literature-review` 抢走单纯 BibTeX 清理。
- `citation-verification` 因为需要查源而变成一般论文发现工具。

### D. 回归检查

至少运行仓库当前要求的完整 source/generation/validation 链，包括：

- `python scripts/skills.py registry --write`
- `python scripts/skills.py validate`
- `python scripts/skills.py audit --all`
- `python scripts/skills.py catalog --write`
- `python scripts/audit_skill_provenance.py --write`
- `python scripts/build_codex_marketplace.py --write --validate --check --path-report`
- `python scripts/provenance_audit.py --check`
- `python scripts/icon_audit.py --scope marketplace --check`
- `python -m unittest discover -s tests`

如果当前环境的 Python 命令名称不同，使用仓库已有兼容方式，但不得降低检查范围。

Reviewer 还必须直接读取真实 diff，并用本 Plan 的自然语言案例做语义检查；不得用关键词打分器代替模型判断。

## Natural-language usage / routing expectations

### Routing contract: `research-paper-workflow`

**front-door**: `research-writing` -> `research-paper-workflow`

**neighbor skills**: `writing-style`, `literature-and-citations`, `research-presentations`, visualization/diagram skills，以及 aggregate 内的 `scientific-writing`, `paper-workflow-orchestrator`, `peer-review`, `nature-manuscript-workflow`, `venue-templates`, `latex-paper-authoring`。

**should-trigger**:

- “帮我把这篇论文从实验结果整理成完整投稿稿件。”
- “先规划这篇论文的主张、章节和图表怎么组织。”
- “把 Results 和 Discussion 改成正式论文文字。”
- “投稿前按审稿人视角检查主要风险。”
- “根据 reviewer comments 修改正文并准备 rebuttal。”
- “检查这篇稿子离目标期刊投稿还缺什么。”
- “把 LaTeX 论文和投稿材料收尾到可提交状态。”

**should-not-trigger**:

- “找一下这个方向最近两年的论文。” -> `literature-and-citations`
- “只把这段中文改得自然一点，事实不要动。” -> `writing-style`
- “把这篇论文做成组会 PPT。” -> presentation capability
- “给这个方法画一张可编辑流程图。” -> visualization/diagram capability

**reason**: 用户只需要描述“写论文、改论文、验收论文、投稿收尾”这类真实任务；aggregate 根据任务阶段分派，不要求记住内部 skill 名。

### Routing contract: `literature-and-citations`

**front-door**: `research-writing` -> `literature-and-citations`

**neighbor skills**: `research-paper-workflow`, `writing-style`, provider-specific database skills，以及 aggregate 内的 `literature-review`, `research-lookup`, `citation-verification`, `citation-management`, `pyzotero`。

**should-trigger**:

- “帮我找这个方向最新的论文。”
- “围绕这个问题做一次相关工作综述。”
- “精读这篇论文，整理核心主张和证据。”
- “检查这篇稿子的引用是否真实、是否支持正文主张。”
- “把这些 DOI/PMID 整理成准确的 BibTeX。”
- “清理这份参考文献，去重并补全元数据。”
- “把这批论文整理进 Zotero。”

**should-not-trigger**:

- “帮我重写这篇论文的 Results。” -> `research-paper-workflow`
- “像 reviewer 一样判断这篇稿子的拒稿风险。” -> `research-paper-workflow`
- “把这段话润色得更自然。” -> `writing-style`
- “查一下今天某家公司发布了什么产品。” -> 不属于本 aggregate 的学术文献任务

**reason**: 用户只需要表达“找论文、做综述、精读、核引用、整理参考文献”等自然目标；aggregate 再根据交付物选择具体能力，不要求用户知道检索 backend、内部 skill 名或来源仓库。

## Out of scope

- 不处理另外 10 个审计冲突组：OCR/PDF、可视化、前端、生物信息、医学影像、临床医学、数据科学、通用 AI/ML、演示文稿、OpenAI/system helpers。
- 不处理任何 Notion candidate，不读取或合并 `Type=Research` 资源。
- 不新增或删除 plugin/skill/profile。
- 不调整 provider-specific database skills 的具体内容或 marketplace 暴露。
- 不建立新的 routing engine、关键词评分器、语义 hash、额外状态机或 Agent-Flow 机制。
- 不因为本轮边界调整顺便重写技能正文的大量参考材料；只改完成冻结边界所必需的 description、When-to-Use、Routing/Hand Off 和少量相关说明。
- Reviewer 不得把“将来可以进一步 merge/精简”升级成本任务 blocker，除非当前实现直接违反本 Plan。
