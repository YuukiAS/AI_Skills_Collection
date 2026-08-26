---
schema: AI_BRIDGE_REVIEWED_PLAN_V1
task_key: 030_stage3_visual_recovery
decision: PLAN_FROZEN
---

# 030 Stage 3 Visual-Maturity Recovery — Plan

## Frozen decisions

本任务是 027 在 review limit 后的质量保持 recovery，不是 027 的第三轮 review。027 已通过的 Stage 3 基础能力全部视为冻结资产；本任务只修 fresh Terra 已明确定位的四个未成熟 layout primitive。

保持 Program Goal 的最高视觉标准：不得为了进入 Stage 4 而接受不可读 plot、generic card/arrow、假 image zoom 或模板化 future-work 页面。不得扩大 Stage 2 corpus，也不得改变 exact CUHK production contract。

本任务必须真实启用 Bridge Kit task-local Visual Review contract：`CURRENT.visual_review_required=true`，manifest/evidence 均使用 030 自己的 repository-relative task-local path。缺 visual evidence 时只等待，不消耗 review round；禁止再次依赖 repository-level 固定 manifest vars 或人为创建 dispatch recovery。

## Implementation scope

### 1. Preserve accepted Stage 3 capabilities

以下 027 能力不得重做、降级或改回低级 fallback：

- canonical exact CUHK Beamer source identity 与真实 xelatex compile/render；
- normal Stage 2 selector -> gold recipe -> CUHK content-space resolver -> emitted TeX 链；
- source-derived geometry mutation 会真实改变 resolved/emitted geometry；
- capacity 不匹配触发 `SPLIT_REQUIRED`，不退回 generic layout；
- `slide_2_statistical_model` 的 native LaTeX model page；
- `slide_5_negative_result` 当前通过的 negative-evidence layout；
- audience-facing 页面不泄漏 RRL/gold/QA/provenance/recipe 等内部元语言。

对 slide 2 与 slide 5 不做有意视觉重设计。重新生成后若其像素 identity 变化，RESULT 必须解释原因；若无必要应保持现有通过结构。

### 2. Quantitative result — presentation-native result figure

修复 027 `slide_3_real_data_application` 的投影可读性 blocker。不能继续只扩大 raster 外框。

必须建立可复用的 result-figure path，使下列元素由 presentation-scale contract 直接控制：

- axes / tick labels；
- facet labels；
- method legend；
- nominal/reference line；
- point/interval annotation 与关键 callout；
- caption 与图本体之间的语义绑定。

优先使用 native/vector redraw 或基于原始数值的 presentation-native 重排。若现有 raster 无法安全达到投影尺度，应重绘或触发 `SPLIT_REQUIRED`；禁止继续缩放带小字 raster。

当前 regression 的科学语义与数值不允许为了视觉效果被改写。颜色/符号必须有完整、邻近、可读的 method mapping，不能只靠远端 caption 猜测。

### 3. Experiment design — typed scientific hierarchy/relations

修复 `slide_4_experiment_design`。禁止继续使用“四个浅色矩形卡片 + 箭头”的 generic workflow primitive。

建立可复用的 experiment-design primitive，图形结构本身必须让听众读出：

- center / subject 层级；
- DGP 或设计因素，例如 cluster count、ICC、balance/imbalance；
- procedure / method branches；
- evaluation endpoints，例如 coverage / width / bias；
- typed relations 的真实方向。

允许使用分层树、分支实验结构、factor-to-procedure-to-endpoint map 等 scientific relation geometry，但不得用大块同质卡片把关系隐藏在文字里。每条 connector 必须有真实科研关系；不得出现 source-like `centers -> subjects` audience text 代替图形关系。

### 4. Medical comparison — real same-case error crop/zoom

修复 `slide_6_medical_image_comparison`。必须把“error zoom”从文字说明变成真实 image primitive。

要求：

- input / GT / prediction / error 来自同一病例、同一坐标系；
- 从同一病例真实 error ROI 坐标裁剪 crop/zoom；
- 原图与 zoom 之间有可理解的 callout/ROI 关系；
- TP / FP / FN legend 邻近 overlay，投影尺度可读；
- lesion/error 必须达到可检查面积，不能只看到大图里一个小点；
- 若一个页面无法同时保证上下文和 ROI 可检查性，使用 medical-specific split/zoom layout 或 `SPLIT_REQUIRED`，不得用文字框冒充放大图。

不得制造与原 panel 无关的新病例或伪造 error pattern。

### 5. Next experiment — evidence-to-decision research reasoning

修复 `slide_7_next_experiment`。必须继续通过正常 Stage 2 selector 消费 discussion/next-experiment compatible gold，优先保持 `GSC-018` 在兼容查询下的真实 runtime role；不得 force-id 或 score override。

建立专门的 evidence-to-decision executable layout，至少显式组织：

- 当前失败/限制证据；
- 下一轮要操纵的关键因素或 sampling/batch strategy；
- 并列 comparator arms / procedures；
- 预期诊断量或 quantitative endpoints；
- 清楚的 decision criterion / go-no-go 规则。

关系必须由 typed scientific relations 与 quantitative endpoints 驱动，而不是三个相似卡片串联。观众应从结构直接理解“为什么做下一实验、比较什么、看什么指标、什么结果会改变决策”。

