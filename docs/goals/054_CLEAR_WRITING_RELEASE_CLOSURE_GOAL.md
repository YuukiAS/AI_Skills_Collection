# 054 Clear Writing Release Closure — Canonical Goal

本文件是 `054_clear_writing_release_closure` 的顶层 completion contract。任何 REQUEST / PLAN / CURRENT / RESULT / test / Reviewer / CI / Terra / release receipt 都只能服务于本 Goal，不能缩小或替换本 Goal。

默认中文汇报。代码、路径、命令、字段和正式名称保留原文。

## 1. 产品目标

054 的目标不是再做一次局部修补，而是把 Clear Writing 从“已有较强架构与大量局部证据，但 release-quality 仍不够稳定”收口到一个可以正常用于真实中文科研/技术重写的版本。

053 已经证明并实现了很多必要修复：

- raw wiki / HTML / template / citation scaffolding 不应直接泄漏到正文；
- 公式必须是可渲染的 Markdown/LaTeX math，而不是 fenced `text`；
- `k − 1`、指数、上下标、变量关系等不能在 normalization 中损坏；
- 简体/繁体目标应与请求一致；
- 普通英文和 `provenance/audit/当前 main/当前仓库` 等内部项目口吻应减少；
- 完整 Deep Research 长文必须直接由 final candidate 验证；
- candidate replay 应优先复用 OpenAI 官方 local marketplace / cachebuster / reinstall / fresh-session 开发路径，而不是发明新的插件 runtime。

053 最终没有发布，因为 fresh H1 暴露了一个新的真实问题：面向中文普通技术读者的重写把 source 中并非任务要求、也非理解/识别/归因/复现所必需的俄文别名提升成正文内容。该别名随后又触发当前中文数学 PDF renderer 的 Cyrillic glyph 缺失。053 frozen fresh batch 因此合法 FAIL，不能在原 batch 上修后重算 unseen PASS。

054 不把这件事升级成“任意 Unicode / 任意语言 renderer”工程。真正要修的是 Clear Writing 的 reader relevance / information selection：

> source 里的每个事实都不等于最终正文必须出现。对于面向中文读者的独立科研/技术成稿，应保留对理解、识别、归因、复现、精确技术身份或用户明确要求真正有价值的信息；对最终读者没有实际作用的来源包装、百科元数据、附带外语别名、重复链接、页面维护信息、编辑性说明等应被省略或压缩，而不是为了“保真”全部搬入正文。

但该规则不能变成“删掉所有非中文”。正式算法/模型/数据集/API/作者/文献身份、标准英文名、必要原文术语、代码/路径/配置、公式、用户明确要求的原名等仍应保留。

054 PASS 后允许的最大产品声明是：

**Clear Writing 已达到可正常投入真实中文/中文主导科研与技术文档重写使用的 production-validated 版本；能够在明确测试范围内同时处理长文结构、自然中文、数学/表格/引用、source fidelity、source-format cleanup、reader relevance 和正常 production routing。**

这不等于任意语言、任意文体、任意网页格式、任意领域内容都永不出错。

## 2. Source of truth 与继承关系

054 exact branch：

`reviewed/054_clear_writing_release_closure`

054 exact task-owned worktree：

`/tmp/ai-skills-054-clear-writing-release-closure`

054 branch 从 053 final evidence branch 的已记录人类决策点开始，但 053 本身保持：

`NOT_RELEASED / evidence-bearing / fresh batch FAIL`

不得改写 053 为 PASS，不得把 053 H1/H2 当成 054 fresh holdout，也不得在 053 上重跑后重新宣称 unseen PASS。

054 必须读取并继承 053 frozen production candidate：

`d4570c764326cd10b63eae5e605cc8ff885bd7f2`

053 在该 candidate 上已经给出有价值的 known-regression evidence，但 054 最终 release 仍必须在 **054 final candidate** 上重新跑关键 known regressions；predecessor evidence 只能做 baseline，不能替代 final-candidate evidence。

启动和最终 integration 前都必须 `git fetch origin`，并与 then-current latest `origin/main` 比较。若 latest main 有与 054 无关的可兼容变化，应正常整合；不得把旧 main SHA 当成永久基线。

## 3. Five-Pass preflight

### Product

