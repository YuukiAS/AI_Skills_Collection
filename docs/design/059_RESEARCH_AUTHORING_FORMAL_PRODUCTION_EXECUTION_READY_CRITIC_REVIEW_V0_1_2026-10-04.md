# 059 Research Authoring 正式科研文档生产 — Execution-ready Critic Review v0.1

日期：2026-10-04  
角色：独立 Critic  
结果：PASS  
审查阶段：EXECUTION_READY_REVIEW

## Active Review Context

- target_repo: `YuukiAS/AI_Skills_Collection`
- target_plugin_or_domain: `research-writing / Research Authoring`
- human workflow number: `059`
- design_topic_or_task_key: `research-authoring--formal-production-authoring`
- source_branch_or_ref: `main`
- approved architecture: `docs/design/059_RESEARCH_AUTHORING_FORMAL_PRODUCTION_ARCHITECTURE_V0_3_PLANNER_PROPOSAL_2026-10-04.md`
- architecture commit: `42a86fcae336a139ed5def027b12f3cd9715dbaa`
- architecture Critic PASS: `docs/design/059_RESEARCH_AUTHORING_FORMAL_PRODUCTION_ARCHITECTURE_V0_3_CRITIC_REVIEW_2026-10-04.md`
- architecture Critic review commit: `a446b2ed3e0dc41ade9d6a3315091f9fbe36e084`
- Implementation Plan: `docs/design/059_RESEARCH_AUTHORING_FORMAL_PRODUCTION_IMPLEMENTATION_PLAN_V0_1_2026-10-04.md`
- Canonical Goal: `docs/goals/059_RESEARCH_AUTHORING_FORMAL_PRODUCTION_GOAL_V0_1.md`
- Kickoff Draft: `docs/operations/prompts/059_RESEARCH_AUTHORING_FORMAL_PRODUCTION_KICKOFF_V0_1.md`
- approved package commit: `706ff245c4421f5d5d9160eb821a7c762b1d4473`

本轮实际读取了 AI_Skills_Collection 当前 main、仓库角色/Capability Gate/维护看板/版本规则、approved v0.3 architecture + PASS、Plan/Goal/Kickoff、当前 Research Authoring source/profile/config/tests/generated route，以及 Bridge Kit 最新 main `9d60f4cf949c9da327a154001b13881cfd91233b` 的 AGENTS 与 branch/worktree/authorization 规则。当前 AI_Skills main 正好等于 package commit；package 之后没有新的 main drift。

## 核心判断

Plan、Goal 与 Kickoff 三者语义一致，并且把已经批准的 v0.3 架构落实为可执行合同，没有重新设计 owner、Gate taxonomy 或产品边界。

本 package 已满足 execution-ready 条件：

1. implementation 不只新增 `research-authoring-core`，还要求修改 profile、Marketplace source config、thin routes、routing tests 与 generated layer，能够真实接通 normal entry；
2. RA2 incremental contract 已变成明确执行步骤和受保护不变量，不是仅写一句原则；
3. development regression、pre-final candidate、final packet freeze、pre-final Critic、same-final-candidate final Gate 的顺序正确，已知 DII/CAT-TRACE regression 不会被重复包装成 fresh evidence；
4. G2 两阶段在 final Gate 前冻结 candidate/rubric/raw-input/delta，Phase 1 与 Phase 2 之间禁止 adaptive rescue；
5. G3 明确排除已用于产品调优的既有 CAT-TRACE workspace 自动充当 fresh holdout，并要求 pre-final 时冻结真正未用于调优的 manuscript task；
6. G4 不在当前 Kickoff 中预授权 Plugin Creator live mutation，未授权时只能进入 `WAITING_USER_PLUGIN_MUTATION_AUTHORIZATION`，不能用替代分发路线冒充完成；
7. Executor 不拥有 G1–G4 最终定性 PASS；独立 Reviewer 必须直接读取完整 input/source/output；
8. `research-writing 0.2 -> 0.3` 只作为未发布 final candidate identity；repository VERSION、main merge、formal release 均不在当前 Goal；
9. maintenance umbrella 仍如实标为未同步，并在 production edit 前按合法 Clear Writing / Issue / Project surface 处理或 fail closed；
10. branch/worktree 与普通非强制发布 effect 已由 approved Kickoff 精确绑定；当前人工 Planner -> Executor -> pre-final Critic -> final evidence -> Reviewer 流程不需要额外 Reviewed Handoff watcher/state machine。

## Bridge / branch / worktree

人工 workflow 与当前 Bridge/AI_Skills contract 相容。

Exact identity：

```text
task_key = research-authoring--formal-production-authoring
branch = work/research-authoring--formal-production-authoring
worktree = ../AI_Skills_Collection-research-authoring--formal-production-authoring
```

这是 ordinary task workflow，不是 Reviewed Handoff task，因此不需要为了形式强制改成 `reviewed/<task_key>` 或增加 watcher。

用户实际发送 approved Kickoff 后，exact local branch/worktree creation/reuse、task-owned commits 和 exact branch ordinary non-force publication 属于同一 bounded authorization。执行时仍须遵守 current Host/Bridge canonical command/transport fences；bounded publisher/normal path 失败不授权 raw/broader fallback，也不授权换 branch/worktree/clone。

## Implementation surface

Plan 明确要求 source-first：

