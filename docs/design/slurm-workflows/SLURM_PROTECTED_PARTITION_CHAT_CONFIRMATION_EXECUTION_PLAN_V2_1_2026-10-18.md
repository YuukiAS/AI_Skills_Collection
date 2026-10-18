# Slurm Workflows：受保护分区聊天二次确认 Execution Plan v2.1

日期：2026-10-18
task：hpc--slurm-cancel-production-closure
owner：YuukiAS/AI_Skills_Collection standalone skill slurm-workflows

架构 authority：
- docs/design/slurm-workflows/SLURM_PROTECTED_PARTITION_CHAT_CONFIRMATION_PROPOSAL_V2_1_2026-10-18.md
- approved Proposal commit：31910548fe5d08eb8e1f5a8fe44040a2f51b32b9
- approved Proposal blob：26760ae8bb0a19809f1048436fa14aba0bb4e49a

execution-package preparation base：
31910548fe5d08eb8e1f5a8fe44040a2f51b32b9

Repository version baseline：
5.4.5

standalone skill baseline：
slurm-workflows 0.4

状态：
EXECUTION_PACKAGE / AUTHORIZED_ONLY_AFTER_CRITIC_PASS_AND_USER_SEND / PHASE_0_TO_3_ONLY

永久拒绝旧 execution packages：
- 4d940d7510e29f74a14c5b5070a1a9671f3f27e7
- 38a76797439c6b29098aade7539270cbc51e8836
- ER-V2-01 未关闭期间形成的旧 v2 execution drafts

不得复活旧 Kickoff、terminal confirmer、persisted-confirmed-token 或“下一 ordinary scancel 消费确认”语义。

## 1. 完成后新增的真实能力

Longleaf private policy：

protected_cancel_partitions = ["htzhulab"]

正常交互：

ordinary scancel exact JobId
-> central guard read-only scontrol show job -o
-> non-protected：不新增 protected-cancel 二次确认
-> protected：第一次绝不 mutation
-> NEEDS_INTERACTIVE_CHAT_CONFIRMATION
-> root interactive Codex native request_user_input
-> 用户明确选择“确认取消”
-> trusted PostToolUse host Hook
-> 验证 private authority boundary
-> 重新解析 exact JobId / Partition / operation
-> atomic one-time reservation
-> trusted absolute /usr/bin/scancel exact target once
-> consumer/controller resume，只观察真实状态并继续业务流程

用户不复制 challenge、不打开 terminal、不运行 confirmation wrapper、不维护 pending state。

明确不实现：
- H100 / accelerator protection
- current-run ownership
- owned-job-id
- old three-state safe-cancel
- persisted confirmed token
- terminal confirmer
- UserPromptSubmit authorization
- execpolicy prompt / auto_review human proof
- MCP server
- database / daemon / broker
- fifth Capability Gate

## 2. 冻结 source identities 与全新 execution identities

### AI_Skills_Collection

下一 execution-ready Critic 必须将 APPROVED_COMMIT 绑定到最终 v2.1 execution package commit 本身。

执行时：
- fetch/read exact APPROVED_COMMIT；
- origin/main 必须仍能定位该 commit；
- 若 main 后续只前进无关文档，不允许静默把新内容吸进当前 candidate；
- branch 必须从 APPROVED_COMMIT 创建；
- 若 slurm-workflows / workflow contract / relevant .codex semantics 已在 main 发生实质变化，STOP -> Planner。

R：
/overflow/htzhu/mingcheng_new/AI_Skills_Collection

branch：
work/hpc--slurm-protected-partition-chat-confirmation-v2-1

W：
/overflow/htzhu/mingcheng_new/AI_Skills_Collection-hpc--slurm-protected-partition-chat-confirmation-v2-1

### DII

frozen source：
747829b957b19e8fcffa6bd5f1bb7ae62ae11f6f

R：
/users/a/e/aereinh/Distributed_Imaging_Inference

branch：
work/hpc--slurm-protected-partition-chat-confirmation-v2-1

