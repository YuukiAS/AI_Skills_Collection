# v0.8 设计包与本轮证据

日期：2026-10-22。任务：`chatgpt-web--pass-integrity`。
阶段：DESIGN_REVIEW_PENDING。没有执行就绪批准，没有实施 1.8。

## 同一准确快照中的文件

调用方提供 PACKAGE_COMMIT。以下文件均从该提交读取；文件不填写自身所在提交号，避免自引用。

1. `docs/workflows/CHATGPT_WEB_USER_NEEDS_AND_PLANNER_LESSONS_2026-10-22.md`
2. `docs/workflows/CHATGPT_WEB_ARCHITECTURE_TRANSPARENCY_PROPOSAL_V0_8_2026-10-22.md`
3. `docs/workflows/CHATGPT_WEB_ARCHITECTURE_TRANSPARENCY_PLAN_V0_8_2026-10-22.md`
4. `docs/goals/CHATGPT_WEB_ARCHITECTURE_TRANSPARENCY_GOAL_V0_8.md`
5. `docs/operations/prompts/CHATGPT_WEB_ARCHITECTURE_TRANSPARENCY_KICKOFF_DRAFT_V0_8_2026-10-22.md`
6. `docs/workflows/CHATGPT_WEB_ARCHITECTURE_TRANSPARENCY_CRITIC_PROMPT_V0_8_2026-10-22.md`
7. 本文件。

## 当前用户交付的来源

Planner 当前回复的机制说明来自 Proposal §1，实施落点来自 Plan §2。不是仅把这两项作为未来要求，本轮已实际生成可审正文。

下一位 Critic 必须对照 Proposal §1 与 §4、Plan §2、稳定用户需求和直接证据。它可以推翻机制，不能预设 Planner 正确；也不能只审内部合同而不检查用户会看到什么。

当前完整 Critic 回复尚未产生，用户尚未验收 v0.8。Planner 的自行检查不叫独立通过；不能把本轮提前收入优质示例。

## 正式与历史来源

正式基线：AI_Skills_Collection main `f1de8e85957d32a50f4458349f450ec65add13bb`。本轮重新核对两份 1.7 合同、能力验收政策 1.2、维护看板、项目设置快照和仓库规则。目标设计分支的 AGENTS blob 与该 main 一致：`3c3bdc9084b05747fd862f83ab142f4c6f589236`。

旧 v0.7 包：`0bd4dbf09be68811cafac53afdaad0f671206023`。关键改变不是缩短旧文案，而是将机制说明作为受审对象、保留决定性技术身份、独立核对后复用交付。旧 Plan/Goal/Kickoff 不再适用当前设计。

真实事故来源：
- Clear Writing 原批准包：`d7b810d194ead881303aaca9c2e4f1d59a97c1f1`。
- Phase C 停止证据：`38a81dc1df9a362ecee4be597cb3db5bd6fcac41`，`results/clear-writing--single-entry-artifact-finalization/phase-c/PHASE_C_STOP_BEFORE_LIVE_MUTATION.md`。
- 已保存原始停止回复：`0bd4dbf09be68811cafac53afdaad0f671206023:results/chatgpt-web--pass-integrity/real-validation/case-b/ORIGINAL_REPLY.md`。
- 当前 Slurm 正式机制：基线 main 的 `skills/tools/hpc/slurm-workflows/SKILL.md` 受保护取消节；对应 `scripts/setup_protected_cancel.py`、`slurm_cancel_hook.py`、`slurm_protected_cancel_mcp.py` 及 `results/hpc--slurm-cancel-production-closure/FINAL_RELEASE_CLOSURE.md`。这些用于解释重要机制身份为什么必须公开，不是本任务重新运行或修改 Slurm。

Bridge 当前 AGENTS 已核对，新正式工作树不应落入 `/tmp`，普通授权与发布边界也不能由角色合同绕过。本轮不启用其任何运行器，不修改 Bridge。

外部只采用 Proposal §10 已列 AWS 官方架构决策记录的轻量原则；状态 REFERENCE_ONLY，不引入工具或运行依赖。

## 不再复用的错误主张

- 不把“无非必要英文”解释成删除 Hook、Wrapper、MCP 或具体技术名称。
- 不把所有机器信息都加入正文当作可信度。
- 不把加载 Clear Writing 当作完整回复通过。
- 不把检查过一个字段或正文存在当作解释充分。
- 不声称原生 Web 已有受控发送前拦截。
- 不让历史案例 PASS 代替当前完整审查。
- 不在测试输入里附标准归因，再称模型独立发现。

## 本轮允许的副作用

仅在现有设计分支新增本版设计文件。正式角色合同、main、release、项目设置、产品源码、Personal Plugin 均不修改；不运行产品 Gate、调度器命令、后台任务或付费验证。

维护待办见 Plan §8。精确 task key 检索无匹配 Issue，本轮未变更 Issue/Project；不声称看板已同步，不要求用户手工处理。

## 下一入口

独立 Critic，设计审查，只给 PROCEED / REVISE，并给同任务 Planner 的完整返回提示词。
当前不提供 Codex 执行入口。