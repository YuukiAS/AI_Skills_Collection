# 052 Writing Style Reader-Facing Generalization Closure — Canonical Goal

本文件是新 Codex Goal 的**顶层 completion contract**。内部 objective、bootstrap、phase、单个 commit、本地测试或某个 handoff 阶段都只是子目标，不能覆盖本文件。

默认用中文汇报；代码、命令、字段和路径保留原文即可。

## 1. 最终目标

完成 `052_writing_style_reader_facing_generalization_closure`，把 051 已验证的 writing-style heavy Chinese rewrite 主体收口为可发布版本，并真正完成：

`implementation -> known regression -> frozen fresh holdouts -> final Text Review -> full/release CI -> production install/upgrade smoke -> GPT Reviewer -> 用户最终验收 -> latest main integration -> remote verification`

只有以上全部通过，才允许把用户可见 Goal 标记为 `ACHIEVED`。

任何 `IN_PROGRESS / WAITING / READY_FOR_GPT_REVIEW / AWAIT_HUMAN_DECISION / REVISE / BLOCKED / PARTIAL_PROGRESS` 都不是 achieved。

## 2. 当前真实起点

目标 repo：`YuukiAS/AI_Skills_Collection`

现有本地 task-owned worktree：

`/tmp/ai-skills-052-20260910`

exact branch：

`reviewed/052_writing_style_reader_facing_generalization_closure`

已知本地提交：

- `7db1a09`：source-process framing / Text Review packet construction 修复；
- `4197093`：052 partial execution status。

上一轮报告称 branch 尚未 push，`CURRENT.state=EXECUTING`。因此第一步不是重做，而是定位并恢复现有 worktree/commits，确认真实状态后把合法工作 push 到 exact remote branch。

若上述 worktree 不存在，先按 commit/branch 定位现有本地工作；不要重新从头实现。

不得创建 053，不得重新开启 051。051 保持 `STOPPED / NOT_RELEASED / FINAL_TEXT_REVIEW_REVISE` 历史。

## 3. 先修复通用执行治理

052 已暴露两个与 writing-style 专业能力无关的通用 process regression：

1. 子 objective 完成被误报为整个 Goal achieved；
2. 有效 task commits 只留在本地，未 push 就结束 run，导致 Scheduled GPT 看不到 task。

开始后先检查当前 `main/AGENTS.md`。若以下语义尚未完整存在，做**最小 generic hardening**，单独 governance commit，并在最终集成时确保进入 main：

### 3.1 顶层 Goal 不得被子目标缩窄

用户当前明确给出的整体 Goal 是最高 completion contract。objective 文件读取、bootstrap、某 phase、implementation、tests、RESULT、CURRENT 更新、handoff 到另一角色，都不能单独触发 overall Goal achieved。

只要 frozen Goal 仍有 required product/artifact/review/CI/release/smoke/human/integration gate 未完成，整体状态必须保持真实的未完成状态。

### 3.2 Remote handoff 是硬条件

Reviewed Handoff 中，只要 tracked changes 需要后续 Executor、CI、Scheduled GPT Planner/Reviewer、human gate 或 integration 消费，当前 run 在 yield 前必须：

1. commit 合法工作；
2. push exact task branch；
3. 验证 remote tip 等于 intended local HEAD；
4. 写出真实 `CURRENT.next_action`。

local-only branch/worktree 不是有效 handoff。push 失败就是 push blocker，不能因此声称完成。

这只授权当前 exact task branch 的普通 non-force push，不是永久授权任意 `reviewed/*`，也不改变 Host Policy / Bridge Kit / execpolicy。

### 3.3 Process regression 必须回馈治理层

以后用户或真实运行指出 execution/workflow/control-plane 问题时，必须判断：换一个 AI_Skills task 是否仍可能重现？若 YES，且已有真实 failure、可命名 future failure、以及最小可执行防线，则优先补现有 AGENTS/workflow；不要只埋在 RESULT，也不要为了记录事故新增 state/schema/ledger/framework。

