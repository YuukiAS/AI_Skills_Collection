---
schema: AI_BRIDGE_REVIEWED_PLAN_V2
task_key: documents-media--pdf-save-as-delivery
decision: PLAN_FROZEN
---

# Reviewed Handoff Plan — PDF 首次回复直接交付可另存为成品

## Objective and value

只实施已经通过独立 Critic 的小范围修复：`render-chinese-math-pdf` 在 PDF 渲染与质量检查成功后，正常用户的**第一次完成回复**就直接提供当前宿主可打开、可另存为的最终 PDF；用户不再需要追加一句“PDF 呢”。

批准依据保持不变：

- Proposal：`docs/design/pdf-artifact-delivery/PDF_SAVE_AS_DELIVERY_PROPOSAL_V0_1.md`
- Goal：`docs/goals/DOCUMENTS_MEDIA_PDF_SAVE_AS_DELIVERY_GOAL_V0_1.md`
- Kickoff：`docs/operations/prompts/PDF_SAVE_AS_DELIVERY_KICKOFF_DRAFT_V0_1.md`
- 冻结三文件内容：设计分支提交 `da6063bedb8db4779347fc08f9ae1875da2dd115`
- 设计分支后续 `2f04291c0d802a010836b955d3b6167cb235be78` 只追加 Critic prompt；不能把该 prompt 当作 verdict
- 独立 Critic 的 `EXECUTION_READY PASS` 由用户在当前 Planner 线程明确转交；本 Plan 不伪造独立 review 文件
- CI 基线恢复 Proposal：`results/documents-media--pdf-save-as-delivery/PLANNER_CI_BASELINE_RECOVERY_PROPOSAL_V0_1.md` @ `1480b6c8da3aff96707a7f898f19981ce0b2f304`
- 该恢复 Proposal 的 `RECOVERY_ACCEPTANCE_REVIEW` 已由用户转交独立 Critic `PASS`；批准范围只允许用唯一一次 Plan revision 改写 CI 验收语义，不改变 PDF 产品、D1–D3、隐私、版本意图或其他 owner

任务身份：

```text
repo = YuukiAS/AI_Skills_Collection
task_key = documents-media--pdf-save-as-delivery
branch = reviewed/documents-media--pdf-save-as-delivery
worktree = /overflow/htzhu/mingcheng_new/AI_Skills_Collection-documents-media--pdf-save-as-delivery
base_branch = main
base_commit = 1c59199f88c7527f2bd853e606f20146134fda47
```

当前预检已经证明当前客户端存在真实文件入口：用户明确确认基线 `probe.pdf` 可以打开、另存为。因此不要再重复探测“这个客户端有没有文件入口”，也不要新增上传服务。基线探针只证明交付通道存在，不是修复后的 D1 最终候选 PASS。

Feedback promotion decision：`PROMOTE_NOW`。理由是用户明确确认这是长期跨项目偏好，真实失败已经出现，owner、适用边界和 D1–D3 回归均已冻结。canonical TODO 的维护状态/追踪编号在正式维护收口时按现行看板规则更新，不由 Executor 擅自创造第二套状态。

Maintenance companion：`ai-skills-core`  
Domain owner：`render-chinese-math-pdf`

## Frozen decisions

