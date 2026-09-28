# Frontend Design Production Consolidation — Kickoff Draft v0.3

只在 independent execution-ready Critic 对以下 v0.2 recovery package 返回 PASS / READY_FOR_CODEX，并把真实 review 写入固定 repo locator 后使用：

- `docs/design/frontend-design/FRONTEND_DESIGN_PRODUCTION_CONSOLIDATION_EXECUTION_PLAN_V0_3_2026-09-28.md`
- `docs/goals/FRONTEND_DESIGN_PRODUCTION_CONSOLIDATION_GOAL_V0_3.md`
- 本 Kickoff Draft v0.2

Durable Critic review locator：

`docs/design/frontend-design/FRONTEND_DESIGN_PRODUCTION_CONSOLIDATION_EXECUTION_CRITIC_REVIEW_V0_3_2026-09-28.md`

用户发送获批 Kickoff v0.3 后，只构成**恢复/继续既有 task**的授权。现有 reviewed branch 与 sibling worktree 已由第一次 bootstrap 创建；本 Kickoff 不授权再次创建 branch/worktree、second bootstrap、raw `git worktree add`、move/remove/recreate。

---

## Kickoff

Repository:

`YuukiAS/AI_Skills_Collection`

Exact task identity / recovery target:

```text
task_key = web-development--frontend-design-production-consolidation
branch = reviewed/web-development--frontend-design-production-consolidation
worktree = /home/yuukias/AI_Skills_Collection-web-development--frontend-design-production-consolidation
```

当前事故现场已经进入：

```text
CURRENT.state = PLAN_REQUESTED
CURRENT.next_action = RUN_GPT_PLANNER
```

这是合法 Bridge 初态，不是 Executor blocker。

Approved architecture:

`docs/design/frontend-design/FRONTEND_DESIGN_PRODUCTION_CONSOLIDATION_PROPOSAL_V0_3_2026-09-27.md`

Approved architecture commit:

`effa02b4e7e02f012ea24bda1683857609a09fe1`

Canonical Goal:

`docs/goals/FRONTEND_DESIGN_PRODUCTION_CONSOLIDATION_GOAL_V0_3.md`

Durable execution-ready Critic review:

`docs/design/frontend-design/FRONTEND_DESIGN_PRODUCTION_CONSOLIDATION_EXECUTION_CRITIC_REVIEW_V0_3_2026-09-28.md`

Execution Plan:

`docs/design/frontend-design/FRONTEND_DESIGN_PRODUCTION_CONSOLIDATION_EXECUTION_PLAN_V0_3_2026-09-28.md`

这是 existing-task recovery + implementation-continuation kickoff，不是重新设计架构。

上一轮 v0.2 durable Critic review：
`docs/design/frontend-design/FRONTEND_DESIGN_PRODUCTION_CONSOLIDATION_EXECUTION_CRITIC_REVIEW_V0_2_2026-09-28.md` @ `d2a7dcd4c153256df1b221c3365ec9875cffd4ba`
结论为 `REVISE / READY_FOR_CODEX=NO`，只作为历史 evidence；当前唯一有效 execution-ready authority 必须来自 v0.3 durable review locator。

关键规则：

- 当前 task 已存在时，**不要再次运行** `ai-bridge reviewed-handoff task bootstrap`；
- 不创建第二个 branch/worktree；
- 不移动、删除或重建现有 sibling worktree；
- Executor 不能自己写 task-local PLAN，也不能自己宣布 PLAN_FROZEN；
- 只有 GPT Planner 合法写入 `AI_BRIDGE_REVIEWED_PLAN_V2` 并把 CURRENT 最后推进到 `PLAN_FROZEN / RUN_CODEX_EXECUTOR` 后，implementation 才能继续。

### 1. Recovery preflight：优先收养现有 sibling worktree

先读取最新 Bridge/AI_Skills contracts，并核实当前 machine-local task：

1. `git worktree list --porcelain` 中 exact path：
   `/home/yuukias/AI_Skills_Collection-web-development--frontend-design-production-consolidation`
   必须绑定：
   `refs/heads/reviewed/web-development--frontend-design-production-consolidation`。
2. 当前 worktree 的 `REQUEST.md` 必须记录同一 Reviewed worktree locator。
3. `CURRENT.json` 必须：
   - task_key 相同；
   - state = `PLAN_REQUESTED`；
   - next_action = `RUN_GPT_PLANNER`；
   - base_branch/base_commit 与 first bootstrap 一致。
