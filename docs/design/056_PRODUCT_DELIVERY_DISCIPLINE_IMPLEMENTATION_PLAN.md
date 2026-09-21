# 056 交付工作流可靠性基线 — Implementation Plan v0.5

- Historical task key：`056_product_delivery_discipline`
- Human-readable name：交付工作流可靠性基线
- Package version：`v0.5`
- Status：`READY_FOR_INDEPENDENT_EXECUTION_PACKAGE_CRITIC_REVIEW`
- Prior reviewed package：`v0.4 @ 2df53f24964673fbf79cb3bcdab63b6dfd5ee4c4`
- Revision scope：只关闭 `C056-E3-EXACT-WORKTREE-AUTHORIZATION`
- AI_Skills production/evidence baseline：`main@72f163330ea5a21637df95f08289e2c4739d2bd9`
- Bridge planning baseline：`main@9d2da9f485f26ca51842a1909a276cb44f73351a`
- Amendment authority：`docs/design/056_DELIVERY_WORKFLOW_RELIABILITY_BASELINE_V6_AMENDMENT_2026-09-21.md`
- Base architecture：Product Delivery Discipline v6 + post-probe addendum + v0.4 bounded amendment
- Goal：`docs/goals/056_PRODUCT_DELIVERY_DISCIPLINE_GOAL.md` v0.5
- Kickoff：`docs/operations/prompts/056_PRODUCT_DELIVERY_DISCIPLINE_KICKOFF.md` v0.5

本 Plan 替代 v0.4 execution package。v0.5 不重新设计 v6、不改变 Gate taxonomy、不改变 least-privilege absorption、不改变 defer disposition、不改变版本路线。它只把两个 reviewed branches 对应的 task-owned worktree locator 从“建议/对应 worktree”收紧为当前用户可见、唯一、可复核的 exact locator。

只有独立 Critic 对同一 v0.5 Plan + Goal + Kickoff 给 `READY_FOR_CODEX=YES`，且用户随后实际发送 approved Kickoff，才授权 Executor 开始。

## 1. 当前 source reality

### AI_Skills

当前 release identity：

~~~text
Repository / CLI  5.0.6
workflow-core      0.2
web-development    0.1
ai-skills-core     0.3
~~~

5.0.6 已完成 semantic task identity、human label separation、Gate lifecycle、regression bank、narrow/broad-full release selection、same-final-candidate 等 production behavior，并通过 candidate plugin replay 与 production smoke。056 必须保留这些能力，不得重新实现或降级。

仍未完成的 v6 production behavior：

- workflow-core W1-W5 delivery / Human Gate / evidence / repeat-failure / should-not-change；
- W2 的 least-privilege equivalent recovery；
- Frontend Design F-A/F-B/F-C production wiring，包括已有 Figma-handoff / motion capability 的正常消费；
- AI Skills Maintainer 中尚未被 0.3 完整覆盖的 production-consumption diagnosis；
- 原 v6 Source Discovery regression 的 residual enforcement。

### Bridge

当前 source version `0.8.4`，已拥有：

- Persistent Run 0.8.0；
- upfront authorization / persistent authoring 0.8.1；
- fresh-root / raw-byte / Lite versioning 0.8.3；
- semantic task-key compatibility 0.8.4。

仍未完成的 056 work：

- Default required HUMAN_ONLY 不依赖 auto-resolving native card；
- managed Host desired state 从 `default_mode_request_user_input=true` 改为 v6 approved fail-closed candidate `false`，并验证 current supported-key handling；
- Host/Lite docs/tests 与 durable transcript wait/resume 对齐；
- preserve Plan-mode 合法行为。

Persistent Run 本身不在本轮写 scope。

## 2. Frozen architecture

保持：

~~~text
Lite: L1-L6
workflow-core: W1-W5
Frontend Design: F-A / F-B / F-C
AI Skills Maintainer: production-consumption diagnosis
Bridge: transport / wait-resume / recovery + Lite distribution
Capability Gates: G1-G8
Source Discovery regression: existing capability, not G9
~~~

