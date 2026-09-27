# Frontend Design Production Consolidation — Canonical Goal v0.1

执行包版本：`v0.1`  
任务键：`web-development--frontend-design-production-consolidation`  
目标仓库：`YuukiAS/AI_Skills_Collection`  
目标：`web-development` / Frontend Design  
已批准架构：`docs/design/frontend-design/FRONTEND_DESIGN_PRODUCTION_CONSOLIDATION_PROPOSAL_V0_3_2026-09-27.md` @ `effa02b4e7e02f012ea24bda1683857609a09fe1`  
Execution Plan：`docs/design/frontend-design/FRONTEND_DESIGN_PRODUCTION_CONSOLIDATION_EXECUTION_PLAN_V0_1_2026-09-27.md`  
源分支：`main`  
Execution-ready Critic：尚未 PASS  
当前 execution branch/worktree：尚未创建

计划获批后唯一允许的执行身份：

```text
task_key = web-development--frontend-design-production-consolidation
branch = reviewed/web-development--frontend-design-production-consolidation
worktree = /tmp/ai-skills-web-development-frontend-design-production-consolidation
```

本 Goal 在 independent execution-ready Critic 对同版 Plan + Goal + Kickoff 返回 PASS/READY_FOR_CODEX，并且用户随后发送该获批 Kickoff 之前，不构成执行授权。

---

## 1. 总目标

把 Frontend Design 从当前 `web-development 0.2` 的“正确规则分散存在、generated aggregate 仍平级任选 source、实际 review/evidence 闭环不完整”状态，收敛为一个可从正常插件入口使用的 production coordinator workflow。

Goal 真正完成后，必须同时成立：

1. generic Frontend Design normal entry 先进入 `frontend-visual-systems` coordinator；
2. coordinator 按任务规模、design authority、target surface、产品/状态风险委派现有 specialist；
3. generated payload 真正体现 coordinator-first，不只是 source 文档写了 coordinator；
4. 未启用新模式的其它 aggregate 仍保持原 choose-one contract；
5. `product-ux-planning` 不再通过 research aggregate 绕过 generic coordinator；
6. `research-product-frontend` 保持 research-specific specialist，而不是第二个 generic owner；
7. `webapp-testing` 是 browser evidence companion，不是 design owner；
8. `implementation-react-tailwind` 继续 downstream builder；
9. S1/S2/S3 + authority/surface scale-down 正常工作；
10. canonical Figma、其它 durable authority、无 Figma route 都可正确处理；
11. browser/native-WebView evidence 与 claim 对齐；
12. P1/P2/P3 producer self-QA 与 independent review admission 生效；
13. handoff action reachability 阻止“用户第一次发现按钮不能点”的 routine failure；
14. whole-product taste 能用可观察问题拒绝“功能正确但明显粗糙/拼装”的候选；
15. #52/#62/#69 retained semantics 完整保留；
16. Bobbio/Lucerna/Asteria replay 不把 repo-local contract 冒充 plugin capability；
17. 若三个真实 replay 都只能证明 compatibility，maturity 继续 `unclassified`；
18. 不新增第四个 synthetic maturity project；
19. Product UI Copy / Clear Writing deferred scope 未被偷跑；
20. README、version、changelog、generated parity 与 release evidence 最终一致。

---

## 2. 冻结实现方向

不得重新设计以下已获 architecture Critic PASS 的决定：

### Coordinator / topology

- `frontend-visual-systems` = 唯一 generic production coordinator；
- aggregate generator = 最小 opt-in `coordinator-first`；
- default aggregate = 原 choose-one 不变；
- 不新增 orchestrator Skill；
- main Frontend aggregate 收纳 generic delegates 和 `research-product-frontend` specialist；
- 当前独立 research aggregate 不再作为 generic Frontend Design 平级入口；
- `frontend-reference-research` 保持窄范围显式入口；
- `implementation-react-tailwind` 不并入 design owner。

### Workflow

保持：

- P0–P4；
- F-A / F-B / F-C / F-D；
- S1 / S2 / S3；
- design authority modifier；
- browser / native-WebView surface modifier；
- design defect / implementation drift / product semantic defect / runtime-only repair classification；
- conditional Figma；
- no-Figma 正常完成；
- tiny/local fix scale-down；
- handoff action reachability；
- P1/P2/P3 admission；
- whole-product taste observable questions。

---

## 3. 必须实现的 generator contract

在现有 aggregate generator 内实现一个 opt-in coordinator-first mode。

