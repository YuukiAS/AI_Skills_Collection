# AI_Skills_Collection：PIE 0.1 最终验收、main 收口与分支清理 Goal

你现在在 `YuukiAS/AI_Skills_Collection` 做一次**仓库收口与分支卫生整理**。这是已有工作的完成与清理，不开启新的架构设计，不启动新的 Critic，不创建 C12，不实现 Clear Writing 下一版。

用户当前明确决定：

1. Project Instructions Editor（PIE）0.1 还差一次真实 Server+VPS Project 验收；这次**不再把中文自然度、非必要英文、机械换行作为 PIE 0.1 的阻断项**，这些已经转交 Clear Writing 后续版本。
2. PIE 0.1 仍必须在 Server+VPS 真实场景证明：Project-instruction 编辑器本身的语义、来源、授权、安全、证据和有限编辑能力成立。
3. 当前 `main` 看不到 PIE README 更新，是未完成的收口；必须查清并处理。
4. 除当前 PIE 和 Research Authoring 仍在进行的工作外，AI_Skills_Collection 旧任务分支不应长期残留。
5. 不要因为“清分支”丢掉尚未进入 main 的有效 production 改动或必须保留的审查/验收证据；先判定，再整合或归档，最后删分支。

## 0. 当前已核对事实

开始时必须重新 fetch 并验证，不得盲信下面 SHA；它们只是本 Goal 写入时的锚点。

写入 Goal 时：

```text
main = d437b90f880f47c92331a3f12a0d096e44e2f4bd
release = 06d135d8a6ee62cd41abb40fc5771fcef7f8db25
PIE closure branch = work/project-instructions-editor--0.1-closure
PIE closure tip = 12ce72e790b9bae802830e9a9b010178c0b0e16d
PIE source commit = 47f3a2d9caec295955040d90cfb19c0f4d3bf7a8
old PIE C11 stop branch = work/project-instructions-editor--standalone-skill-implementation
C11 stop = 1325ffba51be6ecbe46cde7e46492f9e69284c4c
```

当前 `main` 仍显示：

```text
Repository / CLI release: 5.4.4
```

而 PIE closure branch 才包含：

- Project Instructions Editor v0.1 README 项；
- 新 SVG icon；
- PIE source / registry / catalog / provenance / contact sheet；
- `VERSION=5.5.0` 和 5.5.0 changelog 候选。

因此上轮所谓“同步”只完成了任务分支，不是 main/release 集成。不要再用“已同步”描述 main。

PIE closure 分支当前相对 main 已经 diverged；写入 Goal 时是 ahead 3 / behind 6，merge-base 为 `260d160...`。main 后续 6 个提交属于 Research Authoring 当前工作。必须先安全吸收最新 main，不能覆盖 Research Authoring。

## 1. 先读取最小必要合同

实际读取最新 main：

```text
AGENTS.md
docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md
docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md
docs/skill-todos/project-instructions-editor.md
```

以及 PIE closure branch：

```text
skills/core/codex-system/project-instructions-editor/SKILL.md
skills/core/codex-system/project-instructions-editor/references/editor-contract.md
results/project-instructions-editor--standalone-skill-implementation/PIE_0_1_CLOSURE_VALIDATION.md
docs/operations/prompts/PROJECT_INSTRUCTIONS_EDITOR_CHATGPT_PLUGIN_UPDATE.md
```

只为 Server+VPS 验收读取必要的既有真实失败/验收摘要，不重跑 C5–C11 整个旧循环。至少读取：

```text
C5_REAL_USER_ACCEPTANCE_CRITIC_REVIEW.md
C7_G4_REPLAY_CRITIC_REVIEW.md
C11_READER_BASELINE_GATE_CRITIC_REVIEW.md
```

C11 的中文阅读层失败永久保留，不能重新解释成 PASS。

## 2. PIE 0.1：先把候选更新到最新 main，但暂不虚假发布

在 `work/project-instructions-editor--0.1-closure`：

1. 检查工作树干净；
2. fetch 最新 `main`；
3. 安全 merge/rebase 最新 main，使 Research Authoring 当前提交全部保留；
4. 解决冲突时以最新 main 的 Research Authoring / Presentations 等内容为准，只叠加 PIE 自己的变更；
5. 重跑 PIE focused tests、registry/catalog/provenance/icon 校验；
6. 不因为无关 central Plugin drift 修改 Presentations / Research Authoring production behavior。

