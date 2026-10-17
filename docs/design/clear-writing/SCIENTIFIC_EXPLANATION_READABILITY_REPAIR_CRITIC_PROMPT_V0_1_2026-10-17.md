你现在担任 Clear Writing 最小 successor repair 的独立 Critic。不要重新研究或重做 Clear Writing 架构。

Active Review Context：

- target_repo: `YuukiAS/AI_Skills_Collection`
- target_plugin_or_domain: `writing-style / Clear Writing / response-clarity`
- design_topic_or_task_key: `clear-writing--scientific-explanation-readability-repair`
- source_branch_or_ref: `reviewed/clear-writing--scientific-explanation-readability-repair`
- review_stage: `execution-ready successor repair`
- package content commit: `19e1122fd90fb748f85fb552b4a8734cea035a32`
- predecessor review-limit commit: `4eaa6481ee7202779286e65f6f832bbb235f6916`
- predecessor task: `clear-writing--cross-surface-language-layer`
- current successor state: `PLAN_REQUESTED / RUN_GPT_PLANNER`

用户已经明确决定继续修。不要把“旧任务 review budget 已用尽”当成新 blocker；本 successor 就是 Review_2 要求的人类决定后的最小新周期。

先读取 latest main 的：

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/plugin-todos/writing-style.md`

再读取前序任务：

- `automation/reviewed_handoff/tasks/clear-writing--cross-surface-language-layer/PLAN.md`
- `results/clear-writing--cross-surface-language-layer/REVIEW_2.md`
- `results/clear-writing--cross-surface-language-layer/FINAL_REPORT.md`

再审本 successor package：

- `automation/reviewed_handoff/tasks/clear-writing--scientific-explanation-readability-repair/REQUEST.md`
- `automation/reviewed_handoff/tasks/clear-writing--scientific-explanation-readability-repair/CURRENT.json`
- `docs/design/clear-writing/SCIENTIFIC_EXPLANATION_READABILITY_REPAIR_PLAN_V0_1_2026-10-17.md`
- `docs/goals/CLEAR_WRITING_SCIENTIFIC_EXPLANATION_READABILITY_REPAIR_GOAL_V0_1_2026-10-17.md`
- `docs/operations/prompts/CLEAR_WRITING_SCIENTIFIC_EXPLANATION_READABILITY_REPAIR_KICKOFF_V0_1_2026-10-17.md`
- `results/clear-writing--scientific-explanation-readability-repair/REAL_WEB_KNOWN_REGRESSION_BANK_V2.md`

本轮只需要判断这份最小 successor 是否 execution-ready。重点检查：

1. **是否真正只修 Review_2 的两个缺口。**
   - 语义/推理单元成段 + 整篇碎片化检查；
   - 陌生科研方法/术语/多重下标对象先建立不越权 reader mental model，再进入正式术语/公式；信息不足时不得猜科学定义。
   不允许借机新增 skill/router、改其他 writing skill、改 Research Authoring / Presentations，或重新设计 Clear Writing。

2. **9 组真实样本是否全部被正确使用，而不是只挑失败样本。**
   `REAL_WEB_KNOWN_REGRESSION_BANK_V2.md` 应覆盖：
   - KR-WEB-01 长回答淹没判断；
   - KR-WEB-02 伪澄清/建议漂移/自我检讨；
   - KR-WEB-03 具体解释 + 例子 + 证据边界正例；
   - KR-WEB-04 伪结构化；
   - KR-WEB-05 综合膨胀成方案文档；
   - KR-WEB-06 一句一段/标题/公式碎片化；
   - KR-WEB-07 非必要英文概念栈及 10/17 复发；
   - KR-WEB-08 复杂科研方法解释正例；
   - KR-WEB-09 三方案比较正例 + 陌生术语/多重下标对象反例。
   
   检查是否做到：
   - 不复制私人科研原文，只冻结“好在哪里 / 坏在哪里”；
   - 全部是 known regression / positive control，不冒充 G7；
   - 正例是硬保护，防止“清晰 = 强制短答”。

3. **样本使用顺序是否避免过拟合。**
   - 旧 RW-WEB-01..05 与四组 should-not-change 复用既有 fixtures/evidence；
   - 新增 KR-WEB-06..09 在 production edit 前建立 public-safe 泛化 fixture 并跑现有候选 baseline；
   - 修复后再完整跑 KR-WEB-01..09；
   - 不用 DII 名词、论文名、私有公式或项目答案做 selector；
   - 不用关键词 grep、英文比例、段落/标题/公式数量阈值做 qualitative PASS oracle。

4. **KR-WEB-07 的英文问题是否被正确限界。**
   Review_2 已明确判断“普通英文中文化 / 精确名称保留”合同已经存在，只缺新增 DII runtime evidence。本 successor 应主要验证并在必要时加强现有 final-output check，不应制造第三套英文词表机制。

5. **reader mental model 是否保真而不越权。**
   Plan 应明确：
   - 只说明 domain/source 已建立的对象类型、层级、已知/估计状态、用途；
   - 多重下标只解释已有定义；
   - 信息不足时明确“对象定义不足”，而不是由 Clear Writing 猜出科学含义；
   - 正式术语、符号、公式保持精确。

6. **是否保护复杂长解释。**
   KR-WEB-03、08、09 的正向部分必须证明：
   - 必要例子、真实对照、因果解释、公式直觉、限制和不确定性不会被删掉；
   - 真正复杂推导仍允许标题、列表、展示公式；
   - 完整 report / execution prompt / machine output 不受 conversation-style 压缩。

7. **工程范围与验收是否够完整但不过重。**
   - production source 只改 `response-clarity` 和直接相关 eval/tests/generated mirror；
   - full tests、Marketplace check、source/generated parity、GitHub CI 都保留；
   - 最终独立 Reviewer 必须实际读 9 组输出；
   - Web A/E、B/C、G7、PIE 0.2、release 仍明确留到后续，不塞进本 successor。

请给 `PASS` 或 `REVISE`。

若 `REVISE`：
- 只列真正阻断 Codex 执行的最小 finding；
- 不要求新架构研究；
- 给 Planner 可直接继续的完整修订 prompt。

若 `PASS`：
- 明确：
  `APPROVED_PLAN_PATH`
  `APPROVED_GOAL_PATH`
  `APPROVED_KICKOFF_PATH`
  `APPROVED_PACKAGE_COMMIT=19e1122fd90fb748f85fb552b4a8734cea035a32`
- 返回 `NEXT_HANDOFF=PLANNER`；
- 不修改 successor 的 `CURRENT.json`；
- 给 Planner 一段最小 prompt，要求其把批准内容 materialize 到 task-local `PLAN.md`，合法执行 `PLAN_REQUESTED -> PLAN_FROZEN`，保持 `plan_revision=0`、`review_round=0`，然后由 Planner逐字交付已审过的 Kickoff 给 Codex。

本 Critic PASS 只表示这个最小 successor 可以执行，不表示 9 组回归、ChatGPT Web、G7 或 release 已经 PASS。
