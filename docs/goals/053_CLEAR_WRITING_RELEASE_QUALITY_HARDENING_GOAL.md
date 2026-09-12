# 053 Clear Writing Release Quality Hardening — Canonical Goal

本文件是 `053_clear_writing_release_quality_hardening` 的顶层 completion contract。内部 objective、bootstrap、单个 commit、tests、handoff 或某个 Gate PASS 都只是子目标，不能覆盖本文件。

默认用中文汇报；代码、命令、字段和路径保留原文即可。

## 1. 产品目标

Clear Writing 0.2 已证明 heavy Chinese rewrite 的 routing、Meaning Map / Reader Plan / REALIZE_MEANING 主体和 source-process framing 修复可工作，但用户人工阅读真实 artifact 后发现：**0.2 还不能作为最终中文科研/技术成稿版本直接交付。**

053 不重做 051/052 架构；目标是保留 051 的成稿质量优点与 0.2 的结构/边界改进，把当前真实失败闭合为一次可发布的兼容升级。

成功后的正常用户体验应是：

- 长中文科研/技术材料可重组为自然、直接、面向读者的简体中文（除非用户明确要求繁体或保留原语言变体）；
- 公式以正常 Markdown/LaTeX 数学表达存在，可被现有 PDF renderer 正确排版，不用 fenced `text` code block 冒充公式；
- 表格保持可渲染结构；
- Wikipedia/HTML/template 等源格式标记不会泄漏到普通读者正文；
- 引用含义保留，但不把 `{{sfnp...}}`、`<ref>...</ref>`、`{{harvtxt...}}` 等平台语法原样交给读者；
- 数学符号、减号、上下标、变量、数字、引用、条件、限制和结论强度不因格式清理而损坏；
- 普通英文和内部项目/审计口吻明显减少，正式方法名、模型名、数据集名、指标、代码/路径等必要英文继续保留；
- 长文重组不新增无来源的更强解释，不漏掉关键命题和证据边界。

只有最终真实 artifact 达到这些要求，才允许发布。

## 2. 当前真实基线与证据

启动时必须 `git fetch origin`，以当时最新 `main` 为 repo source of truth。创建本文件时的参考 main 是 `2881bbf992f2dc50ccb68be1b34d155e5db31d7f`，但不得把该 SHA 当成未来固定基线。

当前正式 plugin identity：

- slug: `writing-style`
- displayName: `Clear Writing`
- version: `0.2`

051 保持历史 `STOPPED / NOT_RELEASED`，但其 Gate 4 Deep Research 长文是有价值的只读 style/render baseline；不得改写 051 历史。

052 保持已完成历史；其 PASS 只证明 frozen 052 rubric，不得用于反驳用户对真实 artifact 的新发现。

053 已有四类人工诊断证据：

1. 052 Acceptance Dossier：暴露 Bloom raw wiki/citation markup、HTML provenance comment、FFT 公式 code block 等漏验问题；
2. 当前正式 0.2 对完整 Deep Research 报告的新生成：长文更展开，但公式大量退化为 fenced text、普通英文和 `provenance/audit/当前 main/当前仓库` 等内部口吻增多；
3. 051 vs 0.2 同源比较：051 约 30,738 chars / 562 lines / 194 个数学标记 / 2 个 code fences；0.2 约 43,180 chars / 648 lines / 0 个数学标记 / 60 个 code fences；051 在公式、紧凑度、普通英文密度、内部审计词方面明显更接近可直接阅读稿；
4. 051 Gate 4 14 页 historical PDF：同一 Deep Research source 的历史成稿基线，数学和表格真实排版较好。

repo-local private diagnostic 预计位于：

`private/exports/clear-writing-0.2-deep-research-diagnostic/`

历史 051 private baseline 预计位于：

`private/exports/051_writing_style_rebuild/gate4-full-report/`

若 exact private locator 发生变化，允许在 repo 内定位同 SHA / 同 artifact；不得伪造、重新生成 051 historical output 或把 private plaintext commit/push。

## 3. Five-Pass preflight 结论

### Product

本次真正目标是 final reader artifact，而不是再获得一个 mechanical PASS。最终用户要消费的是 Markdown/PDF 长文，因此 tests、receipt、route evidence、Terra PASS 都不能替代实际可读成稿。

