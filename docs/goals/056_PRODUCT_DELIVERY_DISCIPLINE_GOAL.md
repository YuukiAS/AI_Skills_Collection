# 056 交付工作流可靠性基线 — Canonical Goal v0.5

- Historical task key：`056_product_delivery_discipline`
- Human-readable name：交付工作流可靠性基线
- Package version：`v0.5`
- Status：`AWAITING_INDEPENDENT_EXECUTION_PACKAGE_CRITIC`
- Prior reviewed package：`v0.4 @ 2df53f24964673fbf79cb3bcdab63b6dfd5ee4c4`
- Revision scope：关闭 `C056-E3-EXACT-WORKTREE-AUTHORIZATION`
- Plan：`docs/design/056_PRODUCT_DELIVERY_DISCIPLINE_IMPLEMENTATION_PLAN.md` v0.5
- Amendment：`docs/design/056_DELIVERY_WORKFLOW_RELIABILITY_BASELINE_V6_AMENDMENT_2026-09-21.md`
- Kickoff：`docs/operations/prompts/056_PRODUCT_DELIVERY_DISCIPLINE_KICKOFF.md` v0.5

本 Goal 在 Critic 对同一 v0.5 Plan + Goal + Kickoff 给 `READY_FOR_CODEX=YES` 且用户实际发送 approved Kickoff 前不可执行。

## 1. Positive outcome

把 v6 接入最新 production baseline，使复杂/高风险任务在正常入口下满足：

- agent-resolvable work 在找用户前由 agent 自己完成；
- 只有 genuine HUMAN_ONLY 才询问用户；
- 在因为某个实现路线权限不足而扩大 credential/provider 权限前，先检查 frozen Goal 是否存在已授权、权限更低且真正等价的路线；
- Default required human input 使用 durable plain-text transcript wait/resume，不依赖 auto-resolving native card；
- human action 后继续同一 Goal 的 integration closure，human action 本身不是 completion；
- acceptance/release/user-ready claim 需要 vertical closure、faithful evidence、actual surface 与 same-final-candidate evidence；
- repeat failure 不把用户/Reviewer当 debug loop；
- canonical design存在时由 Frontend Design真实消费；
- active rule存在但 real task仍失败时，AI Skills Maintainer先查 installed/generated/invocation/session/consumer path；
- 小任务不被强制升级成重型流程。

## 2. Architecture

保持 v6：

~~~text
Lite L1-L6
workflow-core W1-W5
Frontend Design F-A/F-B/F-C
AI Skills Maintainer production-consumption diagnosis
Bridge transport / wait-resume / recovery + Lite distribution
G1-G8
existing Source Discovery regression
~~~

没有 W6/W7/G9/G10，没有新 state/schema/ledger/controller/watcher。

## 3. Current baseline

AI_Skills：

~~~text
production/evidence baseline locator: 72f163330ea5a21637df95f08289e2c4739d2bd9
prior package commit: 2df53f24964673fbf79cb3bcdab63b6dfd5ee4c4
Repository / CLI: 5.0.6
workflow-core: 0.2
web-development: 0.1
ai-skills-core: 0.3
~~~

Bridge：

~~~text
planning baseline locator: 9d2da9f485f26ca51842a1909a276cb44f73351a
source version: 0.8.4
~~~

后续纯 docs/evidence SHA advance 不自动使本 Goal失效；相关 production overlap 才重审。

## 3.1 Exact execution branch / worktree locators

这些值属于本 Goal 的 frozen execution identity。用户发送 approved v0.5 Kickoff 后，才形成 current-user-visible authorization。

### AI_Skills_Collection

Exact branch：

`reviewed/056_product_delivery_discipline`

Exact worktree locator：

`../AI_Skills_Collection-056-product-delivery-discipline`

该 locator 以 verified canonical AI_Skills checkout root 为基准，解析为其父目录下同名唯一 sibling worktree。不得选择其他路径、第二个 worktree 或 `/tmp` clone。已有 exact locator 仅在 repo identity 与 exact branch 都匹配时复用；占用或不匹配则停止。

### GPT_Codex_AI_Bridge_Kit

Exact branch：

