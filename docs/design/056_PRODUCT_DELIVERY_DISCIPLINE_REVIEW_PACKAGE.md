# 056 Product Delivery Discipline — Review Package

状态：`AWAITING_EXECUTION_PACKAGE_CRITIC_R2`

## Task identity

- Task key: `056_product_delivery_discipline`
- Review stage: v6 architecture + post-probe direction passed; execution package v0.1 received Critic `REVISE`; Planner v0.2 response awaits independent Critic re-review
- Architecture authority: `docs/design/PRODUCT_DELIVERY_DISCIPLINE_V6_PROPOSAL_2026-09-16.md`
- Post-probe authority: `docs/design/PRODUCT_DELIVERY_DISCIPLINE_V6_POST_PROBE_ADDENDUM_2026-09-17.md`
- Probe result: `docs/design/056_PERSISTENT_PROMPT_CAPABILITY_PROBE_RESULT_2026-09-17.md`
- CUHK Date evidence: `docs/design/PRODUCT_DELIVERY_DISCIPLINE_V6_CUHK_DATE_REAL_FEEDBACK_2026-09-17.md`
- Implementation Plan: `docs/design/056_PRODUCT_DELIVERY_DISCIPLINE_IMPLEMENTATION_PLAN.md` v0.2
- Canonical Goal: `docs/goals/056_PRODUCT_DELIVERY_DISCIPLINE_GOAL.md` v0.2
- Kickoff Draft: `docs/operations/prompts/056_PRODUCT_DELIVERY_DISCIPLINE_KICKOFF.md` v0.2
- Critic reporting contract: `docs/workflows/CRITIC_ROLE_CONTRACT.md` v1.3
- Primary maintenance inbox: `docs/plugin-todos/workflow-core.md`

本 package 仍只是 review object。没有创建 execution branch/worktree，没有修改 production plugin/skill、真实 Bridge Kit production/Host Policy 或产品 repo AGENTS，也没有启动 Executor。只有独立 Critic 对同版 Plan + Goal + Kickoff 给出 `READY_FOR_CODEX=YES`，且用户之后实际发送获批 Kickoff，才允许执行。

## Review history

### Round 1 — v5 architecture

Decision: `REVISE`

Stable blockers：`C056-B1`～`C056-B4`。

### Round 2 — v6 architecture / probe draft

`docs/design/PRODUCT_DELIVERY_DISCIPLINE_V6_PROPOSAL_2026-09-16.md`

Independent Critic gave architecture `PASS`; persistent input transport remained probe-dependent。

### Capability probe

Default-mode native `request_user_input` auto-resolved empty after 114 seconds; durable transcript fallback resumed once. Canonical result：

`docs/design/056_PERSISTENT_PROMPT_CAPABILITY_PROBE_RESULT_2026-09-17.md`

### Post-probe short review

User-relayed Critic decision：

```text
RESULT = PASS
V6_ARCHITECTURE_STILL_VALID = YES
W2_TRANSPORT = DURABLE_TRANSCRIPT_WAIT_RESUME
DEFAULT_MODE_REQUEST_USER_INPUT_FLAG = DISABLE
SOURCE_DISCOVERY_REFINEMENT = PASS
CUHK_DATE_REFINEMENTS = PASS
READY_FOR_IMPLEMENTATION_PLAN_DRAFT = YES
```

### Execution-ready review R1 — package v0.1

Reviewed commit：

`01766a47325a5e7efb84dc2b75b90d67a010c157`

Decision：

```text
RESULT = REVISE
READY_FOR_CODEX = NO
```

Stable blockers：

- `C056-E1-HUMAN-GATE-BLOCKED-NOT-ACHIEVED`
- `C056-E2-POST-REVISE-PASS-HUMAN-EXPLANATION`

## Planner v0.2 response

Planner 不自行宣布 blocker closed；以下只是待 Critic 独立复核的 disposition。

| Finding | Planner disposition | v0.2 response | Status before Critic R2 |
|---|---|---|---|
| `C056-E1-HUMAN-GATE-BLOCKED-NOT-ACHIEVED` | `ACCEPT` | 保持 transcript transport/native flag=false，但删除“永远非 terminal block”的无期限语义；定义 human deadline/run-end authority；无答复到边界必须 `GOAL_BLOCKED=YES / GOAL_ACHIEVED=NO / COMPLETE=NO / READY_FOR_USER_REVIEW=NO`，machine state复用已有 human-required/recovery enum；later explicit reply same Goal exact-once recovery；G1拆成 reply/no-reply 两个 behavior replay | `RESPONDED_PENDING_CRITIC` |
| `C056-E2-POST-REVISE-PASS-HUMAN-EXPLANATION` | `ACCEPT` | `CRITIC_ROLE_CONTRACT.md` 升至 v1.3，新增通用 post-REVISE PASS closure explanation；要求在 machine fields/approved kickoff前用自然中文解释 blockers、affected/unaffected layers、Gates、repo-specific disposition、normal workflow变化和PASS边界；不硬编码056 | `RESPONDED_PENDING_CRITIC` |

## E1 exact semantic change

Default `HUMAN_ONLY` remains：

```text
preserve Goal / resume point / prompt identity
-> one concise plain-text question
-> stop dependent execution
```

等待边界 authority：

1. frozen task/workflow已有 explicit human-response deadline/hard deadline/run-lifetime -> 使用它；
2. 没有显式 timeout，而 plain-text question后 current Codex run/turn结束 -> run-end 是当前 handoff边界；
3. native question card的60+60秒不是 transcript deadline；
4. External GPT normal waiting 不受本规则改变。

边界到达无答复：

