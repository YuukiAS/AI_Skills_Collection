# Clear Writing Web Gate v0.4 — approved-execution Kickoff draft

只在以下两项都成立后执行：

1. 独立 Critic 已对 **同一 v0.4 execution package** 给出 execution-ready PASS；
2. 用户在该 PASS 之后明确发送这份 approved Kickoff。

在此之前，不执行任何 watcher mutation、W2 preflight、candidate creation、
Project creation/edit 或 W0/W1/W2/W3。

---

继续 Clear Writing 真实 ChatGPT Web 调用策略验收。

仓库：`YuukiAS/AI_Skills_Collection`  
任务：`clear-writing--every-response-invocation-policy`  
证据分支：`reviewed/clear-writing--scientific-explanation-readability-repair`

冻结 production candidate：

`fd7a1578a5042a46a55c5b638f6d550655b1096b`

本轮是 **manual Web evaluation**。不要使用 Reviewed Handoff watcher/Codex
作为 Web Gate execution transport，也不要试图 re-arm 已耗尽 revision budget
的 `CURRENT`。

## 0. 先读取冻结合同

必须读取并按原样执行：

- `docs/design/clear-writing/CLEAR_WRITING_WEB_GATE_EXECUTION_PLAN_V0_4_2026-10-18.md`
- `docs/goals/CLEAR_WRITING_EVERY_RESPONSE_INVOCATION_POLICY_WEB_GATE_GOAL_V0_4_2026-10-18.md`
- `docs/design/clear-writing/CLEAR_WRITING_WEB_GATE_TASK_BANK_V0_4_2026-10-18.md`
- `docs/design/clear-writing/CLEAR_WRITING_W2_MATCHED_ENVIRONMENT_PREFLIGHT_V0_4_2026-10-18.md`
- `docs/design/clear-writing/CLEAR_WRITING_WEB_TEST_CANDIDATE_MATERIALIZATION_V0_3_2026-10-18.md`
- `docs/design/clear-writing/CLEAR_WRITING_W2_REVEAL_MAP_V0_3_2026-10-18.json`
- `docs/design/clear-writing/CLEAR_WRITING_W2_BLIND_REVIEW_CONTEXT_V0_4_2026-10-18.md`
- `docs/operations/prompts/CLEAR_WRITING_W2_BLIND_REVIEW_PROMPT_V0_4_2026-10-18.md`
- `docs/operations/prompts/CLEAR_WRITING_WEB_GATE_FINAL_REVIEW_PROMPT_V0_4_2026-10-18.md`
- approved invocation-policy proposal v0.2；
- proposal Critic PASS；
- 本 v0.4 package 的 execution-ready Critic PASS。

这些对象 execution-ready PASS 后全部只读。任何 frozen contract 想改：
立即停止 -> Planner -> independent Critic。

## 1. 不再修改 Reviewed Handoff CURRENT

当前 machine state：

```text
CURRENT.state=NEEDS_GPT_PLANNER
plan_revision=1
max_plan_revisions=1
ci_status=NOT_REQUIRED
```

这是已经耗尽 plan-revision budget 的 inert control-plane state。

本次 manual Web execution：

- 不执行 `NEEDS_GPT_PLANNER -> PLAN_FROZEN`；
- 不 raw edit CURRENT；
- 不 reset/increase revision budget；
- 不新增 state/schema；
- 不修改 Bridge Kit；
- 不写 REVIEW_1.md；
- 不改变 CURRENT.review_round；
- 不使用 watcher/Codex Executor执行 Web Gate。

CURRENT 在整个 manual Web batch 中保持不变。

## 2. 任何 live mutation 前先证明 watcher inactive

解析当前 exact AI_Skills checkout + exact branch：

`reviewed/clear-writing--scientific-explanation-readability-repair`

运行 current Bridge Kit：

```text
ai-bridge reviewed-handoff watcher status --target <resolved-target> --branch reviewed/clear-writing--scientific-explanation-readability-repair
```

若 active：

```text
ai-bridge reviewed-handoff watcher stop --target <resolved-target> --branch reviewed/clear-writing--scientific-explanation-readability-repair
```

然后重新 `watcher status`。

