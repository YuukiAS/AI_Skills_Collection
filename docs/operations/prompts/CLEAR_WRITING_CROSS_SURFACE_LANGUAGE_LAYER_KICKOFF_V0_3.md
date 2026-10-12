# Clear Writing 跨 ChatGPT / Codex — Kickoff Draft v0.3

> **只供未来使用，当前严禁直接启动。** 必须先有独立执行前 Critic 对本 v0.3 Proposal / Gate / Plan / Goal / Kickoff 精确版本给出 `PASS / READY_FOR_CODEX=YES` 的真实持久审查记录，随后由用户亲自发送这份被批准的 Kickoff。架构阶段 PASS 只批准精简方向，不能冒充实现授权。

## 1. 启动身份及审核依赖

你是 `YuukiAS/AI_Skills_Collection` 任务 `clear-writing--cross-surface-language-layer` 的 Codex Executor。唯一中央插件：`writing-style` / Clear Writing。目标是执行获批 v0.3 范围：保留现有五项正式技能标识和科研长文重写主链，新增轻量 `response-clarity`，完善普通聊天与中文文档的触发分界，并从同一正式源构建 Codex 和 ChatGPT 私有插件候选，证明正常无 `@` 的实际增量与现有领域消费者的真实使用。

执行包在 `planner/clear-writing-cross-surface-v0.1`，必须读取下列**同一版本**：

- `docs/design/clear-writing/CROSS_SURFACE_LANGUAGE_LAYER_PROPOSAL_V0_3_2026-10-12.md`
- `docs/design/clear-writing/CROSS_SURFACE_LANGUAGE_LAYER_GATE_MATRIX_V0_3_2026-10-12.md`
- `docs/design/clear-writing/CROSS_SURFACE_LANGUAGE_LAYER_EXECUTION_PLAN_V0_3_2026-10-12.md`
- `docs/goals/CLEAR_WRITING_CROSS_SURFACE_LANGUAGE_LAYER_GOAL_V0_3.md`
- 本 Kickoff v0.3
- **未来新增且经过独立审查的**执行前 Critic PASS 记录，必须包含审查提交、包版本与 `READY_FOR_CODEX=YES`；不存在或身份不匹配就立即停止。

架构阶段的独立 Critic PASS 由用户转述，审查对象是 `819f861de7dc626f473390df8a9c42b70d24dd92` 的 v0.1；不得把它虚构为已存在的仓库审查文件。旧 PR #100 关闭且未合并。当前 v0.3 执行前没有 PASS 和用户启动授权。

## 2. 用户未来发送此 Kickoff 后所授的有界权限

准确 Reviewed Handoff 身份：

`task_key = clear-writing--cross-surface-language-layer`
`branch = reviewed/clear-writing--cross-surface-language-layer`
`canonical checkout = 执行机经验证的 YuukiAS/AI_Skills_Collection 根目录`
`worktree = 该 checkout 所在父目录下 AI_Skills_Collection-clear-writing--cross-surface-language-layer`
`base_commit = 执行机 fetch 后的 origin/main 精确提交`
`max_review_rounds = 2`
`ci_required = true`
`no_paid_text_or_visual_review = true`

只允许对此准确任务的一次 Bridge 正式 bootstrap、合法非强制首次同名远端发布、任务所属源码/生成包/测试/公开安全评估/必要发布文档更改，使用当前已授权 Codex 账户做零额外付费候选运行和可查看的报告、界面、演示文稿渲染。按 Goal 在项目认可的场景中可准备且后续经用户批准创建**最多一个**个人 PRIVATE/USER-scope Clear Writing 技能型 ChatGPT 插件，并有限更新该同一身份的候选发行；Plugin Creator 调用属于有工具和授权的 GPT 线程职责，不假定 Codex 可以直接修改 ChatGPT 用户账户。用户可见的平台安装确认仍按平台执行。仅限用户批准的试点 Project 短桥试验，不授权修改所有真实 Project 或全局个性化指令。

