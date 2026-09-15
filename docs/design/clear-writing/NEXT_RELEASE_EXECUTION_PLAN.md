# Clear Writing 下一次正式发布收口 — Execution Plan

- Execution package version: `v0.1`
- Task key: `055_clear_writing_release_convergence`
- Target plugin: `writing-style` / Clear Writing
- Design authority: `docs/design/clear-writing/NEXT_RELEASE_PROPOSAL.md` v0.1
- Design Critic authority: `docs/design/clear-writing/NEXT_RELEASE_CRITIC_REVIEW.md` round 1 `PASS`
- Canonical Goal: `docs/goals/055_CLEAR_WRITING_RELEASE_CONVERGENCE_GOAL.md`
- Kickoff Draft: `docs/operations/prompts/055_CLEAR_WRITING_RELEASE_CONVERGENCE_KICKOFF.md`
- Status: `READY_FOR_EXECUTION_CRITIC_REVIEW`

本文件把已经通过 Critic 的 Proposal v0.1 转成可执行合同，不重新设计架构。只有独立 Critic 对本 execution package v0.1 的 Plan + Goal + Kickoff Draft 同版给出 execution-ready PASS，且用户随后实际发送获批 kickoff，才允许启动 Executor。

## 1. 目标与边界

本任务只收口 Clear Writing 下一次兼容发布。核心目标是让普通用户从正式 `writing-style` 入口把已有中文/中文主导科研技术材料重写成真正面向读者的成稿，同时保持 source fidelity、公式/表格/代码/引用/必要复现信息，并正确清理 wrapper、内部流程痕迹与无关来源包装。

不重新设计 051–054 已建立的主链，不新增顶级 plugin/runtime/state/ledger，不修改 Bridge Kit，不把 Clear Writing 扩成自动事实核查器或 Research Authoring。

历史表述按 Critic N1/N2 校正：

- 052 已完成其 bounded reader-facing closure，包括 release CI、production smoke、用户 ACCEPT 与 main integration；它证明的是该冻结范围，不等于跨任务长期成熟度。
- 053 fresh H1 的正式失败是 PDF 中 Cyrillic glyph 缺失的真实 render failure；它进入 render regression，不改写成 reader-relevance failure。reader relevance 的主要直接证据来自 054 F1/F2 与后续真实使用反馈。

## 2. Exact task / branch / worktree

若 execution-ready Critic PASS 后用户发送获批 kickoff：

- exact task: `055_clear_writing_release_convergence`
- exact branch: `reviewed/055_clear_writing_release_convergence`
- exact worktree: `/tmp/ai-skills-055-clear-writing-release-convergence`

启动时先 `git fetch origin main`。branch 必须从当时最新 `origin/main` 创建，但最新 main 必须仍包含本 execution package 的获批版本，且没有改变本任务相关 policy/design。若存在相关语义变化或同名 task/branch 冲突，停止并回 Planner/Critic；不得自行换 task 编号或改合同。

Executor 必须按 `AGENTS.md` 同时使用 `workflow-core + ai-skills-core + writing-style` 的职责边界。生产实现只发生在 exact task branch/worktree；main 只在最终用户 ACCEPT 后按本 Plan 集成。

## 3. 已批准的实现机制

保留主链：

`ordinary entry -> Meaning Map -> Reader Plan -> REALIZE_MEANING -> assembly / whole-document finish -> fidelity/audit -> bounded repair -> final candidate`

只做以下有限职责修正：

1. **Reader Plan 变成真正的读者处置合同。** 对 source obligation 明确其读者角色：正文核心、正文支持、结构化技术对象、需要移位的复现细节、source future work、应清理 wrapper、应删除内部 trace。执行实现必须优先复用并扩展现有 Meaning Map / Reader Plan 与 `inline-critical | relocatable-trace | internal-workflow-trace` 语义；不得再建平行持久 ledger/schema/state。新增字段只有在现有表示无法表达且测试证明必要时才允许最小增加。
2. **REALIZE_MEANING 保持 modality。** 必须区分已完成/未完成、source author proposal/assistant recommendation、scientific limitation/workflow blocker、hypothetical/conditional/committed action、external attribution/narrator voice。不得靠禁词判断。
3. **assembly/final pass 承担完整成稿。** 不是只拼接/去重，而要处理全文目的、章节顺序、跨 bundle 重复或冲突、定义位置、过渡、future work/limitations/repro details 的位置与全局 voice。优先复用现有 `chinese-prose` + assembly/final pass，不建立第二生成 runtime。
4. **fidelity/audit 继续做 verifier。** 核查 proposition/evidence 与 Reader Plan disposition 是否一致，不能反过来成为新的 prose generator。
5. **deterministic helper 只做机械保护/拒绝。** 可以检查结构、literal、公式、表格、路径类别、render/generated parity；不得用关键词、英文数量、code fence 数量、路径外观或禁词墙冒充 reader judgment，不得机械生成正文。
6. **054 只选择性吸收。** 必须从最新 main 出发，对 054 branch 逐项比较；只移植能被 Proposal/Critic 与真实 evidence 支持的最小机制，禁止 whole-branch merge 或 sample-specific patch。

