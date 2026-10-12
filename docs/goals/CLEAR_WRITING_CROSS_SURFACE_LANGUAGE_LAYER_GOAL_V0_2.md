# Clear Writing 跨 ChatGPT / Codex 通用表达层 — Canonical Goal v0.2

- 状态：`DRAFT / EXECUTION_READY_CRITIC_PENDING`；不代表已授权启动
- Repository：`YuukiAS/AI_Skills_Collection`
- Proposal：`docs/design/clear-writing/CROSS_SURFACE_LANGUAGE_LAYER_PROPOSAL_V0_2_2026-10-12.md`
- Capability Gates：`docs/design/clear-writing/CROSS_SURFACE_LANGUAGE_LAYER_GATE_MATRIX_V0_2_2026-10-12.md` G0–G7
- Execution Plan：`docs/design/clear-writing/CROSS_SURFACE_LANGUAGE_LAYER_EXECUTION_PLAN_V0_2_2026-10-12.md`
- Kickoff Draft：`docs/operations/prompts/CLEAR_WRITING_CROSS_SURFACE_LANGUAGE_LAYER_KICKOFF_V0_2.md`
- Task key：`clear-writing--cross-surface-language-layer`
- Execution branch：`reviewed/clear-writing--cross-surface-language-layer`（当前尚未创建）
- Worktree：由 Bridge 当前正式入口基于实际 canonical 仓库路径与该 task key 派生唯一 sibling worktree；执行时冻结为绝对路径，不允许自行替换
- Architecture anchor：规划分支 `819f861de7dc626f473390df8a9c42b70d24dd92` 的 v0.1；用户转述独立 Critic 架构阶段 PASS，明确精简范围。**没有可假称为仓库已有的 Critic 评审文件。**
- Implementation authorization：`NO`，直到独立执行前 Critic 对同一 v0.2 package 返回 `PASS / READY_FOR_CODEX=YES`，且用户实际发送获批 Kickoff。

本 Goal 是未来获批任务的**唯一总体完成合同**。任何单项测试、局部 Review、Codex 执行回执、工具安装或“语言像样了”的主观印象，都不能自行替代以下全体条件。它不创建任务状态机，不改目前已经完成的 PIE 0.1，也不将 PR #100 重新开案。

## 1. 最终新能力与最小真实作用

用户可以在有 Project 和无 Project 的普通 ChatGPT 中直接问科研、统计、工程、服务器、应用、管理与生活问题，不须每轮 `@Clear Writing`，在第一条完整回复获得自然目标语言、连续有意义的段落、合理的信息顺序与必要机器细节，同时保留真实结论与技术边界。插件相对基础 Project/个性化阅读规则必须显示稳定的、可观察的增益，否则按更简方案收口而非强行宣称插件自动最终审校。

Codex 面对文档、中文/英文科研表述、已有中文科研技术重写、真实网页和应用界面、完整演示文稿、普通软件/统计任务结果报告时，由原领域负责人处理专业语义、页面/段落结构和可编辑/渲染验收，在需要面向人的文字时适当消费 Clear Writing。旧五项技能不能回归，也不要求每个任务都加载六项。

现有用户私人个人插件/Project 配置的修改范围必须严格来自未来用户 Kickoff 授权；正常工作路径无需新模型服务、额外收费 API、密钥、MCP、浏览器扩展或后台守护进程。

## 2. 具体生产更改

**保持正式身份**：`writing-style` 插件、Clear Writing 产品名，现有 `chinese-prose`、`scientific-prose`、`scientific-rewrite`、`product-ui-copy`、`writing-fidelity` 五个技能名与正式路由。**唯一新技能**：`response-clarity`，只用于普通面向人类的解释和任务结果说明。轻量技能与 `chinese-prose` 的描述正反区分，且单次独立加载就有本轮适用的受保护语义规范；不得依赖另外一个 Skill 之后必然运行。

当前 `scientific-rewrite` 已有主链保持，除明确经批准的真实回归修复不重写。现有 Frontend Design 与 Presentations 交接规则保留，不迁移其源码，不把纯后端数据任务误分配给界面写作。

生成同源双端：从 `skills/writing/core/` 的正式源经已有 `scripts/codex_marketplace_config.json` 和 `scripts/build_codex_marketplace.py` 构建 Codex `writing-style` 六技能载荷；用同一冻结源可复现地打包一个 ChatGPT 用户私有、无 MCP 的 Clear Writing 插件。两者必须可核对为同一候选技能内容，不靠复制手工二次维护。ChatGPT 端若目标账户无法经合法 Creator 创建/安装/新会话观察，则不能用 Codex PASS 代替。

## 3. 必须满足的用户能力 G0–G7

1. G0：候选六技能源、生成包、Codex 正式安装以及 ChatGPT 个人插件 ZIP、安装可见身份匹配；无错版和重复顶级产品。
2. G1：ChatGPT 有 Project 的 A/B/C/D 成对对照及无 Project 的固定个性化对照，首答无需 `@`，插件相对仅短指令确有稳定增量；Codex 普通任务无显式名称也能正确选择。达不到增量必须回 Planner 简化，不能强行宣传。
3. G2：科研/工程/统计/服务器等领域完整首次回复自然、读者优先、去掉不必要普通英文、机械换行、来源标签与裸日志，人工定性审查完整产物。
4. G3：来源命题级保真、机器精确身份、公式/引用、否定条件、权限安全、时间与完成状态全部保持；纯机器输入/输出与逐字请求正确绕过。
5. G4：原五项技能的中文轻修、英文科研文字、中文重型源重写、正式报告与独立保真核查均不退化；合法代码/公式/复现信息不被错删；必要渲染真实可读。
6. G5：Frontend Design、Presentations 和普通 Codex 技术报告从真实候选正常路径消费合适写作技能；必须检查实际界面、完整演示文稿和必要来源；不以单页或静态配置代替。
7. G6：不同语言 Project、香港繁体、当前消息语言覆盖、多轮读取大量英文后的回复、简单问答、代码与纯机器输出均不受错误路由或模式污染。
8. G7：最终候选、评审标准、任务族、次数与分组预先冻结；独立 Reviewer 实际看全文与渲染；不可拼接不同提交、不同个人插件发行或挑选成功一次冒充稳定。

