# Slurm protected-partition chat confirmation — Kickoff Draft v2.1

状态：
EXECUTION_PACKAGE / EFFECTIVE_ONLY_AFTER_CRITIC_PASS_AND_USER_SEND / PHASE_0_TO_3_ONLY

Critic PASS 本身不执行任何动作。只有独立 Critic 对最终 v2.1 package commit 给出 PASS，并且用户本人随后实际发送本 Kickoff，才授权 Phase 0–3。

本 Kickoff 不授权 production activation，也不授权任何真实 Slurm mutation。

Phase 0–3 唯一允许的 user-level `$CODEX_HOME/config.toml` 副作用是：**用户本人通过官方 Codex Hook trust UI**，为本 task 已冻结的 exact Hook key/current_hash 写入对应 `hooks.state.<key>.trusted_hash`。Executor 不得直接编辑 user config，不得修改其它 user-level 字段。

Task：
hpc--slurm-cancel-production-closure

必须先读取并严格服从：

- docs/design/slurm-workflows/SLURM_PROTECTED_PARTITION_CHAT_CONFIRMATION_PROPOSAL_V2_1_2026-10-18.md
- docs/design/slurm-workflows/SLURM_PROTECTED_PARTITION_CHAT_CONFIRMATION_EXECUTION_PLAN_V2_1_2026-10-18.md
- docs/goals/hpc--slurm-protected-partition-chat-confirmation-goal-v2_1.md
- 三个目标 repo 的 AGENTS.md

approved Proposal blob 必须仍为：

26760ae8bb0a19809f1048436fa14aba0bb4e49a

AI Skills execution base 必须精确等于 execution-ready Critic 返回的 APPROVED_COMMIT。不得吸收未审 main 变化。

冻结 execution identities：

AI_Skills_Collection
R=/overflow/htzhu/mingcheng_new/AI_Skills_Collection
branch=work/hpc--slurm-protected-partition-chat-confirmation-v2-1
W=/overflow/htzhu/mingcheng_new/AI_Skills_Collection-hpc--slurm-protected-partition-chat-confirmation-v2-1

DII
source=747829b957b19e8fcffa6bd5f1bb7ae62ae11f6f
R=/users/a/e/aereinh/Distributed_Imaging_Inference
branch=work/hpc--slurm-protected-partition-chat-confirmation-v2-1
W=/users/a/e/aereinh/Distributed_Imaging_Inference-hpc--slurm-protected-partition-chat-confirmation-v2-1

CARE
source=75a40e454de43b64e59a0b0b438ff57ef2bb8345
R=/users/a/e/aereinh/CARE
branch=work/hpc--slurm-protected-partition-chat-confirmation-v2-1
W=/users/a/e/aereinh/CARE-hpc--slurm-protected-partition-chat-confirmation-v2-1

永久拒绝：
- 4d940d7510e29f74a14c5b5070a1a9671f3f27e7
- 38a76797439c6b29098aade7539270cbc51e8836
- ER-V2-01 未关闭期间形成的旧 execution drafts
- terminal confirmer
- persisted confirmed token / next-shell consume semantics

## Phase 0 — capability + authority probe first

1. 对 AI Skills/DII/CARE 三个 R 做只读 preflight：
   repo/origin/clean/source/target branch/target W/remote branch。
   任一 source drift、dirty、collision 或 lineage mismatch 必须 fail closed。

2. 先只创建 AI Skills exact v2.1 branch/worktree。
   DII/CARE 在 Phase 0 PASS 前不创建 worktree。

3. 在 AI Skills W 准备 harmless project-local probe：
   - trusted project .codex/config.toml
   - default_mode_request_user_input=true
   - locked profile extends=:workspace
   - project .codex explicit deny
   - harmless SessionStart Hook
   - harmless PostToolUse matcher ^request_user_input$
   - fake private binder/capability/runtime/consumed area
   - probe results under:
     results/hpc--slurm-cancel-production-closure/chat-confirmation-v2-1-probe/

4. Phase 0 不得调用任何 Slurm command，包括 read-only Slurm。
   它只验证 Codex chat / Hook / permission / anti-tamper primitive。

5. 在任何 Hook trust 动作前冻结并记录：
   - current Codex identity / CODEX_HOME locator
   - exact project root / task branch
   - exact Hook source
   - exact stable Hook key
   - exact current_hash
   - trust status
   - pre-trust exact hooks.state key state（通过正式 readback，可取得则记录旧 hash）

6. 如果 Desktop 要求 Hook trust：
   - 只允许用户本人通过官方 Codex Hook trust UI trust上述 exact key/current_hash；
   - 不允许 Executor 直接编辑 `$CODEX_HOME/config.toml`；
   - 不允许 Executor 直接调用通用 config writer伪造 trust；
   - 用户 UI trust 后必须用 `hooks/list` + 正式 config readback证明：
     - exact Hook status=Trusted
     - exact trusted_hash == frozen current_hash
     - 本 task 未直接修改其它 user config 字段。

   这一步是真实 user-level config side effect，已由本 Kickoff 明确授权。

