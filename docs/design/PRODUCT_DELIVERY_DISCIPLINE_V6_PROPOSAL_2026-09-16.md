# Product Delivery Discipline v6 — Planner Proposal

状态：`DRAFT_FOR_CRITIC_REVIEW`  
日期：2026-09-16  
任务：`056_product_delivery_discipline`  
基线：`main@efd6896a97977158e4641c662e5830c0088ed2b8`  
替代关系：本提案替代 v5 作为 056 当前 Planner review object。它只收敛架构，不修改 production skill/plugin、Bridge Kit production、产品 AGENTS，不创建 execution Goal/Kickoff/branch，不运行 capability probe。

## 1. 结论与 v5 → v6 修订摘要

Critic 第一轮 `REVISE` 的方向成立。v6 不继续扩张 v5 的十条顶级机制，而采用更小的中央架构：

```text
Lite baseline       6 条
workflow-core       5 个 capability
Frontend Design     3 个 production gate
AI Skills Maintainer 1 个 consumption-diagnosis capability
Bridge Kit          只负责 user-input transport / wait-resume / recoverability
repo AGENTS         只保留项目独有 invariant / locator
```

同时吸收 2026-09-15 Lucerna Goal 01035 的新证据：v5 只规定了“怎样进入 Human Gate”，仍不足以阻止 Executor 把自己能够解决的工程依赖包装成用户动作。v6 因此不新增第六个 workflow capability，而把三个新机制分别嵌入现有 capability：

1. **Human-Gate Eligibility / Dependency Triage** → W2 Human Decision Gate；
2. **Vertical Capability Closure** → W1 Acceptance Review Admission + W3 verification；
3. **轻量 Goal Coverage Table** → 仅高风险/多 deliverable Goal 的 W1/W2 evidence shape，不是持久 ledger、schema 或新状态机。

另一个关键修正是：**persistent blocking prompt 不再被当作已验证能力。** 当前公开 Codex source 明确表明 Default-mode `request_user_input` 被转发为 `is_blocking=false`；当前 Default-mode instruction 还要求真正必须用户回答时使用简短 plain-text question，而不是依赖 `request_user_input`。近期公开 issue 又报告 Default-mode prompt 可能在约 1–2 分钟后自动 resolve。Bridge Kit 当前只验证 feature flag 存在/启用，没有验证 Desktop/App 的 no-expiry、exact-once resume。因此 transport 状态改为 `PROBE_REQUIRED`。

## 2. 本轮实际核对的事实

### 2.1 AI_Skills / Bridge Kit

重新读取了最新 main 的 Planner/Critic contracts、Capability Gate Policy、AGENTS、v5、workflow/frontend/maintainer/scientific-visualization TODO，以及 workflow task template、verification/live-state references、Figma/design-system/visual/motion skills。

Bridge Kit `main@cc7a6a3ea7a95d15d253821c50f2beda9bf221f9` 当前能直接证明：

- host config 管理 `features.default_mode_request_user_input = true`；
- host policy 规定 recoverable user question 不应直接成为 terminal `BLOCKED`；
- external waiting 不应消费 review/repair/retry budget。

它**不能直接证明** Default-mode prompt 在 Desktop/App 中 indefinitely pending、不会被 client auto-resolve、或回答后能 exact-once resume。`tests/test_host_policy.py` 目前验证的是配置合并/安装，而非真实 prompt 生命周期。

### 2.2 当前 Codex source / public evidence

本轮重新核对 `openai/codex` 当前公开 source：

- `codex-rs/features/src/lib.rs` 把 `default_mode_request_user_input` 标为 under-development feature；
- `codex-rs/app-server/tests/suite/v2/request_user_input.rs` 明确测试：Plan mode `is_blocking=true`，Default mode（feature enabled）`is_blocking=false`，两者 server request 的 `auto_resolution_ms=None`；
- 当前 `codex-rs/collaboration-mode-templates/templates/default.md` 明确要求 Default mode 中 `request_user_input` 只用于 optional question；真正必须用户输入才能继续时，应直接问一条简短 plain-text question；
- `openai/codex` issue #37472、#43759、#34455 报告 Default/Desktop/CLI 中未回答 question 可能在约 1–2 分钟后自动 resolve / submit empty answer，并请求 no-timeout blocking control。

因此 `auto_resolution_ms=None` 只能说明 server request 没携带该字段，**不能证明当前 Desktop client 没有自己的 auto-resolution 行为**。需要本机真实 probe。

### 2.3 Lucerna 01033 / 01034 / 01035

