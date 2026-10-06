# 059 Research Authoring C2 G1 最终验收失败 — 收口要求 v0.1

日期：2026-10-06  
角色：独立 Critic  
任务：`research-authoring--formal-production-authoring`

## 目的

前几轮失败说明，不能再按“看到一个症状 -> 局部补一句规则 -> 再进最终验收”的方式推进。

下一候选在实现前，Planner 必须一次性证明完整正常入口的所有权链条，而不是只修当前失败命令。

## 已确认根因

C2 的 Research Authoring 聚合入口已经被实际读取，但全局 `render-chinese-math-pdf` 仍在同一自然请求中被提前选择并执行。

因此当前问题不是：

- candidate 未加载；
- replay isolation；
- renderer 本身不会生成 PDF；
- aggregate 缺少同义禁止句。

真正缺口是：

**Research Authoring 与 renderer 之间缺少可执行的入口所有权协调。**

“某个 renderer Skill 在机器上可发现”不能等于“当前 Research Authoring 请求已经授权它接管产物阶段”。

## 下一候选必须同时解决的三种正常入口

Planner 提案必须用同一个机制同时解释并验证：

### 1. 独立 Research Authoring

自然请求：

“把研究更新整理成正式 PDF。”

在 standalone `research-writing` / Marketplace Research Authoring 入口：

- Research Authoring 负责文档语义和 source；
- 输出完整下游生产交接；
- 即使机器全局安装了 renderer，也不能自动进入 renderer；
- 不创建/预览/检查 PDF。

### 2. `research-main` 正式生产组合

同类请求在明确包含 Research Authoring + renderer 的正式生产 profile：

- 必须先进入 Research Authoring；
- 文档语义稳定后产生明确下游交接；
- renderer 之后才可进入；
- renderer 负责 PDF mechanics / QA；
- 不允许 renderer 抢先成为主 owner。

### 3. 真正 render-only

例如：

“把这个已经最终定稿的 Markdown 渲染成 PDF。”

- renderer 可以直接成为 owner；
- 不强制进入完整 Research Authoring 文档规划；
- 不能因为本轮修复把正常 renderer 能力破坏掉。

## Planner 必须比较的最小机制

不得默认只改一个文件。

必须比较：

1. Research Authoring canonical core/report owner boundary；
2. `render-chinese-math-pdf` 的 Trigger Boundary / primary-owner exclusion；
3. `research-main` 与 standalone Research Authoring 的 profile/routing metadata。

最终可以选择其中最小组合，但必须解释为什么没有被修改的层不需要改。

## 不接受的“修复”

以下不能支持新候选：

- 只在 generated report aggregate 再加一句禁止；
- G1 专用 prompt；
- 命令黑名单；
- fixture/path/hash 特判；
- replay helper 隐藏 renderer；
- 把全局 renderer 暂时卸载后声称产品已修；
- 只做静态字符串测试；
- 只证明 standalone，不证明 `research-main` 仍能正常生产 PDF；
- 只证明 `research-main`，不证明 render-only 没退化。

## C3 前置开发回归矩阵

任何新的 product candidate 冻结前，必须在真实正常入口至少覆盖：

1. standalone report + formal PDF request -> source + handoff，禁止 PDF mechanics；
2. standalone non-PDF advisor report -> Research Authoring正常完成；
3. standalone manuscript + formal PDF request -> source/package handoff，不偷跑 renderer；
4. research-main report + formal PDF -> Research Authoring先行、renderer后行、真实 PDF成功；
5. research-main manuscript + PDF -> paper route先行、renderer后行；
6. render-only finalized Markdown -> renderer直接工作；
7. render-only finalized LaTeX -> renderer直接工作；
8. neighboring owner：PPT/Beamer、citation-only、ordinary Q&A 不被误路由。

至少还要有两个反例：

- renderer 全局可发现，但 standalone Research Authoring仍停止在 handoff；
- unrelated non-candidate Skill/global state存在时不改变上述 owner判定。

每个 case 要有实际 runtime consumption / command evidence，不能用描述或字符串检查替代。

## 候选冻结规则

只有上述开发回归全部通过，才能形成新的 Research Authoring product candidate C3。

C3 必须包含所有真实 production owner/routing修改；不得把关键修复放在 test harness 或本地环境中。

C2 G1 FAIL 永久保留。

C3形成后：

1. 独立 Critic 审 development matrix 与 candidate diff；
2. 冻结新的 pre-final packet；
3. 再执行 final G1-G4；
4. 所有 final evidence直接绑定同一个 C3。

## ChatGPT Plugin 准备

如果 C3开发回归通过，Executor应在进入 pre-final前同时准备：

- exact-C3 skills-only `research-authoring` wrapper archive；
- 完整 file/hash manifest；
- expected distribution version；
- guarded-update输入。

这一步不修改 live Plugin。

这样后续 G4若需要真实 ChatGPT试用，只需要一次用户明确授权进行 guarded live update，不再临时组包。

## 目标

下一轮不是“再补一个 blocker”。

下一轮的成功标准是：

**一个候选在 standalone、正式生产 profile、render-only 三类真实入口上同时证明 owner路由正确，再进入最终 Gate。**

在这个开发矩阵通过之前，不再消耗新的 final Gate。
