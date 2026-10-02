# Project Instructions Editor — Implementation Execution Critic Review v0.1

Date: 2026-10-02  
Result: `REVISE`  
Repository: `YuukiAS/AI_Skills_Collection`  
Source branch/ref: `main`  
Main observed before this review: `1c7ff0d5d2037e7a0ef2ba4bf44bdb829d3c26e6`  
Review stage: execution-ready implementation package review  
Tracking: `#93`

Reviewed same-version package:

- Plan: `docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_IMPLEMENTATION_PLAN_V0_1_2026-10-02.md`
- Goal: `docs/goals/PROJECT_INSTRUCTIONS_EDITOR_IMPLEMENTATION_GOAL_V0_1.md`
- Kickoff Draft: `docs/operations/prompts/PROJECT_INSTRUCTIONS_EDITOR_IMPLEMENTATION_KICKOFF_V0_1.md`
- Package commit: `eece8a8bd89c84559a1d1b8d079fef4b5e4bb9ae`

Approved design authority:

- `docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_PRE_IMPLEMENTATION_DESIGN_FREEZE_V1_PLANNER_PROPOSAL_2026-10-02.md`
- `docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_PRE_IMPLEMENTATION_DESIGN_FREEZE_V1_CRITIC_REVIEW_2026-10-02.md`
- Design-freeze Critic PASS commit: `bf9add585924e93ab8844bb59a366f1cd4f837d6`

```text
CRITIC_RESULT=REVISE
READY_FOR_CODEX=NO
NEXT_HANDOFF=PLANNER
BLOCKERS=E1,E2
```

## 1. 结论

Implementation package 的主体方向正确，但还不能 execution-ready PASS。

本轮没有重新打开已经冻结的产品设计。source placement、metadata、normal-entry 方向、四个 Gate family、ChatGPT/Codex surface 边界、版本判断、README/release-candidate 范围和授权边界总体都与已批准设计及当前仓库规则一致。

真正阻塞执行的是两个 execution-contract 问题：

1. Executor 与独立 Reviewer 对 G4 的所有权发生自相矛盾；
2. “同一 final candidate”缺少可执行的冻结顺序，当前 Kickoff 可能让 Gate evidence 在 final candidate identity 真正确定之前产生。

这两项会直接导致假 PASS 或证据绑定错误，不是文档美化问题。

## 2. 已通过的部分

### 2.1 Source placement / taxonomy

`PASS`.

`skills/core/codex-system/project-instructions-editor/` 与当前仓库 taxonomy 一致。该 Skill 是跨 Project、跨领域的系统级 support capability，不属于普通 writing route，也没有理由为单一 Skill 新建 domain/taxonomy。

### 2.2 Skill structure / capability metadata

`PASS`.

计划中的：

- `SKILL.md`
- `agents/openai.yaml`
- `references/editor-contract.md`
- `evals/trigger_queries.json`
- `assets/app-facing.svg`
- focused contract test
- standalone baseline test update

足够实现冻结能力，没有不必要 runtime script。

以下 metadata 与冻结产品一致：

```text
version=0.1
provenance=user-authored
trusted=false
requires_network=false
writes_files=false
executes_code=false
secrets_needed=[]
recommended_scope=global
```

`requires_network=false` 表示没有硬网络依赖；source/history 不可得时按冻结合同降级，不等于禁止宿主在可用时读取 canonical source。

`writes_files=false` 也正确：普通产品行为输出 setting candidate/advice，不自动修改 ChatGPT Project UI 或 repo。

### 2.3 Normal entry

`PASS` as a planned capability.

当前 repo 的 skill-creator reference 支持 `agents/openai.yaml -> policy.allow_implicit_invocation`。Implementation Plan 也正确规定：implicit=true、description、trigger eval 或 route receipt 都不能单独证明 G1；必须由安装后的 final candidate 在 fresh normal Codex session 中用自然、未点名 Skill 的请求直接验证。

官方 OpenAI Skills 文档也支持这一产品模型：技能发现主要依赖 name/description，模型根据 metadata 决定是否调用；代表性测试应同时覆盖应触发和不应触发的请求。

### 2.4 ChatGPT / Codex surface boundary

`PASS`.

2026-10-02 独立核查当前 OpenAI 官方资料：

- ChatGPT Skills 当前面向符合条件的 Business、Enterprise、Healthcare、Edu 用户，并受 workspace/product availability 影响；
- Codex/其他产品也可支持 Skills，但安装/同步方式可以不同；
- Codex skills 使用 skill directory / `SKILL.md`，模型通过 name/description 做 discovery。

