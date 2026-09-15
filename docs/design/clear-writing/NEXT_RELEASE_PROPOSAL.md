# Clear Writing 下一次正式发布收口 Proposal

- Proposal version: `v0.1`
- Date: `2026-09-15`
- Planner base main: `0573977472c9557fa8b7aa87ef819961d464fe36`
- Status: `READY_FOR_CRITIC_REVIEW`
- Architecture decision: `PARTIAL_REDESIGN`
- Scope: 研究与方案设计；不是可执行 Goal / Plan，不授权实现、paid API、自动化或 successor task。

## 0. 结论

Clear Writing 不应推翻 051–054 建立的主架构，也不应继续沿着“再加禁词、脚本统计、例外分支”的方向修补。现有证据更支持 **PARTIAL_REDESIGN**：保留 `Meaning Map -> Reader Plan -> REALIZE_MEANING -> assembly -> fidelity/audit` 的职责分层，但重新定义 Reader Plan、REALIZE_MEANING、assembly 和 reviewer 的语义边界，使系统真正按“内容在成稿里扮演什么角色”处理信息，而不是按“它长得像代码、路径、英文、future work”决定删留。

下一次发布真正需要闭合的不是更多格式规则，而是三个机制缺口：

1. **读者处置（reader disposition）没有成为稳定的语义合同。** 同样是代码、路径、配置或 future work，有的属于正文必要信息，有的属于内部过程垃圾。054 已证明仅靠 exact-item / keyword / local audit 无法可靠区分。
2. **局部 realization 可以全部“合法”，完整文档仍然可能像项目备忘录。** 054 Deep Research 的本地 Gate B8 通过，但独立整篇阅读仍立即发现执行计划口吻、内部路径和来源过程框架，说明 assembly / final pass 缺少真正的 whole-document reader responsibility。
3. **Reviewer contract 混合了三件不同的事：source fidelity、reader-facing quality、external factual truth。** 054 中 legitimate code 被 blanket rule 拒绝，历史事实问题又被当成默认 rewrite blocker；这会把 reviewer rubric defect 误报为 plugin defect。

因此，下一轮若经 Critic PASS 后进入实现，应从最新 `main` 出发，选择性吸收 053/054 branch 中已被证据支持的机制，而不是把 `reviewed/054_clear_writing_release_closure` 整体当成待 merge 的 release candidate。当前 `main` 的 Clear Writing manifest 仍为 `writing-style` 0.2；054 branch 与当前 main 已 diverged，且 054 的 production changes 并未形成正式 release/integration。

---

## 1. 已核对的当前事实

### 1.1 当前正式 source 与产品边界

当前 `main` 的 plugin identity 为：

- slug: `writing-style`
- display name: `Clear Writing`
- version: `0.2`
- maturity: `unclassified`

当前 source 的职责已经基本合理：

- `skills/writing/core/scientific-rewrite/SKILL.md`：heavy Chinese source-faithful structural rewrite，负责 source anchors、Meaning Map、Reader Plan、assembly 和语义审计路线；
- `skills/writing/core/chinese-prose/SKILL.md`：负责 `REALIZE_MEANING` 和中文成稿自然度；
- `skills/writing/core/writing-fidelity/SKILL.md`：负责 claim / evidence / attribution / exact-item / structure 变化后的保真；
- `docs/workflows/CANDIDATE_PLUGIN_REPLAY.md`：要求通过正式 local marketplace / install-or-upgrade / fresh-session 路径验证 candidate identity，而不能用 direct skill path 代替 production entry。

当前 source 已经包含几个应保留的正确方向：Meaning Map 与 Reader Plan 分离；`REALIZE_MEANING` 不直接吃 raw source 段落；exact item 不等于“所有英文都原样保留”；internal workflow trace 与 scientific content 有区分；fidelity 允许 reader-facing regrouping，而不是强迫逐段对应。

### 1.2 051–054 实际解决了什么

**051** 建立了真正的 successor candidate 和 heavy Chinese rewrite 主路径，并证明 ordinary installed-plugin request 可以路由进入新路线；同时建立 candidate replay、known regression、完整报告、fresh holdout 和 Text Review。它最终不是 release PASS：最后独立 Text Review 仍发现 internal workflow terminology leakage 和 source-process / rewrite framing，任务以 `051_FINAL_TEXT_REVIEW_FAIL` 停止。051 另有一个 workflow/accounting 故障属于 Bridge / paid-review recovery 问题，不应混同为写作产品缺陷。

**052** 的价值主要是把 reader-facing generalization、candidate replay 和 production identity 进一步收敛，并证明 Meaning Map / Reader Plan / realization packet 可以在普通插件入口下成立。它没有证明“成稿已经可直接长期使用”，也没有完成完整 release。

