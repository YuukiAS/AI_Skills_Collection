[合并流程草案与流程图](../design/assurance/ASSURANCE_PROCESS_DRAFT_20261109.md)

# Design Assurance — Plugin TODO

用户现在明确要正式做 Design Assurance 和 Delivery Assurance 两个插件。已有材料对基本分工较一致：先澄清真正需要用户决定的问题，再把复杂设计收敛到可实施的冻结方案；Grill Me 是其中的按需澄清步骤，Blueprint 承载设计与证据。尚未统一的是固定双路设计还是按风险调用、Blueprint 是否为必经关卡、冻结前验收要准备到什么程度，以及交付阶段允许补哪些检查程序。另一个研究分支曾建议把决策与设计合为 Reasoned Design，不能悄悄覆盖本轮两个插件的整理目标。下面保留这些差异，不把材料汇总当成新设计批准或生产实现。（[D00](#source-d00)、[D02](#source-d02)、[D04](#source-d04)、[D13](#source-d13)；本轮用户要求）

## 2026-11-09：集中设计输入，保留待裁定分歧

status: NEW
source: 用户要求汇总 AI_Skills_Collection 与 AI Research Toolkit 全部分支材料
evidence: [完整来源索引](assurance-sources-20261109.md)
problem: 设计、澄清、验收与交付材料分散，旧提案、设计通过和真实运行证据容易混为一谈。
project-specific context: 私有项目只作为定位与通用失败类型，不复制其具体内容、数据或代码；本轮没有修改任何插件实现。

### Grill Me：用户此前定义的按需澄清步骤

- **只问用户才有权决定的事。** 偏好、范围、成功标准、风险承受，以及会改变产品行为、架构、失败恢复、权限、成本或不可逆边界的互斥取舍，才需要问。仓库、文档与证据可以查清的事实自行查；设计者能依据现有权威决定的技术细节自行决定并写明理由。目的在于避免 AI 静默替用户作关键决定，不能把工作退给用户。（[D00](#source-d00)、[D01](#source-d01)、[D05](#source-d05)）
- **输出决定与理由。** Grill Me 用于快速暴露和解决未决问题；Grill with Docs 将重要决定、术语与理由写进可引用的现有文档、ADR 或规格。只有有长期意义的决定、约束和修订进入 Blueprint，完整问答不逐条对象化。Grill Me 本身不成为 Blueprint 的运行模块。（[D01](#source-d01)、[D07](#source-d07)）
- **已经回答的决定应被后续消费。** 用户回答成为带出处的需求，接到唯一设计和实施约束；发现新反证时重开受影响的问题。自动进入 Grill 的阈值、是否直接采用上游、哪些回答必须落盘，历史输入明确留待正式设计。（[D00](#source-d00)、[D01](#source-d01)）
- **独立定义与 skill 的位置。** Toolkit 已有独立定义文件 `docs/research/design-assurance/GRILL_AND_ASTERIA_BLUEPRINT_INPUT_20261102.md`，其中分设 Grill Me / Grill with Docs。AI_Skills 的组合研究记录了上游四份独立 skill：`skills/productivity/grill-me/SKILL.md`、`skills/productivity/grilling/SKILL.md`、`skills/engineering/grill-with-docs/SKILL.md`、`skills/engineering/domain-modeling/SKILL.md`，位于 `mattpocock/skills@4ae2317ddb22b046e26455e4f9c9b3aaaf62212d`；该研究记为 MIT、仅供参考。本轮未重查上游，两个来源仓库中未找到已纳入中央生产的 Grill skill。（[D01](#source-d01)、[D04](#source-d04)）
- **保留上游描述差异。** 11 月 8 日旧 TODO 说上游“什么都问”，11 月 7 日研究在固定上游提交下却记录“事实由 Agent 自查、用户裁定偏好”。二者对上游行为的描述不一致；用户要求的筛选边界本身很清楚。后续采用前需要按实际版本复核，不能凭旧评价选择实现。（[D00](#source-d00)、[D04](#source-d04)）

### Reasoned Decision、设计与交付怎样衔接

- Reasoned Decision 保持当前目标、证据和路线判断；Design Assurance 负责多路研究、盲区检查、实施就绪与冻结；Delivery Assurance 在真实候选出现后核对最终对象、旧功能、防降级和可交付范围。设计或执行发现满足推翻条件的新证据，连同具体依据回到原决策方，不能由执行者自行换路线。（[D03](#source-d03)、[D04](#source-d04)）
- workflow-core 负责既有角色、权限、入口、交接、等待与恢复；Bridge Kit 负责受权执行、身份、传输和恢复机制。Design Assurance 给现有规划者与审查者可读取的设计就绪证据，不另建第二套任务状态、数据库或审批体系。（[D04](#source-d04)、[D11](#source-d11)、[D12](#source-d12)）
- 每份实质执行包交给用户前，需要简短说明“上一轮什么问题、这次具体写到哪里、运行时怎样发现复发”。研究标题、截图和“加强检查”不能替代可定位的条款。该摘要帮助用户决定是否运行，不替代完整设计和执行合同。（[D06](#source-d06)）

### 冻结合同与退回设计

- 冻结前要明确目标、对象、关系、机制、真实调用与接收者、失败恢复、权限、证据入口、验收和应保持的旧行为。高影响事实先查源码或做最小试证；结构检查只能证明填得完整，领域判断仍交给相应专业方。（[D05](#source-d05)、[D08](#source-d08)、[D09](#source-d09)）
- 陌生执行者冷读应能开工，无需再决定核心产品、科研或验收语义。冻结后的普通接线、配置与实现错误留在原任务修复；推翻核心机制、验收成功定义、权限或科学承诺时，带原证据退回设计，并保留同一任务的修订轨迹。（[D09](#source-d09)、[D10](#source-d10)、[D11](#source-d11)）
- 设计阶段通过与执行就绪、执行授权、最终产品验收分别取证。`PROCEED` 不能当作执行许可；当前角色合同要求完整执行包经最终审查，且实际用户授权仍需单独满足。本轮只整理材料。（[D11](#source-d11)、[D12](#source-d12)）

### 验收器：设计阶段需要交出什么

这里先区分“正确标准”“检查程序”“控制样本/独立参考”“真实观察”。历史材料没有形成“冻结前所有检查程序都必须写完”的统一合同；也没有给交付阶段任意新增标准的权力。完整的历史说法与冲突逐条放在 [Delivery Assurance 的验收器章节](delivery-assurance.md#验收器的历史说法与分歧)，本页只保留设计方的交接问题。（[D09](#source-d09)、[D14](#source-d14)、[D15](#source-d15)）

- 冻结前应说明每项重要承诺由谁定义、谁检查、用什么输入和真实入口、怎样区分正确/错误/缺证、谁接失败、何时退回设计。验收者必须能取得全文、真实成品或所需观察；不能等实现完才发现合法证据入口不存在。（[D08](#source-d08)、[D09](#source-d09)、[D11](#source-d11)）
- `da/1` 明确允许执行者按既有冻结标准补建/修复机械检查；`da/2` 进一步要求校准、按风险独立准入和激活。需要冻结到“标准与可执行方法”还是“可用程序与已冻结控制集”，哪些可在实现期间补齐，仍需在新插件合同中明确。不能用一句“机械实现”掩盖这一选择。（[D14](#source-d14)、[D15](#source-d15)）
- 新专业标准、阈值、独立参考和应保留行为的变更由对应项目/领域负责人裁定；程序可写不等于执行者可批准自己的答案。设计退回与普通程序维修之间的边界，是两插件必须共用的交接内容。（[D11](#source-d11)、[D14](#source-d14)、[D15](#source-d15)）

### 仍需正面裁定的历史差异

| 问题 | 材料中的不同说法 | 目前不能直接推出什么 |
|---|---|---|
| 固定角色还是按风险调用 | 旧 TODO 草拟两路 Pro、单路汇总和冷读；角色研究与设计协议主张一个主设计者，按风险安排第二路、调查与领域专家。（[D00](#source-d00)、[D05](#source-d05)、[D10](#source-d10)） | 不能把固定排班写成已定的所有任务默认流程。 |
| Blueprint 的位置 | 旧 TODO 把它作为冻结前产物与关卡；Toolkit 强调冻结后的系统真相，也允许设计阶段映射；组合研究允许用现有 Plan/ADR 先承载。（[D00](#source-d00)、[D01](#source-d01)、[D04](#source-d04)） | 尚未统一它是必需依赖、可替换载体还是独立产品接口。 |
| 一次设计到位的含义 | 旧反馈希望冻结后追问、停工接近零；设计协议允许授权的可逆实现自由度、有界试证和受影响范围重开。（[D00](#source-d00)、[D09](#source-d09)、[D10](#source-d10)） | 不能把目标写成“永不发现新事实”，也不能借实现自由度留下核心决定。 |
| 决策与设计是否独立 | main 与 Toolkit 使用 Reasoned Decision → Design Assurance → Delivery Assurance；另一个分支建议 Reasoned Design 合并前两者。（[D02](#source-d02)、[D03](#source-d03)、[D13](#source-d13)） | 本轮不采纳合并，也不删除该历史候选。 |
| 谁最终组织下一步 | 旧 TODO 希望 Design Assurance 告诉用户每步发给谁；组合研究将正式角色与流转保留给 workflow-core。（[D00](#source-d00)、[D04](#source-d04)、[D06](#source-d06)） | 需明确设计建议与实际调度/授权的边界，避免两个编排者。 |

### 后续正式设计需要的证据

先沿本页来源冻结一个共同合同：何时触发、最低设计证据、Grill 的提问与落盘、验收方法和程序的准备程度、Blueprint 接口、普通维修与返回设计的分界。再用科研和非科研的真实输入检验冷读能否直接开工、用户是否仍被迫协调、冻结后哪些问题本可提前想到；保留不能触发重流程的小修作为对照。这是整理后的待办，尚未启动设计、试验或插件实现。（[D00](#source-d00)、[D04](#source-d04)、[D08](#source-d08)、[D09](#source-d09)）

## 2026-11-08 原记录（原文保留）

以下原记录来自 [D00](#source-d00)。其中候选行动、角色排班和衡量目标仍按原来的提案身份阅读；本轮新增材料没有替它们宣布通过。

> 计划中的独立插件，尚未生产实现。它负责把一个复杂系统一次设计到位，再交给执行者机械实现。生命周期位置见 `docs/design/reasoned-decision/REASONED_DECISION_V0_1_ARCHITECTURE_2026-11-05.md`：Reasoned Decision → Design Assurance → Delivery Assurance。

## 2026-11-08：先固定 Grill Me、Design Assurance、Blueprint 三者的位置，再测 Blueprint

status: NEW
source: Asteria Blueprint 与 Design Assurance 先后顺序讨论，2026-11-08
evidence: Asteria Blueprint 已有可运行的设计载体与校验，最新分支 `draft/blueprint-round7-20261107`（私有仓库，只记分支名）；CAT-TRACE 的 Design Assurance 协议原稿 `docs/decisions/2026-11-03_cat_trace_design_assurance_protocol.md`（私有仓库）；本仓库 `docs/plugin-todos/workflow-core.md` 中“关键变化与落实点”一条；`docs/plugin-todos/writing-style.md` 中两条 Design Assurance / Grill Me 讨论记录
problem: 用户的目标是让设计者一次把复杂系统设计完，不能用户一问简单问题就暴露没设计；真正需要用户拍板的事必须提前问清楚。现在有三样东西，各自只解决一部分：
- Grill Me（Matt Pocock 的 `grill-me`，MIT）会逐个决定追问用户，直到没有歧义，但它什么都问，不区分哪些该问用户、哪些设计者自己能查到，问完也不留下可检查的产物。
- Design Assurance 已有一份手写协议（多路独立设计 → 一份权威汇总 → 冷读 → 冻结 → 机械执行），但冻结的方案仍会被执行暴露缺口，而且每一步之后“下一步发给谁”（GPT Pro、Codex 还是用户）都要用户自己判断，很难稳定复现。
- Blueprint 是设计载体和关卡：需求追踪、递归组件、具体设计字段、证据、验收器、失败路径、版本留痕、走查和疑问记录。它能逼设计者填满，但不能保证填对，也不负责问用户。
没有一个地方固定三者的位置，所以 Blueprint 的盲测每一步都要人工编排，结果噪声大。
project-specific context: Asteria Blueprint 的界面、CAT-TRACE 与 Mica 的具体内容都只是这次的真实案例。通用问题是：复杂设计流程需要一个固定的编排者，决定每一步由谁做、交什么、何时能冻结，并把澄清工具和设计载体放在固定位置。

candidate_action:
- 三者位置：
  - Grill Me 是 Design Assurance 开头的按需澄清步骤，不是独立流程。每个问题先分类：只有用户能定的（偏好、范围、成功标准、风险承受）才问用户；查得到的自己查；设计者该定的自己定并写理由。用户的回答直接成为 Blueprint 中带出处的需求。
  - Design Assurance 是编排者，决定每一步交给谁、交什么、满足什么条件进入下一步。
  - Blueprint 是 Design Assurance 的产物和冻结关卡：校验不过、依据缺失、走查讲不清就不能冻结；冻结后的用户疑问和执行停工都记成 Blueprint 的版本改动，并标明“本可想到”还是“跑了才知道”。
- 草拟的步骤与执行者：
  1. 澄清：Grill Me，和用户进行，产出需求清单；
  2. 独立设计：两路 GPT Pro 并行，Codex 只读盘点代码现实；
  3. 汇总：一个 GPT Pro 合成一份 Blueprint；
  4. 关卡：Codex 跑 Blueprint 校验；另一个模型扮演用户逐组件追问，答案不在 Blueprint 里即为缺口；Codex 只拿 Blueprint 冷读，列出开工前仍需问的问题；有缺口回到第 3 步；
  5. 冻结并执行：Codex 实现；执行中需要设计判断时停下（如 `NEEDS_GPT_PLANNER`），回到第 3 步并记一次改口。
- 每一步结束时，Design Assurance 直接告诉用户“下一步把什么发给谁”，并附上 `workflow-core` TODO 中要求的“关键变化与落实点”。
- 衡量标准：冻结后用户还要问几个本可提前想到的问题，执行者停工几次。目标接近零。
- 最小版本可以先不做成完整插件：一份记录当前步骤的状态文件，加每一步现成的提示词，就能实现“下一步发给谁”。用真实项目跑通一次后，再决定插件结构。

promotion_gate:
1. 用 CAT-TRACE 的真实需求与 Codex 停工记录跑通一次完整流程，Blueprint 冻结后的停工与用户追问数量有记录；
2. 用户在每一步都不需要自己判断下一步交给谁；
3. 澄清步骤问用户的问题都属于只有用户能定的类别，不出现设计者自己能查到的问题；
4. 换到非科研项目（如浏览器插件）时，步骤与角色不需要改写。


## 本页来源

下面每项都给出仓库、分支、固定提交和路径；完整的其他分支与内容版本见[来源索引](assurance-sources-20261109.md)。

| 来源 | 仓库 / 分支 | 固定提交 | 路径 |
|---|---|---|---|
| <a id="source-d00"></a>D00 | AI_Skills_Collection / `origin/todo/design-assurance-20261108` | `79c3d2cfa2b4da7c2edc544564d38de6fb140cb1` | [`docs/plugin-todos/design-assurance.md`](assurance-sources-20261109.md#a-f039) |
| <a id="source-d01"></a>D01 | AI_Research_Toolkit / `origin/main` | `e0c40e593f00835a9f5f66441e68628ccc48f216` | [`docs/research/design-assurance/GRILL_AND_ASTERIA_BLUEPRINT_INPUT_20261102.md`](assurance-sources-20261109.md#t-f164) |
| <a id="source-d02"></a>D02 | AI_Research_Toolkit / `origin/main` | `e0c40e593f00835a9f5f66441e68628ccc48f216` | [`AI_RELIABILITY_SYSTEM_REFERENCE.md`](assurance-sources-20261109.md#t-f002) |
| <a id="source-d03"></a>D03 | AI_Skills_Collection / `origin/main` | `4de2e557f68c5071d1c3df8b71082abbafe57bb1` | [`docs/design/reasoned-decision/REASONED_DECISION_V0_1_ARCHITECTURE_2026-11-05.md`](assurance-sources-20261109.md#a-f029) |
| <a id="source-d04"></a>D04 | AI_Skills_Collection / `origin/research/ai-skills-portfolio-consolidation-20261107` | `50a6ecced7c1c0745b312786dc704d916c7c9c9a` | [`docs/research/ai-skills-portfolio-consolidation-20261107/WORKSTREAMS/DESIGN_ASSURANCE.md`](assurance-sources-20261109.md#a-f065) |
| <a id="source-d05"></a>D05 | AI_Skills_Collection / `origin/design/frontend-feedback-continuity-20261104` | `37451ada08dd435d44536d41108dc6d828b6c9ff` | [`docs/design/frontend-design/DESIGN_ASSURANCE_CLAUDE_ROLE_DECISION_20261104.md`](assurance-sources-20261109.md#a-f022) |
| <a id="source-d06"></a>D06 | AI_Skills_Collection / `origin/main` | `4de2e557f68c5071d1c3df8b71082abbafe57bb1` | [`docs/plugin-todos/workflow-core.md`](assurance-sources-20261109.md#a-f044) |
| <a id="source-d07"></a>D07 | AI_Skills_Collection / `origin/main` | `4de2e557f68c5071d1c3df8b71082abbafe57bb1` | [`docs/plugin-todos/writing-style.md`](assurance-sources-20261109.md#a-f048) |
| <a id="source-d08"></a>D08 | AI_Research_Toolkit / `origin/main` | `e0c40e593f00835a9f5f66441e68628ccc48f216` | [`COMPLEX_SYSTEM_DESIGN_GUIDE.md`](assurance-sources-20261109.md#t-f006) |
| <a id="source-d09"></a>D09 | AI_Research_Toolkit / `origin/research/architecture-production-protocol-20261027-pro-a` | `6c3092e0ec88ebb11e7d085cfa1b51a0c0c5644e` | [`docs/research/architecture-production-protocol-20261027/pro-a/FREEZE_AND_HANDOFF.md`](assurance-sources-20261109.md#t-f041) |
| <a id="source-d10"></a>D10 | AI_Research_Toolkit / `origin/research/architecture-production-protocol-20261027-pro-b` | `cb1aebea147fd5b953c9cad987e4811d901b85e7` | [`docs/research/architecture-production-protocol-20261027/pro-b/RESULT.md`](assurance-sources-20261109.md#t-f065) |
| <a id="source-d11"></a>D11 | AI_Skills_Collection / `origin/main` | `4de2e557f68c5071d1c3df8b71082abbafe57bb1` | [`docs/workflows/PLANNER_ROLE_CONTRACT.md`](assurance-sources-20261109.md#a-f094) |
| <a id="source-d12"></a>D12 | AI_Skills_Collection / `origin/main` | `4de2e557f68c5071d1c3df8b71082abbafe57bb1` | [`docs/workflows/CRITIC_ROLE_CONTRACT.md`](assurance-sources-20261109.md#a-f089) |
| <a id="source-d13"></a>D13 | AI_Skills_Collection / `origin/design/ai-reliability-architecture-20261026` | `0f0d24e4e83460b35321a776c66433189c3f38fd` | [`docs/design/ai-reliability-architecture/ARCHITECTURE_ZH.md`](assurance-sources-20261109.md#a-f007) |
| <a id="source-d14"></a>D14 | AI_Research_Toolkit / `origin/research/software-production-decision-20261013` | `ae2766a62b1546048ec6122e01ee95f1904fb73c` | [`docs/research/software-production/16_THREE_RUN_SYNTHESIS_AND_DELIVERY_ASSURANCE_20261015/DELIVERY_ASSURANCE_PUBLIC_DA1_INTERFACE_FREEZE_V1_20261020.md`](assurance-sources-20261109.md#t-f381) |
| <a id="source-d15"></a>D15 | AI_Research_Toolkit / `origin/research/software-production-decision-20261013` | `ae2766a62b1546048ec6122e01ee95f1904fb73c` | [`docs/research/software-production/22_DELIVERY_ASSURANCE_GLOBAL_WORK_RESEARCH_20261022/WORK_OUTPUT/03_END_TO_END_EXECUTION_AND_VALIDATORS.md`](assurance-sources-20261109.md#t-f702) |
