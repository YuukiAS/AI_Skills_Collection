# Slurm Workflows v0.3 — Exact Kickoff Draft（待 execution-ready Critic PASS）

状态：PENDING_EXECUTION_READY_REVIEW / NOT_YET_USER_AUTHORIZED。

当且仅当独立 Critic 对当前同版执行包给出 execution-ready PASS，并在用户发送本段时同时提供准确的 APPROVED_COMMIT，本 Kickoff 才成为当前用户对下述**限定范围**的执行授权。没有 APPROVED_COMMIT、提交不一致、用户未实际发送本段，全部停止。

目标：
- repo：YuukiAS/AI_Skills_Collection
- task：hpc--slurm-cancel-human-confirmation
- 主仓库 R：/overflow/htzhu/mingcheng_new/AI_Skills_Collection
- 工作树 W：/overflow/htzhu/mingcheng_new/AI_Skills_Collection-hpc--slurm-cancel-human-confirmation
- branch：reviewed/hpc--slurm-cancel-human-confirmation
- canonical design：docs/design/slurm-workflows/SLURM_WORKFLOWS_CANCEL_PROTECTION_PROPOSAL_V0_3_2026-10-13.md
- execution Plan：docs/design/slurm-workflows/SLURM_WORKFLOWS_CANCEL_PROTECTION_EXECUTION_PLAN_V0_3_2026-10-13.md
- Goal：docs/goals/hpc--slurm-cancel-human-confirmation-goal-draft-v0_3.md

执行顺序严格如下：

1. 只在 R 中运行。先确认 repo/origin/clean 状态仍与冻结合同一致，然后执行 git fetch origin main。要求 refs/remotes/origin/main == APPROVED_COMMIT；否则立即停止，不创建任何 branch/worktree。
2. 再确认 W 不存在/未注册、同名 local/remote-tracking branch 不存在，并核对上述三份合同及 Kickoff 在 APPROVED_COMMIT 中与被审版本一致。
3. 仅使用正式 Bridge 入口初始化：
   ai-bridge reviewed-handoff task bootstrap --task-key hpc--slurm-cancel-human-confirmation --expected-repo YuukiAS/AI_Skills_Collection --expected-base-commit "$APPROVED_COMMIT" --objective "Implement only approved v0.3 Stage A Slurm cancellation protection; no real Slurm or remote deployment."
   禁止 raw git branch、git worktree add、切换到别的目录或改 Git 配置作为 fallback。
4. 核对 bootstrap 只创建固定 branch、W 和本任务首份 REQUEST.md/CURRENT.json。首次 commit 只能包含这两份元数据；首次远端发布只能使用：
   ai-bridge reviewed-handoff task publish-first --task-key hpc--slurm-cancel-human-confirmation --expected-repo YuukiAS/AI_Skills_Collection
   禁止 raw push、force、main 修改、其它 branch/remote 或夹带实现代码。
5. 首次发布成功后，**不要开始 Stage A**。读取新 task 的 CURRENT.json，要求它仍为 Bridge Kit 正常初始状态 PLAN_REQUESTED，next action 属于 RUN_GPT_PLANNER；若不是，立即停止。Codex/Executor 此时不得写 PLAN.md、不得自行把 CURRENT 改成 PLAN_FROZEN、不得启动实现。
6. 将 task 交给正式 GPT Planner。Planner 必须读取 REQUEST.md、本 Kickoff 引用的已批准 v0.3 Proposal/Execution Plan/Goal，以及运行时 automation/reviewed_handoff/prompts/PLANNER.md 与 templates/PLAN.md，只把已批准方案冻结为 automation/reviewed_handoff/tasks/hpc--slurm-cancel-human-confirmation/PLAN.md；必须使用 AI_BRIDGE_REVIEWED_PLAN_V2，保留 G1–G6、ER-02、所有权限和 out-of-scope，不重新设计。Planner 写 PLAN.md 后重新读取并按当前模板自检，只有合法时才最后更新 CURRENT.state=PLAN_FROZEN。若当前没有实际可用的 Planner/Scheduled Planner 交接入口，就保持 PLAN_REQUESTED / RUN_GPT_PLANNER 并报告等待，不把等待写成 BLOCKED 或成功，也不让 Executor 代替 Planner。
7. 只有远端 task branch 已经存在合法 PLAN.md 且 CURRENT.state=PLAN_FROZEN 后，Codex Executor/已有合法 Review watcher 才能在 W/固定 branch 执行 Stage A：通用 slurm-workflows 取消判定、本地私有策略接口、短本人确认表示、可选 Hook 辅助、确定性/纯函数测试、DII/CARE 只读消费者清单和 G1–G6 对应离线证据。后续普通非强制发布只允许同一已授权 branch，使用 Host Policy 当前正式受限入口。
8. **危险模拟必须先通过 ER-02 的同一进程隔离证明。** 如果运行环境仍可能访问真实 Slurm 控制器/API/MUNGE/socket、生产 SSH key/agent/凭据、真实远端网络/代理/隧道、宿主 PID/信号、现有 salloc/tmux holder、特权宿主控制入口或生产路径写挂载，则不得运行模拟 scancel、SSH/远端取消、Python subprocess 取消、数组/批量取消或 holder signal 测试。只能继续纯函数/静态测试并如实报告 G3 相应部分 BLOCKED_BY_ISOLATION。
9. 完成 Stage A 后提交任务范围内源码、离线证据和 RESULT，按 Review 状态协议交独立 Reviewer；不得自动进入真实部署、消费者写入或正式发布阶段。

如果首次发布后没有 Planner 交接入口，或 Planner 不能合法产生 AI_BRIDGE_REVIEWED_PLAN_V2，**本 Kickoff 的正确结果是停在 PLAN_REQUESTED 等待 Planner**；这不是 Codex 失败，也绝不授权绕过 Planner 直接实施。
绝对禁止：任何真实 sbatch/salloc/srun/scancel、mutating scontrol、真实 kill/pkill/tmux holder 终止；任何 H100 或 Longleaf htzhulab allocation 操作；服务器/Slurm/SSH key/authorized_keys/credential/private override/Codex Host Policy/生产 Hook 修改；DII/CARE 正式源码修改；Bridge Kit 修改；付费实验；新增 daemon/database/control plane；绕过隔离或把 auto_review/长 Goal/历史竞速许可当成本人取消确认。

如果任何步骤发现 scope、repo、commit、R/W、分支、Bridge 入口、隔离能力或授权边界不一致，立即停止并报告精确差异，不自行修复扩大范围。
