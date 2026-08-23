---
schema: AI_BRIDGE_REVIEWED_REVIEW_V1
task_key: 020_research_presentation_reference_calibrated_candidate_search
review_round: 2
decision: PASS
implementation_commit: 59147c7aff097cff91d103a8ec28d2297a4306a8
---

# GPT Review

## Decision

`PASS`。

020 第一轮指出的两个核心 blocker 已经被实质关闭，而且修复没有越出冻结范围。当前 candidate search 不再只是“先选 family、再套一套固定坐标”：selected 019 composition record 的 normalized regions 已经进入候选几何计算，`geometry_transfer` 由实际 split / scale / translate / reorder 操作产生；同时，candidate source pool 现在有明确的 scientific-job compatibility gate，医学影像 request 不再把无关 Bayesian model page 当 wildcard reference。

当前 handoff tip `0b1c3aacfd09d017ad4ca2d3d406b78b0d59d428` 的 `reviewed-handoff/ci-summary=success`，指向 GitHub Actions run `32630920085`。因此冻结 Plan 对真实 CI 的要求也已满足。

## Independent review

### 1. 真实 source geometry 已进入 candidate 计算

当前生成器不再仅根据 `layout_family` 返回一套固定 bbox。统计 request 会从 selected source 的 title / equation / primary / secondary regions 派生 equation、annotation 与 caption；医学影像 request 会从 selected source 的 image-grid / legend geometry 派生 evidence row、panel split、focus-callout 与 legend/annotation 区域。

这不是只改了 manifest 文案。回归测试直接把同一 `aligned-multi-panel` family 的 RRL-022 与 RRL-013 分别送入同一 `reference_faithful` path，并要求两个 source 的不同 primary geometry 产生不同 candidate primary bboxes。当前测试通过，说明 source bbox 已经真正影响生成结果。

实际 manifest 也与该行为一致：

- RRL-022 的 primary image grid 为 `x=.10, y=.08, w=.78, h=.76`，reference-faithful candidate 从该区域派生四个约 `w=.1755, h=.3944` 的 evidence panels；
- RRL-013 的 sample grid 为 `x=.03, y=.25, w=.94, h=.25`，alternative candidate 从该区域派生三列约 `w=.296, h=.2482` 的 panels；
- 两个候选即使 family 都是 `aligned-multi-panel`，几何仍明显不同。

因此第一轮 F-020-01 所担心的“换一个同-family reference，candidate 基本不变”已经不成立。

### 2. transfer trace 与真实几何操作一致

新的 `candidate_regions()` path 直接返回 `regions + transfers`；manifest 使用这些实际 transfers，而不是调用旧的事后推测 trace。当前 medical manifest 中，RRL-022 的 `image_grid` 到四个 evidence panels 明确记录为 `split`，RRL-013 的 dominant overlay / error sidecar 分别记录为 `scale` / `split`；统计 equation page 也记录 selected equation region 的真实 bbox 及 scale/translate 关系。

文件中仍保留一个旧 `transfer_trace()` helper，但当前 `build_candidate()` 不调用它。它属于非阻断清理项，不影响当前 manifest 的真实 transfer provenance；后续如整理 shared helper 可删除，但不值得在 020 再开返修。

### 3. compatibility gate 已阻止“离得远但不相关”的 wildcard

当前 `tokens()` 已过滤第一轮发现的通用词；更重要的是，distance 之前增加了 page-job / content-mode compatibility gate：

- `MEDICAL_IMAGE_COMPARISON` 只接受真正的 medical-image comparison record 且必须含 `medical_image` mode；
- estimator / statistical-model / theorem / derivation 类 request 要求 equation-compatible record；
- composition distance 只在通过 gate 的 pool 内排序。

当前 medical request 实际只检索到 RRL-022 与 RRL-013 两个强兼容 inspected records，三个 candidate 都只使用这两个来源；RRL-034 已从 source selection 中消失。由于兼容来源不足 3 个，controlled wildcard 合法复用 RRL-013 的真实 geometry 做 focus-callout 重组，而不是退化到无关统计模型页。这个处理符合冻结 Plan 对“兼容 family 不足时使用 alternate topology / 真实几何重组”的要求。

### 4. 三候选仍然是同内容、不同构图，而不是换色

两个 regression requests 都保持恰好三个 candidate、同一 content payload、同一 neutral preview skin。候选 preview SHA 均不同；统计 request 覆盖 equation-dominant、split visual explanation 与 source-derived reordered callout；医学影像 request 覆盖两种 source-derived aligned multi-panel geometry 与 focus-callout topology。

候选中的公式和医学影像是真实本地 scientific objects，不是空 wireframe；audience-facing text 也没有 strategy、RRL、repo path、QA/provenance 泄漏。当前 task 仍没有复制 reference pixels 到 candidate preview。

### 5. 范围边界保持

020 没有修改 active `research-presentations/SKILL.md`、Terra、Bridge Kit、PPTX/Beamer renderer 或 019 composition records，也没有偷跑 comparative review、winner selection、deck-wide design-system locking 或真实 holdout。

这点很重要：020 证明的是“有多个真正由 reference geometry 驱动的候选可供比较”，不是证明这些候选已经达到成熟科研汇报质量。

## CI

current handoff tip `0b1c3aacfd09d017ad4ca2d3d406b78b0d59d428` 的 `reviewed-handoff/ci-summary=success`，GitHub Actions run `32630920085` 成功。

Executor 记录的 candidate-manifest validator、targeted Presentation tests、全库 115 tests、skills validation、Codex marketplace validation、Reviewed Handoff validation 与 `git diff --check` 均通过。

## Non-blocking note

当前 candidate preview renderer 本身仍是 neutral regression skin，而且部分文本/图像区域仍使用圆角容器；这在 020 不构成 blocker，因为本任务明确只验证 composition search，不验证最终视觉品味。下一阶段必须把候选与真实 inspected reference renders 放在同一个相对审查框架里，防止“候选之间确实不同”被误当成“候选已经好看”。

## Final assessment

020 冻结范围内没有剩余 blocker，可以关闭。

下一 bounded task 应进入 **comparative reference-calibrated visual review**：对每个 scientific job，把 020 的三个 generated candidates 与 2–4 个匹配的真实 inspected reference renders 一起送给独立视觉 reviewer，使用匿名 item IDs 和真实 render identity 做相对判断，并允许结论是“所有 candidate 都明显落后于 reference”，而不是强制从三个候选中挑一个 winner。

长期 `PROGRAM_MATURE=false`，`REFERENCE_CALIBRATED_ONE_SHOT_QUALITY` 仍远未完成。
