# 055 Clear Writing Release Convergence — Canonical Goal

- Execution package version: `v0.1`
- Exact task: `055_clear_writing_release_convergence`
- Exact branch: `reviewed/055_clear_writing_release_convergence`
- Exact worktree: `/tmp/ai-skills-055-clear-writing-release-convergence`
- Target: `writing-style` / Clear Writing
- Approved architecture authority: `docs/design/clear-writing/NEXT_RELEASE_PROPOSAL.md` v0.1
- Design Critic review: `docs/design/clear-writing/NEXT_RELEASE_CRITIC_REVIEW.md` round 1 `PASS`
- Execution Plan: `docs/design/clear-writing/NEXT_RELEASE_EXECUTION_PLAN.md` v0.1
- Kickoff Draft: `docs/operations/prompts/055_CLEAR_WRITING_RELEASE_CONVERGENCE_KICKOFF.md` v0.1
- State before execution-ready Critic PASS: `DO_NOT_EXECUTE`

本文件是 055 的顶层 completion contract。测试、单个 Gate、一次 Reviewer/Terra PASS、branch push、CI 或 production smoke 都不能覆盖本 Goal。只有 execution package v0.1 获独立 Critic execution-ready PASS，且用户实际发送获批 kickoff 后，才允许启动本任务。

## 1. 最终产品目标

普通用户从正式 Clear Writing 安装入口，用自然语言要求把已有中文或中文主导科研/技术材料“在不改变内容的前提下重新组织得清楚、自然、可直接给读者看”时，最终版本必须稳定做到：

- 保留 source 中任务相关的事实、数字、公式、表格、引用、比较关系、条件、限制、不确定性、归因和必要复现信息；
- 可以重排、合并、拆分、解释和移位，但不能靠逐段照抄 source framing；
- 合法代码、路径、配置、命令按读者/复现角色处理，不按外观一刀切；
- source future work/limitation 保持原主体、时态、语气和未完成状态，不写成 Executor 当前行动清单，也不能改成已完成结果；
- 网页/Wiki/RST/导出 wrapper、内部 task/review/audit trace 与无关来源包装不进入读者正文；
- 简繁体服从用户目标；正式专名、API、方法、数据集、代码 identifier 可保留必要英文，普通论述不退化成英文关键词脚手架；
- 完整长文在实际 Markdown/PDF/render 中是一篇连贯成稿，而不是局部正确段落的拼接。

Clear Writing 仍是 source-faithful rewrite 产品，不自动承担外部事实核查、文献研究或 Research Authoring。

## 2. 历史基线必须按事实使用

- 050：证明 source-conditioned memo/style、过度 source wording 与机械 PASS 不能替代成稿质量。
- 051：建立 meaning-first 主链，但 final review 仍发现 internal workflow terminology 与 source-process framing。
- 052：已经完成其 bounded reader-facing closure，包括 release CI、production smoke、用户 ACCEPT 与 main integration；本任务必须把它作为正向兼容基线，而不能写成“052 未完成 release”。它不证明跨任务长期成熟度。
- 053：known regression 对 raw markup、公式、表格、完整 Deep Research 等有价值；其 fresh H1 正式失败是 PDF Cyrillic glyph 缺失的真实 render failure，必须作为 render regression，不得改写成 reader-relevance failure。
- 054：F1/F2 是本轮 reader-facing product repair 的主要证据；F3 合法 Python code 的 blanket blocker 属 reviewer rubric overreach；F4 source 自带历史事实问题默认属于外部事实维度，不是自动 rewrite defect。

不得重写 050–054 历史、不得把已曝光样本重新称 fresh。

## 3. 实现合同

保留并强化现有主链：

`ordinary Clear Writing entry -> Meaning Map -> Reader Plan -> REALIZE_MEANING -> assembly / whole-document finish -> fidelity/audit -> bounded repair -> rendered final candidate`

必须实现以下机制，不得另起架构：

1. **Reader Plan reader disposition**：每个需要保留/删/移/结构化的 obligation 都必须有读者角色和理由。优先扩展/映射现有 Meaning Map / Reader Plan 与 `inline-critical | relocatable-trace | internal-workflow-trace`；不得新增平行持久 ledger/schema/state。
2. **REALIZE_MEANING modality preservation**：保护完成状态、主体、时态、条件、认识状态、source-author proposal 与 assistant recommendation 的区别。
3. **assembly whole-document responsibility**：负责全文目的、章节顺序、定义位置、跨 bundle 重复/冲突、过渡、future work/limitations/repro details placement 和统一 reader-facing voice，而不是只拼接/去重。
4. **writing-fidelity 继续独立**：检查 source proposition/evidence/attribution 与 reader disposition 一致性，不承担 prose generation。
5. **机械 helper 只验证**：可以检查 literal、结构、公式、表格、路径类别、generated parity、render；不得用 regex/禁词/英文计数/code fence/path 外观生成或判定整体语言质量。
6. **选择性吸收 053/054**：从最新 main 出发，只移植 evidence 支持且符合 Proposal/Critic 的最小实现；禁止 whole-branch merge、样本特判或新 runtime。