已已有规则覆盖的 stale CURRENT、重复授权、canonical replay 等不要再堆同义条款。

## 4. 本 Goal 的预授权边界

用户希望 hands-off 推进，正常情况下只在最终 artifact 验收时暂停。

本 Goal 被用户发送后，视为对以下**当前 052 范围**的明确授权：

- exact 052 branch 的普通 commit / fetch / non-force push；
- canonical candidate replay 所需的 repo-local pinned runtime、existing Codex account/CODEX_HOME、reserved temporary candidate identity/cache、install/remove/cleanup；
- exactly 2 个 public-safe fresh holdouts；
- exactly 1 次最终 `gpt-5.6-terra` candidate-only Text Review，沿现有 OpenAI/GitHub Actions provider/privacy path，`store=false`，worst-case `<= USD 0.25`，automatic paid retry `0`；
- required zero-paid CI；
- current approved environment 中 bounded writing-style production install/upgrade smoke；
- 最终用户 `ACCEPT` 后，conflict-free 的普通 latest-main integration + push。

不得复制 `auth.json` 到新环境，不得升级 global Codex，不得改 Host Policy，不得新造 runtime 架构，不得 force/destructive Git。

新的 provider、private-data scope、credential-copy path、更高 paid-cost boundary、破坏性 Git 或真实 integration conflict 才需要新授权。

## 5. 052 只解决两个 residual

不要重做 heavy rewrite architecture。

### 5.1 SOURCE_PROCESS_FRAME

Standalone reader-facing scientific/technical rewrite 应直接陈述技术内容，不应无必要地写：

- “原文指出/原文同时提到/原文在……中……”；
- “根据给定材料……”；
- “源文……”；
- “这里保留原文……”。

只有用户明确要求 source comparison、editorial commentary、peer review、translation commentary 或 provenance/audit 时才允许。

这不是 phrase blacklist。应在 semantic contract/audit 中表达“source/rewrite process framing 与 subject-matter exposition 的区别”。合法 scholarly attribution（作者、论文、引用）必须保留。

### 5.2 REVIEW PACKET CONSTRUCTION

评价 reader-facing artifact 的 Text Review plaintext 只能包含真实 candidate text 和自然文档标题；以下 wrapper identity 留在 manifest/metadata，不得进入被审正文：

`Gate / known regression / holdout / recovery / candidate / Planner / Reviewer / Executor / task id / commit / hash / workflow run`

若 reviewer finding 只命中 wrapper，而 candidate bytes 本身没有问题，应分类为 `REVIEW_PACKET_CONSTRUCTION_FAILURE`，不是 writing-style product failure。

先 targeted 检查 `7db1a09` 是否已正确实现；若已经正确，不要继续改 production。

## 6. Known regression 与 unrelated regressions

051 的 Bloom output 只作为 `KNOWN_REGRESSION`，不能再算 fresh evidence。

通过当前 canonical candidate replay 验证：ordinary prompt 自然进入 `scientific-rewrite`、actual candidate consumption、无 source-process framing、无 workflow wrapper leakage、meaning/exact objects preserved、cleanup PASS。

在冻结 fresh holdout 前同时跑：

- light Chinese polish；
- fidelity-only；
- English scientific-prose。

若 known regression 在 holdout freeze 前失败，只允许最小 generic repair；修后重跑 known regression。

## 7. Fresh holdout 一次冻结完整 batch

一次性冻结 exactly 2 个 public-safe fresh holdouts，来自两个不同 document family。

每个必须：Chinese/Chinese-dominant、真实 reader-facing scientific/technical prose、未用于 051/052 tuning、不是 workflow/CI/FINAL_REPORT/task result/plugin source。

冻结前做 semantic-completeness preflight：不得半句、半列表、停在“如下式/如下定义/如下图”之后、缺承诺公式/定义、或截断 section。

在任何 candidate generation 前记录 source locator、exact range、SHA256、document family、completeness evidence、acceptance questions。

batch 一旦冻结，production candidate 冻结。两个 holdout 任意一个真实 FAIL，则 whole batch FAIL；不得换第三个，不得 adaptive chasing，不得看失败文本后修改实现再重新声称 unseen。