**053** 证明了一个重要反例：新架构在结构和边界上更先进，但实际成稿质量可能倒退。历史对比显示 051 某些 artifact 反而更像成稿；053 因此集中修 raw markup、数学、表格、语言混杂和完整 Deep Research 等真实问题。fresh holdout 中一例出现无关俄文 alias，再次说明问题是 reader relevance，而不是简单的“非中文字符存在”。

**054** 在 branch candidate 上把 reader relevance、dirty-source cleanup、数学、表格、中文质量、fidelity、compatibility、完整 Deep Research、fresh generalization、candidate replay 都纳入 release closure。已记录的 known/stress/fresh local evidence 表明很多 053 regression 确实保持修复；但 Terra 仍给出 `REVISE`。最终 release CI、正式 production smoke、final Reviewer、用户验收和 integration 都未发生。

### 1.3 054 暴露出的 defect 归因

按 `results/054_clear_writing_release_closure/FAILURE_ATTRIBUTION_AUDIT.md` 与实际 Text Review，至少应区分以下五类：

| 现象 | 当前归因 | 是否是下一轮产品 blocker |
|---|---|---|
| Deep Research 仍像“下一轮怎么做”的执行计划/项目备忘录，而不是直接面向读者的成稿 | `PLUGIN_DEFECT` | 是 |
| 成稿保留 task/repo contract、无读者价值的内部路径、来源处理框架、license/disclaimer debris | `PLUGIN_DEFECT`（需按语义判断） | 是 |
| legitimate Python 示例因为“存在 fenced code”被 Terra blanket blocking | `REVIEWER_RUBRIC_DEFECT`，除非该代码对当前读者任务确实无关 | 否，先修 rubric |
| 2015 LeCun/Bengio/Hinton 历史归因被作为默认 rewrite blocker | 默认属于 `EXTERNAL_FACTUAL_TRUTH` 维度；只有 output 相对 source 新增/强化错误时才转为 fidelity defect | 默认否 |
| dirty mirror / ChatGPT-export-like HTML / messenger wrapper 本身质量差 | `SOURCE_DEFECT`，但 plugin 仍应清掉明显 wrapper 垃圾 | source 本身不等于 plugin defect |
| 051 incomplete Kalman holdout | `EVALUATION_SOURCE_DEFECT` | 否 |
| 051 paid-review immutable-campaign accounting 阻塞 | `WORKFLOW/ENVIRONMENT_DEFECT` | 否 |
| local gates 全 PASS，Terra 才第一次发现整篇明显成稿问题 | `WORKFLOW_DEFECT` + reviewer staging defect | 是，必须修流程 |

核心结论：054 不是“Terra 找到四个 plugin bug”，也不是“plugin 其实没问题”。它同时暴露了真实产品缺陷、source/rubric/workflow 缺陷；下一轮必须先分开，否则会继续用错误的修复手段优化错误的目标。

---

## 2. 最终正常用户到底应得到什么

Clear Writing 的 heavy rewrite 产品合同应收敛为：

> 用户给出一份已经存在的中文或中文主导科研/技术材料，并要求“内容不要变，但重新组织得清楚、自然、能直接给读者看”时，Clear Writing 应从普通插件入口产出一份 **独立可读的 reader-facing 文档**。它可以重排、合并、拆分、显式解释和清理 source wrapper，但必须保留 source 中任务相关的事实、数字、公式、引用、比较关系、条件、限制、不确定性、归因和必要复现信息，不得偷偷把 rewrite 变成 fact-check 或 Research Authoring。

这意味着：

- 正常代码示例如果承担算法解释、API/interface、教学或复现职责，应保留并适当整理；代码 fence 本身不是垃圾。
- path / config / command 如果是复现步骤、接口合同或 reader 真正需要定位的对象，应保留或移到技术附录；如果只是 task branch、review bundle、内部 audit path，则应删除。
- future work 如果是 source 正文真正的科研未来工作、限制或作者计划，应保留为“该研究/作者下一步拟做什么”；只有把它写成“我们现在应该执行下一轮实验”的 assistant/executor voice 才是失败。
- source 自身可能存在外部事实错误。默认 rewrite 不应偷偷改事实；应保留 source meaning。除非用户明确要求 fact-check，否则 external factual truth 单独记录，不作为 Clear Writing 默认 release blocker。
- 简体/繁体应服从 user target / source context；正式方法名、库名、数据集名、API、代码 identifier 可保留英文，普通论述不应退化成英文关键词脚手架。
- 长文必须是一篇真正读得通的完整文档，而不是多个局部 PASS 段落的拼接。

### 明确 non-goals

本 proposal 不把 Clear Writing 变成：

- 自动事实核查器；
- Research Authoring / evidence selection / literature synthesis；
- domain semantics owner；
- 通用 Markdown sanitizer；
- detector-evasion / “去 AI 味”关键词引擎；
- 新 runtime / 新 top-level plugin；
- Bridge Kit workflow owner。

---

## 3. Architecture decision: PARTIAL_REDESIGN

### 3.1 KEEP 的部分

保留主链：

