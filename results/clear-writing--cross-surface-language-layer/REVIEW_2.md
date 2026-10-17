---
schema: AI_BRIDGE_REVIEWED_REVIEW_V1
task_key: clear-writing--cross-surface-language-layer
review_round: 2
decision: REVISE
implementation_commit: c9ccd80ab428aa1b7c8679bef089f082f8fcf05f
---

# Clear Writing 第二轮独立审查

## Decision

**REVISE。PROCESS PASS，PRODUCT / ARTIFACT PASS 尚未成立。**

第一轮唯一阻断 `CW-CI-01` 已关闭：当前 reviewed branch 的必需 GitHub CI `38838231833` 全部通过，`codex-marketplace` 实际运行 342 项单元测试全部 PASS，Marketplace 生成/校验/freshness、skills validate/audit、generated cleanliness、Windows sparse checkout 和 Linux/Windows 安装 smoke 均通过。

本轮也实际读取了 RW-WEB-01..05 修复后完整输出、四组 should-not-change fixtures / outputs / verdicts，而不是只看 Executor 总结。五个已知回归在当前 `response-clarity` 产品源码身份上全部通过；RW-WEB-03 正向控制保留了类比、两个具体场景、因果关系和未知边界，证明当前修复没有把 Clear Writing 退化成固定短答。完整合同、真正有分支价值的流程、纯 JSON 精确旁路和正式机器字符串也都保持正确。

但是，latest main 的 2026-10-16/17 DII 真实用户反馈暴露了一个当前普通回复路线的**明显通用合同缺口**。这些材料已经暴露，因此本轮只作为独立覆盖证据，不作为 G7 fresh，也没有据此修改 candidate。由于该缺口命中 `response-clarity` 自己明确拥有的普通科研解释范围，不能以 CI 绿灯或正式文档路线已有规则替代，因此本轮不能 PASS。

## Blocking findings

### CW-R2-01 — 普通复杂科研解释的读者负担合同不完整

**冻结要求 / 回归依据**

当前 PLAN 明确规定：

- `response-clarity` 拥有普通技术、科研、统计等用户解释；
- “clear” 必须降低读者负担，而不是机械缩短；
- 格式复杂度必须与信息结构相称；
- 正式中文文档/科研长文仍归 `chinese-prose` / `scientific-rewrite`，普通聊天不能错误转给文档路线；
- latest main 中新增的真实 DII 反馈只能作为 known real-use coverage，不得调当前 candidate 或冒充 fresh evidence。

**观察证据**

1. 当前 `response-clarity/SKILL.md` 有 “Prefer concise paragraphs”、列表只在真正并列/可扫描时使用、不要把简单问题写成报告等规则，但**没有明确要求相邻句子按一个完整语义/推理单元组成自然段，也没有整篇层面的碎片化检查**。  
   2026-10-16 的真实反馈恰好是连续科研解释被拆成一句一段、十几个小标题、短公式单独占块，导致纵向阅读负担显著增加。现有 “concise paragraphs” 甚至不足以排除一句一段的实现。

2. 当前普通回复路线没有明确要求：面对陌生科研方法、正式术语、数学对象或多重下标符号时，先建立 reader mental model，再给正式术语/公式，并紧接解释“算出来以后做什么”。  
   latest main 的 DII 正反例显示，这一顺序对复杂科研解释是实质可读性条件；尤其 (widehat T_{kij}) 这类对象，读者需要先知道对象层级、各下标角色、已知/估计状态、近似对象和后续用途。当前 `response-clarity` 只有“lead with human meaning / conclusion first”，不足以约束这一失败模式。

3. 正式文档路线并非缺失：`chinese-prose` 已明确“正文优先用连贯段落”，并在 heavy route 中拥有 `METHOD_MENTAL_MODEL`、`FORMULA_WALKTHROUGH` 和英文语义分类；`scientific-rewrite` 也要求 Reader Plan、公式附近中文解释和普通 Latin technical word 不因英文身份自动受保护。  
   但这不能关闭本 finding，因为这些技能明确把**普通聊天解释**交给 `response-clarity`。让 ordinary ChatGPT 科研解释临时误路由到文档重写路线会违反当前职责边界。

4. 本轮实际 runtime replay **没有覆盖**长篇复杂科研解释、陌生正式术语或多重下标公式。RW-WEB-03 能证明“不要过度压缩例子/因果/不确定性”，RW-WEB-05 能证明“来源共识和助手建议分层”，但二者都不能证明上述新增科研解释行为。  
   因此这些新增 DII 关注点必须标记为 **NOT_YET_RUNTIME_VERIFIED**。