W：
/users/a/e/aereinh/Distributed_Imaging_Inference-hpc--slurm-protected-partition-chat-confirmation-v2-1

### CARE

frozen source：
75a40e454de43b64e59a0b0b438ff57ef2bb8345

R：
/users/a/e/aereinh/CARE

branch：
work/hpc--slurm-protected-partition-chat-confirmation-v2-1

W：
/users/a/e/aereinh/CARE-hpc--slurm-protected-partition-chat-confirmation-v2-1

### 平台 source

OpenAI Codex reviewed main：
8c076942cb70fba8e5c4732c23f1faabc4aed484

Bridge Kit reviewed main：
d4b694673501d4933eca5cd68394c740c0cb823d

Bridge 相比上一轮只新增 `docs/design/bridge_kit_planner_critic_governance_layer_correction_proposal_v0.1_2026-10-18.md`，没有 Host Policy / Hook / approvals runtime 变化。本任务：
Bridge Kit source = NO_CHANGE。

执行包准备时三个新的 v2.1 remote task branch 均不存在。

## 3. branch/worktree 与首次远端发布

Critic PASS 本身不创建任何 branch。

只有用户本人实际发送 approved Kickoff 后：

Phase 0：
- 只创建 AI Skills exact v2.1 branch/worktree；
- DII/CARE 只读 preflight，不创建 worktree。

Phase 0 PASS 后：
- 才创建 DII/CARE exact v2.1 branch/worktree。

每个 repo 创建前必须验证：
- exact repo root；
- origin identity；
- clean source；
- frozen source commit；
- target local branch 不存在；
- target W 不存在；
- same-name remote branch 不存在。

任何 drift / dirty / collision / lineage mismatch fail closed。

候选完成后、独立 Reviewer handoff 前，每个 exact task branch最多授权一次普通非强制同名首次发布：

git push --set-upstream origin work/hpc--slurm-protected-partition-chat-confirmation-v2-1

禁止：
- 其它 branch / remote
- force / force-with-lease
- delete / tag
- history rewrite
- raw main push

首次发布后普通同分支更新使用现有 bounded current-branch publisher。

## 4. locked project permission profile

每个适配 repo 最终 candidate 都使用 trusted project .codex/config.toml。

必须启用：

[features]
default_mode_request_user_input = true

并冻结一个专用 profile，例如：

default_permissions = "slurm-chat-guard"

[permissions.slurm-chat-guard]
extends = ":workspace"

[permissions.slurm-chat-guard.filesystem.":workspace_roots"]
".codex" = "deny"

精确 TOML 语法必须先由当前 Codex config compiler / config read验证；语义不得改变：

普通 Codex tool execution对 project .codex显式 deny。

必须证明：
- shell denied；
- Python direct file access denied；
- apply_patch denied；
- absolute path denied；
- symlink / alias denied；
- require_escalated denied；
- approvals_reviewer=auto_review approved-command escalation后仍 denied。

不得以“默认 .codex protected metadata”代替 explicit-deny evidence。

Host-side Codex config / hooks / rules discovery仍必须正常工作。

用户 ordinary shell不受 project sandbox profile影响。

## 5. authority material：binder 本身也在 private boundary

每个适配 repo 的 runtime-private root：

.codex/slurm-protected-cancel-private/

只允许包含 runtime authority material：

bin/slurm-protected-cancel-binder
capability.key
runtime.json
consumed/
audit/

全部：
- 不提交 Git；
- 不进入 Prompt / tool output /普通日志；
- owner-only；
- model tool sandbox explicit deny；
- Host Hook可访问。

### 5.1 reviewed binder source 与 private runtime copy

reviewed binder source可以作为 central slurm-workflows product source受正常代码审查。

但真正拥有 protected-cancel execution authority的 runtime binder只能是：

<project-root>/.codex/slurm-protected-cancel-private/bin/slurm-protected-cancel-binder

候选 setup 在进入 locked fresh runtime session前：