在真实 Server+VPS 验收通过前，不要把“5.5.0 已正式发布”写成完成事实。可以保留 5.5.0 release candidate，但 release closure 只有验收通过后才能成立。

## 3. ChatGPT Web wrapper 必须先对齐正确 PIE 0.1 source

真实 Server+VPS 验收必须测试最终 PIE 0.1，而不是仍装着旧 C11 payload 的 wrapper。

目标 source：

```text
47f3a2d9caec295955040d90cfb19c0f4d3bf7a8
skills/core/codex-system/project-instructions-editor/
```

按：

```text
docs/operations/prompts/PROJECT_INSTRUCTIONS_EDITOR_CHATGPT_PLUGIN_UPDATE.md
```

准备或执行现有 `skills-only` ChatGPT personal Plugin wrapper 更新。

要求：

- standalone Skill version 仍为 `0.1`；
- wrapper 包版本独立处理，不得把 wrapper 的三段版本冒充 Skill version；
- 包内 `SKILL.md`、`agents/openai.yaml`、icon、evals、editor-contract 必须来自同一最终 source；
- 不包含 MCP finalizer、外部模型、API key、sibling-Skill chain；
- wrapper 只是分发封装，不是第二份能力来源。

若当前 Codex 环境无法直接调用 Plugin Creator：

- 生成一个准确的 wrapper update archive / handoff；
- 给出文件路径、SHA256、source commit 和当前 wrapper → candidate wrapper 的版本差异；
- 然后只提出一次最小用户操作请求，不要反复让用户搬文件；
- 在 wrapper 真正更新之前，不能声称 Server+VPS 验收的是最终 PIE 0.1。

## 4. Server+VPS 最后一次真实验收：只审 PIE 编辑器能力

验收表面必须是普通 ChatGPT Web 的真实 Server+VPS Project，新开 fresh thread，并使用已经更新到最终 0.1 source 的 PIE wrapper。

不要显式写 `@Project Instructions Editor`，不要提示内部 Gate，不要给预期答案，不要提供翻译清单。

建议自然首问：

```text
帮我重新审一下这个 Project 现在的长期 instructions，看有没有还应该调整的地方。只做确实有必要的长期修改，不要重做整个 Project；如果需要改，给我完整可替换版本和简短理由，如果不需要改就说明为什么。不要实际修改账号、网络、服务或远程资源。
```

只能用第一条完整回答判定本轮真实验收；不得第二轮提示后洗成 PASS。

### 本轮明确不作为 PIE 0.1 blocker

以下仅记录并转交 Clear Writing #13，不阻断 PIE：

- 普通英文残留；
- 中文是否足够自然；
- 中英混杂；
- 机械换行；
- 状态腔/日志腔；
- 跨轮阅读层长期稳定性。

不要因此再修改 PIE 规则。

### 本轮必须 PASS 的 PIE 0.1 能力

从真实 Server+VPS 当前 setting、目标历史和 canonical repo 事实逐项审：

1. **编辑模式正确**：已有 live setting 时必须按 preservation-sensitive 处理，不把旧候选当 live baseline。
2. **有限编辑优先**：能 bounded edit / consolidation 就不无理由整体重做；真正 no-op 也必须有成立理由。
3. **no-op 不逃避真实结构缺陷**：若存在与中文无关、可安全修复的 ownership / volatile-detail / placement / duplication 缺陷，不能因为“怕漂移”直接 no-op。
4. **source ownership / locator 正确**：易变机器清单、客户端库存、运行状态等若已有 canonical repo owner，不应长期复制一大份进 Project setting；但 Project 在动作前必须知道的授权、安全、查询触发仍应留直接规则或短桥。
5. **protected absence 正确**：用户已删除/拒绝且 live setting 已不存在的规则，不得仅凭旧 thread/history 复活；也不能把删除历史泛化成新的长期 tombstone 规则。
6. **授权与副作用边界不漂移**：不得把“只读/需授权”改成可直接修改账号、网络、服务、隧道、驱动、远程资源。
7. **隐私边界不漂移**：secret、token、private endpoint 等不得被扩写/回显。
8. **证据强度与 fail-closed 保持**：旧成功、旧日志、source-only/partial evidence 不能冒充当前 live/global PASS；证据不足时结论必须收紧。
9. **mandatory / optional、current / future、完成 / 未完成保持**。
10. **精确标识保持**：repo、路径、命令、字段、状态值、协议/产品/机器身份等需要 exact matching 的字符串不能被改坏。
11. **预算与范围**：如果当前 Project 有实际字符预算或明显冗余，应给合理 bounded consolidation；不能凭历史 8000 字假设通用产品上限。
12. **缺关键输入时诚实降级**：如果模型实际上拿不到足够 live baseline / source / authority，不能假装安全给完整替换。

