---
schema: AI_BRIDGE_REVIEWED_PLAN_V2
task_key: 054_clear_writing_release_closure
decision: PLAN_FROZEN
---

# Reviewed Handoff Plan

## Objective and value

把 053 已经显著改善但尚未发布的 Clear Writing candidate 收口成一个真正可以用于真实中文/中文主导科研与技术重写的 production-validated release。054 不重做 051/052/053 heavy rewrite 架构；唯一新的产品修复是 **semantic reader relevance / information selection**：来源中出现的事实、标签或包装，不等于最终独立中文成稿必须逐项呈现。最终正文只保留对理解、技术身份、归因、检索/消歧、复现、公式/条件/限制/负结果/不确定性或用户明确要求有实际价值的信息；来源平台语言标签、百科附带外语别名、重复链接、页面维护/归档元数据、workflow/repository/audit 包装等若没有读者价值，应省略或压缩。

这不是“遇到外语就删”的规则，也不是 renderer/font 工程。正式算法、模型、数据集、API/package、作者、文献、标准英文名、必要原文术语、代码/路径/配置、公式和用户明确要求的名称仍必须保留。053 的 Karatsuba H1 只作为失败历史和设计动机，不得成为 054 tuning fixture 或 fresh evidence。

Canonical completion contract 始终是 `docs/goals/054_CLEAR_WRITING_RELEASE_CLOSURE_GOAL.md`；本 Plan 只能使其可执行，不能缩小 Goal。

Process owner: `workflow-core`

Maintenance companion: `ai-skills-core`

Domain owner: `writing-style`

当前 release planning snapshot：repository `VERSION=5.0.4`，`writing-style=0.2`。按 `docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md`，如果本任务按本 Plan 完成并准备正式交付：

```text
Repository bump decision: PATCH
Current planned delta: 5.0.4 -> 5.0.5
Reason: compatible user-visible quality/reliability improvement in an existing plugin; no new repository-level capability.
Affected plugins:
- writing-style: 0.2 -> 0.3
  Reason: 054 completes a bounded user-visible Clear Writing quality/relevance release.
- all other central plugins: NO_BUMP
```

若 final release closure 前 `origin/main` 的 repository version 因无关 release 已前移，则 repository patch target 按 then-current main 机械顺延并重跑 version/parity/release checks；这不是产品 scope revision。若 `writing-style` 本身在 main 上发生竞争性 release/source 变化，则视为真实 integration conflict，不得静默覆盖。

## Frozen decisions

1. **继承而非重做。** 生产实现必须从 053 frozen candidate `d4570c764326cd10b63eae5e605cc8ff885bd7f2` 的能力继续，保留路线：`writing-style -> scientific-rewrite -> Meaning Map -> Reader Plan -> chinese-prose REALIZE_MEANING -> assembly -> writing-fidelity / semantic audit -> bounded repair`。053 保持 `NOT_RELEASED / evidence-bearing / fresh batch FAIL`，不得追认 PASS。

2. **reader relevance 是语义决策，不是脚本/语言 blacklist。** Meaning Map 仍负责 source authority；但 source anchor 被 accounted for 不代表该 anchor 的每个附带事实都必须成为 reader-facing proposition。Host Codex 可以把无关来源包装识别为 source-context / reader-irrelevant metadata，并在 Reader Plan/semantic audit 中作“已审阅但不进入正文”的语义决策。不要新建 Reviewed Handoff schema/state/ledger，也不要为了本规则新增第二套写作 runtime。

3. **保真保护 task-relevant substantive content，而不是保留所有 source bytes。** 必须保留：科学/技术命题及极性、证据、归因/引用、正式身份、公式与变量关系、数字、比较对象、条件、限制、负结果、不确定性、结论强度、复现所需信息和用户显式 protected content。允许省略/压缩的是对目标读者没有新增价值的来源包装与附带元数据。`writing-fidelity` 不得把 irrelevant source metadata 错当成 `inline-critical`，也不得以“完整保真”为理由把页面语言标签、重复链接、维护信息等强制塞入正文。

