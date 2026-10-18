---
schema: AI_BRIDGE_REVIEWED_PLAN_V2
task_key: clear-writing--scientific-explanation-readability-repair
decision: PLAN_FROZEN
---

# Clear Writing 普通科研解释可读性最小修复 — task-local frozen Plan

- Repository: `YuukiAS/AI_Skills_Collection`
- Task: `clear-writing--scientific-explanation-readability-repair`
- Execution branch: `reviewed/clear-writing--scientific-explanation-readability-repair`
- Successor of: `clear-writing--cross-surface-language-layer`
- Approved design: `docs/design/clear-writing/SCIENTIFIC_EXPLANATION_READABILITY_REPAIR_PLAN_V0_1_2026-10-17.md`
- Approved Goal: `docs/goals/CLEAR_WRITING_SCIENTIFIC_EXPLANATION_READABILITY_REPAIR_GOAL_V0_1_2026-10-17.md`
- Approved Kickoff: `docs/operations/prompts/CLEAR_WRITING_SCIENTIFIC_EXPLANATION_READABILITY_REPAIR_KICKOFF_V0_1_2026-10-17.md`
- Approved package commit: `19e1122fd90fb748f85fb552b4a8734cea035a32`
- Critic review: `results/clear-writing--scientific-explanation-readability-repair/CRITIC_EXECUTION_READY_REVIEW_V0_1_2026-10-17.md`
- Maintenance companion: `ai-skills-core`
- Domain owner: `writing-style`
- Plan revision: `0 / 1`
- Review round: `0 / 2`

## Objective and value

不重做 Clear Writing。保留当前六技能架构和上一任务已经通过的 `response-clarity` 能力，只关闭第二轮独立 Reviewer 明确指出的两个普通科研解释缺口：

1. 同一个完整语义/推理单元应优先组成自然段；避免一句一段、标题过密、短公式与解释无必要分裂造成的整篇碎片化。
2. 陌生方法、术语、数学对象尤其多重下标对象第一次出现时，应先建立不越权的读者模型，再进入正式术语/公式；上游信息不足时不得猜科学定义。

本轮目标不是“让回答更短”，而是让复杂科研解释在保持必要深度时更连续、更容易建立读者模型。

## Frozen decisions

- 保留现有 `writing-style` / Clear Writing、`response-clarity` 和其余五个 skill 的产品边界。
- 普通 ChatGPT/Codex 科研解释由 `response-clarity` 负责最终阅读层；正式中文 Markdown/报告/科研长文仍由 `chinese-prose` / `scientific-rewrite` 负责。
- 中央插件维护继续使用现有 `workflow-core + ai-skills-core + writing-style` 合同：`workflow-core` 负责执行协议，`ai-skills-core` 负责 source authority、TODO/duplicate triage、generated parity、production replay、unrelated regression、version/changelog/release closure，`writing-style` 负责本任务的专业语言判断。三者不得互相替代。
- 不新增 skill、router、state machine、外部模型、API 或新的写作系统。
- 不修改 Research Authoring / Presentations 的职责或专业逻辑。
- 2026-10-14 至 2026-10-17 已记录的 9 组真实 Web 样本全部为 known regression / positive control，永久不得作为 G7 fresh。
- 9 组样本的冻结摘要为 `results/clear-writing--scientific-explanation-readability-repair/REAL_WEB_KNOWN_REGRESSION_BANK_V2.md`。
- 本轮只有 KR-WEB-06 和 KR-WEB-09 中 Reviewer 指出的两个缺口授权新增 production contract；其他样本用于防回归、正向保护或 runtime 验证。
- KR-WEB-07 的“非必要英文”已有现行合同覆盖，本轮先验证实际 runtime，不新增英文禁词表或比例规则。
- 不使用段落数、行数、标题数、公式数、英文比例、关键词命中或 DII 专名作为质量 oracle。

## Positive completion

本 successor 只有在同一最终候选上同时满足以下条件才完成：

