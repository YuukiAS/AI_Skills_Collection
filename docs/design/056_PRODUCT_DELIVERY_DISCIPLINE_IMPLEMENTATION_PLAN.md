# 056 Product Delivery Discipline — Implementation Plan

- Execution package version: `v0.2`
- Task key: `056_product_delivery_discipline`
- Status: `READY_FOR_EXECUTION_CRITIC_REVIEW`
- Revision base: `AI_Skills_Collection main@01766a47325a5e7efb84dc2b75b90d67a010c157`
- Prior execution package: `v0.1`, reviewed commit `01766a47325a5e7efb84dc2b75b90d67a010c157`, Critic decision `REVISE`
- Bridge Kit source ref at revision: `GPT_Codex_AI_Bridge_Kit main@cb77b1cc5a1fce097a38066d2db452291e359852`
- Bobbio source ref at revision: `develop@0811116ac7197590f0af773f3c6296d4ca41db80`
- Lucerna source ref checked: `main@461dcea4015434f90d50922d9b7ae054286c98bc`
- Mica source ref checked: `main@aa4ce52581fff2e207d1f93600becbb3018b0efc`
- Asteria source ref checked: `main@166791c27752c70255043f026dcbda4deb693c04`
- SeminarArc source ref checked: `main@71c59d39f4d7e9cd3a3d813ad55d5cf6a38a4b11`
- CUHK Date source ref checked: `main@57dd5432c744ef16ec614e1e10b1b3f21564c7ba`
- Architecture authority: `docs/design/PRODUCT_DELIVERY_DISCIPLINE_V6_PROPOSAL_2026-09-16.md`
- Post-probe authority: `docs/design/PRODUCT_DELIVERY_DISCIPLINE_V6_POST_PROBE_ADDENDUM_2026-09-17.md`
- Probe result: `docs/design/056_PERSISTENT_PROMPT_CAPABILITY_PROBE_RESULT_2026-09-17.md`
- CUHK Date evidence: `docs/design/PRODUCT_DELIVERY_DISCIPLINE_V6_CUHK_DATE_REAL_FEEDBACK_2026-09-17.md`
- Canonical Goal: `docs/goals/056_PRODUCT_DELIVERY_DISCIPLINE_GOAL.md` v0.2
- Kickoff Draft: `docs/operations/prompts/056_PRODUCT_DELIVERY_DISCIPLINE_KICKOFF.md` v0.2

本文件只返修 execution contract，不重开已经通过的 v6 架构。只有独立 Critic 对本 v0.2 Plan + Goal + Kickoff 同版给出 `READY_FOR_CODEX=YES`，且用户随后实际发送获批 Kickoff，才允许创建 task branch/worktree、修改 production source、修改真实 Host Policy 或启动 Executor。

## 0. 对 execution-ready Critic blockers 的处理

### C056-E1-HUMAN-GATE-BLOCKED-NOT-ACHIEVED — `ACCEPT`

v0.1 把 `DEPENDENT_EXECUTION_BLOCKED=YES / TERMINAL_BLOCKED=NO` 写成了无期限语义，不能满足用户当前直接要求：HUMAN_ONLY 问题在合法等待窗口结束或当前 execution run 必须结束而仍无明确回复时，Goal 必须诚实进入 blocked-for-human 状态，且绝不能标 achieved/complete/PASS/user-ready。

修订依据：

1. 当前 Codex Default mode 仍明确要求：真正必须用户输入才能安全继续时，使用一条 concise plain-text question，而不是 Default native `request_user_input`；后者仍由 `mode == Plan` 决定 blocking。
2. 056 probe 已证明当前 Default native card 会 auto-resolve；因此 transport 仍保持 `DURABLE_TRANSCRIPT_WAIT_RESUME`，不退回 native card。
3. Bridge Kit 当前 `HANDOFF_STATE_MACHINE.md` 没有字面 `BLOCKED` enum，但已有 `NEEDS_HUMAN_APPROVAL` 等合法 human-required state。故 v0.2 不新增 enum/state machine，而把 **Goal completion semantics** 与 **machine state vocabulary** 分开：machine 使用现有合法 human-required/recovery state，user-facing result 必须明确 `GOAL_BLOCKED=YES`、`GOAL_ACHIEVED=NO`。
4. External GPT Planner/Reviewer waiting 是另一类 owner-wait，不属于 HUMAN_ONLY gate；现有 external wait semantics 保持不变。

