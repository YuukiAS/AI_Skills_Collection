# Slurm Workflows：受保护分区聊天二次确认 Execution Plan v2

日期：2026-10-18
task：hpc--slurm-cancel-production-closure
owner：YuukiAS/AI_Skills_Collection standalone skill slurm-workflows
approved Proposal：docs/design/slurm-workflows/SLURM_PROTECTED_PARTITION_CHAT_CONFIRMATION_PROPOSAL_V2_2026-10-18.md
approved Proposal commit：5692e7441d33b115df9220bd18d9fd8b872019b8
approved Proposal blob：bc62264c6010b3e5371885899138f72c03095250
execution-package preparation base：3ac112b38b44f4feffd34a7c0a91eb663a0dedc6
Repository version baseline：5.4.5
状态：EXECUTION_PACKAGE / AUTHORIZED_ONLY_AFTER_CRITIC_PASS_AND_USER_SEND / PHASE_0_TO_3_ONLY

被否决旧 execution package：

4d940d7510e29f74a14c5b5070a1a9671f3f27e7 = REJECTED_FOR_EXECUTION

旧 Kickoff、terminal confirmer、v1 pending->confirmed terminal 流程永久不得复活。

## 1. 冻结产品行为

Longleaf 私有保护值：

protected_cancel_partitions = ["htzhulab"]

产品因果链：

1. Codex / automation 产生 ordinary scancel <exact JobId> intent。
2. 中央 guard 用 scontrol show job -o <JobId> 只读解析 exact target 与真实 Partition。
3. non-protected：
   - 不新增 protected-cancel 二次确认；
   - 当前 Goal / 既有权限本来允许时正常调用真实 /usr/bin/scancel。
4. protected：
   - 第一次绝不 mutation；
   - 创建用户不可见的短寿命 pending record；
   - 返回 CHAT_CONFIRMATION_REQUIRED 与 exact JobId / Partition / opaque question id。
5. interactive root Codex 使用 native request_user_input 显示：
   - “确认取消”
   - “保留 Job”
6. 只有这次专用客户端 request 的明确“确认取消”回答，经过 tiny synchronous PostToolUse binder 后，才把该 pending record 原子改为 confirmed。
7. 再次 ordinary scancel 时，guard 重新只读解析 exact JobId / Partition / operation；完全一致才 one-time consume 后调用 /usr/bin/scancel。
8. replay、expired、empty answer、保留、wrong question、target/Partition/operation 变化全部 fail closed。

用户永远不复制 nonce/challenge、不打开 terminal 执行 confirmation wrapper、不手工维护状态。

不允许重新引入 H100/accelerator 保护、current-run ownership、owned-job-id、旧三态 safe-cancel、terminal confirmer、MCP server、database/daemon/broker 或第五个 Capability Gate。

## 2. 冻结 source 与全新执行身份

### AI_Skills_Collection

下一 execution-ready Critic 必须把 APPROVED_COMMIT 绑定到最终 execution package commit 本身。

执行时要求：
origin/main == APPROVED_COMMIT

R：
/overflow/htzhu/mingcheng_new/AI_Skills_Collection

branch：
work/hpc--slurm-protected-partition-chat-confirmation

W：
/overflow/htzhu/mingcheng_new/AI_Skills_Collection-hpc--slurm-protected-partition-chat-confirmation

### DII

frozen source：
747829b957b19e8fcffa6bd5f1bb7ae62ae11f6f

R：
/users/a/e/aereinh/Distributed_Imaging_Inference

branch：
work/hpc--slurm-protected-partition-chat-confirmation

W：
/users/a/e/aereinh/Distributed_Imaging_Inference-hpc--slurm-protected-partition-chat-confirmation

### CARE

frozen source：
75a40e454de43b64e59a0b0b438ff57ef2bb8345

R：
/users/a/e/aereinh/CARE

branch：
work/hpc--slurm-protected-partition-chat-confirmation

W：
/users/a/e/aereinh/CARE-hpc--slurm-protected-partition-chat-confirmation

### 外部平台 source

OpenAI Codex：
8c076942cb70fba8e5c4732c23f1faabc4aed484

Bridge Kit：
f67ac9155c1a844f171afbeef03e8169b8eec6fc

Bridge Kit source 本任务 NO_CHANGE。

三个新 work/hpc--slurm-protected-partition-chat-confirmation remote branch 在 execution package 准备时均不存在。任何 source drift、dirty worktree、同名 branch/worktree/remote collision、lineage mismatch 都 fail closed。

## 3. 配置层决定：不修改 Bridge 全局 false

