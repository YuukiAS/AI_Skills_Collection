# Research Presentation Current Round

当前仍属于 `REFERENCE_CALIBRATED_ONE_SHOT_QUALITY`，长期 `PROGRAM_MATURE=false`。

**Source of truth：** `RESEARCH_PRESENTATION_CORPUS_PROGRAM_GOAL.md` 的 Five-Stage Closure Roadmap、Quality-Preserving Continuation Policy 与 Final Quality Gates。本文只记录当前阶段状态与已经冻结的历史结论，不维护第二套 roadmap。

## Historical decision on 023

`023_research_presentation_deck_design_system_integration` 保持历史 `AWAIT_HUMAN_DECISION / REVIEW_LIMIT / REVISE`，不伪造第三轮。其 low-level editable-PPTX design-profile renderer 不再是第一成熟 production route；当前 production contract 以 canonical exact CUHK Beamer `.tex + PDF` 为主。

## Completed stages

### Stage 1 — Product Contract Reset — PASS

`024_research_presentation_product_contract_reset` 已独立 PASS。普通科研组会 / paper talk / research update 未指定格式时，默认走 exact CUHK Beamer/source-editable TeX；显式 PowerPoint/PPTX/Slides 仍可覆盖。Exact CUHK identity 绑定 canonical CUHK Beamer source，derived PPTX/scaffold 不得冒充 exact production source。

### Stage 2 — Gold Scientific Composition Library — PASS

`025_research_presentation_gold_scientific_composition_library` 保留 review-limit 历史，其唯一 coverage gap 由 `026_research_presentation_discussion_next_experiment_gold_recovery` 关闭。026 第二轮独立 PASS。当前 production gold 已覆盖 roadmap 所需主要 scientific jobs，并建立 `RUNTIME_SELECTED -> ACTUALLY_CONSUMED -> OUTPUT_AFFECTED` 的真实选择/消费证据。

### Stage 3 — Executable CUHK Scientific Layout System — PASS

`027_research_presentation_executable_cuhk_scientific_layout_system` 建立核心工程链并保留 review-limit 历史；028 关闭旧 visual dispatch gap；029 完成 task-local Visual Review consumer adaptation；`030_stage3_visual_recovery` 第二轮独立 PASS。六个主要内容页已证明成熟 scientific composition 可在 exact CUHK content area 中执行为统计模型、定量结果、实验设计、负结果、医学影像比较与下一实验布局，并达到 item/page-level mature research-group-meeting / strong conference-talk bar。

### Stage 4 — One-Call Production + Bounded Quality Loop — PASS

Stage 4 已由 Planner 整体判定 PASS；该结论证明普通一次调用会真实串起 source fidelity、storyline、gold retrieval、canonical CUHK、compile/render、task-local visual handoff、deck contact sheet、双层 render identity 与单次 bounded quality-loop contract，但不替代真实 unseen paper 泛化验收。

Stage 4 历史链保持：031 建立 one-call production；032 关闭 multi-workstream coherence；033 建立 deck-level rhythm/quality loop；034 关闭 render identity 与 CI 证据语义；035 关闭 generic model support hardcode；036 关闭 process-page projection/source-grounding；037 关闭最后一个 audience-facing workstream transition 元语言 gap。此前达到 review limit 的 task 历史均保留，后续 recovery 只关闭未解决 blocker，没有事后改写旧 task 为 PASS。

## Stage 5 — frozen 4-paper batch acceptance

### 038 — first two real-paper holdouts — terminal REVIEW_LIMIT / REVISE

`038_research_presentation_two_real_paper_holdouts` 是第一次真正的双论文 unseen evaluation：

1. statistics/methodology：Bürkner (2017), **brms: An R Package for Bayesian Multilevel Models Using Stan**；
2. medical imaging：Ma et al. (2024), **Segment anything in medical images**。

两篇都在首次 render 前完成 tracked-corpus/tuning exclusion audit、source/license audit 与 source-bundle freeze，并通过正常 production entry 生成真实 exact-CUHK deck。真实 Terra 暴露 7 个阻断视觉问题；允许的单次 quality loop 随后因为真实 review finding 不含 consumer 期望的 `repair_intent` 而没有选择任何 repair，也没有改变 pixels。Round 2 仍失败。

038 保持两轮 review limit 的真实失败历史；没有第三轮，也没有降低质量门。**brms 与 MedSAM 永久失去 unseen holdout 资格**，不得修漂亮后重新宣称 one-shot PASS。

### 039 — generic quality-loop execution recovery — PASS

`039_research_presentation_quality_loop_execution_recovery` 已在第二轮 Planner 独立审核 PASS。该 task 使用与 038 无关的 non-holdout stress bundle，关闭了 038 暴露的通用 consumer/execution gap：