Lucerna 当前 `AGENTS.md` 已经明确要求：user-visible feature/fix 有 matching regression、provider 使用真实数据、不能 second manual refresh、normal live UI 不得用 fixture/mock、Windows release interaction 要实际验证。

01033/01034 的 result 也确实运行了大量 OpenAI targeted/backend/build/live-route checks，但真实 credential sequence 仍在用户操作后暴露 stale `Not set up` / validation-state 问题。这更像 **faithful sequence / release-path enforcement 不足**，不是缺一段相同 AGENTS 文案。

01035 提供了更强的 workflow 证据：task 本身已经明确“finish all non-human work before asking for any user input”，并授权读取/必要时修改 Longleaf_Bridge、读取 Zotero mirror oracle；但结果仍把这些内容聚合进 Human Boundary：

- local Longleaf_Bridge checkout ownership / 缺文件没有先用已授权 remote/canonical source 解决；
- `Zotero_Koofr_GPT_Mirror` 本地没找到，被呈现为 `Needs setup`，尽管 task 已授权读取远端 oracle；
- VS Code/Cursor 已调查到 `UNAVAILABLE_WITH_SUPPORTED_INTERFACES`，仍被列入可选 human intake；
- `SEVEN_PATH_LIFECYCLE_UI=IMPLEMENTED_WHEN_CONTRACT_PROVIDES_LIFECYCLE`、`LONGLEAF_RECOVERY_EXTENSION=IMPLEMENTED_READ_ONLY_NEEDS_BOUNDED_ACTION_CONTRACT`、Overleaf/Zotero `NEEDS_SETUP` 等 scaffold/条件式结果与 broad test PASS 同时存在；
- task 明确禁止 optional credential 变 global BLOCKED，但 result 仍以 `NEEDS_HUMAN_ACTION` 聚合多个并非 HUMAN_ONLY 的依赖。

这说明 Human Gate 前必须先做 dependency triage 与 deliverable closure accounting。

### 2.4 Bobbio / Mica / Asteria / SeminarArc

- **Bobbio develop** 已有 pre-user pipeline：deterministic tests → native Windows self-QA → UI/copy polish → GPT Work → repair P1/P2 → user acceptance。`docs/design/FIGMA_HANDOFF.md` 已明确 Figma 是 production visual source；但当前 `AGENTS.md` 的 frontend/Product Design read-list 只列 `PRODUCT_DESIGN_BRIEF.md` 与概念图，没有列 `FIGMA_HANDOFF.md`，所以 normal-entry consumption 仍有 locator 缺口。
- **Mica main** 已有 reproduce-real-failure、bounded diagnostic UX、improve synthetic fixture、focused-before-full-E2E、one-short-manual-loop 和真实站点最终手动 acceptance 等规则。默认不再复制一条同义 replay 规则；应先验证历史/当前 task 是否真的消费这些规则、fixture 是否忠实。
- **Asteria main** 已有 developer visual self-QA、generic-fix、canonical scientific graph visual system 和 GPT Work-before-human gate；当前 source 已足够强，下一步应验证 normal task entry 的 consumption，而不是再加 visual policy。
- **SeminarArc main** 当前 AGENTS 与 code search 没有找到项目级 canonical Figma file/locator。repo 中存在 generic Compose/Figma skill reference 不能证明项目有 canonical Figma source；保持 `EVIDENCE_NEEDED`。

## 3. Critic blocker 响应矩阵

Planner 不自行宣布 blocker closed；以下只是待 Critic 复核的响应。

| Blocker | Planner response | 当前状态 |
|---|---|---|
| `C056-B1-PERSISTENT-PROMPT-CAPABILITY` | R4 transport 改为 `PROBE_REQUIRED`；定义独立、无生产副作用的 host probe；native fail 时只允许 durable transcript question + suspend + resume point，不冒充 native prompt | `RESPONDED_PENDING_CRITIC; PROBE_REQUIRED` |
| `C056-B2-REVIEW-ADMISSION-SCOPE` | Review Admission 只硬 gate acceptance/release/user-ready review；advisory/diagnostic/design/architecture review 可在未完成 candidate 上进行，但不得输出 readiness/completion；complete 只相对 frozen review object | `RESPONDED_PENDING_CRITIC` |
| `C056-B3-ACTIVE-RULE-CONSUMPTION` | 建立 Lucerna/Bobbio/Mica/Asteria consumption matrix；已有 active rule 默认查 normal-entry consumption / fidelity / enforcement，不再先加同义 AGENTS | `RESPONDED_PENDING_CRITIC` |
| `C056-B4-LAYER-DUPLICATION` | 收敛为 6 Lite + 5 workflow + 3 Frontend + 1 maintainer capability；Bridge/repo 只保留边界职责 | `RESPONDED_PENDING_CRITIC` |

