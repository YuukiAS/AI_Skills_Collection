# Clear Writing 下一次正式发布收口 — Execution Plan

- Execution package version: `v0.2`
- Task key: `055_clear_writing_release_convergence`
- Target plugin: `writing-style` / Clear Writing
- Design authority: `docs/design/clear-writing/NEXT_RELEASE_PROPOSAL.md` v0.1
- Design Critic authority: `docs/design/clear-writing/NEXT_RELEASE_CRITIC_REVIEW.md` round 1 `PASS`
- Prior execution-ready review: `docs/design/clear-writing/NEXT_RELEASE_EXECUTION_CRITIC_REVIEW.md`, commit `92251dd6f7a94b942fd0cd181f7f0c5b01db43bc`, decision `REVISE`, blockers `C1,C2,C3,C4`
- Canonical Goal: `docs/goals/055_CLEAR_WRITING_RELEASE_CONVERGENCE_GOAL.md` v0.2
- Kickoff Draft: `docs/operations/prompts/055_CLEAR_WRITING_RELEASE_CONVERGENCE_KICKOFF.md` v0.2
- Status: `READY_FOR_EXECUTION_CRITIC_REVIEW`

本文件只修订 execution contract，不重新设计已经 PASS 的 Clear Writing architecture、G1–G8 taxonomy 或 A/B/C Reviewer 基本设计。只有独立 Critic 对本 v0.2 Plan + Goal + Kickoff 同版给出 execution-ready PASS，且用户随后实际发送获批 kickoff，才允许启动 Executor。

## 0. 对上一轮 C1–C4 的处理

### C1 — `ACCEPT`

修改位置：本 Plan 的 G8、§6 执行顺序、§10 release identity；Goal 的 G8、Phase 4–7 与完成条件；Kickoff 的严格顺序与停止条件。

修订后，**最后一次 pre-final Critic 实际审查并 PASS 的 exact candidate commit / generated payload，就是进入 fresh 的 final candidate**。版本号、changelog、latest-main reconcile、source/generated parity、generated payload 都在该次 Critic review 之前完成。Critic 若要求任何会改变 production source、generated payload、rubric 或代表性 artifact 的修复，必须产生新 candidate，重新生成完整代表性 artifact/render，并再次交 Critic；旧 PASS 不带到新 candidate。

Critic PASS 后只允许 task-local control/evidence 写入；这些写入不得改变 pinned `FINAL_CANDIDATE_COMMIT`、rubric 或 plugin payload hash。fresh/review/release replay 始终显式 pin 该 exact candidate。若任何 post-PASS 变化触及 production source、generated payload、version/release identity、rubric 或 user-facing representative artifact，pre-final PASS 立即失效，回到 pre-final candidate closure + artifact + Critic 循环。

### C2 — `ACCEPT`

修改位置：本 Plan §8 Private artifacts 与 §6 Phase 5；Goal 的 private handoff 段；Kickoff 的 manual upload gate。

采用最简单、无新 provider 的路线：Executor 在 repo-local private 路径生成固定的 pre-final Critic bundle并停止；由**用户本人**把指定 source/candidate/render 文件上传到已有长期 Critic thread。Executor 不主动上传 private plaintext，不引入 artifact transport framework，不修改 Bridge Kit。

固定 bundle root：

`private/exports/055_clear_writing_release_convergence/pre_final_critic_bundle/`

至少包含：

- `01_SOURCE_FULL.txt`：用于该代表性 Deep Research replay 的完整 source 文本；若 replay 的 canonical input 不是纯文本，同时保留 exact original input under `source_original/`，并在 manifest 列出；
- `02_CANDIDATE.md`：该 exact candidate 生成的完整 Deep Research candidate；
- `03_RENDER.pdf`：上述 candidate 的实际 render；
- `04_BUNDLE_MANIFEST.md`：`FINAL_CANDIDATE_COMMIT` 候选 SHA、plugin payload hash、source file/hash、candidate/render hash、rubric version、公开 G1–G6 evidence locators，以及需要用户上传给 Critic 的 exact file list。

