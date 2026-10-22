# Clear Writing 0.6：普通GPT审校可执行性与GitHub终稿质量独立审查 v0.8

继续担任原 Clear Writing 0.6 任务的**独立 Critic**，针对新增用户反馈复核同一未发布版本的完整设计和执行方案。用户的唯一正式目标是：显式选择Clear Writing后，GPT正常回答有读者价值；需要更新/创建GitHub文件时，真实最终文件完成全篇可读性、保真与写入身份检查。不要新建任务或版本，也不要以不可强制自动生成外部Reviewer为由放弃GPT版本。

## 精确对象

```text
repo = YuukiAS/AI_Skills_Collection
branch = design/clear-writing--single-entry-artifact-finalization
task = clear-writing--single-entry-artifact-finalization
tracking = #13
review_stage = COMPLETE_EXECUTION_READY_REVIEW_V0_4_QUALITY_STAGES
previous_package = f0bac70bc51d1a81cd3114e05cfbd29f7a1054cc
historical_candidate = 079bd7987bb33d624d244feb415327d5cf2343d8
```

新的准确`PACKAGE_COMMIT`由用户本轮同时发送，必须从同一exact commit完整读取：

1. `docs/design/clear-writing/CLEAR_WRITING_0_6_PRODUCT_AND_EXECUTION_PLAN_V0_4_2026-10-22.md`
2. `docs/goals/CLEAR_WRITING_0_6_UNIFIED_DELIVERY_GOAL_V0_4_2026-10-22.md`
3. `docs/design/clear-writing/CLEAR_WRITING_0_6_GATE_RUNBOOK_V0_4_2026-10-22.md`
4. `docs/operations/prompts/CLEAR_WRITING_0_6_KICKOFF_DRAFT_V0_4_2026-10-22.md`
5. `results/clear-writing--single-entry-artifact-finalization/PLANNER_CURRENT_PACKAGE_20261022.json`
6. 本审查提示词 `CLEAR_WRITING_0_6_UNIFIED_CRITIC_PROMPT_V0_8_2026-10-22.md`。

先依最新main实际读取AGENTS、Planner/Critic两份角色合同、Capability Gate Policy、AI Skills维护看板、writing-style TODO及六条canonical职责。读已批准v0.2机械合同和此前v0.4原独立审查提示词，不接受旧PASS自动覆盖。

## 本轮必须明确审的关键风险

**A. 所谓“独立审查者”在普通GPT中是否被伪造。** 按当前OpenAI插件Skills官方规范，Skill仅给出模型执行流程，不内置独立模型调用；没有用户授权的MCP/App/新模型/后台服务，本版本日常用户调用不能承诺“每篇自动由第二独立Reviewer审过”。必须确认Plan明确：
- 普通GPT同模型分阶段：确定对象/源与目标→完整候选→单独对照源文查保真→单独作为读者全文通读→必要返修并重新通读→写入→真实全文回读；
- “通读”和“事实核对”是编辑操作，不能用加载记录、散文片段或“review PASS”文字替代；
- 正式G2/G3/G4/G5/G6与原独立Critic才对正常使用完整产物提供**实际独立**质量判断；
- 日常不额外让用户运行另一个审稿对话，也不借此把GPT外部文档支持降级或推迟。

**B. 具体过去失败的正确归因。** 当前0.5.0正式插件有六个同层Skill，无单独总交付入口。Bridge/Phase C真实失败中，`response-clarity`即使实际读到，内部审计证据仍可能构成整篇正文；这是内容选择、理解顺序与完整答复消费不正确，不是只缺少“少用英文”的条款。此前用户指出过README、版本化中文技术文档在实际写入/修改中出现非必要英文和生硬结构；这些是正式文件产物风险。**不能把Bridge聊天失败本身冒充对某一个GitHub文档的实际写入失败**。独立检查当前方案是否同时修复：ChatGPT/Codex共享的普通回答前置内容组织，以及GitHub文件单独选长文路线、写前完整候选可读性、写入后相同文稿回读。

**C. 质量闭环是否真正具备失败含义。** GPT普通调用中发现不自然/错引事实时，能否在写入前做实际全文返修？源缺失/复杂长文支持能力不可用时是否停止不写而不造低配简化文稿？已经写入但回读后质量仍失败，是否有同任务授权范围内的带版本安全返修或准确未终稿状态？模型自审不可冒充独立评审，独立Gate只看最终完整问题/源/实际输出并能判严重退化FAIL，不能以hash或“模型已自查”蒙混。

**D. 不退化与正常入口。** 不新增独立服务/MCP/App/第二模型/强制Hook，保留六专业路线、长篇结构重写和公式、GitHub既有文件更新及非覆盖创建、双交付、精确机器字符串、Codex同源、G1–G6、一次产品答案/仅无模型输出的基础设施重试、唯一fresh G6、0.5→0.6版本、原Phase C真实tar.gz备份和恢复/网页执行边界。留意G3机械约束与真实工具schema，确保不把关键可执行问题拖到安装时。

## 结论与下一入口

审查必须覆盖整个v0.4 Proposal/Goal/Kickoff/Runbook、成功/关键失败/恢复链，不仅只给当前两个问题的意见。本轮不实施、不更新个人插件、不建G3 branch、不跑付费Web模型或正式Gate。若全部闭合，只能给
`DECISION=PASS`
及`READY_FOR_CODEX=YES`，准确绑定用户给出的PACKAGE_COMMIT并按最新角色合同给短中文Codex交接供用户发送。若存在真正阻塞，给`DECISION=REVISE`、`READY_FOR_CODEX=NO`、稳定`CW06-U4-xx` findings和一份可复制的同任务Planner最小返修提示词。不要求用户手工拼装资料。