最终用户消费的是完整 Markdown/PDF 成稿，而不是 validator receipt。054 的 release bar 是“真实稿件在多个维度都达标”，不是“又多几个 tests PASS”。

### Reality

当前 heavy route 架构继续保留：

`writing-style -> scientific-rewrite -> Meaning Map -> Reader Plan -> chinese-prose REALIZE_MEANING -> assembly -> writing-fidelity / semantic audit -> bounded repair`

`rewrite_support.py` 继续只做机械保护/验证，不得变成机械全文改写器。

### Alternatives

明确拒绝：

- 为一个偶然俄文别名扩成任意 Unicode 多语种 renderer 工程；
- 写“遇到俄语就删”的脚本/blacklist；
- 为 054 新建顶级 writing plugin / 新 heavy runtime；
- 用 PDF renderer 隐藏脏 Markdown；
- 用 phrase scan、English-count、validator PASS 冒充成稿质量；
- 只修 H1 wording 再把它重算 fresh PASS；
- 为了推进再添加自适应第三/第四 fresh holdout；
- 修改 Bridge Kit 来解决 repo-specific writing semantics。

Bridge Kit 只负责 general capability。054 的 Clear Writing、holdout、candidate replay consumer、repo-specific QA 与 release closure 全部留在 AI_Skills_Collection 内。

### Red Team

054 必须主动防止：

- 修“无关外语别名”时误删必要英文标准名、作者、算法、数据集、API、引用；
- 再次为了 literal fidelity 把 source metadata、workflow、网页包装全部塞进正文；
- 已修好的公式又退回 code fence / raw LaTeX；
- 数字还在但减号、指数、上下标、变量关系丢失；
- 长文结构变好但偷偷新增 source 不支持的解释；
- 简体正文又混入大面积繁体；
- 表格真实 render 时溢出、截断或 pipe source 直接可见；
- known regression 只跑旧 commit，不跑 054 final candidate；
- fresh source 选择本身与产品目标不匹配，制造无意义的边缘能力要求；
- Terra / Reviewer 只看 summary/receipt，不看实际 candidate；
- production smoke 只证明安装，不证明普通自然 prompt 真走到新能力；
- 只给用户看通过摘要，不给完整最终成稿。

### Execution readiness

053 已留下足够真实证据，054 不需要再次研究大架构。READY FOR EXECUTION，但先由 Planner 冻结 bounded Plan。

## 4. Upfront authorization envelope

用户发送引用本 Goal 的 kickoff prompt 后，明确授权 054 当前范围：

- exact branch/worktree 的普通 commit / fetch / non-force push；
- 读取 051/052/053 tracked evidence 与 repo-local private Deep Research baseline；
- 继续使用 OpenAI 官方支持的 local marketplace / cachebuster / reinstall / fresh-session candidate replay 路线；
- 同一份已授权 private Deep Research source，经当前既有 Codex/OpenAI provider、同一 purpose、同一 account/CODEX_HOME，最多 **2 次 054 candidate replay**；不得复制 credential、不得换 provider；
- exactly **3 个** public-safe fresh holdouts，一次性冻结完整 batch 后再生成；
- exactly **1 次**最终 `gpt-5.6-terra` Text Review，`store=false`，automatic paid retry `0`，worst-case per-call `<= USD 0.25`；
- required local tests、render QA、zero-paid CI；
- bounded production `writing-style@yuukias-ai-skills` install/upgrade smoke，开始前 snapshot，结束后 restore；
- 用户最终 ACCEPT 后 conflict-free latest-main integration + non-force push。

禁止 force/destructive Git、新 provider、新 credential location、复制 `auth.json`、无限 replay、额外 paid review、额外 private artifact、Bridge Kit/Host Policy redesign。

同一 scope 不得重复询问用户。只有真正扩大 private data/provider/credential/cost/live-global target/destructive risk 才重新授权。

## 5. Planner 必须冻结的 owner 与职责

Maintenance companion: `ai-skills-core`

Domain owner: `writing-style`

`ai-skills-core` 负责 AI_Skills repo maintenance closure：source authority、TODO/duplicate triage、generated parity、official plugin-development flow、unrelated regression、version/changelog/release policy、normal production-entry verification。

