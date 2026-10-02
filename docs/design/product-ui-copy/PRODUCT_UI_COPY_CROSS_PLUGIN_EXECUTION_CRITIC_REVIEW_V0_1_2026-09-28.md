# Product UI Copy Cross-Plugin — Execution-Ready Critic Review v0.1

Date: 2026-09-28  
Repository: `YuukiAS/AI_Skills_Collection`  
Review stage: execution-ready  
Reviewed package commit: `3a447c5cfeb2cee11ec4a37693ffb4ee7e19ec02`  
Latest AI_Skills main checked before review: `285f04568221d66888d8382eee812c8f6669e0d3`  
Latest Bridge main checked before review: `f85622fd26fa1b8648d957e20b4f047a671e999f`

REVIEWED_OBJECT = Product UI Copy Cross-Plugin execution package  
REVIEWED_PACKAGE_VERSION = v0.1  
REVIEWED_PACKAGE_COMMIT = 3a447c5cfeb2cee11ec4a37693ffb4ee7e19ec02  
RESULT = REVISE  
READY_FOR_CODEX = NO

APPROVED_PLAN = docs/design/product-ui-copy/PRODUCT_UI_COPY_CROSS_PLUGIN_EXECUTION_PLAN_V0_1_2026-09-28.md  
APPROVED_GOAL = docs/goals/PRODUCT_UI_COPY_CROSS_PLUGIN_GOAL_V0_1.md  
APPROVED_KICKOFF = docs/operations/prompts/PRODUCT_UI_COPY_CROSS_PLUGIN_KICKOFF_V0_1.md

APPROVED_TASK_KEY = product-ui-copy--cross-plugin-production-integration  
APPROVED_BRANCH = reviewed/product-ui-copy--cross-plugin-production-integration  
APPROVED_WORKTREE = /home/yuukias/AI_Skills_Collection-product-ui-copy--cross-plugin-production-integration

ARCHITECTURE_AUTHORITY = docs/design/product-ui-copy/PRODUCT_UI_COPY_CROSS_PLUGIN_PROPOSAL_V0_2_2026-09-28.md @ a0ac70226c7b1ddd7d6e33c9d4c00aebbf473f67

## 结论

execution package 的主体方向是可执行的：Bridge first bootstrap、task-local V2 Plan、同会话双 candidate plugin replay、G1–G8 能力覆盖、H0→H4 freshness 设计、SeminarArc mobile 正负 replay、repo-safe rendered evidence、版本方向、权限与 tracking 边界都基本成立。

当前只有一个 blocker：**release-critical G1–G6 目前按时序在版本/生成层变更之前完成，而 H2 final candidate 在这些变更之后才冻结。** 这会允许最终 release 把 pre-H2 candidate 的 G1–G6 与 post-H2 candidate 的 H4/CI/G8 拼在一起，违反本 Plan 自己和当前 Capability Gate policy 的 same-final-candidate 要求。

这不是 Product UI Copy architecture 问题，也不需要修改 Bridge Kit。只需修正 Plan / Goal / Kickoff 的 final-candidate gate chronology。

## Bridge bootstrap

PASS。

当前 Bridge `bootstrap_task_worktree` 仍由 canonical checkout 的 parent/name 与 semantic task key 派生 sibling worktree：

`/home/yuukias/AI_Skills_Collection-product-ui-copy--cross-plugin-production-integration`

并固定创建：

`reviewed/product-ui-copy--cross-plugin-production-integration`

Kickoff 没有发明 caller-chosen worktree 参数，而是要求先验证 canonical checkout 恰为 `/home/yuukias/AI_Skills_Collection`，不匹配则在 branch/worktree creation 前 fail closed。CLI 参数也与 current Bridge first-bootstrap surface 一致。

虽然 Execution Plan 记录的 Bridge source checkpoint 是较早的 `9d15247...`，最新 Bridge main `f85622f...` 的相关 bootstrap/worktree/state implementation 没有发生语义变化；新 main 主要增加文档性 workflow/naming 说明。因此无需仅为 locator freshness 修改 package。

Future recovery 继续走 artifact-bound `materialize-worktree --mode resume`；禁止 second bootstrap/raw worktree add 的边界正确。

## Initial Planner transaction

PASS。

当前 Bridge first bootstrap 创建：