中央 plugin refinement 必须显式遵守 `workflow-core + ai-skills-core + writing-style` 三层职责。

## 4. G1–G8 必须全部由最终候选满足

### G1 正常入口 / install / routing / compatibility

从 official candidate marketplace、install/upgrade、fresh session、普通自然 prompt 证明 exact candidate 真正被加载和消费。heavy rewrite、light Chinese、English scientific prose、fidelity-only、source comparison 等合法 route 必须保持。direct skill/helper 不能充当正式入口证据。

### G2 Source fidelity / attribution

对 source + candidate 检查 claim、evidence、否定、数量、比较、条件、caveat、不确定性、citation、attribution、结论强度及删/移/结构化决定。任何遗漏、无来源新增、strengthening、错误归因、条件/否定漂移均 FAIL。

### G3 公式 / 表格 / code / reproducibility

至少覆盖 FFT math/operator、table-rich technical case、合法 Python 示例、必要 path/config/command/API/identifier 与内部 trace 的 should-keep/should-drop 对照。结构化内容必须语义与 render 都正确；不得靠 fence/path count PASS。

### G4 Dirty source cleanup

Bloom/wikitext、noisy RST/HTML/wiki/export 类 source 中 wrapper、导航、模板、重复链接、无关 disclaimer/license debris 不得进入普通正文；清理不能破坏 G2/G3。

### G5 Reader-facing quality

必须直接修复 054 F1/F2 代表的问题：全文不能继续像项目备忘录/执行计划；source future work 不能变成当前 executor instruction；内部 audit/task/repo 路径不能挤进正文；真正复现信息不能因像路径而误删；中文自然、简繁体正确、必要英文有真实定位价值。禁词/English count/script count 只能诊断，不能判 PASS。

### G6 完整长文与真实 render

用完整 Deep Research + 至少一份独立已曝光长文 known regression 直接生成、阅读全文并实际 render。检查全文结构、过渡、重复、定义位置、technical detail placement 与 PDF 可读性。053 Cyrillic glyph failure 必须作为真实 render regression。最终付费 review 前必须已有 independent whole-artifact qualitative PASS。

### G7 Fresh generalization

final candidate 与 rubric 冻结后 exactly 3 个新的 public-safe holdout，分别以以下风险为主：

1. noisy technical + legitimate code/reproduction token；
2. formula/table structured technical content；
3. long-form + future-work/limitation/attribution/reader-relevance decision。

具体 source 在 candidate freeze 后才由独立 selection/freeze 步骤确定，先做 completeness preflight，再记录 source/provenance/hash/task。不得使用 050–054 已曝光样本；看 output 后不得换题、加第 4 个、补赢家或改 production 后继续称 unseen。

### G8 Same-final-candidate production certification

同一 final candidate 必须同时拥有：G1–G6 final regression证据、G7 complete fresh PASS、一次最终独立 Text Review 或合法 Critic adjudication、release CI、production install/upgrade smoke + restore、final GPT Reviewer PASS、用户 final artifact ACCEPT、最终 main integration。不同 commit/payload 的关键 PASS 不得拼接。

冻结时至少记录：`FINAL_CANDIDATE_COMMIT`、source/generated parity、generated plugin payload/hash、plugin version、rubric version、fresh manifest hash。final certification 后 production payload 不能变化。

## 5. Reviewer / Terra 冻结标准

### A — Source fidelity

硬 blocker。Reviewer 必须看到 source + candidate，判断是否遗漏、新增、改变条件/否定/数量/归因/引用/公式表格语义，以及 disposition 是否与 Reader Plan 一致。

### B — Reader-facing quality

硬 blocker。Reviewer 直接读 candidate/render，判断文章是否自包含、自然、连贯、没有内部过程泄漏，future work voice 正确，code/path/config 放置合理，真实 render 可读。

### C — External factual truth

本任务默认非 blocker，不授权自动 fact-check。若 candidate 相对 source 新增、强化或错误归因，则转为 A；否则只能记录 source-quality warning，不得偷偷改 source meaning。

正常代码不能仅因是 code 被 blocker；路径不能仅因像文件路径被删除；source future work/limitation 不能被抹掉或改成已完成结果。

所有 blocker 必须包含：A/B/C、对应 frozen Gate/requirement、candidate 精确位置；A 还要 source 位置；违反理由；初步归因；最小关闭条件。无法回指 frozen requirement 的 finding 只能 advisory。

