# 059 Research Authoring 正式科研文档生产架构 v0.2 — Critic 复核

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
- proposal_path_and_version: `docs/design/059_RESEARCH_AUTHORING_FORMAL_PRODUCTION_ARCHITECTURE_V0_2_PLANNER_PROPOSAL_2026-10-04.md`
- proposal_commit: `e4d62e5377295a2449e9ed5fffa2b92f1426dba8`
- prior review: `docs/design/059_RESEARCH_AUTHORING_FORMAL_PRODUCTION_ARCHITECTURE_V0_1_CRITIC_REVIEW_2026-10-04.md`
- prior result: `REVISE`
- stable blockers: `RA1`, `RA2`, `RA3`, `RA4`

本轮重新读取了最新 main 的仓库规则、Capability Gate policy、维护看板、Research Authoring 当前 source/profile/generated plugin、Clear Writing、renderer、Presentations research route，以及 CAT-TRACE / Distributed_Imaging_Inference 的真实文档证据。本轮只审架构，没有修改 production source、创建 Goal/Kickoff、调用 Plugin Creator mutation、启动 Executor、paid API 或 automation。

## 核心判断

v0.2 已经关闭 RA1、RA2，并在当前运行面约束下足以关闭 RA4 的架构阻塞。RA3 仍有一个很窄但真实的验收覆盖缺口：G2 只证明“已有好文档怎样安全增量修改”，没有直接证明 Research Authoring 能从原始项目证据新建一份合格的 advisor/research report。

这不是要求增加第五个 Gate，也不是要求再造一个独立任务族。最小修订是把 G2 变成同一科研文档语义能力的两阶段验收：先从真实原始证据生成完整书面科研报告，冻结该成稿；再对同一文档施加预先冻结的新 evidence/decision delta，验证 incremental contract。这样同时覆盖“从零组织科研文档”和“长期维护不漂移”，而不增加控制层或用户回归负担。

因此本轮仍为 REVISE，但只保留 RA3。RA1、RA2、RA4 不得在下一轮无新证据重开。

## RA1 — CLOSED

### Requirement

所有真正 document-producing 的科研文档请求必须消费同一个跨 ChatGPT/Codex 的 Research Authoring 文档级合同，不能让 `scientific-writing`、`literature-review` 等下层 skill 成为旁路。

### Direct evidence

当前 production 的确存在旁路风险：`profiles/research-main.json` 直接安装 `scientific-writing`、`paper-workflow-orchestrator`、`literature-review` 等；generated Research Authoring plugin 仍是 `report / paper / litcite` 三个入口。

v0.2 已冻结：
- `skills/writing/research/research-authoring-core/` 作为唯一 canonical orchestration skill；
- document-producing request 必须先消费 core；
- `report` / `paper` 继续作为薄 family route；
- `litcite` 明确拆成 document-producing 与 support-only 两支；
- “写 Methods / Discussion / related work / research update / 修改现有报告”等属于 document production；
- DOI 核验、paper lookup、BibTeX/Zotero、纯语言润色、render-only、PPT/Beamer 等不强制进入 core；
- ChatGPT wrapper 与 Codex `research-main` 绑定同一 canonical core commit；
- G1 明确把“正例直接落到下层 skill、未消费 core”定义为 FAIL。

### Judgment

这已经把 v0.1 的“理念上应该先做文档计划”变成了可实现、可验收的产品合同。新增一个共享 orchestration skill 是最低充分复杂度：单纯共享 reference 仍不能解决自然入口绕过，Chat-specific skill 又会制造双源。

实现阶段不能只把 core 路径加入 profile 就宣称完成；必须同时让 lower-level descriptions / aggregate routes / profile routing 真正服从 core 的 document-producing 边界，并由 G1 从 normal entry 直接证明。这是实现细节与 Gate evidence，不再是架构 blocker。

RA1 = CLOSED.

## RA2 — CLOSED

### Requirement

已有科研文档的更新不能默认全文重写；需要保护未受影响的正文、记号、主张强度、引用、表图身份和交叉引用，同时允许真正相关的非连续单元联动修改。

### Direct evidence

v0.2 已冻结：
- canonical baseline + new evidence/decision/reviewer delta；
- affected claims / section jobs；
- minimal dependency closure；
- local patch；
- protected invariants；
- diff-based QA；
- 只有用户明确要求、document spine 失效、系统性结构失败或 venue/project authority 改变时才扩大重构；
- 不新增 database / ledger / state machine。

`minimal dependency closure` 允许一个新结果同时更新 Results、Abstract、Discussion、caption，而不把不相关 Introduction 一并改写；protected invariants 也都带有“除非 delta 真正要求变化”的条件，因此不会把科学修订冻结死。

