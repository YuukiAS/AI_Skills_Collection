# 013 Presentation TODO Consolidation — Request

本任务是 Research Presentation Corpus & Quality Program 当前 improvement cycle 的 Phase A。先系统整理 `research-presentations/TODO.md`，把历史经验与当前 active Presentation 规则、视觉 QA、archetypes、deck-plan contract、generator 行为和 regression tests 对齐；在这一步完成独立复核之前，不扩新的 source corpus，不开始新的 statistical/medical benchmark，也不直接返修当前 Terra 四页 regression。

每个 TODO 条目或可独立执行的规则都必须归入且只归入四类之一：`ALREADY_IMPLEMENTED`、`PROMOTE_NOW`、`KEEP_BACKLOG`、`DUPLICATE_OR_SUPERSEDED`。分类必须有当前实现/测试/更强规则的真实依据，不能为了清单好看把历史经验删除，也不能把所有 `[ ]` 机械实现。

本任务只允许做 TODO consolidation、少量已经由 Planner 冻结的高价值通用规则提升、对应 regression tests，以及必要的 source/generated 同步。不得顺手扩 source registry / inspected page library，不得新增 benchmark，不得重做 Presentation 插件架构，不得处理当前 Terra slide 1–3 的具体 generator repair；这些属于后续独立 bounded task。