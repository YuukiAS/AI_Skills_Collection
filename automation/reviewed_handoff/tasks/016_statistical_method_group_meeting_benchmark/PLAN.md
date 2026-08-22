---
schema: AI_BRIDGE_REVIEWED_PLAN_V1
task_key: 016_statistical_method_group_meeting_benchmark
decision: PLAN_FROZEN
---

# 016 Statistical / Biostatistical Method Group Meeting Benchmark — Plan

## Objective and value

建立一个真正像统计方法组会、而不是“统计主题模板”的 5 页 benchmark。核心问题固定为：**多中心数据存在组内相关时，点估计可能看起来稳定，但把个体当作独立观测会让置信区间覆盖率失真；cluster-robust inference 能修正大部分问题，但在中心数很少时仍存在负结果。**

这条故事线用于检验 Presentation skill 对 statistical model、estimator/derivation、simulation design、uncertainty/result、negative result / next discriminating experiment 的表达能力。页面必须以公式、DGP、结果图、诊断和实验设计等真实统计对象为中心，不能退化成 cards/dashboard。

## Frozen decisions

### Frozen benchmark story

使用完全 synthetic、固定随机种子的多中心连续结局模拟，不宣称真实临床或真实研究结果。DGP 为：

```text
Y_ij = beta_0 + beta_1 T_ij + u_j + epsilon_ij
u_j ~ N(0, tau^2)
epsilon_ij ~ N(0, sigma^2)
ICC rho = tau^2 / (tau^2 + sigma^2)
```

其中中心 `j` 是相关性单元，目标 estimand 为 treatment effect `beta_1`。比较至少：

- naive iid OLS interval；
- center-cluster-robust interval。

可以加入一个简单、透明且由同一 simulation 真实计算的第三 comparator，但不得为了视觉丰富而引入无法解释或未实现的方法。任何数值结果都必须由 benchmark simulation 脚本实际生成，不得手工编造结果图。

Simulation grid 至少覆盖：

- center count：small / moderate / larger（建议 `G=8,20,50`）；
- ICC：从接近独立到明显相关（建议 `rho=0,0.1,0.3,0.5`）；
- 至少一个 cluster-size imbalance 条件或等价 stress condition。

主要 endpoint：95% interval coverage；辅助 endpoint 可包含 bias 与 interval width。Coverage 图必须显示 nominal 95% reference line，并显示 Monte Carlo uncertainty 或等价可解释的不确定性信息。

## 五页页面合同

### Slide 1 — STATISTICAL_MODEL / “What is the inferential failure?”

页面只完成一个任务：让听众理解 estimand、中心内相关从哪里来，以及为什么“点估计没明显偏”不代表 interval 正确。

必须可见：

- `beta_1` 的 estimand 定义；
- DGP 主公式；
- `u_j`、`epsilon_ij`、ICC `rho` 的现实含义；
- center 是相关性/推断单元的直接说明；
- synthetic benchmark evidence boundary。

不要用三张定义卡代替模型式。

### Slide 2 — ESTIMATOR / DERIVATION / “What changes in the variance?”

页面只解释 naive variance 与 cluster-robust sandwich variance 的关键区别。

必须可见 cluster-robust covariance 的代表性公式，例如：

```text
V_CR = (X'X)^(-1) [sum_g X_g' u_g u_g' X_g] (X'X)^(-1)
```

不要求教科书式完整证明，但必须解释每个关键块为何按 center 聚合、它修正的是什么。公式是主 scientific object；不能把公式缩在卡片角落。

### Slide 3 — SIMULATION_DESIGN / “What experiment can distinguish the intervals?”

必须把 DGP knobs、methods、replicates 与 evaluation endpoints 连成可读实验设计。

需要清楚展示 `G`、`rho`、cluster-size imbalance、replicate count、95% coverage/bias/width。若使用 diagram：

- connector 必须是结构连接线；
- 方向必须一眼可见，使用可见 arrowhead；
- 不允许 edge crossing；
- 主阅读方向只能有一个。