## 8. 最终一次 Terra

仅在以下全部 PASS 后才 dispatch：

- Bloom known regression；
- unrelated regressions；
- fresh holdout 1/2；
- candidate frozen；
- review packet construction check。

Text Review plaintext 仅含：Bloom repaired candidate + fresh holdout 1 + fresh holdout 2，并使用自然文档标题。

本 task 最多 1 次 paid Text Review，`<= USD 0.25`，retry 0，不做 intermediate Terra，不做 review/repair/review loop。

若 pre-request infrastructure failure 且 `/v1/responses` 未发送，按 main AGENTS 的 unsent-call recovery 语义处理，不得重复问相同授权。

若实际 Terra `REVISE`，如实记录 `052_PRODUCT_REVIEW_FAIL`，不得私自开第二次 paid review，也不得标 achieved。

## 9. 跨 Planner / Reviewer 状态继续同一个 Goal

已有外部自动化 `052 Planner Reviewer Watch` 负责 GPT-owned 状态。

Codex 到达 GPT-owned state 时必须先 commit + push + verify remote + 写/推正确 CURRENT，然后等待/轮询 remote；当 CURRENT 回到 Executor-owned state 时，继续同一个 Goal，不要求用户手工中转 Planner/Reviewer 结果，也不能因为暂时交给其他角色就把 Goal 标 achieved。

若当前 remote branch 不存在，Scheduled GPT 无法工作；因此 remote handoff 是第一优先级。

## 10. Final CI / smoke / Reviewer / 用户验收 / integration

只有最终 Text Review PASS 后继续：

1. focused + full/release tests；
2. source/generated parity；
3. required full/release CI；
4. version/changelog closure（以届时 latest main + version policy 为准，不能沿用旧数字猜测）；
5. real production `writing-style` install/upgrade smoke；
6. ordinary natural heavy-route production smoke；
7. push `READY_FOR_GPT_REVIEW`，由 Scheduled GPT Reviewer 独立验收。

只有 GPT Reviewer PASS 后，才向用户发**唯一计划内人工暂停**：最终 artifact `ACCEPT / REJECT`。

用户 ACCEPT 后无需再次问“是否 merge”：fetch latest main，做 integration preflight，保留并发 main 修改，集成 052 + generic governance，push main，并验证 `origin/main` 与 intended integrated SHA 一致、released writing-style production identity 可正常使用。

## 11. Overall Goal completion predicate

仅当以下全部 TRUE 才能 `ACHIEVED`：

```text
bloom_known_regression=PASS
unrelated_regressions=PASS
fresh_holdout_1=PASS
fresh_holdout_2=PASS
terra_review=PASS
full_release_ci=PASS
production_install_upgrade_smoke=PASS
ordinary_production_routing=PASS
gpt_reviewer=PASS
human_acceptance=ACCEPT
integrated_latest_main=YES
remote_main_verified=YES
released_writing_style_identity_verified=YES
generic_governance_in_main=YES
```

任何一项 pending/false 都不得 achieved。

若 execution environment 因 context/time/tool limit 强制结束一个 run，而整体 Goal 未完成：报告 `PARTIAL_PROGRESS`；结束前 commit、push exact task branch、verify remote、写真实 CURRENT.next_action 和 remaining gates。不得再次用“前置目标已完成”代替整体状态。

## 12. 最终报告

最终至少输出：

```text
overall_goal_status=
goal_completion_predicate_satisfied=YES/NO
052_current_state=
local_head=
remote_052_tip=
remote_handoff_verified=
generic_governance_commit=
generic_governance_in_main=
implementation_commit=
bloom_known_regression=
unrelated_regressions=
fresh_holdout_1=
fresh_holdout_2=
terra_review=
full_release_ci=
production_smoke=
gpt_reviewer=
human_acceptance=
integrated_main_sha=
remote_main_verified=
released_writing_style_identity_verified=
```

若未 achieved，再输出 `remaining_gates / next_owner / next_action`。
