---
schema: AI_BRIDGE_REVIEWED_PLAN_V1
task_key: 047_writing_style_scientific_rewrite_architecture
decision: PLAN_FROZEN
---

# 047 Writing Style — 科研长文自然重写架构实验

## Objective and value

本任务要解决的不是“再找一些 AI 味词语”，而是当前 `writing-style` 在中文科研长文上的架构冲突：模型既被要求大幅降低阅读负担，又被一套越来越宽的表面保护与局部禁令限制在原句附近，最终容易得到“词换了、逻辑和机器句法还在”的结果。

044 已经提供严重 production failure 证据：当前 instruction-only + 大范围 protected spans + phrase scan + final reviewer 的组合，不能可靠同时满足“科学内容保真”和“真正自然的中文长文”。TRACE v8 -> v9 则提供相反方向的真实证据：在没有新 `writing-style` runtime 的情况下，先明确听众、页面目的、概念角色、读者应记住什么，再给正向表达方向并做全成品回读，语言明显改善。两者共同支持把主路线改成 **meaning-first scientific rewrite**，而不是继续扩规则。

047 因而冻结为一个 **实验性架构实现与验证任务**：在现有 `writing-style` plugin 内加入内部 `scientific-rewrite` 编排能力，把长篇科研/技术原文拆成完整论证单元，先建立近乎无损的意义与保真清单，再从“意思 + 原文”重写，最后分别做精确项检查、语义保真审计和全文语言/一致性复核。

本轮可以证明“这套架构是否值得进入 production release”，但当前冻结的 holdout 数量不足以证明 20–50 页中文科研长文已经成熟。因此即使 Reviewer 最终给 `PASS`，本任务的语义也只是 **bounded experimental architecture PASS**；不得自动宣称 `writing-style` 已达到 production maturity。

## Frozen decisions

### 1. Promotion decision

Feedback promotion decision: `PROMOTE_NOW`。

理由：044 已经从“待验证输入”变成了真实 production regression，而且用户明确要求长期跨项目解决“中文科研材料说人话但不改科学内容”的问题。Promotion gate 已满足“严重真实 production failure + 明确长期跨项目偏好”。本轮不再等待第二个同样失败的私有长报告，也不再把 044 的具体词汇扩成禁词表。

Target layer: `writing`，owner 为现有 `writing-style`。

Maintenance companion: `ai-skills-core`

Domain owner: `writing-style`

### 2. 顶级产品边界不变

- 用户入口仍然只有现有 `writing-style` plugin。
- 不创建新的顶级 plugin。
- `research-writing/research-reporting` 继续负责“从研究证据写一份报告”的科学叙事与结构；047 只负责**已有原文的高保真重表达**，不得抢走新稿写作/研究结构 ownership。
- `scientific-prose` 继续负责英文科研 prose，不被 047 重构。
- 044 branch 保持只读 known regression evidence；不 merge、不删除、不继续做 044 专用 rule repair。

### 3. 新增内部 `scientific-rewrite` skill

在 `writing-style` 内新增一个内部 skill，canonical source path 冻结为：

`skills/writing/core/scientific-rewrite/`

它是 orchestration contract，不是另一份大 banned-word prompt。职责固定为：

```text
original document
-> compact document map
-> complete argument/discourse units
-> meaning card + fidelity ledger
-> source-to-plan coverage check
-> metadata-selected positive transformations
-> rewrite from meaning + original
-> deterministic exact verification
-> semantic fidelity audit
-> targeted local repair
-> Chinese language-quality review
-> whole-document terminology/coherence review
```

### 4. `chinese-prose` 降级为语言目标与局部审阅层

`chinese-prose` 保留现有普通中文终审能力，但在科研长文深度重写中不再承担主算法。它只负责：

- 中文正向风格合同：具体主体/动作、关系显式、中文逻辑承担句子骨架、允许普通句子、语域匹配；
- 场景和 rewrite-problem 判断；
- translationese / noun-stack / workflow-language / reader-effort 的语言质量审阅；
- 普通轻度中文润色仍直接走 `chinese-prose`，不得因为新增 heavy route 而全部升级成 scientific rewrite。