1. 在任何 production edit 前，对新增 KR-WEB-06..09 建立 public-safe 泛化 fixtures，并用继承的当前候选做 baseline replay；保存完整输出和判定。
2. 最小修改后的 `response-clarity` 对两个 Reviewer 缺口有明确、通用、非阈值式合同。
3. 修复后完整运行 KR-WEB-01..09：
   - 所有负例要求均 PASS；
   - KR-WEB-03、08、09 正向部分继续 PASS，证明复杂解释没有被机械压短；
   - KR-WEB-07 证明普通中文概念不再机械回退到英文栈，同时正式名称和机器字符串仍受保护。
4. 原四组 should-not-change 全部 PASS。
5. 现有 `response-clarity` 路由、source/generated parity、原五技能和相关 routing 不回归。
6. full repository tests、Marketplace generation/check、required GitHub CI PASS。
7. 独立 Reviewer 实际读取 9 组最终输出，而不是只看 Executor summary。

最大声明范围：这只证明 repo/Codex candidate 对全部已知样本的通用修复与回归闭合。不得声称 ChatGPT Web 自动调用、A/E、B/C、G7、PIE 0.2 或正式 release 已通过。

## Non-substitutable semantics

### A. 完整推理单元成段

普通复杂解释中，如果相邻句子共同完成以下任一任务，应优先留在同一自然段：

- 定义同一个对象；
- 解释同一条因果链；
- 完成一个局部比较；
- 给出一个局部推导及其意义；
- 一个结论及其直接 caveat / evidence boundary。

新段落、标题、列表或独立展示公式只有在它提供真实导航、比较、执行或数学可读性价值时才使用。

最终阅读层必须检查整篇碎片化：一句一段连续出现、标题只包一两句话、公式和紧邻解释被无意义拆开，都属于需要重组的信号。

不得把这些要求实现成固定阈值。复杂推导、真正独立的主题、比较表和核心展示公式仍可以单独成块。

### B. 陌生科研对象的 reader mental model

新方法、陌生术语或新数学对象首次进入普通科研解释时，若上下文尚未建立，先用已知事实说明：

- 它是什么类型的对象；
- 它处于什么层级/单位（如中心、患者、样本、位置、目标组成量等）；
- 它是给定量、观测量、估计量还是待求量（只在已有信息支持时说明）；
- 为什么当前需要它；
- 后面它参与什么计算、判断或步骤。

多重下标首次出现时，应解释每个尚未建立的下标角色，或明确引用此前定义。

正式术语、符号和公式必须保留精确身份；自然语言解释不是替代公式，而是让读者在看到公式时知道自己在看什么。

如果 domain reasoning / source 没有提供足够信息来确定上述属性，`response-clarity` 必须保留不确定性、指出对象定义不足或请求上游补定义；不得凭语境猜出科学含义再润色成确定事实。

### C. 已有能力不得退化

继续保留上一任务已经通过的：

- 结论优先；
- 回答完成后的语义停止条件；
- 来源共识与助手建议分层；
- 普通英文概念自然中文化、精确名称保留；
- 反馈意图匹配；
- 精确机器输出旁路；
- 必要例子、因果解释、限制和不确定性。

## Implementation scope

允许修改：

- `skills/writing/core/response-clarity/SKILL.md`；
- 由正式 generator 产生的同源 `plugins/codex/plugins/writing-style/skills/response-clarity/SKILL.md`；
- `response-clarity` 直接相关 eval / public-safe regression fixtures / deterministic contract tests；
- 当前 successor 的 results / task evidence。

执行顺序必须保持：

1. 从当前 successor branch 开始，读取旧任务最终候选与 REVIEW_2。
2. fetch latest `origin/main`，在当前已授权 successor branch 做普通 non-force merge；若出现和 Clear Writing product source 的实质冲突，停回 Planner。不得 rebase/force/新建 successor。
3. 复用已有 RW-WEB-01..05 和 should-not-change fixtures，不复制。
4. 为 KR-WEB-06..09 创建 public-safe 泛化 fixtures：
   - 不使用 DII、具体论文名、私有公式或项目科学答案；
   - 保留失败机制：复杂连续推理、普通英文概念、长而清楚的正例、陌生术语/多重下标对象。
