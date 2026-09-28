# Presentations 双模板生产架构重设计 Plan

Plan version: 1.1
Status: READY FOR CRITIC REVIEW / NOT EXECUTION AUTHORIZATION
Date: 2026-09-28
Repository: YuukiAS/AI_Skills_Collection
Target plugin: presentations
Design topic / task key: presentations--two-template-production-redesign
Source branch/ref: main
Repository baseline reviewed: 21c739b270105c222f523fd5625993fa5902e00f
Supersedes as current proposal: PRESENTATIONS_TWO_TEMPLATE_PRODUCTION_REDESIGN_PLAN_V1_0_2026-09-28.md
Critic review addressed: results/presentations--two-template-production-redesign/CRITIC_REVIEW_V1.md @ 21c739b270105c222f523fd5625993fa5902e00f

本文件是完整 V1.1，不是 V1.0 的补丁。V1.0、旧 V0.1/V0.2 与 045 继续保留为历史设计和真实失败证据；只有本 V1.1 在获得独立 Critic PASS 后，才可作为后续 execution package 的设计依据。

本轮只冻结产品入口、双模板架构、shared-core 权责、TODO disposition、Capability Gates、实施分期、迁移与恢复以及 release closure。它不修改 production source，不创建 Executor task，不运行付费 review，不发布，也不改变任何 canonical TODO maturity。

---

## 0. V1.0 Critic blocker disposition

### PRES-V1-F01 — ACCEPT

V1.1 将“所有 PPT 先进入 presentations”绑定到现有真实 consumer，而不是只增加一条 shared routing 文档：

natural presentation request
-> installed Presentations plugin discovery/intake
-> mode + deliverable + template decision
-> shared core 或 local-edit fast path
-> official Presentation/Slides adapter 或 Beamer adapter
-> artifact/render QA

Source/consumer authority 冻结如下：

1. scripts/codex_marketplace_config.json
   - canonical plugin packaging/interface source；
   - 负责 Presentations 的 display description、default prompts、shared payload 与 source skill 暴露；
   - 必须覆盖 research、teaching、business/executive、existing-deck revision、local edit、editable PPTX/Slides 和 explicit Beamer intents，而不是只描述 research/business planning。

