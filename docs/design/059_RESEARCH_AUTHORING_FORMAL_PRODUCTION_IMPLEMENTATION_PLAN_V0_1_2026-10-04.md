# 059 Research Authoring 正式科研文档生产 — Implementation Plan v0.1

日期：2026-10-04  
状态：READY_FOR_EXECUTION_READY_CRITIC_REVIEW / NOT_EXECUTION_AUTHORIZATION  
Repository：`YuukiAS/AI_Skills_Collection`  
Target plugin：`research-writing / Research Authoring`  
Task key：`research-authoring--formal-production-authoring`  
Human workflow number：`059`  
Source ref：`main`

架构 authority：

- Proposal：`docs/design/059_RESEARCH_AUTHORING_FORMAL_PRODUCTION_ARCHITECTURE_V0_3_PLANNER_PROPOSAL_2026-10-04.md`
- Proposal commit：`42a86fcae336a139ed5def027b12f3cd9715dbaa`
- Architecture Critic PASS：`docs/design/059_RESEARCH_AUTHORING_FORMAL_PRODUCTION_ARCHITECTURE_V0_3_CRITIC_REVIEW_2026-10-04.md`
- Critic review commit：`a446b2ed3e0dc41ade9d6a3315091f9fbe36e084`

同版 Canonical Goal：

`docs/goals/059_RESEARCH_AUTHORING_FORMAL_PRODUCTION_GOAL_V0_1.md`

同版 Kickoff Draft：

`docs/operations/prompts/059_RESEARCH_AUTHORING_FORMAL_PRODUCTION_KICKOFF_V0_1.md`

本 Plan 只把已经 PASS 的 v0.3 架构落实成执行合同，不重新设计 Research Authoring。只有独立 Critic 对本 Plan、同版 Goal 与同版 Kickoff 给出 execution-ready PASS，且用户随后实际发送 approved Kickoff，才形成 implementation authorization。

## 1. Positive completion

本任务的真实完成对象是一个**尚未正式发布的 Research Authoring 0.3 最终候选**。同一个 final candidate 必须同时证明：

1. 所有真正的新建、实质修改科研文档请求会先消费 canonical Research Authoring core，而不是直接落到下层写作/文献 skill；
2. `report`、`paper`、`litcite` 保留为已批准的薄路由，support-only 文献/引文、纯语言润色、render-only、PPT/Beamer、普通科研问答不被 Research Authoring 抢走；
3. 已有 canonical document 可以按 evidence/decision/reviewer delta 做最小依赖闭包更新，并保护未受影响内容；
4. G2 同一真实 report-family 任务能先从原始科研证据建立完整文档，再在预冻结 delta 到达后安全增量更新；
5. G3 一个真实 manuscript task 能按 venue/project authority 选择必要文件，并保持主文、补充、引用、图表、label 和声明一致，不固定生成全部 sidecar；
6. G4 同一个 canonical candidate 能从 PRIVATE / USER-scope / skills-only ChatGPT wrapper 形成稳定 source/handoff，再由 exact Codex `research-main` candidate 生产真实最终 artifact；wrapper 与 Codex 消费同一 core identity，Clear Writing support 绑定同一 canonical commit；
7. 最终 artifact 通过 Research Authoring 文档级科学 QA；renderer/LaTeX/DOCX 只承担各自 mechanics；
8. generated source、profile、Marketplace、README/changelog/version candidate 与实际加载内容一致；
9. 所有 final Gate evidence 只绑定同一个 `FINAL_CANDIDATE_COMMIT=C`，不得跨 candidate 拼 PASS。

本任务不包含正式 merge/release。实现与 Gate 全部通过后最大产品状态是：

```text
RESEARCH_AUTHORING_0_3_CANDIDATE_READY=YES
FORMAL_RELEASED=NO
MAIN_MERGED=NO
```

## 2. Exact execution identity

```text
task_key = research-authoring--formal-production-authoring
branch = work/research-authoring--formal-production-authoring
worktree = ../AI_Skills_Collection-research-authoring--formal-production-authoring
```

worktree 以 verified canonical `AI_Skills_Collection` checkout root 的父目录为基准，basename 必须精确匹配。开始时解析并打印真实绝对路径。

本任务采用人工：

```text
Planner -> Codex Executor -> pre-final Critic -> final Gate evidence -> independent Reviewer
```

不安装 watcher、daemon、自动任务链或新的状态机。

