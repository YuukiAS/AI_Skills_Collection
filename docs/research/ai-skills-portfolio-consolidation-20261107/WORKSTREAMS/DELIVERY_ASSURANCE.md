# Delivery Assurance：用真实入口证明交付

Delivery Assurance 的独立产品方向已经明确。它要解决的是：代码、报告或发布包都已有结果，用户仍得亲自找出没有走通的入口、核对拿到的是哪版、把失败转给原执行任务。现有规则已经覆盖不少判断。值得独立成产品的增量是把领域验收接到真实交付入口，按证据限制当前可以承诺什么，并把可修复失败送回原任务。以下构想供正式 Planner 使用。

## 当前进度与权威来源

|层次|查到的事实|可据此作出的判断|
|---|---|---|
|056 底座|已随集合 5.0.7、Workflow Core 0.3、Bridge Kit 0.8.5 等发布。它确立了验收准入、真实界面、Human Gate 分类与同任务等待恢复，当前 Workflow Core 源文件仍保留相关要求。|继续复用。普通提示、入口或消费者未落实时，先修已有路径。 [056 正式收口](../../../../results/056_product_delivery_discipline/FINAL_INTEGRATION_RELEASE_CLOSURE.md) · [Workflow Core 入口](../../../../skills/core/codex-system/codex-workflow-protocol/SKILL.md)|
|Hook 研究|Toolkit Phase 1 R5 Attempt 3 得到 GO。受信任项目级 Stop Hook 在受测宿主拦住一次假完成，继续原任务，并在新候选产生有效证据后结束。早期未信任尝试和 R5 Attempt 2 的污染尝试分别保留。|证据限于该探针。生产 DA-G10–DA-G15、七仓消费和宿主覆盖另验。 [Phase 1 结项](https://github.com/YuukiAS/AI_Research_Toolkit/blob/a73b851a031b6146e3ef27916663280d69a772c5/docs/research/software-production/16_THREE_RUN_SYNTHESIS_AND_DELIVERY_ASSURANCE_20261015/PHASE1_CLOSURE_20261019.md)|
|v0.3 → v0.4|2026-10-20 的真实外部 Critic 对 v0.3 给出 REVISE。前三仓已有正式证据，后四仓欠具体采用合同，另有旧 locator、适配器漏项、正负链和人类边界问题。#107 仍指向补齐后等待独立审查的 v0.4 包。|保留 Critic 的反例。#107 的正文是旧执行锚点，需核对后来已形成的设计与交接。 [外部 Critic 回归](../../../../results/chatgpt-web--pass-integrity/DELIVERY_ASSURANCE_FRESH_CRITIC_REGRESSION_2026-10-20.md) · [Issue #107](https://github.com/YuukiAS/AI_Skills_Collection/issues/107)|
|远端后续设计|截至 2026-11-06，Toolkit 指定研究分支远端为 `ae2766a62b1546048ec6122e01ee95f1904fb73c`。分支历史有 `da/1` 冻结与执行包，后续 `da/2` 设计包记录了用户转交的 R3 `PROCEED`，批准范围是设计。当前 P0 探针及 Kickoff 仍是待实施前审查的未授权草稿。|沿 R3 和同任务 P0 继续。不同代接口要明确迁移或退场，旧冻结记录不足以作为新产品执行依据。没有独立审查原文可再核对。 [R3 当前状态](https://github.com/YuukiAS/AI_Research_Toolkit/blob/ae2766a62b1546048ec6122e01ee95f1904fb73c/docs/research/software-production/22_DELIVERY_ASSURANCE_GLOBAL_WORK_RESEARCH_20261022/WORK_OUTPUT/CURRENT.md) · [分阶段实施前审查包](https://github.com/YuukiAS/AI_Research_Toolkit/blob/ae2766a62b1546048ec6122e01ee95f1904fb73c/docs/research/software-production/22_DELIVERY_ASSURANCE_GLOBAL_WORK_RESEARCH_20261022/WORK_OUTPUT/12_STAGED_EXECUTION_REVIEW_PACKAGE.md)|
|消费者进展|六仓验收器实施任务已写入正式路径，本轮逐个确认 GitHub 内容对象可读，CARE 未列入该专项。指定结果路径中，Mica 有可读的验收器加固结果，其余五个指定路径本轮返回 404。Mica 加强了实际 runner 输出和候选绑定，真实登录态、目标低配设备和实际 PDF 查看器仍为 UNKNOWN。|“任务已交接”“领域验收器修好了”“DA 已从正常入口调用验收器”分别取证。五个路径的 404 只限查询分支和路径。 [六仓交接](https://github.com/YuukiAS/AI_Research_Toolkit/blob/ae2766a62b1546048ec6122e01ee95f1904fb73c/docs/research/software-production/23_SIX_REPO_VALIDATOR_SPRINT_20261022/WORK_OUTPUT/SIX_REPO_HANDOFFS.md) · [Mica 结果](https://github.com/YuukiAS/Mica-for-ChatGPT/blob/codex/mica-functional-convergence/results/mica-product-system-rebuild/validator-hardening-2026-10-22.md)|

2026-10-26 的证据先行研究可作为补充。Mica 的路线图即使列全要求，也无法凭空得到登录态下的真实界面证据。凡关键结论依赖真实设备、登录态或外部宿主，接入前先约定合法取证入口、最少人工操作、可复现方式和拿不到证据时的可交付范围。该分支提供取证方法和案例，不能代签 R3 探针。 [证据先行研究](https://github.com/YuukiAS/AI_Research_Toolkit/blob/90e43b66073cf30e2af128a9ed1a5c3f9c7cdf50/COMPLEX_SYSTEM_DESIGN_GUIDE.md) · [Mica 失败案例](https://github.com/YuukiAS/AI_Research_Toolkit/blob/90e43b66073cf30e2af128a9ed1a5c3f9c7cdf50/docs/examples/MICA_REAL_UI_EVIDENCE_GATE_FAILURE_2026-10-26_ZH.md)

## 真实案例如何进入同一套回归

|失败类型|真实案例与已有覆盖|后续接入应证明什么|
|---|---|---|
|入口和候选错配|Lucerna 在真实高 DPI 证据缺失时仍报 Windows 界面完成。Bobbio 的旧版接受记录与新分支当前里程碑可能混用。现有 056 要求核对实际界面，v0.4 又明确 locator 漂移和适配器不得删除必验项。|旧 EXE、旧运行进程或旧里程碑报告失去当前证明资格。由原专业验收器输出准确身份，通用层拒绝用旧证据升级交付声明。|
|把部件或替代路径当整条功能|CUHK_Date 的模拟 provider、单分支和手动回退掩盖了真实 hosted 路径缺口。Mica 的合成压力测试不证明目标设备的真实收益。SeminarArc 模拟器可证明指定版本的持久化或导出，真实硬件另取证。|从声明的入口跑通正常链，并按风险选择会影响结论的真实变体。相同报告里保留 mock、Emulator、真实宿主各自的证明范围。|
|验收器与产品一起被改绿|Asteria 的几何结果或科学关系不能只凭恒零计数。CARE 的调度结束和 collector 成功不足以证明训练尺度、科学比较或原控制器确实消费结果。|现有领域 owner 决定标准。保留既有好例、坏例、缺证和应保持结果，通过真实入口运行。缺证保持未知，充分的科学负结果保留其原结论。|
|最终文件或用户操作未到位|#101 实测发现 PDF 在宿主上渲染成功，用户的第一次完成回复却没有可另存的文件入口。5.4.5 / standalone 0.3 已针对该客户端完成正式发布与正常入口验证。|复用同一份 QA-passed 文件从首次完成回复可打开、可保存的正例，及文件缺失/宿主不能交付时明确报告的坏例。预览、路径、receipt、hash 可定位证据，各自不证明用户已收到。|
|验收和恢复把人当作中转|056 真实宿主证据区分 native Default-mode 问答自动结束与同任务显式回复后恢复。后续外部 Critic 再次要求从真实入口验证拒绝和恢复。|权限未知、取消、真实等待或已有副作用未查清时，保持原任务和恢复点。可解错误由原执行端接收原始差异并修复，用户只处理真正的登录、设备、授权或最终判断。|

七仓具体正负链在公开研究附录。上表合并的是可回归的同类误判，项目内业务、科学阈值及具体适配器仍分别归项目。#10 的报告比较/验收包可先映射 056 已有规则，保留实际最终对象、并排比较语义及角色证据的差异。#101 可进入回归库，正式条目保持已关闭。 [七仓附录](https://github.com/YuukiAS/AI_Research_Toolkit/blob/a73b851a031b6146e3ef27916663280d69a772c5/docs/research/software-production/16_THREE_RUN_SYNTHESIS_AND_DELIVERY_ASSURANCE_20261015/DELIVERY_ASSURANCE_SEVEN_CONSUMER_ADOPTION_ANNEX_V0_1_20261019.md) · [CUHK_Date 事故](../../../../docs/design/PRODUCT_DELIVERY_DISCIPLINE_V6_CUHK_DATE_REAL_FEEDBACK_2026-09-17.md) · [Issue #10](https://github.com/YuukiAS/AI_Skills_Collection/issues/10) · [Issue #101](https://github.com/YuukiAS/AI_Skills_Collection/issues/101)

## 产品边界与入口假设

用户仍然以原方式提出“完成并交付这个功能/文件”或“帮我核对当前候选可以交付到哪一步”。建议以 Codex 正常完成入口为主，提供一个可显式调用的只读交付检查入口，方便核验已有候选。GPT 侧适合澄清所承诺的对象、独立复核专业结论或阅读真实产物，以及解释用户现在能做什么。两端共享当前候选、要求的逐项结果、来源、实际入口与剩余限制。只有 GPT 端真的打开对应产物或使用相应入口时，它的观察才进入该候选证据。不需要为对称而设置一个能自行宣布交付的 GPT 入口。

1. **选定交付对象和必验范围。** 从原要求、已批准设计和真实消费路径选出必须的专业检查，保留分支、版本、对象与身份。低风险小改按受影响范围核验，已承诺的合法回退仍在范围内。
2. **消费专业验收结果。** 复用原生 runner、QA 和独立审查者。薄适配器传递已冻结必验项、结果与缺证原因，不能删掉或降低必验项。修改候选后让受影响的旧证据失效。
3. **在交付出口约束声明。** 分别证明源码、最终成品、安装加载、实际运行与用户可用范围。也支持已完成文件等窄任务直接提供真实文件入口。声明可按项目约定细化，不用固定层级代替实际要求。
4. **把失败送回原任务。** 复用 Bridge 的运行身份、消息传递、Stop/恢复和风险隔离，原任务收到失败后在共享预算内修复并重验。真实等待、取消和权限不足保留原边界。

Workflow Core 继续管何时可进入验收、通用选择和工作流交接。Bridge Kit 管真实执行、身份绑定、证据传输、信任与恢复。Design Assurance 管交给实现前的要求、场景和约束能否审查。Reasoned Decision 管需要先选择哪条路。领域插件和项目保有专业标准及验收器，PIE 保有项目指令投影，AI Skills Maintainer 负责实际单个消费者的安装与适配。独立 Delivery Assurance 入口的价值在于给用户一份可兑现的交付判断，同时复用上述各层。单靠把规则加厚，无法证明真实入口消费了这些规则。把它做成新的跨机控制器又会增加第二个生命周期。现有看板已经区分中央完成与 `ADAPTING`，只按冻结合同覆盖必需消费者，凭实际加载、正常入口和风险匹配证据收口。 [能力门政策](../../../../docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md) · [维护看板规则](../../../../docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md)

## 外部方案

以下均于 2026-11-06 阅读公开原始来源。采用状态描述本轮研究结论。

|来源、版本与许可|实际查阅、可借鉴之处和边界|采用状态|
|---|---|---|
|in-toto 规范 v1.0。规范仓库 MIT。USENIX 2019 作者论文页面提供开放阅读。|查了 layout、材料/成品、授权执行者、客户端 inspection 及 MATCH/REQUIRE。适合解释“原验收所用对象与用户拿到的对象一致”。签名链和摘要没有提供专业质量或 UI/实际宿主运行证明。 [稳定规范入口](https://in-toto.io/docs/specs/) · [规范](https://github.com/in-toto/specification/blob/master/in-toto-spec.md) · [许可证](https://github.com/in-toto/specification/blob/master/LICENSE) · [原始论文](https://www.usenix.org/conference/usenixsecurity19/presentation/torres-arias)|`REFERENCE_ONLY`|
|OpenSSF SLSA 1.2。Community Specification License 1.0，历史部分按仓库说明为 Apache-2.0。|核对签名、subject digest、builder 信任及明确的威胁边界。适合复用“声明必须绑定对象与有资格的观察者”这一判断。SLSA level 不证明运行正常或软件对用户可用。 [验证章节](https://slsa.dev/spec/v1.2/verifying-artifacts) · [许可](https://github.com/slsa-framework/slsa#license)|`REFERENCE_ONLY`|
|Google SRE 书中 PRR 章节。网页标明 CC BY-NC-ND 4.0。|查阅服务特定检查、交接双方、逐步移交和早期介入。适合参考“由负责消费的人说明所需证据”。整套服务交接对单个 PDF、项目小修或短研究任务过重。 [PRR 原文](https://sre.google/sre-book/evolving-sre-engagement-model/)|`REFERENCE_ONLY`|
|Pact 官方合同测试文档。Pact Specification 仓库 MIT。|查了消息接口与实际副作用的分工。可为薄适配器编写生产路径的好例、漏项、缺证及兼容例。额外部署 Broker 无法证明真实 GUI、文件落地或科学结果，当前不引入。 [合同与功能测试](https://docs.pact.io/consumer/contract_tests_not_functional_tests) · [规范仓库](https://github.com/pact-foundation/pact-specification)|`REFERENCE_ONLY`|
|Playwright Download API，自 v1.8。Apache-2.0。|官方示例在点击前等待下载事件并实际保存，跨平台 CDP issue 提供了事件发生但本地保存失败的报告。真实浏览器交付可观察保存后的字节，远程浏览器、桌面附件和实际设备分别取证。 [下载指南](https://playwright.dev/docs/downloads) · [API](https://github.com/microsoft/playwright/blob/main/docs/src/api/class-download.md) · [公开故障 #38805](https://github.com/microsoft/playwright/issues/38805) · [许可](https://github.com/microsoft/playwright/blob/main/LICENSE)|`REFERENCE_ONLY`|
|GitHub Releases 官方文档及 GitHub CLI，在线手册。文档 CC BY，CLI MIT。|查阅不可变 release 及 `gh release verify-asset` 的分工和自动生成源码压缩包例外。适合对已正式上传资产做用户侧字节核对，仍需单独验证安装加载与正常入口。 [发布完整性](https://docs.github.com/en/code-security/how-tos/secure-your-supply-chain/secure-your-dependencies/verify-release-integrity) · [文档许可](https://docs.github.com/en/contributing/style-guide-and-content-model/style-guide#licensed-content) · [CLI 许可](https://github.com/cli/cli/blob/trunk/LICENSE)|`REFERENCE_ONLY`|

## 后续正式审查

- **沿现有 R3 准备最小 P0。** 对现有 Windows 非交互 CLI 单元进行实施前审查，明确当前宿主版本、信任、入口、同任务恢复、取消后零重复动作及权限。Desktop、交互式 CLI、Remote 证据单列。先回答未调用显式完成 helper 时，实际完成出口是否仍会检查。
- **选择现有 Lucerna 首片检验净收益。** 正例由原入口消费当前候选和原专业角色结果，再由当前用户拿到对应结论。坏例包括旧 PID/截图、缺独立结果、同时改坏例标准、取消后重复执行。真正发版所需的 Windows、设备或账号观察待该任务获得明确授权。先比较用户提醒、手动转发和首个发现问题的人，再决定扩大。
- **让其他项目的验收器修复独立推进。** 依据六仓 handoff 和当前结果继续核对。保留已发布 PDF 首次交付正例及无入口坏例、Mica 合成证据不能升级的反例，以及 CARE 的真实负结果与临时等待反例。普通文档变更保留轻量入口。按现有分发和消费者规则验证已安装、已加载且实际使用。
- **留给 Planner 的决定。** 以哪个精确提交作为产品权威，并如何把 #107 过期锚点与当前设计关联。哪些宿主能强制执行、哪些只能显式有限检查。何时启用旧接口兼容或退役。首片应达到的净收益与可承受延迟。七仓中各阶段真正必需的消费者、现场授权和最终声明上限。设计审查通过、探针成功、任务交接、专业验收和生产启用分别记录。
