# Critic Review Request — Presentations 双模板生产架构重设计 V1.1

你是 AI Research Stack 的独立 Critic thread。本轮是同一 major round 的 V1.1 复核，不是新任务。只做架构、TODO disposition、Capability Gate 与 implementation-stage 审查。

不要实现代码。
不要修改 production plugin。
不要创建 Executor task。
不要创建 execution branch/worktree。
不要运行付费 review。
不要发布。

## Active Review Context

target_repo = YuukiAS/AI_Skills_Collection
target_plugin_or_domain = presentations
design_topic_or_task_key = presentations--two-template-production-redesign
review_stage = architecture_revision_review_v1_1
source_branch_or_ref = main

previous proposal:
docs/design/PRESENTATIONS_TWO_TEMPLATE_PRODUCTION_REDESIGN_PLAN_V1_0_2026-09-28.md
@ 78901482243a877cdcec3150ca229b3fa58b7173

previous Critic review:
results/presentations--two-template-production-redesign/CRITIC_REVIEW_V1.md
@ 21c739b270105c222f523fd5625993fa5902e00f

revised proposal:
docs/design/PRESENTATIONS_TWO_TEMPLATE_PRODUCTION_REDESIGN_PLAN_V1_1_2026-09-28.md
@ f71e97c06938ab2ce175ccf3b4ac19da9309fda1

Planner response:
results/presentations--two-template-production-redesign/PLANNER_RESPONSE_V1_1.md
@ b7b6499f4ac2cbd50c19f12005ac24b66cbd0b48

execution_branch = NOT_CREATED
execution_worktree = NOT_CREATED

## 必须先实际读取

从最新 main 重新读取必要 source：

- AGENTS.md
- docs/workflows/PLANNER_ROLE_CONTRACT.md
- docs/workflows/CRITIC_ROLE_CONTRACT.md
- docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md
- docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md
- docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md
- docs/plugin-todos/presentations.md
- scripts/codex_marketplace_config.json 中 presentations entry
- profiles/presentation-desktop.json
- skills/tools/documents-media/presentations/research-presentations/SKILL.md
- skills/tools/documents-media/presentations/business-presentations/SKILL.md
- skills/tools/documents-media/presentations/shared/template-routing.md
- skills/tools/documents-media/presentations/shared/ppt-skill-routing.md
- V1.1 proposal
- Planner response V1.1
- 上一轮 Critic review

V1.0、旧 V0.2、045 只在需要核对历史语义时读取，不要重新把旧计划当 authority。

## 本轮审查优先级

这是 REVISE 后复核。必须先逐项复核旧 blocker：

- PRES-V1-F01
- PRES-V1-F02
- PRES-V1-F03
- PRES-V1-F04

只有出现以下情况才新增 blocker：
- 新事实；
- 上轮遗漏的关键真实风险；
- V1.1 修订引入的新回归。

不要移动终点。

## PRES-V1-F01 复核要求

上一轮要求统一 Presentations 前门绑定真实 consumer，并保护 business/editable route。

请核对 V1.1 是否已经冻结完整因果链：

natural presentation request
-> installed Presentations plugin discovery/intake
-> mode + deliverable + template decision
-> shared core / local-edit fast path
-> official Presentation/Slides 或 Beamer adapter
-> artifact/render QA

重点检查：

1. scripts/codex_marketplace_config.json 是否被正确定位为 canonical plugin interface/packaging source；
2. research/business source skills + shared routing 是否成为内部 dispatch authority；
3. presentation-desktop 是否被正确限制为 installation/composition profile，而不是第二套路由 authority；
4. generated layers 是否保持 generator-only；
5. minor/local edit 是否是“仍进 Presentations intake，但不跑 full planning”，而不是绕过 plugin；
6. routing matrix 是否明确保护：
   - research no-format -> cuhk-research Beamer；
   - teaching no-format -> course-standard Beamer；
   - business/executive no-format -> editable PPTX/Slides；
   - explicit PPTX/Slides -> official editable adapter；
   - existing deck -> preserve current format/template；
   - local edit -> preserve current format/template + fast path；
   - external locked template -> pass-through，不进入 built-in registry；
7. G1 是否要求真实安装后的 natural request，而非 helper/fixture。

若你认为当前平台的 plugin discovery 不能由这些 existing surfaces真正实现，请给直接 source/平台证据，并说明最小关闭条件。不要自行新增顶级 skill/plugin 或 implicit-invocation hack。

## PRES-V1-F02 复核要求

核对 canonical TODO 当前 maturity 与 V1.1 disposition：

- #44 必须继续 BLOCKED_NEEDS_EVIDENCE；
- #45–#48 必须继续 CANDIDATE_GENERIC，除非有直接新 evidence 满足各自 canonical promotion gate；
- V1.1 可以复用 045 或 #29–#43 已正式/真实支持的机制；
- 不能因为相关机制存在就宣布 #45–#48 solved/promoted；
- implementation stages 不得偷偷包含 #44–#48 专属新机制。

