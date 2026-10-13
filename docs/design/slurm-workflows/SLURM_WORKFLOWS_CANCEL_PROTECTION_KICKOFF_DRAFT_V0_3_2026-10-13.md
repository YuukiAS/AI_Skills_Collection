# Slurm Workflows v0.3 — Kickoff Draft（仅供 Critic 审查，严禁直接启动）

本文件目前状态：DRAFT_NOT_AUTHORIZED。v0.3 设计 PASS 不等于执行就绪 PASS；本文件尚未经过独立 Critic 审查，发送前还必须核对确切分支/工作树并取得用户明确授权。

以下为拟审查的简短 Codex 启动文字：

---

目标：YuukiAS/AI_Skills_Collection；任务 hpc--slurm-cancel-human-confirmation；建议独立分支 reviewed/hpc--slurm-cancel-human-confirmation（必须先按获批计划创建并核对）。

先阅读同版批准文件：
- docs/design/slurm-workflows/SLURM_WORKFLOWS_CANCEL_PROTECTION_PROPOSAL_V0_3_2026-10-13.md
- docs/design/slurm-workflows/SLURM_WORKFLOWS_CANCEL_PROTECTION_EXECUTION_PLAN_V0_3_2026-10-13.md
- docs/goals/hpc--slurm-cancel-human-confirmation-goal-draft-v0_3.md

本次**仅授权 Plan 阶段 A 的离线实现和假 Slurm 回归**。实现逐服务器用户指定分区与个人加速器保护的统一取消决策、默认拒绝、短本人请求、可选钩子提前拒绝；保留原有正常路由/查询/训练语义，输出 G1–G6 真实证据与 DII/CARE 只读消费入口清单。无法证明执行隔离时必须明确停止强制保护声明。

**绝对禁止：真实 Slurm 的提交/取消/释放/重排；任何 H100 或 htzhulab allocation 操作；远端部署、真实 SSH/凭据/权限修改、终止 salloc/tmux holder；DII/CARE 源码修改、Bridge Kit 修改、真实钩子安装和付费实验。不能靠长 Goal、竞速许可、自动审批替代真人取消确认。**

仅在隔离假 Slurm 和本仓库授权工作树运行离线测试；如需改变站点权限、消除共享 UID 绕过或启动真实探针，立即停止并返还 Planner，不能自作主张扩项。不得宣称 Longleaf 已启用强制保护或自批发版。

完成后提交任务范围内的代码、离线回归与完整结果供独立 Reviewer 检查；不因测试 PASS 自动集成发布。执行前按 Reviewed Handoff 与当前仓库规则确认准确 source、branch、权限和用户当次授权。

---

草案未获 execution-ready Critic PASS、未有实际用户随后发送经审同版启动指令前，以上文字没有执行权限，也不授权任何工具操作。
