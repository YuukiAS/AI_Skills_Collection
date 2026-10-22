Clear Writing 0.6 的代码实施与 Codex 候选回归已完成，可以交回 Phase C。正式个人插件尚未更新，0.6 尚未发布；ChatGPT Web 验收和 G6 留给后续阶段。

本轮沿用批准的写作实现，只补齐候选回放的可选模型传参，并修复真实结构重写暴露的两项 helper 问题：必要技术身份被误判为流程泄漏，以及两个 CLI 入口对提示词末尾换行的处理不一致。写作规则、六个入口、权限和验收标准均保持在已批准的范围内。

Codex 按用户最新决定使用固定 CLI `0.153.4` 的正常默认入口，没有传模型或推理档位参数。真实子进程记录为 `gpt-6-astra`，`reasoning_effort=None`（CLI 未显式设置该项）。此前强制使用历史模型时出现的 HTTP 400 仅保留为基础设施诊断。

18 项已知开发回归和 4 项保护性对照的首次完整产品答案均经独立审阅，覆盖复杂技术汇报、必要长篇数学说明、完整中文文档与结构重写、英文科研、UI、精确输出及混合机器内容。22 份首次答案绑定 `157725b909775e169926c449844301e772e50f08`。最终提交仅修改 helper；受影响的结构重写已使用原始输入、阶段包和首次成稿，在真实安装的新候选中完成全链路复验，没有重新生成文稿。

证据仍有以下限制：精确 JSON 样本逐字符一致，按纯精确输出豁免未读取 Skill；回放器退出码 1 原样保存，不称其为通用回放成功或加载后旁路。另两项文稿的完整文件已独立审阅，但读取命令在日志中返回空正文；不虚构可见回读记录，也不以本地结果替代 Web 关口。