### Reality

当前 `scientific-rewrite` 已明确把 `rewrite_support.py` 定义为 mechanical validator，并把自然中文实现交给 `chinese-prose/REALIZE_MEANING`；这一职责划分继续保留。当前 helper 的 exact-item extraction 主要识别 `$...$` / `$$...$$` / `\(...\)` / `\[...\]` 等数学定界形式，对 raw wiki/template 中的公式/运算符保护不足，是 `k − 1 -> k 1` 一类错误需要重点核查的现实线索，但 Planner 必须先读实现再决定最小修复位置。

### Alternatives

至少比较并明确拒绝以下错误路线：

- **只修 PDF renderer**：不能接受。坏的 Markdown/候选稿不能靠 PDF 渲染器藏起来；公式、markup、语言质量必须先在 candidate 层正确。
- **写一个大规模 source-markup postprocessor 自动改正文**：默认不采用。机械替换容易再次损坏 `k − 1`、上下标、引用和公式语义。
- **重写 heavy architecture / 新建另一个 writing plugin**：不采用。051/052 已证明主体路线有效。

优先路线是：在现有 `scientific-rewrite + chinese-prose + writing-fidelity + rewrite_support` 层内，增强 semantic/output contract 与必要的机械 validator；helper 负责拒绝明显坏 artifact，不负责生成自然语言。

### Red Team

053 必须主动防止以下“看起来 PASS、实际没解决”：

- raw Markdown/LaTeX/wikitext 只在 PDF 中被隐藏，源 candidate 仍脏；
- 只检查 `原文指出`，却放过 wiki/HTML markup、公式 code block、繁简混杂、普通英文堆叠；
- exact-item PASS 只保护数字，却丢减号、指数、上下标、变量关系；
- Deep Research 只比较开头几页，后半篇公式/表格/引用继续退化；
- 长文更“完整”但偷偷新增 source 不支持的解释；
- fresh holdout 失败后静默换样本；
- Reviewer 只读 receipt/RESULT，不读实际 candidate/render；
- predecessor candidate 的长文证据冒充 final candidate 证据。

### Execution readiness

前述问题已由真实 0.2 artifact 与 051 同源 baseline 直接观察，修复方向不要求重做产品架构；因此 053 **READY FOR EXECUTION**，但 Executor 必须先由 Planner 冻结 bounded Plan。

## 4. Exact task identity 与用户交互目标

exact task key：

`053_clear_writing_release_quality_hardening`

exact branch：

`reviewed/053_clear_writing_release_quality_hardening`

exact task-owned worktree：

`/tmp/ai-skills-053-clear-writing-release-quality`

本 Goal 的 workflow 目标是：**正常情况下除最终 artifact `ACCEPT / REJECT` 外，不再向用户弹 branch、worktree、candidate cache、是否发送到同一 OpenAI/Codex 路径、是否跑 CI、是否做 production smoke、是否 push/merge 等 routine prompt。**

现有 `AGENTS.md` 已有 exact-branch bootstrap、same-scope authorization dedup、canonical candidate replay、task-bound watcher、unsent-call recovery、live-smoke upfront authorization 等规则。053 不重复堆同义 AGENTS 规则；若仍出现同 scope 的 routine prompt，按 workflow regression 处理，而不是修改 Clear Writing 产品语义。

## 5. 本 Goal 的 upfront authorization envelope

用户发送引用本文件的 kickoff prompt 后，视为明确授权当前 053 范围内：

