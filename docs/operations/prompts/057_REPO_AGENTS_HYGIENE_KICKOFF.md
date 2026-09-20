# 057 Repo AGENTS Hygiene — Codex Kickoff Draft

- Execution package version: `v0.2`
- Task: `057_repo_agents_hygiene`
- Plan: `docs/design/057_REPO_AGENTS_HYGIENE_IMPLEMENTATION_PLAN.md` v0.2
- Goal: `docs/goals/057_REPO_AGENTS_HYGIENE_GOAL.md` v0.2
- Bounded amendment: `docs/design/057_LITE_VERSIONING_DEFAULT_AMENDMENT_2026-09-17.md`
- Status: `DRAFT_NOT_AUTHORIZED`

Only after independent Critic reviews this exact package and returns `READY_FOR_CODEX=YES` does the user sending the approved `## Kickoff` text authorize execution.

## Kickoff

执行 `057_repo_agents_hygiene`，严格按已审 v0.2 Plan/Goal；这是 instruction-surface hygiene + Bridge fresh-repo scaffold +（仅若本 v0.2 Critic 明确批准）Lite 默认版本规则任务。不要重新设计 056，不修改任何产品/runtime。

本次授权范围：

- `YuukiAS/AI_Skills_Collection`：从届时最新、仍包含获批 v0.2 package 且无相关语义漂移的 `origin/main` 创建 exact branch `reviewed/057_repo_agents_hygiene`，优先从已验证本地 canonical checkout 建 task-owned clean worktree。只允许写 `results/057_repo_agents_hygiene/` evidence/result/manifest 和当前 Goal 明确需要的 057 control artifact；不改中央 plugin production。
- `YuukiAS/GPT_Codex_AI_Bridge_Kit`：从届时最新 `origin/main` 创建 exact branch `reviewed/057_repo_agents_hygiene` 和 task-owned worktree。允许实现 `templates/repo/AGENTS_TEMPLATE.md`、`ai_bridge_kit/cli.py` fresh/existing AGENTS init 行为、相关 tests/docs/changelog/version `0.8.3` candidate；若本 v0.2 Critic 批准 versioning amendment，还允许修改 canonical `templates/prompts/AGENT_RULES.md`，加入 fallback versioning contract。不得改 Host Policy、056 Default prompt transport、Review/Control 状态机或其它无关能力。
- `YuukiAS/Bobbio`：从届时 current `origin/develop` 创建 exact branch `reviewed/057_repo_agents_hygiene`。允许修改 `AGENTS.md`；允许 `docs/PRODUCT_DESIGN_BRIEF.md` **仅**修改 visual/source-of-truth / old-PNG positioning 文字；只有 preservation table 证明有 unique moved detail 时才允许修改 `docs/DEVELOPMENT_WORKFLOW.md` / `docs/quality/NATIVE_DESKTOP_ACCEPTANCE.md`。不得改 Figma、product code、schema、runtime version。
- `YuukiAS/Lucerna`：从届时最新 `origin/main` 创建 exact branch `reviewed/057_repo_agents_hygiene`。只允许轻量整理 `AGENTS.md` 的 project-owned 部分；Bridge managed block必须保持 canonical；不得改产品/source/runtime。
- `YuukiAS/Mica-for-ChatGPT`：从届时最新 `origin/main` 创建 exact branch `reviewed/057_repo_agents_hygiene`。只允许整理 `AGENTS.md`；不得改 extension/runtime/version。
- `YuukiAS/Asteria`：从届时最新 `origin/main` 创建 exact branch `reviewed/057_repo_agents_hygiene`。只允许修改 `AGENTS.md` 和新增 `docs/operations/development/RUNTIME_OPERATIONS.md`；不得改 product/runtime，也不得改 `prompts/AGENT_RULES.md`。若发现必须改 delegated rule 才能解决真实 contradiction，停止并回 Planner。
- `YuukiAS/SeminarArc`：从届时最新 `origin/main` 创建 exact branch `reviewed/057_repo_agents_hygiene`。只允许修改 `AGENTS.md` 和 `docs/DEVICE_TESTING.md`；不得改 Android/runtime/product，不新建第三份 device/environment manual。
- `YuukiAS/CUHK_Date`：只读检查 current prototype instruction surface；不得创建 root `AGENTS.md`，不得修改 repo。
- CARE Challenge、Server/VPS、EAT Research 完全不在本次 mutation scope。

Git/source 授权：

- 允许 ordinary fetch、读取 remote authority、创建上述 exact task branches/worktrees、task-owned stage/commit/push 到上述 exact task branches；
- 先复用本机已有 canonical repo并核 identity/origin/base/freshness/dirty ownership；unrelated dirty必须保护；本机没有可用 source 才允许 network clone；
- 不授权 remote remap、force push、rebase/history rewrite、删除branch/tag、PR、main/develop merge或 unrelated repo mutation；
- exact task branch 若已存在且 ownership 不清，停该 repo 回 Planner，不另造 branch 名。

执行顺序：

1. 先在 `AI_Skills_Collection/results/057_repo_agents_hygiene/SEMANTIC_PRESERVATION.md` 为每个将修改 repo 建 preservation table；没有 mapping 不得先改。
2. Bridge Kit实现/测试 fresh scaffold、existing-root preservation；若 versioning amendment已获批准，同一候选把 fallback version policy写入 canonical Lite `templates/prompts/AGENT_RULES.md`，root scaffold只做 locator，不复制规则。
3. 再按 Plan逐 repo整理：Bobbio substantial + authority closure、Lucerna light、Mica testing consolidation、Asteria map conversion、SeminarArc owner closure/map conversion、CUHK Date inspect-only。
4. Bridge-managed blocks只能从 canonical Bridge source生成；不得在产品repo手工重写。
5. 每个repo记录before/after bytes/lines、authority changes、moved-rule locators、exact diff；字数下降不能代替语义保留。
6. 最后在同一 final candidate set 上执行 H1–H9。

