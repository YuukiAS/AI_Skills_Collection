# 059 Research Authoring C3 integrated owner-chain recovery — Critic Review v0.2

日期：2026-10-07  
角色：独立 Critic  
审查阶段：EXECUTION_READY_REVIEW_AFTER_C3_DEVELOPMENT_FAIL  
Task：`research-authoring--formal-production-authoring`

## 结论

```text
RA-C3DEV1=CLOSED
RA-C3DEV1_RECOVERY_DESIGN=PASS
RESULT=PASS
READY_FOR_CODEX=YES

C2_G1_FAIL=PERMANENT
04a17a904ce522cb4a517cb33f22e062f2bcbc09=FAILED_PROVISIONAL_DEVELOPMENT_ATTEMPT

P2=NOT_CREATED
C3_FINAL_CANDIDATE_COMMIT=NOT_ADMITTED

FINAL_GATES_AUTHORIZED=NO
LIVE_PLUGIN_UPDATE_AUTHORIZED=NO
PAID_API_AUTHORIZED=NO
MAIN_MERGE_RELEASE_AUTHORIZED=NO

NEXT_HANDOFF=CODEX
```

上一轮唯一 blocker 已关闭。本轮没有重新打开 Research Authoring 主架构、shared replay、Bridge 或 Gate taxonomy，也没有 production 修改。

## RA-C3DEV1 closure

上一轮缺口是：`research-main` 将 `latex-paper-authoring` 设为 profile-scoped explicit-only 后，没有保留完整的 direct existing-LaTeX normal entry。

本轮 recovery package 已同步关闭：

### Existing LaTeX direct mode

```text
existing LaTeX source
+ compile/debug/template repair/source hygiene/
  bibliography/build troubleshooting/existing-source build
-> explicitly load latex-paper-authoring
-> compile/debug/build allowed
```

Research Authoring 不为这种 source-maintenance 请求重新规划或重写已有 manuscript。

### Finalized-source render-only

```text
finalized Markdown/LaTeX
+ final PDF render/QA only
-> explicitly load render-chinese-math-pdf
-> render/QA
```

LaTeX 文件本身不再足以把 source-debug/template repair误判为 render-only。

### New/substantially revised manuscript

无论最终是否要求 PDF：

```text
FIRST Research Authoring core/paper
-> optional explicit latex-paper-authoring only for source/package
-> return source/package to Research Authoring
-> if PDF requested: stable handoff
-> explicit render-chinese-math-pdf
-> PDF/QA
-> Research Authoring scientific QA
```

existing-LaTeX direct route不能绕过这个 owner sequence。

## Runtime regression closure

没有新增 DEV-12 或 G5。

direct existing-LaTeX should-not-change 被折入现有 DEV-07：

- DEV-07A：research-main + existing LaTeX + natural compile/debug/template/source-hygiene/build；
- 必须实际读取 `latex-paper-authoring`；
- compile/debug成功；
- Research Authoring不重写/重新规划现有论文；
- generic `pdf` 不成为 owner；
- renderer不把 source-debug误判为 render-only。

同一 DEV-07 继续验证 finalized LaTeX render-only：

- explicit `render-chinese-math-pdf`；
- real PDF/QA；
- Research Authoring planning = 0；
- `latex-paper-authoring` 不因 `.tex` 本身接管纯渲染。

因此本次 explicit-only policy直接影响的原有 LaTeX能力现在有对应 normal-entry runtime should-not-change evidence。

## Stable recovery mechanism

上一轮已接受且本轮未改变：

- `research-main` 中 `latex-paper-authoring`、generic `pdf`、`render-chinese-math-pdf` 为 profile-scoped explicit-only；
- destination-local `agents/openai.yaml` 使用 `policy.allow_implicit_invocation=false`；
- pinned current-runtime preflight必须先证明该 machine-consumed policy在本机 Codex有效；
- generic `pdf` canonical source不全局修改；
- renderer不再增加新的 wording patch；
- LaTeX direct mode允许 compile，Research Authoring delegate mode禁止提前 final compile；
-完整 11-case matrix从零绑定同一 P2；
- README必须有真实 Clear Writing durable evidence；
- exact-C3 offline wrapper在 P2 matrix PASS/C3 freeze后重建；
- no G5；
- no Bridge/shared replay change。

