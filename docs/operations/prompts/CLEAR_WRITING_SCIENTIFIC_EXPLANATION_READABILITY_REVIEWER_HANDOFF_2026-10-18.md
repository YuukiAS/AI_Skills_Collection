你现在作为 Clear Writing 的独立实现 Reviewer，审查现有 Reviewed Handoff 任务；不要重做架构，也不要重新设计产品。

Active Review Context：

- target_repo: `YuukiAS/AI_Skills_Collection`
- target_plugin_or_domain: `writing-style / Clear Writing / response-clarity`
- task: `clear-writing--scientific-explanation-readability-repair`
- branch: `reviewed/clear-writing--scientific-explanation-readability-repair`
- review_stage: `implementation / product-artifact review after required CI PASS`
- implementation_commit: `fd7a1578a5042a46a55c5b638f6d550655b1096b`
- required CI: `39109965934` PASS
- CI branch head: `03dadfb75eba3e609b10411f8177c13644f5683f`
- current state: `READY_FOR_GPT_REVIEW / ci_status=PASS / review_round=0`

先按当前 main 的 Reviewed Handoff Reviewer contract 和 Critic role contract，实际读取：

- `automation/reviewed_handoff/tasks/clear-writing--scientific-explanation-readability-repair/REQUEST.md`
- `automation/reviewed_handoff/tasks/clear-writing--scientific-explanation-readability-repair/PLAN.md`
- `automation/reviewed_handoff/tasks/clear-writing--scientific-explanation-readability-repair/CURRENT.json`
- `results/clear-writing--scientific-explanation-readability-repair/RESULT.md`
- `results/clear-writing--scientific-explanation-readability-repair/REAL_WEB_KNOWN_REGRESSION_BANK_V2.md`
- implementation commit 的真实 diff
- required CI `39109965934` 的真实 jobs/steps/logs

本轮不要只看测试摘要。必须实际读取当前最终候选的 9 组完整输出：

`results/clear-writing--scientific-explanation-readability-repair/web-regression-post-repair/fd7a157/`

并实际读取四组 should-not-change 输出：

`results/clear-writing--scientific-explanation-readability-repair/should-not-change/fd7a157/`

审查目标只限冻结 Plan：

1. KR-WEB-01..09 是否全部真实满足冻结标准，而不是靠关键词或机械格式规则取得 PASS；
2. KR-WEB-06 是否真正按完整语义/推理单元成段，避免一句一段、无价值小标题链和公式碎片化，同时没有机械压短复杂解释；
3. KR-WEB-09 是否真正对陌生方法/术语/多重下标对象建立不越权的 reader mental model，再进入正式术语/公式；信息不足时是否明确缺定义而没有猜科学含义；
4. KR-WEB-03、08、09 的正向部分是否继续保留必要例子、真实对照、因果解释、公式直觉、限制和不确定性；
5. KR-WEB-07 是否继续做到普通概念自然中文化，同时正式方法名、稳定缩写和机器字符串保持精确；
6. 四组 should-not-change 是否仍保护完整 report/prompt/contract、真正复杂结构、pure machine output bypass 和 exact identities；
7. `response-clarity` 是否仍只负责普通解释层，没有接管 `chinese-prose` / `scientific-rewrite` / Research Authoring / Presentations；
8. source/generated parity、full tests、Marketplace 和 required CI 是否与同一最终候选链一致；
9. 外部 Presentations portability blocker 的修复只作为 CI 解阻证据，不得把 broader Presentations 工作带入本 review。

必须明确区分：

- PROCESS PASS
- PRODUCT / ARTIFACT PASS

CI、tests、parity 只能证明 process。Product PASS 必须来自你实际阅读 9 组最终输出与四组保护输出。

请给 `PASS` 或 `REVISE`。

若 `REVISE`：
- 每条 blocker 必须引用冻结 Plan/known regression、实际输出证据、因果风险、最小修复条件；
- 不得新增第三个产品缺口、重开架构或把 Web A/E/B/C、G7 提前塞进本轮；
- 按现有 Reviewed Handoff review budget 路由。

若 `PASS`：
- 明确说明本次只批准 repo/Codex known-regression candidate；
- 明确写出这不代表 ChatGPT Web automatic selection、A/E、B/C、fresh G7、用户验收或正式 release 已通过；
- 下一阶段按原冻结路线进入真实 ChatGPT Web A/E、B/C matched comparison，再做完整 frozen fresh G7，最后用户验收与 release closure；
- broader Presentations 与 Research Authoring 继续暂停，不得借 PASS 启动。

不要修改 production candidate。不要进行新的 recovery design。
