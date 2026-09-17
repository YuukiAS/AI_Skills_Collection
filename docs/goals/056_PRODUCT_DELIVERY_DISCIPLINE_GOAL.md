# 056 Product Delivery Discipline — Canonical Goal

- Execution package version: `v0.1`
- Exact task: `056_product_delivery_discipline`
- Status: `READY_FOR_EXECUTION_CRITIC_REVIEW`
- Plan: `docs/design/056_PRODUCT_DELIVERY_DISCIPLINE_IMPLEMENTATION_PLAN.md` v0.1
- Kickoff: `docs/operations/prompts/056_PRODUCT_DELIVERY_DISCIPLINE_KICKOFF.md` v0.1
- Architecture authority: `docs/design/PRODUCT_DELIVERY_DISCIPLINE_V6_PROPOSAL_2026-09-16.md`
- Post-probe authority: `docs/design/PRODUCT_DELIVERY_DISCIPLINE_V6_POST_PROBE_ADDENDUM_2026-09-17.md`

本 Goal 只有在独立 Critic 对 **同版 Plan + Goal + Kickoff** 给出 `READY_FOR_CODEX=YES`，且用户随后实际发送获批 Kickoff 后才可执行。当前文件本身不是执行授权。

## 0. 完成目标

把已经批准的 Product Delivery Discipline v6 真正接入 normal production path，使以后复杂/高风险产品开发优先由 agent 自己完成实现、忠实测试、真实 surface、自审和修复，再进入 GPT Work/用户 acceptance；真正需要用户的 Default-mode gate 使用 durable transcript wait/resume，不再依赖会 auto-resolve 的 native card；Frontend Design 有 canonical design 时按 design source 实现；active rule 已存在但失效时先查消费链，不继续堆同义规则。

完成必须体现为真实 normal-entry behavior，而不是仅新增 Markdown、TODO、字段或字符串。

## 1. Execution scope

### AI_Skills_Collection

实现并发布：

- Lite 的详细行为不复制到 AI_Skills；AI_Skills负责 `workflow-core 0.2`、`web-development 0.2`、`ai-skills-core 0.3`；
- repository release target `5.0.5`；
- source-first 修改、generated Marketplace parity、changelog/TODO/release closure；
- G1–G8 normal-entry capability replays。

Exact execution branch after approved kickoff:

`reviewed/056_product_delivery_discipline`

### GPT_Codex_AI_Bridge_Kit

实现：

- Lite Handoff 6-rule baseline in canonical project template；
- `default_mode_request_user_input=false` fail-closed Host Policy；
- durable transcript HUMAN_ONLY semantics；
- supported-key vs desired-enabled-state validation；
- Bridge target release `0.8.3`；
- current-host bounded install/rollback path。

Exact execution branch after approved kickoff:

`reviewed/056_product_delivery_discipline`

### Bobbio

只允许在现有 `develop` 中做一个 locator change：frontend/Product Design task read-list 加入 current canonical `docs/design/FIGMA_HANDOFF.md`，同时保留 `docs/PRODUCT_DESIGN_BRIEF.md` 与 current milestone。不得复制中央 checklist，不改 product code/Figma/runtime version。

### Explicitly untouched

Lucerna、Mica-for-ChatGPT、Asteria、SeminarArc、CUHK Date、CARE/EAT、Server/VPS、Longleaf_Bridge，以及 Scientific Visualization production behavior 都不在本 Goal 修改范围。

## 2. Git/source preflight

执行开始后先按 Plan §3 做 Source Discovery：

- 找已有 canonical checkout/worktree/clone；
- 核 repo identity、branch/ref、origin、freshness、dirty ownership；
- unrelated dirty work只保护，不因此弃用 local source；
- AI_Skills 与 Bridge Kit 的 task branch/worktree必须从 kickoff 当时最新 remote authority 建立；
- 不 network clone 已存在的正确 repo；
- 不 remap Git remote；
- Bobbio继续 current `develop`，不新建 Bobbio task branch。

若 exact task branch/worktree identity冲突、authority发生与056相关的实质变化、或 source无法安全定位，`NEEDS_GPT_PLANNER`，不要自行换编号/路线。

## 3. Bridge Kit implementation contract