1. 从 exact reviewed central candidate 构建/复制 binder；
2. 计算 SHA-256；
3. 写 private runtime copy；
4. mode至少 owner-readable/executable；
5. 写 runtime.json；
6. 生成与该 exact private binder匹配的 project Hook declaration。

不允许保留另一个普通中央 CLI “authority mode”。

普通 central guard永远没有 chat-confirmation execution authority。

### 5.2 Hook declaration必须绑定 binder path + digest

PostToolUse Hook declaration必须冻结：

- canonical absolute private binder path；
- reviewed binder SHA-256；
- invocation shape。

Host Hook真正执行 binder前必须：

1. 使用 trusted host absolute hashing executable；
2. 对 exact private binder计算 SHA-256；
3. 与 declaration冻结值精确比较；
4. mismatch => fail closed；
5. mismatch时不得调用 binder或任何 Slurm命令。

不得依赖 non-plugin project Hook trust hash自动包含外部 binder内容。

### 5.3 trusted Slurm executable binding

runtime.json由 candidate/setup 在 locked session前只读发现并冻结：

- canonical project root；
- exact binder digest；
- canonical absolute scontrol path；
- canonical absolute scancel path；
- expected cluster / runtime identity中必要但非secret的定位信息。

scontrol/scancel必须：
- 位于 workspace外；
- ordinary Codex tool不可写；
- 通过 trusted setup只读验证是真实 host executable。

binder运行时：
- 禁止 PATH lookup；
- 禁止 shell alias/function；
- 禁止相对路径；
- 只调用 runtime.json冻结的 absolute scontrol/scancel。

model-controlled PATH中即使放入伪造 scontrol/scancel也不得影响结果。

## 6. SessionStart capability

trusted project SessionStart Hook：

- root interactive session only；
- OS CSPRNG生成至少256-bit capability；
- 写入 private capability.key；
- mode 0600；
- runtime record绑定 exact session_id、project root identity、trusted Hook版本/hash、created_at；
- 不回显 capability；
- 不进入 model环境；
- 不进入普通日志；
- stale/session-end cleanup；
- capability缺失 => protected confirmation fail closed。

生产配置禁止：
- --dangerously-bypass-hook-trust
- bypass_hook_trust=true
- 未经用户Hook trust review的Modified Hook

新的/修改后的 project Hook如果 Desktop要求trust：
- Executor不得用auto_review替代；
- 停在明确最小用户动作；
- 用户只需在Desktop中确认当前 exact hook declaration；
- hook current hash与candidate evidence必须一致，否则不得要求用户trust。

## 7. thin guard：只负责first block

central ai-slurm-scancel仍保持薄职责：

支持：
- ordinary exact JobId；
- explicit exact JobId list；
- 唯一只读解析的 exact array element。

fail closed：
- array parent/range；
- heterogeneous；
- job step；
- dynamic selectors；
- federation / cluster switch；
- non-default signal / batch / full。

每次先：
scontrol show job -o <exact JobId>

必要时 bounded squeue cross-check。

non-protected：
- 不增加chat confirmation；
- 当前原授权允许时才调用trusted real scancel normal path。

protected：
- 第一次绝不 mutation；
- 返回 NEEDS_INTERACTIVE_CHAT_CONFIRMATION；
- exact JobId；
- current Partition；
- normalized operation；
- opaque question id；
- short-lived UNTRUSTED_REQUEST_METADATA。

guard不生成persisted confirmed authority。

## 8. native request_user_input contract

只有interactive root Codex可继续protected cancellation。

canonical visible question：

“Job <id> 当前位于受保护分区 <partition>。确认取消这个 Job 吗？”

canonical options：

- 确认取消
- 保留 Job

只有dedicated response中的canonical“确认取消”进入authority Hook path。

全部拒绝：
- empty answers；
- timeout；
- 保留 Job；
- Other/free text；
- wrong question；
- initial blanket Goal；
- historical authorization；
- standing race opt-in；
- auto_review；
- assistant-generated confirmation；
- UserPromptSubmit；
- subagent / internal automatic message。

