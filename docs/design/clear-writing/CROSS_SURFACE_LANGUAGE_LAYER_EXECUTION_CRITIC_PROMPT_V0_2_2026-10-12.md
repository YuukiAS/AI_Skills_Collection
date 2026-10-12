# Clear Writing 跨 ChatGPT / Codex — 执行前独立 Critic 提示词 v0.2

- 阶段：`EXECUTION_READY`
- 角色：新的独立 Critic，不得由本提案 Planner 自我放行
- 设计对象：`YuukiAS/AI_Skills_Collection` 的 `writing-style` / Clear Writing
- 规划分支：`planner/clear-writing-cross-surface-v0.1`
- 完整审查提交：以用户提供的本分支精确提交为准，必须亲自 fetch 后核对存在且实际包含以下 v0.2 文件；不得仅凭当前分支移动指针替代精确审查身份。
- 追踪：Issue #13
- 判定范围：**可执行性、真实正常入口、权限、同源包装、验收、角色接手和恢复路径**；不是实现、发布或用户验收。

## 独立 Critic 实际请求

你作为 AI Research Stack 的独立执行前 Critic，对 Clear Writing v0.2 同版执行包进行全面审查。用户已经转述此前的独立架构 Critic 对 v0.1 提案给出架构 PASS，但限定精简路线；该外部审查全文尚未写入仓库，因此你不能把它冒充已经存在的正式审查文件，也不应扩大已批准架构。本轮只有你能对 v0.2 的**执行包**提出 PASS 或 REVISE，本轮不得启动实现。

