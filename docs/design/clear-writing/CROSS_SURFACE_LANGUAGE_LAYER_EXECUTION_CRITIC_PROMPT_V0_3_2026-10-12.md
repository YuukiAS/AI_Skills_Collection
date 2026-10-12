# Clear Writing 跨 ChatGPT / Codex — 执行前独立 Critic 提示词 v0.3

- 阶段：`EXECUTION_READY`
- 角色：新的独立 Critic，不得由本提案 Planner 自我放行
- 设计对象：`YuukiAS/AI_Skills_Collection` 的 `writing-style` / Clear Writing
- 规划分支：`planner/clear-writing-cross-surface-v0.1`
- 完整审查提交：以用户提供的本分支精确提交为准，必须亲自 fetch 后核对存在且实际包含以下 v0.3 文件；不得仅凭当前分支移动指针替代精确审查身份。
- 追踪：Issue #13
- 任务标识：`clear-writing--cross-surface-language-layer`
- 判定范围：**可执行性、真实正常入口、权限、同源包装、验收、角色接手和恢复路径**；不是实现、发布或用户验收。

## 本次执行前复核的唯一实质范围

上一轮独立 Critic 对 `fd7213c56a9cfca29de096e42cf64053453e16f5` 的 **v0.2** 执行包给出 `REVISE / READY_FOR_CODEX=NO`，原审查意见由用户转交，**并无真实已提交仓库的本轮 Critic review 文件**。Planner 两项均决定 `ACCEPT`，没有 REBUT；请只复核阻断的关闭情况，不冒充已读独立 Critic 原文。

- **CW-ER-01**：Bridge Kit `task bootstrap` 仅本地创建任务；v0.3 是否将首次交接冻结为：验证批准包不可变提交和**六份**文件路径、真实执行前 Critic review 提交 → bootstrap → 进入派生 reviewed 工作树 → 在首次 REQUEST 记录上述权威定位 → 只提交 REQUEST/CURRENT 两个新文件，形成 `CURRENT.base_commit` 的单一直接子提交 → 调用正式 `task publish-first` → 远端核对 SHA、REQUEST、CURRENT、`next_action=RUN_GPT_PLANNER` 和已发布人工 Planner 接手？核对当前 Bridge 源与真实曾成功消费者，不凭计划字符串自证。
- **CW-ER-02**：G1 不另设 Gate，保留 A/B/C/D 并新增 E。A/E 均无短桥、相同 Project 基础语言合同，仅候选插件有无不同；B/C 均有同一短桥，同样仅候选有无不同；D 仅 `@` 显式诊断。若对照环境无法合法、可靠匹配是否必须 `INCONCLUSIVE`，不得归功插件或以模型自述替代行为？

历史其他已通过的技能标识、重写架构、分发、G0–G7、领域消费者、权限、版本、研究插件冻结等要求仅做**不回归**核对。除非发现 v0.3 改动引入的真实新问题或此前遗漏的关键直接证据，不新增阻断，不移动终点。

五份执行正文已在 `planner/clear-writing-cross-surface-v0.1@2e6f856af3720a5ff68f9da70e0309a6c7793025` 存在。本第六份审查提示词在该提交之后添加；**六份文件共同的最终审查提交由 Planner 在交接消息里给出的实际完整 40 位 SHA 指定，Critic 必须以它读取六份文件，不能用该五文件中间提交假称“六份已同版”。**

## 独立 Critic 实际请求

你作为 AI Research Stack 的独立执行前 Critic，**仅复核 Clear Writing v0.3 对 CW-ER-01／CW-ER-02 的关闭及改动导致的直接回归**。用户转述 v0.1 架构 PASS 和原 v0.2 执行前 `REVISE / READY_FOR_CODEX=NO`，原独立审查全文未写入仓库，不能冒充其已有仓库记录。本次不重开获批准架构，也不授权任何产品实现。

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

1. `docs/design/clear-writing/CROSS_SURFACE_LANGUAGE_LAYER_PROPOSAL_V0_3_2026-10-12.md`
2. `docs/design/clear-writing/CROSS_SURFACE_LANGUAGE_LAYER_GATE_MATRIX_V0_3_2026-10-12.md`
3. `docs/design/clear-writing/CROSS_SURFACE_LANGUAGE_LAYER_EXECUTION_PLAN_V0_3_2026-10-12.md`
4. `docs/goals/CLEAR_WRITING_CROSS_SURFACE_LANGUAGE_LAYER_GOAL_V0_3.md`
5. `docs/operations/prompts/CLEAR_WRITING_CROSS_SURFACE_LANGUAGE_LAYER_KICKOFF_V0_3.md`
6. `docs/design/clear-writing/CROSS_SURFACE_LANGUAGE_LAYER_EXECUTION_CRITIC_PROMPT_V0_3_2026-10-12.md`（本提示词）