```text
ordinary Clear Writing entry
    -> scientific-rewrite routing
    -> Meaning Map
    -> Reader Plan
    -> REALIZE_MEANING
    -> assembly / whole-document finish
    -> source-fidelity + semantic audit
    -> bounded repair
    -> rendered final candidate
```

保留原因：

1. **Meaning Map 与 Reader Plan 的分离是必要的。** 前者回答“source 说了什么、哪些 obligation 不能丢”，后者回答“读者需要按什么顺序、以什么形态看到这些内容”。这两个问题混成一个 prompt 会重新回到逐段 paraphrase 或 summary drift。
2. **clean-room `REALIZE_MEANING` 是正确方向。** 051/052 已证明直接把 raw source prose 重新喂回 drafting 很容易复制 source framing；meaning-driven realization 至少建立了从语义到自然表达的隔离层。
3. **writing-fidelity 独立于 style 是正确的。** 改得更自然和是否保持 claim/evidence 是不同性质的判断，不能由同一个“看起来顺不顺”评分代替。

### 3.2 REDESIGN 的部分

#### A. Reader Plan 从“排序计划”升级为“读者处置合同”

不新增一套大型 schema/state machine，而是在现有 Reader Plan 语义中明确：每个 Meaning Map obligation 必须有 reader-facing disposition。概念上至少覆盖：

- `CORE_INLINE`：正文核心 claim / definition / mechanism / evidence；
- `SUPPORT_INLINE`：必要解释、条件、caveat；
- `STRUCTURED`：公式、表格、引用、合法代码等应以结构化形式出现；
- `RELOCATE`：必要但不应打断正文的 path/config/复现细节，可放 technical note / appendix；
- `SOURCE_FUTURE_WORK`：future work / limitation 保留，但必须保持 source/author modality；
- `DROP_WRAPPER`：网页导航、导出 UI、免责声明残片、内部 review/task/audit framing；
- `DROP_IRRELEVANT_TRACE`：与读者任务无关的 branch/commit/result path/internal contract。

重点不是这些名字本身，而是 **要求每个删、留、移、改形态动作都有 source role + reader reason**。Executor 若能用现有字段表达，不应为这些标签另建复杂 runtime schema。

#### B. REALIZE_MEANING 增加“modality preservation”

目前 fidelity 更擅长核对事实和 exact items，但 054 Deep Research 表明“未来工作”特别容易从 source content 变成 executor instruction。下一轮应把以下关系视为受保护语义：

- 已完成 vs 尚未完成；
- source author proposal vs assistant recommendation；
- scientific limitation vs workflow blocker；
- hypothetical / conditional vs committed action；
- external attribution vs narrator voice。

这不是禁用“下一步”三个字，而是要求 realization 保持 source 的主体、时态、语气和 epistemic status。

#### C. assembly / final pass 明确承担 whole-document composition

054 最大的产品信号是：各 bundle、math/table/fidelity audit 可以局部 PASS，但完整 Deep Research 仍像工作备忘录。assembly 不能只做拼接和去重；它应承担一个 candidate-only、Reader-Plan-aware 的 whole-document finish：

- 读者是否一开始知道这篇文档在解释什么；
- section 顺序是否是读者问题顺序，而不是 source/process 顺序；
- 同一个概念是否重复定义或在不同 bundle 中视角冲突；
- future work、limitations、reproducibility details 的位置是否合理；
- 是否出现“本项目/本轮/下一轮应执行/来源抓取过程”等不属于目标文体的全局 voice；
- 标题、过渡、表格前后解释是否让完整 artifact 连贯。

这个职责应尽量复用现有 `chinese-prose` final naturalness / assembly 路线，不新建第二个 generative runtime。

#### D. fidelity audit 从“存在性检查”补足到“处置正确性检查”

保留现有 proposition/evidence/exact-item 检查，同时新增一个最小问题：

> 每个 source obligation 在 final candidate 中是 preserved / summarized / relocated / omitted；这个处理是否与 Reader Plan 一致？

这可以防止两个相反失败：

- 为了 fidelity 把所有 path/code/internal trace 全塞回正文；
- 为了“干净中文”把 legitimate code、引用、复现条件、future work 全删掉。

### 3.3 不采用的现实替代

**Alternative 1 — KEEP unchanged：拒绝。** 054 的 Deep Research 与 Terra evidence 已经证明 local mechanical/fidelity PASS 不能保证 whole-artifact 成稿质量；不改职责边界只会再次把问题拖到最后。

**Alternative 2 — REPLACE 为 one-pass “把全文重写好”：拒绝。** 一次长 prompt 的确更简单，但会重新失去 source obligation tracking、claim/evidence 可追溯性和 compatibility route 控制；051–054 已投入的正确分层会被一并丢掉。

**Alternative 3 — giant postprocessor / banned-word / script blacklist：拒绝。** 俄文 alias、英文关键词、path/code 的问题都是 role-dependent；regex 只能看到表面形态，无法判断 legitimate technical content 与 internal trace。

