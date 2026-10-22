# Planner–Critic 1.8 v0.13：执行范围草案

状态：`DRAFT / NOT_AUTHORIZED`。任务：`chatgpt-web--pass-integrity`。  
当前正式 main 仍是 Planner/Critic 1.7。只有同版 v0.13 包获唯一 execution-ready `PASS + READY_FOR_CODEX=YES`，且用户实际发送 Critic 给出的短 `COPY TO CODEX`，才授权实施。

## 唯一当前包

同一 PACKAGE_COMMIT 必须包含：
- `docs/workflows/CHATGPT_WEB_DECISION_VISIBILITY_PROPOSAL_V0_13_2026-10-22.md`
- `docs/workflows/CHATGPT_WEB_DECISION_VISIBILITY_EXECUTION_PLAN_V0_13_2026-10-22.md`
- `docs/goals/CHATGPT_WEB_DECISION_VISIBILITY_GOAL_V0_13.md`
- 本 Kickoff Draft
- `results/chatgpt-web--pass-integrity/VALIDATION_CONTRACT_V0_13_2026-10-22.md`
- `docs/workflows/CHATGPT_WEB_DECISION_VISIBILITY_FINAL_CRITIC_PROMPT_V0_13_2026-10-22.md`
- `results/chatgpt-web--pass-integrity/EXECUTION_READY_PACKAGE_V0_13_2026-10-22.md`
- 已经发生的历史 Critic authorities（例如 v0.12 `REVISE` 原文）。

**当前 v0.13 final Critic reply 不属于 PACKAGE_COMMIT，也不要求预先存在。** 它只能在 Critic 审完这个 immutable package 之后作为 post-review evidence 产生。

旧 v0.7/v0.8/v0.9/v0.10/v0.11 或错误扩项 v1.0 只作历史证据，不是当前实施 authority。

## 获准后允许

1. 在用户实际选择的现有 AI Skills workspace 中只读核对 repo/origin/current branch/HEAD/dirty ownership/授权；执行目标是已存在 `design/chatgpt-web--pass-integrity-v0-4`。若实际 checkout 不匹配或需新 worktree/switch/吸收无关 dirty，STOP 返回 Planner；不得沿用旧 `/tmp` 正式工作树方案或擅自切换用户工作。
2. 按 v0.13 Plan **完整**实现 Planner/Critic 1.8 的 P18/C18 合同，不再从历史 v0.7猜继承关系。future C18-2 direct `NEXT_HANDOFF=CODEX` 明确替换为 technical PASS→Planner delivery acceptance；bootstrap 本次批准仍遵当前1.7 direct Codex。
3. 修改仅限两份 role contract、collaboration regressions、当前 results/validation和必要最小 deterministic test。不得修改 AGENTS/README，除非实际实施 diff暴露当前包未审的必要变化；那时 STOP 返回 Planner/Critic。
4. 当前 Critic若 PASS，short `COPY TO CODEX` 必须自包含 `BOOTSTRAP_CRITIC_AUTHORITY`：`reviewed_package_commit`、review stage、PASS/READY、approved Proposal/Plan/Goal/Kickoff locators、执行授权边界和关键 limitations。该 `reviewed_package_commit` 才获得 `IMPLEMENTATION_APPROVED_PACKAGE` 身份。用户实际发送该短 handoff 后，Codex先把自己实际收到的两项 identity/evidence 如实写入 task results，且早于任何 candidate 1.8 Web输出。若没有 current PASS/READY，禁止开始。完整 Critic自然中文原文不是 short handoff 的必要内容，也不属于原 package commit；只有实际取得后才能另存为 post-review evidence。
5. 修改稳定后运行 cheap deterministic eight-case，提交 `GOVERNANCE_CANDIDATE_COMMIT` 和候选 manifest；candidate-defining source变化使旧 evaluation失效。
6. 交独立 Critic implementation safety gate，仅 `PROCEED_TO_FINAL_EVALUATION/REVISE`；前者才允许运行冻结 A/B/C/D Web验证。fresh Web没有已验证自动入口，必要 UI动作由 Planner/Codex预备完整prompt，用户只打开指定对话/粘贴/回传完整回复。
7. 符合冻结真实评估后，若当前 Kickoff授权覆盖普通 integration，按现行 AGENTS §8.5 做 main preflight、non-force merge/push 和 remote readback；conflict/same-area competing change/identity mismatch STOP。
8. 远端 main 两份合同确认为同一受审1.8候选后，只称“正式规则源已升级”。未来真实新任务正常入口出现前，不称长期新任务可靠性已验证。

## 明确禁止

不修改 Project setting、Capability Gate Policy、Clear Writing、Slurm、Bridge Kit、Mica、Plugin Creator、其它插件产品；不使用付费 API、真实调度/插件生产 mutation、账户/credential变更、私有数据新外传；不增加第三人工角色、service/watcher/daemon/database/state machine/prompt compiler/浏览器拦截；不 force/rewrite history、不删除无关分支、不无授权创建/switch正式工作树。

普通实现错误不改变冻结语义时同一 Codex修；要改变用户承诺、角色 owner、权限/数据/费用、验收标准、最终 PASS route或恢复语义，STOP回 Planner/Critic重新审查。

## 当前与未来 PASS 路由区别

**当前本次实施 1.8 的最终审查：** 正式合同仍1.7，所以若 PASS，Critic同回复直接给短 `COPY TO CODEX`，其中携带启动所需的 `BOOTSTRAP_CRITIC_AUTHORITY`。用户发送该 handoff 才构成实施指令；final Critic完整自然中文正文如另行归档，只能是审查后的 evidence，不属于被审 package。

**1.8正式生效后的未来复杂架构：**
`Critic technical PASS + READY_FOR_CODEX=YES -> NEXT_HANDOFF=PLANNER -> Planner delivery acceptance -> short COPY TO CODEX -> user sends -> Codex`。

不得把两种时点混为同一协议。