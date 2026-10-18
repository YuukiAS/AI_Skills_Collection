# Slurm protected-partition chat confirmation — Kickoff Draft v2.1

状态：
EXECUTION_PACKAGE / EFFECTIVE_ONLY_AFTER_CRITIC_PASS_AND_USER_SEND / PHASE_0_TO_3_ONLY

Critic PASS 本身不执行任何动作。只有独立 Critic 对最终 recovered v2.1 package commit 给出 PASS，并且用户本人随后实际发送本 Kickoff，才授权 Phase 0–3。

本 Kickoff 不授权 production activation，也不授权任何真实 Slurm mutation。

本 recovery 只改变候选运行拓扑：

linked worktree
→ standalone Git clone

approved Proposal v2.1、authority boundary、Gate A-D、CARE/DII合同、Hook trust副作用、production Hook hash identity、version/release contract全部保持。

AI Skills candidate code source仍固定为：

c3879065c782f1b0a03107a927bb3176a8788d02

不得把之后的 AI_Skills_Collection main内容吸进candidate。

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

execution-ready Critic 的 APPROVED_COMMIT 只绑定本 recovery execution package 文档，不改变下面冻结的 candidate source commits。

## 冻结 canonical roots / candidate clones

AI_Skills_Collection

canonical R（只读）：
/overflow/htzhu/mingcheng_new/AI_Skills_Collection

candidate source：
c3879065c782f1b0a03107a927bb3176a8788d02

branch：
work/hpc--slurm-protected-partition-chat-confirmation-v2-1

standalone candidate clone C：
/overflow/htzhu/mingcheng_new/AI_Skills_Collection-hpc--slurm-protected-partition-chat-confirmation-v2-1-standalone-clone

旧 failed linked-worktree path：
/overflow/htzhu/mingcheng_new/AI_Skills_Collection-hpc--slurm-protected-partition-chat-confirmation-v2-1

DII

canonical R（只读）：
/users/a/e/aereinh/Distributed_Imaging_Inference

candidate source：
747829b957b19e8fcffa6bd5f1bb7ae62ae11f6f

branch：
work/hpc--slurm-protected-partition-chat-confirmation-v2-1

standalone candidate clone C：
/users/a/e/aereinh/Distributed_Imaging_Inference-hpc--slurm-protected-partition-chat-confirmation-v2-1-standalone-clone

旧 failed linked-worktree path：
/users/a/e/aereinh/Distributed_Imaging_Inference-hpc--slurm-protected-partition-chat-confirmation-v2-1

CARE

canonical R（只读）：
/users/a/e/aereinh/CARE

candidate source：
75a40e454de43b64e59a0b0b438ff57ef2bb8345

branch：
work/hpc--slurm-protected-partition-chat-confirmation-v2-1

standalone candidate clone C：
/users/a/e/aereinh/CARE-hpc--slurm-protected-partition-chat-confirmation-v2-1-standalone-clone

旧 failed linked-worktree path：
/users/a/e/aereinh/CARE-hpc--slurm-protected-partition-chat-confirmation-v2-1

三个旧 linked-worktree path：
- 不复用
- 不要求清理
- 不 reset/stash/clean
- 不作为本 task candidate runtime

三个 canonical R 在 Phase 0–3 完全只读。禁止：
- 写文件
- 写 canonical .codex
- checkout/switch
- stash
- reset
- clean
- restore
- worktree add/remove
- branch创建
- fetch/pull
- 其它会修改 canonical working tree 或 .git 的动作

允许只读：
- remote get-url
- rev-parse
- status --short
- AGENTS/规则/source读取
- pre-existing dirty状态记录

pre-existing dirty/其它checkout不清理、不接管。

永久拒绝：
- 4d940d7510e29f74a14c5b5070a1a9671f3f27e7
- 38a76797439c6b29098aade7539270cbc51e8836
- ER-V2-01未关闭期间旧execution drafts
- terminal confirmer
- persisted confirmed token / next-shell consume semantics

## Phase 0 — standalone AI Skills clone + capability recovery