### B1 — Lite baseline

将 v6 L1–L6 写入 canonical Lite `templates/prompts/AGENT_RULES.md`，保持短而通用：

1. positive goal / normal entry / no silent downgrade；
2. acceptance Review Admission + human action != acceptance；
3. foreseeable HUMAN_ONLY gate + eligibility + visible transcript question + resume point；
4. faithful validation + evidence surface + final-candidate identity；
5. no blind rerun + protect accepted/adjacent behavior；
6. truthful handoff + unverified boundary + resume point。

禁止把 Figma/icon/motion/provider/locale/full-E2E checklist写入 Lite。

### B2 — Default user-input fail-closed

`ai_bridge_kit/host.py` managed config：

```toml
[features]
default_mode_request_user_input = false
memories = true
```

Feature key supported/present 与 desired state 分开。supported + false + desired false必须 validate PASS；stale true是 drift；missing key保持 truthful incompatible/unsupported，不伪造支持。

### B3 — Default HUMAN_ONLY transport

更新 Host Policy active guidance：

```text
HUMAN_ONLY
-> preserve resume point
-> one concise plain-text question
-> immediately stop dependent execution
-> unanswered: no dependent work / polling / default / retry / timeout-continue / completion
-> DEPENDENT_EXECUTION_BLOCKED=YES
-> TERMINAL_BLOCKED=NO
-> same-thread explicit answer
-> reread current task/resume point
-> validate scope
-> exact-once resume
-> executor completes post-action integration closure
```

Default native `request_user_input` 不用于 HUMAN_ONLY。不得新增 watcher/daemon/Persistent Run/tmux/Control/ledger/state machine。Plan mode不由本 Goal重实现或禁用。

### B4 — Bridge regression/release

补 Host Policy/Lite tests、完整 unit suite、current docs/version closure。Release只有 gates全绿才从 `0.8.2 -> 0.8.3`。

## 4. Verified Workflow implementation contract

仅强化 W1–W5 与 existing Source Discovery，不新增 W6。

### W1

只 hard-gate acceptance/release/user-ready review；advisory/diagnostic/design/architecture review可提前。Frozen scope内适用项 vertical closure + post-action closure。高风险/多 deliverable才可用 task-local closure table。

吸收 CUHK Date：breadth、material branch、locale finite values、persisted lifecycle在 frozen claim 相关时做 representative closure。fallback只证明 recoverability，除非 Goal明确等价，不证明 primary capability complete。

### W2

依赖分类固定为：

`HUMAN_ONLY / AGENT_RESOLVABLE / UNSUPPORTED_WITH_EVIDENCE / OPTIONAL_NOT_REQUIRED_FOR_CURRENT_CLOSURE / SAFETY_OR_AUTHORITY_BLOCKER`

只有 HUMAN_ONLY走 Default transcript wait/resume。AGENT_RESOLVABLE必须自己解决；UNSUPPORTED truthful close；OPTIONAL不阻塞当前 frozen closure；安全/授权边界走现有 STOP/Planner/approval。

### W3

focused exact failure + evidence fidelity + final candidate identity。mock adapter不能证明hosted provider；configured hosted claim需bounded real-target evidence。intermediate input会被代码转换时测真实 type/paste/backspace/blur sequence。source count/type support不能代替normal product-entry branch replay。

### W4

同类失败第二次且无新信息，禁止继续 full-suite/GPT Work/human rerun；先重查 candidate、consumer、hypothesis、fixture、evidence surface/root cause。

### W5

shared change保护 accepted/adjacent behavior；rewrite/refactor不把成熟 structured interaction静默降级成 generic/free-text fallback。

### Source Discovery

已有本地 canonical repo优先；dirty ownership分离；需要隔离优先已存在正确 source或经授权 canonical worktree；无本地 source才 network clone；不 remap remote作为普通路径。

保持当前 trigger boundary，普通小任务不得被056升级重流程。

## 5. Frontend Design implementation contract

### F-A — Design Authority & State Coverage

有 canonical Figma/design必须实际读取；material production state/variant/responsive/interaction缺失，先更新 design并自审/freeze，再实现；design正确而implementation偏离，只修implementation；必要platform/accessibility deviation显式记录；没有Figma的项目不强建。

