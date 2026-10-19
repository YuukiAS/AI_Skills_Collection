# slurm-workflows — Long-Term TODO

Maintenance inbox for the standalone `slurm-workflows` skill.

This skill is not one of the central Marketplace plugins, so its real-use failures should not be forced into an unrelated plugin TODO. This file stays under `docs/` so maintenance history is not shipped as ordinary skill runtime payload. For new real-project feedback, follow the same evidence-first `status: NEW` discipline described in `docs/plugin-todos/README.md`: record the failure and current evidence first; do not pre-decide the implementation architecture or release.

## Open candidates


### 受保护作业取消必须取得本人当次确认
status: NEW
source: 2026-10-12/13 用户报告真实 H100 interactive allocation 在长 Codex Goal 中被未经本人独立确认的清理操作取消；2026-10-19 已唯一定位当前候选漏拦根因为 Hook 启动 Python 的动态库环境失配导致进程退出 127，而 nested Bash PreToolUse 本身已真实触发。
evidence: docs/design/slurm-workflows/SLURM_PROTECTED_CANCEL_PORTABLE_RUNTIME_PROPOSAL_V3_2026-10-19.md；docs/design/slurm-workflows/SLURM_PROTECTED_CANCEL_PORTABLE_RUNTIME_EXECUTION_PLAN_V3_2026-10-19.md；docs/goals/hpc--slurm-cancel-production-closure-goal-v3.md；docs/design/slurm-workflows/SLURM_PROTECTED_CANCEL_PORTABLE_RUNTIME_KICKOFF_DRAFT_V3_2026-10-19.md；历史失败候选 work/hpc--slurm-protected-partition-chat-confirmation-v2-1@1b8df2c1f2b93de1605d571f5125cd4aaa99fd20 仅作选择性移植/回归来源。
problem:
- 受保护作业的取消必须在 Codex 正常执行边界取得当前根交互线程中用户对 exact Job 的当次确认；旧任务许可、竞速授权、自动批准或历史确认不能替代。
- 当前已确认 user-level Hook 是正确强制边界，但安装器把安装时 sys.executable 直接冻结为生产 Hook Python；当 app-server 环境无法启动该解释器时，Codex 会把普通 Hook process failure 当作非阻断并继续执行原 Bash。正式修复必须同时解决可移植 runtime 资格验证和 Hook 基础设施故障时的 fail-closed 行为。
project-specific context: Longleaf 的 htzhulab 是机器私有策略，不得写入公共 Skill；公共实现不得使用 scancel wrapper、PATH interception、Direct-mode override 或 Codex patch。当前默认分支检索未发现 DII/CARE 活跃生产源码直接执行 scancel，故 v3 默认两者 NO CHANGE。
next action: Proposal v3 已获独立 Critic 设计 PASS；v3 Proposal/Execution Plan/Goal/Kickoff 已写入 main，下一步只做同版 execution-ready Critic review。只有该 review 给 READY_FOR_CODEX=YES 且用户随后发送批准 handoff，才进入实现。
tracking issue: PENDING_CLEAR_WRITING_AND_PROJECT_MUTATION — 当前 Planner surface 不能同时满足 reader-facing Issue 创建前的真实 Clear Writing 调用与 GitHub Project mutation。下一具两项能力的维护入口应为同一 task 创建/绑定一个 maintenance-track Issue，分类 kind:new-capability / scope:standalone-skill / area:standalone-skill，Project Status=DOING、Area=standalone-skill，并回填 tracking: #实际编号；不复用已关闭 #96，不要求用户手工维护。


## Recently promoted