## 9. PostToolUse binder直接成为exact mutation owner

matcher：

^request_user_input$

必须synchronous。

binder在任何Slurm mutation前依次验证：

1. 当前tool event确实为request_user_input PostToolUse；
2. root interactive session；
3. private binder pre-exec digest已由Hook验证；
4. private capability.key可读；
5. runtime.json可读并与当前project/session匹配；
6. question schema为canonical protected-cancel question；
7. response为canonical“确认取消”；
8. session_id / turn_id / tool_use_id / question id尚未consumed；
9. exact target / declared Partition / normalized operation与first-block request匹配；
10. 使用runtime.json冻结的absolute scontrol重新解析；
11. current exact JobId / Partition / operation仍匹配；
12. current Partition仍命中protected_cancel_partitions；
13. target仍在允许ordinary cancellation的Slurm state；
14. atomic O_EXCL或等价机制成功占用one-time consumed reservation。

然后才：

trusted absolute scancel <exact JobId>

只允许exact target。

禁止filter、array parent/range、heterogeneous、step、non-default signal等。

执行结果写private consumed/audit。

如果reservation成功后、scancel前crash：
- fail closed；
- 不自动replay；
- 旧response不能再次mutation；
- 用户重新发起fresh cancellation/confirmation。

## 10. anti-tamper contract

必须直接证明ordinary Codex normal entry不能获得同等authority。

### direct binder / copied binder / fabricated JSON

普通tool shell：
- private .codex explicit deny；
- 读不到private binder；
- 读不到capability；
- 读不到runtime.json；
- 不能直接执行private binder path；
- 不能复制private binder source/runtime bytes；
- fabricated PostToolUse JSON喂给普通自写程序也没有private capability。

### direct state edits

普通tool shell / auto_review escalation均不能：
- 修改capability.key；
- 修改runtime.json；
- 写/delete/reset consumed；
- 修改private audit以获得authority；
- 修改/替换/chmod private binder。

### Hook/config/rules tamper

locked fresh runtime session中普通tool不能修改project .codex：
- hooks.json；
- config.toml；
- rules；
- private subtree。

若外部变更使Hook declaration/current hash变化：
- status必须Modified；
- 不允许作为原Trusted Hook运行；
- 要重新经过真实Hook trust review。

## 11. Phase 0：无Slurm mutation capability + authority probe

Phase 0先于产品实现。

只创建AI Skills v2.1 worktree。

DII/CARE只读preflight。

在AI Skills W中准备harmless probe版本：

- project .codex/config.toml：
  - default_mode_request_user_input=true；
  - locked slurm-chat-guard profile；
- project hook config：
  - harmless SessionStart；
  - harmless PostToolUse ^request_user_input$；
- fake private binder / capability / runtime area；
- 不调用任何Slurm；
- results：
  results/hpc--slurm-cancel-production-closure/chat-confirmation-v2-1-probe/

### 11.1 config/runtime probe

必须证明：
- W为trusted project；
- Project config高于Bridge user-level false；
- active permission profile=slurm-chat-guard；
- .codex explicit deny实际加载；
- Bridge user-level config未修改。

### 11.2 Desktop native interaction probe

fresh Longleaf Codex Desktop root chat，cwd=W。

harmless request_user_input：
“这是聊天确认能力测试。请选择‘确认测试’或‘取消测试’。”

必须证明：
- Default mode tool可用；
- UI真实显示；
- 用户显式回答dedicated response返回；
- PostToolUse真实收到tool_input/tool_response/session/turn/tool_use；
- unanswered request auto-resolves empty；
- empty不触发harmless authority action。

如果Executor无法自行创建/展示fresh Desktop chat：
STOP at PROBE_READY_FOR_USER_CHAT。

用户唯一最小动作：
- 在Longleaf_Codex打开exact W的新chat；
- 若平台显示exact project Hook trust screen，只trust与evidence current hash一致的probe hooks；
- 发送指定harmless probe prompt并完成一次“确认测试”，另一次不回答以观察empty。