`writing-style` 负责语言、结构、信息取舍、fidelity 和 reader-facing quality。

`workflow-core` 只负责 Reviewed Handoff 状态与 gate，不替代 writing/domain 判断。

不得因为维护 companion 存在就重造 Codex plugin runtime。

## 6. Gate A — 继承 053 candidate + focused relevance repair

Planner/Executor 先证明 054 真正从 053 frozen production candidate 继承，而不是从 0.2 重新实现。

新增的核心产品规则必须是 semantic reader relevance，不是语言/script blacklist：

### 默认保留

- 公式、数字、变量关系；
- 方法/模型/算法/数据集/指标/API/package 等正式身份；
- 作者、文献、归因、时间、条件、限制、负结果、不确定性；
- 用户明确要求保留的原名/别名；
- 对检索或消歧真实必要的标准英文/原文名；
- 复现所需的 code/path/config/command。

### 默认不进入独立中文正文

若对理解、识别、归因、检索或复现没有实际价值：

- 来源平台的语言模板/alternate-language label；
- 百科式附带外语别名；
- 页面编辑/维护/归档元数据；
- 重复链接、重复来源包装；
- source-process / workflow / repository / audit 元数据；
- 对目标读者没有新增信息的语言学/页面身份信息。

该规则必须通过 **独立于 053 H1 的 public-safe/synthetic regression** 验证，至少包含一对 should-drop / should-keep：

- 一个无实际读者价值的外语别名/网页元数据应被省略；
- 一个真正必要的英文算法/模型/数据集/作者/标准身份必须保留。

不得使用 `Karatsuba / Алгоритм Карацубы` 作为 tuning fixture，也不得按具体语言写 hardcode。

Focused tests 必须先失败再修；不得通过固定 expected output 句子把模型逼向 test-specific wording。

## 7. Gate B — 全面 known-regression / stress matrix

在进入 fresh holdout 之前，054 final implementation candidate 必须同时关闭以下维度。任何一项失败都继续 repair，不得进入 fresh batch。

### B1 Reader relevance

- 新 reader-relevance regression PASS；
- 保留必要 formal identities，省略不必要 source metadata；
- 不出现“为了简洁把真正科学信息也删掉”的过修。

### B2 Raw source cleanup

重新跑 Bloom 和至少一个独立 raw-markup stress case：

- no `{{...}}` / `<ref>` / `[[...]]` / HTML comments / source template leakage；
- citation/attribution meaning retained；
- source-process framing 不复发。

### B3 Mathematics / operators

重新跑 FFT + operator regressions：

- 真正 renderable inline/block math；
- no fenced `text` formula；
- no raw LaTeX outside math delimiters；
- `k − 1`、负号、等号、不等号、指数、上下标、变量、`O(N^2)` / `O(N log N)` 等关系无损；
- PDF 实际排版可读。

### B4 Tables

至少一个真实 table-rich known/stress case：

- Markdown candidate 是有效表格或被有意识地重组；
- 不把 pipe source 当正文；
- A4 PDF 不溢出、不裁剪、不产生不可读小字；
- 行/列含义、数字、条件、比较方向不丢。

### B5 Chinese language quality

- 简体请求默认简体；明确繁体请求才繁体；
- 普通英文 process/abstraction words 不支配中文正文；
- 允许正式英文名和必要 lookup identity；
- 没有 `provenance/audit/candidate/pipeline/当前 main/当前仓库` 一类内部工程口吻；
- 段落衔接自然，不写成 bullet dump / audit log / source summary。

### B6 Source fidelity / claim-evidence

- 数字、公式、引用、归因、比较对象、条件、限制、不确定性、负结果和结论强度不漂移；
- 允许结构重组，但不得新增更强 source-unsupported explanation；
- proposition/evidence coverage 必须覆盖完整文档，而非只检查 token presence。

### B7 Compatibility routes

最终 054 candidate 必须重新跑：

- Python `re` technical rewrite；
- light Chinese polish；
- fidelity-only；
- English `scientific-prose`；
- explicit source-comparison/editorial task（确保 source-process rule 不误伤合法比较）；
- ordinary natural routing，不得 forced subskill。

### B8 完整 Deep Research headline artifact

必须对同一完整 private Deep Research source 直接运行 054 final candidate。

