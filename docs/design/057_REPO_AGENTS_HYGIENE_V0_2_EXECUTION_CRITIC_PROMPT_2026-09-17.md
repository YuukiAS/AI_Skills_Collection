# 057 Repo AGENTS Hygiene — v0.2 Execution Critic Prompt

你是 AI Research Stack 的长期独立 Critic thread。

继续：

`TASK_KEY = 057_repo_agents_hygiene`

本轮只复审 execution-ready package v0.2 以及用户新增的 bounded Lite versioning amendment。不要实现，不修改产品 repo/AGENTS，不修改 Bridge Kit production，不创建 branch/worktree，不启动 Executor，不运行 paid API。

## 1. 强制读取

先读取 AI_Skills_Collection 最新 main：

- `AGENTS.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/design/057_REPO_AGENTS_HYGIENE_V2_PROPOSAL_2026-09-17.md`
- `docs/design/057_LITE_VERSIONING_DEFAULT_AMENDMENT_2026-09-17.md`
- `docs/design/057_REPO_AGENTS_HYGIENE_IMPLEMENTATION_PLAN.md` v0.2
- `docs/goals/057_REPO_AGENTS_HYGIENE_GOAL.md` v0.2
- `docs/operations/prompts/057_REPO_AGENTS_HYGIENE_KICKOFF.md` v0.2
- `docs/design/057_REPO_AGENTS_HYGIENE_REVIEW_PACKAGE.md`

上一轮 execution package v0.1：

- commit `57f58821deecf56ee69a6504f85145ce3bdfb11e`
- result `REVISE`
- blockers：
  - `C057-E1-BOBBIO-AUTHORITY-OWNER-SCOPE`
  - `C057-E2-SEMINARARC-AUTHORITY-INVERSION`
  - `C057-E3-SELF-REFERENTIAL-FINAL-CANDIDATE`

除非 v0.2 自己引入直接冲突，不重开已经通过的 v2 架构、repo dispositions、H1–H9、task-branch isolation、Bridge scaffold 方向、0.8.3 PATCH 方向或 057 -> independent review -> integration -> bounded 056 revalidation sequencing。

## 2. 复核 C057-E1

重新读取 Bobbio `develop`：

- `AGENTS.md`
- `docs/design/FIGMA_HANDOFF.md`
- `docs/PRODUCT_DESIGN_BRIEF.md`
- `docs/DEVELOPMENT_WORKFLOW.md`
- `docs/quality/NATIVE_DESKTOP_ACCEPTANCE.md`

确认 v0.2 已把 `docs/PRODUCT_DESIGN_BRIEF.md` 加入窄 mutation scope，且只允许 source-of-truth/visual-authority wording。

最终必须能形成无冲突的三层 authority：

- Figma = current canonical visual design/components/screen composition；
- Product Design Brief = durable product/interaction constraints；
- old `Bobbio_Design_*.png` = historical/supporting visual references，不是 parallel production authority。

H2 必须直接比较 final AGENTS + FIGMA_HANDOFF + PRODUCT_DESIGN_BRIEF，不能只查 locator。

若 Plan/Goal/Kickoff 任一处仍不给 Executor 合法修改 brief 的窄权限，E1 仍未关闭。

## 3. 复核 C057-E2

重新读取 SeminarArc `main`：

- `AGENTS.md`
- `docs/DEVICE_TESTING.md`
- `prompts/AGENT_RULES.md`

确认 v0.2 会修复 `docs/DEVICE_TESTING.md` 中当前 stale owner 句，不形成 `DEVICE_TESTING -> AGENTS complete rules -> DEVICE_TESTING detail` 的循环。

Final ownership 必须是：

- root AGENTS = prominent hard safety summary + locator；
- DEVICE_TESTING = detailed device/environment/test mechanics、command restrictions、volatile inventory、mixed-inventory procedure、historical incident evidence。

root必须继续显眼保留：

- Emulator-first；
- protected physical device不是generic connected/instrumentation target；
- no automatic transport recovery/reset；
- authorized physical write = explicit verified serial + preflight/postflight；
- physical-device channel failure不阻塞independent WSL/headless/Emulator work；
- PIN/secret不得进入repo/task/result/log/screenshot/commit。

不得新建第三份device/environment manual，不得削弱安全。

H2/H3/H6 必须真实验证这个 owner closure。

## 4. 复核 C057-E3

确认 v0.2 final-candidate identity 不再 self-reference。

要求：

### Stage A — evidence/result commit E

finalize：

- RESULT.md
- SEMANTIC_PRESERVATION.md
- SIZE_REPORT.md
- H1–H9 evidence/locators

tracked content 不要求写入自己的 E SHA。

### Stage B — manifest closure commit M

MANIFEST 记录：

- AI_SKILLS_RESULT_COMMIT=E
- BRIDGE_CANDIDATE_COMMIT
- BRIDGE_VERSION
- BOBBIO_CANDIDATE_COMMIT
- LUCERNA_CANDIDATE_COMMIT
- MICA_CANDIDATE_COMMIT
- ASTERIA_CANDIDATE_COMMIT
- SEMINARARC_CANDIDATE_COMMIT
- CUHK_DATE_INSPECTED_REF
- H1–H9 status/evidence locators

MANIFEST 不写自己的 M SHA。

Executor handoff 外部报告 `AI_SKILLS_MANIFEST_COMMIT=M`；independent implementation review target = M 所绑定 exact tuple。