## 4. 两类 Review：只对 Acceptance Review 设硬 gate

### 4.1 Acceptance / release / user-ready review

目标是支持类似以下 claim：

- `READY_FOR_USER_REVIEW=YES`；
- release / RC ready；
- milestone complete；
- GPT Work acceptance candidate；
- 用户可以开始最终验收。

这类 review 才受 W1 Review Admission 硬 gate。`complete` 的范围永远是当前 frozen feature / milestone / review object，不自动扩大到整个长期产品。

### 4.2 Advisory / diagnostic / design / architecture review

可以在 candidate 未完成时发生，用于：

- 方案攻击；
- 设计方向评审；
- debug / evidence interpretation；
- prototype feedback；
- architecture alternatives；
- early qualitative consultation。

它不要求 feature complete，也不需要强制 Figma/GPT Work/full E2E/native smoke；但它**不能产出** user-ready、release-ready、product-complete 等 acceptance claim。

这样保留早期高价值审查，同时避免把每个小任务都升级成 release ceremony。

## 5. 最小充分架构

### 5.1 Lite baseline：6 条

Lite 是所有项目的短底线，不复制专业 checklist。

**L1 — Positive goal / normal entry / no silent downgrade**  
保持当前 frozen objective、normal entry、candidate identity 与不可替代条件；proxy/fallback 只有被明确批准为等价时才可替代原目标。

**L2 — Acceptance Review Admission + human action ≠ acceptance**  
只有 acceptance/release/user-ready handoff 需要 review admission。中途 credential/login/OS permission 等 Human Action 只是 execution checkpoint，不是 acceptance，也不能把半成品变成 user-ready candidate。

**L3 — Foreseeable human gate + eligibility + visible request + resume point**  
Goal 可预见 human gate 时先分类依赖；只有 irreducible `HUMAN_ONLY` 才允许询问。到点必须有明确可见 request 与 resume point。native persistent transport 是否可用由 probe 决定；未验证前不得宣称已有 persistent prompt。

**L4 — Faithful validation + evidence surface + final candidate identity**  
feature/change/fix 使用风险匹配验证；claim 不超过 evidence surface；关键 acceptance evidence 来自同一 final candidate。

**L5 — No blind rerun + protect accepted/adjacent behavior**  
同类失败无新信息时停止重复 full-suite/external/human QA；先重诊断。修改共享机制时保护已接受行为和邻近受影响能力。

**L6 — Truthful handoff / unverified boundary / resume point**  
明确区分 complete、partial、unsupported、waiting、unverified；给出真实恢复点，不用过程字段冒充产品完成。

Lite 不包含 Figma、icon、motion、具体 test suite、native/browser checklist。

### 5.2 workflow-core：5 个 capability

已有 source discovery、goal fidelity、domain routing、risk-scaled verification、final report/status 继续沿用，不重新包装成“新能力”。

#### W1 — Acceptance Review Admission + Vertical Closure + Post-action Closure

仅对 acceptance/release/user-ready review 生效。进入 admission 前，当前 frozen feature/milestone 必须有直接证据证明适用的 end-to-end chain 已闭环：

```text
authoritative source / contract
-> backend/runtime
-> persistence/state（若适用）
-> normal product entry
-> real target behavior
-> failure/recovery semantics
-> targeted regression
-> actual-surface confirmation（风险需要时）
```

`UI shell`、handler、placeholder、setup surface、schema field、fixture、条件式 `IMPLEMENTED_WHEN_*` 都不能单独算 capability complete。

Human Action 后，Executor 自动继续当前 Goal，完成与该动作相关的 integration closure；只有新的 candidate 重新满足 admission，才允许进入 acceptance review。

对于高风险或多 deliverable Goal，在 Human Gate 或 Acceptance Admission 前生成一张**轻量 closure table**：

| User deliverable | Disposition | Direct evidence | Human-only dependency? |
|---|---|---|---|
| item | COMPLETE / INCOMPLETE / UNSUPPORTED_WITH_EVIDENCE / OPTIONAL | evidence | YES / NO |

存在 `INCOMPLETE + Human-only=NO` 时，不允许把该依赖转给用户，也不允许声称 acceptance-ready。这张表是 task-local evidence，不是 repository-wide ledger/schema/state machine；普通小任务不要求生成。

#### W2 — Human Decision Gate Semantics

在任何 user-input request 前做 dependency triage：

