# Slurm protected-partition fresh-confirmation — Kickoff Draft v1

状态：EXECUTION_PACKAGE / EFFECTIVE_ONLY_AFTER_CRITIC_PASS_AND_USER_SEND / PHASE_0_TO_3_ONLY

Critic PASS 本身不执行任何动作。只有独立 Critic 对最终 package commit 给出 PASS，并且用户本人随后实际发送本段，才授权以下 Phase 0–3 候选实现。本 Kickoff 始终不授权 production Host Policy/private config 部署，也不授权任何真实 Slurm mutation。

Task：
hpc--slurm-cancel-production-closure

execution-package revision base main：06648df4f2951766c257e19ee035e141a8a1ceb3
Repository version baseline：5.4.5

必须先读取：
- docs/design/slurm-workflows/SLURM_PROTECTED_PARTITION_FRESH_CONFIRMATION_PROPOSAL_V1_2026-10-17.md
- docs/design/slurm-workflows/SLURM_PROTECTED_PARTITION_FRESH_CONFIRMATION_EXECUTION_PLAN_V1_2026-10-17.md
- docs/goals/hpc--slurm-protected-partition-fresh-confirmation-goal-v1.md
- 各目标 repo 的 AGENTS.md

下一 execution-ready Critic 必须把 APPROVED_COMMIT 绑定到最终 package commit 本身。用户发送本段开始执行时，AI Skills origin/main 必须精确等于该 APPROVED_COMMIT；不等则立即停止。

冻结执行身份：

AI_Skills_Collection
R=/overflow/htzhu/mingcheng_new/AI_Skills_Collection
branch=work/hpc--slurm-protected-partition-fresh-confirmation
W=/overflow/htzhu/mingcheng_new/AI_Skills_Collection-hpc--slurm-protected-partition-fresh-confirmation

DII
source=747829b957b19e8fcffa6bd5f1bb7ae62ae11f6f
R=/users/a/e/aereinh/Distributed_Imaging_Inference
branch=work/hpc--slurm-protected-partition-fresh-confirmation
W=/users/a/e/aereinh/Distributed_Imaging_Inference-hpc--slurm-protected-partition-fresh-confirmation

CARE
source=75a40e454de43b64e59a0b0b438ff57ef2bb8345
R=/users/a/e/aereinh/CARE
branch=work/hpc--slurm-protected-partition-fresh-confirmation
W=/users/a/e/aereinh/CARE-hpc--slurm-protected-partition-fresh-confirmation

旧 work/hpc--slurm-cancel-production-closure 和旧三个 Phase 3 candidate 均为 rejected historical evidence，禁止复用、merge 或 cherry-pick 成新候选。

## 授权步骤

1. 对三个 R 做只读 preflight：repo/origin/clean/source/target branch/target W。任一不符只停止对应 repo，并且整体不能宣称完成。
2. 仅创建上面三个 exact work branch/worktree；不得创建其它 branch，不改 main，不 reset/clean/stash/rebase/force。
3. 在 AI Skills 中从当前 main 正常实现 Proposal v1：thin ai-slurm-scancel guard、protected_cancel_partitions、one-time challenge local files、independent shell confirmer（只确认不取消）、automation-only scancel shim、Gate A-D tests/evidence。不得继承 old ownership/H100/三态逻辑。
4. DII 只做 exact central candidate 安装/同步与必要 automation PATH / launcher resolution；不复制 protection logic。
5. CARE 只做 Plan 冻结的最小 adaptation：
   - B1：returncode 0 才加入 cancelled；
   - M7：returncode 0 才退出成功分支；
   - M8：code 0 才退出；
   - interactive takeover：returncode 0 才进入 CANCELLED accounting / launch；
   - cascade formal race：保留 interval re-entry，nonzero 不谎报成功；
   - 所有 normal automation bare scancel 必须实际解析到 reviewed shim。
6. production Codex rules 只生成/测试候选文件；不要写任何真实 CODEX_HOME。
7. PreToolUse 是 OPTIONAL_NOT_REQUIRED；不要为它扩大范围。
8. deterministic tests 先跑。需要实际调用 fake cancellation/subprocess mutation 的测试，只能在 Plan 定义的真正隔离 fake Slurm 环境运行；隔离不能证明就标 BLOCKED_BY_ISOLATION，不得改用 Longleaf。
9. 绝不执行真实 sbatch/salloc/srun/scancel、mutating scontrol、kill allocation holder、H100/htzhulab cancellation test，也不提交测试 job。
10. 冻结三仓 candidate commit 与 evidence。
11. 准备独立 Reviewer handoff 前，对每个 exact task branch 最多允许一次普通、非强制、同名首次远端发布并绑定 upstream：
   git push --set-upstream origin work/hpc--slurm-protected-partition-fresh-confirmation
   前提是 exact repo/origin/clean/lineage 正确且同名 remote branch 不存在。禁止其它 branch/remote、force/force-with-lease、delete、tag、history rewrite。首次成功后后续同分支发布只用已有 bounded current-branch publisher。
12. 发布 candidate 后立即停止，输出三仓 exact commit、Gate A-D evidence、isolation 状态、production rules/private-config candidate、rollback 和 Reviewer prompt。

## 永久禁止

本 Kickoff 不授权：
- 写 /users/a/e/aereinh/.codex 或 /overflow/htzhu/mingcheng_new/.codex 的 production rules；
- 写真实 ~/.config/ai-skills/local-overrides.toml；
- production AI Skills install；
- production automation PATH 改动；
- production Hook；
- DII/CARE main integration；
- slurm-workflows 0.5 / Repository version bump / release；
- Bridge Kit source 修改；
- daemon/database/broker；
- paid model/API；
- 任何真实 Slurm mutation。

候选必须停在 mandatory independent Reviewer。Reviewer PASS 后仍需要用户一条新的、短的 production authorization；不得从本 Kickoff 自动继续部署。