4. **exact item 机制不能替代 relevance 判断。** 不得把所有非中文 token/别名自动 exact-protect；也不得通过扩充正则把 reader relevance 变成机械删除。`rewrite_support.py` 仍只做机械保护/检测/失败关闭，不承担 prose authoring 或语义取舍。

5. **独立 should-drop / should-keep 回归先于真实 known matrix。** 必须使用与 053 Karatsuba H1 无关的 public-safe 或 synthetic 技术材料，至少形成一对互补回归：
   - should-drop：来源包含对理解/识别/归因/检索/复现没有价值的页面语言标签、附带外语别名、维护/归档元数据或重复包装；正常中文成稿应省略/压缩；
   - should-keep：来源包含真正必要的标准英文算法/模型/数据集/API/package、作者/文献身份、正式缩写或复现 token；成稿必须保留。
   测试只冻结“语义必须保留/可省略”的事实，不冻结具体目标句式，不得 test-specific wording。

6. **053 已修维度全部作为 hard regression。** Bloom/raw markup、FFT/renderable math、operator/sign/subscript/exponent、宽表 PDF、简繁、普通英文/internal audit、source-process、Python `re`、light Chinese、fidelity-only、English `scientific-prose`、explicit source-comparison exception、ordinary natural routing、source/generated parity 都必须在 054 final candidate 上重新通过。053 receipt 只能是 baseline。

7. **完整 Deep Research 必须重新生成。** 使用已授权的同一 private source `sha256=f447de7acaae76486e42e6281f9280b482c770303a67c0861256ddba67316213`，通过 054 final candidate 直接生成完整 Markdown/PDF。对比 051 style/render floor、0.2 failure baseline 和 053 strongest predecessor。054 最多 2 次 candidate replay：第一次若暴露可修 known regression，可修后使用第二次；第二次仍失败则 054 不 release，不申请 routine 第三次。

8. **fresh batch 只有一次、恰好 3 项。** 只有完整 known/stress matrix 与 Deep Research 全部 PASS 后，才冻结 exact candidate commit，再一次性冻结 H1/H2/H3。053 H1/H2 不得复用为 fresh，也不得在看到 candidate 后换样本；没有 H4。

9. **fresh source 选择先做 model-output-independent suitability preflight。** 只检查语义完整性、目标使用相关性、必须保留的技术事实和 canonical renderer 对任务真正要求内容的呈现能力。不得为了“压力测试字体”故意选择无关多语边缘材料，也不得先看 candidate 再调整 source range/task。

10. **fresh batch 开始后冻结产品行为。** production source/rules/prompt/validator/renderer 均不得依据任一 fresh 输出调优。一个 true product/artifact failure 即整批 FAIL，停止 Terra/release。只有明确发生在 candidate/model 输出之前、且没有暴露 candidate 结果的可恢复基础设施故障，才可按现有 policy 对同一冻结输入做 bounded retry；不得利用 retry 改候选或换任务。

11. **Terra 单次、最后进行。** exactly one `gpt-5.6-terra` Text Review，`store=false`、automatic retry `0`、worst-case `<= USD 0.25`。只有 known/stress、Deep Research、3-item fresh batch、Markdown/PDF/visual QA 全部 PASS 后才允许发送。review plaintext 只包含自然标题和 4 份真实最终 candidate（Deep Research + H1/H2/H3），所有 task/Gate/recovery/candidate/Reviewer/commit/hash wrapper 放 metadata。

12. **candidate replay 使用已硬化的官方正常路径。** 继续使用 OpenAI-supported local marketplace/cachebuster/reinstall/fresh-session 行为和现有 `candidate_plugin_replay.py` consumer；不重新研究 undocumented no-install hot-load，不改 Bridge Kit，不复制/symlink credential，不创建新 credential home。

13. **PROCESS PASS 与 PRODUCT / ARTIFACT PASS 分离。** CI、validators、hashes、source/generated parity、Terra 或 receipt 均不能单独证明 release-quality。实际 Markdown/PDF 和可见 public artifacts 必须通过人工/Reviewer 检查。

14. **用户只看最终内部全 PASS 的成稿。** 在 known/stress、Deep Research、fresh batch、Terra、full CI、production smoke、Scheduled GPT Reviewer 全部 PASS 前，不进入 final human artifact gate。用户 `REJECT` 覆盖所有内部 PASS；没有 `ACCEPT` 不得 integrate/release。

