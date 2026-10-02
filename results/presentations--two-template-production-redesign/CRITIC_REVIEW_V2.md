# Presentations 双模板生产架构 V1.1 — Critic Review

**Review object:** `PRESENTATIONS_TWO_TEMPLATE_PRODUCTION_REDESIGN_PLAN_V1_1`  
**Review stage:** `architecture_revision_review_v1_1`  
**Target repo:** `YuukiAS/AI_Skills_Collection`  
**Target plugin/domain:** `presentations`  
**Task key:** `presentations--two-template-production-redesign`  
**Source branch/ref:** `main`  
**Reviewed proposal:** `docs/design/PRESENTATIONS_TWO_TEMPLATE_PRODUCTION_REDESIGN_PLAN_V1_1_2026-09-28.md`  
**Reviewed proposal commit:** `f71e97c06938ab2ce175ccf3b4ac19da9309fda1`  
**Planner response:** `results/presentations--two-template-production-redesign/PLANNER_RESPONSE_V1_1.md`  
**Planner response commit:** `b7b6499f4ac2cbd50c19f12005ac24b66cbd0b48`  
**Critic request:** `results/presentations--two-template-production-redesign/CRITIC_REVIEW_REQUEST_V2.md`  
**Current main inspected:** `28ac05a53a857b8259bfdc4165bbbc5e95366d76`  
**Verdict:** **PASS**

## 1. 用户可读结论

V1.1 已经把上一轮四个 blocker 实质关闭，可以结束本轮 architecture round。

这次不是“把文档写得更完整”就放行。四处原本会直接导致错误实现的结构问题都已经改变：统一前门现在绑定到真实 Marketplace/source-skill/shared-routing/profile/generated-layer 消费链，并明确保护 business/editable 与 local-edit fast path；#44–#48 的 canonical maturity truth 得到保留，不再为了“清完 TODO”偷 promotion；Capability Gates 已把产品能力与 review/final-candidate/source-identity 等横向证据规则分开；原来过大的 B/C 已拆成六个可独立执行、停止和恢复的 stage。

本 PASS 只批准 V1.1 的架构、TODO disposition、Gate taxonomy、stage decomposition、migration/recovery/release boundary。它不授权实现、不创建 branch/worktree、不授权付费 review、不批准 production install、version bump 或 release。下一步应由 Planner **只为 Stage 1** 准备 execution package（Proposal/Plan + Canonical Goal + Kickoff Draft），再送独立 Critic 做 execution-ready review。

从上一轮 Critic commit `21c739b270105c222f523fd5625993fa5902e00f` 到当前 main，Git compare 只新增 V1.1 Plan、Planner response 与本轮 Critic request，没有 production source 修改；因此本轮审查对象仍然是设计，不是实现成品。

## 2. 复核旧 blocker

### PRES-V1-F01 = CLOSED

上一轮问题是“所有演示文稿先进入 Presentations”只存在于设计叙述，没有绑定真实 discovery/routing consumer，而且可能把 business/editable route 错改成 Beamer。

V1.1 已冻结完整因果链：

```text
natural presentation request
-> installed Presentations plugin discovery/intake
-> mode + deliverable + template decision
-> shared core / local-edit fast path
-> official Presentation/Slides or Beamer adapter
-> artifact/render QA
```

并明确 source/consumer authority：

- `scripts/codex_marketplace_config.json`：canonical plugin packaging/interface source；
- research/business source skills + shared routing：内部 dispatch authority；
- `presentation-desktop`：安装/组合 profile，不是第二套路由 source；
- `plugins/codex/plugins/**` 与 `.agents/plugins/marketplace.json`：generated-only；
- local edit 仍先经过 Presentations intake，但绕过 full planning，进入 fast path。

Deliverable matrix 也明确保护：
- research/group meeting/seminar/QE/oral/defense 无格式 -> `cuhk-research` Beamer；
- tutorial/lecture/teaching 无格式 -> `course-standard` Beamer；
- business/executive/product/strategy/client 无格式 -> editable PPTX/Slides；
- explicit PPTX/Slides -> official editable adapter；
- existing deck/local edit -> preserve current format/template；
- external locked template -> current-task pass-through；
- plan-only -> 只交语义计划，不伪装完成 deck。

G1 明确要求从真实安装后的 Presentations plugin 发自然请求验证，helper/fixture/direct script 不能替代。

