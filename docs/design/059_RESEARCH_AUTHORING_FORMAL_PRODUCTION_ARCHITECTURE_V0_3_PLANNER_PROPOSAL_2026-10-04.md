# 059 Research Authoring 正式科研文档生产架构 v0.3 — Planner Proposal

日期：2026-10-04  
状态：DRAFT_FOR_CRITIC_REVIEW  
Repository：`YuukiAS/AI_Skills_Collection`  
Source branch：`main`  
Target plugin/domain：`research-writing / Research Authoring`  
Human workflow number：`059`  
Design task key：`research-authoring--formal-production-authoring`  
Review stage：`PRE_IMPLEMENTATION_ARCHITECTURE_REVISION`  
Prior Proposal：`docs/design/059_RESEARCH_AUTHORING_FORMAL_PRODUCTION_ARCHITECTURE_V0_2_PLANNER_PROPOSAL_2026-10-04.md`  
Prior Proposal commit：`e4d62e5377295a2449e9ed5fffa2b92f1426dba8`  
Prior Critic review：`docs/design/059_RESEARCH_AUTHORING_FORMAL_PRODUCTION_ARCHITECTURE_V0_2_CRITIC_REVIEW_2026-10-04.md`  
Prior Critic review commit：`14e4fe1bdd0cde6a590068e2e9af96d81948c778`  
Prior Critic result：`REVISE`  
Stable blocker status：`RA1=CLOSED; RA2=CLOSED; RA3=OPEN; RA4=CLOSED_FOR_ARCHITECTURE_STAGE`

本文件是完整 v0.3 Proposal，取代 v0.2 作为当前 059 架构审查对象。v0.3 只修订 RA3：把 G2 从“仅验证已有文档的增量修改”扩展为同一真实 report-family 任务上的 greenfield authoring + incremental authoring 两阶段 final Gate。RA1、RA2、RA4 及其余产品边界不重开。本轮仍只做设计收敛，不修改 production source，不创建 Goal/Kickoff，不启动 Executor，不创建或更新 ChatGPT Plugin，不调用 paid API，不启动自动化。

## 0. RA1–RA4 正式回应

### RA1 — ACCEPT

Critic 的因果风险成立：现有 `report / paper / litcite` 与下层 `scientific-writing`、`literature-review` 等技能可以分别完成局部工作，但没有一个跨 ChatGPT/Codex 表面的、所有科研文档生产入口都必须消费的文档级合同。因此“用了 research-writing 里的某个技能”不等于“执行了 Research Authoring”。

v0.2 冻结一个新的 canonical orchestration skill：

```text
skills/writing/research/research-authoring-core/
```

它是 Research Authoring 的共享文档级总控，不是新的顶级 Plugin，也不是 Chat-specific Skill。ChatGPT 私有 wrapper 与 Codex `research-main` 都必须消费同一 canonical core source/commit。

core 的职责只到科研文档语义与生产组织：

```text
task intent
-> audience / document purpose
-> source authority / evidence boundary
-> document family
-> claim-evidence spine
-> section jobs
-> main text vs appendix/provenance
-> table / figure / formula scientific roles
-> citation authority
-> incremental-edit scope
-> downstream language / literature / artifact route
-> final document-level scientific QA
```

它不选择统计模型、不发明实验、不拥有语言风格、不拥有 slide/deck、不实现 PDF/LaTeX/DOCX 渲染。

现有入口保留，但降为薄路由：

- `report`：保留。负责 advisor/supervisor/group-meeting written report、research update、milestone、methods note、experiment retrospective、research evolution/decision record、meeting minutes、preregistration/statistical analysis plan 等 report-family 路由。任何新写或实质修改都先消费 core。
- `paper`：保留。负责 manuscript、supplement、submission package、cover letter、reviewer response、thesis/dissertation chapter 等 paper-family 路由。任何新写或实质修改都先消费 core。
- `litcite`：保留，但明确拆成两类：
  - **document-producing branch**：literature review、related work、evidence synthesis、paper-card synthesis when assembled into a reader-facing scholarly document，必须先消费 core；
  - **support-only branch**：paper lookup、exact citation verification、BibTeX/metadata cleanup、Zotero/library hygiene、DOI/PMID/arXiv record resolution，可直接使用文献/引用 support skill，不强制建立文档计划。

下层技能仍保留专业职责，但不再作为顶层科研文档自然请求的替代入口。例如：
- “写 Methods”“重写 Discussion”“写 related work”属于文档生产，即使只改一个 section，也必须经过 core；
- “把这句 Methods 润色一下，内容不变”可以直接进入 Clear Writing / scientific prose；
- “验证这个 DOI 是否支持这句话”可以直接进入 citation verification；
- “找三篇最近论文”可以直接进入 research lookup。

