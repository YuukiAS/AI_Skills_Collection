# Frontend Design Production Consolidation — Execution Plan v0.1

状态：`DRAFT_FOR_EXECUTION_READY_CRITIC`  
日期：2026-09-27  
目标仓库：`YuukiAS/AI_Skills_Collection`  
目标插件：`web-development` / Frontend Design  
执行包版本：`v0.1`  
任务键：`web-development--frontend-design-production-consolidation`  
计划执行分支：`reviewed/web-development--frontend-design-production-consolidation`  
计划任务工作树：`/tmp/ai-skills-web-development-frontend-design-production-consolidation`  
已批准架构：`docs/design/frontend-design/FRONTEND_DESIGN_PRODUCTION_CONSOLIDATION_PROPOSAL_V0_3_2026-09-27.md` @ `effa02b4e7e02f012ea24bda1683857609a09fe1`

本文件把已获独立 Critic PASS 的 v0.3 架构冻结成可执行合同。它不重新设计架构，也不授权立即实现。只有本执行计划、同版 Canonical Goal、同版 Kickoff Draft 一起通过 execution-ready Critic，且用户随后发送获批 Kickoff，才允许创建上述分支/工作树并启动 Executor。

---

## 1. 本轮真实目标

把当前 `web-development 0.2` 从“已有若干正确 Frontend Design 规则，但 generated aggregate 仍平级任选 source、实际闭环不完整”的状态，收敛为一个真正的 Frontend Design 正常生产入口：

1. 普通 Frontend Design 请求首先进入 `frontend-visual-systems` coordinator；
2. coordinator 再按任务需要调用产品规划、视觉方向、设计系统、Figma、动效、响应式/可访问性、浏览器证据与科研产品 specialist；
3. S1 小修不会被强迫跑完整设计仪式；
4. 有 canonical Figma 时实现不能自行漂移，无 Figma 时仍可正常完成；
5. browser 与 native-WebView 的证据强度和 claim 对齐；
6. producer 在交独立 reviewer 或用户前先发现并修掉明显 P1/P2；
7. 准备让用户执行的界面动作，若可安全预演，producer 已先验证到用户专属操作边界；
8. tests、generated parity、截图存在都不能单独冒充视觉/交互质量完成；
9. Bobbio / Lucerna / Asteria 真实回放严格区分“项目本地规则兼容”与“插件自己提供的能力”；
10. 若三项真实回放最终都只能证明兼容，插件仍可完成本轮兼容改进，但 maturity 保持 `unclassified`，不制造第四个 synthetic 项目追求升级。

本轮不是 Lucerna 专项。架构必须继续适用于 Bobbio、Asteria，并为未来自然出现的 Mica for ChatGPT、SeminarArc 等不同前端形态保留同一通用入口，同时尊重各项目自己的平台、安全和设计 authority。

---

## 2. 已冻结、不得重新设计的架构

Executor 必须忠实实现 v0.3，下列内容不得重新选择：

- `frontend-visual-systems` 是唯一 generic production coordinator；
- aggregate generator 增加最小、opt-in 的 coordinator-first 模式；
- 未启用该模式的其它 aggregate 保持原 choose-one 行为；
- 不新增 orchestrator Skill；
- `product-ux-planning` 是 generic coordinator delegate；
- `research-product-frontend` 只保留 research-specific specialist 身份；
- `responsive-accessibility-review` 进入适用的 P1/P3 closure；
- `webapp-testing` 是窄范围 browser evidence companion，不是 design owner；
- `implementation-react-tailwind` 继续是 downstream builder；
- P0–P4；
- F-A / F-B / F-C / F-D；
- S1 / S2 / S3 + design-authority / surface 两个正交修饰符；
- canonical Figma / other durable authority / current production grammar；
- browser / native-WebView evidence boundary；
- P1/P2/P3 producer admission；
- handoff action reachability；
- whole-product taste 的可观察问题；
- #52 / #62 / #69 的 retained semantics；
- no-Figma 正常完成；
- tiny/local fix 不跑完整 ceremony；
- user 不承担 routine P1/P2 discovery。