Bridge 当前有意保持：

default_mode_request_user_input=false

v2 不修改 Bridge source，也不把用户级 $CODEX_HOME/config.toml 全局改成 true。

当前 OpenAI config loader 的 precedence 明确是：

SessionFlags > Project .codex/config.toml > User config。

因此 v2 使用可信项目范围配置，只在需要该能力的适配仓库加入：

.codex/config.toml

内容只增加：

[features]
default_mode_request_user_input = true

这样：

- Bridge 管理的 user-level false 保持不变；
- 只有已适配、受信任项目的 fresh Codex thread 启用 native request_user_input；
- DII/CARE/AI Skills 的变化都进入可审 Git diff；
- 回滚就是恢复/删除该项目文件；
- 未适配仓库继续 fail closed，不被宣称已保护。

如果目标 Codex build / project trust / config origin readback 证明 Project layer 不能覆盖当前 User layer，Phase 0 直接 FAIL，返回 Planner；不得改全局 user config 兜底。

## 4. Phase 0：真实客户端 capability probe，先于产品实现

Phase 0 必须先通过；失败不得继续 Phase 1。

本阶段无任何 Slurm mutation，也不运行 fake scancel destructive replay。

### 4.1 只准备 probe surface

在 AI Skills 新 task worktree 内允许新增 task-owned probe 文件：

- project-local .codex/config.toml，仅开启 default_mode_request_user_input=true；
- project-local .codex/hooks.json，只注册 harmless PostToolUse matcher ^request_user_input$ 的 probe logger；
- 一个 probe logger，只把收到的 session_id / turn_id / tool_use_id / tool_input / tool_response 写入 task results；不得修改确认状态、不得调用 Slurm、不得联网；
- task result path：results/hpc--slurm-cancel-production-closure/chat-confirmation-probe/。

probe hook 只用于证明平台能力，不是最终 binder。

执行前必须通过 config/hook discovery readback 证明：
- AI Skills worktree 被当前 Codex 视为 trusted project；
- effective feature origin 是该 Project layer；
- Bridge user-level false 没被修改；
- probe hook 来源是该 task worktree。

### 4.2 actual Longleaf Codex Desktop normal-chat probe

必须使用 fresh Longleaf Codex Desktop interactive root chat，cwd/root 指向 AI Skills task worktree。

当前线程如果已经在 feature enablement 之前创建，不得假装热加载；优先使用支持的 fresh thread/session。不得 kill/restart 正在工作的 app-server。

如果平台无法由当前 Executor 自行创建并把 fresh Desktop chat 展示给用户，则 Executor 停在：

PROBE_READY_FOR_USER_CHAT

并只要求用户执行一个最小动作：在 Longleaf_Codex 中打开这个 exact task worktree 的新聊天并发送指定 harmless probe prompt。不得让用户打开 terminal。

harmless probe 只问与 Slurm 无关的问题，例如：

“这是聊天确认能力测试。请选择‘确认测试’或‘取消测试’。”

必须直接证明：

1. Default mode 中 request_user_input 实际暴露；
2. Desktop UI 显示原生问题；
3. 用户显式选择“确认测试”后 dedicated response 返回；
4. PostToolUse probe logger 收到 exact tool_input + tool_response + session/turn/tool_use id；
5. 另一轮故意不回答直到 auto-resolution，得到 empty answers；
6. empty answers 不被 probe 判作确认；
7. probe 不修改任何 Slurm/生产配置。

### 4.3 headless negative probe

只做无 Slurm 的能力检查，确认当前 codex exec 路径不能完成 request_user_input，并把该事实冻结为：

HEADLESS_PROTECTED_CANCEL = NEEDS_INTERACTIVE_CHAT_CONFIRMATION

不得为通过 probe 而给 codex exec 增加 terminal/approval fallback。

### 4.4 Phase 0 判定

PASS 需要上述 1–7 和 headless negative probe 全部成立。

任何一项失败：
- 停止；
- 不进入产品实现；
- 输出 direct evidence；
- 返回 Planner；
- 不 fallback 到 terminal confirmer、UserPromptSubmit、execpolicy prompt、MCP server 或全局 user config。

## 5. Phase 1：中央候选实现

仅 Phase 0 PASS 后实施。

### 5.1 thin guard

在现有 slurm-workflows 内实现一个小型中央 executable，例如：

ai-slurm-scancel

职责：

- 接收 v2 支持的 exact target；
- read-only Slurm resolution；
- 读取 protected_cancel_partitions；
- non-protected exact forwarding；
- protected first-block / pending record；
- confirmed revalidation / one-time consume；
- 最终只调用真实 /usr/bin/scancel。