因此，core 是“是否在生产/实质修改科研文档”的语义门，不是所有科研相关请求的总入口。

### RA2 — ACCEPT

v0.2 新增最小 incremental authoring contract。它不创建 database、ledger、长期状态机或另一套 CURRENT。

当目标文档已经存在 canonical source 时，默认流程固定为：

1. **Recover baseline**：读取当前 canonical document/source、必要的 companion files，以及本轮新增的 evidence / decision / reviewer delta。
2. **Locate affected jobs**：按 section job、claim/evidence binding、figure/table/formula/citation dependency 定位受影响单元。
3. **Compute minimal dependency closure**：局部修改不是“只改一个连续段落”，而是只扩展到被新事实真正依赖的最小单元。例如一个新结果可以同时影响 Results、Abstract、Discussion、caption，但不会授权重写未相关的 Introduction。
4. **Patch locally**：默认只改最小 dependency closure。
5. **Protect accepted invariants**：未受影响的已接受文本、notation、claim strength、claim/evidence binding、citation key、LaTeX label/ref、figure/table identity、caption identity、venue-required macro/template 视为 protected by default。
6. **Diff-based QA**：使用现有 document source、Git diff、必要 provenance/source locators 检查是否出现非授权 drift。
7. **Escalate only when justified**：只有下列情况允许全文/大范围重构：
   - 用户明确要求；
   - 新证据推翻现有 document spine，导致原结构失效；
   - venue/project authority 改变了必须满足的结构；
   - 当前文档存在无法通过局部补丁解决的系统性结构错误。
   扩大范围时必须说明“为什么局部 patch 不足”，不能把一次局部更新默认为重新生成全文。

对 paired/bilingual artifacts，科学证据、数字、公式与 claim strength 必须同步；语言组织可按读者分别优化，不要求逐句对应。

CAT-TRACE architecture-evolution 的真实维护规则直接支持这一合同：后续变化修改对应模块，而不是在末尾追加日期流水账。DII advisor report 的 bounded-result-slot 经验也说明，新结果到达后应只补结果槽与直接依赖解释，而不是把早先方法动机重写成“结果早已注定”。

### RA3 — ACCEPT（针对 v0.2 Critic 的窄缺口）

最新 Critic 已接受 G1–G4 四 Gate 架构，但指出 v0.2 的 G2 只直接证明“已有科研文档 + evidence delta -> 安全增量修改”，因此存在一个真实 acceptance loophole：系统可能从未证明自己能从原始 repo evidence / notes / results / figures / prior decisions 独立建立一份合格的 advisor/research report，就凭对一份已经很好、已经被人工组织过的文档做局部 patch 而通过 G2。

这个 finding 成立。v0.3 不增加第五个 Gate，也不拆分 G2。G2 仍证明同一个用户能力族：

> **从原始科研证据建立 reader-first 科研文档，并在同一科学语义合同下长期增量维护而不漂移。**

G2 的 final evidence 改为一个预先冻结的真实 report-family 任务上的连续两阶段：

1. **Greenfield authoring phase**
   - 输入必须是原始项目证据：repo source、notes、results、figures、prior decisions、必要文献来源；
   - 不得把已经整理好的 reader-facing advisor report / research update 当主要输入；
   - normal entry 类似“把这几天研究整理成给老师看的报告”；
   - 从原始证据独立建立完整 advisor/research-update 或 research-evolution document；
   - Reviewer 必须直接读取原始 evidence 与完整成稿；
   - 直接检查 reader-first scientific structure、方法/数据 orientation、claim/evidence boundary、内部运行/审计/执行时间线过滤、table/figure/formula scientific role、reader-facing references 与 internal provenance 分离，以及 Clear Writing handoff 后科学语义是否保持。

2. **Incremental authoring phase**
   - 将第一阶段通过的文档冻结为 baseline；
   - 在整个 final G2 开始前就预先冻结后续 evidence / decision delta，并在第一阶段 authoring 输入范围中排除该 delta，防止事后叙事或未来信息泄漏；
   - 不修改 final candidate、不修改 Reviewer rubric；
   - 使用 RA2 的 minimal dependency closure 更新同一文档；
   - Reviewer 直接比较 baseline、delta、candidate、diff；
   - 检查未受影响正文、notation、claim strength、citation keys、equation labels、figure/table identity、cross references 等 protected invariants。

G2 的 final-candidate/fresh 规则同时冻结：

