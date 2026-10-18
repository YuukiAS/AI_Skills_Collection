# Clear Writing Web Gate v0.3 — execution Kickoff draft

只在以下两项都成立后执行：

1. 独立 Critic 已对 **同一 v0.3 package** 给出 execution-ready PASS；
2. 用户在该 PASS 之后明确发送这份 approved Kickoff。

在此之前，不做任何真实 ChatGPT candidate、Project、账号或 Web Gate
操作。

---

继续 Clear Writing 真实 ChatGPT Web 调用策略验收。不要修改 production
candidate。

仓库：`YuukiAS/AI_Skills_Collection`  
任务：`clear-writing--every-response-invocation-policy`  
证据分支：`reviewed/clear-writing--scientific-explanation-readability-repair`

冻结 production candidate：

`fd7a1578a5042a46a55c5b638f6d550655b1096b`

先读取并严格执行以下 **v0.3 冻结只读合同**：

- `automation/reviewed_handoff/tasks/clear-writing--every-response-invocation-policy/REQUEST.md`
- `automation/reviewed_handoff/tasks/clear-writing--every-response-invocation-policy/PLAN.md`
- `automation/reviewed_handoff/tasks/clear-writing--every-response-invocation-policy/CURRENT.json`
- `docs/goals/CLEAR_WRITING_EVERY_RESPONSE_INVOCATION_POLICY_WEB_GATE_GOAL_V0_3_2026-10-18.md`
- `docs/design/clear-writing/CLEAR_WRITING_WEB_GATE_TASK_BANK_V0_3_2026-10-18.md`
- `docs/design/clear-writing/CLEAR_WRITING_W2_MATCHED_ENVIRONMENT_PREFLIGHT_V0_3_2026-10-18.md`
- `docs/design/clear-writing/CLEAR_WRITING_WEB_TEST_CANDIDATE_MATERIALIZATION_V0_3_2026-10-18.md`
- `docs/design/clear-writing/CLEAR_WRITING_W2_REVEAL_MAP_V0_3_2026-10-18.json`
- approved invocation-policy proposal v0.2；
- proposal Critic PASS；
- 本 package 的 execution-ready Critic PASS。

execution-ready PASS 后，上述 proposal/review/REQUEST/PLAN/Goal/Kickoff/bridge/
Task Bank/preflight/materialization/reveal-map/rubric/order/budget/stop rules
全部只读。任何一项需要改变：立即停止 -> Planner -> Critic；不得原地修改后继续。

## 0. 当前机器状态和 watcher 必须先 fail closed

开始时要求：

`CURRENT.state=NEEDS_GPT_PLANNER`

这不是 Web Gate 已经开始执行，而是为了避免 `PLAN_FROZEN` 被 Reviewed
Handoff watcher 当作 Codex Executor event。

本 Web Gate **不使用 watcher/Codex 作为执行 transport**。

在任何 ChatGPT live mutation 之前，先解析当前真正授权的本地
AI_Skills_Collection checkout，并对 exact branch 执行：

```text
ai-bridge reviewed-handoff watcher status --target <resolved-target> --branch reviewed/clear-writing--scientific-explanation-readability-repair
```

若该 exact target + branch 有 active watcher：

```text
ai-bridge reviewed-handoff watcher stop --target <resolved-target> --branch reviewed/clear-writing--scientific-explanation-readability-repair
```

随后必须再次 `watcher status`，确认：

- watcher inactive；
- 没有 active Executor event。

无法取得 status、无法证明 inactive、或无法安全停止 active Executor：
立即停止。不得继续到任何 ChatGPT mutation。

整个 manual Web Gate 期间，不得重新 start/restart 该 exact branch watcher。

## 1. 先做只读 W2 matched-environment preflight

这一步发生在：

- 创建 test Clear Writing candidate 之前；
- 创建/修改任何测试 Project 之前；
- 写入 Project bridge 之前；
- 第一个模型请求之前。

严格执行：

`CLEAR_WRITING_W2_MATCHED_ENVIRONMENT_PREFLIGHT_V0_3_2026-10-18.md`

必须真实证明当前 surface 能在授权范围内建立：

- same account/workspace boundary；
- same surface/model/effort；
- exact same Project bridge bytes；
- candidate availability/consumption 是唯一实质 arm 差异；
- 无账号/订阅/workspace/role/permission mutation；
- 无反复 global plugin install/uninstall；
- 两 arm 不可读取彼此历史；
- Project memory 是真正 project-only，或有明确等价隔离机制。

默认/普通 memory 只要可能跨 Project 引用历史，就不能算 isolation PASS。

如果任何一项不能证明：

`W2=INCONCLUSIVE`

把只读 preflight evidence 写入：

`results/clear-writing--every-response-invocation-policy/web-gate-v0.3/preflight/`

然后停止整个 live batch。