如果实现发现这些冻结项本身不成立，停止并返回 Planner/Critic；不得由 Executor自行改架构。

---

## 3. 当前真实实现与最小改动方向

### 3.1 Generated aggregate 的核心缺口

当前 `scripts/build_codex_marketplace.py` 对所有 aggregate 固定生成：

`Choose the source workflow whose trigger boundary best matches the user request.`

因此只改 `frontend-visual-systems/SKILL.md` 无法让 generated production entry 变成 coordinator-first。

冻结的最小 generator 设计：

- aggregate config 新增可选 `routing_mode`；
- 当前仅允许：
  - 缺省 / `choose-one`：保持现有行为；
  - `coordinator-first`：使用 coordinator 模式；
- coordinator 模式另有 `coordinator_artifact_id`，必须引用该 aggregate `source_skills` 中真实存在且唯一的 artifact id；
- 只有显式启用 coordinator 模式的 aggregate 使用新 workflow；
- 其它 aggregate 的生成语义与输出正文保持现状。

对 Frontend Design 的 main aggregate：

```text
routing_mode = coordinator-first
coordinator_artifact_id = system
```

其中 `system` 对应 `skills/tools/frontend/frontend-visual-systems`。

生成后的主 Frontend aggregate 必须：

1. 首先读取 `_src/system/source.md`；
2. 由 coordinator 判断规模、design authority、target surface、产品/状态风险；
3. 只读取 coordinator 判定需要的 delegate source；
4. delegate 结果回 coordinator 做 convergence / admission；
5. 不再出现与 coordinator-first 冲突的 “choose one source workflow” 正常入口语义。

### 3.2 Frontend aggregate topology

`web-development` 的 main `visual` aggregate 应包含：

- `frontend-visual-systems` — coordinator；
- `product-ux-planning`；
- `visual-direction`；
- `design-system-tokens`；
- `figma-design-to-code`；
- `motion-interaction`；
- `responsive-accessibility-review`；
- `webapp-testing`；
- `research-product-frontend`。

当前单独 generated 的 `research-product-frontend` aggregate 从 Marketplace plugin 顶层 active skills 中移除，避免 generic research-product request 绕过 coordinator。canonical source skill `skills/tools/frontend/research-product-frontend` 不删除，继续作为 coordinator 的 research-specific specialist。

`frontend-reference-research` 保持现有窄范围显式入口；它不是本轮 generic production coordinator，也不因本轮删除。

`implementation-react-tailwind` 不加入 Frontend Design Marketplace aggregate；它继续作为 downstream builder / profile 能力。只需要把“实现约束暴露 design gap 时返回 P0/P1”边界写清。

### 3.3 Source Skill 职责

优先把规则放回现有 owner，而不是把 coordinator 写成巨型规则墙：

- `frontend-visual-systems`：P0–P4 总协调、F-A–F-D、S1–S3、authority/surface、repair routing、review admission；
- `product-ux-planning`：产品任务、primary states、actionability/lifecycle、normal-vs-diagnostics、metric/ranking visible semantics；
- `visual-direction`：whole-screen freeze、composition、observable taste questions；
- `design-system-tokens`：component craftsmanship、semantic typography/color/status、#52 icon source/registry/provenance；
- `figma-design-to-code`：conditional Figma authority、Figma complete、round-trip、design/render convergence；
- `motion-interaction`：motion intent 与 runtime latency/jank 的边界，不冻结跨项目统一毫秒阈值；
- `responsive-accessibility-review`：按规模参与 P1 constraint 与 P3 closure；
- `webapp-testing`：browser evidence、claim/evidence 边界；不得声称 browser fixture 证明 native；
- `research-product-frontend`：科研产品的专业 UI constraint，不重复 generic 产品规划；
- `implementation-react-tailwind`：下游实现，发现 design gap 时返回 coordinator。

---

## 4. 明确禁止的 scope

本 execution package 不得修改或实现：