1. 对三个 canonical R 做只读 preflight：
   - exact repo identity
   - origin URL
   - current status只记录
   - frozen source commit可在remote定位
   - target standalone clone C path不存在
   - same-name remote branch不存在

   canonical dirty不是清理理由；不得修改R。

2. 只创建 AI Skills standalone clone C：
   - 从canonical R只读得到exact origin URL；
   - clone到冻结C path；
   - C创建前必须不存在；
   - clone后只在C内操作Git；
   - candidate branch必须从exact source
     c3879065c782f1b0a03107a927bb3176a8788d02
     创建；
   - 不得把clone默认remote main的新内容merge/rebase/cherry-pick进candidate。

3. 必须证明 C 是独立 standalone checkout：
   - `C/.git` 是该clone自己的Git目录，不是linked-worktree gitfile；
   - `git -C C rev-parse --show-toplevel` 精确等于C；
   - `git -C C rev-parse --git-common-dir` 解析到C自己的 `.git`；
   - branch lineage/base精确绑定c3879065...；
   - 不存在对canonical R的worktree linkage。

4. 只在 AI Skills C 内准备 harmless clone-local probe：
   - C/.codex/config.toml
   - default_mode_request_user_input=true
   - locked profile extends=:workspace
   - project .codex explicit deny
   - harmless SessionStart Hook
   - harmless PostToolUse matcher ^request_user_input$
   - fake private binder/capability/runtime/consumed area
   - results under:
     results/hpc--slurm-cancel-production-closure/chat-confirmation-v2-1-probe/

5. 在任何 Desktop probe / Hook trust 之前，必须先用正式 `hooks/list` 或等价官方入口证明：
   - cwd/root = exact AI Skills C；
   - discovered probe Hook source位于 `<C>/.codex/...`；
   - discovered Hook source不位于canonical
     `/overflow/htzhu/mingcheng_new/AI_Skills_Collection/.codex/...`；
   - clone-local declaration/current_hash就是实际加载对象。

   如果 `hooks/list` 仍找不到clone-local Hook，或仍发现canonical/root-checkout Hook：
   PHASE_0_CAPABILITY=FAIL
   → STOP -> Planner

   不得向canonical R写probe Hook兜底。

6. Phase 0 不得调用任何 Slurm command，包括read-only Slurm。
   它只验证Codex chat / Hook / permission / anti-tamper primitive。

7. 在任何 Hook trust动作前冻结：
   - current Codex identity / CODEX_HOME locator
   - exact candidate clone C
   - exact Hook source
   - exact stable Hook key
   - exact current_hash
   - trust status
   - pre-trust exact hooks.state key state

8. 如果Desktop要求Hook trust：
   - 只允许用户本人通过官方 Codex Hook trust UI trust上述exact key/current_hash；
   - Executor不得直接编辑 `$CODEX_HOME/config.toml`；
   - 不得直接调用通用 config writer伪造trust；
   - user UI trust后用 `hooks/list` +正式config readback证明：
     - exact Hook status=Trusted
     - trusted_hash == frozen current_hash
     - 本task未直接修改其它user config字段。

9. 使用fresh Longleaf Codex Desktop interactive root chat，root/cwd=exact AI Skills C，验证：
   - native request_user_input在Default mode实际可用
   - UI显示harmless question
   - 用户显式“确认测试”返回dedicated response
   - PostToolUse收到matching tool_input/tool_response/session_id/turn_id/tool_use_id
   - 第二轮不回答得到empty answers
   - empty不触发authority action

10. 如果Executor无法自行创建并展示fresh Desktop chat：
    STOP at PROBE_READY_FOR_USER_CHAT

    只要求用户：
    - 在Longleaf_Codex打开exact AI Skills C的新chat
    - 若显示Hook trust，只trust evidence中exact key+current_hash匹配的probe Hooks
    - 发送harmless probe prompt
    - 完成一次“确认测试”，另一次不回答

    不要求terminal。