**Alternative 4 — 默认接入 web fact-check：拒绝。** 这会改变产品边界、成本、隐私与 latency，并把 Clear Writing 与 Research Authoring / research workflow 混合。外部事实核查应是显式上游/旁路能力。

---

## 4. 防回归设计

下一轮不能只修 Terra 的四个句子。053/054 已证明的能力应全部进入 regression boundary：

- Bloom / raw markup cleanup；
- FFT 数学与 operator fidelity；
- table-rich self-attention / structured tables；
- complete Deep Research long document；
- ordinary natural routing；
- light Chinese polish；
- English scientific prose；
- fidelity-only route；
- source-comparison editorial route；
- 054 fresh H1/H2/H3 中已经有效的数学、表格、中文、clean source、normal routing 能力；
- legitimate code examples；
- necessary path/config/reproduction information；
- Simplified/Traditional target handling；
- prior accepted source-process framing fixes。

修复 reader relevance 时，必须同时测试 `should-drop` 与 `should-keep`。如果只验证“内部路径消失”，很容易把真实复现路径也删掉；如果只验证“代码保留”，又可能把网页抓取垃圾原样带入成稿。

---

## 5. Capability Gate Matrix

下面 8 个 gate 是 bounded matrix。G2–G6 是产品能力；G1/G7/G8 证明正常入口、泛化和 release identity。G8 的 independent review 是对 G2–G6 的独立认证，不另造第九个“质量 gate”。

| Gate | Capability / claim | Why distinct | Normal entry | Evidence | Failure | Regression boundary | Final-candidate requirement |
|---|---|---|---|---|---|---|---|
| G1 | **ordinary routing / install / compatibility**：用户从正式 Clear Writing 安装身份、普通自然语言请求进入正确 route；light Chinese、English scientific prose、fidelity-only、source comparison 等兼容路线不被 heavy rewrite 吞掉 | 没有正常入口，后面只是在证明 helper/fixture | official local marketplace -> install/upgrade -> fresh session -> ordinary prompt | candidate hash/manifest、loaded skill identity、route receipt、compatibility suite、should-not-change cases | 只能 direct skill 跑通；装到旧版本；fresh session 未加载 candidate；兼容路线变化 | 052 replay + 054 compatibility + current 0.2 routes | **必须由 exact release candidate 直接通过**；不得用另一 candidate 的 replay 代替 |
| G2 | **source fidelity / attribution**：claim、evidence、polarity、quantifier、comparator、condition、caveat、uncertainty、citation、attribution 保真；不新增 source 不支持的 claim | 这是“内容没变”，与“好不好读”不同 | ordinary heavy rewrite | source-to-output obligation map + proposition/evidence audit + source-visible qualitative review | omission、invented claim、strengthening、reattribution、条件/否定漂移、citation 损坏 | 051/052 fidelity evidence；053/054 exact & semantic regression | exact final candidate；A 维度必须 PASS；external-world truth 不混入此 gate |
| G3 | **structured technical / reproducibility content**：公式、operators、表格、合法 code、commands、必要 path/config/API/identifier 依据 role 保留、整理或 relocate | 同样看似“机器内容”，有的必须保留，有的应删除，不能与一般 prose cleanup 混为一谈 | ordinary technical rewrite | formula render、table parse/render、code/path should-keep & should-drop pair、citation/identifier checks、human artifact inspection | 公式损坏、表格失真、合法 code 被 blanket 删除、内部 trace 被当复现信息保留 | FFT、table-D2L、054 H1 legitimate code、source comparison、reproducibility cases | exact final candidate；不得只靠 regex count / fence count |
| G4 | **dirty source / markup cleanup**：wiki/rst/html/export wrapper、navigation、template、license/disclaimer debris 等不进入 reader-facing正文，同时正文语义不丢 | 这是 source hygiene，不等于语言质量；可以有较确定的结构检查 | ordinary rewrite of dirty source | dirty-source known cases + source-role mapping + rendered artifact | wrapper 留存；清理误删正文；renderer 仅隐藏未清掉的 source garbage | Bloom、Karatsuba/wiki、054 noisy docs、Deep Research source wrapper | exact final candidate；source cleanup 后仍须过 G2/G3 |
| G5 | **reader relevance / Chinese quality / voice / script**：选择与读者有关的信息；自然中文；必要英文保留；简繁体服从 target；future work 保持 source modality；无 internal audit/execution-plan voice | 这是 054 真正未闭合的核心产品能力，机械结构 PASS 不能替代 | ordinary heavy Chinese rewrite | semantic role/disposition evidence + candidate-only whole-artifact reader review + calibrated model/human rubric | 中文像英文关键词脚手架；俄文/无关 alias；内部 workflow 口吻；source future work 被写成 executor instruction；无意义 path 冒头 | 053 language cases、054 Deep Research、H1 language anomaly、DII/TRACE TODO 中的真实 reader feedback | exact final candidate；**不能用 banned-word/English count 作为 PASS 代理** |
| G6 | **complete long-document structure / coherence / real render**：完整长文是一篇独立可读的 finished artifact，而不是局部 bundle 拼接；实际 PDF/HTML render 可读 | 长程 coherence 是局部段落和结构元素检查捕捉不到的能力 | ordinary complete long-document request | full Deep Research + 至少一个独立长文；完整 render；section/transition/definition/coherence review；whole-artifact qualitative review | 成稿仍像 memo/plan；段落各自正确但全局跳跃；重复定义；附件/路径主导正文；render 实际不可读 | 053/054 complete Deep Research 与 H3 long-form | exact final candidate；**必须在 paid Terra 前完成 whole-artifact qualitative PASS** |
| G7 | **fresh generalization**：上述能力不是 known-case 特判 | 防止只对 051–054 samples 打补丁 | same ordinary plugin entry, frozen unseen inputs | 预先冻结的 fresh batch，覆盖 noisy technical、formula/table、long-form，并显式包含 legitimate code/repro 或 future-work 语义中的至少一个；source completeness preflight | exposure 后换题、针对 holdout 调 production、只追加赢家、fresh 中出现真实 G2–G6 failure | 051 holdout completeness lesson；053/054 frozen batch rules | candidate 在看 fresh output 前冻结；candidate 改动后旧 fresh 不能再称 unseen release proof |
| G8 | **same-candidate production certification + independent qualitative verification**：真正要发布的那个 candidate 以正式 plugin identity 正常工作，并由独立 reviewer 验证 G2–G6，而不是第一次发现基本成稿问题 | candidate identity 和 independent judgment 是 release claim 的最后两类证据；它们不新增产品能力，但防止 patchwork PASS | official install/upgrade/fresh session + actual production-facing prompt | candidate replay、release CI、production smoke、independent Text Review/Terra、final GPT Reviewer、user acceptance dossier | 混用多个版本 PASS；Terra rubric 越界；production identity 未证明；review 只看摘要/receipt | `CANDIDATE_PLUGIN_REPLAY.md`、Paid External Review Policy、054 failure audit | **所有 release-critical evidence 绑定同一 final candidate**；paid reviewer 应是验证，不是首次 full-artifact reader |