## Positive completion

054 只有在以下用户可观察结果同时成立时才算完成：

- 普通中文/中文主导科研与技术长文能够在保留必要科学/技术身份与 source fidelity 的同时，主动省略无读者价值的来源包装/附带元数据，而不是机械复制 source；
- 053 已修的 raw markup、数学渲染、运算符/上下标、表格、简繁、内部工程措辞、source-process framing 和长文 fidelity 均无回归；
- 完整 private Deep Research 由 054 final candidate 直接重放，Markdown/PDF 全文质量不低于 051 style/render floor，保留 053 的结构优势，并在 reader relevance 上进一步改善；
- exactly 3 个预冻结 fresh holdout 作为完整 batch 全部通过 actual candidate consumption、reader-clean Markdown、semantic/fidelity audit、真实 PDF render、visual QA、公式/表格、目标中文和 reader relevance；
- exactly one Terra review PASS；
- focused/full tests、source/generated parity、release CI、version/changelog/TODO closure、官方 plugin-development replay、bounded production install/upgrade smoke 和普通自然 routing 全 PASS；
- Scheduled GPT Reviewer 分别给出 `PROCESS PASS` 与 `PRODUCT / ARTIFACT PASS`；
- repo-local private acceptance artifacts 存在并可供用户直接检查：
  - `private/exports/054_clear_writing_release_closure/Clear_Writing_0.3_Comprehensive_Acceptance_Dossier.pdf`
  - `private/exports/054_clear_writing_release_closure/Clear_Writing_Deep_Research_Final.pdf`
  - H1/H2/H3 final PDFs（独立文件或 dossier appendices）；
- 用户明确 `ACCEPT` 后，任务与 then-current latest `main` conflict-free integration、non-force push、remote main 和 released `writing-style` identity/version 验证全部 PASS。

Maximum claim scope：可声明 Clear Writing `0.3` 已在本 Plan 覆盖的中文/中文主导科研与技术重写场景中完成 production validation，包含长文结构、reader relevance、source fidelity、数学/表格/引用、source-format cleanup 与正常 production routing。不得宣称任意语言、任意网页、任意领域或任意格式 universally correct。

任何实现 commit、局部测试、known regression、fresh batch、Terra、CI、Reviewer PASS 或到达人工 gate 都只是 `IN_PROGRESS`，不能单独称 Goal achieved。

## Non-substitutable semantics

- **Reader relevance 不是摘要。** 可以删除无读者价值的 source metadata，但不能为了“更简洁”删除技术命题、条件、限制、负结果、不确定性、正式身份、引用/归因或复现信息。
- **Source accounting 与 final inclusion 分开。** source anchor 可以被 Meaning Map 审阅并判定为非 reader-facing metadata；这不等于 source 没读，也不要求把该 metadata 再说给读者。
- **必要外文身份必须保留。** 判断标准是去掉后是否损失技术身份、检索/消歧、归因、复现或用户明确要求，而不是字符脚本。不得出现“非中文一律删”或特定俄文/英文 blacklist。
- **正式引用与重复包装不同。** 作者、论文、DOI/必要链接、标准名可保留；网页存档重复链接、语言导航、编辑/维护说明等若不服务正文任务可省略。
- **数学和表格是语义内容。** formula-like code fence、raw LaTeX、operator/sign/subscript/exponent 损坏、raw pipe table、PDF clipping/不可读表格都直接 FAIL；renderer 不能掩盖脏 Markdown。
- **结构重写允许重排，不允许 claim drift。** 每个 task-relevant substantive proposition 必须保持证据 authority、attribution、polarity、condition、comparator、caveat、uncertainty、negative finding 与 conclusion strength。
- **053 fresh failure不可洗白。** Karatsuba H1/H2 只做历史证据；不得修后重算 054 fresh，也不得作为 should-drop fixture。
- **Fresh evidence 必须来自完整冻结 batch。** H1/H2/H3 全部 PASS 才支持 generalization；跨 batch 拼赢家无效。
- **Private/paid scope 不变。** 只使用已授权 Deep Research private artifact、现有 Codex/OpenAI provider/account/CODEX_HOME 和当前 writing-validation purpose；最多 2 次 054 private replay；Terra exactly 1 次，预算上限不变。
- **最终 release 必须经过真实 production entry。** 不能用 direct source invocation、unit tests 或 receipt 替代官方 candidate replay与 bounded production smoke。

