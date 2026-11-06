# 接下来做什么

最先推进已经能回答独立审查问题、且反复阻塞真实使用的方向。已进入实现或候选验收的工作继续沿原任务，避免重开架构。

| 优先 | 建议动作 | 为什么现在做 | 到哪里停 |
| --- | --- | --- | --- |
| 1 | **Reasoned Decision v0.1** 送独立 Critic | 近期 Edge、Tailscale、iTerm2、UU 反复出现查找范围太窄、内部限制被当成用户目标、过早推荐或求助。现有设计已收敛，可审新案例是否进入实际行为。 | 用同一设计版本审查原生方案调查、退出/改判、仅证据不足时的可逆调查和授权交接。研究阶段不启动实现。 [工作流](WORKSTREAMS/REASONED_DECISION.md) |
| 2 | **Clear Writing** 沿 #13 继续 Phase C | 近期多次显式纠偏仍失败，跨源综合也多让用户自己做比较。已有候选与实施审查，重写设计会丢掉真实首稿与未完成的正常入口证据。 | 核对 exact candidate 的账号备份/恢复和 Web 入口。近期未入冻结集的案例进入独立回归设计，避免污染原冻结集。领域自动消费另验。 [工作流](WORKSTREAMS/CLEAR_WRITING.md) |
| 3 | **Design Assurance** 起草正式 Proposal | Asteria、课程材料和科研设计都暴露执行包看不出约束如何落实。先解决准备度可审查性，能减少后续设计与实现返工。 | 独立比较一个 UI 和一个非 UI 任务，证明成熟参考、约束、设计差异和负例都进入真实交接。沿现有角色合同审查，不增流程层。 [工作流](WORKSTREAMS/DESIGN_ASSURANCE.md) |
| 4 | **Delivery Assurance** 先审既有 R3 后的 P0 | 交付事故跨产品，已有 056、领域验收与外部设计。先验证具体入口的收益，可以阻止继续叠管理层。 | 保留原 #107 与 Toolkit 边界。实施前审查通过及授权后，验证 Windows 非交互探针，再选 Lucerna 的真实首片和领域验收器，分别核对成功、拦截、恢复和实际用户入口。 [工作流](WORKSTREAMS/DELIVERY_ASSURANCE.md) |
| 5 | **Presentations** 用现有 0.5 设计做正式收敛 | 教学和科研已有可复验失败，模板与锁保护足以划清产品范围。完整候选的渲染/独立 review 是瓶颈。 | 沿远端现有双端设计，把 #98 模板、既有 deck 改页与完整 artifact 审查的证据讲清楚，再由 Critic 裁定。 [工作流](WORKSTREAMS/PRESENTATIONS.md) |

**Research Authoring #99 可并行。** 已有候选和独立 pre-live 判断，接下来取正常入口和发布证据。课程文档的语义分页、冻结内容、渲染与教师保护继续以领域案例研究，学习笔记只做补证。它们不宜并入当前 release 的已冻结验收范围。 [工作流](WORKSTREAMS/RESEARCH_AUTHORING.md)

## 普通修复与补证

- **直接从既有规则复现**。Workflow Core 的可用能力/最小权限误判与真恢复，Frontend Design 的 #89 内容交接和 #97 原生路径，PDF #83 部分字体规则和上游是否调用，均先读正常入口证据。AI Skills Maintainer 继续查真实安装与消费，避免另开机器编排。
- **先拿样本**。统计 #75–78 可选同一真实方案检查四类不同证据。#74 的先验预测、影像 #79/#85、生信 #84、可视化 #51 等在现有插件内小范围取证。PIE #108 可沿已存在的研究准备提案，私有 locator 另查可用性和权威。
- **合并、降级或延后**。历史 Reasoned Decision standalone 只保留证据。Artifact Director / Artifact Content Design 暂为共享研究能力。课程方向先走已有 Research Authoring 领域路由。已覆盖的 Web 和旧 PDF/Slurm 条目回到回归库。缺兼容现场的课程式扩展、跨所有载体的总控和无差别双端入口延后。
- **合并交付复盘中的重复项**。#10 的比对包、领域验收消费和 #101 的首次下载应在同一任务里证明各自的真实对象，避免重复写 owner 或重复开 gate。课程、演示、前端、统计和影像仍保留各自专业验收。

下一轮正式 Proposal 或独立 Critic 使用仓库现有角色合同。对应工作流、候选身份、读者可见结果、正常入口、真实正反样本和保持范围都要明确。冻结门槛应来自承诺与风险。独立研究报告只供审查取舍。 [Planner 合同](../../workflows/PLANNER_ROLE_CONTRACT.md) · [Critic 合同](../../workflows/CRITIC_ROLE_CONTRACT.md) · [能力验收](../../workflows/PLUGIN_CAPABILITY_GATE_POLICY.md)
