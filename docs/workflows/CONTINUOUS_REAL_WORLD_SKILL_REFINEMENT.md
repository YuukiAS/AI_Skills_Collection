# Continuous Real-World Skill Refinement

本文件定义 `AI_Skills_Collection` 的长期维护方式。仓库不再以“做完一轮审计/benchmark 即结束”为目标，而是持续从真实科研、写作、Presentation、统计、医学影像、HPC 与工程任务中吸收用户反馈，并把真正可泛化的经验沉淀为稳定能力。

核心原则：**真实任务先于 synthetic benchmark；TODO 是证据入口，不是 active rule；promotion 必须有边界、有回归、有真实 user-facing effect。**

## 1. Source of truth 优先级

长期维护时按以下优先级读取：

1. 当前用户任务、真实项目 repo、真实 artifact/render 与用户反馈；
2. target plugin 的 `docs/plugin-todos/<plugin>.md`；
3. active skill / shared runtime / profile / tests / CI；
4. `docs/provenance/` 中的历史复盘和来源记录；
5. synthetic regression / benchmark。

旧聊天、旧 TODO、旧 benchmark PASS 不能替代当前 production evidence。

## 2. 每个中央 plugin 只有一个长期 TODO 入口

十个中央 Marketplace plugin 的长期 backlog 统一位于：

```text
docs/plugin-todos/
```

每个 plugin 一个文件。这里是 **source-only maintenance inbox**，不进入生成后的 Codex plugin payload，不作为普通用户运行时上下文。

真实项目可以有自己的详细 review / provenance 文档，但跨项目候选最终必须归并到对应 plugin TODO；不要继续在 active skill 目录中新增 `TODO_<PROJECT>_V2/V3/...` 文件。

## 3. Feedback lifecycle

每条真实反馈只能处于以下一种维护状态：

- `NEW`：刚记录，尚未判断是否通用；
- `PROJECT_LOCAL`：只属于当前项目/模板/科学语义，不进入中央 plugin；
- `CANDIDATE_GENERIC`：可能跨项目复用，但还未达到 promotion gate；
- `PROMOTE_NOW`：证据足够，可进入 bounded Reviewed Handoff；
- `PROMOTED`：已进入 active skill/shared runtime/QA/profile，并有 regression；
- `BLOCKED_NEEDS_EVIDENCE`：方向合理，但缺真实 render / 第二项目 / production evidence；
- `REJECTED`：不应进入中央能力；
- `SUPERSEDED`：被更强、更通用的 active rule 覆盖。

这些只是 TODO 标签，不是第二套 workflow state machine。

## 4. Promotion gate

反馈只有满足以下至少一条，才可从 TODO 进入 active plugin：

1. 在两个独立真实项目中重复出现；或
2. 单次出现但属于严重 production failure，例如科学事实错误、证据伪造、真实图片/公式不可读、对象遮挡、错误路由、source fidelity 破坏、低质量 fallback 冒充完成；或
3. 用户明确确认这是长期跨项目偏好，并且 Planner 能给出清楚边界和可观察 regression。

Promotion 时必须同时冻结：

- `problem`：真实失败是什么；
- `evidence`：来自哪个真实项目/artifact；
- `target layer`：routing / scientific reasoning / composition-rendering / QA-regression / writing-style / repository-distribution；
- `boundary`：哪些相邻情况不适用；
- `regression`：以后如何证明没有回归；
- `user effect`：普通用户正常调用后具体变好什么。

缺少其中任一项时，不应直接修改 active rule。

## 5. TODO 不是规则

项目经验不能直接复制进中央插件。

例如某个 TRACE 页面出现“两栏 block 高度不一致”，不能直接写成“所有两栏必须等高”。Planner 需要先判断：

- 是否只是该项目的页面选择；
- 是否是通用 peer-level comparison rule；
- 是否需要 renderer/layout primitive；
- 是否已有规则但 consumer 没执行；
- 是否仅需要 QA；
- 是否与现有规则重复。

中央 plugin 只保留抽象后的最小通用能力；项目科学事实、页码、论文名、数据集名、特定 theorem 名称继续留在项目或 provenance。

## 6. 六个稳定层

任何 promoted change 必须归入现有层之一：

1. **Routing / product contract**：用户自然语言应进入哪个 plugin/skill/profile；
2. **Scientific reasoning / narrative**：如何组织问题、证据、模型、理论、限制和下一步；
3. **Composition / rendering**：layout、figure、table、equation、diagram、medical panel、export；
4. **QA / regression**：真实 render、可读性、source fidelity、anti-fallback、重复失败；
5. **Writing style**：读者语气、去日志化、中文/英文表达、不过度结论；
6. **Repository / distribution**：registry、profile、Marketplace、version、changelog、安装与 generated layer。