### 覆盖关系说明

- formulas / tables / legitimate code / citations / path/config 统一放 G3，因为共同问题是“结构化技术内容按语义角色处置”，但每类仍需独立 case。
- dirty markup 单独 G4，因为其 failure mode 是 source wrapper 污染，与 legitimate code 的保留方向相反。
- Simplified/Traditional、中文自然度、reader relevance、future-work voice 合并 G5，因为它们共同判断“这段内容以什么读者语言/语气出现”；但不能只凭 script counts PASS。
- long-document coherence 单独 G6，因为 054 已直接证明 item/local gates 全 PASS 后仍可能整篇失败。
- independent review 不再扩成额外 gate；它是 G8 对 G2–G6 的独立认证层。

---

## 6. Reviewer / Terra rubric redesign

### 6.1 必须拆开的三个维度

#### A. Source fidelity

Reviewer 必须同时看到 source 与 candidate，判断：

- candidate 的 claim 是否能回指 source；
- 是否遗漏任务相关内容；
- 是否改变 polarity / comparator / condition / quantifier / caveat / uncertainty；
- attribution / citation / formula / table / code 的语义是否漂移；
- 删除/relocate 是否与 frozen Reader Plan disposition 一致。

A 是 Clear Writing 的硬 blocker。

#### B. Reader-facing quality

Reviewer 主要读 candidate 和 render，再按需要回看 Reader Plan，判断：

- 第一次读的人能否知道“这篇在讲什么、为什么、结论是什么”；
- 中文是否自然，必要英文是否有定位价值；
- section / transitions / information hierarchy 是否连贯；
- 是否还有 source-process / audit / executor / internal project frame；
- future work 是否是正确的 source/author voice；
- code / path / config 的位置与篇幅是否符合目标读者；
- artifact 是否真正 rendered readable。

B 是 Clear Writing 的硬 blocker。

#### C. External factual truth

Reviewer 可以记录 candidate/source 中的外部事实疑点，但默认 **不作为 Clear Writing blocker**。只有两种情况可 blocking：

1. 当前 frozen task 明确包含 fact-check；或
2. candidate 相比 source 自己新增、强化、错误归因了该事实，此时它实际上转化为 A/source-fidelity failure。

这能避免“source 本来就错 -> rewrite plugin 必须偷偷改正”的职责漂移。

### 6.2 特殊内容的 blocking 规则

**正常代码**：只有在代码与目标读者任务无关、明显是 source wrapper/抓取垃圾、或 user 明确要求无代码时才可因 code 本身 blocking。算法教学、API、复现、实现说明中的合法 code 应按 fidelity 保护。

