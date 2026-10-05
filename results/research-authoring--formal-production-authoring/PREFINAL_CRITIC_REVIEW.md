# Research Authoring 059 — Pre-Final Gate Admission Critic Review

日期：2026-10-05  
角色：独立 Critic  
审查阶段：PRE_FINAL_GATE_ADMISSION  
结果：PASS

## 审查对象

- Repository: `YuukiAS/AI_Skills_Collection`
- Task: `research-authoring--formal-production-authoring`
- Execution branch: `work/research-authoring--formal-production-authoring`
- Frozen packet head: `67f2f1fc082d5a87438e5c37447ac96c8839a654`
- Implementation candidate C0: `1c37c0715aca0096606f24e56192b7857e72bbd6`

架构状态保持：

```text
RA1 = CLOSED
RA2 = CLOSED
RA3 = CLOSED
RA4 = CLOSED_FOR_ARCHITECTURE_STAGE
```

本轮没有重新打开架构。

## C0 不可变性

独立比较 `C0..67f2f1f` 后，C0 之后的变化仅位于：

- `results/research-authoring--formal-production-authoring/**`
- `private/exports/research-authoring--formal-production-authoring/**`

没有 Research Authoring candidate-owned source/profile/config/tests/generated/release-metadata 变化。

因此：

`FINAL_CANDIDATE_COMMIT=C=1c37c0715aca0096606f24e56192b7857e72bbd6`

可以在本次 pre-final PASS 后成立。

## G2 admission

### Exact task

- Project: `YuukiAS/Distributed_Imaging_Inference`
- Frozen ref: `c6ed0fb40c702936ec1f41454390ef188a5b4d97`
- Phase 1: clean CARE subject-disjoint + Pattern H robustness + supporting M&Ms replication 的 greenfield advisor update
- Phase 2: pre-frozen personalized partial-pooling delta

### Freshness

独立核对 AI_Skills 059 source/design/development material后，没有发现以下 exact final inputs被用于调 C0：

- `care_clean_subject_disjoint_2026-09-04`
- `care_pattern_h_robustness_2026-09-04`
- `care_personalized_partial_pooling_2026-09-04`

DII 仓库和其他 DII advisor-report 经验曾参与 059 设计/开发，并不等价于这个 exact task 被用于产品调优。

因此 task-level freshness 成立。

### Phase 1 raw input sufficiency

Phase 1 六个冻结 blob 已逐项核对，blob identity 与 manifest 一致。

它们直接包含：
- clean subject-disjoint experiment contract；
- clean CARE Pattern H decision；
- H-ROBUST decision；
- robustness bootstrap uncertainty/effect evidence；
- M&Ms frozen experiment contract；
- M&Ms replication decision。

这些材料足以支持一份 bounded greenfield advisor update：可以说明 clean CARE/H-ROBUST 的主要结论、M&Ms 的 supporting replication 身份、证据边界和下一科学问题；不需要现成 advisor/group-meeting report 才能建立文档 spine。

### Phase separation

Phase 2 四个 delta blob 也逐项核对，identity 与 frozen delta 一致。

它们在 Phase 1 开始前已经冻结，但正式执行时不得 materialize 到 Phase 1 input。Phase 1 只 materialize 六个 raw blobs；Phase 2 只有在 independent `PHASE1=PASS` 后才 materialize。

当前合同不声称建立新的数据库或严格 OS 级 read-isolation；它要求 final runtime 的实际输入/消费范围只包含冻结 Phase 1 manifest，并以 Reviewer 的 provenance/no-leakage 判定为准。由于 Phase 2 科学结果 blob 在 Phase 1 前不进入运行输入，且任何 leakage 都是 Phase 1 FAIL，这足以满足已批准的 G2 final-evidence contract。

### Rubric / access

G2 rubric 与 v0.3 架构一致：
- greenfield provenance；
- reader-first structure；
- orientation；
- claim/evidence；
- uncertainty；
- internal-detail filtering；
- table/figure/formula role；
- provenance boundary；
- Clear Writing semantic fidelity；
- no Phase 2 leakage；
- Phase 2 minimal dependency closure / no broad drift。

Reviewer access 要求完整 raw input、Phase1全文、delta、baseline、Phase2全文和 diff；摘要不能替代。

结论：

```text
G2_TASK_ADMITTED=YES
G2_FRESHNESS=PASS
G2_PHASE_SEPARATION=PASS
```

## G3 admission

### Exact task

- Project: `YuukiAS/MoSAIC_Paper`
- Frozen ref: `590bfbac1450fbab5e4ca8ce77c877ece845f094`
- Task: 将 author-approved CARE 2026 LNCS manuscript truth 从当前 14 页 baseline 收到 frozen <=12 页 absolute limit，保持 double-blind、科学主张边界和 LNCS template 不变，产出 buildable package + PDF + submission manifest。

实际读取并核对了：
- `AGENTS.md`
- `README.md`
- `PAPER_STATUS.md`
- `RESULTS_TRUTH.md`
- `METHOD_TRUTH.md`
- `CLAIM_LEDGER.md`
- `review/AUTHOR_DECISIONS.md`
- `submission/mosaic.tex`
- `submission/refs.bib`
- LNCS class/style identity；
- active figure identity；
- baseline PDF identity。

