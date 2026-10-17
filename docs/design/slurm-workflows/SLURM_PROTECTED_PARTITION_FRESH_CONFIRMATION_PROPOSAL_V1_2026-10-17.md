# Slurm Workflows：受保护分区取消二次确认架构 Proposal v1

日期：2026-10-17  
task：hpc--slurm-cancel-production-closure  
owner：YuukiAS/AI_Skills_Collection standalone slurm-workflows  
source revision read：main@11013e1caaaee4293d6249dfdc2a85351302c226  
external source identities at R1 revision：DII main@747829b957b19e8fcffa6bd5f1bb7ae62ae11f6f；CARE main@75a40e454de43b64e59a0b0b438ff57ef2bb8345；Bridge Kit main@24b703235a7e6a583653c59d560c809304cf6db3  
阶段：架构纠偏设计；EXECUTION_NOT_AUTHORIZED

旧 Phase 3 候选全部标记为 REJECTED_NOT_DEPLOYABLE：

- AI Skills b4815a35f708078184bff27b34f185fea6938cc3
- DII e04f6a8da729c05a9e286b38c2c14cfd9ab13d31
- CARE 74d2948def67502070c06336866638f0869d9481

## 0. Planner 结论

OLD_PRODUCTION_DESIGN = REJECT

RECOMMENDED_ARCHITECTURE = partition-only scancel guard + fresh one-time challenge + trusted human-confirmation adapter + Codex-scoped raw-scancel deny + auxiliary PreToolUse

旧设计的核心产品语义应被推翻，而不是继续修补。旧实现把“取消是否需要二次确认”同时绑定到 current-run ownership、protected accelerator、三态 safe-cancel、confirmation receipt 等维度，超出了用户真正要求；DII/CARE 又被迫理解中央保护决策，导致逻辑扩散。

新的产品规则只看一件事：当前将被取消的 exact Slurm target 是否属于用户私有配置中的 protected partition。

Longleaf 第一条私有规则仅为：

protected_cancel_partitions = ["htzhulab"]

不继承 H100 跨 partition 特例，不继承 current-run ownership 特例。未命中 protected partition 时，guard 不新增二次确认；当前 Goal 是否已经允许取消仍由原任务和 Host Policy 决定。

本轮研究同时发现一个重要的平台事实：截至 2026-10-17，stock Codex 的 UserPromptSubmit 不能作为“该文本一定由人类本人直接发送”的可靠证明。OpenAI 当前 hook schema 暴露 prompt、session_id、turn_id 和可选 subagent metadata，却没有稳定的 origin=human 字段；OpenAI 公开 issue #29640 仍然 open，明确记录 UserPromptSubmit 可以对 Codex-originated subagent prompt 触发，并请求新增 human-only event / origin metadata。Codex 内部其实已经维护 UserInputMetadata.origin，但当前 UserPromptSubmit hook payload 没有暴露它。

因此，不能把 UserPromptSubmit + challenge 直接宣传成已经证明的本人二次确认通道。这样会再次用“看起来像安全机制”的接口冒充真实能力。

Proposal v1 把“薄 guard”和“本人确认 transport”分开：guard 与 challenge 机制现在就可以正确设计；当前可部署的人类确认 transport 使用独立用户 shell 的一次性确认命令。未来 OpenAI 若提供稳定 human-origin hook/event，只替换 confirmation adapter，不改变 guard、Slurm target resolution 或消费者架构。

如果用户最终坚持“必须只靠聊天新消息完成确认”，当前 stock Codex 平台能力应如实标为 BLOCKED，而不是伪造保证。

## 1. 用户产品合同

对每个自动取消请求：

1. 先得到 exact JobId 集合。
2. guard 用只读 Slurm 查询取得当前 target 的 Partition。
3. 所有 target 都不命中 protected_cancel_partitions：
   - guard 不增加任何二次确认；
   - 在当前 Goal / Host Policy 已允许取消的前提下，按原始 exact target 正常调用真实 /usr/bin/scancel。
