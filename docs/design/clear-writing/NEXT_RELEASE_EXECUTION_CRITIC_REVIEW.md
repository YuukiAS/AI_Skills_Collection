# Clear Writing 下一次正式发布收口 — Execution-ready Critic Review

- Review round: `1`
- Date: `2026-09-15`
- Review stage: `EXECUTION_READY`
- Decision: `REVISE`
- Target repo: `YuukiAS/AI_Skills_Collection`
- Target plugin: `writing-style` / Clear Writing
- Task key: `055_clear_writing_release_convergence`
- Source ref at review start: `main@17ae20b18f160017ca65ff4e2d69e5390e66ac1c`
- Reviewed package commit: `17ae20b18f160017ca65ff4e2d69e5390e66ac1c`
- Approved design authority: `docs/design/clear-writing/NEXT_RELEASE_PROPOSAL.md` v0.1
- Prior design Critic: `docs/design/clear-writing/NEXT_RELEASE_CRITIC_REVIEW.md` round 1 `PASS`
- Execution Plan: `docs/design/clear-writing/NEXT_RELEASE_EXECUTION_PLAN.md` v0.1
- Canonical Goal: `docs/goals/055_CLEAR_WRITING_RELEASE_CONVERGENCE_GOAL.md` v0.1
- Kickoff Draft: `docs/operations/prompts/055_CLEAR_WRITING_RELEASE_CONVERGENCE_KICKOFF.md` v0.1
- Ready for Codex: `NO`

## 1. 结论

本轮结论是 `REVISE`，但不是重开已经通过的 Clear Writing 架构设计。

Execution package v0.1 在大方向上忠实实现了上一轮 PASS：target identity、PARTIAL_REDESIGN 主链、G1–G8、A/B/C reviewer rubric、bounded paid Terra、private scope、candidate replay、CI、production smoke、restore、Git 边界都已经写得相当清楚；上一轮 Critic 的 N1–N4 也已实质吸收。

当前仍有四个 execution-level blocker。它们都集中在“最终候选到底是哪一个版本、不可调优评估前谁直接审过它、fresh 到底怎样才算 PASS、私有全文怎样真正交给独立 Critic，以及合同歧义出现时由谁裁定”。如果不关闭，会出现两种假完成路径：一是 pre-final Critic 审的是旧 commit，而 fresh/Terra 跑的是后来变化的 final candidate；二是 G7 只完成冻结和机械检查就被记为 fresh PASS，真正的 whole-artifact reader judgment 又拖到 Terra。

因此本轮不批准把当前 Kickoff 直接发给 Codex。Planner 只需修 execution contract，不需要重新设计 Clear Writing 产品架构。

## 2. 本轮实际读取

按最新 main 重新读取了：