## Implementation scope

允许的 production change 只限于现有 Clear Writing 架构中 reader relevance 所属 owner layer，以及为防回归所需的最小测试/发布面：

- `skills/writing/core/scientific-rewrite/SKILL.md`：明确 source accounting、reader relevance 与 Reader Plan/semantic audit 的关系；
- `skills/writing/core/chinese-prose/SKILL.md`：中文 realization/final pass 对 incidental source metadata 的省略/压缩，以及 necessary identity 的保留；
- `skills/writing/core/writing-fidelity/SKILL.md`：把“task-relevant substantive fidelity”与“source wrapper/metadata preservation”分开，防止过删和过保留；
- `skills/writing/core/scientific-rewrite/scripts/rewrite_support.py`：仅在真正需要的机械边界做小改动；不得实现语言/别名黑名单、自动 prose deletion 或第二套语义分类器；
- 相关 focused tests（优先 `tests/test_scientific_rewrite.py` 与现有 writing-style/chinese/fidelity tests），包含独立 should-drop/should-keep、数学/表格/operator/source-process/variant/compatibility 回归；
- generated `plugins/codex/plugins/writing-style/**` 只能通过现有 source authority/generator 同步，不手改漂移；
- `docs/plugin-todos/writing-style.md`、`docs/plugin-changelogs/writing-style.md`、Marketplace/version/release dashboard、root release metadata 按 version policy 在 release closure 更新；
- `results/054_clear_writing_release_closure/**` 存 tracked public-safe evidence；
- `private/exports/054_clear_writing_release_closure/**` 存 private Deep Research、最终 dossier 与 private final artifacts，不提交 private plaintext。

不得：新建顶级 writing plugin、重写 heavy route、引入新 model runtime、改 Bridge Kit/Host Policy、创建新 Reviewed Handoff schema/state/ledger、扩成任意 Unicode renderer 工程、或用 renderer-only 修补 reader-relevance 问题。

Executor 在任何 production source edit 前必须确认 production `ai-skills-core` installed/enabled 并实际调用其 maintenance preflight；`workflow-core` 管流程，`writing-style` 管专业语言/保真判断。

## Acceptance and regression gates

必须严格按顺序执行；后面的 PASS 不能抵消前面的 FAIL。

### Gate A — inheritance + focused reader-relevance repair

1. fetch `origin`，重新读取 054 CURRENT，确认 exact branch/worktree 与 Executor ownership；记录 then-current `origin/main`，但不把旧 main SHA 当永久基线。
2. 证明 054 candidate 是在 053 frozen production candidate `d4570c...` 上继续，而不是从 production 0.2 重新实现。
3. 执行 `workflow-core + ai-skills-core + writing-style` maintenance preflight。
4. 在与 053 H1 无关的 public-safe/synthetic technical fixtures 上先建立 failing regressions，再做最小 semantic repair：
   - should-drop：无 reader value 的 source metadata/alternate-language/page wrapper 不进入独立中文正文；
   - should-keep：标准英文技术身份/作者/数据集/API/文献或复现 token 保留。
5. 明确证明实现不是 script/language blacklist，不按具体 `Karatsuba/Алгоритм Карацубы` 写特例，不把机械 helper 变成 prose rewriter。
6. focused tests PASS，source/generated payload 同步。

### Gate B — complete known/stress matrix on the 054 final implementation candidate

在进入 fresh 之前，下列全部必须在**同一个 final candidate commit**上重新跑并 PASS，并保存 actual candidate SKILL consumption 证据：