不得要求用户开terminal。

### 11.3 authority-boundary probe

完全不触碰Slurm。

必须证明：

- trusted SessionStart host Hook能创建fake private capability；
- trusted PostToolUse host Hook能读取private area；
- ordinary shell读private binder/capability/runtime => denied；
- Python/apply_patch/absolute/symlink alias => denied；
- direct private binder invocation => denied；
- copied-binder attempt无法读取private bytes/capability；
- fabricated harmless PostToolUse JSON => no authority；
- auto_review-approved escalation尝试读取private area =>仍denied；
- modified Hook fixture => HookTrustStatus::Modified；
- bypass_hook_trust=false；
- fake private binder content被篡改后，host pre-exec digest mismatch => binder不执行；
- model PATH中放假scontrol/scancel，harmless binder probe仍只解析runtime.json frozen absolute paths。

### 11.4 should-not-change regression

locked .codex profile下必须保持：

- git status --short正常；
- read-only git diff / rev-parse / remote identity正常；
- AI Skills本任务代表性普通tests可以运行，前提是其原设计不依赖model直接读取project .codex。

如果full .codex deny真实破坏正常入口：
STOP -> Planner。

Executor不得自行缩窄deny surface。

### 11.5 headless negative probe

无Slurm地确认：

codex exec不能完成request_user_input。

冻结：
HEADLESS_PROTECTED_CANCEL=NEEDS_INTERACTIVE_CHAT_CONFIRMATION

Phase 0任一关键项FAIL：
STOP -> Planner。

不得fallback到terminal confirmer、MCP、UserPromptSubmit、approval prompt或Bridge global config。

## 12. Phase 1：candidate implementation

只有Phase 0 PASS后：

1. 创建DII/CARE exact v2.1 branch/worktree。
2. AI Skills实现：
   - central thin guard；
   - private config field protected_cancel_partitions；
   - reviewed authority binder source；
   - deterministic candidate/setup tooling；
   - exact private binder copy/digest/runtime.json generation；
   - SessionStart capability hook；
   - PostToolUse exact execution Hook；
   - project config/hooks/rules；
   - automation-only scancel shim。
3. DII只做：
   - exact central candidate integration；
   - project config/hooks/rules；
   - automation PATH/launcher resolution；
   - existing business cancellation intent不变。
4. CARE只做：
   - project config/hooks/rules；
   - PATH/launcher resolution；
   - chat blocker propagation最小修复。

不写真实Longleaf private protected_cancel_partitions。
不production install。
不集成main。
不release。

## 13. CARE / DII consumer contract

consumer不解析：
- protected policy；
- question；
- answer；
- capability；
- binder digest；
- consumed ledger。

CARE：

B1：
- scancel nonzero不加入cancelled；
- propagation nonzero/guard output；
- 结束当前cancellation attempt。

M7：
- nonzero直接传播。

M8：
- nonzero直接传播。

interactive takeover：
- nonzero不进入sacct CANCELLED wait；
- 不launch；
- 直接传播。

cascade formal race：
- cancel nonzero结束当前watcher round并传播；
- 不继续内部interval loop吞掉chat blocker。

root interactive Codex收到NEEDS_INTERACTIVE_CHAT_CONFIRMATION：
- request_user_input；
- user确认后Host Hook直接完成exact cancellation；
- controller/watcher resume只观察真实Slurm状态并继续业务流程；
- 不再发第二次scancel来消费confirmation。

DII同理，只保留business-level cancellation intent。

新source若出现absolute /usr/bin/scancel、SSH scancel或Slurm API bypass：
STOP -> Planner。

## 14. Codex normal-entry rules与automation PATH

每个candidate project必须有reviewed project-local rules：

- raw scancel => forbidden；
- system /usr/bin/scancel => forbidden；
- any ordinary direct private-binder invocation shape => forbidden；
- guard不blanket allow。

rules只是normal-entry bypass防线，不替代private capability boundary。