冻结 blob identity 与 G3 authority packet 一致。

### Real task / authority

MoSAIC 当前 manuscript truth 确实存在真实生产冲突：
- README 冻结 CARE 2026 absolute maximum = 12 pages including references；
- baseline `submission/mosaic.pdf` 被 project QA 记录为 14 pages；
- active manuscript 已为 double-blind anonymous source；
- truth files 对 active results、unsupported ablation/robustness、old edema row、citation/result strength 有明确边界。

这不是机械 compile task，而是真实 manuscript production / compression / package-consistency 任务。

### Freshness

AI_Skills 中存在 2026-07 的 MoSAIC generic writing lessons/provenance，但它们影响的是通用 writing-fidelity/Clear Writing 经验。

没有直接证据表明：
- exact ref `590bfb...`；
- exact current manuscript truth set；
- exact 14 -> <=12 CARE package task；
- exact G3 rubric；

曾被 059 用来调 Research Authoring C0。

因此旧的 repo-level generic writing exposure 不足以污染本次 task-level fresh final evidence。

### Package subset

冻结 package：

- `mosaic.tex`
- `refs.bib`
- `figures/fig1_original_redraw.pdf`
- `llncs.cls`
- `splncs04.bst`
- `mosaic.pdf`
- `SUBMISSION_MANIFEST.md`

是 task-driven 的最小真实集合。

`mosaic.tex` 的 active figure 只有 `fig1_original_redraw.pdf`；第二个 qualitative figure 位于 inactive `\iffalse ... \fi` 区域，因此不要求它进入 active final package 是合理的。

不机械生成 supplement、cover letter、reviewer response、独立 declaration/checklist 等文件也符合已批准的“按任务选择”合同。

### Reviewer access

文本 truth/source 可由 GitHub connector 直接读取。binary figure/PDF 在当前 connector 只能稳定绑定 blob identity，final Gate 前若 Reviewer surface 不能直接呈现完整 binary/render，合同已要求 Executor materialize exact blob/artifact 到 AI_Skills private export 并绑定 hash。

因此不存在不可恢复的 Reviewer-access 死路。

结论：

```text
G3_TASK_ADMITTED=YES
G3_FRESHNESS=PASS
G3_REVIEWER_ACCESS=PASS
```

## G4 admission

G4 复用 G2 是正确的。

它只在 G2 full PASS 后使用 G2 Phase 2 approved document 作为 semantic baseline，验证：
- exact candidate wrapper；
- same-commit Clear Writing support；
- Chat source/handoff；
- exact-C Codex `research-main`；
- Research Authoring before renderer；
- final PDF / renderer QA；
- post-render scientific QA；
- actual artifact delivery。

没有增加第四个 science task，也没有把 G3 的 manuscript-package复杂度混入 cross-surface integration Gate。

Live Plugin Creator / ChatGPT account mutation仍未授权；本 pre-final PASS 不改变该状态。

结论：

```text
G4_REUSED_TASK=G2
G4_TASK_REUSE=PASS
```

## C0 implementation admission sanity check

C0 的 canonical `research-authoring-core`、thin route source、profiles、Marketplace config 与 generated report/paper/litcite 已实际读取。

关键实现已存在：
- report/paper/litcite generated aggregates 使用 `coordinator-first`；
- document-producing route 先进入 `research-authoring-core`；
- lower-level report/paper/literature skills明确禁止绕过 core；
- support-only branch 仍由 core boundary/direct support skill 合同限制，不应建立完整 document brief；
- RA2 minimal dependency closure 与 protected invariants 已写入 canonical core；
- generated/plugin/profile identity 已由 deterministic validation/profile smoke/replay证明。

support-only normal-entry 是否在真实运行中误触发 full document planning，属于冻结 G1 final Gate 的直接验收对象，不构成本次 pre-final admission 前的已知 source-level blocker。

## Final judgment

```text
PREFINAL_CRITIC=PASS

FINAL_CANDIDATE_COMMIT=1c37c0715aca0096606f24e56192b7857e72bbd6
FROZEN_PACKET_HEAD=67f2f1fc082d5a87438e5c37447ac96c8839a654

G2_TASK_ADMITTED=YES
G2_FRESHNESS=PASS
G2_PHASE_SEPARATION=PASS

G3_TASK_ADMITTED=YES
G3_FRESHNESS=PASS
G3_REVIEWER_ACCESS=PASS

G4_REUSED_TASK=G2
G4_TASK_REUSE=PASS

FINAL_GATES_MAY_START=YES
```

这只批准 frozen final Gate execution。

它不等于：
- G1-G4 PASS；
- Research Authoring 0.3 implementation overall PASS；
- Research Authoring 0.3 正式发布。

它也不授权：
- Plugin Creator live mutation；
- ChatGPT account mutation；
- main merge；
- formal release；
- paid API；
- private/sensitive external upload。

Executor 应继续同一个 Goal，不改变 candidate-owned content、不换 task/delta/rubric、不跨 candidate 拼 PASS。G4 到 live Plugin mutation 前必须再次 STOP，请求用户的 bounded authorization。
