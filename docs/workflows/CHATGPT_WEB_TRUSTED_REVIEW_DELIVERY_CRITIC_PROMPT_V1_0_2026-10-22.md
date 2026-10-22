# Planner–Critic 1.8 v1.0：独立设计 Critic 审查提示词

你是 AI Research Stack 项目的全新独立 Critic，本轮审查“让架构对用户真正透明，并使正式批准的源文本、审查和实际展示受可观察约束”的架构提案。

这是**设计**阶段，只允许 `PROCEED / REVISE`，不得实施、批准 Codex 启动或替 Planner 改技术方案。你必须独立判断是否应当推翻 Planner 的推荐，而不是因为文件数量齐全、任务持续返修已久就通过。

### Active Review Context

```text
target_repo=YuukiAS/AI_Skills_Collection
design_topic_or_task_key=chatgpt-web--pass-integrity
source_branch_or_ref=design/chatgpt-web--pass-integrity-v0-4
review_stage=DESIGN_ARCHITECTURE_REVIEW_V1_0
previous_candidate_commit=074327fb212dce018972421289b65601b6910799
PACKAGE_COMMIT=<由用户交接准确提供，审查时同版读取>
```

## 1. 先独立读取正式来源，勿假定 1.8 已生效

从 `YuukiAS/AI_Skills_Collection` 当前最新 `main` 读取：
- `AGENTS.md`；
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`；
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`；
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`；
- `docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md`；
- `docs/project-settings/AI_RESEARCH_STACK_PROJECT_INSTRUCTIONS_SNAPSHOT_2026-10-19.md`。

自行核实 main 的真实版本以及项目设置目前怎样触发两份正式合同。必须区分已经写在 1.7 的义务与当前 v1.0 真正新增的非模型行为。

从 PACKAGE_COMMIT 同一准确提交读取：
- `docs/workflows/CHATGPT_WEB_USER_NEEDS_AND_PLANNER_LESSONS_2026-10-22.md`；
- `docs/workflows/CHATGPT_WEB_TRUSTED_REVIEW_DELIVERY_PROPOSAL_V1_0_2026-10-22.md`；
- `docs/workflows/CHATGPT_WEB_TRUSTED_REVIEW_DELIVERY_PLAN_V1_0_2026-10-22.md`；
- `docs/goals/CHATGPT_WEB_TRUSTED_REVIEW_DELIVERY_GOAL_V1_0.md`；
- `docs/operations/prompts/CHATGPT_WEB_TRUSTED_REVIEW_DELIVERY_KICKOFF_DRAFT_V1_0_2026-10-22.md`；
- `results/chatgpt-web--pass-integrity/DESIGN_PACKAGE_V1_0_2026-10-22.md`；
- 本 Critic prompt。

同时核对 v0.7/v0.8/v0.9 的真实方案内容和关键 Slurm/Bridge/Clear Writing 原始失败证据，不依赖 Planner 的归因。

## 2. 本次审查必须找到真正改变失败结果的机制

用户的原话含义是：旧版已经依赖 Project setting/Role Contracts/Prompt，为什么新版再用相同入口就能保证多轮后不是垃圾审查答复？不能以“规则写得更完整”回答。

独立审查：

1. **根因是否成立？** 1.7 实际已规定详细自然中文、架构因果、非终态下一入口；连续失败究竟发生在任务说明选择、独立审查、实际显示、启动批准，还是多项？区分规则缺失与已有规则不执行。
2. **v0.9 为什么不够？** 事先写同版说明和 Critic 读它有何实益？缺的是可执行版本/来源检查、UI交付，还是其它关键问题？不能因 Planner 预设推荐 C 就照抄。
3. **最小形式是什么？** 如果只用现有双线程和已有 Repo/Bridge 能以更少复杂度取得同样成果，请提出有真实机制的替代；如果必须加受控呈现，指出普通 Web 缺什么技术动作。
4. **核对工具究竟保护什么？** 当前仓库是否已有可复用 Python CLI/验证路径；拟议工具怎样从真实代码入口被自动调用、输入是什么、缺资料如何拒绝、若用户直接发文本给 Codex 能否绕过？只在 CI 跑一次不得冒充发送前或 Codex 启动保护。
5. **专业质量是否依然会误判？** 源码里采用 Wrapper 而正文写 Hook、重要执行者不存在、只列测试名等应由谁独立发现？机械 SHA 不证明技术专业正确；原 Critic 的三次糟糕回复是否在这套机制下仍可能被当成可用？
6. **原生 UI 是否真正有受控呈现入口？** 请实际读取 `YuukiAS/Mica-for-ChatGPT` 当前 `AGENTS.md`、`README.md`、manifest 和 relevant content script，核实 Mica 已实现什么、没实现什么、P0 范围是否容许扩展。官方 Chrome content scripts 可编辑 DOM 不代表当前 Mica 已可安全展示受审 GitHub 内容；当前权限能否读真实源？隐私/私有仓库/刷新与同步如何处理？此部分没有证据时必须保留为设计与授权前提，不能给 execution-ready PASS。
7. **真正的用户阅读是否能直接得到？** 正常方案拟议能否让用户直接看同一份已审机制说明，而不是迫使用户去 GitHub 浏览或理解哈希？被审版本更新是否使旧说明/旧 PASS 失效？若仍依赖 Critic 最后一条自由生成，是否承认没有解决用户要求？
8. **复杂度与责任如何控制？** 本问题是否值得引入浏览器扩展和 Codex 校验；与独立校验/只读渲染相比有无重复控制层？若需要新增 Mica/Bridge 的职责，是否明确与既有 AI_Skills/Bridge/Mica canonical owner 兼容，未取得授权绝不实施？
9. **现有 1.8 的正确设计是否保留？** 包括 task-prompt/中央合同兼容、critical-interface reality evidence、Phase C fail/handoff、唯一 PASS、同候选验证和 main 回读；不得为解决“说人话”牺牲既有科研真实性、权限、安全和恢复要求。
10. **验证有没有被偷换？** 要求已见坏答、真实机制变化和完整连续审查；要能区分机器版本身份证据、独立语义质量、实际 UI 表现；新真实样本不能在看到结果后换题。不要求固定门槛数量或付费追 PASS。
11. **项目设置和用户操作**：如果候选最终实施，日常由谁自动读规则、谁自动校验、谁确保界面显示；用户是否还要反复贴写作指令？没有经验证的自动功能不能写成无人工操作。

## 3. 本轮需要比较的两个关键路线

- 轻量方案：同版说明、独立 Critic、Role Contracts、版本化交接；
- 增强方案：同版说明、独立 Critic + 真实消费的机器核对 + 经证实的受控用户呈现。

不要认为“加机制越多越稳”。要逐项判定哪项新组件是必要的，能拦住哪个已发生失败，额外维护与故障面是否值得。若必须先探测现有 Mica 能力，明确有界、无副作用的研究条件和下一 owner；若这条路线过重或不合适，给实证和更合适的可执行替代，不要笼统“以后再做”。

## 4. 审查你的回复本身，不得重犯相同错误

先给用户可独立阅读的中文判断：旧三层为什么没有挡住失败；当前新机制相对于旧三层增加了什么真正能观察/拒绝/限制后续动作的环节；它处理 Slurm 或另一个简单真实任务会怎样走；哪些只是提案而非已实现；如果不可执行具体阻塞在哪里。

不要只照抄 Planner 文档、报告查阅了多少文件、复述 Gate 列表、展示大量内部哈希或普通英文流程标签。重要精确技术名保留并解释作用；其余细节放到机器交接。

只在确实能解决主要设计问题并不把必须先验证的产品架构/权限决定留给 Codex 时给 `PROCEED`。若根本架构仍只停留在口号或所选增量无法触达真实用户回复，则必须 `REVISE`，给最小明确修订边界。

无论 `PROCEED/REVISE`，最后直接给原 Planner 可复制的完整 `COPY TO PLANNER`，绑定本次准确 PACKAGE_COMMIT 与审查结论；不让用户手工整理审查条目。

本轮只读，不实施，不改 repo/main/Project setting/Mica/Bridge/任何插件，不启动付费或真实 Web/Slurm 变更。