v0.2 将这一语义同步到 Lite L3/L6、Bridge Host user-input contract、workflow W1/W2、G1/G3、recovery 和 Kickoff。

### C056-E2-POST-REVISE-PASS-HUMAN-EXPLANATION — `ACCEPT`

当前 Critic contract 已要求先用自然中文给判断，再给 machine fields；但 execution-ready PASS 小节会直接进入 approved paths/fields/verbatim Kickoff，没有明确要求“同一 major round 曾 REVISE 后，最终 PASS 必须解释到底改了什么”。这正是用户指出的可读性缺口。

本轮将 `docs/workflows/CRITIC_ROLE_CONTRACT.md` 升为新的文档版本并加入通用规则：同一 Active Review Context / major round 曾有正式 `REVISE`，后续 `PASS` 必须在 machine-readable fields / approved next-role prompt 之前给 plain-language closure explanation。该说明按适用项解释 blockers 如何关闭、哪些层改/没改、Gate 证明什么、repo-specific rule/locator disposition、normal workflow 的实际变化，以及 PASS 证明与不证明什么。此规则不是 056 专用，也不新增 review gate/state。README 的 Planner/Critic 模板只做一行级摘要同步，避免模板继续诱导“只有 fields + kickoff”。

## 1. 本轮通过后新增的真实能力

通过 056 后，用户获得的是可观察的开发行为，而不是更多 Markdown：

1. 复杂/高风险任务不会把 agent 自己能解决的 repo/source/environment 问题转嫁给用户；只有真正 `HUMAN_ONLY` 才询问。
2. Default-mode HUMAN_ONLY 使用 durable transcript question。问题发出后 dependent work 立即停止；若合法等待结束/当前 run 结束仍无回复，Goal 明确 blocked、achieved=no；用户以后明确回复时从同一个 Goal/resume point 恢复，不开 successor、不重复问。
3. acceptance/release/user-ready handoff 在 frozen feature/milestone 尚未真正闭环时会被拒绝；advisory/diagnostic/design/architecture review 仍可轻量发生。
4. `workflow-core` 区分 proxy/synthetic/helper 与真实 target surface，要求 faithful failure/regression、final-candidate identity、repeat-failure stop rule 和 should-not-change protection。
5. `Frontend Design` 形成 F-A/F-B/F-C 三个 production gate；有 canonical Figma/design 时必须消费设计源，缺 material state 先回设计源而不是代码临场发明。
6. `AI Skills Maintainer` 遇到“规则已经写了但还是犯错”时先诊断 installed/source/generated/invocation/trigger/session/normal-entry consumption，而不是堆同义 policy。
7. Bridge Kit Default host config fail-closed：`default_mode_request_user_input=false`；Plan-mode native blocking question 不因该 Default-only flag 被禁用。
8. Lite Handoff 只保留六条最低交付底线，不把 Figma/icon/provider/locale/full-E2E checklist 塞进每个 repo。

## 2. 绝对边界与已关闭架构

本任务保持已通过的最小架构：

```text
Lite baseline             6
workflow-core             5 capability
Frontend Design           3 production gate
AI Skills Maintainer      1 consumption-diagnosis capability
Bridge Kit                transport / wait / recovery + Lite distribution
repo AGENTS               project-specific invariant / locator only
```

不得新增 W6/W7、G9/G10、Control、watcher、ledger、daemon、第二状态机、第二 review engine、新顶级 plugin 或 Codex fork。不得调用 paid API/Terra。

`scientific-visualization` 本轮不做 production change。Lucerna、Mica、Asteria、SeminarArc、CUHK Date、CARE/EAT、Server/VPS、Longleaf_Bridge 不做 product/AGENTS production change。Bobbio 只允许一个 canonical design locator 修正。

普通 docs-only、backend-only、server-only、tiny nonvisual fix 不得因为 056 自动升级成 Figma/GPT Work/full E2E/native-smoke ceremony。

## 3. Repo-specific AGENTS 审核与冻结 disposition

本轮重新直接读取了问题最多的项目规则。目标不是“每个 repo 再加一段 056”，而是确认中央规则与项目规则的边界，避免越改越臃肿。