- 创建/使用上述 exact branch 与 exact worktree；
- exact branch 上普通 commit / fetch / non-force push / remote handoff；
- canonical candidate replay：repo-local pinned runtime、existing Codex account/CODEX_HOME、reserved temporary candidate identity/cache、install/remove/finally cleanup；
- 读取并使用 repo-local `private/exports/` 中上述同一 Deep Research source / 051 historical / 0.2 diagnostic artifact，仅用于 053 known-regression、candidate generation、render 和 review；private plaintext 不 commit/push；
- 同一 Deep Research private source 最多 **2 次** 053 candidate replay/generation，经现有 Codex/OpenAI 路径完成；不得换 provider、复制 credential 到新环境或扩大 private artifact 范围；
- exactly **2 个 public-safe fresh holdouts**；
- exactly **1 次最终 `gpt-5.6-terra` Text Review**，沿现有 OpenAI/GitHub Actions review path，`store=false`，automatic paid retry `0`，per-call worst-case `<= USD 0.25`；允许该最终 candidate-only review 包含同一份 053 Deep Research candidate，但不得扩大到其他 private artifact；
- required zero-paid CI / deterministic render QA；
- bounded live `writing-style@yuukias-ai-skills` production install/upgrade smoke，开始前记录 live state，结束后恢复原 marketplace/plugin state；
- 用户最终 `ACCEPT` 后，conflict-free latest-main integration + non-force push。

禁止：force/destructive Git、global Codex upgrade、Host Policy/Bridge Kit/execpolicy 改动、复制 `auth.json`、新 provider/账户、无限 retry、额外 paid review、额外 private artifact。

若 scope 不变，不得重复询问上述授权。只有真正扩大 private data、provider/credential、paid-call count/cost、live-global target 或 destructive risk 才允许再次询问。

## 6. Gate 0 — Planner freeze / evidence freeze

Scheduled GPT Planner 必须先读取：

- current `main/AGENTS.md`；
- `TODO.md`、`docs/workflows/CONTINUOUS_REAL_WORLD_SKILL_REFINEMENT.md`、`docs/plugin-todos/writing-style.md`；
- current `scientific-rewrite` / `chinese-prose` / `writing-fidelity` source 与 focused tests；
- 051 Gate 4 historical evidence；
- 052 PLAN / RESULT / FINAL_REPORT / REVIEW_1 / Text Review / known+fresh regressions；
- repo-private 0.2 Deep Research diagnostic 与 051-vs-0.2 comparison。

Planner 将用户人工发现写回现有 `writing-style` TODO（若尚无等价条目），并冻结一个 bounded 053 Plan；不要重写 051/052 历史，不要扩大成 generic writing redesign。

Plan 必须明确每个 observed failure 的 owner layer、known-regression、fresh holdout 和最终 artifact acceptance。

## 7. Gate 1 — Focused implementation/mechanical regression

先用 exact observed failures 写回归，再实现最小修复。

至少覆盖：

- Bloom raw wikitext/template/HTML：普通 reader candidate 不得出现 `{{...}}`、`<ref>...</ref>`、`{{harvtxt...}}`、HTML provenance comment 等源平台语法（明确代码/markup 示例任务除外）；
- `k − 1` / `k-1` / 上下标 / 指数 / 变量关系不能在 normalization 中丢失运算符；
- FFT/科学公式不得默认进入 fenced `text` code block；公式应输出为正常 Markdown/LaTeX math；
- Markdown table 语义保持可渲染；
- 简体用户请求且未要求繁体时，普通正文保持简体；明确要求繁体时才输出繁体；
- 普通英文关系词、`provenance/audit/当前 main/当前仓库` 等内部策划/审计口吻不得支配导师/读者正文；正式专名、算法、指标、路径、代码和引用身份继续保留；
- source-process framing 与 workflow leakage 的 052 regression 继续 PASS；
- long rewrite 的 proposition/evidence coverage 与 exact-item preservation 继续 PASS。

实现优先落在现有层；禁止新建顶级 skill/plugin/schema/state/ledger。若 helper 新增 validator，只能拒绝坏 artifact，不得机械改写正文。

## 8. Gate 2 — Known product regressions

在 fresh holdout evaluation 前，candidate 可以针对以下已知失败做 bounded repair/replay：

### K1 Bloom raw-wikitext

必须同时满足：

- no raw wiki/HTML/template leakage；
- citation meaning retained in readable form；
- `k − 1` 等运算符与变量关系无损；
- output language variant 符合简体请求；
- source-process framing 不复发。

### K2 FFT math

必须同时满足：

- DFT 公式是实际数学表达，不是 fenced `text`；
- `O(N^2)`、`O(N log N)`、`(N/2)\log_2 N` 等关键关系准确；
- complexity caveat、Cooley–Tukey 条件与 attribution 保留；
- PDF render 中公式可读、无 raw LaTeX/code-fence 泄漏。

