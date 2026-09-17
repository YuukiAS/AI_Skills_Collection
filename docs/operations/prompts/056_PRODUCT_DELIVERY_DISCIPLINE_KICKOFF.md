# 056 Product Delivery Discipline — Codex Kickoff Draft

- Execution package version: `v0.2`
- Task: `056_product_delivery_discipline`
- Plan: `docs/design/056_PRODUCT_DELIVERY_DISCIPLINE_IMPLEMENTATION_PLAN.md` v0.2
- Goal: `docs/goals/056_PRODUCT_DELIVERY_DISCIPLINE_GOAL.md` v0.2
- Status: `DRAFT_NOT_AUTHORIZED`

只有独立 Critic 对上述同版 package 给出 `READY_FOR_CODEX=YES` 后，用户实际发送本 Kickoff 才构成执行授权。

## Kickoff

执行 `056_product_delivery_discipline`，严格按 v0.2 frozen Plan/Goal，不重新设计已通过的 v6 架构。

本次授权范围：

- `YuukiAS/AI_Skills_Collection`：从届时最新、仍包含获批 v0.2 package 且没有相关语义漂移的 `origin/main` 创建 exact branch `reviewed/056_product_delivery_discipline`；优先从已验证本地 canonical checkout 建同级 worktree `AI_Skills_Collection-056-product-delivery-discipline`。允许 Plan 内 task-owned source/test/generated/TODO/changelog/release metadata修改、普通 commit和push到该 exact branch。
- `YuukiAS/GPT_Codex_AI_Bridge_Kit`：从届时最新 `origin/main` 创建 exact branch `reviewed/056_product_delivery_discipline`；优先从已验证本地 canonical checkout 建同级 worktree `GPT_Codex_AI_Bridge_Kit-056-product-delivery-discipline`。允许 Plan 内 Lite/Host Policy/source/test/docs/version `0.8.3` candidate修改、普通 commit和push到该 exact branch。
- `YuukiAS/Bobbio`：只允许在现有 `develop` 修改 `AGENTS.md` frontend/Product Design read-list，加入 current `docs/design/FIGMA_HANDOFF.md` canonical locator；允许该单一 docs change 的普通 commit/push。不得改 Figma、product code、runtime version或复制中央 Frontend checklist。
- **不得修改** Lucerna、Mica-for-ChatGPT、Asteria、SeminarArc、CUHK Date、CARE/EAT、Server/VPS、Longleaf_Bridge 或 Scientific Visualization production/AGENTS。它们在本任务中的 disposition 已由 Plan冻结为 ALREADY_COVERED / NO_CHANGE / EVIDENCE_NEEDED / NO_GENERIC_COPY；Executor不得临场扩写。
- 允许普通 fetch、对已选authority的ff-only同步、task-owned stage/commit/push。不得remote remap、force push、历史重写、删除branch/tag、PR或unrelated repo mutation。
- 允许在 **056 probe同一 Windows Codex identity** 上安装 task-owned Bridge candidate，并执行 `ai-bridge host install` / `ai-bridge host validate`。该授权包含使用 Bridge自带 backup机制把 managed `features.default_mode_request_user_input` 收敛为显式 `false` 并保留 unrelated config；若 smoke失败，只允许恢复该次install创建的exact backup。
- 允许安装/升级 task-owned AI_Skills candidate plugins并启动fresh local Codex session执行 G1–G8 production replay；不授权paid API/Terra。

执行前先做 Source Discovery / identity / dirty ownership preflight：已有正确 local repo先复用并核freshness；unrelated dirty不等于放弃repo；没有已授权 isolation时不得自行建别的branch/worktree；本机确无可用source才network clone；禁止local clone后`git remote set-url`绕路。

### HUMAN_ONLY hard contract

能自行解决的 `AGENT_RESOLVABLE` repo/source/environment/test/config/diagnostic问题不要问我；`UNSUPPORTED_WITH_EVIDENCE` truthful close；只有真正 `HUMAN_ONLY` 才问。

Default HUMAN_ONLY 不得使用 native `request_user_input` card。必须：

```text
preserve current Goal/resume point/prompt identity
-> 发一条清楚、单步的 plain-text user question
-> 立即停止所有 dependent execution
```

合法等待边界来自 frozen Goal/workflow已有的人类回复deadline/run-lifetime；若没有显式timeout，而question后当前Codex execution run/turn结束，则run-end就是本次handoff边界。不得使用native card的60+60秒作为transcript timeout。

如果边界到达仍无明确回复，必须报告：

```text
GOAL_BLOCKED=YES
GOAL_ACHIEVED=NO
COMPLETE=NO
READY_FOR_USER_REVIEW=NO
DEPENDENT_EXECUTION_BLOCKED=YES
```

machine state使用当前workflow已有 `NEEDS_HUMAN_APPROVAL` / human-required / legal recovery等价，不发明`BLOCKED`新enum；这仍是可恢复Goal，不等于STOP/impossibility。不得default inference、polling、auto retry、timeout后继续或fake PASS。

我以后在同一thread明确回复时：重读current Goal/resume point，确认prompt/scope仍current，不开successor、不重复prompt，只consume一次answer，exact-once恢复同一个Goal，然后由Executor完成post-action closure。若Goal已superseded/stale，回Planner而不是消费旧答复。

G1必须分别验证：

1. reply path：question -> no dependent work -> explicit reply -> exact-once resume；
2. no-reply path：faithful bounded fixture模拟/观察deadline或run-end -> Goal blocked/achieved=no -> later explicit recovery -> same Goal resume。第二条不要求我真人等待，但不能靠grep字符串冒充behavior。

所有 agent自己能完成的 implementation/tests/source-generated parity/local replay/G1-B fixture/G2–G8非人工部分必须先完成。最后真人 G1-A smoke 到点时，只向我请求一次：

`056 W2 final normal-entry smoke：请回复精确文本 W2_RESUME_056_FINAL。`

如果我没有在当前run结束前回复，按上面的blocked contract结束本run；我以后回复 `W2_RESUME_056_FINAL` 时恢复同一Goal，不重新索权，不让我做其他developer debugging。

### Acceptance / user-time boundary

在 producer-local implementation、targeted regression、actual-surface evidence、relevant design/source consumption、candidate identity和适用closure未完成前，不得把candidate交给GPT Work/用户作为acceptance-ready。Advisory/diagnostic/design review可以提前，但不得宣称ready/complete。

CUHK-Date-like broad-green fixture必须能拒绝 demo breadth、missing branch、raw token、mock-only hosted provider、real interaction-sequence bug、fallback-only primary feature或hosted config未消费backend capability；普通docs/server/tiny nonvisual负例不得因此进入重UI矩阵。

完成 implementation、自测、current-host smoke、G1–G8 final evidence、exact candidate freeze、普通commit/push后停止在 implementation handoff，报告：AI_Skills/Bridge/Bobbio exact commits、generated plugin hashes、host backup/final config hash、各Gate结果、Source Discovery regression和未验证边界。

明确禁止：

- 新增 W6/W7、G9/G10、Control/watcher/daemon/ledger/state machine/Persistent Run/tmux fallback；
- fork/patch Codex；
- paid/external model API；
- 把Figma/icon/motion/provider/locale/full-E2E checklist复制进Lite或各产品repo AGENTS；
- main merge/release integration、force push、branch deletion；这些必须等 independent implementation audit 对 exact final candidate tuple PASS 后按后续批准步骤进行。

不得自行宣布整个056 achieved。

`NEXT_HANDOFF = INDEPENDENT_IMPLEMENTATION_REVIEW`