支持：

- ordinary exact JobId；
- explicit exact JobId list；
- read-only 唯一定位的 exact array element。

fail closed：

- array parent/range；
- heterogeneous；
- job step；
- dynamic selectors；
- federation/cluster switching；
- non-default signal/batch/full mutation。

execute 前再次 scontrol show job -o，必要时 bounded squeue -j cross-check。清除会扩大 target/filter 的 SCANCEL_* 环境变量。

### 5.2 internal pending record

用户不可见、短寿命、本地 user-private state。

只含：

- random opaque nonce；
- opaque question id；
- exact sorted JobId；
- resolved Partition set；
- normalized operation；
- created/expiry；
- pending/confirmed/consumed；
- confirmed 时记录 session_id / turn_id / tool_use_id。

要求：

- 0700 state root / user-only files；
- atomic create/update/consume；
- bounded expiry；
- consumed 不复活；
- target/Partition/operation 变化失效；
- confirmed authority 不能只是一个普通 Codex shell 可直接改写的布尔字段或纯文本；
- direct binder executable 被 Codex project rules 禁止只是第一层，仍必须有回归证明：普通 Codex normal shell 即使知道 question id、state 路径和文件格式，也不能制造一个 guard 会接受的 confirmed authority；
- 如果在当前平台边界内无法证明这点，Phase 1 必须停止回 Planner，不得以“同 UID 无法绝对隔离”为理由降级接受伪造路径。

它不是数据库、长期授权或跨机器 service。实现可以利用当前 Codex 已有的 request_user_input / PostToolUse 可信事件证据完成绑定，但不得新增 daemon/broker/MCP server 或把确认权交给普通 shell。

### 5.3 native question contract

guard 返回 protected block 时输出机器可读：

NEEDS_INTERACTIVE_CHAT_CONFIRMATION

并包含：

- opaque question id；
- exact JobId；
- exact resolved Partition；
- canonical visible question；
- canonical labels：
  - 确认取消
  - 保留 Job

skill/runtime instruction 只允许 interactive root Codex 调 native request_user_input。

empty / timeout / other/free-text / retain 都不算确认。实现第一版不做模糊 NLP。

### 5.4 tiny synchronous PostToolUse binder

最终 binder 是中央 executable，不由 consumer 复制逻辑。

项目 .codex/hooks.json 只注册：

- event：PostToolUse
- matcher：^request_user_input$
- command：exact installed/reviewed central binder executable。

binder 只有在全部匹配时 pending -> confirmed：

- exact question id；
- exact JobId；
- exact Partition；
- exact normalized operation；
- pending 且未过期；
- response 对 exact question 非空；
- canonical answer 精确为 确认取消。

其它全部不确认。

hook 未安装、未信任、失败、timeout、response malformed：
confirmed state 不产生，guard 后续继续 fail closed。

binder 本身不执行 Slurm mutation。

## 6. project-local normal-entry enforcement

为了不改 Bridge user-level Host Policy，AI Skills、DII、CARE 三个适配仓库最终 candidate 都使用可信 project-local .codex：

1. .codex/config.toml
   - default_mode_request_user_input=true
2. .codex/hooks.json
   - 只注册中央 request_user_input binder
3. .codex/rules/slurm-protected-cancel.rules
   - Codex normal entry raw scancel => forbidden
   - actual system /usr/bin/scancel => forbidden
   - direct binder executable => forbidden
   - justification 指向 ai-slurm-scancel

不得 blanket allow guard；non-protected cancellation 继续服从原 Goal/approval 语义。

必须用实际 config/read / hooks/list / codex execpolicy check 或同等正式入口证明 project layer 已加载。

用户 ordinary shell 不读取 Codex project execpolicy，因此普通 shell 的系统 scancel 不受本机制限制。

## 7. automation PATH shim

中央候选提供 automation-only shim directory：

scancel -> ai-slurm-scancel

只给 Codex/DII/CARE automation process prepend，不替换系统 /usr/bin/scancel，不改用户普通 shell PATH。

每个 required consumer 必须用 runtime evidence 证明：

command -v scancel

和 Python：

shutil.which("scancel")

解析到 exact reviewed shim。

若某 launcher 无法可靠继承 PATH，只允许最小 launcher/executable-resolution 修复；不得复制 protected policy。

## 8. DII / CARE consumer contract

consumer 只表达 ordinary cancellation intent，不解析 protected partition、nonce、question、answer 或 confirmation。