### K3 完整 Deep Research 长文

这是 053 headline known regression，不能用 predecessor evidence 替代。

最终 candidate 必须对同一完整 source 直接运行，并同时与：

- 051 Gate 4 historical output；
- current 0.2 diagnostic output

比较。

051 作为 style/render floor，不要求复制其结构或压缩率；0.2 的结构展开优点可以保留。但最终候选至少应做到：

- 数学公式/关系不比 051 更差；
- 表格真实可读；
- 普通英文和内部审计/仓库口吻明显低于 0.2；
- 读者开头直接说明研究判断，不写成执行计划/内部策划记录；
- 数字、文献、方法比较、实验限制、GO/STOP 边界和不确定性不漂移；
- proposition-level audit 无 critical omission/invention/strengthening；
- 生成完整 PDF，实际阅读中无明显乱码、截断、raw Markdown/LaTeX、公式 code block。

最多使用本 Goal 预授权的 2 次 private Deep Research candidate replay；超过即 STOP 053，不得再问 routine retry 授权。

### K4 052 compatibility

必须继续通过：

- Python `re`；
- light Chinese polish；
- fidelity-only；
- English scientific prose；
- source-process framing；
- review-packet wrapper isolation。

Known regression 全部 PASS 后 production candidate 冻结；冻结后不得再根据 fresh holdout 调 production。

## 9. Gate 3 — Fresh generalization batch

在 implementation 完成、known regressions PASS 后才进入 fresh evaluation。Planner 在 candidate generation 前预先冻结 **exactly 2** 个 public-safe sources；来源不同、未用于 050–053 tuning。

要求：

### H1 Math/markup-rich technical source

应同时含真实公式/符号、引用或 structured markup，能暴露公式表示、operator preservation、citation normalization 和 target-language 问题。

### H2 Long-form Chinese technical/scientific source

应是完整 reader-facing 长文，而不是 task result、CI、FINAL_REPORT、plugin source 或 synthetic toy；长度和结构足以检验段落重组、表格/公式、普通英文密度、内部口吻和长文保真。

两份 source 都必须通过 semantic-completeness preflight，不得半句、半列表、缺承诺公式/定义或截断 section。

fresh batch 一旦开始，任何一个真实 FAIL 都使 053 fresh gate FAIL；不得静默替换第三个 holdout，不得针对失败输出改 production 后仍称 unseen。

每个 fresh candidate 都要保存原始 Markdown + 正常 render PDF，并做 source/candidate proposition + exact-item audit。

## 10. Gate 4 — Reader-visible render QA

053 的 acceptance 评价对象是实际读者看到的 Markdown/PDF，不是 receipt。

对 Bloom、FFT、Deep Research、2 个 fresh holdouts 至少检查：

- raw wiki/HTML/template syntax；
- raw Markdown table syntax 是否被当正文显示；
- unrendered LaTeX；
- fenced-code formula；
- 公式/表格 clipping、乱码、missing glyph；
- requested simplified/traditional variant；
- 数学运算符/上下标/指数丢失；
- reader-visible provenance/workflow leakage；
- 第一屏/章节是否仍像内部计划或审计记录；
- 普通英文是否不必要地占据中文句子骨架。

必须复用成熟的 `render-chinese-math-pdf` 路线；不得另造低质量 PDF renderer。render QA 不得通过“文件存在”替代真实页面检查。

## 11. Gate 5 — Final independent review

只有 Gate 1–4 全部 PASS、candidate frozen 后，才允许 exactly 1 次 Terra Text Review。

final review packet 使用自然文档标题，只包含 candidate 文本，不含 Gate/task/recovery wrapper。rubric 必须覆盖：

- natural Chinese / target language variant；
- formula/table representation；
- raw source markup/provenance leakage；
- obvious operator/symbol loss；
- internal audit/planning language；
- key fact/condition/limitation/attribution drift；
- Deep Research 长文是否像可以交给导师/读者的报告，而不是内部运行记录。

Terra PASS 只证明这份 frozen rubric，不自动等于最终发布；仍需 GPT Reviewer 和用户 artifact acceptance。

## 12. Gate 6 — Release closure / production entrypoint