Kickoff 本身授权 Executor**准备该 bundle、在该 gate 停止并请求用户按 manifest 手动上传到既有 Critic thread**；这不是授权 Executor/API 主动传输 private data。只有改成别的 provider/主动传输、扩大到上述 exact bundle 之外的 private data，或要求新的 credential，才需要新的用户授权。Credentials、`auth.json`、`.local-runtime` JSONL、Meaning Map、Reader Plan、self-audit、repo logs、unrelated private artifacts 严禁随此 handoff 上传。

### C3 — `ACCEPT`

修改位置：本 Plan §9 Failure attribution / recovery；Goal Recovery；Kickoff failure handling。

新增 `CONTRACT_AMBIGUITY` 作为**归因/恢复类别**，不是新 workflow state/schema。发现 frozen requirement 存在两种合理解释时，默认停止当前 certification，保留原 candidate、source、output、fresh identity、review finding 与历史 evidence，不调 production、不临时放宽 rubric、不改写旧 review。Owner 为 Planner + Critic。

只有 Planner + Critic 认定属于“不改变既有 frozen requirement 的解释性澄清”时，才可在同一 certification 上继续；若裁定实质改变 acceptance、rubric、产品边界、fresh contract、费用或 recovery semantics，则原 certification 不能直接沿用，必须形成新的明确批准范围。本 v0.2 不预授权新的 fresh batch、第二次 Terra 或 successor。只有真正涉及新的产品偏好、private/provider/credential/cost/live-global 授权时才请求用户决定。

### C4 — `ACCEPT`

修改位置：本 Plan G7、§6 Phase 7–8；Goal G7 与 fresh 阶段；Kickoff 的 fresh PASS 条件。

G7 不再只是“冻结样本管理”。三个 fresh item 全部必须由**同一个 exact final candidate 的 normal production entry**生成；每个 item 在生成前就在 manifest 中冻结主要风险、适用 G2–G6 条件和是否必须 render。每项都必须有 source-aware A 证据和对完整 candidate 的真实 B 定性阅读；公式/表格/code/reproducibility 按 G3，dirty source 按 G4，reader relevance/modality/中文/voice 按 G5，长文与需要视觉核对的结构化内容按 G6/真实 render。receipt/hash/deterministic audit 只能辅助，不能单独判 capability PASS。只有 `3/3` 全部满足预先冻结标准，G7 batch 才 PASS；Terra 是之后的额外独立最终认证，不是 fresh artifact 第一层 qualitative grader。

## 1. 目标与边界

本任务只收口 Clear Writing 下一次兼容发布。普通用户从正式 `writing-style` 入口提交已有中文/中文主导科研技术材料时，应得到真正面向读者的成稿，同时保持 source fidelity、公式/表格/代码/引用/必要复现信息，并正确清理 wrapper、内部流程痕迹与无关来源包装。

不重新设计 051–054 已建立的主链，不新增顶级 plugin/runtime/state/ledger，不修改 Bridge Kit，不把 Clear Writing 扩成自动事实核查器或 Research Authoring。

历史表述继续按已通过 N1/N2：

- 052 已完成其 bounded reader-facing closure，包括 release CI、production smoke、用户 ACCEPT 与 main integration；这不等于跨任务长期成熟度。
- 053 fresh H1 的正式失败是 PDF 中 Cyrillic glyph 缺失的真实 render failure；reader relevance 的主要直接证据来自 054 F1/F2 与后续真实反馈。

## 2. Exact task / branch / worktree

若 execution-ready Critic PASS 后用户发送获批 kickoff：

- exact task: `055_clear_writing_release_convergence`
- exact branch: `reviewed/055_clear_writing_release_convergence`
- exact worktree: `/tmp/ai-skills-055-clear-writing-release-convergence`

启动时先 `git fetch origin main`。branch 必须从当时最新 `origin/main` 创建，且最新 main 必须仍包含获批 package，并未改变本任务相关 policy/design。若存在相关语义变化或同名 task/branch 冲突，停止并回 Planner/Critic；不得自行换编号或改合同。