- `CURRENT.state = PLAN_REQUESTED`
- `CURRENT.next_action = RUN_GPT_PLANNER`
- `plan_revision = 0`
- `max_plan_revisions = 1`

新的 `PLAN_FROZEN` 必须使用 `AI_BRIDGE_REVIEWED_PLAN_V2`。Execution package 正确要求外部 Planner写 task-local PLAN、按当前 template 自检，再最后执行：

`PLAN_REQUESTED -> PLAN_FROZEN / RUN_CODEX_EXECUTOR`

Initial freeze 不增加 `plan_revision`。Executor 不得 self-freeze PLAN。

## Implementation scope

PASS。

Clear Writing scope只包含：

- 新 `product-ui-copy` sibling；
- `writing-fidelity` 窄 semantic-fidelity handoff；
- `chinese-prose` frontmatter narrowing + 最小 route seam；
- Clear Writing routing/plugin metadata/package；
- 必要 tests。

Frontend Design scope只包含：

- coordinator现有 source 中的 Product UI Copy handoff/discovery；
- `product-ux-planning` content architecture；
- rendered copy acceptance；
- surface-agnostic trigger/tests；
- Frontend plugin metadata。

没有重开 coordinator-first topology，也没有把 consumer repo binding 拉入本 task。Profile 只在真实需要 companion exposure 时最小修改，generated layer仍由 generator 管理。

## Same-session multi-plugin candidate replay

PASS。

对 repository-level claim，两个完全分离的单插件 run 确实不足以证明同一正常 runtime 能完成：

Frontend Design → Clear Writing / Product UI Copy → return-to-Frontend

当前 `scripts/candidate_plugin_replay.py` 已经具备：

- committed candidate staging；
- temporary candidate marketplace；
- plugin add/remove；
- actual Skill-path consumption parsing；
- stale candidate cleanup；
- production same-name install snapshot/unchanged assertion；
- single-plugin replay regression。

它当前只是 manifest、enable config、consumption parser 和 snapshot 数据结构按一个 plugin 编写。把这些结构最小泛化为多个 candidate plugins，同一 marketplace / child Codex session 同时 enable 两个 candidate identity，并分别要求两个 installed path 的消费事件，是现实且最小的改法。不需要第二套 replay framework或新 service。

执行时必须继续保留现有 single-plugin CLI 行为和回归，并证明两个 candidate identity 都被清理、两个 production same-name installs 都未变化。

## Gate Matrix

REVISE，仅因 final-candidate chronology。

Gate本身的能力划分合理且不重复：

- G1：discovery / activation / packaging
- G2：ownership / handoff / protected meaning
- G3：naturalness / locale / linguistic rhythm
- G4：rendered acceptance
- G5：should-not-change
- G6：same-session cross-plugin normal entry + real-project compatibility
- G7：fresh H0→H4
- G8：release / CI / README / review closure

G1/G6不能由“文案看起来正确”冒充，G3/G4明确要求 qualitative / rendered evidence，G7不把 known replay冒充 fresh，G5覆盖 shared metadata/generator/helper 的 blast radius。

唯一问题见 `PUC-ER-01`：当前时序没有保证 G1–G6 的 **release-critical pass** 来自 H2 versioned final candidate。

## H3 Planner revision / freshness

PASS。

从 current Bridge state graph看：

- `EXECUTING -> NEEDS_GPT_PLANNER` 合法；
- `NEEDS_GPT_PLANNER -> PLAN_FROZEN` 合法；
- 该 re-freeze 自动消耗唯一 `plan_revision: 0 -> 1`；
- 第二次自动 plan revision 不再允许。

Bridge Planner contract把这条边限制为“Executor无法从 frozen Plan 安全推导的最小歧义”。本 package 的 H0故意不允许 frozen Plan/Executor包含 exact fresh prompts；因此到 H2 后，Executor能够直接证明 exact H3 batch **按合同不可由自己安全推导**。Planner只补：

- exact holdout locator/identity；
- exact H2 candidate binding；
- rubric binding；

并且禁止 production/architecture change。这个用法仍属于一次 bounded minimal re-plan，而不是拿 `NEEDS_GPT_PLANNER` 当通用阶段编排器。

H4 failure 后没有第二次 revision budget，也禁止 fresh-batch chasing，符合 Bridge和本项目 freshness policy。