- Clear Writing / `writing-style` production behavior；
- Product UI copy content-architecture deferred heading；
- writing-style #17；
- writing-style #20；
- writing-style #13（只保留下一阶段 dependency-to-review）；
- CUHK Date Product UI Copy naturalness；
- Bridge Kit；
- Host Policy / execpolicy；
- 新中央 plugin；
- 新 orchestrator Skill；
- paid API / paid reviewer / Terra；
- Bobbio、Lucerna、Asteria、Mica for ChatGPT、SeminarArc 的产品 source；
- 任何 unrelated repo；
- force push、history rewrite、branch deletion、destructive Git。

如果要关闭上述 deferred scope 才能继续，停止返回 Planner/Critic。

---

## 5. 允许修改的 source / generated surface

### 5.1 Production source

允许按 approved architecture 修改：

- `skills/tools/frontend/frontend-visual-systems/**`
- `skills/tools/frontend/product-ux-planning/**`
- `skills/tools/frontend/visual-direction/**`
- `skills/tools/frontend/design-system-tokens/**`
- `skills/tools/frontend/figma-design-to-code/**`
- `skills/tools/frontend/motion-interaction/**`
- `skills/tools/frontend/responsive-accessibility-review/**`
- `skills/tools/frontend/webapp-testing/**`
- `skills/tools/frontend/research-product-frontend/**`
- `skills/tools/frontend/implementation-react-tailwind/**`，仅限 downstream handoff boundary，若不需要则不改；
- `scripts/build_codex_marketplace.py`
- `scripts/codex_marketplace_config.json`
- 直接必要的 tests / repo-safe fixtures。

### 5.2 Generated layer

只能通过现有 generator 重新生成并验证：

- `.agents/plugins/marketplace.json`
- `plugins/codex/plugins/**`

禁止手改 generated payload。

### 5.3 Evidence / closure

允许：

- `results/web-development--frontend-design-production-consolidation/**`
- `docs/plugin-todos/web-development.md`，只在最终 closure 按真实实现更新 #52–#72；
- `docs/plugin-changelogs/web-development.md`
- `CHANGELOG.md`
- `README.md`
- `VERSION`
- 与版本/生成一致性直接相关的现有 version tests。

`docs/PLUGIN_MATURITY.md` 默认不改；只有真实 attribution 支持且后续用户/Planner另有明确决定才可改变。本任务当前冻结为 `unclassified`。

---

## 6. Producer severity 与用户时间保护

统一使用已批准语义：

- P1：阻塞或危及核心用户流程、状态正确性或证据真实性；
- P2：正常用户可直接看到的实质困惑、摩擦、视觉/层级/一致性缺陷；
- P3：不破坏 acceptance 的 polish。

Producer 的 `P1=0/P2=0` 必须绑定 exact candidate、exact target surface 与具体 evidence；它只是进入独立 review 的 admission，不是独立质量证明。

### Handoff action reachability

只要最终 handoff 要用户点击、选择、展开、保存或授权某个控件，且 producer 可以在不替代用户私有决定的前提下安全预演，就必须先验证：

- control 可见；
- control enabled；
- 真实交互能触发；
- 到达预期 next state / user-only boundary；
- 当前状态不存在明显 P2。

不可安全预演的 destructive/credential/人类选择，只验证到最后一个安全边界。

Lucerna 01052 的 `Choose folder` 事故属于该 gate 的已知 regression，但 Lucerna 已有同义 repo-local 规则时只计 compatibility，不自动计 plugin capability。

---

## 7. Capability Gate Matrix v0.1

所有 release-critical gates 必须由同一个 final candidate 直接通过，不拼接不同 commit 的 PASS。

### G1 — Normal Entry / Coordinator Routing

**用户能力**  
普通 Frontend Design 请求进入 `frontend-visual-systems` coordinator，再按需调用 delegate。

**必须证明**

- generated main aggregate 是 coordinator-first；
- coordinator source 是 `system`；
- `product-ux-planning` 不再由独立 research aggregate 平级抢 generic route；
- `research-product-frontend` 作为 coordinator 内 research-specific specialist；
- `webapp-testing` 在 coordinator 内真实可达但不是 design owner；
- `implementation-react-tailwind` 不被并入 design owner；
- 正常 production plugin replay 记录实际 coordinator/delegate consumption。