Executor 必须按 `AGENTS.md` 显式使用 `workflow-core + ai-skills-core + writing-style`。生产实现只发生在 exact task branch/worktree；main 只在所有 Gate、review、用户 `ACCEPT` 后按本 Plan 集成。

## 3. 已批准的实现机制

保留主链：

`ordinary entry -> Meaning Map -> Reader Plan -> REALIZE_MEANING -> assembly / whole-document finish -> fidelity/audit -> bounded repair -> final candidate`

仅执行已批准的有限职责修正：

1. Reader Plan 负责读者处置：正文核心、正文支持、结构化技术对象、需移位复现细节、source future work、wrapper、internal trace。优先复用现有 Meaning Map / Reader Plan 与 `inline-critical | relocatable-trace | internal-workflow-trace`；不建平行持久 ledger/schema/state。
2. REALIZE_MEANING 保持完成状态、主体、时态、条件、认识状态、source-author proposal 与 assistant recommendation 的差异；不靠禁词判断。
3. assembly/final pass 负责全文目的、章节顺序、跨 bundle 重复/冲突、定义位置、过渡、future work/limitations/repro details placement 与统一 reader voice；不建立第二生成 runtime。
4. writing-fidelity 继续做 verifier，检查 proposition/evidence/attribution 与 Reader Plan disposition，一律不承担 prose generation。
5. deterministic helper 只做机械保护/拒绝：literal、公式、表格、路径类别、render、generated parity 等；不得用关键词、英文数量、code fence、路径外观或禁词墙冒充 reader judgment。
6. 053/054 只作 evidence/选择性实现来源；禁止 whole-branch merge 和 sample-specific patch。

## 4. G1–G8 Capability Gates

### G1 — 正常入口、安装与兼容

证明 exact candidate 从 canonical candidate marketplace、install/upgrade、fresh session、普通自然 prompt 真正被加载和消费；heavy rewrite 不得吞掉 light Chinese、English scientific prose、fidelity-only、source-comparison 等合法路线。direct skill/helper 不能代替正式入口。

### G2 — Source fidelity / attribution

对 source + candidate 检查 claim、evidence、polarity、quantifier、comparator、condition、caveat、uncertainty、citation、attribution、结论强度及 Reader Plan 的删除/移位决定。遗漏、无来源新增、strengthening、错误归因、条件/否定漂移、citation 损坏均 FAIL。外部世界事实默认不属于此 Gate，除非 candidate 相对 source 新增/强化错误。

### G3 — 公式、表格、代码与复现信息

至少覆盖 FFT math/operator、table-rich technical case、合法 Python 示例、必要 path/config/command/API/identifier 与 internal trace 的 should-keep/should-drop 对照。结构化内容必须语义与实际 render 正确；不得靠 fence/path/字符计数 PASS。

### G4 — Dirty source / markup cleanup

Bloom/wikitext、noisy RST/HTML/wiki/export 类 source 中 wrapper、导航、模板、重复链接、无关 disclaimer/license debris 不得进入普通正文；清理不能破坏 G2/G3。

### G5 — Reader relevance / 中文质量 / voice / script

直接修复 054 F1/F2：全文不能继续像项目备忘录/执行计划；source future work 不能变成 executor 当前 action；internal audit/task/repo path 不得挤进正文；真正复现信息不能因像路径而误删；中文自然、简繁体正确、必要英文有真实定位价值。禁词/English count/script count 只能诊断，不能判 PASS。

### G6 — 完整长文、结构连贯与真实 render

用完整 Deep Research + 至少一份独立已曝光长文 known regression 直接生成、阅读全文并实际 render。检查全文目的、章节顺序、定义位置、过渡、重复/冲突、technical detail placement、future work/limitations/reproducibility placement 与 PDF 可读性。053 Cyrillic glyph failure 必须作为真实 render regression。

**G6 的最后一次 release-critical PASS 必须来自准备进入 fresh 的 exact candidate。**

### G7 — Fresh generalization

在最后一次 pre-final Critic 已对 exact candidate PASS 后，冻结 exactly 3 个新的 public-safe holdout，分别以以下主要风险为主：

