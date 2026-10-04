# 059 Research Authoring 正式科研文档生产 — Canonical Goal v0.1

状态：DRAFT_FOR_EXECUTION_READY_CRITIC_REVIEW / NOT_EXECUTION_AUTHORIZATION  
日期：2026-10-04  
Repository：`YuukiAS/AI_Skills_Collection`  
Task key：`research-authoring--formal-production-authoring`

批准的架构：

- `docs/design/059_RESEARCH_AUTHORING_FORMAL_PRODUCTION_ARCHITECTURE_V0_3_PLANNER_PROPOSAL_2026-10-04.md`
- Proposal commit：`42a86fcae336a139ed5def027b12f3cd9715dbaa`
- Critic PASS：`docs/design/059_RESEARCH_AUTHORING_FORMAL_PRODUCTION_ARCHITECTURE_V0_3_CRITIC_REVIEW_2026-10-04.md`
- Critic review commit：`a446b2ed3e0dc41ade9d6a3315091f9fbe36e084`

执行 Plan：

`docs/design/059_RESEARCH_AUTHORING_FORMAL_PRODUCTION_IMPLEMENTATION_PLAN_V0_1_2026-10-04.md`

Kickoff Draft：

`docs/operations/prompts/059_RESEARCH_AUTHORING_FORMAL_PRODUCTION_KICKOFF_V0_1.md`

本 Goal 不重新设计 Research Authoring；出现架构、Gate taxonomy、owner、权限或最终证据语义冲突时返回 Planner/Critic。

## 1. Goal

实现一个可作为 `research-writing 0.3` release candidate 的 Research Authoring 正式科研文档生产能力，使：

1. ChatGPT 与 Codex 共享同一个 canonical `research-authoring-core`；
2. 真正 document-producing 的 report / paper / literature requests 不能绕过 core；
3. support-only lookup/citation/BibTeX/Zotero/纯语言润色/render-only/PPT/普通问答保持原 owner；
4. 已有科研文档支持最小依赖闭包增量更新；
5. Research Authoring 与 Clear Writing、Presentations、Statistical Modeling、renderer 的责任边界保持不变；
6. G1–G4 在同一个 exact final candidate 上得到真实完整证据；
7. 当前任务结束时只形成未发布的 `research-writing 0.3` final candidate，不 merge main、不推进 formal release。

## 2. Exact execution identity

```text
branch = work/research-authoring--formal-production-authoring
worktree = ../AI_Skills_Collection-research-authoring--formal-production-authoring
task_key = research-authoring--formal-production-authoring
```

不得换 branch、worktree、clone 或 task key 规避失败。

## 3. Required implementation

### 3.1 Canonical core

新增：

```text
skills/writing/research/research-authoring-core/SKILL.md
```

它必须拥有：

- audience / document purpose；
- source authority / evidence boundary；
- document family；
- claim-evidence spine；
- section jobs；
- main text / appendix / provenance；
- table / figure / formula scientific roles；
- citation authority；
- incremental edit scope；
- downstream owner route；
- final document-level scientific QA。

不得拥有统计方法设计、通用语言规则、slide/deck、字体/PDF mechanics。

### 3.2 Thin routes

使：

- `research-reporting`
- `paper-workflow-orchestrator`
- `scientific-writing`
- `literature-review`
- citation / lookup support boundaries

符合批准的 document-producing vs support-only contract。

`report / paper / litcite` 用户入口保持，不创建 Chat-specific canonical Skill。

### 3.3 Real consumers

必须实际更新并验证：

- `profiles/research-main.json`
- `profiles/codex-research-writing.json`
- `scripts/codex_marketplace_config.json`
- generated Research Authoring plugin
- routing/profile tests
- required registry/catalog/provenance/generated parity。

不能只创建 core 文件而不接正常入口。

### 3.4 Incremental authoring

落实：

```text
canonical document + delta
-> affected claims
-> affected section jobs
-> dependent figures/tables/formulas/citations
-> minimal dependency closure
-> local patch
-> diff QA
```

