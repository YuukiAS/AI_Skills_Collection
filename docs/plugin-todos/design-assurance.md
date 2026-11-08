# Design Assurance — Plugin TODO

> 计划中的独立插件，尚未生产实现。它负责把一个复杂系统一次设计到位，再交给执行者机械实现。生命周期位置见 `docs/design/reasoned-decision/REASONED_DECISION_V0_1_ARCHITECTURE_2026-11-05.md`：Reasoned Decision → Design Assurance → Delivery Assurance。

## 2026-11-08：先固定 Grill Me、Design Assurance、Blueprint 三者的位置，再测 Blueprint

status: NEW
source: Asteria Blueprint 与 Design Assurance 先后顺序讨论，2026-11-08
evidence: Asteria Blueprint 已有可运行的设计载体与校验，最新分支 `draft/blueprint-round7-20261107`（私有仓库，只记分支名）；CAT-TRACE 的 Design Assurance 协议原稿 `docs/decisions/2026-11-03_cat_trace_design_assurance_protocol.md`（私有仓库）；本仓库 `docs/plugin-todos/workflow-core.md` 中“关键变化与落实点”一条；`docs/plugin-todos/writing-style.md` 中两条 Design Assurance / Grill Me 讨论记录
problem: 用户的目标是让设计者一次把复杂系统设计完，不能用户一问简单问题就暴露没设计；真正需要用户拍板的事必须提前问清楚。现在有三样东西，各自只解决一部分：
- Grill Me（Matt Pocock 的 `grill-me`，MIT）会逐个决定追问用户，直到没有歧义，但它什么都问，不区分哪些该问用户、哪些设计者自己能查到，问完也不留下可检查的产物。
- Design Assurance 已有一份手写协议（多路独立设计 → 一份权威汇总 → 冷读 → 冻结 → 机械执行），但冻结的方案仍会被执行暴露缺口，而且每一步之后“下一步发给谁”（GPT Pro、Codex 还是用户）都要用户自己判断，很难稳定复现。
- Blueprint 是设计载体和关卡：需求追踪、递归组件、具体设计字段、证据、验收器、失败路径、版本留痕、走查和疑问记录。它能逼设计者填满，但不能保证填对，也不负责问用户。
没有一个地方固定三者的位置，所以 Blueprint 的盲测每一步都要人工编排，结果噪声大。
project-specific context: Asteria Blueprint 的界面、CAT-TRACE 与 Mica 的具体内容都只是这次的真实案例。通用问题是：复杂设计流程需要一个固定的编排者，决定每一步由谁做、交什么、何时能冻结，并把澄清工具和设计载体放在固定位置。

candidate_action:
- 三者位置：
  - Grill Me 是 Design Assurance 开头的按需澄清步骤，不是独立流程。每个问题先分类：只有用户能定的（偏好、范围、成功标准、风险承受）才问用户；查得到的自己查；设计者该定的自己定并写理由。用户的回答直接成为 Blueprint 中带出处的需求。
  - Design Assurance 是编排者，决定每一步交给谁、交什么、满足什么条件进入下一步。
  - Blueprint 是 Design Assurance 的产物和冻结关卡：校验不过、依据缺失、走查讲不清就不能冻结；冻结后的用户疑问和执行停工都记成 Blueprint 的版本改动，并标明“本可想到”还是“跑了才知道”。
- 草拟的步骤与执行者：
  1. 澄清：Grill Me，和用户进行，产出需求清单；
  2. 独立设计：两路 GPT Pro 并行，Codex 只读盘点代码现实；
  3. 汇总：一个 GPT Pro 合成一份 Blueprint；
  4. 关卡：Codex 跑 Blueprint 校验；另一个模型扮演用户逐组件追问，答案不在 Blueprint 里即为缺口；Codex 只拿 Blueprint 冷读，列出开工前仍需问的问题；有缺口回到第 3 步；
  5. 冻结并执行：Codex 实现；执行中需要设计判断时停下（如 `NEEDS_GPT_PLANNER`），回到第 3 步并记一次改口。
- 每一步结束时，Design Assurance 直接告诉用户“下一步把什么发给谁”，并附上 `workflow-core` TODO 中要求的“关键变化与落实点”。
- 衡量标准：冻结后用户还要问几个本可提前想到的问题，执行者停工几次。目标接近零。
- 最小版本可以先不做成完整插件：一份记录当前步骤的状态文件，加每一步现成的提示词，就能实现“下一步发给谁”。用真实项目跑通一次后，再决定插件结构。

promotion_gate:
1. 用 CAT-TRACE 的真实需求与 Codex 停工记录跑通一次完整流程，Blueprint 冻结后的停工与用户追问数量有记录；
2. 用户在每一步都不需要自己判断下一步交给谁；
3. 澄清步骤问用户的问题都属于只有用户能定的类别，不出现设计者自己能查到的问题；
4. 换到非科研项目（如浏览器插件）时，步骤与角色不需要改写。
