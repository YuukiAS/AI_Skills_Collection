# 以后可以怎样整理原有记录

这些动作留待对应维护任务处理。先核对真实问题、实际 owner 和现有验收，再动源码入口、Issue 或 Project。

| 位置 | 候选动作 | 执行前要查 |
| --- | --- | --- |
| [Reasoned Decision TODO](../../plugin-todos/reasoned-decision.md) 与 [历史 Skill TODO](../../skill-todos/reasoned-decision.md) | 保留插件入口与冻结设计定位。将原生入口、跨语言调查和 UU 补证作为同一问题族下的不同反例。历史 seed 保留人工接受样本，引用新入口。 | 独立 Critic 核对原生能力、用户目标、可逆探查和安全停手。正式纳入 tracking 时确认无重复 Issue。 |
| [Clear Writing TODO](../../plugin-todos/writing-style.md) 与 [#13](https://github.com/YuukiAS/AI_Skills_Collection/issues/13) | 按直接作答、解释顺序、纠偏重答、跨源长文和下游消费归并反馈。#13 更新执行锚点时保留同候选、未运行账号/Web 条件和下游适配。 | 重读 Phase C。#49、#73 的消费者适配分别取证，不能随 0.6 候选默认关闭。 |
| [workflow-core TODO](../../plugin-todos/workflow-core.md) 的 Asteria 条目 | Design Assurance 有正式 owner 和 Proposal 后，在新入口收敛“关键变化与落实点”。Workflow Core 保留执行、权限和恢复要求，引用设计准备证据。 | 核对缺少关键约束时是否还会启动执行。Asteria 的具体产品选择留项目。 |
| [#107](https://github.com/YuukiAS/AI_Skills_Collection/issues/107) 的 Delivery Assurance 执行锚点 | 将旧 v0.4 材料作为历史审查证据，后续核实 Toolkit R3/P0 设计、实施前审查包、消费结果和下一动作，再更新 Issue。 | R3 的 `PROCEED` 来自可读转交记录，原始 Critic 文本尚待核。P0 以及消费者实际成功另验。 |
| [Presentations TODO](../../plugin-todos/presentations.md)、[制作](../../plugin-todos/presentations-authoring-production-workflow.md) 与[历史锁](../../plugin-todos/presentations-core-history-lock.md) | 教学模板、视觉审查、冻结返修、文件交付各保留一处维护入口，原条目作为实际失败的引用。#98 保留共享模板协议。 | 区分 0.5 提案和 0.4 真实消费。错绑编号逐条核实，避免按重复数字批量转移。 |
| [Research Authoring TODO](../../plugin-todos/research-writing.md)、[课程 Skill TODO](../../skill-todos/course-assessment-authoring.md) 与 [#99](https://github.com/YuukiAS/AI_Skills_Collection/issues/99) | #99 的公开锚点同步到当前 pre-live 候选与独立审查。课程领域文档收束到一处 runbook 和正反回归，保留信息准入、语义分页和受保护层证据。 | 继续 #99 的冻结流程。学习笔记、课程专门能力与当前科研发布分开验收。 |
| [Artifact Content Design](../../skill-todos/artifact-content-design.md)、[Frontend Design](../../plugin-todos/web-development.md)、[Scientific Visualization](../../plugin-todos/scientific-visualization.md) | 内容准入作为共享候选，项目 UI、课程文档和专家图分别保留领域决定。科学图语义回归归图，原生交互归 Frontend Design。 | 要有真实首稿和现场证据，先查 #89 和 #90 是否缺真正消费。 |
| [PDF renderer](../../skill-todos/render-chinese-math-pdf.md)、[PIE](../../skill-todos/project-instructions-editor.md)、[Slurm](../../skill-todos/slurm-workflows.md) | 压缩已发布项目的历史叙述，保留原 release、兼容和安全回归。PDF 保留 #83 部分覆盖与上游自动交接，PIE 保留 #108 和独立的 locator 候选。 | 核实 exact release 与关闭范围。Slurm 仍需保留 live retain `NOT_RUN` 和豁免。 |
| [根 TODO](../../../TODO.md) 与 [插件 TODO 目录说明](../../plugin-todos/README.md) | 有稳定 owner 后补 Design Assurance、Delivery Assurance 的入口。Reasoned Decision 历史 Skill 保留清楚的迁移指向。 | 目录做导航。根 README 如需改，按仓库规则调用实际安装的 Clear Writing。 |

## 优先核对的 Issue 编号

同一个 `tracking: #N` 可覆盖同一主题的多个案例。扫描到 93 个不同源码编号，在公开 Issue 中均可解析。以下有明显语义不符，处理前还需核对 Issue 的完整 scope。

| Issue | 公开问题主题 | 候选整理 |
| --- | --- | --- |
| [#29](https://github.com/YuukiAS/AI_Skills_Collection/issues/29) | CAT-TRACE v13/v14 演示反馈 | Research Writing 的 PDF 首交段落可引用 #101 的已有发布，自动适配仍需验证。 |
| [#49](https://github.com/YuukiAS/AI_Skills_Collection/issues/49)、[#50](https://github.com/YuukiAS/AI_Skills_Collection/issues/50)、[#51](https://github.com/YuukiAS/AI_Skills_Collection/issues/51) | 科研图文案交接、科学示意图真实渲染、可视化课程驱动能力 | Presentations 同号条目分别涉及教学模板、讲者学习和讲次引用。模板优先比对 #98，其他按独立承诺复用或留证。 |
| [#53–59 的入口](https://github.com/YuukiAS/AI_Skills_Collection/issues/53)、[#63–65 的入口](https://github.com/YuukiAS/AI_Skills_Collection/issues/63) | 前端原生、动效、组件、Figma 和界面语义 | Presentations 同号条目涉及教学结尾、视觉评审、审查者能力等。核对现有演示 Issue 和完整产物审查归属，前端关闭记录只证明其自身。 |
| [#73](https://github.com/YuukiAS/AI_Skills_Collection/issues/73)、[#74](https://github.com/YuukiAS/AI_Skills_Collection/issues/74) | 统计语义交接、先验预测课程试点 | Presentations 同号的首次文件交付、Beamer 导航留原 owner。首次交付可引用 #101，演示包实际消费仍需验证。 |

下次获准同步时，先更新执行锚点和可见证据。Project 生命周期依据真实进度、完整消费者证据与 Issue closure。本轮研究没有进入执行或适配，故没有需要执行的 Project 状态变更。
