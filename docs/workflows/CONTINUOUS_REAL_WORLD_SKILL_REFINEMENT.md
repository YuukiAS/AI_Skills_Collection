# Continuous Real-World Skill Refinement

本文件定义 `AI_Skills_Collection` 的长期维护方式。核心目标是：真实项目一边正常使用 plugin，一边把 plugin 真正暴露出来的问题记回来；中央 Planner 再负责去重、提炼和决定是否值得修改 plugin。

核心原则：**项目自己的问题留在项目 repo；plugin 自己的问题直接进入 AI_Skills_Collection 对应 plugin TODO；项目 thread 记录真实失败，中央 Planner 负责提炼。**

## 1. Source of truth 优先级

长期维护时按以下优先级读取：

1. 当前用户反馈与真实 artifact/render/result；
2. 根 `TODO.md` 和目标 `docs/plugin-todos/<plugin>.md`；
3. 当前 active skill / shared runtime / profile / tests / CI；
4. 其他真实项目留下的同类 plugin 证据；
5. synthetic regression / benchmark。

旧聊天、旧计划和旧 benchmark PASS 不能替代当前真实输出。

## 2. 每个中央 plugin 只有一个长期 TODO

十个中央 Marketplace plugin 的长期 TODO 都在：

```text
docs/plugin-todos/
```

根 `TODO.md` 只负责导航，不复制具体条目。

### 2.1 什么应该写进项目 repo

项目 repo 只保存项目本身的事情，例如：

- 科学问题和研究方向；
- 模型、数据、实验、论文内容；
- 项目自己的代码 bug；
- 项目自己的产品/业务决定；
- 与 plugin 无关的长期 TODO。

### 2.2 什么应该直接写进 plugin TODO

如果问题是在**使用某个 AI_Skills plugin 时暴露出来的 plugin 行为问题**，直接写回对应 plugin TODO，不需要先在项目 repo 建一份中转记录。

例如：

- `presentations`：布局、返修范围、公式/图/diagram 可读性、existing-deck routing、错误 fallback；
- `research-writing`：报告结构、日志化语言、claim/evidence 组织；
- `statistical-modeling`：通用统计 workflow、诊断、分析 routing；
- `medical-imaging`：通用影像 workflow、数据格式、任务 routing。

一个简单判断：

> 换成另一个真实项目，plugin 仍然可能犯同样的错吗？

如果大概率会，优先按 plugin 问题处理。

## 3. 真实项目 thread 如何直接记录一条 plugin 问题

当用户要求“记录 repo”“保存到合适的地方”或明确要求沉淀经验时，真实项目 thread 应：

1. 找到并读取当前 `AI_Skills_Collection/main`；
2. 读取根 `TODO.md`；
3. 读取 `docs/plugin-todos/<target-plugin>.md`；
4. 检查是否已经有明显相同的问题；
5. 若没有可直接合并的条目，新增一个 `status: NEW` 的真实使用反馈。

项目 thread 写入时只需要最小字段：

```text
### <简短的问题标题>
status: NEW
source: <真实项目 / 当前任务>
evidence: <实际输出的路径、链接、commit 或 render>
problem: <用户实际看到的问题>
project-specific context: <哪些细节只属于当前项目，不应变成通用规则>
```

这一步只保存事实。

项目 thread **不负责**决定 `CANDIDATE_GENERIC / PROMOTE_NOW`，也不需要填写 `target layer`、`candidate action`、`promotion gate`。

如果 AI_Skills_Collection 当前不可访问或不可写，不要在项目 repo 建影子 plugin TODO；明确报告中央 TODO 尚未记录，待恢复中央 repo 访问后补记。

## 4. AI_Skills Planner / maintainer 如何整理

Planner 处理 `NEW` 条目前必须检查：

1. 当前 plugin 是否已经有同类 active rule；
2. plugin TODO 是否已经有同一问题；
3. 其他真实项目是否出现过类似失败；
4. 当前条目中哪些只是项目自己的内容。

只允许以下处理：

- **已有 active rule，但真实输出仍失败**：按 production regression 处理，补充真实证据并检查实际 consumer/runtime；不要再造同义规则。
- **已有 TODO**：合并新的真实案例，不复制条目。
- **PROJECT_LOCAL**：只是当前项目特殊情况，不升级成通用规则；必要时从活跃区清理。
- **CANDIDATE_GENERIC**：新的跨项目候选，由 Planner 抽象成最小通用问题并写清适用边界。
- **PROMOTE_NOW**：只有满足 promotion gate 才允许进入 bounded implementation。
- **SUPERSEDED / REJECTED**：已有更强规则覆盖或方向不成立。