1. **Owner 不变**：问题属于 `render-chinese-math-pdf` 的最终用户交付，不属于 `slurm-workflows`。
2. **不改 PDF 制作架构**：保留 Pandoc AST → LaTeX → XeLaTeX、现有字体、公式、模板、项目渲染 authority 和完整 PDF QA。
3. **复用当前已证实可用的文件入口**：优先使用当前 Codex 客户端已经被用户确认可以打开/另存为的正常文件链接/文件入口；不得新增公共上传服务、第三方网盘、伪 `sandbox:` URL 或跨插件文件基础设施。
4. **首次完成回复即交付**：渲染成功只表示 renderer 完成；面向用户的任务只有在第一次完成回复中给出最终 PDF 的真实可取用入口时，才可声称“已交付”。
5. **失败必须诚实**：文件不存在、不可读、宿主入口不可用、权限不足或交付失败时，可以保留 renderer 成功事实，但必须明确“交付未完成”；不得把服务器绝对路径、receipt、哈希、预览图或 `queued` 状态冒充成已交付。
6. **最小 production 修复**：优先修改正式 skill 的完成/交付合同、检查清单和直接必要的回归。只有真实证据证明现有 renderer receipt 无法维持最终文件身份时，才允许在 renderer 范围做最小身份核验；不得借机重写 renderer。
7. **无跨 owner 扩项**：若真实实现证明必须修改 Codex App、Bridge Kit、跨插件 shared runtime、外部传输平台或新的权限/数据边界，停止当前实现并返回 Planner；本 Plan 不授权这些改动。
8. **不重复要求用户确认通道**：当前 `probe.pdf` 的用户确认已经关闭“本客户端是否存在可另存为入口”的前置未知。最终候选仍必须自己在第一次完成回复中使用同一已确认通道，并绑定最终 PDF 身份，但无需再次让用户回答“能不能下载”才能继续普通实现。
9. **Reviewer 可以人工交接**：本任务需要独立 Reviewer 对真实最终候选和 D1–D3 证据判定；不存在 task-bound 自动 Reviewer 时，采用完整人工交接，不新增长期自动化，也不把 generic watcher 冒充 Reviewer。
10. **用户参与边界**：除非合法进入 `AWAIT_HUMAN_DECISION` 或真实 `BLOCKED`，普通实现、回归、CI、Reviewer 交接和同范围修复不再要求用户重复决策。
11. **唯一恢复修订已冻结**：本次 `plan_revision: 0 -> 1` 只把“仓库全绿”改成获批的 current-main-vs-final-candidate 广义差分回归门。`REVIEW_1`、`review_round=1`、D1/D2/D3、implementation commit、最终 PDF 身份和产品代码均保持历史不变。
12. **旧 CI 事实不可改写**：GitHub Actions run `38706208966` 永久保留为 `FAIL` 证据。它证明当时仓库级工作流为红，不得在任何报告中重标为 PASS；本恢复只改变后续如何判断本 PDF 候选是否新增仓库回归。
13. **D1 finding 只由新证据关闭**：`results/documents-media--pdf-save-as-delivery/D1_DELIVERY_EVENT.md` 是 REVIEW_1 finding 2 的新增证据。没有新的相反证据时，不重新渲染、不重新修改产品，也不要求用户再次证明同一宿主文件入口可另存。

## Positive completion

同一个最终候选只有在以下全部成立时才完成：

1. 正常安装/加载该最终候选后，用户以自然语言请求生成一份公开安全的中英/数学 PDF。
2. renderer 通过原有 PDF 质量检查。
3. **第一次完成回复**直接包含最终 PDF 的当前宿主真实文件入口；该入口对应本次已通过 QA 的最终 PDF，而不是基线 `probe.pdf`、旧候选、预览图或仅服务器路径。
4. 最终候选的交付证据能够把回复中的文件入口与已验收 PDF 的路径/大小/必要哈希或等价身份信息绑定。当前客户端通道的“可以打开/另存为”能力已由用户基线确认，不要求重复索取同一人类确认。
5. D2 的受控失败用例证明：当最终文件不可读取/不可通过合法入口交付时，首次回复不虚构下载链接、不声称已交付、不做未经授权外传，并给出真实最小恢复信息。
6. D3 证明现有 Markdown、直接 `.tex`、数学、中文字体、项目模板、render receipt 和非 PDF 边界没有被本次交付修复破坏。
7. 冻结候选后的仓库级回归必须满足本 Plan 的“仓库基线差分回归门”：执行前立即刷新并绑定 then-current `main`；如果该 main 已经全绿，优先使用更强的普通 all-green CI；否则 current main 与 exact final candidate 必须在同一环境、同一命令下比较，候选不得新增或恶化任何全仓失败或 generated/publication 差异。
8. 独立 Reviewer 实际读取最终候选的交付证据、相关 PDF/渲染身份、D1–D3 结果和仓库基线差分证据后给 PASS；只有 tests、旧 CI、字符串存在、路径名或失败数量不能代替产品/回归 PASS。
9. `REVIEW_2` 必须把“bounded PDF product/reviewer acceptance”和“repository integration/release closure”分开判断；Reviewer PASS 只能说明本 PDF 候选满足冻结能力和差分回归门，不能声称 current-main 的既有基线债已经修复。
10. 若确实形成 production user-facing behavior change并准备正式发布，完成 standalone skill 版本、README/CHANGELOG 及维护看板/source backlink 的合法收口；integration/release 时重新读取 then-current main、版本政策、CHANGELOG、Issue #101 与仓库基线。无关 owner 的 release prerequisite 仍红时，由其 owner 处理，本 PDF task 不越界修复，也不得声称已解决。

最大允许声明：

> 当前已验证宿主中的 `render-chinese-math-pdf` 最终候选能够在 PDF 渲染和检查完成后的第一次完成回复中直接交付可另存为的最终 PDF，并在不能合法交付时如实失败，同时保持原渲染质量与调用兼容。