这一条用于延续 015 中未阻断但值得跨 benchmark 验证的 diagram-clarity 观察，不回头修改 015 的 accepted slide。

### Slide 4 — RESULT_FIGURE / “Where does coverage actually fail?”

这是主结果页。必须由真实 simulation 输出生成 plot，而不是手工画示意 bars。

至少展示 coverage 对 ICC 的变化，并区分方法；95% nominal line 一眼可见。Monte Carlo uncertainty 必须直接编码在图上或紧邻图。页面结论只能陈述当前 synthetic simulation 真正支持的结果，不得把 preliminary benchmark 说成一般定理。

主图必须获得最大页面面积；不要使用 `title + cards + summary strip`。

### Slide 5 — NEGATIVE_RESULT + NEXT_EXPERIMENT / “What still fails, and what would we test next?”

只聚焦一个负结果：small-G / high-ICC 等 stress regime 下 cluster-robust interval 仍可能不稳定或覆盖不足（必须由本次 simulation 实际结果支持；若实际 simulation 不支持该预设，则按真实结果改写，不得强行制造 failure）。

必须同时显示：

- 负结果的实际 quantitative evidence 或 diagnostic；
- failure mechanism 的简洁解释；
- 一个真正有区分力的下一实验，例如 small-sample correction / CR2 / wild cluster bootstrap comparison；
- next experiment 明确标记为 planned，不能伪装成已完成结果。

## Reference retrieval contract

使用现有 inspected-page library，不扩 corpus、不下载新 source、不做 Source Scout。

每页根据 page function + statistics/biostatistics domain + evidence type 语义检索 2–5 个 inspected reference pages，并保存 retrieval trace：query、candidate IDs、selected IDs、ranking/relevance reason、source tier。PRIMARY_RESEARCH_PRESENTATION 优先；不得重新硬编码一组固定 RRL IDs 代替检索。

Reference 只用于组织与视觉经验，不复制完整原 slide。

## Implementation scope

允许新增/修改：

- 新 benchmark fixture，例如 `tests/fixtures/presentations/statistical_method_group_meeting/`；
- deterministic simulation/generator/reviewer/visual-input adapter 所需脚本；
- 对应 editable PPTX、PDF、rendered PNG、expected render、evidence manifest、render status、mechanical visual review；
- `tests/test_presentations.py` 中与本 benchmark 直接相关的 deterministic regression；
- `results/016_statistical_method_group_meeting_benchmark/RESULT.md`；
- `results/016_statistical_method_group_meeting_benchmark/visual_review/visual_inputs.json` 与由 Bridge Kit 写回的 `VISUAL_REVIEW.json`。

不得预先修改 active SKILL / visual-qa / archetype contract。若本 benchmark 后续独立 review 暴露出 active contract 真正缺失的通用规则，由 Planner 判断是最小 re-plan 还是下一 bounded task；Executor 不得在首轮实现里自行扩规则。

## Implementation requirements

1. Simulation 必须 deterministic（固定 seed）且在合理时间内完成；结果 artifact 要记录 DGP、grid、replicates、methods 和 raw/summary output，便于审计。
2. 生成器必须创建真实 editable PPTX，不得另画 parallel PDF 冒充 render。
3. 真实链路固定为 editable PPTX -> presentation engine -> PDF -> PNG；若运行环境缺真实 renderer，必须明确 BLOCKED，而不是把 source artifact 当 render PASS。
4. Mechanical reviewer 只给机械/渲染结论，不得冒充 academic visual PASS。
5. 每页 one-slide-one-job；公式、主图、DGP、negative evidence 等 scientific object 按科学层级分配面积，不机械追求 50/50 或三栏对称。
6. 首次出现的 `G`、`rho`、ICC、cluster-robust 等概念必须在同页视觉邻域 grounding；不允许下一页才解释上一页符号。
7. 所有 simulation/result 页必须明确 `synthetic` / `simulation` evidence boundary。
8. 不使用内部 run ID、repo path、RRL ID 作为 audience-facing slide 内容；retrieval trace 只留 evidence/notes。
9. Slide 3 若用 diagram，显式检查 arrowhead、direction、crossing 与 peer alignment；不能用文本字符箭头冒充结构 connector。
10. Slide 4 coverage 图的 favorable direction/target semantics 必须明确：接近 nominal 95% 是目标，不能用“越高越好”误读超过 nominal 的 over-coverage。