当前 main 仍然保留旧 routing 文案，这是 Stage 1 要修改的真实 source，不构成架构失败；V1.1 已把“实际平台 discovery 若无法做到”定义为 Stage 1 fail-closed stop condition，而不是通过 implicit invocation hack 或新顶级 skill 绕过。

### PRES-V1-F02 = CLOSED

Canonical TODO 当前仍保持：

- #44 = `BLOCKED_NEEDS_EVIDENCE`
- #45 = `CANDIDATE_GENERIC`
- #46 = `CANDIDATE_GENERIC`
- #47 = `CANDIDATE_GENERIC`
- #48 = `CANDIDATE_GENERIC`

V1.1 的 TODO disposition 与这组 maturity truth 一致。

关键点是：Stage 2/3/4 只继续使用已有独立真实 failure 已经支持的能力，例如 #29 的 first-use、oracle-vs-fitted distinction、045 English final pass、#38 scale regression、#39 diagram utility、#41 model reassembly need；它没有把这些既有机制重新包装成 #45 consistency engine、#46 theory taxonomy、#47 simulation schema 或 #48 broader natural-language contract。

六个 stage 的 non-goals 也显式禁止偷跑 #44–#48 candidate-only mechanisms。V1.1 正确地把“TODO 全覆盖”解释为 truthful disposition，而不是“每个 TODO 都必须实现”。

### PRES-V1-F03 = CLOSED

V1.1 已把 Product Gates 收敛为 G1–G9，并把横向有效性规则移到 H1–H4：

- H1：scope-honest independent review；
- H2：same-final-candidate / no stitching；
- H3：regression/fresh-evidence integrity；
- H4：source/runtime/render identity。

这四项不再冒充新的用户能力 Gate。

G2 现在只判 semantic dependency/storyline：page job、audience state、prerequisite、first-use、transition、decision logic；G8 只判 final wording/spoken reader effort，不重新决定 page order。G3 与 G4 的边界也清楚：前者是 generic composition/readability，后者是 scientific-object semantics/representation。

G5 保持一个 Gate，但明确要求两个不可互相抵消的证据流：
A. canonical template actual consumption；
B. visual fidelity。
任一失败都使 G5 FAIL。

G9 现在承担的是 cross-mode normal-entry/generalization/production integration。README/changelog/version 等已经移到 release closure，不再当成产品能力。

一个轻微重复仍存在：G9 的 failure 示例提到“换 candidate 拼证据”，而 H2 已专门负责这一规则。但这只是 Gate failure 描述引用横向规则，不形成第二套检查或 control artifact，因此不构成 blocker。

### PRES-V1-F04 = CLOSED

原来的 Package B/C 已拆为六个 bounded stages：

1. Front door + routing + two-template adapter foundation；
2. Semantic sequence core；
3. Composition + approved visual/object regressions；
4. Citation/text layer + final language handoff；
5. Existing-deck revision runtime + preservation；
6. Cross-mode integration/generalization + release closure。

每个 stage 都写明：
- 一个可观察的新用户能力；
- scope / explicit non-goals；
- dependencies；
- stop conditions；
- recovery；
- primary Gate。

Stage 1 没有提前造 universal composition IR；Stage 2 禁止 layout/density；Stage 3 只做已有直接真实 evidence 支持的 composition/object regressions；Stage 4 遇到 writing owner 本身失败会停止，不顺手改 writing-style；Stage 5 明确是 `diagnose -> plan -> edit -> render -> compare`，不是 validator 再包一层；Stage 6 只有在 Stage 1–5 PASS 后才做跨模式 integration/generalization 与 release closure。

这个拆法已经达到 bounded implementation package 的要求。后续不能把六个 stage 再合并成一个 Executor Goal。

## 3. TODO 完整性

### #29

#29 的全部独立 failure 均有显式映射，而不是被一行 “covered” 吞掉：

- first-use ordering -> S2/G2；
- scoped review cannot global PASS -> H1；
- new/rewrite pre-writing brief -> S2/G2；
- internal planner/version label firewall -> S2/G2 + S4/G8；
- diagram utility + visual floor -> S3/G4；
- example-to-takeaway bridge -> S2/G2；
- spoken scientific language second pass -> S4/G8；
- simplification preserves object purpose -> S2/G2；
- all-visible-text first-use -> S2/G2；
- claim-first result figure -> S3/G4；
- cumulative diagram geometry -> existing regression bank, S3/G4；
- symbol/conditioning-level first-use -> S2/G2；
- oracle/generative vs fitted simulation job distinction -> #29 real regression in S2/G2，不创建 #47 generic contract；
- best accepted readability baseline -> S4/G8 + H3。

