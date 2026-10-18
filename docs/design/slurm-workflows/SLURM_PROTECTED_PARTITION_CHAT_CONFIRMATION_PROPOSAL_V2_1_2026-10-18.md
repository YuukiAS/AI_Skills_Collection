# Slurm Workflows：受保护分区聊天二次确认 Proposal v2.1

日期：2026-10-18
task：hpc--slurm-cancel-production-closure
owner：YuukiAS/AI_Skills_Collection standalone skill slurm-workflows
source main at this revision：97f60dd87d65732388090235b2bdbc478a2e6222
supersedes execution package：38a76797439c6b29098aade7539270cbc51e8836
status：ARCHITECTURE_NARROW_REVISION / CRITIC_REQUIRED / NO_IMPLEMENTATION

上版 Proposal v2：
docs/design/slurm-workflows/SLURM_PROTECTED_PARTITION_CHAT_CONFIRMATION_PROPOSAL_V2_2026-10-18.md
commit：5692e7441d33b115df9220bd18d9fd8b872019b8
blob：bc62264c6010b3e5371885899138f72c03095250

v2 主架构继续有效；本 v2.1 只修正一个内部执行点：
**真人确认之后，exact cancellation 的执行 owner。**

## 0. Planner 结论

ER-V2-01_CONFIRMATION_AUTHORITY_NOT_FROZEN = ACCEPTED

旧 execution package 的结构：

request_user_input 真人确认
→ PostToolUse binder 写 persisted confirmed state
→ 下一次普通 shell guard 读取/consume
→ scancel

不能冻结为可靠安全机制。

原因：普通 Codex shell 与 guard 处在同一 sandbox/Unix identity。即使 binder 文件和 direct invocation 被 rules 禁止，只要 confirmed authority 最终落成一个 guard 能读写的普通文件，shell 也处于同等文件权限域；把“以后做 anti-forgery regression”留给 Executor，不能证明 direct state edit / fabricated artifact / auto-review escalation 无法产生同等 authority。

推荐的最小修订：

CHAT_CONFIRMATION_AUTHORITY_MECHANISM =
POSTTOOLUSE_HOST_HOOK_DIRECT_EXACT_EXECUTION

也就是：

protected guard 第一次 block
→ native request_user_input
→ 用户明确“确认取消”
→ trusted PostToolUse hook 在 host-side 同一次处理里：
   1. 验证 dedicated response
   2. 重新只读解析 exact JobId / Partition / operation
   3. 验证仍匹配受保护目标
   4. 原子占用 one-time tool-response identity
   5. 直接执行这一笔 exact /usr/bin/scancel
   6. 记录 consumed/result
→ 不再产生供普通 shell 后续消费的 persisted confirmed authority

用户体验不变；只删除了内部“confirmed file -> 下一 shell consume”这一层。

## 1. 为什么必须改变 exact execution owner

### 1.1 当前 .codex 默认保护不够

OpenAI Codex 当前 restricted workspace 确实默认保护顶层：
- .git
- .agents
- .codex
- .aws

但当前源码 FileSystemSandboxPolicy::for_approved_command() 明确会在 approved command 上扩大 root / root-metadata write，**除非存在 explicit deny**。

当前官方测试 target_approved_materialization_tests.rs 直接证明：
- 默认 protected metadata 在 approved command 后可以获得 write；
- 显式 deny 的 .codex/private 子路径仍保持 deny。

因此：
- 仅依赖“普通 workspace-write 下 .codex 默认只读”不能阻止 auto_review / sandbox escalation；
- 需要一个显式 deny 的 private hook authority boundary。

### 1.2 Hook command 与普通 shell 不在同一执行边界

当前 hooks/src/engine/command_runner.rs 的 command hook 直接通过 host Command spawn；
core/src/hook_runtime.rs 也明确说明：
“Hooks run on the host”。

它不是普通 exec_command / unified_exec 的 sandbox 子进程。

因此可复用当前 Codex 已有边界：

普通 Codex tool shell
→ restricted sandbox + explicit deny

trusted PostToolUse command hook
→ host-side hook runtime

而无需新增 daemon、broker、MCP server 或新 Unix identity。

## 2. 冻结 authority boundary

每个适配项目使用 trusted project-local .codex/config.toml，除了 v2 已批准的：

[features]
default_mode_request_user_input = true

还必须选择一个项目 permission profile，例如：