4. base commit 必须是该 first bootstrap 实际使用的 post-sync `origin/main`，branch lineage 必须正确。
5. 不得已有 Frontend production implementation diff/commit。
6. working tree 若只有 first-bootstrap task-owned REQUEST/CURRENT control metadata，可继续 recovery；若有来源不明 dirty state，fail closed，不 stash/reset/clean/restore。
7. 读取 durable Critic review locator并验证：
   - RESULT = PASS
   - READY_FOR_CODEX = YES
   - package version = v0.3
   - Plan/Goal/Kickoff 路径正确
   - task key / branch / sibling worktree 正确
   - approved package commit 与 Critic 实际审查对象一致。

上述全部成立时，收养现有 sibling worktree。旧 v0.1 的 `/tmp` locator 作废；不要为了它移动/删除/重建 worktree。

如果现有 task/worktree 不能安全收养，停止并报告直接证据与最小恢复建议。本 Kickoff 不授权 destructive recovery。

#### 1.1 不重复 first bootstrap

当前 branch/worktree 已由 first bootstrap 创建时：

- 禁止第二次 `reviewed-handoff task bootstrap`；
- 禁止 raw `git worktree add` 创建替代 worktree；
- 禁止创建 successor task；
- 若 future worktree 丢失但 exact reviewed branch + REQUEST/CURRENT 已经远端存在，后续只能按 Bridge contract 使用 artifact-bound `materialize-worktree --mode resume`，并断言 REQUEST 里冻结的 sibling path。

#### 1.2 如果 task metadata 尚未远端发布

如果 exact local task 合法、但 reviewed branch 还没有远端 task metadata：

- 只 commit/push first-bootstrap task-owned `REQUEST.md`、`CURRENT.json`；
- 不加入任何 Frontend production implementation；
- 不创建/修改 `PLAN.md`；
- 保持 `PLAN_REQUESTED / RUN_GPT_PLANNER`；
- publish 后停止，等待 GPT Planner transaction。

这一步是 control-plane publication，不是 Executor implementation。

#### 1.3 GPT Planner 冻结 task-local PLAN

下一 owner 是 GPT Planner，不是 Executor。

Planner 在 exact reviewed branch：

1. 读取 REQUEST/CURRENT；
2. 读取 approved Proposal v0.3、Execution Plan v0.2、Goal v0.2、durable Critic PASS；
3. 按当前 `automation/reviewed_handoff/templates/PLAN.md` 写完整 `AI_BRIDGE_REVIEWED_PLAN_V2`；
4. task-local PLAN 只落实已批准 package，不重新设计 Frontend；
5. 重新读取刚写 PLAN 和 current template，自检 frontmatter + required sections；
6. 自检通过后，最后更新 CURRENT：
   - state = `PLAN_FROZEN`
   - next_action = `RUN_CODEX_EXECUTOR`
   - 初次 freeze 不增加 plan_revision；
7. commit/push Planner transaction。

Executor 不得代替 Planner做上述步骤。

#### 1.4 Executor resume condition

只有同时满足：

- exact reviewed branch/worktree；
- valid V2 PLAN；
- `CURRENT.state=PLAN_FROZEN`；
- `CURRENT.next_action=RUN_CODEX_EXECUTOR`；
- durable Critic PASS 匹配 v0.3 package；

才允许继续下面 implementation。

### 3. Existing-task continuation authority

本 Kickoff 不授权创建 task branch/worktree。只有 recovery preflight 已确认并收养：

```text
branch = reviewed/web-development--frontend-design-production-consolidation
worktree = /home/yuukias/AI_Skills_Collection-web-development--frontend-design-production-consolidation
```

且 GPT Planner 已合法写入 task-local `AI_BRIDGE_REVIEWED_PLAN_V2`、将 CURRENT 推进到 `PLAN_FROZEN / RUN_CODEX_EXECUTOR` 后，才继续 production implementation。

如果 existing worktree 未来丢失，只允许当前 Bridge artifact-bound `materialize-worktree --mode resume`；不得 second bootstrap、raw worktree add、move/remove/recreate。

### 4. 必须实现的 normal-entry coordinator

实现 approved coordinator-first architecture：

- `frontend-visual-systems` 是唯一 generic production coordinator；
- aggregate generator 增加最小 opt-in `coordinator-first` mode；
- default/未启用 aggregate 继续原 choose-one；
- Frontend main aggregate 的 coordinator = artifact `system`；
- generic coordinator delegates：
  - product-ux-planning
  - visual-direction
  - design-system-tokens
  - figma-design-to-code
  - motion-interaction
  - responsive-accessibility-review
  - webapp-testing
  - research-product-frontend