| Repo | 当前项目规则直接证据 | 056 disposition | 需要新增 repo AGENTS? | 保留的项目特有内容 |
|---|---|---|---|---|
| Bobbio `develop` | `AGENTS.md` frontend/Product Design read-list 有 `PRODUCT_DESIGN_BRIEF` 和概念图，但遗漏 `docs/design/FIGMA_HANDOFF.md`；`DEVELOPMENT_WORKFLOW.md` 已有 tests -> native self-QA -> GPT Work -> user；Figma handoff 明确是 canonical visual source | `ADD_MINIMAL_LOCATOR` | **YES，仅 locator** | Zotero authority/isolation、安全 GUI、native acceptance、milestone 产品不变量 |
| Lucerna `main` | `AGENTS.md` 已要求真实 Windows release、matching regression、real provider/no second refresh、normal live UI 禁止 mock/fixture release evidence、canonical screenshot helper、Longleaf integration | `ALREADY_COVERED` | **NO** | Windows/tray lifecycle、live provider truth、screenshot helper、Longleaf 权限/入口 |
| Mica `main` | 已要求 real failure reproduction、内建 privacy-safe diagnostics、focused-before-full-E2E、same focused failure 两次后先查 source/fixture/validator、one-short-manual-loop、保护 authenticated Edge/ChatGPT、typing hot path | `ALREADY_COVERED` | **NO** | ChatGPT DOM/账号边界、诊断报告、typing 性能、Tier 测试与真实站点手工验收 |
| Asteria `main` | root/`prompts/AGENT_RULES.md` 已有 developer visual self-QA、canonical scientific graph system、generic-fix、GPT Work-before-human、fix-specific regression | `ALREADY_COVERED` | **NO** | scientific graph grammar、fixed public URL、black-box browser contract、release campaign |
| SeminarArc `main` | AGENTS 主要是 Android/Windows/WSL/Emulator/真机安全与真实媒体测试；未找到 project-level canonical Figma locator 的直接证据 | `NO_CHANGE / EVIDENCE_NEEDED` | **NO** | device safety、environment paths、emulator-first、真实素材 privacy |
| CUHK Date `main` | 当前 GitHub 没有 tracked root `AGENTS.md`；有 `docs/design/prototype/AGENTS.md`，但 Questionnaire V4 failures 已能由 W1/W3/W5/Frontend 表达 | `NO_GENERIC_056_AGENTS_COPY` | **NO** | 若以后发现长期项目特有 locator/invariant，需给 direct source evidence 再交 Critic；Executor 不得临场扩 scope |

### AGENTS hygiene 原则

1. repo AGENTS 只保留 project-specific invariant、canonical source locator、机器/数据/安全边界、项目 normal-entry 事实；中央 delivery discipline 不复制进去。
2. 已有项目规则与中央新能力语义重叠时，本任务默认**不删**项目保护。先让中央 production consumer 真正通过 G1–G8；未来若要瘦身，只删已经证明完全由中央 normal entry 稳定消费、且删除不会丢失项目语义的重复句子。
3. 不把“AGENTS 很长”本身当缺陷。SeminarArc 的设备安全、Bobbio 的 Zotero authority、Asteria 的 fixed URL/black-box、Lucerna 的 Windows/live-provider、Mica 的 ChatGPT DOM/typing 都是项目事实，不能为了简短塞进通用 plugin 或删除。
4. 反过来，也不因项目已有一部分通用语义，就继续加入 056 同义段落。真实复发先由 AI Skills Maintainer 查 consumer/session/install/enforcement。
5. 本 056 对产品 repo 唯一 planned write 是 Bobbio locator；其余 disposition 已冻结，Executor 无权重新判断“顺手加一条 AGENTS”。

## 4. 执行时的 bounded Git/source strategy

本节只有 execution-ready Critic PASS 且用户实际发送获批 Kickoff 后才生效。

### AI_Skills_Collection

- exact branch: `reviewed/056_product_delivery_discipline`
- base: kickoff 当时最新、仍包含获批 package 且无相关语义漂移的 `origin/main`
- preferred worktree: 从本机已验证 canonical checkout 建 task-owned clean worktree，目录名 `AI_Skills_Collection-056-product-delivery-discipline`，放 canonical repo 同级；不得先 network clone。

### GPT_Codex_AI_Bridge_Kit

- exact branch: `reviewed/056_product_delivery_discipline`
- base: kickoff 当时最新 `origin/main`
- preferred worktree: 从本机已验证 canonical checkout 建同级 `GPT_Codex_AI_Bridge_Kit-056-product-delivery-discipline`
- unrelated dirty state 留在原 checkout，不 stash/reset/restore；dirty 不等于放弃 local source。

### Bobbio