### #30–#43

这些当前 NEW 条目都获得了与原 failure 匹配的机制/Stage/Gate，而不是仅写表格：

- #30 advisor decision value -> S2/G2；
- #31 transitions -> S2/G2；
- #32 semantic accent roles -> S3/G3；
- #33 citation/bibliography/text layer -> S4/G6；
- #34 pre-writing brief -> S2/G2；
- #35 full-deck responsive reader-effort -> S3/G3；
- #36 review self-certification -> S5 + H1；
- #37 packet misses visible regression -> S3/S5 + G3/G7/H1；
- #38 scale hierarchy -> S3/G3；
- #39 diagram utility + existing invariants -> S3/G4；
- #40 paragraph/list/table grammar -> S3/G3；
- #41 model reassembly need + realization -> S2/S3 + G2/G4；
- #42 Question/Background responsive primitive -> S3/G3；
- #43 merged into #33 while retaining `Source:` / `Figure:` / `Data:` / author-year role distinction -> S4/G6。

### #44–#48

均保持 evidence-gated/candidate status，不作为本轮必须清空的 production TODO。PASS 不改变 canonical source maturity。

## 4. Normal-entry red-team result

V1.1 已对上一轮主要绕行路径给出明确架构防线：

- Marketplace description/defaultPrompt 未来 Stage 1 必须扩展到 teaching/local-edit 等 intents；
- child source skill 不再拥有“small edit bypass plugin”权力；
- shared routing 是 mode/deliverable/template decision source；
- profile 不再是第二套 routing authority；
- generated layer只能 generator 重建；
- business/executive 无格式保持 editable；
- explicit PPTX/Slides 不被两个 Beamer template 劫持；
- external locked template 不进 built-in registry；
- local edit 不运行 full storyboard；
- existing deck preservation 高于默认模板；
- plan-only 不声称生成 artifact。

真正的 platform/plugin discovery 是否能在当前安装机制下实现仍是 Stage 1 要用 normal entry 直接证明的事实。V1.1 没有把这个未知当已完成能力，因此不阻塞 architecture PASS。

## 5. Architecture red-team result

未发现 V1.1 引入新的架构级 blocker：

- semantic layer 没有重新出现 columns/layout/density/dominant object；
- composition 明确不得重排 story、改 evidence boundary 或 claim；
- Stage 1 明确不建 universal composition schema；
- `deck-plan.yaml` 只保 compatibility read/import/export，且 retirement 需要未来独立 migration evidence；
- gold/reference library允许诚实降为 REFERENCE_ONLY；
- H1 要求 reviewer直接拿到完整 required artifact，不允许 scope 字段自证；
- H2/H4 防止 source/generated/installed/render/review candidate identity 拼接；
- candidate TODO不能以“regression”名义偷 promotion；
- helper/fixture不能满足 G1/G9 normal-entry evidence。

## 6. Migration / recovery

迁移和恢复边界足够明确：

- research/business triggers至少保留一个正式兼容 release；
- `deck-plan.yaml` 不再扩职责，也不在本轮提前删除；
- existing-deck validator降为 evidence checker，Stage 5 才负责真实 runtime；
- gold/reference library可以降为 REFERENCE_ONLY；
- `render-chinese-math-pdf`、TeX/font/cache/PDF QA 等现有资源 contract 明确保留；
- current `presentations 0.3` / 最后已发布版本仍是 rollback boundary；
- generated layer只由 generator重建；
- README/version/changelog/maturity只在真实 release closure处理。

## 7. External re-check

2026-09-28 再次核对 CTAN：

- Beamer 当前为 3.78，日期 2026-08-20；CTAN 仍标注 Tagged PDF unsupported。
- `ltx-talk` 当前为 0.6.7，日期 2026-09-26；其目标包含 tagged accessible PDF，但 package 仍明确声明 experimental，接口可能变化，且开发优先级偏 tagging/functionality 而非 design。

因此没有出现足以推翻当前 Beamer 主路线的新事实。

References:
- https://ctan.org/pkg/beamer
- https://ctan.org/pkg/ltx-talk
- https://ctan.org/ctan-ann/pkg/ltx-talk

## 8. Non-blocking notes

### N1 — Stage 6 execution package 要把 pre-final Critic 放在 frozen final batch 之前

