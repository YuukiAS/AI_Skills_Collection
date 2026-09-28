# Product UI Copy Cross-Plugin Planner — 2026-09-28

你现在是 `YuukiAS/AI_Skills_Collection` 的跨插件 Planner。

这是第二阶段设计任务，目标是解决 **Frontend Design + Clear Writing 在真实产品 UI 文案上的 ownership、routing、自然度和 rendered acceptance 缺口**。

这是 **PLANNING ONLY**。

不要实现代码。
不要修改 production Skill。
不要 bump plugin version。
不要关闭 TODO。
不要修改 CUHK Date 产品。
不要创建 Executor Goal。
不要因为已有候选方案就直接假设一定要新增 Skill。

---

## 一、先读取最新事实

Repository:

`YuukiAS/AI_Skills_Collection`

Branch:

`main`

先同步最新 `origin/main`。

本 Prompt 编写时当前 HEAD 为：

`72ebd56705713c01d05fef34ccab1c5c04c15671`

如果 main 已前进，以最新 main 为准，并记录实际 source commit。

至少读取：

- `results/web-development--frontend-design-production-consolidation/FINAL_REPORT.md`
- `docs/plugin-changelogs/web-development.md`
- `docs/plugin-todos/web-development.md`
- `skills/tools/frontend/frontend-visual-systems/SKILL.md`
- `skills/tools/frontend/product-ux-planning/SKILL.md`
- `skills/tools/frontend/responsive-accessibility-review/SKILL.md`
- `scripts/codex_marketplace_config.json`
- `docs/plugin-todos/writing-style.md`
- `skills/writing/core/writing-fidelity/SKILL.md`
- `skills/writing/core/chinese-prose/SKILL.md`
- `docs/design/READER_FACING_COMMUNICATION_PLUGIN_BOUNDARIES.md`
- `docs/design/product-ui-copy/evidence/CUHK_DATE_PRODUCT_COPY_NATURALNESS_AUDIT_2026-09-26.md`
- `docs/SKILL_AUTHORING.md`

按需继续读取上述文件引用的直接相关证据。

---

## 二、当前已经冻结的前提

### Frontend Design

Frontend Design / `web-development` 已完成第一阶段 consolidation：

- plugin version = `0.3`
- repository release = `5.3.1`
- normal production entry 已改成 coordinator-first
- `frontend-visual-systems` 是 normal Frontend Design coordinator
- `product-ux-planning`、visual direction、tokens、Figma、motion、responsive/accessibility、webapp-testing、research-product frontend 是按需 delegates
- `implementation-react-tailwind` 保持 downstream，不是 design owner
- 已建立 S1/S2/S3 scale-down
- canonical Figma 是条件性 authority，不强制所有项目使用 Figma
- browser evidence 与 native-WebView evidence 已分开
- producer self-QA / handoff reachability / whole-product taste 已进入 production contract
- Bobbio / Lucerna / Asteria replay 为 compatibility/regression PASS
- maturity 仍为 `unclassified`，这不代表 Frontend Design 不可使用；只是还没有足够新项目长期证据把 maturity 提升到 baseline/alpha/stable

本任务不得重新设计或推翻这套 Frontend Design 0.3 基础架构，除非发现与 Product UI Copy integration 有直接冲突，并明确说明。

### Clear Writing

`writing-style` / Clear Writing 当前 version = `0.3`。

现有：
- `writing-fidelity`
- `chinese-prose`
- `scientific-prose`
- `scientific-rewrite`

其中 `chinese-prose` 已主要服务中文报告、README、科研/技术材料、说人话终审等长文本/段落级任务。

不要因为 Product UI Copy 问题破坏已经可用的科研/技术中文路线。

---

## 三、本轮精确 scope

本轮只处理以下 cross-plugin 缺口。

### Frontend Design 侧

以 TODO 标题作为 durable locator：

`Product UI copy needs an explicit Frontend Design content-architecture contract`