- structured visual finding 即使没有内部 `repair_intent`，也能在 requirement/target/page-job 语义唯一且安全时映射到现有 bounded repair vocabulary；未知/歧义 finding 继续 fail closed；
- audience meta copy、caption/support collision、undersized primary object、process-diagram collision 与 medical legend/callout obstruction 的安全 repair 都有真实下游 layout consumer；
- stress run 实际使用且只使用一次 repair cycle，前后 render-input 与 rendered-pixel identity 均真实变化；source fidelity、CUHK identity 和 medical source pixels 受保护；
- Review 1 唯一剩余的 stress-title 工程语言泄漏由窄范围 revision 关闭；没有借机修改 normal production rules 或使用 brms/MedSAM 调参；
- 真实 GitHub CI PASS；fresh task-local Terra 与最终 implementation/render identities 绑定，六个主要内容页与整套 contact sheet 全部 item-level PASS，无 blocking finding。

039 PASS 只证明 generic recovery，**不构成 Stage 5 holdout PASS**。

### 040 — superseded before execution

`040_research_presentation_replacement_two_real_paper_holdouts` 在旧 two-paper replacement protocol 下冻结，但在 Executor acquisition/render 前被停止，并由新的 frozen-batch generalization protocol 取代。

旧 040 protocol 不再作为充分的泛化证据，因为它允许潜在的 adaptive holdout replacement：真实论文失败后修系统、再换论文，循环直到偶然找到两个通过样本。040 不得执行，也不能关闭 Program。

由于 040 从未执行，其拟议的 TMB 与 cardiac-ultrasound 论文没有被 040 消费；tracked-repository 中只有 Planner 文档提及，`implementation_commit=null`，terminal report 记录无 acquisition、source-bundle freeze、render、Terra 或 production invocation。

### 041 — frozen four-paper generalization batch — terminal REVIEW_LIMIT / REVISE

`041_research_presentation_frozen_four_paper_generalization_batch` 已完成第一次完整 4-paper frozen batch，并在 Round 2 独立审核后依法终止为失败批次；没有第三轮，也没有在 batch 内换论文、改 source bundle、扩 gold、改 selector/repair mapping 或降低视觉门槛。

冻结并全部 consumed 的四篇是：

1. statistics / computational methodology：Kristensen et al. (2016), **TMB: Automatic Differentiation and Laplace Approximation**；
2. biostatistics / methodology：Love, Huber & Anders (2014), **Moderated estimation of fold change and dispersion for RNA-seq data with DESeq2**；
3. medical imaging：Ferreira et al. (2025), **Self-supervised learning for label-free segmentation in cardiac ultrasound**；
4. medical imaging：Zhou et al. (2023), **A foundation model for generalizable disease detection from retinal images**。

四个 source bundle 均在任何成功 render 前整体冻结，production behavior 保持冻结；真实 GitHub CI 通过。最终结果为：

- TMB 与 RETFound 都在正常 production entry 的成熟 gold composition selector 阶段于 render 前失败，错误为 `no compatible gold composition record`；
- DESeq2 与 cardiac-ultrasound 均成功生成 exact-CUHK deck，但 Review 1 允许的唯一 shipped quality-loop consumer 在真实 Terra finding 上无法安全、唯一地选择 repair directive；两套均 `UNSAFE_REPAIR_MAPPING / QUALITY_LOOP_FAIL_NO_WINNER`，没有新 render/pixel identity；
- 最新 task-local Terra 与最终 implementation、manifest、source freeze 和实际 pixels 绑定，仍记录 DESeq2 / cardiac-ultrasound 的底部正文/引用碰撞，两个 contact sheet 均未通过，同时保留两个 pre-render selector failure 与 quality-loop fail-closed 为 batch blocker。

因此 041 严格 4/4 FAIL，四篇全部永久失去 unseen holdout 资格。其 Round 1、Round 2、FINAL_REPORT、failure logs、quality-loop state 与 Terra evidence 保持为真实 generalization failure corpus，不允许后续把四篇修漂亮后重新宣称 unseen success。

### 042 — semantic-compatibility generic recovery — terminal PLANNER_DECISION / REVISE

`042_research_presentation_semantic_compatibility_recovery` 已在唯一 Plan revision 边界依法终止，并保留未满足的 live-repair acceptance gate；没有伪造第二轮 PASS，也没有继续改变 fixture 追逐一个方便的 Terra failure。

042 的核心通用机制是真实有效的：mature gold selector 与 bounded quality-loop mapper 现在共享同一套有限 canonical scientific-object semantic normalizer；中性 alias 可归一到数学模型、定量 source object、process diagram、medical image panel、discussion/decision 等结构角色，同时 page-function/domain/panel/capacity、mature gold membership、existing repair vocabulary、single-cycle limit 与 fail-closed boundary 保持。042 没有使用 041 四篇的正文、图像、DOI 或 page-specific content 调参。

