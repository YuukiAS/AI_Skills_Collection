# 启动范围草案 v0.8

任务：`chatgpt-web--pass-integrity`。日期：2026-10-22。
DRAFT ONLY。当前阶段为设计审查，不是 execution-ready；不得将本文直接发送 Codex 启动。旧 v0.7 Kickoff 亦不再覆盖本版实质修订。

## 后续执行对象

目标仓库：`YuukiAS/AI_Skills_Collection`。
当前设计分支：`design/chatgpt-web--pass-integrity-v0-4`。
正式 Planner/Critic 目标版本：1.8；当前 main 正式版本仍为 1.7。

后续最终批准必须绑定同一个准确提交中的：
- `docs/workflows/CHATGPT_WEB_ARCHITECTURE_TRANSPARENCY_PROPOSAL_V0_8_2026-10-22.md`
- `docs/workflows/CHATGPT_WEB_ARCHITECTURE_TRANSPARENCY_PLAN_V0_8_2026-10-22.md`
- `docs/goals/CHATGPT_WEB_ARCHITECTURE_TRANSPARENCY_GOAL_V0_8.md`
- 本启动范围草案及对应独立审查结论。

## 将允许的工作

只实施原两份角色合同中的说明准备、独立来源核对、同版说明交付、任务提示词兼容、最终 PASS 一次性交付、接口证据和非终态交接职责；更新对应真实事故与验证记录。不得新增另一位人工 Reviewer 或运行控制系统。

把机制说明放在原 Proposal/Plan 内，Plan/Goal/Kickoff 引用同版内容。最终 Critic 不仅审技术包，也审将给用户阅读的内容，且不得用新的审计摘要替换已核对的说明。

实施后冻结角色文本和验证输入的准确提交；后继证据引用该提交，不形成自引用哈希要求。完成本地检查，交既有实现后 Critic 作安全检查；获准后运行冻结的真实 Web 验证。候选通过后按仓库规则完成集成前检查、普通 main 合入、推送与远端回读。整体默认行为是否成立，继续以真实普通任务观察为准。

## 必须在最终执行就绪批准前核实

设计结论、对应合同修订文字、当前实际工作区与所选分支、允许文件范围、真实 Web 输入与次数、独立检查者的可读证据及返回路径。不得把任何产品/架构/权限/验收决定留给 Codex 启动后自行补齐。

不沿用旧草案中新建正式工作树位于 `/tmp` 的安排；使用符合当前仓库和 Bridge 规则的实际定位，不为治理任务强行启用 Reviewed Handoff 或后台运行。

普通授权后的源码读取和安全环境确认仍可由 Codex 在执行开始时做；这不等于把关键架构前提拖到实施后才决定。

## 授权边界

当前只授权 Planner 写入原设计分支的本轮设计文件，不授权正式合同实施、main 合入、真实验证、产品更新或付费操作。

后续唯一执行就绪 PASS 仍不代替用户授权。用户实际发送批准的短执行入口后，才在该入口明确的范围内执行。原有不重复索权原则保持。

禁止修改项目设置、Capability Gate Policy、Clear Writing 产品、Slurm、Bridge Kit、Mica、Plugin Creator；禁止付费 API、线上插件更新、危险调度器动作、强推、删除无关分支、发布或其他未授权副作用。

## 失败与下一入口

普通实现错误留同一 Codex 任务；核心语义、权限或验证标准必须改变时回原 Planner。当前 Planner 能处理的设计工作继续处理；只能用户完成的界面操作由 Planner 提前准备材料并压缩动作。不得用“需要一个环境”代替责任与交接。

最终可发送给 Codex 的提示词应短，只引用批准包、必要定位、当前授权与停止条件，不全文复制本草案。