对比基线：

- 051 Gate 4 historical output：作为紧凑度、数学/表格、中文成稿 style floor；
- 0.2 diagnostic：作为已知失败 baseline；
- 053 final candidate：作为当前 strongest predecessor。

054 final Deep Research 必须同时做到：

- 数学/表格不低于 051 的可读性 floor；
- 保留 0.2/053 中真正有价值的结构清晰度；
- 明显减少不必要英文、内部审计/仓库语言和 source metadata；
- 不因 relevance filter 丢科学命题；
- 全文不是只检查第一页/前几页；
- Markdown 与 PDF 都需完整 QA。

第一次 054 Deep Research replay 是正常 final-candidate evidence；若它暴露可修 known regression，可在同一 scope 内做一次 bounded repair 并使用第二次 replay。若第二次仍不达标，本 054 不 release，不申请 routine 第三次。

## 8. Gate C — Pre-fresh release candidate freeze

只有 Gate B 全部 PASS，才允许冻结 production candidate。

冻结后记录：

- exact candidate commit；
- source/generated parity；
- all focused/full local tests；
- candidate replay identity；
- known regression matrix；
- Deep Research final candidate hash/locator；
- no open blocker list。

从此到 fresh batch 完成，不允许改 production code/rules/prompt/validator/renderer。

## 9. Gate D — exactly 3 fresh holdouts

Planner 在第一次 fresh generation 前一次性冻结完整 3-item batch。三项来自不同 document families，均 public-safe、语义完整、未用于 050–054 tuning。

### H1 — noisy technical source

包含真实 source scaffolding / markup / references / secondary metadata，目标是验证：

- 清掉 source packaging；
- 不过度保留无关 metadata；
- 保留真正 technical identity、attribution、formula/citation meaning。

不得为了测试任意语言字体而故意选择多语种边缘材料。

### H2 — formula + table-rich Chinese technical material

必须同时包含公式和真实表格/比较结构，用来验证 final Markdown + PDF，而不是只验证 prose。

### H3 — long-form Chinese scientific/technical material

足够长，必须需要 document-level restructuring，而不是一两段 polish。目标是验证结构、连贯性、信息取舍、fidelity 和自然中文。

### Fresh source preflight

冻结前只做 model-output-independent preflight：

- source 属于真实目标使用场景；
- selected range 完整，不截断公式/定义/列表/section；
- task requirement 明确哪些 scientific/technical facts 必须保留；
- 不把与目标产品无关的偶然 source metadata 自动升级成产品能力要求；
- 当前 canonical renderer 足以呈现 **任务真正要求保留的内容**。

不得为了“避免失败”看 candidate 后换样本。

### Fresh gate

三个 holdout 必须作为完整 batch 全部 PASS：

- actual candidate plugin consumption；
- ordinary user task；
- reader-clean Markdown；
- semantic/fidelity audit；
- actual PDF render；
- visual QA；
- formulas/tables readable；
- no raw markup / workflow leakage；
- natural target Chinese；
- reader relevance correct；
- no critical omission/invention/strengthening。

任何一个 true product/artifact failure => fresh batch FAIL，054 不 release。不得追加 H4 或 replacement 来拼 PASS。

## 10. Gate E — final independent Text Review

仅在 Gate D 完整 PASS 后，执行 exactly one final `gpt-5.6-terra` review。

review packet 必须让 Terra 实际阅读：

- 054 complete Deep Research final candidate；
- H1/H2/H3 三个 fresh final candidates；
- natural titles only；
- 不把 Gate/hash/Reviewer/Executor/commit wrapper 混入正文。

Terra rubric 至少覆盖：

- 中文是否自然、直接、像真正技术/科研成稿；
- 结构与过渡；
- 是否有不必要 source metadata / 外语别名 / engineering jargon；
- 是否有 raw markup / code-fence formula / unrendered math / raw table source；
- 数学、表格、引用、条件、限制是否明显损坏；
- 是否有 source-process/workflow framing；
- 是否有明显 unsupported strengthening / omission / reattribution。

Terra PASS 只是独立证据，不覆盖用户最终人工判断。

## 11. Gate F — release engineering / production entry

只有 artifact-quality gates PASS 后才做：

