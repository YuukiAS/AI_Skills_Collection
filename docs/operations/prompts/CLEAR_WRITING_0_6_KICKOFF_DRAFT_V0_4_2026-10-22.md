# Clear Writing 0.6 原任务实施交接草案 v0.4

待原独立Critic审核；本文件不构成当前执行授权。实际用户入口由Critic批准后按最新角色合同生成简短中文交接；不得把整份草案和审查元数据倒给用户。

```text
repo = YuukiAS/AI_Skills_Collection
branch = design/clear-writing--single-entry-artifact-finalization
task = clear-writing--single-entry-artifact-finalization
tracking = #13
```

批准后按同一提交的PRODUCT_AND_EXECUTION_PLAN v0.4、UNIFIED_DELIVERY_GOAL v0.4、GATE_RUNBOOK v0.4执行，使用workflow-core + ai-skills-core + writing-style。继续原Codex任务和既有可用实施审查路径，不新开任务/分支，不假设后台路径自动可用。

当前有两类实质工作：在现有canonical专业路线中落实读者内容选择、理解组织、全文审校与最终候选绑定，并让ChatGPT单入口和Codex六直接入口共享；修复prepare-restore的安全ZIP/tar.gz兼容，与上述改变形成同一个新候选。保留原专业保真、重写helper、英文学术与UI边界；不扩成全领域判断器。

task-owned源码、文档、生成物、测试与证据可按批准范围提交和普通非force发布。不得修改Project setting、Planner/Critic合同、Bridge/Slurm/CAT-TRACE实现或研究事实；不新增MCP/App/额外模型/后台服务/数据库。不得覆盖其它分支或无关并行修改。

先完成源文/生成/安全归档、已有开发回归、必需CI与独立实施审查，再冻结候选。真实个人插件更新仍须Phase C-A备份、恢复和实际文件工具可执行，以及Phase C-B新鲜Web入口具备；同范围授权不重复索要，但平台审批不能绕过。原0.5.0在前置具备前保持。按Runbook同一候选完成G1–G5后停，交原Critic进行最终评估前检查；不得自行选择G6。

失败优先在同任务、冻结语义内修复；若改变主张、权限、职责、验收标准或恢复意义，停并回Planner。正式测试产品失败不reroll，live后终止性失败走已冻结forward restore。完整验收、用户必要确认与release closure前，不称0.6已发布或普遍可靠。