最终 `gpt-5.6-terra` Text Review 主要独立验证 B；不得把 C 临场升级为 blocker。A 的 source-aware 独立验证必须由 pre-final Critic / final GPT Reviewer 对同一候选完成。

## 6. 强制执行顺序

### Phase 1 — Bootstrap

1. 读取最新 main 的 AGENTS、角色合同、Gate policy、paid policy、approved Proposal/Critic review、本 Goal/Plan/Kickoff、当前 Clear Writing source、版本政策与必要 050–054 evidence。
2. branch/worktree 必须是本 Goal 的 exact identity；若 main 未包含获批 package 或相关 policy/design 有实质变化，停止。
3. bootstrap Reviewed Handoff task control files时只引用本 Goal/Plan；不得重做 architecture research。

### Phase 2 — Implementation + known regression

在 final freeze 前允许针对已知回归反复开发。先写 should-keep/should-drop、modality、whole-document 相关测试，再修改现有 source；保持 generated payload parity。G1–G5 必须在开发候选上通过。

### Phase 3 — Representative whole artifact / G6

对完整 Deep Research 与另一份已曝光长文回归使用 actual candidate replay，生成真实 Markdown/PDF/render并阅读全文。任何明显成稿问题在这里返修，不得留到 fresh/Terra。

### Phase 4 — Pre-final independent Critic

Executor 必须在 repo 中保存并 commit/push 一个可供 Critic 直接审查的 packet，至少包含：

- candidate commit/diff；
- G1–G6 evidence summary 与真实 artifact/render locator；
- source + candidate 可达方式；
- A/B/C rubric 与 blocking contract；
- should-keep/should-drop 代表例；
- proposed fresh categories；
- paid-review packet 边界与剩余预算。

Executor 停止，等待独立 Critic 实际阅读代表性全文/render。Critic PASS 前不得 freeze fresh、不得调用 Terra。

### Phase 5 — Final candidate freeze

Pre-final Critic 若只要求 approved architecture 内的产品修复，可继续修并重跑所有受影响 G1–G6；若要求改变 architecture、范围、Gate、预算或 recovery，返回 Planner/Critic 新 review。

最终 freeze 前必须：

- reconcile latest main；
- plugin version/changelog closure；
- source/generated parity；
- exact candidate commit + payload hash；
- full known regression + representative artifact PASS；
- rubric frozen。

当前 main 为 repository `5.0.4`、writing-style `0.2`；若无 concurrent release，预期发布为 repo `5.0.5`、writing-style `0.3`。若执行期间版本已变化，严格按 `PLUGIN_VERSIONING_AND_CHANGELOGS.md` 机械确定下一合法版本；若 concurrent change 修改 writing-style production behavior，必须回 Planner/Critic，不能只改数字。

### Phase 6 — Fresh / G7

候选 freeze 后才冻结 exactly 3 个 fresh sources；source completeness preflight 在生成前完成。运行后不允许 production tuning。三个必须作为完整 batch 判定。

### Phase 7 — Failure attribution

任何 fresh finding 都先区分 `PLUGIN_DEFECT | SOURCE_DEFECT | REVIEWER_RUBRIC_DEFECT | ENVIRONMENT_DEFECT | WORKFLOW_DEFECT`。真实 product failure 立即停止 final certification。

### Phase 8 — Final independent review

只有 G7 complete PASS 才能执行一次最终 Terra Text Review。不得自动 repair/review loop。若 Terra finding 疑似 rubric 越权，保留原 review 并交独立 Critic adjudication；不得伪造新的模型 PASS。

### Phase 9 — Production/release closure

只有最终 review 无 unresolved hard blocker 后：

1. final zero-paid release CI；
2. bounded live production install/upgrade smoke；
3. finally restore 原 production marketplace/plugin state；
4. final GPT Reviewer/Reviewed Handoff review；
5. 形成用户 acceptance dossier；
6. 用户明确 `ACCEPT / REJECT`。

只有 `ACCEPT` 才允许 integration。

### Phase 10 — Integration

普通 non-force integration/push。若 main drift 与 Clear Writing/source/generated payload/candidate replay/review/release/versioning path 重叠，停止；无关 drift 只有在 final payload/hash 保持完全一致且必要 zero-paid CI 重跑后才可集成。

## 7. 当前 bounded authorization envelope

**只有用户实际发送 execution-ready Critic 批准后的 kickoff，才授权以下内容。本文存在本身不是授权。**

### Git / task

允许创建和使用 exact branch/worktree；ordinary commit/fetch/merge latest main/non-force push/remote handoff；最终所有 gate + review + 用户 ACCEPT 后允许 non-force main integration。

禁止 force push、历史改写、破坏性 reset/clean、删除其他 branch/worktree、绕过保护或用 destructive Git 解决冲突。