## 4. G1–G8 Capability Gate Matrix

### G1 — 正常入口、安装与兼容

证明普通用户从正式 Clear Writing 安装身份，用自然请求可以进入正确 route；heavy rewrite 不得吞掉 light Chinese、English scientific prose、fidelity-only、source-comparison 等现有合法路线。

材料：当前 main；052 已完成的 install/routing closure 作为历史基线；053/054 candidate replay/compatibility evidence 作为回归来源。

验收：exact candidate 通过 canonical candidate replay，使用正式本地 marketplace staging、fresh session、普通自然 prompt；不得 direct skill/import helper 冒充。应有 should-change 与 should-not-change cases。

### G2 — Source fidelity / attribution

证明重写没有改变 source meaning。

检查：claim、evidence、polarity、quantifier、comparator、condition、caveat、uncertainty、citation、attribution、结论强度以及 Reader Plan 的删除/移位决定。

材料：Bloom、FFT、完整 Deep Research、052/053/054 已知 fidelity regression，以及最终 fresh sources。

失败：遗漏任务相关命题、无来源新增、强化结论、错误归因、条件/否定漂移、citation 损坏。外部世界事实本身默认不属于此 Gate，除非 candidate 相对 source 新增/强化错误。

### G3 — 公式、表格、代码与复现信息

证明结构化技术内容按语义角色正确保留、整理、移位或删除。

材料至少覆盖：FFT 公式/operator；D2L/self-attention table 类已知案例；054 H1 FeatureHasher 合法 Python 示例；Deep Research 中必要 checkpoint/provenance 与 project-local filename/path 的区分；code/path/config 的 should-keep 与 should-drop 成对回归。

失败：公式/运算符损坏、表格语义或 render 失真、合法代码被一刀切删除、内部 task/review 路径被伪装成复现信息、真正复现信息被清掉。不得以 fence/path/字符计数作为 PASS。

### G4 — Dirty source / markup cleanup

证明 wiki/RST/HTML/export wrapper、导航、模板、重复链接、license/disclaimer debris 等不会进入正常读者正文，同时正文语义不丢。

材料：Bloom raw wikitext、Karatsuba/wiki 历史回归、054 noisy sklearn/RST 类案例和独立 dirty-source regression。

失败：wrapper 残留，或清理时误删正文、引用、代码、技术身份。G4 PASS 后仍必须过 G2/G3。

### G5 — Reader relevance / 中文质量 / voice / script

这是本轮核心产品 Gate。证明输出是给读者看的成稿，而不是项目备忘录、审核日志或执行清单。

材料：050 source-conditioned memo/style failure；051 internal workflow/source-process framing；052 bounded reader-facing closure 作为防回归正例；054 Deep Research F1/F2；future-work、internal path 与真正 reproducibility path 的成对案例；必要英文与普通英文脚手架的成对案例。

检查：自然中文、简繁体目标、必要英文、信息取舍、source future work 的主体/时态/语气、内部 audit/executor/project voice、无关路径/别名/来源过程是否进入正文。

禁止用禁词、English count、script count 作为 PASS 代理。

### G6 — 完整长文、结构连贯与真实 render

证明一整篇长文真正成立，而不是局部段落全部 PASS 后拼起来仍像 memo。

已知代表材料：完整 Deep Research + 至少一份独立已曝光长文回归（可使用 054 H3 作为 known regression，不再称 fresh）；053 Cyrillic glyph 缺失作为真实 render regression。

检查：全文目的、章节顺序、定义位置、前后衔接、重复/冲突、main text vs technical note/appendix、future work/limitations/reproducibility placement，以及 Markdown + 实际 PDF/render 可读性。

在最终付费 review 前，必须已有完整 artifact 的独立定性 PASS；render exit code/file existence 不能代替人工/模型实际阅读。

### G7 — Fresh generalization