1. noisy technical + legitimate code/reproduction token；
2. formula/table structured technical content；
3. long-form + future-work/limitation/attribution/reader-relevance decision。

不得使用 050–054 已曝光样本。生成前必须对完整 3-item manifest 做 source completeness preflight，并为每项冻结：`PRIMARY_RISK`、`APPLICABLE_GATES`、source/provenance/hash、自然用户任务、`RENDER_REQUIRED=YES/NO`。

每个 fresh item 的 PASS 至少要求：

- **Normal entry**：全部由同一个 `FINAL_CANDIDATE_COMMIT` 的普通 plugin entry 运行，不能 direct skill/helper。
- **A / G2**：必须有 source-aware fidelity evidence，直接核对 source 与完整 candidate；机械 overlap/receipt 不能代替。
- **B / G5**：必须对完整 candidate 做一次真实定性阅读，按冻结 reader-facing rubric判断自包含、中文、voice、modality、reader relevance；不能只用 generator self-audit、关键词或 mechanical scan。该本地定性阅读不是“独立最终认证”，最终独立性由后续 Terra/Reviewer提供。
- **G3**：涉及 formula/table/code/repro/path/config/API 的 item 必须按结构化技术内容标准核对；formula/table 等需要视觉确认时必须实际 render。
- **G4**：noisy/dirty-source item 必须检查 wrapper 清理且正文语义不丢。
- **G6**：long-form item 必须实际生成完整 render 并检查全文结构、过渡和可读性；任何 manifest 标记 `RENDER_REQUIRED=YES` 的 item 必须实际查看 render，不以 file existence 代替。
- deterministic audit、receipt、hash、route event 只能作为辅助证据，不能单独把 item 判成 capability PASS。

G7 batch 只有 `3/3` 全部满足预先冻结的适用 G2–G6 标准才 PASS。candidate 在 batch 中不得修改。任一 true product failure 都使该 final candidate 的 G7 certification FAIL；该 item 从此转 known regression。不得替换、补第 4 个、改 production 后重用该 fresh batch，或让 Terra成为这些 fresh artifacts 的第一层 qualitative grader。

### G8 — 同一 final candidate 的 production certification + 独立定性复核

所有 release-critical evidence 必须绑定同一个 final plugin candidate：

- `FINAL_CANDIDATE_COMMIT`；
- generated plugin payload/hash；
- G1–G6 在该 exact candidate 上的最终 regression + representative artifact evidence；
- 最后一次 pre-final Critic 对该 exact candidate 的 source/candidate/render 实际 review `PASS`；
- G7 frozen fresh batch `3/3 PASS`；
- exactly 1 次最终 `gpt-5.6-terra` Text Review，或对其 rubric finding 的合法 Critic adjudication；
- final zero-paid release CI；
- bounded production install/upgrade smoke + restore；
- final GPT Reviewer/Reviewed Handoff review；
- 用户 final artifact `ACCEPT`；
- latest-main integration 后 final plugin payload/hash 不变化。

**Candidate identity rule：** version/changelog、latest-main reconcile、source/generated parity 与 generated Marketplace/plugin payload closure 必须在最后一次 pre-final Critic review 前完成。Critic review 的 candidate commit 与进入 fresh 的 `FINAL_CANDIDATE_COMMIT` 必须相同。

Critic PASS 后只允许 `results/055...`、Reviewed Handoff control/review evidence、fresh manifest/results 等不影响 production/release payload的 control/evidence-only写入。所有 post-PASS replay显式 pin `FINAL_CANDIDATE_COMMIT`。若 post-PASS 修改触及 production source、generated payload、plugin/repo version identity、frozen rubric 或已审代表性 artifact，则 prior pre-final Critic PASS 失效，禁止 fresh/Terra，必须形成新 candidate并重复代表性 artifact + Critic review。

## 5. Reviewer / Terra rubric

所有定性 finding 必须先归入：

