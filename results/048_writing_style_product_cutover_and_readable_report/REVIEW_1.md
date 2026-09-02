---
schema: AI_BRIDGE_REVIEWED_REVIEW_V1
task_key: 048_writing_style_product_cutover_and_readable_report
review_round: 1
decision: REVISE
implementation_commit: 928de2325d781ca630883d03e0f381092675b269
---

# 048 Writing Style Product Cutover — Review 1

reviewed_implementation_commit: `928de2325d781ca630883d03e0f381092675b269`
reviewed_branch_tip: `fe7764636888e856bccf935c513bbf1c8b0a5ae5`
current_main_snapshot: `8faafd5a7ee60b394a53de5debfde3ccfe60b8cc`
review_round: 1
decision: `REVISE`

## 结论

048 已经把最难的私有报告链路真正跑通：安全私有文本转换已产生完整候选稿，最终私有全文 Text Review 为 `PASS`，公开回归和两组 should-not-fix 也提供了正向证据；当前 048 分支最新一次 `Codex Marketplace` CI（run `33613131960`）同样完成为 success。

但现在还不能进入 Product/Artifact PASS。剩下的是两个明确、可修复且都直接来自冻结 Plan 的 blocker：第一，048 为了让全库 CI 变绿，修改了 `presentations` 的 source/generated/tests，违反本任务明确的 out-of-scope 边界；第二，冻结 Plan 要求的真实 production invocation / normal installed entrypoint 证据仍然没有落地，现有 install smoke、unit tests 和 Executor 说明不能替代这一门槛。

这两个问题都不要求重新设计 scientific-rewrite，也不要求重做私有报告，更不允许回到 044/047。返修应严格限于清理 048 scope 和补齐真实 production evidence。

## 已通过、不得无故重做的部分

### 私有报告生成与独立全文审查

`results/048_writing_style_product_cutover_and_readable_report/text_transform/TEXT_TRANSFORM.json` 已记录真实 OpenAI Responses API transform 成功，最终 output plaintext SHA-256 为 `f5d19cd38993edd313801af396897efb7af5f65a0117494fb518866aceed3b5b`。对应 consumer workflow 固定使用 Bridge Kit commit `7c6fe7b1e59f03515188754641734b1c5311d532`，并保持 `store=false`、密文进 Git、结果重新 age 加密返回本机的边界。

随后 `results/048_writing_style_product_cutover_and_readable_report/text_review/TEXT_REVIEW.json` 对完整 source + 完整 candidate 给出 `overall_decision=PASS`，四个检查项——科学/来源保真、中文可读性、完整性、全文一致性——均为 PASS，且没有 blocking findings。Reviewer 当前没有证据要求重新生成这份私有稿。

### 公开回归

`PUBLIC_REGRESSION_REPORT.md` 中两个 positive regression 均记录 exact fidelity 通过且没有 critical semantic violation；Bobbio 的实际 candidate 也确实把 reader-facing 的 workflow 英文骨架改成了自然中文，同时保留 Zotero、Notion、Semantic Scholar、PubMed、arXiv、GPT、Codex 等正式名称。两组 should-not-fix 保持低编辑/不深改。

这些证据足以继续作为 048 fixed regression evidence，不需要换题或继续 Source Scout。

### 当前分支 CI 的机器事实

最新 048 branch tip `fe7764636888e856bccf935c513bbf1c8b0a5ae5` 的 `Codex Marketplace` run `33613131960` 已 completed/success。`CURRENT.ci_status` 可以记为机器事实上的 `PASS`。

但这个 CI PASS 不能单独支持 Product PASS，因为它包含下面的 scope contamination。

## Blocker 1：048 修改了明确禁止触碰的 presentations

冻结 Plan 的 Out of scope 明确写了“不修改 `presentations` … production behavior/version”。当前 branch 相对最新 main `8faafd5a7ee60b394a53de5debfde3ccfe60b8cc` 仍包含多项 presentations-only diff，包括但不限于：

- `skills/tools/documents-media/presentations/shared/scripts/generate_cuhk_scientific_layout_stage3.py`
- `skills/tools/documents-media/presentations/shared/scripts/validate_cuhk_scientific_layout_stage3.py`
- `skills/tools/documents-media/presentations/shared/scripts/validate_research_presentation_production_entry.py`
- 对应 `plugins/codex/plugins/presentations/...` generated copies
- `tests/test_presentations.py`

并且 branch 历史中存在 `7b9e4fa897ac814088c608175c536b652f0a5869`（`Repair unrelated presentation CI blocker`），其目的就是通过改变 presentations source/tests 来消除与 048 无关的 CI 失败。这违反了 048 的 frozen ownership 边界，也违反了本任务“不要修改 presentations”的明确要求。