### Private artifacts

只读：

- `private/exports/054_clear_writing_release_closure/inputs/`
- `private/exports/054_clear_writing_release_closure/deep_research_attempt1/`

本任务可写：

- `private/exports/055_clear_writing_release_convergence/`
- task-local ignored `.local-runtime/` replay output

只用于本 Goal 的已知回归、完整长文、render、Critic review与最终验收。private plaintext/PDF/intermediate/JSONL/credentials 不得 commit/push。

### Candidate replay

允许 canonical repo-local pinned candidate replay，使用 existing Codex account/CODEX_HOME 和 temporary `@ai-skills-candidate` identity；不得复制 `auth.json`，不得 global Codex upgrade，不得覆盖 live production identity。

### CI

允许 focused/full zero-paid tests、render QA、source/generated parity、Marketplace/release CI。ordinary push 不得触发 paid review。

### Paid final review

用户发送 kickoff 后授权且只授权：

- OpenAI API；`gpt-5.6-terra`；final Text Review only；
- `POST /v1/responses/input_tokens` 做 preflight，`POST /v1/responses` 做最终 review；
- `store=false`，default service tier，low reasoning，`max_output_tokens<=4096`，paid tools none；
- exactly **1** paid model call maximum；automatic retry `0`；
- per-call worst-case `<= USD 0.25`；campaign reserved-cost hard ceiling `<= USD 0.25`；
- credential 仅 existing GitHub Actions `OPENAI_REVIEW_API_KEY`，不读取/回显/复制，不 fallback 到 visual-review secret；
- 可发送本任务 final Deep Research candidate text + public-safe fresh candidate text + audience/rubric；不得发送 private source、Meaning Map、Reader Plan、intermediate/self-audit、repo log、credential；
- 若完整 frozen packet 超预算，fail closed，不拆第二 call、不静默删关键材料。

### Bounded production smoke

最终阶段允许一次 bounded `writing-style@yuukias-ai-skills` install/upgrade smoke：先保存 live marketplace/plugin identity + enabled state，安装 exact final identity，fresh session 走普通用户 prompt，然后 finally 恢复原状态。不得修改其他 plugins/profiles，不得升级 global Codex，不得扩成持续部署。

## 8. Recovery

- final freeze 前的真实 product defect：可在已批准机制内修复，重跑受影响 G1–G6。
- pre-final Critic 要求架构/范围/Gate/费用/恢复机制变化：回 Planner + Critic，不由 Executor扩展。
- fresh product failure：当前 candidate FAIL；样本降级为 known regression；本 package 不授权第二 fresh batch、candidate repair 后重称 unseen 或自动 successor。
- fresh source defect：保留原证据并停止；不得看 output 后替换。
- reviewer/rubric defect：保留原 finding，由独立 Critic追加裁定；不得改写历史 review。
- environment/infrastructure defect：只有 candidate/source/rubric 未变且有现有合法恢复路径时可恢复。
- Terra real product defect：candidate FAIL；不自动第二 Terra，不重置 call/budget，不自动创建 056。
- verified pre-request paid failure：若 `/v1/responses` 未发送、未产生 response、未消费 authorized call，可按现行 paid policy在同一授权内恢复；否则视为已消费。
- production restore failure：安全 blocker，停止 integration。
- main release-critical drift：停止并回 Planner/Critic。

## 9. Non-goals

本任务明确不做：

- Bridge Kit / Host Policy / execpolicy 修改；
- 新 top-level plugin/runtime/daemon/queue/state/schema/ledger；
- Research Authoring 重构或合并；
- 默认联网事实核查；
- maturity status 提升；
- 大规模语料/外部依赖接入；
- 以禁词、regex、字符统计、sample-specific rule 代替语义处理；
- 将 050–054 exposed samples 重新包装成 fresh；
- 第二次付费 Terra 或自动 paid retry；
- 扩大 private data/provider/credential/live-global scope；
- force/destructive Git；
- 自动创建 successor。

## 10. 完成条件

只有以下全部成立，才能报告 `055` 完成：

1. approved architecture 已按本 Goal 实现，没有未审扩张；
2. G1–G8 在同一 final candidate 上全部满足；
3. pre-final Critic 已实际审代表性全文/render并 PASS；
4. exactly 3 fresh batch complete PASS，或所有非产品 finding 已按冻结恢复合同合法裁定且无 unresolved blocker；
5. final independent review 无 unresolved blocker；
6. release CI PASS；
7. bounded production smoke PASS 且原 live state成功恢复；
8. final GPT Reviewer PASS；
9. 用户明确 `ACCEPT` 最终 artifact；
10. final plugin payload/hash 未变化并完成 non-force main integration。

否则只能报告当前阶段、失败归因和下一合法动作，不得以局部 PASS 宣布 release 完成。