最小 source contract：

```text
routing_mode = coordinator-first
coordinator_artifact_id = <existing unique source artifact id>
```

要求：

- 未声明 `routing_mode` 的 aggregate 继续使用现有 choose-one；
- coordinator-first 的 `coordinator_artifact_id` 必须引用当前 `source_skills` 中真实存在且唯一的 artifact id；
- invalid/missing coordinator 配置 fail closed；
- generated coordinator aggregate 先读 coordinator source，再按 coordinator 委派 source；
- generated coordinator aggregate 不保留冲突的 choose-one normal-entry 文案；
- aggregate metadata union、secrets、scope、determinism、path budget 等现有 contract 不变。

Frontend Design main aggregate 使用 coordinator artifact `system`。

---

## 4. 必须实现的 Frontend source ownership

### coordinator

`skills/tools/frontend/frontend-visual-systems`

负责：

- P0–P4；
- F-A–F-D；
- S1–S3；
- authority/surface modifiers；
- delegate routing；
- repair routing；
- P1/P2/P3 admission；
- handoff action reachability；
- final convergence / independent review admission。

### delegates

- `product-ux-planning`：产品任务、state、actionability、lifecycle、visible semantics；
- `visual-direction`：whole-screen freeze、composition、taste；
- `design-system-tokens`：component/icon/typography/color/status grammar；
- `figma-design-to-code`：conditional Figma authority、complete、round-trip；
- `motion-interaction`：motion intent / runtime performance boundary；
- `responsive-accessibility-review`：适用的 P1/P3 closure；
- `webapp-testing`：browser evidence companion；
- `research-product-frontend`：research-specific specialist；
- `implementation-react-tailwind`：downstream builder only；实现发现 design gap 返回 P0/P1。

不要把相同 contract 复制到每个 skill。

---

## 5. Capability Gates

同一 final candidate 必须直接通过 Execution Plan v0.1 的 G1–G7：

- G1：Normal Entry / Coordinator Routing；
- G2：Coordinator Decision / Scale / Authority；
- G3：Visual-System / Ownership Fidelity；
- G4：Evidence Fidelity / Producer Admission；
- G5：Shared Generator Should-Not-Change / Generated Parity；
- G6：Bobbio / Lucerna / Asteria Real Replay + Attribution；
- G7：Final Candidate / Release Metadata / Human-Facing Closure。

机械 tests 不替代 G3/G4/G6 的实际行为和独立判断。

---

## 6. Replay contract

### 6.1 不新增第四个项目

本任务真实项目 replay 固定为：

- Bobbio；
- Lucerna；
- Asteria。

Mica for ChatGPT、SeminarArc 可作为未来自然真实使用证据，但不在本任务为 maturity 人为制造 replay。

### 6.2 每个 replay 的 production identity

必须使用：

- exact final candidate；
- 正式 candidate plugin identity；
- normal Frontend Design entry；
- coordinator-first route；
- 实际 source/delegate consumption evidence。

### 6.3 Attribution

每个 replay 必须区分：

```text
COMPATIBILITY / REGRESSION EVIDENCE
PLUGIN-ORIGINATED CAPABILITY EVIDENCE
```

只有 repo-local contract 没有直接给答案，而 coordinator 自主作出的 generic P0/P1/P3/F-D decision 才可计 plugin capability。

### 6.4 Lucerna authority

Lucerna replay 至少读取冻结 ref 下：

- `AGENTS.md`
- `docs/workflows/LUCERNA_VISUAL_ACCEPTANCE.md`
- `docs/design/lucerna/LUCERNA_UI_PRODUCT_SYSTEM_V1.md`
- `docs/design/lucerna/LUCERNA_EXTENSION_IDENTITY_STATUS_AUTH_V1.md`

上述 source 已直接冻结的行为只算 compatibility。01052 handoff-action-reachability 继续是 regression，但不得偷算 maturity。

---

## 7. Evidence 与结果目录

任务 evidence 必须保存在：

`results/web-development--frontend-design-production-consolidation/`

至少包含：

- final candidate identity；
- targeted test summary；
- generator should-not-change report；
- generated parity report；
- candidate-visible deterministic replay inputs/outputs；
- Bobbio/Lucerna/Asteria exact ref + replay prompt + raw response；
- coordinator/delegate route-consumption receipt；
- replay attribution adjudication；
- version/changelog/README closure report；
- independent review handoff manifest。

不把任务证据只留 `/tmp`。

