---
schema: AI_BRIDGE_REVIEWED_PLAN_V1
task_key: 048_writing_style_product_cutover_and_readable_report
decision: PLAN_FROZEN
---

# Reviewed Handoff Plan

## Objective and value

本任务不是再做一轮架构实验，而是把 `writing-style` 的中文科研长文重写能力真正收口成可用产品，并用用户那份 22 页 Deep Research 报告作为最终真实交付物验证。

最终必须同时交付两件东西：

1. 一个通过正常安装入口即可使用的 `writing-style`，能够把“已有中文科研/技术长文说人话但不能改科学内容”自动路由到内部 `scientific-rewrite`；
2. 一份完整、信息不缩水、科学含义不漂移、但明显更容易连续阅读的 Deep Research 报告重写版，供用户随后直接阅读并据此开展实验。

二者缺一不可。047 的实验实现和公开回归已经证明 meaning-first 路线值得继续，但 047 因私有报告外发政策被验收合同卡住，没有 Product PASS。048 的任务是保留有价值的实现，移除错误的私有传输阻塞，把验收重新绑定到真实产品目标。

Feedback promotion decision: `PROMOTE_NOW`。

真实依据：用户已经明确长期跨项目要求“科研长文在不改变事实、数字、公式、引用、术语、证据边界和结论强度的前提下显著降低阅读负担”；044 的真实产物暴露了当前 instruction-only / phrase-scan / blanket protection 路线的严重 production failure；047 又提供了独立公开材料上的正向架构证据。Promotion gate 已满足严重真实失败 + 明确长期偏好。

Target layer: `writing`

Maintenance companion: `ai-skills-core`

Domain owner: `writing-style`

## Frozen decisions

### 1. 产品边界

- 顶级用户入口仍然只有现有 `writing-style`，不新建 humanizer / scientific-rewrite 顶级 plugin。
- `scientific-rewrite` 是 `writing-style` 内部 heavy route，只处理**已有原文**的中文或中文为主科研/技术长文高保真重表达。
- `chinese-prose` 继续负责短文本、轻度润色、中文最终语言审阅；不得让所有中文请求都升级成 heavy route。
- `writing-fidelity` 负责字面不变量和语义关系保真；不得因为“保护内容”而把普通标题、句法、中文表达骨架锁死。
- `scientific-prose` 继续负责英文科研 prose；`research-writing` 继续负责从证据新写报告/论文结构。048 不修改这两个 ownership。
- 044 Reviewed Handoff 永久保持历史只读；不得 reopen、修改、继续消耗其 Reviewer/Planner budget。
- 047 保持历史实验分支；不得整分支 merge/cherry-pick。只允许从 implementation freeze commit `ade5a1f653f88df07eb0c70edfd016c744b1611a` 按当前 main 逐项重放仍然成立的 production source changes。

### 2. 保留 047 已验证的核心架构

`scientific-rewrite` 的 production contract 冻结为：

```text
original document
-> compact document map
-> complete argument/discourse units
-> Meaning Card + Fidelity Ledger
-> source-to-card coverage check
-> metadata-selected positive transformations
-> rewrite from meaning + original
-> deterministic exact verification
-> semantic claim/relation audit
-> targeted local repair
-> Chinese language-quality review
-> whole-document terminology/coherence review
```

Meaning Card 不是摘要，也没有事实 authority；原始 source unit 始终与 Meaning Card 一起进入 writer。Seed examples 只教 transformation，永远不得提供实体、数字、算法、数据集、结论或其他事实。

长文按完整论证单元切分，默认一整个 subsection 或约 2–5 个逻辑紧密段落；不得为了 token 均匀把定义、实验条件、结果、限制或结论从中间切断。

### 3. `writing-fidelity` 必须明确拆分两类保护

Literal preservation 只用于需要逐 token 保留的对象：数字、日期、范围、单位、公式/变量/符号、引用/DOI、精确引文、代码/命令/路径/config/identifier、需要精确命名的正式算法/数据集/benchmark/metric/package/product/method name，以及用户明确 no-touch span。