特别审查：

#45：
不能把已有 colour/scale/first-use 回归重新包装成新的 deck-wide consistency engine。

#46：
不能因为 Stage 3 有公式尺度检查，就声称建立完整 math/theory hierarchy contract。

#47：
不能因为有 simulation regression，就新增 simulation-specific schema/layout contract。

#48：
045 English final pass 与 #29/#31/#34 handoff 可继续，但不能等于更广泛 natural scientific slide language promotion。

## PRES-V1-F03 复核要求

审查新的 Gate taxonomy 是否真正收敛。

Product Gates：
- G1 normal-entry routing；
- G2 semantic dependency/storyline；
- G3 generic composition/readability；
- G4 domain/scientific-object representation；
- G5 template actual consumption + visual fidelity；
- G6 citation/bibliography/text-layer delivery；
- G7 existing-deck revision/preservation；
- G8 final language/spoken reader effort；
- G9 cross-mode normal-entry/generalization/production integration。

Horizontal rules：
- H1 scope-honest independent review；
- H2 same-final-candidate / no stitching；
- H3 regression/fresh-evidence integrity；
- H4 source/runtime/render identity。

检查：

1. G2 是否只判 semantic order、dependency、first-use、page job，而不重新判语言 polish；
2. G8 是否只判 final wording/spoken reader effort，而不重复判 page order；
3. G3/G4 是否仍证明不同能力；
4. G5 是否用两个不可互相抵消的 evidence stream：
   - actual canonical template consumption；
   - visual fidelity；
5. G9 是否只负责 cross-mode/generalization/production integration；
6. README/changelog/version/Marketplace/profile closure 是否已退出 product Gate；
7. H1/H2 是否真的横向约束所有相关 Gate，而不是又形成隐形产品 Gate；
8. taxonomy 是否仍存在重复、过重或可被 control artifacts 钻空子的地方。

不要为了数字好看机械增加/删除 Gate。

## PRES-V1-F04 复核要求

V1.1 现在分成六个 implementation stages：

1. Front door + routing + two-template adapter foundation
2. Semantic sequence core
3. Composition + approved visual/object regressions
4. Citation/text layer + final language handoff
5. Existing-deck revision runtime + preservation
6. Cross-mode integration/generalization + release closure

逐阶段检查：

- 是否新增一个可观察的真实用户能力；
- dependency 是否清楚；
- stop condition 是否能及时阻止错误方向；
- recovery 是否能独立回滚；
- failure 是否能定位到责任层；
- 是否把 candidate-only TODO 提前实现；
- 是否仍然过大到不适合独立 execution package。

特别检查：

Stage 1：
模板 adapter foundation 是否会在 semantic core前错误冻结一个 universal composition schema。V1.1 明确 Stage 1 不实现 universal composition contract；确认这足够。

Stage 2：
是否严格停留在 semantic sequence，不承担 layout。

Stage 3：
是否只实现已经有真实 evidence 的 composition/object regressions；#44–#47 不得借机扩 scope。

Stage 4：
如果 Clear Writing/scientific-prose 本身失败，是否正确返回 writing owner，而不是顺手修改 writing-style。

Stage 5：
是否是真正 diagnose -> edit -> render -> compare runtime，而不是 packet validator再包装。

Stage 6：
release closure 是否只是 closure；不能用 metadata PASS 掩盖 G1–G8 failure。

## 保留上一轮已接受结论

除非 V1.1 引入新证据或回归，不要重新争论：

- exactly two built-in templates；
- external locked input不进入 built-in registry；
- existing-deck保留原模板；
- strict semantic-storyboard/page-composition boundary；
- teaching作为 shared-core mode；
- research/business trigger至少保留一个 compatibility release；
- #43 merged into #33；
- #44 evidence-gated；
- 045-promoted failures继续作为 regression bank；
- Beamer 主路线；
- 本轮不迁移 ltx-talk；
- course-standard template fidelity与 teaching readability分开验收。

## TODO completeness review

逐项检查 #29–#48：

- 每项是否都有 truthful disposition；
- #29 子项是否被显式映射，而非一行吞掉；
- NEW items是否进入有证据支持的 stage/gate；
- candidate/evidence-gated items是否保持 maturity truth；
- #43 merge是否保留 slide source role house style；
- 045 regressions是否仍在 bank；
- 是否因为“覆盖全部 TODO”又出现规则堆叠。

## Normal-entry and deliverable matrix red team

主动寻找：

