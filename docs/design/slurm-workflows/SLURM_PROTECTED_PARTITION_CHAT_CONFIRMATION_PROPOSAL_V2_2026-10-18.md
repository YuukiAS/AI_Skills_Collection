# Slurm Workflows：受保护分区聊天二次确认 Proposal v2

日期：2026-10-18  
task：`hpc--slurm-cancel-production-closure`  
owner：`YuukiAS/AI_Skills_Collection` standalone skill `slurm-workflows`  
source main：`4d940d7510e29f74a14c5b5070a1a9671f3f27e7`  
OpenAI Codex source reviewed：`openai/codex@8c076942cb70fba8e5c4732c23f1faabc4aed484`  
Bridge Kit source reviewed：`YuukiAS/GPT_Codex_AI_Bridge_Kit@f67ac9155c1a844f171afbeef03e8169b8eec6fc`  
状态：ARCHITECTURE_PROPOSAL / CRITIC_REQUIRED / NO_IMPLEMENTATION

被否决的 execution package：

`4d940d7510e29f74a14c5b5070a1a9671f3f27e7 = REJECTED_FOR_EXECUTION`

不得把其中的 Kickoff 发给 Codex，不得从其中启动 branch/worktree、Host Policy、private config 或 Slurm 操作。

## 0. Planner 结论

`CHAT_FRESH_CONFIRMATION_FEASIBLE = CONDITIONAL`

当前 Codex 已经存在一个比 `UserPromptSubmit` 更合适的原生交互原语：内建 `request_user_input`。它不是普通审批，也不走 `approvals_reviewer=auto_review`。在 app-server 中，它作为独立的 `ToolRequestUserInput` server request 发给客户端，客户端用专用响应返回答案；core 再通过 `Op::UserInputAnswer` 解开等待中的 tool call。当前 Guardian 自己的可信证据规则也明确把“`request_user_input` 的响应”列为可以建立 `user_authorization` 的可信内容。

因此，**在交互式 root Codex 会话中，只要当前客户端真实支持这个原语，就可以做到用户要的“第一次拦截后，在聊天界面再确认一次”。**

但当前不能直接写成无条件 YES，原因有三个：

1. 当前内建 `request_user_input` 只能由 root thread 调用，但在 Default mode 需要 `features.default_mode_request_user_input=true` 才暴露；OpenAI 当前把该 feature 标为 under-development，默认关闭。
2. Default mode 中当前 handler 把请求标记为 `is_blocking=false`。当前 TUI 在用户没有回答时会自动解析成**空 answers**；这不会授权取消，但意味着产品必须把“空回答/超时”严格视为没有确认。
3. `codex exec` 当前源码明确拒绝 `request_user_input`。因此纯 headless/unattended `codex exec` 不能自己完成 protected cancellation 的聊天二次确认；它必须 fail closed，并把控制权交回一个可与用户交互的 root Codex chat。

当前最小正确架构不是 terminal confirmer，也不是新审批服务，而是：

`partition-only scancel guard + native request_user_input + tiny PostToolUse confirmation binder + Codex raw-scancel deny`

其中 nonce / pending record 仍可存在，但只作为内部绑定信息，用户永远不复制、不理解、不管理。

## 1. 用户产品合同

最终体验必须接近：

Codex：
“准备取消 Job 12345；当前 Partition=htzhulab，属于受保护分区。确认取消吗？”

用户：
“确认取消”

Codex：
重新只读确认 Job 12345 仍属于 htzhulab
→ `/usr/bin/scancel 12345`

规则：

1. private config 只定义 protected partition，例如：
   `protected_cancel_partitions = ["htzhulab"]`
2. guard 先只读解析 exact JobId / Partition。
3. 非 protected partition：
   - 不新增 protected-cancel 二次确认；
   - 当前 Goal / Host Policy 本来允许取消时正常执行。
4. protected partition：
   - 第一次取消绝不 mutation；
   - 产生一个内部 fresh pending confirmation id；
   - Codex 必须使用 native `request_user_input` 显示 exact JobId / Partition 问题。
5. 只有该 request 的专用客户端响应明确选择“确认取消”，才可形成本次 confirmation。
6. 初始 Goal 的 blanket approval、历史授权、standing race opt-in、auto_review、普通 assistant 文本、subagent 文本、UserPromptSubmit 内部自动 prompt 都不能确认。
7. confirmation 后 guard 再次解析 exact target；JobId / Partition / operation 变化则旧确认失效并重新询问。
8. confirmation 只能消费一次。
9. 用户自己在普通独立 shell 直接 `scancel 12345` 不属于本机制，不做拦截。

