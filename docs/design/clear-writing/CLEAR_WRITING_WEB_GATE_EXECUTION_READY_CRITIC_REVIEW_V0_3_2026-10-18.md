# Clear Writing Web Gate execution package v0.3 — 独立 execution-ready Critic Review

日期：2026-10-18  
审查阶段：execution package v0.3 re-review after execution-ready REVISE  
审查对象：`clear-writing--every-response-invocation-policy`  
Package commit：`870e5c1766549b27819c14fbd8109c7ad9484bf6`  
Approved invocation-policy proposal：`docs/design/clear-writing/CLEAR_WRITING_EVERY_RESPONSE_INVOCATION_POLICY_PROPOSAL_V0_2_2026-10-18.md@1f905d294c3c2e5b0951c9d5e818c285d236cef7`  
Proposal Critic PASS：`docs/design/clear-writing/CLEAR_WRITING_EVERY_RESPONSE_INVOCATION_POLICY_CRITIC_REVIEW_V0_2_2026-10-18.md@50e09a2dc68a097ef21e0cf245f7951eb9d06f89`  
Frozen production candidate：`fd7a1578a5042a46a55c5b638f6d550655b1096b`  
Bridge Kit source checked：`YuukiAS/GPT_Codex_AI_Bridge_Kit@35a976e79c036f6e68ba70e9d2364abc1c274a45`

## Decision

**REVISE / READY_FOR_WEB_GATE=NO**

本轮只复核上一轮五个 stable blockers。结论：

- `CW-WEB-ER-01 = STILL_OPEN`
- `CW-WEB-ER-02 = CLOSED`
- `CW-WEB-ER-03 = CLOSED`
- `CW-WEB-ER-04 = CLOSED`
- `CW-WEB-ER-05 = STILL_OPEN`

没有重新打开 invocation-policy proposal v0.2、六技能架构、`response-clarity` 内容质量、W2 已批准评分阈值或 production candidate。

## CW-WEB-ER-01 — STILL OPEN

### 已关闭部分

v0.3 已正确把当前机器状态移出 watcher 可执行集合：

`CURRENT.state=NEEDS_GPT_PLANNER`

Bridge Kit 当前实现直接证明：

`ELIGIBLE_EXECUTOR_STATES = {"PLAN_FROZEN", "REVISE"}`

因此当前 `NEEDS_GPT_PLANNER` 不会被 watcher 当成 Executor event。

当前 Bridge 也确实提供并实现：

- `reviewed-handoff watcher status`
- `reviewed-handoff watcher stop`

`watcher status` 会报告 exact target/branch watcher process 以及 task runtime；`watcher stop` 会核实 PID 确实属于 exact target/branch 后再停止。v0.3 要求 live mutation 前检查并关闭 exact branch watcher的方向成立。

### 仍然阻塞的问题

v0.3 计划在 execution-ready PASS + 用户 Kickoff + watcher inactive + W2 preflight PASS 后走：

`NEEDS_GPT_PLANNER -> PLAN_FROZEN -> EXECUTING`

但当前 `CURRENT.json` 已经是：

- `plan_revision=1`
- `max_plan_revisions=1`

Bridge Kit 当前 canonical `apply_transition()` 对
`NEEDS_GPT_PLANNER -> PLAN_FROZEN` 明确执行：

- 若 `plan_revision >= max_plan_revisions`，直接拒绝；
- 只有未耗尽时才把 `plan_revision` 再加一。

因此 v0.3 冻结的 re-arm 路径在当前真实 Bridge 上**不可执行**。当前 latch 确实 fail closed，但没有合法的 reopen 路径。

这不是一个可在执行时自行解决的小细节：raw edit CURRENT、重置 revision、提高 max revision、直接跳状态或改 Bridge schema 都会改变既有 workflow contract。

### 最小关闭条件

Planner 必须为 v0.4 冻结一个**当前 Bridge Kit 真实允许的** re-entry / manual-Web execution 路径，并证明：

1. execution-ready review 与用户 Kickoff 前继续 fail closed；
2. 不 raw edit `CURRENT`；
3. 不重置/增加 `plan_revision` 或 `max_plan_revisions`；
4. 不新增 state/schema；
5. 不修改 Bridge Kit；
6. 不触发 watcher/Codex Executor；
7. Web evidence 完成后仍能按合法 workflow 交给后续 Reviewer。

