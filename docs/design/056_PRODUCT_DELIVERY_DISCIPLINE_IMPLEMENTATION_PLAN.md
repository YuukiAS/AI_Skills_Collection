# 056 Product Delivery Discipline — Implementation Plan

- Execution package version: `v0.1`
- Task key: `056_product_delivery_discipline`
- Status: `READY_FOR_EXECUTION_CRITIC_REVIEW`
- Draft source ref: `AI_Skills_Collection main@415a839ec65589b3ebae3aa355b9028114b9a514`
- Bridge Kit source ref: `GPT_Codex_AI_Bridge_Kit main@cb77b1cc5a1fce097a38066d2db452291e359852`
- Bobbio source ref: `develop@0811116ac7197590f0af773f3c6296d4ca41db80`
- Architecture authority: `docs/design/PRODUCT_DELIVERY_DISCIPLINE_V6_PROPOSAL_2026-09-16.md`
- Post-probe authority: `docs/design/PRODUCT_DELIVERY_DISCIPLINE_V6_POST_PROBE_ADDENDUM_2026-09-17.md`
- Probe result: `docs/design/056_PERSISTENT_PROMPT_CAPABILITY_PROBE_RESULT_2026-09-17.md`
- CUHK Date evidence: `docs/design/PRODUCT_DELIVERY_DISCIPLINE_V6_CUHK_DATE_REAL_FEEDBACK_2026-09-17.md`
- Canonical Goal: `docs/goals/056_PRODUCT_DELIVERY_DISCIPLINE_GOAL.md` v0.1
- Kickoff Draft: `docs/operations/prompts/056_PRODUCT_DELIVERY_DISCIPLINE_KICKOFF.md` v0.1

本文件只把已经由独立 Critic 批准的 v6 架构收敛成可执行合同。它不重新设计 6 Lite / 5 workflow / 3 Frontend / 1 maintainer 架构，也不把当前 Critic PASS 当成执行授权。只有独立 Critic 对本 v0.1 Plan + Goal + Kickoff 同版给出 `READY_FOR_CODEX=YES`，且用户随后实际发送获批 Kickoff，才允许创建 task branch/worktree、修改 production source、修改 Host Policy 或启动 Executor。

## 1. 本轮新增的真实能力

通过 056 后，用户新增的不是更多文档，而是以下可观察行为：

1. 复杂/高风险任务不会把 agent 自己能解决的 repo/source/environment 问题转嫁给用户；真正 `HUMAN_ONLY` 的 Default-mode gate 使用 durable transcript wait/resume，未回答时 dependent execution 必须停住，但任务不是 terminal `BLOCKED`。
2. acceptance/release/user-ready handoff 在 frozen feature/milestone 尚未真正闭环时会被拒绝；advisory/diagnostic/design/architecture review 仍可轻量发生。
3. `workflow-core` 能区分 proxy/synthetic/helper 与真实 target surface，要求 faithful failure/regression、final-candidate identity、repeat-failure stop rule 和 should-not-change protection。
4. `Frontend Design` 形成三个真正的 production gates：Design Authority & State Coverage、Design-System Coherence、Actual-Surface Convergence；有 canonical Figma/design 时不能在 implementation 层随手发明缺失状态。
5. `AI Skills Maintainer` 遇到“规则已经写了但还是犯错”时先诊断 installed/source/generated/invocation/trigger/session/normal-entry consumption，而不是继续堆同义 policy。
6. Bridge Kit 的 Default host config fail-closed：不再向 Default mode 暴露会 auto-resolve 的 native `request_user_input`；Plan-mode native blocking question 不因该 Default-only flag 被禁用。
7. Lite Handoff 的项目模板只保留 6 条最基本交付底线，不把 Figma/icon/full-E2E 等专业 checklist 塞进所有项目。

## 2. 绝对不变的边界

本任务不新增 W6/W7、G9/G10、Control、watcher、ledger、daemon、第二套状态机、第二个 review engine 或新的顶级 plugin。不得 fork/patch Codex Desktop/CLI。不得调用 paid API/Terra。不得修改 Lucerna、Mica、Asteria、SeminarArc、CUHK Date、CARE、EAT、Server/VPS 的 production 或 AGENTS。