**失败**

- generated payload 仍出现 generic choose-one 正常入口；
- natural generic UI request 可绕过 coordinator；
- specialist 单独结果被当成 production-ready 总结。

### G2 — Coordinator Decision / Scale / Authority

**用户能力**  
coordinator 能正确区分 S1/S2/S3、design authority、browser/native surface，并按 P0–P4 执行而不过重。

**冻结回归至少覆盖**

1. S1 browser 小修：使用 current production grammar，不强迫 Figma/独立外审；
2. S2 有 durable authority：只扩展必要 state/组件；
3. S3 redesign：完整 P0–P4；
4. canonical Figma：material design defect 回 authority；
5. no-Figma：用其他 durable authority 正常完成；
6. native-WebView：只增加与 native claim 相称的 evidence；
7. implementation drift：不无意义改 design source。

这些 deterministic/candidate replays 可以证明实现，不计 maturity。

### G3 — Visual-System / Ownership Fidelity

**用户能力**  
各类视觉/产品判断由正确 owner 承担，不形成重复规则墙。

**必须证明**

- #52：canonical/platform icon source、central registry/component、brand/generic 分工、optical normalization、a11y/theme、third-party source/license/provenance 全保留；
- #55/#66/#68/#71/#72：component/system grammar 一致；
- #57/#59：whole-screen direction 与 taste 使用可观察问题；
- #58/#60/#61：conditional Figma authority、complete、round-trip；
- #62：design authority → implementation → actual surface → self-QA → confirmation 对 Figma/非 Figma 都成立；
- #63/#64/#65/#70：正常界面边界、actionability、visible data semantics、lifecycle disclosure；
- #54：motion intent 与 runtime performance 分工；
- #69：interaction causality 属于 F-C，只有 competing route/control-path claim 才加强 proof。

### G4 — Evidence Fidelity / Producer Admission

**用户能力**  
生产候选在交 reviewer/user 前，证据与 claim 对齐，producer 先清掉 routine P1/P2。

**冻结回归至少覆盖**

- browser screenshot 不冒充 click；
- browser fixture 不冒充 native；
- ordinary locator/actionability + postcondition 无需额外 handler instrumentation；
- competing hide/focus/outside-click route 时不能只看 final state；
- handoff action reachability；
- P1/P2/P3 ledger 绑定 exact evidence；
- targeted/local fix 可只 producer self-QA；
- substantive redesign / baseline/release / major design/native milestone 强制 independent review。

### G5 — Shared Generator Should-Not-Change / Generated Parity

本任务修改 shared Marketplace generator，因此必须 broad regression。

**必须证明**

- 未启用 `coordinator-first` 的 aggregate 仍生成原 choose-one workflow；
- coordinator config 引用不存在/重复 artifact id 时 fail closed；
- aggregate metadata union、scope、secrets、路径预算、nested `SKILL.md` 重命名、determinism 等已有 generator contract 不回归；
- 除 web-development 及共享 marketplace manifest 的预期变化外，其它 central plugin generated payload 不出现语义变化；
- registry/catalog/Marketplace 重新生成后 parity PASS；
- 全部现有 unittest PASS。

### G6 — Bobbio / Lucerna / Asteria Real Replay + Attribution

不新增第四个 synthetic 项目。

每个 replay：

- 使用 final candidate 的正式 candidate plugin identity；
- 从 normal Frontend Design entry 进入 coordinator；
- prompt 只给真实目标/项目 source，不复述待测 generic rule；
- 记录 coordinator → delegate source consumption；
- project source 只读，不修改目标 repo；
- 保存 raw response、candidate identity、repo ref、adjudication。

#### Bobbio

至少读取当时冻结 ref 的 canonical Figma handoff、Product Design Brief、black-box review policy。已由 repo-local source 给出的 Figma/P1/P2规则只计 compatibility。

#### Lucerna

至少读取当时冻结 ref 的：

