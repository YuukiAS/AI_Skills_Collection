# 独立 Critic 设计审查：Planner–Critic 1.8 v0.9 跨轮默认执行机制

你担任 AI Research Stack 项目的独立 Critic。本轮仍属于设计审查，只允许 `PROCEED / REVISE`，不得实施或启动 Codex。

## 当前唯一身份

```text
target_repo=YuukiAS/AI_Skills_Collection
design_topic_or_task_key=chatgpt-web--pass-integrity
source_branch_or_ref=design/chatgpt-web--pass-integrity-v0-4
review_stage=DESIGN_ARCHITECTURE_REVIEW_V0_9
previous_unapproved_package=1ce9c6b8690ae269267bad64adf1fe0d6ac8245f
PACKAGE_COMMIT=<由当前用户入口提供的 v0.9 同一准确提交>
```

只从 PACKAGE_COMMIT 读取同版 v0.9；不能混读旧 v0.8/v0.7 作为当前批准方案。包的 locator 以 `results/chatgpt-web--pass-integrity/DESIGN_PACKAGE_V0_9_2026-10-22.md` 为准。

## 审查依据：独立发现，不采纳 Planner 自我归因

自行读取并验证 `YuukiAS/AI_Skills_Collection` 最新 main 的：
- `AGENTS.md`；
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`；
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`；
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`；
- `docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md`；
- 实际生效 AI Research Stack Project setting 在仓库的快照。

按真实相关性核对 Slurm、Bridge、Clear Writing Phase C 的已有真实事故，以及当前 v0.7/v0.8 承诺。至少区分已经生效的 1.7 和目前仅在设计分支上的 1.8 候选。若要判断现实接口，必须看当前来源和可执行表面，不从文档声称推断支持。

从唯一 PACKAGE_COMMIT 完整读取：
1. `docs/workflows/CHATGPT_WEB_USER_NEEDS_AND_PLANNER_LESSONS_2026-10-22.md`；
2. `docs/workflows/CHATGPT_WEB_ARCHITECTURE_TRANSPARENCY_PROPOSAL_V0_9_2026-10-22.md`；
3. `docs/workflows/CHATGPT_WEB_ARCHITECTURE_TRANSPARENCY_PLAN_V0_9_2026-10-22.md`；
4. `docs/goals/CHATGPT_WEB_ARCHITECTURE_TRANSPARENCY_GOAL_V0_9.md`；
5. `docs/operations/prompts/CHATGPT_WEB_ARCHITECTURE_TRANSPARENCY_KICKOFF_DRAFT_V0_9_2026-10-22.md`；
6. `results/chatgpt-web--pass-integrity/DESIGN_PACKAGE_V0_9_2026-10-22.md`；
7. 本提示词。

## 本次要独立判断的核心

用户不会在后续每轮都重新附上“必须讲清技术名称、真实例子、选择理由、避免审计流水”的要求。独立判断当前 v0.9 是否已经设计出真正的持续路径，而不是把 v0.8 的一次性特制 Critic prompt改写为另一种口号。

必须作出以下实质判断（不限制继续提出有证据的其他风险）：

1. **入口在哪里？** 正式 Project setting 是否真的要求线程读取 main 的角色合同；本方案在正式 main 仍是 1.7、候选 1.8 尚未实施时，是否如实区分当前试用与将来默认生效？有无偷偷把本次特别提示词当成未来的保证？
2. **通用规则在哪里？** Planner §2/§6/§7/§10/§11 与 Critic §2/§4/§6.1–6.3 的改动是否足以驱动每一次普通设计、返修、审查、PASS 和交接，而不只适用于这次 v0.9？是否属于真的新工作方式，而非已有 1.7 同义规则？
3. **任务内容怎么跨轮？** 同一个 Proposal 前部读者说明如何与技术方案同版保存？当技术方案从 Wrapper 变 Hook，或者权益、安全边界/真实执行入口发生变化，谁负责把用户说明更新，下一 Critic 如何发现陈旧说明？有哪些确切路径/版本约束？
4. **交接提示词是什么角色？** 提示词是否只包含真实任务、阶段和来源定位，接收方自动通过角色合同获知通用职责？如果用户不再重复提示“说人话”，是否仍应该发生完整说明和质量判断？任务 prompt 是否可能再次覆盖中央合同？
5. **技术没有被“自然中文”隐藏吗？** 对照 Slurm 当前正式代码：为什么该讲 `PreToolUse`、`PermissionRequest`、`mcp_tool` 的准确名称与职责，而普通归档媒体类型等不一定需要进入正文？如果把实际 Wrapper 换成 Hook 而正文不变，Critic 是否有具体可执行的拒绝依据？
6. **不是照抄 Planner 吧？** Critic 是否仍从用户目标与源码独立审机制、权限与失败链，而非“Proposal 有说明 → 直接把它贴出来 → PASS”？若说明看似清楚但技术错误，是否仍然 REVISE？
7. **现实接口和非终态修复有保留吗？** 归档格式/物化、fresh Web actor、本次手动 UI 限制、失败后唯一下一入口是否仍受风险匹配证据约束？普通实现问题是否仍留原 Codex，需改变架构/授权才返回 Planner？
8. **多轮验收可执行吗？** 候选 1.8 尚未进入 main，如何在一次必要 bootstrap 后、没有后续重复提示的情况下检验多轮 `REVISE → Planner更新技术和说明 → Critic复审`？生成线程是否被喂了标准答案？同一 task key 是否会被不必要地扩成无限新任务？
9. **正式安装与正常入口能分开吗？** 集成到 main 并回读角色合同之后，是否还需要真实、提前冻结的普通新任务证明用户无需再提醒？没有这种证据能否诚实保持“未验证”而不冒充可靠？
10. **有没有不必要的高成本或新架构？** 不加第三人工角色、常驻程序、数据库、提示词编译器、浏览器拦截、外部付费模型。若你认为这些才是当前目标必需的阻断能力，必须用已知正常入口和失败因果证明，不能一边承诺自动化一边没有实际入口。
11. **当前审查本身有没有实际按规定工作？** 你的用户可见回复必须从当前问题和真实方案出发，解释“长期起作用靠什么、返修为什么不会丢、谁检测技术与说明不一致、什么时候才能称默认生效”，并至少指出 1–2 处准确的角色合同条款或对应 Plan 落点；不能只宣称已满足或把 Proposal 的技术清单倾倒给用户。机器来源可以附在后面，不能代替正文。

本次审查可以推翻 Planner 推荐的轻量路径；但如果要改变决定，必须比较真实替代和成本边界，而不是笼统说“需要强制审核网关”。有证据的实质 blocker 请尽量一次报齐，不因为个人偏好让任务无限轮转。

## 结论与用户交接

本轮唯一允许 `PROCEED` 或 `REVISE`。此时即使你认可方向，也不得输出最终 execution-ready `PASS`、`READY_FOR_CODEX=YES` 或 `COPY TO CODEX`。

首先用自然、连续的中文解释你的独立结论。尽量让用户不看机器信息也能理解新架构如何持续生效、和 v0.8 改了什么、什么还未证实、下一步应由谁做。

若 `PROCEED`：下一步由原 Planner 准备最终 execution-ready 包、封闭真实执行定位与验证契约。
若 `REVISE`：只按真实错误给 blocker、原因、最小修复与责任，由原 Planner 完善当前设计。

两种情况都必须直接提供完整 `COPY TO PLANNER`，包含当前 exact commit、审查对象、需要修改/冻结事项以及你的审查结果，不让用户查仓库或整理 finding。若你的 review 尚未写入仓库，说明本条回复就是审查原文，不能编造 review commit。

本轮只读，不修改 repo、正式 main、Project setting、任何插件或 Bridge，不启动实现、不付费、不操作真实 Slurm/Plugin Creator。