- **A — source fidelity**：硬 blocker。Reviewer 必须能看到 source + candidate；检查遗漏、新增、条件/否定/数量/归因/引用/结构化对象及 disposition 一致性。
- **B — reader-facing quality**：硬 blocker。Reviewer 直接读 candidate/render；检查自包含、自然中文、全文连贯、内部过程泄漏、future-work voice、code/path/config placement 与 render 可读性。
- **C — external factual truth**：默认非 Clear Writing blocker。本任务不授权自动 fact-check。只有 candidate 相比 source 新增/强化/错误归因时转成 A；否则记录 source-quality warning，不偷偷改正文。

合法代码不能仅因是 code 被 blocker；path/config 按 reader/reproducibility role 判断；source future work/limitation 必须保持真实 modality；source 自带外部事实问题不自动算 rewrite defect。

任何 blocker 必须给出 A/B/C、对应 frozen Gate/requirement、candidate 精确位置；A 还需 source 位置；违反理由；初步归因；最小关闭条件。无法回指 frozen requirement 的观察只能 advisory。

最终 Terra 主要独立验证 B，并检查其可见 packet 内的 contract-compatible structured content；不得临场把 C 变 blocker。A 的 release-critical source-aware独立验证由最后一次 pre-final Critic / final GPT Reviewer 对同一 `FINAL_CANDIDATE_COMMIT` 完成。

## 6. 强制执行顺序

### Phase 1 — Bootstrap

latest-main preflight；创建 exact branch/worktree/task control；读取获批 package/current source/必要历史 evidence；不重新设计。

### Phase 2 — Implementation + known regression

只在已知 050–054 failures 与新增 should-keep/should-drop regression 上迭代；完成开发阶段 G1–G5。此阶段允许在 approved architecture 内正常修复。

### Phase 3 — Pre-final release payload closure

在请求 Critic 之前完成所有会改变 final candidate identity 的事项：

1. reconcile 当时 latest main；若 concurrent change 触及 writing-style production behavior / relevant policy，停止回 Planner/Critic；
2. 按 `PLUGIN_VERSIONING_AND_CHANGELOGS.md` 完成 plugin version、plugin changelog、repository release metadata/changelog 的候选 closure；
3. 生成正式 Marketplace/plugin payload并使 source/generated parity PASS；
4. 冻结 A/B/C rubric；
5. commit 一个 exact candidate `C_n`，记录 candidate commit 与 plugin payload hash。

此后 G1–G6 的 release-critical evidence必须从 `C_n` 生成。

### Phase 4 — Representative whole-artifact / G1–G6 on `C_n`

使用 canonical candidate replay显式 pin `C_n`，重跑完整 G1–G6；生成完整 Deep Research 与另一份已曝光长文回归的 Markdown/PDF/render并实际阅读全文。任何问题都在进入 Critic 前修复；一旦修改 production/payload/rubric，形成新的 `C_(n+1)` 并从 Phase 3 重新开始。

### Phase 5 — Pre-final independent Critic + private handoff

Executor 准备两部分材料：

**公开可 push 的 evidence packet**：candidate commit/diff、payload hash、G1–G6 evidence summary、rubric、should-keep/should-drop cases、fresh risk categories、paid-review边界；不得包含 private plaintext。

**repo-local private bundle**：

`private/exports/055_clear_writing_release_convergence/pre_final_critic_bundle/`

包含 `01_SOURCE_FULL.txt`、`02_CANDIDATE.md`、`03_RENDER.pdf`、`04_BUNDLE_MANIFEST.md`；若 replay canonical source 不是纯文本，另在 `source_original/` 保存 exact original input，并在 manifest 中列出用户需要上传的 exact source file(s)。

Executor commit/push公开 packet 后停止，并向用户报告 manifest 和需要上传给长期 Critic thread 的 exact private file paths。**用户本人手动上传**这些文件到已有 Critic thread；Executor 不主动传输。Critic 必须实际读取 source + candidate + render 后，才可对 `C_n` 给 pre-final PASS。

若 Critic `REVISE`：

- 仅 control/evidence 表述修正且不改变 candidate/payload/rubric/artifact：修正后可复核同一 `C_n`；
- 任何 production source、generated payload、version identity、rubric、代表性 candidate/render 改变：旧 PASS/审查不适用于新 candidate；回 Phase 3，生成新 candidate、重跑 G1–G6、重建 private bundle并重新交 Critic；
- 若要求改变已批准 architecture、Gate、预算、授权或 recovery semantics：回 Planner/Critic execution-package amendment，不由 Executor临场改。

