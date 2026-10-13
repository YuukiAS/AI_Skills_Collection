# Clear Writing 首轮全仓 CI 阻断 — Planner 单次最小恢复判断

- 当前角色：原长期 Planner；恢复阶段：第一次 `NEEDS_GPT_PLANNER`；**不属于新的设计任务或正式插件实现**。
- 仓库与任务：`YuukiAS/AI_Skills_Collection` / `clear-writing--cross-surface-language-layer`。
- 同一执行分支：`reviewed/clear-writing--cross-surface-language-layer`；本轮进入时远端提交 `8633961c871c522191ce76cc1a7d7761fdb274bf`。
- 原冻结 PLAN：`automation/reviewed_handoff/tasks/clear-writing--cross-surface-language-layer/PLAN.md`；获批包 `b960ec57941fc058a22ca8896c92d5dc19191009`，执行前 Critic PASS `0f8ee7d98ba8890d074b488c87cb65c20cd8b82f`。
- 实现提交：`cac70c3bfcce6aeeba9c3e80adfa317235b54ee9`，保留不动。
- 第一轮独立 Reviewer：`results/clear-writing--cross-surface-language-layer/REVIEW_1.md`；`REVISE` 仅因必需 CI 失败，**未完成产品质量判定**。
- 必需 CI：`https://github.com/YuukiAS/AI_Skills_Collection/actions/runs/38260835399`，测试提交 `64d9efdf0c2f1cf15485bade34d085c694d2e62a`，`codex-marketplace` 作业 `114850626740` 失败。全仓单元测试共 341 项，5 项失败；其后的生成与校验步骤被跳过，不能判定整条 CI 成功。
- 恢复前状态：`CURRENT.state=NEEDS_GPT_PLANNER`、`next_action=RUN_GPT_PLANNER`、`plan_revision=0`、`review_round=1`、`ci_required=true`、`ci_status=FAIL`、`implementation_commit=cac70c3bfcce6aeeba9c3e80adfa317235b54ee9`。
- 本次决策：**没有处于已批准 Clear Writing 范围内、现在可直接运行并使全仓 CI 合法通过的最小修复。暂停冻结，不消费唯一剩余计划修订与第二轮 Reviewer 预算；需要跨领域源或仓库级验收代码的最小权限更改先交独立 Critic。**

## 1. 核查既有维护成果与错误归因

按 Reviewer `CW-CI-01` 对照当前仓库来源与现有分支，结论如下：

1. `tests/test_central_plugin_icon_assets.py` 的图标/版本测试把 `VERSION` 写死为 `5.5.0`；本任务基线、最新 `main` 与当前 `release` 实际均为 `5.4.4`。在该测试未根据当前有效版本合同修正前，不能为满足断言擅自提升仓库版本。此为仓库级测试/版本合同维护，**不是** `response-clarity` 行为修复。
2. `tests/test_codex_marketplace.py` 两项失败把所有 `docs/plugin-todos/*.md` 强制等同十个中央插件名称；实际已有合法工作流程专属 TODO。这是中央维护清单与测试假设不一致，不能为通过 CI 删除七份有效 TODO，也不能把该问题算为 Clear Writing 技能缺陷。
3. 同一测试集的生成层一致性报告 16 处差异，现有 Executor `IMPLEMENTATION_EVIDENCE.md` 定位于 `plugins/codex/plugins/presentations` 与 `plugins/codex/plugins/research-writing`，不属于本 task 的 `writing-style` 源生成修改。此前确实运行生成器，但 Executor 特意没有提交这些跨范围更改；**尚无在最新 main 上独立完成整套生成/全仓测试的实测 PASS**，不能凭推断声称 main 已干净。
4. `tests/test_presentations.py` 的源/已生成镜像比较失败；Reviewer 已核对其测试与 Presentations 源在基线到 Clear Writing 实现之间未变。这是 Presentations 所属专业镜像一致性问题，不能在 Clear Writing 任务里直接覆盖其正式载荷。

截至此次只读核对：最新 `main@6fcbde22b334e471736debfee4d1d86084e8b270` 相对任务 `CURRENT.base_commit=34e47fe6d0dc06d57ee1e6e37c0ff0f2fdfefc1b` 的后续改动仅涉及 Slurm 方案/待办文档，没有上述五项测试或生成层的正式修复。`release@06d135d8a6ee62cd41abb40fc5771fcef7f8db25` 同样为 `VERSION=5.4.4`，而非可直接替换的修复版本。