- `AGENTS.md`
- `docs/workflows/LUCERNA_VISUAL_ACCEPTANCE.md`
- `docs/design/lucerna/LUCERNA_UI_PRODUCT_SYSTEM_V1.md`
- `docs/design/lucerna/LUCERNA_EXTENSION_IDENTITY_STATUS_AUTH_V1.md`

这些已冻结行为只计 compatibility。01052 handoff-action-reachability regression 保留，但只有 repo-local contract 未直接给答案、normal coordinator 自主作出的 generic admission/evidence decision 才可计 plugin capability。

#### Asteria

至少读取 accepted concepts 与 developer visual self-QA contract。重点证明 browser-only / no-Figma should-not-overreach compatibility。

#### Attribution receipt

每个 replay 必须逐项记录：

- `REPO_LOCAL_RULE_GAVE_ANSWER = YES|NO`
- `COORDINATOR_GENERIC_DECISION_OBSERVED = YES|NO`
- `COUNTS_AS_COMPATIBILITY = YES|NO`
- `COUNTS_AS_PLUGIN_CAPABILITY = YES|NO`
- 直接 evidence locator。

若 Bobbio/Lucerna/Asteria 全部只能证明 compatibility，G6 仍可因“兼容且无回归”PASS，但 maturity 必须继续 `unclassified`。

### G7 — Final Candidate / Release Metadata / Human-Facing Closure

本任务一旦按批准架构实现完成，就一定改变 `web-development` 的正式 production behavior：normal entry、aggregate routing、coordinator/delegate topology、review/admission 与 evidence contract 都会发生用户可观察变化。因此，**完成本任务的 release candidate 必须 bump 版本；不存在“实现完成但 web-development 仍保持 0.2”的合法 PASS 路径。**

**Plan-time 决策**

当前 main 的真实版本基线是：

```text
Repository = 5.3.0
web-development = 0.2
```

因此，在 kickoff base 仍为该版本基线时，本任务预期正式 release 为：

```text
Repository bump decision: PATCH
Expected repository release: 5.3.0 -> 5.3.1

Affected plugins:
- web-development: 0.2 -> 0.3
  Reason: Frontend Design 获得 coordinator-first normal entry、完整 production QA/evidence/admission 闭环与新的 generated routing。
- all other central plugins: NO_BUMP
```

如果 kickoff 前 `main` 已被其它已完成 release 推进，则不得覆盖并发历史；Executor 必须从 kickoff-time then-current source 重新计算：
- repository = then-current compatible PATCH；
- `web-development` = then-current two-part version 的下一 release；
- all other plugins = NO_BUMP。

这只是**版本基线顺延**，不是重新决定“要不要 bump”。只要本任务实现完成并通过 release gates，版本 bump 是强制 closure。

**版本时序**

1. 开发早期不提前 bump；
2. implementation + known regression + broad compatibility 稳定后，重新读取 then-current version source；
3. 写入本任务唯一一次 repository/plugin version bump，并同步 web-development changelog、root CHANGELOG、README、version tests、generated manifests；
4. 之后冻结 final candidate；
5. G1–G7 必须在这个已经带最终版本 metadata 的同一 final candidate 上重新通过；
6. independent implementation review 若 REVISE，继续修同一个 release candidate/version，不再次 bump；
7. 如果实现无法达到 release gates，则本任务不能 PASS，也不能把已经完成的 production behavior 以 unchanged version 交付；应如实返回 blocker。

maturity 继续保持 `unclassified`。README 是 mandatory closure。

---

## 8. 冻结 replay 设计与反过拟合要求

### 8.1 Candidate-visible deterministic regressions

Executor 可以建立少量 repo-safe scenario inputs，用来证明 G1–G4，但这些是开发/发布回归，不是 maturity evidence。

输入不得包含诸如 `EXPECTED_DECISION=...`、`USE_F_D=YES` 等 answer-shaped fields。Rubric 与 expected behavior 应放在 candidate 不可见的 adjudication artifact 中。

至少覆盖：

1. tiny browser visual drift；
2. design-heavy no-Figma 产品；
3. canonical-Figma material design change；
4. native handoff action reachability；
5. competing-route interaction claim；
6. unsupported ranking/metric semantic claim；
7. implementation-only drift should-not-change。

