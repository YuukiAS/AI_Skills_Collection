# Slurm protected-partition chat confirmation — Kickoff Draft v2

状态：
EXECUTION_PACKAGE / EFFECTIVE_ONLY_AFTER_CRITIC_PASS_AND_USER_SEND / PHASE_0_TO_3_ONLY

Critic PASS 本身不执行任何动作。只有独立 Critic 对最终 package commit 给出 PASS，并且用户本人随后实际发送本 Kickoff，才授权下面的 Phase 0–3。

本 Kickoff 不授权 production deployment，也不授权任何真实 Slurm mutation。

Task：
hpc--slurm-cancel-production-closure

先读取并严格服从：

- docs/design/slurm-workflows/SLURM_PROTECTED_PARTITION_CHAT_CONFIRMATION_PROPOSAL_V2_2026-10-18.md
- docs/design/slurm-workflows/SLURM_PROTECTED_PARTITION_CHAT_CONFIRMATION_EXECUTION_PLAN_V2_2026-10-18.md
- docs/goals/hpc--slurm-protected-partition-chat-confirmation-goal-v2.md
- 三个目标仓库各自 AGENTS.md

approved Proposal blob 必须仍为：
bc62264c6010b3e5371885899138f72c03095250

AI Skills origin/main 必须精确等于 execution-ready Critic 返回的 APPROVED_COMMIT。否则停止。

冻结执行身份：

AI_Skills_Collection
R=/overflow/htzhu/mingcheng_new/AI_Skills_Collection
branch=work/hpc--slurm-protected-partition-chat-confirmation
W=/overflow/htzhu/mingcheng_new/AI_Skills_Collection-hpc--slurm-protected-partition-chat-confirmation

DII
source=747829b957b19e8fcffa6bd5f1bb7ae62ae11f6f
R=/users/a/e/aereinh/Distributed_Imaging_Inference
branch=work/hpc--slurm-protected-partition-chat-confirmation
W=/users/a/e/aereinh/Distributed_Imaging_Inference-hpc--slurm-protected-partition-chat-confirmation

CARE
source=75a40e454de43b64e59a0b0b438ff57ef2bb8345
R=/users/a/e/aereinh/CARE
branch=work/hpc--slurm-protected-partition-chat-confirmation
W=/users/a/e/aereinh/CARE-hpc--slurm-protected-partition-chat-confirmation

被否决 package：
4d940d7510e29f74a14c5b5070a1a9671f3f27e7

禁止复活其 Kickoff、terminal confirmer、old v1 implementation 或 old Phase-3 candidate。

## Phase 0 — capability probe first

1. 对三个 R 只读核实 repo/origin/clean/source/target branch/target W/remote branch。任何 drift、dirty、collision、lineage mismatch 停止对应 repo，整体不得继续声称 ready。
2. Phase 0 先只创建 AI Skills 的 exact branch/worktree；DII/CARE 在 probe PASS 前只做只读 preflight，不创建其 branch/worktree。不得创建其它 branch，不改 main，不 reset/clean/stash/rebase/force。
3. 在 AI Skills W 先只准备 harmless probe：
   - .codex/config.toml：仅启用 features.default_mode_request_user_input=true；
   - .codex/hooks.json：仅注册 PostToolUse matcher ^request_user_input$ 的 harmless probe logger；
   - probe logger 只写 results/hpc--slurm-cancel-production-closure/chat-confirmation-probe/，不得调用 Slurm、不得联网、不得写 confirmation state。
4. readback 证明：
   - W 是 trusted project；
   - effective feature origin 来自 Project layer；
   - Bridge user-level default_mode_request_user_input=false 没有被修改；
   - probe hook 来源是 W。
5. 使用 fresh Longleaf Codex Desktop interactive root chat，cwd/root 为 AI Skills W，运行 harmless native request_user_input 测试。
6. 必须验证：
   - Default mode request_user_input 真正出现；
   - Desktop UI 显示问题；
   - 用户显式“确认测试”后 dedicated response 返回；
   - PostToolUse logger 收到 matching tool_input/tool_response/session_id/turn_id/tool_use_id；
   - 另一轮不回答直到 auto-resolution，得到 empty answers；
   - empty answers 不算确认。
7. 如果当前 Executor 无法自己创建并向用户展示这个 fresh Desktop chat，停止在：
   PROBE_READY_FOR_USER_CHAT
   只要求用户在 Longleaf_Codex 打开 exact W 的一个新聊天并发送 harmless probe prompt。不得要求用户打开 terminal。
8. 无 Slurm 地确认 codex exec 不支持该交互；记录：
   HEADLESS_PROTECTED_CANCEL=NEEDS_INTERACTIVE_CHAT_CONFIRMATION