CAT-TRACE 的模块化演变记录与 DII bounded-result-slot 经验都直接支持这种维护方式。

RA2 = CLOSED.

## RA3 — REMAINS BLOCKING

### Requirement

`PLUGIN_CAPABILITY_GATE_POLICY.md` 要求 Gate Matrix 覆盖插件真正声称的主要能力、重要任务族、完整产物、normal entry、fresh evidence 和真实定性质量，不能让某类核心能力仅靠邻近 Gate 间接推断。

Research Authoring 明确声称能“把真实研究证据组织成可交给导师的科研文档”，并且 report family 是正式主要文档族，而不仅是 existing-document editor。

### Direct evidence

v0.2 的 G1 只证明路由与边界；它明确“不证明写得好”。

G2 的 Normal entry / real input 是：

> 一份真实 DII/CAT-TRACE 风格 advisor/research-update 或 research-evolution 文档 + 冻结 baseline + 新 evidence/decision delta

G2 的能力声明也明确是“证明已有科研文档可以按 evidence delta 安全更新”。

G3 证明的是 manuscript package；它不能替代 report-family 的 reader-first 组织能力，因为论文与导师书面报告的 audience、结构与典型失败不同。当前真实 DII regressions 正是 report-family 的“运行日志化、方法/数据背景不足、内部 provenance 泄漏、bounded result”等问题。

因此当前 final Gate 可以出现一种假 PASS：给它一份已经很好、已经由人工/旧流程组织好的 advisor report，只让新系统做一次局部增量 patch；G2 全通过，但系统从未证明自己能从原始 repo evidence / notes / results 中独立建立 reader-first report spine。这会漏掉用户最直接的自然请求：“把这几天研究整理成给老师看的报告”。

这不是新产品方向，而是 RA3 原本要求的“advisor/research-update 文档语义质量”在 v0.2 Matrix 中被增量测试收窄后暴露出的 acceptance loophole。

### Causal risk

实现可以针对 incremental diff 做得非常保守而通过 G2，同时继续在 greenfield advisor report 上：
- 按执行时间线写；
- 过早进入项目结果；
- 不先解释方法/数据；
- 把内部状态、repo provenance 或运行细节写入正文；
- 不能从原始证据决定哪些 claim / table / figure / formula 值得进入主文。

这会让“正式科研文档生产能力”在最常见的 report 新建场景上没有直接 final-candidate 证据。

### Minimum closure

不增加第五个 Gate，也不新增第四类用户验收对象。

只修改 G2，使它用一个预先冻结的真实 report-family 任务同时证明两个阶段：

1. **Greenfield authoring phase**
   - 输入是真实项目的原始 source/evidence/notes/results，而不是已经整理好的 reader-facing report；
   - 从 normal entry（例如“把这几天研究整理成给老师看的报告”）生成完整 advisor/research-update 或 research-evolution 文档；
   - Reviewer 直接审完整 source/evidence 与完整 candidate；
   - 明确检查 reader-first structure、方法/数据 orientation、claim/evidence、内部流程抑制、表图公式职责、reader-facing references/provenance 边界和 Clear Writing handoff。

2. **Incremental phase**
   - 将第一阶段通过的成稿冻结为 baseline；
   - 在任务开始前就预先冻结一份后续 evidence/decision delta（或者使用另一个不会被开发调优的等价真实 delta）；
   - 按 RA2 contract 更新 minimal dependency closure；
   - 直接审 baseline、delta、candidate、diff 和 protected invariants。

最终 candidate 与 Reviewer 标准在这两个阶段前冻结；第一阶段或第二阶段失败都使 G2 FAIL。不能在第一阶段看到问题后修改产品，再把第二阶段仍称同一 fresh final Gate。

这样 G2 仍然只证明一个能力族：**科研文档语义组织 + 其长期增量维护**；无需 split/new Gate，也不会增加用户多轮测试负担。

owner: Planner

RA3 = OPEN.

## RA4 — CLOSED FOR THIS ARCHITECTURE STAGE

### Requirement

059 promotion 需要一个真实 top-level maintenance owner，不能把 #20–#29 中的窄 Issue 冒充 umbrella；但仓库同时要求 reader-facing tracking Issue / Project copy 在 mutation 前真实调用 Clear Writing，并为无 Project mutation surface 定义了 pending-mutation fallback。

### Direct evidence