**path/config**：内部 task/review/branch/result path 可 blocking；复现路径、checkpoint/config/interface 若对 source claim 或 user task 必要，保留或 relocate，不得 blanket block。

**future work**：source 本身的 future work、limitation、proposed study 不是坏文体。只有把它变成 assistant 当前行动清单、release plan、review workflow 才 blocking。

**source factual error**：标记到 C；不能为“让文章看起来正确”静默改变 source。若用户另行授权 fact-check，应由对应 research/domain route 提供 evidence 后再改。

### 6.3 blocking finding 的最小证据合同

任何 Reviewer/Terra blocking finding 必须同时给出：

1. `DIMENSION = A | B | C`；
2. 对应的 frozen requirement / Gate；
3. candidate 精确位置/摘录；若是 A 还要给 source 对应位置；
4. 为什么违反该 requirement，而不是“我不喜欢这种写法”；
5. 初步 attribution：`PLUGIN_DEFECT | SOURCE_DEFECT | REVIEWER_RUBRIC_DEFECT | ENVIRONMENT_DEFECT | WORKFLOW_DEFECT`；
6. 最小解决条件。

若 finding 无法回指 frozen requirement，则只能是 advisory，不得临场升级成 release blocker。

---

## 7. 为什么以前 local PASS 后 Terra 才第一次发现明显问题

054 已给出足够直接的因果证据，不需要再猜：

1. local gates 主要验证 route、receipt、exact-item、semantic coverage、math/table syntax、render existence、language heuristics 等 **局部或机械性质**；
2. Deep Research Gate B8 即使记录为 local PASS，也没有一位独立 reviewer 以普通读者身份完整读 finished artifact；
3. H1 local audit 明确把 source-required code 视为合法，但 Terra rubric 又把 fenced code 本身当 blocker，说明两套 reviewer semantics 没校准；
4. Terra 同时评价 external historical truth，超出了默认 source-faithful rewrite 的产品边界；
5. 当 paid Terra 被安排成第一位真正从头到尾读成稿的人时，它自然会第一次发现“这不像成稿”——这不是 Terra 太严格，而是 qualitative whole-artifact check 放得太晚。

当前 `main` 的 capability-gate / paid-review policy 已要求避免这种顺序：最终付费 review 应验证成熟 candidate，而不是第一次承担完整定性产品审查。

---

## 8. Fresh / paid review 顺序

若未来 Proposal 获 Critic PASS 并被用户授权实现，建议按以下顺序设计 execution contract；本 proposal 本身不启动任何一步：

1. **known development / mechanism repair**：只在已知 051–054 regression 和明确新增 unit cases 上迭代。
2. **完整已知回归**：G1–G6 known/stress，全量 should-keep / should-drop，完整 Deep Research 和真实 render。
3. **pre-paid independent whole-artifact qualitative review**：由独立 reviewer 真实阅读全文/render，用与 Terra 相同的 A/B/C contract；任何显著 B blocker 在这里返回开发，不消耗最终 paid gate。
4. **freeze candidate identity**：source snapshot、plugin snapshot、hash、normal-entry replay identity 固定。
5. **fresh batch freeze + completeness preflight**：只检查 source 是否语义完整、是否符合预先定义的 capability coverage；不能看输出后换题。
6. **fresh execution on same candidate**：G7。出现 product failure，则该 candidate 的 release attempt 失败；不针对已曝光 holdout 打补丁后继续称它 fresh PASS。
7. **failure attribution / rubric adjudication**：在花最终 paid review 前先把 source defect、rubric defect、environment defect 与 product defect 分开。
8. **paid Terra / independent final verification**：只验证同一 final candidate 的 A/B，以及单独报告 C；不允许第一次在这里才读完整成稿。
9. **release production entry**：同一 candidate 执行 official install/upgrade/fresh-session smoke、release CI、final Reviewer、用户验收和 integration。

### 为什么 qualitative review 要在 fresh 前还是后

最省成本的做法是：**已知完整 artifact 的独立 qualitative review 在 candidate freeze / fresh 之前；fresh 之后仍需一次 final independent verification，但它不应承担基础问题发现。**

这样能避免两种浪费：

- 候选连已知长文都不像成稿，却先烧 unseen/fresh 与 paid budget；
- 只在 known artifacts 上调到好看，没有任何 fresh generalization 证明就 release。

---

## 9. 合法 recovery strategy

下一轮不能再设计成“一次 Terra 第一次发现问题 -> 整个 task 永久报废”，但也不能破坏 fresh integrity。

### 情形 1：pre-paid qualitative review 发现 product defect

返回开发，修机制；重跑受影响回归 + G1–G6；重新 freeze candidate。因为 fresh 尚未曝光，不损害 fresh integrity。

### 情形 2：fresh 暴露真实 product defect