- exact integration branch: current `develop`
- 不新建 Bobbio task branch/worktree；只做 locator-level docs change。
- `AGENTS.md` 有用户未提交修改或 `develop` 无法安全同步时，暂停 Bobbio 子步骤回 Planner，不 clone/remap remote 绕过。

### Existing Source Discovery refinement

任务指向已知 repo时：先找已有 canonical checkout/worktree/clone -> 核 repo identity/branch/ref/origin/freshness/dirty ownership -> unrelated dirty 保护但不自动弃用 repo -> 当前 checkout可安全完成就使用；需要 isolation 时优先已有正确 clean clone/worktree，或在已授权 branch/worktree strategy 下从 canonical local source建 worktree -> 本机确无可用 source才 network clone。`local clone -> git remote set-url` 不是正常隔离路径；remote mutation 始终是独立授权边界。

这只是 existing Source Discovery enforcement，不新增 W6/G9。

## 5. Phase 0 — Preflight 与 baseline

Executor 记录：三 repo exact source refs、当前安装 plugin identity/version、Bridge version、`$CODEX_HOME` identity/Host Policy state、Bridge config backup eligibility、Bobbio locator state，并冻结 public-safe G1–G8 + Source Discovery baseline fixtures。

基线只用于 before/after 归因。旧版本 PASS 不得拼接给 final candidate。

## 6. Phase 1 — Bridge Kit：Lite + HUMAN_ONLY transport

### 6.1 Default Host config fail-closed

`ai_bridge_kit/host.py` managed target：

```toml
[features]
default_mode_request_user_input = false
memories = true
```

必须把 **upstream key/capability presence** 与 **Bridge desired enabled state** 分开：

- key supported + actual false + desired false -> configured；
- stale actual true -> drift；
- `memories` 仍 desired true；
- upstream key完全消失 -> truthful unsupported/incompatible，不因 desired=false 假装兼容；
- unrelated feature config preserved。

### 6.2 HUMAN_ONLY transcript contract：回复路径与无回复路径

任何 user-input request 前仍先做 W2 dependency triage。真正 `HUMAN_ONLY` 才能进入此合同。

共同前缀：

```text
preserve current Goal / resume point / prompt identity
-> one concise plain-text user question
-> immediately stop all dependent execution
-> no polling
-> no default inference
-> no automatic retry
-> no dependent continuation
```

#### 合法等待期限 / run-end authority

不引入 universal 秒数。authority 按以下顺序解析：

1. 当前 frozen Goal/task/workflow 若已有**明确的人类回复期限、hard deadline 或 run-lifetime contract**，使用该现有 contract；056 不自创另一计时器。
2. 若没有显式 human timeout，而 plain-text question 导致当前 interactive Codex execution run/turn 结束，则 **current run end 本身就是当前 handoff 的等待边界**。不得暗示后台仍在持续执行。
3. Default native `request_user_input` 的 60s+60s auto-resolution 与本 transcript transport 无关，绝不能拿来充当 deadline authority。
4. External GPT Planner/Reviewer 的既有 normal-wait contract 是另一类等待，不被本 HUMAN_ONLY 规则改写。

#### A. 明确回复路径

如果在当前 workflow 合法等待仍有效时收到明确回复：

```text
reread current Goal + resume point
-> verify answer belongs to same frozen scope and prompt identity
-> consume answer once
-> exact-once resume
-> Executor performs post-action integration closure
```

Human action 本身不是 completion。

#### B. 无回复 / run-end 路径

若 explicit deadline 到达，或当前 execution run 必须结束而没有明确回复：

```text
GOAL_BLOCKED=YES
GOAL_ACHIEVED=NO
COMPLETE=NO
READY_FOR_USER_REVIEW=NO
DEPENDENT_EXECUTION_BLOCKED=YES
```

controlled workflow 使用**已有合法 human-required/recovery state**。Bridge Lite/Control/Review 若适用 `NEEDS_HUMAN_APPROVAL` 或 repo-defined 等价状态就使用；若某 schema 没有字面 `BLOCKED`，不得新增 enum，只在 user-facing Goal/result 诚实报告 blocked-for-human 并保存 resume point。

这不是“永远不可恢复”或 `STOP`。用户以后在同一 thread 明确回复时：

- 重读 current task/Goal/resume point，确认没有被 supersede；
- 不创建 successor；
- 不重复同一个 prompt；
- consume reply exactly once；
- 同一 Goal 进入现有 recovery/resume path；
- 完成 post-action closure 后才重新进入 completion/admission。