4. 任一 target 命中 protected partition：
   - 第一次 guard 调用绝不执行取消；
   - 生成 fresh random challenge，只绑定这次 exact JobId 集合、解析出的 partition 集合和规范化取消动作；
   - 显示一条很短的本人确认请求；
   - 没有后续新的可信本人动作时保持不执行。
5. 本人确认后再次调用 guard：
   - 重新只读解析 exact JobId / Partition；
   - target 或 partition 与 challenge 绑定不一致则旧 challenge 立即失效；
   - 一致才一次性消费 challenge，并执行这一组 exact cancellation；
   - 消费后重放拒绝。

Standing race opt-in、长 Goal 的“以后全部确认”、auto-review、模型文本、Hook 自己输出、历史授权都不进入 challenge 的 confirmed 状态。

## 2. UserPromptSubmit：研究结论与边界

### 2.1 它能做什么

OpenAI 当前正式 Hooks 文档支持同步 UserPromptSubmit。输入包含 prompt、session_id、turn_id、permission_mode；当前源码还会在 subagent 情况提供可选 agent_id / agent_type。

普通 assistant 输出不会自动变成同一 turn 的 UserPromptSubmit，因此“模型在回答里自己写一句确认”本身不能触发该 hook。随机 challenge 也能阻止初始长 Goal 提前准确写入尚未产生的 challenge。

### 2.2 它为什么当前不能成为授权来源

OpenAI issue #29640 仍 open：当前 UserPromptSubmit 可以对 human prompt 和 Codex-originated subagent prompt 都触发；官方公开 hook input 没有稳定 human-origin 字段。当前 core 内部存在 UserInputMetadata.origin，但 hook payload 不传出该值。

即使过滤 agent_type != null，也不能把 agent_type == null 等价为“本人输入”：内部自动输入、future Goal/automation 行为和客户端产生的输入没有一个被官方合同承诺为稳定的人类来源判据。

因此：

- UserPromptSubmit 不是 v1 的 authoritative confirmer；
- 可以作为将来的 adapter 候选和非阻断可观测信号；
- 在 OpenAI 暴露并稳定支持 human-origin metadata 或 HumanPromptSubmit 之前，不允许由它写入可消费的 protected-cancel confirmation。

这是本 Proposal 与用户最初候选架构唯一的实质纠偏：要证明“本人”，必须先有真实 human-origin primitive；事件名字本身不够。

## 3. 当前可部署的 fresh-human adapter

为避免新增 daemon、broker 或 database，当前 confirmation transport 只增加一个极薄的用户命令，例如：

ai-skills slurm confirm-cancel <job-id-list> <challenge>

流程：

1. guard 第一次命中 protected partition 后写一个本地 pending challenge 小文件。
2. 输出一行短请求，例如：
   Job 12345 当前 Partition=htzhulab。若确认本次取消，请在你自己的终端运行：ai-skills slurm confirm-cancel 12345 <challenge>
3. confirmation command 只把 pending challenge 原子地改为 confirmed；它自己不运行 Slurm mutation。
4. Codex/watcher 下一次调用 guard 时重新读 Slurm target，确认 JobId / Partition 未变化，原子消费 confirmation 后执行一次真实 /usr/bin/scancel。

challenge 状态只是少量 host-local 文件，不是数据库：

- 随机 128-bit challenge；
- exact sorted target IDs；
- resolved partition set；
- normalized operation；
- created / expiry；
- pending / confirmed / consumed；
- 原子 rename / file lock；
- stale challenge 自动清理。

不记录 current-run ownership，不记录 accelerator family，不保存长期“以后都同意”的授权。

Codex normal entry 必须禁止直接调用这个 human-confirm command；用户独立 shell 不受 Codex Host Policy 影响。这个边界仍然不是同 UID 的 OS 级绝对隔离，最终 claim 只覆盖经过验证的 Codex/consumer normal entry。