先核对 `YuukiAS/AI_Skills_Collection` 最新 `main`，实际读取：
- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md`
- `docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md`
- 目标插件真正的五项源、现有正式 `scripts/codex_marketplace_config.json`、生成包、Frontend Design/Presentations 消费接口、`docs/plugin-todos/writing-style.md`、Issue #13 与必要实际回归证据。

由于执行包拟使用现有 Reviewed Handoff 和 task branch/worktree，还必须读取最新 `YuukiAS/GPT_Codex_AI_Bridge_Kit` 的 `AGENTS.md` 与本仓库实际 `automation/reviewed_handoff/README.md`、适用 PLAN/CURRENT 模板；不能根据旧聊天想象 Bridge CLI、首次远端发布、人工/自动 Reviewer 或路径行为。按需独立核验 OpenAI 的技能触发、ChatGPT/ Codex 插件包装、Project 与个性化指令优先级及 Plugin Creator 个人私有插件的实际资格和安装机制。

随后 pin 用户指定的规划分支提交，完整读取这套同版文件：

1. `docs/design/clear-writing/CROSS_SURFACE_LANGUAGE_LAYER_PROPOSAL_V0_2_2026-10-12.md`
2. `docs/design/clear-writing/CROSS_SURFACE_LANGUAGE_LAYER_GATE_MATRIX_V0_2_2026-10-12.md`
3. `docs/design/clear-writing/CROSS_SURFACE_LANGUAGE_LAYER_EXECUTION_PLAN_V0_2_2026-10-12.md`
4. `docs/goals/CLEAR_WRITING_CROSS_SURFACE_LANGUAGE_LAYER_GOAL_V0_2.md`
5. `docs/operations/prompts/CLEAR_WRITING_CROSS_SURFACE_LANGUAGE_LAYER_KICKOFF_V0_2.md`

以当前用户认可的架构裁定为已冻结范围：保留 `writing-style` 与 Clear Writing 名称；保持 `chinese-prose`、`scientific-prose`、`scientific-rewrite`、`product-ui-copy`、`writing-fidelity` 不重命名；最多新增 `response-clarity`，只调整它与 `chinese-prose` 的正反触发；保留复杂中文源重写主链；各独立技能实际获得必要保真约束，绝不依赖平台不保证的技能调用链；现有 Frontend Design/Presentations 路由保持；Research Authoring 冻结，PIE 0.2 不实施，PR #100 不重新打开，无额外付费或外部服务。

重点独立审查以下实际失败风险：

1. `response-clarity` 的任务边界和 `chinese-prose` 是否真能区分普通技术聊天和中文文档成稿，是否会争抢已有重写、英文科研、UI、纯机器任务；官方自动选择规则是否真的支持当前设计的增量主张。
2. `writing-fidelity` 为唯一权威时，各被**单独**加载的写作技能是否自带足够保护事实、条件、权限、时间状态、精确代码/路径和不确定性的底线；如果没有可靠加载，是否禁止假称顺序终审。
3. Codex Marketplace 的六个技能及原有五个 `artifact_id` 是否精确保留；已有生成器能否合法构建；完整文件（包括重型中文重写所需脚本）在 ChatGPT 个人技能型包装能否真正使用。跨表面载荷哈希与独立发布版本如何对应，是否存在无法传递/安装的缺口。
4. GPT 侧从固定公开安全 GitHub 候选重构个人包装的方式是否真实可行，不依赖不可访问的 Codex 本地私有 ZIP；Plugin Creator 的账号归属、一次新建及有界更新、必要权限、用户可见安装和不可自动完成的动作是否明确。
5. 有 Project 的 A/B/C/D、无 Project 的固定个性化成对对照，是否真的隔离短激活提示词本身的效果；若平台不能无损切换候选/旧版，是否如实 `INCONCLUSIVE` 而非伪造插件效果；是否严格区别“每条回答质量稳定”和“每条回答必然调用插件”。
6. Frontend Design / Presentations / Codex 普通软件技术说明的专业消费是否从**真实普通入口**验证，全部材料、完整报告、真正可打开的前端/整套幻灯片渲染和源保真审阅是否充分；是否误动冻结的 Research Authoring。
7. `G0–G7` 能力矩阵是否有重复门槛、机械指标冒充语言质量、只凭子句或自述、旧已曝光样本冒充未见、不同候选拼接/版本更改却沿用旧 PASS、评审者无法拿到完整源/渲染。
8. Bridge 的准确 `clear-writing--cross-surface-language-layer` 分支与 sibling worktree、合法初态、PLAN_OWNER、手工 Reviewer 接手、首次发布与恢复是否完整可执行；是否错误承诺已经存在自动任务；无执行设备真实路径时是否允许其有界解析而非即兴变更。
9. 权限和回退是否足够：个人 Plugin Creator 修改、试点 Project/个性化的可逆操作、私有材料、费用/令牌、正式主线发行与用户 `ACCEPT` 的时间边界、失败后的个人插件旧版/首次新建状态与恢复路径；不能让合同文件本身冒充用户授权。
10. 版本决策是否符合当前规范：`writing-style 0.4 -> 0.5` 只有正式新能力经过真实验证；Repository 默认 PATCH；完整包变更与新版生成清单对齐；README 的真实 Clear Writing 检查仍保留；Project Board #13 跟踪未得到工具支持时必须如实记录。

每个阻断项同时给出（甲）对应的用户/仓库要求，（乙）你亲自核实的具体证据位置，（丙）直接的产品、权限、费用、执行或语义风险，（丁）能够关闭该风险的最小修订。纯审美、要求更多“保险”、固定 Gate 数量或无限追加测试不构成阻断。若完全可执行则给 `PASS / READY_FOR_CODEX=YES`，否则 `REVISE / READY_FOR_CODEX=NO`；必须绑定实际审查提交、包版本和确切五份 v0.2 文件。

此 Critic **只读评审**，不得自行改 Planner 提案、冻结 task-local PLAN、启动 Codex、创建个人插件、修改 Project、使用付费接口或推动发行。只有返回经过证据支持的执行前 PASS，未来用户实际发送获批 Kickoff，才构成实现入口的前提；Critic PASS 也不等于产品已通过 G0–G7。