若 Goal/contract/answer identity 已经 stale，则不盲恢复，走现有 Planner/recovery 路由。

### 6.3 GLOBAL_AGENTS_SNIPPET 精确修订

删除“因为 host policy 开启 Default request_user_input 所以……”的过时语义。新规则必须同时表达：

- active run 仍能合法等待时，不仅因为“问用户麻烦”就提前把 Goal判失败；
- HUMAN_ONLY gate 在合法等待结束/run end仍无答复时，Goal 必须 blocked、achieved=no；
- blocked-for-human 是可恢复 handoff，不等于 impossibility/STOP；
- External Planner/Reviewer Waiting 现有语义保持原样。

### 6.4 Lite Handoff L1–L6

canonical `templates/prompts/AGENT_RULES.md` 只加入六条短底线：

- **L1** Positive goal / normal entry / no silent downgrade。
- **L2** Acceptance Review Admission + human action != acceptance。
- **L3** Foreseeable HUMAN_ONLY gate：先 eligibility，plain-text visible question + resume point；run-end/合法 deadline 无回复则 Goal blocked/achieved=no，用 existing legal human-required state，不自创 enum。
- **L4** Faithful validation + evidence-surface + final-candidate identity。
- **L5** No blind rerun + protect accepted/adjacent behavior。
- **L6** Truthful handoff：complete/partial/unsupported/human-blocked/unverified 分清；blocked 必须带 resume point，不能因等待用户而写 achieved/ready。

Lite 不含 Figma/icon/motion/provider/locale/full-suite checklist。

### 6.5 Bridge tests 与 release closure

focused tests至少覆盖：

- fresh install写 `default_mode_request_user_input=false`；
- merge/idempotency/unrelated features preserved；
- stale true -> drift；
- supported + disabled + desired false -> validate PASS；
- missing upstream key truthful handling；
- `memories=true`/现有 Host Policy安全规则不回归；
- canonical Lite install真正得到 L1–L6；
- Host AGENTS 的 HUMAN_ONLY blocked/recovery语义与 External GPT waiting 不冲突。

这些机械测试不单独证明 G1。Bridge target release只有行为 Gates 全过才 `0.8.2 -> 0.8.3`，并同步 `__version__`、CHANGELOG、README current version、CODEX_CONFIG_PROFILE 等当前文档；历史 release/design记录不篡改。

## 7. Phase 2 — AI_Skills 中央 production refinement

### 7.1 Verified Workflow / workflow-core

source authority仍为 current workflow skill/references，不新增顶级 skill/state/schema。

**W1 — Acceptance Review Admission + Vertical/Post-action Closure**

仅 hard-gate acceptance/release/user-ready review。Advisory/diagnostic/design/architecture review可提前但不能输出 readiness。Vertical chain按任务适用项，不机械全选；高风险/多 deliverable才允许 task-local closure table。

HUMAN_ONLY 尚未解决或已进入 blocked-for-human 时，当前 candidate不能通过 Acceptance Admission。Human reply/resume后由 Executor完成 post-action integration closure，再重新评 readiness。

CUHK Date evidence继续并入 W1：breadth claim -> representative corpus/known items；material branches -> small branch coverage；locale claim -> reachable finite-value coverage；persisted/setup/upload state在风险相关时做 action -> visible result -> navigation -> refresh/re-entry -> authoritative state。fallback/recovery只证明 recoverability，除非 Goal明确接受等价，否则不能证明 primary capability complete。

**W2 — Human Decision Gate Semantics**

固定分类：

`HUMAN_ONLY / AGENT_RESOLVABLE / UNSUPPORTED_WITH_EVIDENCE / OPTIONAL_NOT_REQUIRED_FOR_CURRENT_CLOSURE / SAFETY_OR_AUTHORITY_BLOCKER`

只有 HUMAN_ONLY 进入 Default transcript contract。AGENT_RESOLVABLE由 Executor解决；UNSUPPORTED truthful close；OPTIONAL不得为了过 gate偷改 frozen required；SAFETY/AUTHORITY用现有 STOP/Planner/approval。

W2 必须携带 §6.2 的 deadline/run-end semantics：无回复到边界 -> blocked/achieved=no + existing legal recovery state；later explicit reply -> same Goal exact-once recovery。

**W3 — Exact Failure / Verification / Evidence Fidelity**

focused failure evidence、claim scope <= evidence scope、same final candidate。Mock provider只证明 adapter；hosted claim需要安全 bounded configured-target evidence。intermediate input会被代码转换时验证 type/paste/backspace-replace/blur-commit。source count/type support不代替 normal product-entry branch replay。

