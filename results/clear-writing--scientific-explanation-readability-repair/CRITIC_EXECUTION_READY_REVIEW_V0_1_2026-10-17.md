# Clear Writing 普通科研解释可读性最小修复 v0.1 — 独立 Critic execution-ready 审查

- target_repo: `YuukiAS/AI_Skills_Collection`
- target_plugin_or_domain: `writing-style / Clear Writing / response-clarity`
- design_topic_or_task_key: `clear-writing--scientific-explanation-readability-repair`
- source_branch_or_ref: `reviewed/clear-writing--scientific-explanation-readability-repair`
- review_stage: `execution-ready successor repair`
- reviewed package commit: `19e1122fd90fb748f85fb552b4a8734cea035a32`
- predecessor review-limit commit: `4eaa6481ee7202779286e65f6f832bbb235f6916`
- latest main checked: `adb06823b95c45e5e12ac1258ca73ebf8f1846d3`
- latest Bridge Kit main checked: `a03742ed07d00d36e3436f64a17e92c40a51064e`
- decision: **PASS**
- new blocking findings: **NONE**

本 PASS 只批准这个最小 successor 进入 Planner 冻结与后续 Codex 执行，不代表 9 组回归、ChatGPT Web、A/E、B/C、G7、PIE 0.2 或 release 已通过。本 Critic 不修改 successor `CURRENT.json`。

## 1. Review_2 两个缺口是否被严格限界

PASS。

`REQUEST.md`、Plan、Goal 和 Kickoff 都把 production repair 限定为 Review_2 的两个 finding：

1. 普通复杂科研解释按完整语义/推理单元组织自然段，并在整篇层面检查一句一段、过密标题和无价值公式碎片化；
2. 新方法、陌生术语和数学对象，尤其多重下标对象，在已有 domain/source 事实范围内先建立 reader mental model，再进入正式术语/公式；信息不足时明确缺定义，不得猜科学含义。

允许修改的 production source 只有 `skills/writing/core/response-clarity/SKILL.md` 和直接相关 eval/tests；generated mirror 只能通过正式 generator 更新。Package 明确禁止修改其他 writing skill 的 production semantics、Research Authoring、Presentations、PIE、Bridge Kit，也禁止新增 skill/router/state machine/model/API。

因此 successor 没有借 review-limit 重开 Clear Writing 架构，也没有把前序任务的产品边界重新谈一遍。

## 2. 九组真实样本是否完整、诚实使用

PASS。

`REAL_WEB_KNOWN_REGRESSION_BANK_V2.md` 完整覆盖 KR-WEB-01..09：

- 01 长回答淹没判断；
- 02 伪澄清/建议漂移/自我检讨；
- 03 具体解释、例子和证据边界正例；
- 04 伪结构化；
- 05 综合膨胀成方案文档；
- 06 一句一段、标题/公式碎片化；
- 07 非必要英文概念栈及 10/17 复发；
- 08 复杂科研方法解释正例；
- 09 三方案比较正例 + 陌生术语/多重下标对象反例。

Bank 只冻结可迁移的好/坏机制，没有复制私人科研原文或项目科学答案。九组全部明确为 known regression / positive control，永久排除 G7 fresh/unseen。

KR-WEB-03、08、09 的正向部分都是硬保护。它们共同防止“清晰 = 强制短答”：必要例子、真实对照、因果解释、公式直觉、限制、证据边界和停止条件都必须保留。

latest main 的对应 writing-style TODO 在 package 使用的 source anchor `c96b5e...` 之后没有发生这些条目的内容变更，因此 regression bank 没有因 main 前进而失真。

## 3. 样本使用顺序与过拟合风险

PASS。

执行顺序满足开发回归先于 production repair：

- 原 RW-WEB-01..05 与四组 should-not-change 直接复用前序真实 fixtures/evidence，不重新造近似样本；
- KR-WEB-06..09 在 production edit 前创建 public-safe 泛化 fixtures并跑继承候选 baseline；
- fixture 明确禁止 DII 名称、私有公式、论文专名和项目答案；
- production repair 后再完整跑 KR-WEB-01..09；
- qualitative PASS 禁止使用关键词 grep、英文比例、段落/标题/公式数量和固定字数阈值。

successor branch 继承前序 candidate；latest main 当前没有 `response-clarity` source，因此 package 要求的 main merge 本身不会提供一个“已经按新样本调过”的 response-clarity 替代候选。若实际 merge 出现 product-source substantive conflict，Plan 已要求停回 Planner。

## 4. KR-WEB-07 英文问题的边界

PASS。

Review_2 已判定“普通英文自然中文化 / 正式名称和机器字符串保留”是现有 contract capability，不是新的第三个产品缺口。Successor 正确把 KR-WEB-07 主要作为 runtime regression：

- 正式模型/方法名、稳定缩写、代码/机器字符串和检索身份继续保留；
- 普通推理概念优先自然中文；
- 如果 baseline 仍失败，只允许加强现有 final-output semantic check；
- 禁止英文词表、英文比例或新的独立语言机制。

这不会把用户真实复发误写成“再加一套禁词规则”。

## 5. reader mental model 是否保真且不越权

PASS。

Plan 明确把 reader model 限定在 domain/source 已建立的事实：

- 对象类型；
- 层级/单位；
- 已知/观测/估计/待求状态，仅在已有信息支持时说明；
- 为什么当前需要；
- 后续参与什么计算、判断或步骤。

