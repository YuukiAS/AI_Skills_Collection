---
schema: AI_BRIDGE_REVIEWED_REQUEST_V1
task_key: 033_research_presentation_deck_rhythm_quality_loop
---

# 033 Research Presentation Deck Rhythm + Bounded Quality Loop — Request

## Why this task exists

Stage 4 已经通过 031/032 建立了 normal one-call production entry、source fidelity、gold/layout consumption、exact CUHK compile/render、page-level visual review 与通用 multi-workstream storyline grouping。剩余的 Stage 4 合同不是再修某一页，而是让 normal production route 能在整套 deck 尺度检查视觉节奏与页面序列，并在发现明确质量 blocker 时进行有限、可追踪、source-faithful 的修复，而不是把第一次生成结果直接交付。

## Product outcome

完成后，普通 `research-presentations` production path 应具备一个真正可执行的 deck-level quality loop：

- 对完整 rendered deck 做 sequence/contact-sheet 级审查，而不只逐页判断；
- 识别跨页节奏、信息密度、重复布局、突然的视觉/主题跳变、过密/过空、transition 失衡等 deck-level blocker；
- 将 reviewer finding 转成受限的修复动作；
- 最多执行有限次数的 repair + rerender + rereview；
- 如果候选仍低于成熟 bar，明确 FAIL/no-winner，不从低质量结果中强制挑一个；
- 全程保留 source fidelity、normal gold retrieval、Stage 3 layouts 与 exact CUHK identity。

## Scope

本任务只允许在现有 normal production path 上增加 deck-level rhythm review 与 bounded repair-loop contract，并用当前 Stage 4 engineering bundle 做工程回归证明。

不得：

- 使用 Stage 5 两篇最终 holdout paper；
- 引入 task-specific 033 deck generator；
- 绕过 normal `research-presentations` production entry；
- 修改 Stage 2 gold admission bar 或 Stage 3 scientific layout semantics；
- 为了“修节奏”改写 source claims、结果、符号、图像语义或虚构跨 workstream 科学关系；
- 把 synthetic/engineering regression 当作最终 Program PASS。

033 PASS 后，Planner 才可判断 Stage 4 的工程闭环是否整体完成并是否可以进入 Stage 5 的两个真实 paper holdout。