**W4 — Repeat-failure Circuit Breaker + Human-time Budget**

相同症状再次出现、tests绿但real path再失败、同类问题再次由人发现、active rule再次失效时，下一次 full suite/GPT Work/human QA前先核 candidate/consumer/hypothesis/fixture/evidence/root cause；无新信息不得重跑。

**W5 — Change-impact / Should-not-change**

shared runtime/state/UI/rewrite保护 accepted/adjacent behavior；成熟 structured interaction不得未经产品决策退化为 generic/free-text fallback。

**Existing Source Discovery refinement（不是 W6）**

落实 §4 的 local-source reuse contract，保持原 trigger boundary。普通小任务不因 056 进入重 workflow。

### 7.2 Frontend Design / web-development

仍实现三个 production gate：

**F-A Design Authority & State Coverage**：有 canonical Figma/design 必须读取。material state/variant/responsive/interaction缺失 -> 先改 design source、自审/freeze，再实现；design正确而implementation偏离 -> 只修implementation；无 canonical Figma不强建。

**F-B Design-System Coherence**：shared components/tokens/states、layout/typography/spacing/radius/surface、coherent icon family、brand/generic asset边界、interaction feedback、meaningful motion、reduced-motion/accessibility。generic icon优先项目既有/platform/mature library；custom icon只限 identity/domain/genuine gap。不固定全球唯一库、不强制所有icon动画、不强制小项目central registry。若 frozen objective包含多 locale，finite reachable enum/token必须完整本地化，internal identifier不得production fallback，proper noun/acronym只narrow allowlist。

**F-C Actual-Surface Convergence**：真实 target surface whole-product、canonical design比较、risk-scaled visual/interaction regression、producer obvious defect先清零再external acceptance；screenshot不冒充click/native/live。

当前 generated Frontend Design production visual aggregate尚未直接消费 standalone `figma-design-to-code` 与 `motion-interaction`。实施时通过 `scripts/codex_marketplace_config.json` source authority接入现有 `web-development` plugin generated payload，再用 canonical generator更新；不手改 generated plugin，也不建新 plugin。

### 7.3 AI Skills Maintainer / ai-skills-core

强化一个 `production consumption diagnosis`：active rule仍失败时先核 installed version、source/generated parity、plugin invocation、trigger、task entry、session loading、normal-entry replay，区分 rule missing/not loaded/stale install/consumer not routed/test not faithful/execution noncompliance/capability gap。source `SKILL.md`存在不等于production invocation。

### 7.4 TODO、release metadata 与版本

只有 final candidate 通过 original-failure replay + unrelated regression + release closure，才合并/promote相关 TODO 并正式 bump：

```text
Repository bump decision: PATCH
AI_Skills_Collection: 5.0.4 -> 5.0.5
workflow-core: 0.1 -> 0.2
web-development: 0.1 -> 0.2
ai-skills-core: 0.2 -> 0.3
Bridge Kit: 0.8.2 -> 0.8.3
Bobbio runtime: unchanged
```

056 只是兼容 refinement，不新增 repository-level user workflow/plugin，所以不是 AI_Skills minor。Critic reporting contract/README 本轮 planning-doc修改本身也不触发 plugin/repo release bump。

## 8. Phase 3 — Bobbio 最小 locator

只修改 Bobbio `AGENTS.md` frontend/Product Design required read-list，加入：

`docs/design/FIGMA_HANDOFF.md` — current canonical visual design source。

保留 `docs/PRODUCT_DESIGN_BRIEF.md` 和 active milestone requirement。不得复制 F-A/F-B/F-C checklist，不改 Figma/product code/runtime version。其余 repo按 §3 disposition全部不改 AGENTS。

## 9. Mechanical/source/generated verification

AI_Skills先窄 tests，再 canonical registry/catalog/Marketplace generation/validate/audit/unittest；证明 generated `workflow-core 0.2`、`web-development 0.2`、`ai-skills-core 0.3` 与 source/config/changelog一致，并证明 Frontend production payload实际消费 Figma+motion source。

Bridge Kit先 focused host/Lite tests，再 full unit suite与版本/docs一致性。Mechanical PASS只证明机械性质，不能替代 G1–G8 normal-entry behavior。

## 10. Final-candidate freeze

所有 production source、generated payload、versions/changelogs、Bridge release metadata稳定后冻结：