多重下标只解释已经定义或能由上游事实确定的角色；否则必须指出对象定义不足，不能由 Clear Writing 猜出科学含义。正式术语、符号和公式的精确身份仍保留。

这正好关闭 Review_2 的缺口，同时没有把 `response-clarity` 变成科研推理或 Research Authoring owner。

## 6. 是否保护复杂长解释和合法结构

PASS。

Plan 与 regression bank 同时保护：

- KR-WEB-03 的具体例子、因果关系和未知边界；
- KR-WEB-08 的长方法解释、真实强基线对照、公式直觉和 caveat；
- KR-WEB-09 的连续方案比较、紧凑比较表和最终判断；
- 真正复杂推导所需的标题、列表和展示公式；
- 完整 report / executable prompt / contract；
- pure JSON/YAML/code/raw log exact output；
- 正式方法名、稳定缩写、命令、路径、字段和其他机器字符串。

所以“语义成段”不是把内容压短，“mental model”也不是把正式数学替换成通俗比喻。

## 7. 工程范围和验收是否完整但不过重

PASS。

Package 使用三个窄的 successor 能力检查：语义段落、陌生对象首次解释、九组 known regression/positive control，并继续使用既有 fidelity / bypass 和 process gate。没有创建新的顶层 G8/G9；这是对原 G2/G3/G4 范围的有界细化。

执行后必须保留：

- focused tests；
- `skills validate`；
- source/generated parity；
- Marketplace write/check 及第二次 clean check；
- full repository tests；
- `git diff --check`；
- required zero-paid GitHub CI；
- 最终独立 Reviewer 亲自读取九组最终输出。

Web A/E、B/C、G7、PIE 0.2 和 release 均明确留在后续，未塞入本 successor。

Repo 级中央插件维护合同仍适用：Executor 修改 production source 时必须遵守当前 `AGENTS.md` 的 `workflow-core + ai-skills-core + writing-style` 维护组合、source authority、generated parity 和正常发布边界。这是已有仓库合同，不是本 successor 新增产品范围。

当前 Kickoff 中的 Git 同步语义是“获取 latest origin/main 后在已授权 successor branch 做普通 non-force merge”。运行时具体低风险命令形态仍服从当时最新 repo/Host Policy；当前 `AGENTS.md` 的 canonical fetch 形态是 `git fetch origin main`。这不改变 package 的产品语义，也不授权 rebase/force/新 branch。

## 8. 外部现实核对

OpenAI 当前官方资料仍说明：已安装 Skill 由模型根据 metadata 与用户目标决定是否相关并加载；插件可被 ChatGPT/Codex 消费，但具体能力和安装/运行条件可以因 surface 不同而不同。因此本 successor 只修 repo/Codex known regressions，而把真实 Web automatic selection 的 A/E、B/C 继续留到后续，是正确的证据边界；不能用本轮 repo PASS 替代 Web normal-entry 证明。

参考：
- https://developers.openai.com/plugins/concepts/skills
- https://help.openai.com/en/articles/20001066-skills-in-chatgpt
- https://developers.openai.com/plugins/concepts/plugins

## 9. Tracking / lifecycle

`writing-style` 长期能力仍由 Issue #13 跟踪。Issue 当前仍是 open，生命周期不应因本 Critic PASS 变成 DONE。

当前 Issue 的 reader-facing “当前执行”仍停在前序 recovery package，尚未反映 successor。按照 maintenance board policy，下一次具备真实 Clear Writing invocation + Project/Issue mutation 能力的维护动作应把：

- Status 保持 `DOING`；
- Area 保持 `writing-style`；
- 当前执行锚点更新为本 successor 的 Planner freeze commit；
- 下一步更新为 successor Codex implementation -> full regression/CI -> independent Reviewer。

本 Critic 不声称 Project 已同步，也不要求用户手工维护。

## 10. Final decision

```text
DECISION=PASS
NEW_BLOCKERS=NONE
APPROVED_PLAN_PATH=docs/design/clear-writing/SCIENTIFIC_EXPLANATION_READABILITY_REPAIR_PLAN_V0_1_2026-10-17.md
APPROVED_GOAL_PATH=docs/goals/CLEAR_WRITING_SCIENTIFIC_EXPLANATION_READABILITY_REPAIR_GOAL_V0_1_2026-10-17.md
APPROVED_KICKOFF_PATH=docs/operations/prompts/CLEAR_WRITING_SCIENTIFIC_EXPLANATION_READABILITY_REPAIR_KICKOFF_V0_1_2026-10-17.md
APPROVED_PACKAGE_COMMIT=19e1122fd90fb748f85fb552b4a8734cea035a32
NEXT_HANDOFF=PLANNER
READY_FOR_CODEX=NO
```

下一步由 Planner 把已批准 package materialize 为 task-local `PLAN.md`，使用当前 `AI_BRIDGE_REVIEWED_PLAN_V2` 模板并保留 maintenance companion/domain owner 信息；随后合法执行 `PLAN_REQUESTED -> PLAN_FROZEN`。该首次 freeze 不增加 `plan_revision`，保持 `plan_revision=0`、`review_round=0`。Critic 不修改 `CURRENT.json`。

Planner 完成远端核验后，再逐字交付已经审过的 Kickoff 给 Codex。Critic PASS 本身不是执行授权，也不是九组回归或产品最终 PASS。
