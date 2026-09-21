# 056 交付工作流可靠性基线 — v0.5 Critic Recheck Prompt

你是 AI Research Stack 的长期独立 Critic thread。

当前继续审 historical task `056_product_delivery_discipline`。这不是重新设计 056。本轮 Planner 只针对你上一轮唯一 blocker：

`C056-E3-EXACT-WORKTREE-AUTHORIZATION`

提交了 v0.5 execution package 修订。

不要实现代码，不创建 branch/worktree，不启动 Executor，不调用 paid API，不修改 production，也不替用户发送 Kickoff。

## Active Review Context

target_repo:
- YuukiAS/AI_Skills_Collection
- cross-repo dependency: YuukiAS/GPT_Codex_AI_Bridge_Kit

target_plugin_or_domain:
- workflow-core / Verified Workflow
- web-development / Frontend Design
- ai-skills-core / AI Skills Maintainer
- Bridge Host/Lite human-input transport

design_topic_or_task_key:
- historical technical locator: 056_product_delivery_discipline
- human-readable name: 交付工作流可靠性基线

review_stage:
EXECUTION_READY_PACKAGE_RECHECK_AFTER_C056_E3

prior reviewed package:
- AI_Skills main@2df53f24964673fbf79cb3bcdab63b6dfd5ee4c4
- package version: v0.4

prior Critic:
- chat-only independent review
- DECISION=REVISE
- only blocker: C056-E3-EXACT-WORKTREE-AUTHORIZATION
- no Critic repo write/commit

## 一、先读取 current source

按 Critic Role Contract 读取 AI_Skills 最新 main：

- AGENTS.md
- docs/workflows/PLANNER_ROLE_CONTRACT.md
- docs/workflows/CRITIC_ROLE_CONTRACT.md
- docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md
- docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md

然后读取 v0.5 package：

- docs/design/056_PRODUCT_DELIVERY_DISCIPLINE_IMPLEMENTATION_PLAN.md
- docs/goals/056_PRODUCT_DELIVERY_DISCIPLINE_GOAL.md
- docs/operations/prompts/056_PRODUCT_DELIVERY_DISCIPLINE_KICKOFF.md
- docs/design/056_PRODUCT_DELIVERY_DISCIPLINE_REVIEW_PACKAGE.md

Architecture amendment保持不变，只需作为 authority locator：

- docs/design/056_DELIVERY_WORKFLOW_RELIABILITY_BASELINE_V6_AMENDMENT_2026-09-21.md

Bridge 只需核对 latest main 是否发生与 056 frozen semantics 直接相关的 production/version drift。Planner本轮核对时 Bridge仍为：

`main@9d2da9f485f26ca51842a1909a276cb44f73351a`
`version 0.8.4`

纯 docs/evidence locator advance 不触发重审。

## 二、上一轮已经接受的内容不要重开

除非 latest source 出现新的直接语义证据，保持以下已接受结论：

- human-readable name“交付工作流可靠性基线”；
- historical key保留；
- bounded baseline task，而非 evergreen mega-task；
- V6_BOUNDED_AMENDMENT；
- least-privilege recovery -> W2/G1；
- no W6/G9；
- Persistent Run durability = Bridge-only followup；
- ordinary bounded kickoff renderer = post-056 workflow-core；
- task-local prohibition expiry = post-056 workflow-core；
- acceptance packaging = post-056 workflow-core + domain/artifact owner；
- G1-G8保持；
- Source Discovery不变G9；
- BROAD_FULL_FALLBACK / cheap deterministic first / same-final-candidate；
- 5.0.6 -> 5.0.7 PATCH；
- workflow-core 0.2 -> 0.3；
- web-development 0.1 -> 0.2；
- ai-skills-core 0.3 -> 0.4仅限residual diagnosis，或 direct normal-entry evidence支持 NO_BUMP；
- Bridge 0.8.4 -> 0.8.5；
- C056-E1已关闭；
- C056-E2已由 Critic Role Contract v1.4关闭。

