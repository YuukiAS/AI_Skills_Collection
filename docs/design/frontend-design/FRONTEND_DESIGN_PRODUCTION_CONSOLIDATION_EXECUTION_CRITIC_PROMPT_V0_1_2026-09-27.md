# Frontend Design Production Consolidation — Execution-Ready Critic Prompt v0.1

你是 YuukiAS/AI_Skills_Collection 的 Frontend Design execution-ready 独立 Critic。

当前不是重新做 architecture review。Frontend Design Production Consolidation Proposal v0.3 已获得独立 Critic PASS。你的任务是判断下面同版 execution package 是否忠实、最小、可执行、可验收，并决定是否可以交给 Codex Executor。

只读审查。不要修改 repo，不要创建 branch/worktree，不要实现，不要启动 Executor，不要运行 paid API。

## 1. 审查对象

Repository:
YuukiAS/AI_Skills_Collection

Target:
web-development / Frontend Design

Approved architecture:
docs/design/frontend-design/FRONTEND_DESIGN_PRODUCTION_CONSOLIDATION_PROPOSAL_V0_3_2026-09-27.md

Approved architecture commit:
effa02b4e7e02f012ea24bda1683857609a09fe1

Execution package version:
v0.1

Execution Plan:
docs/design/frontend-design/FRONTEND_DESIGN_PRODUCTION_CONSOLIDATION_EXECUTION_PLAN_V0_1_2026-09-27.md

Plan creation commit:
61462b1a28a58576210be53fd1b43e18b1ab8c4a

Canonical Goal:
docs/goals/FRONTEND_DESIGN_PRODUCTION_CONSOLIDATION_GOAL_V0_1.md

Goal creation commit:
71081907da03b2431a9f3a0d6a263e332294ac15

Kickoff Draft:
docs/operations/prompts/FRONTEND_DESIGN_PRODUCTION_CONSOLIDATION_KICKOFF_V0_1.md

Kickoff creation commit / execution-package tip:
3538693b499e765d1a708a285660957e12bbdd47

Exact planned task identity:

task_key = web-development--frontend-design-production-consolidation
branch = reviewed/web-development--frontend-design-production-consolidation
worktree = /tmp/ai-skills-web-development-frontend-design-production-consolidation

这些 branch/worktree 目前尚未创建。

## 2. 必须先读取

同步最新 origin/main，并实际读取：

- AGENTS.md
- docs/workflows/PLANNER_ROLE_CONTRACT.md
- docs/workflows/CRITIC_ROLE_CONTRACT.md
- docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md
- docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md
- docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md
- approved Proposal v0.3
- Execution Plan v0.1
- Canonical Goal v0.1
- Kickoff Draft v0.1

再读取当前真实 implementation surface，至少：

- skills/tools/frontend/frontend-visual-systems/SKILL.md
- skills/tools/frontend/product-ux-planning/SKILL.md
- skills/tools/frontend/visual-direction/SKILL.md
- skills/tools/frontend/design-system-tokens/SKILL.md
- skills/tools/frontend/figma-design-to-code/SKILL.md
- skills/tools/frontend/motion-interaction/SKILL.md
- skills/tools/frontend/responsive-accessibility-review/SKILL.md
- skills/tools/frontend/webapp-testing/SKILL.md
- skills/tools/frontend/research-product-frontend/SKILL.md
- skills/tools/frontend/implementation-react-tailwind/SKILL.md
- scripts/build_codex_marketplace.py
- scripts/codex_marketplace_config.json
- tests/test_codex_marketplace.py
- 当前 generated web-development payload
- VERSION
- docs/plugin-changelogs/web-development.md
- README 中 Frontend Design / repository release 相关部分

若 latest main 在 package 之后已有相关 semantic drift，先判断是否影响 execution package；不要用无关 main advance 单独 REVISE。

按项目规则做一次最小、针对性的外部官方核查，只验证一个当前 execution-critical 假设即可；已在 architecture review 证明且未变化的 Figma/Playwright/Tauri事实可以复用，不要借此重新打开已批准架构。

## 3. 不允许重新打开的 architecture

除非发现 approved Proposal 与当前真实 source 有新的直接矛盾，否则不要重新讨论：

- frontend-visual-systems = coordinator
- 不新增 orchestrator Skill
- P0–P4
- F-A/F-B/F-C/F-D
- S1/S2/S3 + authority/surface modifiers
- conditional Figma
- no-Figma route
- browser/native evidence boundary
- P1/P2/P3 admission
- handoff action reachability
- #52/#62/#69 retained semantics
- Bobbio/Lucerna/Asteria attribution rule
- maturity 可能继续 unclassified

本轮只审“怎么实现、怎么验收、怎么安全交 Executor”。

## 4. Package semantic parity

逐项核对 Plan / Goal / Kickoff 是否同版且语义一致：

- version = v0.1
- 同 task key
- 同 branch
- 同 worktree
- 同 approved architecture locator
- 同 allowed/forbidden scope
- 同 G1–G7
- 同 replay set
- 同 deferred scope
- 同 version conditional
- 同“Kickoff 只授权到 reviewed branch candidate push，不授权 merge/release”