**此 Kickoff 不授权**：Research Authoring 任何源码/包装/插件/迁移，PIE 0.2、其它中央插件的生产重构、外部 API/付费审核/托管/密钥/MCP/钩子、持续 watcher/自动调度、敏感数据公开传输、批量改账号设置、公开插件发布、主线/正式发行立即合并、危险 Git/reset/clean/force。最后正式集成仍需独立 Reviewer 与用户最终 `ACCEPT`。

## 3. 首次预检与 Bridge 有界入口

在准确目标仓库中读取最新 `AGENTS.md`、Planner/Critic 角色合同、能力验收政策、维护看板、版本规则、AI Skills Maintainer 规则，并读取最新 Bridge Kit `AGENTS.md`、当前 `automation/reviewed_handoff/README.md` 和模板。实际核对 Git remote、当前 branch/worktree、可安装插件、用户已有个人 Clear Writing 是否存在、当前 `main/release` 发行基线，不能靠规划期快照推断运行环境。

在新任务分支/工作树尚不存在且目标路径未被占用时，使用 Bridge 正式入口，不用 raw `git worktree add` 或 `git push -u`：

`ai-bridge reviewed-handoff task bootstrap --task-key clear-writing--cross-surface-language-layer --expected-repo YuukiAS/AI_Skills_Collection --expected-base-commit <执行时实际 fetch 的 origin/main OID> --objective "实现经执行前 Critic 批准的 Clear Writing v0.3 跨 ChatGPT/Codex 通用表达层；原五项标识不变，新增 response-clarity，证明无 @ 正常入口和领域真实消费；Research Authoring/PIE 不在范围。" --max-review-rounds 2 --ci-required`

该命令须在执行环境核对合法参数和当前 Bridge 规则；如不支持，停止并报告，不另造 CLI 或绕过。**CW-ER-01 首次远端交接必须在 bootstrap 之后另行完成；bootstrap 只创建本地 reviewed 分支、派生工作树和未提交的首份 REQUEST/CURRENT，并不自动 commit/publish。**

**首次 bootstrap 前的不可变审批定位（未满足则停止，不运行命令）：** 未来用户实际发送本获批 Kickoff 时，必须一并给出完整 `APPROVED_V03_PACKAGE_COMMIT`（六份 v0.3 文件全部存在的不可变 Git 提交）、真实独立执行前 Critic `PASS / READY_FOR_CODEX=YES` 审查文件的 `EXECUTION_CRITIC_REVIEW_PATH` 及完整 `EXECUTION_CRITIC_REVIEW_COMMIT`。执行者必须从固定规划提交而非浮动规划分支读取六份文件、核对审查记录指向同一包；未提交仓库的旧审查转述和 v0.2 `REVISE` 均不能代替这个后续真实的执行前 PASS。

需在首次 REQUEST 记录的六个精确 v0.3 路径：

- `docs/design/clear-writing/CROSS_SURFACE_LANGUAGE_LAYER_PROPOSAL_V0_3_2026-10-12.md`
- `docs/design/clear-writing/CROSS_SURFACE_LANGUAGE_LAYER_GATE_MATRIX_V0_3_2026-10-12.md`
- `docs/design/clear-writing/CROSS_SURFACE_LANGUAGE_LAYER_EXECUTION_PLAN_V0_3_2026-10-12.md`
- `docs/goals/CLEAR_WRITING_CROSS_SURFACE_LANGUAGE_LAYER_GOAL_V0_3.md`
- `docs/operations/prompts/CLEAR_WRITING_CROSS_SURFACE_LANGUAGE_LAYER_KICKOFF_V0_3.md`
- `docs/design/clear-writing/CROSS_SURFACE_LANGUAGE_LAYER_EXECUTION_CRITIC_PROMPT_V0_3_2026-10-12.md`

按以下次序完成**首次合法远端交接**：