`scientific-visualization` 本轮只保留既有 TODO/evidence，不做 production change。Bobbio 只允许一项 repo-specific locator 修正：frontend/Product Design normal entry 增加当前 canonical `docs/design/FIGMA_HANDOFF.md`，不复制中央 Frontend Design checklist，不改产品代码、不 bump Bobbio app version。

普通 docs-only、backend-only、server-only、tiny nonvisual fix 不能因为 056 自动升级成 Figma/GPT Work/full E2E/native-smoke ceremony。

## 3. 执行时的 bounded Git/source strategy

本节只有在 execution-ready Critic PASS 且用户实际发送获批 Kickoff 后才生效。

### AI_Skills_Collection

- exact branch: `reviewed/056_product_delivery_discipline`
- base: kickoff 当时最新且包含本 execution package 的 `origin/main`
- preferred worktree: 从本机已验证 canonical checkout 建立 task-owned clean worktree，目录名固定为 `AI_Skills_Collection-056-product-delivery-discipline`，放在 canonical repo 的同级目录；不得先 network clone。
- 若该 exact branch/worktree 已存在且 identity 不明，停止并回 Planner，不自行换 branch 名或编号。

### GPT_Codex_AI_Bridge_Kit

- exact branch: `reviewed/056_product_delivery_discipline`
- base: kickoff 当时最新 `origin/main`
- preferred worktree: 从本机已验证 canonical checkout 建立 task-owned clean worktree，目录名固定为 `GPT_Codex_AI_Bridge_Kit-056-product-delivery-discipline`，放在 canonical repo 的同级目录；不得先 network clone。
- unrelated dirty state 留在原 canonical checkout，不 stash/reset/restore；dirty 不等于放弃本地 canonical source。

### Bobbio

- exact integration branch: current `develop`
- 不新建 Bobbio task branch/worktree；这是一个单行级 locator/入口修正，遵守 Bobbio 当前 normal development policy。
- 只有中央 candidate 已通过本地实现/回归 gates 后才修改 Bobbio；如果 `AGENTS.md` 本身有用户未提交修改或 `develop` 不能安全 fast-forward，则只暂停 Bobbio locator 子步骤并回 Planner，不 clone/remap remote 绕过。

### Source Discovery hard rule

每个 repo 先找 existing canonical checkout/worktree/clone，再核 repo identity、branch/ref、origin、freshness、dirty ownership。必要且已授权时 fetch 当前 remote；local-first 不等于相信 stale checkout。只有本机确无可用 source 才允许 network clone。禁止 `local clone -> git remote set-url` 作为正常隔离路径；remote mutation 仍是独立授权边界。

## 4. Phase 0 — Preflight 与 baseline

Executor 先读取三 repo 当前 rules/version/changelog/tests，并记录：

- exact source refs；
- current installed AI_Skills plugin identities/versions；
- current installed Bridge Kit version；
- current `$CODEX_HOME` identity、managed Host Policy state 与 config backup eligibility；
- `workflow-core 0.1`、`web-development 0.1`、`ai-skills-core 0.2` 当前 production replay baseline；
- Bridge Kit 当前 `0.8.2` host behavior；
- Bobbio current `develop` AGENTS locator state。

冻结一组 public-safe baseline scenarios，覆盖 G1–G8 和 source-discovery regression。baseline 用于 before/after 归因，但旧版本 PASS 不能拼给 final candidate。

## 5. Phase 1 — Bridge Kit：Lite + Default HUMAN_ONLY transport

### 5.1 Host config fail-closed

修改 `ai_bridge_kit/host.py`：

```toml
[features]
default_mode_request_user_input = false
memories = true
```

不是删除 key，而是显式 managed false。

同时修正 `_feature_availability()` / `validate_host_policy()` 的语义：