因此 v0.1 不要求当前 Pro regular Chat 完成 standalone Skill upload/auto-use，required normal-entry evidence 使用 AI_Skills/Codex standalone install + fresh Codex session，是诚实且可执行的 release evidence boundary。

### 2.5 Version decision

`PASS`.

当前 `VERSION=5.4.0`。

Repository version policy 规定：新增此前不存在、可观察的 repository-level user capability 才触发 MINOR；新增 Project Thread Handoff standalone Skill 的 `5.1.0` 是直接先例。

`project-instructions-editor` 是一个此前 collection 不能完成的新可安装 standalone user capability，因此：

```text
Repository bump decision: MINOR
Expected candidate if main remains 5.4.0: 5.4.0 -> 5.5.0
project-instructions-editor standalone: 0.1
all central plugins: NO_BUMP
```

成立。

`VERSION_DRIFT` 时停止 version/release metadata 部分并返回 Planner，也避免 Executor 自行猜版本。

### 2.6 Authorization / stop boundary

`PASS` except for E1/E2 below.

Kickoff 授权范围足够且没有过宽：

- exact branch/worktree；
- task-owned source/docs/tests/generated/release-candidate/results；
- deterministic tests；
- task-local install/fresh Codex smoke；
- public-safe regression；
- zip；
- ordinary commit / non-force push exact branch。

明确不授权 main merge、release/tag/GitHub Release、paid API/model review、private Project data external transmission、live ChatGPT mutation、central Plugin changes、Bridge changes、force/destructive Git。

## 3. Blocking findings

### E1 — G4 的独立 Reviewer 所有权与 Executor stop point 自相矛盾

**对应要求**

Design freeze 与 Capability Gate policy 都要求完整用户产物的定性质量由能够看到完整输入/source/output 的独立 Reviewer 判断，Executor 不得用自己的结果或机械证据冒充产品 PASS。

同时本任务冻结的 Executor 最大 claim 是：

```text
FINAL_CANDIDATE_READY_FOR_INDEPENDENT_REVIEW=YES
```

即 Executor 应在独立 review 之前停止。

**直接证据**

Implementation Plan 的 G4 明确规定：

- G4 evidence 包含“独立 Reviewer 读取完整输入、baseline/source 与完整输出做定性审查”；
- §13 又规定 G4 representative outputs 产生后，必须交独立 Critic/Reviewer；
- §17 却要求 Executor stop point 之前“G1–G4 evidence complete”。

Goal 同时要求 final candidate “passes the four frozen capability families”，但最大 Executor claim 又只是“ready for independent review”。

Kickoff §12 进一步要求 Executor “完成所有……G1–G4……后”才停止并交 independent Reviewer。

**因果风险**

Executor 会遇到两种错误选择之一：

1. 自己把 G4 判成 PASS，违反独立评审边界；
2. 等待一个本来应该发生在 Executor stop point 之后的 Reviewer，导致 execution contract 无法闭合。

这会让 G4 的真实用户质量门槛变成自评或死锁。

**最小关闭条件**

Plan、Goal、Kickoff 同版统一改成：

- Executor 可以完成 G1–G3；
- Executor 生成并冻结 G4 所需的完整代表性 input/source/output packet；
- Executor 对 G4 只能声明：
  `G4_READY_FOR_INDEPENDENT_REVIEW=YES`
  或同义明确状态，不能声明 G4 PASS；
- 达到该状态后即可停止在：
  `FINAL_CANDIDATE_READY_FOR_INDEPENDENT_REVIEW=YES`；
- 独立 Reviewer 才拥有 G4 qualitative PASS/REVISE 和 implementation overall PASS。

可保留现有四 Gate taxonomy，不需要新增第五 Gate。

Evidence 文件可以：
- 将 Executor-owned 文件改为 `G4_COMPLETE_TASK_PACKET.md`；或
- 保留现有文件名，但必须明确其内容是 pending-review packet，绝不能由 Executor写成独立 review PASS。

Owner: Planner.

---

### E2 — final candidate identity 的冻结顺序还不能保证所有 Gate 真正绑定同一候选

**对应要求**

Capability Gate policy 明确要求所有 release evidence 来自同一个 final candidate，不能把不同 commit 的 PASS 拼起来。

本 package 也反复声明 G1–G4 必须直接由 same final candidate 通过，并要求 Reviewer 获得 exact final candidate commit。

**直接证据**