以当前用户认可的架构裁定为已冻结范围：保留 `writing-style` 与 Clear Writing 名称；保持 `chinese-prose`、`scientific-prose`、`scientific-rewrite`、`product-ui-copy`、`writing-fidelity` 不重命名；最多新增 `response-clarity`，只调整它与 `chinese-prose` 的正反触发；保留复杂中文源重写主链；各独立技能实际获得必要保真约束，绝不依赖平台不保证的技能调用链；现有 Frontend Design/Presentations 路由保持；Research Authoring 冻结，PIE 0.2 不实施，PR #100 不重新打开，无额外付费或外部服务。

下面既有审查问题保留为未修改范围的**兼容核对**；此次唯一需要逐项给出关闭判定的是 CW-ER-01 和 CW-ER-02，不能把此前通过事项重新当作开放式审批：

1. `response-clarity` 的任务边界和 `chinese-prose` 是否真能区分普通技术聊天和中文文档成稿，是否会争抢已有重写、英文科研、UI、纯机器任务；官方自动选择规则是否真的支持当前设计的增量主张。
2. `writing-fidelity` 为唯一权威时，各被**单独**加载的写作技能是否自带足够保护事实、条件、权限、时间状态、精确代码/路径和不确定性的底线；如果没有可靠加载，是否禁止假称顺序终审。
3. Codex Marketplace 的六个技能及原有五个 `artifact_id` 是否精确保留；已有生成器能否合法构建；完整文件（包括重型中文重写所需脚本）在 ChatGPT 个人技能型包装能否真正使用。跨表面载荷哈希与独立发布版本如何对应，是否存在无法传递/安装的缺口。
4. GPT 侧从固定公开安全 GitHub 候选重构个人包装的方式是否真实可行，不依赖不可访问的 Codex 本地私有 ZIP；Plugin Creator 的账号归属、一次新建及有界更新、必要权限、用户可见安装和不可自动完成的动作是否明确。
5. **CW-ER-02**：有 Project 的 A/E 与 B/C 两组严格配对条件是否使“候选存在”成为组内唯一差异，D 是否只诊断；不能合法切换安装/短桥或控制对照时是否 `INCONCLUSIVE`，不误把持久指令当插件增量。
6. Frontend Design / Presentations / Codex 普通软件技术说明的专业消费是否从**真实普通入口**验证，全部材料、完整报告、真正可打开的前端/整套幻灯片渲染和源保真审阅是否充分；是否误动冻结的 Research Authoring。
7. `G0–G7` 能力矩阵是否有重复门槛、机械指标冒充语言质量、只凭子句或自述、旧已曝光样本冒充未见、不同候选拼接/版本更改却沿用旧 PASS、评审者无法拿到完整源/渲染。
8. **CW-ER-01**：从真实 Bridge 首次 `task bootstrap` 的本地结果到 reviewed 工作树里的两文件**唯一直接子提交**、`publish-first`、远端 SHA/REQUEST/CURRENT 与 `next_action=RUN_GPT_PLANNER` 核验、人工 Planner 交接是否每步可行且正确；首次 REQUEST 是否记录获批准 v0.3 六份合同的不可变提交/文件路径与真实执行前 Critic review 的精确路径/提交，使从 main 派生的分支可以跨 ref 读取权威文档。
9. 权限和回退是否足够：个人 Plugin Creator 修改、试点 Project/个性化的可逆操作、私有材料、费用/令牌、正式主线发行与用户 `ACCEPT` 的时间边界、失败后的个人插件旧版/首次新建状态与恢复路径；不能让合同文件本身冒充用户授权。
10. 版本决策是否符合当前规范：`writing-style 0.4 -> 0.5` 只有正式新能力经过真实验证；Repository 默认 PATCH；完整包变更与新版生成清单对齐；README 的真实 Clear Writing 检查仍保留；Project Board #13 跟踪未得到工具支持时必须如实记录。

先对 **CW-ER-01、CW-ER-02** 各自给 `CLOSED` 或 `OPEN`，附原用户要求、直接证据、因果风险及最小关闭条件。新增阻断只限本版变动造成的真实回归或新发现的关键证据，不能因格式、审美、更多保险或重复测试新增。两项均关闭且无新真实阻断，给 `PASS / READY_FOR_CODEX=YES`；否则 `REVISE / READY_FOR_CODEX=NO`。必须绑定交接消息所给的**六文件同一最终 SHA**、v0.3 版本和实际审查对象；PASS 也不授权自行启动 Executor。

此 Critic **只读评审**，不得自行改 Planner 提案、冻结 task-local PLAN、启动 Codex、创建个人插件、修改 Project、使用付费接口或推动发行。只有返回经过证据支持的执行前 PASS，未来用户实际发送获批 Kickoff，才构成实现入口的前提；Critic PASS 也不等于产品已通过 G0–G7。