现有其他维护分支也不能当成获批准的即时修复：`work/presentation-historical-blackbox-validator-v1` 相对 main 落后大量提交，主要新增演示文稿历史渲染验证器，不修上述版本/TODO 测试；`work/research-authoring--formal-production-authoring` 与 main 大幅分叉，涉及大量 Research Authoring 载荷与未整合成果，用户已明确禁止本任务覆盖；另两条 Research Authoring 工作分支只修改其专属 TODO。**没有发现既已完成、可安全单独移植且解决全部五项问题的权威提交。** 不进行未经审批的 cherry-pick、merge、regen、版本提升或 CI 跳过。

## 2. 只做一个恢复决定

**决定：保留既有 Clear Writing 实现和冻结标准；在独立 Critic 允许最窄的跨负责人基线修复或源消费方式之前，不冻结修订版 PLAN、不释放 Codex 进行第二轮无效 CI。**

最小首选路径是让各正式负责人在其原有治理与发行合同内解决本来就存在的仓库级基线：
- `ai-skills-core`／仓库维护负责人：修正测试中与版本合同、中央插件 TODO 与流程专属 TODO 的错误假设，不能动真实版本或删除合法维护证据。
- Presentations 正式负责人：核对源文件与生成镜像的权威并完成必要正式校验；不由本 task 擅自覆盖。
- Research Authoring／正式生成层负责人：核对其正式源与打包载荷的一致性。Research Authoring 依用户要求**继续冻结**；本次不能直接动它，若需要变更先有本领域明确授权。
- 中央构建负责人：确认最终修复后完整生成层和全仓 CI 能从正式入口通过，不在测试中静默忽略跨插件差异。

如这些修复由既有维护工作合法集成至主线，Planner 再核实精确提交/范围，并决定能否按冻结合同合法引入当前任务。**在现有事实下，立即引入跨插件/全仓测试变更、为当前任务单独放宽 CI，均需新的独立 Critic 审查；不能由 Planner 自行允许。** 本次不创建新任务、新分支、后台运行器、额外 Gate 或减少任何全仓测试。

只有原始五项失败真正修复、当前 reviewed 分支的新候选全仓必需 CI 直接通过、Reviewer 取得完整证据后才能继续原有产品验收；别的主线/维护分支 PASS 不可拼接为当前任务 PASS。

## 3. 保留与后续角色交接

本次只提交这份恢复判断文件，**不修改**既有 `PLAN.md`、`CURRENT.json`、`REQUEST.md`、第一轮 `REVIEW_1.md`、`RESULT.md`、实现源码、Research Authoring、Presentations、根版本与测试。保持 `NEEDS_GPT_PLANNER / RUN_GPT_PLANNER`、`plan_revision=0`、`review_round=1`、`ci_status=FAIL`，剩余一次合法 Planner 修订与一次 Reviewer 轮次完整保留。等待权威修复／独立复核不是产品失败，不把当前任务标为已完成或重新 bootstrap。

### 下一位独立 Critic 的定向判断

审查对象为**本恢复记录所绑定的 reviewed 分支精确提交**、已批准 v0.3 冻结 PLAN、第一轮 `REVIEW_1.md`、CI `38260835399` 与上述仓库核查结果。请先确认 `CW-CI-01` 五项失败的真实归因，独立核实是否存在当前任务批准范围内真正能修绿全仓 CI 的小改动；若没有，判定能否仅允许**已有正式维护成果经各负责人的授权集成后，再由本任务只消费已批准修复**，而不修改 Clear Writing 的产品架构、Research Authoring/Presentations 源和 CI 门槛。若必须直接扩大本任务到通用测试或跨插件生成层，明确说明**需要的最小授权/审查范围**，不要自行替 Planner 冻结 PLAN 或宣布 CI 已通过。返回 `PASS` 或 `REVISE` 及必要最小条件；在获得同范围正式批准之前，任务继续合法停在 `NEEDS_GPT_PLANNER`。不创建 successor 或追加 Reviewer 次数。
