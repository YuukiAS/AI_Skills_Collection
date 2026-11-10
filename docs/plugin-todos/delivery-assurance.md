[合并流程草案与流程图](../design/assurance/ASSURANCE_PROCESS_DRAFT_20261109.md)

# Delivery Assurance — Plugin TODO

用户已明确要正式做 Delivery Assurance。材料已经说明要解决什么：让正式交付有当前成品与真实专业证据支撑，保护旧功能，拒绝降级替代，并让失败回到原任务。历史上已有有效的 Stop Hook 探针、`da/1` 接口冻结及后来由用户转交的 `da/2` R3 设计通过；这些都不等于生产插件或七仓接入已完成。尚未统一的是交付判断归 workflow-core 还是独立插件、沿哪代接口实施，以及冻结前后验收器各部分由谁准备和批准。本页集中这些未决点，不选择架构或替用户批准实施。（[V01](#source-v01)、[V02](#source-v02)、[V09](#source-v09)、[V13](#source-v13)；本轮用户要求）

## 2026-11-09：集中交付设计、验收器责任与真实试验证据

status: NEW
source: 用户要求汇总 AI_Skills_Collection 与 AI Research Toolkit 全部分支材料
evidence: [完整来源索引](assurance-sources-20261109.md)
problem: 多轮设计、审查、Phase 1 和项目验收专项分散，难以辨认已经证明的接点、仍待实现的能力和相互冲突的归属。
project-specific context: 消费者只作为仓库与来源定位，不复制私有业务、科研数据、代码或具体阈值。本轮仅整理 TODO。

### 先分清已存在的材料和未完成的系统

| 历史层次 | 现有依据 | 边界与待办 |
|---|---|---|
| workflow-core 既有交付规则 | 当前源码已有验收准入、真实对象、证据强度、人工依赖分类与恢复要求。（[V19](#source-v19)） | 是既有保护；新插件未真实接通前不能删掉。 |
| Phase 1 Hook 探针 | R5 的有效尝试记录 Stop 阻止假完成、原任务续修、新候选重验；污染和无效尝试分别保留。（[V04](#source-v04)、[V05](#source-v05)） | 只证明受测宿主与探针接点；不证明生产 DA-G10–DA-G15 或七仓可用。 |
| v0.3 审查到 v0.4 | 有早期通过记录，也有完整七仓复审的 REVISE，后者要求具体接入、旧定位恢复、遗漏检测与人类边界。（[V06](#source-v06)、[V07](#source-v07)、[V08](#source-v08)） | 不取其中一个顶层通过覆盖后续反例；实施包仍需按版本使用。 |
| 历史 da/1 冻结与实施拆包 | 公共字段、责任、失效和防自签有冻结文档，18/19 目录拆成各层实施包。（[V09](#source-v09)、[V24](#source-v24)；全表见索引） | 冻结的是当时设计，不是所有接点均已实现或当前新方案可直接继承。 |
| 用户价值修订与 da/2 | 20 目录曾主张 da/1 无需改动；22 目录已研究 da/2、反馈回执和分阶段接线。（[V22](#source-v22)、[V14](#source-v14)） | 接口与职责变化必须说明迁移与失效，不能拼成一份从未审过的混合合同。 |
| R3 当前记录 | CURRENT 明示设计阶段已通过，来源是用户转交的结论；无另一份 GitHub 审查原件可核对。（[V13](#source-v13)） | 实施包仍是未授权草稿，P0、宿主和七仓启用未完成；不写成可立即执行。（[V23](#source-v23)） |
| 六仓验收器专项 | 23 目录安排各仓复用和加固原检查，不等中央 DA 上线。（[V16](#source-v16)） | 提示词已准备和实际实施结果分开；本轮没有去私有仓检查完成情况。 |

### 预期能力与相邻插件的交接

- 从原用户要求、批准设计与已接受旧行为确定必需义务，不能只看当前已有测试清单。按实际依赖和最终消费对象选择检查；局部小修、共享变化、完整交付分别决定范围，完整覆盖不等于每次重跑所有机器。（[V10](#source-v10)、[V12](#source-v12)、[V14](#source-v14)）
- 领域与项目负责专业标准和真实判断，原 Codex 写程序、跑项目正常入口、采集证据与返修。Bridge 核对身份、候选和证据新鲜度；既有控制流程继续管理预算、等待、取消和长任务。发现改变目标、科学方法或成功定义的新问题，退回 [Design Assurance](design-assurance.md) 与原决策方。（[V09](#source-v09)、[V12](#source-v12)、[V18](#source-v18)）
- 分开证明源码、构建、安装加载、真实运行、最终文稿或科学结果；一个文件存在、测试绿灯或作业终态不能代签整条交付链。修改候选或观察方法后，只复用仍然有效的证据。（[V01](#source-v01)、[V10](#source-v10)、[V14](#source-v14)）
- 失败必须有真实接收者和合法续修入口；写出失败文件不等于原任务收到，更不等于已修复。外部审查、用户中断和等待不能被当作产品错误无限重试；已有预算不因换回合而重置。（[V14](#source-v14)、[V15](#source-v15)）
- 已确认的产品边界是：受支持普通入口尽量自动接入，受管交付严格核证据，不建第二客户端/调度器/数据库。Hook 完全未执行时无法保证拦住聊天中的错误完成文字，这个限制不能放松受管交付的质量要求。历史批准范围不构成本轮运行授权。（[V15](#source-v15)）

## 验收器的历史说法与分歧

“谁搭验收器”在材料里至少包含四件事：谁定义正确标准，谁写检查程序，谁冻结控制样本或独立参考，谁批准其进入正式验收。下面逐条保留原说法；程序维修权与标准决定权不能相互代替。

| 来源与阶段 | 谁负责、何时做、允许怎样改 | 分歧或必须保留的限制 |
|---|---|---|
| 早期 Reviewer/validator 准入合同，11 目录 | 领域负责人在样本编写、模型配置前冻结资格与正确/错误/缺证三组样本；测试或参考不能与候选同权任改；按能力授予正式判断资格。（[V17](#source-v17) §§2–5） | 这是一份资格制度提案，未培养出达到门槛的新 Reviewer；不能把新会话或自测当独立资格。 |
| Phase 1 事实清单，16 目录 | 项目/领域已有命令与审查者；workflow-core 声明所需检查，Bridge 只验身份；DA-G10–DA-G15 尚待生产验证。（[V05](#source-v05) §§2、4–6） | 探针没有实现通用“自动搭验收器”能力。 |
| 历史失败到验收家族映射 | 先归已有职责；标准已定但 runner 缺失，由执行者同任务补；程序坏则修程序；新专业含义才由项目/领域冻结新类别。（[V11](#source-v11) §§2–5） | 不把每个事故建成一个新验收器，也不把历史事故数量当今天缺陷数。 |
| 17 目录最终架构合同 C04/C08/C09 | 项目冻结业务参数，领域冻结最低标准；执行者可新增/修复机械程序；投入使用前跑正确、真实坏例与缺证校准；专业负责人依现有准入标准裁决。（[V12](#source-v12)） | 程序修复可留在当前任务；阈值、rubric、预期、适用范围、保护集合等语义变化需差异、旧结果与负责人冻结。 |
| v0.4 生产合同 §8 | 标准已冻结、机械实现缺失或有 bug 时，执行者在同一任务实现/修复；标准缺失回项目/领域负责人。（[V08](#source-v08)） | 明确允许交付期间补程序；禁止为当前候选变绿而改标准、删样本、换证据面。 |
| 历史 da/1 冻结 §§1、5、10、13 | 标准归专业负责人，程序由执行者写；缺失或坏的机械程序在当前任务修，真正的新标准先由专业方冻结。（[V09](#source-v09)） | 这是当时已冻结的职责；接口、负责人或决定语义变动要退回规划与审查。 |
| 责任与验收指南 | 标准已明确就自动补程序，不让用户逐项提醒；正确应通过、错误应失败、缺证应无法判断。程序和产品可以同改，标准不能一起改松。（[V10](#source-v10)“验收标准和验收程序怎么产生”等节） | 指南开头“架构已通过”不能盖过完整七仓复审或后续新接口的未实施状态。 |
| 用户价值 v0.5 | 实质实现前先冻结义务、最终对象、旧保护、检查集合和程序缺口；第一条功能链时跑便宜检查，完成后对最终候选重验；缺程序由当前执行者补。（[V22](#source-v22) §§1、5–6） | 说明不是只在任务结束时临时加测试；该版还主张 da/1 无需改动，与后来的 da/2 路线有版本分歧。 |
| da/2 生命周期 E8、C11–C13、F5 | 当前执行者接具体补建工作项，按原标准写程序，跑正确/错误/缺证/旧保护四类校准，再准入和激活；新标准回原专业方；原程序及结果须从正常入口被消费。（[V14](#source-v14)） | 产品和程序可同改，但高风险需独立准入；只有既有冻结政策和控制集支持的机械变化才可自动准入。普通写权限不等于批准权。 |
| da/2 更新、暂停、合并和退休 | 改程序后回放旧坏例、重新校准并使受影响通过失效；采集坏要重采；只改判分且原观察可靠可重判。停检查不取消质量义务；合并/退休需迁移旧保护与消费者。（[V14](#source-v14) E8、C30、F5） | 执行者不能靠删检查、降低要求、改参考答案或未知消费者退场来自签；也不建无限“验收器的验收器”。 |
| 六仓专项，中央尚未实现时 | 复用、加固或补项目原生检查，标准明确且已获权就可在原项目做；先坏例再修产品，检查接入原 runner；逐项报告新增/增强/回归与真实运行。（[V16](#source-v16) §§1、4–8） | 不等待中央 P0、Hook 或新 reader；不实施整个中央协议。它是项目加固任务的设计输入，不是七仓中央启用证据。 |
| 当前可靠性总览与另一个整体架构分支 | 独立 Delivery Assurance 找义务和程序缺口、作交付判断；workflow-core 路由能力与接收失败；原 Codex 实现，专业方定标准，Bridge 保持基础设施。（[V02](#source-v02)、[V03](#source-v03) §5） | 与旧 17/da/1 由 workflow-core 选择必验项并聚合声明的归属不同。新插件应采用哪套职责需要正式裁定。 |
| 当前 Planner 合同 | 验收方法、责任和可访问证据在执行包前明确；执行中改变成功定义、验收或恢复语义需返回同任务修订和复审。（[V18](#source-v18) §§5–7） | 不禁止原授权内普通程序维修；但“临时补测试”不能成为改变验收语义的通道。 |

### 真正相冲突的说法与尚未写清的边界

1. **交付判断的负责人有两套。** 17、`da/1` 和 22 的架构主要让 workflow-core 解析必验项并聚合声明；Toolkit 总览和 AI_Skills 的另一整体架构候选把义务与交付准入交给独立 Delivery Assurance，workflow-core 保留路由。两者不能同时成为同一结论的平级最终负责人。（[V02](#source-v02)、[V03](#source-v03)、[V09](#source-v09)、[V12](#source-v12)、[V14](#source-v14)）
2. **冻结前必须完成到哪一层仍不一致。** Design Assurance 的旧反馈要求冻结后机械实现、尽量不再停工；交付合同却明确允许同任务补建和修复检查程序。若前者被理解为“所有验收程序都已完成且不能再动”，就与后者冲突；若只冻结标准与方法，则可兼容，但历史材料没有把程序、样本和独立参考的最迟完成点统一写清。不能替用户选一个解释。（[Design Assurance 原记录](design-assurance.md#2026-11-08-原记录原文保留)、[V09](#source-v09)、[V14](#source-v14)、[V18](#source-v18)）
3. **自动补程序不等于自动批准。** 早期指南强调当前 Codex 自动补缺口；早期准入与后续 da/2 又要求专业资格、控制集冻结和高风险独立准入。它们在“谁写代码”上大致一致，在“什么时候可自动启用、谁批准”上有逐步加严和未统一部分。新合同需要按风险写明，不能一律自批，也不能每个小测试都升级用户审批。（[V10](#source-v10)、[V17](#source-v17)、[V14](#source-v14)）
4. **旧冻结与新接口不能无缝混用。** 20 目录仍说不改 da/1；22 目录已进入 da/2 并有 R3 设计记录；11 月总览又要求交付判断独立。需要明确哪份保留、迁移或重新审查，旧 PASS 不自动覆盖新字段与职责。（[V09](#source-v09)、[V22](#source-v22)、[V13](#source-v13)、[V02](#source-v02)）
5. **标准缺失该回谁存在表述宽窄差异。** 有的整体候选说回 Reasoned Design 或专业方；旧合同说对应项目/领域负责人；Planner 合同又要求验收语义变动重新审查。必须明确哪个问题只是程序 bug，哪个缺专业规则，哪个会推翻冻结设计；不让执行者自己挑一个较易通过的负责人。（[V03](#source-v03)、[V09](#source-v09)、[V12](#source-v12)、[V18](#source-v18)）
6. **哪些保护可以后补，哪些必须先验，需要落到任务。** 六仓专项允许中央尚未落地先加固原测试；da/2 则要求相关新定义和 adapter 校准准入后才签对应交付。前者不是绕过后者的交付许可，后者也不能让全部既有项目开发停等中央系统。任务冻结时仍需说明依赖与可独立推进范围。（[V16](#source-v16)、[V14](#source-v14)、[V23](#source-v23)）

### 历史失败映射怎样继续使用

16 目录保存“历史失败→验收家族”说明与 CSV，17 目录保存 83 条要求、363 条历史记录的多种分类和对照，22 目录还有后来的覆盖表。它们的范围、版本与分类方法不同，不能相加成缺陷总量，也不能把映射覆盖说成事故已复测。优先复用原有检查、补坏例与旧保护；只有所验能力、证据、入口、专业负责人、失败含义或可支持声明出现实质差异，才讨论新类别。验收器漏检、产品错误、环境缺证和科学负结果分别处理。（[V11](#source-v11)、[V12](#source-v12)、[V14](#source-v14)、[V17](#source-v17)；各 CSV 全路径见索引）

### 仅在本地未推送提交里的材料

- `work/delivery-assurance-hook-probe-r2` 的 `005fee947bafabbfc77f47d744b4717238439905`，提交说明为 “Record Phase 1 setup usability blocker”。新增 `16_*/phase1_hook_probe_r1/` 下 14 个文件，包括结果、检查、事件与配套 Hook 输入/实现。结论是初始化条件与使用负担无法同时满足；主体场景未启动。（[V20](#source-v20)）
- `work/delivery-assurance-hook-probe-r4` 的 `5f3ecc7e77c6b2deedf221cc6c717ccd1a7b78f6`，提交说明为 “Record R4 setup state isolation blocker”。新增对应 r4 目录下 7 个文件，记录状态隔离未证明，主体场景未启动。它没有创建项目 Hook，不存在让用户信任该 Hook 的下一步。（[V21](#source-v21)）

21 个完整文件路径都在来源索引中，远端不存在对应新增文件。两次失败不被后来的有效 R5 尝试覆盖；它们约束的是执行准备，不构成 Hook 主链已经失败或已经通过的证据。

### 后续正式设计要先收敛什么

先确定独立 Delivery Assurance 与 workflow-core、Bridge、专业方的单一职责；明确沿哪代设计继续；把验收标准、程序、控制集、准入和修改权限写成共同合同。然后从最小正常入口证明：用户不额外提醒也会补验收、坏候选被拒、旧行为被保护、失败确实回到同一任务、最终当前对象才可交付。宿主、七仓、账号设备与付费权限逐项按后续合法任务取证。本轮没有启动这些实施或试验。（[V01](#source-v01)、[V13](#source-v13)、[V14](#source-v14)、[V15](#source-v15)、[V23](#source-v23)）

## 本页来源

下面每项都给出仓库、分支、固定提交和路径；完整的其他分支与内容版本见[来源索引](assurance-sources-20261109.md)。

| 来源 | 仓库 / 分支 | 固定提交 | 路径 |
|---|---|---|---|
| <a id="source-v01"></a>V01 | AI_Skills_Collection / `origin/research/ai-skills-portfolio-consolidation-20261107` | `50a6ecced7c1c0745b312786dc704d916c7c9c9a` | [`docs/research/ai-skills-portfolio-consolidation-20261107/WORKSTREAMS/DELIVERY_ASSURANCE.md`](assurance-sources-20261109.md#a-f064) |
| <a id="source-v02"></a>V02 | AI_Research_Toolkit / `origin/main` | `e0c40e593f00835a9f5f66441e68628ccc48f216` | [`AI_RELIABILITY_SYSTEM_REFERENCE.md`](assurance-sources-20261109.md#t-f002) |
| <a id="source-v03"></a>V03 | AI_Skills_Collection / `origin/design/ai-reliability-architecture-20261026` | `0f0d24e4e83460b35321a776c66433189c3f38fd` | [`docs/design/ai-reliability-architecture/ARCHITECTURE_ZH.md`](assurance-sources-20261109.md#a-f007) |
| <a id="source-v04"></a>V04 | AI_Research_Toolkit / `origin/research/software-production-decision-20261013` | `ae2766a62b1546048ec6122e01ee95f1904fb73c` | [`docs/research/software-production/16_THREE_RUN_SYNTHESIS_AND_DELIVERY_ASSURANCE_20261015/PHASE1_CLOSURE_20261019.md`](assurance-sources-20261109.md#t-f386) |
| <a id="source-v05"></a>V05 | AI_Research_Toolkit / `origin/research/software-production-decision-20261013` | `ae2766a62b1546048ec6122e01ee95f1904fb73c` | [`docs/research/software-production/16_THREE_RUN_SYNTHESIS_AND_DELIVERY_ASSURANCE_20261015/GATE_LIFECYCLE_FACT_INVENTORY_20261019.md`](assurance-sources-20261109.md#t-f385) |
| <a id="source-v06"></a>V06 | AI_Research_Toolkit / `origin/research/software-production-decision-20261013` | `ae2766a62b1546048ec6122e01ee95f1904fb73c` | [`docs/research/software-production/16_THREE_RUN_SYNTHESIS_AND_DELIVERY_ASSURANCE_20261015/DELIVERY_ASSURANCE_PRODUCTION_CONTRACT_COMPLETION_CRITIC_REVIEW_V0_3_20261019.md`](assurance-sources-20261109.md#t-f368) |
| <a id="source-v07"></a>V07 | AI_Research_Toolkit / `origin/research/software-production-decision-20261013` | `ae2766a62b1546048ec6122e01ee95f1904fb73c` | [`docs/research/software-production/16_THREE_RUN_SYNTHESIS_AND_DELIVERY_ASSURANCE_20261015/DELIVERY_ASSURANCE_PRODUCTION_CONTRACT_COMPLETION_CRITIC_REVIEW_V0_3_FULL_SEVEN_CONSUMER_REAUDIT_20261019.md`](assurance-sources-20261109.md#t-f369) |
| <a id="source-v08"></a>V08 | AI_Research_Toolkit / `origin/research/software-production-decision-20261013` | `ae2766a62b1546048ec6122e01ee95f1904fb73c` | [`docs/research/software-production/16_THREE_RUN_SYNTHESIS_AND_DELIVERY_ASSURANCE_20261015/DELIVERY_ASSURANCE_PRODUCTION_CONTRACT_COMPLETION_PROPOSAL_V0_4_20261019.md`](assurance-sources-20261109.md#t-f374) |
| <a id="source-v09"></a>V09 | AI_Research_Toolkit / `origin/research/software-production-decision-20261013` | `ae2766a62b1546048ec6122e01ee95f1904fb73c` | [`docs/research/software-production/16_THREE_RUN_SYNTHESIS_AND_DELIVERY_ASSURANCE_20261015/DELIVERY_ASSURANCE_PUBLIC_DA1_INTERFACE_FREEZE_V1_20261020.md`](assurance-sources-20261109.md#t-f381) |
| <a id="source-v10"></a>V10 | AI_Research_Toolkit / `origin/research/software-production-decision-20261013` | `ae2766a62b1546048ec6122e01ee95f1904fb73c` | [`docs/research/software-production/16_THREE_RUN_SYNTHESIS_AND_DELIVERY_ASSURANCE_20261015/DELIVERY_ASSURANCE_RESPONSIBILITY_AND_VALIDATION_GUIDE_20261019.md`](assurance-sources-20261109.md#t-f382) |
| <a id="source-v11"></a>V11 | AI_Research_Toolkit / `origin/research/software-production-decision-20261013` | `ae2766a62b1546048ec6122e01ee95f1904fb73c` | [`docs/research/software-production/16_THREE_RUN_SYNTHESIS_AND_DELIVERY_ASSURANCE_20261015/DELIVERY_ASSURANCE_HISTORICAL_FAILURE_TO_VALIDATOR_MAP_V0_1_20261019.md`](assurance-sources-20261109.md#t-f353) |
| <a id="source-v12"></a>V12 | AI_Research_Toolkit / `origin/research/software-production-decision-20261013` | `ae2766a62b1546048ec6122e01ee95f1904fb73c` | [`docs/research/software-production/17_DELIVERY_ASSURANCE_ARCHITECTURE_CLOSURE_GPT_WORK_R0/06_FINAL_ARCHITECTURE_CONTRACT.md`](assurance-sources-20261109.md#t-f639) |
| <a id="source-v13"></a>V13 | AI_Research_Toolkit / `origin/research/software-production-decision-20261013` | `ae2766a62b1546048ec6122e01ee95f1904fb73c` | [`docs/research/software-production/22_DELIVERY_ASSURANCE_GLOBAL_WORK_RESEARCH_20261022/WORK_OUTPUT/CURRENT.md`](assurance-sources-20261109.md#t-f719) |
| <a id="source-v14"></a>V14 | AI_Research_Toolkit / `origin/research/software-production-decision-20261013` | `ae2766a62b1546048ec6122e01ee95f1904fb73c` | [`docs/research/software-production/22_DELIVERY_ASSURANCE_GLOBAL_WORK_RESEARCH_20261022/WORK_OUTPUT/03_END_TO_END_EXECUTION_AND_VALIDATORS.md`](assurance-sources-20261109.md#t-f702) |
| <a id="source-v15"></a>V15 | AI_Research_Toolkit / `origin/research/software-production-decision-20261013` | `ae2766a62b1546048ec6122e01ee95f1904fb73c` | [`docs/research/software-production/22_DELIVERY_ASSURANCE_GLOBAL_WORK_RESEARCH_20261022/WORK_OUTPUT/10_ACCEPTED_BOUNDARY_AND_FINAL_ARCHITECTURE_GPT_WORK_PROMPT.md`](assurance-sources-20261109.md#t-f710) |
| <a id="source-v16"></a>V16 | AI_Research_Toolkit / `origin/research/software-production-decision-20261013` | `ae2766a62b1546048ec6122e01ee95f1904fb73c` | [`docs/research/software-production/23_SIX_REPO_VALIDATOR_SPRINT_20261022/GPT_WORK_MASTER_PROMPT.md`](assurance-sources-20261109.md#t-f721) |
| <a id="source-v17"></a>V17 | AI_Research_Toolkit / `origin/research/software-production-decision-20261013` | `ae2766a62b1546048ec6122e01ee95f1904fb73c` | [`docs/research/software-production/11_THREE_CRITIC_RECONCILIATION_V0_8/03_REVIEWER_AND_VALIDATOR_ADMISSION.md`](assurance-sources-20261109.md#t-f263) |
| <a id="source-v18"></a>V18 | AI_Skills_Collection / `origin/main` | `4de2e557f68c5071d1c3df8b71082abbafe57bb1` | [`docs/workflows/PLANNER_ROLE_CONTRACT.md`](assurance-sources-20261109.md#a-f094) |
| <a id="source-v19"></a>V19 | AI_Skills_Collection / `origin/main` | `4de2e557f68c5071d1c3df8b71082abbafe57bb1` | [`skills/core/codex-system/codex-workflow-protocol/SKILL.md`](assurance-sources-20261109.md#a-f103) |
| <a id="source-v20"></a>V20 | AI_Research_Toolkit / `本地 work/delivery-assurance-hook-probe-r2` | `005fee947bafabbfc77f47d744b4717238439905` | [`docs/research/software-production/16_THREE_RUN_SYNTHESIS_AND_DELIVERY_ASSURANCE_20261015/phase1_hook_probe_r1/FINAL_RESULT.md`](assurance-sources-20261109.md#t-f394) |
| <a id="source-v21"></a>V21 | AI_Research_Toolkit / `本地 work/delivery-assurance-hook-probe-r4` | `5f3ecc7e77c6b2deedf221cc6c717ccd1a7b78f6` | [`docs/research/software-production/16_THREE_RUN_SYNTHESIS_AND_DELIVERY_ASSURANCE_20261015/phase1_hook_probe_r4/FINAL_RESULT.md`](assurance-sources-20261109.md#t-f408) |
| <a id="source-v22"></a>V22 | AI_Research_Toolkit / `origin/research/software-production-decision-20261013` | `ae2766a62b1546048ec6122e01ee95f1904fb73c` | [`docs/research/software-production/20_DELIVERY_ASSURANCE_USER_VALUE_REVISION_V0_5_20261022/DELIVERY_ASSURANCE_USER_VALUE_REVISION_PROPOSAL_V0_5_20261022.md`](assurance-sources-20261109.md#t-f692) |
| <a id="source-v23"></a>V23 | AI_Research_Toolkit / `origin/research/software-production-decision-20261013` | `ae2766a62b1546048ec6122e01ee95f1904fb73c` | [`docs/research/software-production/22_DELIVERY_ASSURANCE_GLOBAL_WORK_RESEARCH_20261022/WORK_OUTPUT/12_STAGED_EXECUTION_REVIEW_PACKAGE.md`](assurance-sources-20261109.md#t-f716) |
| <a id="source-v24"></a>V24 | AI_Research_Toolkit / `origin/research/software-production-decision-20261013` | `ae2766a62b1546048ec6122e01ee95f1904fb73c` | [`docs/research/software-production/19_DELIVERY_ASSURANCE_IMPLEMENTATION_PACKAGES_V0_2_20261020/PACKAGE_SET_MANIFEST.md`](assurance-sources-20261109.md#t-f679) |
