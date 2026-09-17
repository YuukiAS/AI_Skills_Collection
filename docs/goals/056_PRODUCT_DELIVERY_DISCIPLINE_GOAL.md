# 056 Product Delivery Discipline — Canonical Goal

- Execution package version: `v0.2`
- Exact task: `056_product_delivery_discipline`
- Status: `READY_FOR_EXECUTION_CRITIC_REVIEW`
- Plan: `docs/design/056_PRODUCT_DELIVERY_DISCIPLINE_IMPLEMENTATION_PLAN.md` v0.2
- Kickoff: `docs/operations/prompts/056_PRODUCT_DELIVERY_DISCIPLINE_KICKOFF.md` v0.2
- Architecture authority: `docs/design/PRODUCT_DELIVERY_DISCIPLINE_V6_PROPOSAL_2026-09-16.md`
- Post-probe authority: `docs/design/PRODUCT_DELIVERY_DISCIPLINE_V6_POST_PROBE_ADDENDUM_2026-09-17.md`
- Prior execution package: v0.1 at `01766a47325a5e7efb84dc2b75b90d67a010c157`, Critic `REVISE`

本 Goal 只有在独立 Critic 对 **同版 Plan + Goal + Kickoff** 给出 `READY_FOR_CODEX=YES`，且用户随后实际发送获批 Kickoff 后才可执行。当前文件本身不是执行授权。

## 0. Positive completion target

把已批准的 Product Delivery Discipline v6 真正接入 normal production path，使以后复杂/高风险开发默认由 agent 自己完成实现、忠实测试、真实 surface、自审与修复，再进入 GPT Work/用户 acceptance；真正需要用户的 Default HUMAN_ONLY gate 使用 durable transcript question，未答时绝不继续，run/deadline结束仍未答则 Goal 明确 blocked/achieved=no，并允许后来从同一个 Goal 精确恢复；Frontend Design 有 canonical design 时必须消费设计源；active rule 已存在但失效时先查真实消费链。

完成必须由 normal-entry behavior 证明，不得以新增 Markdown/TODO/字段/关键词替代。

## 1. Execution scope

### AI_Skills_Collection

实现并在 gates 全部通过后形成兼容 release candidate：

- `workflow-core 0.2`：W1–W5 + existing Source Discovery refinement；
- `web-development 0.2` / Frontend Design：F-A/F-B/F-C，并把现有 Figma handoff + motion capability真正接入 production payload；
- `ai-skills-core 0.3` / AI Skills Maintainer：production consumption diagnosis；
- repository target `5.0.5 PATCH`；
- source-first、generated parity、TODO/changelog/version/release closure；
- G1–G8 normal-entry capability replays。

Exact execution branch only after approved kickoff:

`reviewed/056_product_delivery_discipline`

### GPT_Codex_AI_Bridge_Kit

实现：

- Lite Handoff L1–L6 baseline；
- managed `default_mode_request_user_input=false`；
- Default HUMAN_ONLY durable transcript blocked/recovery semantics；
- supported-key vs desired-enabled-state validation；
- current Host Policy docs/tests；
- target release `0.8.3` only after gates pass。

Exact execution branch only after approved kickoff:

`reviewed/056_product_delivery_discipline`

### Bobbio

只允许在现有 `develop` 做一个 locator change：frontend/Product Design required read-list 加入 current canonical `docs/design/FIGMA_HANDOFF.md`，保留 `docs/PRODUCT_DESIGN_BRIEF.md` 与 active milestone。不得复制中央 Frontend checklist，不改 Figma/product code/runtime version。

### Explicitly untouched product repos

Lucerna、Mica-for-ChatGPT、Asteria、SeminarArc、CUHK Date、CARE/EAT、Server/VPS、Longleaf_Bridge 以及 Scientific Visualization production behavior 不在本 Goal 修改范围。

## 2. Repo-specific AGENTS frozen disposition

Executor 不得临场重新扩 scope：