生成一个新的、非常短的真实验收记录，例如：

```text
results/project-instructions-editor--standalone-skill-implementation/PIE_0_1_SERVER_VPS_NON_READER_ACCEPTANCE.md
```

只记录：
- tested wrapper/source identity；
- exact first user prompt；
- first response locator/transcript evidence；
- 上述 12 项的结论；
- reader-layer issues = OUT_OF_SCOPE_FOR_PIE_0_1 / tracking #13；
- OVERALL = PASS / FAIL。

若任一非阅读层核心能力 FAIL，PIE 0.1 不发布；做最小 bounded repair，不创建 C12，不重新进入中文循环。

## 5. 通过后才正式把 PIE 0.1 集成到 main / release

如果 Server+VPS 非阅读层验收 PASS：

1. 重新跑 focused tests 和直接受影响的 release checks；
2. 无关 current-main central Plugin drift 单独归因，不得拿来阻止一个已经验证通过的 PIE bounded release，也不得顺手修改；
3. 按 `PLUGIN_VERSIONING_AND_CHANGELOGS.md` 确认 repository bump；
4. 如果新 standalone PIE 0.1 确实形成新的 repository-level user capability，保持已规划的 `5.4.4 -> 5.5.0`；否则按政策纠正，不能凭旧分支硬推；
5. merge / integrate PIE 到最新 main；
6. 核实 main 的 README 真实出现 Project Instructions Editor v0.1 和新 SVG icon；
7. 核实 main 的 VERSION / CHANGELOG / registry / catalog / provenance / tests 一致；
8. 按仓库正式发布流程推进 `release` 到同一已验证 release candidate；
9. 更新 Issue #93，只有此时才允许 DONE；
10. 明确记录：
   `C11 reader-layer failure preserved; not reclassified as PASS.`

如果 Server+VPS 非阅读层验收尚未执行或 FAIL：
- main 不得冒充 5.5.0 已发布；
- Issue #93 保持 DOING；
- PIE closure branch 保留为唯一 active PIE branch；
- 但仍继续完成下面的无关旧分支清理。

## 6. 系统性清理远端 branches

先：

```bash
git fetch --all --prune
git worktree list --porcelain
git branch -r
```

重新列出所有 remote branches 和 open PR。不要只按本 Goal 的旧列表删。

### 最终允许长期存在的分支

基础：

```text
main
release
```

当前仍在做：

```text
work/project-instructions-editor--0.1-closure
work/research-authoring--formal-production-authoring
work/research-authoring--student-facing-authority-todo
work/research-authoring--table-wrap-readability-todo
```

对 Research Authoring 三个 branch 也做一次真实性检查：如果其中 TODO branch 实际已被 main 吸收或明确结束，可以清理；不要因为名字包含 research-authoring 就机械保留。至少保留真正正在执行的 Research Authoring 主分支。

PIE 0.1 一旦正式合入 main/release，也应删除 closure branch。最终理想状态是只有 main / release + 真正仍 active 的 Research Authoring 分支。

**不要为未来 Clear Writing 工作提前保留一个闲置 branch。需要开始时再从当时最新 main 建。**

### 6.1 可直接删除的“head 已是 main ancestor”分支

写入 Goal 时已经确认以下 branch 对 main 为 `ahead=0`，只落后 main；运行时重新确认后可直接删：

```text
reviewed/hpc--slurm-race-policy-bounded-opt-in
reviewed/hpc--slurm-workflows-routing-refactor
reviewed/product-ui-copy--cross-plugin-production-integration
reviewed/repo--maintenance-board-lifecycle
reviewed/science-communication--project-thread-handoff-recovery-integration
work/workflow-core--normal-entry-reliability
```

