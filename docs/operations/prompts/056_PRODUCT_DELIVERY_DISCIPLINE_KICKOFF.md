# 056 交付工作流可靠性基线 — Codex Kickoff Draft v0.5

- Historical task key：`056_product_delivery_discipline`
- Human-readable name：交付工作流可靠性基线
- Plan：`docs/design/056_PRODUCT_DELIVERY_DISCIPLINE_IMPLEMENTATION_PLAN.md` v0.5
- Goal：`docs/goals/056_PRODUCT_DELIVERY_DISCIPLINE_GOAL.md` v0.5
- Amendment：`docs/design/056_DELIVERY_WORKFLOW_RELIABILITY_BASELINE_V6_AMENDMENT_2026-09-21.md`
- Prior reviewed package：`v0.4 @ 2df53f24964673fbf79cb3bcdab63b6dfd5ee4c4`
- Status：`DRAFT_NOT_AUTHORIZED`

只有独立 Critic 审完同一 v0.5 Plan + Goal + Kickoff，并返回 `READY_FOR_CODEX=YES` 后，用户实际发送下面的 Kickoff 正文，才构成 current-user authorization。

## Kickoff

执行 historical task `056_product_delivery_discipline` 的 v0.5 implementation stage；人类可读名称为“交付工作流可靠性基线”。

严格按 v0.5 Plan / Canonical Goal；不要重新设计已通过的 v6 architecture，不创建 successor，不把本任务扩成长期 program。

### 1. Exact branch / worktree authorization

我在这条当前用户消息中明确授权以下两个、且仅以下两个 execution branch / worktree pair。

#### AI_Skills_Collection

Exact branch：

`reviewed/056_product_delivery_discipline`

Exact task-owned worktree locator：

`../AI_Skills_Collection-056-product-delivery-discipline`

该 locator 必须相对 verified canonical AI_Skills_Collection checkout root 解析。先用当前 canonical repo 的 `git rev-parse --show-toplevel` 确认 root；目标是其父目录下 basename 精确为 `AI_Skills_Collection-056-product-delivery-discipline` 的唯一 sibling worktree。

不得选择其他 path、其他 basename、第二个 worktree 或 `/tmp` clone。若该 exact locator 已存在，只能在它属于同一 canonical repo 且绑定 exact branch 时复用；若被无关目录/worktree占用、repo identity不匹配或 branch不匹配，停止并报告，不得临场改用另一位置。

#### GPT_Codex_AI_Bridge_Kit

Exact branch：

`reviewed/056_product_delivery_discipline`

Exact task-owned worktree locator：

`../GPT_Codex_AI_Bridge_Kit-056-product-delivery-discipline`

该 locator 必须相对 verified canonical GPT_Codex_AI_Bridge_Kit checkout root 解析。先用当前 canonical repo 的 `git rev-parse --show-toplevel` 确认 root；目标是其父目录下 basename 精确为 `GPT_Codex_AI_Bridge_Kit-056-product-delivery-discipline` 的唯一 sibling worktree。

不得选择其他 path、其他 basename、第二个 worktree 或 `/tmp` clone。若该 exact locator 已存在，只能在它属于同一 canonical repo 且绑定 exact branch 时复用；若被无关目录/worktree占用、repo identity不匹配或 branch不匹配，停止并报告，不得临场改用另一位置。

这两个 exact branch/worktree pair 属于同一个 frozen effect。后续到达 `git worktree add`、branch creation、task-owned commit/push 等同一已授权执行步骤时，不要仅因为阶段较晚再次询问授权。

### 2. Source / identity preflight

当前 planning locators：

~~~text
AI_Skills production/evidence baseline = 72f163330ea5a21637df95f08289e2c4739d2bd9
Prior v0.4 package commit              = 2df53f24964673fbf79cb3bcdab63b6dfd5ee4c4
Bridge planning baseline               = 9d2da9f485f26ca51842a1909a276cb44f73351a
~~~