- product final candidate、Reviewer rubric、greenfield input scope、phase-2 delta identity 在 G2 开始前全部冻结；
- phase 1 或 phase 2 任一 FAIL，G2 即 FAIL；
- phase 1 结束后不得修产品、改 rubric、换 task、换 delta，再把 phase 2 继续算作同一 fresh final evidence；
- 若根据 phase 1 或 phase 2 输出修改产品，下一次 final G2 必须使用新的 final candidate，并重新获得符合 fresh 条件的真实任务/delta；开发期可以继续用已经见过的材料做 regression，但不能伪装成 final evidence；
- 尽量由同一个真实任务完成两个阶段，避免增加用户回归负担。

完整 Matrix 与 final-evidence 语义见第 7 节。

### RA4 — PARTIAL_ACCEPT（设计已由 v0.2 Critic 判定 CLOSED_FOR_ARCHITECTURE_STAGE；保留 pending mutation）

Critic 对 umbrella owner 的要求成立：#20–#29 都是窄问题，不能冒充本轮整体 promotion owner。

v0.2 冻结新的 umbrella 维护对象：

```text
title: Research Authoring 正式科研文档生产收口
kind: enhancement
scope: plugin
area: research-writing
lifecycle: DOING
resolution commit: <blank until truthful closure>
current anchor:
docs/design/059_RESEARCH_AUTHORING_FORMAL_PRODUCTION_ARCHITECTURE_V0_2_PLANNER_PROPOSAL_2026-10-04.md
next action:
independent Critic PRE_IMPLEMENTATION_ARCHITECTURE_REVIEW of v0.2
```

对应 canonical TODO 顶层条目应写入 `docs/plugin-todos/research-writing.md`，并绑定真实 `tracking: #N`。

已有 #20–#29 的独立 backlink 不重绑。当前 `tracking: UNASSIGNED` 且属于本轮同一 promotion 的三个条目计划并入 umbrella：
- advisor report bounded result slot；
- formula display / notation role；
- reader-facing references vs internal provenance。

它们不是三个新 Gate，只是 G2/G3 regression evidence。

但当前 ChatGPT Planner runtime 没有可真实调用的 Clear Writing skill surface；仓库 `AGENTS.md` 与 Maintenance Board 明确要求 reader-facing Issue/Project copy 在 GitHub mutation 前必须真实调用 Clear Writing，并在不可调用时返回 `CLEAR_WRITING_UNAVAILABLE`。因此本轮不能合法创建或实质改写 umbrella Issue，也不能伪造 `tracking: #N`。这不是要求用户手工维护；精确 pending mutation 见第 10 节。Issue 创建后，同一 maintenance action 才能回写 TODO 的真实 `tracking: #N`。

## 1. 产品目标与完成定义

Research Authoring 的产品目标是：

> 把真实研究证据组织成可交给研究者、导师、审稿人或投稿系统使用的科研文档，并在新建、增量修改、跨文件生产与最终 artifact 交付中保持科学语义、证据强度和文档身份一致。

它不是“写得像论文”的语言模板，也不是 PDF 生成器。

下一正式候选仍为：

```text
research-writing 0.2 -> 0.3
```

本轮设计 PASS 只证明架构可进入 implementation planning；不等于 0.3 已发布，更不等于 1.0/stable。

## 2. Canonical Research Authoring Core Contract

### 2.1 唯一共享核心

v0.2 选择 **canonical orchestration skill**，而不是只放一份被动 reference。

原因：

- normal-entry 失败来自“下层 skill 可以被直接命中”，仅靠 reference 存在不能证明其被消费；
- ChatGPT 与 Codex 都能消费同一个 skill source；
- skill 可以拥有明确 trigger boundary、workflow、incremental contract 和 final QA；
- 不需要新 Plugin、MCP、database 或 control plane。

设计身份：

```text
skills/writing/research/research-authoring-core/
```

它应被：
- Codex `research-main` 正常入口包含；
- generated Research Authoring Plugin 的文档生产 routes 强制依赖；
- ChatGPT PRIVATE/USER-scope skills-only wrapper 以同一 canonical commit 打包。

不创建：
- `research-authoring-chat`
- `research-report-chat`
- 第二套 Chat canonical source
- 第二套 TODO/changelog

### 2.2 什么请求必须经过 core

只要任务会 **新建、实质重构或增量修改一个 reader-facing scholarly/research document**，必须消费 core。

包括但不限于：
- manuscript section/full manuscript；
- supplement；
- related work / literature synthesis document；
- advisor/group-meeting written report；
- research update；
- methods/technical note；
- research evolution/decision record；
- meeting minutes；
- preregistration / statistical analysis plan；
- thesis/dissertation chapter；
- cover letter / reviewer response when they are part of scholarly submission authoring。