### 8.2 Real replay freeze

Bobbio / Lucerna / Asteria 的 replay prompt、repo ref、rubric 在 final replay 前一次性冻结。开发中已看过的 replay 可继续作为 known regression；如果需要 fresh qualitative evidence，只能在 final-candidate freeze 前预先冻结，不允许失败后换题追 PASS。

不允许把 Mica for ChatGPT、SeminarArc 临时加入本轮 replay 来追 maturity。

---

## 9. Validation chronology

### Phase A — Bootstrap / source drift

1. 验证 canonical checkout、`origin/main`、approved architecture 与本 execution package；
2. execution-ready Critic PASS 后，只有用户发送 approved Kickoff 才创建 exact reviewed branch/worktree；
3. 读取 `workflow-core + ai-skills-core + web-development` 生产入口及必要 target source；
4. 若 kickoff-time main 对 Frontend/generator/version policy 有相关 semantic drift，停止返回 Planner，而不是静默覆盖。

### Phase B — Generator + source implementation

1. 先写/更新 generator targeted tests；
2. 实现 opt-in coordinator-first mode；
3. 更新 web-development source config/topology；
4. 更新 coordinator 与 delegates；
5. 生成 payload；
6. 运行 targeted tests。

### Phase C — Cheap deterministic regression

1. G1–G4 candidate-visible regressions；
2. generator default-mode should-not-change；
3. existing web-development 056 regressions；
4. 失败则在同一冻结 scope 内修复，不进入真实 replay。

### Phase D — Broad repository regression

至少运行：

```text
python scripts/skills.py registry --write
python scripts/skills.py validate
python scripts/skills.py audit --all
python scripts/skills.py catalog --write
python scripts/build_codex_marketplace.py --write --validate --check --path-report
python -m unittest discover -s tests
```

并证明 non-web aggregates 未发生非预期 generated semantic drift。

### Phase E — Development replays

使用 isolated candidate plugin identity 运行 Bobbio / Lucerna / Asteria 已冻结 read-only replay，修复 generic plugin 问题。不得修改三个项目 repo。

### Phase F — Release-candidate decision and freeze

当实现、known regressions、broad compatibility 都稳定后：

1. 重读版本政策和 then-current version sources；
2. 若满足正式 behavior-change release 条件，执行一次且仅一次 conditional version/changelog/README/repository PATCH closure；
3. 重新生成 payload；
4. 冻结 final candidate commit、replay inputs、rubric、project refs；
5. final-candidate freeze 后禁止继续视觉/规则调参，除非 independent review 返回真实 blocker；修复仍使用同 task/version，不再二次 bump。

### Phase G — Same-final-candidate final gates

在完全相同 final candidate 上重新通过 G1–G7：

- targeted tests；
- full unittest / registry / audit / generator parity；
- candidate plugin normal-entry replay；
- Bobbio/Lucerna/Asteria final replay；
- attribution adjudication；
- version/changelog/README consistency。

提交并 ordinary non-force push 到 exact reviewed branch，确认 remote tip == intended local HEAD。

### Phase H — Independent implementation review

Executor 停止并交 independent Reviewer/Critic：

- final commit；
- raw replay outputs；
- route/source-consumption evidence；
- attribution receipts；
- generated diff；
- test/validation evidence；
- README/version/changelog decision。

独立 review PASS 前：

- 不 merge main；
- 不更新 release ref；
- 不关闭 #52–#72；
- 不声称整体 Goal achieved。

如果 review REVISE，沿同 task key/branch/worktree 修复并重新跑受影响 gate；不创建 successor task。

### Phase I — Integration / release closure

只有后续得到明确 integration authorization 后才可：

- 集成 reviewed candidate 到 main；
- 完成正式 release/ref/CI 所需步骤；
- 更新 TODO / Maintenance Board / Resolution evidence；
- 依据真实 attribution 决定 maturity；本 execution package 默认保持 `unclassified`。

当前 Kickoff 不授权 Phase I。

---