- **upstream key/capability 是否存在** 与 **Bridge desired enabled state** 分开；
- `default_mode_request_user_input` 存在但 disabled，且 managed expectation=false => 正常 `configured`；
- stale `true` => config drift；
- `memories` 仍按 desired enabled=true 校验；
- upstream key 完全消失时不得把“desired false”偷换成已验证兼容：保持清楚的 unsupported/incompatible 诊断，等未来新 upstream evidence/re-probe；
- 不改变 unrelated feature config。

### 5.2 Host user-input contract

更新 `templates/host/GLOBAL_AGENTS_SNIPPET.md`：

Default-mode `HUMAN_ONLY` 必须：

```text
preserve current resume point
-> one concise plain-text user question
-> stop all dependent execution
-> no answer: no dependent work / polling / default inference / auto retry / timeout-continue
-> DEPENDENT_EXECUTION_BLOCKED=YES
-> TERMINAL_BLOCKED=NO
-> same-thread explicit answer
-> reread current task/resume point
-> validate answer against frozen scope
-> exact-once resume
-> post-action integration closure
```

不得再写 “Because host policy enables default_mode_request_user_input”。Default native question card 不用于 HUMAN_ONLY。Plan-mode合法 native `request_user_input` 仍由 upstream Plan semantics 拥有，不由 Bridge Kit重实现。

### 5.3 Lite Handoff 6 条 baseline

更新 canonical `templates/prompts/AGENT_RULES.md`，只加入 v6 六条短底线：

- L1 positive goal / normal entry / no silent downgrade；
- L2 acceptance Review Admission + human action != acceptance；
- L3 foreseeable human gate + eligibility + visible transcript question + resume point；
- L4 faithful validation + evidence-surface + final-candidate identity；
- L5 no blind rerun + protect accepted/adjacent behavior；
- L6 truthful handoff + unverified boundary + resume point。

不把 Figma/icon/motion/provider/locale/full-suite checklist 写进 Lite。

### 5.4 Bridge tests

至少补/修 `tests/test_host_policy.py`：

- fresh install 写 `default_mode_request_user_input=false`；
- merge/idempotency；
- existing unrelated `[features]` preserved；
- stale true -> drift；
- feature key supported + actual disabled + desired false -> `host validate` PASS；
- missing upstream key 仍 truthful incompatible/unsupported；
- `memories=true` 等其他 managed expectations 不回归；
- generated Host AGENTS 包含 durable transcript semantics，不再声称 Default native tool enabled。

补 Lite template/install regression：由 canonical installer/template 生成的项目 `prompts/AGENT_RULES.md` 真正包含 6 条 baseline，且不带 Frontend checklist。不要靠只检查一个关键词代表能力完成。

### 5.5 Bridge release closure

本变更是兼容 Host Policy/Lite behavior fix：若 gates 全通过，Bridge Kit target release 为 `0.8.3`。同步 `__version__`、`CHANGELOG.md`、README current version/0.8.2/0.8.3 说明和当前配置文档。历史 0.4/旧 design 文档保持历史，不为改当前默认值篡改旧版本记录。

## 6. Phase 2 — AI_Skills：三类中央 plugin production refinement

本阶段必须按 `workflow-core + ai-skills-core + target domain plugin` 的 maintenance companion 规则 source-first 修改，再生成 Marketplace payload。

### 6.1 Verified Workflow / workflow-core

修改 source authority：

- `skills/core/codex-system/codex-workflow-protocol/SKILL.md`
- `references/task-template.md`
- `references/verification-matrix.md`
- `references/live-state-delegation.md`
- `references/escalation-rules.md`

不新增新顶级 skill/state/schema。把 v6 五个 capability 接入现有流程：

**W1 Acceptance Review Admission + Vertical/Post-action Closure**

只 hard-gate acceptance/release/user-ready review。advisory/diagnostic/design/architecture review 可以提前发生，但不能输出 readiness/completion。`complete` 只相对 frozen feature/milestone/review object。

Vertical closure 是“适用项 closure”，不是所有任务机械全选。对高风险/多 deliverable Goal 可使用 task-local closure table；普通小任务不要求。