candidate 与 rubric 冻结后，使用 **exactly 3 个** 新的 public-safe holdout。数量 3 是为了覆盖三个不同风险族，而不是机械继承 054：

1. noisy technical material，并含 legitimate code 或 reproduction token；
2. 公式/表格等结构化技术内容；
3. 较长文档，并含 future-work/limitation/attribution 或明显 reader-relevance 取舍。

三项可以同时覆盖其他能力，但必须分别有独立主要风险。不得使用 050–054 已曝光样本作为 fresh。

fresh source 的具体内容不得在开发期用于调 production。pre-final Critic PASS 后先冻结 final candidate，再由独立 fresh-source selection/freeze 步骤完成 source completeness preflight、来源/哈希/任务说明与完整 3-item manifest。看到 candidate output 后不得换题、补赢家或新增第 4 项。任何 production 改动都会使该批次失去 unseen release-proof 身份。

### G8 — 同一 final candidate 的 production certification + 独立定性复核

所有 release-critical evidence 必须绑定同一个 final plugin candidate。最终需要：

- exact candidate commit + generated plugin payload/hash；
- G1–G6 的 final-candidate regression evidence；
- G7 frozen fresh batch PASS；
- exactly 1 次最终 `gpt-5.6-terra` Text Review 或经独立 Critic 裁定其 rubric finding；
- final zero-paid release CI；
- bounded production install/upgrade smoke + restore；
- final GPT Reviewer/Reviewed Handoff review；
- 用户 final artifact `ACCEPT`；
- latest-main integration，且 final plugin payload 不发生变化。

不同 candidate 的 PASS 不得拼接。若最终 candidate 改变，旧 fresh 与旧 final review 不能继续作为 unseen/final release proof。

## 5. Reviewer / Terra rubric

所有定性 finding 必须先归入：

- **A — source fidelity**：硬 blocker。Reviewer 必须能看到 source + candidate；检查遗漏、新增、条件/否定/数量/归因/引用/结构化对象及 disposition 一致性。
- **B — reader-facing quality**：硬 blocker。Reviewer 直接读 candidate/render；检查自包含、自然中文、全文连贯、内部过程泄漏、future-work voice、code/path/config placement 与 render 可读性。
- **C — external factual truth**：默认非 Clear Writing blocker。本任务不授权自动 fact-check。只有 candidate 相比 source 新增/强化/错误归因时，转成 A；否则记录 source-quality warning，不偷偷改正文。

特殊规则：

- 合法代码不能仅因是 code 而 blocker；
- path/config 要按 reader/reproducibility role 判断；
- source future work/limitation 必须保留真实 modality，不能被改成已完成结果，也不能写成 Executor action list；
- source 自带的外部事实问题不自动算 rewrite defect。

任何 blocking finding 必须给出：维度 A/B/C、对应 Gate/冻结要求、candidate 精确位置；A 还需 source 位置；违反理由；初步归因；最小关闭条件。无法回指冻结 requirement 的观察只能 advisory。

最终 Terra Text Review 的主要职责是独立验证 B，并检查其可见 packet 内的 contract-compatible structured content；不得临场把 C 变成 blocker。A 的 source-aware独立验证由 pre-final Critic / final GPT Reviewer 对同一 final candidate 完成。

## 6. 执行顺序

严格按以下顺序，不允许把 final paid review 提前：

1. **Bootstrap**：latest-main preflight；创建 exact branch/worktree/task control；读取 approved package/current source/必要历史 evidence；不重新设计。
2. **Implementation + known regression**：只在已知 050–054 failures 与新增 should-keep/should-drop regression 上迭代；完成 G1–G5 的开发检查。
3. **Representative whole-artifact**：生成完整 Deep Research 与另一独立已曝光长文回归，实际 render，完成 G6；允许在这一阶段返修。
4. **Pre-final independent Critic**：Executor 将 source、candidate、render、G1–G6 evidence、rubric、candidate diff 与 proposed fresh categories 形成 repo evidence packet并 commit/push；停止等待 Critic。Critic 必须实际读代表性全文/render；PASS 前不得进入 fresh。
5. **Final candidate freeze**：吸收 Critic 非架构性修复后重新跑受影响 G1–G6；reconcile latest main；完成 source/generated parity、plugin version/changelog closure；冻结 exact candidate commit、plugin payload hash、rubric 与 reviewer packet。若 Critic 要求改变架构/范围/关键验收，返回 Planner + Critic，而不是 Executor 自行改。
6. **Fresh freeze + G7**：冻结 3-item public-safe manifest，再第一次生成 outputs；不允许 production tuning。
7. **Fresh attribution**：全部 PASS 才继续；任何 finding 先分类 product/source/reviewer/environment/workflow。真实 product failure 立即停止 final certification。
8. **Final independent review**：同一 final candidate 上执行最多 1 次 Terra Text Review；如存在 reviewer/rubric 争议，保留原 review，交独立 Critic adjudication，不伪造新模型 PASS、不自动发第二次 paid review。
9. **Final release closure**：Terra/合法 adjudication PASS 后，执行 release CI、bounded production install/upgrade smoke + restore、final GPT Reviewer。全部 PASS 后给用户 final artifact/acceptance dossier；只有用户 `ACCEPT` 后才能集成 main。
10. **Integration**：ordinary non-force integration/push。若 main 自 freeze 后出现影响 Clear Writing、generated payload、candidate replay、review/release policy 或 versioning 的重叠变化，停止并回 Planner/Critic；不得通过 force/rebase-history rewrite 绕过。若仅无关 main drift，允许普通 merge，但必须验证 final plugin payload/hash 与已认证 candidate 完全一致并重新跑必要 zero-paid integration CI。