如果一个 TODO 无法解释为什么必须创建新 skill/schema/state，而现有层可以承载，就不得新建顶级能力。

## 7. Reviewed Handoff 的长期角色

Reviewed Handoff 保留，但采用 **bounded batch**，不常驻寻找任务：

```text
真实项目使用
-> 用户反馈
-> 写入 plugin TODO / provenance
-> Planner triage
-> 只冻结 PROMOTE_NOW 的有限批次
-> Codex implementation
-> replay 原失败案例
-> unrelated regression
-> independent review
-> 关闭 watcher
```

下一批真实反馈积累后再开启下一轮。不得因为一个 synthetic task PASS 自动生成无限验证链。

Planner 必须保护已经通过的行为，优先修真实 blocker；没有真实 blocker 时结束 batch。

## 8. Replay 与 generalization 分开

已暴露问题的真实项目可以成为 regression/replay case，用于证明已知失败被修复；但如果材料曾用于调参，就不能再被称为 unseen/generalization acceptance。

最终 generalization 如有必要，仍应使用完整预冻结 fresh batch，且 production 在 batch 内冻结。不要让 generalization benchmark 取代真实用户 workflow。

## 9. Version 与 capability status 分开

长期版本规则见：

```text
docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md
```

核心边界：

- repository / CLI 有自己的 release SemVer；
- 每个中央 plugin 有自己的独立 SemVer；
- plugin version 不再跟 repository 锁步；
- capability status 只是可选说明，不是第二套版本。

下一次长期维护架构正式发布为 repository `5.0.0`。这是 repository-level versioning/refinement epoch，不表示所有 plugin 都达到 stable。

已有同名 plugin 不向下重置版本号；`4.4.2` 作为最后 lockstep baseline，5.0.0 起只 bump 真正改变的 plugin。

## 10. 近期真实工作流路线

### Repository 5.0.0 — long-term refinement foundation

目标：

- repository version single source of truth；
- independent plugin SemVer；
- per-plugin TODO + per-plugin changelog；
- root CHANGELOG 作为 release 首页；
- README 可直接看到 plugin version/status/changelog；
- 关闭已知 release/control-plane/production false-blocker；
- 不重启 synthetic Stage-5 challenge。

### 5.0.0 之后 — TRACE Presentation real refinement

5.0.0 Goal 完成后，优先**调用已安装的 `presentations` plugin 继续修改现有 CAT-TRACE deck**，而不是从头重新生成 PPT。

真实循环：

```text
现有 CAT-TRACE deck
-> plugin revision mode
-> 用户逐页/整套验收
-> 新问题写入 presentations TODO / provenance
-> Planner triage
-> bounded promotion
-> replay 同一 deck failure
-> unrelated presentation regression
-> plugin changelog/version bump（若 production behavior 真改变）
```

现有 deck 中已经被用户接受的页面/元素必须成为 regression constraint；局部返修不授权全局重做。

### Reporting

`research-reporting` 已吸收 Distributed Imaging Inference 的导师报告经验。下一步不是 synthetic report，而是等待新的独立真实 advisor/group-meeting report；真实失败再进入 `research-writing` TODO。

### 更长期

只有在多个独立真实任务上，普通调用已经能稳定产出用户愿意交给导师/同事的 artifact，才考虑新的 repository minor/major milestone。未来 website 可以读取现有 version/changelog/status source，但现在不建立额外网站数据层。

## 11. 每次 release 前必须回答

每个 repository minor/major release 和每个 plugin minor/major bump 都必须能清楚回答：

> 这版让普通用户以前做不好的哪个真实任务，现在做得更好了？

如果答案只是新增 schema、audit、metadata、synthetic benchmark 或更多 TODO 文件，不应形成 major milestone。

## 12. Presentation / Reporting 当前边界

- `research-presentations` 已形成 Base v1 engineering path，但真实泛化和真实长期返修质量仍需通过 CAT-TRACE 等现有 deck 继续迭代；当前 status 不需要为了填表强行命名 beta/stable。
- `research-reporting` 已吸收 Distributed Imaging Inference 的导师报告复盘规则；继续用下一份真实报告验证，不因单次复盘自动宣布成熟。
- 详细 capability status 只在 `docs/PLUGIN_MATURITY.md` 维护；plugin SemVer 才是长期版本主线。
