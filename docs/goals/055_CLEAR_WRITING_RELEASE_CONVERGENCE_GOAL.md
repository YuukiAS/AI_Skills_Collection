# 055 Clear Writing Release Convergence — Canonical Goal

- Execution package version: `v0.2`
- Exact task: `055_clear_writing_release_convergence`
- Exact branch: `reviewed/055_clear_writing_release_convergence`
- Exact worktree: `/tmp/ai-skills-055-clear-writing-release-convergence`
- Target: `writing-style` / Clear Writing
- Approved architecture authority: `docs/design/clear-writing/NEXT_RELEASE_PROPOSAL.md` v0.1
- Design Critic review: `docs/design/clear-writing/NEXT_RELEASE_CRITIC_REVIEW.md` round 1 `PASS`
- Prior execution-ready review: `docs/design/clear-writing/NEXT_RELEASE_EXECUTION_CRITIC_REVIEW.md`, commit `92251dd6f7a94b942fd0cd181f7f0c5b01db43bc`, decision `REVISE`, blockers `C1,C2,C3,C4`
- Execution Plan: `docs/design/clear-writing/NEXT_RELEASE_EXECUTION_PLAN.md` v0.2
- Kickoff Draft: `docs/operations/prompts/055_CLEAR_WRITING_RELEASE_CONVERGENCE_KICKOFF.md` v0.2
- State before execution-ready Critic PASS: `DO_NOT_EXECUTE`

本文件是 055 的顶层 completion contract。它只把已经 PASS 的 Clear Writing 设计收口为执行合同，不重开 architecture、Gate taxonomy 或 A/B/C Reviewer 基本设计。只有 execution package v0.2 获独立 Critic execution-ready PASS，且用户实际发送获批 kickoff 后，才允许启动本任务。

## 1. 最终产品目标

普通用户从正式 Clear Writing 安装入口，用自然语言要求把已有中文或中文主导科研/技术材料“在不改变内容的前提下重新组织得清楚、自然、可直接给读者看”时，最终版本必须稳定做到：

- 保留 source 中任务相关的事实、数字、公式、表格、引用、比较关系、条件、限制、不确定性、归因和必要复现信息；
- 可以重排、合并、拆分、解释和移位，但不能退化为逐段照抄 source framing；
- 合法 code/path/config/command 按读者与复现角色处理，不按外观一刀切；
- source future work/limitation 保持原主体、时态、语气和未完成状态，不写成 Executor 当前行动清单，也不能改成已完成结果；
- 网页/Wiki/RST/export wrapper、内部 task/review/audit trace 与无关来源包装不进入正文；
- 简繁体服从用户目标；正式专名/API/方法/数据集/code identifier 可保留必要英文，普通论述不退化成英文关键词脚手架；
- 完整长文在真实 Markdown/PDF/render 中是一篇连贯成稿，而不是局部正确段落的拼接。

Clear Writing 仍是 source-faithful rewrite 产品，不自动承担外部事实核查、文献研究或 Research Authoring。

## 2. 历史基线

- 050：证明 source-conditioned memo/style、过度 source wording 与机械 PASS 不能替代成稿质量。
- 051：建立 meaning-first 主链，但 final review 仍发现 internal workflow terminology 与 source-process framing。
- 052：已经完成其 bounded reader-facing closure，包括 release CI、production smoke、用户 ACCEPT 与 main integration；本任务把它作为正向兼容基线，但不把该 bounded closure说成长期 maturity。
- 053：raw markup、公式、表格、完整 Deep Research 等 known regression 有价值；fresh H1 的正式失败是 PDF Cyrillic glyph 缺失的真实 render failure，必须保留为 render regression。
- 054：F1/F2 是本轮 reader-facing product repair 的主要直接证据；F3 合法 Python code 的 blanket blocker 属 reviewer rubric overreach；F4 source 自带历史事实问题默认属于外部事实维度。

不得重写 050–054 历史、不得把已曝光样本重新称 fresh。

## 3. 实现合同

保留并强化已批准主链：

`ordinary Clear Writing entry -> Meaning Map -> Reader Plan -> REALIZE_MEANING -> assembly / whole-document finish -> fidelity/audit -> bounded repair -> rendered final candidate`

