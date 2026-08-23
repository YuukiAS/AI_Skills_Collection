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

更重要的是，021 第一次给出了可信的负面质量结论：

- statistical estimator/equation：真实成熟 reference RRL-028 明显优于全部三个 generated candidates；generated 最好的一版仍存在 equation contrast / legibility 与 direct mathematical annotation 差距；
- medical-image comparison：所有 items 都低于 mature research-group-meeting / strong conference-talk bar；generated candidates 的可修问题包括 image prominence、panel integration 与 sparse fixture 感，同时 synthetic/demo-like evidence 本身也是当前 regression 的上限。

因此 021 的 PASS 只代表“比较机制可信”，不代表 candidate quality PASS。

## 当前 bounded task

当前任务：

`022_research_presentation_candidate_visual_finish_repair`

目标：在保持 019/020 reference geometry transfer 与 semantic compatibility 的前提下，修 candidate visual finish / scientific-object treatment，而不是继续扩 reference metadata。

022 重点冻结为：

- statistical equation page：提高公式对比度、投影可读性，annotation 必须直接绑定具体数学对象/term，而不是远距离解释文字；
- medical-image page：让 image/overlay 真正占据 source-derived primary region，panel labels / legend / annotation 直接整合，去掉 generic card/padding 与小图 + 大块空白的 fixture 感；
- 三候选继续共享同一 page-level visual tokens，差异仍来自 composition，而不是换 theme；
- old candidate identities 保留，repair 后产生新的 preview SHA；
- 复用 021 comparative pipeline，对新的 immutable statistical / medical identities 各只运行一次 live Terra；
- 不把 synthetic medical fixture 美化成真实临床证据；若剩余差距主要来自 synthetic evidence realism，必须明确留给后续 real holdout。

022 通过前不得进入 deck-wide design-system locking / generation integration。

## 后续 roadmap（非 Executor 授权）

只有 repaired candidates 已接近真实 reference bar，Planner 才创建下一 bounded task 进入 deck-wide design-system locking / generation integration。

长期仍需完成：

- deck-wide design-system locking / generation integration；
- contact-sheet / deck-rhythm QA；
- real statistical holdout one-shot；
- real medical-imaging holdout one-shot；
- 必要时独立 Beamer holdout。

没有对应 `PLAN_FROZEN` 时，Executor 不得自行开始这些阶段。

## 当前完成条件

本 round 只有在 reference-to-composition transfer、内部设计探索、comparative review、candidate visual quality、deck-rhythm QA 与两个真实 holdout one-shot benchmark 全部成立后，才有资格写 `ONE_SHOT_QUALITY_PASS`。

当前绝不能宣告本轮 PASS，也不能再次用单一 Terra absolute PASS 关闭 design-quality 目标。