Semantic preservation 用于允许彻底换句法、但不能改变含义的对象：claim/polarity、uncertainty/evidence strength、scope/condition/exception、comparator、chronology、causality、attribution、caveat、negative result、decision logic、conclusion strength。

普通 reader-facing heading、内部 workflow label、section wording、英文抽象标签默认不属于 literal-protected；只要不是正式题名、引用题名、精确 identifier 或用户明确要求，就可以重写为自然中文。

### 4. 中文目标是正向表达，不是禁词表

`scientific-rewrite` / `chinese-prose` 的目标是让技术上有能力的研究者直接读懂：谁做了什么、为什么这样比较、证据说明什么、还有什么不确定、下一步决策是什么。

不得把 044 中出现的 `provenance`、`estimand`、`scientific gap`、`resource contract`、`state of the art` 等词做成项目专用 blacklist；它们只能作为“英文抽象标签承担中文句法”的真实回归例。不得使用英文比例、禁词数量、AI detector 分数作为 release gate。

### 5. 外部来源决定保持不变

- `MrGeDiao/shuorenhua@6de1fcfeca5fff6fd15b28c619c11b6d41d1f657`, MIT：`SELECTIVELY_PORTED`。只吸收正向中文风格、scene/scope、literal-vs-semantic protection、should-fix/should-not-fix 等已审计思想。
- `whh110112/human-writing-skills@2b02ae77bd1ea009ea2d7a1cc6d2dcdce1437a00`, MIT：`SELECTIVELY_PORTED`。只吸收 original/reference/source authority separation、claim-ledger fidelity、bounded long-form context 和 deterministic exact-check 等已审计思想。
- `AIScientists-Dev/academic-humanizer@94b88b23703bed7df507acae7d6d5876209a0cdf`：`REFERENCE_ONLY`，留给以后英文 academic-writing 审计；048 不吸收其 AI-tell 列表、em-dash house style、grant-writing 规则，也不扩展 `scientific-prose`。
- 不再 Source Scout；不引入 Gemini、Claude routing、fine-tuning、embedding、FAISS、Chroma、BGE、sentence-transformers 或任何新 runtime dependency。

若 current main 尚无稳定 provenance 记录，Executor 应把 047 `SOURCE_ADOPTION.md` 中两项 exact commit/license/decision 压缩到稳定 `docs/provenance/` 记录，并在 `INTEGRATION_HISTORY.md` 引用该稳定记录；不得把未 merge 的 047 results path 作为 production provenance 的唯一长期定位点。

### 6. 公开验证集角色固定为 regression，不再冒充 unseen proof

048 不消费新的广泛 source corpus。直接重放 047 已冻结的四个公开单元，角色改为固定 public regression batch：

- positive regression A：`YuukiAS/Bobbio@2d8a054bd34291dc061b8b64d5d841d458cc6296`, `README.md` lines 1–70, blob `0152199c6c5f9b75978b06318bc9b0e6b93c4830`；验证 workflow/product mixed-English skeleton 能否转成自然中文且保留 Zotero/Notion/Semantic Scholar/PubMed/arXiv/GPT/Codex 等正式名称。
- positive regression B：`YuukiAS/Distributed_Imaging_Inference@0e895fdbce37c34967d8375059154df1d76397f4`, `docs/SEGCOMM_CORRECTION_STABILITY_REPORT_2026-08-28.md` lines 1–8, blob `41c47f88042c7c877707546431df89674076e8f2`；验证真实科研结果、比较、限制和 formal terms 保真同时降低日志感。
- should-not-fix A：`YuukiAS/AI_Research_Toolkit@b822dff09794766a1a013b100eb8f78a45514c7b`, `R_RESEARCH_STACK.md` lines 1–13, blob `d315fd6bbd5c08e271ecea95b3a05d451bce78c2`；应保持低编辑/不深改，包名、版本、复现约束不能被“说人话”破坏。
- should-not-fix B：`YuukiAS/Asteria@80ad881bc88ad1caf017959e320e539028eb5a25`, `ROADMAP.md` lines 5–17, blob `1b5862a32e2ddbb6ad8e1805a4e785c158181de5`；已可读的技术推理不得被强行口语化或改弱产品/模型/证据区分。