当前 candidate 的 release attempt 失败。已曝光 item 永久降级为 regression；修复后若要再次声称 fresh generalization，需要新的、预先冻结的 fresh batch，并经过新的批准范围。不得换一道题继续拼 PASS，也不得把失败样本修好后重新标 unseen。

### 情形 3：reviewer rubric defect

保存原 review，不篡改。按 frozen A/B/C requirement 做独立 adjudication；如果 candidate 未改且明确是 reviewer 越界，可以记录“原 review finding 被裁定 non-blocking”，而不是伪造一份新的模型 PASS。

### 情形 4：source defect / invalid evaluation source

若 source 本身不完整、错误或不属于 gate 的预定分布，记录 evaluation-source defect。不能在看过 candidate 结果后静默替换同一 fresh slot；下一次有效 generalization proof 必须是新批准的 frozen batch。

### 情形 5：environment / harness failure

只要 candidate、prompt/source 和 grader contract 没变，允许对同一 frozen item 进行 infrastructure recovery；必须保留失败证据并证明重跑仅修复环境。

### 情形 6：paid Terra 发现此前未见的真实 product defect

该 release candidate 不通过。后续修复不是“同一 final candidate 继续 PASS”，而是新的 candidate certification attempt；是否需要新的 paid call、fresh batch和任务载体由当时 Planner/Critic 根据变更范围决定。**不自动创建 successor task，不把某个号码写死在本 proposal。**

---

## 10. 外部研究与采用决定

本轮在 2026-09-15 做了当前网页研究，目的不是引入依赖，而是寻找反例和成熟实践。

### 10.1 Anthropic — *Demystifying evals for AI agents*（2026-01-09）

URL: https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents

采用状态：`SELECTIVELY_ADOPTED_AS_DESIGN_REFERENCE`

采用：

- capability eval 与 regression eval 分开；
- deterministic / model / human grader 各自适合不同性质；
- model grader 要用 human judgment 校准；
- open-ended task 更应看最终 outcome，而不是死扣内部步骤；
- grader bug / ambiguous spec 会制造假失败；
- 多层 eval 比单一 metric 更可靠。

对应 Clear Writing：mechanical fidelity/math checks 不能代替整篇 reader review；Terra rubric 必须先在 legitimate code/path/future-work cases 上校准。

不采用：agent transcript/tool-call 评价本身不是 Clear Writing 的主要 release target，本文档不据此增加新的 workflow telemetry。

### 10.2 OpenAI — Graders / Evals API reference

URL: https://platform.openai.com/docs/api-reference/graders

采用状态：`SELECTIVELY_ADOPTED_AS_DESIGN_REFERENCE`

采用：官方 grader 体系本身把 string check、text similarity、model grader、Python grader、multi-grader 分成不同工具，支持“不同属性用不同 grader”的设计。Clear Writing 应据此保持 G2 fidelity、G3 structured technical correctness、G5/G6 qualitative quality 的分工，而不是让一个总分或一个 Terra prompt 混判一切。

不采用：本 proposal 不要求 OpenAI API 成为 runtime/release dependency，也不启动任何 paid grader。

### 10.3 Pandoc filters / AST

URL: https://pandoc.org/filters.html

采用状态：`REFERENCE_ONLY / PRINCIPLE_ADOPTED`

采用：成熟 document transformation 先把文档解析为结构化 AST，再对结构节点变换；这支持一个现实反例——code、math、table、link 并不是“普通 prose 里长得奇怪的字符”，而是不同语义/结构对象。

不采用：不因此把 Pandoc 设为 Clear Writing runtime dependency；是否复用 parser 需未来实现阶段单独比较。

### 10.4 Vale markup scopes

URL: https://vale.sh/features/markup

采用状态：`REVIEWED_NOT_ADOPTED_AS_CORE_ARCHITECTURE`

Vale 明确区分 prose 与 code/URL/markup structure，并让 lint rule 只作用于正确 scope。这直接反驳 blanket code/path regex。但 Vale 自己也明确是 prose style linter，不是 general-purpose writing aid，因此不能解决 semantic reader relevance、source fidelity 或 document-level rewrite。

采用其“structure-aware, scope-aware”的设计原则；不把 Vale 当主生成/评审引擎。

### 10.5 QAFactEval（NAACL 2022）与 AlignScore（ACL 2023）

URLs:

- https://aclanthology.org/2022.naacl-main.187/
- https://aclanthology.org/2023.acl-long.634/

采用状态：`REFERENCE_ONLY / FIDELITY_CONCEPT_ADOPTED`

两类工作都把 factual consistency 定义为 **generated text 与 input/source information 的一致性**，而不是自动验证世界上所有事实。这与 Clear Writing 的 A/source-fidelity 边界吻合。

不采用：自动 metric 不应成为 release oracle；长文 coherence、reader quality、code/path relevance 仍需 qualitative judgment。

### 10.6 Document-Level Text Simplification（EMNLP 2021）

URL: https://aclanthology.org/2021.emnlp-main.630/

采用状态：`REFERENCE_ONLY`