- 当前独立 research aggregate 不再作为 generic Frontend Design 平级入口；
- research-product-frontend canonical source 保留，作为 research-specific specialist；
- frontend-reference-research 保持窄范围显式入口；
- implementation-react-tailwind 继续 downstream builder，不成为 design owner；
- builder 如果暴露 design gap，必须回 P0/P1。

不要新增 orchestrator Skill、plugin、状态机或第二套 frontend workflow。

### 5. 必须保留的 Frontend contract

忠实实现 approved：

- P0–P4；
- F-A / F-B / F-C / F-D；
- S1 / S2 / S3；
- design authority：
  - canonical Figma
  - other durable authority
  - current production grammar（仅适用小修/部分 bounded change）
- surface：
  - browser
  - native-WebView
- no-Figma 正常完成；
- tiny/local fix scale-down；
- design defect / implementation drift / product semantic defect / runtime-only repair routing；
- P1/P2/P3 producer admission；
- whole-product taste observable questions；
- handoff action reachability；
- browser/native evidence fidelity；
- #52 / #62 / #69 retained semantics。

### 6. Generator contract

按 Execution Plan v0.3 实现：

```text
routing_mode = coordinator-first
coordinator_artifact_id = <existing source artifact id>
```

必须：

- opt-in only；
- invalid coordinator config fail closed；
- coordinator generated workflow 先读取 coordinator source；
- delegate 由 coordinator 决定；
- coordinator mode 不再输出冲突的 choose-one normal entry；
- 未启用 mode 的其它 aggregate 生成语义不变；
- 现有 aggregate metadata / scope / secrets / deterministic / path-budget contract 不回归。

先补 targeted generator tests，再改 generator。

### 7. Source ownership

不要把所有规则复制进 coordinator。

按 Goal/Plan 的 owner 修改：

- frontend-visual-systems：总协调；
- product-ux-planning：任务/state/actionability/lifecycle/visible semantics；
- visual-direction：整屏方向与 taste；
- design-system-tokens：component/icon/typography/color/status grammar；
- figma-design-to-code：conditional Figma authority / complete / round-trip；
- motion-interaction：motion intent / runtime latency boundary；
- responsive-accessibility-review：适用 P1/P3 closure；
- webapp-testing：browser evidence companion；
- research-product-frontend：research-specific UI constraints；
- implementation-react-tailwind：downstream handoff boundary only。

### 8. 明确 deferred / forbidden

不得修改或实现：

- Clear Writing / writing-style production；
- Product UI copy content-architecture deferred heading；
- writing-style #17；
- writing-style #20；
- writing-style #13；
- CUHK Date Product UI Copy naturalness；
- Bridge Kit（本 recovery 只消费当前正常入口，不修改 Bridge Kit）；
- Host Policy / execpolicy；
- Bobbio/Lucerna/Asteria/Mica/SeminarArc source；
- unrelated repo；
- paid reviewer/API；
- 新 provider/credential/private-data scope；
- force push / rebase / history rewrite / branch deletion；
- merge main；
- update release ref。

如果必须扩这些 scope 才能继续，停止返回 Planner/Critic。

### 9. Tests 与 generator broad regression

必须先跑 targeted tests，再跑完整 broad regression。

至少覆盖：

- coordinator-first config validation；
- generated coordinator workflow；
- default choose-one aggregate 完全保留；
- product-ux generic route 不再由 research aggregate绕过；
- webapp-testing 在 coordinator 内可达但不是 design owner；
- research-product specialist route；
- aggregate metadata union；
- generated determinism；
- nested source rename；
- Windows path budget；
- Marketplace/generated parity；
- 056 F-A/F-B/F-C 不回归；
- whole unittest suite。

最低 broad commands 见 Execution Plan v0.3 Phase D。

### 10. Candidate-visible regression

建立少量 repo-safe、非 answer-shaped 的冻结 scenario，至少覆盖：

- S1 browser tiny fix；
- S3 no-Figma redesign；
- canonical-Figma material design change；
- native handoff action reachability；
- competing-route interaction claim；
- unsupported metric/ranking semantic claim；
- implementation drift should-not-change。

这些证明 production behavior，但不计 maturity。

### 11. Bobbio / Lucerna / Asteria final replay

只读，不修改三个项目。

final replay 前冻结：

- exact repo ref；
- neutral replay prompt；
- rubric；
- final candidate identity。

每次都从 normal Frontend Design entry 进入 coordinator，并保存真实 route/delegate consumption。

