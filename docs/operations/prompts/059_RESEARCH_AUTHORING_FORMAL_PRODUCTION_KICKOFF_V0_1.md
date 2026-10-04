# 059 Research Authoring 正式科研文档生产 — Kickoff Draft v0.1

状态：DRAFT_FOR_EXECUTION_READY_CRITIC_REVIEW / NOT_AUTHORIZED  
日期：2026-10-04

只有独立 Critic 对以下同版 execution package 给出 execution-ready PASS，并逐字返回本 Kickoff 后，用户实际发送该批准正文才形成 implementation authorization：

- Architecture Proposal：
  `docs/design/059_RESEARCH_AUTHORING_FORMAL_PRODUCTION_ARCHITECTURE_V0_3_PLANNER_PROPOSAL_2026-10-04.md`
- Architecture Critic PASS：
  `docs/design/059_RESEARCH_AUTHORING_FORMAL_PRODUCTION_ARCHITECTURE_V0_3_CRITIC_REVIEW_2026-10-04.md`
- Implementation Plan：
  `docs/design/059_RESEARCH_AUTHORING_FORMAL_PRODUCTION_IMPLEMENTATION_PLAN_V0_1_2026-10-04.md`
- Canonical Goal：
  `docs/goals/059_RESEARCH_AUTHORING_FORMAL_PRODUCTION_GOAL_V0_1.md`
- 本 Kickoff：
  `docs/operations/prompts/059_RESEARCH_AUTHORING_FORMAL_PRODUCTION_KICKOFF_V0_1.md`

## Kickoff 正文

执行 `research-authoring--formal-production-authoring`，只实现已批准的 Research Authoring v0.3 架构和 Implementation Plan v0.1，不重新设计产品、owner 或 G1–G4。

Repository：

`YuukiAS/AI_Skills_Collection`

Exact branch：

`work/research-authoring--formal-production-authoring`

Exact task-owned worktree：

`../AI_Skills_Collection-research-authoring--formal-production-authoring`

我明确授权本任务创建/复用上述唯一 exact branch/worktree，并在该 branch 进行本 Goal 明确允许的 task-owned edits、commits 与 ordinary non-force push。若现有 worktree/branch identity 不匹配，停止，不换路径、branch、clone 或 remote。

开始前：

1. 在 canonical checkout 核实 repo/origin/clean ownership；
2. `git fetch origin main`；
3. 确认 current `origin/main` 包含 execution-ready Critic 批准的同版 package；
4. 读取 current `AGENTS.md`、版本/Capability Gate/maintenance policy、approved v0.3 architecture、Implementation Plan v0.1 与 Canonical Goal v0.1；
5. 按 Plan §3.1 处理或如实阻塞 umbrella maintenance pending mutation；
6. 读取 current Research Authoring source/profile/Marketplace config/tests；不要按旧聊天猜实现。

实现范围：

- 新增 canonical `skills/writing/research/research-authoring-core/`；
- 让 report / paper / litcite 的 document-producing normal entry 先消费 core；
- 保持 lookup/citation/BibTeX/Zotero/纯局部语言润色/render-only/PPT/普通问答的 approved support-only boundary；
- 落实 RA2 incremental authoring contract；
- 更新 `research-main`、`codex-research-writing`、Marketplace source config、必要 tests 与 generated layer；
- 保持 Statistical Modeling、Clear Writing、Presentations、renderer owner不变；
- 开发期回放已知 DII/CAT-TRACE regressions，但不把它们伪装成 final fresh evidence。

版本与候选：

- 本 task 的 exact final candidate 将 `research-writing 0.2 -> 0.3`；
- maturity 保持 `unclassified`；
- 本 task 不改 repository `VERSION`；
- 同步 plugin changelog、root CHANGELOG Unreleased、README 与 generated parity；
- README 有用户可见改动时必须真实调用 installed Clear Writing。

严格按 Plan：

```text
implementation
-> deterministic validation + development regression
-> pre-final candidate C0 + frozen G1–G4 inputs/rubrics
-> STOP for independent pre-final Critic
-> Critic PASS with no candidate-owned changes
-> FINAL_CANDIDATE_COMMIT=C
-> final Gate evidence
-> independent Reviewer
```

不得在 pre-final Critic PASS 前消费 final fresh G1–G4 evidence。

G2 必须是批准的同一真实 report-family 两阶段任务：
- Phase 1 raw evidence -> greenfield complete report；
- independent Phase 1 PASS；
- Phase 2 使用预冻结且 Phase 1 不可见的 delta做 incremental update；
- 任一阶段失败 => G2 FAIL；
- Phase间不得改 product/rubric/task/delta。

G3 必须使用 pre-final 时已经冻结、未用于 059 产品调优的真实 manuscript task；不得执行后挑赢家。

G4：
- 只准备 exact PRIVATE / USER-scope / skills-only `research-authoring` wrapper composition/archive/manifest；
- wrapper Research Authoring payload绑定 exact final candidate；
- Clear Writing support只取同一 canonical commit 的 `writing-fidelity`、`chinese-prose`、`scientific-prose`；
- 不打包 renderer runtime、MCP、connector、database、watcher或state；
- **本 Kickoff 不授权 Plugin Creator create/update，也不授权 live ChatGPT account mutation。**
- 到达 live wrapper mutation时停止并请求一次新的 bounded user authorization；未授权不得换分发路线。

本 Kickoff授权：
- exact branch/worktree；
- 059 source/profile/config/tests/generated/docs/results/private-export candidate工作；
- deterministic tests/generator/CI；
- repo-safe development regression；
- exact candidate task-local install/fresh Codex replay；
- pre-final packet；
- pre-final Critic前的准备工作；
- Critic PASS 后 G1–G3 final evidence；
- G4 wrapper package/manifest准备；
- task-owned commits；
- ordinary non-force push exact branch。

本 Kickoff不授权：
- Plugin Creator live mutation；
- ChatGPT live account mutation；
- main merge；
- `release` ref/tag/GitHub Release/formal publication；
- paid API/model review；
- private/sensitive research data external upload；
- Bridge Kit修改；
- Clear Writing/Presentations/renderer/Statistical Modeling产品改造；
- force push、remote remap、reset/clean/restore他人工作；
- watcher、daemon、automation、database、ledger、state machine。

必须把所有 AI_Skills 产物留在 repo；大/私有产物放 `private/exports/research-authoring--formal-production-authoring/`，不要只留 `/tmp`。

如果实现暴露 approved architecture/Gate/owner 不成立，或需要扩大 provider、数据、权限、费用、release/merge范围，停止并返回 Planner/Critic，不要自行补设计。

首次强制停止点：

当 development candidate、deterministic validation、代表性开发产物与 frozen G1–G4 final packet 已准备好后，写完整 pre-final evidence 并停止：

```text
PREFINAL_CANDIDATE_READY=YES
FINAL_GATES_NOT_STARTED=YES
NEXT_HANDOFF=CRITIC
```

不要越过该点直接跑 final holdout。