如果用户明确拒绝独立 terminal confirmation，并坚持 chat-only，则方案停止在 guard/challenge，记录：

CHAT_HUMAN_CONFIRMATION = BLOCKED_BY_CODEX_HUMAN_ORIGIN_SIGNAL

不得把 UserPromptSubmit 冒充实现。


### 3.1 V1-R1：确认后由谁完成取消

本轮比较了两个现实选择：

A. 保持原 v1：独立 shell confirmation command **只确认、不取消**；consumer 后续再次调用普通 scancel，guard 重查 target/partition、一次性消费 confirmation，再执行 exact scancel。

B. 让独立 shell confirmation command 在重查 target/partition 后直接执行这次取消。

选择 **A，保持原 Proposal 架构不变**。

原因：

- B 会把 Slurm mutation 权限并入 human-confirm adapter，使“证明 fresh human event”和“执行 scheduler mutation”两个职责重新耦合；这不是关闭当前 blocker 所必需。
- 部分 CARE consumer 在取消后还有业务控制流。例如 interactive takeover 在 queue job 真正 CANCELLED 后才允许启动 interactive lane。即使 confirmation command 自己取消，consumer 仍需要继续观察状态并恢复业务流程，所以 B 并没有消除 consumer outcome contract。
- A 只需要让消费者正确理解普通 scancel 的最小结果：**exit 0 才表示 guard 已经实际调用真实 scancel 并且该调用成功返回；非 0 表示本次没有成功执行 cancellation，consumer 不得把目标标记 cancelled，也不得结束本应继续监控的 cancellation branch。** consumer 不需要知道 protected partition、challenge、confirmation 或 pending-challenge 状态。

因此 v1 的 authoritative fresh-human flow 仍为：

protected ordinary scancel -> guard 首次 block + challenge -> 用户独立 shell confirmation（只确认） -> consumer 的正常监控/有界重试再次发出同一 ordinary scancel intent -> guard 重查 JobId/Partition -> 原子消费 confirmation -> exact /usr/bin/scancel。

### 3.2 极小 consumer outcome contract

中央 guard / compatibility shim 对 consumer 的稳定接口只有：

- **exit 0**：这一调用已经实际到达真实 scancel，且 scancel 成功返回；consumer 可以进入它原来“取消请求已提交成功”之后的既有状态机。
- **nonzero**：这一调用没有成功执行 cancellation（包括 fresh-human confirmation 尚未完成、target/partition 变化、challenge 无效、解析失败或真实 scancel 失败）；consumer 必须保留 target，不得把它记录为 cancelled，不得把 cancellation branch 当作成功完成。
- 用户可见的 challenge / reason 可以写 stdout/stderr 或结构化日志，但 consumer 不解析这些保护语义。
- 对 nonzero，consumer 只做它原本业务上合理的继续监控 / 有界重试；是否 protected、是否已确认、challenge 是否可消费全部仍由中央 guard 决定。

这不是第二套保护逻辑，而是普通进程对“子命令成功/未成功”的基本控制流语义。

### 3.3 CARE 当前四个 blocker consumer 的最小控制流修复

本轮实际读取 CARE main@75a40e454de43b64e59a0b0b438ff57ef2bb8345。

1. scripts/route_B_round04/watch_B1_race.py
   - 当前在调用 scancel 后无条件把 partition 加入 cancelled。
   - 最小修复：只有 returncode == 0 才加入 cancelled；nonzero 时记录本次未取消并保持该 partition 可在下一轮 poll 再次尝试。
   - 外层 while 本来就在持续轮询，因此无需新增 retry subsystem、timer 或保护逻辑。

2. scripts/evaluation/watch_srr_v3_m7_routing.py
   - 当前检测 winner 后调用 scancel，随后无条件 return 0。
   - 最小修复：只有 scancel returncode == 0 才走现有 return 0；nonzero 时记录“cancel not executed / continue monitoring”，进入现有 for-loop 下一轮。
   - 不增加 challenge 解析，也不增加新的状态机。

