# Presentations 双模板生产架构 V1.0 — Critic Review

**Review object:** `PRESENTATIONS_TWO_TEMPLATE_PRODUCTION_REDESIGN_PLAN_V1_0`  
**Review stage:** architecture_and_capability_gate_review  
**Target repo:** `YuukiAS/AI_Skills_Collection`  
**Target plugin/domain:** `presentations`  
**Task key:** `presentations--two-template-production-redesign`  
**Source branch/ref:** `main`  
**Reviewed proposal:** `docs/design/PRESENTATIONS_TWO_TEMPLATE_PRODUCTION_REDESIGN_PLAN_V1_0_2026-09-28.md`  
**Reviewed proposal commit:** `78901482243a877cdcec3150ca229b3fa58b7173`  
**Main inspected:** `e83790cf69664b893f533e0ba12f087b89c4ad90`  
**Verdict:** **REVISE**

## 1. 用户可读结论

V1.0 的主架构方向是对的，不需要推倒重来。最重要的三点——“所有演示文稿先经过 presentations 前门”“语义故事板与页面构图严格分离”“两个内置模板只负责视觉/渲染，不接管故事线和科学内容”——都比当前以 `deck-plan.yaml`、局部 validator 和 exact-CUHK 路径为中心的架构更接近真实失败根因。

本轮不能 PASS，原因不是“还可以多测一点”，而是四个会直接影响实现方向的合同缺口：统一前门还没有绑定到当前真正的 plugin discovery/routing consumer，且商业/可编辑 deck 的默认格式可能回归；#45–#48 的 evidence-gated TODO 被 V1.0 部分提前写成了必做 production contract；G9/G10 把横向证据规则与产品能力 Gate 混在一起；Package B/C 仍然大到足以让一次 Executor Goal 同时改变太多独立能力。修这些即可，不需要另起第三模板、第三 presentation skill、几何引擎或新状态机。

## 2. 已实际读取的 source