### F-B — Design-System Coherence

shared components/tokens/states、layout/typography/spacing/radius/surface、coherent icon family、brand/generic asset边界、interaction feedback、motion grammar、reduced-motion/accessibility。generic icons优先项目既有或成熟library；custom icon只限 identity/domain/genuine gap；不固定全球唯一库、不强制所有icon动画、不强制小项目建registry。

locale frozen claim存在时，finite reachable tokens必须完整本地化，internal enum不得production fallback，proper noun/acronym只narrow allowlist。

### F-C — Actual-Surface Convergence

真实target surface whole-product review、与canonical design比较、risk-matched visual/interaction regression、producer obvious defects先清零再external acceptance；screenshot不冒充click/native/live。

### Production wiring

当前 `web-development` production visual aggregate尚未包含 standalone `figma-design-to-code` 与 `motion-interaction` source。必须通过 `scripts/codex_marketplace_config.json` 的 source authority将它们接入同一 Frontend Design plugin generated payload，再由 canonical generator生成；不得只改未被 production plugin消费的 source，也不得手改 generated plugin。

## 6. AI Skills Maintainer implementation contract

在 canonical maintainer source强化 `production consumption diagnosis`：

active rule failure时先核 installed version、source/generated parity、plugin invocation、trigger、task entry、session loading、normal-entry replay，再区分 missing rule / not invoked / old install / execution noncompliance / conflict / capability gap。source `SKILL.md`存在不等于 production invocation。

相关 TODO应合并新evidence，不重复建同义规则。

## 7. Bobbio locator contract

只把 `docs/design/FIGMA_HANDOFF.md` 加入 `AGENTS.md` 的 frontend/Product Design required read-list，并说明其为 current canonical visual source。不得新增中央 Figma checklist；Bobbio现有 pre-user native self-QA -> GPT Work -> user acceptance保持不变。

## 8. Mechanical validation and release metadata

AI_Skills至少执行 canonical source/generated/full-test gate，包括 Marketplace regenerate/validate、skill validate/audit/catalog、unit tests、version/changelog/README parity。

如果 production behavior通过并准备交付：

```text
AI_Skills repository: 5.0.4 -> 5.0.5
workflow-core: 0.1 -> 0.2
web-development: 0.1 -> 0.2
ai-skills-core: 0.2 -> 0.3
Bridge Kit: 0.8.2 -> 0.8.3
Bobbio runtime version: unchanged
```

如果 original-failure replay / unrelated regression / normal-entry gates未通过，不得提前以version/changelog existence声称release成功。

## 9. Final candidate identity

Freeze前必须完成production source、generated payload、versions/changelogs。记录：

- exact AI_Skills candidate commit + three generated plugin hashes；
- exact Bridge candidate commit/version；
- Bobbio locator commit（若中央 gates已允许落地）；
- exact current Codex host identity；
- pre-change Host Policy backup；
- final managed config hash。

任何改变production source/generated/version/acceptance contract的修复都会使受影响final PASS失效，需要new candidate和相应gate replay。

## 10. G1–G8 capability gates

### G1 — Human gate / transport

同 final candidate直接证明：AGENT_RESOLVABLE不prompt；UNSUPPORTED truthful close；Default HUMAN_ONLY发plain-text question且native card不出现；未回答时dependent execution不继续/不完成/不poll/retry；明确回答后exact-once resume并继续post-action closure。

所有非人工 gates完成后，才进行一次最终安全人工 smoke。Executor发送一条普通聊天问题：

`056 W2 final normal-entry smoke：请回复精确文本 W2_RESUME_056_FINAL。未回复前我不会继续 dependent step。`

这不是native card。用户回复前停止依赖步骤；回复后只恢复一次。不得让用户做其他开发debugging。

同host还要证明 `default_mode_request_user_input=false` 生效，fresh Default正常入口不暴露该optional tool；Plan正常入口仍具合法 question capability，不因Default-only flag关闭而消失。

### G2 — Acceptance Admission

incomplete producer evidence不能生成 user-ready acceptance claim。Advisory review允许但不能变ready。CUHK-Date-like broad-green candidate只要仍有demo breadth/missing branch/raw token/mock-only provider/sequence bug/fallback-only primary/hosted config未消费backend，`READY_FOR_USER_REVIEW=NO`。