3. scripts/evaluation/watch_srr_v3_m8_myops_race.py
   - 当前调用 scancel 后立即 return。
   - 最小修复：只有 code == 0 才 return；nonzero 时记录未执行取消并继续现有 check loop。
   - winner/loser 判定、both-running 语义、poll cadence 均不改变。

4. scripts/target_domain_gap_closure/monitor_interactive_takeover.py
   - 当前调用 scancel 后立即进入最多 60 次 sacct CANCELLED 等待；若 guard 首次 block，这条路径会等待后 return 2，无法自然等到后续确认。
   - 最小修复：先检查 cancel.returncode。只有 == 0 才进入原有 sacct CANCELLED 确认和后续 launch_m1；nonzero 时记录“cancellation not executed”，不进入 CANCELLED accounting wait、不启动 takeover，直接回到现有 outer poll。
   - 这样用户确认后，下一轮 outer poll 仍看到 queue job PENDING，会自然再次调用 ordinary scancel；guard 此时重新解析并消费 confirmation。

5. scripts/evaluation/watch_care_srr_cascade_formal_race.py
   - 当前主循环本来每个 interval 都重新 evaluate_once；只要 loser 仍 PENDING，下一轮会自然再次调用 cancel_if_pending。
   - 因此不需要控制流重构。
   - 仅要求结果日志保持真实：returncode == 0 才可记录 cancellation request 已成功提交；nonzero 记录未执行/待重试，不得把 action 文案写成已经成功取消。主 decision 在 active target 仍存在时继续 NEEDS_MONITOR。

这些修改不会让 CARE 知道 protected partition 或 challenge。所有 watcher 仍然只发普通 scancel intent；只是停止把“子命令没有执行取消”误当作取消成功。


## 4. 薄 scancel guard

### 4.1 唯一职责

guard 只有四个职责：

- 解析允许的 exact scancel target；
- 只读查询 Slurm 当前 JobId / Partition；
- 判断是否命中 private protected partition；
- 直接转发，或者发 challenge / 消费 challenge 后一次性转发。

guard 不负责 current-run ownership、race ownership、H100/A100 family、workload identity、scientific budget、DII/CARE 业务状态机、standing opt-in 或通用 authorization ledger。

### 4.2 Slurm target resolution

官方 Slurm 事实：

- scancel 支持一个或多个具体 JobId，也支持 array、heterogeneous job、step 与 --user/--partition/--name/--state 等筛选器；
- array parent ID 可能影响全部 array elements；
- heterogeneous leader/component 的取消范围依 PENDING/RUNNING 和 component 位置而不同；
- scontrol show job -o <id> 是详细、只读的 job query；
- squeue -j 可作为 active-target cross-check。

v1 保持小。

直接支持：
- 单个普通 exact JobId；
- 多个明确列出的普通 exact JobId；
- exact array element ArrayJobID_ArrayTaskID，前提是只读查询能唯一定位一个 element。

默认拒绝并要求先显式展开：
- array parent；
- array range / expression；
- heterogeneous job leader / component；
- job step；
- --user、--partition、--name、--state、reservation 等动态 filters；
- federation / cluster-switching 参数；
- 非默认 signal / batch/full 等改变动作语义的选项。

理由不是这些永远不能支持，而是 v1 的产品目标只是保护普通 job cancellation。动态 filter 在 resolve 与 mutate 之间目标集合可能变化，heterogeneous/array-parent 的 Slurm 取消语义也明显更复杂。让调用方先把目标化成 exact IDs 更小、更可审。

目标解析以 scontrol show job -o <exact-id> 为 primary，必要时用 squeue -h -j <id> cross-check active state。对 PENDING multi-partition job，若解析出的候选 partition 集合含 protected partition，则按 protected 处理。

执行真实 scancel 前再做一次相同只读解析；JobId 消失、target 变形或 Partition 集合变化都 fail closed / challenge invalid。