- Marketplace description/default prompts仍不能触发 local edit/teaching；
- source skill自身边界与 shared routing冲突；
- profile仍宣称不同 default；
- generated layer手工漂移；
- business no-format被改成 Beamer；
- explicit PPTX/Slides被两个 built-in template劫持；
- external locked template变成隐藏第三 registry；
- local edit被 full storyboard做重；
- existing deck被换皮；
- plan-only被误报为完成 deck。

## Architecture red team

主动寻找：

- semantic layer重新出现 columns/density/dominant object；
- composition layer重新排序 story/改变 claim；
- Stage 1先造了一套后来 Stage 2/3不得不兼容的第二 IR；
- deck-plan compatibility reader演变成永久旧架构；
- gold/reference library为了证明历史投入被强制消费；
- review scope只写字段但 reviewer仍看不到完整 artifact；
- generated source/runtime/render不是同一候选；
- candidate TODO被 regression名义偷渡实现。

## External targeted re-check

按 Critic Role Contract 做少量独立网络核查。优先官方来源。

至少核对：
- Beamer 当前 version/tagged PDF status；
- ltx-talk 当前 version/experimental status；
- 是否出现足以推翻本轮 Beamer路线的新事实。

如果无变化，简要记录即可，不要无限检索。

## Maintenance Board

Canonical Issues #29–#48 source maturity必须保持当前真实值。

如果本 Critic surface不能在满足 Clear Writing前置条件的情况下直接修改 GitHub Project：
- 不声称已同步；
- 不要求用户手工拖卡片；
- 输出 exact pending Project mutation。

Expected pending mutation if V1.1 is the current anchor：
- Project: AI Skills Maintenance
- Area: presentations
- Issues: #29–#48
- Status: DOING
- Current execution anchor:
  docs/design/PRESENTATIONS_TWO_TEMPLATE_PRODUCTION_REDESIGN_PLAN_V1_1_2026-09-28.md
  @ f71e97c06938ab2ce175ccf3b4ac19da9309fda1
- Next action:
  independent Critic V1.1 review / after PASS, Planner prepares Stage 1 execution package
- no source maturity change
- no PROMOTED/DONE
- no issue close

## Blocker standard

只有满足 Critic Role Contract 的真实 blocker才能 REVISE。

每个 blocker必须包含：
- 对应 requirement；
- direct evidence；
- causal user/product risk；
- minimum closure condition。

不要因：
- “可以更保险”；
- 想多加测试；
- 文档措辞偏好；
- 可在批准架构内普通修复的局部实现细节；
- 可恢复的假设风险；
单独 REVISE。

## 期望输出

先给自然中文结论，并明确旧四个 blocker逐项：

PRES-V1-F01 = CLOSED | STILL_OPEN
PRES-V1-F02 = CLOSED | STILL_OPEN
PRES-V1-F03 = CLOSED | STILL_OPEN
PRES-V1-F04 = CLOSED | STILL_OPEN

然后输出：

RESULT = PASS | REVISE
REVIEW_OBJECT = PRESENTATIONS_TWO_TEMPLATE_PRODUCTION_REDESIGN_PLAN_V1_1
REVIEWED_PATH = docs/design/PRESENTATIONS_TWO_TEMPLATE_PRODUCTION_REDESIGN_PLAN_V1_1_2026-09-28.md
REVIEWED_COMMIT = f71e97c06938ab2ce175ccf3b4ac19da9309fda1
PLANNER_RESPONSE = results/presentations--two-template-production-redesign/PLANNER_RESPONSE_V1_1.md
PLANNER_RESPONSE_COMMIT = b7b6499f4ac2cbd50c19f12005ac24b66cbd0b48
ARCHITECTURE_VERDICT = ...
NORMAL_ENTRY_VERDICT = ...
TWO_TEMPLATE_VERDICT = ...
TODO_COVERAGE_VERDICT = ...
CAPABILITY_GATE_VERDICT = ...
IMPLEMENTATION_STAGING_VERDICT = ...
MIGRATION_AND_RECOVERY_VERDICT = ...
READY_FOR_EXECUTION_PACKAGE = YES | NO

如果 REVISE：
- 优先复核旧 blocker；
- 使用稳定 finding IDs；
- 新 blocker只允许来自新事实、旧轮遗漏的关键风险或 V1.1新回归；
- 按 Critic Role Contract 自动给 Planner完整下一条 prompt；
- 要求完整 V1.2，不要只给补丁。

如果 PASS：
- PASS只批准本 V1.1 architecture / TODO disposition / Gate taxonomy / staging；
- PASS不授权 implementation、branch/worktree、paid review、production install、version bump或release；
- 下一步必须回 Planner，为 Stage 1 单独准备 execution package：
  Proposal/Plan + Canonical Goal + Kickoff Draft；
- 该 Stage 1 execution package仍需 execution-ready Critic PASS；
- 按 Critic Role Contract 自动生成下一条 Planner prompt，不要让用户自己拼上下文。
