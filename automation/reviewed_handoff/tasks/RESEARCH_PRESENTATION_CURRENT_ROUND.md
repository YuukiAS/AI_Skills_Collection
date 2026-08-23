# Research Presentation Current Round

上一轮 synthetic statistical / medical-imaging benchmark 继续只作为工程链路、科学正确性和基础视觉 QA baseline，不是高质量科研汇报的 gold visual baseline。长期 `PROGRAM_MATURE=false`。

当前仍处于 **REFERENCE_CALIBRATED_ONE_SHOT_QUALITY** round。Reviewed Handoff 继续作为主流程：每个阶段拆成独立 bounded task，最多两轮 review；Codex Executor 不得根据长期 roadmap 自主连续实现多个阶段。

## 已完成：018 外部 Presentation 方法审计

`018_presentation_external_method_audit` 已 PASS。

核心结论：当前主要缺口不是继续堆抽象规则，而是把真实优秀 reference slide 转成机器可用、可进入生成决策的设计表示。

## 已完成：019 Reference Composition Representation

`019_research_presentation_exemplar_composition_representation` 已 PASS。

当前 composition layer 已包含 13 个真实 inspected composition records、8 类 renderer-neutral composition families、normalized geometry / hierarchy / alignment / reading flow、deterministic validator、只读 selector 与不含 source pixels 的 abstract debug montage。

019 证明系统已经能机器读取“优秀科研页面怎么构图”。

## 已完成：020 Reference-Calibrated Candidate Search

`020_research_presentation_reference_calibrated_candidate_search` 已在第二轮独立审核中 PASS。

020 证明：

- 同一 scientific content 可以内部生成恰好 3 个 compositionally distinct candidates；
- selected 019 source record 的真实 normalized geometry 已进入 candidate bbox 推导；
- source-to-candidate split / scale / translate / reorder 可审计；
- statistical estimator 与 medical-image 两类 request 共用同一 shared candidate engine；
- wildcard / alternative source selection 只在 scientific-job compatible pool 中工作。

## 已完成：021 Comparative Reference-Calibrated Visual Review

`021_research_presentation_comparative_reference_calibrated_visual_review` 已在第一轮独立审核中 PASS。

021 证明 comparative review mechanism 已成立：

- statistical / medical 两个 case 都真实包含 3 个 generated candidates 与 2 个 inspected reference renders；
- reference pixels 真实送入 `gpt-5.6-terra`；
- Terra-visible 输入使用匿名 ID，不暴露作者、机构、RRL/SRC、candidate strategy 或 generated/reference 身份；
- canonical inspected render SHA 与本次 actual reviewer-input SHA 分开绑定；
- 每个 immutable case identity 只运行一次 live Terra；
- no-winner 是合法结果，没有 best-of-three 强制晋级；
- required CI 已 PASS。

021 同时给出了可信的负面质量基线：统计 generated candidates 全部低于成熟公式页 reference bar，医学影像 candidates 也存在 image prominence / panel integration / fixture 感问题。

## 已完成：022 Candidate Visual Finish Repair

`022_research_presentation_candidate_visual_finish_repair` 已在第一轮独立审核中 PASS。

022 关闭了 021 暴露出的 candidate-layer visual-finish blocker，同时保持 019/020 reference-to-geometry 与 semantic compatibility：

- statistical generated `reference_faithful` candidate 在匿名 comparative review 中达到 mature research-group-meeting / strong conference-talk bar；公式对比度、投影可读性与 direct mathematical annotation 已实质修复；
- medical generated `controlled_wildcard` 与 `alternative_composition` 达到成熟组会水平；image prominence、panel labels、legend 与 annotation integration 已明显改善；
- 三候选继续共享同一 page-level visual tokens，差异来自 composition 而不是换 theme；
- old candidate identities 保留，repair 后产生新的 preview SHA；
- 每个 repaired immutable identity 只运行一次 live Terra；
- required CI 已 PASS。

这证明单页 candidate engine 已开始接近真实成熟 reference bar，但还不能推出完整 deck 已成熟。

## 当前 bounded task

当前任务：

`023_research_presentation_deck_design_system_integration`

023 已完成两轮正式 review，当前停在人工决策点，**尚未 PASS**。真实 CI 已成功；第二轮继续 `REVISE` 的原因不是工程失败，而是第一轮同一个 design-profile integration blocker 只部分关闭。

已经成立的部分：

- deck profile 已真正驱动字体、字号、颜色角色、annotation leader 与 equation highlight / leader role；
- profile mutation 已证明修改 `accent` / `title_pt` 会改变 native PPTX XML，同时 page-local geometry signature 保持稳定；
- 两套 coherent multi-page PPTX engineering fixtures、real render、mechanical QA 与 composition diversity 都继续通过。

仍未闭合的部分：

- `spacing.outer_margin/object_gap/annotation_gap/panel_label_gap` 仍主要只是 profile metadata，实际 title/caption/panel-label 等位置仍存在固定字面坐标；
- `image_panel.label_position/legend_binding/container_role` 与 `caption.position/style` 仍没有完整驱动 renderer；
- 当前 mutation regression 只覆盖颜色和标题字号，不能证明剩余 spacing / caption / image-panel contract 已成为 executable design-system input。

因此 023 已达到两轮 review limit，当前状态为 `AWAIT_HUMAN_DECISION`。在用户明确授权恢复之前，不得自动开启第三轮修复，也不得提前创建 contact-sheet / deck-rhythm QA task。

## 后续 roadmap（非 Executor 授权）

如果用户授权一次严格限定的 023 recovery，应只补齐剩余 design-profile executable contract，并通过新的 mutation regression + real CI 做 recovery closure；不得改 reference corpus、019/020/021/022 机制，也不得提前开始 holdout。

只有 023 recovery 独立关闭后，Planner 才创建下一 bounded task 进入正式 **contact-sheet / deck-rhythm QA**。

随后长期仍需完成：

- real statistical holdout one-shot；
- real medical-imaging holdout one-shot；
- 必要时独立 Beamer holdout。

没有对应 `PLAN_FROZEN` 时，Executor 不得自行开始这些阶段。

## 当前完成条件

本 round 只有在 reference-to-composition transfer、内部设计探索、comparative review、candidate visual quality、deck-wide design-system integration、deck-rhythm QA 与两个真实 holdout one-shot benchmark 全部成立后，才有资格写 `ONE_SHOT_QUALITY_PASS`。

当前绝不能宣告本轮 PASS，也不能再次用单一 Terra absolute PASS 关闭 design-quality 目标。