禁止为 044 新增项目专用英文 blacklist、phrase wall 或“发现一个词就永久加一条规则”的实现。

### 5. `writing-fidelity` 必须拆开字面保护与语义保护

当前 blanket protection 把 headings/labels/section order 等 reader-facing wording 与数字/公式混成一类，本轮必须修正。

Literal preservation 只用于确实需要逐字/逐 token 保留的对象，例如：

- numbers / dates / ranges / units；
- formulas / notation / variables；
- citations / DOI / quoted exact source text；
- code / commands / paths / config / identifiers；
- formal algorithm, dataset, benchmark, metric, product names when exact naming matters；
- user-explicit no-touch spans。

Semantic preservation 用于允许彻底换句法但不能改变意义的对象，例如：

- claims and polarity；
- uncertainty / evidence strength；
- conditions / scope / exceptions；
- comparisons / comparators；
- chronology / causality；
- attribution / who observed or inferred；
- caveats / negative results；
- conclusion strength。

普通报告 heading、内部 workflow label、读者面对的小标题默认不是 literal-protected；只有正式题名、引用题名、精确标识符或用户明确要求原样时才逐字保护。

### 6. Meaning Card 不是摘要

每个 rewrite unit 至少包含：

- audience；
- purpose；
- claims；
- evidence/results；
- conditions/comparators；
- caveats/uncertainty/negative findings；
- literal-protected items；
- terminology；
- relation to previous/next argument；
- reader takeaway。

`reader takeaway` 只是生成辅助，不具有 factual authority。原始 source unit 始终与 Meaning Card 一起交给 writer；不得先把原文压成摘要后只从摘要生成。

必须先做 source -> meaning-card coverage check：重要 proposition 无法在 Meaning Card 中定位时，不得进入 rewrite。

### 7. 长文单位按论证边界切，不按固定 token 硬切

默认 rewrite unit 是一个完整小 subsection 或约 2–5 个逻辑紧密段落。definition、实验条件、结果、限制不得为了 token 均匀从中间切断。

每个 local writer packet 只携带：

- compact global document map；
- global terminology contract；
- 与当前单元有关的 cross-section dependencies；
- short previous rewritten tail（只读 continuity）；
- current original unit；
- small next-source preview；
- current Meaning Card + Fidelity Ledger；
- 3–5 个相关且多样的 seed transformations。

最终 whole-document pass 只能定位 terminology drift、重复定义、过渡、回指、结论强度漂移和局部 style outlier；不得再自由“全文润色一遍”。任何修复回到对应 local unit。

### 8. Positive transformation library 小而明确

P0 只建立 12–20 个高置信 seed transformations，不构建“大型 humanizer corpus”。建议覆盖：

- definition / first-use context；
- workflow/abstract label -> real subject + relation + action；
- comparison；
- method explanation；
- result interpretation；
- caveat / uncertainty / negative result；
- audit/log narration -> reader-facing fact；
- translationese / noun-stack；
- formal terminology that should remain unchanged。

每条 example 必须带 metadata：

`scene`, `discourse_function`, `rewrite_problem`, `rewrite_depth`, `fidelity_risk`, `register`, `source`, `license/provenance`, `approval_status`。

第一版只能使用 `SEED` / `REFERENCE` / `REVIEWED` 等真实状态；未经人类直接批准的例子不得叫 `HUMAN_GOLD`。

允许来源：两个已审计 MIT repo 中适合科研/技术写作的 transformation pattern，以及 TRACE v8 -> v9 中已经公开、非 holdout 的正向改写经验。禁止把 044、Bobbio holdout、Distributed Imaging holdout 的当前/未来输出加入 seed library。

Examples 只教 transformation，不提供 factual authority。优先把实体/数字 slot 化；writer contract 必须明确 `never borrow facts from examples`。

### 9. P0 retrieval 不使用 embedding/vector DB