即使用户只说“写 Methods”或“整理 related work”，也属于 document-producing request。

### 2.3 什么请求可以绕过 core

不是所有 research-related task 都需要文档总控。以下 support-only request 可直接路由：

- exact paper lookup；
- current-paper discovery；
- DOI/PMID/arXiv metadata resolution；
- citation existence/support verification；
- BibTeX cleanup / duplicate repair；
- Zotero/library hygiene；
- 对已经冻结内容的一句/一段纯语言润色；
- 普通模型解释/问答；
- 单纯把已冻结 source render 成 PDF；
- PPT/Beamer/slide-deck authoring。

如果 support-only 任务随后升级为“把这些证据写成一个正式 related-work section/report”，从升级点开始必须进入 core。

## 3. Document-family routes

core 先决定 document family，再调用专门路线；专门路线不得反向重新定义科学事实。

### 3.1 Report family

`report` 保留为薄路由，负责：
- advisor/supervisor/group-meeting written report；
- milestone / research update；
- technical/methods note；
- experiment retrospective；
- research evolution / decision record；
- meeting minutes；
- preregistration / analysis plan。

书面组会报告属于这里；PPT/Beamer/slide-deck 及其导出 PDF 仍属于 Presentations。

### 3.2 Paper family

`paper` 保留为薄路由，负责：
- manuscript；
- supplement；
- thesis/dissertation chapter；
- submission package；
- cover letter；
- reviewer response / rebuttal；
- pre-submission document QA。

`paper-workflow-orchestrator`、`scientific-writing`、`latex-paper-authoring` 等成为 family 内 support skills，不替代 core。

### 3.3 Literature/citation family

`litcite` 保留，但不再把“找资料”和“写相关工作”视为同一种顶层任务：

- lookup / citation verification / bibliography hygiene：support-only，可直接执行；
- literature review / related work / evidence synthesis artifact：document-producing，先经过 core，再由 literature skills 负责检索、筛选、证据结构和引用核验。

## 4. Incremental Authoring Contract

### 4.1 Canonical baseline

已有文档默认先识别：
- canonical source file/root；
- currently accepted/reviewer-seen artifact when relevant；
- related bibliography；
- figure/table/supplement identities；
- project/venue template authority；
- 本轮 evidence/decision/comment delta。

不把旧聊天当 canonical source。

### 4.2 Affected-unit model

不新增持久 schema。运行时只需要临时形成：

```text
delta
-> affected claim(s)
-> affected section job(s)
-> dependent figures/tables/formulas/citations
-> minimal edit closure
```

这一临时 mapping 可以存在于当前 reasoning、review note 或 task-local evidence；默认不作为新的长期 sidecar 文件。

### 4.3 Protected invariants

除非 delta 真正要求变化，下列对象默认保持：

- 已接受的未受影响正文；
- notation 与符号含义；
- theorem/lemma/equation labels；
- citation keys 与 attribution；
- claim strength / uncertainty / limitation；
- figure/table stable identity；
- cross-reference anchor；
- venue-required macros、class、front matter；
- 读者已看到并接受的结构。

### 4.4 允许的大范围重构

仅在以下条件之一成立时：
- 用户明确要求重写；
- document spine 与新证据冲突；
- 原 source 本身存在系统性结构失败；
- venue/project contract 改变。

即使全文重构，也必须重新做 source-fidelity / claim-evidence / citation / figure-table QA，不得以“重写授权”抹掉证据边界。

## 5. Downstream owner boundaries

### Clear Writing

Research Authoring 先冻结：
- audience；
- purpose；
- document/section job；
- claim/evidence；
- allowed structural freedom；
- table/figure/formula role。

Clear Writing 负责内容保真的中文/英文表达、去翻译腔、局部解释和读者可读性。

语言层不得：
- 更换 decisive experiment；
- 改 contribution scope；
- 强化/弱化证据；
- 改 citation authority；
- 删除科学限制。

语言 pass 后，Research Authoring 必须做一次 document-level scientific QA。

### Statistical Modeling / domain methods

统计方法、estimand、模型、实验与数学正确性继续由 Statistical Modeling 或对应领域 owner 决定。Research Authoring 只负责如何在文档中忠实呈现。

### Presentations

Presentations 拥有：
- PPT/PPTX；
- Google Slides；
- Beamer/LaTeX slide deck；
- research/group-meeting deck；
- deck-export PDF。

Research Authoring 拥有书面 advisor/group-meeting report，即使最终形式也是 PDF。

判断依据是 artifact function，不是文件扩展名。

### Renderer / LaTeX / DOCX / Quarto

这些是生产 route，不是科研语义 owner。