9. Phase 0 任一失败：立即停止回 Planner。不得 fallback terminal confirmer、UserPromptSubmit、MCP server、auto_review、approval prompt 或修改 user-level CODEX_HOME config。

只有 Phase 0 PASS 才继续。

## Phase 1 — product candidate

Phase 0 PASS 后，才创建 DII/CARE 冻结的 exact branch/worktree。

AI Skills：

- 实现 thin ai-slurm-scancel guard；
- private field 只有 protected_cancel_partitions；
- protected first attempt 零 mutation；
- short-lived hidden pending record；
- native request_user_input question contract；
- tiny synchronous PostToolUse binder；
- binder 只接受 exact canonical “确认取消”；
- binder 自己绝不执行 Slurm mutation；
- ordinary Codex normal shell 即使知道 question id、state path、record format，也不能通过直接 binder invocation、直接改写 state 或伪造 question/answer artifact 产生 guard 可接受的 confirmed authority；该 anti-forgery regression 不通过就停止回 Planner；
- automation-only scancel shim；
- project-local .codex/config.toml / hooks.json / rules/slurm-protected-cancel.rules candidate；
- raw scancel、/usr/bin/scancel、direct binder 在 Codex normal entry forbidden；
- guard 不 blanket allow。

不得实现 terminal ai-slurm-confirm-cancel、H100/current-run/old three-state/MCP server/database/daemon/broker。

DII：

- 只同步/使用 exact central candidate；
- project-local feature/hook/rules adapter；
- 必要 automation PATH / launcher integration；
- 不复制 partition/nonce/question/answer policy。

CARE：

只做冻结的 chat-return transport 修复：

- B1：scancel nonzero 不加入 cancelled，传播 nonzero/guard output 后结束当前 cancellation attempt；
- M7：nonzero 直接传播；
- M8：nonzero 直接传播；
- interactive takeover：nonzero 不进入 CANCELLED accounting / launch，直接传播；
- cascade formal race：cancel nonzero 后结束当前 watcher round并传播，不能内部 interval loop 吞掉 blocker。

non-protected returncode 0 的原状态机保持。

interactive root Codex 收到 NEEDS_INTERACTIVE_CHAT_CONFIRMATION 后调用 native request_user_input；用户确认后 resume/rerun ordinary cancellation intent。

## Phase 2 — validation

先跑 deterministic tests。

任何会实际调用 fake scancel / subprocess destructive path 的测试，只能在真正隔离 fake Slurm 环境：

- network disabled
- isolated PID namespace
- no production SSH key/agent/token
- no real Slurm/MUNGE/controller/socket
- no host control socket
- no production writable mount
- fake Slurm only

不能证明隔离：
BLOCKED_BY_ISOLATION

不得转真实 Longleaf mutation。

完成并冻结 Gate A-D evidence：

Gate A：partition routing
Gate B：native fresh chat confirmation
Gate C：consumer/runtime coverage
Gate D：target integrity / claim truth

不得新增 Gate E。

## Phase 3 — candidate publication and Reviewer handoff

冻结 AI Skills / DII / CARE exact candidate commits。

每个 exact task branch 最多允许一次普通、非强制、同名 first publication：

git push --set-upstream origin work/hpc--slurm-protected-partition-chat-confirmation

仅在：
- exact repo/origin/branch/lineage/clean；
- 同名 remote branch 不存在

时允许。

禁止：
- 其它 branch/remote
- force / force-with-lease
- delete/tag
- history rewrite

首次发布后，后续同 branch publication 只能走已有 bounded current-branch publisher。

发布后立即停止，输出：

- 三仓 exact candidate commit；
- Phase 0 live probe evidence；
- Gate A-D evidence；
- isolation status；
- project-local config/hook/rules candidate；
- private protected_cancel_partitions candidate；
- automation PATH evidence；
- rollback；
- independent Reviewer prompt。

## 本 Kickoff 永久不授权

- 写 user-level $CODEX_HOME/config.toml
- 修改 Bridge Kit source
- 修改 ai-bridge-global.rules
- user-level production hooks
- production AI Skills install
- production private protected_cancel_partitions
- production automation PATH
- AI Skills/DII/CARE main integration
- release/version bump
- real sbatch/salloc/srun/scancel
- mutating scontrol
- signal/requeue/release
- kill allocation holder
- any real htzhulab/H100/other job cancellation test
- test allocation
- paid model/API
- daemon/database/broker
- MCP server
- fifth Capability Gate

Phase 3 independent Reviewer PASS 后仍不能自动部署。

production activation 必须等用户第二条短、独立、绑定 exact reviewed commits 的授权。