固定用 metadata-based selection，从上面的标签中过滤并选 3–5 个多样例子。主题相似度不得优先于 transformation similarity。

不安装或引入：FAISS、Chroma、BGE、`sentence-transformers`、embedding API、Gemini、Claude、fine-tuning/DPO 或其他新 runtime dependency。

### 10. 外部来源采用方式

以下两个来源保持 `SELECTIVELY_PORTED`：

- `MrGeDiao/shuorenhua@6de1fcfeca5fff6fd15b28c619c11b6d41d1f657`, MIT；
- `whh110112/human-writing-skills@2b02ae77bd1ea009ea2d7a1cc6d2dcdce1437a00`, MIT。

`SOURCE_ADOPTION.md` 是 047 的 intake evidence。不得 wholesale vendor，也不得建立 runtime dependency。优先重新实现其**架构思想和小型数据结构**；如果确实复制上游 code/text，必须按当前 repository provenance/license convention 保存 attribution。不得复制 fiction/webnovel/character continuity，也不得把 shuorenhua 的 chat/social phrase lists 拉进 scientific route。

### 11. Deterministic helper 是小外壳，不是第二套框架

允许在 `scientific-rewrite` skill 内增加一个标准库为主的轻量 helper，例如 `scripts/rewrite_support.py`，只提供三类能力：

- `prepare`：识别 Markdown/text 的 section/paragraph boundaries，建立 unit ids 与可供 model 补充的 rewrite packet；
- `select-examples`：从 seed metadata 做 deterministic filter/diversity selection；
- `verify-exact`：依据 literal ledger 检查数字、日期、单位、citation、代码/路径、formal identifiers 等精确项是否遗漏/变异。

helper 不得判断 prose naturalness、claim polarity、causality 或 semantic equivalence。后者属于 model-assisted semantic audit 和独立 Reviewer。

如果实现该 helper，则 `scientific-rewrite` frontmatter 必须真实声明其执行能力；不得隐藏脚本执行边界。

### 12. 本轮是实验，不做 production release

Repository bump decision: `NONE`

Reason: 047 的冻结目标是验证一套新架构，当前两个 positive holdout + 两个 should-not-fix control 足够做 bounded experiment，但不足以证明 20–50 页长文 production maturity。本任务不得把实验性 branch 自动切入 main。

Affected plugins:

- `writing-style`: `NO_BUMP`
  - Reason: 即使 branch 上实现真实 user-facing candidate behavior，本轮仍是 experimental architecture evaluation；正式 production cutover/version bump 必须等本轮 Reviewer evidence 与用户后续接受后另行决定。
- `presentations`: `NO_BUMP`
  - Reason: TRACE 只提供 architecture evidence，不修改 presentations。

本轮 `PASS` 不改变 `docs/PLUGIN_MATURITY.md` 中 `writing-style: unclassified`。

## Implementation scope

### A. Canonical source changes

Executor 可修改/新增的主要 source 范围冻结为：

- `skills/writing/core/scientific-rewrite/`
  - `SKILL.md`
  - `assets/app-facing.svg`
  - 小型 `references/`：Meaning Card/Fidelity Ledger contract、positive-style contract、seed transformation library/schema 等必要文件
  - 可选但推荐的 `scripts/rewrite_support.py` 及其最小测试支撑
- `skills/writing/core/writing-fidelity/SKILL.md`
  - 只做 literal-vs-semantic preservation 与 source->candidate claim/relation audit 所需的边界重构
- `skills/writing/core/chinese-prose/SKILL.md`
  - 只做职责边界、positive-style/classification/language-review 所需的最小调整；不得继续扩 044 phrase rules
- `scripts/codex_marketplace_config.json`
  - 在现有 `writing-style` plugin 中增加 `scientific-rewrite` copy skill 与自然用户入口/routing description；不得新建 plugin
- 与本能力直接相关的 tests，例如：
  - `tests/test_scientific_rewrite.py`
  - 现有 Marketplace/routing/source-generated parity tests 的最小更新
