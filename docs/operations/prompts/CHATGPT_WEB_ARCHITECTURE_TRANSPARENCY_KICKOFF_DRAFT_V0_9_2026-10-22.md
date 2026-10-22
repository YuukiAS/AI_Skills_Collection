# Kickoff 草案 v0.9：Planner–Critic 1.8 跨轮默认生效

任务：`chatgpt-web--pass-integrity`。日期：2026-10-22。
状态：DRAFT，不是用户的 Codex 执行授权。本轮仍在设计审查；只有同版完整包经最终 Critic `PASS + READY_FOR_CODEX=YES`，且用户实际发送短 `COPY TO CODEX` 后才可能执行。

## 执行身份与唯一来源

目标仓库：`YuukiAS/AI_Skills_Collection`。
设计分支：`design/chatgpt-web--pass-integrity-v0-4`。
正式角色合同目标版本：1.8；当前 main 正式版本仍 1.7。
本版执行权限将来绑定同一 PACKAGE_COMMIT 的：
- `docs/workflows/CHATGPT_WEB_ARCHITECTURE_TRANSPARENCY_PROPOSAL_V0_9_2026-10-22.md`
- `docs/workflows/CHATGPT_WEB_ARCHITECTURE_TRANSPARENCY_PLAN_V0_9_2026-10-22.md`
- `docs/goals/CHATGPT_WEB_ARCHITECTURE_TRANSPARENCY_GOAL_V0_9.md`
- 本草案与最终独立批准结论。

当前不能沿用早期计划中“正式新工作树固定于 /tmp”的位置；如确需创建工作树，必须在最终执行就绪包按现行目标仓库和 Bridge 规则确认实际合法路径与授权。原 task key 不变，不自行新建 successor 或控制角色。

## 批准后预定工作，不得提前执行

1. 在 `PLANNER_ROLE_CONTRACT.md` 的 §2/§6/§7/§10/§11 加入并落实 Proposal/Plan 中冻结的持续工作职责：默认读取 main、同一提案用户机制说明、每轮返修同步更新、独立审查输入、实际交接。不得只添加同义口号。
2. 在 `CRITIC_ROLE_CONTRACT.md` 的 §2/§4/§6.1–6.3 加入独立对照源码、替换反证、同版说明审查、跨轮技术/说明变更核对、真正受审内容交付的职责。保留原两角色、唯一最终 PASS 与短机器交接。
3. 保留原 1.8 的 task-prompt compatibility、关键执行接口现实证据、非终态唯一下一入口、同候选身份、最终评估前独立安全检查、main integration/readback，不复制出新状态机或第三套 workflow。
4. 冻结正式 1.8 候选源码与完整验证合同；后继 evidence 引用准确 candidate commit 和文件身份，避免 commit 自引用。运行必要 deterministic check，但不以机械通过代表自然中文/机制说明质量。
5. 在候选条件下完成真实多轮返修与角色交接验证：新对话首次明确绑定 candidate role text，此后不再重复写作要求；保存完整多轮输入、实际用户输出及对应来源身份，交现有独立 Critic 判断；有 blocker 就 REVISE，不换题追 PASS。
6. 独立的实现后 Critic 安全门只有 `PROCEED_TO_FINAL_EVALUATION / REVISE`；此后按冻结实际 Web 批次检查，不触发 paid API，必要 fresh ChatGPT Web UI 操作由 Planner 提前准备完整 prompt，用户只做无法自动完成的界面步骤。
7. 满足既有准入条件后按 `AGENTS.md §8.5` 进行安全集成、正常推送和远端 main 回读；新 1.8 真正进入正式 main 后，另用提前冻结的真实普通任务验证不提醒也能自行触发。不得把 main 更新当作稳定行为已经证明。

## 权限与限制

仅在最终执行就绪 Critic PASS 和用户短入口授权之后，允许任务范围内角色合同、关联治理回归与证据的修改以及原 Plan 规定的集成动作。

本轮禁止修改 Project setting、Capability Gate Policy、Clear Writing 产品、其他插件、Slurm、Bridge、Mica、Plugin Creator；禁止开启额外模型付费、真实账户变更、生产取消、未授权 external transfer、强制发布服务、操作其他人工作或重写 Git 历史。任何实质扩大范围必须先重新进入 Planner–Critic 与用户授权。

每次用户可见回复先讲清任务变化、机制如何工作、风险与下一步，再附准确机器交接；提示词无须一遍遍复制这项要求，正式实施后从 main 的角色合同消费它。原生 Web 没有受控发送前 Hook 的事实必须如实保留。

## Stop / next owner

普通源文件改错、实现测试失败：同一 Codex 任务继续修，若不改变冻结语义不重开设计。
改变技术方案、权限、执行职责、验收或安全恢复：回原 Planner，更新技术包和给用户的架构说明，再由独立 Critic 审新版本。
无法验证 normal-entry Web 或候选身份：停止声称该能力通过；由当前 Planner 准备明确的合法用户界面动作和可回传的完整证据包，不能让用户自己寻找环境。
本轮仍只待设计 Critic `PROCEED / REVISE`；不得现在运行上述工作。