转发真实 scancel 时 guard 清除会暗中改变 target/filter 的 SCANCEL_* 环境变量，并拒绝本轮不支持的 cluster/filter 语义，避免命令行看似 exact target 却被环境扩大范围。

## 5. Codex Host Policy、PATH 与 PreToolUse

### 5.1 execpolicy 不能独立解决问题

OpenAI 当前 execpolicy 的 prompt 只表示“需要 approval”，不能指定这条 rule 必须由 user 而不是 auto_review 审。公开 issue #30598 / #44780 仍记录这种 per-rule human reviewer override 缺失。

因此：
- prompt 单独使用不满足 protected cancellation 的本人二次确认；
- auto_review 不能成为 confirmation adapter；
- forbidden 适合阻止 Codex 顶层显式绕过 guard。

### 5.2 normal entry

推荐一个中央 guard executable：

ai-slurm-scancel

以及一个只对 Codex / 自动 watcher launch environment 生效的 compatibility shim：

scancel -> ai-slurm-scancel

这样当前 CARE 的 Python watcher 仍然只表达：

subprocess.run(["scancel", job_id])

不需要理解 protected partition 或 challenge。

已实际搜索当前 DII/CARE：

- DII 当前主线没有发现 /usr/bin/scancel、os.system(scancel)、Slurm API cancellation；
- CARE 当前几个真实 watcher 使用 bare "scancel" + Python subprocess，没有发现 /usr/bin/scancel 硬编码、SSH scancel 或 Slurm kill API；
- 因而当前消费者可以优先通过一个受控 automation PATH shim 收敛，无需复制中央保护逻辑。

PATH 只有在实际 consumer launch environment 被证明时才算接通。若某个 tmux/watcher/consumer 不继承该 PATH，只对它做最小 launcher/executable-resolution 修复，不复制 guard policy。

用户自己的普通 shell PATH 不改；用户仍可直接使用系统 Slurm，包括 /usr/bin/scancel。

### 5.3 raw bypass

Codex Host Policy 应：

- 对顶层显式 /usr/bin/scancel 及核实后的真实系统 scancel executable 设 forbidden；
- 允许 exact guard executable；
- 不把 read-only Slurm、普通 shell 或全部 Python 一律改成人工审核。

不能声称 execpolicy 能拦截已经启动的 Python 进程内部所有 subprocess。正因如此，consumer PATH / exact executable 必须统一进入 guard。

### 5.4 PreToolUse

PreToolUse 仅作为辅助层：

- 顶层命令明显出现 /usr/bin/scancel、PATH 绕行等已知 raw bypass 时提前 deny；
- 输出清楚的 guard 使用提示。

它不是唯一执行边界，因为：

- hook error / timeout / malformed output 不能被当成可靠阻断；
- permissionDecision: "ask" 当前不支持；
- 外层 python watcher.py 的内部 subprocess.run(["scancel", ...]) 不是一个新的 Codex tool call，PreToolUse 看不到该子进程；
- Code Mode/tool hook coverage 过去存在已记录的实现差异，最终必须实际验证当前 Longleaf build。

## 6. DII / CARE 的最小适配

消费者只拥有一个业务事实：

“现在业务上希望取消这些 exact JobId。”

消费者不判断 partition 是否受保护、是否已经二次确认、challenge 是否新鲜、auto-review 是否算用户、confirmation 是否可消费。

DII / CARE 目标仍是 ordinary cancellation intent 自动进入中央 guard；**但 PATH shim 并不意味着所有 watcher 可以零代码修改。consumer 必须遵守第 3.2 节的最小 outcome contract：只有 guard/scancel exit 0 才能按取消成功路径推进；nonzero 必须保留 target 并继续原有监控/有界重试。**

当前 source identity：

- DII current main：747829b957b19e8fcffa6bd5f1bb7ae62ae11f6f。
- CARE current main：75a40e454de43b64e59a0b0b438ff57ef2bb8345。

当前代码事实：