这四个单元已经在 047 被看过，因此只能证明 regression/compatibility，不得宣称 fresh unseen generalization。真正的长文产品证明来自用户完整 Deep Research 报告的最终人工验收。

### 7. 私有 Deep Research 报告是最终产品 artifact，但不再走 Codex 私有外发

源 artifact 固定为用户已上传到 ChatGPT/File Library 的 22 页 PDF：

`共享预训练医学分割模型下的极低通信联邦适应：项目事实审计、算法前沿与下一轮实验决策`

Codex/Longleaf 不得再为了 048 把该私有 plaintext 发送到外部 Codex/OpenAI endpoint，也不得再次申请 `auth.json` 或 token 来重演 047 的 transport gate。

当 production candidate 的 implementation commit 与 rewrite contract 冻结后，Executor 只在 public repo 生成不含私有正文的 `results/048_writing_style_product_cutover_and_readable_report/PRIVATE_ARTIFACT_HANDOFF.md`，至少记录：source title、intended audience、implementation commit、canonical rewrite contract paths、生成要求、禁止事项、待回填的 candidate SHA-256 / user ACCEPT|REJECT。

私有完整重写由 ChatGPT 已有附件/File Library surface 读取源 PDF 后生成。Public Git 只能保存 source identity/title、candidate SHA-256、contract/implementation identity、用户 ACCEPT/REJECT 和不泄密的简短 findings；不得保存原文或重写正文。

该报告必须是全文、长文、信息完整版本，不是 executive summary。必须保留所有科学上重要的项目历史、数字、样本量、数据集、模型、方法、比较、公式/符号、引用身份、不确定性、限制、负结果、STOP/GO 逻辑、下一轮实验建议和决策条件。允许重写普通标题、段落结构和句法，只要论证关系和科学力度不变。

### 8. Release / version decision

Repository bump decision: `PATCH`, **仅在两个产品 gate 都通过且用户明确 ACCEPT 后执行**。

以 048 base `5.0.3` 为参照，目标 release 是 `5.0.4`。如果 integration 前 `main` 已推进，保持“当前 main 的下一个兼容 patch”这一冻结语义，由 integration preflight 机械解析新数字；不得覆盖已有 release，也不得借机改成 minor/major。

Affected plugins:

- `writing-style`: `0.1 -> 0.2`, **仅在两个产品 gate 都通过且准备正式 cutover 时 exactly once bump**。
  - Reason: 新增普通用户可观察的长篇中文科研高保真重写 production route，属于 existing plugin 的 compatible user-facing improvement batch。

失败、用户 REJECT、只完成技术 candidate 或只完成报告时：`NO_BUMP / NO_CUTOVER`。

`writing-style` capability status 本轮默认保持 `unclassified`；一次真实长报告成功不足以自动宣称 `alpha/stable`，除非用户另有明确决定。

## Implementation scope

Executor 从当前 048/main 出发，逐项对照 047 implementation freeze commit `ade5a1f653f88df07eb0c70edfd016c744b1611a`，只重放以下仍成立的 production source change；不得 cherry-pick 047 的 task state/results/control-plane history：

- 新增 `skills/writing/core/scientific-rewrite/`：`SKILL.md`、`assets/app-facing.svg`、`references/meaning-card-and-fidelity-ledger.md`、`references/positive-style-contract.md`、`references/seed-transformations.json`、`scripts/rewrite_support.py`；
- 最小修改 `skills/writing/core/writing-fidelity/SKILL.md`：literal-vs-semantic preservation + claim/relation audit；
- 最小修改 `skills/writing/core/chinese-prose/SKILL.md`：heavy-route ownership 边界、positive-style/classification/final language review；
- 修改 `scripts/codex_marketplace_config.json`：仍只有 `writing-style` 顶级入口，加入 `scientific-rewrite` copy skill 和自然用户 routing/default prompt；
- 新增/更新与上述能力直接相关的 tests，至少覆盖 routing boundary、source/generated parity、seed factual-authority boundary、metadata selection、exact verification 和 heavy-vs-light routing；
- 稳定 provenance 记录：`docs/provenance/INTEGRATION_HISTORY.md` + 必要的一份小型 scientific-rewrite source-adoption note；
- `docs/plugin-todos/writing-style.md`：把 Deep Research 长文问题从旧 `BLOCKED_NEEDS_EVIDENCE` 整理为本次 `PROMOTE_NOW` / 048 active refinement；只有最终正式 release 后才标 `PROMOTED`；
- `results/048_writing_style_product_cutover_and_readable_report/`：只保存 public regression、production entrypoint、fidelity、private-artifact handoff/receipt 等不泄露私有正文的 evidence。