V1.1 已包含 final pre-release Critic review，但真正的 Stage 6 execution package 需要明确顺序：开发回归/代表性完整产物 -> pre-final Critic -> 冻结 candidate/rubric/final batch -> final generalization evidence -> release closure。当前只是 architecture round，且下一步只准备 Stage 1，因此不阻塞 V1.1 PASS。

### N2 — G2/G4 对 model reassembly 的双层职责要在实现包继续保持“need vs realization”

S2 已明确只判断是否需要 reassembly，S3/G4负责视觉实现。后续不要让 G2 通过检查最终布局来重新侵入 composition，也不要让 G4重新决定 story sequence。当前 Plan 的 owner 边界足够清楚，不阻塞。

### N3 — Chapter1 visual fidelity 仍属于 Stage 1 artifact review，不属于本轮架构 PASS

本 Critic 没有把未直接审查的 private/reference `Chapter1.pdf` 视觉细节冒充已验收事实。V1.1 只冻结 reconstruction contract；Stage 1 implementation review 必须直接取得 reference 与真实 render，分别验证 G5 actual consumption 和 visual fidelity。

## 9. Verdict

```text
PRES-V1-F01 = CLOSED
PRES-V1-F02 = CLOSED
PRES-V1-F03 = CLOSED
PRES-V1-F04 = CLOSED

RESULT = PASS

REVIEW_OBJECT = PRESENTATIONS_TWO_TEMPLATE_PRODUCTION_REDESIGN_PLAN_V1_1
REVIEWED_PATH = docs/design/PRESENTATIONS_TWO_TEMPLATE_PRODUCTION_REDESIGN_PLAN_V1_1_2026-09-28.md
REVIEWED_COMMIT = f71e97c06938ab2ce175ccf3b4ac19da9309fda1

PLANNER_RESPONSE = results/presentations--two-template-production-redesign/PLANNER_RESPONSE_V1_1.md
PLANNER_RESPONSE_COMMIT = b7b6499f4ac2cbd50c19f12005ac24b66cbd0b48

CRITIC_REQUEST = results/presentations--two-template-production-redesign/CRITIC_REVIEW_REQUEST_V2.md
CURRENT_MAIN = 28ac05a53a857b8259bfdc4165bbbc5e95366d76

ARCHITECTURE_VERDICT = PASS
NORMAL_ENTRY_VERDICT = PASS_ARCHITECTURE_CONTRACT_STAGE1_MUST_PROVE_REAL_DISCOVERY
TWO_TEMPLATE_VERDICT = PASS
TODO_COVERAGE_VERDICT = PASS_TRUTHFUL_DISPOSITION_NO_CANDIDATE_PROMOTION
CAPABILITY_GATE_VERDICT = PASS_G1_G9_WITH_H1_H4_HORIZONTAL_RULES
IMPLEMENTATION_STAGING_VERDICT = PASS_SIX_BOUNDED_STAGES
MIGRATION_AND_RECOVERY_VERDICT = PASS

READY_FOR_EXECUTION_PACKAGE = YES
```

## 10. Scope of PASS

本 PASS 只批准 V1.1 architecture、TODO disposition、Capability Gate taxonomy、six-stage decomposition、migration/recovery/release boundaries。

它不授权：
- implementation；
- execution branch/worktree；
- paid review；
- production installation；
- external account/credential；
- version bump；
- release。

下一步只能回 Planner，为 **Stage 1** 准备同一版本的：

1. Stage 1 Proposal/Plan；
2. Stage 1 Canonical Goal；
3. Stage 1 Kickoff Draft。

三者齐全后，再送独立 Critic 做 execution-ready review。未经过该 review，不能启动 Stage 1 Executor。

## 11. Maintenance Board pending mutation

当前 Critic surface没有 GitHub Project field mutation能力，因此 Project sync **未执行、未声称已同步**。

Exact pending mutation:

```text
Project = AI Skills Maintenance
Area = presentations
Issues = #29-#48
Status = DOING

Current execution anchor =
  results/presentations--two-template-production-redesign/CRITIC_REVIEW_V2.md
  @ <this review commit>

Next action =
  Planner prepares Stage 1 execution package:
  Proposal/Plan + Canonical Goal + Kickoff Draft,
  then independent execution-ready Critic review.

Resolution commit = unset
Source maturity/status = unchanged
Issues remain open
Do not mark PROMOTED/DONE or close issues.
```

## 12. Next handoff

```text
NEXT_HANDOFF=PLANNER
```

Planner 下一步只准备 Stage 1 execution package，不得把 Stage 2–6 合并进同一个 Goal，也不得把本 architecture PASS 当成 implementation authorization。