5. “普通英文概念应自然中文化、正式方法名/稳定缩写/机器字符串保留”本身已有通用合同：`response-clarity` 要求中文回复使用自然中文、来源是英文不能成为保留普通英文的理由，并保护 exact technical strings；`chinese-prose` / `scientific-rewrite` 对正式文档还有更完整的语义分类。这里**不是新增禁词表缺口**。但 2026-10-17 的真实复发没有当前 candidate runtime evidence，仍为 **NOT_YET_RUNTIME_VERIFIED**，不能写成产品已通过。

**因果风险**

如果现在放行，当前候选完全可能继续产生一种“每句都清楚、整篇却像卡片流”的科研解释；也可能在公式数学正确时直接丢给用户一个未建立对象层级的符号。两者都符合已有机械 CI 和当前 5 个短/中型回归，却仍会重现用户明确指出的真实阅读失败。因此现有证据可以由一个不满足用户真实目标的较弱实现解释，按 Reviewer contract 不能 PASS。

**最小修复**

后续只需在普通回复路线补两个语义级要求，不需要重做架构：

1. **语义单元成段 / 整篇碎片化检查**  
   相邻句子共同解释同一个对象、因果链、比较或局部推导时，应组成自然段；标题、列表、独立公式只在提供真实导航/比较/推导价值时拆开。最终检查整屏/整篇是否出现一句一段、过密标题或公式碎片化。不得实现成固定段落长度、标题上限或行数阈值。

2. **陌生科研对象的 reader mental model**  
   普通科研解释遇到新方法/新术语/新符号时，在不擅自补科学定义的前提下，先说明它在当前语境中“是什么/处于哪一层/为什么需要/后面拿来做什么”；多重下标对象首次出现时解释下标角色，或明确引用已建立定义；再给正式术语/公式。若上游 domain reasoning 没有足够信息，应暴露“对象定义不足”，不能猜测。

修复时继续保留：
- 正式方法/模型名、稳定缩写、公式和机器字符串；
- 必要标题、复杂推导、展示公式；
- 例子、因果解释、限制和不确定性；
- 完整报告、完整执行 prompt 和机器输出的完整性；
- `chinese-prose` / `scientific-rewrite` 对正式长 Markdown / source-faithful rewrite 的现有 ownership。

**修复后所需证据**

- 以上 DII 材料只作为 known regression，不能成为 G7；
- 至少用公共安全的泛化 fixture 证明普通复杂科研解释的 semantic paragraphing 和 unfamiliar-object/formula explanation，不按 DII 名词硬编码；
- 保留现有 RW-WEB-01..05、四组 should-not-change、focused tests、source/generated parity 和 full CI；
- 真正产品验证仍必须进入后续 ChatGPT Web A/E、B/C matched comparison；新增 DII 真实样本在 Web 阶段只能作为 known-regression batch；
- G7 必须另用冻结的 fresh/unseen batch。

## Non-blocking notes

- **RW-WEB-01..05：实际 replay PASS。** 这些证据足以关闭 2026-10-14/15 已知失败，但不能外推到本轮新增的复杂科研解释。
- **RW-WEB-03：实际正向控制 PASS。** 当前候选已经证明 Clear Writing 不等于“越短越好”。
- **英语边界：合同已覆盖，runtime 尚未覆盖新增 DII 复发。** 当前规则不是禁词/比例机制，正式名称与机器字符串保护也在 should-not-change 中有实际证据；状态为 **CONTRACT_COVERED / NOT_YET_RUNTIME_VERIFIED_FOR_NEW_DII_CASES**。
- **正式长 Markdown / scientific rewrite：owner 正确。** `chinese-prose` / `scientific-rewrite` 已拥有段落、英文分类、方法直觉和公式解释机制；这些新 DII 文档反馈不应成为让 `response-clarity` 接管文档重写的理由。对本轮新增样本的实际运行仍为 **NOT_YET_RUNTIME_VERIFIED**。
- 本轮没有证据允许声称 ChatGPT Web automatic activation、G1 A/E、G1 B/C、G7、PIE 0.2 或正式发布已经通过。

由于这是第 2 / 2 轮 Reviewer，自动返修预算已经用尽。按当前 Reviewed Handoff 合同，本结果必须进入 `AWAIT_HUMAN_DECISION / REVIEW_LIMIT`，不得创建第三轮自动 Reviewer 或直接继续改 production candidate。