用户实际发送 execution-ready Critic 已逐字批准的 Kickoff 后，才授权创建/复用上述 exact branch/worktree，并授权该分支 task-owned commit 与 ordinary non-force push。若 exact branch/worktree 已存在，只能在 repo identity 与 branch 完全匹配时复用；不创建替代 worktree、第二 clone 或不同 branch。

## 3. Latest-main / governance preflight

Executor 在任何 production edit 前必须：

1. 在 canonical checkout 执行 `git fetch origin main`；
2. 核实 repo root、origin、current `origin/main`；
3. 确认本 execution package commit 已在 current history；
4. 读取 current：
   - `AGENTS.md`
   - `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
   - `docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md`
   - `docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md`
   - `docs/PLUGIN_MATURITY.md`
   - `docs/plugin-todos/research-writing.md`
   - `docs/plugin-changelogs/research-writing.md`
   - approved v0.3 Proposal + Critic PASS
   - `skills/core/codex-system/codex-workflow-protocol/SKILL.md`
   - current `ai-skills-core` maintenance instructions
   - current Research Authoring source/profile/config/tests；
5. 确认 `origin/main:VERSION` 与 current formal release history；
6. 检查 exact branch/worktree 冲突与 unrelated dirty work ownership。

### 3.1 Umbrella maintenance pending mutation

架构阶段已经批准 umbrella：

`Research Authoring 正式科研文档生产收口`

但截至本 execution package 形成时：

```text
UMBRELLA_ISSUE_CREATED=NO
PROJECT_FIELDS_SYNCED=NO
```

原因仍是 Planner surface 缺少“真实 Clear Writing invocation + GitHub Project mutation”组合能力，不能绕过仓库规则。

Executor preflight 必须机械刷新 approved pending mutation：

- current proposal locator：
  `docs/design/059_RESEARCH_AUTHORING_FORMAL_PRODUCTION_ARCHITECTURE_V0_3_PLANNER_PROPOSAL_2026-10-04.md`
- architecture PASS review：
  `docs/design/059_RESEARCH_AUTHORING_FORMAL_PRODUCTION_ARCHITECTURE_V0_3_CRITIC_REVIEW_2026-10-04.md`
- current execution anchor：
  本 Implementation Plan v0.1
- next action：
  execution-ready Critic PASS 后执行 059 implementation

若执行环境**同时**可以：
- 真实调用当前 installed Clear Writing；
- 创建/更新 GitHub Issue；
- 修改 `AI Skills Maintenance` Project fields；

则在 production edit 前按 v0.3 §10 exact pending mutation 创建/同步 umbrella，Area=`research-writing`、Status=`DOING`、Resolution commit 为空，并取得真实 `tracking: #N` 后更新 canonical TODO backlink。

若只有 Clear Writing + Issue write、但无 Project field mutation，可合法创建 Issue/更新 TODO 后记录 exact pending Project mutation；不得声称 Project 已同步。

若连合法 reader-facing Issue mutation 前提都不满足，记录：

`BLOCKED_MAINTENANCE_TRACKING_SURFACE`

并停止 production implementation，等待下一个合法 maintenance surface。不得要求用户手工创建 Issue/拖 Project，也不得自行仿冒 Clear Writing invocation。

## 4. Implementation scope

### 4.1 Canonical core

新增：

```text
skills/writing/research/research-authoring-core/
└── SKILL.md
```

默认不新增 runtime script、database、schema、ledger 或永久 sidecar。只有 current Skill validation 明确要求既有标准 metadata 文件时，才按 repo convention 增加最小 metadata；不得借实现扩大产品。