不得引入 ledger/schema/state/controller 来解决 SHA 问题。

## 5. 审用户新增 Lite versioning amendment

这是本轮唯一新增设计点。请独立判断是否最小充分、是否会和现有 repo-local versioning policy 冲突。

拟定 owner：

`GPT_Codex_AI_Bridge_Kit/templates/prompts/AGENT_RULES.md`

root `AGENTS_TEMPLATE.md` 只做 locator/项目override槽位，不复制规则。

拟定 precedence：

1. current user/frozen task；
2. explicit current repo-local versioning policy；
3. Lite fallback。

Lite fallback：

- default formal version = `MAJOR.MINOR.PATCH`；
- PATCH = compatible repair；
- MINOR = compatible user-visible capability；
- MAJOR = incompatible public/product contract or migration and requires explicit Planner/user approval；
- `0.y.z` = allowed initial development；`1.0.0` = explicit stability/default-use decision；
- `alpha` / `beta` / `rc` / preview/date/arbitrary prerelease labels are opt-in only with an approved repo lifecycle or explicit current task/user authorization；
- one formal version cannot represent two distinct user-consumable runtime candidates；
- build label/commit SHA may supplement identity but not replace required formal version；
- docs/TODO/test-only changes normally do not require a release bump；
- release-ready version/source/changelog parity must be truthful。

重点攻击：

- 是否错误把所有现有 repo 强迁到 SemVer；
- 是否会破坏 AI_Skills 自己已批准的 two-part plugin version等 local override；
- 是否把 prerelease 禁令写得过死，阻止 repo 明确批准的 alpha/beta/rc lifecycle；
- 是否应该把 MAJOR approval说成“必须用户批准”还是“Planner/user explicit frozen decision”更准确；
- 是否会导致每个普通 commit 都机械 bump；
- 是否真正解决 Mica 等“runtime行为变了但仍报同一版本”和新repo随便造 alpha/beta/rc 的问题；
- 是否应该保持 H1–H9，不新增 H10。

独立核查 SemVer 2.0.0 官方规范：MAJOR/MINOR/PATCH含义、0.y.z、prerelease optional semantics。不要把外部 SemVer规范当成强制覆盖本地已批准version contract。

如果 amendment 方向不成立，REVISE这个 bounded amendment/执行包；不要因此重开整个057 v2。

## 6. 保持已通过 repo dispositions

只检查 v0.2 blocker修订是否意外越界：

- Lucerna = LIGHT_EDIT；distinct Windows/provider/regression/screenshot/Longleaf rules保留；
- Mica = testing ladder consolidation，manual real-site vs automated authenticated boundary清楚；
- Asteria = root map + single RUNTIME_OPERATIONS owner；不改 delegated AGENT_RULES；
- CUHK Date = inspect-only/no root creation；
- Git isolation = exact `reviewed/057_repo_agents_hygiene` temporary branches；independent review前不merge。

## 7. H1–H9

保持九个 gate，不新增 H10。

特别检查：

- H2 = Bobbio three-way + SeminarArc owner closure直接比较；
- H7 = real fresh `ai-bridge init -> validate`，若 versioning amendment PASS，也证明生成的 canonical Lite surface真实包含 fallback；
- H8 = existing root normal/force init不被 scaffold迁移/重排；
- H9 = root不复制Lite execution/versioning policy。

Preservation table、line/byte count、关键词存在都不能单独 PASS。

## 8. Future all-active-repo adaptation boundary

用户已明确：057与056都完成后，要对当前所有进行中repo做一次完整adaptation。

本057只允许记录这个future requirement，不得提前扩大mutation scope。

后续独立 major round 至少需要 inventory：

- Bridge/Lite installed identity；
- root/delegated AGENTS structure；
- versioning authority/current version/changelog parity；
- explicit local override / alpha-beta-rc history；
- final 056 consumption。

Critic判断把它留到后续独立round是否正确，还是当前有某项必须提前做才能让057成立。

## 9. 结论

如果仍有 blocker：

```text
RESULT = REVISE
TASK_KEY = 057_repo_agents_hygiene
REVIEW_PACKAGE_VERSION = v0.2
READY_FOR_CODEX = NO
NEXT_HANDOFF = PLANNER
```

按 Critic contract 自动附完整 Planner返修 prompt。

如果 E1/E2/E3 全部关闭且 versioning amendment 可接受：

先按 Critic contract用正常中文解释：三个 blocker怎么关闭、新 versioning rule最终如何工作、各repo会怎么变/不变、H1–H9证明什么、PASS不证明什么。

然后给：

```text
RESULT = PASS
TASK_KEY = 057_repo_agents_hygiene
REVIEW_PACKAGE_VERSION = v0.2
PLAN = docs/design/057_REPO_AGENTS_HYGIENE_IMPLEMENTATION_PLAN.md
GOAL = docs/goals/057_REPO_AGENTS_HYGIENE_GOAL.md
KICKOFF = docs/operations/prompts/057_REPO_AGENTS_HYGIENE_KICKOFF.md
VERSIONING_AMENDMENT = docs/design/057_LITE_VERSIONING_DEFAULT_AMENDMENT_2026-09-17.md
READY_FOR_CODEX = YES
```

再逐字返回你实际审过的 v0.2 `## Kickoff` 正文；不要 PASS 后另写不同 prompt。

`NEXT_HANDOFF = USER_SENDS_APPROVED_KICKOFF`