必须实现以下机制，不得另起架构：

1. **Reader Plan reader disposition**：每个需要保留/删/移/结构化的 obligation 都有读者角色和理由；优先扩展/映射现有 Meaning Map / Reader Plan 与 `inline-critical | relocatable-trace | internal-workflow-trace`，不得新增平行持久 ledger/schema/state。
2. **REALIZE_MEANING modality preservation**：保护完成状态、主体、时态、条件、认识状态、source-author proposal 与 assistant recommendation 的区别。
3. **assembly whole-document responsibility**：负责全文目的、章节顺序、定义位置、跨 bundle 重复/冲突、过渡、future work/limitations/repro details placement 与统一 reader-facing voice，而不是只拼接/去重。
4. **writing-fidelity 继续独立**：检查 source proposition/evidence/attribution 与 reader disposition，不承担 prose generation。
5. **机械 helper 只验证**：可检查 literal、结构、公式、表格、路径类别、generated parity、render；不得用 regex/禁词/英文计数/code fence/path 外观生成或判定整体语言质量。
6. **选择性吸收 053/054**：只移植 evidence 支持且符合 Proposal/Critic 的最小实现；禁止 whole-branch merge、sample-specific patch或新 runtime。

中央 plugin refinement 必须显式遵守 `workflow-core + ai-skills-core + writing-style`。

## 4. G1–G8 acceptance

### G1 — 正常入口 / install / routing / compatibility

从 canonical candidate marketplace、install/upgrade、fresh session、普通自然 prompt 证明 exact candidate 真正被加载和消费。heavy rewrite、light Chinese、English scientific prose、fidelity-only、source comparison 等合法 route 必须保持。direct skill/helper 不能充当正式入口证据。

### G2 — Source fidelity / attribution

对 source + candidate 检查 claim、evidence、否定、数量、比较、条件、caveat、不确定性、citation、attribution、结论强度及删/移/结构化决定。遗漏、无来源新增、strengthening、错误归因、条件/否定漂移均 FAIL。

### G3 — 公式 / 表格 / code / reproducibility

至少覆盖 FFT math/operator、table-rich technical case、合法 Python 示例、必要 path/config/command/API/identifier 与 internal trace 的 should-keep/should-drop 对照。结构化内容必须语义与实际 render 都正确；不得靠 fence/path count PASS。

### G4 — Dirty source cleanup

Bloom/wikitext、noisy RST/HTML/wiki/export 类 source 中 wrapper、导航、模板、重复链接、无关 disclaimer/license debris 不得进入普通正文；清理不能破坏 G2/G3。

### G5 — Reader-facing quality

必须直接修复 054 F1/F2 代表的问题：全文不能继续像项目备忘录/执行计划；source future work 不能变成当前 executor instruction；internal audit/task/repo path 不得挤进正文；真正复现信息不能因像路径而误删；中文自然、简繁体正确、必要英文有真实定位价值。禁词/English count/script count 只能诊断，不能判 PASS。

### G6 — 完整长文与真实 render

用完整 Deep Research + 至少一份独立已曝光长文 known regression 直接生成、阅读全文并实际 render。检查全文目的、章节顺序、定义位置、过渡、重复/冲突、technical detail placement、future work/limitations/reproducibility placement 与 PDF 可读性。053 Cyrillic glyph failure 必须作为真实 render regression。

进入 fresh 前，G6 release-critical evidence 必须来自最后一次 pre-final Critic 实际审过的 exact candidate。

### G7 — Fresh generalization

最后一次 pre-final Critic PASS 后，冻结 exactly 3 个新的 public-safe holdout，分别以以下风险为主：

1. noisy technical + legitimate code/reproduction token；
2. formula/table structured technical content；
3. long-form + future-work/limitation/attribution/reader-relevance decision。

不得使用 050–054 已曝光样本。任何 candidate output 生成前，必须完成 source completeness preflight，并为每项冻结 source/provenance/hash、自然用户任务、`PRIMARY_RISK`、`APPLICABLE_GATES`、`RENDER_REQUIRED`。

每项 fresh artifact 必须：