11. authority-boundary probe继续必须证明：
    - trusted Host Hook可访问fake private area
    - ordinary shell/Python/apply_patch/absolute/symlink被explicit .codex deny
    - auto_review-approved escalation仍不能访问private area
    - direct fake binder/fabricated JSON无authority
    - Modified Hook不能按原Trusted Hook运行
    - bypass_hook_trust=false
    - fake private binder digest mismatch => no execution
    - model-controlled PATH伪造scontrol/scancel不影响runtime.json frozen absolute path

12. Hook trust retention / rollback继续按Plan v2.1：
    - exact probe/candidate trust可保留至Phase 3 review
    - Hook声明删除/改变后旧hash只能inert
    - cleanup/revoke只走官方Hook trust管理入口
    - 若官方UI没有revoke/remove：
      HOOK_TRUST_RETENTION=INERT_RECORD
      + exact key/hash + reason
    - 禁止手工改user config

13. should-not-change regression：
    - git status --short
    - read-only git diff/rev-parse/remote identity
    - representative normal AI Skills tests

    full .codex deny造成真实退化：
    STOP -> Planner
    Executor不得自行缩窄deny。

14. 无Slurm确认：
    HEADLESS_PROTECTED_CANCEL=NEEDS_INTERACTIVE_CHAT_CONFIRMATION

15. Phase 0任一关键项FAIL：
    STOP -> Planner

    不得fallback：
    - canonical checkout Hook
    - linked worktree
    - terminal confirmer
    - UserPromptSubmit
    - auto_review
    - approval prompt
    - MCP
    - daemon/database/broker
    - Bridge global config

只有Phase 0 PASS才继续。

## Phase 1 — standalone DII/CARE clones + product candidate

16. Phase 0 PASS 后才创建DII/CARE standalone candidate clones。

17. 每个DII/CARE C都必须重复：
    - C path预先不存在
    - 从canonical R只读得到origin URL
    - standalone clone
    - exact frozen source checkout
    - 在clone内创建冻结task branch
    - C/.git为clone-local Git目录
    - show-toplevel==C
    - git-common-dir==C/.git
    - hooks/list发现C-local Hook
    - hooks/list不得发现canonical R Hook

    任一失败：
    STOP -> Planner

    不得写canonical R/.codex兜底。

18. AI Skills实现exact Proposal v2.1：
    - thin central guard
    - protected_cancel_partitions
    - reviewed binder source
    - candidate/setup tooling
    - private authority root
    - private runtime binder
    - capability.key
    - runtime.json
    - consumed/
    - trusted SessionStart Hook
    - synchronous PostToolUse exact execution Hook
    - project config/hooks/rules
    - automation-only scancel shim

19. Hook declaration冻结：
    - canonical absolute private binder path within candidate clone
    - exact reviewed binder SHA-256
    - invocation shape

    Host Hook执行binder前用trusted absolute hash executable验证digest。
    mismatch => no binder / no Slurm。

20. runtime.json冻结：
    - candidate clone root
    - binder SHA-256
    - trusted absolute scontrol
    - trusted absolute scancel

    binder禁止PATH lookup/alias/function/relative Slurm path。

21. DII只做：
    - exact central candidate integration
    - clone-local project config/hooks/rules
    - automation PATH/launcher resolution
    - existing business cancellation intent

    不复制protected policy/authority logic。

22. CARE只做：
    - clone-local project config/hooks/rules
    - PATH/launcher resolution
    - chat-blocker propagation

    B1/M7/M8/interactive takeover/cascade行为继续完全按approved v2.1合同。

    用户确认后Host Hook已经完成exact cancellation。
    controller/watcher resume只观察状态并继续业务，不再第二次scancel消费confirmation。

## Phase 2 — validation

23. deterministic tests继续覆盖：
    - config compile/origin
    - Hook discovery/trust
    - standalone clone Hook source identity
    - explicit deny
    - binder digest mismatch
    - trusted absolute executable binding
    - request schema/response classification
    - CARE blocker propagation
    - DII minimal integration
    - headless fail closed
    - git/status/test should-not-change