注意：当前 TODO 文本里的 `tracking: #73` 与仓库其它插件 Issue 编号存在历史 collision，因此 **不要把 #73 当唯一 durable identity**。本任务必须使用 TODO 标题 + 文件路径定位。

Frontend Design 侧核心问题：

- 决定 UI 位置到底需不需要文字；
- 决定文字是什么 UI role；
- 决定该说多少；
- 判断是否与邻近 copy 重复同一产品状态；
- 判断问题属于 content architecture、wording/localization、product semantics 还是 legal/trust；
- 把 frozen UI role/context 交给 Writing；
- Writing 返回后，仍由 Frontend Design 在真实 rendered surface 做 page-level / viewport-level acceptance。

### Clear Writing 侧

直接 scope：

1. `writing-style #17`
   `Product UI microcopy should state user consequence, not internal implementation reassurance`

2. `writing-style #20`
   `Product UI copy naturalness needs a dedicated microcopy capability, not more long-form prose rules`

另外必须审查但 **不默认实现/关闭**：

3. `writing-style #13`
   `Promote writing-style into the generic content-preserving language layer`

只回答：
- #13 是否已经提供本任务需要的底层 language/fidelity ownership；
- 是否存在必须一起补的 routing seam；
- 还是 Product UI Copy 可以作为独立 bounded capability，而不重新开启整个 #13 大任务。

除非证据证明存在直接依赖，否则不要顺手处理：
- #12 README
- #14 advisor-facing English
- #15 scientific slide microcopy
- #16 versioned Chinese technical docs
- #18 academic-humanizer
- #19 general style-cleanup boundary

---

## 四、真实问题证据

核心 evidence：

`docs/design/product-ui-copy/evidence/CUHK_DATE_PRODUCT_COPY_NATURALNESS_AUDIT_2026-09-26.md`

这是已知 regression/replay evidence，不是 fresh holdout。

审计覆盖 production 匿名页面的 150 条 zh-Hans / zh-Hant-HK 用户可见文本：

- A / natural = 53
- B / readable-but-modelish = 72
- C / clearly unnatural = 15
- D / product-semantic/trust problem = 10

已观察模式包括：

- product self-definition before action；
- 不必要的显式第二人称；
- 反复出现工整结构：
  - 不是 X，而是 Y
  - 只有 X，才 Y
  - 先 X，再 Y
- ordinary status 被 slogan 化；
- internal product-state / engineering / legal nouns 泄露；
- reassurance 过度完整；
- zh-Hans / zh-Hant-HK 机械转换；
- 单句各自能读，但整页 rhetorical rhythm 仍像模型连续润色。

Founder 已明确确认代表例子，例如：

- `這是一個私密、低頻的交友流程。你先完成資料；固定輪次開放後，再自行決定是否參加。`
- `只開放註冊 / 先把資料準備好`

问题不是语法错误，而是“可读但不像成熟真实产品会这样说”。

另外读取 Clear Writing #17 的 Lucerna real-project evidence：
正常 UI 把 implementation reassurance / maintenance detail 写给普通用户，即使技术准确仍不是好 microcopy。

---

## 五、Planner 首先要回答的核心架构问题

不要先写 implementation plan。

先判断并冻结 ownership。

至少回答：

### A. Frontend Design 到底拥有哪一层？

候选原则：

Frontend Design 拥有：

- whether to say
- where to say
- UI role
- hierarchy
- duplication
- progressive disclosure
- rendered prominence
- viewport/line-wrap/CTA relationship
- page-level rhetorical repetition
- product-semantic escalation

验证这是不是正确边界。

### B. Clear Writing 到底拥有哪一层？

候选原则：

Clear Writing 拥有：

- frozen meaning 下的自然语言 realization；
- locale-specific register；
- UI-role-aware wording；
- short-copy naturalness；
- local rhetorical shape；
- protected meaning fidelity；
- 在不能安全润色时返回 escalation，而不是硬改。

验证这是不是正确边界。

### C. writing-fidelity 的角色