- `docs/plugin-todos/writing-style.md`
  - 把本次已验证的 architecture-level feedback 从旧 `BLOCKED_NEEDS_EVIDENCE` 状态收口到与 047 一致的 promotion/实验记录；不得保留误导性的旧状态
- `docs/provenance/INTEGRATION_HISTORY.md`
  - 记录两个 exact upstream commits、MIT、selective adoption target；若没有逐字复制，可标明 distilled/selective architecture adoption
- `results/047_writing_style_scientific_rewrite_architecture/`
  - baseline/candidate experiment evidence、public holdout outputs、fidelity reports、routing/replay summaries、private Text Review encrypted/evidence files

Generated `.agents/plugins/marketplace.json` 与 `plugins/codex/plugins/` 只能由现有 generator 从 source regenerate，禁止手改。

### B. Routing contract

Front door: `writing-style`。

Neighbor skills:

- `chinese-prose`: 轻度/局部中文润色与普通终审；
- `writing-fidelity`: 保真 guardrail/audit，不独自承担长文生成；
- `research-reporting`: 从项目证据**新写**科研报告；
- `scientific-prose`: 英文科研 prose；
- `research-paper-workflow`: 正式 manuscript planning/drafting/review。

Should-trigger natural requests（至少这些语义必须覆盖）：

1. “把这份中文科研长报告重新讲得自然一点，但数字、公式、引用和结论都不能变。”
2. “这篇技术报告内容是对的，但太像运行日志了，按原意重新写成人能连续读的中文。”
3. “不要总结，也不要删限制条件；把这几节科研说明说人话。”
4. “保留算法名和数据集名，把其余中英混杂的内部工作流语言改成正常科研中文。”
5. “这份结果报告事实不能动，但标题、句法和解释顺序可以重写，让第一次看的研究者能直接理解。”
6. “按原文逐条保留 claim/caveat，把长段落重新组织得更清楚。”
7. “把整份 Markdown 科研报告做一次高保真自然重写，不是局部润色。”

Should-not-trigger：

1. “帮我从这些实验结果新写一份组会报告。” -> `research-reporting`
2. “把这两句中文润色一下/改顺一点。” -> `chinese-prose`
3. “润色这段英文 Results/caption。” -> `scientific-prose`
4. “帮我规划整篇论文结构/写 rebuttal。” -> `research-paper-workflow`
5. “只检查数字、版本、公式有没有被改。” -> `writing-fidelity` audit，不启动 heavy rewrite。

用户不需要知道 `scientific-rewrite` 内部名称、external repo 名或 helper 命令。

### C. Implementation sequence

为了保护 holdout，执行顺序冻结为：

1. 读取并确认 047 PLAN / REQUEST / SOURCE_ADOPTION / HOLDOUT_MANIFEST；
2. 使用两个 external repos、TRACE architecture evidence、044 known regression 和 synthetic/non-holdout fixtures 设计/实现 candidate；
3. 建立 12–20 seed transformations 与 helper/tests；
4. 用 044 做 known-regression replay，允许只做**通用机制**修复；不能加入 044-specific phrase rules；
5. 完成 source/generated parity、normal installed routing、unit/regression tests；
6. 冻结 candidate implementation commit；从此不再改变 production code/prompt/examples/helper behavior；
7. 一次性执行完整 frozen evaluation batch：base `8909eb1389dcc419d3168c13e1cddbcf252134cf` 与 candidate 在两个 positive holdout 上做对照，同时执行两个 should-not-fix controls；
8. batch 开始后不得根据其中任何一项结果修改 production behavior，也不得替换失败 item；
9. 生成结果/审计 artifact，进入 CI / Reviewer；
10. Reviewer PASS 后仍不 merge main，等待用户后续决定是否把该 experimental architecture 作为正式 `writing-style` release。

## Acceptance and regression gates

### A. PROCESS PASS — 必要但不能证明语言质量

以下必须通过，但任何一项都不能单独构成 PRODUCT PASS：