`render-chinese-math-pdf` 继续拥有字体、纸张、分页、Pandoc/XeLaTeX、公式渲染和 PDF QA。Research Authoring 只向 renderer 传递已冻结的 document identity / venue-project authority / table-figure-formula roles。

## 6. ChatGPT + Codex 双表面

### 6.1 Canonical source

两表面必须绑定同一 Research Authoring core commit。

### 6.2 ChatGPT surface

未来使用一个 PRIVATE / USER-scope / skills-only personal Plugin wrapper。

wrapper 只是 distribution composition，不是第二套产品源。

它包含：
- Research Authoring core；
- report/paper/litcite 的所需 canonical skill snapshot；
- 同一 canonical commit 的最小必要 Clear Writing support snapshot。

它不包含：
- PDF renderer runtime；
- MCP；
- connector；
- database；
- watcher；
- state machine。

Chat 模式的正常正式输出是：
- stable Markdown/LaTeX 或结构化文本；
- 必要 source/provenance locators；
- document/artifact intent；
- table/figure/formula roles；
- venue/project authority；
- 一个短的 Codex production/render handoff。

### 6.3 Codex surface

Codex `research-main` 负责 repo-grounded production：
- canonical source read/write；
- bibliography/figures/tables；
- LaTeX/DOCX/Quarto route；
- renderer；
- full artifact QA；
- durable repo delivery。

### 6.4 Chat -> Codex handoff minimum contract

handoff 至少携带：

```text
canonical Research Authoring version/commit
document family + audience + purpose
canonical source locator
evidence authority / unresolved evidence
allowed edit scope (incremental vs restructure)
table / figure / formula roles
citation / bibliography authority
venue/project formatting authority
required production route
final artifact(s)
final scientific QA required after rendering
```

不得只写“请把这个 Markdown 渲染成 PDF”。

## 7. Capability Gate Matrix

v0.3 继续只保留 4 个不同用户能力 Gate。RA3 的修订只改变 G2 的 final evidence：G2 现在必须用同一预先冻结的真实 report-family 任务同时证明 greenfield authoring 与 incremental authoring。G1、G3、G4 的架构保持不变。