default_permissions = "slurm-chat-guard"

[permissions.slurm-chat-guard]
extends = ":workspace"

[permissions.slurm-chat-guard.filesystem.":workspace_roots"]
".codex" = "deny"

精确 TOML 语法由实现前 deterministic config-compile test 固定；语义不可改变：

**普通 Codex tool execution 对项目 .codex 全部 deny read/write/execute。**

这条 deny 必须直接验证在：

- normal workspace shell；
- apply_patch；
- Python direct file access；
- absolute path；
- symlink/alias；
- require_escalated；
- approvals_reviewer=auto_review

下都仍然保持。

Critic/Executor 不得把 default .codex read-only 当作等价证据；必须验证 explicit deny 在 approved-command materialization 后仍存在。

Codex core 自己的 project config / hook / rules discovery 是 host-side，继续可以加载该 .codex。

用户 ordinary shell 不受 Codex sandbox profile 影响。

## 3. private hook authority material

项目 .codex 下增加 runtime-private、非 Git secret 区域：

.codex/slurm-protected-cancel-private/

其中包含：

- bin/slurm-protected-cancel-binder
- capability.key
- runtime.json
- consumed/
- optional audit metadata

这里的 **authority binder executable/source 本身也属于 private authority material**，不能继续放在普通中央安装路径。

冻结要求：

- binder 是 exact reviewed candidate 的固定构建产物；候选 setup 在 locked runtime session 启动前把它复制到上述 private bin 路径；
- binder 文件至少 owner-only executable/readable，private directory 为 owner-only；
- capability.key 为随机 256-bit，mode 0600；
- binder/capability/runtime/consumed 全部不提交 Git，不写入 Prompt、tool output 或普通日志；
- ordinary Codex tool shell 因 explicit .codex deny 无法读取、复制、覆盖、删除、chmod 或替换 binder 与 authority material；
- auto_review approved-command escalation 不能解除 explicit deny；
- **不得依赖 project Hook declaration hash 自动覆盖 binder 内容**。

为把 Hook trust 与 external binder 内容真正绑定，trusted PostToolUse Hook declaration 必须冻结：

1. private binder 的 canonical absolute path；
2. exact reviewed binder SHA-256；
3. host-side pre-exec integrity check。

Hook command 在执行 binder 前，必须使用 trusted host absolute executable（例如平台实际核实后的 /usr/bin/sha256sum 或等价成熟工具）计算 private binder digest；digest 与 Hook declaration 中冻结的 expected SHA-256 不一致时立即 fail closed，绝不运行 binder。

因此：
- hooks.json / config 中的 trusted declaration hash绑定“binder absolute path + expected binder digest + invocation shape”；
- private explicit deny阻止 model修改 binder内容；
- binder digest check阻止外部内容漂移在 Hook declaration仍 Trusted时被静默执行。

生产安装/候选 setup负责生成 capability、复制 reviewed binder并写 runtime.json；这些都不是用户操作步骤。

## 4. guard 第一次 block

thin guard 保持 Proposal v2 语义：

ordinary scancel exact JobId
→ scontrol show job -o
→ 解析真实 Partition

non-protected：
→ 不新增确认
→ 原授权允许时正常 ordinary cancellation

protected：
→ 第一次绝不 mutation
→ 返回 NEEDS_INTERACTIVE_CHAT_CONFIRMATION
→ 包含 exact JobId / current Partition / normalized operation / opaque question id
→ 不生成 persisted confirmed authority

guard 可以产生普通 request descriptor 供聊天层构造问题，但它明确是：
UNTRUSTED_REQUEST_METADATA

即使普通 shell能看到或改写该 descriptor，也不能凭它获得 mutation authority。

## 5. native request_user_input 保持不变

interactive root Codex 根据 guard 输出调用 native request_user_input。

可见问题只允许：

“Job <id> 当前位于受保护分区 <partition>。确认取消这个 Job 吗？”

canonical options：

- 确认取消
- 保留 Job

UserPromptSubmit、assistant text、auto_review、subagent、internal automatic message 都不是 authority source。

empty answers / timeout / Other / free text / 保留 Job 全部不执行。

## 6. PostToolUse hook 成为 protected cancellation 的 exact execution owner

matcher 仍只为：

^request_user_input$

但 binder 不再写 confirmed=true 给下一 shell消费。

