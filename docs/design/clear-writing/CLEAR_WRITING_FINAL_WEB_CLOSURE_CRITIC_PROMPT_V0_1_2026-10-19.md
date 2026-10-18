# Clear Writing 最终 Web 收尾最小验收 v0.1 — Critic 复核 Prompt

你现在担任 Clear Writing 最终网页端收尾验收方案的独立 Critic。

本轮是对上一轮唯一 blocker `CW-FWC-01` 的最小复核。

不要重开：

- invocation-policy proposal v0.2；
- 六技能架构；
- frozen production candidate；
- KR-WEB-01..09；
- 四组 should-not-change；
- repo/full CI；
- independent artifact review；
- PRIVATE plugin parity；
- W2 4/7 matched scoring；
- PIE / Mica / Research Authoring / Presentations。

也不要执行任何测试。

## Active Review Context

- target_repo:
  `YuukiAS/AI_Skills_Collection`
- target_plugin_or_domain:
  `writing-style / Clear Writing`
- design_topic_or_task_key:
  `clear-writing--final-web-closure-minimal-gate`
- source/evidence branch:
  `reviewed/clear-writing--scientific-explanation-readability-repair`
- review_stage:
  `minimal final Web closure gate revision after CW-FWC-01`
- frozen production candidate:
  `fd7a1578a5042a46a55c5b638f6d550655b1096b`
- approved invocation-policy proposal:
  `docs/design/clear-writing/CLEAR_WRITING_EVERY_RESPONSE_INVOCATION_POLICY_PROPOSAL_V0_2_2026-10-18.md@1f905d294c3c2e5b0951c9d5e818c285d236cef7`
- proposal Critic PASS:
  `50e09a2dc68a097ef21e0cf245f7951eb9d06f89`
- Web Gate v0.4 execution-ready Critic PASS:
  `docs/design/clear-writing/CLEAR_WRITING_WEB_GATE_EXECUTION_READY_CRITIC_REVIEW_V0_4_2026-10-18.md@dc76d19691c222e475f48971ddb98225f27b6dad`
- historical W2:
  `results/clear-writing--every-response-invocation-policy/web-gate-v0.4/preflight/W2_MATCHED_ENVIRONMENT_PREFLIGHT.md`
- historical W2 result:
  `INCONCLUSIVE`
- tracking Issue:
  `#13`

## 先读取