独立核对最新 main 的 CI 也证明，这是一个预先存在的全库问题，而不是 048 writing-style 引入的问题：main commit `8faafd5a7ee60b394a53de5debfde3ccfe60b8cc` 的 run `33586884130` 本身就是 failure，其中包含多个 presentation render-probe test failure，另有 repository-version test 的既有不一致。048 不能通过顺手修另一个 plugin 来把这些 baseline failures 变成自己的绿灯。

### 最小返修要求

1. 从 048 的 candidate/integration diff 中移除所有本任务新增的 presentations source、generated payload 和 presentation-only test 改动；不得继续调整 presentations 来让 048 CI 变绿。
2. 重新同步/检查最新 main。若这些 baseline CI failures 已被独立修复，则在不引入 presentation diff 的前提下重跑 048 CI。
3. 若最新 main 仍有同一 pre-existing unrelated failure，记录它的 exact main commit/run/job 作为 baseline evidence，并保持 048 在可恢复等待状态；不要用 048 的 Reviewer budget 或业务 scope 去维修 presentations。

这不是要求 048 去修另一个项目，而是要求 048 恢复自己的边界。

## Blocker 2：真实 production maintenance / installed entrypoint gate 尚未证明

冻结 Plan 的 Installed production-entrypoint technical gate 要求：当前 generated `writing-style` 必须通过正常 Marketplace/plugin install 进入 isolated/shadow Codex environment，再用 fresh session 和普通用户请求证明：

- 长篇中文科研重写自动进入 `scientific-rewrite`；
- 轻度中文润色留在 `chinese-prose`；
- 仅数字/公式/引用审计留在 `writing-fidelity`；
- source-tree 直接调用、test-only router、普通 install smoke 都不能冒充该 gate。

同时 branch-local `CODEX_EXECUTOR.md` 与 `AGENTS.md` 要求中央 production plugin refinement 必须真实调用 production `ai-skills-core` maintenance companion；只读取 source SKILL、写“已遵守 maintainer”或运行项目测试不算 production invocation proof。

当前 task results 只提供了 public regression、private fidelity、Text Transform、Text Review 与 RESULT summary，没有单独的 production replay / normal-entry routing evidence；`RESULT.md` 记录的是生成检查、unit tests、temporary install smoke 与“AI Skills Maintainer 已读取/遵循”，不足以满足上面两个真实 runtime gate。

### 最小返修要求

1. 用当前真实 installed/enabled 的 exact `ai-skills-core` plugin id 运行一次受控 production maintenance preflight/replay，并保存不含秘密的输出证据。优先使用仓库规定的 `ai-bridge plugin-replay`，不要自行拼 raw nested `codex exec`。
2. 对当前 048 generated `writing-style` 做一次真正的正常安装入口验证：isolated/shadow 环境、fresh session、普通用户语言。至少固定并记录一个 heavy should-trigger、一个 light polish、一个 fidelity-only 请求及其实际 routing/skill exposure 结果。
3. 证据必须绑定当前 implementation/generated identity，并记录 exact plugin id、安装来源/生成身份、普通用户 prompt 与可观察 routing outcome。不能只补一段 Executor 自述。
4. 私有 Deep Research report 不需要、也不应再通过 Codex auth/replay来完成这一 gate；它已经由 secure transform + Text Review 独立覆盖。

## 非阻断说明

`TEXT_TRANSFORM.json` 当前 `bridge_kit_commit` 字段为空，但 consumer workflow 本身明确 pin 到 `7c6fe7b1e59f03515188754641734b1c5311d532`，`RESULT.md` 也记录同一 commit，因此 Reviewer 当前可以从独立证据确认 companion identity。本轮不把这个空字段单独升级成第三个 blocker；如果现有 transform tooling 能无风险补全元数据，可在不改变 private artifact identity 的前提下顺手修正，但不得因此重跑或改写已 PASS 的全文。

同样，private deterministic exact helper 曾对旧 ledger 报出若干 URL/path fragment 缺失，但独立 Text Review 对完整 source/candidate 已给出 fidelity PASS，现有 private-fidelity report 也把这些项归因为 extractor/ledger fragment，而没有发现 unresolved critical scientific drift。当前没有依据要求为了这些 helper false positives 重写全文。

## 返修边界

Review 1 只要求：

1. 清除 048 对 presentations 的越界修改，并把 pre-existing main CI failure 与 048 自身回归分开处理；
2. 补齐真实 `ai-skills-core` production invocation 与正常 installed `writing-style` routing evidence。

不要重新设计 scientific-rewrite，不要修改 044/047，不要重新 Source Scout，不要新增 phrase blacklist，不要重做已经 PASS 的 private transform/Text Review，也不要 bump version 或 merge main。完成最小返修后，再把同一 048 task 交给 Review 2。