### G3 — Resume/post-action closure

G1明确回答后，同一Goal从已记录resume point exact-once继续；human action本身不算completion；Executor完成相关integration closure后才可进入acceptance。

### G4 — Faithful regression

old-bad/real failing sequence被focused evidence捕获，new final candidate同层级PASS。至少包括interaction sequence与mock-vs-hosted provider类fixture，不把broad suite代替原失败。

### G5 — Evidence/final candidate

unit/synthetic/browser/helper/screenshot各自只证明对应surface；release-critical evidence来自同一final tuple；fallback只证明recoverability。

### G6 — Frontend design consumption

用一个有canonical design的真实 normal UI task做read-only/implementation-handoff replay，优先使用Bobbio current Product Design Brief + FIGMA_HANDOFF；production Frontend Design必须定位/消费design source，missing material state不在implementation临时发明。无需本轮修改Bobbio Figma/product code。

### G7 — Non-overreach

至少 docs-only、backend/server-only、tiny nonvisual fix三个负例，证明不会被强制Figma/locale/catalog/provider/GPT Work/full E2E/native smoke。

### G8 — Consumption regression diagnosis

public-safe fixture中 active source rule存在但 installed/generated/session/trigger/task entry未消费时，production AI Skills Maintainer必须先暴露/定位consumption regression，不新增同义policy。

### Existing Source Discovery regression

existing canonical local repo + unrelated dirty file + needs clean surface -> dirty preserved -> correct local source found -> authorized reuse/worktree -> no redundant network clone -> no remote remap。此项不新增G编号。

## 11. Current-host install gate

只有Bridge source tests与AI_Skills source/generated机械gates绿后，才使用Kickoff授权对**056 probe同一Windows Codex identity**执行：

- candidate Bridge Kit local install/upgrade；
- `ai-bridge host install`（自动生成exact backup）；
- `ai-bridge host validate`；
- candidate AI_Skills plugins install/upgrade + fresh session replay。

不得作用到另一个 `$CODEX_HOME` 冒充current-host gate。若identity无法证明，完成其他independent work后停在truthful environment boundary。

## 12. Rollback

Bridge Host Policy失败：恢复本次install生成的exact backup，保留candidate/evidence，回Planner/Critic；不手工猜config。AI_Skills replay失败：保留released baseline identity并恢复/重装baseline payload；不删failure fixture或降标准。Bobbio relevant dirty/conflict：暂停locator子步骤，不clone/remap/overwrite。

## 13. Commit/push 与 handoff

Kickoff可授权 task-owned ordinary commits/push：

- AI_Skills exact reviewed branch；
- Bridge exact reviewed branch；
- Bobbio existing `develop` only for locator change。

不得force push、remote mutation、PR、main merge、branch deletion或跨scope publication。

Executor完成实现、自测、G1–G8 evidence和final candidate commit/push后，状态必须是 implementation handoff（例如 `EXECUTED_UNAUDITED` / repo合法等价状态），交独立 Reviewer/Critic审 final tuple。Executor不得自行宣布整个056 achieved或直接把task branches集成main。

## 14. Result artifacts

AI_Skills task result/evidence必须留repo；public-safe summary进入 task result，private/current-host evidence放：

`private/exports/056_product_delivery_discipline/`

不要把host secrets、tokens、private config正文上传。Bridge/Bobbio各自只提交其正常repo-safe source/test/docs；跨repo final manifest由AI_Skills task result记录commit/hash locator。

## 15. Stop conditions

立即回 `NEEDS_GPT_PLANNER` / 等价合法状态，而不是自行扩大范围：

- upstream source变化使W2 transport事实不再成立；
-需要新provider/credential/paid API；
-必须新增state machine/controller/watchers才能继续；
- exact repo/branch/worktree identity冲突且不能按frozen strategy安全解决；
- F-A/F-B/F-C需要改变已批准architecture而不只是实现；
- G1–G8暴露 v6 mechanism本身无法阻止原failure；
-任何需要修改当前明确 untouched product repo才能“做出PASS”的情况。