最终代码的 397 项全仓测试通过，源与生成物、支持文件及确定性分发检查通过；必需 CI [39743659101](https://github.com/YuukiAS/AI_Skills_Collection/actions/runs/39743659101) 四项通过，独立实施审查无剩余缺陷。

当前执行锚点：

- task：`clear-writing--single-entry-artifact-finalization`。
- branch：`design/clear-writing--single-entry-artifact-finalization`。
- 唯一最终候选源：`cee207d3fa83ad4571f94774f3896798d837a5ca`。
- 候选身份：`results/clear-writing--single-entry-artifact-finalization/candidate/FINAL_CANDIDATE.json`。
- 当前交接：`results/clear-writing--single-entry-artifact-finalization/v0.4/PHASE_C_HANDOFF.md`。
- ChatGPT 包装 ZIP：185820 bytes，SHA-256 `775432e7d98ca975d17cec2c672a72aaabd6d24b9d19d46d07c80bb27e749aa5`；分发片和回执位于同一 `v0.4/` 目录。

下一接收方是原 ChatGPT Planner / Phase C：核对真实账户，保存真实备份，验证恢复包及 Web 入口的前置条件，然后按原合同安排后续正式验收。Web 仍使用 `GPT-5.6 Sol`，与本轮 Codex 默认运行配置分开。本轮 Codex 在代码阶段结束，不自行更新个人插件或运行 G6。

本 Issue 保持 open；维护看板保持 `DOING`，Area=`writing-style`，Resolution commit 留空。#73 和 #49 的下游接入仍 pending，不将本轮代码完成记为更广泛推广任务 DONE。旧 `079bd7987bb33d624d244feb415327d5cf2343d8` 及其历史回放永久仅作历史记录。


<details>
<summary>此前执行记录（仅供历史追溯，以当前执行锚点为准）</summary>

问题：

Clear Writing 0.6 要让 ChatGPT 和 Codex 使用同一套写作规则：先围绕用户的问题组织必要内容，生成全文后重新通读并实际返修；需要保存的文档必须单独完成全文处理、写入和回读，不能用清楚的聊天说明代替。

当前进度：

用户已批准同一任务的 v0.4 执行包 `48c42f89d23ba168e2d2045034a7f7117c2e0448`。共享源文、ChatGPT 单入口、Codex 生成物，以及用于安全恢复 ZIP/tar.gz 的读取器，都已在原分支实现。本地 389 项单测通过，完整 CI 结果见当前证据目录。六条入口均未删除、合并或改名；英文科研和界面文案没有新增专业语义，其他插件未修改。

新版的已知回归和保护性对照尚未运行，不能沿用旧 13 组 PASS。旧候选 `079bd7987bb33d624d244feb415327d5cf2343d8` 仅作为历史记录保留，已明确标记为不可发布；新版 FINAL_CANDIDATE 尚未冻结。

当前执行锚点：

- task：`clear-writing--single-entry-artifact-finalization`。
- branch：`design/clear-writing--single-entry-artifact-finalization`。
- 实现提交：`0b4248c7eb2abd4b03a06c97061aa895a556a0e7`。
- Plan：`docs/design/clear-writing/CLEAR_WRITING_0_6_PRODUCT_AND_EXECUTION_PLAN_V0_4_2026-10-22.md`。
- 证据：`results/clear-writing--single-entry-artifact-finalization/v0.4/`。
- 精确交接：`results/clear-writing--single-entry-artifact-finalization/v0.4/PLANNER_HANDOFF.md`。

下一步：

下一步由原 Planner 解决候选回放入口无法保留既定 `gpt-6.1-sol/high` 配置的问题。原模型身份已通过实际日志核实，但现有候选入口固定忽略用户配置，也没有模型配置的传参入口，调用时未显式传入模型配置；另一个 Bridge 回放入口也不能证明安装的是精确对应的候选版本。当前没有发送新的候选模型请求，不更换默认模型，也不把读取候选源码计作 G5。

入口问题解决后，在同一任务中继续开展实际回归、完整产物审查，并冻结最终候选。更新任何个人插件之前，仍须取得真实账户的 0.5 archive 字节、验证恢复包，并确认 helper 与 fresh Web/GitHub 路径可执行。当前尚未更新个人插件（无 live update），正式 G1-G6 均未运行，G6 未选择，0.6 未发布。

Issue #13 保持 open，生命周期为 `DOING`，Area 为 `writing-style`，Resolution commit 留空。#73 与 #49 的下游接入仍未完成（pending）；本任务不修改这些插件，0.6 成功也不会自动关闭 #13。该入口缺口不代表 Clear Writing 产品 FAIL，也不意味着因 Plugin Creator 缺席而在本地停工。

<details>
<summary>历史记录（v0.4 本轮实施交接前，原文保留，不代表当前执行授权或结果）</summary>

## 最新状态（2026-10-20，Clear Writing 0.6 内容选择修订）

新增真实使用回归证明：用户显式选择 Clear Writing，且 `response-clarity` / `writing-fidelity` 已进入生成上下文后，普通聊天仍可能把“分析时需要读取的全部技术证据”误当成“用户必须阅读的正文”。因此当前 0.6 不再继续 Phase C live mutation，而是在**同一个任务**中修订 `CHAT_RESPONSE` 内容选择机制。

当前 Planner 已冻结新版方向：由唯一 `clear-writing` 入口先根据用户问题确定需要展示的结论、机制、可信证据、限制和行动，再交给现有 `response-clarity` / `writing-fidelity`。六项 canonical writing route、Codex direct exposure、GitHub external-finalization、G1-G6 顶层结构和版本方向均保留。

新版 execution-ready package：
- commit：`f2dc07cdd396f43788236a04e28f445fe1bfd3ec`
- Proposal：`docs/design/clear-writing/CLEAR_WRITING_0_6_CHAT_RESPONSE_CONTENT_SELECTION_PROPOSAL_V0_2_2026-10-20.md`
- Plan：`docs/design/clear-writing/CLEAR_WRITING_0_6_EXECUTION_READY_PLAN_V0_3_2026-10-20.md`
- Goal：`docs/goals/CLEAR_WRITING_0_6_SINGLE_ENTRY_ARTIFACT_FINALIZATION_GOAL_V0_3_2026-10-20.md`
- Runbook：`docs/design/clear-writing/CLEAR_WRITING_0_6_GATE_EXECUTION_RUNBOOK_V0_3_2026-10-20.md`

旧候选 `079bd7987bb33d624d244feb415327d5cf2343d8` 保留为历史实现基线，但不再是新版 0.6 的 release candidate。正式 Personal Plugin 仍是 `0.5.0`，没有进行本轮 live update。

Phase C 的两个既有问题同时收拢：真实 0.5 archive 的 tar.gz 兼容修复将与新版 wrapper 放进**同一个下一候选**；fresh ChatGPT Web 验收与 archive/mutation 不再假设必须由同一个工具表面完成。当前唯一下一步是原独立 Critic 审查上述新版 package；Critic PASS 前不启动 Codex、不更新 Personal Plugin、不运行正式 G1-G6。

Issue #13 继续 open / DOING；Resolution commit 为空；#73 / #49 downstream adaptation 仍 pending，0.6 修订不改变这些事实。

---

问题：

Clear Writing 的个人插件需要一个总入口，能识别同一请求中的聊天说明和完整文档，并分别完成写作处理与验收。对于 GitHub 文档，只有读取全文、完成候选全文的终审、写入并确认回读内容逐字一致后，才能声称已完成。

当前进度：

0.6 执行包已获用户批准，本地候选已实现并推送。全仓 370 项测试、GitHub CI 的 4 项必需检查，以及 9 组已知回归和 4 组保护性对照均已通过。独立实现审查的实际结论见证据目录中的 `review/IMPLEMENTATION_REVIEW.md`。六项专业 Skill 的源正文、profile 和 Codex 六入口保持不变。

本轮生命周期为 `DOING`，Area 为 `writing-style`，Issue #13 保持 open，Resolution commit 留空。正式发布版本仍为 `writing-style 0.5` / 仓库 5.5.1；0.6 尚未发布，Personal Plugin 尚未由本轮更新，G1-G6 尚未运行。

当前执行锚点：

- 任务：`clear-writing--single-entry-artifact-finalization`。
- 分支：`design/clear-writing--single-entry-artifact-finalization`。
- 批准执行包：`d7b810d194ead881303aaca9c2e4f1d59a97c1f1`。
- 实现候选：`079bd7987bb33d624d244feb415327d5cf2343d8`。
- CI：`https://github.com/YuukiAS/AI_Skills_Collection/actions/runs/39368960081`。
- 证据目录：`results/clear-writing--single-entry-artifact-finalization/`。

下一步：

由批准包指定的 ChatGPT 阶段读取候选与完整证据，完成账户只读回读、准备恢复包、更新现有 PRIVATE 插件，并执行 G1-G6。ChatGPT 可根据证据目录中的 `transport/MANIFEST.json` 与有序纯文本分片重建候选 ZIP，无需手工上传 ZIP。G3 必须实际取得 GitHub 最终全文，不能以聊天说明或本地回放替代。只有全部必需验收关口和最终完整产物审查通过后，才进行正式 0.6 发布并收尾。

本地回放只证明开发阶段的已知回归，不证明 ChatGPT 账户上的插件已更新或真实 Web 验收已通过；缺少 Codex Plugin Creator 工具不再视为本地实施的阻塞因素。

原有下游接入仍未完成：#73 对应 `docs/plugin-todos/statistical-modeling.md` 中的 `Delegate reader-facing wording without giving away statistical semantics`；#49 对应 `docs/plugin-todos/scientific-visualization.md` 中的 `Delegate captions/annotations without giving away visual semantics`。本轮不实施这些接入，0.6 成功也不自动关闭 #13。

<details>
<summary>历史记录（截至本轮 0.6 实施交接前，原文保留，不代表当前状态或待执行指令）</summary>

问题：

让 Clear Writing（`writing-style`）成为可由各领域复用的表达层：改善普通解释、科研文档和图表文字的可读性，同时保留事实、公式、不确定性、精确机器字符串及各领域的专业判断。

当前进度：

Clear Writing 0.5 已随仓库 5.5.1 正式发布，并已整合回 main。现有 PRIVATE 插件已由 ChatGPT / Plugin Creator 更新至 0.5.0。用户确认已实际回读全部 27 个文件并逐文件比对，结果无漂移；版本统一为仓库 0.5 对应网页端 0.5.0。

#13 保持 open，生命周期为 `ADAPTING`，Area 为 `writing-style`。统计结果和科研图表的下游接入仍未完成；正式发布成功不代表本 Issue 的推广条件已全部满足。

当前执行锚点：

- 正式发布：`fd79c4be54fc50bd66d9a51bbc1e681f361f6a77`（仓库 5.5.1 / `writing-style` 0.5）。
- main 整合：`57c5a2c8124752587688475b3ebc09c198d35186`；正式发布提交已是 main 的祖先。
- 维护条目：`docs/plugin-todos/writing-style.md`，``Promote `writing-style` into the generic content-preserving language layer``，`tracking: #13`。
- 批准执行包：`12a8ccd61778cca9a56df826072618cb06a81632`。

下一步：

- #73：`docs/plugin-todos/statistical-modeling.md` 中 `Delegate reader-facing wording without giving away statistical semantics`。由该领域任务基于真实统计分析，完成结果、图注与结论的交接回放，确认统计含义没有漂移。
- #49：`docs/plugin-todos/scientific-visualization.md` 中 `Delegate captions/annotations without giving away visual semantics`。由该领域任务完成真实科研图的图注与标注交接回放，确认图形含义保持一致，且表达更加清楚。
- 完成这些接入后，逐项核对 #13 原有推广条件及持久证据，再判断能否关闭。当前不填写 Resolution commit，也不在本发布任务中实施下游插件修改。

正式发布不声称 Clear Writing 每轮必然加载，也不声称已证明严格匹配实验中的因果增益。历史 `W2=INCONCLUSIVE` 保留为诊断事实；它不是当前正式发布失败或待重跑项。

<details>
<summary>历史记录（截至 2026-10-19 发布收口前，原文保留，不代表当前状态或待执行指令）</summary>

问题：

普通 ChatGPT Web 即使已有 Project instructions、个性化语言偏好和写作规则，在读取英文仓库、论文、技能、插件、日志或 Planner/Critic 材料后，仍可能把普通英文、内部状态、机械换行、伪流程图和重复结构带进最终回答。PIE C11 已证明：仅靠 Project instructions 不能可靠保证每一轮跨轮最终阅读层。

目标：

让 Clear Writing（`writing-style`）成为普通 ChatGPT / Codex 面向用户解释层的中央能力，在不要求用户每轮显式 `@Clear Writing`、不依赖额外外部模型服务的前提下，尽可能稳定做到：

- 先说人能直接理解的结论、意义和必要动作；
- 普通中文解释减少非必要英文、内部流程词和裸状态；
- 不把简单问题写成报告、流程图或大量机械分节；
- 保留事实、条件、否定、不确定性、权限、公式和需要精确匹配的机器字符串；
- 正式文档、科研长文、UI 文案和 Presentation 继续由既有专业 writing / domain route 负责，不让普通回复能力接管它们。

当前正式执行：

- 生命周期继续为 `DOING`；Issue 保持 open；Area 继续为 `writing-style`。
- Clear Writing 最终 4-answer Web closure 已真实 PASS，当前只做 `0.5` 正式发布收口；不再追加 Web Gate，也不重跑 W2。
- frozen production candidate：`fd7a1578a5042a46a55c5b638f6d550655b1096b`。
- release-closure 设计任务：`clear-writing--release-closure`。
- 上一版 Plan v0.1 经独立 Critic `REVISE`，只剩 `CW-RC-03 / CW-RC-05 / CW-RC-07`。
- Planner 已冻结完整 Plan v0.2：
  `docs/design/clear-writing/CLEAR_WRITING_0_5_RELEASE_CLOSURE_PLAN_V0_2_2026-10-19.md@6e321ced9ee14c936c06397ead9862f70312bd40`。
- v0.2 已明确：
  - `codex-writing-style` profile 必须对齐 frozen candidate 的六个 writing skills；
  - `product-ui-copy` 本轮只同步 profile exposure，不修改其 Skill/runtime；
  - exact committed clean `5.5.1 / writing-style 0.5` candidate 在 release 前必须完成 fresh install + `5.5.0/0.4 -> 5.5.1/0.5` upgrade smoke，并回读实际 repository/plugin/profile identity；
  - 0.5 formal release 成功不自动等于 Issue #13 DONE；
  - 若 #13 canonical promotion gate 仍有 required downstream consumer pending，0.5 仍可成功发布，但 #13 保持 open，并按看板语义进入 `ADAPTING`；
  - 本轮不实施 Statistical Modeling、Scientific Visualization、Presentations、Research Authoring、PIE 或 Mica。
- 版本与 release-isolation 设计保持不变：
  - repository `5.5.0 -> 5.5.1`（PATCH）
  - writing-style `0.4 -> 0.5`
  - all others NO_BUMP
  - maturity NO CHANGE
  - formal release 继续从执行时 current `origin/release` 构建 isolated candidate；baseline drift 则 stop + Planner late-bind。
- 当前仍是设计返修阶段：没有写 Goal/Kickoff，没有启动 Codex，没有构建 candidate，没有推进 release，没有修改 PRIVATE plugin。
- 下一步：独立 Critic 只复核 `CW-RC-03 / CW-RC-05 / CW-RC-07` 及 v0.2 改动影响。
- Critic prompt：
  `docs/design/clear-writing/CLEAR_WRITING_0_5_RELEASE_CLOSURE_CRITIC_PROMPT_V0_2_2026-10-19.md@a6644381227ae026c8a6c14daf7caa72a062b9f4`。

GitHub Project field mutation surface 当前不可用，待同步 mutation 精确为：

```text
Issue #13
Status = DOING
Area = writing-style
Execution anchor = a6644381227ae026c8a6c14daf7caa72a062b9f4
Next action = independent Critic re-review of Clear Writing 0.5 release-closure Plan v0.2; prioritize CW-RC-03 / CW-RC-05 / CW-RC-07
```

2026-10-14 至 10-15 新增真实 ChatGPT Web 证据：

当前已冻结 5 个真实网页端开发样本：

1. 长回答把真正判断淹没在大量分节、列表和机器细节中 — 反例；
2. 伪澄清、反复改变建议、自我检讨代替回答 — 反例；
3. 具体选择 + 日常例子 + 明确未核查边界 — 正例；
4. 简单线性关系被大代码框、逐行箭头和内部名词清单伪结构化 — 反例；
5. 研究综合在核心结论已经完成后继续膨胀成小型架构方案文档，并混淆来源共识与助手建议 — 反例。

这些样本全部属于 known regression，不得用于 G7 fresh / unseen 证明。正例必须作为 should-not-change，防止把 Clear Writing 修成“强制短答”。

当前恢复包：

- regression bank：`results/clear-writing--cross-surface-language-layer/REAL_WEB_REGRESSION_BANK_V1.md`
- Planner recovery Plan：`docs/design/clear-writing/CROSS_SURFACE_RECOVERY_PLAN_V0_1_2026-10-15.md`
- Goal：`docs/goals/CLEAR_WRITING_CROSS_SURFACE_RECOVERY_GOAL_V0_1_2026-10-15.md`
- Kickoff draft：`docs/operations/prompts/CLEAR_WRITING_CROSS_SURFACE_RECOVERY_KICKOFF_V0_1_2026-10-15.md`
- Critic prompt：`docs/design/clear-writing/CROSS_SURFACE_RECOVERY_CRITIC_PROMPT_V0_1_2026-10-15.md`
- package head：`ac44e1cf07df08e9042bfc53e2b2ab79ec4871ad`

恢复策略：

1. 先用现有候选 replay 五个 known cases，保存 baseline；不先按样本改代码。
2. 再同步最新 main。
3. 只有真实失败才对 `response-clarity` 做 bounded generic repair；禁止禁词表、英文比例、固定长度、固定箭头/代码框规则和项目特判。
4. 同时关闭阻塞当前任务的仓库 CI 既有基线；不允许删测试、隐藏失败或假升级版本。
5. full CI 与 known regression 全部通过后，才继续真实 ChatGPT Web A/E、B/C 自动调用对照和后续 G7 fresh。
6. PIE 0.2 暂不实施；只有 Clear Writing Web 自动消费证明成立后，PIE 才做薄的 Project bridge，不复制写作规则。

平台边界：

OpenAI 当前公开说明中，Skill 的自动使用依赖模型根据 metadata/用户目标判断是否相关；Project instructions 只在对应 Project 中生效。当前没有可依赖的通用“每条回复发送前强制 finalizer”合同。因此最终必须用真实 Web matched comparison 证明 automatic selection，而不能因为 Project setting 写了“请用 Clear Writing”或显式 `@` 能工作就宣布完成。

下一步：

把已经过 Critic PASS 的 Kickoff 逐字交给 Codex，在现有 successor branch 执行：先为 KR-WEB-06..09 建 public-safe baseline，再只修两个冻结缺口，随后完整重跑 KR-WEB-01..09、四组 should-not-change、full repository / Marketplace / GitHub CI，并交独立 Reviewer 实际读取九组最终输出。当前仍不实施 PIE 0.2、Web A/E/B/C、G7 fresh 或 release；这些后续门槛不能被本 successor 的 repo/CI PASS 替代。

</details>

</details>

</details>


</details>