7. 使用 fresh Longleaf Codex Desktop interactive root chat on exact AI Skills W 验证：
   - native request_user_input 在 Default mode 实际可用
   - UI 显示 harmless question
   - 用户显式“确认测试”返回 dedicated response
   - PostToolUse 收到 matching tool_input/tool_response/session_id/turn_id/tool_use_id
   - 第二轮不回答得到 empty answers
   - empty answers不触发任何authority action

8. 如果 Executor 无法自行创建并展示 fresh Desktop chat，停止于：

   PROBE_READY_FOR_USER_CHAT

   只要求用户：
   - 在 Longleaf_Codex 打开 exact W 的新 chat
   - 若显示 Hook trust，只 trust evidence 中 exact key + current_hash 完全匹配的 probe Hooks
   - 发送 harmless probe prompt
   - 完成一次“确认测试”，另一次不回答

   不要求用户打开 terminal。

9. authority-boundary probe必须证明：
   - trusted Host Hook可访问 fake private area
   - ordinary shell/Python/apply_patch/absolute/symlink path均被 explicit .codex deny
   - auto_review-approved escalation仍不能访问 private area
   - direct fake binder invocation/fabricated JSON无authority
   - Modified Hook不会按原 Trusted Hook执行
   - bypass_hook_trust=false
   - fake private binder digest mismatch => no execution
   - model-controlled PATH 中伪造 scontrol/scancel 不影响 runtime.json frozen absolute-path resolution

10. Hook trust retention / rollback：
    - exact probe/candidate Hook trust record可以保留到 Phase 3 Reviewer package冻结，以支持同task replay；
    - Hook声明删除/改变后，旧trusted_hash只能作为 inert stale record，不能trust新hash；
    - cleanup/revoke只使用Codex官方Hook trust管理入口；
    - 如果当前官方UI没有revoke/remove，禁止手工编辑user config，记录：
      HOOK_TRUST_RETENTION=INERT_RECORD
      + exact key/hash + reason；
    - 不得声称未发生user-level side effect或已删除实际上仍保留的record。

11. should-not-change regression必须证明：
    - git status --short 正常
    - read-only git diff/rev-parse/remote identity正常
    - representative normal AI Skills tests正常

    如果 full .codex deny造成真实正常入口退化：
    STOP -> Planner。
    Executor不得自行缩窄deny。

12. 无 Slurm地确认：
    HEADLESS_PROTECTED_CANCEL=NEEDS_INTERACTIVE_CHAT_CONFIRMATION

13. Phase 0 任一关键项 FAIL：
    立即 STOP -> Planner。
    不得 fallback terminal confirmer、UserPromptSubmit、auto_review、approval prompt、MCP、daemon/database/broker 或 Bridge global config。

只有 Phase 0 PASS 才继续。

## Phase 1 — product candidate

14. Phase 0 PASS 后才创建 DII/CARE exact v2.1 branch/worktree。

15. AI Skills 实现 exact Proposal v2.1：
    - thin central guard
    - protected_cancel_partitions
    - reviewed binder source
    - candidate/setup tooling
    - private authority root:
      .codex/slurm-protected-cancel-private/
    - private runtime binder only at:
      .codex/slurm-protected-cancel-private/bin/slurm-protected-cancel-binder
    - capability.key
    - runtime.json
    - consumed/
    - trusted SessionStart capability Hook
    - synchronous PostToolUse exact execution Hook
    - project config/hooks/rules
    - automation-only scancel shim

16. Hook declaration必须冻结：
    - canonical absolute private binder path
    - exact reviewed binder SHA-256
    - invocation shape

    Host Hook执行binder前必须使用 trusted absolute hashing executable验证digest。
    mismatch => no binder / no Slurm。

17. runtime.json必须冻结并验证：
    - canonical project root
    - binder SHA-256
    - canonical absolute scontrol
    - canonical absolute scancel

    binder禁止PATH lookup、alias、function或relative Slurm path。

18. ordinary Codex normal entry必须无法：
    - read/modify/execute/copy private binder
    - read capability
    - modify runtime.json
    - write/delete/reset consumed
    - modify locked hooks/config/rules
    - bypass via direct binder/copied binder/fabricated JSON
    - bypass via auto_review escalation

19. DII只做：
    - exact central candidate integration
    - project config/hooks/rules
    - automation PATH/launcher resolution
    - existing business cancellation intent

    不复制protected policy/authority logic。

20. CARE只做 chat-blocker transport：
    - B1 nonzero不加入cancelled，传播并结束当前attempt
    - M7 nonzero传播
    - M8 nonzero传播
    - interactive takeover nonzero不进CANCELLED wait、不launch，传播
    - cascade formal race cancel nonzero结束当前round并传播

    用户确认后Host Hook已经完成exact cancellation。
    watcher/controller resume只观察真实状态并继续原业务，不再发第二次scancel消费confirmation。