- branch source 与 generated Marketplace payload 一致；
- `python3 scripts/skills.py validate` 与相关 repository audit/marketplace checks 通过；
- scientific-rewrite helper/unit tests 通过；
- seed library 每条都有 metadata/provenance/status，且不存在 holdout/044 private material；
- metadata retrieval 可稳定选择 3–5 个多样例子，不依赖 embedding/vector DB；
- `verify-exact` 能报告 literal invariant drift，并对数字、单位、citation、code/path/formal identifier 有正负 fixtures；
- normal installed `writing-style` front door 能区分 heavy scientific rewrite、light chinese-prose、新稿 research-reporting 与 English scientific-prose；
- 044 fresh candidate replay 通过正式 installed `writing-style` path，而不是手工临时 prompt；
- GitHub required CI 对 candidate commit 明确 PASS；若 CI evidence 尚未可读，只能继续等待，不能推导 PASS。

### B. 044 known-regression gate

044 不算 unseen，但新架构必须关闭它暴露的根本问题：

- 完整 final rewrite 不能靠删信息/总结获得“变短”；
- scientific claims、数字、公式、算法/数据集名称、引用、caveat、negative result、条件、uncertainty、conclusion strength 不得发生 critical drift；
- ordinary English abstractions/workflow labels 不得继续作为中文标题或句子骨架；判断按具体语境，不按 blacklist；
- 不能只做 `anchor -> 锚点`、`provenance -> 来源追踪` 这类逐词替换后保留原机器逻辑。

private 044 plaintext 不得 commit。最终 044 candidate 必须通过现有 `GPT_Codex_AI_Bridge_Kit` Text Review transport；047 不实现新的 transport。

Task-local private Text Review paths 冻结为：

- encrypted payload: `results/047_writing_style_scientific_rewrite_architecture/text_review/payload.age`
- manifest: `results/047_writing_style_scientific_rewrite_architecture/text_review/text_inputs.json`
- evidence: `results/047_writing_style_scientific_rewrite_architecture/text_review/TEXT_REVIEW.json`

Text Review 必须绑定当前 candidate implementation identity 与 final plaintext SHA，并同时检查 semantic fidelity + whole-document natural Chinese/reader effort。缺失、stale、SHA mismatch、manifest mismatch 或 non-PASS 都不能支持 Reviewer PASS；如果 evidence 尚在等待，语义是 `WAITING_FOR_EVIDENCE / NEEDS_REVIEW`，不是 BLOCKED。

### C. Positive frozen batch — 架构是否真的改善

Frozen identities 只能来自当前 `HOLDOUT_MANIFEST.md`：

- Bobbio `README.md` exact commit/blob，lines `1-70`；
- Distributed Imaging `SEGCOMM_CORRECTION_STABILITY_REPORT_2026-08-28.md` exact commit/blob，lines `1-8`。

在 candidate implementation freeze 后，对每个 unit 同时生成：

- base (`writing-style 0.1` at base commit 8909eb...) output；
- candidate Architecture-C output；
- exact fidelity report；
- semantic fidelity report；
- reader-facing comparison artifact。

Gate 顺序固定：**先保真，再比较自然度**。

Critical fidelity violation 必须为 0，至少包括：

- number/formula/citation/identifier corruption；
- claim polarity reversal；
- omitted caveat/negative result/condition；
- changed comparator/scope；
- erased uncertainty；
- conclusion-strength upgrade；
- invented or reattributed scientific/technical claim。

只有两个 candidate 都通过 critical fidelity gate 后，Reviewer 才比较 base vs candidate 的：

- natural Chinese；
- reader effort；
- terminology correctness；
- relation/argument clarity。

Acceptance bar：candidate 在**两个 positive units 上都必须至少不差于 base**，并且至少一个 unit 显示明确、可引用的 reader-effort/naturalness 改善；任一 positive unit critical fidelity fail 或明显更难读，整个 positive batch 失败。不得挑赢家、替换失败项或改完再把同一项称为 unseen。

### D. Should-not-fix / low-edit batch