- 从同一个 `FINAL_CANDIDATE_COMMIT` 的 normal plugin entry 生成；
- 有 source-aware A/G2 evidence；
- 对完整 candidate 做真实 B/G5 定性阅读，而不是只靠 mechanical audit、generator self-audit、关键词或 receipt；
- 涉及 formula/table/code/repro/path/config/API 时按 G3 检查；
- dirty/noisy source 按 G4 检查；
- long-form 与所有 `RENDER_REQUIRED=YES` item 生成并实际查看真实 render，按 G6 检查全文结构/可读性；
- deterministic audit/receipt/hash 只能辅助，不得独立判 capability PASS。

完整 G7 batch 只有 `3/3` 都满足预先冻结的适用 G2–G6 criteria 才 PASS。candidate 在 batch 中不得修改。任一 true product failure 都使该 final candidate 的 G7 certification FAIL，该 item 永久转 known regression；不得替换、加第 4 个、改 candidate 后继续称 unseen。最终 Terra 是额外 independent final certification，不是 fresh artifact 第一层 qualitative grader。

### G8 — Same-final-candidate production certification

同一 final candidate 必须同时拥有：

- `FINAL_CANDIDATE_COMMIT` + generated plugin payload hash；
- G1–G6 final regression/representative artifact evidence；
- 最后一次 pre-final Critic 对该 exact candidate 的 source/candidate/render实际 review `PASS`；
- G7 `3/3 PASS`；
- exactly 1 次最终独立 Terra Text Review或合法 Critic adjudication；
- final zero-paid release CI；
- bounded production install/upgrade smoke + restore；
- final GPT Reviewer/Reviewed Handoff review；
- 用户 final artifact `ACCEPT`；
- 最终 main integration 后 plugin payload/hash不变化。

不同 commit/payload 的关键 PASS 不得拼接。

## 5. Final candidate identity 不得漂移

这是 055 的硬合同：

1. latest-main reconcile、plugin/repository version候选、plugin/root changelog、Marketplace/generated payload、source/generated parity、frozen rubric，都必须在最后一次 pre-final Critic review之前完成并进入 exact candidate `C_n`。
2. G1–G6 release-critical evidence、代表性 Deep Research candidate/render都必须显式从 `C_n` 生成。
3. Critic 必须实际审 `C_n` 的 source/candidate/render并明确 PASS；只有这时 `C_n` 才成为 `FINAL_CANDIDATE_COMMIT`。
4. 如果 Critic finding 导致 production source、generated payload、version identity、rubric或代表性 artifact发生任何改变，旧审查/PASS立即失效；形成新 candidate并重新生成代表性 artifact/render，再交 Critic，直到 exact candidate PASS。
5. Critic PASS 后只允许 control/evidence-only写入；后续 fresh/Terra/CI/smoke均 pin `FINAL_CANDIDATE_COMMIT`。不得再 merge latest main 后拿新的 production HEAD进入 fresh。
6. 任一 post-PASS 修改如果触及 production source、generated payload、version/release identity、rubric或已审代表性 artifact，禁止继续 certification，必须回到 pre-final closure + Critic。

这不新增第三套 freeze system、ledger或state machine；只用现有 commit/hash/evidence明确候选身份。

## 6. Reviewer / Terra 冻结标准

### A — Source fidelity

硬 blocker。Reviewer 必须看到 source + candidate，判断是否遗漏、新增、改变条件/否定/数量/归因/引用/公式表格语义，以及 disposition 是否与 Reader Plan 一致。

### B — Reader-facing quality

硬 blocker。Reviewer 直接读 candidate/render，判断文章是否自包含、自然、连贯、没有内部过程泄漏，future work voice正确，code/path/config放置合理，真实 render可读。

### C — External factual truth

本任务默认非 blocker，不授权自动 fact-check。若 candidate相对 source新增、强化或错误归因，则转为 A；否则只能记录 source-quality warning，不得偷偷改 source meaning。

正常 code不能仅因是 code被 blocker；path不能仅因像文件路径被删除；source future work/limitation不能被抹掉或改成已完成结果。

所有 blocker 必须包含：A/B/C、对应 frozen Gate/requirement、candidate精确位置；A还要 source位置；违反理由；初步归因；最小关闭条件。无法回指 frozen requirement 的 finding只能 advisory。