当前 Kickoff 的顺序是：

1. 完成实现、generated parity、tests、G1–G4、release-candidate metadata、package、evidence；
2. 然后“freeze exact final candidate”；
3. 然后 commit / push。

也就是说 Gate runs 发生时，exact final candidate commit 还不存在。

同时 evidence/result 文件本身会在 Gate 后继续写入 branch；如果 runtime/source/generated/release-candidate 文件在 Gate 后发生任何修订，旧 Gate evidence 会变成 stale，但当前 package 没有冻结“哪些文件在 candidate freeze 后绝对不能再变化”以及怎样证明后续 commit 只是 evidence-only。

**因果风险**

可能出现：

- Gate 在候选 A 上运行；
- 后续 metadata/source/generated 文件又发生变化；
- 最终 branch HEAD/“final commit”变成候选 B；
- Reviewer 看到的是 B，却拿 A 的 G1/G2/G3/G4 evidence 宣称 same-final-candidate PASS。

这正是当前 Gate policy 禁止的证据拼接。

**最小关闭条件**

Plan、Goal、Kickoff 必须冻结一个无循环的 candidate/evidence sequence。推荐最小方案：

1. 完成所有 candidate-owned 内容：
   - Skill source/reference/evals/assets；
   - generated parity；
   - README/VERSION/CHANGELOG release-candidate metadata；
   - candidate tests/baseline declarations；
2. 创建并记录一个 exact **candidate commit C**；
3. 从 C 做 task-local install，并运行 G1–G3 与 G4 representative outputs；
4. portable zip 必须由 C 的 runtime tree 生成并记录 hash/file list；
5. Gate/evidence 只能在 C 之后写 evidence-only files；
6. Reviewer handoff 明确：
   `FINAL_CANDIDATE_COMMIT=C`；
7. 从 C 到 evidence HEAD 的 diff 必须只包含明确允许的 evidence/review/result 文件；若 Skill source/generated/release-candidate metadata 等 candidate-owned 内容发生任何实质变化，则旧 Gate evidence 失效，必须形成新的 C 并按风险重跑相应 Gate。

不要求 evidence 文件本身包含在 candidate commit；重点是 runtime/release candidate identity 与 Gate 输入必须固定且可证明。

Owner: Planner.

## 4. Non-blocking observations

### agents/openai.yaml generation

当前 skill-creator 的 `generate_openai_yaml.py` 主要生成 `interface`，而同目录的 current reference 还定义了 `policy.allow_implicit_invocation`。

因此实现时可以先用 generator 生成合法 interface，再按 current schema/reference 加入 policy，并由 focused test 验证。这个差异属于实现细节，不需要改变产品设计，也不构成 blocker。

### G1 near-miss

未来 G1 最好在 candidate 与 relevant neighboring skills 同时可发现的正常环境里验证 near-miss owner，而不是只证明“candidate 没触发”。但具体安装组合/fixture 属于实现期测试设计；现有 Gate claim 已经明确 owner boundary，不单独阻塞 package。

## 5. Maintenance state

Current main 已确认：

- canonical TODO 保持 `tracking: #93`；
- Issue #93 为 open；
- labels 为：
  - `maintenance-track`
  - `kind:new-capability`
  - `scope:standalone-skill`
  - `area:standalone-skill`

Issue reader-facing body 仍落后于当前 implementation stage。

当前 Critic surface 没有可验证的 installed Clear Writing invocation，因此本轮不修改 Issue body：

```text
CLEAR_WRITING_UNAVAILABLE
```

当前也没有 GitHub Project field mutation surface，因此不能声称 Project 已同步。

Exact pending Project mutation：

```text
Project = AI Skills Maintenance
Issue = #93
Status = DOING
Area = standalone-skill
current execution anchor =
docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_IMPLEMENTATION_PLAN_V0_1_2026-10-02.md
```

不要要求用户手工维护 Project 卡片。

## 6. Review boundary

本轮没有否定 implementation phase，也没有重新打开 product design freeze。

只需要 Planner 对 execution package 做最小 v0.2 修订，关闭 E1/E2：

- 明确 Executor 只准备 G4 packet，独立 Reviewer 才给 G4 PASS；
- 固定 exact candidate commit -> Gate runs -> evidence-only commits 的顺序与失效条件。

其他已通过部分不应重新设计。

```text
CRITIC_RESULT=REVISE
READY_FOR_CODEX=NO
NEXT_HANDOFF=PLANNER
BLOCKERS=E1,E2
```