- `AGENTS.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md` v1.1
- `docs/workflows/PLANNER_ROLE_CONTRACT.md` v1.1
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md` v1.0
- `docs/workflows/PAID_EXTERNAL_REVIEW_POLICY.md`
- `docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md`
- `docs/workflows/CANDIDATE_PLUGIN_REPLAY.md`
- `docs/design/clear-writing/NEXT_RELEASE_PROPOSAL.md`
- `docs/design/clear-writing/NEXT_RELEASE_CRITIC_REVIEW.md`
- `docs/design/clear-writing/NEXT_RELEASE_EXECUTION_PLAN.md`
- `docs/goals/055_CLEAR_WRITING_RELEASE_CONVERGENCE_GOAL.md`
- `docs/operations/prompts/055_CLEAR_WRITING_RELEASE_CONVERGENCE_KICKOFF.md`
- `scripts/codex_marketplace_config.json`
- `automation/reviewed_handoff/prompts/REVIEWER_SCHEDULED_TASK.md` 中与 private artifact / final Reviewer 有关的现行规则

当前 Marketplace source 确认 `writing-style` display name 为 Clear Writing、version 为 `0.2`。当前远端尚不存在 `reviewed/055_clear_writing_release_convergence`，与 package 规定“用户发送批准 kickoff 后再从当时 latest main 建 exact branch/worktree”一致。

## 3. 已通过的 execution package 部分

### 3.1 Scope identity — PASS

- exact task = `055_clear_writing_release_convergence`
- exact branch = `reviewed/055_clear_writing_release_convergence`
- exact worktree = `/tmp/ai-skills-055-clear-writing-release-convergence`
- target = `writing-style` / Clear Writing
- 明确从当时 latest `origin/main` 创建，且相关 policy/design 变化时停止。
- 053/054 只作 evidence / selective implementation source，明确禁止 whole-branch merge。
- Bridge Kit / Host Policy / execpolicy 明确 out of scope。

### 3.2 Architecture fidelity — PASS

Execution Plan / Goal 保留批准主链：

`ordinary entry -> Meaning Map -> Reader Plan -> REALIZE_MEANING -> assembly / whole-document finish -> fidelity/audit -> bounded repair -> final candidate`

没有把方案偷换成禁词/regex patch、第二 writing runtime、新 state/schema/ledger、per-stage paid generation、giant postprocessor、自动 fact-check 或 Research Authoring。

Reader disposition 明确优先复用现有 Meaning Map / Reader Plan 与 `inline-critical | relocatable-trace | internal-workflow-trace`；REALIZE_MEANING 保护 modality；assembly 承担 whole-document composition；fidelity/audit 保持 verifier。这与上一轮 design PASS 一致。

### 3.3 上一轮 N1–N4 — PASS

- N1：052 已准确写为完成 bounded closure、release CI、production smoke、用户 ACCEPT 与 main integration，但不代表长期 maturity。
- N2：053 H1 已准确保留为 Cyrillic glyph render failure，没有追认成 reader-relevance failure。
- N3：明确禁止另建 parallel persistent ledger/schema/state，并要求优先扩展现有语义。
- N4：paid Terra 被单独写成“只有用户实际发送批准 kickoff 后才授权”的 bounded final-review envelope，并给出了 model、endpoint、purpose、call count、retry、cost ceiling、credential、private-data boundary 与停止条件。

### 3.4 Reviewer rubric — PASS

Goal/Plan 已冻结：

- A = source fidelity，硬 blocker；
- B = reader-facing quality，硬 blocker；
- C = external factual truth，默认非 Clear Writing blocker；candidate 相对 source 新增/强化/错误归因时才转 A。

也明确禁止 code/path/future-work 的 blanket rule。Blocking finding 必须回指冻结 Gate/requirement 和具体 artifact evidence；A 还必须能回指 source。该设计足以避免 054 F3/F4 类型的 reviewer 越权。

### 3.5 Authorization envelope — 除 C2 外基本 PASS

Kickoff 已明确：exact task/branch/worktree、private read/write scope、canonical candidate replay、CI、ordinary commit/non-force push、一次 final Terra、OpenAI Responses endpoints、`OPENAI_REVIEW_API_KEY`、`USD 0.25` 单次/总 reservation ceiling、一次 bounded production install/upgrade smoke 与 finally restore，以及 force/destructive Git、new provider/account/credential location 等禁止项。

当前官方 OpenAI API 文档仍确认 `gpt-5.6-terra` 为 `$2/M` input、`$0.20/M` cached input、`$12/M` output，cache write 为 uncached input 的 `1.25x`，`POST /responses/input_tokens` 仍是正式 input-token count endpoint。因此当前 repo paid-policy 所依赖的价格/endpoint 假设没有在本轮失效。

## 4. 独立外部核查

本轮没有把 Planner 上轮引用当成默认正确结论，而是针对 execution contract 独立核查了三个关键假设。

1. Anthropic, **Demystifying evals for AI agents** (2026-01-09): https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
   - deterministic / model / human grader 各自适合不同性质；LLM graders 需要 human calibration；任务与 rubric 必须无歧义；应该同时有 should-do / should-not-do cases；评估 harness 要尽量接近 production，并区分 agent failure 与 grader/harness failure。
   - 对本包的影响：支持 G1 正常入口、G3/G5 成对案例、A/B/C 拆分和 rubric adjudication；也说明不能把机械 gate 当 reader-quality PASS。

2. Dwork et al., **The reusable holdout: Preserving validity in adaptive data analysis** / **Generalization in Adaptive Data Analysis and Holdout Reuse** (Science/NeurIPS 2015): https://pubmed.ncbi.nlm.nih.gov/26250683/ ; https://proceedings.neurips.cc/paper/2015/hash/bad5f33780c42f2588878a9d07405083-Abstract.html
   - 反复根据 holdout 结果适配会对 holdout 本身过拟合。
   - 对本包的影响：支持“candidate/rubric 先冻结、fresh 输出曝光后不得 production tuning、失败 item 永久转 known regression”的方向。

3. OpenAI, **A shared playbook for trustworthy third party evaluations** (2026-05-29): https://openai.com/index/trustworthy-third-party-evaluations-foundations/
   - 评估报告必须明确 claim、tested system/harness、budget 和 validity checks；contamination、broken problems、unfair scoring、harness differences 都可能使分数失真；真实能力结论不能与被测系统版本/环境脱钩。
   - 对本包的影响：支持 same-final-candidate identity、source/reviewer/environment 分开归因，也使 C1/C3 成为 execution blocker 而不是格式建议。

## 5. Blocking findings

### C1 — Pre-final Critic PASS 与 exact final candidate identity 没有闭合

**对应要求**

- 用户本轮要求：所有 release-critical Gate 必须由同一个 exact final candidate 直接通过；fresh/final paid 之前必须已有代表性完整 artifact + 独立 whole-artifact qualitative review。
- `PLUGIN_CAPABILITY_GATE_POLICY.md` §5：旧候选的关键 Gate 不能替代后来修改后的最终候选。

**真实证据**

Plan Phase 4 先做 `Pre-final independent Critic`；Phase 5 才做 `Final candidate freeze`，并明确允许“吸收 Critic 非架构性修复”、reconcile latest main、version/changelog closure、source/generated parity 后再冻结 exact candidate。Goal 采用同样顺序。

这意味着 pre-final Critic 可能实际审的是 commit A，而 fresh/Terra 使用 commit B。尤其 version/changelog closure 会改变 candidate commit / generated plugin payload identity；更严重的是，若 Critic finding 导致产品输出修复，完整 artifact 也会改变。

**为什么会导致假 PASS**

G6 的 independent whole-artifact qualitative evidence 可能来自 A，却被用来放行 B 进入不可调优的 fresh。这样违反 same-final-candidate contract，也重新打开“独立审查发现问题 -> Executor 修 -> 不再独立复审 -> 直接 freeze/fresh”的路径。

**最小关闭条件**

Plan / Goal / Kickoff 必须使以下语义唯一：

- 进入 fresh 的 exact candidate commit/payload 必须就是最后一次 pre-final Critic 实际审过并给 PASS 的 candidate；
- 任何会改变 production source、generated payload identity 或 user-facing artifact 的 post-review 修改，都使该 Critic PASS 对 final candidate 失效，必须重新生成代表性 artifact/render并再次交 Critic，直到 exact final candidate PASS；
- version/changelog/source-generated parity 等会改变 release payload identity 的 closure，应在最后一次 pre-fresh Critic PASS 前完成，或明确证明 post-PASS 只发生不改变 candidate/payload hash 的 control-only change。

**Owner**: Planner。Executor 不得临场自行解释。

### C2 — Private Deep Research 的 pre-final Critic 可达路径未预先定义

**对应要求**

- Critic role contract：Critic 不能只凭路径/摘要声称读过私有全文/render。
- Planner role contract：私有全文只能本地访问时，应提前安排用户明确授权的可访问交付途径。
- 用户本轮要求：fresh/Terra 前必须有独立 whole-artifact qualitative review，并核对 private artifact/data scope。

**真实证据**

Goal/Plan 要求 pre-final Critic 实际读取代表性完整 Deep Research 的 source、candidate 和 render。与此同时，private plaintext/PDF/intermediate 明确不得 commit/push，只能留在 `private/exports/...` / ignored runtime。当前长期 Critic thread 的真实执行面是 GitHub connector，无法直接读取该本地 ignored 路径。

Plan 只要求 Executor 在 packet 中写“source + candidate 可达方式”，但没有冻结真正的 handoff/transport。Kickoff 只明确授权了 final candidate text 通过 GitHub Actions/OpenAI Terra；没有说明 pre-final private source/candidate/render 如何进入独立 Critic 可访问范围。

**为什么会导致错误方向或停摆**

到 Phase 4 后，Executor 只能：

- 给 Critic 一个不可达 local path/summary，导致 Critic 无法合法 PASS；或
- 临时发明新的上传/provider/transport，触发新的数据授权问题；或
- 再让用户现场设计交接方式。

这不是产品架构问题，而是 execution path 尚未闭合。

**最小关闭条件**

预先写明一个当前能力真实可用的 bounded handoff：至少说明谁把哪些 source/candidate/render 文件以什么方式交给该 Critic thread、是否需要用户手动上传、哪些内容禁止外发，以及该步骤是否属于当前授权。最简单的合法路线可以是 Executor 只在 repo-local `private/exports/055.../` 生成一个明确 bundle 后停止，向用户给出 exact paths，由用户本人上传到 Critic thread；若改为 Executor 主动发送到新的外部 provider，则必须单独获得相应 data/provider authorization。

**Owner**: Planner；如选择新的外部数据传输，authorization owner 为用户。

### C3 — `CONTRACT_AMBIGUITY` 没有成为完整的冻结恢复类型

**对应要求**

用户本轮明确要求为 `true product defect / source-input defect / reviewer-rubric error / environment-render-infrastructure failure / contract ambiguity` 分别定义 owner 和合法恢复路线。

**真实证据**

Plan §9 / Goal §8 已分别定义 product、source、reviewer、environment、paid pre-request、restore、main drift；pre-final 阶段也提到 `rubric/contract mismatch`。但 fresh attribution 的正式枚举只有：

`PLUGIN_DEFECT | SOURCE_DEFECT | REVIEWER_RUBRIC_DEFECT | ENVIRONMENT_DEFECT | WORKFLOW_DEFECT`

没有 `CONTRACT_AMBIGUITY`，也没有规定“fresh/Terra 已曝光后才发现 frozen requirement 本身有两种合理解释”时谁裁定、candidate/fresh 身份如何保持。

**为什么会导致错误方向或假 PASS**

真正的合同歧义可能被硬塞成 plugin defect 或 reviewer defect；随后要么针对已曝光 fresh 调产品，要么临场改 rubric 把 failure 变 non-blocking。这两种都可能污染 fresh integrity。

**最小关闭条件**

把 contract ambiguity 明确为独立恢复类：默认停止当前 certification，保留 candidate/source/output/original review，不修改历史；由 Planner + Critic 对 frozen user/Goal requirement 做裁定。只有不改变既有 requirement 的解释性澄清才可继续；若裁定实质改变 acceptance/rubric/产品边界，则当前 fresh/final certification 不能直接沿用，必须按新的批准范围处理。只有涉及新的用户偏好/授权时才回用户。

**Owner**: Planner + Critic；必要授权/产品偏好才由用户决定。

### C4 — G7 定义了“fresh 怎么冻结”，但没有充分定义“fresh 怎样才算能力 PASS”

**对应要求**

- 用户本轮要求 G1–G8 都成为真实可执行 Gate，而不是 Proposal 中的名字。
- `PLUGIN_CAPABILITY_GATE_POLICY.md` 要求 Gate 具有 normal entry、真实 evidence、明确 failure、regression boundary 和 final-candidate requirement。

**真实证据**

G7 很好地冻结了 exactly 3 个风险族、source completeness、candidate/rubric freeze 和禁止 adaptive replacement/tuning；但 Plan/Goal 没有明确规定每个 fresh output 必须通过哪些冻结的 G2–G6 reader/fidelity/render 条件才可记 `G7 PASS`。

当前 Phase 6/7 文字只说运行 batch、finding attribution、`全部 PASS 才继续`。如果 Executor 把“PASS”解释为 route/receipt/local mechanical audit PASS，final Terra 仍可能成为 fresh output 第一位真正按 A/B 完整阅读的人——这正是本轮想避免的旧模式。

**为什么会导致假 PASS**

Fresh generalization 是用户能力 Gate，不是 holdout-management Gate。只证明题目没被换、candidate 没被改，并不能证明三份新 artifact 在 source fidelity、reader relevance、structured content 和真实 render 上真的成功。

**最小关闭条件**

明确冻结 G7 item/batch 的 acceptance：

- 三项都必须通过 same exact final plugin normal entry；
- 每项按其预定风险直接应用相关的 G2–G6 frozen criteria；
- source fidelity A 必须有 source-aware evidence；reader-facing B 必须真实阅读 candidate；涉及公式/表格/长文的 item 必须生成并检查实际 render；
- deterministic audits 只能辅助，不能独立判 G7 capability PASS；
- complete batch 只有 3/3 均满足预先冻结标准才可 PASS；final Terra 是额外 independent certification，不是第一层 qualitative grader。

这不要求在 fresh 后允许调参，也不要求第二次 paid review。

**Owner**: Planner。

## 6. 非阻塞观察

当前 paid envelope 本身不需要扩大：一次 Terra、`USD 0.25` per-call/campaign、0 automatic retry 已比 repo 默认 policy 更窄。Kickoff 已把 credential 限定为 existing GitHub Actions `OPENAI_REVIEW_API_KEY`，并禁止新 provider/account/credential location，因此没有理由为了本轮 execution-ready review再增加账户体系、第二 secret 或第二 provider。

如果 Planner 修订 execution package，顺手把 paid project 名 `AI_Research_Review` 作为现行 policy locator 写入 authorization envelope 会更直观，但在 credential 已由唯一 repository secret 固定、且任何 new account 明确禁止的前提下，这一点本轮不单独作为 blocker。

## 7. 本轮判定

```text
REVIEWED_PROPOSAL_PATH=docs/design/clear-writing/NEXT_RELEASE_PROPOSAL.md
REVIEWED_EXECUTION_PLAN_PATH=docs/design/clear-writing/NEXT_RELEASE_EXECUTION_PLAN.md
REVIEWED_GOAL_PATH=docs/goals/055_CLEAR_WRITING_RELEASE_CONVERGENCE_GOAL.md
REVIEWED_KICKOFF_PATH=docs/operations/prompts/055_CLEAR_WRITING_RELEASE_CONVERGENCE_KICKOFF.md
REVIEWED_PACKAGE_COMMIT=17ae20b18f160017ca65ff4e2d69e5390e66ac1c
DECISION=REVISE
READY_FOR_CODEX=NO
BLOCKERS=C1,C2,C3,C4
```

本 `REVISE` 不撤销上一轮 Proposal v0.1 的 design PASS，也不要求重做 architecture/Gate taxonomy。Planner 只需关闭上述 execution-contract blockers，再提交一个明确新版本的 Plan + Goal + Kickoff package 给本 Critic 复审。