## Fresh holdout

PASS。

8 个 scenario 是风险相称的小 batch；scenario允许覆盖多个维度，没有机械“一维一个样本”。H0只冻结 families/coverage/rubric/batch size，H2后才 H3 exact batch，H4完整 batch一次运行。

禁止：

- cherry-pick；
- failed-prompt replacement；
- easy-case padding；
- candidate修改后继续称同批 fresh。

如果根据 H4 结果修改 candidate，该 batch自动降为 known regression；后续 fresh evaluation 需要新 candidate freeze + 单独授权，不能在当前失败 run 里继续追。

## Real-project replay

PASS。

Lucerna、Mica、SeminarArc都被限定为 read-only compatibility/discovery evidence，不计 maturity。

SeminarArc pair足以关闭 mobile evidence seam：

- natural Compose/UI prompt不能写 expected routing；
- Frontend Design只拥有 generic product-interface hierarchy/design/evidence；
- repo-local `android-lead` / `compose-expert` 保留 Android/Compose implementation authority；
- Room/WorkManager/data-only negative必须不触发 Frontend Design。

Kickoff把 source transmission 限定到三项 named repositories、当前 task compatibility purpose、minimum frozen source、current authorized Codex/OpenAI execution path，并禁止 consumer write、unrelated private data、secret、broad export和 redistribution。Exact source locators在 replay 前还必须冻结；扩大 source/provider/data scope需重新授权。

## Rendered review path

PASS。

本 package 不启用 paid Visual Review/Text Review/Terra，这本身没有问题，因为目标 artifact 是允许提交 repo 的代表性 UI fixture/screenshots，而不是不能提交的 private artifact。

我直接验证了当前 GitHub connector surface可以按 repository path 读取已提交 PNG 的 base64 bytes，并将其作为实际 image input 交给当前 Reviewer视觉读取。因此 Scheduled GPT Reviewer存在真实的 repo-safe image access path，不必仅靠 filename/OCR/Executor prose。

Plan/Kickoff也已经 fail closed：如果届时 Reviewer surface不能实际读取 image bytes，则不能 PASS，必须返回 evidence-access blocker；不得偷偷改成机械检查。

## Version / release chronology

REVISE，仅因 `PUC-ER-01`。

版本方向本身仍正确：

- repository MINOR `5.3.1 -> 5.4.0`
- `web-development 0.3 -> 0.4`
- `writing-style 0.3 -> 0.4`
- other central plugins NO_BUMP
- maturity unchanged

Current main仍是上述 baseline。

问题不是 bump class，而是 bump / regenerate 与 release-critical gates 的先后关系。

## Tracking closure

PASS。

Package正确：

- 保留 Issue #17；
- Issue #13只作为 dependency；
- 不把 unrelated #73 / #20 当本任务 issue；
- 只创建两个新的 Product UI Copy tracking Issues并更新对应 source locator；
- reader-facing Issue/Project copy先经过 installed Clear Writing；
- Project surface不可用时输出 exact pending mutation，不伪称同步；
- central release后 consumer hard bindings仍未完成时进入 ADAPTING，而不是 DONE。

没有要求本任务修改 consumer repos。

## Permissions

PASS。

用户以后发送 approved Kickoff 时，授权范围被限定到：

- exact task / reviewed branch / Bridge-derived sibling worktree；
- bounded AI_Skills production edits；
- generated updates / CI；
- temporary candidate replay；
- Lucerna/Mica/SeminarArc minimal frozen source read-only compatibility transmission；
- 两个 Product UI Copy tracking Issue creation/rebinding。

明确不授权：

- consumer writes；
- paid review；
- Bridge changes；
- destructive Git；
- main merge / release ref；
- public deploy；
- maturity promotion；
- successor task。

## Blocking finding

### PUC-ER-01 — RELEASE-CRITICAL G1–G6 RUN BEFORE THE VERSIONED H2 FINAL CANDIDATE

**Requirement**

当前 Capability Gate policy和 Execution Plan自身都要求所有 release-critical gates 绑定同一个 final candidate。Plan中 G1–G6 均标记 `Final candidate = YES`；尤其 G1验证最终 plugin packaging/identity，G6验证最终 installed candidate 的双插件 normal-entry consumption。

**Direct evidence**

Execution Plan Phase F 规定：