- reader relevance should-drop + should-keep；
- Bloom + 至少一个独立 raw-markup stress：无 `{{...}}`、`[[...]]`、`<ref>`、HTML/template leakage，citation/attribution meaning 保留；
- FFT + operator/sign/equality/inequality/subscript/exponent/variable relations，真实 renderable math，无 fenced `text`/raw LaTeX；
- 至少一个 table-rich case：Markdown 为有效表格或有意识语义重组；A4 PDF 无 clipping/overflow/不可读小字，行列含义/数字/比较方向保留；
- Simplified request 与 Traditional request 各自一致；必要 formal English 可保留，普通 internal/process English 不支配正文；
- internal audit/workflow/repository framing 与 source-process framing 不复发；
- source fidelity / proposition-evidence coverage：数字、公式、引用、归因、条件、比较、限制、不确定性、负结果、结论强度无 critical drift；
- Python `re` technical rewrite；
- light Chinese polish；
- fidelity-only；
- English `scientific-prose`；
- explicit source-comparison/editorial exception，确保合法 source-oriented framing 不被误伤；
- ordinary natural prompt routing，不能 forced subskill；
- source/generated parity；
- focused tests + full relevant local tests。

### Gate B8 — complete private Deep Research headline artifact

使用同一已授权 private source 直接通过 Gate B final candidate 生成完整 Markdown/PDF；normal evidence 是 replay 1，最多允许一个 bounded repair + replay 2。比较：051 Gate 4 style/render floor、0.2 diagnostic failure baseline、053 strongest predecessor。

PASS 必须同时证明：全文命题/证据边界无 critical drift；数学/表格不低于 051 floor；结构不低于 053 strongest predecessor；不必要英文、workflow/source metadata 与 audit framing 进一步减少；reader relevance filter 未删除必要科学信息；完整 Markdown 与完整 PDF QA，不只抽查首页。第二次仍不达标 => 054 不 release。

### Gate C — pre-fresh candidate freeze

只有 Gate A/B/B8 全 PASS 后才冻结：exact candidate commit、source/generated parity、tests、candidate replay identity、known/stress matrix、Deep Research final candidate hash/locator、open blockers=`none`。冻结后直到完整 fresh batch 结束，不得修改 production code/rules/prompt/validator/renderer。

### Gate D — exactly three fresh holdouts

第一次 fresh generation 前，一次性冻结完整 manifest：

- H1：noisy technical source，含真实 source scaffolding/references/secondary metadata，用于测试 source cleanup + reader relevance；
- H2：formula + table-rich Chinese technical material，必须真实验证 Markdown 与 PDF；
- H3：足够长的 Chinese scientific/technical document，需要 document-level restructuring。

三者来自不同 document families、public-safe、语义完整、未用于 050–054 tuning。冻结前只做 model-output-independent source/task preflight，并记录 source hash/range、completeness、task、must-preserve facts、renderer suitability。不得看 output 后换 source/range/task。

三个 holdout 必须全部通过：actual candidate consumption、ordinary user task、reader-clean Markdown、semantic/fidelity audit、actual PDF render、visual QA、formula/table readability、target Chinese、reader relevance、无 raw markup/workflow leakage、无 critical omission/invention/strengthening。任一 true failure => batch FAIL，停止 Gate E/F，不添加 H4/replacement。

### Gate E — exactly one final Terra review

仅 Gate D 完整 PASS 后执行。plaintext 只放自然文档标题 + complete Deep Research + H1/H2/H3 real final candidates；wrapper 全放 metadata。模型固定 `gpt-5.6-terra`，`store=false`，retry `0`，worst-case `<= USD 0.25`。

Terra 至少评价：自然中文、结构/过渡、reader relevance/source metadata、markup/math/table presentation、条件/限制/引用明显损坏、source-process/workflow framing、明显 omission/invention/strengthening。任何 blocking `REVISE` 都按普通 artifact failure 处理；不得第二次 paid review。

### Gate F — release engineering + production entry

只有 A–E 全 PASS 后：

1. source/generated Marketplace parity；
2. full local test suite；
3. fetch then-current main，检查 version/release policy 与竞争修改；
4. version closure：当前计划 `writing-style 0.2 -> 0.3` exactly once；repository 当前计划 `5.0.4 -> 5.0.5 PATCH`，若 latest main repository version 已无关前移则机械顺延 patch target；
5. 同步 plugin changelog、root changelog/release metadata、README release dashboard、generated manifest/version、plugin TODO closure；
6. required GitHub full/release CI 全 PASS；
7. official local-marketplace/cachebuster/reinstall/fresh-session candidate smoke；
8. bounded production `writing-style@yuukias-ai-skills` install/upgrade smoke：before snapshot、普通自然 prompt routing、actual new skill consumption、after restore，证明 production snapshot before==after（除正式 release identity preparation 外不得留下 live residue）。