它收到 tool_input + tool_response 后，只有全部成立才继续：

1. 当前 tool 是真实 request_user_input PostToolUse event；
2. root interactive session；
3. question schema 是 canonical protected-cancel question；
4. response 对 exact question 明确为 canonical “确认取消”；
5. capability.key 能从 private denied .codex 区域成功读取；
6. tool_use_id / session_id / turn_id 尚未在 private consumed ledger 中占用；
7. 从 question 取得 exact JobId / declared Partition / operation；
8. host-side 重新调用 read-only Slurm：
   scontrol show job -o <exact JobId>
9. current JobId / Partition / operation 与用户刚确认的问题完全一致；
10. current Partition 仍在 private protected_cancel_partitions；
11. target 当前仍是可取消状态；
12. atomic create consumed reservation 成功。

然后 binder **直接**执行：

/usr/bin/scancel <exact JobId>

只允许 exact target；不接受 filter、array parent/range、heterogeneous、step、non-default signal 等 v2 已拒绝语义。

执行结果写入 private consumed ledger。

如果在 reservation 后、scancel 前 crash：
- 状态保持 fail closed；
- 不自动 replay；
- 用户需要重新发起一次 fresh confirmation。

这比“先写 confirmed，再让普通 shell consume”更保守。

## 7. ordinary Codex shell为什么不能伪造 authority

### 7.1 direct binder invocation

authority binder **只允许从 private denied absolute path 执行**：

.codex/slurm-protected-cancel-private/bin/slurm-protected-cancel-binder

不存在另一个可供 normal Codex shell直接调用的“authority mode”中央 CLI。

trusted Hook 先核对该文件的 frozen SHA-256，再执行它。binder随后在任何 Slurm动作前读取：

.codex/slurm-protected-cancel-private/capability.key

ordinary Codex shell处于 explicit .codex deny sandbox：

- 无法读取或执行 private binder path；
- 无法读取 binder源码后复制到可写位置；
- 无法替换 binder再等 trusted Hook执行；
- fabricated PostToolUse JSON即使喂给另一份自写程序，也没有 private capability；
- 直接运行中央普通 guard不具备 authority mode，因此不能代替 private binder。

因此 binder 必须把以下任一情况视为硬失败，并在任何 Slurm query/mutation前退出非零：

- private binder pre-exec digest mismatch；
- private capability.key 不可读；
- runtime.json 不可读或内容不匹配；
- Hook session / question identity 不匹配。

### 7.2 direct state edit

private runtime.json、capability.key 与 consumed ledger 位于同一 explicit denied .codex subtree。

runtime.json 还冻结本次部署允许 binder调用的 trusted host executables：
- canonical absolute scontrol path；
- canonical absolute scancel path。

这些路径由 trusted candidate/setup在进入 locked runtime前只读解析和验证，必须是 workspace外、非当前 ordinary Codex tool可写的真实 host executable。binder运行时只使用这些绝对路径，禁止通过 PATH、shell alias、function或相对路径解析 Slurm命令。

normal shell / auto_review escalation不能：
- 修改、替换或读取 private binder；
- 修改 runtime.json 中的 trusted executable binding；
- 写 consumed；
- 删除 consumed；
- 回滚 consumed；
- 替换 capability.key；
- 修改 private runtime metadata。

### 7.3 修改 hooks.json / config / rules

v2.1 初始候选 runtime profile deny 整个 project .codex，而不是只 deny private 子目录。这样不仅保护 capability/binder，也防止当前 locked session直接改写决定 authority path 的 config/hooks/rules。

因此当前 runtime session中的普通 shell也不能通过：
- 修改 hooks.json 指向恶意 hook；
- 删除 deny profile；
- 修改 project rules；
- 替换 binder registration

来伪造 authority。

候选开发阶段要修改 .codex 时，必须由尚未进入该 locked runtime profile 的 task setup session完成；一旦 fresh runtime session加载 locked profile，就把 .codex 当成不可由 agent 修改的 runtime metadata。

### 7.4 auto_review

当前 approved-command materialization 对 explicit deny 必须保持。

所以 approvals_reviewer=auto_review 即使批准 sandbox escalation，也不能得到该 denied .codex authority subtree。

这必须成为 Gate B 的直接回归，不允许用文档推断代替。

## 8. one-time / replay / target-change

one-time identity：

(session_id, turn_id, tool_use_id, canonical question id)

