---
schema: AI_BRIDGE_REVIEWED_REVIEW_V1
task_key: 019_research_presentation_exemplar_composition_representation
review_round: 1
decision: PASS
implementation_commit: b858b857d5f26077917a4fbe5032a81f33b4b69d
---

# GPT Review

## Decision

`PASS`。

019 已完成冻结范围内的 reference -> composition 中间层，而且这次不是再增加一批文字版“设计经验”。当前实现把 13 个既有、已真实检查的科研页面转成了 renderer-neutral 的结构化构图记录，绑定原有 RRL identity 与 canonical rendered-page SHA，并提供 normalized region geometry、主科学对象面积、视觉层级、对齐关系、阅读方向和 composition family。真实 CI 已通过，因此本任务可以在第一轮独立审核中关闭。

当前 handoff tip `2b4f9bd3d2d427fbfe6b764db773ac7b2881464e` 的 `reviewed-handoff/ci-summary=success`，指向 GitHub Actions run `32625441399`。

## Independent review

### 1. 产物确实从 prose lesson 前进到了机器可用的构图对象

`research_slide_composition_index.json` 当前包含 13 个 records、8 个 source IDs，覆盖 estimator/equation、statistical model、quantitative result、method/experiment flow、medical-image aligned panels、negative/model-check 与 decision/next-step 等需要。每个 record 都包含真实 `reference_id`、`source_id`、`actual_page_number`、`page_function`、`rendered_page_sha256`，同时加入 normalized `regions[]`、主 scientific-object region、面积比例、alignment groups、visual hierarchy、reading flow 与 layout family。

这解决了 018 指出的核心缺口：后续生成器不再只能知道“这页值得学习 single dominant visual”，而是可以直接取得主对象大约位于哪里、面积占比多少、哪些对象共享对齐关系、页面采用什么阅读方向。当前 representation 仍然只是上游参考对象，不越权决定最终 PPTX/Beamer layout。

### 2. 构图 family 足够小，而且来自真实科研页面

当前 vocabulary 只有 8 类：`equation-dominant`、`single-visual-dominant`、`split-visual-explanation`、`aligned-multi-panel`、`horizontal-process-flow`、`result-with-callout`、`model-check-or-negative`、`decision-or-next-step`。

这些 family 是科学任务层面的构图类型，而不是 PowerPoint 模板、品牌主题或 style preset。定义中同时写了适用条件与不适用情况，例如 `horizontal-process-flow` 明确只适用于真实数据流/实验路径，不允许把 prose 塞进 boxes；`aligned-multi-panel` 强调稳定 panel semantics，而不是缩略图网格。这个边界与 019 的 renderer-neutral 目标一致。

### 3. identity / geometry / scope 的机械约束成立

新的 validator 会核对：RRL 是否真实存在且为 `verification_status=inspected`，source/page/page-function/scientific-object/evidence-type/rendered SHA 是否与原 reference index 一致，bbox 是否在 `[0,1]`，primary region 是否存在且面积一致，family 是否在受控 vocabulary 中，以及 debug montage 是否意外嵌入 source image / binary / local path。

Presentation regression 也实际调用 validator，并检查 record/source/page/function/SHA 绑定、composition coverage、selector 的 result/equation/medical-image 查询，以及 debug montage 不含 source pixels。Executor 记录的 targeted tests 与全库测试均通过；current-tip required CI 也已经成功。

### 4. selector 没有越权成为生成器

`select_reference_compositions.py` 只根据 page function、evidence type 与 scientific-object token overlap 对 composition records 排序，并返回 reference ID、family、reading flow、primary area 和 primary bbox。它没有生成 slide、写 deck plan、选择最终 design system 或调用 Terra，因此没有提前实现后续阶段。

### 5. debug montage 符合内部 annotation QA 边界

当前 SVG 只把 13 个 record 的 normalized region boxes、role labels、primary region、family 与 reading flow 可视化，不嵌入原始 slide screenshot、论文 figure、医学图像或品牌资产。它足以让 Reviewer 快速检查记录是不是形成合理的构图结构，同时不会把 source visual identity 变成可复制模板。

### 6. 没有把旧 synthetic benchmark 升格为 gold exemplar

13 个 records 均来自既有 inspected reference library；019 没有使用 016/017 synthetic benchmark 页面做 exemplar，也没有扩 source corpus、修改 active `research-presentations/SKILL.md`、Terra rubric、PPTX/Beamer renderer 或 Bridge Kit。长期 one-shot quality 目标没有被提前宣告完成。

## Non-blocking note

本轮所有 seed records 都使用 `rendered_page_annotation`。报告说明少数 PDF 在当前环境重新渲染时可能与历史 canonical PNG hash 不同，因此 committed record 仍绑定原 reference index 的 canonical `rendered_page_sha256`。这不违反当前冻结 Plan，因为 record identity 仍与已 inspected RRL 完全一致，而且 geometry 来自同一真实页面的重新渲染/人工检查；但下一阶段若需要像素级 reference comparison，应该显式使用可复现、实际提供给视觉 reviewer 的 reference render identity，而不能假设不同 renderer 产生的 PNG 字节一致。

## Final assessment

019 冻结范围内没有剩余 blocker，可以关闭。

这只证明 reference library 已经具备可查询的 composition representation；它仍不能证明生成器会真正利用这些构图、会探索多个设计方向、会相对比较真实 reference，更不能证明 one-shot deck 已成熟。下一 bounded task 应开始把 composition records 真正用于内部 multi-candidate design search，但仍不应直接跳到最终真实 holdout。