1. 在已核实的 canonical 仓库工作目录成功运行上述 `task bootstrap` 后，读取其返回的 sibling worktree **真实绝对路径**，然后**进入这一派生的 reviewed 工作树**。核实当前分支为 `reviewed/clear-writing--cross-surface-language-layer`，`CURRENT.base_branch=main`、`CURRENT.base_commit=bootstrap 所使用的 origin/main SHA`、`CURRENT.state=PLAN_REQUESTED`、`CURRENT.next_action=RUN_GPT_PLANNER`、`review_round=0`、`plan_revision=0`、`implementation_commit=null`，以及 REQUEST 中的合法工作树定位。
2. 编辑**该任务工作树中新建的首份** `automation/reviewed_handoff/tasks/clear-writing--cross-surface-language-layer/REQUEST.md`，保留 Bridge 已生成的任务/工作树信息，准确补记上面的 `APPROVED_V03_PACKAGE_COMMIT`、六份文档路径、真实审查 `EXECUTION_CRITIC_REVIEW_PATH@EXECUTION_CRITIC_REVIEW_COMMIT` 以及对应 `PASS`。**不修改**首次 `CURRENT.json` 状态。由于 reviewed 分支以 `origin/main` 为基线，不能假设它拥有规划分支新增的 v0.3 文件；下一 Planner 必须使用 REQUEST 中的不可变 Git 定位远端读取，不得复制设计文件进首个提交。
3. 在**此 reviewed 工作树**只暂存这两个 task-owned 新文件。以下命令必须在该工作树执行，不在 canonical main 执行：

   `git add -- automation/reviewed_handoff/tasks/clear-writing--cross-surface-language-layer/REQUEST.md automation/reviewed_handoff/tasks/clear-writing--cross-surface-language-layer/CURRENT.json`

   `git diff --cached --name-status`

   暂存变更必须**严格只有两行新增 `A`**，分别是上述 REQUEST 和 CURRENT。确认当前 HEAD 尚为 `CURRENT.base_commit`，然后普通提交一次，例如：

   `git commit -m "chore(reviewed): initialize Clear Writing task metadata"`

   提交后核对 **HEAD 是 `CURRENT.base_commit` 的一个直接子提交且仅有这个一个新提交**，原始树差异正好是这两个 `A` 新增文件，工作树干净；严禁包含 PLAN、RESULT、源代码、其它任务文件或第二个提交。任何不匹配立即停止，不通过 raw push 或改写历史修饰。
4. 确认当前工作树无已设置的 upstream，远端同名 reviewed 分支不存在，且 Bridge 允许的 HTTPS 传输条件成立。仍在该 reviewed 工作树执行：

   `ai-bridge reviewed-handoff task publish-first --task-key clear-writing--cross-surface-language-layer --expected-repo YuukiAS/AI_Skills_Collection`

   不使用 `git push`、`git push -u`、强制更新、其它工作树、第二 bootstrap 或盲目重试。若发布失败、远端结果有歧义或部分成功，保留候选、提交与输出，停止并依现有 Bridge 合法恢复机制诊断。
5. **真实远端回读**：从远端检查 `origin/reviewed/clear-writing--cross-surface-language-layer` 的分支 SHA 必须等于唯一基线提交，upstream 正确且工作树干净；远端 `REQUEST.md` 必须保留完整 v0.3 批准包 SHA、全部六份路径、真实 Critic review 路径及其精确提交；远端 `CURRENT.json` 的 `task_key`、`base_commit`、`state=PLAN_REQUESTED`、`next_action=RUN_GPT_PLANNER`、轮次为 0、`implementation_commit=null` 均一致。还应能从 REQUEST 指向的精确规划/审查提交实际读取相应文件。只打印本地路径或自报已发布不算交接完成。

**以上五步全部通过才停下，将真实远端 reviewed 分支、基线提交和 `RUN_GPT_PLANNER` 下一动作交给人工 Planner。** 长期 Planner 必须从已发布的 reviewed 分支读取 REQUEST/CURRENT，并根据其中的不可变规划包和真实 Critic review 定位读取完整 v0.3 合同，按现有 `AI_BRIDGE_REVIEWED_PLAN_V2` 模板写、核对 task-local PLAN，然后才合法推进 `PLAN_FROZEN / RUN_CODEX_EXECUTOR`。不假定自动 Planner/Reviewer 已存在，不在本首次发布阶段修改任何生产源码。