如果 preflight证明 pinned runtime不支持 profile-scoped explicit-only，必须 STOP，不允许退回更强 wording。

## Package synchronization

已核对当前 branch 上以下对象与其声明 commit逐字一致：

```text
APPROVED_STABLE_PROPOSAL_PATH=docs/design/059_RESEARCH_AUTHORING_C3_NORMAL_ENTRY_OWNERSHIP_CLOSURE_PROPOSAL_V0_1_2026-10-06.md
APPROVED_STABLE_PROPOSAL_COMMIT=b4820e49e3473959010afe5fa1e9f92bc0f4844f

APPROVED_RECOVERY_PROPOSAL_PATH=docs/design/059_RESEARCH_AUTHORING_C3_INTEGRATED_OWNER_CHAIN_RECOVERY_PROPOSAL_V0_1_2026-10-07.md
APPROVED_RECOVERY_PROPOSAL_COMMIT=b4cfef6685b232a215d56b942175bf50de415a98

APPROVED_PLAN_PATH=docs/design/059_RESEARCH_AUTHORING_C3_NORMAL_ENTRY_OWNERSHIP_CLOSURE_IMPLEMENTATION_PLAN_V0_3_2026-10-07.md
APPROVED_PLAN_COMMIT=409dedc44931527e02551ac9689521655b328db3

APPROVED_GOAL_PATH=docs/goals/059_RESEARCH_AUTHORING_C3_NORMAL_ENTRY_OWNERSHIP_CLOSURE_GOAL_V0_3.md
APPROVED_GOAL_COMMIT=89aef6c6454d449b23c953cb5a66b3c7a27a1c5a

APPROVED_KICKOFF_PATH=docs/operations/prompts/059_RESEARCH_AUTHORING_C3_NORMAL_ENTRY_OWNERSHIP_CLOSURE_KICKOFF_V0_3.md
APPROVED_KICKOFF_COMMIT=30c6e3d733126b8862c0592cced3e969b685df66

APPROVED_GATE_IMPACT_PATH=docs/design/059_RESEARCH_AUTHORING_C3_CAPABILITY_GATE_IMPACT_V0_3_2026-10-07.md
APPROVED_GATE_IMPACT_COMMIT=c66a7be9b81d976e65ad54081326c4d3ad5fb687

APPROVED_PACKAGE_PATH=results/research-authoring--formal-production-authoring/C3_INTEGRATED_OWNER_CHAIN_RECOVERY_EXECUTION_PACKAGE_V0_1.md
APPROVED_PACKAGE_COMMIT=fedbca2e9ffe5356dc384408a9fb9ce578213399
```

从上一轮 Critic commit `e24ae290647456200c7f66c555caf61a56278d3c` 到本轮 handoff HEAD `e0772c6d1de501f1c4d0c1abd4a38893286fe006` 只有 recovery docs/Goal/Kickoff/package同步；没有 `skills/**`、`profiles/**`、`scripts/**`、`tests/**`、README、CHANGELOG 或 VERSION 的 production变化。

## Bridge / authorization

已读取最新 Bridge Kit main `050c786d7480a00b924aa6f2b0c4542eae4b1e3f` 的 `AGENTS.md`。

本 Kickoff继续绑定 exact repository/task/branch/worktree，并只授权：

- P2 bounded source/profile/installer/test修改；
- task-local current-runtime preflight；
- deterministic/full tests；
-真实 README Clear Writing调用；
-完整 11-case P2 matrix；
- P2/C3 evidence；
- exact-C3 offline wrapper rebuild；
- exact task branch普通 non-force publish。

不授权 final G1-G4、live Plugin、Plugin Creator、paid API、main merge/release、global/user Skill mutation、Bridge/shared replay或 destructive Git。

## Maintenance tracking

Issue #99 reader-facing copy仍旧过时，但其更新必须先真实调用 Clear Writing。该 tracking drift不阻断本 execution-ready PASS，也不改变 Project lifecycle应继续为 `DOING` 的事实。

## Execution boundary

本 PASS批准 recovery package进入 Codex实现，不等于用户已经授权执行。只有用户实际发送本次逐字批准的 Kickoff v0.3 后，才形成 bounded implementation authorization。