- DII 当前主线没有发现 direct absolute scancel / subprocess cancellation；主要影响仍是 standing race contract、安装的 Slurm Skill 和最终 launcher executable resolution。
- CARE current main 的 watch_B1_race.py、watch_care_srr_cascade_formal_race.py、watch_srr_v3_m7_routing.py、watch_srr_v3_m8_myops_race.py、monitor_interactive_takeover.py 使用 bare scancel，适合由 PATH shim 收敛；其中四个 watcher 需要第 3.3 节的极小 success/non-success 控制流修复，cascade formal race 只需保证日志语义真实。

消费者适配顺序：

1. 先证明各 normal launcher 下 command -v scancel / Python shutil.which("scancel") 都解析到 guard shim。
2. 对 CARE 四个一次调用后会误结束/误标记的 watcher，应用第 3.3 节的最小 return-code 控制流修复。
3. cascade formal race 保留现有轮询重入，只修必要的结果语义，不创建新的保护状态机。
4. 若某入口解析不到 guard，只改该 launcher / executable resolution。
5. 若出现 hardcoded absolute scancel / SSH / Slurm API，再做最小替换，使它调用中央 guard。
6. 不再保留 CARE scripts/ops/slurm_safe_cancel.py 这种复制 current-run / 三态逻辑的 adapter。

CARE 当前授权 task/blueprint 和 AGENTS 的科学/调度合同仍可以写“取消 pending loser”；中央运行环境负责决定这次 ordinary scancel 是否要二次确认。无需在每份科学 prompt 里重复 protected partition / challenge 规则。

## 7. 旧候选代码处置

### 删除 / 不再移植

AI Skills 旧候选中以下语义应删除：

- ALLOW_OWNED_UNPROTECTED / 三态 classifier 作为产品架构；
- --owned-job-id；
- --current-run-id；
- ownership_verified / owner_run_id / cancel_responsibility；
- protected_accelerators / H100 family matcher；
- confirmation receipt / expected_human_identity 作为 execution authority；
- cancel_policy_version / cancel_policy_confirmed 这组为旧复杂 policy 服务的字段；
- 任何要求 consumer 理解 REQUIRE_FRESH_HUMAN / DENY... 的 adapter。

CARE 旧候选的 scripts/ops/slurm_safe_cancel.py 不进入新生产架构。

DII/CARE 旧候选中围绕 central safe-cancel 三态的 AGENTS / consumer 文案不作为目标实现来源。

### 可以选择性复用

- existing local override 读取框架；
- read-only Slurm discovery / command runner；
- exact JobId parser 的安全思路；
- fake Slurm 测试框架；
- Stage A / Phase 3 consumer inventory；
- 证明 broad selector 不应直接 mutation 的回归思想；
- 旧事故样本“长 Goal 偷藏取消”作为永久 regression。

这是工具代码复用，不是旧架构 PARTIAL_KEEP；产品架构本身仍判定 REJECT。

## 8. 六种现实方案比较

| 方案 | fresh 本人确认 | 子进程 | 长 Goal / auto-review | consumer 改动 | 结论 |
| --- | --- | --- | --- | --- | --- |
| execpolicy prompt only | FAIL：当前可路由给 auto-review | 只覆盖 Codex 顶层 | FAIL | 低 | 拒绝 |
| PreToolUse only | FAIL：不是本人确认 transport | Python 内 subprocess 可绕 | FAIL | 低 | 拒绝 |
| UserPromptSubmit + PreToolUse | 无法证明 human origin；官方 hook contract 缺 origin | subprocess 仍需 guard | challenge 可防提前文本，但不是 human-proof | 中 | 拒绝作为 production authority |
| scancel guard only | 能按 partition 阻断，但不能证明新本人动作 | 能覆盖通过 guard 的 subprocess | 没有独立 confirmer 就不够 | 低 | 不完整 |
| guard + trusted fresh-human adapter + PreToolUse | PASS；当前 adapter=独立 user shell，未来可换 human-origin hook | consumer 路径统一进 guard；少数 watcher 仅修 exit-code 重入 | PASS，PreToolUse 只是辅助 | 低 | 推荐 |
| 旧复杂 safe-cancel | 非需求维度过多，receipt 仍不等于 fresh human provenance | consumers 复制逻辑 | 复杂且偏离产品要求 | 高 | 拒绝 |