最终 task-local Terra 与 implementation、manifest、render-input/rendered-pixel identity 真实绑定；统计模型、定量结果、实验设计、负结果、下一实验、医学影像六张 substantive page 与完整 contact sheet 全部 item-level PASS，且 contact sheet 明确认可成熟的 result→failure→next-experiment 节奏与独立影像 workstream。因此 semantic compatibility 的非回归证据成立。

042 不能 PASS 的唯一剩余原因是 frozen Plan 还要求直接证明一次 **real Terra substantive finding → shared canonical role → existing safe repair → changed render inputs/pixels → fresh final Terra**。唯一 staging bridge 后，真实 initial Terra 返回 `blocking_findings=0`；consumer 因此正确执行 `repair_cycle_count=0`，没有可合法修复的 finding。Plan revision 已用尽，所以 042 保留 terminal `AWAIT_HUMAN_DECISION / PLANNER_DECISION / REVISE` 历史，但依据 Quality-Preserving Continuation Policy，这个机械 evidence gap 不要求用户在“保持门槛/降低门槛”之间做选择，直接由新的 bounded recovery 继续。

### 043 — active real-visual-repair challenge recovery — PLAN_FROZEN

当前唯一活动任务：

`043_research_presentation_real_visual_repair_challenge_recovery`

043 不再重复 042 的单 fixture 迭代，而是冻结一个新的有限验证机制：在任何 challenge Terra 结果被读取前，一次性生成并追踪恰好三个与 041 完全无关的 non-holdout/public-safe challenge variant——`Q_SCALE`、`Q_SUPPORT`、`PROCESS_REFLOW`，分别针对已经 shipped 的主科研对象投影缩放、图注/支持区域分离、流程图兼容 reflow 三类 repair family。三个初始 source/input、manifest、render-input、pixel 和 target-page identity 必须先整体冻结，之后禁止根据 Terra 改 challenge 或创建第四个 variant。

真实 task-local Terra 只负责判断是否真的出现 substantive-page blocker；若多于一个 variant 可安全映射，按预先冻结的 `Q_SCALE -> Q_SUPPORT -> PROCESS_REFLOW` 优先级选择，禁止事后挑最好修的。选中后只允许现有 quality-loop 执行一次 repair；必须证明 pre/post render-input、rendered-pixel 与目标页 hash 均真实变化，再由 fresh final Terra 对修复页和完整 contact sheet 达到成熟博士组会 / strong paper-talk bar。若三者都没有真实可修 finding、需要新 repair/gold/semantic rule，或一次 repair 后仍不合格，043 按 stop condition失败，不继续追逐。

043 不修改 mature gold、canonical semantic roles、safe-repair vocabulary/mapping、selector hard constraints、视觉门槛或 Stage 5 holdout。它如果 PASS，只代表 041 之后的 generic recovery evidence终于闭环；**随后必须真正停在用户 human gate，报告 041 失败原因、039/042/043 的通用恢复和证据，由用户决定是否值得再消耗下一组 fresh four-paper batch。** Stage 5 仍未通过，`PROGRAM_MATURE=false`。

## Standing workflow decisions

- 始终保持最高冻结质量标准；review/plan limit 后若存在唯一、范围清楚、质量保持的 bounded recovery，自动创建新 task，不让用户在“保持质量”与“降低质量”之间重复选择。
- 每个 bounded task 最多两轮 review；不得增加 REVIEW_3。
- 视觉型 Reviewed Handoff 优先使用 Bridge Kit task-local Visual Review contract；缺 evidence 属于等待，不消耗 review round。
- 单 task PASS 不等于 Program PASS。
- Stage 1–4 首次整体 PASS 的旁路 notifier 不是 approval gate，不暂停下一 stage。
- 对高成本 final holdout acceptance，failed batch + generic recovery 后，消耗下一批 fresh holdout 前必须打断用户。
- 只有真正存在互斥产品/科学选择、显著架构改变、新成本/风险/隐私/许可问题、必须降低质量门槛，或 Stage 5 最终 4-deck batch 验收时才打断用户。

## Non-negotiable final acceptance

最终仍必须由完整 frozen batch 中的四篇 unseen paper 各自产生一套完整真实 CUHK 组会 deck；paper notation/data/figures/images 必须主导内容，不能用 synthetic/fixture/CI/mechanical PASS 替代。Terra 必须读 item/page-level evidence，Planner 必须独立审核真实 source/trace/render。

只有一个完整 frozen 4-paper batch 的四套 deck 全部通过 Terra + Planner，Stage 5 才能进入最终用户人工门，并把四套真实 rendered deck/artifact 提供给用户检查。只有用户明确接受四套结果，才允许 `ONE_SHOT_QUALITY_PASS`、`PROGRAM_MATURE=true` 与停止 Planner automation。