禁止 W6/W7/G9/G10、新 state/schema/ledger/controller/watcher、第二套 authorization engine、Codex fork。

## 3. W2 bounded amendment：least-privilege equivalent recovery

在任何因 credential scope、provider permission、paid resource、environment mutation 准备请求用户扩大权限之前，W2 增加一层 bounded eligibility check。

### 3.1 先判断“Goal 需要”还是“路线需要”

必须区分：

- frozen Goal 的唯一合法路线确实缺 credential / permission；
- credential missing / expired / revoked；
- credential 本身有效，但只对 Executor 当前选择的某条实现路线权限不足；
- preferred / optional route 不可用；
- frozen Goal 下已经存在 authorized equivalent route。

这些是诊断语义，不新增 machine enum/state。

### 3.2 equivalent route 条件

只有同时满足以下条件才可自动切换：

- 已在当前 frozen authorization envelope 内；
- 不引入新的 provider/account/recipient/purpose/data boundary；
- security/privacy 不降低；
- product behavior / normal entry 不降低；
- evidence surface / acceptance quality 不降低；
- 不把 manual/degraded/fallback 冒充 primary result；
- 不改变 frozen product/scientific semantics。

存在多个等价路线时，优先不新增 credential scope / provider mutation / human maintenance burden 的路线。

### 3.3 bounded search

Executor 只对当前已知、已有 source 指示或当前环境可直接验证的候选路线做 equivalence check；不要求为了避免 Human Gate 无限搜索互联网、安装新服务或迁移 provider。

没有等价已授权路线，或切换会改变 provider/data/security/product semantics 时，正常进入 Human Gate / Planner。

## 4. 本轮明确不吸收

### 4.1 Persistent Run durability

不修改 Bridge Persistent Run production source、template、CLI 或 TODO。本轮只保护其已有 contract 不回归。

Bridge 后续单独研究：

- tmux discovery/preflight；
- true SSH disconnect/reconnect；
- hours/overnight；
- stale session；
- checkpoint/resume；
- duplicate launch；
- progress/ETA。

### 4.2 ordinary bounded kickoff renderer

不在 056 新增 generic authorization renderer。当前 v1.4 Planner/Critic execution package 已负责自带 Kickoff；Bridge 0.8.1 已负责 runtime consumption。普通非 Planner/Critic 复杂任务的 copy-ready kickoff 留作 workflow-core 后续 refinement。

### 4.3 task-local restriction lifetime

instruction lifetime/scope precedence 留作 workflow-core 后续 refinement。

### 4.4 acceptance comparison packaging

generic W1/W3/W4/W5 继续保护 acceptance truth；research-document semantic alignment 与 slide/page/render quality 不进入 056。

## 5. Exact branch / worktree authorization after approved Kickoff

本节是 v0.5 唯一实质 execution-package 修订。下列 locator 都是冻结值，不是建议，不允许 Executor 临场改名或选择另一路径。

### AI_Skills_Collection — WRITE

Exact branch：

`reviewed/056_product_delivery_discipline`

Exact task-owned worktree locator：

`../AI_Skills_Collection-056-product-delivery-discipline`

解析规则：

- 该相对路径必须以**已验证的 canonical AI_Skills_Collection checkout root** 为基准，而不是以任意当前 shell 子目录为基准；
- canonical root 由当前 repo 的 `git rev-parse --show-toplevel` 确认；
- 即目标是该 canonical root 的父目录下、basename 精确为 `AI_Skills_Collection-056-product-delivery-discipline` 的唯一 sibling worktree；
- 不允许改成其他 basename、`/tmp` clone、第二个 worktree 或临时自选路径；
- 如果该 exact locator 已存在，只有在它确实属于同一 canonical repo 且绑定 exact branch 时才可复用；
- 如果该 locator 被无关目录/worktree占用、repo identity 不匹配或 branch identity 不匹配，停止并报告；不得自动选择替代路径。

允许：

- workflow-core W1-W5 + W2 least-privilege amendment + existing Source Discovery residual enforcement；
- web-development F-A/F-B/F-C 与已有 Figma/motion capability 正常 production wiring；
- ai-skills-core residual production-consumption diagnosis；
- tests / regression fixtures / generated Marketplace payload / version-changelog-release metadata；
- `results/056_product_delivery_discipline/` 或当前 repo contract 等价的 task-owned evidence。