core 必须实现：

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
-> downstream owner route
-> final document-level scientific QA
```

同时实现明确 trigger boundary：
- document-producing request 必须先消费 core；
- support-only request 不强制 core。

### 4.2 Thin routes

必须调整现有 source，使其服从 core，而不是复制 core 规则：

- `research-reporting`：report-family thin route；
- `paper-workflow-orchestrator`：paper-family thin route；
- `scientific-writing`：文档生产中的 section prose support；纯局部内容保真润色仍可作为 support-only；
- `literature-review`：document-producing literature/related-work 必须经过 core；
- `citation-verification`、`research-lookup`、`citation-management`：保留 support-only 边界；只有实现发现当前 description 会错误抢 document-producing request 时才做最小 routing 修订。

不得把 core 内容复制进多个 skill 形成第二套规则。各 route 只保留 owner、何时进入 core、何时 handoff 给下层 specialist。

### 4.3 Real consumers

至少修改并验证：

```text
profiles/research-main.json
profiles/codex-research-writing.json
scripts/codex_marketplace_config.json
tests/test_research_writing_routing.py
```

以及实现真正需要的最小 focused tests。

`scripts/codex_marketplace_config.json` 必须让 generated Research Authoring plugin 的 document-producing routes 实际消费 core。实现可将 `report/paper/litcite` 保持相同 artifact id/用户入口，但必须在现有 generator 能表达的最小结构中实现：

- report：core 为 document-level coordinator，再进入 research-reporting；
- paper：core 为 document-level coordinator，再进入 paper workflow/support skills；
- litcite：document-producing branch 经过 core；lookup/citation/BibTeX/Zotero support-only branch不得被迫执行完整 document plan。

如果 current aggregate generator 无法在不新增新架构的情况下表达已批准 routing，停止并返回 Planner/Critic；不得偷偷建立第二个 router/runtime。

### 4.4 Generated layer

生成层只通过 current generator 更新，不手改：

```text
plugins/codex/plugins/research-writing/**
.agents/plugins/marketplace.json
registry.json
docs/SKILL_CATALOG.md
docs/domains/**
docs/SKILL_PROVENANCE.md
docs/skill_provenance_audit.json
```

以及 current scripts 实际产生的直接相关 generated files。

### 4.5 Explicitly out of scope

不得修改以下 owner 的核心行为：

- Statistical Modeling / domain model design；
- `writing-style` / Clear Writing source；
- Presentations source、deck routing、Beamer/PPTX ownership；
- `render-chinese-math-pdf` rendering/font/pagination implementation；
- Bridge Kit；
- 外部研究仓库 production source；
- MCP / connector / database / watcher / state machine；
- 新 top-level Research Authoring Plugin；
- Chat-specific canonical `research-authoring-chat` / `research-report-chat`；
- 论文 venue 固定模板；
- 固定 sidecar file set。

若实现发现这些 owner 本身有直接缺陷，记录证据并返回 Planner；不要把 059 变成跨插件返修。

## 5. Incremental authoring contract

core 必须落实已批准 RA2：

```text
existing canonical document
+ evidence / decision / reviewer delta
-> affected claims
-> affected section jobs
-> dependent figures/tables/formulas/citations
-> minimal dependency closure
-> local patch
-> diff QA
```

默认保护未受影响：

- accepted text；
- notation；
- claim strength；
- claim/evidence binding；
- citation keys / attribution；
- equation/theorem labels；
- figure/table identity；
- captions；
- cross references；
- limitations / uncertainty；
- venue/project-required macros/template/front matter。

只有：
- 用户明确要求全文重构；
- evidence 推翻 document spine；
- 原 source 存在系统性结构失败；
- venue/project authority 改变；

才允许扩大范围，并必须解释为什么局部 patch 不足。

不得为此新增长期 change ledger、persistent claim database 或 mandatory sidecar。运行时临时 dependency map 可以存在于当前 reasoning、task-local evidence 或 review packet。

## 6. Owner boundaries and support composition

### Clear Writing

Research Authoring 先冻结 audience/purpose/document job/claim-evidence/allowed structural freedom/table-figure-formula role。

然后调用已有：
- `writing-fidelity`
- 中文：`chinese-prose`
- 英文科学写作：`scientific-prose`

Clear Writing 只改善表达，不能改科学事实、decisive experiment、contribution scope、claim strength、citation authority 或限制条件。语言 pass 后 Research Authoring 必须重新做 document-level scientific QA。

本任务不修改 Clear Writing source。

### Presentations

PPT/PPTX、Google Slides、Beamer/LaTeX slide deck 及其导出 PDF 继续归 Presentations。书面 advisor/group-meeting report 即使最终导出 PDF，仍归 Research Authoring。

### Renderer

正式 PDF mechanics 继续归 `render-chinese-math-pdf`。Research Authoring 只传：
- document identity；
- venue/project authority；
- table/figure/formula role；
- source locator；
- expected final artifact。

不得复制字体、Pandoc/XeLaTeX、paper-size 或 PDF QA 实现。

## 7. Development regression phase

在 final holdout 前，允许反复使用已知真实失败做开发回归：

- DII advisor report 运行日志化；
- 方法/数据背景不足；
- bounded result slot；
- 双语结构；
- 公式职责；
- reader-facing references / internal provenance；
- CAT-TRACE architecture evolution 按模块增量更新；
- report/paper/litcite routing near-miss；
- existing Research Authoring formal-PDF handoff；
- current citation lookup / verification boundary。

这些材料只能证明 development regression。任何已经用于设计/修产品的 DII/CAT-TRACE 样本不得重新标为 final fresh evidence。

开发期先运行便宜、确定性检查与现有 tests；必要时生成代表性完整文档让 Planner/Critic判断机制是否稳定。不要为了准备 final Gate 无限增加样本。

## 8. Candidate-owned content and pre-final freeze

在任何 final G1–G4 之前完成全部 candidate-owned content：

### Runtime/source

```text
skills/writing/research/research-authoring-core/**
直接必要的 research-writing source boundary edits
profiles/research-main.json
profiles/codex-research-writing.json
scripts/codex_marketplace_config.json
```

### Product tests

```text
tests/test_research_writing_routing.py
directly necessary new focused test(s), if justified
repo-safe fixture(s), only when needed
```

### Generated identity

current generator 输出的 Research Authoring/registry/catalog/provenance/Marketplace/plugin/profile parity files。

### Release-candidate metadata

在 final candidate freeze 前准备：
- `research-writing` plugin config：`0.2 -> 0.3` exactly once；
- `docs/plugin-changelogs/research-writing.md`：0.3 before/after；
- root `CHANGELOG.md`：写入 Unreleased candidate summary，不冒充 formal repository release；
- root `README.md`：Research Authoring version/能力描述与真实 candidate 一致；
- `docs/PLUGIN_MATURITY.md` 默认保持 `unclassified`，除非用户/Planner基于真实多任务 evidence 另行决定；059 不自动升 maturity。

根 `VERSION` **本任务不修改**。Repository version 只在后续 formal release closure 根据当时 formal baseline 决定 PATCH。当前 planning baseline 为 `5.4.4`，但不得预先硬编码未来 formal version。

README 若发生用户可见变化，Executor 必须在提交前真实调用 installed Clear Writing；若不可用，返回 `CLEAR_WRITING_UNAVAILABLE`，不得自行仿冒。若最终确定无需 README 改动，结果中必须写：

`README checked: no update required`

但当前版本从 0.2 到 0.3 会改变 README plugin table，因此默认预期需要 README 更新。

## 9. Deterministic validation before final candidate

候选冻结前至少运行 current canonical equivalents：

```bash
python scripts/skills.py registry --write
python scripts/skills.py catalog --write
python scripts/audit_skill_provenance.py --write
python scripts/skills.py validate
python scripts/skills.py audit --all
python scripts/build_codex_marketplace.py --write --validate --check --path-report
python -m unittest tests.test_research_writing_routing
python -m unittest tests.test_codex_marketplace
python -m unittest discover -s tests
git diff --check
```

并执行：
- generated Research Authoring plugin source parity；
- `research-main` / `codex-research-writing` install smoke；
- no renderer behavior/source change proof；
- no Presentations/Clear Writing/Statistical Modeling production-source change proof；
- plugin version/changelog/README parity。

这些都只是 mechanical/development evidence，不是 G1–G4 final PASS。

## 10. Pre-final Critic admission

deterministic validation 与开发回归稳定后，先形成一个 exact pre-final candidate commit `C0`，并冻结完整 final Gate packet：

- G1 natural positive + near-miss case list；
- G2 exact real report-family task identity；
- G2 Phase 1 raw-evidence input scope；
- G2 Phase 2 evidence/decision delta identity；
- G2 Reviewer rubric；
- G3 exact real manuscript task identity；
- G3 venue/project authority；
- G3 required package subset + Reviewer rubric；
- G4 复用 G2 或 G3 的 exact task；
- G4 wrapper composition；
- G4 Chat -> Codex handoff rubric；
- privacy/reviewer-access path；
- final evaluation count/budget；
- should-not-change bank；
- exact candidate-owned allowlist。

这些对象必须在 final Gate 输出出现前冻结，不能看结果后换题。

独立 pre-final Critic 必须直接审：
- `C0` candidate source/生成层/metadata；
- representative development artifact；
- G1–G4 frozen inputs/rubrics；
- Reviewer 能否访问完整 source/render/artifact；
- 用户/隐私/外部传输/Plugin Creator authority；
- final evidence 是否真正 fresh。

若 Critic REVISE：
- 不运行 final G1–G4；
- 只按 finding 修 development candidate/packet；
- 形成新的 `C0_n` 再审；
- 不消耗 final evidence。

若 Critic PASS 且不要求 candidate-owned change：

```text
FINAL_CANDIDATE_COMMIT=C=C0
```

从此直到 final Reviewer decision，candidate-owned content 不得变化。

## 11. Final-candidate immutability

`C` 后允许 tracked changes 默认只在：

```text
results/research-authoring--formal-production-authoring/**
```

用于 Gate inputs/outputs、review packet、evidence、RESULT/MANIFEST 和独立 review。

ChatGPT wrapper archive、可能含私有/大文件的完整 artifacts 放：

```text
private/exports/research-authoring--formal-production-authoring/
```

并记录 hashes/manifest；不得只留 `/tmp`。

如果 `C` 后任何 candidate-owned file 变化：
1. 所有受影响 final evidence 立即 stale；
2. 修复后创建新 candidate `C2`；
3. pre-final Critic 必须按变更风险重新确认；
4. 使用新的 fresh final evidence；
5. 不跨 candidate 拼 PASS。

## 12. G1 — 自然入口与边界

Final claim：真正 document-producing 请求在 ChatGPT/Codex 两表面都消费 core；near-miss 保持正确 owner。

冻结 positive 至少覆盖自然未点名请求：
- 写/修改 Methods；
- 整理 research update；
- 写 related work；
- 修改 existing research document。

near-miss 至少覆盖：
- citation verify；
- paper lookup；
- 单句内容不变润色；
- README / 邮件；
- PPT / Beamer；
- render-only；
- 普通科研问答。

Codex surface 先从 exact `C` 构建/安装 candidate，在 fresh normal runtime 执行。Chat surface 的对应 final evidence在 G4 wrapper授权后补齐。

Executor只生成 route/runtime evidence；独立 Reviewer最终决定 G1 PASS/FAIL。不能由：
- description；
- trigger JSON；
- static routing note；
- keyword；
- install success；

单独 PASS。

G1 FAIL：
- document-producing 正例直接命中下层 skill 而无 core；
- near-miss被 Research Authoring 抢走；
- Chat/Codex 对同一请求 owner 不一致；
- installed runtime不能回指 `C`。

## 13. G2 — 科研文档语义组织与长期增量维护

G2 使用**一个预先冻结的真实 report-family 任务**连续两阶段。

### Phase 1 greenfield

输入：
- 原始 repo evidence；
- notes；
- results；
- figures；
- prior decisions；
- 必要文献来源。

不得把已经整理好的 reader-facing advisor report/research update 当主要输入。Phase 1 输入范围必须显式排除 Phase 2 delta。

normal entry 类似：

“把这几天研究整理成给老师看的报告”

final candidate runtime 产生完整 advisor/research-update 或 research-evolution document。

独立 Reviewer必须直接看原始 evidence 与完整成稿，检查：
- reader-first scientific structure；
- scientific question/decision；
- 方法和数据 orientation；
- claim/evidence boundary；
- unfinished/conditional/negative evidence strength；
- runtime/audit/job/implementation chronology过滤；
- table/figure/formula scientific role；
- reader-facing references vs internal provenance；
- Clear Writing handoff 后科学语义。

Phase 1 任一关键失败 => G2 FAIL，停止 Phase 2。

### Phase 2 incremental

只有独立 Reviewer对 Phase 1 给出 `PHASE1=PASS` 才继续。

将 Phase 1 成稿冻结为 baseline。使用**在整个 G2 开始前已经冻结且 Phase 1 看不到**的 evidence/decision delta。

final candidate与 Reviewer rubric 不变。按 RA2 minimal dependency closure 更新同一文档。

Reviewer直接比较：
- baseline；
- delta；
- candidate；
- diff。

保护：
- 未受影响 accepted text；
- notation；
- claim strength；
- citation keys；
- equation/theorem labels；
- figure/table identity；
- cross refs；
- limitation/uncertainty；
- venue/project identity。

Phase 2 FAIL => G2 FAIL。

如果看到任一 final phase 输出后修 product/rubric/task/delta，本次 final G2 终止；旧材料只回开发 regression，新的 candidate必须重新取得 fresh final task/delta。

## 14. G3 — 正式 manuscript production package

在 pre-final Critic 前冻结一个**未用于 059 产品调优**的真实 manuscript task；不得执行后挑赢家。

CAT-TRACE 当前 `paper/manuscript/`、`paper/submission/` 可以继续用于 development regression/结构参考，但因为已参与本轮设计取证，默认不作为最终 fresh holdout；若 pre-final Critic 有直接证据证明某个完全未用于调优的 CAT-TRACE 新任务仍满足 fresh 条件，可显式批准，否则选另一独立真实 manuscript task。

冻结：
- source repo/ref；
- manuscript task；
- venue/project authority；
- required package subset；
- source/reviewer access；
- rubric。

按需集合来自已批准架构：

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

只生成该任务真正要求的子集。不得为 PASS 制造空文件或无关 sidecar。

Reviewer直接检查：
- 科学主张跨主文/补充/表图一致；
- citation key/label/cross-ref完整；
- bibliography authority；
- venue-required statements/forms；
- figures/tables/captions identity；
- 未触及章节/模板不漂移；
- 无旧结果/旧版本残留；
- compile/render只是辅助，不是质量 PASS。

## 15. G4 — ChatGPT + Codex 双表面最终生产

G4 复用已经通过 G2 或 G3 的同一个真实内容任务，不新增第四个内容样本。

### 15.1 Future ChatGPT wrapper composition

本轮 Kickoff **不授权 Plugin Creator mutation**。Executor只准备 exact wrapper composition/manifest，不创建/更新 live Plugin。

未来 wrapper 是：

```text
scope = USER
discoverability = PRIVATE
skills-only = YES
MCP = NO
connector = NO
database/watcher/state = NO
PDF renderer runtime = NO
```

wrapper canonical Research Authoring 内容必须来自 exact `C` generated Research Authoring skill payload，并用 hashes证明与：

`plugins/codex/plugins/research-writing/skills/** @ C`

一致。

额外打包同一 canonical commit 的最小 Clear Writing support：

```text
skills/writing/core/writing-fidelity/**
skills/writing/core/chinese-prose/**
skills/writing/core/scientific-prose/**
```

只作 support snapshot，不改变 Clear Writing ownership。

当前计划的个人 wrapper 名称为：

`research-authoring`

首次 bootstrap version：

`0.1.0`

真正 mutation 前必须重新盘点 Plugin Creator inventory：
- 0 个同名 wrapper：只有取得用户明确授权后才允许 initial create；
- 1 个：只有取得用户明确授权后才允许 guarded update；
- >1 个：停止并向用户请求一次最小 identity 选择；
- update必须使用 current release id concurrency guard；
- overlay 不能安全删除/rename stale file 时停止，不伪装更新成功。

### 15.2 Required user-only boundary

G1–G3 与 wrapper package/manifest 都准备完成后，若 G4 尚缺 live wrapper，唯一必要用户授权应压缩为一次：

> 批准从 exact final candidate C 创建/更新 PRIVATE USER-scope skills-only `research-authoring` wrapper，并仅用于当前 G1/G4 验收；不添加 MCP/connector，不发布公开，不发送私有科研数据到未批准外部服务。

未获得该授权：
- 保留 G1 Codex evidence、G2/G3 PASS evidence；
- `G4=WAITING_USER_PLUGIN_MUTATION_AUTHORIZATION`；
- overall candidate不能宣称 complete；
- 不换别的分发路线。

若新安装的 Plugin 必须新开 ChatGPT 会话才能加载，用户最多执行一次 unavoidable action：开启 fresh thread 并发送预冻结的 G1/G4 natural request。不得要求用户多轮试错。

### 15.3 Cross-surface handoff

Chat side必须输出：
- stable Markdown/LaTeX/structured source；
- document family + audience + purpose；
- canonical source locator；
- evidence authority/unresolved evidence；
- incremental/restructure scope；
- table/figure/formula role；
- citation authority；
- venue/project authority；
- required production route；
- final artifacts；
- final Research Authoring QA requirement。

不得只写“请渲染这个 Markdown”。

Codex side使用 exact `C` 的 `research-main` candidate继续，必须证明：
- Research Authoring core已消费；
- handoff字段没有丢；
- renderer/LaTeX/DOCX只处理 mechanics；
- 最终 artifact真实存在、可打开/保存、可读；
- final Research Authoring scientific QA实际执行。

## 16. Reviewer ownership and evidence paths

Executor不拥有 G1–G4 最终定性 PASS。Executor负责 exact candidate与完整 evidence packets；独立 Reviewer按冻结 rubric判 Gate。

建议 tracked evidence：

```text
results/research-authoring--formal-production-authoring/
├── RESULT.md
├── MANIFEST.md
├── PREFINAL_GATE_FREEZE.md
├── PREFINAL_CRITIC_REVIEW.md              # external Critic evidence/locator
├── G1_ROUTING_PACKET.md
├── G1_ROUTING_REVIEW.md                   # Reviewer
├── G2_PHASE1_PACKET.md
├── G2_PHASE1_REVIEW.md                    # Reviewer intermediate decision
├── G2_PHASE2_PACKET.md
├── G2_FINAL_REVIEW.md                     # Reviewer
├── G3_MANUSCRIPT_PACKET.md
├── G3_MANUSCRIPT_REVIEW.md                # Reviewer
├── G4_CHAT_CODEX_PACKET.md
├── G4_CHAT_CODEX_REVIEW.md                # Reviewer
└── IMPLEMENTATION_REVIEW.md               # overall Reviewer
```

不要为了列表机械创建空文件；只有实际阶段产生内容才创建。

如果完整 artifact 太大或不适合 public repo：
- 放 `private/exports/research-authoring--formal-production-authoring/`；
- tracked packet记录 hash、identity、review access；
- Reviewer必须实际拿到全文/render，不能只读摘要。

### Reviewer rubric

G1–G4 rubric必须在 pre-final Critic前冻结，严格采用 v0.3 Gate Matrix，不临场新增“更保险”标准。

Reviewer最大职责：
- 核实 exact `C`；
- 直接审完整 inputs/source/output；
- 给每个 Gate PASS/FAIL；
- 检查同一 candidate；
- 区分产品失败、输入问题、renderer/environment、reviewer误判；
- 最终写 `IMPLEMENTATION_OVERALL=PASS|REVISE`。

## 17. Evidence head / same-candidate proof

final Gate evidence完成后形成：

`EVIDENCE_HEAD=E`

必须直接证明：

```text
C..E
=> candidate-owned content unchanged
```

保存：
- `git diff --name-status C..E`；
- candidate-owned allowlist/deny check；
- Research Authoring source/generated tree hashes；
- installed runtime identity；
- wrapper manifest/hash绑定 `C`；
- final artifact hashes。

如果 `C..E` 出现 candidate-owned变化：
- 当前 final Gate evidence失效；
- 不能由 Reviewer“酌情放行”；
- 返回 candidate repair + pre-final Critic + fresh final evidence。

## 18. Version / changelog / README / generated parity

### Current implementation candidate

```text
Repository bump decision: NONE in this implementation task
research-writing: 0.2 -> 0.3 in exact final candidate
maturity: remains unclassified
```

理由：
- 当前任务只形成未发布 final candidate，不推进 formal repository release；
- 0.3 是已批准的真实 user-facing improvement batch identity；
- repository `VERSION` 只由后续 formal release closure决定 PATCH，不在 059 implementation branch 预先改变。

必须同步：
- `scripts/codex_marketplace_config.json`
- `docs/plugin-changelogs/research-writing.md`
- README Research Authoring row/描述
- generated plugin manifest
- registry/catalog/provenance/profile identity
- root `CHANGELOG.md -> Unreleased`

README修改必须真实调用 Clear Writing；Clear Writing只可改善表述，不得改版本/事实/路径/安装语义。

后续 formal release 才决定：

```text
Repository bump decision: PATCH
exact version = next patch from then-current formal release baseline
Affected plugin:
- research-writing: candidate 0.3 -> formally released 0.3
```

本 Plan 不授权这一步。

## 19. Failure and recovery

### Implementation/development failure

在 final candidate freeze前：
- 定位根因；
- 在冻结架构内修复；
- 重跑风险匹配回归；
- 不因测试失败自动开 successor。

若修复需要改变 core owner、Gate taxonomy、wrapper architecture、数据/费用/权限边界，返回 Planner/Critic。

### Pre-final Critic REVISE

不运行 final holdout。保持 development evidence，修 candidate/packet后重新 pre-final review；不消费 final fresh task。

### G1/G2/G3 final FAIL

- 记录 first failure；
- 不换题、不换 delta、不挑赢家；
- 本 final candidate该 Gate为 FAIL；
- 如要修 product，旧 final materials转 development regression；
- 新 candidate需要重新 pre-final review + fresh final evidence。

### G4 authorization/platform failure

未授权 Plugin Creator：
`WAITING_USER_PLUGIN_MUTATION_AUTHORIZATION`

Plugin Creator/Chat surface真实不可用：
`BLOCKED_G4_CHAT_SURFACE`

不得偷偷改用 MCP、公开 plugin、renderer-only或用户手工复制多轮流程。

### Renderer / dependency failure

如内容已经正确但 renderer缺依赖，按 renderer owner报告真实 `blocked_missing_dependency`/QA failure；不得把环境故障归成 Research Authoring科学失败，也不得换低质量 renderer冒充 PASS。

### Release/merge drift

本任务不 merge/release。后续 release closure若 current main/release已前进：
- 先比较 exact candidate与新 baseline；
- 不静默吸收 unrelated production changes；
- 若 candidate-owned内容需要改变，返回 Planner并重跑受影响 Gate；
- 无 candidate-owned change时，release owner按当时版本政策做独立 closure。

## 20. Authorization boundary for future approved Kickoff

若用户以后发送 execution-ready Critic逐字批准的 Kickoff，本次授权仅覆盖：

- exact `work/research-authoring--formal-production-authoring` branch/worktree创建/复用；
- approved 059 production source/profile/config/test/generated/doc candidate edits；
- umbrella pending mutation，仅在真实 Clear Writing +合法 GitHub Project surface存在时；
- deterministic tests/generator/CI；
- repo-safe development regression；
- task-local candidate install / fresh Codex replay；
- pre-final packet；
- G1–G3 final evidence；
- G4 wrapper archive/manifest准备（不含 live Plugin mutation）；
- results/private exports；
- task-owned commits；
- ordinary non-force push exact branch。

本 Kickoff**不授权**：
- Plugin Creator create/update；
- ChatGPT live account mutation；
- main merge；
- formal release/ref/tag/GitHub Release；
- paid API/model review；
- private/sensitive research data external upload；
- Bridge Kit change；
- Clear Writing/Presentations/renderer/Statistical Modeling产品改造；
- force push、remote remap、destructive Git；
- watcher/daemon/database/ledger/state machine。

达到 G4 live wrapper mutation 时必须请求一次新的 bounded user authorization，不能把本 Kickoff冒充该授权。

## 21. Executor stop points

### Stop A — pre-final Critic

development稳定、`C0` 与 final Gate packet冻结后，停止 final Gate执行并交独立 Critic。

最大 claim：

```text
PREFINAL_CANDIDATE_READY=YES
FINAL_GATES_NOT_STARTED=YES
```

### Stop B — G4 user authority

G1 Codex/G2/G3 evidence已完成，wrapper package/manifest绑定 `C` 后，如无 Plugin Creator授权：

```text
G4=WAITING_USER_PLUGIN_MUTATION_AUTHORIZATION
OVERALL_COMPLETE=NO
```

### Stop C — independent final Reviewer

所有允许执行的 final evidence与 G4 external evidence都完成后：

```text
FINAL_CANDIDATE_COMMIT=C
EVIDENCE_HEAD=E
G1_G4_READY_FOR_INDEPENDENT_REVIEW=YES
```

Executor不得自行声明 overall PASS。

## 22. Execution-ready Critic check

execution-ready Critic必须同时审本 Plan、同版 Goal、同版 Kickoff，并重点检查：

1. implementation surface是否足够实现 core而没有扩大 owner；
2. report/paper/litcite与 profile/generated consumer是否真实闭合；
3. candidate freeze -> pre-final Critic -> final Gates顺序是否符合 fresh evidence；
4. G2两阶段与 G3真实 manuscript final task selection是否不会复用开发样本；
5. G4 wrapper composition与一次用户授权边界是否真实可执行；
6. Executor/Reviewer owner是否清楚；
7. 0.3 version/changelog/README candidate与“未正式 release”是否不矛盾；
8. umbrella pending mutation是否没有被伪装成已同步；
9. rollback/stop语义是否不会让 final FAIL通过换题恢复成 PASS。

只有 Critic 对 Plan + Goal + Kickoff 同版 PASS，才能：

`READY_FOR_CODEX=YES`

否则保持：

`READY_FOR_CODEX=NO`