开始前 fetch/re-read current main，核对 canonical repository identity、origin fetch destination、所有 effective push destinations、branch/version sources 和 dirty ownership。

如果 main 只新增无关 docs/evidence commit，刷新 locator后继续，不因 SHA 前进停止。只有 production/version/release/frozen semantics 与本 v0.5 scope 实质 overlap 才停止并返回 Planner/Critic。

不得 remap remote、改 pushurl 或通过修改 Git config 让 identity check 通过。

### 3. 我在这条消息中授权的 bounded implementation effects

仅对本 frozen Goal 和上面两个 exact branch/worktree pair：

- 创建或复用上面唯一冻结的 task-owned worktree；
- 创建或使用上面唯一冻结的 reviewed branch；
- 对这两个 task branch 做普通 task-owned edit / test / stage / commit / non-force push；
- 运行本 Goal 已声明的本地/fixture/normal-entry验证；
- 生成 task-owned results/evidence。

这是一次性 bounded authorization。后续到达同一个 frozen effect 时不要仅因为进入较晚阶段再次询问。

任何新的 provider/account/credential purpose、真实 Host mutation、paid call、deployment、main merge/release、产品 repo write 或本 Goal 外副作用不在授权内。

### 4. AI_Skills write scope

只改：

- workflow-core：W1-W5、W2 least-privilege equivalent recovery、Source Discovery residual enforcement；
- web-development：F-A/F-B/F-C 与已有 Figma-handoff/motion production wiring；
- ai-skills-core：0.3 尚未覆盖的 production-consumption diagnosis；
- 对应 tests / regression fixtures；
- canonical source -> generated Marketplace parity；
- candidate version/changelog/release metadata；
- 056 task-owned evidence。

保护当前 5.0.6 已完成的 semantic task identity、Gate lifecycle、regression bank、broad/full fallback、same-final-candidate behavior。不要重新实现 task-key parser，也不要改 domain plugin专业语义。

当前 version baseline：

~~~text
Repository 5.0.6
workflow-core 0.2
web-development 0.1
ai-skills-core 0.3
~~~

如果形成正式 candidate，预期：

~~~text
Repository 5.0.7 PATCH
workflow-core 0.3
web-development 0.2
ai-skills-core 0.4
~~~

必须按当前 version policy从 source重新判断；若某项行为已经被 compatible main完整实现并由 normal-entry evidence证明，则该 plugin `NO_BUMP`，不机械升级。

### 5. Bridge write scope

当前 version baseline `0.8.4`。只改原 v6 residual：

- managed desired `default_mode_request_user_input=false` candidate；
- supported-key / desired-state validation；
- HUMAN_ONLY durable transcript wait/resume Host/Lite guidance与 tests；
- 必要的 README/changelog/version candidate parity。

若形成 compatible candidate，预期 `0.8.5`。

必须保护：

- 0.8.4 semantic task-key兼容；
- 0.8.3 fresh-root/raw-byte/Lite behavior；
- 0.8.1 upfront authorization；
- 0.8.0 Persistent Run；
- Plan-mode合法 user-input behavior。

不要修改 Persistent Run production source或其 progress/ETA TODO。

### 6. W2 Human Gate / least-privilege hard contract

任何 user-input request 前先按 v6 分类：

`HUMAN_ONLY / AGENT_RESOLVABLE / UNSUPPORTED_WITH_EVIDENCE / OPTIONAL_NOT_REQUIRED_FOR_CURRENT_CLOSURE / SAFETY_OR_AUTHORITY_BLOCKER`。

只有 genuine `HUMAN_ONLY` 可以进入普通 Human Gate。

如果 blocker 表面上是 credential scope / provider permission / paid resource / environment mutation，不要立即找用户。先做 bounded check：

