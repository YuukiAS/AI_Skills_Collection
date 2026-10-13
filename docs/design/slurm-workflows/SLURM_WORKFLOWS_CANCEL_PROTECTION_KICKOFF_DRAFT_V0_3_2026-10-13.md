# Slurm Workflows v0.3 — Kickoff Draft（ER-01/ER-02 修订，仍不可执行）

状态：DRAFT_NOT_AUTHORIZED / EXACT_WORKTREE_UNKNOWN / NO_CODEX_STARTED。设计方向 PASS 不代表 execution-ready PASS；本文件供独立 Critic 审查，**当前用户并未授权发送、执行本草案、运行 Codex、创建分支或访问任何服务器**。

目标仓库：YuukiAS/AI_Skills_Collection
任务键：hpc--slurm-cancel-human-confirmation
**唯一冻结执行分支**：reviewed/hpc--slurm-cancel-human-confirmation（尚未创建）
**执行工作树绝对路径**：尚未从实际 Codex 机器取证，严禁猜测。
设计与执行合同：
- docs/design/slurm-workflows/SLURM_WORKFLOWS_CANCEL_PROTECTION_PROPOSAL_V0_3_2026-10-13.md
- docs/design/slurm-workflows/SLURM_WORKFLOWS_CANCEL_PROTECTION_EXECUTION_PLAN_V0_3_2026-10-13.md
- docs/goals/hpc--slurm-cancel-human-confirmation-goal-draft-v0_3.md
已审原包提交为 6fcbde22b334e471736debfee4d1d86084e8b270；本次 ER 修订提交需以三份修订文件均发布后的准确 GitHub 提交绑定，不能沿用旧身份。

## 下一步只读定位交接草案（**尚未获用户授权**）

在用户以后明确选定的**既有 AI_Skills_Collection 工作目录**，只读核实 git 主仓库真实绝对路径、仓库和 origin 身份、当前分支/干净程度、工作树列表、同名分支碰撞、Bridge Kit 当前 CLI 入口和四份合同文件身份。将真实主仓库绝对路径 R 与 Bridge Kit 唯一派生的同级工作树 W = parent(R)/(basename(R) + "-hpc--slurm-cancel-human-confirmation") 及固定分支单独简短展示，等待用户针对确切 R/W/branch 同意。

**本交接不得进行 git fetch/pull/branch/worktree、安装、写入、远端发布、测试、模拟取消、真实 Slurm 查询或操作；不得自动继续。** 没有明确真实路径或存在碰撞/工作区不匹配时直接停止，不能由 Codex 改选目录。

## 实施 Kickoff 的形成条件（不在当前草案中冒充授权）

只有 R/W 经真实取证并由用户单独授权准确目标、初次分支/工作树建立及首次发布，且 execution-ready Critic 复核同版合同后，才能机械准备真正可发送的阶段 A Kickoff。初始化只准复用正式 ai-bridge reviewed-handoff task bootstrap（提交基线必须等于安全同步后 origin/main），首次元数据提交只包含本任务 REQUEST.md 与 CURRENT.json，再通过 ai-bridge reviewed-handoff task publish-first 将同名 reviewed 分支首次发布。不得调用 raw git worktree add/raw push/force，也不得将其他源码混进首次提交。实施工作中已存在任务分支的普通非强制发布仅限同一获授权分支和 Host Policy 受限入口。

阶段 A 若获后续独立批准，仅包括通用 slurm-workflows 源码和隔离离线测试、DII/CARE 只读消费清单以及既定 G1–G6 证据；不新增能力门。**危险模拟运行的绝对前提**：实际被测子进程具有经核实的操作系统隔离，不能访问任何真实 Slurm 控制/API/socket、生产 SSH 凭据/agent、真实远端网络/代理/隧道、宿主 PID/信号、salloc/tmux holder、生产路径或特权控制入口。没有同一进程层面的可核验证据就不运行模拟 scancel、远端调用、Python subprocess、数组批量取消或 holder 信号测试，改为静态/纯函数检查并报告对应部分未通过；单纯 PATH 假命令或 DRY_RUN 不算隔离。

**永久越界禁止：**任何真实 Slurm 提交/取消/释放/重排、H100 或 Longleaf htzhulab allocation 操作、服务器/SSH/凭据/权限变动、生产钩子部署、终止真实 holder、DII/CARE 代码修改、Bridge Kit 修改、付费实验、无人确认下的自动取消、强制发布及自行宣布已实现强制防护。不得从阶段 A 自动进入需要新权限的 B/C。

本文件的内容不应被复制给 Codex 作为已批准实施指令。若必须提供可执行 Kickoff，先冻结经证实的绝对 R/W 和最终文件提交，再接受下一轮独立 Critic 审查及用户针对准确范围的当次授权。