- `HUMAN_ONLY`：用户独有 secret、网页登录、OS permission、物理设备动作、真正不可代理的产品决定；
- `AGENT_RESOLVABLE`：代码、repo/remote source、clone/sync、环境、测试、配置生成、diagnostics、已授权 source 读取；Executor 自己解决；
- `UNSUPPORTED_WITH_EVIDENCE`：当前受支持接口不存在；truthful limitation，不能让用户“配置一下试试”；
- `OPTIONAL_NOT_REQUIRED_FOR_CURRENT_CLOSURE`：可选增强，不阻塞当前 frozen objective；
- `SAFETY_OR_AUTHORITY_BLOCKER`：继续会越权、破坏数据或需要新战略决定；使用现有 STOP/Planner/approval 语义。

只有 `HUMAN_ONLY` 可以进入 Human Gate。

Goal authoring 若能预见 HUMAN_ONLY gate，只需在现有 Human Decision section 记录最小语义：trigger、one action、reply/unblock condition、safety note（若需要）、resume point、post-action agent work。**不新增固定 schema 字段泥潭。**

Transport adapter 本轮状态：`PROBE_REQUIRED`。Bridge Kit 只负责暴露/验证 host transport，不拥有 eligibility 或 Review Admission。

#### W3 — Exact Failure / Verification / Evidence Fidelity

合并 v5 的 exact-failure 与 evidence-surface：

- deterministic bug 优先 `old-bad FAIL -> new-good PASS`；
- live/native 无法全自动时保留真实 failure capture + faithful replay + 必要 actual-surface smoke；
- broad suite 不能替代原投诉；
- unit/synthetic/browser/screenshot/helper/native/live 各自只证明自身 surface；
- critical acceptance PASS 来自同一 final candidate。

01033/01034 的关键 lesson 是 sequence fidelity：分别验证 backend、UI handler、route 和 build，仍不能替代 `credential submit -> validation -> active state -> provider refresh -> normal UI` 的真实闭环。

#### W4 — Repeat-failure Circuit Breaker + Human-time Budget

相同症状再次出现、tests 绿但 real path 再失败、同类缺陷再次由 user/reviewer 发现、或 active rule 再次被违反时，不继续无信息 full suite / Atlas / GPT Work / human retry。

下一次高成本或真人重试前必须出现至少一种新信息：new hypothesis、faithful fixture、root-cause repair、candidate correction、rule-loading evidence 或 environment explanation。人的时间不是 debug loop budget。

#### W5 — Change-impact / Should-not-change

修改共享行为前识别受影响的 accepted behavior / adjacent capabilities，并做风险匹配回归。视觉系统的一致性细节交 Frontend Design；workflow 只负责“改 shared family 不能只修当前实例且破坏邻近能力”。

### 5.3 Frontend Design：3 个 production gate

#### F-A — Design Authority & State Coverage

- 不强制所有项目拥有 Figma；
- 有 canonical Figma/design 时必须读取当前 source；
- material production state/variant/responsive/interaction 缺失时先补 design；
- design 正确、implementation 偏离时固定 design、修 implementation；
- platform/accessibility 必要 deviation 应记录并同步设计决策，不能静默漂移。

Figma 当前 Dev Mode 的 Ready for dev、focus/version history、components/variants/properties 正好支持这种 source-of-truth handoff；但这些工具能力不等于我们的项目自动完成设计闭环。

#### F-B — Design-System Coherence

合并当前 web-development TODO 的 component craftsmanship、icon discipline、motion/performance、whole-screen consistency 等重复候选：

- shared components/tokens/variants/states；
- layout/typography/spacing/radius/surface/semantic color；
- coherent icon family；brand asset 与 generic icon 分开；
- generic icon 优先项目 canonical family、platform-native 或成熟维护库；
- custom icon 仅限 product identity、真正 domain-specific symbol 或成熟库确实没有的 gap；
- interaction feedback 覆盖适用的 hover/pressed/focus/selected/busy/disabled；
- motion 使用统一 grammar 并尊重 reduced-motion / system animation setting。

不固定 Fluent/Lucide 为全球默认；不强制所有 icon 动画；不强制小项目新建 central icon registry。Microsoft Fluent guidance强调 icon 应有明确 semantic purpose，AnimatedIcon 只适用于由 interaction/visual-state transition 触发的 icon；不需要动画时应使用 static icon，并应限制单屏动画 icon 数量。

#### F-C — Actual-Surface Convergence

- 在真正 target surface 看 whole product，而不是只看 DOM/组件 crop；
- canonical design 存在时做 whole-screen design-to-implementation comparison；
- 用风险匹配的 visual/interaction regression；
- producer 清掉 obvious local must-fix defects 后才进入 acceptance visual review；
- screenshot 不能冒充 click/native/live behavior。

### 5.4 AI Skills Maintainer：1 个 capability