不得外推为所有 ChatGPT/Codex 客户端、所有远程环境或任意第三方文件传输都已支持。

## Non-substitutable semantics

- “PDF 文件存在”不是 D1。
- renderer `receipt.status=complete` 不是用户交付完成。
- 服务器绝对路径、SHA-256、测试 PASS、截图、PNG 预览或 `open_in_codex=queued` 不能替代第一次回复中的真实文件入口。
- 第二次追问后才出现文件仍然是 D1 FAIL。
- 基线 `probe.pdf` 证明当前客户端通道存在，但不能替代修复后最终候选 D1。
- 不能通过换成 Chromium/browser PDF、图片、手工附件或降低字体/公式/模板质量来换取交付 PASS。
- 不得读取或外传 CAT-TRACE 私有论文/数据来完成回归；使用公开安全/任务自建的非敏感 fixture。
- 不能新增公网下载 URL、云盘、外部 API、付费模型、Slurm 作业/GPU 或新的 credential。
- 如果正常宿主最终证明不能让正式 skill 使用现有文件入口，必须停止并回 Planner；“只改 SKILL.md 后测试字符串存在”不能冒充解决。
- 不能把 `38706208966` 从 FAIL 改写为 PASS，也不能用“忽略 CI”作为恢复理由。
- 差分回归不能只比较 test ID、文件路径或数量；必须保留足以判断同一 failure 是否变严重的精确 assertion diagnostics 与 generated/publication difference records。
- 若候选使继承自 main 的同一个 failing assertion / generated difference 发生候选侧恶化，即使 test ID 或 path 没变，也属于 candidate-caused regression，必须阻断。
- current main 自身已有的无关失败可以保持未修复，但候选不得新增、扩大或隐藏它们；“和坏 baseline 一样坏”只有在精确诊断完全无候选侧恶化时才可作为 no-new-regression 证据。

## Implementation scope

优先且预期只修改：

- `skills/tools/documents-media/render-chinese-math-pdf/SKILL.md`
  - 明确区分 renderer complete 与 user delivery complete；
  - 冻结首次完成回复直接提供最终 PDF 的正常行为；
  - 冻结无法合法交付时的诚实失败语义。
- `skills/tools/documents-media/render-chinese-math-pdf/references/checklists.md`
  - 在最终交付检查中加入真实可取用成品、最终文件身份和失败语义。
- `tests/test_render_chinese_math_pdf.py` 或同一既有测试面中的直接必要回归
  - 保护新的完成/交付合同和原有 renderer 行为；
  - 机械测试仅作为回归，不得替代 D1/D2 真实入口证据。

只有必要且有直接证据时允许：

- `skills/tools/documents-media/render-chinese-math-pdf/scripts/render_scientific_pdf.py`
  - 仅用于维持最终交付文件身份所必需的最小 receipt/identity 信息；
  - 不改变 Pandoc/XeLaTeX 路线、排版语义、字体或 QA owner。

恢复执行新增唯一 evidence artifact：

- `results/documents-media--pdf-save-as-delivery/CI_BASELINE_DIFFERENTIAL.md`
  - 绑定 then-current main SHA 与 exact final candidate SHA；
  - 记录两边完全相同的命令、环境与依赖；
  - 记录两边 full-suite failure sets 以及每项精确 assertion diagnostics；
  - 记录两边 generated/publication difference sets 及其详细差异；
  - 明确计算 candidate-minus-main 的新增/恶化 delta；
  - 任何 candidate-only failure、candidate-caused diagnostic worsening 或 generated/publication worsening 均 FAIL。

该文件是仓库级差分回归证据，不是新的产品实现层，也不允许修改其他 owner 只为追绿。

维护与正式发布收口可以按当时最新 main 更新：

- `docs/skill-todos/render-chinese-math-pdf.md`
- `CHANGELOG.md`
- `README.md`
- standalone skill 自身版本字段及现有版本/registry/catalog 派生面（只通过现有生成/验证入口，不手改生成层）。

不得修改中央 Marketplace plugin 行为；所有中央 plugin 版本 `NO_BUMP`。

版本冻结：

```text
Repository bump decision: NONE during recovery execution
Reason: 当前先完成并验证 standalone skill production change；不提前制造 repository release。
Affected central plugins:
- all: NO_BUMP
Standalone skill:
- render-chinese-math-pdf: 0.2 -> 0.3 only if D1-D3 + independent review + release closure pass
```