删除前仍检查没有 dirty worktree / 未 push local commit。

### 6.2 已完成但 branch 有 main 未包含的独有提交：先判定证据，再删

这些 branch 不能机械删：

```text
reviewed/ai-skills-core--machine-update-orchestration
reviewed/presentations--stage1-front-door-two-template-foundation
reviewed/repo--maintenance-board-issue-maturity
reviewed/science-communication--project-thread-handoff
reviewed/science-communication--project-thread-handoff-recovery
reviewed/workflow-core--first-remote-publication-gate
reviewed/workflow-core--first-remote-publication-repair-gate
work/presentations-validator-v1
work/project-instructions-editor--standalone-skill-implementation
planner/reader-layer-finalization-v0.1
```

统一处理规则：

#### A. 已完成 / 已发布，只剩独有 evidence 或 control files
- 检查 tracking Issue / main / release 是否已经证明任务完成；
- 将仍被 durable closure 引用、但 main 缺失的**必要总结性 evidence**整合进 main；
- 不要把大量临时 stdout、缓存、重复 raw replay、测试工作目录全部塞进 main；
- 保留真正 canonical 的 plan/review/final report/acceptance/closure evidence；
- 然后删除 remote branch 和对应 clean worktree。

#### B. production 改动已被更新实现取代
- 不把旧 implementation 重新 merge；
- 记录 SUPERSEDED / NOT_ADOPTED 的最小 durable evidence（若当前 source 尚未说明）；
- 删除 branch。

#### C. branch 含尚未进入 main、而且仍然是已接受的 production 能力
- 先按当前 main 重新验证；
- 正确集成到 main；
- 再删除 branch。
- 不允许以“清分支”为理由丢 production work。

### 已知具体判断线索

#### `reviewed/ai-skills-core--machine-update-orchestration`
Issue #86 已明确写明中央实现、正式发布、五个 required consumer 和 closure 全部完成。branch 仍有独有 result commits。确认 main 是否缺 Issue #86 仍引用的 final closure evidence；需要的总结证据补进 main 后删除 branch。不要重跑整机验收。

#### `reviewed/product-ui-copy--cross-plugin-production-integration`
branch head 已是 main ancestor，因此 production 已进入 main。删除 branch；顺便核对 Issue #89/#90 是否还错误地把这个已结束 branch 写成当前 DOING anchor。若 main/release 已完成对应 closure，就 truthfully 收口；若更大 TODO 仍在，不关闭能力问题，但必须移除 stale branch anchor。

#### `reviewed/repo--maintenance-board-lifecycle`
Issue #4 已记录 DONE / Resolution commit，branch 是 main ancestor。删除。

#### `reviewed/repo--maintenance-board-issue-maturity`
Issue #4 当前说明 v7 Issue taxonomy/intake 已完成，但 Issue #92 仍可能留着旧“正在 Stage A”文字。核对 main 的 v7 closure evidence；如果真实完成，更新/关闭 #92 并保存必要 final evidence，然后删 branch。

#### Project Thread Handoff 三个 reviewed branches
v0.2 已正式进入 main/release，integration branch 已是 main ancestor。旧 base/recovery branches 如有少量 unique commits，只保留仍被正式 closure 引用的总结 evidence；不得重新 merge 旧 production snapshot。然后三个分支全部删除。

#### Workflow Core 两个 first-remote-publication gate branches
当前各自主要只剩旧 Reviewed Handoff control files。确认对应任务已被后续正式 workflow-core 覆盖/结束；无未合入 production 后删除，不保留“空壳任务分支”。

#### `reviewed/presentations--stage1-front-door-two-template-foundation`
branch 仍有较多旧 production diff。必须比较当前 main 的 Presentations 现状；如果这些改动已经被更新版本/后续工作替代，不 merge 旧 snapshot，记录 superseded 后删；如果仍有 accepted capability 缺失，先整合当前有效部分并走必要测试，再删。

#### `work/presentations-validator-v1`
这是最不能盲删的一个：写入 Goal 时仍有 7 个 main 未包含提交，且包括真实 validator production code 与 auditor findings。
本次必须把它变成一个明确结论，不能继续悬着：
- 若已经被当前 main 的 Presentation workflow 取代 / 未获最终接受：记录 REVIEWED_NOT_ADOPTED 或 SUPERSEDED，保留必要 implementation/auditor evidence，然后删；
- 若它是已经接受、只是忘了合 main 的 production capability：按当前 main 重放测试，正确集成后删。
任务结束时不得继续保留这个 branch 作为“以后再说”。