automation-only PATH：
scancel -> central guard

不替换系统/usr/bin/scancel。
不改用户ordinary shell PATH。

每个required consumer必须用：
- command -v scancel
- Python shutil.which("scancel")

证明解析到reviewed guard shim。

## 15. Gate A-D

只保留四项。

### Gate A：partition routing

证明：
- non-protected exact job不新增chat confirmation；
- htzhulab first block零mutation；
- explicit multi-target任一protected =>整组protected；
- blanket initial authorization不能跳过first block。

### Gate B：native fresh chat confirmation + authority boundary

证明：
- live Desktop native request_user_input；
- dedicated explicit response；
- empty/timeout/retain/Other不mutation；
- initial Goal/assistant/auto_review/UserPromptSubmit/subagent不产生authority；
- trusted Hook能访问private authority area；
- ordinary tool shell / Python / apply_patch / alias / symlink / direct/copy/fabricated path不能访问；
- auto_review escalation保持explicit deny；
- private binder digest mismatch拒绝；
- model PATH伪造scontrol/scancel不影响trusted absolute executable binding；
- modified Hook不能以Trusted身份运行；
- bypass_hook_trust=false；
- exact re-resolution在mutation前；
- atomic consumed；
- duplicate/replay/target-change no mutation。

### Gate C：consumer/runtime coverage + should-not-change

证明：
- AI Skills/DII/CARE project config/hooks/rules实际加载；
- required automation scancel解析guard；
- raw system scancel不能从Codex normal entry绕过；
- CARE blocker传播而不吞掉；
- DII不复制policy；
- headless protected flow fail closed；
- user ordinary shell system scancel不受影响；
- locked .codex 后 git status --short、read-only Git diff/identity和代表性正常tests不退化。

### Gate D：target integrity / claim truth

证明：
- exact target only；
- complex selector fail closed；
- binder mutation前re-resolve；
- destructive replay只在真正isolated fake Slurm；
- Longleaf live验证不真实cancel任何job；
- claim仅覆盖verified interactive Codex / required consumer normal entry；
- 不宣称same-UID OS-level unbypassable。

不新增Gate E。

## 16. destructive fake Slurm isolation

任何会真正执行fake scancel/subprocess mutation的验证只能在：

- network disabled；
- isolated PID namespace；
- no production SSH key/agent/token；
- no real Slurm/MUNGE/controller/socket；
- no host control socket；
- no production writable mount；
- fake Slurm only。

不能证明：
BLOCKED_BY_ISOLATION

不得转真实Longleaf mutation。

允许在真实Longleaf Desktop运行的只有：
- request_user_input；
- Hook trust / Hook observation；
- config/read；
- sandbox deny；
- harmless fake authority probe；
- read-only filesystem/Git/runtime checks；
- 后续production阶段的read-only Slurm inspection。

## 17. Phase 2：deterministic + isolated fake validation

Phase 0 PASS、Phase 1完成后：

- parser/state/request schema tests；
- Hook binder classification；
- digest mismatch；
- absolute executable binding；
- sandbox deny / escalation regression；
- CARE transport；
- headless fail closed；
- project config/hooks/rules load；
- isolated fake Slurm exact cancellation；
- duplicate/replay；
- target/Partition/op change；
- regression bank。

冻结AI Skills/DII/CARE exact candidate commits与完整Gate A-D evidence。

## 18. Phase 3：mandatory independent implementation review

每个candidate branch第一次发布按第3节授权。

Reviewer必须实际审：

- approved Proposal v2.1；
-本Plan/Goal；
-三仓diff；
- Phase 0 live Desktop/authority probe；
- Gate A-D；
- isolated fake evidence；
- private binder digest/path/runtime binding；
- Hook trust evidence；
- should-not-change regression；
- rollback；
- production activation proposal。

Reviewer PASS前：
NO PRODUCTION DEPLOYMENT。

## 19. Phase 4：production activation需要第二条短用户授权

当前Implementation Kickoff不授权Phase 4。