当前 `main` 的 `CHANGELOG.md -> Unreleased` 已有其他任务声明“下一正式 repository release 为 MINOR”。本任务自身只属于兼容改进，不产生新的 repository minor。正式发布时必须重新读取当时 `VERSION` / `CHANGELOG`：
- 若那个已批准的 MINOR 仍是下一正式 release，则把本 skill 的 `0.3` 改进纳入同一次 release，不额外制造 `5.4.5`；
- 若该 MINOR 已先行发布，则本任务后续独立正式 release按当时最新版本做普通 PATCH。
这只是版本算术，不改变本任务产品范围。

维护看板不是实施前 blocker，但正式 release closure 前必须按当前政策真实同步。现阶段没有匹配的 tracking Issue；不要虚构编号。具有真实 Clear Writing + Project mutation 能力的维护动作应查重后创建/绑定 Issue、设置正确 Area/Status，并回填 canonical TODO 的 `tracking: #N`；否则保留精确待同步动作并不得称看板已同步。

## Acceptance and regression gates

### 仓库基线差分回归门（流程/发布回归门，不新增 D4）

本门只替换旧的“repository required CI 必须绝对全绿”条件；D1–D3 不变。

执行规则：

1. **比较前立即刷新并冻结基线**：用仓库正常只读/同步入口刷新 then-current `main`，记录 exact main SHA；不能沿用 Critic 审查时的旧 SHA 假装仍是当前基线。
2. **强路线优先**：如果 then-current main 在相同 full-suite / generated-publication 检查下已经全绿，则不用差分例外；把 exact final candidate 安全对齐到已修复基线所允许的范围并走普通 all-green CI，仍不得改 PDF 产品语义。
3. **否则执行同环境差分**：current main 与 exact final candidate 使用同一运行环境、相同依赖和相同命令。不要只复用旧 run 摘要。
4. **PDF/standalone target tests 必须 PASS**：候选自己的目标回归继续是硬门槛。
5. **保留平台 smoke**：现有 Windows/Linux editable-install smoke 与 Windows sparse-checkout PASS 可以复用，前提是最终候选身份及这些 surface 未变化；若候选/相关 surface 变化则刷新对应 smoke。
6. **full-suite 不得新增或恶化**：记录 main 与 candidate 的完整 failing test IDs、精确 assertion diagnostics、traceback/expected-vs-actual 等足以比较严重度的内容。candidate-only failure = FAIL；同一 test ID 但候选 assertion/difference 更坏 = FAIL。
7. **generated/publication 不得新增或恶化**：两边分别记录 publication/generated difference path 与实际 difference 内容；candidate-only difference 或同路径候选侧扩大 = FAIL。
8. **禁止机械代理**：仅比较 test IDs、path names、失败数量、exit code 或“都是 4 个失败”不能 PASS。
9. **差分证据文件**：写入 `results/documents-media--pdf-save-as-delivery/CI_BASELINE_DIFFERENTIAL.md`，至少包含 main SHA、candidate SHA、commands/environment、两边 failure sets + diagnostics、两边 generated/publication differences、candidate-minus-main delta 和结论。
10. **旧 CI 不改写**：run `38706208966` 保持 FAIL。它和三个成功 platform jobs继续作为历史过程证据。
11. **不修无关 owner**：不得为了差分 PASS 修改 Presentations、Research Authoring、publication baseline、Bridge Kit、Slurm 或其他 plugin。
12. **差分 PASS 后才进入 REVIEW_2**：同一最终候选进入第二轮独立 Reviewer。若差分 FAIL，只允许修本任务引入的 candidate regression；如果修复需要越出冻结 scope，返回 Planner/用户，不开 successor。
13. **review budget 不重置**：`REVIEW_1` 保留，下一次正式 implementation review 是 `REVIEW_2`，不存在第三轮。
14. **integration/release 单独收口**：REVIEW_2 可以对 bounded PDF product/reviewer acceptance 给 PASS，但不能宣称 current-main 既有 repository baseline debt 已修复。后续 merge/release 前重新核对 then-current main、版本政策、CHANGELOG、Issue #101 和 release prerequisites；无关 debt 由其 owner 处理。


### D1 — 第一次完成回复直接提供最终 PDF

正常入口：

- 使用实际安装/加载的最终候选；
- 自然语言请求公开安全的中英/数学 PDF；
- 不在提示词中要求“再给我附件”或点名内部实现。

PASS：

- renderer QA 通过；
- 第一次完成回复中直接出现当前已验证宿主可取用的最终 PDF 文件入口；
- 文件入口绑定本次最终候选的真实 PDF identity；
- 不需要第二次用户追问。

FAIL：

- 只给服务器路径、receipt、hash、预览图；
- 文件入口指向错误/旧 PDF；
- 第二次追问后才提供；
- 依赖手工把另一个 PDF 冒充本次最终产物。