| Gate | Distinct capability | Normal entry & real input | Complete artifact/evidence | FAIL | Should-not-change | Independent qualitative review | Same final candidate |
|---|---|---|---|---|---|---|---|
| **G1 自然入口与边界** | 证明“科研文档生产必须消费 core”，并且 support-only/邻近领域不误触发；它不证明写得好 | ChatGPT 与 Codex 的自然语言请求；正例至少包括 Methods、research update、related work、existing document revision；near-miss 至少包括 citation verify、paper lookup、单句润色、README/邮件、PPT/Beamer、render-only、普通问答 | 对每个正例看到 core 实际消费后的 document brief/route decision；对负例看到正确 owner；不能只看 trigger match | 正例直接落到下层 skill 未消费 core；负例错误进入 Research Authoring；Chat/Codex 对同一任务给出不同 owner | 纯引用/lookup、Clear Writing、Presentations、renderer-only route 保持独立 | **需要**，对自然语言边界与实际 route 做独立定性判断；机械 routing evidence 只作辅助 | **是** |
| **G2 科研文档语义组织与长期增量维护** | 证明同一个 final candidate 既能从原始科研证据独立建立 reader-first report-family 文档，又能在随后真实 evidence/decision delta 到达时按 RA2 最小依赖闭包更新而不漂移；它不证明 manuscript package 或跨表面分发 | **同一个预先冻结的真实 report-family task，连续两阶段。Phase 1 greenfield：** 从真实 repo evidence / notes / results / figures / prior decisions 开始，不能把已经整理好的 reader-facing report 当主要输入；normal entry 类似“把这几天研究整理成给老师看的报告”。**Phase 2 incremental：** Phase 1 通过后冻结其完整文档为 baseline；使用在整个 final G2 开始前已经冻结、且 Phase 1 authoring 输入范围明确排除的后续 evidence/decision delta，按 RA2 更新 minimal dependency closure | **Phase 1：** 原始 source/evidence scope、完整 advisor/research-update 或 research-evolution source/artifact、必要的 source/claim anchors；Reviewer 直接看到原始证据与完整成稿，并检查 reader-first structure、方法/数据 orientation、claim/evidence、流程/审计抑制、table/figure/formula role、reader-facing references vs internal provenance、Clear Writing handoff 后科学语义。**Phase 2：** frozen baseline、预冻结 delta、完整 candidate、baseline→candidate diff、protected-invariant evidence；Reviewer 直接比较 baseline/delta/candidate/diff | 任一阶段 FAIL 即 G2 FAIL。Phase 1 FAIL 包括：依赖已整理好的 reader-facing report 作为主要输入、按运行时间线组织、方法/数据背景不足、claim/evidence 漂移、内部状态/provenance 泄漏主文、表图公式职责错误、Clear Writing 后语义变化。Phase 2 FAIL 包括：非受影响正文大面积漂移；notation/citation/equation label/figure-table identity/cross-reference 无依据变化；claim strength/limitation 漂移；bounded result 被事后改写成必然结论；或为了通过 Phase 2 在 Phase 1 后修改产品/rubric/task/delta | Phase 1 不得借“reader-first”改写原始科学事实、数字、公式、引用权威、未完成状态；Phase 2 必须保护未受影响 accepted text、notation、citation keys、equation labels、claim/evidence、figure/table identity、cross references；G2 失败后开发可以修产品，但原 final evidence 失去 fresh 身份 | **必须**。同一独立 Reviewer/rubric 可以覆盖两个阶段，但必须直接看到 Phase 1 原始 evidence + 完整成稿，以及 Phase 2 baseline + delta + candidate + diff；不能只跑字符串、diff size 或自动评分 | **是。** final candidate 与 Reviewer rubric 在两个阶段开始前冻结，Phase 1 与 Phase 2 之间禁止 product/rubric 修改；同一 candidate 必须直接通过两阶段 |
| **G3 正式论文生产包与跨文件一致性** | 证明真实 manuscript 任务能按 venue/task 选择必要文件并保持主文、补充材料、引用、图表与声明一致；它不证明 Chat/Codex 分发 | 一个真实 manuscript production task，优先使用 CAT-TRACE 当前 canonical manuscript/submission workspace 或另一个真实项目；在 final candidate 冻结前锁定任务与 venue/project authority | 完整选定 package：manuscript + 本任务实际需要的 supplement/bibliography/figures/tables/captions/metadata/contributions/declarations/checklist/submission files 的**按需子集**；同时提供 package selection rationale 与 cross-file consistency evidence | 固定生成无关 sidecars；遗漏 venue-required artifact；主文/补充/图表/引用矛盾；citation key/label 断裂；旧结果残留；模板被无依据改写 | 未触及章节、venue template、已有 label/cite identity、科学 claim scope | **必须**，并结合 citation/LaTeX 等专业检查；文件存在或 compile success 不算质量 PASS | **是** |
| **G4 ChatGPT/Codex 双表面生产与最终产物** | 证明同一 canonical candidate 能从 Chat 形成可执行 authoring source/handoff，并由 Codex 正常生产最终 artifact；它不重复评估 G2/G3 的全部内容质量 | 选用已经通过 G2 或 G3 语义检查的一项真实任务，从 PRIVATE skills-only Chat wrapper 的自然请求开始，再交给 Codex `research-main` | wrapper/source identity、Chat 输出、Codex handoff、Codex canonical source update、真实最终 PDF/DOCX/LaTeX artifact、renderer/file QA、最终 Research Authoring scientific QA | wrapper 与 Codex core/Clear Writing snapshot identity 不一致；handoff 丢 audience/purpose/edit scope/venue/renderer contract；Codex 只调用 renderer 绕过 authoring；最终 artifact 不可读或科学语义漂移；只返回 repo path 不实际交付 requested artifact | Markdown-only Chat request 不强制 PDF；slide PDF 仍归 Presentations；support-only lookup 不变 | **必须**看真实 final artifact；identity/render 检查同时存在 | **是** |

### 7.1 Regression bank

开发期优先回放已知真实失败：
- DII advisor report 运行日志化、方法/数据背景不足、bounded result slot、双语拆分、公式强调、provenance 泄漏；
- CAT-TRACE architecture evolution 按模块增量更新；
- Clear Writing 与 document semantics 边界；
- renderer/document identity handoff；
- current report/paper/litcite route near-miss。

这些是 development regression，不因为重复使用而伪装成 fresh evidence。尤其已经用于修 G2 greenfield/incremental 机制的 report 与 delta 可以继续做开发回归，但不能再算 final fresh evidence。

### 7.2 Fresh/final evidence

最终批次冻结后：