### DII

只允许：

- exact central candidate 安装/同步；
- project-local feature/hook/rules adapter；
- automation PATH / launcher resolution；
- standing race 继续表达普通 loser cancellation。

若新 source scan 出现 hardcoded /usr/bin/scancel、SSH scancel 或 Slurm API cancel，停止并回 Planner。

### CARE

protected guard nonzero 不能在 watcher 内部吞掉，因为 root interactive Codex 必须重新取得控制权并发起 native question。

冻结最小修复：

- B1：scancel nonzero 不加入 cancelled，将 nonzero 与 guard 输出传播给 supervising Codex，结束本次 watcher cancellation attempt；
- M7：scancel nonzero 直接传播；
- M8：scancel nonzero 直接传播；
- interactive takeover：nonzero 不进入 sacct CANCELLED wait / launch，直接传播；
- cascade formal race：cancel nonzero 时结束当前 watcher round 并传播，不继续内部 interval loop 吞掉 blocker。

non-protected scancel returncode 0 时原正常状态机完全保持。

supervising interactive root Codex 收到 NEEDS_INTERACTIVE_CHAT_CONFIRMATION 后才调用 request_user_input。用户确认后由现有 Goal/controller resume/rerun ordinary cancellation intent。

## 9. headless behavior

codex exec 当前不支持 native request_user_input。

因此：

- non-protected job：无新增确认；
- protected job：guard 第一次 block；
- headless supervisor 必须输出 NEEDS_INTERACTIVE_CHAT_CONFIRMATION 并停止 protected cancellation；
- 不 fallback terminal、auto_review、UserPromptSubmit 或 approval prompt。

只有 interactive root Codex chat 能继续。

## 10. 四项 Capability Gate

### Gate A：partition routing

必须证明：

- fake non-protected exact job 在原授权下不新增 chat confirmation；
- fake htzhulab exact job 第一次零 mutation；
- exact JobId / Partition / opaque pending id 正确；
- initial blanket approval 不能跳过 first block。

### Gate B：native fresh chat confirmation

必须证明：

- target Longleaf Codex Desktop fresh Default-mode chat 原生 question 可见；
- dedicated explicit response 能返回；
- PostToolUse binder 收到 exact tool input/response；
- initial Goal、assistant text、auto_review、UserPromptSubmit、subagent 都不能 confirm；
- empty/timeout/retain/wrong question/expired 不 confirm；
- canonical “确认取消”才 pending -> confirmed；
- ordinary Codex normal shell 直接调用 binder、改写 state、伪造 question/answer 文件都不能产生 guard 可接受的 confirmed authority；
- confirmed 后 next ordinary scancel re-resolve 后最多执行一次；
- replay / target / Partition / operation change 拒绝。

### Gate C：consumer/runtime coverage

必须证明：

- AI Skills/DII/CARE trusted project config/hook/rules 真正加载；
- raw system scancel 在 Codex normal entry forbidden；
- binder direct invocation在 Codex normal entry forbidden；
- automation bare scancel解析 reviewed shim；
- protected nonzero 从 CARE 五个 watcher 返回 supervising Codex，不被内部 loop 吞掉；
- headless protected flow fail closed；
- user ordinary shell system scancel 不受影响。

### Gate D：target integrity / claim truth

必须证明：

- explicit multiple IDs 任一 protected => 整组 fresh confirmation；
- complex selector fail closed；
- execute 前 re-resolve；
- destructive replay 只在真正隔离 fake Slurm；
- Longleaf live validation不真实取消任何 job；
- final claim 只覆盖 verified interactive Codex/required consumer normal entry；
- 不声称 same-UID OS-level unbypassable，也不声称 headless 可自行完成 protected cancellation。

不新增第五 Gate。

## 11. destructive replay isolation

实际调用 fake scancel / subprocess destructive path 仅允许在：

- network disabled；
- isolated PID namespace；
- 无生产 SSH key/agent/token；
- 无真实 Slurm/MUNGE/controller/socket；
- 无 host control socket；
- 无 production writable mounts；
- fake Slurm only。

不能证明则该 destructive replay 标记 BLOCKED_BY_ISOLATION，不转 Longleaf 真机。

Phase 0 live chat probe不涉及 Slurm，允许在真实 Longleaf Codex Desktop进行。

## 12. 实施阶段与授权

### Phase 0：capability probe

由 approved Kickoff 授权：
- 先只创建 AI Skills 新 task worktree/branch；
- 对 DII/CARE 只做 source/branch/worktree 的只读 preflight，Phase 0 PASS 前不创建其 worktree；
- AI Skills worktree 先准备 harmless project-local feature/hook probe；
- 执行真实 Desktop chat probe；
- headless negative probe。