必须证明：

- no active watcher；
- no active Executor event。

无法证明则停止，不做任何 ChatGPT live mutation。

manual Web batch 结束前不得重新 start/restart exact branch watcher。

## 3. gate zero：W2 matched-environment preflight v0.4

在下列所有动作之前执行：

- candidate create；
- Project create/edit；
- bridge write；
- first model prompt。

严格执行：

`CLEAR_WRITING_W2_MATCHED_ENVIRONMENT_PREFLIGHT_V0_4_2026-10-18.md`

必须真实证明：

- same account/workspace；
- same surface/model/effort；
- exact same bridge bytes；
- candidate availability/consumption 能成为 W2 唯一实质 arm 差异；
- 不需要 account/subscription/workspace/role/permission mutation；
- 不需要 repeated global install/uninstall；
- Treatment / Control cross-arm history 真正隔离；
- Project memory 是 project-only 或明确等价隔离；
- 后续 W2 blind preference review 也能建立新的空白、隔离 review context。

任何一项不能证明：

`W2=INCONCLUSIVE`

保存只读 preflight evidence 后立即停止 entire live batch。

此时不创建 candidate、Project，不执行 W0/W1/W2/W3。

## 4. preflight PASS 后构建唯一 PRIVATE test candidate

严格执行：

`CLEAR_WRITING_WEB_TEST_CANDIDATE_MATERIALIZATION_V0_3_2026-10-18.md`

唯一 source：

`fd7a1578a5042a46a55c5b638f6d550655b1096b`

必须：

- 核对冻结的六个 source Skill tree；
- 核对 generated writing-style tree；
- source/generated parity；
- deterministic archive；
- per-file SHA-256；
- archive SHA-256；
- pre-create owned-plugin inventory guard。

只有这些 PASS 后，最多创建一次 PRIVATE Clear Writing test candidate。

记录真实：

- `plugin_id`
- `release_id`
- `current_release_id`
- `latest_release_id`（若提供）
- version
- scope
- discoverability

不得更新/reuse/delete其他 plugin，不得创建第二个 candidate。

## 5. W0 前核对实际 Web release

使用 exact returned `plugin_id`：

- 读 metadata；
- list current release files；
- read可读 text files；
- get complete archive；
- 重算完整 manifest/hash；
- 与 pre-create archive 做 parity。

无法证明 actual Web release 与 frozen source 同源：停止 W0。

## 6. W0

严格按 Task Bank v0.4 执行 W0-A/W0-B。

W0-B 若没有具体 Skill-load evidence，最大结论只允许：

`PLUGIN_SELECTION_DOES_NOT_CONTAMINATE_EXACT_OUTPUT`

任一 release-critical W0 FAIL：停止。

已创建 candidate 保持 unchanged + PRIVATE。

## 7. W1

W0 PASS 后运行 W1。

使用 frozen Project bridge；每轮不手工 `@Clear Writing`。

唯一正式结论：

`PROJECT_POLICY_BEHAVIOR_RELIABILITY`

没有真实 load evidence就写不可观察，不能用模型自述证明 plugin causality。

W1 FAIL：停止。

## 8. W2 strict matched execution

W1 PASS 后按 preflight 已证明的 exact matched mechanism执行。

持续要求：

- same account/workspace；
- same surface/model/effort；
- identical Project bridge bytes；
- same project-only/equivalent memory isolation；
- same tasks/order/budget/rubric/evaluation；
- fresh isolated contexts；
- no cross-arm history；
- only candidate availability/consumption differs。

任一条件失效：

`W2=INCONCLUSIVE`

停止；W3 不执行。

评分规则不变：

- P01-P07 Treatment至少 4/7 preferred；
- Control最多 1/7 preferred；
- Treatment zero hard failure；
- exact/mixed protection不退化；
- P08只做 hard control。

## 9. W2 blind preference review 必须使用隔离 Project

在任何 blind Reviewer 输出之前，严格执行：

`CLEAR_WRITING_W2_BLIND_REVIEW_CONTEXT_V0_4_2026-10-18.md`

优先创建一个全新空白 review Project：

`CW-W2-BLIND-v04`