CUHK Date evidence并入 W1：breadth claim -> representative corpus/known items；material branches -> small branch coverage；locale claim -> reachable finite-value coverage；persisted/setup/upload state 在风险相关时验证 action -> visible result -> navigation -> refresh/re-entry -> authoritative state。fallback/recovery 只证明 recoverability，除非 Goal 明确接受为等价，否则不能证明 primary capability complete。

**W2 Human Decision Gate Semantics**

先分类：`HUMAN_ONLY / AGENT_RESOLVABLE / UNSUPPORTED_WITH_EVIDENCE / OPTIONAL_NOT_REQUIRED_FOR_CURRENT_CLOSURE / SAFETY_OR_AUTHORITY_BLOCKER`。只有 `HUMAN_ONLY` 进入普通 Human Gate。Default transport 固定为 `DURABLE_TRANSCRIPT_WAIT_RESUME`；不再用 Default native `request_user_input`。

**W3 Exact Failure / Verification / Evidence Fidelity**

要求 focused failure evidence、claim scope <= evidence scope、同 final candidate。external/provider claim 的 mock test只证明 adapter；hosted claim需要安全 bounded configured-target evidence。controlled input intermediate state 会被转换时，验证 type/paste/backspace-replace/blur-commit 等真实 sequence。source count/type support 不代替 product-entry branch replay。

**W4 Repeat-failure Circuit Breaker + Human-time Budget**

相同症状再次出现、tests 绿但 real path又失败、同一 user/reviewer 再指出同类问题或 active rule 再次失效时，在下一次 full suite/GPT Work/human QA 前先核 candidate identity、hypothesis、fixture fidelity、consumer loading、evidence surface/root cause；无新信息不重复昂贵/人工 rerun。

**W5 Change-impact / Should-not-change**

修 shared runtime/state/UI 时保护已接受/邻近行为；rewrite/refactor 不得未经产品决策把已接受 structured interaction 降级成 generic/free-text fallback。

**Source Discovery refinement（不是 W6）**

将“existing canonical local repo + unrelated dirty work”场景写入既有 source discovery：先找 local source、核 identity/origin/freshness/ownership；dirty 保护但不自动放弃 repo；隔离优先已存在正确 clone/worktree或经授权的 canonical worktree；无本地 source 才 network clone；不 remap remote 作为普通路径。

保持原 trigger boundary：简单 docs/wording/单命令/小范围普通任务不会只因 056 而触发重 workflow。

### 6.2 Frontend Design / web-development

实现三个 production gate，不新增第二套视觉 checklist：

**F-A Design Authority & State Coverage**

有 canonical Figma/design source 时必须读取。material production state/variant/responsive/interaction 缺失 -> 先更新 design source 并自审/freeze，再实现；design正确而实现偏离 -> 只修 implementation；平台/accessibility必要偏差显式记录；没有 canonical Figma 的项目不强制创建 Figma。

**F-B Design-System Coherence**

同一 product surface 使用 coherent shared components/tokens/states、layout/typography/spacing/radius/surface、统一 icon family、brand-vs-generic asset边界、interaction feedback、motion grammar、reduced-motion/accessibility。generic icon 优先项目既有或成熟 library；custom icon仅 product identity/domain-specific/genuine gap。不得规定 Lucide/Fluent 为全球唯一库，不要求每个 icon 动画，不要求小项目强造 central registry。

Locale claim并入 F-B/F-C：supported locale 的 finite reachable enum/token 完整本地化；internal enum identifier 不得成为 production fallback；proper noun/acronym仅 narrow allowlist。

**F-C Actual-Surface Convergence**

在真实 target surface 看 whole product并与 canonical design 比较；risk-scaled visual/interaction regression；producer 清掉 obvious must-fix 后才进入 external acceptance review；screenshot 不冒充 click/native/live behavior。

当前 production `web-development` payload 的 visual aggregate只包含 `frontend-visual-systems + visual-direction + design-system-tokens`。为让 F-A/F-B 真正进入 **Frontend Design plugin normal entry**，实施时应把现有 `figma-design-to-code` 与 `motion-interaction` source skill 接入该 aggregate（或同一 plugin 的等价生成入口），而不是只修改未被 plugin 消费的 source 文件。修改 `scripts/codex_marketplace_config.json` 后通过官方生成脚本更新 payload；不得手改 `plugins/codex/plugins/`。