## 4. Planner 冻结后，Executor 的实施范围

满足 `PLAN_FROZEN / RUN_CODEX_EXECUTOR` 后，严格遵守 Canonical Goal v0.3，明确使用：

`workflow-core + ai-skills-core + writing-style`

只新增 `skills/writing/core/response-clarity/`，最小收紧 `chinese-prose` 的元数据和必要的保真条款；五项旧技能名字、复杂 `scientific-rewrite` 主链保持。更新正式 `scripts/codex_marketplace_config.json` 中同一个 `writing-style` 条目，从现有生成器重新构建六项技能和 Marketplace，旧五项 generated artifact id 不动；若实际包支持文件必须自包含，直接在需要的独立技能中提供最小保护合同，不假定再调用其它技能。

只运行批准范围的正向/间接/近似/负向触发与旧功能回归；领域集成只读取现有 Frontend Design / Presentations 入口并用真实产物验证，不主动改它们的生产源码。除用户明确选择的私有测试场景外，使用公开安全材料；保存完整答复、真正可打开的前端渲染与整套幻灯片，以及中英文文稿的源/输出对照。已知 C5–C11、050–055 用于开发而非最终未见认证。

按 Plan 在最后一次不可调优验收之前完成候选版本与必要的正式生成包/文档/评分标准封口，交独立 Critic 实读代表性完整材料。只有获批的同一最终 `C_n` 可以进入正式 Codex 安装和 ChatGPT 个人私有插件同源包装；包装若无法从公开安全冻结源在 GPT 端重建并核对哈希，停止 G0，不假称已安装。

随后按照 G0–G7 做 Project **A/E 无短桥匹配、B/C 有相同短桥匹配**以及 D 显式 `@` 诊断，另做无 Project 个性化基线。A/E 与 B/C 各自仅能改变插件有无；无法合法、可靠地匹配必须记 `INCONCLUSIVE`，不能宣称自动增益，只有 D 通过或无稳定增量时回 Planner 简化，不无限重试。完整专业产物、真实渲染与语义保真由独立 Reviewer 直接获取。最终未见样本、次数和准则在冻结候选后、生成前锁定。

## 5. 交接、版本与完成边界

执行过程中如要外部 Planner、Critic 或 Reviewer 接手，只发布准确任务状态、分支提交、结果文件和安全可读的完整审查材料位置。等待外部审查是正常等待，不冒充产品失败或任务完成；没有已验证的 Scheduled GPT 时只走人工交接，不增添 watcher/自动任务。

`Repository bump decision = PATCH（仅经最终用户接受之后的正式 release；精确三段号按届时发行基线）`
`Affected plugin = writing-style 0.4 -> 0.5（仅同一正式候选全部关键 Gate 成立后一次）`
`Other plugin versions = NO_BUMP`
`Maturity = NO_CHANGE`

提交前按当前仓库规则执行零额外付费回归、技能校验、生成层一致性与必要正式 CI。最终正式发布前检查 README：若需改，必须真实调用已安装的 Clear Writing 完成读者质量检查，未能调用则停下，不把本设计自审当作调用。

失败时保留准确候选和原始审查结果，停止发布，恢复项目试点短桥、已变更的个人 Clear Writing 插件版本与 Codex 原安装（若是首次新建无旧版，先取得合法停用/卸载动作的授权）。不删除别的插件、不修改 Research Authoring、不声称设置自动恢复成功。最后经独立 Reviewer PASS、用户明确 `ACCEPT`、合法非强制集成与版本一致性闭环之后，才可报告正式完成。

**当前这份 Kickoff 仍是草稿。任何执行都必须等到执行前独立 Critic 的精确版本 PASS，且用户亲自发送获批文本之后。**