- canonical `research-authoring-core`;
- report/paper/litcite 与 lower-level source boundary；
- `profiles/research-main.json`;
- `profiles/codex-research-writing.json`;
- `scripts/codex_marketplace_config.json`;
- `tests/test_research_writing_routing.py` 与必要 focused tests；
- generator-produced plugin/registry/catalog/provenance parity。

当前 generator 已有 aggregate coordinator-first 能力，因此 Plan 的“如果 current generator 无法表达，则返回 Planner/Critic，不另造第二 router”是合理 fail-closed，而不是已知实现 blocker。

当前 `AGENTS.md` 仍强制 production plugin refinement 使用 workflow-core + ai-skills-core + target domain plugin/skill；Kickoff 又要求执行开始读取 current AGENTS，因此这项仓库级强制条件继续生效，不能用只读 source 代替真实 required consumption。

## Final Gate order

批准的执行顺序为：

```text
implementation
-> deterministic validation + development regression
-> pre-final candidate C0
-> freeze G1-G4 inputs/rubrics/access/privacy/budget/allowlist
-> independent pre-final Critic
-> if PASS and no candidate-owned change: FINAL_CANDIDATE_COMMIT=C=C0
-> final G1-G4 evidence
-> independent Reviewer
```

C 后 candidate-owned content 不得变化。若变化，受影响 evidence stale，需新 candidate + risk-matched pre-final review + fresh final evidence。不得跨 candidate 拼 PASS。

## G1-G4 execution judgment

- G1：Codex normal-entry evidence 可先完成；Chat surface 对应证据必须等 G4 live wrapper 授权/安装后补齐。未补齐前不得给完整 G1 PASS。
- G2：Phase 1 raw evidence -> complete greenfield report -> independent Phase1 PASS；Phase 2 使用预冻结且 Phase1 不可见 delta。任一阶段 FAIL 即 G2 FAIL。
- G3：真实 manuscript task、venue authority、package subset、reviewer access 与 rubric 必须 pre-final 冻结；compile/file existence 仅辅助。
- G4：复用已通过 G2/G3 的内容任务；wrapper 只打包 exact C generated Research Authoring payload + same-commit writing-fidelity/chinese-prose/scientific-prose support，不复制 Clear Writing owner，也不带 renderer/MCP/connector/state。

## Authorization judgment

当前 approved Kickoff 只授权：

- exact branch/worktree；
- 059 candidate source/profile/config/tests/generated/docs/results/private-export work；
- deterministic tests/generator/CI；
- development regression；
- task-local candidate install/fresh Codex replay；
- pre-final packet；
- pre-final PASS 后 G1–G3 final evidence；
- G4 wrapper archive/manifest preparation；
- task-owned commits + exact branch ordinary non-force push。

明确不授权：

- Plugin Creator live create/update；
- live ChatGPT account mutation；
- main merge；
- formal release/tag/GitHub Release；
- paid API/model review；
- private/sensitive external upload；
- Bridge Kit mutation；
- other-domain redesign；
- destructive Git；
- automation/watcher/daemon/database/state machine。

达到 G4 live wrapper mutation 时，必须基于 exact C 再请求一次 bounded authorization。用户拒绝或尚未授权时，overall completion 必须保持 NO。

## Version / README / release

`research-writing 0.2 -> 0.3` 作为 exact branch final candidate 是合理的。当前 task 不修改 repository VERSION，不声称 0.3 已正式发布。后续 formal release closure 再按 then-current release baseline决定 repository PATCH。

README 预计因 version/capability row 变化而需要更新；必须真实调用 Clear Writing。不能调用时必须按 current repo contract 如实停止对应 reader-facing mutation，不能自行模仿。

## Maintenance umbrella

`RA4=CLOSED_FOR_ARCHITECTURE_STAGE` 不等于 live tracking 已同步。本 Plan 正确保留：

```text
UMBRELLA_ISSUE_CREATED=NO
PROJECT_FIELDS_SYNCED=NO
```

并要求 production edit 前机械刷新 pending mutation。不能合法执行 reader-facing tracking mutation时不得伪装完成，也不得要求用户手工维护。

## Final result

```text
RESULT=PASS
READY_FOR_CODEX=YES
APPROVED_ARCHITECTURE_PATH=docs/design/059_RESEARCH_AUTHORING_FORMAL_PRODUCTION_ARCHITECTURE_V0_3_PLANNER_PROPOSAL_2026-10-04.md
APPROVED_PLAN_PATH=docs/design/059_RESEARCH_AUTHORING_FORMAL_PRODUCTION_IMPLEMENTATION_PLAN_V0_1_2026-10-04.md
APPROVED_GOAL_PATH=docs/goals/059_RESEARCH_AUTHORING_FORMAL_PRODUCTION_GOAL_V0_1.md
APPROVED_KICKOFF_PATH=docs/operations/prompts/059_RESEARCH_AUTHORING_FORMAL_PRODUCTION_KICKOFF_V0_1.md
APPROVED_PACKAGE_COMMIT=706ff245c4421f5d5d9160eb821a7c762b1d4473
```

本 PASS 只批准用户发送同版 Kickoff 后开始 059 bounded implementation。它不授权 Plugin Creator live mutation、main merge、formal release、paid API 或其他被 Kickoff 明确排除的副作用。