保护未受影响的 accepted text、notation、claim strength、claim/evidence、citation keys、equation/theorem labels、figure/table identity、cross refs、limitations/uncertainty 和 venue/project identity。

不新增 database、ledger、state machine 或 mandatory sidecar system。

## 4. Development regressions

开发期允许反复使用已知 DII/CAT-TRACE 真实失败和 current routing regressions，但这些材料不能在修产品后冒充 final fresh evidence。

至少保护：

- advisor report 不按运行/审计时间线组织；
- 方法/数据 background 足够；
- bounded result slot；
- 双语文档语义一致但不逐句翻译；
- 公式职责；
- reader-facing references 与 internal provenance 分离；
- CAT-TRACE 按模块增量更新；
- report/paper/litcite support-only near-miss；
- existing formal PDF handoff 不退化。

## 5. Candidate freeze

完成 source、tests、profiles/config、generated parity、README/changelog/plugin version candidate 与 deterministic validation 后，形成 exact pre-final candidate commit `C0`。

在 final Gate 前冻结：

- G1 positive/near-miss cases；
- G2 real two-phase report task；
- G2 Phase 1 raw input scope；
- G2 Phase 2 delta；
- G2 rubric；
- G3 real manuscript task；
- G3 venue/project authority；
- G3 package subset/rubric；
- G4 reused task；
- G4 wrapper composition；
- G4 handoff/final artifact rubric；
- reviewer access/privacy route；
- should-not-change bank。

独立 pre-final Critic PASS 且不要求 candidate-owned changes 时：

```text
FINAL_CANDIDATE_COMMIT=C=C0
```

之后 candidate-owned content不得变化。

## 6. Capability Gates

### G1 — 自然入口与边界

正例至少覆盖：
- Methods；
- research update；
- related work；
- existing document revision。

near-miss 至少覆盖：
- citation verify；
- paper lookup；
- 单句内容不变润色；
- README/邮件；
- PPT/Beamer；
- render-only；
- 普通科研问答。

必须是 natural unnamed normal entry；static trigger/description/test 不能单独 PASS。

### G2 — 科研文档语义组织与长期增量维护

使用同一个真实 report-family task 两阶段。

Phase 1：
- 从原始 repo evidence/notes/results/figures/prior decisions 生成完整 reader-facing report-family 文档；
- 不得以已经整理好的 reader-facing report 为主要输入；
- Reviewer 直接读原始证据与完整成稿。

Phase 2：
- Phase 1 PASS 成稿冻结为 baseline；
- 使用 final G2 开始前已冻结且 Phase 1 不可见的 delta；
- 按 minimal dependency closure更新同一文档；
- Reviewer直接比较 baseline、delta、candidate、diff。

final candidate、rubric、Phase 1 input scope、Phase 2 delta在 G2 开始前全部冻结。任一阶段失败 => G2 FAIL；看到 final 输出后修改 product/rubric/task/delta => 当前 final G2 终止。

### G3 — 正式 manuscript package

冻结一个未用于本任务产品调优的真实 manuscript task及 venue/project authority。

按任务只生成实际需要的：

```text
manuscript / supplement / bibliography / figures / tables / captions /
author metadata / contributions / declarations / reporting checklist /
submission manifest / cover letter / reviewer response
```

的子集。

必须检查跨文件科学、引用、label、表图和 venue consistency。compile/file existence不能单独 PASS。

### G4 — ChatGPT + Codex 双表面生产

G4 复用 G2 或 G3 已通过的真实内容任务。

未来 ChatGPT wrapper：

```text
name = research-authoring
scope = USER
discoverability = PRIVATE
skills-only = YES
initial wrapper version = 0.1.0
```

wrapper Research Authoring payload必须绑定 exact `C` generated plugin skills，额外 Clear Writing support只可取同一 canonical commit 的：

- `writing-fidelity`
- `chinese-prose`
- `scientific-prose`

不得加入 renderer runtime、MCP、connector、database、watcher、state machine。

本 Goal不授权 live Plugin Creator mutation。达到 wrapper live mutation前必须取得一次新的 bounded user authorization。

