# Clear Writing 0.6 通用双端架构与最终交付：原独立Critic复核 v0.7

继续同一任务，不新建版本/长期路线。用户本轮明确要求提炼多次真实反馈，设计服务整个ChatGPT/Codex写作需求的Clear Writing，不再围绕某个插件说明特判。PACKAGE_COMMIT由转交消息给定，必须读同一精确提交。

```text
repo = YuukiAS/AI_Skills_Collection
branch = design/clear-writing--single-entry-artifact-finalization
task = clear-writing--single-entry-artifact-finalization
tracking = #13
review_stage = REVISED_COMPLETE_PACKAGE_REVIEW_V0_4
previous_package = ca018937b3528b8cc62ace9c02e33c1d5f84fde6
historical_candidate = 079bd7987bb33d624d244feb415327d5cf2343d8
```

先读最新main的AGENTS、两份角色合同、Capability Gate Policy、维护看板、writing-style TODO与沟通职责边界，及Issue #13。读取目标分支当前源码和既有Phase C归因，不以过去PASS或Planner自述作证。

从exact PACKAGE_COMMIT完整读取：

- `docs/design/clear-writing/CLEAR_WRITING_0_6_PRODUCT_AND_EXECUTION_PLAN_V0_4_2026-10-22.md`
- `docs/goals/CLEAR_WRITING_0_6_UNIFIED_DELIVERY_GOAL_V0_4_2026-10-22.md`
- `docs/design/clear-writing/CLEAR_WRITING_0_6_GATE_RUNBOOK_V0_4_2026-10-22.md`
- `docs/operations/prompts/CLEAR_WRITING_0_6_KICKOFF_DRAFT_V0_4_2026-10-22.md`
- `results/clear-writing--single-entry-artifact-finalization/ACCEPTED_EXPLANATIONS_AND_BOUNDARIES_20261022.md`
- `results/clear-writing--single-entry-artifact-finalization/PLANNER_CURRENT_PACKAGE_20261022.json`
- 本提示词及Runbook精确继承的原机械/任务合同。

重点独立审查，不替Planner维护结论：

1. 新方案是否真的负责整个Clear Writing：普通问答、科研/数学解释、比较建议、进展交接、中文正式文档、长文重写、英文科研、UI和精确内容？是否把正向Slurm/Bridge/CAT例子错误固化为所有任务格式？
2. 职责与另一线程是否清楚：不改Project setting/Planner/Critic合同；事实、方法、下一owner与授权由领域/工作流负责，Clear Writing仅清晰表达和保真；普通聊天内容选择属于已定事实的读者投影，而非重新决定研究证据/科学结论。已有长文授权重写与新研究报告论证设计是否分开？
3. 最关键的改变：从“禁止改六条canonical、只改ChatGPT包装”改为在既有response-clarity中重整普通回复工作步骤、在writing-fidelity中集中最终全文绑定，包装只路由，Codex直接技能共享相同能力。此归属是否最小且合理，是否重复六条既有路线，是否伤及下游？不能把“六能力保留”误解为“六文件不得修”。
4. 不是增加同义规则：实际工作步骤是否从当前问题/深度和不变量开始，再选内容、组织解释、生成全文、对照原题/来源审校、交付同一文本？是否保护简短问题、深入推导、精确机器内容及用户允许的编辑幅度？
5. GitHub文本的三个独立条件是否闭合：正确内容/保真、全文读者质量、真正保存同一候选；聊天与文件是否各自处理。检查existing update、new create、预写身份、完整回读的真实工具合同；事后parent检查不能宣传成事务锁。Codex本地写入/回读与授权后remote publish不得混淆。
6. G1–G6是否仍覆盖同一候选、真实Web、完整来源/聊天/仓库文件、已知负例与正向深度、独立定性审查和唯一fresh？G5能否通过既有Codex六路实质输出证明双端消费，而非仅生成hash相同；不凭一端PASS代签另一端。
7. Phase C仍有真实归档字节与Web操作前置。当前只读导出确认tar.gz，但本轮下载网络失败，不能冒充restore PASS。必须判断现有责任、工具与材料交接是否已足以执行；不接受“以后找到一个环境即可”就给execution-ready。未知若阻塞，指出最小条件及既有负责人，不扩新系统。
8. 原0.5.0不变、旧候选仅历史、archive兼容与共享写作源必须冻结为同一新候选。仓库当前发布已推进，不能从旧5.5.1回退覆盖Slurm。版本、README/changelog、Issue #13与#73/#49保持真实。

本轮只读，不修改仓库/Issue/Project，不启动Codex，不更新个人插件，不建G3分支，不跑G1–G6，不调用付费API。

审查完整包及正常成功/关键失败/恢复链。若全部已闭合，可按最新角色合同给唯一 `PASS / READY_FOR_CODEX=YES` 并直接输出短中文Codex handoff，准确绑定本PACKAGE_COMMIT；不是已实现/已发布证明，不替代用户发送执行指令。若尚缺现实前置或需修语义，给 `REVISE / READY_FOR_CODEX=NO`，使用稳定 `CW06-U4-xx` finding，直接给当前Planner最小完整返修prompt。若只接受产品方向但未达执行就绪，按合同用 `PROCEED / READY_FOR_CODEX=NO` 明确下一步仍属Planner，不允许混用为执行授权。不要新增审批轮次或自动控制层。