如果现有 Reviewed Handoff state graph 无法同时满足这些条件，就应明确把 manual Web Gate transport 与这个耗尽 re-plan task state 解耦，而不是伪造一个合法 transition。具体方式由 Planner 在既有机制内选择并重新送审。

## CW-WEB-ER-02 — CLOSED

v0.3 已把此前空泛的 “test candidate setup” 换成可执行、可复核的 materialization contract。

独立核验 `fd7a1578a5042a46a55c5b638f6d550655b1096b` 的 Git tree，六个 source Skill tree SHA 与 proposal 冻结值完全一致：

- `writing-fidelity = 13e759a03e551e44f2ffe8513f5b1db542fd526a`
- `response-clarity = 85358b462caff5e2a7629c8349740e971255dd54`
- `scientific-prose = e935f3e3ed0961bdca114db61ac1ea66beef142d`
- `product-ui-copy = 84f001d31be1f9ddd349197199c1858033fd1362`
- `scientific-rewrite = 77ab9af8add9926cd0c19a86f0c3b6d1f1e5024e`
- `chinese-prose = dd03fb660ae3bf499abdae88ad641e901f2d339d`

generated writing-style root 也精确匹配：

`a3b6842c8a870b455ca725e425bc1fbf9b336fc9`

并确认 generated tree 中实际存在
`skills/scientific-rewrite/scripts/rewrite_support.py`。

contract 已冻结：

- deterministic archive；
- per-file / archive SHA-256；
- pre-create owned-plugin inventory；
- 最多一次 PRIVATE create；
- returned plugin/release/scope/discoverability identity；
- Plugin Creator metadata/files/full archive 回读；
- actual Web release 与 frozen archive 的完整 parity；
- 无法证明同源即停止 W0；
- 不修改任何其他 plugin；
- failure 后 retain unchanged + PRIVATE；
- cleanup/update/delete/replacement 不在本 package。

当前 Plugin Creator 能力也真实支持 create、metadata、file list/read 与完整 archive retrieval。

因此 `CW-WEB-ER-02` 已关闭。

## CW-WEB-ER-03 — CLOSED

v0.3 已将 W2 feasibility 提前为 gate zero，并明确发生在所有以下操作之前：

- candidate create；
- Project create/edit；
- bridge write；
- first model prompt。

preflight 需要真实证明：

- same account/workspace；
- same surface/model/effort；
- candidate availability/consumption 可成为唯一 arm 差异；
- 无 account/subscription/workspace/role/permission mutation；
- 无 repeated global install/uninstall；
- no cross-arm history；
- project-only 或真实等价 memory isolation。

它已明确说明 “same memory mode” 不足，default memory 只要可能跨 Project 引用历史就不能 PASS。

无法证明 candidate isolation 或 memory isolation 时：

`W2=INCONCLUSIVE`

并在任何 candidate / Project / model mutation 前停止整个 live batch；W0/W1/W2/W3 均不运行。运行中 strict matching 失效同样转 `INCONCLUSIVE`，W3 不允许 rescue。

因此上一轮 feasibility / late-discovery blocker 已关闭。该 preflight 最终可能在真实 surface 上得到 INCONCLUSIVE；这属于有效产品证据，不构成 execution-package defect。

## CW-WEB-ER-04 — CLOSED

v0.3 已把 execution-ready PASS 后的冻结对象完整列为只读：

- proposal + proposal review；
- REQUEST；
- PLAN；
- Goal；
- Kickoff；
- bridge bytes；
- Task Bank；
- W2 preflight；
- candidate materialization；
- reveal map；
- task/pair order；
- attempt budget；
- rubric；
- scoring threshold；
- stop/recovery conditions。

execution 只允许写：

- `results/clear-writing--every-response-invocation-policy/**`
- Reviewed Handoff 既有协议允许的 executor-owned CURRENT 字段 / 合法 transition；
- Issue #13 必要 tracking copy。

`docs/goals/`、`docs/operations/prompts/`、`docs/design/clear-writing/`、`skills/`、`plugins/`、profiles/Marketplace production source 都明确不可写。

任何 frozen contract 变化必须 stop -> Planner -> independent Critic。

因此不存在 execution 后改题、改 rubric、改 cutoff 或改 prompt 再继续的授权漏洞，`CW-WEB-ER-04` 已关闭。

## CW-WEB-ER-05 — STILL OPEN

### 已关闭部分

opaque mapping 本身已经正确冻结在 Web output 之前，且 label 不等于 first/second execution order。