5. 在修改 `response-clarity` 前，用继承候选跑 KR-WEB-06..09 baseline，保存完整输出。
6. 仅实现 A/B 两项通用合同；如果 baseline 显示 KR-WEB-07 仍失败，只能通过已有“普通英文 vs 精确身份”通用规则的最终输出检查来修，不能扩展成第三套词表机制。
7. 修复后运行 KR-WEB-01..09 + 四组 should-not-change。
8. 运行 focused tests、skills validate、source/generated parity、Marketplace generator、full repository tests、`git diff --check` 和 required GitHub CI。
9. CI PASS 后交独立 Reviewer；Reviewer 必须实际读取 9 组最终输出。

Executor 修改 production source 前，必须按仓库现有 maintenance contract 实际完成 `ai-skills-core` production maintenance preflight；只读取 source `SKILL.md` 不能替代 production invocation。

不允许修改：

- `chinese-prose`、`scientific-rewrite`、`scientific-prose`、`product-ui-copy`、`writing-fidelity` 的 production semantics；
- Research Authoring / Presentations production source；
- Project instructions / PIE 0.2；
- Bridge Kit；
- personal ChatGPT account/plugin state；
- paid review；
- unrelated repository behavior。

## Acceptance and regression gates

### G2-R1 — 语义段落与整篇连续性

PASS：

- public-safe complex scientific explanation 中，同一推理单元形成自然段；
- 不出现无价值的一句一段链、小标题链或公式碎片链；
- 长解释仍可保留必要结构和细节。

FAIL：

- 仅通过减少总字数、删除解释或固定段落数量取得“紧凑”。

### G2-R2 — 陌生对象/公式首次解释

PASS：

- 新对象先有足够 reader model；
- 多重下标角色清楚；
- 正式公式后说明其下一步用途；
- 信息不足时明确不足，不猜定义。

FAIL：

- 只重述符号；
- 以英文术语本身代替解释；
- 凭上下文补出 source/domain 没有给出的科学含义。

### G2-R3 — 全部 9 组 known regression / positive control

以 `REAL_WEB_KNOWN_REGRESSION_BANK_V2.md` 为唯一摘要标准。旧 5 组、新 4 组全部参与。正例是硬保护，不是可选参考。

### G3/G4 — fidelity 与旁路

数字、公式、证据强度、正式名称、机器字符串和 exact-output request 不得退化。正式文档路线 ownership 不变。

原四组 should-not-change 必须全部通过：

1. 完整 report / executable prompt / contract；
2. 真正有分支、层级或逐步执行价值的结构；
3. pure JSON/YAML/code/raw log exact output；
4. 正式名称、稳定缩写和机器字符串。

### Process gate

- focused tests PASS；
- `skills validate` PASS；
- source/generated parity PASS；
- Marketplace write/check 与第二次 clean/idempotent check PASS；
- full repository tests PASS；
- `git diff --check` PASS；
- required zero-paid GitHub CI PASS；
- 独立 Reviewer artifact review PASS，并实际读取 9 组最终输出。

## Natural-language usage / routing expectations

应改进的普通请求示例：

- “这个方法到底在做什么？把公式也解释给我。”
- “这几个下标分别是谁？这个量算出来后去哪一步？”
- “比较这三种方法，详细一点，但别每句话都单独一段。”
- “论文用了很多英文术语，用中文把机制说清楚，正式方法名保留。”

不应被本 successor 接管：

- “重写这整份中文科研报告并保持全部公式引用” → 正式文档路线；
- “Return exactly this JSON” → 精确机器输出旁路；
- “给我完整 Codex execution prompt” → 完整机器交付物；
- Research Authoring / Presentations 的领域结构和科学内容决策。

## Out of scope

- 不重做 Clear Writing 架构；
- 不新增 skill/router；
- 不做 PIE 0.2；
- 不做 ChatGPT Web 安装或 A/E、B/C；
- 不做 G7 fresh；
- 不做 release/version bump；
- 不改 Research Authoring / Presentations；
- 不为“读起来紧凑”创建硬阈值、禁词表或格式 blacklist；
- 不加入 DII-specific selectors、术语或公式；
- 不增加新的顶层 Gate、Reviewer、数据库或长期 ledger。

Version decision 保持：Repository `NO_BUMP`；`writing-style` 在本 repair 阶段 `NO_BUMP`。正式版本收口留到后续 Web/product gates 完成后。
