# Clear Writing 跨 ChatGPT / Codex 通用表达层 — 独立 Critic 交接 v0.1

- 角色：独立 Critic；阶段：ARCHITECTURE_DESIGN_REVIEW
- 审查仓库：YuukiAS/AI_Skills_Collection
- 审查分支：`planner/clear-writing-cross-surface-v0.1`
- 设计事实基线：`main@00a90661a3cb3e287ed83a7a2e5dc9beffbf8b91`（审查时另 fetch 最新 main 比对变动）
- 跟踪 Issue：`#13`
- 唯一设计对象：现有 `writing-style` / Clear Writing 下一版
- 提案：`docs/design/clear-writing/CROSS_SURFACE_LANGUAGE_LAYER_PROPOSAL_V0_1_2026-10-12.md`
- 验收矩阵：`docs/design/clear-writing/CROSS_SURFACE_LANGUAGE_LAYER_GATE_MATRIX_V0_1_2026-10-12.md`
- Research Authoring：本轮完全冻结；PIE 0.2：后续可选，不作为本轮实现对象
- 结果：仅独立审查并给 `PASS` / `REVISE`；不修改生产技能、插件、版本、线上设置，不启动实现或付费调用

## 可直接交给 Critic 的提示词

你担任 AI Research Stack 的独立 Clear Writing 架构 Critic。本轮目标是判断下一版 Clear Writing 是否真的能作为 ChatGPT 与 Codex 共用的自然、语义保真的读者表达能力，并让普通对话、中文/英文科研文稿、技术报告、演示文稿、网页和应用界面文字在正常任务中按需使用，而不要求用户每轮 `@Clear Writing`。重点不是增加写作技能数量，而是名称清晰、职责不冲突、正常入口真实有效、专业语义不被改动、完整产物质量稳定。

先读取 YuukiAS/AI_Skills_Collection 最新 main 的 `AGENTS.md`、`docs/workflows/PLANNER_ROLE_CONTRACT.md`、`docs/workflows/CRITIC_ROLE_CONTRACT.md`、`docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md` 和 `docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md`；再 fetch `planner/clear-writing-cross-surface-v0.1`，读取该分支的提案与能力验收矩阵。必须直接核对该分支所用的五项当前 Clear Writing Skill、Codex `writing-style` 插件清单、现有 Frontend Design / Presentations 消费入口、`docs/plugin-todos/writing-style.md` 与 Issue #13。PR #100 已关闭且未合并，不是本轮审批对象；055 的已有科研长文主链只作现状/兼容性证据，不可与本轮新设计混为一项已批准实现。按需要独立核实最新 OpenAI 官方技能、插件分发与项目指令机制，不能默认 Planner 的平台结论正确。

逐项重点质疑：

1. `response-clarity` 是真实缺失的独立正常回答能力，还是现有 `chinese-prose` 与简短持久指令的重复？在普通 ChatGPT Web 没有每轮强制调用钩子时，静默可用的声明是否可验证、是否夸大？
2. 六项候选命名 `response-clarity`、`chinese-writing`、`scientific-english`、`chinese-source-rewrite`、`interface-writing`、`meaning-fidelity` 是否准确、足够区分且值得迁移；是否有更小但同样有效的命名调整？特别审现有中文长文重写的范围、保真技能是否仍需独立入口、与其它技能的触发冲突。
3. 保留复杂科研重写主链、统一保真原则并为普通回答增加轻量能力的分层是否真正比单一万能技能、纯项目规则、全面重构或者独立后处理更优？
4. ChatGPT 个人 Plugin Creator 包装与 Codex Marketplace 同源构建能否形成一致而不重复的生产身份；哪些技能需在 Web 包装可见；如何证明实际安装、普通无 `@` 调用和新会话行为，而不是自称加载？
5. 有 Project 与无 Project 两种持久偏好入口是否有可靠且不夸大的落地方法；项目指令覆盖个性化后，如何避免语言规则缺席；PIE 0.2 不应被错误当成当前已实现的强制终审。
6. Frontend Design、Presentations、普通软件/统计任务和技术报告的真实消费如何衔接，不能只靠“安装两个插件”或未经支持的确定技能链；命名改动是否会断开现有消费者，实际渲染/全文验收是否充分？
7. Gate 矩阵是否覆盖首次完整回答、用户未指定插件、候选对短指令的可观察增量、跨多轮英文输入、精确机器标识、语言覆盖、长文全文、UI 和幻灯片真实渲染、已安装身份、最终冻结未见泛化；是否有重复、虚假代理指标或过重成本？
8. Research Authoring 本轮不得修改、迁移或用其废弃包装作为完成证据。PIE 0.2、个人设置写入、全局 Codex 配置、外部凭据、收费调用与插件发布均不属于本轮授权。历史 C5–C11 是开发回归而非未见样本；私有聊天不得写入公共仓库。

请用明确证据检查方向错误、过度复杂、过度简化和真实平台失败风险。每个阻断问题须附对应要求、直接证据、因果风险和最小修复条件；普通命名审美或更多保险不能单独阻断。明确写出本次审查分支的 **精确提交**、提案版本、审查范围、结论 `PASS` 或 `REVISE`，并区分通过架构与批准执行/发布。不要以同一线程冒充 Planner 和 Critic。Critic 不修改本提案或运行 Executor；若需要修订，交还 Planner 给出完整 v0.2，而不是自行批准自己的新设计。