## 7. Paid Terra contract（只有用户发送获批 kickoff 后才授权）

本 execution package 本身不产生付费授权。用户实际发送 Critic 批准后的 kickoff 时，才授权以下 bounded paid scope：

- provider: OpenAI API；
- model: `gpt-5.6-terra`；
- purpose: final candidate independent Text Review only；不参与 generation、planning、repair、assembly 或 intermediate audit；
- preflight endpoint: `POST /v1/responses/input_tokens`；
- paid endpoint: `POST /v1/responses`；
- `store=false`，`service_tier=default`，low reasoning，`max_output_tokens<=4096`，paid tools = none；
- max paid model calls: **1**；automatic paid retries: **0**；
- per-call worst-case ceiling: **USD 0.25**；campaign reserved-cost hard ceiling: **USD 0.25**；
- credential: existing GitHub Actions secret `OPENAI_REVIEW_API_KEY` only；不得读取/回显 secret，不得复制到本地、新账户或新 secret；不得 fallback 到 `OPENAI_VISUAL_REVIEW_API_KEY`；
- review packet: final candidate-only text + audience + frozen A/B/C-compatible rubric；可包含本任务生成的 private Deep Research **final candidate text**，但不得发送 private source、Meaning Map、Reader Plan、intermediate draft/self-audit、repo logs/credentials；public-safe fresh candidate text可以同包发送；
- 若完整冻结 packet 在 preflight 下超过 USD 0.25，不得拆成第二次调用或静默删关键材料，必须 fail closed 并回 Planner/用户；
- 已发送/已消费的 paid call 不因 REVISE 或 task restart 重置；pre-request 且可证明 `/v1/responses` 未发送的 deterministic/infrastructure failure，可按现行 paid policy 在同一未消费授权下恢复。

## 8. Private artifact / candidate replay / CI / production smoke 授权边界

只有用户实际发送获批 kickoff 后，当前 task 才获得以下授权：

### Private artifacts

只读历史范围：

- `private/exports/054_clear_writing_release_closure/inputs/`
- `private/exports/054_clear_writing_release_closure/deep_research_attempt1/`

本任务可写范围：

- `private/exports/055_clear_writing_release_convergence/`
- task-local ignored `.local-runtime/` replay outputs

用途仅限 known regression、representative whole-artifact generation/render、pre-final Critic evidence 与最终 acceptance。private plaintext、PDF、intermediate、JSONL、credentials 不得 commit/push；需要长期留存但不宜上传的最终用户文件留在上述 repo-local `private/exports/055.../`。

### Candidate replay

允许按 `docs/workflows/CANDIDATE_PLUGIN_REPLAY.md` 使用 repo-local pinned runtime、existing Codex account/CODEX_HOME、temporary `@ai-skills-candidate` identity、fresh ephemeral session 与 finally cleanup。不得复制 `auth.json`、不得升级 global Codex、不得覆盖 `writing-style@yuukias-ai-skills` live identity。

### CI

允许运行本任务相关 focused tests、full zero-paid tests/CI、generated parity、render QA、Marketplace/release CI。普通 push 不得触发付费 review；paid Terra 必须 explicit/manual dispatch。

### Production install/smoke

最终阶段允许一次 bounded `writing-style@yuukias-ai-skills` install/upgrade smoke：开始前记录当前 marketplace/plugin identity+enabled state，安装 exact final candidate/release identity，fresh session 用普通 prompt 验证，结束后无论 PASS/FAIL 都恢复原 live state。不得改其他 plugin/profile，不得 global Codex upgrade，不得扩成长期 live deployment。