不得重做 5.0.6 已完成的 semantic task-key parser、Gate lifecycle architecture 或 task identity design。

### GPT_Codex_AI_Bridge_Kit — WRITE

Exact branch：

`reviewed/056_product_delivery_discipline`

Exact task-owned worktree locator：

`../GPT_Codex_AI_Bridge_Kit-056-product-delivery-discipline`

解析规则：

- 该相对路径必须以**已验证的 canonical GPT_Codex_AI_Bridge_Kit checkout root** 为基准；
- canonical root 由当前 repo 的 `git rev-parse --show-toplevel` 确认；
- 即目标是该 canonical root 的父目录下、basename 精确为 `GPT_Codex_AI_Bridge_Kit-056-product-delivery-discipline` 的唯一 sibling worktree；
- 不允许改成其他 basename、`/tmp` clone、第二个 worktree 或临时自选路径；
- 如果该 exact locator 已存在，只有在它确实属于同一 canonical repo 且绑定 exact branch 时才可复用；
- 如果 locator 被无关目录/worktree占用、repo identity 不匹配或 branch identity 不匹配，停止并报告；不得自动选择替代路径。

允许：

- Host desired `default_mode_request_user_input=false` candidate；
- supported-key / desired-state validation；
- HUMAN_ONLY durable transcript wait/resume guidance；
- Lite/Host docs/tests consistency；
- 0.8.5 candidate metadata。

必须保护 0.8.4 semantic task-key behavior 与 0.8.0/0.8.1 Persistent Run/upfront authorization。

### Product repos — ZERO WRITE

Bobbio、Lucerna、Mica、Asteria、SeminarArc、CUHK Date、CARE/EAT、Server/VPS、Longleaf_Bridge、Scientific Visualization production 均为 zero-write；只可作为已冻结 Gate 的只读 evidence source。

## 6. Version disposition

当前 planning 不改 version source。候选形成且 replay/regression/release closure 达标时：

~~~text
Repository bump decision: PATCH
AI_Skills_Collection 5.0.6 -> 5.0.7

Affected plugins:
workflow-core    0.2 -> 0.3
web-development  0.1 -> 0.2
ai-skills-core   0.3 -> 0.4

Bridge:
0.8.4 -> 0.8.5 compatible patch
~~~

Executor 必须在真正修改前重读 canonical version sources。若某项 production behavior 已被后续 compatible main 完整实现，必须用 direct normal-entry evidence 证明后再改为 `NO_BUMP`；不得只因 version slot 预写在 Plan 就机械推进。

## 7. Capability Gate Matrix

本轮属于 shared workflow/default-prompt/Marketplace/cross-plugin behavior change，release selection 为 `BROAD_FULL_FALLBACK`。不允许事后降成 narrow。

| Gate | 证明的能力 | v0.5 主要 evidence | 失败条件 |
|---|---|---|---|
| G1 | genuine Human Gate + durable wait/resume + least-priv eligibility | reply/no-reply；AGENT_RESOLVABLE 不 prompt；optional high-priv route 有 equivalent lower-priv route 时自动继续；degraded route 不偷换；Plan mode不回归 | agent 可解决/等价路线存在仍找用户；required answer 前继续；重复消费回答 |
| G2 | acceptance admission | incomplete/human-blocked candidate 不能 user-ready；advisory review仍可 | self-report/broad tests 绕过 closure |
| G3 | same-Goal recovery / post-action closure | explicit reply 后 exact-once resume 并继续 agent closure | human action 本身被当 completion；新 task/重复 prompt |
| G4 | faithful failure replay | old-bad/new-good、interaction/provider等真实 surface | broad suite 代替原 failure |
| G5 | evidence scope / final candidate | same final candidate，claim不超过 evidence | 旧候选/低层 proxy 拼 PASS |
| G6 | Frontend canonical design consumption | normal production entry 真正消费 canonical design / state | 只存在 locator 或 code自行发明 material design |
| G7 | non-overreach | docs/server/tiny nonvisual route不被拉进全套 UI/provider gates | 小任务被自动重流程 |
| G8 | production-consumption diagnosis | stale install/wrong generated/session/entry/trigger 类 regression 能定位 consumer path | active rule失败后只再加同义 policy |