在 host-side private consumed ledger 中通过 O_EXCL / equivalent atomic create占用。

任何重复 PostToolUse delivery：
→ consumed reservation 已存在
→ no mutation

Job / Partition / operation 任何变化：
→ re-resolve mismatch
→ no mutation

旧 request_user_input response不能用于另一 Job。

不存在 shell-readable confirmed token，所以没有“复制 token 后 replay”的路径。

## 9. CARE / DII transport 的变化

CARE/DII 不增加任何 protection logic。

CARE：

protected guard nonzero
→ watcher按 v2 已批准合同传播给 supervising interactive Codex
→ root Codex request_user_input
→ 用户确认后，PostToolUse binder已经直接完成 exact cancellation
→ root Codex随后 resume/rerun watcher，只负责观察/继续原业务状态机

因此不再要求“用户确认后下一 watcher ordinary scancel来消费 confirmed state”。

具体：
- B1：nonzero传播；确认后 resume 观察 loser 状态
- M7：nonzero传播；确认后 resume
- M8：nonzero传播；确认后 resume
- interactive takeover：nonzero传播；确认后 resume，只有观察到合法 cancellation state 才继续 takeover
- cascade formal race：nonzero结束当前 round并传播；确认后由 controller恢复下一 round

consumer仍不解析：
- protected partition policy
- nonce
- request_user_input answer
- capability.key
- consumed ledger

DII同理。

这是 v2.1 唯一与 v2 execution semantics 的变化。

## 10. headless behavior不变

codex exec没有 request_user_input：

protected cancel
→ NEEDS_INTERACTIVE_CHAT_CONFIRMATION
→ fail closed

不使用 terminal confirmer、auto_review、ordinary approval、UserPromptSubmit 或 MCP fallback。

## 11. 四项 Capability Gate保持不变

不新增第五 Gate，只更新 Gate B/C 的 exact evidence。

### Gate A：partition routing

不变。

### Gate B：native fresh chat confirmation + authority boundary

必须新增证明：

1. canonical request_user_input真人“确认取消”触发 host-side binder；
2. binder可读取 private capability.key；
3. normal Codex shell读不到 key；
4. apply_patch / Python / symlink alias / direct binder / copied binder / fabricated JSON全部不能得到 authority；
5. normal shell不能读取、替换或执行 private authority binder，且无法改写 runtime.json 的 trusted Slurm absolute paths；
6. Hook pre-exec digest check能拒绝任何与 reviewed SHA-256不一致的 private binder；
7. binder只调用 runtime.json冻结的 trusted absolute scontrol/scancel，完全不使用 model-controlled PATH；
8. auto_review批准的 escalated command仍不能越过 explicit .codex deny；
9. hooks.json / config / rules在locked runtime session不可由普通 shell修改；
10. binder重新 resolve exact Job/Partition/op后才允许 fake exact mutation；
11. consumed ledger one-time；
12. duplicate PostToolUse / replay / target-change均不 mutation。

### Gate C：consumer/runtime coverage

更新为：
- CARE/DII protected blocker传播给 interactive root；
- user确认后 binder直接完成 exact cancellation；
- consumer resume只观察/继续业务，不再消费 confirmation；
- **should-not-change 回归**：locked project permission profile启用后，普通必要开发行为仍可正常完成，至少覆盖 repo内正常 `git status --short`、普通 read-only Git identity/diff 检查，以及各仓库与本任务相关、原本不依赖读取 project .codex 的代表性测试；
- 如果 explicit deny整个 project .codex 确实造成上述正常开发入口的真实退化，本轮不能由 Executor临场放宽。返回 Planner做**最小 deny surface 收缩**，同时必须继续保护 authority binder/private material和决定authority path的配置，且仍不得新增第五Gate。

### Gate D：target integrity / claim truth

不变；live Longleaf仍不做真实 cancellation test。

## 12. isolated testing

真实 scancel路径只允许 fake Slurm isolation：

- network disabled
- isolated PID namespace
- no production SSH/key/token
- no real Slurm/MUNGE/controller/socket
- no host control socket
- no production writable mount
- fake Slurm only

必须专门测试：

