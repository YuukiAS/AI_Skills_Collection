# slurm-workflows — Long-Term TODO

Maintenance inbox for the standalone `slurm-workflows` skill.

This skill is not one of the central Marketplace plugins, so its real-use failures should not be forced into an unrelated plugin TODO. This file stays under `docs/` so maintenance history is not shipped as ordinary skill runtime payload. For new real-project feedback, follow the same evidence-first `status: NEW` discipline described in `docs/plugin-todos/README.md`: record the failure and current evidence first; do not pre-decide the implementation architecture or release.

## Open candidates

No open candidates.

## Recently promoted

### 受保护作业取消必须取得本人当次确认
status: PROMOTED
source: 2026-10-12/13 用户报告真实 H100 interactive allocation 在长 Codex Goal 中被未经本人独立确认的清理操作取消；2026-10-19 已唯一定位当前候选漏拦根因为 Hook 启动 Python 的动态库环境失配导致进程退出 127，而 nested Bash PreToolUse 本身已真实触发。
evidence: docs/design/slurm-workflows/SLURM_PROTECTED_CANCEL_PORTABLE_RUNTIME_PROPOSAL_V3_2026-10-19.md；docs/design/slurm-workflows/SLURM_PROTECTED_CANCEL_PORTABLE_RUNTIME_EXECUTION_PLAN_V3_2026-10-19.md；docs/goals/hpc--slurm-cancel-production-closure-goal-v3.md；docs/design/slurm-workflows/SLURM_PROTECTED_CANCEL_PORTABLE_RUNTIME_KICKOFF_DRAFT_V3_2026-10-19.md；历史失败候选 work/hpc--slurm-protected-partition-chat-confirmation-v2-1@1b8df2c1f2b93de1605d571f5125cd4aaa99fd20 仅作选择性移植/回归来源。
problem:
- 受保护作业的取消必须在 Codex 正常执行边界取得当前根交互线程中用户对 exact Job 的当次确认；旧任务许可、竞速授权、自动批准或历史确认不能替代。
- 当前已确认 user-level Hook 是正确强制边界，但安装器把安装时 sys.executable 直接冻结为生产 Hook Python；当 app-server 环境无法启动该解释器时，Codex 会把普通 Hook process failure 当作非阻断并继续执行原 Bash。正式修复必须同时解决可移植 runtime 资格验证和 Hook 基础设施故障时的 fail-closed 行为。
project-specific context: Longleaf 的 htzhulab 是机器私有策略，不得写入公共 Skill；公共实现不得使用 scancel wrapper、PATH interception、Direct-mode override 或 Codex patch。当前默认分支检索未发现 DII/CARE 活跃生产源码直接执行 scancel，故 v3 默认两者 NO CHANGE。
current behavior: Repository 5.5.2 / slurm-workflows 0.5 正式发布于 f4517798a73adf29d3484306d60845488739f1fc。受保护取消在当前根聊天显示原生双选卡；保留零 reservation/零修改，确认经 exact re-resolution 与 durable one-shot reservation 后最多调用一次。无关 Bash 在 mutable runtime 验证前放行，stale loaded threads 通过正常 reload 恢复。中央 Plugin、Bridge Kit、DII、CARE 不变。
promotion gate: CLOSED — 最终 CI 39639471530 全四项 job 与 406 repository tests PASS，独立实现及正式 source/install identity 复核 PASS，G5=PASS，当前 Longleaf Codex USERS consumer 正式安装验证 PASS。修订 G4 保留 LIVE_JOB_RETAIN_TEST=WAIVED_BY_CURRENT_USER、KEEP_TEST=NOT_RUN；harmless native retain mapping、确定性 retain integration 和两次历史 live confirm PASS，不伪造真实 held-Job retain。最终证据 results/hpc--slurm-cancel-production-closure/FINAL_RELEASE_CLOSURE.md。禁止继续创建、查询或操作验收 Job。
next action: None; formal release and the required current-consumer installation are verified.
tracking: #109
current evidence: results/hpc--slurm-cancel-production-closure/REVISED_G4_ACCEPTANCE.md；results/hpc--slurm-cancel-production-closure/INDEPENDENT_FINAL_REVIEW.md；冻结 runtime 3e81802ab0251d3bf31ec2d808d4e3273505b2f6。

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