另比较了“独立 shell confirmation command 直接在重查后执行 cancellation”。它能消除 guard 的一次 re-entry，但会把 fresh-human adapter 与 Slurm mutation 耦合，而且 CARE takeover 等消费者仍需要继续业务控制流，因此没有比第 3.2/3.3 节的最小 outcome contract 更小。本 Proposal 不采用它。

如果 OpenAI 后续增加稳定 HumanPromptSubmit 或 UserPromptSubmit.origin=human，第五方案的 trusted adapter 可以直接改为聊天消息：

确认取消 <exact ids> <challenge>

其余架构完全不变。

## 9. Capability Gate Matrix

不沿用旧三态架构的 G1–G6；新设计按真实能力重新组合成四项 Gate。

### Gate A：partition routing correctness

- 非保护 partition（例如 a100-gpu），当前 Goal 已允许 cancel：guard 不新增二次确认，fake Slurm 正常收到 exact scancel。
- htzhulab：第一次 exact cancellation 永远不 mutation，输出 exact JobId + partition + fresh challenge。
- pending multi-partition 若 candidate set 含 protected partition，也走 protected。

### Gate B：fresh human event / replay

当前可部署 adapter：

- 初始 Goal 即使写“以后所有取消我都提前同意”，无 pending challenge，不能确认；
- auto-review 不写 confirmation state；
- assistant/model 文本不能调用独立 user confirmer；
- challenge 必须在第一次 block 后生成；
- 用户独立 shell 确认后，confirmation command 只确认、不取消；consumer 下一次 ordinary scancel 才由 guard 重查后继续；
- one-time consume，replay 拒绝；
- target / partition 改变，旧 challenge 失效。

chat-only 版本 Gate B 当前必须 FAIL/BLOCKED，直到存在稳定 human-origin signal；不得通过 UserPromptSubmit 事件名字机械判 PASS。

### Gate C：normal-entry / consumer coverage

- Codex 顶层 raw /usr/bin/scancel 被 Host Policy / auxiliary PreToolUse 拒绝；
- exact guard executable 可用；
- DII/CARE 每个当前 normal automatic consumer 的 executable resolution 实际指向 guard；
- Python watcher 的 bare scancel 在隔离 replay 中真实进入 guard；
- B1/M7/M8/takeover 在 guard nonzero 时不误标记 cancelled、不提前结束，并能通过现有 poll 自然再次调用；cascade formal race 保持既有轮询重入；
- 用户确认后下一次 ordinary scancel 能消费 challenge 并只执行一次；
- 没有当前可达 absolute / SSH / API bypass；
- user independent shell 的系统 scancel 不被 Codex Host Policy 破坏。

### Gate D：target integrity / claim truth

- multiple exact IDs 原子判定；一项 protected 则整组先确认；
- array range / parent、heterogeneous、step、filter selector fail closed；
- execution 前重新解析 exact target；
- 只在完全隔离 fake Slurm 运行 destructive replay；
- 真实 Longleaf 验证只读；
- 最终 claim 仅为“已验证的 Codex/consumer normal entry 对 protected partition 强制 fresh confirmation”，不声称 same-UID OS-level 不可绕过。

Regression bank 固定包含用户这次事故和以上 protected/non-protected/fresh/replay/consumer 场景。最终 release evidence 必须来自同一个 final candidate，不能用旧 Phase 3 candidate 的 PASS 拼接。

## 10. 能保证什么 / 不能保证什么

设计通过并部署后可以保证的范围：