Frozen identities：

- AI Research Toolkit `R_RESEARCH_STACK.md`, lines `1-13`；
- Asteria `ROADMAP.md`, lines `5-17`。

这两个本来已经可读，目标不是“必须改出差异”。Acceptance：

- heavy scientific-rewrite router 应识别为低改写需求，允许输出“无需深度重写/只需极轻微调整”；
- 不得翻译/改坏 `renv`, `Bioconductor`, `BiocManager`, `sessionInfo()`、Asteria 等正式名词；
- 不得删版本/环境/证据边界；
- 不得把已经自然的中文改成更口语、更宣传、更模板化的 prose；
- 任何实际改写都必须保持 critical fidelity violation = 0。

任一 control 出现明显 over-rewrite，整个 SNF gate 失败。

### E. PRODUCT / ARTIFACT PASS — Reviewer 必须直接读成品

Reviewer 不能依据 Executor summary、phrase scan、English ratio、AI detector、regex hit count 或测试数量判断语言质量。

最终 Reviewer 必须实际读取：

- public positive holdout 的 base/candidate outputs；
- should-not-fix outputs/decision；
- claim-level semantic fidelity reports；
- 044 fresh `TEXT_REVIEW.json` 及 identity/sha binding；
- candidate implementation diff 与 normal-entry routing evidence。

只要 final artifact 不可访问或 Text Review 未到，不能 PASS。

`PROCESS PASS` 与 `PRODUCT / ARTIFACT PASS` 必须在 RESULT/REVIEW 中分开写。

### F. Experiment interpretation / release boundary

若 A–E 全部满足，Reviewer 可以给 Reviewed Handoff `PASS`，但必须明确：

- 证明的是 047 bounded Architecture-C experiment 成立；
- 不是 20–50 页中文科研长文 production maturity；
- `writing-style` 仍 `NO_BUMP`；
- 不自动 merge main；
- production cutover/version release 是后续用户决策。

若 candidate 在 frozen positive/SNF batch 上失败，不允许在本任务中替换 holdout 追逐 PASS。Reviewer 应 `REVISE` 只在仍有合法 review round 且修复可在 known/non-holdout regression 上完成时使用；下一批 fresh holdout 必须经过新的用户许可，不能在 047 内自适应生成。

## Natural-language usage / routing expectations

成功的 branch candidate 应让用户仍然只面对 `Writing Style`，自然说出类似请求即可：

> 把这份中文科研长报告重新讲清楚。内容不要总结，数字、公式、引用、算法名和结论强度都不能变；英文专名该留就留，但普通工作流语言不要再撑着中文句子。

系统内部应自动把长篇高保真重写交给 `scientific-rewrite`，而不是要求用户手工运行 Meaning Card、claim ledger 或 helper。

轻量请求例如“把这两句话改顺一点”仍直接由 `chinese-prose` 完成；“从这些结果新写一份组会报告”仍交给 `research-reporting`。新增能力必须减少用户负担，不能把内部 pipeline 暴露成用户必须操作的步骤。

## Out of scope

以下均不得被 Executor 或 Reviewer 扩成 047 blocker：

- Gemini / Claude / 任意多模型 routing；
- OpenAI/Gemini embedding API；
- FAISS / Chroma / BGE / sentence-transformers；
- fine-tuning / SFT / DPO / preference training；
- 新顶级 plugin；
- wholesale vendor `shuorenhua` 或 `human-writing-skills`；
- fiction/webnovel/character/persona/style-imitation 能力；
- AI detector evasion、watermark/source hiding、伪原创；
- 以 044 具体英文词构建项目禁词表；
- 自动从用户全部历史文档学习个人 voice；
- 用本轮两个 holdout 声称广泛 20–50 页长文 maturity；
- 修改 `presentations`、`research-writing`、`medical-imaging` 等相邻 plugin 的 production behavior；
- 新建数据库、服务、daemon、MCP 或网络 runtime；
- 在 Reviewer PASS 前 merge 047 到 `main`。
