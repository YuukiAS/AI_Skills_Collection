# Research Presentation Corpus & Quality Program Goal

长期目标：逐轮建设 research/statistics/biostatistics/medical-imaging presentation reference corpus，并把它接入可编辑 PPTX 生成、真实渲染、机械 visual QA、外部 Planner 复核闭环。

本文件不是 Planner PASS，也不是成熟度声明。当前只允许有限执行 round，目标是建立干净分层、真实 inspected page library、4 页 regression packet 和可复核证据。

## Program Goal

- Source Registry、Inspected Page Library、Synthesized Knowledge 三层分开维护。
- page-level reference 只能来自实际打开或渲染过的缓存页面。
- statistics/biostatistics primary candidates 逐轮扩充，未检查 URL 保持 backlog。
- generator 只能输出 source artifacts 和 render evidence。
- mechanical reviewer 只能给 `MECHANICAL_VISUAL_REVIEW`，不能替代外部 Planner 的学术质量判断。

## Maturity Criteria

`PROGRAM_MATURE` 只能在未来 round 中由外部 Planner 基于多轮证据确认。至少需要：

- 多领域、多人、多机构 primary research decks 覆盖充分；
- 每个核心 page function 有多个 inspected page examples；
- regression deck 多轮真实 PPTX render 稳定；
- mechanical QA 与 Planner 学术判断边界稳定；
- current round history 无未关闭 integrity 问题。

当前 round 结论只能是 `READY_FOR_EXTERNAL_PLANNER_REVIEW`。
