# Frontend Design Production Consolidation — Kickoff Draft v0.1

只在 independent execution-ready Critic 对以下同版执行包返回 PASS / READY_FOR_CODEX 后使用：

- `docs/design/frontend-design/FRONTEND_DESIGN_PRODUCTION_CONSOLIDATION_EXECUTION_PLAN_V0_1_2026-09-27.md`
- `docs/goals/FRONTEND_DESIGN_PRODUCTION_CONSOLIDATION_GOAL_V0_1.md`
- 本 Kickoff Draft v0.1

用户发送获批 Kickoff 后，才构成 branch/worktree 与实现授权。

---

## Kickoff

Repository:

`YuukiAS/AI_Skills_Collection`

Exact task identity:

```text
task_key = web-development--frontend-design-production-consolidation
branch = reviewed/web-development--frontend-design-production-consolidation
worktree = /tmp/ai-skills-web-development-frontend-design-production-consolidation
```

Approved architecture:

`docs/design/frontend-design/FRONTEND_DESIGN_PRODUCTION_CONSOLIDATION_PROPOSAL_V0_3_2026-09-27.md`

Approved architecture commit:

`effa02b4e7e02f012ea24bda1683857609a09fe1`

Canonical Goal:

`docs/goals/FRONTEND_DESIGN_PRODUCTION_CONSOLIDATION_GOAL_V0_1.md`

Execution Plan:

`docs/design/frontend-design/FRONTEND_DESIGN_PRODUCTION_CONSOLIDATION_EXECUTION_PLAN_V0_1_2026-09-27.md`

这是 implementation kickoff，不是重新设计架构。

### 1. Bootstrap

开始时：

1. fetch 最新 `origin/main`；
2. 验证当前 repo identity / remote / clean compatible source；
3. 验证最新 main 仍包含上述 approved architecture 与 v0.1 Plan/Goal/Kickoff；
4. 重新读取当前：
   - `AGENTS.md`
   - Planner/Critic role contract
   - `PLUGIN_CAPABILITY_GATE_POLICY.md`
   - `AI_SKILLS_MAINTENANCE_BOARD.md`
   - `PLUGIN_VERSIONING_AND_CHANGELOGS.md`
   - approved Proposal v0.3
   - Canonical Goal v0.1
   - Execution Plan v0.1
   - target frontend source/config/generator/tests
5. 按中央 production plugin refinement contract 使用：
   - `workflow-core`
   - `ai-skills-core`
   - `web-development`
6. 如果 kickoff-time main 对 target Frontend/generator/version policy 有会改变批准实现语义的 drift，停止返回 Planner，不静默覆盖。

只有 preflight compatible 后，才从 kickoff-time verified `origin/main` 创建：

- `reviewed/web-development--frontend-design-production-consolidation`
- `/tmp/ai-skills-web-development-frontend-design-production-consolidation`

不得使用其它 branch/worktree，也不得创建第二个 fallback clone。

### 2. 必须实现的 normal-entry coordinator

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

### 3. 必须保留的 Frontend contract

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

### 4. Generator contract

按 Plan v0.1 实现：

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

### 5. Source ownership

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

### 6. 明确 deferred / forbidden

不得修改或实现：

- Clear Writing / writing-style production；
- Product UI copy content-architecture deferred heading；
- writing-style #17；
- writing-style #20；
- writing-style #13；
- CUHK Date Product UI Copy naturalness；
- Bridge Kit；
- Host Policy / execpolicy；
- Bobbio/Lucerna/Asteria/Mica/SeminarArc source；
- unrelated repo；
- paid reviewer/API；
- 新 provider/credential/private-data scope；
- force push / rebase / history rewrite / branch deletion；
- merge main；
- update release ref。

如果必须扩这些 scope 才能继续，停止返回 Planner/Critic。

### 7. Tests 与 generator broad regression

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

最低 broad commands 见 Plan v0.1 Phase D。

### 8. Candidate-visible regression

建立少量 repo-safe、非 answer-shaped 的冻结 scenario，至少覆盖：

- S1 browser tiny fix；
- S3 no-Figma redesign；
- canonical-Figma material design change；
- native handoff action reachability；
- competing-route interaction claim；
- unsupported metric/ranking semantic claim；
- implementation drift should-not-change。

这些证明 production behavior，但不计 maturity。

### 9. Bobbio / Lucerna / Asteria final replay

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

### 10. Handoff action reachability

如果最终报告要用户执行 UI action，且该动作能安全预演：

- 先证明可见；
- enabled；
- 可由真实 interaction 触发；
- 到达 expected next state / user-only boundary；
- 没有明显 P2。

不可替代的人类选择/credential/destructive action只验证到最后一个安全边界。

用户不是第一轮交互 QA。

### 11. Final-candidate 与版本纪律

当前 main 观察值不是最终授权：

- repository 当前：5.3.0；
- web-development 当前：0.2。

开发期间不要提前 bump。

只有 implementation + known regression + broad compatibility 稳定，并准备冻结正式 release candidate 时：

1. 重读 version policy 与 then-current source；
2. 若确属 production behavior release：
   - repository 做 then-current compatible PATCH；
   - web-development 做 then-current 两段版本的下一 release，exactly once；
   - all other plugins NO_BUMP；
   - maturity 仍 unclassified；
3. 更新 web-development changelog、root CHANGELOG、README、VERSION、version tests；
4. regenerate；
5. freeze final candidate；
6. 所有 release-critical G1–G7 在该 same final candidate 上重跑。

若不能形成正式 release，NO_BUMP，并如实报告。

### 12. README / TODO / Board

README 是 mandatory closure check。

#52–#72 不能因为 Executor 完成、tests PASS 或 execution-ready Critic PASS 就关闭。

Maintenance Board 当前仍有 pending mutation；本 Executor 不伪称 Project 已同步。若当前执行 surface 恰好具备 Project mutation 且符合 Board policy，必须先满足其中 Clear Writing reader-facing mutation要求；本 Kickoff **不授权修改 Clear Writing production**。

### 13. Evidence

所有任务 evidence 留在：

`results/web-development--frontend-design-production-consolidation/`

不要只留 `/tmp`。

### 14. 在交 independent implementation review 前

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