### Bounded duplicate-race opt-in when no site prohibition is known
status: PROMOTED
tracking: #96
source: Reviewed Handoff task `hpc--slurm-race-policy-bounded-opt-in`
evidence: `results/hpc--slurm-race-policy-bounded-opt-in/RESULT.md`; Final Critic PASS in `results/hpc--slurm-race-policy-bounded-opt-in/FINAL_CRITIC_REVIEW_R3_2026-10-04.md`; GitHub CI run `37187784359`; product candidate `5a3dc447da2ea429ba2d229b0301c378be9e8018`; central release closure evidence in `results/hpc--slurm-race-policy-bounded-opt-in/CENTRAL_RELEASE_CLOSURE_2026-10-04.md`
target layer: routing / policy / qa
problem:
- `slurm-workflows 0.3` required a site profile to explicitly allow duplicate race before a user/local opt-in could matter.
- That was too strict for missing, `UNKNOWN`, `disabled_by_default`, and `explicit_user_opt_in` policy states when no site prohibition is known and the user has explicitly opted in.
project-specific context: This entry is scoped to public standalone Slurm Workflows behavior and deterministic fake-Slurm/read-only evidence. It does not authorize real `sbatch`, `salloc`, `scancel`, duplicate GPU race execution, weekly GPU enrollment, DII installation/adaptation, Bridge Kit changes, or central plugin topology changes.
current behavior: Repository `5.4.4` formally ships standalone `slurm-workflows 0.4`. Duplicate race remains off by default; final race authorization requires explicit user/local opt-in, no explicit site prohibition, exactly two distinct candidate routes, full workload/scientific contract identity, hard resource compatibility, and a frozen safe winner/loser cancellation policy. Central Plugins remain `NO_BUMP`; Bridge Kit remains `NO CHANGE`; `REAL_SLURM_MUTATION = NO`.
promotion gate: CLOSED by product candidate `5a3dc447da2ea429ba2d229b0301c378be9e8018`, GitHub CI run `37187784359`, Final Critic PASS, and formal release commit `06d135d8a6ee62cd41abb40fc5771fcef7f8db25`. Issue #96 is CLOSED after DII consumer adaptation; its completed 0.4 scope does not close the separate protected-cancellation task.

### Slurm routing and capacity maintenance closure regression
status: PROMOTED
tracking: #95
source: Reviewed Handoff task `hpc--slurm-workflows-routing-refactor`
evidence: `results/hpc--slurm-workflows-routing-refactor/RESULT.md`; Final Critic PASS in `results/hpc--slurm-workflows-routing-refactor/FINAL_CRITIC_REVIEW_2026-10-03.md`; GitHub CI run `37131439668`; product candidate `9042c6eb210a519a03fcfa127d4d59cd8197ed78`; final integration/release closure evidence in `results/hpc--slurm-workflows-routing-refactor/INTEGRATION_RELEASE_CLOSURE_2026-10-03.md`
target layer: routing / qa / distribution
problem:
- The Slurm Workflows repair had to be restored and carried through final integration after main/release advanced beyond the original candidate assumptions.
- The final release preserves sticky state persistence, calendar-aware capacity lifecycle semantics, exact enrollment `scope_digest` fail-closed behavior, cleanup of obsolete race defaults, site-aware doctor requiredness, true installed G6 normal-entry coverage, and public-safe generated artifacts.
project-specific context: This entry is scoped to the public standalone `slurm-workflows` skill and deterministic fake-Slurm/read-only evidence. It does not authorize real Slurm mutation, real weekly GPU enrollment, Bridge Kit changes, central plugin topology changes, main integration, or release advancement.
current behavior: Repository `5.4.2` formally ships standalone `slurm-workflows 0.3`; `workflow-core` remains `0.5`; central Plugins remain `NO_BUMP`; Bridge Kit remains `NO CHANGE`. The reviewed product candidate passed PF5/G8, complete G1-G8, full local validation, generated parity, exact-SHA GitHub CI, and independent Final Critic review. `REAL_SLURM_MUTATION = NO`.
promotion gate: CLOSED by product candidate `9042c6eb210a519a03fcfa127d4d59cd8197ed78`, GitHub CI run `37131439668`, Final Critic PASS, and final integration/release closure.