跨多个 plugin 的问题只指定一个 owner plugin，其他 TODO 只做短引用。

**Executor 可以提供原因分析，但不拥有 genericity / promotion 的最终决定。**

## 5. Feedback lifecycle

中央 TODO 允许以下维护状态：

- `NEW`：真实项目刚写回来的原始 plugin 问题，尚未由 Planner 整理；
- `PROJECT_LOCAL`：经判断只是当前项目特殊情况；
- `CANDIDATE_GENERIC`：可能跨项目复用，但证据还不够；
- `PROMOTE_NOW`：证据足够，可以开有限范围的正式修改；
- `PROMOTED`：已经进入 active plugin 并有回归；
- `BLOCKED_NEEDS_EVIDENCE`：方向合理，但还缺真实证据；
- `REJECTED`：不应进入中央能力；
- `SUPERSEDED`：被更强规则覆盖。

这些只是 TODO 标签，不是第二套 workflow state machine。

## 6. Promotion gate

只有满足以下至少一条，才可以把问题从 TODO 推进到正式 plugin 修改：

1. 在两个独立真实项目中重复出现；或
2. 单次出现但属于严重 production failure，例如科学事实错误、真实图片/公式不可读、对象遮挡、错误路由、source fidelity 破坏、低质量 fallback 冒充完成；或
3. 用户明确确认这是长期跨项目偏好，并且边界和回归都能写清楚。

Promotion 前必须明确：

- 真实失败是什么；
- 来自哪个真实项目/artifact；
- 改动应该落在哪个已有层；
- 哪些相邻情况不适用；
- 如何 replay 原失败并做 unrelated regression；
- 普通用户最终会看到什么改善。

## 7. 不要把一个真实页面问题直接写成永久规则

例如 TRACE 某页出现“两栏高度不一致”。真实项目 thread 只需把这个问题直接写进 `presentations` TODO，状态先是 `NEW`。

中央 Planner 再判断：

- 是不是只有 peer-level comparison 才需要处理；
- 当前 Presentation 是否已经有类似规则但执行失败；
- 是否需要 renderer primitive；
- 是否只是这一页特殊；
- 是否已有别的真实项目出现同类问题。

中央 plugin 只吸收经过抽象后的最小通用能力。

## 8. 六个稳定层

正式修改必须落在已有层之一：

1. Routing / product contract；
2. Scientific reasoning / narrative；
3. Composition / rendering；
4. QA / regression；
5. Writing style；
6. Repository / distribution。

如果现有层能解决，就不要为了一个 TODO 新建顶级 skill/schema/state。

## 9. Reviewed Handoff 的长期角色

长期循环：

```text
真实项目使用 plugin
-> 用户看到真实问题
-> 项目 thread 直接把问题写进对应 plugin TODO（status: NEW）
-> AI_Skills Planner 去重、提炼、判断状态
-> 只冻结 PROMOTE_NOW 的有限批次
-> Codex implementation
-> replay 原失败案例
-> unrelated regression
-> independent review
-> 关闭 watcher
```

不要因为一个 synthetic task PASS 自动生成无限验证链。

## 10. Replay 与 generalization 分开

已经暴露问题的真实项目可以继续用来证明“已知失败修好了”，但不能再冒充 unseen/generalization。

如果以后需要做 generalization acceptance，再单独冻结新的真实 batch。不要让 benchmark 取代日常真实项目反馈。

## 11. Version 与 capability status 分开

长期版本规则见：

```text
docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md
```

核心边界：

- repository / CLI 使用标准三段 release version；
- 每个中央 plugin 使用独立两段 release version，例如 `0.1 -> 0.2 -> 0.3 -> 1.0`；
- plugin version 不跟 repository 锁步；
- capability status 只是可选说明；
- TODO 增加本身不触发 version bump。

普通真实 refinement 通常形成 repository patch release。只有整个 collection 获得此前没有的 repository-level user capability，才考虑 repository minor。

## 12. 当前 Presentation / Reporting 路线

### Presentation

5.0.0 之后，用已安装的 `presentations` plugin 继续返修现有 CAT-TRACE deck。

如果返修中出现 plugin 问题，直接写入：

```text
docs/plugin-todos/presentations.md
```

不要把“Presentation 插件的问题”继续堆进 TRACE 的科研 TODO。

### Reporting

下一份真实 advisor/group-meeting report 如果暴露 `research-writing` 的问题，直接写入：

```text
docs/plugin-todos/research-writing.md
```

项目自身的科学结论和实验下一步仍留在项目 repo。