### 6. Shared implementation requirement

四类修复必须进入现有 Stage 3 共享 resolver/layout system，成为可复用 primitive 或受约束 layout family；不能只在 030 regression generator 中写死单页坐标。

仍由 gold recipe/source-derived composition 约束正文 content area；新 primitive 可以对 job-specific geometry 做必要解释性变换，但必须保留 runtime trace，说明哪些 source-derived fields 被消费、哪些 job-specific rule 被应用。

新增 deterministic regression，至少检查：

- result figure 不再走旧不可读 raster-only path；
- experiment design 不再实例化旧 generic relation-card primitive；
- medical error zoom 真实引用 same-case crop/ROI image asset，而不是 text box；
- next experiment 不再实例化旧 generic card workflow，并保留正常 gold selection；
- audience-meta leak gate；
- capacity/SPLIT_REQUIRED 不回归；
- slide 2 / slide 5 已通过能力不回归。

### 7. Real render and task-local Visual Review contract

Executor 必须生成真实 Stage 3 regression：

- exact CUHK `.tex` source；
- compiled PDF；
- rendered PNG；
- mechanical QA / trace；
- 030 task-local `visual_inputs.json`。

视觉 manifest 固定路径：

`results/030_stage3_visual_recovery/visual_review/visual_inputs.json`

视觉 evidence 固定路径：

`results/030_stage3_visual_recovery/visual_review/VISUAL_REVIEW.json`

manifest 必须：

- `workflow_type=reviewed_handoff`；
- `task_key=030_stage3_visual_recovery`；
- identity bindings 绑定本任务真实 `implementation_commit`；
- 包含六个主要内容页的当前 rendered PNG identity；
- rubric 明确要求逐页检查真实像素、投影可读性、scientific-object prominence、generic-card/AI-template smell、数学/plot/image语义、medical same-case/ROI、next-experiment evidence-to-decision reasoning；
- top-level package assessable/PASS 不替代 item-level mature-bar judgement。

建议执行顺序：先完成 Plan-owned code/render 并创建 implementation commit；随后用该 SHA 生成 task-local manifest，再写 RESULT/CURRENT handoff。Watcher 发布后，真实 CI 先结算；Planner 将任务推进到 visual-review eligible 阶段后，029 已验证的 push resolver 应自动找到唯一 030 manifest，GitHub Actions 使用 secret 运行 Terra 并写回 evidence。缺 evidence 时等待，不消耗 review round。

## Acceptance and regression gates

Planner 只有在以下全部成立时才可 PASS 030，并据此关闭 Stage 3：

1. 027 已通过的 exact CUHK、selector/recipe、geometry transfer、`SPLIT_REQUIRED`、model page、negative-result page 与 anti-meta 能力保持；
2. quantitative result 使用 presentation-native readable figure path，图内文字、legend、reference line、annotation 在真实 rendered pixels 上可读；
3. experiment design 的结构本身表达真实层级、因素、procedure branches 与 endpoints，不再是 generic card/arrow；
4. medical comparison 包含真实 same-case ROI crop/zoom、overlay 与邻近 TP/FP/FN legend，病灶/error 在投影尺度可检查；
5. next experiment 通过正常 compatible gold path，并形成 evidence -> manipulation/comparator -> endpoint -> decision criterion 的科研推理视觉；
6. 四类新能力是共享 executable primitives/layout families，不是 030-only 坐标硬编码；
7. 六个主要内容页均进入同一 030 fresh visual manifest，并有与当前 identity 一致的 Terra evidence；
8. 必须逐项读取六页 item/page-level judgement 与 observations；六个主要内容页全部达到 mature doctoral research-group-meeting / strong conference-talk bar，不能用 top-level PASS 替代；
9. deterministic tests、full tests、skills/marketplace/Reviewed Handoff validation、真实 compile/render/mechanical QA 与 real GitHub CI 全部通过；
10. 030 task-local push discovery -> Terra -> evidence writeback 正常工作，不再需要手工 workflow_dispatch recovery；
11. 没有扩 Stage 2 corpus、修改 027/028/029 历史、恢复 023、开始 Stage 4/5 或降低 Program Goal。

若 fresh Terra 仍发现某一类 primitive 未达到 mature bar，按普通 Reviewed Handoff review budget 做最小返修；不得因为“其他页都通过”而降低该页质量标准。

## Stop condition

当四类 blocker 均有 shared executable mechanism、真实渲染、fresh task-local Terra item-level PASS，且六个主要内容页全部达到成熟门槛、CI/validation 通过时停止。Planner 独立 PASS 后，Stage 3 首次整体 PASS，并按 Program Goal 发送一次 Stage 3 PASS notifier，然后创建 Stage 4 独立 bounded task。

## Out of scope

030 不得：

- 伪造 027 REVIEW_3 或改写 027/028/029 terminal history；
- 新增/重审 Stage 2 gold 或 source scouting；
- 修改 canonical CUHK visual identity；
- 改变 Terra core/model/quality bar；
- 新造 Reviewed Handoff state machine；
- 实现完整 one-call production entry；
- 运行最终真实 statistics / medical-imaging holdouts；
- 宣告 `PROGRAM_MATURE` 或 `ONE_SHOT_QUALITY_PASS`。
