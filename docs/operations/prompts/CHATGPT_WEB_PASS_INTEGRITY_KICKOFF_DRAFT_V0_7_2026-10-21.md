# Kickoff Draft v0.7 — chatgpt-web--pass-integrity

状态：DRAFT ONLY；当前未授权实施。  
任务：`chatgpt-web--pass-integrity`

## Authority

批准后必须从同一个 exact `PACKAGE_COMMIT` 读取：

- `docs/workflows/CHATGPT_WEB_PASS_INTEGRITY_PROPOSAL_V0_7_2026-10-21.md`
- `docs/workflows/CHATGPT_WEB_PASS_INTEGRITY_EXECUTION_PLAN_V0_7_2026-10-21.md`
- `docs/goals/CHATGPT_WEB_PASS_INTEGRITY_GOAL_V0_7.md`
- 本 Kickoff；
- 对应 final execution-ready Critic review。

只有独立 Critic 对同版完整 package 给出：

```text
PASS
READY_FOR_CODEX=YES
```

并且用户实际发送批准后的短 `COPY TO CODEX`，才允许开始。

## Exact execution identity

```text
repo=YuukiAS/AI_Skills_Collection
task_key=chatgpt-web--pass-integrity
execution_branch=reviewed/chatgpt-web--pass-integrity
execution_worktree=/tmp/ai-skills-chatgpt-web-pass-integrity
```

## Phase 1 — 实施 Planner/Critic 1.8

只按批准 Plan 修改 allowlist。

### Planner 1.8

保留：

- task-specific Critic prompt compatibility preflight；
- short Codex handoff renderability preflight。

新增：

- critical-interface reality evidence；
- 现有非终态唯一下一入口的 handoff closure 判定。

不得复制一遍 Project setting 写作规则；要把已有原则转成可观察 evidence 和 acceptance。

### Critic 1.8

保留：

- task-prompt compatibility hard gate；
- atomic execution-ready PASS；
- PASS 后 explanation / contradiction / new requirement。

新增：

- critical-interface evidence hard gate；
- whole-response handoff/readability acceptance。

## Phase 2 — candidate freeze

完成 candidate-defining source 后提交一次 exact commit：

`GOVERNANCE_CANDIDATE_COMMIT=<exact sha>`

生成：

`results/chatgpt-web--pass-integrity/GOVERNANCE_CANDIDATE_MANIFEST.md`

至少记录：

- exact candidate commit；
- Planner/Critic 1.8 path/version/hash；
- collaboration regression candidate；
- deterministic replay contract；
- real A/B/C validation contract；
- base main；
- exact branch/worktree；
- candidate-defining allowlist。

冻结后：

- candidate-defining source 不得改变；
- evidence 只能追加并绑定同一 candidate；
- source 改变则旧 evidence 失效。

## Phase 3 — deterministic checks

针对 exact candidate：

- diff/scope；
- role version/hash；
- Project setting unchanged；
- Capability Gate Policy unchanged；
- forbidden-path unchanged；
- manifest consistency；
- v0.6 已冻结的 8-case replay。

deterministic replay 只证明对应合同条件，不冒充真实 normal-entry reply 或 interface readiness。

## Phase 4 — post-implementation Critic safety gate

不新增 separate implementation Reviewer。

准备 bundle，交独立 Critic读取：

- actual diff；
- exact candidate；
- 两份 1.8 合同；
- candidate manifest；
- deterministic replay evidence；
- critical-interface evidence；
- A/B/C exact prompts、source locators、expected result 和 stop conditions。

该 Critic 只允许：

```text
PROCEED_TO_FINAL_EVALUATION
或
REVISE
```

只有前者才能进入 Phase 5。

普通实现/doc bug不改变冻结语义时继续同一 Codex task修；必须改变冻结治理语义时回 Planner。

## Phase 5 — real ChatGPT Web validation batch

当前没有 verified automation 能创建 fresh ChatGPT Web conversation 并绑定 candidate role contract。

因此此阶段明确包含最多三次 user-only UI action。Codex 在请求用户之前必须把三份 exact prompt 全部准备完成，包含所有 locators；不得要求用户自己查 repo 或拼 prompt。

### Case A — Clear Writing 0.6 execution-ready negative control

固定：

`package=d7b810d194ead881303aaca9c2e4f1d59a97c1f1`

supporting evidence：

`38a81dc1df9a362ecee4be597cb3db5bd6fcac41`

用户动作：

- 打开 fresh independent Critic conversation；
- 粘贴已准备好的 Case A prompt；
- 返回完整回复。

正确结果：

`REVISE`

必须实际发现：

1. old task-specific final prompt 与中央合同冲突；
2. Plugin Creator archive / restore builder / materialization关键接口未证明；
3. fresh ChatGPT Web actor/surface未证明。