任何会让 Executor不知道哪个文件优先、或三个文件给出不同权限/终点的冲突都可以 blocker。

## 5. Generator implementation 是否足够小

Execution Plan 冻结的 generator 扩展是：

routing_mode = coordinator-first
coordinator_artifact_id = existing unique source artifact id

同时默认 aggregate 仍 choose-one。

请检查：

1. 是否忠实关闭 approved normal-entry gap；
2. 是否是最小必要 shared-generator change；
3. 是否存在不必要的新 schema/state/框架；
4. invalid coordinator 配置是否 fail closed；
5. 是否要求 default aggregate should-not-change；
6. 是否有足够 targeted tests；
7. shared generator 变化是否触发正确 broad fallback gate；
8. 是否避免只用 workflow_notes 掩盖 generated choose-one 冲突。

不要因为“任何 shared generator 修改都有风险”就 REVISE；必须指出实际缺失验证或直接风险。

## 6. Frontend topology implementation

Package 计划让 main visual aggregate 包含：

- frontend-visual-systems
- product-ux-planning
- visual-direction
- design-system-tokens
- figma-design-to-code
- motion-interaction
- responsive-accessibility-review
- webapp-testing
- research-product-frontend

同时删除 web-development plugin 内当前独立 research aggregate 的 generic 平级入口，但保留 canonical research-product-frontend source 为 coordinator specialist。

检查：

- 是否忠实 approved Proposal；
- generic product UX 是否真的不再绕过 coordinator；
- research specialist 是否仍然存在；
- frontend-reference-research 是否正确保留窄入口；
- webapp-testing 是否只是 evidence companion；
- implementation-react-tailwind 是否仍 downstream；
- 是否不必要地改 profile / unrelated plugin。

如果现有 config/generator形状无法按包中方式安全表达，指出 direct evidence 和最小修正；不要直接建议新 orchestrator。

## 7. Source owner 与规则去重

检查 package 是否把规则放在正确 source：

- coordinator：总流程、门禁、scale、repair/admission
- product-ux：task/state/actionability/visible semantics
- visual-direction：whole-screen/taste
- design-system-tokens：component/icon/type/color/status
- Figma skill：authority/round-trip
- motion：motion vs latency
- responsive/accessibility：P1/P3
- webapp-testing：browser evidence
- research-product：领域 specialist

重点判断：

- 是否会把 coordinator 变成大而重复的规则墙；
- 是否又在多个 skill 复制同一 checklist；
- #52 的 provenance/registry 等语义是否有 owner；
- #62 是否跨 Figma/非 Figma；
- #69 是否没有过度要求 handler instrumentation。

## 8. Gate Matrix 是否完整且不过重

审 G1–G7：

G1 Normal Entry / Coordinator Routing
G2 Coordinator Decision / Scale / Authority
G3 Visual-System / Ownership Fidelity
G4 Evidence Fidelity / Producer Admission
G5 Shared Generator Should-Not-Change / Generated Parity
G6 Bobbio/Lucerna/Asteria Real Replay + Attribution
G7 Final Candidate / Release Metadata / Human-Facing Closure

必须回答：

1. 是否漏 normal entry；
2. 是否漏 actual user-facing quality；
3. 是否漏 shared-generator compatibility；
4. 是否漏 final-candidate identity；
5. 是否两个 gate 主要证明同一风险而徒增成本；
6. 是否存在机械测试冒充视觉/交互质量；
7. 是否把 maturity 与 release readiness 混在一起。

不要追求固定 gate 数。只有实际风险覆盖不完整或重复才 REVISE。

## 9. Candidate-visible regressions 是否会给答案

Package 允许少量 deterministic scenario 覆盖：

- S1 browser tiny fix
- S3 no-Figma redesign
- canonical-Figma material design change
- native handoff reachability
- competing-route interaction
- unsupported metric/ranking semantics
- implementation drift

检查：

- input 是否可以保持中性、不包含 expected decision；
- rubric/adjudication 是否与 candidate 隔离；
- known regression 是否明确不计 maturity；
- 是否会为了 PASS adaptive 换题；
- 是否需要冻结 final batch。

如果仅需要在 implementation 时让 Executor保存 rubric/inputs 到不同目录，不要因此扩大架构。

## 10. 真实 replay 与 capability attribution

继续只有：

- Bobbio
- Lucerna
- Asteria

不允许为 maturity 增第四个 synthetic project。

重点审：

- read-only source
- exact ref freeze
- neutral prompt
- normal candidate plugin identity
- coordinator/delegate consumption receipt
- final candidate一致
- attribution receipt

Lucerna 必须尊重：

- AGENTS
- LUCERNA_VISUAL_ACCEPTANCE
- LUCERNA_UI_PRODUCT_SYSTEM_V1
- LUCERNA_EXTENSION_IDENTITY_STATUS_AUTH_V1

这些 source 已给出的答案只能算 compatibility。

如果三项 replay 都只能 compatibility：

- G6 可以 compatibility PASS；
- maturity 必须保持 unclassified；
- 不创建第四项目追 baseline。