最新 `AI_SKILLS_MAINTENANCE_BOARD.md` 明确规定：
- tracking Issue / Project copy 在 mutation 前必须真实调用 Clear Writing；
- runtime 不能调用时，停止 reader-facing mutation 并报告 `CLEAR_WRITING_UNAVAILABLE`；
- 无 Project mutation surface 时，Critic/Planner 记录 exact pending Project mutation，不要求用户手工维护。

本轮实际工具面：
- 可以写 GitHub Issue；
- 没有 GitHub Project field mutation surface；
- 没有可真实调用的 Clear Writing domain skill/tool；
- Plugin discovery 也没有提供可在本轮直接执行 `writing-style` / Clear Writing 的调用入口。

v0.2 第 10 节已经冻结了 Issue title/body、labels、Area、Status、current anchor、next action、TODO umbrella entry、三个 UNASSIGNED 条目的 merge/backlink 规则，以及“已有 #20–#29 不重绑”。

### Judgment

要求 Planner 此时强行创建 Issue 会直接违反当前 canonical board 的 Clear Writing 前置规则；要求用户手工创建/拖 Project 也违反 no-tool fallback。

因此对 **PRE_IMPLEMENTATION_ARCHITECTURE_REVIEW**，RA4 的设计归属与 exact pending mutation 已足以关闭架构 blocker。live mutation 仍然没有执行，也不得声称已同步；它必须由下一个同时具备 Clear Writing invocation 和 GitHub Project mutation/maintenance 能力的合法 surface 机械应用。

这个裁定是对 v0.1 RA4 最小关闭条件的运行面修正，不表示 tracking requirement 被取消。execution package 形成前，Planner 必须重新核对 pending mutation 是否已执行；若仍未执行，应在 execution-ready review 中如实保留为治理前置，而不是伪装成 DONE。

RA4 = CLOSED_FOR_ARCHITECTURE_STAGE.

## Gate Matrix 其余判断

- G1 与 G4 不重复：G1 证明自然入口和 owner boundary；G4 证明同一 canonical candidate 的 ChatGPT→Codex 实际生产链和最终 artifact。
- G3 与 G4 不重复：G3 证明 manuscript package 的科研/跨文件正确性；G4 证明跨表面交接和真实生产。
- G3 的“按需 package”设计正确，避免固定 sidecar 文件爆炸。
- fresh generalization、should-not-change、same-final-candidate 放在 G1–G4 内部而不是另建 Gate，符合 Gate lifecycle policy。
- G4 复用已经通过 G2/G3 的真实内容任务是合理的；它证明 integration，不需要为了数量再造一个内容样本。
- 所有 Gate 都要求同一 final candidate；机械 tests/schema/file existence/render success 只能作为辅助证据，不能单独 PASS。

唯一阻塞是 G2 还必须直接覆盖 greenfield report authoring。

## 独立外部核查

重新核对 OpenAI 当前官方资料后，没有发现会推翻 v0.2 双表面路线的新事实：

- OpenAI Help 的 Skills in ChatGPT 说明，skill 安装后 ChatGPT 可以在有帮助时自动使用一个或多个 skill；ChatGPT 与 Codex 的 availability / installation / syncing 可能因 surface 而不同。
- OpenAI Developers 的 Plugin packaging / architecture 文档明确支持 skills-only plugin；MCP 只在需要额外工具、外部服务、认证或自有基础设施时才需要。
- Build skills 文档明确要求使用 direct、indirect、should-not-activate 和 edge cases 同时测试 activation 与 output quality。

这支持 v0.2 的：
`one canonical authoring core -> skills-only Chat wrapper + Codex profile`
以及 G1 的 normal-entry + near-miss 设计；不支持为 Research Authoring 增加 MCP 或 Chat-specific canonical source。

## 本轮结论

`RESULT = REVISE`

- RA1: CLOSED
- RA2: CLOSED
- RA3: OPEN — 仅需补 G2 greenfield + incremental 两阶段 final evidence
- RA4: CLOSED_FOR_ARCHITECTURE_STAGE
- 新 blocker: NONE

本结论只针对 `docs/design/059_RESEARCH_AUTHORING_FORMAL_PRODUCTION_ARCHITECTURE_V0_2_PLANNER_PROPOSAL_2026-10-04.md` at `e4d62e5377295a2449e9ed5fffa2b92f1426dba8` 的 PRE_IMPLEMENTATION_ARCHITECTURE_REVIEW。

不授权 production implementation、Goal/Kickoff、Plugin Creator mutation、release、merge、paid API 或 automation。下一轮只需 Planner 提交最小 v0.3（或同等版本递增）修订关闭 RA3；不得无新证据重开 RA1、RA2、RA4。