- 在已验证的 Codex normal entry 和当前自动 consumers 中，protected partition 的 exact cancellation 第一次不会执行；
- 旧 Goal / race opt-in / auto-review / model text 不产生 protected confirmation；
- 当前 deployable mode 只有独立 human confirmation adapter 能使 challenge 进入 confirmed；该 command 本身不执行取消；
- consumer 对 guard nonzero 保留目标并继续既有监控/有界重试，使确认后自然发生下一次 guard 调用；
- challenge 只能消费一次，target / partition 变化失效；
- non-protected partition 不新增第二确认；
- DII/CARE 不拥有第二套 protection logic。

不能保证：

- 同一 Unix UID 下，一个主动绕开 Codex normal entry 的任意原生进程在 OS 层永远无法调用 Slurm；
- stock UserPromptSubmit 当前一定代表 direct human-authored input；
- 没有实际验证的未来 consumer / launcher 自动继承 guard；
- 本 Proposal 本身授权任何生产变更。

## 11. 最小实现边界

Critic PASS 后才准备 Execution Package。中央只需要：

1. 一个薄 ai-slurm-scancel guard；
2. 一个极小 pending challenge 文件格式；
3. 一个可信 human-confirm adapter（当前：独立 shell command；未来：human-origin hook）；
4. 一个 private config 字段 protected_cancel_partitions；
5. Codex / watcher 受控 PATH shim；
6. Codex Host Policy 对 raw system scancel 的 bounded deny；
7. 可选 PreToolUse deny/提示。

不创建 daemon、broker、DB、approval service、长期控制面或新的顶级 Plugin。

本轮只提交 Proposal，不准备 Goal/Kickoff，不建立 branch/worktree，不部署 Hook/Host Policy，不运行 Slurm mutation。

## 12. 当前维护真值

docs/skill-todos/slurm-workflows.md 当前仍为 tracking issue: PENDING_CLEAR_WRITING。本运行面没有可真实调用的 Clear Writing，所以不创建或伪造 maintenance Issue / Project lifecycle。

Proposal 若获 Critic PASS，下一具真实 Clear Writing + Project 能力的 AI Skills Maintainer 应创建独立 tracking Issue（不复用 #96），回填真实 tracking: #N 并进入 DOING。未完成前不得声称 ADAPTING / DONE，也不要求用户手工维护。

## 13. 主要外部依据（2026-10-17 重新核实）

OpenAI：

- Hooks：https://developers.openai.com/docs/hooks
  - 支持 UserPromptSubmit / PreToolUse；
  - PreToolUse deny 可阻断支持的 tool call；
  - permissionDecision: ask 当前不支持；
  - hook error / unsupported output 不能当作强制安全边界。
- openai/codex source：
  - codex-rs/hooks/src/events/user_prompt_submit.rs
  - codex-rs/hooks/schema/generated/user-prompt-submit.command.input.schema.json
  - 当前 payload 没有 human-origin 字段。
- openai/codex issue #29640：https://github.com/openai/codex/issues/29640
  - 截至本轮仍 open；
  - 明确记录 UserPromptSubmit 可对 Codex-originated subagent prompt 触发，并请求 human-only event / origin metadata。
- execpolicy / approvals：
  - https://developers.openai.com/codex/rules
  - openai/codex #30598、#44780：当前 per-rule prompt 不能强制指定 reviewer=user；全局 auto-review 仍可处理 prompt。
- PreToolUse coverage：
  - openai/codex #23411 等记录过 Code Mode / tool hook coverage差异，必须以目标 Longleaf build 的实际 probe 为发布证据。

Slurm：

- https://slurm.schedmd.com/scancel.html
- https://slurm.schedmd.com/scontrol.html
- https://slurm.schedmd.com/squeue.html
- https://slurm.schedmd.com/job_array.html
- https://slurm.schedmd.com/heterogeneous_jobs.html

官方语义支持本 Proposal 的“exact ID 优先、复杂 selector fail closed”取舍：array parent、heterogeneous component、step 和 filter 的实际取消范围存在不同语义，不能假装等价于一个普通 exact JobId。