明确：
- 哪些 UI 产品事实属于 protected meaning；
- Product UI Copy 能否删句/压缩/改结构；
- 什么情况下必须返回 Frontend/Product owner；
- 不得为了自然度改变产品状态、资格、隐私、法律事实、consent、安全或用户后果。

### D. 谁负责 page-level rhythm？

这是本任务必须明确解决的问题。

单句自然不等于整页自然。

Planner 必须冻结：
- Writing 是否做 first-pass rhythm analysis；
- Frontend 是否拥有最终 rendered page rhythm acceptance；
- 两者如何避免重复/互相覆盖。

---

## 六、决定是否新增独立 Product UI Copy Skill

当前候选：

`skills/writing/core/product-ui-copy/`

或其他更合适名称。

Planner 必须比较至少三种方案：

### Option 1
扩展现有 `chinese-prose`

### Option 2
新增独立 sibling Skill，例如 `product-ui-copy`

### Option 3
不新增 Skill，只通过 Frontend Design + existing writing-fidelity/chinese-prose 的 handoff mode 实现

必须比较：

- trigger clarity
- overlap risk
- context budget
- long-form regression risk
- UI-role awareness
- zh-Hans / zh-Hant-HK localization
- packaging/routing complexity
- cross-plugin install/use behavior
- testability
- future English/other-locale extension

不要因为 TODO #20 提议“dedicated sibling”就自动选择 Option 2。

但如果选择不新增 Skill，必须证明现有 `chinese-prose` 可以在不污染长文本路线的前提下可靠区分 UI microcopy。

---

## 七、定义 Product UI Copy 输入合同

Planner 必须提出一个 **最小、可执行、尽量不新增重型 schema** 的 handoff contract。

至少考虑：

- SURFACE
- UI_ROLE
- PRODUCT_STATE
- USER_JOB
- USER_CONSEQUENCE / NEXT_ACTION
- NEIGHBORING_VISIBLE_COPY
- LOCALE
- PROTECTED_MEANING
- DISCLOSURE_LEVEL
- LENGTH / VIEWPORT CONSTRAINT

但不要机械照抄。

目标是让 Writing 不再只收到裸句：

`先把资料准备好`

而能知道它是：

- Landing
- status heading
- registration open / matching closed
- 上方已经有 badge
- 下方已经有 explanatory body
- CTA = 创建账户
- mobile first viewport

从而能判断：
- rewrite
- shorten
- merge
- delete recommendation
- escalate

同时要回答：

这个 handoff 是：
- conceptual contract / structured object / prompt convention / lightweight machine schema 中的哪一种？

除非有真实需要，不要新建复杂 protocol/ledger/state machine。

---

## 八、冻结 defect taxonomy

基于 CUHK Date A/B/C/D audit，但不要机械继承名称。

Planner 必须设计一个 production taxonomy，能至少区分：

1. 可以保留；
2. 纯 naturalness/wording 问题；
3. locale/register 问题；
4. content architecture / duplicate / placement 问题；
5. product semantics 问题；
6. legal/trust/safety escalation。

要求：

- Writing 不能自动“润色掉”产品语义问题；
- Frontend 不能把纯语言问题全靠删句解决；
- legal/trust copy 不因为更自然就弱化真实责任/限制；
- 不能变成 AI detector 或 banned phrase scanner。

---

## 九、中文自然度规则必须是机制，不是禁词表

Planner 要把真实 evidence 抽象成机制。

至少覆盖：

- product self-definition vs state/action-first
- explicit second person 何时自然、何时多余
- balanced rhetoric 的累积问题
- ordinary status sloganization
- internal implementation nouns
- over-complete reassurance
- fragment vs full sentence
- UI role 对语体的影响
- standard action label 应优先标准词
- privacy/terms/support/register 不同 register
- zh-Hans / zh-Hant-HK 独立 realization

明确：

不能建立类似：
“禁止 你、禁止 先、禁止 不是 X 而是 Y”

这种机械规则。

单句是否自然必须结合 UI role 和 page context。

---

## 十、Locale ownership