```text
AI_SKILLS_FINAL_CANDIDATE_COMMIT=<sha>
AI_SKILLS_GENERATED_PLUGIN_HASHES=<workflow/web/maint hashes>
BRIDGE_FINAL_CANDIDATE_COMMIT=<sha>
BRIDGE_VERSION=0.8.3
BOBBIO_LOCATOR_COMMIT=<sha or PENDING until central gates pass>
CODEX_HOST_IDENTITY=<exact current identity>
HOST_CONFIG_PRE_CHANGE_BACKUP=<path/hash>
HOST_CONFIG_FINAL_HASH=<hash>
```

release-critical evidence必须来自同一 tuple。任何 post-freeze production source/generated/version/acceptance-contract修改都使相关 PASS失效并要求重新 freeze/replay。

## 11. G1–G8 normal-entry Capability Gates

### G1 — Human-gate recognition / transport

同 final candidate必须分别证明两个 HUMAN_ONLY 分支，而不是只测“有人回复”：

**G1-A reply path**

```text
HUMAN_ONLY recognized
-> one plain-text question
-> no dependent work before answer
-> explicit in-scope reply
-> reread Goal/resume point
-> exact-once resume
```

同时证明 AGENT_RESOLVABLE不prompt、UNSUPPORTED_WITH_EVIDENCE truthful close、Default不出现native auto-resolving card、managed flag=false；Plan-mode合法 native question不因Default-only flag被破坏。

**G1-B no-reply / run-end path**

使用 faithful bounded normal-entry fixture，不要求用户真人等待：

```text
HUMAN_ONLY recognized
-> question emitted
-> simulated/real legal run-end or explicit frozen human deadline reached with no reply
-> no dependent action
-> GOAL_BLOCKED=YES
-> GOAL_ACHIEVED=NO
-> COMPLETE=NO
-> READY_FOR_USER_REVIEW=NO
-> existing legal human-required/recovery state preserved
-> later explicit in-scope recovery answer injected/received
-> same Goal exact-once resume
```

不能靠 grep/字符串存在证明 G1-B；必须观察实际 normal-entry decision/handoff/recovery behavior。fixture不得创建第二状态机。

最终真人 smoke只做 G1-A 的最小安全回复，并且放在所有 agent可完成 gates之后，避免用户成为 debugger。

### G2 — Acceptance Admission

incomplete evidence -> acceptance-ready denied；advisory review仍可发生。CUHK-Date-like broad-green candidate只要存在 demo breadth、missing material branch、raw token、mock-only hosted provider、real interaction sequence bug、fallback-only primary feature或hosted config未消费backend -> `READY_FOR_USER_REVIEW=NO`。

HUMAN_ONLY 当前处于 G1-B blocked 状态时也不得 acceptance-ready。

### G3 — Resume / post-action closure

覆盖两种恢复：

1. reply path：明确答复后 same Goal exact-once继续；
2. blocked recovery path：run-end已报告 blocked/achieved=no 后，后续明确答复通过已有合法 recovery/resume path恢复同一 Goal，不建 successor、不重复prompt。

Human action本身不算 feature completion；Executor完成 post-action integration closure后才重新进入 admission。

### G4 — Faithful regression

old-bad/real failing sequence被focused evidence捕获，new final candidate同层级PASS。至少冻结 interaction-sequence 与 mock-vs-hosted 类 regression；不把 broad suite代替真实 failure。

### G5 — Evidence / final-candidate identity

unit/synthetic/browser/helper/screenshot只证明对应 surface；关键 PASS来自同一 final tuple；old candidate不能拼给new。fallback只证明 recoverability。

### G6 — Frontend design consumption

用一个有 canonical design 的真实 normal UI planning/implementation-handoff task，优先 Bobbio current design authority作为 read-only source，证明 production Frontend Design定位并消费设计源；material missing state要求先回 design，而不是 implementation临时发明。无需本轮修改 Bobbio Figma/product code。

### G7 — Non-overreach

至少 docs-only、backend/server-only、tiny nonvisual fix三个负例，不得被强制 Figma、locale/catalog/provider matrix、GPT Work、full E2E/native UI smoke。

### G8 — Consumption-regression diagnosis

public-safe normal-entry fixture证明：active source rule存在但 installed/generated/session/trigger/task entry未消费时，production AI Skills Maintainer先暴露并定位 consumption regression，不新增同义 rule；正常已消费场景不产生额外长篇政策复盘。

