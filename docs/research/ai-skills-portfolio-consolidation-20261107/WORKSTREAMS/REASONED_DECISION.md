# Reasoned Decision｜把判断做完，再决定怎么做

**建议把现有 v0.1 送交正式 Critic。** 新案例强化了原架构对目标保持、证据裁决和复用现有能力的要求。第一版最需要审查的是两处可执行边界。助手能否在首次推荐前发现足以改变选择的现有能力？关键证据仍缺时，交给 Codex 的调查是否允许推翻推荐？这些问题可以在现有架构内解决。独立 Plugin 的方向已经明确，本轮只提出研究判断。

## 当前依据

初扫基线为 `c83ee4b5ab41d0cd4955916e4c81f71de954cbfd`，交付基线为 `ff5be718a533bf603dc375b52d7dd9f7b6136119`。两次扫描之间，主线只补了 UU 案例的后续证据。v0.1 标记为 `DESIGN_CONVERGED_FOR_REVIEW`，尚无生产实现。在该提交的 Marketplace、skill 注册和发布记录中，未见已发布的 Reasoned Decision 入口。中央 TODO 有 4 条 `NEW`，未绑定 `tracking: #N`。公开 Issue 的精确名称搜索也未找到专属条目。远端历史分支 `research/judgment-integrity-20261024` 的 tip 为 `9c32e83`，该提交仅记录早期判断不稳的研究笔记。原 standalone 文件的 `NEW` 样本继续作为历史证据，文件整体已让位于独立 Plugin 设计。 [中央 TODO](../../../plugin-todos/reasoned-decision.md) · [历史种子](../../../skill-todos/reasoned-decision.md) · [Marketplace](../../../../.agents/plugins/marketplace.json) · [历史分支提交](https://github.com/YuukiAS/AI_Skills_Collection/commit/9c32e83bf4644129643e36033dffda843f170101)

权威设计保留三层职责。Task State Integrity 是每次进入时都要消费的状态合同。Judgment Integrity 与 Solution Design 是两个内部 skill。实际工作在三层间按证据往返，先查真实解空间，再裁决和映射需求，依次考虑采用、组合和小幅扩展。有证据表明残余缺口确实无法覆盖，才考虑自建。决定正式推荐后，只允许新证据、约束变化、前提纠错或选项实质变化触发 `Decision Delta`。设计和配套基线的证据身份有别，后者留存推导与案例，前者定义当前审查对象。 [v0.1 架构](../../../design/reasoned-decision/REASONED_DECISION_V0_1_ARCHITECTURE_2026-11-05.md) · [人类问题解决基线](../../../design/reasoned-decision/REASONED_DECISION_PRIOR_ART_AND_HUMAN_BASELINE_2026-11-05.md)

## 把新案例收进已有能力

| 共用能力 | 实际观察与证据 | 研究判断 |
|---|---|---|
| 保住用户的整体目标和当前事实 | Edge 把浏览器本体更新误认成扩展更新，又从历史材料引入当前用户未设的 WebView2 约束，随后污染诊断提示。UU 远控把跨应用的完整键盘体验缩成单个快捷键，一度推荐会改变终端语义的全局换键。BWG/GFW 记录里已完成的动作在后续轮次被重新讨论。 [Edge](../../../design/reasoned-decision/evidence/EDGE_WINDOWS_DECISION_FAILURE_2026-11-05.md) · [UU](../../../design/reasoned-decision/evidence/UU_REMOTE_KARABINER_DECISION_FAILURE_2026-11-07.md) · [BWG/GFW](https://github.com/YuukiAS/AI_Research_Toolkit/blob/6779cbba31002de284f1c1cb35c1ace305e49e7e/docs/research/reasoned-decision/TODO.md) | 现有 Task State 已覆盖。验收时看最终推荐是否实际消费目标、当前约束、已完事项和反例，单独输出一张状态表不能证明这点。 |
| 先找到足以改变排序的现有方案 | iTerm2 发现原生 Profile 选项后，shell hook 才退为有条件的备选。微信与 Finder 右键案例分别缺少本地语言用户报告、版本兼容或采用与维护信息。Tailscale 泛用恢复文档没有回答当前 Standalone 持久身份到底在哪里。同型 Issue 提供了保留 App 的恢复证据。 [iTerm2](../../../design/reasoned-decision/evidence/ITERM2_SSH_MOUSE_REPORTING_DECISION_FAILURE_2026-11-06.md) · [中央 TODO 的微信记录](../../../plugin-todos/reasoned-decision.md) · [Finder 固定回归](https://github.com/YuukiAS/AI_Research_Toolkit/blob/6779cbba31002de284f1c1cb35c1ace305e49e7e/docs/research/reasoned-decision/regression/RD-REG-001-MACOS-FINDER-RIGHT-CLICK-SOFTWARE-SELECTION.md) · [Tailscale](../../../design/reasoned-decision/evidence/TAILSCALE_MACOS_CLONED_IDENTITY_DECISION_FAILURE_2026-11-06.md) | 合在 Solution-Space Discovery 内。不同来源承担不同证明义务。官方文档核对支持范围，开发说明定位限制，维护者或用户一手报告发现同型失败与成功候选，当前现场裁决能否采用。检索按问题选择语言和社区。来源数量或产品知名度不能替代适用性。 |
| 证据改变多少，就更新多少 | Edge 与 Mac 显示器案例反复换路线，部分修改有合法纠错，部分仅因追问。Asteria 的新证据只证明 Codex 也能发现问题，是否足以改变主盲审者的选择另需核对评审目标。UU 经两轮局部方案被否定后，应先看远程事件是否进入既有处理链。 [Edge](../../../design/reasoned-decision/evidence/EDGE_WINDOWS_DECISION_FAILURE_2026-11-05.md) · [显示器案例](https://github.com/YuukiAS/AI_Research_Toolkit/blob/6779cbba31002de284f1c1cb35c1ace305e49e7e/docs/research/reasoned-decision/REAL_USE_EVIDENCE.md) · [Asteria](https://github.com/YuukiAS/AI_Research_Toolkit/blob/6779cbba31002de284f1c1cb35c1ace305e49e7e/docs/research/reasoned-decision/TODO.md) · [UU](../../../design/reasoned-decision/evidence/UU_REMOTE_KARABINER_DECISION_FAILURE_2026-11-07.md) | 已有 `Decision Delta` 和连续失败时收缩。验收用成对输入。仅追问理由时保持推荐，提交足以推翻前提的新证据时改受影响部分。两个未知都重要时按依赖次序检查，先做能决定是否值得调查第二项的动作。 |
| 推荐强度与行动授权各有依据 | Tailscale 在完成调查前就把删除应用写入执行要求，引出系统权限申请。后续外部证据支持较小恢复路径，但当前环境仍需核对状态归属与可用恢复能力。UU 的官方 fallback 说明不能证明特定远控版本会被稳定捕获，也不能证明会话信号可靠。历史身份核验的用户认可样本给出了单一优先选项与明确停止条件，同时区分当步核验和长期账户状态。 [Tailscale](../../../design/reasoned-decision/evidence/TAILSCALE_MACOS_CLONED_IDENTITY_DECISION_FAILURE_2026-11-06.md) · [UU](../../../design/reasoned-decision/evidence/UU_REMOTE_KARABINER_DECISION_FAILURE_2026-11-07.md) · [历史正例](../../../skill-todos/reasoned-decision.md) | 结论强度和可逆性已经在设计中。值得新增到审查的是接口断言。关键前提未定时，交接只给可证伪的调查和停手条件。即便某动作已有足够推荐证据，是否实际执行仍按原授权边界。历史正例只评价回答结构，保留为当时的行为证据。 |
| 决定和解释分开验收 | 有关 Reasoned Decision 架构的总结曾丢失明确请求的比较、合并理由或运行顺序，即使判断本身已逐渐收敛。UU 的首要回答是能实现到什么程度，随后才解释事件和设备限制。 [Clear Writing 负例](../../../../skills/writing/core/response-clarity/references/reasoned-decision-summary-architecture-negative-example-2026-11-05.md) · [UU](../../../design/reasoned-decision/evidence/UU_REMOTE_KARABINER_DECISION_FAILURE_2026-11-07.md) | 判断内容、证据和条件由 Reasoned Decision 提供。读者能否一次看懂完整结论归 Clear Writing。可用同一个对话测两个输出，但两类失败分别归主责。 |

近期失败多来自本地计算与远程环境。它们能区分数类判断失误，但同一环境的多个案例不能自动视作跨项目独立验证。Asteria 及历史身份核验样本扩大了任务类型，后续仍需要一个此前未参与设计的场景。Edge 取证以仓库记录为界，本次没有重看原始对话附件或复现原机器。Tailscale、iTerm2 与 UU 的现场最终效果同样未在这次研究中复验。命令、身份存储位置、快捷键和厂商参数留在项目证据，回归保留的是触发条件、原错法与应观察的行为。

UU 新补证还提供了一个可观察的回归分界。仓库记录已验证通过 CGEventTap 捕获的一项输入能命中既有规则，设备 ID 仍不可区分。用户目标是保留远控时的键盘体验，识别每个事件的物理设备只是一个实现假设。宣布阻塞前，应先检查可保留唯一远控通道的 UU 会话信号。独立查看的 companion 源码提供了覆盖窗口和辅助功能设备列表两条信号，当前宿主效果与长时间稳定性仍待测。建议把“无法完成”与“某条路线受限”纳入同一 `Gap Proof` 审查，要求停手决定也给出用户目标和可用替代的证据。[主线补证](https://github.com/YuukiAS/AI_Skills_Collection/commit/ff5be718a533bf603dc375b52d7dd9f7b6136119) · [外部源码核对](../EXTERNAL_PRIOR_ART.md#领域与客户端补充取证)

## 外部研究

下列外部资料于 2026-11-06 检查。采用状态只记录本轮结论。

| 来源、版本和授权 | 检查结果与适用边界 | 采用判断 |
|---|---|---|
| Consortium for Service Innovation 的 KCS® v6 Practices Guide，2023-06-08 版，CC BY-NC 4.0。 [原指南](https://www.serviceinnovation.org/included/docs/KCS_v6_Practices_Guide_2023_06_08.pdf) | 检查 Solve Loop 的 Capture、Reuse、Improve 和版权页。把请求者场景带进搜索、边解决边复用已有经验，能防止遇到每个新问题都自建。方法针对组织知识库，缺少开放生态适用性核对和高影响动作判断。KCS® is a service mark of the Consortium for Service Innovation™. | `REFERENCE_ONLY`。借鉴早查、随新事实复查的行为，保留当前仓库与官方生态入口。 |
| Google SRE，第一版 2016 年，出版版权页注明 © Google, all rights reserved。 [排障章节](https://sre.google/sre-book/effective-troubleshooting/) · [出版版权页](https://www.oreilly.com/library/view/site-reliability-engineering/9781491929117/copyright-page01.html) | 检查假设检验、逐层缩小范围、风险匹配的最小测试和负结果案例。适合定义 UU、Edge 的关键未知如何裁决。运行故障归因与可选长期方案排序需要不同证据，章节没有覆盖后者。 | `REFERENCE_ONLY`。采用思想层面的证据顺序，不复制章节。 |
| `obra/superpowers` 的 `systematic-debugging`，skill 最近改动 `bb92a77741419a4ab5f06e711a283343f1ada0c3`，MIT。 [Skill](https://github.com/obra/superpowers/blob/bb92a77741419a4ab5f06e711a283343f1ada0c3/skills/systematic-debugging/SKILL.md) · [许可证](https://github.com/obra/superpowers/blob/main/LICENSE) | 检查四阶段、单变量验证及三次失败后质疑架构。对于代码故障能减少盲修，然而它从已出现的故障进入，对产品选择、环境真实方案搜索和跨轮改判的范围不同。把每次判断受挑战都升级到架构讨论会重现 Edge 的扩张问题。 | `REVIEWED_NOT_ADOPTED`。可作定向调试对照，不移植 Skill、不照搬次数或升级规则。 |
| Michael Nygard 的 ADR 说明（2011-11-15，文章未核实可再分发授权）及 `npryce/adr-tools`（`master`，访问日。工具 GPL-3.0-or-later，工具生成内容 CC BY 4.0）。 [ADR 原文](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions) · [工具许可证](https://github.com/npryce/adr-tools/blob/master/LICENSE.txt) | 检查记录上下文、决策状态、后果与取代关系的做法。对跨人交接的重大架构决策有用，无法判断当前问题是否答对、现实方案是否调查充分，也不足以约束日常对话里的决策漂移。 | `REVIEWED_NOT_ADOPTED`。Reasoned Decision 可在已有交接中给一段简短的改判依据，项目自己的 ADR 可继续由项目保存。 |
| Sierra 的 τ-bench，arXiv:2406.12045v1（2024-06-17，论文 CC BY 4.0，代码 MIT）。 [论文正文](https://arxiv.org/html/2406.12045v1) · [代码许可证](https://github.com/sierra-research/tau-bench/blob/main/LICENSE) | 检查多轮用户、领域政策、真实工具状态与 `pass^k` 一致性评价。可借鉴以行为轨迹和结果判分，而不是数输出中出现了多少术语。零售、航空和模拟用户无法代表开放检索或现场授权。 | `REFERENCE_ONLY`。将“用户只问理由”和“用户带来新约束”设计成成对回放，风险较高的场景重复验证。不照搬基准、样本数或分数。 |
| Tailscale 官方重复地址文档与上游 Issues #14913、#18308（访问日。上游代码 BSD-3-Clause，讨论内容仅引用）。 [官方文档](https://tailscale.com/docs/reference/troubleshooting/network-configuration/multiple-devices-same-100-x-ip-address) · [#14913](https://github.com/tailscale/tailscale/issues/14913) · [#18308](https://github.com/tailscale/tailscale/issues/18308) | 通用文档列出完整恢复，#14913 有维护者给出的 Standalone 同型路径和原报告者确认。#18308 提供额外身份存储的检查线索。Issue 的关闭状态不能替代现场验证，也不能证明当前版本任一叫 Reset 的界面会作用于同一份状态。 | `REFERENCE_ONLY`。保留为已知回归中的证据排序材料。 |
| iTerm2 Terminal Profile 文档（访问日。iTerm2 仓库标注 GPL-2.0，文档仅作引用），Karabiner-Elements v16.3.0（源仓库标注 Unlicense，外部组件另看各自许可）。 [iTerm2 选项](https://iterm2.com/documentation-preferences-profiles-terminal.html#restrict-mouse-reporting-to-alternate-screen-mode) · [Karabiner 发布记录](https://github.com/pqrs-org/Karabiner-Elements/releases/tag/v16.3.0) · [Karabiner 开发说明](https://github.com/pqrs-org/Karabiner-Elements/blob/v16.3.0/DEVELOPMENT.md) | 核对 alternate-screen 选项及设备身份限制。前者说明查已有配置能缩小维护范围。后者说明原生能力也有边界，捕获事件和保持物理设备语义需要分开验证。 | `REFERENCE_ONLY`。保留两种不同的原生能力发现样本。 |
| V2EX 微信更新现场帖（2025-12-02，未核实转载许可）、WeChatTweak `master` 与 #847（2025-07-25，项目 AGPL-3.0）。 [V2EX 实报](https://www.v2ex.com/t/1176334) · [项目说明](https://github.com/sunnyyoung/WeChatTweak) · [#847](https://github.com/sunnyyoung/WeChatTweak/issues/847) | 检查发帖人观察、版本限定、阻断更新的副作用，以及项目说明宣称的能力和 Issue 中的失效报告。这个组合能发现官方功能说明之外的线索。社区报告无法证实未检查版本的兼容性，patch 也不适合作为通用依赖。 | `REFERENCE_ONLY`。只保留检索和核验方法，项目命令不进入插件。 |

## 第一版研究构想

用户可以直接问“这几条路线该选哪一条”“为什么改推荐”“这个故障能不能修到我要求的程度”，也可以明确调用 Reasoned Decision。适合存在真实取舍、上下文会改变选择、或者猜错代价明显的任务。简单事实与已冻结的机械执行沿用现有入口。初版建议验证四件事。

1. **当前目标能穿过多轮。** 同时保留用户期望结果、硬约束、已经排除的路径和待裁决问题。新症状先作为证据进入判断，再决定是否需要改目标。
2. **主动发现现成能力并缩小改动。** 从当前系统、原生设置和可访问的既有仓库出发。若版本兼容性、长期维护或当前推荐对比取决于真实案例，按实际生态查官方实现、维护者讨论及本地语言社区。自建前说明哪条硬约束还有缺口。
3. **给出能行动的推荐和停手条件。** 有足够证据时明确首选和主要取舍。条件未证实则给出可判定的下一步和可见的失败结果。若无法拿到证据，保留条件性结论，避免把候选状态写成已交付。
4. **把关键未知交给能查的一端。** 交接保持简短，写清任务目标、硬约束、已淘汰路径、要观察什么、哪些结果会改判以及检查边界。调查提示允许候选被证伪。修复提示仅在有足够证据及权限时产生。简单决策可留在当前对话。

| 使用面 | 候选职责 |
|---|---|
| GPT | 问清目标、比较选项、检查关键公开证据、交付可执行判断。能独立结束无需现场的咨询或取舍。遇到无权访问的系统只标出会改变判断的未知，避免让用户代做能交给授权工具核实的检查。 |
| Codex | 从当前 repo、版本、配置、现场读到事实。需要跨端时按最小范围回传来源、观察、局限和反证。用户直接在 Codex 提出非平凡决策时，可以在同一入口完成判断和只读调查。第一版优先验证这条场景和接收最小核验交接的场景，再决定是否要做完整对称的入口。 |
| 共享 | 当前问题和成功标准、证据类型、结论强度、改判依据、最小验证、应保留的行为。交接格式优先沿用既有任务提示或文件，由 Planner 决定是否确有互操作需求。 |

通用选路与具体领域判断分开。Reasoned Decision 对“选哪条路线，下一条证据能改变什么”负责。Design Assurance 接续复杂路线的多路研究、独立盲区检查及设计冻结。Asteria 的具体产品选项由 Asteria 项目拥有。workflow-core 承接任务身份、工具授权、执行和复审路由。它的 W4 已防止执行中盲目重试。Reasoned Decision 补的是动手前或跨轮交流中的证据裁决。Delivery Assurance 接受冻结交付对象并核验实际候选。Clear Writing 消费最终判断和限制，处理读者表达。Web Development 的已有参考调查可在前端案例中提供领域来源筛选。统计、医学等领域的事实和有效性由领域专业能力核对。 [架构分界](../../../design/reasoned-decision/REASONED_DECISION_V0_1_ARCHITECTURE_2026-11-05.md#13-与其他插件的边界) · [workflow-core](../../../../skills/core/codex-system/codex-workflow-protocol/SKILL.md) · [Clear Writing](../../../../skills/writing/core/response-clarity/SKILL.md) · [前端参考调查](../../../../skills/tools/frontend/frontend-reference-research/SKILL.md)

相比通用搜索 skill，独立入口有机会同时验收跨轮状态、推荐稳定性和方案复用。相比把判断拆给多个审查角色，先把一条可追问、可证伪的主线做实，更符合已观察到的失败。初版沿用现有三层、两个内部 skill。搜索是行为的一部分。暂缓独立 `search-first`、默认委员会、决策数据库、自动触发的角色堆叠以及每个问题都写 ADR。遇到已有专业工具时优先调用它的正常入口。

## 正式评审应决定什么

- **如何判断已经查够。** 重点看会改变候选排序的决定性事实，而非资料数量。一般设置只需低成本核对。卸载、重装、重认证或服务中断等建议，应额外看实际状态归属、同型适用证据和可逆方案。若关键来源无法读到，评审应检验助手能否给出下一步而不宣告不存在成熟路线。
- **怎样在交接里保存当前任务。** 检查何时需要跨轮锚点，怎样区分用户要求、历史背景、待检验假设与本次授权，怎样在接收端判定仍是同一现场。Tailscale 负例需要可独立核查的断言。调查合同是否只锁结果和保护边界？已推荐动作是否仍遵从授权？
- **怎样组织首批回放。** Edge/UU 作多轮负例，观察追问、两条路线被否定、关键未知变化和没有新证据四种转折。Tailscale/iTerm2 作影响范围和原生能力正反对照。Finder 已有固定回归及示范回答。历史身份核验样本和 Obsidian Graph 设计场景验证明确首选、停止条件和主动找到未点名的成熟路线。Obsidian 目前是文档中的正向场景定义。冻结至少一个新任务族，避免把已知回放当泛化。另做一条确定的简单任务，检查调用开销及相邻领域能力。
- **如何拿到验收证据。** 优先观察普通用户入口下的首次推荐、关键来源及实际采用、无证据追问时的保持、真实反证出现时的局部改判，以及下游是否提前出现越界动作。对交接承诺，至少有一条完整路径实际交给接收端并消费回传。候选方案可以用干净的只读/隔离环境验证。哪些高风险现场无法复现，应作为待验收边界。该选择留给正式 Planner 与 Critic。 [能力验收政策](../../../workflows/PLUGIN_CAPABILITY_GATE_POLICY.md)

本轮建议由 Critic 审三层架构是否足以执行上述行为，再由 Planner 冻结入口、跨端最小交接和验收样本。可把 4 条 `NEW` 按“调查适用方案”和“跨轮维持正确决策”归并到既有能力的回归集合，保留各自的证据和边界。中央 TODO、Issue 和 Project 均以原状态为准。