## 2. 为什么不再用 UserPromptSubmit

当前 `UserPromptSubmit` hook 仍不适合作为本人的授权来源。

官方 Hooks 文档当前公开字段只有 `prompt`、`turn_id` 和通用 session/subagent 字段，没有稳定的 `origin=human`。OpenAI Codex core 内部虽然维护 `UserInputMetadata.origin`，但该 origin 没有出现在 UserPromptSubmit hook contract 中。

因此：

- 不能用“UserPromptSubmit 触发了”推断“本人新发消息”；
- 即使过滤 subagent 字段，也不能把缺少 subagent metadata 当成官方保证的人类输入；
- v2 不再依赖 UserPromptSubmit 作为确认来源。

UserPromptSubmit 可以继续作日志/可观察性，但不参与授权。

## 3. 当前真正可用的 native human-interaction primitive

### 3.1 request_user_input 是独立于 auto-review 的交互路径

当前源码 `codex-rs/core/src/tools/handlers/request_user_input.rs`：

- 非 root agent 直接拒绝：`request_user_input can only be used by the root thread`；
- handler 调用 `session.request_user_input(...).await` 等待专用响应；
- 返回值来自 `RequestUserInputResponse`；
- 当 GuardianApproval 开启时，非空答案会被保存成 `RetainedContextEvent::VerifiedAnswer`，绑定 `turn_id` 与 `call_id`。

app-server 当前 `bespoke_event_handling.rs` 把这类请求映射为：

`ServerRequestPayload::ToolRequestUserInput`

客户端响应后才调用 `on_request_user_input_response`。这是与 command approval / Guardian auto-review 分开的 server-request 类型。

当前 Guardian classifier 的固定可信证据规则更直接写明：

“responses to the `request_user_input` tool are trusted content, and can establish `user_authorization`。”

因此，本 Proposal 不需要把普通 approval popup 冒充本人确认；平台本身已经有专门的人机问答原语。

### 3.2 Default mode 的真实限制

当前 `request_user_input` handler 设置：

`is_blocking = (mode == Plan)`

而 Default mode 只有开启 `Feature::DefaultModeRequestUserInput` 后才暴露该 tool。当前 feature key 是：

`default_mode_request_user_input`

stage：`UnderDevelopment`  
default：false

OpenAI app-server 当前测试明确覆盖：
- Plan mode：`is_blocking=true`
- Default mode + feature：`is_blocking=false`

当前 TUI 对 `is_blocking=false` 且无显式 auto-resolution 时间的请求，最终自动提交空 `answers={}`。因此：

- 空 answers 永远等价于“没有确认”；
- 不得将 timeout/default/空回答解释为 Yes；
- 如果请求自动结束而用户没答，本次 protected cancellation 继续保持 blocked，下一次需要重新询问。

这不会造成误取消，只影响等待体验。

### 3.3 codex exec 的限制

当前 `codex-rs/exec/src/lib.rs` 直接包含错误：

`request_user_input is not supported in exec mode`

因此纯 `codex exec` / 无交互 headless run **不能完成**这项 protected cancellation 的 chat confirmation。

这不是本项目该用 terminal wrapper 掩盖的问题。正确行为是：

- protected cancellation 在 headless run 中 fail closed；
- 将“需要本人聊天确认”作为明确的人机阻塞返回上层；
- 只有恢复到能够展示 `request_user_input` 的交互式 root Codex chat 后才能继续。

非 protected partition 不受这一限制。

## 4. 最小 confirmation binding

单独依赖“模型看见 request_user_input 返回了 Yes”仍然不够，因为 guard 本身必须有一个不可由普通模型文本提前制造的 continuation condition。

v2 使用一个非常小的内部绑定层，但用户完全看不到它。

### 4.1 第一次 guard block

guard 解析到 protected partition 后：

- 不执行 scancel；
- 在 user-private local state 下原子创建一个短寿命 pending record；
- record 只包含：
  - random opaque nonce；
  - exact sorted JobId；
  - resolved Partition；
  - normalized cancel operation；
  - created / expiry；
  - state=pending；
  - expected visible question text / question id；
- guard 返回机器可读：
  - `CHAT_CONFIRMATION_REQUIRED`
  - internal question id / nonce
  - 用户可见 question text。

nonce 不是产品 UI，不要求用户复制。

### 4.2 root Codex 调用 native request_user_input