基线 `probe.pdf` 只证明当前客户端的文件入口确实可打开/另存为；不能作为最终候选 D1 PASS。

### D2 — 交付不可用时诚实失败

用公开安全、可恢复的受控失败场景验证最终候选：最终 PDF 不存在、不可读或当前合法文件入口不能取得时，不允许把 renderer/路径状态包装成“已交付”。

PASS：

- 明确区分“PDF 渲染/产生状态”和“用户交付状态”；
- 不生成伪链接、不未经授权外传；
- 给出真实最小恢复信息；
- 不需要用户猜服务器路径。

机械测试可以辅助证明分支逻辑，但 D2 必须至少包含一次正常用户响应路径的受控失败证据。

### D3 — 原有能力不退化

至少覆盖：

- canonical Markdown → Pandoc/XeLaTeX；
- direct `.tex`；
- 中英文、公式、表格和字体 QA；
- project-owned render contract / profile authority 不被覆盖；
- receipt 兼容；
- 非 PDF 请求不因新交付规则误触发；
- 现有相关单元测试和必要仓库验证。

如 `render_scientific_pdf.py` 未改，不为了形式重复制造新的 renderer 测试；但最终候选仍须通过已有相关回归。

### 阶段顺序

1. 已完成：基线通道确认、最小 production change、候选冻结、D1–D3 证据与首次完成回复真实交付；没有新 contrary evidence 时不重新生成或修改 PDF 产品。
2. 立即刷新 then-current `main` 并执行上面的仓库基线判断。
3. main 已全绿：采用更强的 ordinary all-green CI；main 仍红：执行同环境 main-vs-candidate broad differential gate。
4. 写入并自检 `CI_BASELINE_DIFFERENTIAL.md`；任何候选新增/恶化 FAIL 都先阻断。
5. 差分/普通 all-green 路线 PASS 后，保持同一 final candidate 进入 `REVIEW_2`。Reviewer 重新检查 D1 delivery event、D2/D3 和仓库回归证据，不重新设计产品。
6. `REVIEW_2 PASS` 只证明 bounded PDF product/reviewer acceptance；不得声称 current-main 无关基线债已修复。
7. Reviewer PASS 后再处理必要的版本/README/CHANGELOG/maintenance/integration closure；如 release-facing 文件本身改变 final candidate，按风险重跑受影响的一致性检查。
8. integration/release 时重新读取 then-current main、版本政策、CHANGELOG、Issue #101 和仓库基线。无关 repository release prerequisite 若仍红，交其 owner，不让本 PDF task 越界修复。
9. 无冻结的人类产品选择时，不因为缺 task-bound 自动 Reviewer 就停住；人工交接 Reviewer 即可。
10. 不创建 successor、不新增第三轮 Reviewer。

## Natural-language usage / routing expectations

正常用户只需提出类似：

> 把这份中英文数学 Markdown 渲染成正式 PDF。

正确体验：

1. skill 完成原有渲染和 QA；
2. 第一次完成回复直接显示最终 PDF 文件入口；
3. 用户可以直接打开/另存为，不需要再问“PDF 呢”。

如果合法交付入口不可用，正确回复应直接说明“PDF 已生成，但当前未完成用户文件交付”，而不是只扔服务器路径或虚构链接。

## Out of scope

本任务不得：

- 新建 Proposal/Goal/Kickoff v0.2 或重新设计已批准方向；
- 修改 Bridge Kit、Reviewed Handoff schema/role/watcher 或新建 Planner/Reviewer 自动化；
- 修改 `slurm-workflows` 业务源码、提交/取消 Slurm 作业或申请 GPU；
- 修改 Research Authoring 的文稿语义、其他中央 plugin routing 或 Marketplace 拓扑；
- 新建公共上传服务、第三方下载站、云盘同步、数据库、daemon、定时任务或 credential broker；
- 读取/上传 CAT-TRACE 私有论文、私有数据、凭据；
- 调用付费外部 API/model；
- 降级为 Chromium/browser PDF、图片或低质量替代物；
- 把维护看板工具缺失、Planner/Reviewer transport 形式或其他执行手续升级成新的产品 blocker；
- 宣称一次 baseline probe、测试 PASS 或 PDF 文件存在已经完成最终用户交付；
- 在 D1–D3、批准的 ordinary-all-green 或 broad differential regression gate、独立 `REVIEW_2`、版本/维护/集成收口未达到对应声明边界时发布或宣称整体完成；尤其不得把 REVIEW_2 的 bounded PDF PASS 写成“仓库既有 baseline debt 已修复”。
