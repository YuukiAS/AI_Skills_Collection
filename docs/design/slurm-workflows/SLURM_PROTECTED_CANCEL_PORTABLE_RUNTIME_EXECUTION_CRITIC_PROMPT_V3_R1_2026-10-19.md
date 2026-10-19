# Slurm protected cancel portable runtime — execution-ready Critic 复核提示词 v3 R1

你现在担任 AI Research Stack 的独立 Critic，复核同一任务的 execution-ready 最小修订。

本轮只需要优先确认上一轮唯一 blocker
`ER-V3-01_WORKTREE_LOCATOR_CONFLICTS_WITH_CURRENT_BRIDGE_BOOTSTRAP`
已经关闭，并确认 locator 修订没有改变已通过的 Proposal v3 架构、G1–G5 或授权边界。

不要实施，不要修改仓库，不要创建 branch/worktree，不要修改 live `CODEX_HOME`，不要运行 Slurm，不要创建测试 Job，不要修改 Bridge Kit。

## Active Review Context

- target_repo: `YuukiAS/AI_Skills_Collection`
- target_plugin_or_domain: standalone Skill / HPC / `slurm-workflows`
- design_topic_or_task_key: `hpc--slurm-cancel-production-closure`
- review_stage: `EXECUTION_READY_REVIEW_V3_R1`
- revised package commit: `e84be726d6a7aaefe62d27c7fd2a0410e7f1498b`
- prior reviewed package: `352ff4d02bb41dd89d9335008910880d030de21e`
- prior formal Critic contract:
  `docs/design/slurm-workflows/SLURM_PROTECTED_CANCEL_PORTABLE_RUNTIME_EXECUTION_CRITIC_PROMPT_V3_2026-10-19.md@63f5ede7ab1f4b7c7bcefbaa38a7328267258ae7`
- previous decision: `REVISE`
- stable blocker: `ER-V3-01_WORKTREE_LOCATOR_CONFLICTS_WITH_CURRENT_BRIDGE_BOOTSTRAP`

## 本轮审查对象

在 exact revised package commit
`e84be726d6a7aaefe62d27c7fd2a0410e7f1498b`
读取：

1. Proposal v3：
   `docs/design/slurm-workflows/SLURM_PROTECTED_CANCEL_PORTABLE_RUNTIME_PROPOSAL_V3_2026-10-19.md`
2. Execution Plan v3：
   `docs/design/slurm-workflows/SLURM_PROTECTED_CANCEL_PORTABLE_RUNTIME_EXECUTION_PLAN_V3_2026-10-19.md`
3. Canonical Goal v3：
   `docs/goals/hpc--slurm-cancel-production-closure-goal-v3.md`
4. Kickoff Draft v3：
   `docs/design/slurm-workflows/SLURM_PROTECTED_CANCEL_PORTABLE_RUNTIME_KICKOFF_DRAFT_V3_2026-10-19.md`

Proposal v3 没有冻结错误 worktree locator，因此本轮应保持其架构正文不变。

## 强制读取

先实际读取最新 `YuukiAS/AI_Skills_Collection/main`：

- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md`
- `AGENTS.md`

再读取最新 `YuukiAS/GPT_Codex_AI_Bridge_Kit/main`：

- `AGENTS.md`
- `docs/V0_5_REVIEWED_HANDOFF_IMPLEMENTATION_SPEC.md`
- `ai_bridge_kit/reviewed_handoff.py`

当前 Planner 复核时，Bridge main 为
`bc94e41f44bd5b534d8ab8caa304114b8bf90685`。

必须亲自确认当前源码中：

```text
_repo_local_bootstrap_worktree(target, task_key)
= target.resolve().parent / f"{target.resolve().name}-{task_key}"
```

以及 brand-new `task bootstrap` 的实际首启逻辑确实调用该派生规则，不能通过 consumer package 任意指定另一个 worktree locator。

## ER-V3-01 最小关闭条件

当前冻结：

```text
R =
/overflow/htzhu/mingcheng_new/AI_Skills_Collection

task_key =
hpc--slurm-cancel-production-closure

