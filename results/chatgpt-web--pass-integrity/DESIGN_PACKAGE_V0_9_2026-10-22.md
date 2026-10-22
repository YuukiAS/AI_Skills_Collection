# Planner–Critic 1.8 v0.9 设计包、身份与审查边界

日期：2026-10-22。任务：`chatgpt-web--pass-integrity`。
设计分支：`design/chatgpt-web--pass-integrity-v0-4`。
审查阶段：`DESIGN_ARCHITECTURE_REVIEW_V0_9`，仅 `PROCEED/REVISE`。
本文件不包含自身所在提交 SHA。审查入口负责传递最新同一 PACKAGE_COMMIT，以避免自引用哈希循环。

## 此版唯一完整文件清单

从同一准确 `PACKAGE_COMMIT` 读取：

1. `docs/workflows/CHATGPT_WEB_USER_NEEDS_AND_PLANNER_LESSONS_2026-10-22.md` — 用户稳定需求和新补充的多轮默认生效要求。
2. `docs/workflows/CHATGPT_WEB_ARCHITECTURE_TRANSPARENCY_PROPOSAL_V0_9_2026-10-22.md` — 读者机制说明和架构决定，尤其 §1/§3/§5。
3. `docs/workflows/CHATGPT_WEB_ARCHITECTURE_TRANSPARENCY_PLAN_V0_9_2026-10-22.md` — 两份正式角色合同的具体修改与多轮真实验证合同。
4. `docs/goals/CHATGPT_WEB_ARCHITECTURE_TRANSPARENCY_GOAL_V0_9.md` — 能力结果、同版用户说明、默认触发的验收目标。
5. `docs/operations/prompts/CHATGPT_WEB_ARCHITECTURE_TRANSPARENCY_KICKOFF_DRAFT_V0_9_2026-10-22.md` — 后续允许/禁止执行范围，仍为草案。
6. `docs/workflows/CHATGPT_WEB_ARCHITECTURE_TRANSPARENCY_CRITIC_PROMPT_V0_9_2026-10-22.md` — 独立设计 Critic 全文。
7. 本 manifest。

保留历史但不再作为当前批准依据：
- v0.7 package `0bd4dbf09be68811cafac53afdaad0f671206023`；
- v0.8 package `1ce9c6b8690ae269267bad64adf1fe0d6ac8245f`。

## 已核对正式与外部治理来源

本轮实际读取最新已知 main `f1de8e85957d32a50f4458349f450ec65add13bb` 的：
- `AGENTS.md`；
- `docs/workflows/PLANNER_ROLE_CONTRACT.md` 1.7；
- `docs/workflows/CRITIC_ROLE_CONTRACT.md` 1.7；
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md` 1.2；
- `docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md`；
- `docs/project-settings/AI_RESEARCH_STACK_PROJECT_INSTRUCTIONS_SNAPSHOT_2026-10-19.md`。

Bridge Kit `YuukiAS/GPT_Codex_AI_Bridge_Kit` main 的 `AGENTS.md` 已核对：新正式任务工作树不得默认使用系统 `/tmp`；此包不实施 Bridge，未创建工作树。

真实事故来源：
- Clear Writing Phase C 受阻 `38a81dc1df9a362ecee4be597cb3db5bd6fcac41`；
- Slurm Workflows 0.5 正式技能与可执行源码、安装验收；
- 历史 Bridge、Slurm 用户级交付失效；
- v0.7/v0.8 的三项现有回放 A/B/C。

## 本轮新增的必要机制

原 v0.8 仅设计“事先写说明、Critic对照、最终交付同版”。v0.9 明确：
- **初始化来源**：正式 Project setting 指向 latest main 两份角色合同，不能依赖一条定制审查 prompt；
- **每轮连续**：同 task key 下 `REVISE/PROCEED/PASS`、执行中断和恢复都有对应刷新与审查责任；说明随技术变更同步；
- **跨线程身份**：准确 Proposal 章节、版本和审查记录留在仓库，新线程只需常规 locator；
- **后续验证**：候选合同的一次 bootstrap 后不再给生成线程写作答案；正式 main 后普通新任务验证；
- **约束边界**：正式 main 仍是 1.7；只有完成集成和真实普通入口验证后才能说已证明默认生效。

## 本轮未做的事

没有修改 `main`、正式角色合同、当前 ChatGPT Web 项目设置、Capability Gate Policy、Clear Writing、Bridge Kit、Slurm、Mica、Plugin Creator、正式插件发行物、用户数据或生产服务。

没有运行产品 Gate、付费 API、Slurm 命令或真实插件变更。
没有得到独立 Critic 本轮 verdict；本包不能直接交 Codex 执行。

Maintenance：当前 task key 精确搜索未确认唯一匹配 tracking Issue；待后续合法有写入能力的维护轮次继续按 Maintenance Board 自行查找/复用并同步当前执行锚点，不让用户手工维护，不宣称已完成 Project 变更。

## 用户下一入口

独立 Critic 设计审查 v0.9，只给 `PROCEED/REVISE` 并直接生成返回原 Planner 的完整 prompt。无需用户附加“怎样说人话”的评分清单；审查合同来自正式治理与此版方案本身。