例如：

- P01 execution = Control -> Treatment，但 Treatment label = `P01-LYNX`；
- P02 execution = Treatment -> Control，但 Treatment label = `P02-MICA`；
- 其余 pair 也没有采用统一的 first/second 映射。

Task Bank 只公开 opaque labels，不公开 Treatment/Control mapping。

blind packet 的可见内容也已正确限定为：

- task id；
- exact prompt；
- 两个 opaque labels + raw outputs；
- frozen rubric。

同时禁止 timestamps、execution order、Project names、plugin identity、load evidence、account/workspace locator 等泄露。

当前 execution-ready Critic 因已读取 reveal map，被明确排除出后续 blind Reviewer，方向正确。

### 仍然阻塞的问题

v0.3 只要求后续 W2 初评 Reviewer 是：

“fresh independent thread that has not read the reveal map”。

这还不能证明真正 blindness。

当前 ChatGPT Projects 的公开产品语义允许 Project 内聊天使用同一 Project 的其他对话作为上下文；即使使用 project-only memory，它解决的是“不引用 Project 外”，并不会让**同一 Project 内两个 thread 相互隔离**。

因此，如果新的 blind Reviewer thread 仍位于当前 AI Research Stack Project，它可能通过 Project memory / prior Project conversation context 获得：

- 本次 execution-ready Critic 已经读取过 reveal map 的事实；
- Treatment/Control opaque mapping；
- pair execution metadata；
- 相关 execution-package讨论。

这会使“新 thread”在形式上没主动打开 reveal-map 文件，但仍不能证明 arm identity 对模型不可见。

把 reveal map 放在 repository 本身并不必然破坏盲评；真正缺失的是**blind Reviewer 的隔离合同**。

### 最小关闭条件

v0.4 必须在任何 W2 output 产生前冻结 blind Reviewer transport/context：

1. blind preference Reviewer 必须运行在不会继承当前 AI Research Stack Project 历史的隔离上下文；
2. 若用 ChatGPT Web，优先采用一个新的、空白、无相关文件/历史的独立 review Project，并启用 project-only memory；或者使用另一个能够明确证明不读取当前 Project memory/repo history 的支持表面；
3. blind Reviewer 在 P01-P08 verdict + reason 全部冻结前：
   - 不得进入当前 AI Research Stack Project；
   - 不得访问 AI_Skills GitHub repo；
   - 不得读取 execution package / reveal map；
   - 不得调用可检索当前 Project/history/repo 的连接器；
   - 只接收 frozen blind packet；
4. blind-review context identity / isolation mode 必须在输出产生前记录；
5. verdict 冻结后才可把 reveal map 交给后续 causal review；
6. reveal map 可以继续留在 repository，前提是 blind Reviewer 的真实权限/context 保证它不可达；如果做不到，则 reveal map 必须移到 blind Reviewer 不可访问的私有 execution evidence surface。

没有这种隔离，`CW-WEB-ER-05` 不能关闭。

## Change-impact review

除上述两个 blocker 外，v0.3 没有破坏上一轮已接受内容：

- invocation-policy proposal 仍是 v0.2；
- Project bridge 语义未改变；
- W0 -> W1 -> W2 -> W3 主序保持；
- W1 只声明 `PROJECT_POLICY_BEHAVIOR_RELIABILITY`；
- W3 仍 non-release-critical；
- W2 评分阈值未改变；
- G7 仍禁止；
- one-answer / infra-only retry 未弱化；
- raw-output evidence 和 privacy contract 未弱化；
- `ci_required=false / NOT_REQUIRED` 适合本 evidence-only task；
- 六技能架构与 production candidate 未改变；
- PIE、Mica、Research Authoring、Presentations 仍 out of scope；
- 当前没有 test candidate、Project mutation 或 Web Gate execution。

Issue #13 仍 open，Area 为 `writing-style`，lifecycle `DOING` 的语义正确；current execution anchor 已更新到 `870e5c1766549b27819c14fbd8109c7ad9484bf6`。

## Claim boundary

本 REVISE 不否定 invocation-policy v0.2，也不要求修改 production。

只有 `CW-WEB-ER-01` 和 `CW-WEB-ER-05` 仍需最小返修。

在这两项关闭前：

`READY_FOR_WEB_GATE=NO`

不得执行 watcher mutation、W2 preflight、candidate creation、Project creation/edit 或任何 W0/W1/W2/W3。