`reviewed/056_product_delivery_discipline`

Exact worktree locator：

`../GPT_Codex_AI_Bridge_Kit-056-product-delivery-discipline`

该 locator 以 verified canonical Bridge checkout root 为基准，解析为其父目录下同名唯一 sibling worktree。不得选择其他路径、第二个 worktree 或 `/tmp` clone。已有 exact locator 仅在 repo identity 与 exact branch 都匹配时复用；占用或不匹配则停止。

## 4. Required current implementation

### workflow-core

实现原 v6 W1-W5，并在 W2/G1 吸收 least-privilege equivalent recovery：

- 判断 permission gap 是 Goal-required 还是 chosen-route-required；
- 已授权 lower-priv route 只有在 security/privacy/product/evidence/quality 全等价时才自动切换；
- degraded/manual/fallback 不算 equivalent；
- route change 改 provider/data/security/product semantics 时仍 Human Gate / Planner；
- 不无限搜索替代方案。

### Frontend Design

完成原 F-A/F-B/F-C production wiring 与 actual-surface/self-QA contract；当前 web-development 0.1 仍需变更。

### AI Skills Maintainer

只完成 0.3 尚未覆盖的 residual production-consumption diagnosis；不重复 Gate lifecycle / semantic task identity 已完成工作。

### Bridge

完成原 v6 Host/HUMAN_ONLY residual：

- fail-closed Default required-input behavior；
- managed desired `default_mode_request_user_input=false` candidate；
- supported-key/current-version validation；
- durable transcript wait/resume docs/tests；
- preserve Plan mode、0.8.4 semantic identity、Persistent Run。

## 5. Version candidates

只有 production behavior完成并通过 release contract 时才形成：

~~~text
AI_Skills repository 5.0.6 -> 5.0.7 PATCH
workflow-core         0.2 -> 0.3
web-development       0.1 -> 0.2
ai-skills-core        0.3 -> 0.4
Bridge                0.8.4 -> 0.8.5
~~~

Planning docs commit 不改 version source。

## 6. Deferred / excluded

本轮不实现：

- Persistent Run tmux discovery、overnight durability、SSH reconnect、stale session、checkpoint/resume长期行为、duplicate-launch长期行为、progress/ETA；
- ordinary complex task generic bounded-kickoff renderer；
- task-local prohibition lifetime；
- acceptance comparison artifact semantic alignment/layout rendering；
- product-repo-specific fixes。

Persistent Run仍保持自己的名字和 execution-lifetime owner，不与普通 bounded kickoff 合并。

## 7. Product repo boundary

Bobbio、Lucerna、Mica、Asteria、SeminarArc、CUHK Date、CARE/EAT、Server/VPS、Longleaf_Bridge、Scientific Visualization production 均为 ZERO WRITE。必要时只读用于 Gate evidence。

## 8. Gates

G1-G8 保持数量与职责不变。least-privilege failure 只进入 G1 regression：

- optional higher-priv route权限不足 + equivalent authorized lower-priv route -> no Human Gate；
- lower-priv route会降低 security/quality/product semantics -> 不允许偷换，Human Gate保持；
- only valid route credential expired/revoked -> Human Gate保持；
- repeated same-class false permission blocker -> W4/G8 diagnosis，不重复找用户。

其余 G2-G8 与 Source Discovery regression 按 v0.5 Plan 执行。

## 9. Current execution authorization boundary

即使 Critic PASS，只有用户发送 approved Kickoff 后才授权 implementation stage。

该 Kickoff仍不授权：

- main merge / release / deploy；
- product repo write；
- real user Host Policy / CODEX_HOME mutation；
- paid API/Terra；
- final live user Host smoke；
- Persistent Run refinement；
- remote remap / force push；
- 新 provider/account/credential purpose。

## 10. Completion meaning

当前 implementation stage完成只表示：两个 exact branches / exact worktrees 下的实现、自测、non-host gate evidence、candidate freeze和 push完成，可以进入独立 implementation review。

056 overall complete 还需要原 Goal 后续有效的真实 integration/release boundary closure；不得因为 branch tests PASS就提前宣布。

`NEXT_HANDOFF = CRITIC`。