只发现第 1 项不能通过治理 Case A。

### Case B — Phase C stop Planner response

固定：

- approved package `d7b810d...`；
- Phase C evidence `38a81dc...`；
- original reply：
  `results/chatgpt-web--pass-integrity/real-validation/case-b/ORIGINAL_REPLY.md`

用户动作：

- 打开 fresh Planner conversation；
- 粘贴已准备好的 Case B prompt；
- 返回完整回复。

candidate Planner 必须让用户直接明白：

- formal Personal Plugin仍是 0.5.0；
- 为什么停止；
- archive compatibility默认由同一 Clear Writing Codex task修；
- fresh Web actor/responsibility缺口由 Planner负责；
- 用户当前需要什么动作；
- 唯一下一入口；
- 可直接使用的 handoff。

如果当前 Planner自己仍是下一 owner，它必须继续完成可合法完成的部分，而不是让用户“再找 Planner”。

“需要一个同时具备 X/Y 能力的 execution surface”不算 next entry。

### Case C — real complex execution-ready positive control

固定：

`package=745e6748c5faa7cbad51973142661491224ba5a2`

task：

`055_clear_writing_release_convergence`

用户动作：

- 打开 fresh independent Critic conversation；
- 粘贴已准备好的 Case C prompt；
- 返回完整回复。

candidate Critic必须重新做完整 execution-ready review，历史 PASS不自动有效。

若 current truth支持 PASS，同一回复必须：

- 用自然中文讲清架构、normal use、manual user upload、private/paid boundary、failure/recovery和未证明事项；
- 给 exact approved locators；
- `READY_FOR_CODEX=YES`；
- `NEXT_HANDOFF=CODEX`；
- 给短 `COPY TO CODEX`。

若 current truth发现 blocker：

`REVISE`

并且本批次不得换另一个正控。governance candidate保持未接受。

## Phase 6 — record real evidence

用户返回每个完整 reply 后：

- 长期 Planner或同 task Codex负责保存到：
  `results/chatgpt-web--pass-integrity/real-validation/case-{a,b,c}/`
- 记录 exact `GOVERNANCE_CANDIDATE_COMMIT`；
- 保存完整 user-visible response，不只摘 verdict字段；
- 做 qualitative adjudication；
- 用户不负责建 evidence file。

如果 current Planner无法写 repo，使用同一 Codex task记录；不得把文件整理工作交给用户。

## Phase 7 — candidate acceptance

只有：

- deterministic replay符合 contract；
- post-implementation Critic = `PROCEED_TO_FINAL_EVALUATION`；
- Case A正确 REVISE并发现 interface gaps；
- Case B whole-response handoff/readability PASS；
- Case C genuine execution-ready PASS + atomic delivery；
- candidate-defining source未变化；

才能记录：

`CANDIDATE_ACCEPTED`

任何一个失败：

- 保留原完整输出；
- 不换题；
- 不补第 4 个案例；
- 不挑赢家；
- 按 root cause回 Codex或 Planner。

## Phase 8 — main integration

达到 `CANDIDATE_ACCEPTED` 后：

1. `git fetch origin main`；
2. integration preflight；
3. 检查 current main、task diff、same-area competing changes；
4. ordinary non-force merge task branch -> main；
5. ordinary non-force push；
6. remote-main fresh readback；
7. 直接确认：
   - Planner Role Contract version = 1.8；
   - Critic Role Contract version = 1.8；
   - hashes 与 candidate manifest 一致；
   - regression / final evidence绑定同一 candidate；
8. 记录 integration commit / remote main tip。

merge conflict / same-area main drift / readback mismatch：

`STOP -> Planner/Critic`

不得 force、history rewrite、静默丢弃 main 变化。

## 当前授权范围

用户发送批准后的短 Codex handoff后，仅授权：

- exact branch/worktree；
- ordinary non-force task branch push；
- Plan allowlist中的治理合同和 evidence；
- candidate freeze；
- deterministic checks；
- post-implementation Critic bundle；
- A/B/C prompt/evidence preparation；
- 满足全部条件后的 main integration + readback。

不授权：

- AI Research Stack Project setting 修改；
- Capability Gate Policy 修改；
- Clear Writing 0.6 product/source/G1-G6修改；
- Plugin Creator修改；
- Bridge Kit修改；
- Personal Plugin mutation；
- paid API；
- repository/plugin release；
- force/destructive Git。

## User-only action boundary

本 Kickoff 已明确：final-evaluation 阶段预计需要用户最多做三次 fresh ChatGPT Web UI 动作。

这不是隐藏 blocker，也不是让用户自行找执行环境。所有 prompt 和 locators 必须由任务提前准备。

若未来出现经过验证的等价自动入口，不能由 Codex自行替换；需按现行治理确认其等价性。

README checked: no update required。