> After G1–G6 development evidence and G4 rendered acceptance are stable:
> 1. apply version changes exactly once;
> 2. update changelogs/README/VERSION/tests/generated output;
> 3. run version/parity validation;
> 4. freeze H2 final candidate...

Kickoff §11 同样规定先稳定 G1–G6 development evidence，再做：

`5.3.1 -> 5.4.0`, `web-development 0.4`, `writing-style 0.4`

随后才 freeze H2。

但 H2之后的 package只明确运行 H4、CI和Reviewer，没有要求在 **version bump + regenerate 后的 H2 candidate** 上重新执行 G1–G6 release-critical gates。

Version/regeneration会改变至少：

- repository VERSION；
- both plugin versions；
- generated plugin manifests/metadata；
- candidate install identity/path；
- README/changelog/release metadata。

因此 pre-H2 的 G1 packaging和 G6 installed candidate runtime不是 H2 final candidate identity。

**Causal risk**

任务可以形成：

`pre-version candidate G1–G6 PASS`
+
`post-version H2 candidate H4/CI/G8 PASS`

然后拼成 release PASS。这样最终 `web-development 0.4` / `writing-style 0.4` 没有直接通过 Plan自己要求的 G1–G6 final-candidate gates，违反 current Capability Gate policy 的 same-final-candidate rule。

**Minimal closure condition**

只修改 Plan / Goal / Kickoff 的执行时序，不改 architecture或 gate定义：

1. 开发阶段可继续把 pre-version G1–G6 当 development evidence；
2. development stable 后，执行一次且仅一次 version bump + regenerate；
3. freeze 一个 versioned H2 candidate，随后禁止 production edits；
4. **在进入 H3 前，使用该 exact H2 candidate重新直接执行并通过所有标记 `Final candidate = YES` 的 G1–G6 release-critical gates，包括同会话双插件 candidate replay和 rendered acceptance；**
5. 若其中任何 gate失败，修同一 release version、冻结新的 H2 candidate，并让最终 release-critical G1–G6重新绑定到该新 candidate；在 fresh H3/H4开始前完成；
6. 只有 versioned H2 candidate的 G1–G6全部 PASS后，才进入 H3 exact holdout freeze和 H4；
7. Goal/Kickoff chronology同步同一语义。

不需要新增 gate、额外 project、付费 review或 Bridge state。

**Owner**

Planner。

## External reality check

Current OpenAI official plugin/Skill documentation confirms the execution assumptions used here:

- Skill discovery first exposes `name` and `description`, and description determines when the model considers a Skill;
- focused Skills are preferred when workflows differ in triggers/inputs/success criteria;
- Skill/plugin testing should include direct, indirect, unsupported/negative and boundary requests;
- the complete packaged/installed plugin should be tested, not only individual source instructions.

Sources checked:

- https://developers.openai.com/plugins/concepts/skills
- https://developers.openai.com/plugins/build/skills
- https://developers.openai.com/plugins/deploy/connect-chatgpt

These support G1/G6 and the same-session installed-plugin replay requirement; they do not change the approved Product UI Copy architecture.

## Verdict matrix

```text
RESULT = REVISE
READY_FOR_CODEX = NO

REVIEWED_PACKAGE_VERSION = v0.1
REVIEWED_PACKAGE_COMMIT = 3a447c5cfeb2cee11ec4a37693ffb4ee7e19ec02

BRIDGE_BOOTSTRAP = PASS
INITIAL_PLANNER_TRANSACTION = PASS
IMPLEMENTATION_SCOPE = PASS
MULTI_PLUGIN_CANDIDATE_REPLAY = PASS
GATE_MATRIX = REVISE
H3_PLANNER_REVISION = PASS
FRESH_HOLDOUT = PASS
REAL_PROJECT_REPLAY = PASS
RENDERED_REVIEW_PATH = PASS
VERSION_CLOSURE = REVISE
TRACKING_CLOSURE = PASS
PERMISSIONS = PASS

IMPLEMENTATION_AUTHORIZED = NO
NEXT_STEP = Planner revise only final-candidate gate chronology, then execution-ready Critic re-review
```

## Authorization boundary

This review does not authorize production implementation, branch/worktree creation, Executor launch, paid review, consumer-repo mutation, main merge, release-ref movement, maturity promotion, or Bridge modification.