Reviewer PASS后，用户必须发送第二条短、独立、绑定exact reviewed三仓candidate commits的production authorization。

其最大范围仅允许：

- backup本任务会改的user-local install/private override/project-local runtime metadata；
- 安装exact reviewed central candidate；
- 在真实Longleaf private override写：
  protected_cancel_partitions=["htzhulab"]
  并保留其它字段；
- 在AI Skills/DII/CARE canonical project roots执行reviewed setup：
  - project config/hooks/rules；
  - private binder copy；
  - binder digest；
  - runtime.json trusted absolute executable binding；
  - capability lifecycle；
  - automation PATH shim；
- 若Desktop提示新/修改Hook trust，只允许用户trust与reviewed current hash一致的exact hooks；
- read-only production validation；
- exact reviewed DII/CARE integration。

不修改：
- Bridge source；
- user-level $CODEX_HOME/config.toml；
- ai-bridge-global.rules；
- user-level hooks。

绝不使用真实Slurm cancellation作为production smoke。

## 20. rollback

### candidate/probe rollback

未production前：
- 删除/弃用task worktrees/branches；
- 恢复/删除task-local .codex probe/runtime private material；
- 不存在production side effect。

### production rollback

只恢复本任务改变的：
- central installed candidate；
- private local override；
- AI Skills/DII/CARE project config/hooks/rules；
- private runtime authority material；
- automation PATH integration；
- consumer commits。

Hook trust state若需要撤销，使用Codex正式Hook trust管理入口；不得手工篡改不明user config。

不执行Slurm mutation。
不改MUNGE/SSH/Unix identity。
不改Bridge source。

## 21. version / release

candidate阶段：

Repository bump decision: NONE
Reason: 仍是未发布候选，不改变正式可安装release。

slurm-workflows: NO_BUMP
central Marketplace Plugins: NO_BUMP
Bridge Kit: NO_CHANGE

只有：
- production activation完成；
- required DII/CARE integration完成；
- production Gate A-D完整；
- independent Reviewer最终证据成立；

才进入release closure：

slurm-workflows 0.4 -> 0.5

Repository bump decision: PATCH
若release-time仍为5.4.5，则5.4.6；否则使用当时真实版本的next PATCH。

central Plugins: NO_BUMP
Bridge Kit: NO_CHANGE

README/CHANGELOG/version/generated metadata最后更新。

release metadata不得引入行为变化；任何行为变化先重新review。

## 22. Maintenance truth

当前：

tracking issue: PENDING_CLEAR_WRITING

旧TODO中的H100描述已经被用户最新protected-partition-only合同supersede。

当前无真实Clear Writing / Project mutation入口时：
- 不伪造Issue；
- 不伪造DOING/ADAPTING/DONE；
- final technical report输出exact pending mutation给下一具合法能力Maintainer；
- 不要求用户手工维护。

## 23. Stop conditions

任一出现立即STOP -> Planner/Critic：

- approved Proposal blob != 26760ae8bb0a19809f1048436fa14aba0bb4e49a；
- AI execution package commit无法定位；
- DII/CARE source drift；
- target branch/worktree collision；
- Project config不能安全启用default_mode_request_user_input；
- full .codex explicit deny在normal Git/status/test产生真实不可接受退化；
- explicit deny在auto_review escalation后失效；
- Host Hook不能访问private authority area；
- private binder可被normal tool读取/替换/执行；
- binder digest mismatch仍可执行；
- model PATH能影响binder的scontrol/scancel；
- Modified Hook仍可不经真实trust运行；
- bypass_hook_trust无法保持false；
- request_user_input/ PostToolUse live probe失败；
- CARE blocker无法返回interactive supervisor；
-需要terminal confirmer、MCP、database/daemon/broker、新Unix identity、H100/current-run/old三态；
- destructive testing需要真实Slurm；
- 任何真实cancellation/signal/requeue/release/test allocation；
- 需要Bridge source change；
- 需要付费模型/API。