**Production consumption diagnosis**：active rule 已存在但 real task 仍失败时，先检查：

```text
installed version
source/generated parity
plugin invocation / trigger
task normal entry
current-session loading
candidate/runtime identity
normal-entry replay
```

先判断 `RULE_MISSING`、`RULE_NOT_LOADED`、`STALE_INSTALL`、`CONSUMER_NOT_ROUTED`、`TEST_NOT_FAITHFUL`、`EXECUTION_NONCOMPLIANCE`，再决定是否需要新规则。禁止用更多 policy 文本冒充治理完成。

### 5.5 Bridge Kit 边界

Bridge Kit 只负责：

- 暴露/验证 host user-input transport；
- answerable wait 与 terminal BLOCKED 区分；
- wait 不消耗 retry/repair budget；
- 保持已有 workflow recoverability。

它不拥有 Review Admission、Frontend Design、repo product rule。默认禁止为 056 新建 Control、watcher、polling daemon、ledger、新状态机、第二 controller、Persistent Run/tmux 等机制。

### 5.6 Repo AGENTS 边界

只放项目独有 invariant / locator。中央 workflow/domain rule 不复制。

## 6. Active-rule consumption matrix

| Repo | Failed symptom | Existing active rule | Normal-entry consumer | Consumption evidence | Missing enforcement / fidelity | Proposed action | New AGENTS text? |
|---|---|---|---|---|---|---|---|
| Lucerna | 01033/01034 user credential sequence 后仍出现 stale/`Not set up`；01035 把 remote/source/environment friction、unsupported editor probe 与 scaffold 聚合成 Human Boundary | AGENTS 已要求 matching regression、real provider/no second refresh、actual Windows release/live UI；01035 task 还明确要求 finish all non-human work、optional credential 不得 global BLOCKED | repo `AGENTS.md` + active `prompts/tasks/<goal>.md` + Executor | 规则被**部分消费**：result 有 targeted tests/live route/release smoke；但 sequence closure、dependency eligibility 没有成为 admission condition。01035 task 直接授权读取 remote oracles，仍把 missing local checkout 当 human setup | faithful end-to-end sequence、Human-Gate dependency triage、vertical closure/admission enforcement | workflow regression scenarios：missing local repo+remote available→no prompt；unsupported interface→truthful close；secret genuinely missing→may prompt；UI scaffold without backend contract→not acceptance-ready。先修中央 workflow/consumer，不再加通用 repo 文案 | **NO（默认）**；只有未来证明存在 Lucerna 独有且中央机制不能表达的 provider invariant 才重审 |
| Bobbio | 用户曾成为第一轮 native/UI art director；已有 Figma 但实现曾漂移 | `DEVELOPMENT_WORKFLOW.md` 已有 local tests→native self-QA→GPT Work→repair P1/P2→user；`FIGMA_HANDOFF.md` 已明确 canonical visual source；AGENTS 有 native UI self-inspection | `AGENTS.md` frontend/Product Design read-list + current milestone plan | pre-user QA 规则明确；但 current AGENTS frontend read-list **没有列 `docs/design/FIGMA_HANDOFF.md`**，因此 canonical design locator 不保证 normal entry 消费 | design-source locator / milestone linkage，不是再加视觉 checklist | 后续若 056 获批，仅做最小 locator：frontend/Product Design task 读 current `FIGMA_HANDOFF` + Product Design Brief + active milestone；顺带去重重复 self-QA 文案 | **YES，最多 locator 级别** |
| Mica | synthetic/E2E 绿后 real ChatGPT 仍反复失败，用户 patch-by-patch 手动复现 | AGENTS 已要求 reproduce real failure、bounded diagnostics、improve fixture、focused-before-full-E2E、one short manual loop、final real-site acceptance | current main AGENTS + active task/branch/session | current source 规则已经存在，但现有 GitHub evidence不足以证明历史失败 run 读取的是这版 main / current install；不能简单判“规则被违反” | normal-entry/session identity + faithful fixture；真实 DOM failure 没被 local replay 捕获 | 先做 current normal-entry replay / fixture fidelity diagnosis；不复制 `real failure -> replay -> human` 同义段落 | **NO** |
| Asteria | obvious connector/math/layout defects 曾到 late review 才暴露 | current `prompts/AGENT_RULES.md` 强制 developer visual self-QA、generic-fix、canonical graph system；AGENTS 有 GPT Work-before-human | AGENTS → `prompts/AGENT_RULES.md` → task | 这些规则现在存在且 entry 有 locator；但很多规则是事故后新增，尚不能用“文件存在”证明当前 normal task 会稳定消费并挡住同类 failure | production entry consumption / actual-surface replay | 用一个真实 visual task replay 验证 current entry；失败先修 consumer/enforcement，不加同义 visual rule | **NO** |
| SeminarArc | 用户报告过 design drift，但 repo-level canonical Figma locator 尚无直接 source evidence | 当前 repo 有 generic Compose/Figma skill reference，但不是项目 design authority | 未确认 | current AGENTS/code search 未发现 canonical Figma file/locator | source evidence missing | 保持 `EVIDENCE_NEEDED`，先找真实 design authority 再决定 | **NO / EVIDENCE_NEEDED** |