#### 旧 PIE branch
`work/project-instructions-editor--standalone-skill-implementation` 已被 C11 stop 终止。不要 merge 其 C11 production source。
在删 branch 前，把 Issue #93 / 后续 Clear Writing 设计实际依赖的 canonical failure summaries 保留到 main，至少覆盖：

```text
C5_REAL_USER_ACCEPTANCE_CRITIC_REVIEW.md
C7_G4_REPLAY_CRITIC_REVIEW.md
C9_FINAL_GATE_CRITIC_REVIEW.md
C10_IMPLEMENTATION_CRITIC_REVIEW.md
c10_b3_stage_separation_probe/PROBE_RESULT.md
C11_SIMPLE_FORMAL_CORE_CLOSURE.md
C11_READER_BASELINE_GATE_CRITIC_REVIEW.md
```

如果其中已有等价 durable evidence，可避免重复。不要把整套巨大 replay 临时目录全搬到 main。
然后删除旧 PIE branch，只留 0.1 closure branch直到最终验收完成。

#### Clear Writing reader-layer design branch / PR #100
当前顺序已经改成：
PIE 0.1 收口 -> Clear Writing 下一版 -> 以后 PIE 0.2 薄接入。

因此现在不需要长期占着：
`planner/reader-layer-finalization-v0.1`

处理：
- PR #100 不 merge 为当前 production；
- 在 PR / Issue #13 留一句清楚说明：该设计轮因执行顺序调整暂停，未来从当时最新 main 重新开正式 Clear Writing 轮次；已有研究仍可作参考；
- 关闭 PR #100；
- 删除 branch；
- Issue #13 保留为未来 Clear Writing 工作的 tracking，不把它标 DONE。

## 7. Branch / worktree 删除纪律

对每个删除对象：

1. `git status` 确认对应 worktree clean；
2. 确认没有未 push commit；
3. 对 diverged branch 记录 closure disposition；
4. 需要的 evidence / accepted code 已进入 main；
5. 用正常 Git 删除 remote branch；
6. clean local worktree 用 `git worktree remove`，不要直接 rm；
7. 删除本地 branch；
8. `git fetch --prune`；
9. 再列一次 remote branches。

禁止：
- `reset --hard` 清掉未知 dirty worktree；
- force-delete 含未知 production diff 的 branch；
- 创建“archive/*”长期分支替代真正收口；
- 因删除 branch 而删除 Git 历史；
- 把 main/release 或真实 active Research Authoring branch 清掉。

## 8. 最终仓库一致性

整理结束后必须给出一个简短清单：

```text
MAIN_HEAD=
RELEASE_HEAD=
PIE_0_1_STATUS=
PIE_SERVER_VPS_NON_READER_ACCEPTANCE=
PIE_WEB_WRAPPER_STATUS=
README_ON_MAIN=
REPOSITORY_VERSION=
OPEN_PRS=
REMOTE_BRANCHES=
ACTIVE_RESEARCH_AUTHORING_BRANCHES=
DELETED_BRANCHES=
PRESERVED_DIVERGED_EVIDENCE=
STALE_TRACKING_ISSUES_RECONCILED=
C11_READER_LAYER_FAILURE_PRESERVED=YES
```

### 成功状态

如果 PIE 验收已经 PASS：
- main/release 包含正式 PIE 0.1；
- main README 真实可见；
- wrapper 是最终 0.1 source；
- Issue #93 完成；
- PIE task branches 全删；
- 只保留 main/release + 真正在做的 Research Authoring branches；
- Clear Writing #13 保留 tracking，但没有闲置工作 branch。

如果真实 Web 验收仍需要用户动作：
- 完成所有不依赖该动作的 branch cleanup；
- main 不虚报 PIE release；
- 只保留唯一 PIE closure branch；
- 给用户一个最小操作请求：更新 wrapper（如尚未更新）/ 在 Server+VPS fresh thread 发送冻结自然问题，并把第一条完整回答带回；
- 不要求用户做任何其他仓库维护。
