# 059 Research Authoring C2 Pre-Final Gate Admission — Critic Review v0.1

日期：2026-10-06  
角色：独立 Critic  
审查阶段：C2_PRE_FINAL_GATE_ADMISSION  
Task：`research-authoring--formal-production-authoring`

## 结论

```text
RESULT=PASS
C2_PREFINAL_CRITIC=PASS

FINAL_CANDIDATE_COMMIT=
ac501d988f00cb6672fec105ae5fd51a0679cae0

PREFINAL_PACKET_HEAD=
2ebd8f3de0597b9549a7528c9917222b44c4cb59

CANDIDATE_OWNED_DRIFT=NO

G1_C2_PACKET_ADMITTED=YES

G2_TASK_ADMITTED=YES
G2_FRESHNESS=PASS
G2_PHASE_SEPARATION=PASS
G2_REVIEWER_ACCESS=PASS

G3_TASK_ADMITTED=YES
G3_FRESHNESS=PASS
G3_PROJECT_AUTHORITY=PASS
G3_REVIEWER_ACCESS=PASS

G4_REUSED_TASK=G2
G4_OFFLINE_WRAPPER_C2_BINDING=PASS
G4_FROZEN_RUBRIC_UNCHANGED=YES

FINAL_GATES_MAY_START=YES
```

本 PASS 只批准 exact C2 frozen final Gate execution。它不代表 G1-G4 已经 PASS，不代表 Research Authoring 0.3 已完成，也不授权 live Plugin update、paid API、main merge 或 release。

## C2 identity / drift

独立比较：

`ac501d988f00cb6672fec105ae5fd51a0679cae0..2ebd8f3de0597b9549a7528c9917222b44c4cb59`

结果在以下 candidate-owned Research Authoring production surface 上为零变化：

- `skills/writing/research/**`
- `plugins/codex/plugins/research-writing/**`
- `scripts/codex_marketplace_config.json`
- `tests/test_research_writing_routing.py`
- `profiles/research-main.json`
- `profiles/codex-research-writing.json`
- `README.md`
- `docs/plugin-changelogs/research-writing.md`

Shared replay infrastructure `eafb5e11...` 继续只算 validation infrastructure，不计入 Research Authoring product identity。

## 旧 evidence disposition

新的 packet 没有把 predecessor final PASS 拼给 C2：

- predecessor G1 -> regression only；
- DII G2 -> regression only；
- MoSAIC G3 -> regression / should-not-change only；
- first historical G4 ChatGPT package -> immutable FAIL regression only。

所有 C2 final claim仍要求直接绑定 C2。

## G1

G1 case bank仍测试原 capability：document-producing request是否进入 Research Authoring core，以及 neighboring/support-only request是否保持正确 owner。

新增 formal advisor-PDF natural case是 C2 normal-entry repair的直接真实回归，不是新 Gate；prompt没有加入 XeLaTeX/pdftotext/render等 evaluation-only blacklist。

Rubric明确要求 normal runtime actual consumption，静态 trigger/description不能 PASS；同时明确 G1不评价文档成稿质量，因此没有把 G1错误扩大成 G2/G3。

结论：`G1_C2_PACKET_ADMITTED=YES`。

## G2

新 G2 使用：

`YuukiAS/Reliable_Imaging_Inference`

Phase 1 ref：

`dc0b2ea471e79c29963d2ed92575a77540d23425`

Phase 2 ref：

`0c1fa13f6a4149b012f13191afed164a648478ec`

独立读取冻结 Phase 1 五个 source blob，确认它们共同提供：

- scientific direction / problem framing；
- CARE / CardiacNexus evidence boundary；
- data / annotation constraints；
- seminar-derived research implications；
- 2026-08-22 incremental roadmap refinement。

这些材料足够重新组织一份 greenfield advisor-facing research update，并不要求现成 advisor report作为 outline。

独立读取 Phase 2 四个 delta blob，确认它们确实是后续新增的 novelty / methodology tightening，能够实质改变 Phase 1 的 scientific decision：basic PPI/two-phase framing与hard-case oversampling不再足以作为 novelty，路线收窄为 baseline-first、structured imaging measurement inference / pathology transportability候选 gap，以及 CARE/MyoPS retrospective pseudo-two-phase benchmark。

AI_Skills_Collection 内针对以下 exact identifiers 的独立搜索均无匹配：

- `MEASUREMENT_INFERENCE_LITERATURE_AUDIT_2026-08`
- `PATHOLOGY_TRANSPORTABILITY.md`
- `SEMINAR_ROADMAP_REFINEMENTS_2026-08-22`
- `retrospective pseudo-two-phase`

因此没有直接证据表明这些 exact final materials曾参与 059 Research Authoring产品调优或 predecessor final Gate。

Phase 1 manifest与Phase 2 delta已在 final execution前冻结；Phase 1只能materialize exact五个 Phase 1 blobs，Phase 2四个 blob只有在 independent `PHASE1=PASS` 后才能进入 runtime。

Reviewer access要求完整 raw inputs、完整 Phase 1、delta、baseline、完整 Phase 2和 diff；summary-only不能 PASS。

结论：

```text
G2_TASK_ADMITTED=YES
G2_FRESHNESS=PASS
G2_PHASE_SEPARATION=PASS
G2_REVIEWER_ACCESS=PASS
```

## G3

新 G3 使用：

