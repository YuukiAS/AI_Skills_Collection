# 057 Repo AGENTS Hygiene — Codex Kickoff Draft

- Execution package version: `v0.1`
- Task: `057_repo_agents_hygiene`
- Plan: `docs/design/057_REPO_AGENTS_HYGIENE_IMPLEMENTATION_PLAN.md` v0.1
- Goal: `docs/goals/057_REPO_AGENTS_HYGIENE_GOAL.md` v0.1
- Status: `DRAFT_NOT_AUTHORIZED`

Only after an independent Critic reviews this exact package and returns `READY_FOR_CODEX=YES` does the user sending the approved `## Kickoff` text authorize execution.

## Kickoff

执行 `057_repo_agents_hygiene`，严格按已审 v0.1 Plan/Goal；这是 instruction-surface hygiene + Bridge fresh-repo scaffold 任务，不重新设计 056，不修改产品/runtime。

本次授权范围：

- `YuukiAS/AI_Skills_Collection`：从届时最新、仍包含获批 057 package 且无相关语义漂移的 `origin/main` 创建 exact branch `reviewed/057_repo_agents_hygiene`，优先从已验证本地 canonical checkout 建 task-owned clean worktree。只允许写 `results/057_repo_agents_hygiene/` evidence/result/manifest 和当前 Goal 明确需要的 057 control artifact；不改中央 plugin production。
- `YuukiAS/GPT_Codex_AI_Bridge_Kit`：从届时最新 `origin/main` 创建 exact branch `reviewed/057_repo_agents_hygiene` 和 task-owned worktree。允许实现 `templates/repo/AGENTS_TEMPLATE.md`、`ai_bridge_kit/cli.py` fresh/existing AGENTS init 行为、相关 tests/docs/changelog/version `0.8.3` candidate；不得改 Host Policy、056 Default prompt transport、Review/Control 状态机或其它无关能力。
- `YuukiAS/Bobbio`：从届时 current `origin/develop` 创建 exact branch `reviewed/057_repo_agents_hygiene`。只允许修改 `AGENTS.md`，以及仅在 semantic-preservation table 证明有 unique moved detail 时修改 `docs/DEVELOPMENT_WORKFLOW.md` / `docs/quality/NATIVE_DESKTOP_ACCEPTANCE.md`。不得改 Figma、product code、schema、runtime version。
- `YuukiAS/Lucerna`：从届时最新 `origin/main` 创建 exact branch `reviewed/057_repo_agents_hygiene`。只允许轻量整理 `AGENTS.md` 的 project-owned 部分；Bridge managed block必须保持不变；不得改产品/source/runtime。
- `YuukiAS/Mica-for-ChatGPT`：从届时最新 `origin/main` 创建 exact branch `reviewed/057_repo_agents_hygiene`。只允许整理 `AGENTS.md`；不得改 extension/runtime/version。
- `YuukiAS/Asteria`：从届时最新 `origin/main` 创建 exact branch `reviewed/057_repo_agents_hygiene`。只允许修改 `AGENTS.md` 和新增 `docs/operations/development/RUNTIME_OPERATIONS.md`；不得改 product/runtime，也不得改 `prompts/AGENT_RULES.md`。若发现必须改 delegated rule 才能解决真实 contradiction，停止并回 Planner。
- `YuukiAS/SeminarArc`：从届时最新 `origin/main` 创建 exact branch `reviewed/057_repo_agents_hygiene`。只允许修改 `AGENTS.md` 和 `docs/DEVICE_TESTING.md`；不得改 Android/runtime/product。
- `YuukiAS/CUHK_Date`：只读检查 current `docs/design/prototype/AGENTS.md`；不得创建 root `AGENTS.md`，不得修改 repo。
- CARE Challenge、Server/VPS、EAT Research 完全不在本次 mutation scope。

Git/source 授权：

- 允许 ordinary fetch、读取 remote authority、创建上述 exact task branches/worktrees、task-owned stage/commit/push到上述 exact task branches；
- 先复用本机已有 canonical repo并核 identity/origin/base/freshness/dirty ownership；unrelated dirty必须保护；本机没有可用 source 才允许 network clone；
- 不授权 remote remap、force push、rebase/history rewrite、删除branch/tag、PR、main/develop merge或 unrelated repo mutation。

执行顺序：