先读取最新 main：

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md`

然后从 source/evidence branch 完整读取本轮 package：

- `docs/design/clear-writing/CLEAR_WRITING_FINAL_WEB_CLOSURE_MINIMAL_GATE_V0_1_2026-10-19.md`
- `docs/goals/CLEAR_WRITING_FINAL_WEB_CLOSURE_GOAL_V0_1_2026-10-19.md`
- `docs/operations/prompts/CLEAR_WRITING_FINAL_WEB_CLOSURE_TEST_PROTOCOL_V0_1_2026-10-19.md`

package commit：

`79092d4d28045a75a33eed3fd505f115f3fa6a1c`

同时读取：

- `results/clear-writing--scientific-explanation-readability-repair/REAL_WEB_KNOWN_REGRESSION_BANK_V2.md`
- prior implementation/product review；
- PRIVATE plugin identity/parity evidence；
- historical W2 INCONCLUSIVE evidence。

## 唯一 finding：CW-FWC-01

上一轮 Critic 已判断：

> 4 个回答的数量本身不是问题；真正缺的是原 4-answer gate 没有必然直接覆盖一个不同的兄弟写作任务族，也没有必然直接覆盖 frozen candidate 最新复杂科研解释行为。

Planner 本轮接受该 finding，而且**不增加第五个回答**。

最终 4 个回答改为：

1. Test 1：
   显式真实 PRIVATE `@Clear Writing`；
   普通技术状态解释；
   自然中文；
   结论优先；
   exact branch/status/command；
   不改变事实强度。

2. Project Turn 1：
   不手工 @；
   新的 `scientific-rewrite` 类型 source-faithful 科研技术重写；
   包含多重下标公式链、未定义对象、尚未验证限制和 exact machine identities；
   允许段落重组；
   禁止 claim/formula/variable/validation-status 漂移；
   禁止猜未定义对象；
   禁止机械压短。

3. Project Turn 2：
   不手工 @；
   pure exact JSON：
   `{"status":"PENDING","retry":false,"count":2}`
   assistant message 必须逐字符完全一致。

4. Project Turn 3：
   不手工 @；
   新的复杂科研普通解释；
   包含多重下标对象、后续用途、信息不足对象；
   必须先建立对象/层级/用途，再进入公式关系；
   禁止根据符号形状猜科学含义；
   必要解释不得机械压短；
   同时验证 Turn 2 exact-only 后普通中文解释恢复。

总数必须继续严格等于 4。

## 复核 1：CW-FWC-01 是否关闭

请直接检查 Protocol 中 Turn 1 / Turn 3 的 exact prompts。

判断：

- Turn 1 是否真的属于不同于 ordinary response 的 sibling writing family；
- 它是否真实检验 source-faithful structure rewrite，而不是普通解释换壳；
- Turn 3 是否直接覆盖 KR-WEB-06 / KR-WEB-09 最新修复的核心机制：
  - 语义/推理单元成段；
  - multi-index object reader model；
  - downstream use；
  - 未定义对象不猜；
  - necessary depth 不机械压短；
- Turn 1 / Turn 3 是否是新的 public-safe 输入，而不是直接重用 KR-WEB-01..09。

若这些成立：

`CW-FWC-01=CLOSED`

如果仍有缺口，只允许指出**哪个不同能力仍完全没有被 4 个回答或已有证据观察到**。

禁止以“多测几个更保险”为 blocker。

## 复核 2：四回答 + 已有证据是否足够进入 release closure

已有证据不能当不存在：

- KR-WEB-01..09；
- 四组 should-not-change；
- focused/full tests；
- required CI；
- source/generated parity；
- independent PROCESS + PRODUCT / ARTIFACT review；
- real PRIVATE plugin identity/parity。

判断最终 4-answer gate 是否合理只补真实 Web runtime / normal-entry 缺口，而不是重新做人肉回归。

如果认为仍不足，必须明确：

- 缺哪个 distinct capability；
- 为什么已有 evidence 没覆盖；
- 为什么本 4-answer gate 也没覆盖；
- 为什么它对**当前收窄 release claim**仍然是 release-critical。

不得用样本数直觉代替能力分析。

## 复核 3：release claim boundary

四回答 PASS 后只允许声称：

- 显式真实 Clear Writing 入口工作正常；
- 薄 Project policy + installed Clear Writing 下连续用户行为达到预期；
- exact-only 不受污染；
- 至少一个 sibling writing family 在真实 Web normal entry 下行为正确；
- 当前复杂科研解释修复在真实 Web 得到直接观察。

明确禁止：

- `PLUGIN_LOADED_EVERY_TURN=PASS`
- 每轮后台必然加载 Clear Writing
- plugin 相对于相同 Project setting 的独立因果增量已证明

请判断该 claim 是否与 4-answer evidence 精确匹配。

## 复核 4：W2 是否可以退出 release blocker

历史 W2 保留：

`W2=INCONCLUSIVE`

本方案不把它改判 PASS。

只因为正式 release claim 不再包含“plugin 的独立因果增量”，所以 strict matched W2
退出 release blocker。

请独立判断：

- 这是否是合理的 claim narrowing；
- 是否仍保留历史诊断事实；
- 是否避免把 behavioral PASS 冒充 causal PASS；
- 是否有真实用户能力只能由 W2 观察，而当前 release claim 又确实承诺该能力。

如果没有，则 W2 不应继续阻塞。

## 复核 5：PASS 后是否真正停止加 Web Gate

方案冻结：

四回答全部 PASS 后：

`READY_FOR_RELEASE_CLOSURE=YES`

后续 release-critical 工作只允许：

- repository/plugin version；
- README；
- changelog；
- release branch；
- source/generated/release identity；
- final CI；
- actual released plugin identity/parity。

不得再因为“可能还可以测”追加新的 Web Gate。

只有实际 4-answer run 暴露一个此前合同未覆盖的新产品失败，才能重新进入 Planner/Critic。

判断该 stop rule 是否足够明确。

## 输出

给：

`PASS` 或 `REVISE`

若 `REVISE`：

- 只允许围绕 `CW-FWC-01` 或本轮修订直接引入的新 blocker；
- 不得增加第五个回答，除非你能证明一个 distinct release-critical capability 完全无法由已有 evidence + 当前 4-answer gate 观察；即使如此，也应优先要求替换/合并当前回答，而不是增加总数；
- 使用 stable finding ID；
- 自动给 Planner 一个完整最小返修 prompt。

若 `PASS`：

必须明确输出：

```text
DECISION=PASS
CLOSED_FINDINGS=CW-FWC-01
FINAL_WEB_GATE_TEST_COUNT=4
W2_RELEASE_BLOCKER=NO
RELEASE_CLOSURE_IF_PASS=YES
NEXT_HANDOFF=PLANNER
```

并明确：

本 PASS 只批准“最终 4-answer Web closure gate v0.1”。

它不代表：

- 4 个回答已经执行；
- 4 个回答已经 PASS；
- release closure 已执行；
- version bump / release branch / README / changelog / final CI 已完成；
- 正式 release 已完成。

如果 PASS，下一步只允许 Planner 给出这 4 个冻结测试的最短用户执行入口；不要启动 Codex，不要修改 production，不要先做 release closure。
