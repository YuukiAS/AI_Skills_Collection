你现在担任 Presentations 的独立 Critic，审查一个极小的 CI portability repair；不要重做 Presentation 架构。

Active Design Context：
- target_repo: `YuukiAS/AI_Skills_Collection`
- target_plugin_or_domain: `presentations`
- design_topic_or_task_key: `presentations--ci-missing-render-contract-repair`
- source_branch_or_ref: `reviewed/presentations--ci-missing-render-contract-repair`
- review_stage: `execution-ready bounded repair`
- base main: `38a76797439c6b29098aade7539270cbc51e8836`
- upstream regression commit: `f717d28beef4dd1cbbb66cb491712769d1250aac`
- observed failing CI: `39097236717`

先读取 latest main 的 Planner/Critic contracts、Plugin Capability Gate policy、AGENTS、Presentations TODO/Issue #98，再读取本 package：

- `automation/reviewed_handoff/tasks/presentations--ci-missing-render-contract-repair/REQUEST.md`
- `docs/design/presentations/PRESENTATIONS_CI_MISSING_RENDER_CONTRACT_REPAIR_V0_1_2026-10-18.md`
- `docs/goals/PRESENTATIONS_CI_MISSING_RENDER_CONTRACT_REPAIR_GOAL_V0_1_2026-10-18.md`
- `docs/operations/prompts/PRESENTATIONS_CI_MISSING_RENDER_CONTRACT_REPAIR_KICKOFF_V0_1_2026-10-18.md`

并直接核对当前：
- `generate_cuhk_scientific_layout_stage3.py`
- 两个 validator
- `tests/test_presentations.py`
- `.github/workflows/codex-marketplace.yml`

重点判断：

1. 根因是否确实是 generator 新增 `BLOCKED_MISSING_CANONICAL_FONT_RESOURCE` 后，validator/test 没同步，而非 Clear Writing 缺陷；
2. 无 engine 时先报告 `BLOCKED_MISSING_TEX_ENGINE` 是否是与现有 validator/test 一致的最小 primary-status 修复；
3. `--allow-missing-render` 接受 canonical-font missing 是否符合已有“typed installation/resource error”设计，同时 strict mode 仍 fail closed；
4. 是否应拒绝安装完整 TeX/私有 font bundle 到 CI 作为替代，因为那会掩盖 portability bug；
5. test 是否必须覆盖 no-engine/no-font 与 engine/no-font 两种状态，且不能靠关键词/skip；
6. scope 是否严格限于三份 Presentations script + tests + generated mirrors；
7. 是否保持 `workflow-core + ai-skills-core + presentations` 维护合同。

给 PASS 或 REVISE。

PASS 只表示可执行，不表示 Presentations release PASS。若 PASS，请返回 `NEXT_HANDOFF=PLANNER`，不要修改 CURRENT；Planner 后续再 materialize task-local PLAN 并交付已审过 Kickoff。
