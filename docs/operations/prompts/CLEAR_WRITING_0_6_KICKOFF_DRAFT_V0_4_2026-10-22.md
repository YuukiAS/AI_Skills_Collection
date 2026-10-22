# Clear Writing 0.6 原任务实施交接草案 v0.4

待原独立Critic审核；本文件不构成当前执行授权。实际用户入口由Critic批准后按最新角色合同生成简短中文交接；不得把整份草案和审查元数据倒给用户。

```text
repo = YuukiAS/AI_Skills_Collection
branch = design/clear-writing--single-entry-artifact-finalization
task = clear-writing--single-entry-artifact-finalization
tracking = #13
```

批准后按同一提交的PRODUCT_AND_EXECUTION_PLAN v0.4、UNIFIED_DELIVERY_GOAL v0.4、GATE_RUNBOOK v0.4执行，使用workflow-core + ai-skills-core + writing-style。继续原Codex任务和既有可用实施审查路径，不新开任务/分支，不假设后台路径自动可用。

当前实质范围仍只有同一个0.6修复：**(a)** 改善canonical `response-clarity`的真实生成顺序：按当前用户问题筛选读者内容与解释依赖→完整生成→以原问题重新通读并实际返修；`writing-fidelity`集中保真和最终文本身份，正式文档用原专业全篇路线，GPT写前必须将完成后的候选**全文**作为GitHub工具的`content`并回读实际全文；ChatGPT单入口和Codex原六入口消费相同源。**(b)** 修复既有`prepare-restore`对安全ZIP/tar.gz输入的兼容，与上述行为形成同一新候选。不得新增独立模型/服务/审核器或项目角色；日常GPT“再次审阅”是同模型针对真实候选的编辑阶段，正式Gate才有独立审阅。现有 `scientific-rewrite`重写helper与专业保真边界不能因Web能力不足而静默跳过。

task-owned源码、文档、生成物、测试与证据可按批准范围提交和普通非force发布。不得修改Project setting、Planner/Critic合同、Bridge/Slurm/CAT-TRACE实现或研究事实；不新增MCP/App/额外模型/后台服务/数据库。不得覆盖其它分支或无关并行修改。

先完成源文/生成/安全归档、已有开发回归、必需CI与独立实施审查，再冻结候选。**Codex已完成主要写作实现；只为G5回放修正历史模型绑定过度约束，当前`candidate_plugin_replay.py`已可传入显式模型与推理参数；在同一入口按Runbook §7选定当前账户与固定CLI真正支持的型号并验证、冻结，不改`--ignore-user-config`，绝不按旧`gpt-6.1-sol/high`永久强制。必要时仅修同一helper的通用小型参数/可用性探针接口；不准再改writing canonical行为。无产品答案的HTTP 400按基础设施分类，正式G5不得因产品答案不满意而换模型。** Web `GPT-5.6 Sol`、G1–G6、完整输出质量和原预算全部不变。真实个人插件更新仍须Phase C-A备份、恢复和实际文件工具可执行，以及Phase C-B新鲜Web入口具备；同范围授权不重复索要，但平台审批不能绕过。原0.5.0在前置具备前保持。按Runbook同一候选完成G1–G5后停，交原Critic进行最终评估前检查；不得自行选择G6。

失败优先在同任务、冻结语义内修复；若改变主张、权限、职责、验收标准或恢复意义，停并回Planner。正式测试产品失败不reroll，live后终止性失败走已冻结forward restore。完整验收、用户必要确认与release closure前，不称0.6已发布或普遍可靠。
