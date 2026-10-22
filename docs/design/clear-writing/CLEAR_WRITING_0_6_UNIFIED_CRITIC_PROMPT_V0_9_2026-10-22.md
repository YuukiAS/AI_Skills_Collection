# Clear Writing 0.6 — 同一GPT真实编辑流程与GitHub写前质量：独立执行前复核 v0.9

你继续担任原Clear Writing 0.6任务独立Critic。这不是新版本、新任务或再设计中央审稿系统，而是针对用户指出的**同一GPT自审空转、曾加载Clear Writing仍写得难读、GitHub文件写入前缺少真正全文质量变化**作最后的具体实施合同返修。

```text
target_repo = YuukiAS/AI_Skills_Collection
target_plugin_or_domain = writing-style / Clear Writing
design_topic_or_task_key = clear-writing--single-entry-artifact-finalization
branch = design/clear-writing--single-entry-artifact-finalization
tracking = #13
review_stage = FINAL_EXECUTION_READY_REVIEW_V0_4_PREWRITE_QUALITY
prior_package = aed114cb5bd001466e84f771443902672a4f5b1a
previous_impl_candidate = 079bd7987bb33d624d244feb415327d5cf2343d8
```

从用户转交的唯一 `PACKAGE_COMMIT` 完整读取：
- `docs/design/clear-writing/CLEAR_WRITING_0_6_PRODUCT_AND_EXECUTION_PLAN_V0_4_2026-10-22.md`
- `docs/goals/CLEAR_WRITING_0_6_UNIFIED_DELIVERY_GOAL_V0_4_2026-10-22.md`
- `docs/design/clear-writing/CLEAR_WRITING_0_6_GATE_RUNBOOK_V0_4_2026-10-22.md`
- `docs/operations/prompts/CLEAR_WRITING_0_6_KICKOFF_DRAFT_V0_4_2026-10-22.md`
- `results/clear-writing--single-entry-artifact-finalization/PLANNER_CURRENT_PACKAGE_20261022.json`
- 此版审查提示词。

先真实读取最新main `AGENTS.md`、两份Planner/Critic1.7合同、Capability Gate Policy1.2、维护看板、writing-style TODO，核对原正式0.5 plugin已加载行为、target branch代码、canonical `response-clarity` `writing-fidelity` `chinese-prose` `scientific-rewrite` 实际内容与既有Phase C原始失败；不得从Planner说“已经解决”推断生产已修。

**独立核对下列实质问题：**

1. **前置内容选择是真修还是旧话再说？** 旧 `response-clarity` 是否只先拿known result再做语言处理？新版是否明确把用户的读者问题与概念依赖排在正文生成之前，产生能直接改变段落内容、顺序、解释层级的具体编辑步骤？是否尊重短答、深入数学、精确机器内容与用户要求的完整审计？
2. **同一模型第二阶段有可执行检验对象吗？** 审的不是“我做得好吗”，而是原始用户问题、完整源文以及**已经成形的整篇候选**。候选是否真正纠正了无读者价值章节、推理跳跃、无根据简化、段落/英文问题？是否必须真实修改候选并重读受影响全文，而不能仅自述PASS？普通GPT不新增第二模型/服务/人工审批，但不能因此跳过写前全篇编辑。
3. **GitHub全文路线真实可行吗？** 现有 `fetch_file/update_file/create_file` tool语义、完整UTF-8源/blob、写前候选/审核、工具`content`参数不另生成正文、条件写入、新建非覆盖、写后全篇回读是否已经绑定？如果ChatGPT正常Web不能运行`scientific-rewrite`要求的支持helper或不能在同一会话真正使用已选Clear Writing+GitHub工具，是否明确将此作为**更新live plugin之前**的真实入口能力缺口，绝不静默降成局部段落替换？
4. **独立质量证据可否判真伪？** G2/G3/G4/G5只在真实完整输出上判质量，不以Skill加载、自审声明、hash或patch PASS；已有Bridge复杂回答、README版本化技术文稿、Phase C中断与长科研解释是否覆盖正确失效模式、同时保持必要深度？发布的独立审阅不伪装成普通GPT每次都有第二Reviewer。
5. **实际执行就绪和恢复：** 原0.5.0 Personal Plugin未变；旧candidate仅历史；新的canonical源、两端分发与安全tar.gz恢复必须同一候选；真实旧账户archive字节materialize/恢复、Web fresh会话/选择插件、G1–G6原批准尝试预算和完整产物验证均不降低。若执行合同仍依赖未经证明的用户入口或需要Codex代选方案，应REVISE而不是“后面再补”。
6. **全包完整性：** 自行对照原0.6全部用户承诺、专业路线权限边界、版本与#13事实、Goal/Runbook/Kickoff以及normal success/terminal failure/恢复链；不能只审上述几点。

本轮只读，不修改仓库/Issue/Project，不启动Codex、不更新Personal Plugin、不建G3分支、不运行真实Gates或付费模型。只允许唯一`DECISION=PASS; READY_FOR_CODEX=YES`或`DECISION=REVISE; READY_FOR_CODEX=NO`。REVISE仅给稳定`CW06-QA-xx`真实阻塞、可验证关闭条件和完整短中文Planner返修提示词；PASS准确绑定用户提供的exact PACKAGE_COMMIT且按当前Critic合同给简短可复制Codex授权交接，不把整篇Kickoff贴给用户。PASS不是已实现、已验收或已发布的断言。