- hook host can access fake private authority area，包括binder/runtime/capability/consumed；
- sandboxed normal tool不能读取或修改private binder/runtime/capability；
- private binder被离线篡改后，trusted Hook declaration中的expected SHA-256使pre-exec check拒绝执行；
- model-controlled PATH中放置伪造scontrol/scancel时，binder仍只调用runtime.json冻结的trusted absolute paths；
- approved/auto-reviewed escalation仍不能；
- confirmed hook直接调用 fake scancel一次；
- duplicate hook不再次调用。

Longleaf capability probe仍只做 harmless request_user_input / hook observation，不执行真实 Slurm mutation。

## 13. 为什么不保留旧 persisted-confirmed 结构

比较三个方案：

A. confirmed file -> 下一普通 shell guard consume
- guard必须能读取/修改authority state；
- shell处于同一权限域；
- one-time replay需要额外 privileged consume primitive；
- REJECT。

B. cryptographic signed confirmed token -> 下一普通 shell guard
- 能解决伪造；
- 但 one-time replay仍需要 shell不可写的mutable ledger；
- 为此又必须新增第二个 privileged consume边界；
- 比直接 hook execution更复杂；
- REJECT。

C. request_user_input PostToolUse host hook直接 re-resolve + exact execute
- authority始终停留在已有 host hook boundary；
- 无 shell-readable confirmed state；
- one-time ledger也在同一 protected host-only area；
- 用户交互不变；
- 不增加 daemon/broker/MCP；
- ACCEPT。

## 14. 能保证什么 / 不能保证什么

能保证的目标范围：

- verified Codex normal entry中，普通 shell/auto_review不能制造受保护取消的 chat confirmation authority；
- only dedicated request_user_input response + trusted host PostToolUse path可以触发受保护 exact cancellation；
- exact target/Partition/op在mutation前重查；
- one-time consumed；
- user ordinary shell仍可自己直接scancel。

不能声称：

- same Unix UID下任意绕过Codex sandbox的本地进程在OS层永远不能调用Slurm；
- 未安装locked project permission profile的仓库自动获得保护；
- headless codex exec能完成protected cancel。

## 15. 对 execution package 的影响

现有 execution package：

38a76797439c6b29098aade7539270cbc51e8836

继续：
NOT_EXECUTABLE / REVISE_PENDING

不得发给Codex。

本v2.1若Critic PASS，Planner再重新生成同版：
- Execution Plan v2.1
- Canonical Goal v2.1
- Kickoff Draft v2.1

必须删除：
- persisted confirmed authority
- next ordinary scancel consumes confirmation

并加入：
- explicit locked .codex permission profile
- private authority binder + capability.key + runtime.json + consumed ledger
- Hook declaration绑定private binder absolute path + expected SHA-256
- binder绑定trusted absolute scontrol/scancel
- PostToolUse direct exact execution owner
- CARE/DII confirm-after resume semantics

## 16. Maintenance truth

保持：

tracking issue: PENDING_CLEAR_WRITING

不伪造Issue / DOING / ADAPTING / DONE。

## 17. 当前直接证据

OpenAI Codex reviewed：
8c076942cb70fba8e5c4732c23f1faabc4aed484

关键源码：

- codex-rs/protocol/src/permissions.rs
  - .codex是protected workspace metadata。
- codex-rs/protocol/src/permissions/target.rs
  - for_approved_command扩大approved root/root-metadata write；
  - explicit deny保留。
- codex-rs/protocol/src/permissions/target_approved_materialization_tests.rs
  - 直接测试approved command对metadata write和explicit .codex/private deny。
- codex-rs/hooks/src/engine/command_runner.rs
  - command hook由host Command直接spawn，无普通tool sandbox wrapper。
- codex-rs/hooks/src/engine/discovery.rs
  - non-plugin project Hook trust hash绑定normalized Hook declaration；external command target文件内容不会自动成为Hook content hash，所以v2.1不能依赖Hook declaration hash保护外部binder内容。
- codex-rs/core/src/hook_runtime.rs
  - 明确“Hooks run on the host”。
- codex-rs/core/src/tools/registry.rs
  - PostToolUse只在tool成功后运行；request_user_input属于成功dedicated-response path。
- codex-rs/config/src/permissions_toml.rs
  - project permission profile支持extends=:workspace与filesystem entries。
- codex-rs/config/src/loader/README.md
  - Project config优先于User config。

Bridge Kit latest reviewed in this design round：
f67ac9155c1a844f171afbeef03e8169b8eec6fc

本Proposal不修改Bridge source。