### 6.3 AI Skills Maintainer / ai-skills-core

修改 `skills/core/codex-system/ai-skills-repository-maintainer/SKILL.md`：已有 active rule 仍失败时，先做 production consumption diagnosis：installed version、source/generated parity、plugin invocation、trigger、task entry、session loading、normal-entry replay，并区分 rule missing / not invoked / old install / execution noncompliance / conflict / capability gap。读取 source `SKILL.md` 不算 production invocation。

真实 replay 必须能暴露“active source rule存在，但 installed/generated/session consumer 未消费”的案例；不得用新增 TODO 字符串作为行为 PASS。

### 6.4 TODO 去重与 release metadata

只有当 final candidate 通过原失败 replay + unrelated regression，才把本轮相关 TODO 提升/合并：

- `workflow-core`：将 056 条目收敛为已推广的 5-capability behavior，不保留旧 native-persistent 假设；
- `web-development`：把已有 icon/Figma/design-to-code/whole-screen/self-review/motion 等重复候选合并到 F-A/F-B/F-C，避免十几条同义 open TODO；
- `ai-skills-core`：将 production consumption diagnosis 候选推广；
- `scientific-visualization` 不因本任务改变 production/status。

Target release（仅 gates 全部通过时）：

```text
Repository bump decision: PATCH
AI_Skills_Collection: 5.0.4 -> 5.0.5
workflow-core: 0.1 -> 0.2
web-development: 0.1 -> 0.2
ai-skills-core: 0.2 -> 0.3
其他中央 plugins: unchanged
```

理由：三个既有 plugin 获得 compatible user-visible workflow/quality/maintenance refinement，没有新增 repository-level plugin/workflow，不构成 repo minor。同步三个 plugin changelog、root CHANGELOG、VERSION/setup/registry/README dashboard 与 Marketplace config；版本在 final candidate freeze 前完成 exactly once。

## 7. Phase 3 — Bobbio 最小 repo-specific locator

只修改 `Bobbio/AGENTS.md` frontend/Product Design read-list：在现有 `docs/PRODUCT_DESIGN_BRIEF.md` 前后明确加入：

`docs/design/FIGMA_HANDOFF.md`（current canonical visual design source）

并保留 active milestone requirement。不得复制 F-A/F-B/F-C checklist，不改 Figma、不改 product code、不改 runtime version。

这项修改用于修复 normal-entry locator 缺口；Bobbio 已有 native self-QA -> GPT Work -> user acceptance，不新增同义 review policy。

## 8. Phase 4 — Mechanical/source/generated verification

AI_Skills 先跑窄 tests，再完整 canonical validation：registry/catalog/Marketplace generation/validate/audit/unittest。确认 generated `workflow-core 0.2`、`web-development 0.2`、`ai-skills-core 0.3` 与 source/config/changelog一致；确认 `web-development` production payload实际含 Figma + motion source，而不是 source-only phantom capability。

Bridge Kit 跑 host-policy/Lite相关 focused tests，再 full unit suite。确认 `0.8.3` metadata/docs/tests一致。

任何 mechanical PASS 只证明机械性质，不能替代下一阶段 G1–G8 production replay。

## 9. Phase 5 — Final-candidate freeze 与 G1–G8 normal-entry gates

在所有 production source、generated payload、versions/changelogs、Bridge release metadata稳定后冻结一个 cross-repo candidate tuple：

```text
AI_SKILLS_FINAL_CANDIDATE_COMMIT=<sha>
AI_SKILLS_GENERATED_PLUGIN_HASHES=<workflow/web/maint hashes>
BRIDGE_FINAL_CANDIDATE_COMMIT=<sha>
BRIDGE_VERSION=0.8.3
BOBBIO_LOCATOR_COMMIT=<sha or PENDING until central gates pass>
CODEX_HOST_IDENTITY=<current exact identity>
HOST_CONFIG_PRE_CHANGE_BACKUP=<path/hash>
HOST_CONFIG_FINAL_HASH=<hash after bounded install>
```