24. 任何fake scancel/subprocess destructive path只允许真正隔离fake Slurm：

    - network disabled
    - isolated PID namespace
    - no production SSH key/agent/token
    - no real Slurm/MUNGE/controller/socket
    - no host control socket
    - no production writable mount
    - fake Slurm only

    不能证明：
    BLOCKED_BY_ISOLATION

    不得用真实Longleaf替代。

25. Gate仍只有：
    Gate A：partition routing
    Gate B：native fresh chat confirmation + authority boundary
    Gate C：consumer/runtime coverage + should-not-change
    Gate D：target integrity / claim truth

    不新增Gate E。

26. 绝不执行真实：
    sbatch/salloc/srun/scancel/mutating scontrol/signal/requeue/release/kill holder/test allocation/任何真实job cancellation test。

## Phase 3 — candidate publication + production identity render + Reviewer

27. 冻结三仓standalone candidate clone exact commits和完整evidence。

28. 使用exact final candidate binder digest + exact reviewed setup generator，对三个canonical production roots离线渲染production Hook identities。

canonical production roots仍是：

AI Skills：
/overflow/htzhu/mingcheng_new/AI_Skills_Collection

DII：
/users/a/e/aereinh/Distributed_Imaging_Inference

CARE：
/users/a/e/aereinh/CARE

不得写production文件、不得生成production capability、不得激活production Hook。

每个production root冻结：
- exact candidate commit
- canonical production root
- canonical private binder absolute path
- final binder SHA-256
- exact production SessionStart Hook declaration
- exact production PostToolUse Hook declaration
- exact production stable Hook keys/current_hashes
- expected runtime.json canonical root/digest/trusted absolute Slurm binding
- production project config/rules declaration identity

**candidate clone Hook key/hash不得替代production Hook identity。**

29. 每个candidate clone中的task branch最多允许一次普通、非强制、同名first publication：

git push --set-upstream origin work/hpc--slurm-protected-partition-chat-confirmation-v2-1

仅在：
- clone origin正确
- branch lineage正确
- clone clean
- same-name remote branch不存在

时允许。

禁止canonical checkout push、其它branch/remote、force/force-with-lease、delete/tag/history rewrite。

30. Phase 3 evidence必须包括：
    - 三仓candidate commits
    - 三仓standalone clone identity proof
    - hooks/list clone-local Hook source evidence
    - canonical R未由本task修改的evidence
    - Phase 0 Desktop/authority probe
    - Gate A-D
    - isolation status
    - private binder SHA-256/path contract
    - candidate clone Hook key/current_hash/trust
    - 三仓offline production-rendered Hook identities
    - trusted absolute scontrol/scancel
    - should-not-change
    - Hook trust side-effect inventory
    - rollback
    - independent Reviewer prompt

Reviewer必须实际审production-rendered Hook identities。

## 本 Kickoff 不授权

- 写任何canonical checkout probe/candidate Hook
- linked-worktree candidate runtime
- 清理/reset/stash/checkout canonical R
- production activation
- production AI Skills install
- real protected_cancel_partitions write
- canonical production runtime activation
- production automation PATH
- main integration
- release/version bump
- Bridge source modification
- Executor直接编辑user-level $CODEX_HOME/config.toml
- 除用户通过官方Hook trust UI为本task exact frozen key/current_hash写入hooks.state外的其它user-level config修改
- ai-bridge-global.rules
- user-level Hook declarations
- paid model/API
- any real Slurm mutation

Phase 3 independent Reviewer PASS 后仍不得自动部署。

production activation仍必须等用户第二条短、独立授权，并同时绑定：

- exact reviewed AI Skills/DII/CARE candidate commits
- Reviewer冻结的三仓production Hook stable keys/current_hashes
- canonical production roots
- private binder absolute paths + final binder digests

production setup真正写入canonical project files后，必须先用 hooks/list readback actual production current_hash并与Reviewer冻结值完全一致；不一致立即STOP，禁止trust。

只有完全一致时，用户才可通过官方 Codex Hook trust UI trust exact production hashes。该UI trust write仍是production阶段唯一允许的user-level hooks.state config副作用；Executor不得直接写user config。