slurm-workflows 的正常指令只要求 root Codex：

- 收到 `CHAT_CONFIRMATION_REQUIRED` 后，不再尝试任何 bypass；
- 调用 native `request_user_input`；
- question id 使用 guard 给出的 opaque id；
- 用户可见内容只显示 exact JobId / Partition；
- 两个明确选择：
  - “确认取消”
  - “保留 Job”

不把 nonce 放进用户可见文案。

### 4.3 tiny PostToolUse confirmation binder

当前官方 Hooks 和源码都证明 `PostToolUse` 能匹配其他 local function tools；当前 Codex 测试还直接使用：

`matcher = '^request_user_input$'`

PostToolUse input 包含：
- `session_id`
- `turn_id`
- `tool_name`
- `tool_use_id`
- `tool_input`
- `tool_response`

因此增加一个非常小、同步、fail-closed 的 hook：

`slurm-protected-cancel-bind.py`

只匹配 `request_user_input`。

它只有在以下全部成立时才把 pending -> confirmed：

1. tool name 正是 `request_user_input`；
2. tool input 的 opaque question id 对应一个仍有效 pending record；
3. visible question 中 exact JobId / Partition 与 pending record 一致；
4. tool response 对该 question 有**非空明确答案**；
5. 答案精确为“确认取消”（可在实现时固定一个 canonical label，不做模糊 NLP）；
6. record 仍 pending、未过期；
7. 原子写入 confirmed，并记录当前 `session_id / turn_id / tool_use_id` 作为审计定位信息。

以下都不确认：

- `answers={}`；
- “保留 Job”；
- Other / 模糊文本；
- 不匹配的 question id；
- 没有 pending record；
- 已过期 / 已消费 record。

PostToolUse hook 如果失败、超时或没有安装，结果是**没有 confirmed state**，guard 后续仍拒绝 mutation，因此是 fail closed。这里不依赖 hook 的 block/ask 能力。

### 4.4 第二次 ordinary scancel

native request_user_input 返回明确确认后，root Codex 正常重新发出同一：

`scancel 12345`

automation PATH shim 仍使该命令进入中央 guard。

guard：

1. 找到 exact target 的 confirmed pending record；
2. 再次 `scontrol show job -o 12345`；
3. JobId / Partition / operation 必须与 record 一致；
4. 原子 consume；
5. 调用真实 `/usr/bin/scancel 12345` 一次；
6. replay 无 confirmed record，因此拒绝。

模型即使知道 nonce，也不能通过普通文本把 record 改成 confirmed；正常入口下只有 request_user_input 的 PostToolUse binder 会做这一步。

## 5. 为什么这满足“第一次以后新本人确认”

时间顺序有可验证因果关系：

第一次 protected scancel
→ guard 才创建 pending nonce
→ 在此之前初始长 Goal 不可能已经拥有这个 pending id
→ root Codex 才能针对该 pending id 发起 request_user_input
→ tool handler 等待客户端专用 UserInputAnswer
→ PostToolUse 只看到这次 tool 的实际 response 后才可确认
→ 第二次 guard 才可能执行

因此：

- 初始“以后所有 scancel 都确认”没有 pending nonce，不能授权；
- auto_review 处理 command approval，不会生成 `UserInputAnswer`；
- assistant 自己输出“确认”不是 request_user_input response；
- subagent 不能调用 native request_user_input；
- UserPromptSubmit/internal automatic prompt 不写 confirmed state；
- 空 auto-resolution 不确认；
- 只有第一次 block 后、对应 pending request 的客户端明确回答能确认。

本 Proposal 对“本人”的 claim 仍有边界：它信任当前官方 Codex chat client 对 `ToolRequestUserInput` 的专用响应路径，而不是声称同 UID 下任意自造 app-server client 在密码学上一定是本人。生产前必须在用户实际 Longleaf Codex Desktop 客户端验证这一 normal-entry 行为。

## 6. 当前可行性的条件

所以结论是 CONDITIONAL，而不是无条件 YES。

生产前必须直接验证三个条件：

1. **Longleaf 正常 Codex Desktop chat 能实际暴露 request_user_input。**
   当前 Bridge Host Policy 刻意保持 `default_mode_request_user_input=false`，所以 v2 不能假装现状已经可用。必须决定一个最小、可维护的启用方式，并让 Critic 单独审执行包；不能临场修改 Bridge。
2. **当前 Desktop/app-server 客户端真实把 ToolRequestUserInput 展示给用户，并把显式答案作为专用 response 返回。**
   需要 live UI probe，但不能用真实 Slurm mutation。
