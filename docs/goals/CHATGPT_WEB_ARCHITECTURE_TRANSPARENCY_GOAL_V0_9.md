# Planner–Critic 1.8 的目标草案 v0.9：不用用户重复提醒的架构透明决策

任务：`chatgpt-web--pass-integrity`。日期：2026-10-22。
状态：待设计阶段 Critic 独立审查，非 implementation authority。
同版 Proposal：`docs/workflows/CHATGPT_WEB_ARCHITECTURE_TRANSPARENCY_PROPOSAL_V0_9_2026-10-22.md`。
同版 Plan：`docs/workflows/CHATGPT_WEB_ARCHITECTURE_TRANSPARENCY_PLAN_V0_9_2026-10-22.md`。
所有审查必须绑定调用方给出的同一准确 PACKAGE_COMMIT。

## 用户真正得到的长期能力

以后在 AI Research Stack Project 设计、返修和审查插件、Skills、Profiles 和 Bridge Kit 时，用户无需一轮一轮额外提醒“说人话、说明用哪个 Hook/Wrapper/MCP、讲真实因果例子”。新线程依据已有 Project setting 自行读取最新正式 Planner/Critic 角色合同；合同规定每个重要设计必须在技术方案同版准备、返修、独立审查一份用户真正可理解、可用于赞同/否决技术路线的机制说明。

说明内容选择以决策价值为原则，而非机械减少英文或隐藏技术名称。重要技术选择、真实动作链、安全和恢复边界、替代取舍、用户实际用法必须说清；路径、运行日志、提交标识与机器回执放入 repo 和直接可复制交接。

## 一次返修必须发生什么

`Critic REVISE` 后，Planner 从当前用户承诺和 review 出发修订完整技术 Proposal。如果改变了机制、真实执行者、正常入口、保证或恢复，则同一版本的用户说明也更新，并讲清旧技术为什么退出、新技术如何解决问题、用户发生什么变化。接下来发给 Critic 的 prompt 仅包含真实任务/版本定位，不再重新教它怎么讲技术；Critic 自行消费最新正式合同，独立审本轮技术和说明是否一致。

如果 Critic 发现新说明隐藏 Wrapper/Hook 选择、夸大安全保证、跟不上技术变更或无法说明真实执行路径，应拒绝最终 `PASS`。不能靠“字段存在、文字流畅、测试通过、Skill调用过”当作读者质量保证。

## 最终批准要交付什么

唯一 execution-ready `PASS` 必须：
- 审完整同版 Proposal/Plan/Goal/Kickoff 和正式用户承诺；
- 将已经实际审查过的机制说明的关键完整内容交给用户，并提供自己独立的判定、此前阻塞的实质关闭、限制和唯一下一动作；
- 另给准确批准定位、`READY_FOR_CODEX=YES` 和短 `COPY TO CODEX`；
- 不把被审的机制说明临场替换为审计流水或可复制 Kickoff 全文。

设计阶段仅 `PROCEED/REVISE`，未获最终批准与用户执行授权不启动 Codex；不能把候选合同存在当作正式已生效。

## 原 1.8 关键能力保留

任务 prompt 与中央合同的兼容性、关键外部接口的现实证据与条件性验证、非终态唯一交接、PASS 后解释/新证据/新增要求分类、候选同一身份与真实正常入口验证、实现后 Critic 安全门、正式 main 合入和远端回读。没有第三个人工角色、数据库、服务、浏览器网关或付费验证。

## 必须验证两种不同事实

**候选阶段真实连续返修：** 单次初始候选合同绑定后，至少一轮真实 `REVISE → Planner更新说明 → Critic 复核` 不能再由用户补发输出规则。核完整用户可见文本与技术真实身份，不靠关键词。允许真实结果保持 REVISE，不强迫 PASS。

**main 生效后的普通新任务：** 候选经批准、实施、验收、正式集成并远端回读后，在提前冻结的真实新插件/Bridge 设计或审查中只用普通请求，检查新线程是否自行读取最新 1.8 合同并持续解释机制。未经这类证据，最多声明“合同已正式安装”，不得宣称“以后无需用户提醒的能力已经验证”。

## 不做什么

本轮不修改当前正式 main、Project setting、Capability Gate Policy、Clear Writing 产品、Bridge、Slurm、Mica、Plugin Creator；不做生产动作、危险命令、付费调用或其他高影响授权。不新增并行治理系统、不用固定文风模板取代专业技术判断。

Claim ceiling：ChatGPT Web 的角色合同和独立审查仍不是浏览器级不可绕过发送前 Hook；本版追求的是普通入口持续实际执行、跨轮文本/设计身份相符、真实失败被独立查出，而不是凭文档宣称百分百不会违反。
