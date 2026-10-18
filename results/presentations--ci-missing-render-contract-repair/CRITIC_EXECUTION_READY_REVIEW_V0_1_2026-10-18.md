# Presentations CI missing-render contract repair v0.1 — 独立 Critic execution-ready 审查

- target_repo: `YuukiAS/AI_Skills_Collection`
- target_plugin_or_domain: `presentations`
- design_topic_or_task_key: `presentations--ci-missing-render-contract-repair`
- source_branch_or_ref: `reviewed/presentations--ci-missing-render-contract-repair`
- review_stage: `execution-ready bounded repair`
- package semantic head: `3990ee71705fc0fda654b565e90d8038183cf82f`
- current handoff head before this review: `8c928ef19037d8024b185669d1392e9b90ff7817`
- base main: `38a76797439c6b29098aade7539270cbc51e8836`
- upstream regression commit: `f717d28beef4dd1cbbb66cb491712769d1250aac`
- observed failing CI: `39097236717`
- latest main checked: `9c284187e16164199933bb458fb1604ac6f733ff`
- latest Bridge Kit main checked: `fa560cb36f8203866e9d3e237d6879578377be0e`
- decision: **PASS**
- new blocking findings: **NONE**

本 PASS 只批准这份极小 portability repair 进入 Planner freeze / Executor 实现；不代表 Presentations release、真实视觉产物、Issue #98 全部范围或 Clear Writing 已通过。本 Critic 不修改 `CURRENT.json`。

## 1. 根因归因：PASS

真实 CI `39097236717` 的 head branch 是 `reviewed/clear-writing--scientific-explanation-readability-repair`，不是本 Presentations repair 分支。这一点必须如实记录。

但它仍是有效的 Presentations portability 回归证据：

- 该 CI head 的历史包含 `f717d28beef4dd1cbbb66cb491712769d1250aac`；
- 失败 job 是全仓 `python3 -m unittest discover -s tests`；
- 347 项测试中只有 3 项失败，全部位于 `tests/test_presentations.py`：
  - `test_cuhk_scientific_layout_stage3_contract`
  - `test_research_presentation_one_call_production_entry`
  - `test_research_presentation_deck_quality_loop_consumes_review_and_fails_closed`
- 日志直接显示：
  - dependency probe 观察到没有 TeX engine；
  - manifest primary status 却是 `BLOCKED_MISSING_CANONICAL_FONT_RESOURCE`；
  - 两个 `--allow-missing-render` 路径均把该新状态当失败。

当前 Clear Writing production source 不是这三项失败的调用方，也没有证据表明它改变 Presentations validator 语义。

`f717d28...` 的真实 diff 新增了 canonical font resource binding 和 `BLOCKED_MISSING_CANONICAL_FONT_RESOURCE`；当前 `compile_pdf()` 先获得 engine locator，却在 `if not engine` 之前执行 `materialize_font_binding()` 并优先返回 font-resource blocker。与此同时两个 validator 的 allowlist 仍只有旧的 missing engine/package/pdf-renderer 状态，Stage 3 test 对有无 engine 的断言也仍是旧合同。

因此根因确实是 **generator 新 typed dependency state 与 validator/test missing-render contract 没同步**，不是 Clear Writing 缺陷。

## 2. no-engine primary status：PASS

批准 R1：

- `compile_pdf()` 先判定 TeX engine 是否存在；
- 若不存在，primary compile status 为 `BLOCKED_MISSING_TEX_ENGINE`；
- 不在该 primary decision 前要求 font materialization 成功。

这与当前 Stage 3 validator 的既有显式合同一致：当 `dependency_probe.tex_engine_available != true` 时，compile status 必须映射为 `BLOCKED_MISSING_TEX_ENGINE`。

它也不会隐藏字体问题，因为 `dependency_probe()` 本身独立调用 `font_resource_binding()`，仍可记录 canonical fonts 同时缺失。也就是说：

- primary blocker：当前最前置、足以阻止 compile 的 TeX engine 缺失；
- secondary evidence：字体资源是否也缺失仍保留在 dependency probe。

这是最小状态一致性修复，不是改变字体策略。

## 3. allow-missing-render 接受 canonical-font missing：PASS

批准 R2，但只限显式 `--allow-missing-render`。

当前两个 validator 已经把下列状态视为“当前主机不能真实 render、但可以继续验证 non-render contract”的 typed environmental states：

- `BLOCKED_MISSING_TEX_ENGINE`
- `BLOCKED_MISSING_TEX_PACKAGE`
- `BLOCKED_MISSING_PDF_RENDERER`

`BLOCKED_MISSING_CANONICAL_FONT_RESOURCE` 在 `f717d28...` 后属于同类安装/资源缺失状态，因此加入这个**显式 non-render allowlist** 与现有设计一致。

严格模式仍 fail closed：
- `allow_missing_render=false` 时 helper 不放行；
- Stage 3 strict branch 仍把非 `ok` render status 报错；
- production-entry strict validator 仍把 failed render probe 作为 error。

不得把 `BLOCKED_FONT_RESOURCE_TOKEN_MISSING`、unexpected font、source 缺失或其他 product/source defect 加入 allowlist。这些不是环境“没装”，而是产品/生成内容错误。