3. **PostToolUse matcher=request_user_input 在目标 build 上真实收到 tool_input + tool_response。**
   只用一个完全无副作用的 test question 验证即可。

如果三个条件 PASS，则 chat confirmation 可以落地。

如果当前 Bridge 的 intentional `default_mode_request_user_input=false` 不能在不破坏现有全局行为的前提下被项目/插件范围安全开启，则 v2 保持架构不变，返回 Planner 比较最小启用方式；不得退回 terminal confirmer。

## 7. 不选择的其他平台原语

### 7.1 execpolicy prompt

不采用。

`prompt` 仍走当前 approval reviewer；用户环境是 `approvals_reviewer=auto_review`。把全局 reviewer 改成 user 会让大量无关命令增加摩擦，也不是只针对 protected partition 的最小机制。

### 7.2 UserPromptSubmit

不采用为授权源。

没有稳定 human-origin 字段，不能证明是本人新消息。

### 7.3 PreToolUse

只保留为 raw bypass 辅助 deny。

当前官方文档：
- 可 `permissionDecision: "deny"`；
- `permissionDecision: "ask"` 当前不支持；
- specialized tool path 可绕开默认 hook path；
- Python watcher 内部 subprocess 不是新的 Codex tool call。

因此它不能承担 fresh confirmation。

### 7.4 app-server userVerification

不采用。

当前 OpenAI 已有更强的 device verification / P-256 challenge primitive，但当前 native provider 只有 macOS；非 macOS build 的 `platform_supported()` / `device_supported()` 返回 false。Longleaf app-server 在 Linux，不符合当前目标部署，并且 UX 是设备验证而不是用户要的简单 chat confirmation。

### 7.5 MCP elicitation

当前 MCP flow 确实可以走 blocking `request_user_input`，因此技术上可实现。

但为了一个 Slurm confirmation 新增本地 MCP server 会比“已有 native request_user_input + 一个 PostToolUse binder”更重，也会把 standalone skill 扩成新的 MCP runtime。v2 不采用，除非后续直接证据证明 Default-mode native request_user_input 无法以可维护方式启用。

### 7.6 terminal confirmer

明确拒绝。

用户打开 terminal 时本可直接 scancel；让用户复制 challenge 到 wrapper 是错误产品交互。

## 8. scancel guard 仍保持很薄

保护维度仍只有 private：

`protected_cancel_partitions = ["htzhulab"]`

read-only resolution：

`scontrol show job -o <exact JobId>`

必要时 bounded `squeue -j` cross-check。

第一版直接支持：
- ordinary exact JobId；
- explicit exact JobId list；
- read-only 能唯一解析的 exact array element。

第一版 fail closed：
- array parent/range；
- heterogeneous job；
- job step；
- `--user / --partition / --name / --state` 等动态 selector；
- federation / cluster switch；
- 非默认 signal/batch/full mutation。

execute 前必须重新 resolve。

不增加 current-run ownership，不增加 H100/accelerator 保护。

## 9. DII / CARE：只有 ordinary cancellation intent

DII / CARE 不知道：

- protected partition 列表；
- nonce；
- request_user_input；
- user answer；
- confirmed state。

它们只表达：

“业务上现在想 scancel exact JobId。”

automation-only PATH shim 继续把 bare `scancel` 送进中央 guard；用户 ordinary shell 不改。

### 9.1 protected cancellation 必须把控制权交回聊天层

旧 v1 让 watcher 在 guard nonzero 后自己持续 loop，适合 terminal confirmer，但不适合 chat confirmation：如果 Python watcher 一直占着 command tool，root Codex 没机会调用 request_user_input。

因此 v2 的最小 consumer transport contract 改为：

- guard 成功执行真实 scancel：returncode 0，consumer 按原成功路径继续；
- guard 返回 `CHAT_CONFIRMATION_REQUIRED` 或其他 nonzero：consumer 不把目标标记 cancelled，并把 nonzero / guard message **向上返回给 supervising Codex**，结束当前 cancellation attempt；
- supervising interactive root Codex 调 request_user_input；
- 用户确认后，Codex 重启/恢复同一 watcher 或再次发出 ordinary scancel；
- guard re-resolve + consume confirmed state。

consumer 仍不解析 protected partition 或 confirmation；只传播 cancellation command 的 nonzero。

CARE 现有 watcher 最小变化方向：