Generated `.agents/plugins/marketplace.json` 与 `plugins/codex/plugins/` 必须由 canonical generator 从 source regenerate；禁止手改 generated files。

不要机械复制 047 中与旧 base 冲突的版本测试或 presentations 版本预期；所有 expected versions 必须以 048 current main 为准。

Release closure 只有在最终用户 ACCEPT 后执行：更新 `scripts/codex_marketplace_config.json` 的 `writing-style` version、`docs/plugin-changelogs/writing-style.md`、root `VERSION`、root `CHANGELOG.md`、README release/plugin table 及对应 generated layer，然后跑版本一致性回归。若此时 main 在同一 writing/shared runtime 有竞争性改动，升级 integration preflight，不得强推覆盖。

## Acceptance and regression gates

### A. PROCESS PASS：只能证明工程流程正确，不能单独构成产品通过

必须全部通过：

- canonical Marketplace build/check/validate；
- source/generated parity；
- `scripts/skills.py validate` / 与本能力相关的 repository audit；
- focused scientific-rewrite / writing-fidelity / routing / marketplace tests；
- task-local temporary install smoke；
- current branch GitHub CI；
- working tree/task branch evidence clean，不含 private plaintext、token、auth 文件。

### B. Installed production-entrypoint technical gate

必须在 isolated/shadow Codex home/cache 中通过正常 Marketplace/plugin install 机制安装当前 048 generated `writing-style`，启动 fresh session，并用普通用户语言触发。

Heavy-route positive request必须能自动暴露/选择 `writing-style:scientific-rewrite`，用户不能被要求说内部 skill 名；light polish 必须仍留在 `chinese-prose`；只做数字/公式/引用审计时必须留在 `writing-fidelity`。source-tree 直接调用、benchmark helper、test-only router 都不能冒充 production entrypoint PASS。

不得修改 live global plugin cache。

### C. Public regression artifact gate

在 implementation identity 冻结后重放上面四个固定 public regression units，并保存 actual outputs/decisions/fidelity evidence。

两个 positive regression 必须做到：

- exact literal invariants 无 critical drift；
- semantic audit 不得出现 `broadened/reversed/invented/omitted/reattributed` 的未解决 critical violation；
- 读者负担相对 source/baseline 有真实下降，不能只是替换几个词仍保留机器/英文骨架；
- 不借 seed example 引入任何新事实。

两个 should-not-fix 必须判为低编辑/不深改，并保持正式术语、版本/复现约束、产品/证据关系。heavy route 不能因为存在就自动重写一切。

Scheduled GPT Reviewer 必须实际读取 committed public outputs 和 source range identity，不得只看 Executor summary、phrase scan 或 exact-check 数字。

### D. Private full-report artifact gate

技术 candidate 通过独立 Reviewer 后，任务进入最终人工验收；此时 `PRIVATE_ARTIFACT_HANDOFF.md` 必须已经绑定 exact implementation commit 和 canonical rewrite contract。

ChatGPT surface 依据原始 22 页 PDF 与该冻结 contract 生成完整重写。用户实际阅读后必须明确 `ACCEPT` 才能完成产品；仅“文件生成成功”不算通过。

用户验收至少同时判断：

- 是否仍然覆盖原报告所有科学上重要的信息和决策；
- 数字、公式、引用、模型/数据集/方法名、比较和负结果是否保持；
- uncertainty、scope、caveat、attribution、GO/STOP 条件和结论强度是否没有漂移；
- 是否显著少于原稿/旧 rewrite 的英文抽象标签、审计/仓库/流程语言和翻译腔；
- 是否可以作为研究者接下来阅读并据此跑实验的工作材料，而不是另一份需要二次“解码”的报告。