## Deterministic tests

至少验证：

- 5 页 page function 与 frozen story 对应；
- simulation summary 来源于同一 deterministic script，包含 frozen grid/endpoints；
- slide 1 包含 estimand/DGP/ICC grounding；
- slide 2 包含 cluster-robust covariance 语义和 center aggregation；
- slide 3 的 diagram 若存在，connector/arrowhead metadata 或 PPTX object semantics 符合本 Plan；
- slide 4 的 result data 与 simulation summary 一致，存在 nominal coverage reference 与 uncertainty；
- slide 5 的 negative-result claim 与实际 simulation 数值一致，planned method 没被标成 completed evidence；
- 每页有 2–5 inspected reference retrieval trace；
- source/generated/plugin 不因本 benchmark 发生无关漂移。

不要用单一像素阈值替代最终视觉判断。

## Local validation and CI

Executor 至少运行：

- `python -m unittest tests.test_presentations`
- `python -m unittest discover -s tests`
- `python scripts/skills.py validate`
- `python scripts/build_codex_marketplace.py --validate --check --path-report`
- Reviewed Handoff repository-wide validation
- `git diff --check`

随后写 RESULT、push implementation/handoff，进入 `WAITING_FOR_CI`。本地 CI bridge 必须对 current tip 发布 `reviewed-handoff/ci-summary`。

## Terra visual review

Conventional CI 和真实 render 准备完成后，为 **016 自己的 visual-input manifest** 只 dispatch 一次 Bridge Kit visual review：

```text
manifest=results/016_statistical_method_group_meeting_benchmark/visual_review/visual_inputs.json
output=results/016_statistical_method_group_meeting_benchmark/visual_review/VISUAL_REVIEW.json
```

默认模型必须是 `gpt-5.6-terra`，不创建 repo-level model override。五张 PNG SHA 必须与 manifest identity 一致。Terra `REVISE` 是学术视觉证据，不是 transport CI failure；Planner 独立决定 PASS/REVISE。

## Acceptance and regression gates

本 task 只有以下全部成立才可 PASS：

1. 真实 GitHub CI PASS；
2. deterministic simulation 真实运行，结果图与 negative-result claim 可追溯到 simulation output；
3. 五页形成一条连贯统计方法故事，不是五种模板拼盘；
4. model/estimand/公式在投影尺度可读，符号有 grounding；
5. simulation design 可在约 5 秒内读出 DGP knobs -> methods -> endpoints，若使用 diagram 则无 connector crossing 且方向明确；
6. 主结果 figure 是页面视觉中心，coverage target、method comparison、uncertainty 与 synthetic boundary 清楚；
7. negative-result 页显示真实 failure evidence，并把 next experiment 明确标为 planned；
8. 每页有 2–5 个真实 inspected reference retrieval trace，没有 metadata-derived fake page records；
9. real PPTX render + mechanical QA 合法；
10. 新 identity 只有一次 `gpt-5.6-terra` live review，Planner 独立核对实际页面像素与 frozen contract；
11. 不扩 source corpus，不做 Source Scout，不提前做 medical-imaging benchmark，不借机重构 Presentation plugin。

若第一轮 review 发现可在冻结范围内局部修复的 blocker，只给最小 REVISE；第二轮仍不能关闭则进入 human gate。

## Out of scope

- medical-imaging Phase C benchmark；
- 新 source acquisition / Source Scout；
- active-rule 大规模重写；
- 发布新 Presentation plugin 版本；
- 真实临床数据或私有 patient image；
- 把本 synthetic benchmark 当作统计方法论文结论。