- B1：scancel nonzero 不加入 `cancelled`，记录后返回非零给 controller，而不是在内部无限重试；
- M7：直接传播 scancel nonzero；
- M8：直接传播 scancel nonzero；
- interactive takeover：nonzero 不进入 CANCELLED accounting wait/launch，返回非零；
- cascade formal race：任何取消 action nonzero 时结束本轮 watcher 并传播非零，不继续 interval loop 吞掉 chat blocker。

用户确认后由现有 Goal/controller resume 重新进入，不建立新 daemon/state machine。

### 9.2 headless automation

纯 `codex exec` 当前不能 request_user_input。

因此：
- 非 protected cancellation 仍正常自动；
- protected cancellation 必须 fail closed；
- headless run 输出明确 `NEEDS_INTERACTIVE_CHAT_CONFIRMATION`；
- 不自动改用 terminal、auto_review 或其它确认；
- 只有恢复到 interactive root Codex chat 后才能继续。

这是用户要求“protected cancellation 必须本人聊天确认”的必要代价，不是产品失败。

## 10. Codex normal-entry bypass control

保留原正确方向：

- raw `scancel` / confirmed system `/usr/bin/scancel` 在 Codex normal entry 禁止直接绕过 guard；
- automation PATH 中 bare scancel 解析到 guard；
- 用户 ordinary shell 不受影响；
- PreToolUse 可作为额外 raw bypass deny，但不是唯一安全边界。

confirmation binder hook 本身不得提供普通 CLI “confirm”入口，也不得让模型通过一个 shell command直接写 confirmed state。

最终仍只声明 verified Codex/consumer normal-entry protection，不声称 same-UID OS-level unbypassable。

## 11. 四项 Capability Gate

不新增第五 Gate。

### Gate A：partition routing

必须证明：

1. fake `a100-gpu` exact job 在原 Goal 已授权取消时不新增 chat confirmation。
2. fake `htzhulab` exact job 第一次一定不 mutation。
3. 第一次结果含 exact JobId / Partition 和 internal pending id。
4. long initial blanket approval 不能跳过第一次 block。

### Gate B：native fresh chat confirmation

必须证明：

1. target interactive root Codex 能展示 native request_user_input。
2. initial Goal / assistant text / auto_review / UserPromptSubmit / subagent 不能写 confirmed state。
3. request_user_input question 的 visible JobId / Partition 与 pending record exact 匹配。
4. 空 answers / timeout / “保留 Job”不能确认。
5. 用户显式“确认取消”后 PostToolUse binder 才原子 pending -> confirmed。
6. confirmed 后下一 ordinary scancel re-resolve 后最多执行一次。
7. replay / expiry / JobId / Partition / operation 变化失效。
8. Default-mode feature/client/hook 任一不可用时 fail closed，不回退 terminal wrapper。

### Gate C：consumer / runtime coverage

必须证明：

1. required DII/CARE automation bare scancel 实际解析 guard。
2. protected cancellation nonzero 能退出当前 consumer cancellation attempt并回到 supervising interactive Codex，而不是被 watcher 内部吞掉。
3. 用户确认后正常 resume / rerun 能再次 ordinary scancel。
4. headless `codex exec` protected cancel 只产生 NEEDS_INTERACTIVE_CHAT_CONFIRMATION，不 mutation。
5. raw system scancel 在 Codex normal entry不能绕 guard。
6. user ordinary shell仍可直接使用系统 scancel。

### Gate D：target integrity / claim truth

必须证明：

1. multiple exact IDs 任一 protected => 整组 fresh confirmation。
2. complex selector fail closed。
3. cancellation 执行前 re-resolve。
4. destructive path只在真正隔离 fake Slurm运行。
5. Longleaf production验证不使用真实 htzhulab cancellation。
6. final claim 不扩大到 same-UID OS-level unbypassability，也不宣称 headless automation 能自行完成 protected cancellation。

## 12. 最小内部状态

用户不接触任何 challenge。

允许存在一个很小的短寿命 pending record，仅用于：

- bind exact target / partition；
- bind hidden nonce / request id；
- PostToolUse 写 confirmed；
- guard one-time consume。

它不是 approval database，不跨机器同步，不形成长期授权，不需要后台进程。

如果没有 pending record，就不存在可用 confirmation。

## 13. v1/v0 资产处置

保留：
- exact JobId/Partition read-only resolution；
- private protected_cancel_partitions 方向；
- automation PATH shim 思路；
- raw bypass Codex policy；
- fake Slurm / consumer inventory；
- rejected old incident regressions。