## 三、优先复核 C056-E3

上一轮 finding：

`C056-E3-EXACT-WORKTREE-AUTHORIZATION`

Requirement：
Goal/Kickoff 当前用户消息必须明确绑定 exact branch + exact task-owned worktree，不能把 worktree location留给 Executor临场决定。

v0.5 现在冻结：

### AI_Skills_Collection

Exact branch：

`reviewed/056_product_delivery_discipline`

Exact worktree locator：

`../AI_Skills_Collection-056-product-delivery-discipline`

解析基准：

verified canonical AI_Skills_Collection checkout root，即当前 canonical repo 的 `git rev-parse --show-toplevel` 结果。

### GPT_Codex_AI_Bridge_Kit

Exact branch：

`reviewed/056_product_delivery_discipline`

Exact worktree locator：

`../GPT_Codex_AI_Bridge_Kit-056-product-delivery-discipline`

解析基准：

verified canonical GPT_Codex_AI_Bridge_Kit checkout root。

Plan / Goal / Kickoff 都应明确：

- 不是相对任意 shell cwd；
- 必须解析到 canonical root 父目录下 exact basename sibling；
- 不允许其他 worktree path、第二个 worktree或 /tmp clone；
- exact locator 已存在时只有 repo identity + exact branch都匹配才复用；
- occupied/mismatched则停止，不自动选备用路径；
- 用户实际发送 approved Kickoff后，这两个 exact branch/worktree pair才成为 current-user authorization；
- 后续到达同一 frozen effect时不重复询问。

请逐项核对 Plan / Goal / Kickoff 是否完全一致。

## 四、只检查本次 amendment impact

确认 v0.5 没有趁机扩大：

- remote mutation；
- force push；
- main merge/release/deploy；
- product repo write；
- real CODEX_HOME/Host install；
- paid API/Terra；
- Persistent Run refinement；
- provider/account/credential purpose；
- architecture/Gate/version/defer semantics。

Review Package应明确：

`ARCHITECTURE_CHANGE=NO`
`GATE_CHANGE=NO`
`LEAST_PRIV_SEMANTICS_CHANGE=NO`
`VERSION_ROUTE_CHANGE=NO`
`DEFER_DISPOSITION_CHANGE=NO`

## 五、不要制造新的 review loop

本轮 package v0.5只是为关闭 E3形成新的 execution-package identity。

如果 latest main只比 Planner提交时多 docs/evidence commit，不得因此 REVISE。

只有：
- C056-E3没有真正关闭；
- locator表达仍不唯一；
- Kickoff仍不能形成 current-user-visible authorization；
- 本轮修改意外扩大 scope；
- 或 latest production source出现与 frozen package直接冲突的新事实；

才允许新增/保留 blocker。

## 六、输出

先用正常中文给结论。

如果 REVISE：

- 优先围绕 C056-E3；
- 每条 blocker给 requirement / direct evidence / causal risk / minimum closure / owner；
- 不换措辞移动终点；
- 自动附完整 COPY TO PLANNER prompt。

如果 PASS：

由于同一 056 major round此前有正式 REVISE，先按 CRITIC_ROLE_CONTRACT v1.4给用户可读 closure explanation。

至少明确：

- C056-E3如何关闭；
- exact AI_Skills worktree；
- exact Bridge worktree；
- 其余 architecture/Gate/least-priv/defer/version/C056-E1/E2保持不变；
- PASS不授权 main merge/release/paid/real Host。

随后输出：

`C056-E3=CLOSED`
`READY_FOR_CODEX=YES`
`NEXT_HANDOFF=CODEX`

并给出：

- APPROVED_PLAN_PATH
- APPROVED_GOAL_PATH
- APPROVED_KICKOFF_PATH
- APPROVED_PACKAGE_COMMIT

最后逐字输出 repo 中被审过的 v0.5 Kickoff正文，不要重新改写。