Existing Source Discovery regression 继续单独验证 local canonical source + unrelated dirty state 时不冗余 clone/remap remote。

Gate lifecycle 要求：

- 新 least-priv case 进入 G1 regression bank，不新建 Gate；
- cheap deterministic regression first；
- shared surface 变化使用 broad/full fallback；
- release-critical evidence 绑定同一 final candidate；
- 不用 schema/字符串/TODO 存在冒充 normal-entry PASS。

## 8. Human Gate transport

当前 OpenAI Codex source 继续支持原 post-probe 判断：Default mode required input 应使用 concise plain-text question；`request_user_input` 不用于 permission escalation。

v0.5 继续：

~~~text
HUMAN_ONLY
-> preserve current Goal/resume point/prompt identity
-> one concise plain-text question
-> stop dependent execution
~~~

no reply 到 task 已有合法 deadline/run handoff boundary：

~~~text
GOAL_BLOCKED=YES
GOAL_ACHIEVED=NO
COMPLETE=NO
READY_FOR_USER_REVIEW=NO
DEPENDENT_EXECUTION_BLOCKED=YES
~~~

使用现有合法 recovery representation，不发明 BLOCKED enum。后续 explicit valid reply 重读当前 Goal/resume identity，exact-once resume。

External GPT normal waiting不受此规则影响。

## 9. Current Host boundary

本 v0.5 execution package 仍不授权：

- 修改真实用户 `CODEX_HOME`；
- real Host Policy install/update；
- final real-user W2/G1 fresh-session smoke。

source/unit/isolated fixture 可以测试 Host 逻辑。最终真实 Host integration 若仍是 release-critical requirement，必须在 implementation review 后单独获用户授权，不能用 isolated evidence 冒充。

## 10. Validation order

1. source/identity/version preflight；
2. exact branch/worktree identity preflight；
3. focused cheap deterministic regression；
4. original W1-W5 / least-priv / Frontend / Maintainer / Bridge focused tests；
5. source-generated Marketplace parity；
6. broad/full repository regression；
7. candidate plugin replay / normal-entry evidence；
8. freeze exact candidate tuple；
9. independent implementation review；
10. 后续如需 real Host integration，再单独授权。

不要先跑 paid/fresh/真人检查。本轮不调用 paid API/Terra。

## 11. Should-not-change

必须保护：

- AI_Skills 5.0.6 task identity / Gate lifecycle / broad-full / same-final-candidate；
- Bridge 0.8.4 semantic task-key compatibility；
- Bridge Persistent Run 0.8.0/0.8.1 contract；
- External GPT waiting；
- Plan-mode合法 request-user-input；
- domain plugin专业 ownership；
- product repos zero-write；
- small-task non-overreach；
- no new authorization DB/state/schema/ledger/controller/watcher；
- v0.4 已被 Critic 接受的 architecture / Gate / least-priv / defer / version decisions。

## 12. Source drift rule

SHA 是 locator，不是产品质量。

Kickoff 时如果 main 只增加无关 docs/evidence commit，刷新 locator后继续，不因此制造 Critic loop。只有 production/version/release/frozen semantics 有实质 overlap 才停回 Planner/Critic。

## 13. Execution-stage end state

approved Kickoff 下的 Executor 结束条件：

- 两个 exact task branches / exact task-owned worktrees identity 正确；
- 两个 task branch 的 frozen source changes 完成；
- authorized non-host G1-G8 / source-discovery evidence完成；
- source/generated/version/changelog candidate parity完成；
- task branches ordinary non-force push；
- implementation tuple冻结；
- product repos untouched；
- real Host integration等未授权边界如实 pending；
- handoff给独立 implementation review。

不得宣布 056 overall achieved。

`NEXT_HANDOFF = CRITIC`（当前 planning stage）。