Bobbio hard requirements：

- final `AGENTS.md` + `docs/design/FIGMA_HANDOFF.md` + `docs/PRODUCT_DESIGN_BRIEF.md` 必须一致：Figma = current canonical visual design/components/screen composition；Product Design Brief = durable product/interaction constraints；old `Bobbio_Design_*.png` = historical/supporting visual references，不是 parallel production authority；
- `PRODUCT_DESIGN_BRIEF.md` 只改 authority wording，不借机重写 design brief；
- Zotero/native/knowledge/iPad安全与不变量必须保留。

SeminarArc hard requirements：

- final ownership必须变成 root AGENTS = prominent physical-device safety summary + locator；`docs/DEVICE_TESTING.md` = detailed device/environment/test mechanics、command restrictions、volatile inventory、historical incident evidence；
- 更新 `DEVICE_TESTING.md` 当前“完整物理真机约束以 AGENTS.md 为最高优先级”的 stale/circular owner wording；
- root仍显眼保留 Emulator-first、protected physical device不是generic connected/instrumentation target、禁止 agent 自动 transport recovery/reset、authorized physical write必须 explicit verified serial + preflight/postflight、physical channel failure不阻塞独立WSL/headless/Emulator、PIN/secret不进repo/task/result/log/screenshot/commit；
- 不削弱安全，不新建第三份device/environment manual。

其他 repo hard requirements：

- Lucerna：Windows release/tray、real provider、matching regression、screenshot helper、Longleaf 是 distinct project invariants，不得为缩短而删成 generic rule。
- Mica：real long-conversation 是 final/manual authenticated acceptance，不得变成 automated authenticated ChatGPT regression；保留 privacy diagnostics、typing hot path、fail-open、focused-first testing。
- Asteria：root保留 fixed public entry、canonical browser locator + `可以自动操作页面；不能绕过页面`、GPT Work-before-human、visual/scientific-rule locator；详细 runtime/tunnel/dev-server mechanics只放一个 `RUNTIME_OPERATIONS.md` owner。
- CUHK Date不为统一格式创建root AGENTS。

Lite versioning hard requirements（仅在本v0.2 Critic批准 amendment 后生效）：

- explicit current repo-local versioning policy优先；无本地规则时默认 `MAJOR.MINOR.PATCH`；
- PATCH=compatible repair；MINOR=compatible user-visible capability；MAJOR=incompatible contract/migration且必须显式Planner/user批准；
- `0.y.z`可用于initial development；`1.0.0`是显式稳定/default-use决定；
- 不得自行发明 `alpha` / `beta` / `rc` / `preview` / date / arbitrary prerelease suffix；只有approved repo lifecycle或explicit current task/user authorization才可使用；
- 不得让同一个formal version代表两个不同的user-consumable runtime candidates；
- commit/build label不能替代formal version；release-ready时version/source/changelog必须一致；
- root scaffold不复制这些version rules，只定位到Lite owner。

Bridge scaffold hard requirements：

- fresh repo root = project scaffold + exactly one canonical managed Bridge block + `prompts/AGENT_RULES.md` locator；
- existing root无论normal/force init都不得被自动迁移/重排；
- `--force`不得解释成重写用户project-owned AGENTS；
- H7/H8必须走真实 `ai-bridge init` / `validate` behavior；
- root不复制Lite execution/versioning policy；
- H7–H9/full regression通过后Bridge candidate才可从 `0.8.2` bump到 `0.8.3`。

H1–H9直接按 Plan/Goal验证，不新增H10。H2必须直接比较Bobbio三方authority和SeminarArc两层owner，不能只grep locator。

Final-candidate identity必须使用two-stage closure：

Stage A：提交 finalized `RESULT.md` / `SEMANTIC_PRESERVATION.md` / `SIZE_REPORT.md` / H1–H9 evidence，得到 evidence commit `E`；tracked content不写自己的E SHA。

Stage B：只更新 `MANIFEST.md`，记录 `AI_SKILLS_RESULT_COMMIT=E`、Bridge/version、Bobbio/Lucerna/Mica/Asteria/SeminarArc candidate commits、CUHK inspected ref、H1–H9 evidence locators，提交为 manifest commit `M`；MANIFEST不写自己的M SHA。最终handoff在聊天/result外部报告 `AI_SKILLS_MANIFEST_COMMIT=M`，独立implementation review以M绑定的exact tuple为对象。

完成后：

- ordinary commit/push exact task branches；
- 停在 `EXECUTED_UNAUDITED` / legal equivalent，交 independent implementation review；
- 不merge main/develop，不正式release Bridge，不执行/修改056，不自行宣布057 achieved。

明确禁止：product/runtime changes、central AI_Skills plugin changes、Host Policy changes、056 implementation、new workflow state/controller/ledger/watcher、paid API/Terra、bulk translation、删除安全规则只为缩短、自动迁移existing repos、在root复制Lite rules、在057中批量规范现有repo历史版本号/alpha-beta-rc历史。

057和056都集成完成后，用户要求另开一个经Planner/Critic审查的完整active-repo adaptation round，届时统一检查Bridge/Lite、root/delegated AGENTS、version authority/parity、repo-local override/prerelease history和056 consumption；本057不提前扩这个mutation scope。

若遇到无法从current source裁定的authority conflict、unrelated dirty instruction edits、managed-block drift或必须扩大scope，保留原内容并回Planner，不靠猜测。

`NEXT_HANDOFF = INDEPENDENT_IMPLEMENTATION_REVIEW`