- **Bobbio = `ADD_MINIMAL_LOCATOR`**：只补 `docs/design/FIGMA_HANDOFF.md` locator。现有 Zotero/native/pre-user QA 项目规则保留。
- **Lucerna = `ALREADY_COVERED`**：当前 AGENTS 已有 Windows release、matching regression、real provider/no mock release evidence、tray/provider/Longleaf 项目 invariants；不加 056 同义规则。
- **Mica = `ALREADY_COVERED`**：当前 AGENTS 已有 real failure reproduction、内建 bounded diagnostics、focused-before-full-E2E、short manual loop、ChatGPT/Edge 边界、typing hot path；不加同义规则。
- **Asteria = `ALREADY_COVERED`**：已有 developer visual self-QA、scientific graph system、generic-fix、GPT Work-before-human、regression；不复制中央 checklist。
- **SeminarArc = `NO_CHANGE / EVIDENCE_NEEDED`**：没有 direct evidence 证明 project-level canonical Figma locator 缺失；保持现状。
- **CUHK Date = `NO_GENERIC_056_AGENTS_COPY`**：V4 failure由 W1/W3/W5/Frontend吸收；当前 GitHub无 tracked root AGENTS 可供本任务合理扩写。若未来出现真正项目特有 locator/invariant，必须带 direct evidence回 Planner/Critic。

原则：repo AGENTS只放 project invariant/source locator/安全与环境真值。056 不以“统一”为理由复制中央 delivery policy；也不在中央能力尚未通过 production replay前大规模删除现有项目保护。

## 3. Git/source preflight

执行开始后按 Plan 的 Source Discovery：

- 先定位本机已有 canonical checkout/worktree/clone；
- 核 repo identity、branch/ref、origin、freshness、dirty ownership；
- unrelated dirty work只保护，不因此弃用 local source；
- AI_Skills/Bridge exact task branch/worktree从 kickoff时最新、仍兼容获批 package 的 authority建立；
- 不 network clone 已存在正确 repo；
- 不 remap remote；
- Bobbio继续 current `develop`，不新建 task branch。

identity冲突、authority发生相关语义变化或无法安全定位 source -> `NEEDS_GPT_PLANNER`，不自行换编号/路线。

## 4. Bridge Kit contract

### B1 — Lite baseline

将六条短底线写入 canonical Lite `templates/prompts/AGENT_RULES.md`：

1. L1 positive goal / normal entry / no silent downgrade；
2. L2 acceptance Review Admission + human action != acceptance；
3. L3 foreseeable HUMAN_ONLY gate + eligibility + plain-text question + resume point；若合法 human wait/run结束仍无答复，Goal blocked/achieved=no并使用 existing legal human-required state；
4. L4 faithful validation + evidence surface + final-candidate identity；
5. L5 no blind rerun + protect accepted/adjacent behavior；
6. L6 truthful handoff：complete/partial/unsupported/human-blocked/unverified 分清，blocked带 resume point，不能冒充 ready/achieved。

不得把 Figma/icon/motion/provider/locale/full-E2E checklist 写入 Lite。

### B2 — Default host config fail-closed

Managed config：

```toml
[features]
default_mode_request_user_input = false
memories = true
```

upstream key presence 与 desired state分开。supported+false+desired false => configured；stale true => drift；missing key => truthful unsupported/incompatible；unrelated config preserved。

### B3 — HUMAN_ONLY durable transcript contract

共同流程：

```text
HUMAN_ONLY
-> preserve Goal/resume point/prompt identity
-> one concise plain-text question
-> stop dependent execution immediately
-> no polling/default inference/retry/timeout-continue
```

等待边界 authority：

1. frozen Goal/task/workflow已有明确 human-response deadline/hard deadline/run-lifetime时，用现有 contract；
2. 没有显式 timeout，而 plain-text question 后 current Codex execution run/turn结束时，run-end就是当前 handoff边界；不得假装后台继续等待；
3. native request_user_input 的60+60秒不是 transcript timeout authority；
4. External GPT normal waiting不受此规则改变。