- **G1**：使用一组未用于调 trigger/description 的自然正例 + near-miss。
- **G2**：预先冻结一个真实 report-family 两阶段任务，并在 Gate 开始前同时冻结 final candidate、Reviewer rubric、Phase 1 raw-evidence input scope 与 Phase 2 evidence/decision delta identity。
  1. Phase 1 从原始 repo evidence / notes / results / figures / prior decisions 独立生成完整 advisor/research-update 或 research-evolution 文档；不得把已有 reader-facing report 当主要输入，Phase 1 authoring 输入范围不得包含 Phase 2 delta。
  2. Phase 1 若通过，立即把该文档冻结为 baseline；不修改 product 或 rubric，使用预先冻结的 Phase 2 delta 按 RA2 minimal dependency closure 更新同一文档，并直接审 baseline、delta、candidate、diff。
  3. 任一阶段失败都使 G2 FAIL。看到任一阶段输出后若修产品、改 rubric、换 task 或换 delta，原 final G2 终止；后续只能作为 development regression，新的 final candidate 需要新的 fresh evidence。
  4. 尽量用一个真实任务完成两阶段，不额外要求用户提供两套 report 任务。
- **G3**：使用一个真实 manuscript production task；CAT-TRACE 当前 `paper/manuscript/` + `paper/submission/` 是合适候选，但正式 final task 必须在 candidate 冻结前确定确切 scope，不能跑后挑最好看的结果。
- **G4**：可以复用已经通过 G2/G3 的同一真实任务做 integration proof，不额外制造第四个内容样本。

用户不是 regression tester。开发与独立质评先完成；用户如需最终验收，只做一次真实消费确认，不承担多轮调试。

## 8. 正式论文 package

保留 v0.1 已接受的按需集合：

```text
manuscript
supplement
bibliography
figures
tables
captions
author metadata
contributions
declarations
reporting checklist
submission manifest
cover letter
reviewer response
```

`declarations` 是 venue-required statements/forms 类别，可包含 data/code availability、funding、competing interests、ethics/permissions 等，但不硬编码某一个期刊的固定全集。

core 必须先做 package selection；没有任务需要的文件不生成。

内部 authoring artifacts（如 claim-evidence map、figure inventory）默认是临时 reasoning / task-local evidence，只有多人协作、长期更新、审查/复现确实需要时才持久化。不得为了“正规”给每个小报告固定生成 5 个 sidecar。

## 9. 外部核查与替代方案

本轮重新核对 OpenAI 当前官方 Plugins/Skills 文档：

- plugin 可仅包含 Skills；MCP 是需要外部服务、认证或受控工具时才添加；
- ChatGPT/Codex 可以消费同一 plugin/skill package；
- skill metadata 决定模型何时考虑该能力，完整 skill instructions 在匹配任务时加载；
- 官方建议用直接、间接、负例和 edge cases 测试 skill activation，而不是只测试显式 invocation。

这继续支持“一个 canonical authoring core + skills-only Chat wrapper + Codex profile”的低复杂度路线，不支持为 Chat 另建 canonical skill 或为了写作增加 MCP。

现实替代比较：

1. **保持现状，仅强化 report/paper/litcite 文案**：过简。无法证明所有 document-producing route 都先做统一文档级决策。
2. **共享 reference 被三个入口读取**：比现状好，但仍较容易被下层自然触发绕过；只证明 reference 存在，不证明 orchestration 被消费。
3. **canonical orchestration skill + 薄路由（本方案）**：新增一个内部 canonical skill，但直接解决 RA1，且同时服务 Chat/Codex。
4. **Chat-specific authoring skill**：拒绝。制造双源和版本漂移。
5. **新 MCP/control service**：拒绝。当前能力只需要 workflow instructions 与已有工具，没有外部服务需求。

## 10. Maintenance umbrella — exact pending mutation

本轮需要一个新的 top-level tracking owner，但当前 runtime 暴露 GitHub Issue 写入能力，却没有可真实调用的 Clear Writing skill surface。根据 `AGENTS.md` 与 `AI_SKILLS_MAINTENANCE_BOARD.md`，reader-facing Issue/Project copy 在这种情况下必须停止，不能用“我读过 writing-style source”冒充调用。

因此：

```text
CLEAR_WRITING_UNAVAILABLE=YES
UMBRELLA_ISSUE_CREATED=NO
PROJECT_FIELDS_SYNCED=NO
```

下一次具有 GitHub Project mutation + Clear Writing invocation 能力的 AI_Skills maintenance action 应执行下面的 exact pending mutation，不要求用户手工操作：

1. 真实调用当前 canonical Clear Writing，对下列 Issue 文案做 no-op 或语言修订，但不得改变 lifecycle/Area/locator/tracking truth。
2. 创建 Issue：
   - title：`Research Authoring 正式科研文档生产收口`
   - labels：`maintenance-track`, `kind:enhancement`, `scope:plugin`, `area:research-writing`
   - body 顶部：
     ```text
     问题：
     收口 Research Authoring 的正式科研文档生产能力，使 ChatGPT 与 Codex 共享同一科研文档语义核心，并完成增量修订、真实论文生产和最终成品验收。

     当前进度：
     059 v0.2 架构修订已落库，等待独立 Critic 做 pre-implementation architecture review。

     当前执行锚点：
     docs/design/059_RESEARCH_AUTHORING_FORMAL_PRODUCTION_ARCHITECTURE_V0_2_PLANNER_PROPOSAL_2026-10-04.md

     下一步：
     独立 Critic 复核 v0.2，优先检查 RA1–RA4 是否关闭、四个 Capability Gate 是否充分且不过重。

     Resolution commit：
     ```