---

## 8. 版本与 maturity

当前 planning evidence：

- repository current version：`5.3.0`；
- web-development current version：`0.2`；
- maturity：`unclassified`。

这不是未来版本授权。

### Plan-time decision

```text
Repository bump decision: NONE
Reason: execution package 尚未实现或形成正式 release。

Affected plugins:
- web-development: NO_BUMP
- all other central plugins: NO_BUMP
```

### Final-candidate conditional decision

只有当实际 production behavior 改变、原 failure regression PASS、broad compatibility PASS、准备形成正式 release candidate 时：

- 从 then-current repository version 做 compatible PATCH；
- `web-development` 从 then-current 两段版本推进到下一两段版本，exactly once；
- all other plugins NO_BUMP；
- maturity 仍 `unclassified`；
- 同步 plugin changelog、root CHANGELOG、README、VERSION、version tests、generated manifests。

如果 kickoff/integration 前 main 已有其它 release，必须从 then-current source 计算，不能硬编码覆盖并发历史。

如果最终没有形成 production behavior release，则 NO_BUMP。

---

## 9. README 与 TODO closure

README 是显式 closure gate。

如果 Frontend Design 正常入口、能力描述、version 或用户可观察 workflow 改变，README 必须在同一 release candidate 更新，并与 source/config/generated payload 一致。

#52–#72：

- architecture PASS 不关闭；
- execution-ready PASS 不关闭；
- Executor 自报完成不关闭；
- implementation review PASS 后，只有当对应真实能力、replay、release closure 全部成立时才按维护政策更新/关闭。

Deferred Product UI Copy heading 不属于本 task。

---

## 10. 权限范围

只有用户发送获批 Kickoff 后，才授权：

- ordinary fetch/read `YuukiAS/AI_Skills_Collection`；
- 创建 exact branch：
  `reviewed/web-development--frontend-design-production-consolidation`；
- 创建 exact worktree：
  `/tmp/ai-skills-web-development-frontend-design-production-consolidation`；
- 修改 Goal/Plan 明确允许的 AI_Skills source、generator、config、tests、generated layer；
- repo-safe deterministic regressions；
- Bobbio/Lucerna/Asteria read-only replay；
- candidate plugin install/replay 所需的现有正常工具；
- existing zero-paid CI；
- ordinary non-force commits/push 到 exact reviewed branch；
- repo 内 evidence、README/changelog/version closure。

不授权：

- merge main；
- update release ref；
- force push/rebase/history rewrite；
- branch deletion；
- destructive Git；
- Clear Writing production 修改；
- Product UI Copy scope；
- Bridge Kit 修改；
- paid reviewer/API；
- 新 credential/provider/private-data scope；
- 修改 Bobbio/Lucerna/Asteria/Mica/SeminarArc；
- unrelated repo mutation。

---

## 11. 执行阶段与 Goal 完成语义

本 Goal 是整体 completion contract，不把某个子阶段 PASS 当 overall achieved。

顺序：

1. execution-ready Critic PASS；
2. 用户发送 approved Kickoff；
3. 创建 exact task branch/worktree；
4. implementation + targeted regression；
5. broad generated/whole-repo regression；
6. development replay；
7. conditional release metadata + final-candidate freeze；
8. G1–G7 同 final candidate PASS；
9. push exact reviewed branch；
10. independent implementation review；
11. 若 REVISE，同 task 修复；
12. 若 PASS，等待单独 integration authorization；
13. integration/release closure；
14. TODO/board/release truth closure。

当前 Kickoff 只授权到第 9 步，**不授权第 12–14 步的 main/release mutation**。

在 independent implementation review 与必要 integration/release closure 尚未完成前：

`GOAL_ACHIEVED = NO`

---

## 12. 停止条件

如果实现需要以下任一变化，立即停止返回 Planner/Critic：

- 新 orchestrator Skill；
- 改 P0–P4、F-A–F-D、S1–S3；
- 把 Product UI Copy/Clear Writing 拉入本轮；
- 修改 Bridge Kit；
- 修改真实 replay 项目 source；
- 增加第四 maturity replay project；
- paid review；
- 新 credential/provider/data scope；
- force/destructive Git；
- shared generator 无法用最小 opt-in extension 保持其它 aggregate 行为；
- approved architecture 被真实证据证明不成立。

普通实现 bug、tests、generator error、replay暴露的本 scope plugin defect由 Executor自行修复，不把用户当调试人员。