此时：

- 不创建 candidate；
- 不创建/修改测试 Project；
- 不运行 W0；
- 不运行 W1；
- 不运行 W2；
- **不运行 W3**。

W3 永远不能 rescue W2。

## 2. preflight PASS 后才 re-arm Reviewed Handoff

只有 watcher 已证明 inactive 且
`W2_MATCHED_ENVIRONMENT_PREFLIGHT=PASS` 后，才允许通过现有 Bridge 合法
状态路径把 task 从：

`NEEDS_GPT_PLANNER -> PLAN_FROZEN -> EXECUTING`

推进到 manual execution。

不得 raw 跳过 state graph；不得启动 watcher 来完成这两个 transition。

若合法 transition 无法完成，停止，不做 live mutation。

## 3. 构建唯一 test-only Web candidate

严格执行：

`CLEAR_WRITING_WEB_TEST_CANDIDATE_MATERIALIZATION_V0_3_2026-10-18.md`

唯一 source authority：

`fd7a1578a5042a46a55c5b638f6d550655b1096b`

在 isolated clean checkout 中：

1. 核对冻结的六个 source Skill tree identity；
2. 核对 generated writing-style tree identity；
3. 运行 source/generated parity；
4. 仅把 exact generated
   `plugins/codex/plugins/writing-style/` 内容放到 archive root；
5. 用冻结的 deterministic ZIP 规则构建 archive；
6. 保存每个文件 SHA-256、archive SHA-256、file count、size、source commit。

任何 parity/hash/identity 不一致：停止，不创建 plugin。

## 4. Plugin Creator 只允许一次 PRIVATE create

创建前再次只读核对 owned plugin inventory。

若此时已经出现一个未在本 package 创建的 Clear Writing candidate：
停止，不能 update/reuse/delete。

若 inventory 仍符合冻结前提，最多调用一次 Plugin Creator create，
上传第 3 步 exact archive。

创建结果必须记录：

- `plugin_id`
- `release_id`
- `current_release_id`
- `latest_release_id`（若提供）
- version
- scope
- discoverability

必须是 PRIVATE，scope 必须与 preflight 的 account/workspace boundary 一致。

任何 unexpected `updated`、非 PRIVATE、scope 不符或身份冲突：停止。

不得创建第二个 candidate。

## 5. W0 前必须重新读取实际 Web release

使用第 4 步返回的 exact `plugin_id`：

- 读 plugin metadata；
- 列出 current release files；
- 读取所有可直接读取的 text files；
- 获取完整 current release archive；
- 重算完整 release manifest/hash；
- 与 pre-create frozen archive 逐文件/整体比较。

无法证明 actual Web release 与 frozen source 同源：停止 W0。

不要测试近似 candidate。

## 6. candidate 的失败后语义已经冻结

若后续出现：

- W0 FAIL；
- W1 FAIL；
- W2 FAIL；
- W2 INCONCLUSIVE；
- 其他 package-defined stop；

已创建的 test candidate：

**保留 unchanged + PRIVATE。**

本 Kickoff 不授权：

- uninstall；
- delete；
- update；
- publish；
- permission change；
- replacement candidate；
- 创建第二个 Clear Writing test candidate。

后续 cleanup 是新的 live mutation，必须以后单独授权；不得临场决定。

也不得碰：

- Research Authoring；
- Project Instructions Editor；
- Project Thread Handoff；
- 其他任意 plugin。

## 7. W0

candidate release parity PASS 后，严格按 Task Bank v0.3 顺序执行 W0-A、
W0-B。

W0-A 只判断 frozen natural/mixed safety。

W0-B 做 explicit plugin selection + exact-only stress。

如果只能证明 plugin-level selection，最大结论仍是：

`PLUGIN_SELECTION_DOES_NOT_CONTAMINATE_EXACT_OUTPUT`

不能写 loaded-skill bypass PASS。

任一 release-critical W0 FAIL：停止。candidate 保持 PRIVATE unchanged。

## 8. W1

W0 PASS 后才运行 W1。

使用测试 Project 和 frozen exact bridge；每个 turn 不手工
`@Clear Writing`。

唯一正式结论：

`PROJECT_POLICY_BEHAVIOR_RELIABILITY`

有真实 load evidence 就保存；没有就写不可观察。

模型自述不能证明 plugin load。

W1 FAIL：停止。

W1 PASS 不证明 plugin causality。

## 9. W2 strict matched execution

W1 PASS 后，使用 preflight 已证明合法的 exact matched mechanism。

两 arm 必须持续满足：

- same account/workspace；
- same surface/model/effort；
- identical Project bridge bytes；
- same project-only/equivalent memory isolation；
- same task/order/budget/rubric/evaluation；
- fresh isolated contexts；
- no cross-arm history；
- only candidate availability/consumption differs。