Public repo 的 acceptance receipt 只记录 candidate SHA-256、implementation/contract identity、`ACCEPT|REJECT` 和不敏感 findings。

若用户 `REJECT`：本 task 不完成。将反馈作为最高优先级真实 artifact regression，最多做一次 bounded generic repair；修复必须作用于通用 architecture/routing/fidelity/style contract，禁止加入该报告专属词表/句子规则。修复后重新生成完整私有报告再验收。

### E. Product completion / integration gate

`writing-style` 最终 Product PASS = 技术/公开 artifact 独立 Reviewer gate通过 + 用户完整私有报告 `ACCEPT`。

在用户 ACCEPT 之前：不得 bump version、不得 merge main、不得宣布 production cutover 完成。

在用户 ACCEPT 之后：按本 Plan 已冻结的 PATCH + `writing-style` next-release decision 做 release closure、integration preflight、最终版本一致性测试；若无冲突/branch protection/高风险迁移，则合回 main 并 push。普通机械 integration 不再要求用户第二次决定。

Visual Review: `NOT_REQUIRED`。

Bridge Kit private Text Review: `NOT_REQUIRED` for the private Deep Research artifact；最终 private qualitative gate 由用户本人在 ChatGPT attachment surface 验收，避免再次依赖已证实受限的 Codex private transport。Public regression artifact 由 Scheduled GPT Reviewer 直接读取 GitHub public evidence。

## Natural-language usage / routing expectations

Front door: `writing-style`。用户不需要知道 `scientific-rewrite`、外部 repo 名或内部 helper。

Should-trigger examples：

- “把这份中文科研长报告说人话一些，但不要改变事实、数字、公式、引用和结论强度。”
- “这篇技术报告内容没问题，但读起来像运行日志；按原意重新组织成自然中文。”
- “保留算法名、数据集名和所有限制条件，把这几节中英混杂的科研说明改成正常中文。”
- “不是摘要，整份 Markdown 都要保留信息，只是把句子和段落重新讲清楚。”
- “把这份实验报告改得第一次看的研究者能连续读下去，失败结论和 caveat 不能删。”
- “普通标题和内部 workflow 词可以改，但数字、引用、公式、比较和科学含义不能动。”
- “按原文完整保留证据和不确定性，重新写成自然的中文科研报告。”

Should-not-trigger examples：

- “把这两句话润色顺一点。” -> `chinese-prose`。
- “只检查数字、版本、公式和引用有没有被改坏。” -> `writing-fidelity`。
- “润色这段英文 Results/caption。” -> `scientific-prose`。
- “根据这些实验结果从头写一份新组会报告。” -> `research-reporting` / `research-writing`。
- “帮我规划整篇论文结构或写 rebuttal。” -> `research-paper-workflow`。

Neighbor skills: `chinese-prose`, `writing-fidelity`, `scientific-prose`, `research-reporting`, `research-paper-workflow`。

Routing reason: 用户只需要表达任务意图和保真要求；内部 heavy/light/fidelity 分流由 `writing-style` 负责，不能要求用户知道内部 skill 名。

## Out of scope

- 不修改 044 或 047 workflow 历史；不继续为旧状态机补 evidence。
- 不修改 `presentations`、`research-writing`、`scientific-prose` 或其他 plugin production behavior/version。
- 不新建顶级 plugin、profile、schema、state、requirement ledger 或第二套 reviewer transport。
- 不新增 Gemini、Claude provider、embedding/vector DB、FAISS/Chroma/BGE、fine-tuning/DPO。
- 不做新的广泛 Source Scout；`academic-humanizer` 本轮保持 reference-only。
- 不构建大型 humanizer corpus，不学习用户历史文章个人 voice，不做 AI detector evasion。
- 不把 044/Deep Research 私有正文或最终重写正文 commit 到 public Git。
- 不为了让公开 regression 好看而 adaptive 更换输入、把失败 public unit 加进 seed library，或宣称它们仍是 unseen holdout。
- 不以“所有 em-dash 都删”“英文词数量”“30 字以上句子”等单一表面规则作为产品质量真值。
- 不在用户最终 ACCEPT 前做版本 bump、main merge 或 maturity status 升级。
