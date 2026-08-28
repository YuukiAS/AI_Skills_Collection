---
schema: AI_BRIDGE_REVIEWED_REQUEST_V1
task_key: 032_research_presentation_storyline_coherence_recovery
---

# 032 Research Presentation Storyline Coherence Recovery — Request

## Why this task exists

031 已经建立普通 `research-presentations` one-call production entry，并在第二轮关闭 canonical CUHK rendered identity 与 medical GT/Prediction/Error semantic inspectability 两个 blocker。真实 CI 与 fresh task-local Visual Review 均绑定当前 implementation。

031 第二轮唯一剩余 blocker 是 deck-level storyline coherence：当前 engineering bundle 同时含 clustered interval-calibration workstream 与 synthetic segmentation-robustness workstream，但 normal production ordering 将 medical image page 插在 clustered-coverage failure 与其 next experiment 之间，没有明确 workstream boundary，导致每页局部质量成立但整套 deck 像 benchmark 拼盘。

031 已合法达到两轮 review 上限，必须保留 `REVIEW_LIMIT / REVISE` 历史，不得创建 `REVIEW_3`。依据 Program Goal 的 Quality-Preserving Continuation Policy，本任务作为新的 bounded recovery，只关闭这个已明确的 storyline blocker。

## Product outcome

普通 one-call production route 在输入包含多个彼此没有 source-supported 因果关系的 research workstream 时，应能把同一 workstream 的 page jobs 组织成连续科研故事，并用清楚、source-faithful 的 audience-facing transition 标识 workstream 切换，而不是机械按 source section 顺序把独立页面插进主故事。

对于当前 public-safe engineering bundle，clustered interval-calibration sequence 应保持连续，segmentation comparison 作为明确标识的第二 workstream；不得虚构 segmentation 与 interval coverage 之间不存在的科学关系。

## Scope

本 recovery 只允许：

- 保留 031 已接受的一次调用入口、source-fidelity map、normal gold selection / recipe / Stage 3 layout consumption、exact CUHK compile/render、visible CUHK identity、medical semantic overlays 与 anti-meta leakage；
- 在 normal production storyline/page-job orchestration 中增加最小的 source-derived workstream grouping / ordering / transition contract；
- 使用当前 031 engineering bundle 作为 regression input，通过同一个 production entry 重新生成完整 deck；
- 生成新的 runtime storyline trace、`.tex + PDF + PNG` 和 task-local visual-review manifest/evidence；
- 增加 deterministic regression，证明 multi-workstream grouping 不是按本 fixture 的固定页号、标题或 `GSC-*` ID 写死。

本 recovery 不允许：

- 改写 031 REVIEW/CURRENT/FINAL_REPORT 历史；
- 重做已经通过的六类 Stage 3 page layouts；
- 修改 Stage 2 gold corpus 或 force gold IDs；
- 为了“连起来”发明 source 不支持的医学-统计因果关系；
- 实现完整 deck-rhythm scoring 或 bounded automatic repair loop；
- 使用 Stage 5 holdout papers；
- 宣告 Stage 4、`PROGRAM_MATURE` 或 `ONE_SHOT_QUALITY_PASS` 完成。

032 PASS 只表示 031 的 storyline-coherence blocker 被新的 bounded recovery 关闭。完整 Stage 4 仍需后续独立任务建立 deck-level rhythm review 与 bounded quality-repair loop。