最终 `gpt-5.6-terra` Text Review主要独立验证 B；不得把 C临场升级为 blocker。A 的 release-critical source-aware独立验证必须由最后一次 pre-final Critic / final GPT Reviewer对同一 `FINAL_CANDIDATE_COMMIT`完成。

## 7. 强制执行顺序

### Phase 1 — Bootstrap

读取最新 main 的 AGENTS、角色合同、Gate policy、paid policy、approved Proposal/Critic review、本 Goal/Plan/Kickoff、当前 Clear Writing source、版本政策与必要 050–054 evidence。创建 exact branch/worktree/task control；不得重做 architecture research。

### Phase 2 — Implementation + known regression

在已批准机制内针对 known regressions迭代，完成开发阶段 G1–G5。允许修复，但不得扩大 architecture。

### Phase 3 — Pre-final release payload closure

在请求 Critic前完成：

- reconcile 当时 latest main；
- 按 canonical version policy完成 plugin/repository version候选与 changelog closure；
- 生成正式 Marketplace/plugin payload；
- source/generated parity PASS；
- freeze A/B/C rubric；
- commit exact candidate `C_n`并记录 payload hash。

若 concurrent main触及 writing-style production behavior/relevant policy，停止回 Planner/Critic。

### Phase 4 — Representative G1–G6 on exact `C_n`

canonical candidate replay显式 pin `C_n`；重跑 G1–G6；生成完整 Deep Research和另一份已曝光长文回归的完整 Markdown/PDF/render并真实阅读全文。若任何修复改变 production/payload/rubric，生成新 candidate并重新从 Phase 3开始。

### Phase 5 — Pre-final independent Critic handoff

Executor准备公开 evidence packet，并在以下 repo-local路径生成 private bundle：

`private/exports/055_clear_writing_release_convergence/pre_final_critic_bundle/`

固定内容：

- `01_SOURCE_FULL.txt`：代表性 Deep Research replay使用的完整 source文本；若 canonical replay input不是纯文本，同时把 exact original input放入 `source_original/`；
- `02_CANDIDATE.md`：`C_n`生成的完整 Deep Research candidate；
- `03_RENDER.pdf`：该 candidate的实际 render；
- `04_BUNDLE_MANIFEST.md`：candidate SHA、payload hash、source/candidate/render hash、rubric version、公开 G1–G6 evidence locators，以及用户需要上传给 Critic的 exact file list。

private plaintext/PDF不得 commit/push。Executor push公开 packet后停止，向用户返回 exact paths。**由用户本人把 manifest指定的 source/candidate/render上传到已有长期 Critic thread。** Executor不主动上传，不引入新 provider/transport。

Critic必须实际读取 source + candidate + render才能对 `C_n`给 pre-final PASS。只凭路径/摘要/receipt不能 PASS。

若 Critic要求产品或payload/artifact/rubric修改，形成新 candidate并重新 Phase 3–5；若要求改变 architecture/scope/Gate/预算/授权/recovery，则回 Planner/Critic amendment。

### Phase 6 — Final candidate designation

只有 Critic对 exact `C_n`明确 PASS后，`C_n`才成为 `FINAL_CANDIDATE_COMMIT`。冻结并记录 payload hash、plugin/repo release identity、rubric version、代表性 artifact hashes。此后禁止修改 candidate/payload/rubric；只允许不影响这些 identity 的 control/evidence-only commits。

### Phase 7 — Fresh selection/freeze

冻结 exactly 3 个 public-safe sources。任何 output生成前完成 completeness preflight，并冻结 source/provenance/hash、自然 task、主要风险、`APPLICABLE_GATES`、`RENDER_REQUIRED` 与 batch manifest。

### Phase 8 — G7 fresh execution

全部三项从同一 `FINAL_CANDIDATE_COMMIT` normal plugin entry运行；逐项完成 source-aware A、完整 candidate B qualitative reading、适用 G3/G4/G5/G6 与实际 render检查。只有 `3/3 PASS`才能继续；任何 finding先做归因，不得改 candidate/rubric。

### Phase 9 — Final independent review