所有 release-critical behavior evidence 必须来自这个 tuple；任何 post-freeze production source/generated/version/contract修复都使相关 PASS失效，重新 freeze并重跑受影响 gates。

### G1 — Human-gate recognition / transport

同 final candidate 至少验证：

- `AGENT_RESOLVABLE` local repo/source/environment issue -> Executor自行解决，不 prompt用户；
- `UNSUPPORTED_WITH_EVIDENCE` -> truthful close，不让用户“配置一下试试”；
- genuine `HUMAN_ONLY` -> Default mode发一条 plain-text question，不出现 native auto-resolving card；
- 用户未回答期间 dependent work不继续、不完成、不 polling/retry；
- 用户明确回答后重读 resume point并 exact-once resume；
- post-action integration closure由 Executor继续完成。

最终 HUMAN_ONLY normal-entry smoke放在所有非人工 gates完成之后，避免用户成为开发 debugger。Executor届时只请求一次固定、安全、无 secret 的回复，例如 `W2_RESUME_056_FINAL`，并在收到前停止 dependent step。

同时在 current host上证明：managed `default_mode_request_user_input=false`；fresh Default session不暴露该 optional tool；Plan session仍具有合法 `request_user_input` capability（至少 current tool availability/normal Plan entry不因 Default-only flag消失）。不得通过改 Codex source让测试通过。

### G2 — Acceptance Admission

production workflow replay必须区分 acceptance vs advisory review。至少：

- incomplete producer evidence -> `READY_FOR_USER_REVIEW=NO`；
- advisory/diagnostic review允许在 incomplete candidate 上发生，但不输出 readiness；
- CUHK-Date-like candidate即使 broad tests PASS，只要仍有 demo breadth、missing material branch、raw internal token、mock-only hosted provider、interaction sequence bug、fallback-only primary capability或hosted config未消费backend capability -> acceptance denied。

### G3 — Resume/post-action closure

G1 用户回复后，同一 Goal/session恢复且只恢复一次；human action本身不计 feature completion；Executor完成该动作相关的 integration closure后才允许后续 acceptance claim。

### G4 — Faithful regression

至少覆盖：

- old/bad真实或忠实 sequence FAIL，new final candidate PASS；
- controlled input final-value 绿但 `1 -> 17 -> 178`/paste/backspace/blur sequence坏时必须 FAIL；
- mock provider pass但configured target capability不存在时 hosted claim必须 FAIL。

不要求所有任务都跑这些场景；它们是冻结 056 capability replay fixtures。

### G5 — Evidence / final-candidate identity

unit/synthetic/browser/helper/screenshot只支持对应 surface；关键 PASS来自同一 final candidate tuple。旧 candidate证据不能拼装。fallback只证明recoverability，除非 Goal明确接受等价。

### G6 — Frontend design consumption

使用一个有 canonical Figma/design source 的真实 normal UI planning/implementation-handoff task（优先 Bobbio current design authority作为 read-only source），证明 Frontend Design production plugin实际定位并消费 `FIGMA_HANDOFF`/design source；material missing state要求先回 design source，而不是 implementation随手加圆/按钮/状态；design正确时只修 implementation。actual-surface/whole-product quality由风险匹配 evidence支持。

不要求本 gate修改 Bobbio Figma或product code。

### G7 — Non-overreach

至少三个小型 negative controls：docs-only、backend/server-only、tiny nonvisual fix。它们不得被强制要求 Figma、locale/catalog/provider matrix、GPT Work、full E2E或native UI smoke。

### G8 — Consumption-regression diagnosis

使用 public-safe fixture证明：active rule/source存在，但 installed/generated/session/trigger/task entry没有消费时，`AI Skills Maintainer`首先报告 consumption regression并定位层级，不新增同义 rule；正常已消费场景不产生额外长篇 policy复盘。

### Existing Source Discovery regression（不新增 G 编号）

本地 fixture创建：existing canonical local repo + unrelated dirty file + clean task surface need。期望 dirty保留、发现正确 local source、只使用已授权 reuse/worktree策略、无 redundant network clone、无 remote remap。

