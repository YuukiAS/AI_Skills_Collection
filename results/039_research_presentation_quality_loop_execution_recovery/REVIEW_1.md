---
schema: AI_BRIDGE_REVIEWED_REVIEW_V1
task_key: 039_research_presentation_quality_loop_execution_recovery
review_round: 1
decision: REVISE
implementation_commit: 7470884044ce51bcb204222df385e1e8dc619d94
---

# GPT Review

## Decision

REVISE。

039 的核心恢复机制已经取得真实新增证据，不能因为最后一个包装层问题否定已完成部分：当前 GitHub CI 已真实通过；quality loop 在 non-holdout stress bundle 上真实消费了缺少 `repair_intent` 的结构化 finding，选择了冻结的五类 repair directive，并将 repair count 从 0 推进到 1；repair 前后的 render-input identity 与 rendered-pixel identity 都发生变化。Fresh task-local Terra 与 implementation `747088404...`、当前 repaired render-input / pixel identity 严格绑定后，六张 substantive page 全部逐项 PASS，模型、结果、实验设计、负结果、下一实验和医学影像页均达到既有投影可读与 source-specific bar。

当前唯一 blocking evidence 来自 deck contact sheet：标题页仍显示 `Stage 4 Quality Loop Repair Stress Update`。Terra 明确把这句话判为 audience-facing QA/workflow/process leakage；contact sheet 因此为 `BLOCKED`，虽然同一条 item review 同时确认整套 deck 的构图交替、密度节奏、主 workstream 连续性和独立医学 workstream 切换都已经成熟。由于 039 的冻结 acceptance gate 明确要求所有 stress pages **和 contact sheet** item-level PASS，并要求 audience body 不泄漏内部制作语言，因此当前实现不能 PASS。

## Blocking findings

### 1. Non-holdout stress bundle 的 audience-facing title 自身仍是工程测试语言

**Plan / regression basis**

- Program Goal 禁止 audience-facing workflow / QA / implementation 制作语言。
- 039 Frozen decisions 与 acceptance gates 要求 audience internal/meta copy 不进入最终像素，并要求 fresh Terra 对所有目标页和 `deck_contact_sheet` 达到成熟组会标准。
- 039 只允许使用 non-holdout stress material；本轮不应借返修读取或调优 038 的 brms / MedSAM 内容。

**Observed evidence**

- Fresh Terra 的六张 substantive page 全部 `PASS`，说明本轮真正要验证的 page-level repair 机制已经能产生可接受像素；尤其结果页中原先故意放入的 `QA workflow/source bundle note` 已不再出现在 audience-facing slide。
- 唯一 blocking finding `F-001` 指向 `deck_contact_sheet`：标题页可见 `Stage 4 Quality Loop Repair Stress Update`，Terra 要求把它改成描述 clustered-interval 与 segmentation research content 的科研标题，去除 Stage / Quality Loop / process 语言。
- 独立读取 stress fixture 确认该字符串直接来自 `metadata.title`；同一 fixture 已有 source-grounded subtitle `Uncertainty calibration across clustered data and segmentation stress cases`，所以这里不存在需要新造科学 claim 的歧义。

**Minimal repair**

只修 non-holdout stress fixture 的 audience-facing metadata，不扩大 production architecture：

1. 将 shared 与 `plugins/codex` mirror 中该 stress bundle 的 `metadata.title` 改成由现有 subtitle / research content 直接支持的科研标题，例如 `Uncertainty Calibration Under Clustered Dependence and Segmentation Stress`，不得出现 Stage、Quality Loop、workflow、fixture、QA 等制作语言。
2. 保留当前 subtitle、source material、evidence、page jobs、医学像素和五类 stress finding。特别要保留结果页中故意设置的内部 QA annotation，使 `SANITIZE_AUDIENCE_COPY` 仍被真实触发；不得通过删除该 stress case 来换 Terra PASS。
3. 不修改 038 brms / MedSAM output，不把两篇失败 holdout 重新用于 tuning；不新增 repair cycle，不降低现有 fail-closed contract。
4. 可增加一个窄回归，确保 non-holdout acceptance fixture 的 audience-facing metadata 本身不包含现有 forbidden production terms，防止测试包装再次污染视觉验收。

这次返修不要求为了标题页另造新的 title-repair state 或泛化状态机。当前 blocker 来源是 task-owned non-holdout fixture metadata，而不是来自真实 paper 的不可控标题；直接把测试输入恢复为科研 audience-facing metadata 是更小且不降低质量的闭环。

**Required closure evidence**

- 重新跑正常 one-call production + 同一单次 bounded repair；每次 invocation 内 `repair_cycle_count <= 1`，repair 前后 source bundle identity保持不变。
- 五类 repair stress 仍被执行，unknown / ambiguous finding 仍 fail closed；shared/plugin parity 与真实 GitHub CI PASS。
- 新 render / contact-sheet identity 与 fresh task-local Terra 绑定；六张 substantive page不得回归。
- `deck_contact_sheet` 必须 item-level `PASS`，并明确没有 audience-facing Stage / Quality Loop / QA / workflow 制作语言，且仍达到 mature doctoral research-group-meeting / strong paper-talk bar。

## Non-blocking notes

- `NEXT_EXPERIMENT` 当前 repair trace 以 `SWAP_COMPATIBLE_GOLD_LAYOUT` 名义记录，而 runtime 仍保留同一个正常 selector 选出的 GSC-018，并消费 `compatible_layout_reflow_hint` 完成 source-faithful reflow。Frozen Plan 同时允许 process/next-step collision 使用“compatible gold swap **或** 已有、可证明 source-faithful 的 compatible reflow”；本轮 fresh Terra 对该页已 PASS，且没有 force-gold / score override，因此这一点不作为新的 blocker。但后续 trace 命名若容易让审阅者误以为发生了实际 gold swap，可在不改变行为的情况下作为维护性 backlog 澄清。
- 039 PASS 后仍只能证明 generic quality-loop recovery 完成，不构成 Stage 5 PASS。下一次 Stage 5 必须换两篇新的 unseen real papers。