要求：

- project-only memory；
- zero prior task chats；
- zero Project files/knowledge/repo source；
- 不在当前 AI Research Stack Project；
- 不给 GitHub/Files/Plugin/web/connected apps访问；
- 不给 execution package 或 reveal map；
- 只给 sanitized blind packet。

在第一条盲评输出前记录：

- sanitized context identity；
- isolation mode；
- surface/model/effort；
- zero files/knowledge；
- zero prior task chats；
- blind packet hash；
- blind prompt hash。

无法证明隔离：W2不能 PASS。

## 10. blind Reviewer 只看 sanitized packet

使用：

`CLEAR_WRITING_W2_BLIND_REVIEW_PROMPT_V0_4_2026-10-18.md`

初评 Reviewer 只能看到：

- exact task id；
- exact prompt；
- opaque output labels + raw outputs；
- frozen rubric。

不得看到：

- execution order；
- timestamps；
- Project names；
- plugin/candidate identity；
- load evidence；
- account/workspace locator；
- reveal map。

当前 execution-ready Critic因已看到 reveal map，禁止兼任 blind Reviewer。

blind Reviewer必须是上述隔离 Project中的新 independent thread。

## 11. verdict freeze 后才能 reveal

把 P01-P08全部 verdict + reason 写入：

`results/clear-writing--every-response-invocation-policy/web-gate-v0.4/W2/blind/BLIND_VERDICTS_FROZEN.md`

先记录其 hash。

然后才允许 execution operator读取/use：

`CLEAR_WRITING_W2_REVEAL_MAP_V0_3_2026-10-18.json`

并生成 W2 causal summary。

不得 reveal 后重评分。

## 12. W3

只有 W2得到确定 PASS 或 FAIL 才可运行 W3。

W2 INCONCLUSIVE：

**W3 不运行。**

W3仍只做 no-bridge discoverability diagnostic，不能 rescue W2。

## 13. candidate failure/cleanup 语义

如果 candidate 已创建后出现 W0/W1/W2 FAIL 或 INCONCLUSIVE：

candidate保持：

**unchanged + PRIVATE**

本 Kickoff 不授权：

- uninstall；
- delete；
- update；
- publish；
- permission change；
- replacement candidate；
- second candidate。

后续 cleanup 必须另行明确授权。

## 14. evidence

全部 live evidence 只写：

`results/clear-writing--every-response-invocation-policy/web-gate-v0.4/`

至少保留：

- watcher proof；
- preflight；
- freeze manifest；
- bridge bytes/hash；
- candidate archive/file manifest；
- Web release parity；
- W0 raw outputs；
- W1 full turns；
- W2 raw arm evidence；
- blind context manifest；
- sanitized blind packet；
- frozen blind verdict/hash；
- reveal record/causal summary；
- W3 evidence（若 reachable）；
- attempt/retry log；
- RESULT；
- FINAL_REVIEW_INPUT_MANIFEST。

不得公开 account ID、credential、private URL、无关 Project 内容。

## 15. retry

每个 frozen task/turn/arm默认一个有效模型回答。

仅完全没有 usable model answer 的 transport/service failure允许一次技术 retry。

低质量、答错、格式错、plugin失效都是真实结果，不得重跑。

## 16. final independent review

执行结束后，不通过耗尽的 Reviewed Handoff CURRENT 做 reviewer transition。

直接使用冻结的 manual review prompt：

`docs/operations/prompts/CLEAR_WRITING_WEB_GATE_FINAL_REVIEW_PROMPT_V0_4_2026-10-18.md`

交给独立最终 Critic，读取完整实际 evidence。

最终 review artifact 写入：

`results/clear-writing--every-response-invocation-policy/web-gate-v0.4/final-review/`

不得写 REVIEW_1.md，不修改 CURRENT.review_round。

若 W0/W1/W2全 PASS，最大下一状态只写：

`READY_FOR_G7_FREEZE`

然后停止回 Planner。

## 17. G7 与其他范围禁止

本 Kickoff不执行：

- G7；
- real Project rollout；
- production change；
- release/version bump；
- PIE；
- Mica；
- Research Authoring；
- Presentations。