采用：document-level simplification 被单独提出，论文同时做 automatic 与 human evaluation，说明长文质量不能从 sentence-level improvement 直接推出。

不采用：D-SARI/SARI 的 reference-based simplification setting 与 Clear Writing 的技术长文 source-faithful rewrite 不同，不能直接作为我们的 release metric。

### 外部研究总判断

外部成熟实践并没有支持“继续加词表”。相反，它们共同支持：

- 对不同能力使用不同 evaluator；
- 把 document structure 当结构，而不是字符；
- 把 source consistency 与 external fact-check 分开；
- 长文需要 whole-document / human-like qualitative evaluation；
- grader 本身也必须校准和审计。

因此当前架构不需要推倒重来，但 reviewer/semantic-role/whole-document responsibilities 必须重构。

---

## 11. Expected release claim

若未来所有 gate 由同一个 final candidate 直接通过，允许的 release claim 应限制为：

> Clear Writing 的正式发布版本可从普通安装入口稳定处理中文/中文主导的 source-faithful 科研与技术改写：在允许结构重组和自然中文表达的同时保留 source claims/evidence/公式/表格/引用与必要复现信息，能清理 dirty wrapper、正确处理 legitimate code/path/config/future work，并通过完整长文、fresh generalization、真实 render、production-entry 和独立定性审查；light Chinese、English scientific prose、fidelity-only 等既有 compatibility routes 不回归。

不得声称：

- 自动 fact-check；
- 任意领域 factual correctness；
- `stable` maturity；
- 所有长文/语言风格都零人工修改；
- paid Terra PASS 等于真实用户长期满意。

`docs/PLUGIN_MATURITY.md` 当前仍将 `writing-style` 标为 `unclassified`。本 proposal 不预先提升 status；只有真实 production task + user acceptance 达到对应定义后，才能另行依据事实决定 `baseline` / `alpha`。

---

## 12. Explicit non-goals for the next implementation cycle

即使 Critic 后续 PASS，也不应在同一实现范围顺手做：

- plugin slug rename / directory migration；
- 新 top-level plugin；
- Research Authoring 重构；
- Bridge Kit 新架构；
- 新 automation / watcher / control schema；
- 大规模外部语料摄取；
- 默认联网 fact-check；
- 以“AI 味”禁词库为核心的风格系统；
- 为通过已曝光 fresh 样本写 sample-specific rule；
- maturity status 提升本身。

---

## 13. Unresolved evidence / Critic 应重点质疑的地方

当前仍有几项需要 Critic 独立核查，Proposal 不把它们伪装成已解决：

1. **054 branch 的哪些 production changes 值得 selective port。** 当前 main 与 reviewed/054 已 diverged，不能把 branch diff 整体视为正确实现；Critic 应检查 reader-relevance / rewrite-support 变化是否存在过度 schema 化或 test-specific logic。
2. **reader disposition 是否能用现有 Reader Plan 字段表达。** 本 proposal 明确反对为了语义分类再造大型 schema；实现前应确认最小表示。
3. **whole-document finish 的具体 owner。** 倾向复用 `chinese-prose` + assembly/final pass，不新建 runtime；但 Critic 应检查这会不会形成重复生成或 fidelity 风险。
4. **pre-paid qualitative reviewer 的具体承载方式。** 原则已经明确：必须独立、真实阅读全文、与 Terra rubric 同语义且不消耗最终 paid review；具体是本地模型、ChatGPT thread 还是现有免费 reviewer，应在后续可执行 Plan 中按可用工具选择，不在本 Proposal 锁死。
5. **fresh batch 的确切数量。** Capability coverage 已定义，但不应机械继承 054 的“恰好 3 个”。数量应由覆盖不同 failure mode 的最小集合决定，由 Critic 审核后冻结。
6. **external truth 的显示方式。** 默认 C non-blocking；如果 reviewer 发现 source 有明显错误，是否需要在 dossier 中给 user warning，应在后续 rubric contract 明确，但不得偷偷改正文。

---

## 14. Critic handoff

Critic 应针对本明确版本 `NEXT_RELEASE_PROPOSAL.md v0.1` 独立审查：

- `PARTIAL_REDESIGN` 是否真比 KEEP / REPLACE 更合理；
- semantic disposition 是否解决真实因果问题，还是换名字加 schema；
- whole-document finish 是否有明确能力增益且不重复；
- A/B/C reviewer split 是否会漏掉真正需要阻塞的 factual drift；
- Capability Gate Matrix 是否覆盖用户正常入口、真实 artifact 和 fresh generalization，同时没有过度 gating；
- recovery strategy 是否同时保护 fresh integrity 与可修复性；
- same-final-candidate requirement 是否足够严格；
- 是否存在更成熟、更简单的替代实现路线。

Critic 未对本 proposal version 明确给出 `PASS` 前，不得把它转成 executable Goal / Plan，不得启动实现、paid review 或 release。
