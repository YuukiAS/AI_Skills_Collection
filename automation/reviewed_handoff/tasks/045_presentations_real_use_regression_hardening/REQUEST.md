# Reviewed Handoff Request — 045_presentations_real_use_regression_hardening

## Objective

在继续 CAT-TRACE v5 之前，用 CAT-TRACE v4 这次真实返修作为**已知 replay**，审查并按需加固当前 `presentations` plugin 的 existing-deck revision 生产路径。目标不是把 CAT-TRACE 的页码、模型、术语或审美偏好硬编码进 plugin，而是解决一个已经跨多轮重复的事实：当前 active presentation rules 明明已经写了 first-use、diagram、render QA、accepted-element regression、figure readability 等要求，真实 Codex 返修仍能产出明显违反这些规则的最终 PDF。

本任务必须先判断问题究竟属于：

1. plugin 本身缺能力；
2. existing-deck revision 没有真正走 production/QA 路径，只是“读过 skill 文档”；
3. `presentations` 与 `writing-style/scientific-prose` 的交接没有成为完成门槛；
4. 规则已经存在，但当前 reviewer / renderer / validator 没有把真实失败挡住。

只有证据支持时才修改 plugin。不要为了这一个 deck 批量重写所有 presentation 规则。

## Real evidence

- 真实项目：`YuukiAS/TRACE`
- 已知 replay baseline：CAT-TRACE group-meeting deck v4，TRACE commit `e36cb5d93fc882ce158d88ac9201fe494b98b69a`
- v4 PDF/source 只从本机 TRACE checkout 读取；不要把未公开 CAT-TRACE 正文、完整 PDF 或项目专属内容复制到公开 `AI_Skills_Collection`
- 中央真实反馈已写入：
  - `docs/plugin-todos/presentations.md`
  - `docs/plugin-todos/writing-style.md`

重复失败包括：

- 已有 first-use / narrative-order rule，但新方法名和领域术语仍提前出现；
- diagram 仍出现窄 node、难看的断行、短箭头、connector endpoint / clearance 不一致；
- 页面一侧拥挤、核心对象很小，同时另一部分保留大量空白；
- figure object 存在且不 overflow，但图内 axis/legend/panel/caption 在投影尺度仍不可读；
- source/footer 与正文安全区不稳定；
- presentation task 读取了 `scientific-prose`，最终仍出现反复模板化、机器式英文 slide microcopy；
- 当前复杂模型拆成多页后，听众仍难以重建完整模型，但这一点是否应成为通用 plugin 能力需要 Planner 单独判断。

## User intent and long-term process

用户不希望以后“每修一版 PPT 就先大修一次 plugin”。正确长期流程应是：真实项目继续正常使用 plugin 并把真实失败写回中央 TODO；只有满足 promotion gate 的系统性/重复/严重问题，才暂停项目一轮做 bounded plugin refinement，再回到真实 deck。

本轮用户明确同意：如果当前 v4 暴露的问题达到这个门槛，可以先修 presentation plugin，再做 v5。

## Constraints

- 目标 owner plugin 是 `presentations`；`writing-style` 是相邻能力，不要让 writing-style 接管 layout、scientific structure 或 rendering。
- 不新建顶级 plugin、skill、workflow state machine 或大型 schema family。
- 不把 CAT-TRACE 的页码、theorem 名称、模型组件、数据集或特定英语句子写成通用 selector / hard-code。
- 已知 CAT-TRACE v4 只能证明 known failure 被修复，不能称作 unseen generalization。
- 必须有至少一个与 CAT-TRACE 无关的现有 presentation regression / fixture，证明改动没有把其他 research deck 过度限制。
- `scientific-prose` 先做 baseline-first：如果当前 skill 已经能自然改好 representative English slide prose，则只修 `presentations` 的 routing/completion gate；只有当前 `scientific-prose` 本身真实失败时，才允许把 writing-style 相关问题升级到另一个 bounded task。
- 不在本任务生成 CAT-TRACE v5；本任务通过后，用户再回 TRACE 做下一版。

## Expected outcome

用户回来时应该得到一个清楚结论：

1. v4 的重复失败主要是 plugin 缺能力、consumer 没真正调用 production path，还是两者都有；
2. 哪几项中央 TODO 被本任务真正修进 active `presentations`；
3. 哪些条目继续留作 `CANDIDATE_GENERIC / BLOCKED_NEEDS_EVIDENCE / PROJECT_LOCAL`；
4. 以后 existing-deck revision 应如何实际调用 plugin，而不是只“读取规则”；
5. v5 可以在什么稳定基线上继续。
