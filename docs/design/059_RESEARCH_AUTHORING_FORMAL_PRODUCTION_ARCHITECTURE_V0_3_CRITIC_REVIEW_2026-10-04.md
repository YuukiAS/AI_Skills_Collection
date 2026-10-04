# 059 Research Authoring 正式科研文档生产架构 v0.3 — Critic 窄范围复核

日期：2026-10-04  
角色：独立 Critic  
结果：PASS  
审查阶段：PRE_IMPLEMENTATION_ARCHITECTURE_REVIEW

## Active Review Context

- target_repo: `YuukiAS/AI_Skills_Collection`
- target_plugin_or_domain: `research-writing / Research Authoring`
- human workflow number: `059`
- design_topic_or_task_key: `research-authoring--formal-production-authoring`
- source_branch_or_ref: `main`
- reviewed proposal: `docs/design/059_RESEARCH_AUTHORING_FORMAL_PRODUCTION_ARCHITECTURE_V0_3_PLANNER_PROPOSAL_2026-10-04.md`
- proposal commit: `42a86fcae336a139ed5def027b12f3cd9715dbaa`
- prior Critic review: `docs/design/059_RESEARCH_AUTHORING_FORMAL_PRODUCTION_ARCHITECTURE_V0_2_CRITIC_REVIEW_2026-10-04.md`
- prior Critic result: `REVISE`
- narrow review scope: RA3 v0.3 change and its impact on G1 / G3 / G4

本轮按用户要求只复核 RA3。重新读取了最新 main、仓库角色/门禁/维护规则、v0.2 Critic review 与 v0.3 Proposal。没有发现需要重新打开 RA1、RA2 或 RA4 的新事实。v0.2 到 v0.3 之间只新增 v0.2 Critic review 与 v0.3 Proposal，没有 production source、routing、profile 或 plugin runtime 变化。

## 核心判断

v0.3 已关闭 RA3。

G2 现在不再允许“拿一份已经整理好的好报告做局部修改”来冒充 Research Authoring 的完整能力。它要求同一个最终候选在同一个预先冻结的真实 report-family 任务上连续完成：

1. 从原始科研证据独立建立完整、面向读者的科研文档；
2. 再用预先冻结且第一阶段不可见的 evidence/decision delta 对同一文档做增量更新。

两个阶段共同证明“科研文档语义组织与长期增量维护”这一能力族，仍然适合保留为一个 G2，不需要增加第五个 Gate，也不需要拆成两个 Gate。

## RA3 — CLOSED

### 1. Greenfield authoring 已被直接验证

v0.3 的 Phase 1 输入明确限定为真实 repo evidence、notes、results、figures、prior decisions 和必要 literature/source evidence，并明确禁止把已经整理好的 reader-facing advisor report / research update 当主要输入。

正常入口类似“把这几天研究整理成给老师看的报告”。最终必须生成完整 advisor report、research update 或 research-evolution document，Reviewer 必须直接看到原始 evidence/input scope 与完整成稿。

因此 G2 已经直接覆盖 Research Authoring 最核心的 report-family greenfield authoring，不再依赖“已有好文档”。

### 2. Greenfield + incremental 保持为一个合理 Gate

两个阶段共享：
- 同一个 report-family 任务；
- 同一个 Research Authoring core；
- 同一个最终产品候选；
- 同一套科研文档语义合同；
- 同一类完整用户 artifact。

Phase 1 证明能从原始科研材料建立正确的文档语义和读者结构；Phase 2 证明同一文档语义在新增真实证据到达后可以持续维护而不漂移。两者是同一个长期科研文档能力的前后阶段，不是两个独立产品入口或不同 owner。

因此保留一个两阶段 G2 比增加 G5 更简洁，也没有掩盖不同失败：两阶段的 FAIL 条件已分别明确写出。

### 3. Fresh final evidence 的冻结顺序足够

v0.3 在整个 final G2 开始前同时冻结：
- final product candidate；
- Reviewer rubric；
- Phase 1 raw-evidence input scope；
- Phase 2 evidence/decision delta identity。

同时明确：
- Phase 1 输入必须排除 Phase 2 delta；
- Phase 1 与 Phase 2 之间不得改 product、rubric、task 或 delta；
- 任一阶段 FAIL 即 G2 FAIL；
- 看过任一阶段输出后若修改产品或评审标准，当前 final G2 终止；
- 旧材料之后只能进入 development regression，不能继续充当同一 final candidate 的 fresh evidence。