### Phase 6 — Final candidate designation

只有最后一次 Critic 对 `C_n` 明确 PASS 后，`C_n` 才被指定为 `FINAL_CANDIDATE_COMMIT`。同时冻结/记录：payload hash、plugin/repo release identity、rubric version、代表性 artifact hashes。

从此禁止改变 candidate/payload/rubric。不得再 merge latest main 到 final candidate branch 后拿新 HEAD 去跑 fresh；后续所有 replay pin `FINAL_CANDIDATE_COMMIT`。允许的只是不会改变上述 hash/identity 的 control/evidence-only commits。

### Phase 7 — Fresh selection/freeze

冻结 exactly 3 个 public-safe sources。生成任何 candidate output 前，完成 source completeness preflight，并冻结每项的 source/provenance/hash、自然任务、主要风险、`APPLICABLE_GATES`、`RENDER_REQUIRED` 和完整 3-item manifest。不得用已曝光 050–054 sample。

### Phase 8 — Fresh G7 execution + qualitative acceptance

全部三项使用同一 `FINAL_CANDIDATE_COMMIT` normal plugin entry。按 G7 逐项完成 A source-aware evidence、B完整 candidate qualitative reading及适用 G3–G6/render检查。只有 `3/3 PASS` 才允许继续。任何 finding 先进入 §9 attribution；不得先改 candidate或改 rubric。

### Phase 9 — Final independent paid review

只有 G7 `3/3 PASS` 且无 unresolved hard blocker，才允许最多 1 次 Terra Text Review。若 Terra finding 疑似 reviewer/rubric/contract问题，保留原 review并按 §9 交独立 Critic裁定；不得伪造新模型 PASS、不得第二次 paid review。

### Phase 10 — Release closure

同一 `FINAL_CANDIDATE_COMMIT` 上执行 final zero-paid release CI、bounded production install/upgrade smoke + restore、final GPT Reviewer。全部 PASS 后给用户 final artifact/acceptance dossier；只有用户 `ACCEPT` 才允许 integration。

### Phase 11 — Integration

final certification期间不吸收 main drift。用户 ACCEPT 后才处理 latest main integration：若 drift 与 Clear Writing/source/generated payload/review/release/versioning path 重叠，停止回 Planner/Critic；若仅无关 drift，可普通 non-force merge/integration，但必须证明 final plugin payload/hash与已认证 candidate完全一致，并重跑必要 zero-paid integration CI。任何需要改 payload/version/rubric 的集成都使当前 certification不能直接沿用。

## 7. Paid Terra contract（只有用户发送获批 kickoff 后才授权）

本 package 本身不产生付费授权。用户实际发送 Critic 批准后的 kickoff时，只授权：

- provider: OpenAI API；model: `gpt-5.6-terra`；purpose: final candidate independent Text Review only；
- preflight: `POST /v1/responses/input_tokens`；paid endpoint: `POST /v1/responses`；
- `store=false`，`service_tier=default`，low reasoning，`max_output_tokens<=4096`，paid tools none；
- max paid calls **1**；automatic paid retry **0**；per-call worst-case `<= USD 0.25`；campaign ceiling `<= USD 0.25`；
- credential 仅 existing GitHub Actions `OPENAI_REVIEW_API_KEY`；不得读取/回显/复制，不得 fallback；
- packet 可包含 final Deep Research **candidate text**、public-safe fresh candidate text、audience/rubric；不得向 Terra 发送 private source、Meaning Map、Reader Plan、intermediate/self-audit、repo logs/credentials；
- 若完整冻结 packet 超预算，fail closed；不得拆第二 call或静默删关键材料；
- 已发送/已消费 call 不因 REVISE/restart重置；可证明 `/v1/responses` 未发送的 pre-request infrastructure/deterministic failure 按现行 paid policy恢复。

## 8. Private artifact / candidate replay / CI / production smoke 授权边界

只有用户实际发送获批 kickoff 后，当前 task 才获得这些授权。