**Reply path**：在合法 scope内收到明确回复 -> reread Goal/resume point -> verify current prompt/scope -> consume once -> exact-once resume -> Executor完成 post-action closure。

**No-reply/run-end path**：等待边界到达仍无答复 -> 必须报告：

```text
GOAL_BLOCKED=YES
GOAL_ACHIEVED=NO
COMPLETE=NO
READY_FOR_USER_REVIEW=NO
DEPENDENT_EXECUTION_BLOCKED=YES
```

controlled machine state使用当前 workflow已有的 `NEEDS_HUMAN_APPROVAL` / human-required / recovery等合法等价，不创建 `BLOCKED` 新 enum。该状态可恢复，不等同 STOP/impossibility。

用户以后同 thread回复：重读 current Goal/resume point并确认未 supersede -> 不开 successor、不重复 prompt -> consume once -> same Goal recovery/resume -> post-action closure -> 再评 admission。若 identity stale，回 Planner。

### B4 — Host guidance/tests/release

`GLOBAL_AGENTS_SNIPPET` 必须修掉当前“recoverable question绝不是 terminal blocker”的过宽表述：active run尚能合法等待时不因不便而提前失败；但 HUMAN_ONLY 到期限/run-end无答复时 Goal必须 blocked/achieved=no。External GPT waiting段保持不变。

Host tests/Lite install tests按 Plan覆盖 config false、merge/idempotency、stale true、supported+desired false、missing key、unrelated config、memories、安全规则与 L1–L6。Behavior G1不能靠字符串测试代替。

Bridge `0.8.3` 只有 final gates全通过才发布。

## 5. Verified Workflow contract

不新增 W6。

### W1 — Acceptance Review Admission + Vertical/Post-action Closure

只 hard-gate acceptance/release/user-ready review；advisory/diagnostic/design/architecture review可提前但不得宣称ready。Vertical closure按 frozen scope适用项，高风险/多deliverable才允许 task-local closure table。

HUMAN_ONLY blocked-for-human状态不能通过 acceptance admission。用户恢复后由 Executor完成 post-action integration closure再重新判断。

CUHK Date breadth/branch/locale/state-lifecycle/fallback-not-primary规则按 frozen claim触发，不扩成所有任务全矩阵。

### W2 — Human Decision Gate

分类：

`HUMAN_ONLY / AGENT_RESOLVABLE / UNSUPPORTED_WITH_EVIDENCE / OPTIONAL_NOT_REQUIRED_FOR_CURRENT_CLOSURE / SAFETY_OR_AUTHORITY_BLOCKER`

只有 HUMAN_ONLY进入 B3。AGENT_RESOLVABLE自己解决；UNSUPPORTED truthful close；OPTIONAL不能把 frozen required 偷改可选；SAFETY/AUTHORITY走现有路由。

### W3 — Exact Failure / Verification / Evidence Fidelity

focused real failure、claim scope<=evidence surface、same final candidate。Mock adapter不证明hosted provider；hosted claim需安全 bounded configured-target evidence；controlled input测真实 type/paste/backspace/blur sequence；source count/type不替代normal product-entry branch replay。

### W4 — Repeat-failure Circuit Breaker + Human-time Budget

同类失败第二次且无新信息，禁止继续 full-suite/GPT Work/human rerun；先重查 candidate、consumer、hypothesis、fixture、evidence surface/root cause。

### W5 — Change-impact / Should-not-change

shared change保护 accepted/adjacent behavior；rewrite/refactor不得未经产品决策把成熟 structured interaction降级为 generic/free-text fallback。

### Existing Source Discovery

local canonical source优先并核 freshness/identity/dirty ownership；dirty != abandon；只有无可用 local source才 network clone；不 remap remote作为普通路径。它仍是 existing capability，不新增 W6/G9。