```text
GOAL_BLOCKED=YES
GOAL_ACHIEVED=NO
COMPLETE=NO
READY_FOR_USER_REVIEW=NO
DEPENDENT_EXECUTION_BLOCKED=YES
```

若 machine schema 没有 literal `BLOCKED`，使用已有 `NEEDS_HUMAN_APPROVAL` / human-required / legal recovery等价；不创建新 enum/state machine。这是 recoverable blocked-for-human handoff，不等于 `STOP`/impossibility。

later reply：same Goal、same prompt identity、no successor、no repeated prompt、exact-once resume、post-action closure。

G1 now requires：

- `G1-A reply path`；
- `G1-B no-reply/run-end -> blocked/achieved=no -> later recovery` behavior replay。

G1-B 可用 faithful bounded fixture，不要求用户真人傻等，但不能用字符串扫描替代实际 handoff/recovery behavior。

## E2 generic reporting contract

`docs/workflows/CRITIC_ROLE_CONTRACT.md` v1.3 新增 §6.3：同一 Active Review Context / major round 曾正式 `REVISE`，最终 `PASS` 必须先给用户可读 closure explanation，再输出 machine fields/approved next-role prompt。

它是通用报告规则，不是新 Gate/state。普通没有 prior REVISE 的小 review 不机械增加 ceremony。

README 当前“Planner / Critic双线程”模板已经强制 Critic线程先读 canonical Critic contract；因此本轮**不复制完整新规则进 README**，避免第二 source。若 Critic认为一行摘要仍是必要 discoverability fix，可在本 R2 作为最小 finding提出。

## Repo-specific AGENTS audit / frozen disposition

本轮重新读取真实 repo source，目的既不是加规则数量，也不是为了“瘦身”删掉项目安全事实。

| Repo | Direct finding | Frozen disposition | 056 product-repo write? |
|---|---|---|---|
| Bobbio `develop@0811116...` | frontend/Product Design read-list遗漏 `docs/design/FIGMA_HANDOFF.md`；该文件明确是 canonical visual source；pre-user native self-QA/GPT Work pipeline已存在 | `ADD_MINIMAL_LOCATOR` | **YES，仅 locator** |
| Lucerna `main@461dcea...` | current AGENTS已经把Windows release、matching regression、real provider/no mock、tray lifecycle、screenshot helper、Longleaf boundaries写得具体 | `ALREADY_COVERED` | **NO** |
| Mica `main@aa4ce52...` | current AGENTS已有real failure、内建diagnostics、focused-before-full-E2E、short manual loop、typing hot path、authenticated ChatGPT边界 | `ALREADY_COVERED` | **NO** |
| Asteria `main@166791c...` | AGENTS/AGENT_RULES已有visual self-QA、scientific graph system、generic fix、GPT Work-before-human、focused regression | `ALREADY_COVERED` | **NO** |
| SeminarArc `main@71c59d3...` | AGENTS主要是Android/Windows/Emulator/真机安全；没有direct project-level canonical Figma locator evidence | `NO_CHANGE / EVIDENCE_NEEDED` | **NO** |
| CUHK Date `main@57dd543...` | GitHub current main没有tracked root AGENTS；prototype subtree有prototype-specific rules；V4失败已由central W1/W3/W5/Frontend吸收 | `NO_GENERIC_056_AGENTS_COPY` | **NO** |

AGENTS hygiene：

- 项目独有 invariant/locator/机器/数据/安全 truth 留项目；
- 中央 workflow/frontend delivery discipline 不复制到每个 repo；
- 中央能力尚未通过 production replay前，不为了短而删除现有项目保护；
- 未来若中央 normal entry已稳定消费且项目中存在纯同义重复，可另做最小去重，不在056顺手改；
- Executor不拥有“再给Lucerna/Mica/Asteria补一条056”的决定权。

## Architecture kept closed

v0.2不重开：

```text
Lite 6
workflow 5
Frontend 3
Maintainer 1
no W6/W7
no G9/G10
Source Discovery regression != new Gate
Default native request_user_input disabled candidate
Figma + motion -> Frontend production payload
```

版本方向保持：

```text
AI_Skills 5.0.4 -> 5.0.5 PATCH
workflow-core 0.1 -> 0.2
web-development 0.1 -> 0.2
ai-skills-core 0.2 -> 0.3
Bridge 0.8.2 -> 0.8.3
Bobbio runtime unchanged
```

但只有 original-failure replay / unrelated regression / final release closure全部通过才真正 bump/release。

## Current Critic R2 question

下一轮只需重点复核：

1. `C056-E1` 是否被 v0.2 正确关闭：blocked vs achieved、deadline/run-end authority、existing state mapping、reply/no-reply recovery、External GPT waiting不被污染；
2. `C056-E2` generic Critic reporting contract是否足够且不过重；
3. repo-specific AGENTS disposition是否保持最小且没有把必要项目规则误删/中央规则重复复制；
4. v0.2 是否因为返修新增了第二状态机、额外 Gate、额外 product scope或其他不必要复杂度。

除非本次修改引入直接新风险，不重开已经关闭的 v6 architecture、post-probe transport选择、Frontend wiring、Source Discovery owner或版本方向。

## Expected next step

若且仅若独立 Critic 对 exact v0.2 package 返回：

```text
RESULT = PASS
READY_FOR_CODEX = YES
```

则按 `CRITIC_ROLE_CONTRACT.md` v1.3 先给 plain-language closure explanation，再逐字返回已审 Kickoff。执行仍只在用户实际发送 approved Kickoff 后开始。

当前：

`NEXT_HANDOFF = CRITIC`