任一条件在执行中失效：

`W2=INCONCLUSIVE`

停止 release；**不运行 W3**。

不允许切账号/订阅/workspace，不允许 permission mutation，不允许
install/uninstall chasing。

## 10. W2 blind packet

使用 frozen：

`CLEAR_WRITING_W2_REVEAL_MAP_V0_3_2026-10-18.json`

为每个 pair 按预冻结 mapping 赋 opaque labels。

注意：

- label 与 first/second execution order 没有固定对应；
- 不得临时随机生成；
- 不得看输出后换 label。

完成 W2 outputs 后，生成单独的 blind packet。

初评 Reviewer 必须是一个**新的独立 Critic thread**，且之前没有读取
reveal map。当前 execution-ready Critic 因为审过 reveal map，不能兼任。

给 blind Reviewer 的每题材料只能有：

- exact task id；
- exact prompt；
- opaque output label A；
- raw output A；
- opaque output label B；
- raw output B；
- frozen preference/hard-failure rubric。

必须移除：

- execution order；
- timestamps；
- Treatment/Control Project 名；
- plugin/candidate identity；
- invocation/load evidence；
- account/workspace locator；
- 任何能由 pair order 推断 arm 的 metadata。

先让 blind Reviewer 冻结全部 P01-P08 的逐题 verdict + reason。

**在这之前不得 reveal。**

blind verdict 冻结后，执行线程才能读取/使用 reveal map，并把 verdict
与 process/identity evidence 合并为 W2 causal summary。

评分规则保持 package 中已经批准的：

- P01-P07 中 Treatment 至少 4/7 preferred；
- Control 最多 1/7 preferred；
- Treatment zero hard failure；
- exact/mixed control 不退化；
- P08 仅 hard control，不进入 4/7。

不得事后改 rubric。

## 11. W3

只有 W2 得到确定的 PASS 或 FAIL 后才允许运行 W3。

W2 INCONCLUSIVE 时：

**W3 不运行。**

W3 仍然：

- no Project bridge；
- no manual Clear Writing invocation；
- diagnostic only；
- non-release-critical；
- 不能 rescue W2。

## 12. G7 禁止

本 Kickoff 不执行 G7。

只有 W0/W1/W2 release-critical PASS 后，写：

`READY_FOR_G7_FREEZE`

然后停止回 Planner。

G7 必须另做 freeze + Critic。

## 13. execution-ready PASS 后 frozen contract 只读

执行期间不得修改：

- proposal / Critic review；
- REQUEST；
- PLAN；
- Goal；
- 本 Kickoff；
- bridge bytes；
- Task Bank；
- W2 preflight；
- candidate materialization contract；
- reveal map；
- task/pair order；
- attempt budget；
- rubric；
- scoring threshold；
- stop/recovery rules。

只允许写：

- `results/clear-writing--every-response-invocation-policy/**`
- Reviewed Handoff 允许的 executor-owned CURRENT 字段/合法 state transition
- Issue #13 必要 tracking copy

任何 frozen contract 想改：

立即停止 -> Planner -> 独立 Critic。

## 14. attempt / retry

每个 frozen task/turn/arm 默认只有一个有效模型回答。

只有因为网络/服务中断而完全没有 usable model answer 时，才允许一次
infrastructure-only retry，并保留第一次失败记录。

低质量、答错、格式错、插件没有按预期工作都是真实结果，不准重跑到成功。

## 15. evidence

全部 repo evidence 只写：

`results/clear-writing--every-response-invocation-policy/web-gate-v0.3/`

保留：

- preflight；
- freeze manifest；
- bridge bytes/hash；
- candidate archive/file manifest；
- actual release parity；
- W0 raw outputs；
- W1 full turns；
- W2 raw arm evidence；
- sanitized blind packet；
- blind reviewer verdict；
- reveal/casual summary；
- W3 evidence（若 reachable）；
- attempt/retry log；
- RESULT；
- FINAL_REVIEW_INPUT_MANIFEST。

不得公开 account ID、credentials、private chat URL、无关 Project 内容。

含私人 UI 的 screenshot 只放
`private/exports/clear-writing--every-response-invocation-policy/`。

## 16. 最终独立复核

Web execution 完成后，最终 Reviewer 必须真实读取 raw evidence，并分别给：

- PROCESS / IDENTITY；
- CANDIDATE PARITY；
- W0 PRODUCT SAFETY；
- W1 PROJECT_POLICY_BEHAVIOR_RELIABILITY；
- W2 PLUGIN_INCREMENT PASS / FAIL / INCONCLUSIVE；
- W3 diagnostic（若 reachable）。

最终 Reviewer 不能把 W1 升成 plugin causality，也不能把 confounded W2
判 PASS。

如果 W0/W1/W2 全 PASS，停止于 `READY_FOR_G7_FREEZE`。