## 6. Frontend Design contract

### F-A — Design Authority & State Coverage

有 canonical Figma/design必须读取；material state/variant/responsive/interaction缺失先更新 design source并自审/freeze，再实现；design正确而code偏离只修implementation；无canonical Figma不强建。

### F-B — Design-System Coherence

shared components/tokens/states、layout/typography/spacing/radius/surface、coherent icon family、brand/generic boundary、interaction feedback、meaningful motion、reduced-motion/accessibility。generic icon优先项目既有/platform/mature library；custom只限identity/domain/genuine gap；不固定唯一库、不强制所有icon动画、不强制小项目registry。

frozen locale claim存在时 finite reachable token完整本地化，internal enum不得production fallback，proper noun/acronym narrow allowlist。

### F-C — Actual-Surface Convergence

真实 target surface whole-product、canonical-design compare、risk-scaled visual/interaction regression、producer obvious defects先清零；screenshot不冒充click/native/live。

### Production wiring

通过 `scripts/codex_marketplace_config.json` 把已有 `figma-design-to-code` 与 `motion-interaction` 接入现有 Frontend Design production payload/aggregate，canonical generator生成。不得只改 source不接production，也不得手改 generated plugin。

## 7. AI Skills Maintainer contract

强化 `production consumption diagnosis`：active rule仍失败时先核 installed version、source/generated parity、plugin invocation、trigger、task entry、session loading、normal-entry replay，再区分 rule missing/not loaded/stale install/consumer not routed/test not faithful/execution noncompliance/capability gap。source `SKILL.md`存在不等于 production invocation。

## 8. Bobbio locator contract

只把 `docs/design/FIGMA_HANDOFF.md` 加入 frontend/Product Design required read-list并标为 current canonical visual design source；不得添加中央 checklist、改 Figma/product code/runtime version。

## 9. Mechanical validation / release

AI_Skills执行 canonical source/generated/Marketplace/validate/audit/catalog/unit/version/changelog/README parity；Bridge执行focused host/Lite tests + full unit suite/docs/version parity。

Behavior全部通过且准备正式交付时才：

```text
AI_Skills_Collection 5.0.4 -> 5.0.5 PATCH
workflow-core 0.1 -> 0.2
web-development 0.1 -> 0.2
ai-skills-core 0.2 -> 0.3
Bridge Kit 0.8.2 -> 0.8.3
Bobbio runtime unchanged
```

## 10. Final candidate identity

Freeze前完成 production source/generated/version/changelog。记录 exact AI_Skills candidate+plugin hashes、Bridge candidate/version、Bobbio locator commit、exact host identity、pre-change Host backup、final config hash。任何 production/generated/version/acceptance contract变化使受影响 PASS失效。

## 11. G1–G8

### G1 — Human gate / transport

必须有两个不同 behavior replay：

**G1-A reply path**：HUMAN_ONLY -> plain-text question -> no dependent work -> explicit reply -> reread Goal/resume point -> exact-once resume。并证明 AGENT_RESOLVABLE不prompt、UNSUPPORTED truthful close、Default native card不出现、managed flag=false、Plan-mode合法 capability不回归。

**G1-B no-reply path**：faithful bounded fixture，不要求用户真人等待：question -> legal run-end/explicit frozen deadline with no reply -> no dependent action -> `GOAL_BLOCKED=YES / GOAL_ACHIEVED=NO / COMPLETE=NO / READY_FOR_USER_REVIEW=NO` -> existing legal recovery state -> later explicit recovery answer -> same Goal exact-once resume。不能靠字符串扫描判PASS。

所有非人工 gates完成后才做一次真人 G1-A smoke：请求精确回复 `W2_RESUME_056_FINAL`。若当前 run在用户回复前结束，则先按 G1-B semantics blocked/achieved=no；用户后续回复后同Goal恢复。

### G2 — Acceptance Admission

