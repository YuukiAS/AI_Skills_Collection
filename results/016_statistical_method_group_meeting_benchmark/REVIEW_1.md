---
schema: AI_BRIDGE_REVIEWED_REVIEW_V1
task_key: 016_statistical_method_group_meeting_benchmark
review_round: 1
decision: REVISE
implementation_commit: 6a7c61550860f7895e79bef96a5a70f59a67844e
---

# GPT Review

## Decision

`REVISE`。

016 的统计/生统 benchmark 主体已经达到冻结计划的大部分要求：确定性 simulation、五页连贯故事、真实 editable PPTX 渲染、机械检查、reference retrieval trace、真实 GitHub CI 与一次新的 `gpt-5.6-terra` Visual Review 均已建立。当前 visual evidence 对 slide 2–5 全部给出 PASS，simulation 数值也与同一 deterministic output 一致。

但 slide 1 仍有一个会改变统计模型含义的局部 blocker：页面把 DGP、中心随机效应 `u_j` 和个体残差 `epsilon_ij` 用串行箭头连接，视觉上形成 `DGP -> u_j -> epsilon_ij` 的生成链，而冻结模型实际是 `u_j` 与 `epsilon_ij` 作为两个独立加性项共同进入 `Y_ij`。这不是单纯美观问题，而是会让听众错误理解模型结构，因此第一轮不能 PASS。

## Evidence reviewed

### CI 与 evidence identity

- 当前 CI bridge 在审核前的 main tip 上发布 `reviewed-handoff/ci-summary=success`；016 因此已从等待 CI 合法推进到 GPT review。
- `RESULT.md` 记录本地 016 targeted test、全库 112 tests、skills validation、Marketplace validation、Reviewed Handoff validation 和 `git diff --check` 均通过。
- `RENDER_STATUS.json` 为 `ok`，五张 PNG 来自真实 editable PPTX render；`MECHANICAL_VISUAL_REVIEW.json` 为 `MECHANICAL_PASS`，且明确没有冒充 academic PASS。
- 当前 `VISUAL_REVIEW.json` 使用 `gpt-5.6-terra`，其五张 PNG SHA 与 `visual_inputs.json` identity 一致；这是 016 新 identity 的一次 live review。

### Simulation 与统计故事一致

同一 deterministic simulation 使用 seed `20260822`、每个条件 400 replicates、`G=[8,20,50]`、`rho=[0,0.1,0.3,0.5]` 和 balanced/imbalanced stress grid。实际结果支持 frozen story：例如 `G=8, rho=0.5, imbalanced` 时 naive iid coverage 为 `0.52`，cluster-robust z coverage 为 `0.7775`，因此 slide 5 的 small-G negative result 与 planned CR2 / wild-cluster-bootstrap next experiment 有真实数值依据，而不是手工制造的失败。

### Slide 2–5 可接受并锁定

- slide 2：cluster sandwich 公式与 center aggregation 语义清楚，Terra PASS。
- slide 3：DGP knobs -> replicates -> 两种 interval branches -> coverage/bias/width endpoint 的主阅读方向清楚，可见 arrowhead 且无 crossing；这一页成功验证了 015 遗留的 diagram-clarity note，Terra PASS。
- slide 4：coverage plot 是主视觉对象，nominal 0.95 reference、方法比较、Monte Carlo uncertainty 和 synthetic boundary 均可见；Terra PASS。
- slide 5：small-G stress 的定量 evidence、failure mechanism 与 planned next experiment 边界清楚；Terra PASS。

## Blocking finding

### F-016-01 — slide 1 的 connector 把两个加性误差项错误串行化

**冻结依据**：PLAN 的 slide 1 contract 要求听众理解 DGP、`u_j`、`epsilon_ij` 与 ICC 的真实含义；active Presentation diagram rule 也要求 connector 必须编码真实结构关系，不能用箭头制造错误的因果/生成顺序。

**真实证据**：generator 的 `draw_model_page` 先放置主公式 `Y_ij = beta_0 + beta_1 T_ij + u_j + epsilon_ij`，再放置 `u_j` 和 `epsilon_ij` 两个说明框，但随后依次绘制：

- 主公式区域 -> `u_j`；
- `u_j` -> `epsilon_ij`；
- 下方到 ICC 框。

因此页面像素中出现了从 `u_j` 指向 `epsilon_ij` 的明显箭头。Terra 对同一真实 PNG 也独立指出，这会让观众读成随机效应生成个体残差。实际 DGP 中二者是不同层级、独立建模的加性误差项，串行箭头与模型语义不符。

**最小修复**：只修 slide 1 connector 语义。优先采用以下任一等价方式：

1. 删除 `u_j -> epsilon_ij` 串行连接，并使用两个分别指向主 DGP/结果式的结构连接，明确它们是并列 additive components；或
2. 完全移除这两个说明框之间的方向性连接，用紧邻文字明确 `u_j` 与 `epsilon_ij` 分别是 center-level 与 individual-level additive components。

不得修改 DGP 数值、simulation grid、estimand、ICC 定义、slide 2–5、reference corpus 或 active Presentation rules。

**复验条件**：

- 新 slide 1 不再出现 `u_j -> epsilon_ij` 的串行生成暗示；
- `u_j` 和 `epsilon_ij` 仍在同页、同一视觉邻域被正确 grounding；
- 新真实 render / mechanical QA 合法；
- 生成新的 visual-input identity，并仅对该新 identity 正常运行一次 `gpt-5.6-terra` review；
- 新 Terra evidence 不再因 DGP connector semantics 判 slide 1 `REVISE`；
- slide 2–5 的已接受 pixels/科学内容不得无关漂移。

## Repair scope

本轮只允许上述 F-016-01 的最小修复及直接相关 deterministic regression。建议增加一个针对 slide 1 connector semantics 的检查，防止以后重新出现 `u_j -> epsilon_ij` 串行边；但不要用像素阈值替代视觉审核。

返修后重新生成 016 的真实 PPTX/PDF/PNG、机械证据和 visual-input identity，并对新 identity 做一次 Terra review，再进入第二轮独立审核。不要扩 source corpus，不做 Source Scout，不提前开始 medical-imaging benchmark，也不要借机重写 Presentation plugin。