必须明确：

- zh-Hans 与 zh-Hant-HK 从同一 protected meaning 独立 realization；
- 不能以字符转换作为 localization acceptance；
- Mainland product Chinese 与 Hong Kong product Chinese 要分别有 register judgement；
- 标准品牌/产品/技术 token 保持一致；
- locale-specific wording 不能改变产品语义。

提出后续 evaluation 如何证明两个 locale 都不是机械互转。

---

## 十一、Frontend Design integration

不得破坏 Frontend Design 0.3 coordinator-first。

Planner 应设计：

`frontend-visual-systems coordinator`
→ P0/P1 判断 content architecture / UI role
→ 如需要自然语言 realization，handoff 给 Clear Writing
→ 返回 candidate copy
→ Frontend 继续 P2/P3
→ rendered page/screen copy acceptance
→ P4 whole-product taste

需要明确：

- S1 小修如何 scale down；
- S2 bounded copy/UI change 如何处理；
- S3 landing/redesign 如何跑 page-level rhythm；
- 有 Figma时 copy 是否属于 design authority；
- 没有 Figma 时如何形成 durable copy/content authority；
- copy change 何时算 design defect、wording defect、product-semantic defect。

---

## 十二、Clear Writing routing

Planner 必须明确未来 normal triggers。

至少设计：

### 正向触发
- UI label
- help text
- status
- CTA
- empty/loading/error
- onboarding text
- landing microcopy
- settings/support/privacy surface copy
- “这个产品页面中文不自然”
- “UI 有 AI 味但都能读”

### near-miss / negative
这些不能被 Product UI Copy route 抢走：

- 中文科研报告
- README 长文
- technical docs
- manuscript
- advisor report
- ordinary paragraph rewrite
- source-faithful scientific structural rewrite

同时说明与：
- `chinese-prose`
- `scientific-rewrite`
- `writing-fidelity`

如何路由，不得让新能力吞掉 Clear Writing 已经正常的任务。

---

## 十三、Evaluation / replay 设计

必须分清：

### Known regression
CUHK Date 150-line audit：
`docs/design/product-ui-copy/evidence/CUHK_DATE_PRODUCT_COPY_NATURALNESS_AUDIT_2026-09-26.md`

用途：
- replay
- taxonomy calibration
- ownership validation

不能冒充 unseen holdout。

### Independent real-project evidence
至少使用 Lucerna #17 的 microcopy failure。

Planner 判断是否还有一个现有项目能作为独立真实 replay；
没有就不要编造。

### Fresh holdout
设计 repo-safe、此前没有被规则逐条调过的 UI-copy fixtures。

至少覆盖：

- zh-Hans
- zh-Hant-HK
- CTA
- state
- help text
- empty/error
- privacy/trust
- landing
- repeated page rhythm
- correctly natural copy that must remain unchanged

必须防止过度改写：
好的 A 类 copy 不应为了“显示能力”被重新润色。

---

## 十四、独立评审

最终实现阶段不能只靠 Executor 自评。

Planner 需要设计：

1. deterministic routing/contract tests；
2. known regression replay；
3. unrelated Clear Writing regression；
4. unrelated Frontend Design regression；
5. fresh holdout；
6. independent text/naturalness review；
7. 对真实 rendered UI 的 Frontend acceptance。

CUHK Date 后续正式修改仍属于 CUHK Date 项目自己的产品任务。

本 AI_Skills task 只能证明：
新能力能正确识别/建议/实现 Product UI Copy，而不能在这里直接改 CUHK Date production。

---

## 十五、外部参考研究边界

如果 Planner 认为需要补充 UX writing / localization evidence，可以查权威来源，例如：

- Apple Human Interface Guidelines / Writing
- GOV.UK Design System / Service Manual content and UI writing
- Microsoft Writing Style Guide
- Material / Google UX writing guidance
- 香港政府或成熟香港数字服务的公开语言样例，仅用于 register/reference

但：