### Private artifacts 与 pre-final Critic handoff

历史只读：

- `private/exports/054_clear_writing_release_closure/inputs/`
- `private/exports/054_clear_writing_release_closure/deep_research_attempt1/`

本任务可写：

- `private/exports/055_clear_writing_release_convergence/`
- task-local ignored `.local-runtime/`

用途只限 known regression、representative whole-artifact generation/render、pre-final Critic review 与最终用户验收。private plaintext/PDF/intermediate/JSONL/credential 不得 commit/push。

发送获批 kickoff即表示用户同意**本任务在 pre-final gate 采用人工上传路线**：Executor只准备 `pre_final_critic_bundle/` 并停止，用户本人将 manifest 指定的 Deep Research source/candidate/render上传到已有长期 Critic thread。该同意不允许 Executor主动上传，也不允许把 bundle 发到新的 provider。若 transport/provider改变、需要 Executor主动传输、需要新credential或扩大 private file scope，必须重新获得用户授权。

严禁进入 Critic upload bundle：credentials、`auth.json`、token-bearing config、`.local-runtime` child JSONL、Meaning Map、Reader Plan、intermediate drafts/self-audit、repo logs、unrelated private artifacts。

### Candidate replay

允许按 `docs/workflows/CANDIDATE_PLUGIN_REPLAY.md` 使用 repo-local pinned runtime、existing Codex account/CODEX_HOME、temporary `@ai-skills-candidate` identity、fresh ephemeral session 与 finally cleanup。不得复制 `auth.json`、不得升级 global Codex、不得覆盖 live production identity。

### CI

允许运行 focused tests、full zero-paid tests/CI、generated parity、render QA、Marketplace/release CI。普通 push 不得触发 paid review；Terra必须 explicit/manual dispatch。

### Production install/smoke

最终阶段允许一次 bounded `writing-style@yuukias-ai-skills` install/upgrade smoke：开始前记录 live marketplace/plugin identity+enabled state，安装 exact certified identity，fresh session普通 prompt验证，结束后无论 PASS/FAIL均 restore原 live state。不得改其他 plugin/profile，不得 global Codex upgrade，不得扩成长期 live deployment。

### Git

允许 exact branch/worktree 上 ordinary commit、fetch、pre-final candidate closure时的 ordinary merge latest main、non-force push、remote handoff；最终所有 Gate + Reviewer + 用户 ACCEPT 后允许 conflict-free/non-force main integration。禁止 force push、destructive reset/clean、历史改写、删除其他 branch/worktree或用 destructive Git解决冲突。

## 9. Failure attribution / recovery

正式归因集合为：

`PLUGIN_DEFECT | SOURCE_DEFECT | REVIEWER_RUBRIC_DEFECT | ENVIRONMENT_DEFECT | WORKFLOW_DEFECT | CONTRACT_AMBIGUITY`