仅 G7 `3/3 PASS`且无 unresolved blocker后，允许 exactly 1 次 Terra Text Review。不得自动 repair/review loop。Reviewer/rubric/contract争议保留原 review并交独立 Critic adjudication，不伪造新 model PASS。

### Phase 10 — Production/release closure

同一 `FINAL_CANDIDATE_COMMIT`上执行 final zero-paid release CI、bounded live install/upgrade smoke + restore、final GPT Reviewer，形成 acceptance dossier，用户明确 `ACCEPT/REJECT`。

### Phase 11 — Integration

只有 `ACCEPT`才允许 ordinary non-force integration。Final certification期间不吸收 main drift；integration时若 drift与 Clear Writing/source/generated payload/review/release/versioning path重叠，停止回 Planner/Critic。无关 drift可普通 merge，但必须证明 final plugin payload/hash与已认证 candidate完全一致，并重跑必要 zero-paid integration CI。

## 8. 当前 bounded authorization envelope

**只有用户实际发送 execution-ready Critic批准后的 kickoff，才授权以下内容。本文存在本身不是授权。**

### Git / task

允许创建/使用 exact branch/worktree；ordinary commit、fetch、pre-final closure阶段 ordinary merge latest main、non-force push、remote handoff；所有 Gate/review/用户 ACCEPT后允许 non-force main integration。

禁止 force push、历史改写、destructive reset/clean、删除其他 branch/worktree、绕过保护或用 destructive Git解决冲突。

### Private artifacts

历史只读：

- `private/exports/054_clear_writing_release_closure/inputs/`
- `private/exports/054_clear_writing_release_closure/deep_research_attempt1/`

本任务可写：

- `private/exports/055_clear_writing_release_convergence/`
- task-local ignored `.local-runtime/`

只用于本 Goal的 known regression、完整长文、render、Critic review与最终验收。private plaintext/PDF/intermediate/JSONL/credentials不得 commit/push。

**Manual Critic handoff 已包含在 kickoff 的 bounded scope 中：** Executor被授权准备上述 `pre_final_critic_bundle/`并在 gate停止；用户本人随后手动上传 manifest列出的 exact source/candidate/render到已有 Critic thread。Executor没有主动上传授权。若改成其他 provider/主动传输、扩大 private file scope或需要新 credential，必须重新获得用户授权。

严禁上传到 Critic bundle：credentials、`auth.json`、token-bearing config、`.local-runtime` child JSONL、Meaning Map、Reader Plan、intermediate drafts/self-audit、repo logs、unrelated private artifacts。

### Candidate replay

允许 canonical repo-local pinned candidate replay，使用 existing Codex account/CODEX_HOME和 temporary `@ai-skills-candidate` identity；不得复制 `auth.json`，不得 global Codex upgrade，不得覆盖 live production identity。

### CI

允许 focused/full zero-paid tests、render QA、source/generated parity、Marketplace/release CI。ordinary push不得触发 paid review。

### Paid final review

用户发送 kickoff后只授权：

- OpenAI API；`gpt-5.6-terra`；final Text Review only；
- `POST /v1/responses/input_tokens` preflight，`POST /v1/responses` final review；
- `store=false`，default service tier，low reasoning，`max_output_tokens<=4096`，paid tools none；
- max **1** paid call；automatic retry `0`；per-call worst-case `<= USD 0.25`；campaign ceiling `<= USD 0.25`；
- credential仅 existing GitHub Actions `OPENAI_REVIEW_API_KEY`，不得读取/回显/复制/fallback；
- 可发送 final Deep Research candidate text + public-safe fresh candidate text + audience/rubric；不得向 Terra发送 private source、Meaning Map、Reader Plan、intermediate/self-audit、repo log、credential；
- frozen packet超预算则 fail closed，不拆第二 call、不静默删关键材料。

### Bounded production smoke

最终阶段允许一次 bounded `writing-style@yuukias-ai-skills` install/upgrade smoke：先记录 live marketplace/plugin identity + enabled state，安装 exact certified identity，fresh session走普通 prompt，然后 finally restore原状态。不得修改其他 plugins/profiles，不得升级 global Codex，不得扩成持续部署。