Terra PASS 后：

1. focused + full tests；
2. Marketplace generator source/generated parity；
3. required release CI；
4. version/changelog closure；
5. bounded live production install/upgrade smoke；
6. ordinary natural heavy-route smoke；
7. restore live marketplace/plugin state and verify restoration。

当前参考版本是 repository `5.0.4` / Clear Writing `0.2`。如果届时 latest main 仍满足现行 version policy，compatible user-visible improvement 预期为 Clear Writing `0.3`，repository patch release；但 Executor 必须读取当时最新 version policy，不能硬编码具体 repository version。

## 13. Gate 7 — Scheduled GPT Reviewer

创建/启用 task-bound Planner/Reviewer automation，exact 绑定 053 task + branch，不使用 generic watcher 代替。

Reviewer 必须独立读取：

- real production diff；
- focused/full/CI evidence；
- known regression candidate；
- fresh holdout Markdown + rendered PDF evidence；
- Terra evidence；
- production smoke；
- version/changelog；
- public artifact quality。

Reviewer 不得把 mechanical PASS 当成 artifact PASS。private Deep Research 的完整人工质量由 final Terra candidate review + 用户最终 PDF 验收共同兜底；若 Reviewer 无法访问 private plaintext，不得假装已经直接阅读。

## 14. Gate 8 — Final human acceptance dossier

这是正常情况下唯一计划内用户暂停。

必须在 repo 内生成：

`private/exports/053_clear_writing_release_quality_hardening/`

至少包含：

- `Clear_Writing_0.3_Comprehensive_Acceptance_Dossier.pdf`
- `Clear_Writing_Deep_Research_Final.pdf`
- 对应 Markdown/source identity/evidence index（private plaintext 不 commit）

Dossier 必须真正给人看，而不是 JSON/Markdown dump。至少包含：

- 0.2 已知失败摘录；
- Bloom：source -> 0.2 -> final；
- FFT：source -> 0.2 -> final；
- Deep Research：051 historical -> 0.2 -> final，代表章节并附完整 final PDF；
- 2 个 fresh holdout；
- unrelated regression 摘要；
- Terra / GPT Reviewer / production smoke；
- remaining limitations；
- 用户 checklist。

PDF 中 Markdown table 必须是真表格，数学必须是真公式，不能再次把 source syntax 当读者正文。

用户只需回复 `ACCEPT` 或 `REJECT`。

## 15. Integration 与 completion

只有用户 `ACCEPT` 后，才 fetch latest main、做 integration preflight、保留并发 main work、集成 053、push main，并验证 released Clear Writing identity 与 ordinary routing。

只有以下全部 TRUE 才允许 `GOAL ACHIEVED`：

```text
focused_mechanical_regressions=PASS
bloom_known_regression=PASS
fft_known_regression=PASS
deep_research_full_report=PASS
python_re_compatibility=PASS
unrelated_regressions=PASS
fresh_holdout_1=PASS
fresh_holdout_2=PASS
rendered_artifact_qa=PASS
terra_review=PASS
full_release_ci=PASS
production_install_upgrade_smoke=PASS
ordinary_production_routing=PASS
gpt_reviewer=PASS
human_acceptance=ACCEPT
integrated_latest_main=YES
remote_main_verified=YES
released_clear_writing_identity_verified=YES
```

任何一项 pending/false 都不得 achieved。

若 execution environment 因 context/time/tool limit 强制结束当前 run，而整体 Goal 未完成：报告 `PARTIAL_PROGRESS`，结束前 commit、push exact branch、verify remote、写真实 CURRENT.next_action 和 remaining gates。不得把子 objective 完成冒充 overall Goal 完成。

## 16. 最终报告

最终至少输出：

```text
overall_goal_status=
053_current_state=
implementation_commit=
clear_writing_version=
repository_version=
bloom_known_regression=
fft_known_regression=
deep_research_full_report=
python_re_compatibility=
unrelated_regressions=
fresh_holdout_1=
fresh_holdout_2=
rendered_artifact_qa=
terra_review=
full_release_ci=
production_smoke=
gpt_reviewer=
human_acceptance=
integrated_main_sha=
remote_main_verified=
released_clear_writing_identity_verified=
```