- 不要把任何品牌 voice 复制成通用规则；
- 不要把竞品 marketing copy 当科学证据；
- 不要依赖 AI detector；
- 不要把“像真人”定义成故意制造错误、俚语或随机不一致。

---

## 十六、实施面必须具体，但本轮不实现

Planner 最终要列出未来 Executor 可能修改的 exact surfaces，例如：

- Frontend Design coordinator / product-ux planning 哪些 source Skill
- Clear Writing routing
- `writing-fidelity`
- `chinese-prose` 是否只需要 narrow handoff
- 是否新增 `product-ui-copy`
- Marketplace packaging
- trigger evals
- regression tests
- docs/plugin-todos
- changelog/version bump policy

但 Planner 不得现在修改这些 production surfaces。

---

## 十七、明确不做

本轮不得：

- 直接修 CUHK Date 文案；
- 直接修 Lucerna 文案；
- 修改任何 production project；
- 把 CUHK Date 的品牌语气变成全局风格；
- 建 AI detector；
- 建 banned phrase wall；
- 建“人类化”随机错误机制；
- 为了 Product UI Copy 重写整个 Clear Writing；
- 重新开启 Frontend Design #52–#72 consolidation；
- 顺手处理 writing-style 其它无关 TODO；
- 新建复杂 workflow/state machine/ledger；
- 声称一个 Plugin 能独自完成产品语义/法律判断。

---

## 十八、Planner 产物

建议 proposal：

`docs/design/product-ui-copy/PRODUCT_UI_COPY_CROSS_PLUGIN_PROPOSAL_V0_1_2026-09-28.md`

必须包含：

1. Current reality
2. Exact scoped TODOs / durable locators
3. Evidence summary
4. Ownership matrix
5. Defect taxonomy
6. Frontend → Writing handoff contract
7. Decision: new Skill vs existing Skill mode
8. Clear Writing routing
9. Frontend Design integration
10. writing-fidelity boundary
11. zh-Hans / zh-Hant-HK localization contract
12. line-level workflow
13. page-level rhythm workflow
14. product/legal/trust escalation
15. scale-down for S1/S2/S3
16. packaging/topology
17. tests / known replay / fresh holdout
18. independent review plan
19. implementation surface
20. regression risks
21. explicit non-goals
22. TODO disposition plan
23. version/maturity implications
24. next independent Critic prompt

不要创建 Executor Goal。

---

## 十九、最终返回

```text
RESULT = PLANNED | BLOCKED

SOURCE_MAIN =
FRONTEND_DESIGN_BASELINE = web-development 0.3
FRONTEND_DESIGN_REOPENED = NO

FRONTEND_COPY_TODO_LOCATOR =
WRITING_TODO_17 = INCLUDED
WRITING_TODO_20 = INCLUDED
WRITING_TODO_13 = REVIEWED_AS_DEPENDENCY_ONLY

CUHK_DATE_AUDIT_USED_AS_KNOWN_REPLAY = YES
CUHK_DATE_PRODUCT_MODIFIED = NO

OWNERSHIP_MATRIX_DEFINED = YES | NO
HANDOFF_CONTRACT_DEFINED = YES | NO
DEFECT_TAXONOMY_DEFINED = YES | NO
PAGE_RHYTHM_OWNER_DEFINED = YES | NO
ZH_HANS_ZH_HANT_SEPARATE_REALIZATION = YES | NO

NEW_PRODUCT_UI_COPY_SKILL_RECOMMENDED = YES | NO | UNDECIDED
CHINESE_PROSE_LONG_FORM_PROTECTED = YES | NO
WRITING_FIDELITY_BOUNDARY_DEFINED = YES | NO

KNOWN_REPLAY_PLAN = PASS | MISSING
INDEPENDENT_REAL_PROJECT_REPLAY_PLAN = PASS | MISSING
FRESH_HOLDOUT_PLAN = PASS | MISSING
INDEPENDENT_REVIEW_PLAN = PASS | MISSING

PROPOSAL_PATH =
NEXT_STEP = independent Critic review
```