#### Bobbio

读取当前冻结 ref 的 canonical Figma/design authority 与 black-box review source。repo 已直接规定的行为只算 compatibility。

#### Lucerna

读取：

- `AGENTS.md`
- `docs/workflows/LUCERNA_VISUAL_ACCEPTANCE.md`
- `docs/design/lucerna/LUCERNA_UI_PRODUCT_SYSTEM_V1.md`
- `docs/design/lucerna/LUCERNA_EXTENSION_IDENTITY_STATUS_AUTH_V1.md`

这些项目本地已冻结的 product/UI/action/self-QA 答案只算 compatibility。

保留 01052 handoff-action-reachability regression；只有 repo-local source 未直接给答案，而 coordinator 自主触发 generic reachability/admission decision，才可计 plugin capability。

不要为了 replay 去控制用户当前 Lucerna 桌面。

#### Asteria

读取 accepted concepts 与 developer self-QA source，重点验证 browser/no-Figma should-not-overreach。

#### Attribution

每项写入：

```text
REPO_LOCAL_RULE_GAVE_ANSWER
COORDINATOR_GENERIC_DECISION_OBSERVED
COUNTS_AS_COMPATIBILITY
COUNTS_AS_PLUGIN_CAPABILITY
EVIDENCE_LOCATOR
```

若三者全部只能证明 compatibility，maturity 保持 `unclassified`。不要新增第四项目。

### 12. Handoff action reachability

如果最终报告要用户执行 UI action，且该动作能安全预演：

- 先证明可见；
- enabled；
- 可由真实 interaction 触发；
- 到达 expected next state / user-only boundary；
- 没有明显 P2。

不可替代的人类选择/credential/destructive action只验证到最后一个安全边界。

用户不是第一轮交互 QA。

### 13. Final-candidate 与版本纪律

当前 main 的明确版本基线：

- repository：5.3.0；
- web-development：0.2；
- maturity：unclassified。

本任务完成后必然改变正式 Frontend Design production behavior，因此**完成即必须发布新版本**。不要把本任务实现完成后仍保持 `web-development 0.2`。

如果当前 existing task 继续执行时 main/release baseline 仍是该基线，冻结预期 release：

```text
Repository: 5.3.0 -> 5.3.1
web-development: 0.2 -> 0.3
all other central plugins: NO_BUMP
maturity: unclassified (unchanged)
```

如果 kickoff-time main 已有其它正式 release：

- repository 使用 then-current compatible PATCH；
- web-development 使用 then-current two-part version 的下一 release；
- all other plugins NO_BUMP。

这只允许顺延基线，不允许选择 NO_BUMP。

执行时序：

1. 开发早期不要提前 bump；
2. implementation + known regression + broad compatibility 稳定后，重新读取 version policy 与 then-current source；
3. 写入本任务唯一一次 repository/plugin version bump；
4. 同步 web-development changelog、root CHANGELOG、README、VERSION、version tests、generated manifests；
5. regenerate；
6. freeze final candidate；
7. 所有 release-critical G1–G7 在这个同一、已经带最终版本 metadata 的 candidate 上重跑；
8. independent implementation review 若 REVISE，修同一 release candidate/version，不再次 bump。

如果 release gates 无法通过，任务保持未完成并返回 blocker。不得把已经改变的 production behavior 以 unchanged version 交付。

### 14. README / TODO / Board

README 是 mandatory closure check。

#52–#72 不能因为 Executor 完成、tests PASS 或 execution-ready Critic PASS 就关闭。

Maintenance Board 当前仍有 pending mutation；本 Executor 不伪称 Project 已同步。若当前执行 surface 恰好具备 Project mutation 且符合 Board policy，必须先满足其中 Clear Writing reader-facing mutation要求；本 Kickoff **不授权修改 Clear Writing production**。

### 15. Evidence

所有任务 evidence 留在：

`results/web-development--frontend-design-production-consolidation/`

不要只留 `/tmp`。

### 16. 在交 independent implementation review 前

必须：

- final candidate G1–G7 全部如实记录；
- exact reviewed branch commit/push；
- remote tip == intended local HEAD；
- raw replay outputs、route receipts、attribution、generated diff、tests、version/README closure均可达；
- 报告 remaining gates；
- 停止。

不要：

- merge main；
- update release ref；
- 宣布整体 Goal achieved。

独立 implementation review PASS 后仍需单独 integration authorization。

如果 review REVISE，继续同一个 task key / branch / worktree 修复；不要创建 successor。