incomplete evidence/human-blocked state不得user-ready；advisory review不被拦。CUHK-Date-like broad-green candidate存在 demo breadth/missing branch/raw token/mock-only hosted provider/interaction sequence bug/fallback-only primary/hosted config未消费backend -> `READY_FOR_USER_REVIEW=NO`。

### G3 — Resume/post-action closure

既验证即时 reply path，也验证 blocked后的later recovery path；都必须 same Goal exact-once。Human action本身不算complete，post-action integration closure完成后才可重新 admission。

### G4 — Faithful regression

old-bad/真实失败sequence被focused evidence捕获，new final candidate同层级PASS；包括interaction sequence与mock-vs-hosted代表场景。

### G5 — Evidence/final candidate

unit/synthetic/browser/helper/screenshot只证明对应surface；关键PASS来自同一final tuple；fallback只证明recoverability。

### G6 — Frontend design consumption

用有canonical design的真实 normal UI task（优先Bobbio current authority作read-only source）证明 production Frontend Design实际消费design source；missing state不得implementation临时发明。

### G7 — Non-overreach

至少 docs-only、backend/server-only、tiny nonvisual fix三个负例，不被强制Figma/locale/catalog/provider/GPT Work/full E2E/native smoke。

### G8 — Consumption regression diagnosis

active rule存在但 installed/generated/session/trigger/task entry未消费时，production maintainer先暴露消费问题，不新增同义rule。

### Source Discovery regression（不是 G9）

existing canonical local repo + unrelated dirty -> preserve dirty -> verify identity/freshness -> authorized local reuse/worktree -> no redundant clone -> no remote remap。

## 12. Current-host gate and human-time budget

所有 agent可完成 implementation/test/source-generated/local replay/G1-B fixture/other gates先完成。然后才在 056 probe同一 Windows Codex identity 做 bounded Bridge candidate install/host install+validate、AI_Skills candidate plugin fresh-session replay。最后只请求一次 `W2_RESUME_056_FINAL`，不得让用户做普通 debugging。

## 13. Recovery

- HUMAN_ONLY no-reply：保存 Goal/prompt/resume/state；blocked/achieved=no；later explicit reply同Goal恢复，不自动 successor，不重复prompt；stale identity回Planner。
- Bridge host smoke失败：恢复本次 install exact backup；不手工猜config。
- AI_Skills replay失败：保留released baseline和failure evidence，不删fixture/降标准。
- Bobbio dirty/conflict：暂停locator，不clone/remap/overwrite。

## 14. Commit/push and handoff

Approved Kickoff可授权 AI_Skills/Bridge exact task branches普通commit/push与Bobbio locator在existing develop普通commit/push。不得force、remote mutation、PR、main merge、branch deletion。

Executor完成 implementation/self-QA/G1–G8/final tuple并push后停止在 implementation handoff（`EXECUTED_UNAUDITED`或repo合法等价）。不得自行宣布整个056 achieved。

## 15. Result artifacts

AI_Skills public-safe summary留repo；private/current-host evidence放 `private/exports/056_product_delivery_discipline/`。不得上传host secrets/private config正文。跨repo final manifest记录exact commit/hash locator。

## 16. Stop conditions

回 `NEEDS_GPT_PLANNER` / legal equivalent而不是扩 scope：upstream变化推翻W2；需要新provider/credential/paid API；需要新state/controller/watcher；branch/worktree identity冲突；F-A/B/C需要改变architecture；G1–G8显示v6机制本身不成立；必须修改明确 untouched product repo才能做PASS。

## 17. Critic reporting closure prerequisite

本 execution package同时依赖当前 repo 的通用 Critic reporting contract：同一 major round曾有 `REVISE` 时，后续 `PASS` 必须先向用户用正常中文解释 blocker如何关闭、各层改/没改、Gate证明什么、repo-specific disposition、实际workflow变化与PASS边界，然后才输出 machine fields 和 verbatim approved Kickoff。该合同是 planning/review层规则，不属于 Executor production实现范围。