## Phase 2 — validation

21. 跑 deterministic tests：
    - config compile/origin
    - Hook discovery/trust
    - explicit deny
    - binder digest mismatch
    - trusted absolute executable binding
    - request schema/response classification
    - CARE blocker propagation
    - DII minimal integration
    - headless fail closed
    - git/status/test should-not-change

22. 任何会实际执行 fake scancel/subprocess destructive path 的验证，只能在真正隔离 fake Slurm 环境：

    - network disabled
    - isolated PID namespace
    - no production SSH key/agent/token
    - no real Slurm/MUNGE/controller/socket
    - no host control socket
    - no production writable mount
    - fake Slurm only

    不能证明隔离：
    BLOCKED_BY_ISOLATION

    不得改用真实 Longleaf。

23. 完整 Gate 只能有：
    Gate A：partition routing
    Gate B：native fresh chat confirmation + authority boundary
    Gate C：consumer/runtime coverage + should-not-change
    Gate D：target integrity / claim truth

    不得新增 Gate E。

24. 绝不执行真实：
    - sbatch
    - salloc
    - srun
    - scancel
    - mutating scontrol
    - signal/requeue/release
    - kill allocation holder
    - htzhulab/H100/其它 job cancellation test
    - test allocation

## Phase 3 — candidate publication and independent Reviewer handoff

25. 冻结 AI Skills/DII/CARE exact candidate commits和完整 evidence。

26. 使用 exact final candidate binder digest + exact reviewed setup generator，对三个 canonical production roots离线渲染 production Hook identities；不得写production文件、不得创建production private runtime material、不得激活production Hook。

canonical roots：

- AI Skills:
  /overflow/htzhu/mingcheng_new/AI_Skills_Collection
- DII:
  /users/a/e/aereinh/Distributed_Imaging_Inference
- CARE:
  /users/a/e/aereinh/CARE

每个production root必须冻结：

- exact candidate commit
- canonical production root
- canonical private binder absolute path
- final binder SHA-256
- exact production SessionStart Hook declaration
- exact production PostToolUse Hook declaration
- exact production stable Hook keys/current_hashes
- expected runtime.json canonical root/digest/trusted absolute Slurm binding
- production project config/rules declaration identity

candidate worktree Hook key/hash不得替代production Hook identity。

27. 每个 exact task branch最多允许一次普通、非强制、同名 first publication：

git push --set-upstream origin work/hpc--slurm-protected-partition-chat-confirmation-v2-1

仅在：
- exact repo/origin/branch/lineage/clean
- same-name remote branch不存在

时允许。

禁止其它 branch/remote、force/force-with-lease、delete/tag/history rewrite。

首次发布后，同分支后续 publication只能走已有 bounded current-branch publisher。

28. 发布后立即停止并输出：
    - 三仓 exact candidate commits
    - Phase 0 live Desktop/authority probe
    - Gate A-D evidence
    - isolation status
    - exact private binder SHA-256 / absolute path contract
    - candidate worktree exact Hook keys/current hashes/trust status
    - 三仓offline production-rendered Hook declarations/stable keys/current hashes/canonical roots/private binder paths/binder digests
    - exact trusted absolute scontrol/scancel bindings
    - should-not-change regression
    - Hook trust user-level side-effect inventory / retained inert records
    - rollback
    - independent Reviewer prompt

Reviewer必须实际审production-rendered Hook identities。Phase 3不得拿candidate worktree Hook hash代替production hash。

## 本 Kickoff 不授权

- production activation
- production AI Skills install
- real protected_cancel_partitions write
- canonical repo project runtime activation
- production automation PATH
- main integration
- release/version bump
- Bridge source modification
- Executor直接编辑 user-level $CODEX_HOME/config.toml
- 除用户通过官方Hook trust UI为本task exact frozen key/current_hash写入hooks.state外的其它user-level config修改
- ai-bridge-global.rules
- user-level Hook declarations
- paid model/API
- any real Slurm mutation

Phase 3 independent Reviewer PASS 后仍不得自动部署。

production activation必须等用户第二条短、独立授权，并同时绑定：

- exact reviewed AI Skills/DII/CARE commits
- Reviewer冻结的三仓production Hook stable keys/current_hashes
- canonical roots
- private binder absolute paths + final binder digests

production setup真正写入canonical project files后，必须先用 hooks/list readback actual production current_hash并与Reviewer冻结值完全一致；不一致立即STOP，禁止trust。

只有完全一致时，用户才可通过官方 Codex Hook trust UI trust这些 exact production hashes。该UI trust write是production阶段唯一允许的user-level hooks.state config副作用；Executor不得直接写user config。