3. 将该 Issue 加入/保持在 `AI Skills Maintenance` Project：
   - Area = `research-writing`
   - Status = `DOING`
   - Resolution commit = blank
4. 取得真实 Issue number `#N` 后，在 `docs/plugin-todos/research-writing.md` 增加顶层 promotion entry：
   - title：`Research Authoring formal production authoring promotion`
   - status：`PROMOTE_NOW` 或由当时 Planner 按 current canonical maturity 选择不夸大的等价状态；
   - tracking：`#N`
   - source：059 v0.2 architecture；
   - problem：现有 report/paper/litcite 缺共享 document-producing core、incremental contract、formal manuscript gate 与 cross-surface final production closure；
   - target layer：research-writing routing/orchestration/QA；
   - candidate action：实现 v0.2 core + thin routes + four-gate release；
   - promotion gate：G1–G4 same-final-candidate PASS。
5. 将当前三个 `tracking: UNASSIGNED` 且已被本轮 v0.2 吸收的条目更新为 `tracking: #N`，并明确 `MERGED_INTO_TRACKING_ISSUE`：
   - bounded result slot；
   - formula display / notation role；
   - reader-facing references vs internal provenance。
6. 保持现有 #20–#29 中已经真实绑定的独立 backlink 不变。

Critic 应把这一区分为：
- RA4 的**设计归属与 exact mutation contract 已关闭**；
- live GitHub tracking mutation 尚未执行，原因是当前 surface 缺少仓库要求的 Clear Writing invocation capability。
如果 Critic 仍要求 live Issue 作为本阶段 PASS 前置，则继续保持 RA4 open；Planner 不通过绕过 Clear Writing 来制造假 closure。

## 11. Version / release decision

本轮只是 design docs：

```text
Repository bump decision: NONE
Affected plugins:
- research-writing: NO_BUMP
Reason: no production behavior changed in this design-only revision.
```

未来 implementation + real replay + full Gate PASS 后，候选 release 仍为：

```text
research-writing 0.2 -> 0.3
```

`1.0` 仍要求多个独立真实任务长期证明可作为默认工具，并由用户/Planner明确决定。

## 12. Non-goals

v0.2 明确不做：

- 不创建新的顶级 Plugin；
- 不创建 Chat-specific canonical authoring skill；
- 不创建 database / ledger / state machine；
- 不新建 MCP/connector；
- 不把 Presentations、Clear Writing、Statistical Modeling、renderer 并入 Research Authoring；
- 不固定一种论文模板或一种 venue；
- 不固定每个任务生成全部 submission sidecars；
- 不把 Quarto/LaTeX/DOCX 当科研语义 owner；
- 不在本阶段创建 Goal/Kickoff；
- 不启动 implementation、Plugin Creator mutation 或 paid review。

## 13. Critic 本轮需要裁定的对象

v0.3 只请求 Critic 复核 RA3 的修改及其对已接受 Gate 架构的影响：

1. G2 是否已经直接证明 greenfield report-family authoring，而不再依赖“已有好文档”；
2. greenfield + incremental 两阶段是否仍属于同一个科研文档语义能力 Gate，而不需要 split/new Gate；
3. final candidate、Reviewer rubric、Phase 1 input scope 与 Phase 2 delta 的冻结顺序是否足以防止看结果后继续调产品却冒充同一 fresh final evidence；
4. Phase 1/Phase 2 的 complete artifact、FAIL、should-not-change 与 independent qualitative review 是否足够直接；
5. G2 的修订是否意外与 G1、G3 或 G4 重复，或削弱它们原已接受的职责边界。

稳定状态继续保持：

```text
RA1 = CLOSED
RA2 = CLOSED
RA4 = CLOSED_FOR_ARCHITECTURE_STAGE
```

没有新直接证据时不得重开 RA1、RA2、RA4。

第 10 节 live umbrella Issue / Project mutation 仍未执行，不得声称已同步；其 exact pending mutation 保持 v0.2 设计，不要求用户手工维护。

若 RA3 关闭，本轮得到 PRE_IMPLEMENTATION_ARCHITECTURE PASS。下一步仍应回 Planner 准备同版本 execution package；不得从本 Proposal 直接开始实现。

