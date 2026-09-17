# 056 Product Delivery Discipline — Codex Kickoff Draft

- Execution package version: `v0.1`
- Task: `056_product_delivery_discipline`
- Plan: `docs/design/056_PRODUCT_DELIVERY_DISCIPLINE_IMPLEMENTATION_PLAN.md` v0.1
- Goal: `docs/goals/056_PRODUCT_DELIVERY_DISCIPLINE_GOAL.md` v0.1
- Status: `DRAFT_NOT_AUTHORIZED`

只有独立 Critic 对上述同版 package 给出 `READY_FOR_CODEX=YES` 后，用户实际发送本 Kickoff 才构成执行授权。

## Kickoff

执行 `056_product_delivery_discipline`，严格按上述 frozen Plan/Goal，不重新设计 v6。

本次授权范围：

- `YuukiAS/AI_Skills_Collection`：从届时最新、仍包含获批 package 的 `origin/main` 创建 `reviewed/056_product_delivery_discipline`；优先从已验证本地 canonical checkout 建同级 worktree `AI_Skills_Collection-056-product-delivery-discipline`。允许 task-owned source/test/generated/release metadata 修改、普通 commit 与 push 到该 exact branch。
- `YuukiAS/GPT_Codex_AI_Bridge_Kit`：从届时最新 `origin/main` 创建 `reviewed/056_product_delivery_discipline`；优先从已验证本地 canonical checkout 建同级 worktree `GPT_Codex_AI_Bridge_Kit-056-product-delivery-discipline`。允许 Plan 中的 Lite/Host Policy/source/test/docs/version `0.8.3` 修改、普通 commit 与 push 到该 exact branch。
- `YuukiAS/Bobbio`：只允许在现有 `develop` 修改 `AGENTS.md` frontend/Product Design read-list，加入 current `docs/design/FIGMA_HANDOFF.md` locator；允许该单一 docs change 的普通 commit/push。不得改 Bobbio product code/Figma/runtime version。
- 允许普通 GitHub fetch/pull/ff-only/commit/push 以取得和发布上述 exact scope；不授权 remote remap、force push、历史重写、删除 branch/tag 或 unrelated repo mutation。
- 允许在 **056 probe 同一 Windows Codex identity** 上安装 task-owned Bridge Kit candidate，并执行 `ai-bridge host install` / `validate`。该授权明确包含：按 Bridge Kit 自带 backup 机制把 managed `features.default_mode_request_user_input` 从旧值收敛为 `false`，同时保留 unrelated config；若 smoke 失败，只允许恢复该次 install 创建的 exact backup。
- 允许安装/升级 task-owned AI_Skills candidate plugins并启动 fresh local Codex session做 G1–G8 production replay；不授权 paid API/Terra。
- G1 最终 `HUMAN_ONLY` smoke 到点时，必须用普通 plain-text question 请求我回复 `W2_RESUME_056_FINAL`；这条问题未得到我的明确回复前，dependent execution 必须停止。不要使用 Default native `request_user_input`，不要 polling，不要 timeout 后继续，不要 terminal `BLOCKED`。

明确禁止：

- 修改 Lucerna、Mica、Asteria、SeminarArc、CUHK Date、CARE/EAT、Server/VPS、Longleaf_Bridge 或 Scientific Visualization production；
- 新增 Control/watcher/daemon/ledger/state machine/Persistent Run/tmux fallback；
- fork/patch Codex；
- paid/external model API；
- 因本地已有 repo 有 unrelated dirty file 就直接 network clone，或 local clone 后 remap remote；
- main merge/release integration、force push、branch deletion；这些必须等 final implementation audit 对 exact candidate tuple PASS 后按后续批准步骤进行。

执行时先做 source/identity/dirty preflight。能自行解决的 `AGENT_RESOLVABLE` 问题不要问我；unsupported interface 要 truthful close；只有真正 `HUMAN_ONLY` 才问。

完成实现、自测、current-host smoke、G1–G8 final evidence、commit/push 后停止在 implementation handoff，报告 exact AI_Skills/Bridge/Bobbio commits、generated hashes、host backup/final config hash、各 gate 结果和任何未验证边界。不得自行宣布整个 056 achieved。

`NEXT_HANDOFF = INDEPENDENT_IMPLEMENTATION_REVIEW`