`YuukiAS/CARE_Challenge@75a40e454de43b64e59a0b0b438ff57ef2bb8345`

独立读取并核对 primary source：

- July failure-forensics formal LaTeX report；
- packet/hash manifest；
- evidence claim ledger；
- ranked root-cause table；
- bounded local conclusions；
- research decision tree；
- baseline technical context；
- August 4 CARE-ASE verified negative-result summary / training curve / terminal manifest；
- August 15 hierarchical pathology rescue blueprint。

真实 source直接支持这个任务不是 synthetic manuscript：项目已经存在完整正式 failure-forensics报告和后续真实负结果，而后续 blueprint明确标为 `DEFERRED_BLUEPRINT_ONLY`，因此任务要求“把负结果、failure mechanisms与下一科学决策整理成 manuscript-ready package，同时不能把 blueprint写成已完成方法”具有真实科学约束。

AI_Skills_Collection 内针对以下 exact identifiers 的独立搜索均无匹配：

- `CARE_failure_forensics_20260730`
- `20260730_care_failure_forensics_deep_research_packet`
- `CARE-ASE`
- `20260804_care_ase_r2_deadline_recovery_training_docker`

因此没有直接证据表明 exact G3 source/task曾用于 059 Research Authoring产品调优。

`PROJECT_AUTHORITY_ONLY_NO_EXTERNAL_SUBMISSION` 符合原来“venue/project authority必须真实”的合同：本 Gate测试真实 manuscript authoring与buildable package，不为了 freshness伪造一个投稿 venue。

Required package足够且不过度：`main.tex`、`references.bib`、必要 figures、`main.pdf`、evidence map、package说明；不机械制造 cover letter/reviewer response/submission sidecars。

Reviewer必须直接看到完整 source、baseline PDF、negative evidence、final manuscript source/PDF、references/figures、evidence map和 build/reference QA。

结论：

```text
G3_TASK_ADMITTED=YES
G3_FRESHNESS=PASS
G3_PROJECT_AUTHORITY=PASS
G3_REVIEWER_ACCESS=PASS
```

## G4

G4继续复用新的 C2 G2，是正确的：它测试 Chat -> Codex -> renderer integration，而不是创建第四个科学任务。

普通 natural request与历史 frozen G4 rubric保持不变；没有加入 command blacklist。

Offline wrapper composition全部绑定 exact C2：

- Research Authoring generated payload来自 `plugins/codex/plugins/research-writing/** @ ac501d98...`；
- Clear Writing support三个 snapshot也来自同一 C2；
- wrapper skills-only；
- no renderer runtime / MCP / connector / database / watcher。

官方 OpenAI Plugin/Skill文档当前仍明确区分：Skill提供可重复工作流/指令，Plugin可以只包含Skills而无需connected app；因此 skills-only wrapper本身与当前平台能力模型一致。

Live update仍独立：必须在真正 G4前重新读取 current live Plugin/release identity，并获得用户新的 bounded authorization。

结论：

```text
G4_REUSED_TASK=G2
G4_OFFLINE_WRAPPER_C2_BINDING=PASS
G4_FROZEN_RUBRIC_UNCHANGED=YES
```

## Reviewer / execution sequencing

Final execution必须保持：

1. G1 direct C2 normal-entry evidence；
2. G2 Phase 1 evidence；
3. G3 real manuscript evidence；
4. independent review可在同一 checkpoint审 G1 + G2 Phase 1 + G3，以减少人工往返；
5. 只有 `G2_PHASE1=PASS` 后才允许 materialize / execute G2 Phase 2；
6. G2 full PASS后才能建立 G4 semantic baseline；
7. G4 live wrapper mutation前必须再次 STOP，请求用户 bounded authorization；
8. G4 fresh Chat stage PASS后才允许 Codex renderer stage。

不得换 task/delta/rubric，不得跨 candidate拼 PASS。

## Live Plugin preparation

当前不授权 live Plugin mutation。

为了减少后续等待，final-Gate Executor可以在不改变账号状态的前提下，提前从 exact C2 roots构建完整 skills-only wrapper archive与file/hash manifest，并保存于 task `private/exports/`。这只是 offline preparation。

真正 Plugin Creator guarded update仍必须等 G2 full PASS / G4即将开始时由用户明确授权。

## Maintenance tracking

Issue #99 当前 reader-facing内容仍停在较早的 C0实现阶段，与真实 C2 pre-final状态不一致。当前 Critic surface未执行 Clear Writing + Project mutation，因此不在本 review中改写 Issue/Project。

Exact pending maintenance mutation：

- Issue #99 `当前进度` -> C2已冻结且 pre-final Critic PASS，final Gates可开始；
- `当前执行锚点` -> 本 review + `PREFINAL_GATE_FREEZE.md`；
- `下一步` -> 执行 G1、G2 Phase 1、G3 final evidence；等待 independent checkpoint后再进入 G2 Phase 2；
- Project lifecycle保持 `DOING`，不得提前 DONE。

该 tracking copy drift不阻断 frozen final Gate execution，但下一个具备 Clear Writing + Project mutation能力的 maintainer应先同步。

## 权限边界

```text
FINAL_GATES_MAY_START=YES
LIVE_PLUGIN_UPDATE_AUTHORIZED=NO
PAID_API_AUTHORIZED=NO
MAIN_MERGE_RELEASE_AUTHORIZED=NO
```