## 10. 真实项目 replay 的安全边界

Bobbio、Lucerna、Asteria 本轮均为**只读 evidence source**：

允许：

- fetch/read public/private repository source；
- 固定 exact commit/ref；
- 将 repo-safe source locator 传入 candidate replay；
- 保存 replay response 到 AI_Skills task results。

不允许：

- 修改或 push 这些项目；
- 启动它们的 production mutation；
- 用真实用户数据做 destructive probe；
- 用它们替 AI_Skills 修自己的 plugin 问题。

Lucerna 的 native interaction历史 evidence可作为 regression source；本轮不要求为了 Frontend plugin replay 去控制用户当前 Lucerna 桌面。

---

## 11. 应保留的历史能力

本轮修改不能破坏：

- 056 的 F-A/F-B/F-C；
- explicit frontend reference research；
- research-product specialist 的领域语义；
- no-Figma route；
- docs/backend/nonvisual 不被误加 frontend ceremony；
- existing profiles 的安装能力；
- Marketplace path budget / deterministic generation；
- 其它 central plugin aggregate choose-one 语义；
- current web-development plugin name/slug/icon；
- all unrelated plugins。

如果 shared generator 修改导致其他 aggregate behavior 变化，G5 FAIL，不能以“新模式更好”接受。

---

## 12. Maintenance Board pending mutation

当前 Planner surface 仍没有 GitHub Project field mutation 能力，而且 reader-facing Issue/Project copy mutation 需要先真实调用 Clear Writing；本任务又明确不修改 Clear Writing production。不得伪称已经同步。

下一次 Project-capable AI Skills Maintainer 应先核对 pending mutation 仍 current：

### #52–#72

- 若仍为 `TODO` → `DOING`；
- 若已为 `DOING`，保持；
- `CURRENT_ANCHOR = docs/design/frontend-design/FRONTEND_DESIGN_PRODUCTION_CONSOLIDATION_EXECUTION_PLAN_V0_1_2026-09-27.md`
- `NEXT_STEP = independent execution-ready Critic review`
- 不关闭 TODO；
- 不设置 Resolution commit。

### Deferred Product UI Copy heading

继续执行 v0.3 已冻结的 locator collision 修复 pending mutation；它不属于本 execution scope，不因本任务进入 DOING。

---

## 13. Completion / stop conditions

### Executor 可以自行修复

- approved source skill wording/structure；
- generator implementation bug；
- tests / fixtures；
- generated parity；
- replay暴露的 generic plugin defect；
- version/changelog/README consistency；
- 同 scope 内普通代码错误。

### 必须停止返回 Planner/Critic

- 需要新 orchestrator Skill；
- 需要改变 P0–P4 / F-A–F-D / S1–S3；
- 需要把 Clear Writing / Product UI Copy 拉入本轮；
- 需要修改 Bridge Kit；
- 需要新增第四 real/synthetic maturity project；
- 需要修改 Bobbio/Lucerna/Asteria source；
- coordinator-first 无法在最小 aggregate generator extension 中表达；
- production replay 必须使用新的 credential/provider/private-data scope；
- 需要 paid review；
- 需要 force/destructive Git；
- final replay 证明 approved architecture 本身错误。

---

## 14. 本 execution package 新增的真实能力

如果本包最终实施并通过 review，新增的不是“更多规则文本”，而是以下实际生产能力：

1. Frontend Design 正常入口从平级任选 specialist 变成真实 coordinator-first；
2. 小修、普通改动、产品重设计使用不同成本，不再一律重流程；
3. Figma 与非 Figma 项目都能走同一闭环；
4. browser/native claim 有正确 evidence boundary；
5. producer 在用户前先验证明显视觉、层级和交互问题；
6. 交给用户的 UI action 不再默认由用户第一次证明“能不能点”；
7. generator/shared Marketplace 修改对其它 plugin 有明确 should-not-change 保护；
8. real replay 的 compatibility 与 plugin capability 不再混算，防止虚假 maturity。

这正是本轮值得保留的阶段价值；单纯 schema、测试数量或生成文件数量不算新增能力。