Chat -> Codex handoff不得丢：
- audience / purpose；
- evidence authority；
- edit scope；
- table/figure/formula role；
- citation authority；
- venue/project authority；
- production/renderer contract；
- final artifact；
- final scientific QA requirement。

Codex必须使用 exact `C` 的 `research-main` candidate生产最终 artifact；不能只调用 renderer 绕过 Research Authoring。

## 7. Independent review

Executor负责 candidate与 evidence packet，不拥有 G1–G4 最终 qualitative PASS。

独立 Reviewer必须按 pre-final 冻结 rubric直接审完整 input/source/output。

G2 Phase 1 需要中间独立判断：
- `PHASE1=PASS` 才允许 Phase 2；
- 不允许 Phase 1 后修改 product/rubric。

最终 Reviewer写：
- G1 PASS/FAIL；
- G2 PASS/FAIL；
- G3 PASS/FAIL；
- G4 PASS/FAIL；
- `IMPLEMENTATION_OVERALL=PASS|REVISE`。

所有 PASS必须绑定同一 `FINAL_CANDIDATE_COMMIT=C`。

## 8. Candidate version / README / release

final candidate必须包含：

```text
research-writing: 0.2 -> 0.3
maturity: remains unclassified
Repository VERSION: unchanged in this task
```

同步 plugin changelog、root CHANGELOG Unreleased、README、Marketplace config、generated plugin/profile/catalog/provenance identity。

README改变时必须真实调用 Clear Writing。

本任务不 merge `main`，不推进 `release`，不 tag、不发 GitHub Release。后续 formal repository release 才按当时 formal baseline决定 PATCH 版本。

## 9. Maintenance umbrella

架构已批准 umbrella，但 live Issue/Project尚未同步。

production edit前按 Implementation Plan §3.1执行或如实阻塞。不得声称已同步，也不得要求用户手工拖 Project。

## 10. Required outputs

至少保留：

```text
results/research-authoring--formal-production-authoring/RESULT.md
results/research-authoring--formal-production-authoring/MANIFEST.md
results/research-authoring--formal-production-authoring/PREFINAL_GATE_FREEZE.md
G1/G2/G3/G4实际产生的 evidence/review files
private/exports/research-authoring--formal-production-authoring/  # 大/私有产物按需
```

不创建无内容空文件。

## 11. Stop / recovery

立即停止并返回正确 owner：

- 架构/owner/Gate taxonomy需要改变；
- umbrella tracking合法入口不可得；
- final evidence reviewer无法访问完整必要材料；
- fresh task/delta在 freeze前无法合法确定；
- Plugin Creator live mutation未获授权；
- private/sensitive external upload未获授权；
- candidate-owned内容在 final Gate后变化；
- release/main merge需求出现；
- paid API/model reviewer需求出现。

final Gate失败不能通过换题、换 delta、追加样本或跨 candidate拼接恢复成 PASS。

## 12. Authorization ceiling

用户未来实际发送 execution-ready Critic逐字批准的 Kickoff，只授权 Implementation Plan中明确列出的：
- exact branch/worktree；
- 059 candidate source/profile/config/tests/generated/docs/results；
- tests/generator/CI；
- development regression；
- exact candidate install/replay；
- pre-final packet；
- G1–G3 final evidence；
- G4 wrapper package/manifest准备；
- ordinary task-owned commit/non-force push。

不授权：
- Plugin Creator live mutation；
- ChatGPT account mutation；
- main merge/formal release；
- paid API；
- private/sensitive external upload；
- Bridge/其他 domain plugin redesign；
- destructive Git；
- background automation。

## 13. Positive terminal condition

只有独立 Reviewer确认同一个 `C`：

```text
G1=PASS
G2=PASS
G3=PASS
G4=PASS
IMPLEMENTATION_OVERALL=PASS
```

且 candidate/version/generated/README/changelog identity一致，才能报告：

```text
RESEARCH_AUTHORING_0_3_CANDIDATE_READY=YES
FORMAL_RELEASED=NO
MAIN_MERGED=NO
```

任何较弱状态必须如实报告 partial / waiting / failed / blocked。