- source/generated Marketplace parity；
- full local test suite；
- required GitHub full/release CI；
- version/changelog/TODO closure；
- official local-marketplace/cachebuster/reinstall path smoke；
- bounded production install/upgrade smoke；
- fresh ordinary natural user prompt routing；
- actual `writing-style` candidate skill consumption evidence；
- restore live state after smoke；
- verify production identity/version。

054 不重新研究 no-install process-local plugin hot-loading；除非 OpenAI 官方 plugin tooling 在真实 normal path 上发生新的 concrete failure。

若 version policy 与当前保持一致，预期 `writing-style` 从 `0.2 -> 0.3`；Planner 必须读取 then-current version policy 后冻结 exact release decision。Repository version 只按现有 policy决定，不因单个 plugin 普通兼容改进自动升 minor。

## 12. Gate G — Scheduled GPT Reviewer

Reviewer 必须独立读取：

- real production diff；
- final skill/plugin source；
- known-regression matrix；
- complete Deep Research final artifact evidence；
- 3 个 fresh Markdown + rendered PDF / images；
- Terra evidence；
- full CI；
- production smoke；
- version/changelog/source-generated parity。

Reviewer 必须分别给出：

`PROCESS PASS/REVISE`

`PRODUCT / ARTIFACT PASS/REVISE`

只要存在以下任一项就不得 PRODUCT PASS：

- raw source/platform markup；
- formula code block / unrendered math；
- operator/symbol corruption；
- malformed/clipped/illegible tables；
- obvious Simplified/Traditional mismatch；
- unnecessary workflow/repository/audit framing；
- source metadata over-preservation；
- critical omission/invention/strengthening；
- long文结构明显 audit-like / dump-like；
- production normal prompt 没真正消费新能力。

## 13. Gate H — 只在内部全部通过后给用户看成稿

用户明确要求：不要在明显还有已知问题时提前交稿让用户充当 QA。

所以只有 Gate A–G 全部 PASS，才进入最终人工验收。

必须在 repo 内生成：

`private/exports/054_clear_writing_release_closure/Clear_Writing_0.3_Comprehensive_Acceptance_Dossier.pdf`

`private/exports/054_clear_writing_release_closure/Clear_Writing_Deep_Research_Final.pdf`

以及三个 fresh holdout 的最终 PDF（可作为 dossier appendix 或独立文件）。

Dossier 必须简洁但足够人工判断，至少包含：

- 0.2 已知真实失败摘要；
- 053 做对了什么、为什么仍未 release；
- 054 relevance repair 是什么；
- Bloom / FFT / reader-relevance regression 的 representative before/after；
- complete Deep Research final output 的关键章节与完整附件 locator；
- H1/H2/H3 fresh outputs；
- formula/table/render QA；
- Terra / GPT Reviewer 结论与 non-blocking notes；
- remaining limitations；
- 一页用户 checklist。

不得把 JSON / Gate 日志直接 dump 成 PDF。所有 Markdown table / math 必须真实 render。

只有此时才通知用户并请求：

`ACCEPT` 或 `REJECT`

用户 REJECT 优先级高于所有内部 PASS。

## 14. Final integration

只有用户明确 `ACCEPT` 后：

- fetch then-current latest main；
- 检查 branch diff / integration conflict；
- rerun integration-required checks；
- conflict-free integration；
- non-force push；
- verify remote main；
- verify released `writing-style` identity/version；
- 写 final integration evidence。

没有用户 ACCEPT，不得 release/integrate。

## 15. 完成语义

054 Goal 只有在以下全部成立时才允许 achieved：

- reader relevance repair PASS；
- full known/stress regression matrix PASS；
- complete Deep Research final candidate PASS；
- exactly 3 fresh holdouts complete-batch PASS；
- final Terra PASS；
- full tests/CI/source-generated parity PASS；
- official local plugin development/replay flow PASS；
- bounded production smoke + ordinary routing PASS；
- GPT Reviewer PROCESS + PRODUCT PASS；
- final dossier + complete Deep Research PDF generated；
- user ACCEPT；
- latest-main integration + released identity verification PASS。

任何 partial PASS、test PASS、CI PASS、Terra PASS、Reviewer PASS 或到达 human gate 都不等于 overall Goal completion。