Phase 0 FAIL => STOP / Planner。

### Phase 1：candidate implementation

只在 Phase 0 PASS 后继续：
- 再创建 DII/CARE 冻结的 exact task branch/worktree；
- central guard/pending/binder/private field/shim；
- AI Skills/DII/CARE project-local config/hook/rules；
- DII/CARE consumer minimal transport fixes。

不写 production private protected partition，不安装 production central candidate，不集成 main。

### Phase 2：deterministic + isolated fake validation

完成 Gate A-D 开发期证据，冻结三仓 candidate commits。

### Phase 3：mandatory independent Reviewer

每个新 task branch最多一次普通同名非强制 first remote publication：

git push --set-upstream origin work/hpc--slurm-protected-partition-chat-confirmation

前提：
- exact repo/origin/branch/lineage/clean；
- same-name remote branch 不存在。

禁止 force/force-with-lease/delete/tag/history rewrite/其它 remote。

Reviewer 检查 Proposal、Plan、三仓 diff、Phase 0 live probe、Gate A-D、isolation、rollback、production activation proposal。

当前 Kickoff 到此停止。

### Phase 4：production activation — 需要第二条短用户授权

即使 Phase 3 Reviewer PASS，也不得自动部署。

第二条短 production authorization 必须绑定 exact reviewed central/DII/CARE commits，只允许：

- backup task-owned user-local AI Skills install / private override；
- 安装 exact reviewed central candidate；
- 在实际 Longleaf private override 写 protected_cancel_partitions=["htzhulab"]，保留其它字段；
- 集成 exact reviewed AI Skills/DII/CARE project-local config/hook/rules 与 consumer commits；
- 配置 exact reviewed automation PATH shim；
- 只读 production validation；
- 不真实取消任何 Slurm job。

不修改 Bridge source或 user-level $CODEX_HOME/config.toml / ai-bridge-global.rules / user-level hooks。

### Phase 5：release closure

完整 production Gate A-D 后才：

- slurm-workflows 0.4 -> 0.5
- Repository -> release-time next PATCH；若仍为 5.4.5，则 5.4.6
- central Plugins NO_BUMP
- Bridge Kit NO_CHANGE
- README/CHANGELOG/version/generated closure 最后执行

release metadata 不得夹带产品行为变化。

## 13. rollback

### capability probe rollback

仅恢复/删除 AI Skills task worktree中本 probe 新增的：
- .codex/config.toml
- .codex/hooks.json
- probe logger/result。

不修改用户级 Bridge config。

### candidate rollback

删除/弃用 task worktrees/branches即可；未获 production authorization前不存在 live production install。

### production rollback

只恢复本任务实际改变的：
- central installed candidate；
- private local override；
- AI Skills/DII/CARE exact reviewed project-local config/hook/rules/consumer integration；
- automation PATH launcher。

不执行 Slurm mutation，不改 MUNGE/SSH/Unix identity，不改 Bridge source。

## 14. Maintenance truth

当前仍：

tracking issue: PENDING_CLEAR_WRITING

旧 TODO 中 H100 文案已被用户最新 protected-partition-only 合同 supersede，不得反向覆盖 v2。

没有真实 Clear Writing / Project mutation能力时：
- 不伪造 Issue；
- 不伪造 DOING/ADAPTING/DONE；
- technical closure 时输出 exact pending mutation 给下一具合法 Maintainer；
- 不要求用户手工维护。

## 15. 停止条件

任一出现立即停止并回 Planner/Critic：

- approved Proposal blob != bc62264c6010b3e5371885899138f72c03095250；
- AI execution base != execution-ready Critic APPROVED_COMMIT；
- DII/CARE source drift；
- target branch/worktree collision；
- Phase 0 Desktop native question不可用；
- Project config无法在不修改 Bridge user-level false 的情况下启用 feature；
- PostToolUse matcher无法取得 request_user_input tool input/response；
- empty answer可能产生 confirmed；
- binder可被普通 Codex shell入口直接伪造；
- required consumer无法把 protected nonzero返回 interactive supervisor；
- 需要 terminal confirmer、MCP server、UserPromptSubmit authorization、H100/current-run/三态；
- destructive test需要真实 Slurm；
- 任何真实 cancellation/signal/requeue/release/test allocation；
- 需要 daemon/database/broker或第五 Gate；
- 需要 Bridge source change；
- 需要付费模型/API。