2. skills/tools/documents-media/presentations/research-presentations/SKILL.md
   skills/tools/documents-media/presentations/business-presentations/SKILL.md
   skills/tools/documents-media/presentations/shared/*routing*.md
   - canonical domain/shared routing source；
   - research/business skills 继续作为兼容触发入口；
   - “small existing PPTX/Slides edit 不触发 presentations”这类旧边界必须改成：不进入 full research/business planning，但仍经过 Presentations intake 后立刻走 local-edit fast path；
   - shared routing 决定 mode、deliverable、template 与 adapter，不由 generated layer 再发明一套逻辑。

3. profiles/presentation-desktop.json
   - installation/composition profile，不是第二套路由 authority；
   - description 与所装 skills 必须与 canonical routing 一致；
   - 不得用 profile 文案覆盖 plugin/source routing。

4. plugins/codex/plugins/** 与 .agents/plugins/marketplace.json
   - generated layer；
   - 只能由现有 generator 从 canonical source 重建；
   - 禁止手工 patch；
   - release gate 验证 generated parity 与 installed identity。

G1 必须从真实安装后的 Presentations plugin 发送自然语言任务验证 discovery/intake；helper trace、直接脚本调用或测试 fixture 不能替代 normal-entry evidence。

### PRES-V1-F02 — ACCEPT

V1.1 不再把 #45–#48 自动 promotion：

- #44 保持 BLOCKED_NEEDS_EVIDENCE，不新建 geometry engine。
- #45 保持 CANDIDATE_GENERIC。本轮只复用已经由 #29/#32/#38/045 等独立已具证据机制覆盖的回归，不新增“#45 专属 deck-wide consistency contract”，也不宣布 #45 solved。
- #46 保持 CANDIDATE_GENERIC。本轮不新增独立 math/theory hierarchy 机制；只保留现有 theory 页面能力与 #38 已有真实证据支持的尺度/空间回归。未来只有 theorem/statistical-method real deck + unrelated math-heavy regression 满足 canonical promotion gate 后才 amendment。
- #47 保持 CANDIDATE_GENERIC。本轮不新增 simulation/metric 专属生产 contract；已有 simulation 页面只作为回归观察。promotion 仍要求 simulation-heavy 与 real-data deck 的真实 render 共同证明新的 pattern 有价值。
- #48 保持 CANDIDATE_GENERIC。本轮继续执行 045 已正式推广的 English final pass，以及 #29/#31/#34 已有真实证据支持的 audience/page-job/coherence handoff，但不因此把更广义 “natural scientific slide language” 宣布 promoted/solved。若要形成新的跨 presentation/writing owner contract，必须重新满足 #48 promotion gate。

Canonical source maturity 保持当前真实值；本设计文件只给实施 disposition，不修改 TODO 状态。

### PRES-V1-F03 — ACCEPT

V1.1 删除“review authority”和“same final candidate”作为独立产品 Gate 的做法。

改为：

- 横向证据有效性规则 H1：review scope 必须诚实；需要定性判断的 Gate 必须让 reviewer 看到完整 required artifact；generator/Executor 不能 self-sign final PASS；局部 review 不能发全局 PASS。
- 横向 final-candidate 规则 H2：所有 release gates 必须绑定同一 final candidate 和同一 production identity；禁止跨 commit/evidence stitching、换赢家、挑最好一次。
- 横向回归规则 H3：cheap known regressions + should-not-change 先跑；fresh evidence 只能在候选与 rubric 冻结后使用；已用于调优的样本不再叫 fresh。
- 横向 source/artifact identity 规则 H4：source、loaded runtime、renderer/template、final artifact、reviewed render 必须是同一候选链。

Product Gate taxonomy 收敛为 G1–G9：
G1 normal-entry routing；
G2 semantic dependency/storyline；
G3 generic composition/readability；
G4 domain/scientific-object representation；
G5 template actual consumption + visual fidelity；
G6 citation/bibliography/text-layer delivery；
G7 existing-deck revision/preservation；
G8 final language/spoken reader effort；
G9 cross-mode normal-entry/generalization/production integration。

README/changelog/version/Marketplace/profile parity 属于 release closure，不再冒充产品能力 Gate。

### PRES-V1-F04 — ACCEPT

V1.1 将原 Package B/C 拆成六个 bounded implementation stages。每个阶段只新增一项可观察能力，并写明依赖、对应 Gate、停止条件与恢复边界。Candidate-only #44–#48 不因“全 TODO 覆盖”被提前实现。

---

## 1. 冻结用户目标

### 1.1 统一前门

以后任何演示文稿任务都必须先进入 Presentations plugin，包括：

- new research deck；
- teaching/tutorial/lecture deck；
- business/executive/product/strategy deck；
- seminar、paper talk、QE、oral、defense；
- existing deck revision；
- 单页/单对象/local edit；
- editable PPTX/Slides；
- Beamer/LaTeX slides；
- external locked template；
- plan/storyline-only。

“先进入 Presentations”不等于所有任务都走完整 planning。local edit 必须是 fast path；显式 editable PPTX/Slides 继续交给官方 Presentation/Slides adapter。

### 1.2 内置模板只有两个

A. cuhk-research
- 正式科研、组会、导师讨论、research update、seminar、paper talk、journal club、QE/oral/defense。
- canonical source: skills/tools/documents-media/presentations/shared/templates/cuhk/beamer/source/
- exact template identity 必须由 canonical source 真实消费，不能由 derived tokens/reference deck 冒充。

B. course-standard
- Tutorial、lecture、课程讲解、公式推导、通用非品牌教学 Beamer。
- 根据用户提供的 Chapter1.pdf 复现视觉系统，不复制课程正文、例题、批注或高亮 annotations。
- 目标视觉：4:3；黑色顶部带；蓝色 frame-title 带；白色正文；蓝色 bullet；右下页码；sans 正文与兼容数学字体；支持目录、定义、例子、推导、算法、表格、references。

External locked template：
- 用户、课程、会议、client 或 venue 明确提供的模板只作为 current-task locked input；
- 不进入 built-in template registry；
- 不成为第三个默认模板；
- existing deck revision 必须保留原模板，除非用户明确授权换模板。

### 1.3 两模板不等于两种输出格式

“两种内置模板”只约束 repository 自带 Beamer template library，不改变可编辑办公演示的正常路线。

Business/executive 无显式格式时继续默认 editable PPTX/Slides。
显式 PPT/PowerPoint/.pptx/editable/Slides/Google Slides 时继续默认 official Presentation/Slides。
因此本轮不把 business/editable route 静默改成 Beamer。

---

## 2. 已核实的 repository 与外部现实

### 2.1 Repository current reality

当前 main baseline 21c739b270105c222f523fd5625993fa5902e00f：

- presentations plugin version = 0.3；
- capability status = baseline；
- Marketplace source config 仍描述 research/business planning，并暴露 research-presentations 与 business-presentations；
- presentation-desktop profile 当前描述仍提到 editable PPTX/Slides default routing；
- research/business source skills 当前仍有 small/minor existing PPTX edit 不触发自身 skill 的边界；
- shared routing 同时保留 Beamer、editable PPTX/Slides、existing-deck edit 路线；
- generated plugin layer 从 source config/skills/shared 生成，不是 source authority。

这些事实正是 F01 要解决的入口不一致，不应被 V1.1 隐藏。

### 2.2 External re-check, 2026-09-28

本轮针对性重新核对 CTAN：

- Beamer 当前为 3.78（2026-08-20），仍是成熟 presentation class，外观通过 template system 控制；CTAN 仍标记 Tagged PDF unsupported。
- ltx-talk 当前为 0.6.7（2026-09-26），目标包含 tagged accessible PDF，但官方仍明确称 experimental，接口可能变化，设计能力优先级低于 tagging/functionality。

采用决定保持不变：

- Beamer：RUNTIME_DEPENDENCY / ADOPTED。
- ltx-talk：REVIEWED_NOT_ADOPTED in this round。
- tagged-PDF guidance：REFERENCE_ONLY；本轮不宣称 PDF/UA。
- 第三方 Beamer themes：不采用为第三内置模板。

这轮 blocker 都来自 repo normal entry、TODO maturity、Gate taxonomy 与 implementation scoping；外部 re-check 没有产生要求改主路线的新事实。

---

## 3. Normal-entry 因果链与 routing matrix

### 3.1 Canonical normal-entry chain

真实目标链固定为：

natural request
-> Presentations plugin discovery/intake
-> classify task mode
-> decide deliverable
-> decide template policy
-> run shared core or local-edit fast path
-> call official Presentation/Slides or Beamer adapter
-> produce/render artifact
-> apply risk-matched QA
-> final delivery

任何实现若只能通过内部脚本、fixture 或直接点名某个 child skill 才成立，不能证明 G1。

### 3.2 Task modes

1. new-deck
   - 新建完整 deck；
   - 非平凡任务必须经过 source/evidence boundary、semantic sequence、composition、adapter、render QA。

2. existing-deck-revision
   - 基于 reviewer-seen baseline、用户/导师批注继续返修；
   - 必须 preservation-aware；
   - 不能重新生成一套无关 deck。

3. local-edit
   - 标题、颜色、对齐、页码、一个对象、一处文字或类似局部改动；
   - intake 后立即进入 fast path；
   - 不创建 full semantic storyboard；
   - 保留当前 format/template；
   - 编辑后只强制 affected-page/affected-object render 与必要 should-not-change，比 full-deck review 轻；
   - 若局部改动会改变 storyline、evidence、跨页 first-use 或 accepted element，则自动升级到 existing-deck-revision，而不是静默扩大。

4. plan-only
   - 只交付 storyline、页级 plan、speaker notes、semantic sequence；
   - 不声称已经生成或验证 deck。

### 3.3 Default deliverable matrix

| 用户任务 | 默认 mode | 默认 deliverable | 模板/adapter |
|---|---|---|---|
| 组会、科研进展、导师讨论，无格式指定 | new-deck | .tex + PDF + renders | cuhk-research Beamer |
| seminar、paper talk、journal club，无格式指定 | new-deck | .tex + PDF + renders | cuhk-research Beamer |
| QE、oral、defense，无 venue template | new-deck | .tex + PDF + renders | cuhk-research Beamer |
| Tutorial、lecture、课程讲解，无格式指定 | new-deck | .tex + PDF + renders | course-standard Beamer |
| 泛用非品牌 Beamer/LaTeX slides | new-deck | .tex + PDF + renders | course-standard，除非用户指定 CUHK |
| business/executive/product/strategy/client deck，无格式指定 | new-deck | editable PPTX/Slides | official Presentation/Slides；不强制内置 Beamer 模板 |
| 明确 PPT/PowerPoint/.pptx/editable/Slides/Google Slides | new-deck 或 revision | editable PPTX/Slides | official Presentation/Slides；若用户给 locked template 则保留 |
| 明确 Beamer/LaTeX/.tex/academic PDF | new-deck | .tex + PDF + renders | 按 research/teaching context 选两个内置模板；显式模板优先 |
| existing deck + 批注/继续返修 | existing-deck-revision | 保持原 source/format + revised render | preserve current template，除非明确授权换 |
| 一个标题/颜色/对齐/对象等局部修改 | local-edit | 保持原 source/format | preserve current template；直接轻量 adapter |
| 用户/venue/course/client 提供锁定模板 | 任一适用 mode | 按模板支持的 source/format | external locked input，不注册为第三 built-in |
| 只要 storyline/逐页计划/notes | plan-only | semantic plan/notes | 不要求模板 render |

### 3.4 Discovery/consumer changes that later implementation must make

Stage 1 执行包必须明确修改和验证以下 canonical layers：

- Marketplace plugin config：Presentations description/default prompts 覆盖所有 presentation intents；
- research/business source skill boundaries：small/minor edit 不再“绕过 plugin”，而是“绕过 full domain planning，进入 shared local-edit fast path”；
- shared routing：以本 matrix 为唯一 format/template decision source；
- presentation-desktop profile：只描述已安装能力组合，不再与 shared routing 产生不同默认；
- generated layer：只通过 generator 重建；
- normal-entry regression：从真实安装后的 plugin 发自然请求，验证 mode/deliverable/template 结果。

如果平台实际 discovery 无法让自然 presentation request 进入已安装 Presentations plugin，Stage 1 必须 BLOCKED_DISCOVERY_CONSUMER，而不是增加隐式 invocation flag、新 top-level skill 或声称文档已经解决。

---

## 4. Shared-core architecture

### Layer 1 — Intake and routing

输入：用户自然请求、现有 artifact、显式 format/template、受众、场景。
输出：mode、deliverable、template policy、source boundary、是否 fast path。

不决定 storyline，不决定 layout。

### Layer 2 — Source and evidence boundary

为非平凡新建/返修任务建立可追踪 source anchors：论文页码、报告章节、代码结果、数据、已有 slide、批注、图表、引用等。

Domain owner 决定专业语义。Presentations 可以指出缺解释/缺证据，但不得为了讲故事而改变：
- estimand；
- scientific claim；
- formula；
- uncertainty；
- image/data meaning；
- citation support relation。

缺证据时只能：标未知、转 next step、放 notes/backup 或删除。

### Layer 3 — Semantic sequence core

只决定：
- audience_before / audience_after；
- page_job；
- source/evidence anchors；
- prerequisites / first-use dependency；
- intended takeaway / decision contribution；
- visible-content obligation vs notes/backup；
- incoming dependency / outgoing unresolved question；
- revision preservation constraint。

严格禁止在 semantic layer 写：
- two-column / three-column；
- RESULT_FIGURE 等 page morphology；
- density；
- font size；
- coordinates；
- dominant object；
- renderer-specific primitive。

Deck-level sequence 必须解释为什么 page k 产生 page k+1 的需要，而不是只给 section list。

### Layer 4 — Page composition

只决定：
- text/equation/table/plot/image/diagram/mixed form；
- dominant/supporting objects；
- reading path；
- spatial proportion；
- split/merge/full-width/side-by-side；
- responsive fallback；
- template-relative type/math scale、accent roles、caption/source region。

Composition 不得：
- 改 page order；
- 改 evidence boundary；
- 加强或削弱 scientific claim；
- 发明 transition；
- 改 accepted revision scope。

Diagram 先判断 relationship 是否值得画，再进入已有 geometry invariants；本轮不新建 geometry engine。

### Layer 5 — Domain / writing / visualization handoffs

- statistical-modeling / medical-imaging / bioinformatics 等：专业有效性。
- scientific-visualization：plot/image encoding、axes、uncertainty、presentation-specific redraw。
- Clear Writing / writing-style：在结构、formula、claim、citation 冻结后处理 reader-facing wording。
- presentations：提供 audience/page-job/context brief，接受返回文案后重新检查长度、first-use、口头可讲性和 rendered fit。

Writing layer 不接管 layout；Presentations 不接管 domain truth。

### Layer 6 — Artifact adapter

A. Beamer adapters
- cuhk-research；
- course-standard；
- external locked TeX template when supplied。

B. official editable adapter
- PPTX/Slides/Google Slides；
- 不增加第三 built-in template；
- 不用 whole-slide images 冒充 editable objects。

Adapter 消费 composition contract，不决定 story。

### Layer 7 — Render QA and bounded repair

按 mode 风险匹配：
- local-edit：affected pages/objects + should-not-change；
- new-deck：per-page render + contact sheet + required source/text/citation checks；
- existing-deck-revision：baseline diff + accepted-element preservation + targeted feedback + full relevant regression。

Review 服从横向 H1–H4，不允许 self-sign 或 scoped-global mismatch。

---

## 5. 两模板合同

### 5.1 cuhk-research

Canonical source：
skills/tools/documents-media/presentations/shared/templates/cuhk/beamer/source/

冻结身份：
- 约 16:9；
- CUHK purple #72256D；
- Times New Roman family where current exact source specifies；
- title slide；
- top section navigation/logo；
- footline/navigation/page number；
- template-relative body/source/footer safe zone。

Canonical exact source 必须真实进入编译。以下 derived convenience assets 不能冒充 exact source：
- design tokens；
- derived main.tex；
- reference PPTX；
- convenience builder/helper。

现有 theme provenance/license 和 CUHK assets 的 redistribution boundary 在 Stage 1 implementation review 做 closure；不因此重做模板。

### 5.2 course-standard

Reference source：用户提供 Chapter1.pdf，仅作 private/reference input，不进入 ordinary plugin payload。

Frozen visual identity：
- 4:3；
- 黑色 top band；
- 蓝色 frame-title band；
- 白色正文；
- 蓝色 bullet；
- 右下页码；
- sans 正文与 Computer Modern/兼容数学；
- 教学型 sparse hierarchy；
- 不含 CUHK branding；
- 不复制课程正文、例题或 references；
- 不复制黄色/橙色/绿色/青色 PDF Highlight annotations。

Template fidelity 与 teaching readability 分开验：
- G5：实际 template consumption + visual fidelity；
- G3/G8：教学页面的 composition/readability/spoken flow。
二者不能互相抵消。

### 5.3 External locked input

只在用户/venue/course/client 明确给出时使用。
不进入 built-in registry。
不成为默认 route。
existing-deck revision 默认沿用当前 deck template。

---

## 6. TODO #29–#48 完整 disposition

本表是 V1.1 的设计 disposition，不修改 canonical source maturity。

| TODO | 当前 maturity | V1.1 disposition | 本轮是否新增专属 production mechanism | 主要 Stage/Gate |
|---|---|---|---|---|
| #29 v13/v14 consolidated feedback | NEW | 分解到 sequence、composition、delivery、review regressions；作为真实 failure bank | 是，但按其独立已发生失败分别进入已有 layer，不造一个 #29 mega-validator | S2/S3/S4/S5；G2/G3/G4/G6/G8 + H1 |
| #30 advisor question decision/answerability | NEW | semantic sequence 中加入 decision-value/answerability/presenter-leaning/likely-pushback notes contract | 是 | S2 / G2 |
| #31 sentence/slide transitions mechanical | NEW | transition map 与 end-state -> next-page dependency | 是 | S2 / G2；final prose only in G8 |
| #32 accent colour semantic roles | NEW | composition layer template-relative semantic roles；ordinary prose neutral | 是 | S3 / G3 |
| #33 citation + bibliography + text layer | NEW | one delivery contract；authoritative metadata + role labels + text extraction | 是 | S4 / G6 |
| #34 pre-writing audience/page-job brief | NEW | semantic brief before visible prose handoff | 是 | S2 / G2 |
| #35 full-deck audience-context/responsive-layout | NEW | full contact-sheet reader-effort + responsive fallback；不只 edited lines | 是 | S3 / G3 |
| #36 coverage can self-certify feedback | NEW | requirement-level acceptance evidence + H1 reviewer authority/scope | 是 | S5 + H1 |
| #37 packet can miss obvious rendered regressions | NEW | real high-res pixel evidence；collision/readability cannot be replaced by packet presence | 是 | S3/S5 / G3/G7 + H1 |
| #38 formula/text/emphasis scale drift | NEW | role-driven scale and unused-space/readability checks | 是 | S3 / G3 |
| #39 diagram semantic-purpose before geometry | NEW | utility gate + existing geometry invariants；不新建 engine | 是 | S3 / G4 |
| #40 paragraph/list/table primitives drift | NEW | minimal information-relationship grammar + limit redundant containers | 是 | S3 / G3 |
| #41 model closure missing | NEW | semantic layer decides when audience must reassemble model；composition realizes only when needed | 是 | S2/S3 / G2/G4 |
| #42 Question/Background primitive | NEW | responsive full-width/bottom fallback；minimum readable size | 是 | S3 / G3 |
| #43 slide source/figure citation style | NEW | merged into #33，保留 Source/Figure/Data/author-year role distinction | 否，使用 #33 contract | S4 / G6 |
| #44 diagram canonical geometry | BLOCKED_NEEDS_EVIDENCE | 保持 evidence-gated；只保留 already-accepted geometry regressions | 否 | future amendment only |
| #45 deck-wide style/terminology hierarchy | CANDIDATE_GENERIC | 保持 candidate；本轮只观察已有 #29/#32/#38/first-use 能力是否顺带降低漂移，不新增 #45 consistency engine | 否 | regression observation；future amendment after promotion gate |
| #46 math/theory hierarchy | CANDIDATE_GENERIC | 保持 candidate；不新增独立 theory-role production contract；现有 theory behavior + #38 scale regression继续 | 否 | regression observation；future amendment only after canonical gate |
| #47 simulation/metric structured facts | CANDIDATE_GENERIC | 保持 candidate；不新增 simulation-specific layout/table schema | 否 | regression observation；future amendment after simulation-heavy + real-data evidence |
| #48 natural scientific slide language | CANDIDATE_GENERIC | 保持 candidate；继续 045 English final pass及 #29/#31/#34 handoff，不声明 #48 solved/promoted | 否 | G8 observation；future owner/promotion amendment |

### 6.1 #29 子项显式覆盖

#29 内独立失败不会被“#29 一行”吞掉：

- first-use ordering：S2/G2；
- scoped review cannot global PASS：H1；
- new/rewrite page pre-writing brief：S2/G2；
- internal planner/version labels firewall：S2/G2 + S4/G8 wording；
- diagram utility + visual floor：S3/G4；
- example-to-takeaway explanatory bridge：S2/G2；
- spoken scientific language second pass：S4/G8，使用已有 writing handoff；
- simplification cannot delete why an object exists：S2/G2；
- first-use across all visible text layers：S2 final-visible scan + G2；
- result figure redrawn around claim：S3/G4 + scientific-visualization；
- diagram geometry cumulative：existing regression bank，S3/G4；不触发 #44 promotion；
- math symbol cross-slide first-use/conditioning level：S2/G2；不触发 #46 promotion；
- oracle/generative vs fitted simulation jobs：作为 #29 real regression in S2/G2；不新增 #47 generic contract；
- compare final language against best accepted readability baseline：S4/G8 + H3 regression rule。

---

## 7. Product Capability Gate Matrix

### G1 — Normal-entry routing and deliverable preservation

Capability:
自然 presentation 请求进入 Presentations plugin，并得到正确 mode、deliverable、template/adapter。

Why distinct:
证明 discovery/routing，不证明 deck 内容质量。

Normal entry evidence:
从真实安装后的 plugin 发自然请求，至少覆盖：
- research no-format；
- teaching no-format；
- business/executive no-format；
- explicit PPTX/Slides；
- existing-deck revision；
- local edit；
- external locked template。

PASS evidence:
实际 intake/selected route 与 §3 matrix 一致；business/editable route 未被双模板改成 Beamer；local edit 未跑 full planning。

FAIL:
自然请求绕过 plugin；source skill/shared/profile 给出冲突路线；business 无格式被 silent Beamer；local edit被重做。

Regression boundary:
显式 format/template 始终高于默认；existing deck 保持原 format/template。

Final candidate:
YES。

### G2 — Semantic dependency and storyline

Capability:
在不先决定页面形态的情况下，形成 audience-aware sequence：page job、prerequisite、first-use、transition、decision question、audience-copy firewall、必要的 model reassembly。

Why distinct:
只证明 “为什么这一页现在出现、听众前后状态怎么变”，不判 layout 或 prose polish。

Evidence:
真实 research/teaching deck semantic sequence + final-visible first-use scan；至少一个 advisor decision scene。

FAIL:
术语/符号先用后讲；page k 结束状态不能解释 page k+1；内部 Planner label 泄漏；discussion question不改变任何决策；需要 reassembly 的复杂模型讲完后仍无法恢复整体关系。

Regression boundary:
不写 layout family、dominant object、font/geometry；不新增 #46/#47 专属 contract。

Final candidate:
YES。

### G3 — Generic composition, hierarchy and responsive readability

Capability:
把 semantic brief 转成可读页面，不依赖 domain-specific科学语义判断。

Evidence:
真实 render 覆盖 text/equation/table/figure mix、responsive fallback、role colour、scale hierarchy、Question/Background、paragraph/list/table selection、crowding+unused-space。

FAIL:
一边拥挤一边空；主对象偏小；窄栏继续缩字；普通 prose 任意 accent；简单关系被拆成多卡片+diagram+prose；明显碰撞仍判 PASS。

Regression boundary:
intentional sparse take-home slide不被 occupancy 指标误杀；合法 compact diagram不因机械阈值失败。

Final candidate:
YES。

### G4 — Domain/scientific-object representation

Capability:
需要 plot/image/diagram/model-closure 等科学对象时，presentation form服务于真实 claim/relationship。

Evidence:
至少一个 claim-first result figure、一个 diagram utility case、一个 complex model reassembly case；domain owner/visualization owner能够核对科学语义。

FAIL:
analysis figure直接缩小搬上去；diagram比两句话更慢且无科学关系；edge/node已有已接受几何回归再次出现；model closure只是重复无信息流程图；presentation自行改估计目标/不确定性。

Regression boundary:
不自动实现 #44/#46/#47 candidate-only mechanisms。

Final candidate:
YES。

### G5 — Template actual consumption and visual fidelity

Capability:
两个 built-in template 都从 canonical/approved source 真实消费并得到对应视觉身份。

两个不可互相抵消的子证据：

A. Actual consumption
- cuhk-research build 直接消费 canonical CUHK source；
- course-standard build 直接消费 approved reconstructed source；
- manifest/source hash/compile path 可证明实际使用，不是颜色模仿。

B. Visual fidelity
- render 与 frozen reference identity 对比；
- CUHK title/header/footer/logo/safe-zone；
- course-standard 4:3、黑/蓝 bands、body/bullet/page number/font character；
- annotations 明确不存在。

A PASS B FAIL 或 A FAIL B PASS 都是 Gate FAIL。

Teaching readability 不在 G5 判，由 G3/G8 判。

Regression boundary:
external locked input不进入 built-in registry；existing-deck template preservation不由此强制换皮。

Final candidate:
YES。

### G6 — Citation, bibliography and PDF text delivery

Capability:
research deck 的可见 source roles、References metadata 与 PDF text layer 可验证。

Evidence:
role-labelled on-slide citations；authoritative bibliography metadata；PDF extraction/copy checks覆盖普通数字、年份、页码、citation text、主要中英文。

FAIL:
混用 house style；论文题名被模型改写；支持关系错误；视觉正常但数字/年份/引用复制乱码；source/footer不可读。

Regression boundary:
不宣称 full PDF/UA/tagged PDF。

Final candidate:
YES。

### G7 — Existing-deck revision and preservation

Capability:
普通“继续按批注返修”真正执行 diagnose -> plan -> edit -> render -> compare，而不是只校验 packet。

Evidence:
reviewer-seen baseline、accepted-element ledger、targeted feedback、actual source diff、rerender、requirement-level closure、unrelated-page regression。

FAIL:
重新生成新 deck；比较错误 baseline；accepted element被改坏；只生成 packet/READY 状态却没有像素级问题关闭；local feedback被扩成 global redesign。

Regression boundary:
user明确授权 global redesign时可另开 new-deck/revision scope，不被 preservation错误阻止。

Final candidate:
YES。

### G8 — Final language and spoken reader effort

Capability:
结构与科学含义冻结后，可见 slide copy/notes 能自然讲出来，且不改变事实。

Evidence:
使用当前已正式存在的 writing-fidelity / scientific-prose / chinese-prose 或 Clear Writing handoff；final render reread；spoken explanation检查；页面文字长度与节奏。

FAIL:
noun stacks、memo labels、机械 What/Where/How、内部流程词、句子各自正确但口头不连贯；writing handoff改了 formula/number/citation/claim strength。

Regression boundary:
G8 不再判 page order/first-use；这些属于 G2。#48 maturity保持 candidate。

Final candidate:
YES。

### G9 — Cross-mode normal-entry, generalization and production integration

Capability:
同一 final candidate 在主要模式和真实安装身份下工作，不是只对 CAT-TRACE/Chapter1 特判。

Evidence:
风险匹配的跨模式 final batch至少覆盖：
- research Beamer；
- teaching Beamer；
- business/editable；
- existing-deck revision 或 local-edit 中至少一个，并对另一个做 should-not-change；
- external locked template pass-through 的最小兼容检查。

任务数量不机械固定；由改动 blast radius 和 Critic pre-final review 冻结。

FAIL:
只在 helper/fixture成功；换 candidate拼证据；只 CAT-TRACE selector有效；安装后的 plugin/Marketplace/profile 与被测 source不一致；某模式被 silent fallback。

Regression boundary:
不要求每种任务都使用两个内置 template；business/editable 保持 official adapter。

Final candidate:
YES。

---

## 8. 横向 evidence-validity / completion rules

这些规则不是额外产品 Gate，但任何相关 Gate 不满足就不能用于 release claim。

### H1 — Scope-honest independent review

- reviewer request 显式记录 review_scope、reviewed_requirements、unreviewed_requirements；
- global PASS 只有 mandatory global requirements 全部被实际查看后才合法；
- generator/Executor/self-inspection 不能给 final qualitative PASS；
- reviewer 必须直接拿到 Gate 所需完整 render/source/evidence；
- #29 scoped-global PASS failure 与 #36 self-certification regression 固定进入 acceptance。

### H2 — Same final candidate / no stitching

- 所有 release gates 指向同一 commit/candidate、同一 installed production identity；
- 不把不同 commit 各自 PASS 拼成 release PASS；
- 不在失败后换样本/换赢家并仍称原 final batch PASS。

### H3 — Regression bank and fresh-evidence integrity

- cheap deterministic regressions 与 should-not-change 先跑；
- CAT-TRACE known failures作为开发回归，可反复用，但不再叫 fresh；
- fresh/generalization batch 只在 candidate + rubric 冻结后运行；
- grader/reviewer修复与 product修复分别记录。

### H4 — Source/render/runtime identity

- canonical source、generated payload、installed plugin、renderer/template source、final artifact、reviewed render必须可追踪到同一候选链；
- derived template helper不能冒充 canonical source；
- final PDF/PNG必须来自真实待交付 source。

---

## 9. Bounded implementation stages

所有 stage 都需要后续 execution-ready Planner package + Critic PASS 才能实现。本 V1.1 不授权执行。

### Stage 1 — Front door + routing + two-template adapter foundation

新增真实用户能力：
所有 presentation intents 先进入 Presentations，并在不破坏 editable/business route 的前提下正确选择 mode/deliverable/template；course-standard 获得可真实编译的模板基础。

Scope:
- Marketplace plugin config/interface；
- source research/business boundaries；
- shared routing；
- presentation-desktop profile一致性；
- cuhk exact adapter identity/provenance regression；
- course-standard reconstruction adapter；
- generated parity only via generator；
- G1 + G5 foundation。

Explicit non-goals:
- 不实现 semantic storyboard；
- 不新建 universal composition schema；
- 不改 writing-style；
- 不改 existing-deck runtime；
- 不实现 #44–#48 candidate mechanisms。

Dependencies:
current plugin 0.3、两模板 source/reference、official adapter availability。

Stop conditions:
- natural installed plugin request仍无法进入 Presentations；
- 为了统一前门需要新顶级 skill/plugin/implicit invocation hack；
- course-standard fidelity 需要复制 restricted course content；
- exact CUHK provenance/license/asset boundary无法确认。

Recovery:
保持 main 的 0.3 route；回滚 Stage 1 branch changes；不手改 generated layer。

Primary Gates:
G1；G5 的 actual consumption/fidelity。

### Stage 2 — Semantic sequence core

新增真实用户能力：
新 deck 在写 visible prose/决定 layout 前，先形成 audience-aware、dependency-aware sequence。

Scope:
- page job/audience before-after；
- pre-writing brief (#34)；
- first-use across visible layers；
- transition map (#31)；
- advisor decision-value/answerability (#30)；
- audience-copy firewall；
- #29 example->takeaway、simplification-preserves-purpose、symbol/conditioning first-use；
- model reassembly need detection (#41 semantic half)；
- compatibility import from old deck-plan where required，但不扩旧 schema。

Non-goals:
- 不决定 columns/layout；
- 不实现 #45 consistency engine；
- 不实现 #46/#47 candidate contracts；
- 不改 renderer geometry。

Dependencies:
Stage 1 intake stable；source/evidence anchors可用。

Stop conditions:
- semantic layer开始承载 layout/density/renderer geometry；
- old deck-plan compatibility要求继续增加新字段；
- model/simulation/math要求迫使 #46/#47提前 promotion。

Recovery:
保留 Stage 1 routing/template foundation；退回 current planning artifacts；不改变 renderer。

Primary Gate:
G2。

### Stage 3 — Composition + approved visual/object regressions

新增真实用户能力：
semantic brief 能变成可投影、响应式、claim-first 的页面，并能挡住历史明显视觉回归。

Scope:
- generic composition/readability；
- crowding + unused space；
- responsive split/reflow；
- #32 semantic accent roles；
- #38 formula/text/emphasis scale；
- #40 paragraph/list/table grammar；
- #42 Question/Background responsive primitive；
- #39 diagram utility + already-accepted geometry invariants；
- result-figure claim/readability；
- #41 model closure realization；
- footer/source safe zone；
- figure internal readability/caption pairing；
- local high-res render evidence。

Non-goals:
- 不建新 geometry engine (#44)；
- 不建立 #45 deck consistency engine；
- 不建立 #46 theory taxonomy；
- 不建立 #47 simulation layout schema。

Dependencies:
Stage 2 semantic contracts；existing renderer/render QA。

Stop conditions:
- 解决 diagram回归需要 renderer-wide geometry subsystem；
- 为通过 Gate需要硬编码 CAT-TRACE page/method；
- generic occupancy阈值开始误杀 sparse pages。

Recovery:
保留 semantic core；composition feature按 primitive/regression小范围回滚，不影响 routing/template。

Primary Gates:
G3、G4。

### Stage 4 — Delivery: citation/text layer + final language handoff

新增真实用户能力：
最终 research/teaching deck 的引用可验证、PDF文本可复制，且 visible language 在科学结构冻结后经过真实 reader-facing final pass。

Scope:
- #33 + #43 consolidated citation contract；
- bibliography authoritative metadata；
- PDF text extraction/ToUnicode checks；
- 现有 render-chinese-math-pdf/resource probe regression；
- 045 English final-pass completion；
- #29 spoken scientific language second pass；
- Chinese writing-fidelity + chinese-prose when applicable；
- final language reread；
- 不改变 #48 maturity。

Non-goals:
- 不修改 writing-style production semantics；
- 不宣称 PDF/UA；
- 不重判 semantic order（G2 owner）。

Dependencies:
Stage 2/3 structure和layout稳定；writing skills可用。

Stop conditions:
- Clear Writing/scientific-prose 本身无法保持事实/formula/citation；
- text-layer修复要求替换 renderer/class；
- 需要修改 writing-style production behavior才能闭环。

Recovery:
Presentations 返回 NEEDS_WRITING_OWNER 或 renderer-specific blocker；不在本 task 顺手改 writing-style/ltx-talk。

Primary Gates:
G6、G8。

### Stage 5 — Existing-deck revision runtime + preservation

新增真实用户能力：
“继续按这些批注返修现有 deck”从 validator evidence checker 变成真正的 production revision runtime。

Scope:
- diagnose reviewer-seen baseline；
- accepted-element ledger；
- feedback-to-requirement mapping；
- bounded edit；
- rerender；
- compare against correct baseline；
- requirement-level acceptance evidence；
- affected/full-deck risk-matched regression；
- local-edit escalation boundary；
- #36/#37 real closure。

Non-goals:
- 不重新设计 unrelated slides；
- 不新增 workflow/state machine；
- 不让 validator packet变成新的产品中心。

Dependencies:
Stage 1 routing；Stage 2/3/4 contracts可复用。

Stop conditions:
- 无法拿到 reviewer-seen baseline；
- source不可编辑且用户未授权替代路线；
- accepted-element scope存在冲突；
- revision要改变核心 storyline/模板但用户只授权局部返修。

Recovery:
保持 current existing-deck gate为 evidence checker；返回 BLOCKED/REVISE，不自动重生成新 deck。

Primary Gate:
G7，且受 H1–H4 约束。

### Stage 6 — Cross-mode integration/generalization + release closure

新增真实用户能力：
同一 final candidate 能通过主要真实模式的 normal-entry，并作为一致的安装/发布版本交付。

Scope:
- G9 risk-based cross-mode final batch；
- full generated parity；
- actual installed plugin identity；
- final pre-release Critic review；
- version/changelog/README/Marketplace/profile closure；
- maturity decision based on evidence；
- rollback instructions。

Non-goals:
- 不在 final batch看结果后继续调产品；
- 不把 candidate-only #44–#48强行清空；
- 不用 release metadata弥补能力 Gate失败。

Dependencies:
Stage 1–5 PASS；final candidate冻结。

Stop conditions:
- 任一 release Gate失败；
- evidence来自不同 candidate；
- fresh sample被用于调优；
- generated/installed identity与 source不一致；
- README/changelog/version无法诚实描述实际能力。

Recovery:
不发布；main继续使用 presentations 0.3 或最后已发布版本；失败返回对应 owner stage，而不是靠 successor编号重置证据。

Primary Gate:
G9 + all relevant G1–G8 final-candidate requirements + H1–H4。

---

## 10. Migration plan

### 10.1 research/business triggers

至少保留一个正式 release 周期的兼容 trigger：

- research-presentations；
- business-presentations。

它们逐步变成 mode-specific entry/reference，不再各自拥有完整生产架构。
Teaching 作为 shared-core mode，不新增 teaching-presentations 顶级 skill/plugin。

是否以后合并/退休 business-presentations，不属于本轮；需要真实 route/evidence 后重新 Planner–Critic。

### 10.2 deck-plan.yaml

迁移原则：
- 不再继续扩展为 universal production IR；
- Stage 2 可以提供 compatibility reader/import/export；
- 新 semantic/composition contracts不通过给旧 schema继续加字段实现；
- 至少保留一个兼容 release窗口；
- 只有 normal production、revision、tests和真实用户任务均不再需要旧 IR后才可提出 retirement；
- retirement需要单独 migration evidence，不在当前设计里硬删。

### 10.3 Existing-deck validator

当前 validate_existing_deck_revision_entry.py 继续作为历史 evidence checker，不被包装成“runtime 已完成”。
Stage 5 才构建 normal entry 的 diagnose -> edit -> render -> compare 行为。
若 Stage 5失败，保留现有 validator，不影响 Stage 1–4独立能力。

### 10.4 Gold/reference library

从 hard gate 降为 optional candidate/reference。
若 production最终不消费某资源，则诚实标 REFERENCE_ONLY/retire from normal path；不为了历史投入强行保留 Gate。

### 10.5 Render resources

必须保留现有 render-chinese-math-pdf probe、字体/TeX package、writable cache、PDF QA 与当前 workstation render-resource contract。
不得在 shared-core migration 中又造一套资源发现机制。

---

## 11. Regression bank and should-not-change

Known real regressions continue to include：

- first-use / dependency-order；
- scoped reviewer global-PASS error；
- accepted-element regression；
- diagram short/detached arrows、node crowding、text-edge collision；
- figure internal text too small；
- crowding + unused page space；
- source/footer safe zone；
- formula scale drift；
- Question narrow-column shrink；
- natural-English final pass miss；
- PDF text extraction corruption；
- paragraph/list/table over-structuring；
- claim-first figure miss。

Should-not-change至少包括：

- intentionally sparse take-home/transition slide；
- legitimate compact diagram；
- figure-free math slide；
- explicit editable PPTX route；
- business/executive no-format editable route；
- explicit external locked template；
- local edit不被升级成 full deck；
- existing deck accepted pages不被无关改变。

Candidate-only TODO #44–#48可以作为 observation维度，但除非 canonical promotion gate在未来被满足，否则不能把 release failure自动解释为“必须实现候选机制”。

---

## 12. Release closure

### 12.1 Version decision for this design task

Repository bump decision: NONE
Reason: V1.1 是 design/review 文档，不改变 production behavior。

Affected plugins:
- presentations: NO_BUMP
  Reason: production source/runtime 尚未修改。
- writing-style: NO_BUMP
- workflow-core: NO_BUMP
- ai-skills-core: NO_BUMP

### 12.2 Future implementation release

若 Stage 1–6 最终作为一个 coherent user-facing improvement batch 完成并准备发布，且 current released presentations 仍为 0.3，则按版本政策预计：
- presentations 0.3 -> 0.4，exactly once；
- repository 只在形成正式可安装 release 时按当时 current VERSION 判断通常为 PATCH，而不是因为本设计“很大”自动 MINOR。

若期间另有 presentations release，最终版本号必须从当时 canonical marketplace config重新计算，不能引用本 Plan 猜测。

### 12.3 README

最终 release 必须显式检查 README。
本轮预计有 README-facing变化：
- 所有 presentation intents统一进入 Presentations；
- 两个 built-in templates；
- research/teaching/business/editable routing；
- normal deliverables。

因此真正 release时 README大概率必须同步。Executor不得用“code/tests完成”跳过。
如果最终实现并未改变这些 reader-facing信息，closure必须记录 README checked: no update required，并说明理由。

### 12.4 Generated layer

Canonical edits只能发生在 source：
- scripts/codex_marketplace_config.json；
- skills/tools/documents-media/presentations/**；
- profiles/**；
-必要 shared scripts/templates/tests/docs。

Generated：
- plugins/codex/plugins/**；
- .agents/plugins/marketplace.json；
以及当前 generator维护的其他 generated/catalog payload。

Generated layer只能通过现有 generator重建并验证 source/generated parity，禁止手改。

### 12.5 Maturity

当前 capability status仍是 baseline。
一次 V1.1 architecture PASS不改变 maturity。
最终 Stage 6也不能因 Gate PASS自动升 stable；需多个独立真实任务长期证明后由用户/Planner单独决定。

---

## 13. Failure attribution and recovery

失败必须先归因到：

1. discovery/routing -> Stage 1；
2. semantic sequence -> Stage 2；
3. composition/object render -> Stage 3；
4. citation/text/language -> Stage 4；
5. revision/preservation -> Stage 5；
6. cross-mode integration/install/release -> Stage 6；
7. domain science -> 对应 domain owner；
8. writing skill本身 -> writing owner；
9. renderer/template -> adapter/render resource owner；
10. reviewer misread/scope -> H1 review process。

普通 stage失败不得自动：
- 新建 successor；
- 新建 skill/plugin；
- 修改 Bridge Kit；
- 增加新状态；
- promote #44–#48；
- 扩成全库架构重构。

只有失败证明 V1.1 核心架构或权责不成立时，才回 Planner–Critic revision。

---

## 14. Explicit non-goals

本轮及后续按此设计的默认实现禁止：

- 第三个 built-in template；
- teaching-presentations 新顶级 skill/plugin；
- 新 geometry engine；
- 新 workflow/state machine/ledger/database；
- Bridge Kit change；
- ltx-talk migration；
- full PDF/UA claim；
- CAT-TRACE page/method-specific selectors；
- Chapter1 content copying；
- automatic promotion #44–#48；
- gold-layout hard gate；
- whole-slide image fake editable PPTX；
- infinite reviewer/repair loop。

---

## 15. Completion definition for the architecture round

本 V1.1 只有在独立 Critic 明确 PASS 后，才结束 architecture round。

该 PASS只批准：
- normal-entry consumer chain；
- routing/deliverable matrix；
- two-template contract；
- strict semantic/composition boundary；
- TODO disposition；
- G1–G9 + H1–H4 taxonomy；
- six-stage implementation decomposition；
- migration/recovery/release boundaries。

PASS不授权：
- implementation；
- branch/worktree；
- paid review；
- external account/credential；
- production installation；
- release；
- version bump。

Critic PASS后，Planner下一步应为 Stage 1 准备独立 execution package（Proposal/Plan + Canonical Goal + Kickoff Draft）并再次送 execution-ready Critic review；不得把六个 Stage一次性塞给一个 Executor。

---

## 16. Maintenance Board pending mutation

Canonical source maturity保持当前真实值，Issues #29–#48不在本设计轮次改 maturity。

当前 surface若不能在满足 Clear Writing前置要求的情况下直接修改 GitHub Project，则不要声称已同步。下一次 Project-capable AI Skills Maintainer/Codex 应在核对 current evidence 后机械应用：

Project: AI Skills Maintenance
Area: presentations
Issues: #29–#48
Status: DOING

Current execution anchor:
docs/design/PRESENTATIONS_TWO_TEMPLATE_PRODUCTION_REDESIGN_PLAN_V1_1_2026-09-28.md
@ <V1.1 plan commit>

Next action:
Independent Critic V1.1 review, prioritizing PRES-V1-F01 through PRES-V1-F04.

Do not:
- change source maturity；
- mark PROMOTED/DONE；
- close issues；
- add candidate-only implementation claims。

V1.1 plan commit产生后，由 Planner handoff文件填入 exact locator。