## 4. 拒绝给 CI 安装完整 TeX / 私有 canonical font bundle：PASS

现有 workflow 的 `codex-marketplace` job 只安装 Python presentation regression dependencies，然后运行全仓单测；它没有安装 TeX，也没有安装 renderer-owned private/local resource bundle。

仓库现有设计已经给 `--allow-missing-render` 一个明确用途：在不能真实 render 的主机上继续检查 non-render contract。为了让这三项测试绿而给 GitHub runner 安装完整 TeX 或复制 host-local font bundle，会掩盖 generator / validator 的 portability state mismatch，而且会把 CI 变得更重。

GitHub 官方文档也把 hosted runner 描述为按镜像提供的临时 VM；额外软件应由 workflow 显式安装，镜像的预装软件会持续更新。项目自己的私有/host-local font resource 更不应被假定为 runner 固有状态。

所以本 repair 应修**状态契约**，而不是把 GitHub CI 伪装成生产 render host。

## 5. 两种缺失状态的 regression coverage：PASS

R3 的最小覆盖是必要且足够的：

1. no engine + no canonical font resource  
   -> primary compile status 必须是 `BLOCKED_MISSING_TEX_ENGINE`；
2. engine available + canonical font resource missing  
   -> 可以得到 `BLOCKED_MISSING_CANONICAL_FONT_RESOURCE`；
3. 两者在显式 `--allow-missing-render` 下通过 non-render contract；
4. strict mode 对两者仍拒绝；
5. source/generated 三份脚本保持 parity。

测试应通过 deterministic seam / mock 真正控制 engine/resource availability，而不是：
- 根据当前 CI 主机碰巧装了什么来分支；
- grep 一个状态字符串就算通过；
- skip 测试；
- 真安装 TeX 来制造“engine present”案例。

当前 source/generated 三份目标脚本的 blob 逐份完全一致，因此修复后也应继续通过正式 generator 保持一致。

## 6. scope：PASS

批准范围严格限于：

- `generate_cuhk_scientific_layout_stage3.py`
- `validate_cuhk_scientific_layout_stage3.py`
- `validate_research_presentation_production_entry.py`
- `tests/test_presentations.py`
- 正式 Marketplace generator 产生的对应 Presentations mirrors
- task-local evidence

不批准：

- `.github/workflows/codex-marketplace.yml` 改装 TeX/font 的方案；
- CUHK/course-standard 模板架构；
- typography / font-policy identity；
- renderer resource ownership；
- Presentations routing/version/changelog/README；
- Clear Writing；
- Issue #98 的 broader shared-core implementation。

当前 branch 与 latest main 在三份脚本、`tests/test_presentations.py` 和 workflow 上 blob 相同，所以不存在一个尚未纳入 package 的最新目标代码变化。

## 7. maintenance contract：PASS

该任务是中央 Presentations production refinement，必须继续按已有：

`workflow-core + ai-skills-core + presentations`

执行。Package 已明确记录这一 maintenance contract；Executor 还必须遵守 latest `AGENTS.md` 的 source authority、generated-layer 和 full regression 规则。

Issue #98 可以作为相关的 Presentations font-policy / shared-core umbrella context：其评论已经明确 canonical font policy 与 renderer-owned `render_resources/chinese_math_pdf`。但这个极小 CI repair**不得被描述成关闭 Issue #98**；#98 的主体仍是 shared Beamer core + two skins，范围明显更大。

## 8. Capability / evidence boundary

这是一个窄 portability regression，narrow gate 合理，因为：

- 不改 layout/visual output；
- 不改 routing/default prompt/profile；
- 不改 shared schema/generator topology；
- 不改用户可见 presentation semantics；
- 只同步既有 typed missing-environment contract。

同一最终候选仍必须直接通过：

- 两类 dependency-state focused regressions；
- full `tests/test_presentations.py`；
- full repository tests；
- source/generated parity；
- Marketplace write/check + second clean check；
- `git diff --check`；
- GitHub-hosted runner required CI。

CI 绿灯只能证明该 portability repair 和相关回归门槛通过，不等于 Presentations 整体 artifact/release PASS。

## Final decision

```text
DECISION=PASS
NEW_BLOCKERS=NONE
APPROVED_PLAN_PATH=docs/design/presentations/PRESENTATIONS_CI_MISSING_RENDER_CONTRACT_REPAIR_V0_1_2026-10-18.md
APPROVED_GOAL_PATH=docs/goals/PRESENTATIONS_CI_MISSING_RENDER_CONTRACT_REPAIR_GOAL_V0_1_2026-10-18.md
APPROVED_KICKOFF_PATH=docs/operations/prompts/PRESENTATIONS_CI_MISSING_RENDER_CONTRACT_REPAIR_KICKOFF_V0_1_2026-10-18.md
APPROVED_PACKAGE_COMMIT=3990ee71705fc0fda654b565e90d8038183cf82f
NEXT_HANDOFF=PLANNER
READY_FOR_CODEX=NO
```

按用户当前要求，下一步先由 Planner 将已批准内容 materialize 到 task-local `PLAN.md`，合法执行 `PLAN_REQUESTED -> PLAN_FROZEN`，保持 `plan_revision=0`、`review_round=0`；随后由 Planner 逐字交付已审过的 Kickoff。Critic 不修改 `CURRENT.json`。