这已经关闭了“看结果后调产品，再继续把同一批材料称为 fresh final evidence”的适应性调优漏洞。

### 4. Phase 1 的直接证据充分

Phase 1 的完整验收对象包括：
- 原始 source/evidence scope；
- 完整 reader-facing report-family 成稿；
- 必要 source/claim anchors。

独立 Reviewer 必须直接检查：
- reader-first scientific structure；
- scientific question / decision 是否主导文档；
- 方法与数据背景是否自包含；
- claim/evidence boundary；
- 未完成、条件性、有限证据的强度；
- runtime / audit / job / implementation chronology 是否被过滤；
- table / figure / formula 的科学职责；
- reader-facing references 与 internal provenance 的分离；
- Clear Writing 后科学语义是否保持。

FAIL 与 should-not-change 也直接绑定科学事实、数字、公式含义、引用权威、证据强度和 unfinished/negative/conditional state。机械字符串检查或 diff 大小不能单独 PASS。

### 5. Phase 2 足以执行 RA2

Phase 2 明确使用已关闭的 RA2 合同：

`delta -> affected claims -> affected section jobs -> dependent figures/tables/formulas/citations -> minimal dependency closure -> local update`

Reviewer 直接比较 frozen Phase 1 baseline、预冻结 delta、Phase 2 candidate 与 baseline→candidate diff，并保护未受影响正文、notation、claim strength、citation keys、equation/theorem labels、figure/table identity、cross references、limitations/uncertainty 和 venue/project-required identity。

因此 RA2 没有被削弱，也不需要重开。

## 对 G1 / G3 / G4 的影响

### G1 未重复

G1 仍只证明自然请求是否进入正确 owner / route，以及 near-miss 是否避免误触发。它明确不证明成稿质量。

G2 证明的是 Research Authoring 进入之后能否真正建立和长期维护科研文档。二者证据与失败语义不同。

### G3 未重复

G3 仍证明正式 manuscript production package 的按需文件选择与跨文件一致性，包括 manuscript、supplement、bibliography、figures/tables、声明和 venue-required artifacts。

G2 只验证 report-family 的文档语义组织与增量维护，不承担 manuscript submission package 的跨文件生产责任。

### G4 未重复

G4 仍证明同一 canonical candidate 在 ChatGPT -> Codex 的真实 production chain、handoff identity、renderer route 与最终真实 artifact 上成立。

G2 证明内容语义能力；G4 证明跨表面集成与最终生产。G4 可以复用已经通过 G2/G3 的内容任务，但不能用集成成功替代 G2/G3 的内容质量证据。

## 最终状态

```text
RA1 = CLOSED
RA2 = CLOSED
RA3 = CLOSED
RA4 = CLOSED_FOR_ARCHITECTURE_STAGE
```

G1、G3、G4 的职责未被 v0.3 修改。没有新增 blocker。

本 PASS 只证明 `docs/design/059_RESEARCH_AUTHORING_FORMAL_PRODUCTION_ARCHITECTURE_V0_3_PLANNER_PROPOSAL_2026-10-04.md` at `42a86fcae336a139ed5def027b12f3cd9715dbaa` 在 PRE_IMPLEMENTATION_ARCHITECTURE_REVIEW 阶段通过。

本 PASS 不授权：
- production implementation；
- Goal/Kickoff 执行；
- Plugin Creator mutation；
- release / merge；
- paid API；
- automation。

live umbrella Issue / Project mutation 仍未执行，不得声称已同步。v0.3 保留的 exact pending mutation 在真正执行前应机械刷新当前 proposal/review locator 与 next action；这不改变已通过的架构语义，也不要求用户手工维护。

## 下一步

按照 Critic Role Contract，设计阶段 PASS 后返回 Planner。Planner 应基于同一个已通过的 v0.3 架构准备同版本 execution package：

1. Proposal / Plan；
2. Canonical Goal；
3. Kickoff Draft。

execution package 必须把 G1–G4、同一 final candidate、fresh evidence、用户不承担多轮回归、ChatGPT/Codex 双表面、Clear Writing/renderer/Presentations 边界及恢复条件落实为可执行合同。

完成后再送 execution-ready Critic。不得直接从本次架构 PASS 跳到 Codex implementation。