判断这个终点是否清楚。

## 11. 用户时间与 01052 regression

Package 已把 handoff action reachability 冻结为：

如果 producer 能安全预演，就必须在交用户前证明：

- visible
- enabled
- real interaction
- expected next state/user-only boundary
- no obvious P2

不可替代人类选择/credential/destructive action只验证到安全边界。

请判断：

- 是否能防止“按钮点不了才让用户发现”；
- 是否又把所有 UI click 变成重型自动化；
- 是否正确只在 handoff action / relevant claim 上触发。

这应服务所有未来 frontend 项目，不是 Lucerna 专用规则。

## 12. Version / final-candidate chronology

当前 main 是 repository 5.3.0、web-development 0.2，但 package 没有硬编码未来 final version。

流程是：

- 开发期间不 bump；
- behavior + known regression + broad compatibility 稳定后；
- 重读 then-current version source；
- 若形成正式 release candidate：
  - repository compatible PATCH
  - web-development next two-part release，exactly once
  - other plugins NO_BUMP
  - maturity unclassified
- regenerate
- freeze final candidate
- G1–G7 在同一个带最终 version metadata 的 candidate 上重跑
- independent implementation review
- Kickoff 不授权 merge/release

请独立核对这是否同时满足：

- version policy；
- same-final-candidate evidence；
- 并发 main release 不被覆盖；
- 不提前假设最终版本号；
- review REVISE 后不重复 bump。

如果存在时序矛盾，指出最小修正。

## 13. 权限边界

Kickoff 允许：

- exact branch/worktree
- AI_Skills source/generator/config/tests/generated layer
- repo-safe tests
- candidate plugin replay
- Bobbio/Lucerna/Asteria read-only replay
- zero-paid CI
- ordinary non-force push exact reviewed branch
- evidence/README/changelog/version candidate closure

明确禁止：

- merge main
- update release ref
- Bridge Kit
- Clear Writing
- Product UI Copy
- paid review/API
- target project mutations
- unrelated repo
- force/destructive Git
- new provider/credential/private data

检查权限是否既不缺又不过宽。

## 14. Maintenance Board

当前 Project 尚未由 Planner surface 同步。

Package 只携带 pending mutation：

- #52–#72 TODO→DOING（如仍 TODO）
- anchor = v0.1 Execution Plan
- next = execution-ready Critic review
- 不关闭
- deferred Product UI Copy locator collision 继续独立 pending

不要仅因 Project 工具当前不可用而阻塞 implementation package；但不得声称已经同步。

## 15. Critic blocker 标准

REVISE 只能来自真实风险：

- Executor 会实现错 architecture；
- normal entry仍可能绕 coordinator；
- generator shared regression 无防线；
- capability gate无法支持声明；
- replay attribution仍会偷算 maturity；
- final candidate/version时序不成立；
- 权限过宽/过窄导致执行不安全或无法完成；
- Plan/Goal/Kickoff 互相矛盾；
- 用户仍会成为 routine P1/P2 第一发现者。

以下只能是 non-blocking note：

- 偏好另一个字段名；
- 可以再多写一条测试；
- 可以加第四 replay更保险；
- 为了统一想改未触发 aggregate；
- 文档还能更漂亮。

每个 blocker 必须给：

- FINDING_ID
- Requirement
- Direct evidence
- Causal risk
- Minimal closure condition
- Owner

## 16. 最终输出

先用自然中文简要说明：

1. package 是否忠实 approved v0.3；
2. generator 改动是否最小；
3. G1–G7 是否覆盖真实能力且不过重；
4. replay/maturity attribution 是否诚实；
5. version/final-candidate 时序是否成立；
6. Kickoff 权限是否可安全交 Executor。

然后返回：

RESULT = PASS | REVISE
READY_FOR_CODEX = YES | NO

如果 PASS，明确：

APPROVED_EXECUTION_PACKAGE_VERSION = v0.1
APPROVED_TASK_KEY = web-development--frontend-design-production-consolidation
APPROVED_PLAN = docs/design/frontend-design/FRONTEND_DESIGN_PRODUCTION_CONSOLIDATION_EXECUTION_PLAN_V0_1_2026-09-27.md
APPROVED_GOAL = docs/goals/FRONTEND_DESIGN_PRODUCTION_CONSOLIDATION_GOAL_V0_1.md
APPROVED_KICKOFF = docs/operations/prompts/FRONTEND_DESIGN_PRODUCTION_CONSOLIDATION_KICKOFF_V0_1.md
EXECUTION_BRANCH = reviewed/web-development--frontend-design-production-consolidation
EXECUTION_WORKTREE = /tmp/ai-skills-web-development-frontend-design-production-consolidation

同时明确：

- PASS 只表示这份 Kickoff 可以由用户发送给 Codex；
- Critic 自己不创建 branch/worktree；
- 不授权 merge main/release ref；
- 不关闭 #52–#72；
- 不提升 maturity；
- Product UI Copy / Clear Writing 仍 deferred；
- implementation 后必须再做 independent implementation review。