## 9. Failure attribution / recovery

正式归因集合：

`PLUGIN_DEFECT | SOURCE_DEFECT | REVIEWER_RUBRIC_DEFECT | ENVIRONMENT_DEFECT | WORKFLOW_DEFECT | CONTRACT_AMBIGUITY`

- **pre-final PLUGIN_DEFECT**：可在 approved architecture内修复；任何 production/payload/artifact/rubric变化都形成新 candidate并重新 Phase 3–5。
- **fresh PLUGIN_DEFECT**：`FINAL_CANDIDATE_COMMIT` G7 FAIL；该 item永久转 known regression。本 package不授权第二 fresh batch、第四 sample、第二 Terra、fresh后production tuning或自动 successor。
- **SOURCE_DEFECT**：保留原 source/output/finding并停止；不得曝光后替换。新 replacement/batch需要新的明确批准范围。
- **REVIEWER_RUBRIC_DEFECT**：保留原 review，由独立 Critic追加裁定；不得改写历史 finding或伪造新 PASS。
- **ENVIRONMENT_DEFECT**：只有 candidate/source/rubric不变且现有恢复路径明确时恢复；不得把真实用户可见 render failure仅靠“环境”标签豁免。
- **WORKFLOW_DEFECT**：停止并由 Planner按当前 role contracts归因；只有不改变 frozen execution contract的修复可在同一 task恢复。
- **CONTRACT_AMBIGUITY**：一旦发现 frozen requirement存在两种合理解释，默认停止 current certification，保留 candidate、source、output、fresh identity、原 finding/review和历史 evidence；不调 production、不临时放宽 rubric、不改写旧 review。Owner = Planner + Critic；先依据冻结 user requirement / Goal / approved design裁定。若只是**不改变既有 requirement**的解释性澄清，可在同一 candidate/certification继续；若裁定实质改变 acceptance、rubric、产品边界、fresh contract、费用、授权或 recovery semantics，则原 certification不能直接沿用，必须形成新的明确批准范围。本 package不自动授权新 fresh、第二 Terra或 successor。只有出现新的产品偏好或 private/provider/credential/cost/live-global授权选择时才请求用户决定。
- **Terra real product defect**：candidate FAIL；不自动第二 Terra，不重置 budget，不自动创建 056。
- **verified pre-request paid failure**：若 `/v1/responses`未发送、未产生 response、未消费 authorized call，可按现行 paid policy同一授权恢复；否则视为已消费。
- **production restore failure**：安全 blocker，停止 integration。
- **main release-critical drift**：final candidate PASS前按 Phase 3处理；PASS后不吸收，integration时回 Planner/Critic。

`CONTRACT_AMBIGUITY` 只是归因/恢复类型，不创建新的 workflow state/schema。

## 10. 完成条件

只有以下全部成立，才能报告 `055` 完成：

1. approved architecture已按本 Goal实现，没有未审扩张；
2. G1–G6在同一 `FINAL_CANDIDATE_COMMIT`上 PASS；
3. pre-final Critic已实际读取该 exact candidate的 private Deep Research source/candidate/render并 PASS；
4. exactly 3 fresh batch按预先冻结标准 `3/3 PASS`；
5. final Terra/合法 adjudication无 unresolved blocker；
6. release CI PASS；
7. bounded production smoke PASS且原 live state成功 restore；
8. final GPT Reviewer PASS；
9. 用户明确 `ACCEPT` final artifact；
10. final plugin payload/hash未变化并完成 non-force main integration。

否则只能报告当前阶段、失败归因和下一合法动作；单个 Gate、一次 reviewer PASS、CI或branch push都不能覆盖本 Goal。

## 11. Non-goals

本任务明确不做：Bridge Kit / Host Policy / execpolicy修改；新 top-level plugin/runtime/daemon/queue/state/schema/ledger；Research Authoring重构；默认联网 fact-check；maturity status提升；大规模语料/外部依赖；禁词/regex/sample-specific rule代替语义处理；把 050–054 exposed samples重新包装成 fresh；第二次 Terra或自动 paid retry；扩大 private data/provider/credential/live-global scope；Executor主动传输 private Critic bundle；force/destructive Git；自动创建 successor。