## 7. R1–R10 disposition

按 Critic 第一轮 disposition 正面收敛：

| v5 mechanism | v6 disposition | owner |
|---|---|---|
| R1 Positive-goal fidelity | `MOVE_TO_LITE`；不作为新 workflow capability | Lite L1/L6 + 既有 workflow goal semantics |
| R2 Pre-human readiness | `MERGE_WITH_R5` | W1 Acceptance Admission + post-action closure |
| R3 Foreseeable human action | `MERGE_WITH_R4` | W2 eligibility/Goal human-decision semantics + transport adapter |
| R4 Persistent prompt | `PROBE_FIRST` | Bridge transport probe；W2 只定义 semantics |
| R5 Human action is not acceptance | `MERGE_WITH_R2` | W1 |
| R6 Exact failure | `MERGE_WITH_R7` | W3 |
| R7 Evidence-surface fidelity | `MERGE_WITH_R6` | W3 |
| R8 Repeat-failure | `KEEP` | W4 |
| R9 Protect accepted behavior | `KEEP`，视觉 system consistency 细节下沉 domain | W5 + Frontend F-B |
| R10 Design-source authority | `MOVE_TO_FRONTEND_DESIGN` | F-A/F-B/F-C |

v6 不保留 R1–R10 作为 production 十条平行规则；此表只用于历史映射。

## 8. Persistent prompt capability probe（本轮只设计，不执行）

独立 probe draft：`docs/design/056_PERSISTENT_PROMPT_CAPABILITY_PROBE_DRAFT.md`。

### 8.1 Probe 目的

只回答当前 installed Codex Desktop/App + CLI 的 host transport 问题，不测试产品功能：

- exact Codex CLI/App version；
- Default mode；
- `default_mode_request_user_input` feature 实际状态；
- unanswered 超过公开问题所述约 120 秒 auto-resolve 窗口后，native prompt 是否仍 pending；
- 是否返回 empty/default answer；
- dependent step 是否在明确 answer 前保持未执行；
- 是否 terminal BLOCKED / retry-like rerun；
- explicit answer 后是否 exact-once resume；
- cancel path。

建议观察窗设为 **150 秒**：它只证明“超过公开报告的 60s grace + 60s countdown 仍未 auto-resolve”，不冒充无限时间数学证明。

### 8.2 判定

**Native PASS**：installed Default-mode request-user-input 在 150 秒后仍 pending，未返回 empty/default；明确回答后只恢复一次；cancel 不执行 dependent action；无 terminal failure。只有这种结果才能继续研究是否把 native prompt 作为 production transport。

**Native FAIL**：tool unavailable、`is_blocking`/client 行为导致自动 resolve、empty/default answer、dependent work提前继续、prompt 消失或重复 resume。此时不得把 feature flag 当 persistent prompt。

### 8.3 Negative fallback

native fail 时，唯一默认 fallback 候选是：

```text
durable plain-text transcript question
+ 明确“等待你的回答后再继续”
+ suspend dependent execution
+ existing resume point / repo state保持不变
+ 用户下一条回答后重新进入同一 Goal
```

这与当前 Codex Default-mode官方 guidance 一致：explicit input required 时直接问 concise plain-text question。它是**durable transcript wait fallback**，不是 native persistent prompt；不得换名字声称原要求已经由 request-user-input 满足。

若实际 surface 连 durable transcript wait + resume 都不能可靠保留，则结论是 `HOST_CAPABILITY_GAP`，停止在架构层，不引入 watcher/polling/Persistent Run/tmux/Control/ledger/new state machine。

### 8.4 Probe 对 workflow counter 的证明边界

Host probe 可观察是否因为 unanswered/cancel 直接产出 terminal failure，以及 probe 前后 tracked workflow state 是否被改动。它不能单独证明所有 Reviewed Handoff counter 在任意 workflow 中永远不变；wait/retry budget 的完整 normal-entry行为仍由后续 capability gate 直接验证。不得用 host probe 过度声称 workflow integration 已完成。

## 9. Capability Gate Matrix（设计 gate，不是当前 PASS）