本轮实际读取了最新 `main` 的：

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`（v1.4）
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`（v1.4）
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`（v1.1）
- `docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md`
- `docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md`
- `docs/plugin-todos/presentations.md`
- `docs/plugin-changelogs/presentations.md`
- `skills/tools/documents-media/presentations/research-presentations/SKILL.md`
- `skills/tools/documents-media/presentations/business-presentations/SKILL.md`
- `skills/tools/documents-media/presentations/shared/template-routing.md`
- `skills/tools/documents-media/presentations/shared/ppt-skill-routing.md`
- `profiles/presentation-desktop.json`
- `scripts/codex_marketplace_config.json` 中 `presentations` 当前入口
- `skills/tools/documents-media/presentations/shared/templates/cuhk/beamer/source/**`
- V1.0 Plan 与本轮 Critic request
- V0.2 与 045 Plan，仅作迁移/失败证据

还核对了 tracking Issues #29–#48：当前都仍 open、带 `maintenance-track`，source maturity 仍以 canonical TODO 为准。

## 3. 外部独立核查

### Beamer

CTAN 当前显示 Beamer 3.78（2026-08-20）；其 README 明确说明外观由 template system 控制，因此“共享语义/构图核心 + 少量受控 template adapter”是现实可行的，不需要另造 presentation class。Beamer 当前在 CTAN tagging 状态中仍为 Tagged PDF unsupported，因此 V1.0 不宣称现有 Beamer 路线已经完成 PDF/UA/tagged PDF 是正确的。

Sources:
- https://ctan.org/pkg/beamer
- https://ctan.org/texarchive/macros/latex/contrib/beamer

### ltx-talk

CTAN 当前的 `ltx-talk` 已到 0.6.7（2026-09-26），目标明确包含 tagged accessible PDF，但仍声明为 experimental，接口可能变化，而且开发优先级是 tagging/functionality、设计能力优先级较低。它值得继续跟踪，但现在替换现有 Beamer 双模板路线会引入迁移成本而不能解决 semantic/composition/TODO 根因，因此本轮不采用是合理的。

Sources:
- https://ctan.org/pkg/ltx-talk
- https://ctan.org/ctan-ann/pkg/ltx-talk

### 成熟第三方 Beamer theme

CTAN 有大量成熟 Beamer themes，但它们解决的是视觉皮肤和模板实现，不会解决当前 TODO 中 first-use、叙事连续性、review scope、existing-deck preservation、claim-first figure、自然语言或完成权问题；同时用户已冻结两个内置模板。因此本轮没有明显优于“双模板 + shared core”的第三方替代路线。

## 4. 已接受的架构判断

### 4.1 Semantic storyboard / page composition 分层：接受

V1.0 已把 semantic storyboard 限定在 audience state、page job、evidence、prerequisite、takeaway、visible/notes obligation、dependency 与 revision preservation，并显式禁止 `two-column`、`RESULT_FIGURE`、density、字号、坐标等视觉决定。

Page composition 再负责对象形态、主辅关系、阅读路径、空间比例、split/merge/fallback 和视觉角色。这个边界足够清楚，没有重演旧 `deck-plan.yaml` 的核心混责。

### 4.2 双模板：接受

- `cuhk-research` 以 exact source 为 authority；
- `course-standard` 只复现课程参考的视觉系统，不复制正文/例题/annotations；
- external locked input 不进入 built-in registry，也不成为默认 route；
- existing-deck revision 保留原 deck 模板。

因此“external locked input”与“保留现有 deck 模板”都不是隐藏的第三个内置模板。

### 4.3 Teaching 作为 shared-core mode：接受

没有证据支持再造一个 `teaching-presentations` 顶级 skill/plugin。Teaching 与 research/business 的真正共性是 source boundary、semantic sequence、composition、renderer/review；差异通过 mode policy 和 template routing 表达即可。

当前 `business-presentations` trigger 也不应现在退休。至少保留一个正式 release 的兼容入口是更安全的迁移策略。

### 4.4 #43 合并进 #33：接受

V1.0 的 citation/text-layer contract 已显式保留 `Source:` / `Figure:` / `Data:` / author-year 等 slide-level role labels，G6 也把 role-label drift 列为失败，因此合并不会丢掉 #43 的 house-style 能力。

### 4.5 #44 evidence-gated：接受

不预建新的 geometry engine 是正确的。现有 accepted geometry invariants 可以继续进入 regression bank；只有新的真实 deck 复现 renderer-level 缺口时，才做 bounded amendment。

### 4.6 045 已推广能力继续作为 regression：接受

footer safe zone、first-use、diagram geometry、space use、figure internal readability、English final pass 已经在 045 进入生产合同，但后来真实项目仍回归。V1.0 把它们当 regression 而不是“历史已完成”是正确的。

## 5. Blocking findings

### PRES-V1-F01 — 统一前门没有绑定真实 consumer，且默认 deliverable 对 business/editable route 有回归风险

**要求依据**

用户冻结决定要求：任何 PPT/deck/Beamer/Slides 创建、重构、返修、局部编辑都先进入 `presentations`，小编辑只能走轻量路径，不能绕过前门。

**直接证据**

当前 main 的真实 source 仍明确存在绕行：

- `research-presentations/SKILL.md`：minor text/color/alignment/object edit 不使用该 skill；
- `business-presentations/SKILL.md`：small existing PPTX/Slides edits 不触发；
- `shared/template-routing.md`：existing PPTX/Slides minor edit 直接进入官方 Presentation/Slides；
- `shared/ppt-skill-routing.md`：同样保留直接 adapter route；
- `scripts/codex_marketplace_config.json` 的 `presentations` description/defaultPrompt 仍围绕 research/business planning，并没有形成“所有 presentation intents 先统一 intake”的真实 discovery contract；
- `profiles/presentation-desktop.json` 的描述与 research skill 对 unspecified research format 的默认 CUHK 路由也存在语义不完全一致。

V1.0 只写了 Layer 1 和 Package A 的 “universal front-door routing”，没有冻结**哪个 canonical discovery/routing source 会被改、怎样保证自然请求实际先命中 presentations、再委托官方 adapter**。

同时 §3.2 的“未显式要求 editable PPTX/Slides 时，新的内置模板 deck 默认 .tex + PDF”容易与当前 business/marketing/executive 默认 editable PPTX 路线混淆。两模板决策并不要求 business deck 无格式请求改成 Beamer。

**真实风险**

实现者可以把 shared router 写得很漂亮，但 ChatGPT/Codex discovery 仍从旧 skill description/defaultPrompt/profile 绕过；或者为了“只有两个模板”把普通 business deck 静默改成 `course-standard` Beamer。这两种都是用户可见的正常入口错误。

**最小关闭条件**

V1.1 必须冻结一条可追踪的 normal-entry 因果链：

`natural request -> presentations plugin discovery/intake -> mode + deliverable + template decision -> shared core or local-edit -> official Presentation/Slides / Beamer adapter`

并明确：

1. 哪些 canonical source/consumer 负责 discovery 与 routing（至少覆盖 Marketplace/plugin config、source skills/shared routing、profile；generated layer仍只由 generator 重建）；
2. research、teaching、business/executive、existing deck、local edit、显式 PPTX/Slides、external locked template 的默认 deliverable matrix；
3. business/executive 无显式格式时是否继续 editable route；若改变，必须有用户决定，不得由 Planner默改；
4. local-edit 进入 presentations 后仍能立即轻量委托 adapter，而不运行 full storyboard/review；
5. G1 normal-entry evidence 直接从安装后的真实 plugin 发自然请求验证，而不是 helper trace。

---

### PRES-V1-F02 — #45–#48 的 evidence-gated maturity 被“全 TODO 覆盖”部分提前转成 production contract

**要求依据**

Canonical TODO 是 maintenance source truth；“覆盖全部 TODO”不等于无证据提升 maturity 或直接实现。Candidate/promotion gate 必须先满足，尤其本轮 Critic request 已明确要求保留 evidence-gated disposition。

**直接证据**

当前 main：

- #45 `CANDIDATE_GENERIC`：只有新的真实返修再次证明 deck-wide consistency 问题时才增加最小 contract；
- #46 `CANDIDATE_GENERIC`：新的 math-heavy real deck 再次出现后才进一步加强 theory-page hierarchy；
- #47 `CANDIDATE_GENERIC`：promotion gate 要求 simulation-heavy 与 real-data deck 都证明改善；
- #48 `CANDIDATE_GENERIC`：promotion gate 要求多个独立英文科研 slides 的真实证据，并先判断 owner 是 presentation 还是 writing layer。

V1.0 却把 #45 直接映射到 consistency pass + template roles + first-use，把 #46 变成 math/theory role contract，把 #47 变成 simulation page contract，把 #48 变成 Clear Writing/scientific-prose + G8；Package B/C 又把其中多项列为本轮 implementation scope。

其中“English final pass”作为 045 已推广 regression 可以继续执行，但这不等于 tracking #48 的更广泛“natural scientific slide language”已经满足 promotion gate。

**真实风险**

为了满足“TODO 全解决”而把 candidate 项全部写进 production，会把 CAT-TRACE 经验过早固化成跨项目规则，增加误杀合法页面、规则堆叠和 schema/validator 再膨胀的风险；同时破坏 canonical TODO 的 maturity truth。

**最小关闭条件**

V1.1 对 #45–#48 逐项只允许两种处理：

1. 提供当前已经满足其 promotion gate 的直接真实证据，并明确进行 Planner triage/promote；或
2. 保留原 evidence-gated maturity，把它放入对应 Gate 的 regression observation / future amendment 条件，本轮不新增该项专属 production mechanism。

允许复用已由 045 或其他已晋升条目建立的机制，但不得因此把 #45–#48 自动宣称 solved/promoted。

#44 继续保持当前 evidence-gated 结论。

---

### PRES-V1-F03 — G9/G10 把横向证据规则和 release closure 当成独立产品能力 Gate，Gate taxonomy 过重

**要求依据**

Capability Gate Policy 要求 Gate 证明可观察的用户能力；same-final-candidate identity、reviewer access/scope、release identity 等也必须成立，但它们可以是所有 Gate 的横向 validity/closure 条件，不应为了数量形成重复 Gate。

**直接证据**

- G9 的核心是 reviewer scope、independence、completion authority；
- G10 同时打包 cross-mode fresh tasks、installation/Marketplace/profile identity、README/changelog/version closure、same-final-candidate 防拼接；
- G2 与 G8 都包含 deck sequence/transition review；
- Policy 已独立规定所有 release gates 必须来自同一 final candidate，并要求 qualitative reviewer 能访问完整 artifact。

**真实风险**

Executor 可能花大量工作产出 review-scope、candidate-identity、release metadata 等 control artifacts，再把这些过程正确性当成新的产品 Gate；与此同时，G10 太大，任何失败难以判断究竟是 generalization、integration 还是 release metadata。Gate 的重复还会增加评审费用和 handoff 复杂度。

**最小关闭条件**

V1.1 重新整理 Gate taxonomy，不要求固定数量：

1. 把 G9 的 `review_scope / reviewer authority / no self-sign / full-artifact access` 变成所有需要定性判断 Gate 的横向证据有效性规则，同时保留 #29/#36 的 regression acceptance；
2. 把 same-final-candidate / no evidence stitching 变成所有 release Gate 的横向 final-candidate rule；
3. 将 G10 缩成真正独立的“跨模式正常入口 + generalization + production integration”能力，README/changelog/version 等放 release closure；
4. 明确 G2 只证明 semantic dependency/storyline，G8 只证明最终语言实现与口头可讲性，避免两者都重新判 transition/order；
5. G3 与 G4 可以继续分开：G3 是通用 composition/readability，G4 是 scientific-object-specific semantics/representation。

不要求机械拆 G5；但 G5 必须分别记录“canonical template 被真实消费”和“render visual fidelity”两类独立子证据，不能用一个总分互相抵消。教学可读性仍由 G3/G8 判，不由 G5 模板保真判。

---

### PRES-V1-F04 — Package B/C 仍不是 bounded implementation package

**要求依据**

每个 major stage 通过后必须增加真实用户能力；高成本/高耦合实现不能把多个独立架构风险藏进一个 Executor Goal。若 package 失败，应能明确定位到哪一层，而不是靠后续更多 validator 补洞。

**直接证据**

Package B 同时包含：

- semantic storyboard；
- composition contract；
- `deck-plan.yaml` compatibility；
- first-use/symbol/transition；
- primitive grammar；
- diagram、figure、math、simulation、model closure、Question；
- color/type/caption/source roles；
- G2/G3/G4。

Package C 同时包含：

- citations/bibliography/PDF text layer；
- Clear Writing handoff；
- full-deck review；
- review authority；
- actual existing-deck revision runtime；
- known/unrelated/fresh final batch；
- version/changelog/README/Marketplace/profile release closure；
- G6–G10。

**真实风险**

一次 Executor task 很容易出现：语义层改了一半、composition 同时改、revision runtime 又迁移、最后用 review/release artifacts 掩盖未完成的 production path。失败后也无法可靠归因，尤其 #45–#48 还处于 evidence-gated 状态。

**最小关闭条件**

V1.1 把 execution stages 调整为真正 bounded、可独立回滚、每阶段新增一个可观察能力。Critic 不强制固定拆法，但至少要把当前 B/C 拆开。一个可接受的参考形态是：

1. Front door + routing + two-template adapter foundation；
2. Semantic sequence core：page job / first-use / transition / advisor decision / audience firewall；
3. Composition + generic responsive hierarchy + 已批准 object regressions；
4. Delivery：citation/text layer + final language handoff；
5. Existing-deck revision runtime + preservation；
6. Cross-mode final integration/generalization + release closure。

Planner 可以给出更少的 package，只要每包有清楚的新用户能力、依赖、stop condition、recovery 和对应 Gate，且不把 candidate-only TODO 提前实现。

## 6. Non-blocking notes

### N01 — 双模板本身没有过度复杂

两个 built-in template + external locked pass-through 是当前最小足够产品边界。增加第三模板、主题市场或通用 geometry engine 都没有证据支持。

### N02 — `course-standard` 的“模板保真”和“教学可读性”必须分别验收

V1.0 已大体把二者放在 G5 与 G3/G8，这是正确方向。后续实现不要让“像 Chapter1”自动等于“适合讲课”，也不要为了教学优化擅自改变 frozen visual identity。

本 Critic 当前没有 `Chapter1.pdf` 原件，因此不对 exact course-standard visual fidelity 给 PASS；这不阻塞架构审查。Package/template implementation review 必须直接访问原参考 PDF 与真实 render。

### N03 — exact CUHK source provenance/license 在 Package A 做一次 closure

当前 bundled `beamerthemesintef.sty` header 明确记录了 Sapienza/SINTEF 派生关系与 GPL v3-or-later notice。V1.1/执行包应保留该 provenance/license，并区分 Beamer 本体许可、theme source 与 CUHK assets 的来源/redistribution 边界。无需因此重做现有模板，但 release 前不能让 derived tokens/helper 冒充 canonical source。

### N04 — 现有 render resource / 中文数学 / ToUnicode 路径不能在 shared-core migration 中被丢掉

当前 research skill 已有 `render-chinese-math-pdf` probe 与真实资源检查。Package A/D 的 resource/text-layer contract 应把它作为已有能力回归，而不是另造一套 probe。

### N05 — gold/reference library 没必要维持“强制存在感”

降为候选提示是正确的。若新 shared core 最终没有实际消费它，就应诚实标为 reference-only/retire from normal path；不要为了证明历史投入有用而增加一个 Gate。

## 7. 现实替代路线判断

| 路线 | 判断 |
|---|---|
| 继续给当前 `deck-plan.yaml` / validators 加规则 | **过简且方向错误**：已知真实失败证明 packet/schema 完整不等于 deck 可讲、可看、review scope 诚实。 |
| V1.0 的双模板 + shared semantic/composition core | **主方向采用，需上述窄幅修订**。 |
| 换成熟第三方 Beamer theme | **不采用**：只解决皮肤，不解决当前 TODO 根因，并违背用户冻结的内置模板边界。 |
| 现在改用 `ltx-talk` | **不采用本轮替换**：accessible/tagged PDF 方向更先进，但当前仍 experimental；不能解决现有 semantic/revision/review 问题。 |
| PPTX/Slides 为主、Beamer 为次 | **只在显式 editable / business 等正常路线保留**；不能取代 exact CUHK/course Beamer，也不能解决核心 TODO。 |
| 只加 `course-standard`、不重构 shared core | **过简**：会留下 current first-use、transition、review scope、revision、figure/diagram 等已知回归。 |

## 8. Capability Gate 总体判断

- G1：必要，但必须关闭 F01 后才可执行。
- G2：保留；证明 semantic sequence。
- G3：保留；证明 generic composition/readability。
- G4：保留；证明 scientific-object-specific behavior，但不能借机自动 promotion #46/#47。
- G5：保留；要求 template consumption 与 visual fidelity 两类证据分别成立。
- G6：保留；#43 已被保真合并。
- G7：保留；existing-deck revision 是独立用户能力。
- G8：保留但收窄为 final language/spoken reader effort。
- G9：改成横向 evidence-validity/completion rule，不作为独立产品能力 Gate。
- G10：收窄为 cross-mode normal-entry/generalization/integration；release metadata 另行 closure。

## 9. Machine-readable verdict

```text
RESULT = REVISE
REVIEW_OBJECT = PRESENTATIONS_TWO_TEMPLATE_PRODUCTION_REDESIGN_PLAN_V1_0
REVIEWED_PATH = docs/design/PRESENTATIONS_TWO_TEMPLATE_PRODUCTION_REDESIGN_PLAN_V1_0_2026-09-28.md
REVIEWED_COMMIT = 78901482243a877cdcec3150ca229b3fa58b7173
ARCHITECTURE_VERDICT = MAIN_DIRECTION_ACCEPTED_NARROW_REVISION_REQUIRED
TWO_TEMPLATE_VERDICT = PASS_ARCHITECTURE_ONLY
TODO_COVERAGE_VERDICT = REVISE_EVIDENCE_GATING_45_48
CAPABILITY_GATE_VERDICT = REVISE_HORIZONTAL_RULES_AND_G10_SCOPE
IMPLEMENTATION_PACKAGING_VERDICT = REVISE_SPLIT_B_C
MIGRATION_AND_RECOVERY_VERDICT = MOSTLY_SOUND_FRONT_DOOR_AND_EXISTING_ROUTE_NEED_EXPLICIT_BINDING
READY_FOR_EXECUTION_PACKAGE = NO
```

## 10. Maintenance Board pending mutation

本 Critic surface 没有 GitHub Project field mutation 能力，因此 **Project 尚未同步**。不要把以下内容理解成已执行。

Exact pending Project mutation:

```text
Project = AI Skills Maintenance
Issues = #29-#48
Area = presentations
Status = DOING
Current execution anchor =
  docs/design/PRESENTATIONS_TWO_TEMPLATE_PRODUCTION_REDESIGN_PLAN_V1_0_2026-09-28.md
  @ 78901482243a877cdcec3150ca229b3fa58b7173
Next action =
  Planner submits full V1.1 addressing PRES-V1-F01 through PRES-V1-F04,
  then independent Critic re-review.
Resolution commit = unset
Source maturity/status = unchanged
Issues remain open
```

## 11. Next handoff

```text
NEXT_HANDOFF=PLANNER
```

Planner 必须提交完整 V1.1，而不是零散 patch。优先复核四个旧 blocker，不得因为本轮 REVISE 顺手扩大成第三模板、新 skill、新 workflow、geometry engine、Bridge Kit 或新的状态机。
