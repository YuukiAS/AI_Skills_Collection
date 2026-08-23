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

020 现在证明：

- 同一 scientific content 可以内部生成恰好 3 个 compositionally distinct candidates；
- selected 019 source record 的真实 normalized geometry 已进入 candidate bbox 推导，而不是只选 family 后套固定坐标；
- source-to-candidate split / scale / translate / reorder 可审计；
- statistical estimator 与 medical-image 两类 request 共用同一 shared candidate engine；
- wildcard / alternative source selection 只在 scientific-job compatible pool 中工作；
- candidate 仍使用相同 neutral preview skin，因此差异主要来自 composition，不是换色；
- old synthetic assets 仍只承担 regression content，不是 gold visual baseline。

020 最终 required CI 已 PASS。020 仍不证明任何 candidate 已达到成熟科研汇报视觉质量。

## 当前 bounded task

当前任务：

`021_research_presentation_comparative_reference_calibrated_visual_review`

目标：把 020 的三个 generated candidate previews 与匹配的真实 inspected reference renders 放进同一个匿名相对视觉审查框架，第一次真正回答：

> candidate 和成熟科研 reference 放在一起时，到底差多少？

021 的关键要求：

- statistical estimator 与 medical-image 两个 case 各使用 3 个 020 candidates + 2–4 个真实 inspected reference renders；
- reference pixels 必须真实送入 `gpt-5.6-terra`，不能用 RRL prose / bbox metadata 替代；
- Terra-visible inputs 使用匿名 item IDs，不暴露作者、机构、RRL/SRC、candidate strategy，也不告诉 reviewer 哪些是 generated / reference；
- 同时记录 019 canonical render SHA 与本次实际 reviewer-input SHA；
- 每个 immutable case identity 只运行一次 live Terra；
- reviewer 必须给出逐 item 的相对成熟度 / ordering / visual gap，而不是只给全局绝对 PASS；
- 解码后允许 `NO_CANDIDATE_MEETS_REFERENCE_BAR`，不得强制 best-of-three 晋级；
- 不提交外部 reference pixels，不修改 Bridge Kit core，也不修改 020 candidate geometry 追求本轮结果。

021 的 PASS 只表示 comparative review 机制可信，不代表 candidate 质量 PASS。

## 后续 roadmap（非 Executor 授权）

021 PASS 后，Planner 根据真实 comparative evidence 决定下一 bounded task。若 candidate 明显低于 reference bar，优先修 design/candidate layer；只有 candidate 已接近 reference bar，才进入 deck-wide design-system locking / generation integration。

长期仍需至少完成：

- deck-wide design-system locking / generation integration；
- contact-sheet / deck-rhythm QA；
- real statistical holdout one-shot；
- real medical-imaging holdout one-shot；
- 必要时独立 Beamer holdout。

没有对应 `PLAN_FROZEN` 时，Executor 不得自行开始这些阶段。

## 当前完成条件

本 round 只有在 reference-to-composition transfer、内部设计探索、comparative review、deck-rhythm QA 与两个真实 holdout one-shot benchmark 全部成立后，才有资格写 `ONE_SHOT_QUALITY_PASS`。

当前绝不能宣告本轮 PASS，也不能再次用单一 Terra absolute PASS 关闭 design-quality 目标。