### Gate G — Scheduled GPT independent review

Reviewer 必须直接检查 real production diff、final source/generated payload、known/stress artifacts、public fresh Markdown/PDF/images、Terra evidence、CI、production smoke、version/changelog closure；private Deep Research 只能按 repo privacy boundary 消费其完整 Terra evidence、render QA/non-secret evidence/locator，并把最终 private artifact判断留给 human gate，不能假装看过不可访问的 private plaintext/PDF。

Reviewer 必须分别给：

```text
PROCESS PASS | REVISE
PRODUCT / ARTIFACT PASS | REVISE
```

出现任一 raw markup、formula fence/unrendered math、operator corruption、clipped/illegible table、明显简繁不符、workflow/audit/source-process framing、source metadata 过保留、reader relevance 过删、critical semantic drift、long-form dump/audit-like 结构或 production natural prompt 未消费新能力，都不得 PRODUCT PASS。

### Gate H — final human artifact acceptance

只有 Gate A–G 全 PASS 后才生成并呈现：

- `private/exports/054_clear_writing_release_closure/Clear_Writing_0.3_Comprehensive_Acceptance_Dossier.pdf`
- `private/exports/054_clear_writing_release_closure/Clear_Writing_Deep_Research_Final.pdf`
- H1/H2/H3 final PDFs 或 dossier appendices。

Dossier 必须是人能直接判断的成稿：包含 0.2 真实失败、053 成果与未发布原因、054 relevance repair、代表性 before/after、Deep Research/fresh outputs、math/table/render QA、Terra/Reviewer conclusion、remaining limitations 与一页 acceptance checklist；不得 dump JSON/log/Gate 流水账。

只请求一次 `ACCEPT` 或 `REJECT`。`REJECT` 覆盖所有 prior PASS。

### Gate I — final integration

仅用户 `ACCEPT` 后：fetch latest main；检查真实 conflict；rerun integration-required checks；conflict-free integrate；non-force push；验证 remote main 与 released `writing-style` identity/version；记录 final integration evidence。若发生当前 policy 无法安全解决的 writing-style/shared-runtime 竞争修改，才进入 integration conflict gate。

## Natural-language usage / routing expectations

普通用户不需要知道 internal route。典型请求应自然触发正确行为，例如：

- “把这份长的中文技术资料重新组织成可以直接发给同事看的说明，公式、条件、引用和重要名字都保留，但网页上的杂项不要照搬。”
- “把这份科研报告重写成自然中文，表格和公式要能正常导出 PDF，不要把页面维护信息或重复链接写进正文。”
- “请保留正式英文算法名、数据集名和作者归因，但普通解释用中文，没必要的来源标签不要写。”

同样必须保持兼容：短中文润色仍走 light route；fidelity-only 不强制 heavy rewrite；英文 scientific prose 仍走 `scientific-prose`；用户明确要求“比较原文/解释作者如何表述/做编辑审阅”时，合法 source-oriented framing 仍允许。

## Out of scope

- 不把 054 扩成任意 Unicode / 任意语言 PDF font-coverage 项目；
- 不修或重算 053 Karatsuba H1 来宣称 fresh PASS；
- 不新增 H4、replacement fresh holdout 或 retry-until-PASS；
- 不新增第二次 Terra review；
- 不新增 private artifact/provider/credential location 或复制 credential；
- 不修改 Bridge Kit / Host Policy 解决 AI_Skills-specific semantics；
- 不研究 undocumented no-install hot-load；
- 不新建顶级 writing plugin、alternate heavy runtime、Reviewed Handoff schema/state/ledger；
- 不把 reader relevance 变成语言/字符/短语 blacklist；
- 不借 054 处理 writing-style TODO 中其他尚未被本 Goal promotion 的能力（例如 presentation microcopy、version-aware CAT-TRACE prose、academic-humanizer audit）；
- 不宣称 universal writing quality、任意语言/格式/领域 correctness。