- **known/pre-final PLUGIN_DEFECT**：在 final candidate designation 前可按 approved architecture 修复；任何 production/payload/artifact变化都形成新 candidate并重新走 Phase 3–5。
- **fresh PLUGIN_DEFECT**：`FINAL_CANDIDATE_COMMIT` 的 G7 certification FAIL；该 item 永久转 known regression。当前 package不授权修 candidate后第二 fresh batch、第四 item、第二 Terra或自动 successor。
- **SOURCE_DEFECT**：保留原 source/output/finding并停止；不得曝光后静默替换。需要 replacement/new batch必须形成新的批准范围。
- **REVIEWER_RUBRIC_DEFECT**：保留原 finding/review，由独立 Critic adjudicate；不得删除旧 review、改写 model verdict或伪造新 PASS。
- **ENVIRONMENT_DEFECT**：仅在 candidate/source/rubric不变且现有恢复路径明确时恢复；不得写成 product PASS/FAIL。render/font等真实用户可见 artifact defect若来自最终产品环境，仍按实际 Gate failure处理，不因标签“环境”自动豁免。
- **WORKFLOW_DEFECT**：若 control/CI/handoff实现违反冻结合同，停止并按当前 role contracts由 Planner归因；只有不改变 frozen execution contract的修复可在同一 task恢复。
- **CONTRACT_AMBIGUITY**：frozen requirement存在两种合理解释时，默认暂停当前 certification。完整保留 candidate、source、output、fresh身份、原 review/finding及历史 evidence；不调 production、不临时放宽rubric、不改写旧 review。Owner = Planner + Critic，先回到用户冻结要求、Canonical Goal和approved design裁定。若只是**不改变既有 requirement**的解释性澄清，可由 Critic记录裁定后在同一 candidate/certification继续；若裁定实质改变 acceptance、rubric、产品边界、fresh contract、费用、授权或 recovery semantics，则当前 certification不能直接沿用，必须形成新的明确批准范围。本 package不因此自动授权新 fresh/第二 Terra/successor。只有出现新的产品偏好或 private/provider/credential/cost/live-global授权选择时才请求用户决定。
- **Terra real product defect**：final candidate FAIL；不自动 repair+第二次 Terra、不重置campaign、不创建 successor。
- **paid pre-request failure**：按 paid policy判断是否真正未发送；未发送且未消费可在同一授权恢复，已发送则不能当未消费。
- **production smoke restore failure**：安全 blocker，立即停止，不得 integration。
- **main drift**：pre-final Critic之前可以按 Phase 3处理；final candidate PASS后不吸收 drift。最终 integration如有 release-critical overlap，回 Planner/Critic。

## 10. Version / changelog / release identity

执行时必须重新读取 `PLUGIN_VERSIONING_AND_CHANGELOGS.md` 和当前 version sources，不能盲用历史数字。

本 package 编写时已知基线为 repository `5.0.4`、`writing-style` `0.2`；若执行时无相关 concurrent release，预期 compatible release为 repo下一 patch、writing-style下一两段版本。实际数字以任务启动时 canonical version sources为准。

**关键顺序：** plugin/repository version候选、plugin/root changelog、Marketplace/generated payload、source/generated parity与 latest-main reconcile全部在最后一次 pre-final Critic review之前完成，并成为 `C_n` 的一部分。Critic PASS后不得再修改这些 release identity files；如果必须修改，prior PASS失效，重新进入 Phase 3–5。

本任务不提升 `docs/PLUGIN_MATURITY.md` 状态。

## 11. Non-goals / 明确禁止

- 不改 Bridge Kit、Host Policy、execpolicy；
- 不重做 Proposal v0.1 architecture、G1–G8 taxonomy或A/B/C基本设计；
- 不新增 top-level plugin、runtime、daemon、queue、state machine、schema/ledger；
- 不把 Research Authoring 并入 Clear Writing；
- 不默认联网 fact-check；
- 不引入 Vale/Pandoc等新 production dependency；
- 不新增大规模 corpus/资源摄取；
- 不用禁词/regex/sample-specific特判换 PASS；
- 不修改 050–054历史证据或把暴露样本重称 fresh；
- 不自动创建 successor；
- 不进行第二次 Terra、不扩大 cost/provider/data/credential/live-global scope；
- 不让 Executor主动上传 private Critic bundle；
- 不 force/destructive Git；
- 不把 tests/CI/receipt/hash/file existence当语言质量或总体 PASS。

## 12. 完成定义

`055` 只有在同一个 `FINAL_CANDIDATE_COMMIT` / plugin payload identity 上：

1. approved architecture 已实现且没有未审扩张；
2. G1–G6 final evidence PASS；
3. 独立 Critic 已实际读取该 candidate 的 private Deep Research source/candidate/render并 PASS；
4. exactly 3 fresh item 按预先冻结 G2–G6 标准 `3/3 PASS`；
5. final Terra/合法 adjudication无 unresolved hard blocker；
6. release CI PASS；
7. bounded production smoke PASS且原 live state恢复；
8. final GPT Reviewer PASS；
9. 用户明确 `ACCEPT` final artifact；
10. integration后 final plugin payload/hash不变；

才可报告 release task完成。任何局部 PASS、Critic PASS、fresh PASS、Terra PASS、CI PASS或branch push都不是总体完成。