# Continuous Real-World Skill Refinement

本文件定义 `AI_Skills_Collection` 的长期维护方式。仓库不再以“做完一轮审计/benchmark 即结束”为目标，而是持续从真实科研、写作、Presentation、统计、医学影像、HPC 与工程任务中吸收用户反馈，并把真正可泛化的经验沉淀为稳定能力。

核心原则：**真实任务先于 synthetic benchmark；TODO 是证据入口，不是 active rule；promotion 必须有边界、有回归、有真实 user-facing effect。**

## 1. 三类 source of truth

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

每条真实反馈只能处于以下一种状态：

- `NEW`：刚记录，尚未判断是否通用；
- `PROJECT_LOCAL`：只属于当前项目/模板/科学语义，不进入中央 plugin；
- `CANDIDATE_GENERIC`：可能跨项目复用，但还未达到 promotion gate；
- `PROMOTE_NOW`：证据足够，可进入 bounded Reviewed Handoff；
- `PROMOTED`：已进入 active skill/shared runtime/QA/profile，并有 regression；
- `BLOCKED_NEEDS_EVIDENCE`：方向合理，但缺真实 render / 第二项目 / production evidence；
- `REJECTED`：不应进入中央能力；
- `SUPERSEDED`：被更强、更通用的 active rule 覆盖。

不要为这些状态新增第二套 workflow state machine；它们只是 plugin TODO 的维护标签。

## 4. Promotion gate

反馈只有满足以下至少一条，才可从 TODO 进入 active plugin：

1. 在两个独立真实项目中重复出现；或
2. 单次出现但属于严重 production failure，例如：科学事实错误、证据伪造、真实图片/公式不可读、对象遮挡、错误路由、source fidelity 破坏、低质量 fallback 冒充完成；或
3. 用户明确确认这是长期跨项目偏好，并且 Planner 能给出清楚边界和可观察 regression。

Promotion 时必须同时冻结：

- `problem`：真实失败是什么；
- `evidence`：来自哪个真实项目/artifact；
- `target layer`：routing / scientific reasoning / composition-rendering / QA-regression / writing-style / profile-docs；
- `boundary`：哪些相邻情况不适用；
- `regression`：以后如何证明没有回归；
- `user effect`：普通用户正常调用后具体变好什么。

缺少其中任一项时，不应直接修改 active rule。

## 5. TODO 不是规则，项目经验不能直接复制进中央插件

例如某个 TRACE 页面出现“两栏 block 高度不一致”，不能直接写成“所有两栏必须等高”。Planner 需要先判断：

- 是否只是该项目的页面选择；
- 是否是通用 peer-level comparison rule；
- 是否需要 renderer/layout primitive；
- 是否已有规则但 consumer 没执行；
- 是否仅需要 QA；
- 是否与现有规则重复。

中央 plugin 只保留抽象后的最小通用能力；项目科学事实、页码、论文名、数据集名、特定 theorem 名称继续留在项目或 provenance。

## 6. 六个稳定层，避免 skill 越长越乱

任何 promoted change 必须归入现有层之一：

1. **Routing / product contract**：用户自然语言应进入哪个 plugin/skill/profile；
2. **Scientific reasoning / narrative**：如何组织问题、证据、模型、理论、限制和下一步；
3. **Composition / rendering**：layout、figure、table、equation、diagram、medical panel、export；
4. **QA / regression**：真实 render、可读性、source fidelity、anti-fallback、重复失败；
5. **Writing style**：读者语气、去日志化、中文/英文表达、不过度结论；
6. **Repository / distribution**：registry、profile、marketplace、version、安装与 generated layer。

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

下一批真实反馈积累后再开启下一轮。不得因为一个 synthetic task PASS 自动生成无限 042/043/044 式验证链。

Planner 必须保护已经通过的行为，优先修真实 blocker；没有真实 blocker 时结束 batch。

## 8. Replay 与 generalization 分开

已暴露问题的真实项目可以成为 regression/replay case，用于证明已知失败被修复；但如果材料曾用于调参，就不能再被称为 unseen/generalization acceptance。

最终 generalization 仍应使用完整预冻结 fresh batch，且 production 在 batch 内冻结。

## 9. Repository release、plugin version 与 capability maturity 分开

Repository / CLI release、individual plugin SemVer、capability maturity 是三个不同概念。完整规则见：

```text
docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md
```

从 `4.4.2` 之后不再要求十个中央 plugin 永久锁步升版：

- repository / CLI 继续使用自己的 SemVer release；
- 每个 Marketplace plugin 的 canonical current version 是 `scripts/codex_marketplace_config.json -> plugins[].version`；
- 只有普通用户可观察行为或安装 payload 真正改变的 plugin 才 bump；
- 每个 plugin 的长期 release history 写入 `docs/plugin-changelogs/<plugin>.md`；
- capability maturity 继续只在 `docs/PLUGIN_MATURITY.md` 维护。

Capability maturity 标签仍为：

- `experimental`
- `alpha`
- `beta`
- `stable`

一个 repository release 可以同时包含不同版本、不同 maturity 的 plugin。禁止为了表示某个 skill 尚未成熟而把整个仓库版本倒退到 `0.x`，也禁止为了一个 plugin 的改动机械 bump 全部 plugin。

## 10. Roadmap 只按真实新增能力推进

当前建议方向：

- **4.4.x — Baseline stabilization**：统一长期反馈结构、版本/maturity source of truth、移除 active payload 中的项目 TODO/历史笔记；
- **4.5.x — Real workflow refinement phase**：重点消费 TRACE Presentation 与 Distributed Imaging Inference report 等真实科研反馈；具体 plugin 版本按各自真实改动独立推进，不要求都达到相同 minor；
- **Cross-project generalization phase**：用新的独立真实项目检查已 promoted 规则是否跨项目有效、是否产生副作用；
- **Stable research communication candidate**：只有当 Presentation / Reporting 等高频入口在多个真实项目上能一次产出用户愿意交给导师的 artifact，且人工修改主要是科研观点而不是基础布局/模板/日志化问题时才考虑对应 plugin 提升到 stable maturity 或进行重大版本跃迁。

这些是能力里程碑，不是强制发布日期；若真实证据不支持，不为凑版本推进。

## 11. 每次 release 前必须回答

每个 minor/major release 必须能清楚回答：

> 这版让普通用户以前做不好的哪个真实任务，现在做得更好了？

如果答案只是新增 schema、audit、metadata、synthetic benchmark 或更多 TODO 文件，不应单独升 major milestone。

## 12. Presentation / Reporting 当前边界

- `research-presentations` 当前记录为 `alpha / Base v1`：Stage 1–4 工程链成立，但真实 4-paper generalization 尚未通过；后续优先由 TRACE 等真实任务 refinement 驱动。
- `research-reporting` 已吸收 Distributed Imaging Inference 的导师报告复盘规则；后续继续通过新的真实报告观察是否达到 beta/stable 门槛，不因单次复盘自动宣布成熟。

详细 maturity 只在 `docs/PLUGIN_MATURITY.md` 维护，不把 maturity 写进 release version。