明确区分 `DIRECT_TOOL_ONLY`、`BRIDGE_ONLY_SUFFICIENT`、`INSTALLED_SKILL_WITH_BRIDGE_REQUIRED`、`INSTALLED_SKILL_WITHOUT_BRIDGE_RELIABLE`、`NORMAL_ENTRY_UNSUPPORTED`；只有后两种能够按实际范围支持“普通无需点名的插件表达层”声明。已曝光 C5–C11、050–055 不再作为未见样本。

## 4. 执行顺序与职责门槛

未来只有执行前 Critic 对确切 v0.2 全包 PASS、用户发送经批准的 Kickoff 后，才允许：预检 → Bridge 一次 bootstrap → 独立 Planner 冻结 task-local V2 PLAN → Executor 实现与开发期已知回归 → 代表性完整答复/文稿/界面/整套幻灯片的独立定性查看 → 冻结候选与版本身份 → 最终候选前置独立审查 → 个人 Web/Codex 正式安装与 A–D 实测 → 一次性冻结未见批次 → 独立 Reviewer/用户验收 → 必要合规集成/发行。

Planner/Reviewer 默认通过人工交接，**没有经过验证的自动任务时不得声称一次 Kickoff 自动完成**。执行阶段任务分支、工作树、首次远端发布和恢复必须通过当前 Bridge 支持的有界入口；首次事务状态 `PLAN_REQUESTED` 本身不是实现失败。个人 Plugin Creator 的实际调用由拥有该连接的 GPT 线程执行，Codex 只能准备准确同源归档配方和可复核产物，不假定共享私有路径。

每一阶段必须说明通过后新增的是何种真实用户能力；若 G0 真正不可行，在大量生产实现前停止。若 G1 插件无增益，返回 Planner 考虑只用持久语言规则与旧专业能力。定性读者质量在不可调优最终批次之前先实读，不能最后一步第一次发现机器腔。

## 5. 权限、隐私与不可越界内容

Kickoff 尚未发送：**不能**启动 Executor、创建 reviewed branch、调用户个人插件、修改任何 Project 或个性化指令、使用付费接口或开始正式插件生产修改。

未来经批准 Kickoff 可授权：准确仓库/任务/分支/worktree 内的可逆生产源码和测试修改、零额外付费候选安装/回放/渲染；个人账户下最多一个 Clear Writing 私有技能型插件创建及同一身份有界候选更新（且在实际使用前遵守用户/平台授权）；必要的试点 Project 短激活桥仅在被用户明确指名且可回滚时操作，绝不泛化为批量改所有 Project。最终正式发布、主线合并、个人长期设置整体修改仍需要相应的用户最终 `ACCEPT`。

禁止：Research Authoring 的源/包装/安装/测试或消费者迁移；PIE 0.2；对旧五技能的全面更名；其他插件无批准生产改动；外部大模型、额外模型费用/API key、托管/MCP/钩子/后台自动运行；未批准敏感数据传输；force Git 操作；以不真实的自动触发声明掩盖平台能力缺口。

公共 `results/` 只包含去敏公开安全结果及可审身份；私人聊天、账户插件身份、真实 Project 指令、敏感材料与令牌不得提交。真实不可恢复/需要更大权限时停并报告最小授权请求，不偷换路线。

## 6. 版本、发行身份与最终关闭

`Repository bump decision = PATCH`，仅正式可安装发行时按准确当前 `origin/release` 起点计算三段号，开发中不动 `VERSION`；若真的新增 repository-wide 全新能力而不只是单插件兼容改进，必须返 Planner/Critic，不能临时升中间版本。
`Affected plugin = writing-style 0.4 -> 0.5`（仅形成可观察新能力、原功能回归、最终候选完整审查且准备交付时一次升级）。
`Other plugins = NO_BUMP`。
`Maturity = NO_CHANGE`。
`README checked: 当前仅设计文件，no update required；正式发版前要复核并按原仓库强制 Clear Writing 实际调用规则审查任何受改 README。`

完成所需的最后证据：
- 同一源提交、Codex generated payload、个人插件归档和正式个人发行 ID 均可追溯，版本一一对应；
- G0–G7 每项所需完整答复/内容/真实渲染/来源保真均来自同一候选；
- 真实自动普通首答和相比提示词的增量成立，不靠 `@`、假调用、选择赢家或最后改准则；
- 原五技能/前端/演示文稿等合法消费者不回归；
- 独立 Reviewer 和必要 Critic 均拿到真正完整材料并认可，用户最后 `ACCEPT`；
- 仓库、插件、个人安装与正式发布版本一致，非强制整合/恢复可验证；
- Issue #13 当前进度和 `tracking: #13` 最终真实同步，绝不只凭一次中间 PASS 关闭。

当前只需交给新的执行前 Critic 评审同版包，并以其精确提交/结论决定是否允许未来用户启动；本文件本身不构成执行授权。