| Gate | Capability / claim | Normal entry & direct evidence | Failure | Final candidate / regression boundary |
|---|---|---|---|---|
| G1 Human-gate recognition + transport | normal Goal 能把依赖分类并只对 HUMAN_ONLY 询问；transport truthfully identified | 真实 Goal 含 agent-resolvable/unsupported/human-only 三类依赖；另执行 approved host probe | agent-resolvable 被 prompt；unsupported 让用户配置；native persistence 未 probe 却声称支持 | transport 绑定实际 installed Codex/App version；transport 改变需重测 |
| G2 Acceptance Admission | producer evidence 不完整时不能生成 user-ready/release-ready acceptance candidate | 一个缺 actual-surface/targeted evidence 的真实 task；normal handoff 必须拒绝 readiness claim | 几个自报 PASS 字段即可绕过 | admission 绑定当前 candidate；advisory review 不被误拦 |
| G3 Resume / post-action closure | Human Action 后恢复同一 Goal，agent 完成 integration；action 本身不是 completion | 低风险 test Goal 的 human checkpoint → reply → agent closure | 用户一回答就 feature complete；重复 prompt；重启整个 task | 保护已完成 pre-action work，resume exact scope |
| G4 Faithful regression | old-bad 被 focused regression 捕获，新 candidate PASS，必要 actual surface 确认 | 一个历史真实 failure replay | old-bad 也 PASS；只 broad suite | final candidate 直接通过；不破坏 adjacent behavior |
| G5 Evidence / final-candidate | proxy/synthetic/helper/screenshot 不冒充 native/live/action | 混合 evidence task 的 claim-to-surface check | 旧候选或低层证据拼 release PASS | 同一 final candidate 的关键 gate |
| G6 Frontend design consumption | canonical design 存在的 real UI task 真正读取/消费设计；missing material state 回设计源 | Bobbio 或另一有 canonical design 的 normal task | code 临时发明 state/component；只读路径没消费 | 同时检查 actual-surface convergence 与 should-not-change |
| G7 Non-overreach | docs/server/backend/tiny nonvisual change不会被强制 Figma/GPT Work/full E2E | 至少三个负例 route | 中央规则自动把小任务升级重流程 | Lite/workflow trigger 保持 risk/surface-scaled |
| G8 Consumption-regression diagnosis | active rule 存在但 normal entry 未加载/未执行时 maintainer 能暴露事实 | 模拟 stale install / wrong task entry / session-not-reloaded / generated drift 中至少一种 | 维护者只新增同义 TODO | 诊断 source/install/consumer identity，不修改 domain policy |

这些 gate 必须通过 normal entry / runtime/artifact 行为证明；字符串存在、字段存在、TODO 更新都不算 capability PASS。

## 10. 替代路线比较

### A. v5 原样

不采用。优点是覆盖全面；缺点是 10 个机制重叠、persistent prompt 假设过强、review scope 容易过度、已有规则消费问题仍可能被新 policy 淹没。

### B. 6 Lite + 5 workflow + 3 Frontend（推荐）

推荐。它能解释：

- Lucerna 01033/34：W3 sequence fidelity + W1 actual closure；
- Lucerna 01035：W2 dependency triage + W1 vertical closure/coverage table；
- Bobbio：F-A design authority + F-C actual surface，同时只补 locator；
- Mica：W3 faithful replay + W4 human-time budget，不重复项目规则；
- Asteria：maintainer consumption diagnosis + F-C normal-entry replay。

同时 G7 明确防止 docs/backend/server/tiny fix 被升级为 Figma/GPT Work/full E2E。

### C. Repo-specific only

不采用为主方案。它可以快速修当前四个项目，但会把同一“用户作为 debugger / proxy evidence / Human Gate滥用”复制到多个 AGENTS，并继续造成 drift；01035 的 dependency triage 本质跨项目。

### D. Bridge-first

不足。它能解决 prompt transport/wait，但解决不了 half-finished admission、unfaithful tests、scaffold 冒充 capability、Figma drift 和 external review 过早。

### E. Consumption-only

必须成为重要组成，但不足以单独解决。Lucerna/Asteria 确有 active-rule consumption 问题；然而 01035 的 `AGENT_RESOLVABLE vs HUMAN_ONLY vs UNSUPPORTED` 分类和 acceptance vertical closure 并未被当前通用 workflow 明确表达，需要 W1/W2。

## 11. Red Team