branch =
reviewed/hpc--slurm-cancel-production-closure
```

因此当前 Bridge 正常首启派生的唯一 W 必须是：

```text
/overflow/htzhu/mingcheng_new/AI_Skills_Collection-hpc--slurm-cancel-production-closure
```

请确认 revised package 中：

- Execution Plan v3 的 W 已改成上述路径；
- Canonical Goal v3 的 W 已改成上述路径；
- Kickoff Draft v3 的 W 已改成上述路径；
- 四件套不存在旧的
  `/overflow/htzhu/mingcheng_new/AI_Skills_Collection-hpc--slurm-cancel-production-closure-v3`；
- branch 仍是
  `reviewed/hpc--slurm-cancel-production-closure`；
- task key 仍是
  `hpc--slurm-cancel-production-closure`；
- 仍要求使用当前 Bridge Reviewed Handoff 正常入口；
- 没有增加 raw Git fallback、替代 worktree、自定义 Bridge 参数或 Bridge Kit 修改。

## 必须确认没有语义漂移

除 W locator 外，本轮不允许把上一轮已审对象改成另一个方案。

优先比较 prior package
`352ff4d02bb41dd89d9335008910880d030de21e`
与 revised package
`e84be726d6a7aaefe62d27c7fd2a0410e7f1498b`
的四个审查文件。

应保持不变：

- user-level global Hook 是唯一 protected-cancel 强制边界；
- `config.toml` 内联层是 fail-closed root；
- trusted declaration 绑定外部 supervisor 的预期内容身份；
- Python / Hook / runtime / `scontrol` / `scancel` 在最终 sanitized minimal environment 中激活前完成资格验证；
- Gate 2 包含真实 Codex Hook 正常入口故障注入，并证明合法 deny + underlying Bash launch count = 0；
- PostToolUse reservation 先于任何可能的 protected `scancel` invocation；
- ambiguous outcome 不自动 retry，只做 read-only scheduler reconciliation；
- `slurm_routing.py` 默认 NO CHANGE；
- DII / CARE 默认 NO CHANGE；
- exactly one CPU-only、future-BeginTime、`htzhulab` 测试 Job；
- 只能取消该 task 自己创建的 exact Job；
- 不使用 wrapper、PATH interception、Direct mode、Codex patch、daemon、database；
- Capability Gate 仍且只为 G1–G5；
- repository / Skill version 策略保持原 v3；
- normal non-force release closure 保持原 v3；
- maintenance board pending mutation 语义保持不变，不要求用户手工维护。

## 本轮判定

只允许：

`PASS`

或

`REVISE`

### PASS

如果 ER-V3-01 已关闭，且 locator 修订没有改变原 v3 产品/安全/授权语义，则必须 PASS，不得重新打开已经关闭的问题或移动终点。

PASS 必须明确：

- reviewed object = v3 revised package
  `e84be726d6a7aaefe62d27c7fd2a0410e7f1498b`；
- `ER-V3-01_WORKTREE_LOCATOR_CONFLICTS_WITH_CURRENT_BRIDGE_BOOTSTRAP=CLOSED`；
- exact execution identity：
  - R = `/overflow/htzhu/mingcheng_new/AI_Skills_Collection`
  - branch = `reviewed/hpc--slurm-cancel-production-closure`
  - W = `/overflow/htzhu/mingcheng_new/AI_Skills_Collection-hpc--slurm-cancel-production-closure`
  - task key = `hpc--slurm-cancel-production-closure`
- G1–G5 继续批准；
- bounded authorization envelope 继续批准；
- `READY_FOR_CODEX=YES`；
- PASS 本身不代表用户已经授权 live `CODEX_HOME` mutation、真实 Slurm Job 或正式发布。

然后按最新 Critic Role Contract 直接生成简短、可发送给 Codex 的用户 handoff，不要把 Kickoff Draft 全文复制给用户。

该 handoff 必须引用：

- Proposal path；
- Execution Plan path；
- Goal path；
- Kickoff path；
- approved commit = `e84be726d6a7aaefe62d27c7fd2a0410e7f1498b`；

并显式写清用户发送该 handoff 后才授权的高影响边界：

- exact branch/worktree；
- 仅 protected-cancel 范围的 Longleaf `CODEX_HOME` 修改和可恢复备份；
- exactly one CPU-only、future-BeginTime、`htzhulab` 测试 Job；
- 只能取消该 task 创建的 exact Job；
- G1–G5 和独立 implementation review 通过后，才允许正常非强制 release closure。

### REVISE

只有发现新的、直接由本轮 locator 修订造成或暴露的真实执行 blocker 才能 REVISE。

不要重新阻塞：

- Code Mode；
- Hook matcher/trust；
- Python 动态库根因调查；
- wrapper vs Hook 架构；
- G1–G5 数量；
- DII/CARE 无新证据情况下的适配；
- OS-level same-UID isolation；
- maintenance board 当前无 Project mutation surface。

若 REVISE，必须给稳定 blocker id、实际失败原因、最小修订和关闭证据，并按最新 Critic Role Contract 自动生成完整下一条 Planner prompt。
