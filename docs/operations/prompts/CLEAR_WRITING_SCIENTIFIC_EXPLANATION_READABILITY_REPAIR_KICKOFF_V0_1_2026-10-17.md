继续 Clear Writing 的最小后续修复任务，不要重开架构研究。

仓库：`YuukiAS/AI_Skills_Collection`
任务：`clear-writing--scientific-explanation-readability-repair`
分支：`reviewed/clear-writing--scientific-explanation-readability-repair`

先读取并严格执行：
- `docs/design/clear-writing/SCIENTIFIC_EXPLANATION_READABILITY_REPAIR_PLAN_V0_1_2026-10-17.md`
- `docs/goals/CLEAR_WRITING_SCIENTIFIC_EXPLANATION_READABILITY_REPAIR_GOAL_V0_1_2026-10-17.md`
- `results/clear-writing--scientific-explanation-readability-repair/REAL_WEB_KNOWN_REGRESSION_BANK_V2.md`
- 当前 task 的 REQUEST / PLAN / CURRENT
- 前序任务 `clear-writing--cross-surface-language-layer` 的 REVIEW_2 / FINAL_REPORT
- 本 successor package 的独立 Critic PASS

这轮只修两个 Reviewer blocker：

1. 普通复杂科研解释按完整语义/推理单元组成自然段；避免一句一段、过密标题、短公式与解释无价值拆分；最终检查整篇碎片化，但禁止固定段落/标题/行数阈值。
2. 新方法、陌生术语、数学对象尤其多重下标对象第一次出现时，在已有科学事实范围内先解释“它是什么、处于什么层级/单位、为什么需要、后面拿来做什么”；再给正式术语/公式。信息不足时明确缺定义，不得猜科学含义。

执行顺序：

1. `git fetch origin`，普通 non-force merge latest `origin/main` 到当前 successor branch；禁止 rebase/force。
2. 复用原 RW-WEB-01..05 和四组 should-not-change fixtures，不重新发明。
3. production edit 前，为 KR-WEB-06..09 创建 public-safe 泛化 fixtures，不使用 DII 名词、私有公式、论文专名或项目答案；先用继承的现有候选跑 baseline 并保存完整输出。
4. 只修改 `skills/writing/core/response-clarity/SKILL.md` 与直接相关 eval/tests；generated mirror 只通过正式 generator 更新。
5. 若 KR-WEB-07 的非必要英文仍失败，只在现有“普通概念中文化 / 精确身份保留”合同上做最终输出检查，不新增词表、英文比例或第三套语言机制。
6. 修复后完整运行 KR-WEB-01..09。必须同时保护 KR-WEB-03、08、09 的正向深度：必要例子、真实对照、因果解释、公式直觉、限制和不确定性不得被机械压短。
7. 运行四组 should-not-change：
   - 完整 report / execution prompt / contract；
   - 真正有分支/逐步执行价值的结构；
   - pure JSON/YAML/code/raw log exact output；
   - 正式名称、稳定缩写和机器字符串。
8. 运行 focused tests、skills validate、source/generated parity、Marketplace write/check + second clean check、full repository tests、`git diff --check`。
9. 全部 PASS 后 commit/push，进入 required zero-paid GitHub CI。
10. CI PASS 后交独立 Reviewer；Reviewer 必须实际读取 9 组最终输出，不能只看 RESULT 摘要。

严禁：
- 新 skill/router/state machine；
- PIE 0.2；
- ChatGPT Web account/plugin mutation；
- G7 fresh；
- paid review；
- Research Authoring / Presentations product change；
- DII-specific hard-code；
- 固定字数、段落、标题、公式数、英文比例或关键词规则。

如果这两个 blocker 不能在现有 `response-clarity` 边界内通用解决，停止并回 Planner，不自行扩大范围。