### Existing Source Discovery regression — 明确不是 G9

`existing canonical local repo + unrelated dirty file + needs clean task surface` -> dirty preserved -> identity/freshness checked -> authorized local reuse/worktree -> no redundant network clone -> no remote remap。

它是既有 Source Discovery enforcement regression，不新增用户能力编号，因此保持 G1–G8。

## 12. Human-time budget 与 current-host smoke

所有 implementation、focused tests、source/generated parity、local production replay、Bridge tests、Frontend wiring、maintainer diagnosis fixture、G1-B无回复fixture和其他非人工 gates先完成。

只有它们全绿后，才在 **056 probe 同一 Windows Codex identity** 安装 task-owned Bridge candidate / `ai-bridge host install` / `validate`，安装 candidate AI_Skills plugins并 fresh-session replay。最后只请求用户一次安全的 G1-A回复：

`056 W2 final normal-entry smoke：请回复精确文本 W2_RESUME_056_FINAL。`

如果当前 run 因等待该回复而结束，则必须按 G1-B/§6.2 user-facing semantics报告 blocked/achieved=no；用户以后回复该 token时从同一个 Goal/resume point恢复，不能另开 repair task或再次索权。

## 13. Should-not-change

至少保护：

- Bridge仍只有 Lite/Review/Control三档；Persistent Run不是第四 workflow；
- External GPT normal waiting语义不被 HUMAN_ONLY blocked 规则污染；
- Plan-mode native request_user_input不因Default flag关闭而被Bridge禁用；
- Host Policy其他安全边界不变；
- workflow-core trigger不扩到所有小任务；
- Frontend不强制所有项目Figma、不固定唯一icon library、不强制所有icon动画/registry；
- domain专业判断仍由domain plugin拥有；
- Bobbio native self-QA/GPT Work/user acceptance与Zotero安全不改；
- Lucerna/Mica/Asteria/SeminarArc/CUHK Date AGENTS不新增056同义规则；
- no paid API/Terra。

## 14. Rollback / recovery

### HUMAN_ONLY blocked recovery

blocked-for-human 是当前 Goal无法继续/完成的诚实 handoff，不是 successor trigger。保存 Goal id、prompt identity、resume point、existing machine recovery state。用户后续明确回复后先核 scope/identity是否仍 current，再 same Goal exact-once resume；如果已 superseded/stale则回 Planner，不消费旧回答。

### Bridge host rollback

`ai-bridge host install`必须保留 pre-change exact backup。current-host smoke失败：停止 release/integration，恢复该次 install exact backup；不手工猜 config、不自动把 flag改回true后宣称完成；保留 evidence回 Planner/Critic。

### AI_Skills rollback

candidate branch与released baseline隔离。plugin replay失败则保留失败 evidence，恢复/reinstall released payload；不得删fixture或降 acceptance制造PASS。

### Bobbio

locator遇到相关 dirty/conflict就暂停该子步骤，不clone/remap/overwrite。

## 15. Release / integration boundary

Executor完成后只 commit/push exact authorized task branches与Bobbio locator change，写 final tuple/evidence，然后停止在 implementation handoff。当前 Kickoff不授权 main merge/release integration、branch deletion或Executor自宣 achieved。

implementation audit必须对 exact tuple PASS。只有后续批准的 integration step才允许将 candidate进入 main/release。

## 16. Planning/review contract change（本轮已做，不是 Executor production scope）

本 v0.2 package 同时按用户直接要求修订 `docs/workflows/CRITIC_ROLE_CONTRACT.md`：若同一 major round/Active Review Context 曾正式 `REVISE`，后续 `PASS` 必须先给用户可读的 closure explanation，再给 machine fields/approved kickoff。README Critic复审模板只做最小摘要同步。

这只是 Planner/Critic reporting contract，不是新 capability gate，不触发 plugin/repository版本发布，也不要求 Executor重复修改。

## 17. 本轮外部现实核对

返修时重新核对 current `openai/codex main@1e9564fb859c7543404ede96ba5d92f1ef7faefc`：Default template仍规定 required input用 plain-text question，handler仍按 `mode == Plan` 设置 blocking，故 native-disable + transcript transport方向没有新证据要求重开。OpenAI 当前 agent-first工程经验继续强调 human time/attention与 agent self-verification；Figma current Dev Mode/Ready-for-dev仍支持明确 design handoff/source consumption。以上只验证既有方向，没有新增架构层。

`NEXT_HANDOFF = CRITIC`
