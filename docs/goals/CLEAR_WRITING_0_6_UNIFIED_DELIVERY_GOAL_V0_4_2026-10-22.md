# Clear Writing 0.6 通用表达与最终交付 Goal v0.4

任务仍为 `clear-writing--single-entry-artifact-finalization`，仓库 `YuukiAS/AI_Skills_Collection`，原design分支，tracking: #13。待独立Critic批准；本文件不是启动指令。

## 用户实际得到什么

显式选用Clear Writing后，ChatGPT与Codex的普通解释、比较、建议、科研/工程说明和执行结果，应按当前问题选择必要内容并建立可理解的关系；文档、界面文字和精确机器内容按各自路线处理。输出不是统一短答或统一长报告。详细要求应有详细的推导、条件和复现信息，简短问题不自动扩成审计报告。

同一请求里的聊天与GitHub文件分别处理。文件必须有完整源文或授权依据，形成真正的完整候选，分别完成内容保真和读者质量审查；实际写入和回读的必须是同一个候选。只让聊天清楚、只写入成功或只hash一致均不算双交付完成。

## 实施范围

以同包 `docs/design/clear-writing/CLEAR_WRITING_0_6_PRODUCT_AND_EXECUTION_PLAN_V0_4_2026-10-22.md` 为唯一新产品/实施authority；同包Gate手册固定验收与继承的机械合同。

普通聊天内容选择与解释组织修入唯一canonical `response-clarity`，不是留在ChatGPT包装专属副本；最终候选保真和交付绑定修入 `writing-fidelity` 及 `references/final-delivery.md`。正式长文继续使用 `scientific-rewrite` 与 `chinese-prose`，英文科研/UI原职责保留。ChatGPT只暴露一个入口，Codex六条直接入口不丢失。

生成两端分发、修复真实旧归档的安全ZIP/tar.gz兼容，形成一个新的最终候选。旧 `079bd7987bb33d624d244feb415327d5cf2343d8` 只作历史基线；不能把旧PASS拼到新语义上。

## 不做什么

不修改角色合同、AI Research Stack项目设置、Bridge/Slurm/CAT-TRACE事实和实现，不新增服务、模型、MCP/App、数据库、状态机或第七个技能。不替领域负责人决定科学正确性、发布批准、下一执行角色或用户授权。用户认可的示例不是每个任务的固定格式。

## 完成依据与失败处理

同一个最终候选真实通过G1–G6，Web正常入口与Codex既有直接入口均有实质输出，独立审阅完整问题、来源、聊天与最终文件。G1–G5通过后停止，由原Critic冻结唯一fresh G6。权限、尝试预算、source/generated parity、GitHub修改/新建、恢复规则按同包手册执行，不无限重试。

正式个人插件在真实备份、恢复档案和网页执行入口具备前仍为0.5.0。终止性失败按原恢复路径处理，普通实现错误留同一Codex任务，改变冻结语义才返回Planner/Critic。

发布只将writing-style从0.5推进一次到0.6，个人包装0.6.0，仓库PATCH后绑定，其他插件不因本任务独立升版。检查README和changelog，保留Issue #13下游未完事实。全部正式验收前不得宣称“基本可靠已证明”或“发布完成”。