## 10. Phase 6 — Bounded current-host installation smoke

只有 Bridge candidate tests 与 AI_Skills source/generated gates 都绿后，才允许按 Kickoff 的 exact authorization：

1. 备份当前 `$CODEX_HOME` managed files；
2. 使用 task-owned Bridge `0.8.3` candidate在**probe 同一 Windows Codex identity**执行 bounded `ai-bridge host install` / `validate`；
3. 验证 config从 stale/old true收敛为 explicit false、unrelated config保留；
4. 安装/升级 task-owned AI_Skills candidate plugins，启动 fresh session，验证 production invocation；
5. 执行 G1–G8 final replay。

如果当前 executor不是 probe 所用的 Windows Codex identity，或无法可靠确认 `$CODEX_HOME` identity，不能把另一台机器的 host smoke冒充本 gate；先完成其余 independent work并停在明确 HUMAN/ENVIRONMENT boundary。

## 11. Should-not-change

至少保护：

- Bridge Kit只有 Lite/Review/Control三档；Persistent Run仍不是第四 workflow；
- Plan-mode native request_user_input不因 Default flag关闭而被 Bridge禁用；
- Host Policy其他 approved feature/rules/Slurm/process/tmux/Git安全边界不变；
- AI_Skills `workflow-core` trigger boundary不扩到所有小任务；
- Frontend Design不强制所有项目有Figma，不固定唯一icon library，不强制所有icon动画，不强制小项目建registry；
- Research/scientific domain判断仍由对应domain plugin拥有；
- Bobbio existing native self-QA/GPT Work/user acceptance和Zotero安全规则不改；
- Lucerna/Mica/Asteria/SeminarArc/CUHK Date product repo不被056修改；
- no paid API / no Terra。

## 12. Rollback / recovery

### Bridge host rollback

`ai-bridge host install`必须保留 pre-change backup。若 current-host smoke暴露 host config regression：

- 停止 release/integration；
- 恢复该次 install 创建的 exact backup，不手工猜 config；
- 保留 candidate branch/evidence；
- 不自动把 flag设回 true并宣称解决；回 Planner/Critic归因。

### AI_Skills rollback

Task branch在 main integration前独立。若 plugin replay失败，保留 old/current released plugin安装身份与失败 evidence，重新安装/恢复 baseline released payload；不得通过放宽 acceptance或删除 failing fixture制造 PASS。

### Bobbio

Bobbio locator只在中央 candidate已内部通过后写入 `develop`；若相关 source在执行期间发生冲突，停止该子步骤，不 remap/clone/overwrite用户 work。

## 13. Release / integration identity

本 Goal 的“实现完成”不等于最终主分支发布。Executor必须把 exact final candidate commits、generated hashes、host config backup/hash和G1–G8证据写入 task result，并 commit/push exact authorized task branches；随后交独立 Reviewer/Critic做 implementation audit。

只有 implementation audit对 exact tuple PASS、无 production source/generated/version变化后，才可按后续已批准 integration step将 AI_Skills/Bridge candidate集成到 main并发布对应版本。当前 Kickoff不把 architecture Critic PASS冒充 implementation audit，也不允许 Executor自审后直接宣布整个056 achieved。

## 14. 本轮外部研究记录

本 execution-package drafting round 重新核对：

- current `openai/codex` Default collaboration instructions：Default下真正 required user input应直接 plain-text问用户，而不是使用 optional `request_user_input`；
- current upstream issue #43759 / #37472：Default native question仍缺 always-wait/no-timeout；
- OpenAI `Harness engineering: leveraging Codex in an agent-first world`：human time/attention是稀缺资源，短 AGENTS作为地图、agent自测/应用可观测性优先于把明显问题推给人；
- Figma Dev Mode Ready for dev：handoff本身可迭代，Ready/Completed状态与具体design source应可定位；支持 F-A“先收敛设计再实现”，但不要求所有项目使用Figma；
- Microsoft/平台 motion实践继续支持“有意义的交互反馈+reduced motion”，而不是所有icon强制动画。

采用这些作为现有 v6 机制的现实校验，不新增依赖或新控制体系。