### Git

允许 exact branch/worktree 上 ordinary commit、fetch、merge latest main、non-force push、remote handoff；最终所有 Gate + Reviewer + 用户 ACCEPT 后允许 conflict-free/non-force main integration。禁止 force push、hard reset/clean 导致未保存内容丢失、历史改写、删除其他 branch/worktree、绕过保护或用 destructive Git 解决冲突。

## 9. Failure attribution / recovery

- **known/pre-final product defect**：允许在 final freeze 前正常修复，并重跑受影响 G1–G6；不消耗 fresh 身份或 paid call。
- **pre-final Critic 发现 rubric/contract mismatch**：先修合同实现或 reviewer packet；若要求改变已批准 architecture/范围/关键 Gate，回 Planner/Critic 复审。
- **fresh real product failure**：final candidate certification 失败；该 fresh item 永久降级为 known regression。当前 package 不授权修改 candidate 后再建第二 fresh batch，也不自动建 successor。
- **fresh source defect**：保留原证据，停止；不得看过 output 后静默替换 source。需要 replacement/new batch 时回 Planner/Critic/用户。
- **reviewer rubric defect**：保留原 finding/review，由独立 Critic adjudicate；不得删除原 review或伪造新的模型 PASS。
- **environment/infrastructure defect**：只有 candidate/source/rubric 未变且问题确属环境时，按现有合法恢复路径继续；不能写成 product PASS/FAIL。
- **Terra real product defect**：final candidate FAIL；不自动 repair+第二次 Terra，不重置 campaign，不创建 successor。回 Planner/用户决定新 certification scope。
- **paid pre-request failure**：按 paid policy 判断是否真正未发送；未发送且未消费可在同一授权内恢复，已发送则不能当作未消费。
- **production smoke restore failure**：安全 blocker，立即停止；不得 integration。
- **main drift**：无关 drift 可在验证 payload/hash 不变后普通集成；任何 release-critical overlap 都回 Planner/Critic。

## 10. Version / changelog / release identity

当前 package 编写时 main 为 repository `5.0.4`，`writing-style` 为 `0.2`。若执行时未发生相关 release，目标 plugin release 为 `0.3`，repository release 预期为 `5.0.5`。

正式 candidate freeze 前必须按 `PLUGIN_VERSIONING_AND_CHANGELOGS.md`：

- `writing-style` version 对本次已验证 user-visible improvement **exactly bump once**；
- 更新 `docs/plugin-changelogs/writing-style.md` 与 generated Marketplace/plugin payload；
- source/generated parity PASS；
- root repository version/changelog 作为同一正式 release closure 处理。

若 task 启动/集成前 concurrent main 已改变 current repository/plugin version，不得盲目写死 `5.0.5/0.3`；按 canonical version policy 机械计算下一合法版本，并在 pre-final Critic/final freeze 前固定。若 concurrent change 已触及 `writing-style` production behavior，则不是机械改号，必须回 Planner/Critic。

本任务不提升 `docs/PLUGIN_MATURITY.md` 状态；maturity promotion 是 non-goal。

## 11. Non-goals / 明确禁止

- 不改 Bridge Kit、Host Policy、execpolicy；
- 不重做 Proposal v0.1 architecture；
- 不新增 top-level plugin、runtime、daemon、queue、state machine、schema/ledger；
- 不把 Research Authoring 并入 Clear Writing；
- 不默认联网 fact-check；
- 不把 Vale/Pandoc/外部框架引入 production dependency；
- 不新增大规模 corpus/资源摄取；
- 不用禁词/regex/sample-specific 特判换 PASS；
- 不修改 050–054 历史证据或把暴露样本重新称 fresh；
- 不自动创建 056/下一 successor；
- 不进行第二次 paid Terra、不扩大 cost/provider/data/credential/live-global scope；
- 不 force/destructive Git；
- 不把 tests/CI/receipt/hash/file existence 当作语言质量或产品总体 PASS。

## 12. 完成定义

`055` 只有在同一 final candidate 上 G1–G8 全部满足、所有 hard finding 已合法关闭、final release CI 和 production smoke PASS、final GPT Reviewer PASS、用户对最终 artifact 明确 `ACCEPT`、并完成 non-force main integration 后，才可报告 release task 完成。

任何局部 PASS、pre-final Critic PASS、fresh PASS、Terra PASS、CI PASS 或 branch push 都不是总体完成。