1. 这是 frozen Goal 的必要权限，还是当前实现路线才需要？
2. 当前 source/environment 是否已经存在被授权的 lower-privilege候选路线？
3. 该路线是否保持 security/privacy、product behavior、evidence quality、quality bar、provider/data/purpose boundary完全等价？

如果全部满足，自动使用等价低权限路线继续；不要要求用户扩大权限。

如果 route 会改变 provider/account/data/security/product semantics，或只是 degraded/manual/fallback，就不能冒充 equivalent，按现有 Human Gate/Planner处理。

不要为了避免询问而无限搜索新 provider、安装新基础设施或扩大 scope。

blocker report 必须区分 missing / expired / revoked credential 与“credential 只对某条可选路线权限不足”。

### 7. Durable HUMAN_ONLY wait/resume

Default required human input 不使用 native `request_user_input` permission card。按：

~~~text
preserve Goal/resume point/prompt identity
-> one concise plain-text question
-> stop dependent execution
~~~

没有回答时不得 default infer、polling、auto retry、timeout-continuation。

在当前 task合法 handoff boundary仍未回答时，如实报告：

~~~text
GOAL_BLOCKED=YES
GOAL_ACHIEVED=NO
COMPLETE=NO
READY_FOR_USER_REVIEW=NO
DEPENDENT_EXECUTION_BLOCKED=YES
~~~

使用现有合法 recovery representation，不新增 state enum。

后续 explicit in-scope reply：重读当前 Goal/resume identity -> consume once -> same-Goal exact-once resume -> post-action closure。

### 8. G1-G8

不新增 Gate。

G1 额外加入 least-privilege regression：

- optional high-priv route lacks permission + equivalent authorized lower-priv route -> no Human Gate，继续；
- lower-priv route降低 security/quality/product semantics -> 不自动替代；
- only valid route credential expired/revoked -> Human Gate；
- same-class false permission blocker重复出现 -> W4/G8 diagnosis，不重复索权。

G2-G8 和 Source Discovery regression 按 v0.5 Plan执行。

本轮是 shared workflow/default prompt/Marketplace/cross-plugin change，release selection保持 `BROAD_FULL_FALLBACK`，所有 release-critical evidence绑定同一 final candidate。

### 9. Product repositories ZERO WRITE

不得修改、branch、commit、push：

- Bobbio
- Lucerna
- Mica-for-ChatGPT
- Asteria
- SeminarArc
- CUHK Date
- CARE/EAT
- Server/VPS
- Longleaf_Bridge
- Scientific Visualization production

只在 Gate 已冻结且必要时读 evidence。

### 10. 明确不做

不要：

- 实现 ordinary complex task generic bounded-kickoff renderer；
- 修改 Persistent Run / tmux discovery / progress ETA；
- 实现 task-local prohibition expiry；
- 实现 acceptance comparison artifact packaging；
- 新增 W6/W7/G9/G10；
- 新增 authorization database/state/schema/ledger/controller/watcher；
- fork Codex；
- call paid API/Terra；
- merge main、tag、release、publish、deploy；
- 修改真实 CODEX_HOME / Host Policy；
- 做 final live W2/G1 user smoke；
- remote remap / force push；
- 使用上面两个 exact worktree locator 之外的路径；
- 引入新的 provider/account/credential purpose。

### 11. Validation / handoff

先 cheap focused regression，再 broad/full。完成 source/generated parity、candidate plugin replay / normal-entry evidence、full relevant test、should-not-change和同一 final candidate freeze。

两个 exact task branches ordinary non-force push后，写清：

- AI_Skills exact candidate commit + generated hashes；
- Bridge exact candidate commit；
- candidate versions；
- G1-G8 / Source Discovery在本授权 surface 的 evidence；
- exact branch/worktree identity；
- product repos zero-write；
- real Host integration仍 pending（如果仍需要）。

然后停止：

`NEXT_HANDOFF = INDEPENDENT_IMPLEMENTATION_REVIEW`

不得宣布 overall 056 achieved。