1. **Human Gate laundering**：Executor 把 remote clone、环境、缺 contract 实现包装成“用户 setup”。→ W2 分类；只有 HUMAN_ONLY 可 prompt。
2. **Scaffold laundering**：UI/card/handler 存在就报 feature complete。→ W1 vertical closure；coverage table 对高风险多项 Goal 做逐项 disposition。
3. **Review Admission checklist wall**：任何小修都跑大门禁。→ 只 gate acceptance review；evidence risk/surface-scaled；G7 负例。
4. **Self-reported PASS gaming**：结果文件写几个 PASS 字段。→ G2/G5 要 final candidate direct evidence；producer self-report 只是 locator。
5. **Persistent prompt wishful thinking**：feature flag 被误当 no-expiry。→ PROBE_REQUIRED；native/fallback/gap 三分法。
6. **Fallback rebranding**：plain-text wait 被写成 native persistent prompt。→ 明确不同 capability claim。
7. **Policy duplication**：Lucerna/Bobbio/Mica/Asteria 各抄中央规则。→ consumption matrix + repo AGENTS only invariant/locator。
8. **Coverage table 变新 ledger**：每个小 task 都生成状态账本。→ 仅高风险/多 deliverable Gate前的 task-local evidence，不持久 schema，不是新 state。
9. **Unsupported capability 继续问用户**：VS Code/Cursor 类无 supported interface 仍推给用户。→ `UNSUPPORTED_WITH_EVIDENCE` 直接 truthful close。
10. **Optional 标签逃避 frozen requirement**：Executor 把真正必需 capability 标 optional。→ classification 必须回指 frozen objective/acceptance；Goal owner 决定 required/optional，不由 Executor为了过 gate 改写。

## 12. Recovery / 未决项

### `PROBE_REQUIRED`

- Default-mode persistent request-user-input 的 installed host behavior；
- native cancel behavior；
- durable transcript fallback 在目标 Desktop workflow 中的 resume 可靠性（若 native fail）。

### `EVIDENCE_NEEDED`

- SeminarArc 是否存在 canonical project Figma/design locator；
- Mica 历史失败 run 的真实 plugin/session/branch consumption identity；
- Asteria 当前 post-rule normal-entry replay 是否真的消费 visual contracts。

### Recovery

- probe native PASS → W2 transport 可选择 native，但仍需 workflow normal-entry gate 验证；
- probe native FAIL → 只评估 durable transcript suspend/resume；不造 daemon/state machine；
- fallback 也不可靠 → 显式 `HOST_CAPABILITY_GAP`，056 不冻结依赖 persistent-native 语义的 implementation Plan；
- Critic 认为 6/5/3 仍过重 → 优先合并 owner 内 capability，不把细则重新塞回 Lite；
- Critic 认为过简 → 新机制必须指向一个 v6 现有 gate 无法阻止的真实 failure，不能以“更保险”为理由增加。

## 13. 本轮没有批准什么

- 没有批准任何 production plugin/skill 修改；
- 没有批准 Bridge Kit production 修改；
- 没有批准 Bobbio/Lucerna/Mica/Asteria/SeminarArc AGENTS 修改；
- 没有批准 capability probe 实际运行；
- 没有创建 implementation Goal/Kickoff/branch/worktree；
- 没有把 Critic blocker 标记为 closed。

下一步只把 v6 + probe draft 交独立 Critic。

`NEXT_HANDOFF = CRITIC`

## 参考来源（本轮实际核查）

- OpenAI, *Harness engineering: leveraging Codex in an agent-first world*, 2026-02-11: https://openai.com/index/harness-engineering/
- OpenAI Codex source, Default collaboration-mode template: https://github.com/openai/codex/blob/main/codex-rs/collaboration-mode-templates/templates/default.md
- OpenAI Codex source, request-user-input app-server tests: https://github.com/openai/codex/blob/main/codex-rs/app-server/tests/suite/v2/request_user_input.rs
- OpenAI Codex issues #37472, #43759, #34455: Default-mode blocking / timeout / auto-resolution reports.
- Figma, *Guide to Dev Mode* and *Ready for dev view*: https://help.figma.com/hc/en-us/articles/15023124644247-Guide-to-Dev-Mode and https://help.figma.com/hc/en-us/articles/23918228264855-Dev-Mode-ready-for-dev-view
- Figma, *Variants and component set fundamentals*: https://help.figma.com/hc/en-us/articles/39636737843735-Components-collection-Variants-and-component-set-fundamentals
- Microsoft Fluent 2, *Iconography*: https://fluent2.microsoft.design/iconography
- Microsoft Learn, *AnimatedIcon*: https://learn.microsoft.com/en-us/windows/apps/develop/ui/controls/animated-icon
- Microsoft Learn, *Motion in Windows*: https://learn.microsoft.com/windows/apps/design/signature-experiences/motion