1. 先在 `AI_Skills_Collection/results/057_repo_agents_hygiene/SEMANTIC_PRESERVATION.md` 为每个将修改的 repo 建完整 preservation table，再编辑；没有 preservation mapping 的 repo不得先改。
2. Bridge Kit先实现/测试 fresh scaffold 和 existing-repo preservation；fresh repo必须走真实 `ai-bridge init -> ai-bridge validate`，existing custom AGENTS必须在 normal/force init 下保持 project-owned prose不被迁移/重排。
3. 再按 Plan逐 repo整理：Bobbio substantial、Lucerna light、Mica testing consolidation、Asteria map conversion、SeminarArc map conversion、CUHK Date inspect-only。
4. 所有 Bridge-managed blocks只能从 canonical Bridge source生成；不得在产品repo手工重写 managed block。
5. 每个 repo记录before/after bytes/lines、authority changes、moved-rule locators和 exact diff。
6. 最后在同一 final candidate set 上执行 H1–H9；不能用“字数下降”替代 semantic preservation。

关键 hard requirements：

- Bobbio：必须消除 `Figma canonical visual source` 与旧 `Bobbio_Design_*.png` 可能形成的并列 authority；旧图只能是 historical/supporting reference。Zotero/native/knowledge/iPad安全与不变量必须保留。
- Lucerna：Windows release/tray、real provider、matching regression、screenshot helper、Longleaf 是不同 project invariants，不得为缩短而删成 generic rule。
- Mica：real long-conversation 是最终/manual authenticated acceptance；不得改成 automated authenticated ChatGPT regression。保留 privacy diagnostics、typing hot-path和focused-first testing。
- Asteria：root保留 fixed public entry、canonical browser locator + `可以自动操作页面；不能绕过页面`、GPT Work-before-human、visual/scientific-rule locator；详细runtime/tunnel/dev-server mechanics移入 `RUNTIME_OPERATIONS.md`。
- SeminarArc：Emulator-first、protected physical device不是generic connected-test target、禁止自动transport恢复、显式serial+pre/postflight、device channel failure不阻塞独立开发、secret/PIN不入repo/log/result，必须在root仍显眼；详细操作/历史放 `docs/DEVICE_TESTING.md`。
- CUHK Date不为统一格式创建root AGENTS。

Bridge scaffold hard requirements：

- 新模板只标准化 project-owned structure/ownership，不包含假的项目事实；
- fresh repo root包含 exactly one managed Bridge block + project scaffold + `prompts/AGENT_RULES.md` locator；
- root不复制 Lite execution rules；
- existing repo无论 normal/force init都不得被自动迁移成 scaffold；
- `--force` 不得解释成重写用户 project-owned AGENTS；
- 如果这些行为全部通过，Bridge candidate可从 `0.8.2` bump到 `0.8.3`；未通过不得提前bump制造完成。

H1–H9全部按 frozen Goal直接验证：semantic preservation、no contradiction、discoverability、managed-block integrity、context quality、repo-specific regression、fresh scaffold normal entry、existing-repo should-not-change、no Lite duplication。

完成后：

- freeze exact commits for AI_Skills evidence branch、Bridge、Bobbio、Lucerna、Mica、Asteria、SeminarArc，以及CUHK Date inspected ref；
- 写 `RESULT.md` / `SEMANTIC_PRESERVATION.md` / `SIZE_REPORT.md` / `MANIFEST.md`；
- ordinary commit/push exact task branches；
- 停在 `EXECUTED_UNAUDITED` / legal equivalent，交独立 implementation review；
- 不得 merge 到 main/develop，不得发布 Bridge正式版，不得开始/修改056，不得自行宣布057 achieved。

明确禁止：

- product/runtime changes；
- central AI_Skills plugin changes；
- Host Policy changes；
- 056 implementation；
- new workflow state/controller/ledger/watcher；
- paid API/Terra；
- bulk language translation solely for style uniformity；
- 删除重要安全规则只为了缩短AGENTS；
- 自动迁移 existing repos；
- 把 056 Lite rules复制进root scaffold。

若遇到未能从current source裁定的authority conflict、unrelated dirty instruction edits、managed-block drift或必须扩大文件/repo scope，保留原内容并回 Planner；不要靠猜测完成整理。

`NEXT_HANDOFF = INDEPENDENT_IMPLEMENTATION_REVIEW`