删除/废弃：
- terminal `ai-slurm-confirm-cancel` 用户流程；
- 用户复制 challenge；
- terminal pending->confirmed；
- current-run ownership；
- protected accelerator / H100；
- old three-state safe-cancel；
- confirmation receipt execution authority；
- consumer-specific partition policy。

被否决 package `4d940d7510e29f74a14c5b5070a1a9671f3f27e7` 永久不能作为 execution authorization。

## 14. Capability/平台 probe 要求

Proposal PASS 后的 execution package 在实施前必须包含一个**无 Slurm mutation**的小 probe：

- 在目标 Longleaf Codex Desktop normal chat 中确认 Default mode request_user_input 的真实可用性；
- 若需要启用 `default_mode_request_user_input`，必须明确它与当前 Bridge Host Policy “false is intentional” 的冲突和最小可维护处理，不能临场改全局 config；
- 用 harmless question 验证 client 专用 response；
- 用 PostToolUse matcher `^request_user_input$` 验证 tool_input/tool_response；
- 空 auto-resolution 不产生 confirmed state；
- `codex exec` 路径确认 fail closed。

这项 probe 先于任何 Host Policy/private config/consumer production deployment。

如果 probe 失败，返回 Planner；不改用 terminal confirmation。

## 15. Maintenance truth

当前 `docs/skill-todos/slurm-workflows.md` 仍为：

`tracking issue: PENDING_CLEAR_WRITING`

其中旧 H100 描述已被用户最新要求 supersede，不能反向覆盖本 Proposal。当前运行面仍没有真实 Clear Writing 入口，因此不创建/伪造 Issue、DOING、ADAPTING 或 DONE。

下一具真实 Clear Writing + Project 能力的 Maintainer 应先按用户最新 protected-partition-only 语义更新 reader-facing tracking copy，再创建独立 Issue、不复用 #96、回填真实 `tracking: #N`。

## 16. 不实施

本轮只提交 Proposal v2。

不创建 branch/worktree；不修改 Host Policy、Bridge source、Codex config、hooks、private override、DII/CARE；不运行 Codex probe；不运行任何 Slurm mutation。

## 17. 主要直接证据

OpenAI Codex source reviewed：
`8c076942cb70fba8e5c4732c23f1faabc4aed484`

关键文件：

- `codex-rs/core/src/tools/handlers/request_user_input.rs`
  - root-only；
  - await `session.request_user_input`；
  - explicit response；
  - optional VerifiedAnswer retention。
- `codex-rs/core/tests/suite/request_user_input.rs`
  - `Op::UserInputAnswer` round-trip；
  - Default mode feature gating。
- `codex-rs/app-server/tests/suite/v2/request_user_input.rs`
  - app-server `ToolRequestUserInput` request / dedicated client response；
  - Default mode feature true 时可用。
- `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs`
  - Default nonblocking request auto-resolution produces empty answers。
- `codex-rs/prompts/templates/guardian/classifier_instructions.md`
  - request_user_input responses are trusted content that can establish user_authorization。
- `codex-rs/exec/src/lib.rs`
  - request_user_input unsupported in exec mode。
- `codex-rs/hooks/src/events/post_tool_use.rs` / `hooks/src/schema.rs`
  - PostToolUse receives tool_input + tool_response。
- `codex-rs/app-server/tests/suite/v2/guardian_v2.rs`
  - current test configuration explicitly supports PostToolUse matcher `^request_user_input$`。
- `codex-rs/user-verification/src/lib.rs`
  - current native device verification provider is macOS-only。

Official documentation reviewed 2026-10-18：

- Hooks: https://developers.openai.com/codex/hooks
  - PreToolUse / PostToolUse tool coverage；
  - PostToolUse observes local function tools；
  - PreToolUse `permissionDecision:"ask"` unsupported。
- Rules: https://developers.openai.com/codex/rules
  - decisions allow/prompt/forbidden；
  - most restrictive matching rule wins。
- App Server architecture: https://openai.com/index/unlocking-the-codex-harness/
  - server requests pause/route consequential UI interactions through clients。

Bridge Kit current main reviewed：
`f67ac9155c1a844f171afbeef03e8169b8eec6fc`

Current Bridge `AGENTS.md` explicitly keeps:
`default_mode_request_user_input=false`
and says Default-mode HUMAN_ONLY input currently uses plain-text stop semantics. This is precisely why production feasibility remains CONDITIONAL until a bounded, reviewed activation strategy is proven.
