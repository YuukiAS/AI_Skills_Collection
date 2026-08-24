# Research Presentation Design Quality Program Goal

长期目标：普通用户只提供一篇真实科研 paper（或等价真实科研材料），调用一次 `research-presentations`，系统即可生成**可直接用于博士组会汇报、审美成熟、source-faithful、无明显 AI 模板感**的完整科研 presentation，不需要用户逐页教布局或返修基础视觉问题。

当前 `PROGRAM_MATURE=false`。过去 synthetic statistical / medical-imaging benchmark、019–023 与 Terra evidence 只作为工程/失败历史和可复用机制来源，不自动构成最终产品 PASS。

## Product Contract

### 默认输出与 CUHK 身份

对于未显式指定其他模板/格式的科研组会、paper talk、research update：

- 第一成熟 production route 以 `skills/tools/documents-media/presentations/shared/templates/cuhk/beamer/source/` 为 **canonical exact CUHK template**；
- 直接使用真实 `main.tex + styles + assets`，不以 `design-tokens.json` 或 derived PPTX scaffold 仿制 exact CUHK；
- 标题页、顶部 section navigation、frame title、footline/page number、字体和 CUHK 紫白整体身份必须来自 canonical source；
- 默认交付 `.tex + PDF`。只有用户显式要求 editable PPTX/PowerPoint 时才走 PPTX 路线；PPTX 不作为本轮第一成熟闭环的前置条件。

### 内容必须像真实优秀博士生汇报

Audience-facing slide 必须使用目标 paper / data / experiment 的真实科研对象：真实符号、真实变量、真实模型名、真实数据集/endpoint、真实 figure/table/image/metric 和真实 limitation。

禁止用以下内容替代真实科研信息：

- 泛化的 `alpha/beta/x/y` 占位符（除非原 paper 的正式记号就是如此并已在上下文中定义）；
- synthetic toy 当作真实论文证据；
- 大段 AI 总结话术、内部 workflow 元语言、`Evidence Board`/`deck implication`/`QA` 等制作语言；
- 证据不足时用 rounded cards、空表格、generic box-arrow、装饰图标、默认流程图填充页面；
- 将原论文复杂图缩得不可读后直接贴页；
- 每页同一种模板脸。

目标观感：像一名优秀博士生认真读完 paper、理解方法和证据后，为导师组会重新组织并制作的汇报，而不是“AI 把论文摘要分页”。

## Quality-Preserving Continuation Policy

本 program 默认选择**保持最高冻结质量标准**，而不是为了少跑一轮、少搜几个 source 或更快进入下一 Stage 而放宽合同。

Human gate 只用于真正需要用户改变产品/科学语义、接受质量下降、承担明显新的成本/风险，或最终 Stage 5 artifact 验收；不用于“一个选项保持冻结质量门槛、另一个选项只是放宽门槛”的显然选择。遇到这种情况，Planner 必须自动选择保持质量门槛的路线。

如果某个 bounded task 达到 review/plan limit，但 blocker 已被真实 evidence 明确定位，并且存在唯一、质量保持、范围可界定的后续修复路径：

- 保留原 task 的 `REVIEW_LIMIT / AWAIT_HUMAN_DECISION` 历史，不伪造第三轮；
- Planner 可直接创建一个新的 bounded recovery task，不必再次等待用户；
- recovery 必须只处理尚未关闭的 blocker，保留已经 PASS 的实现/evidence，不重做已通过部分；
- recovery 必须使用新的、与 blocker 对应的有限搜索空间或实现机制，禁止重复同一失败动作形成无限 task/retry 链；
- 必须写清停止条件和资源边界；无法在新边界内取得新增 evidence 时再判断是否出现了真正需要用户决定的新问题。

为补齐明确的 reference-coverage 缺口，小规模、定向、rights-safe 的公开 source scouting / intake / real-pixel admission 视为本 program 已预授权的质量保持 recovery，只要它不涉及私有数据、付费采购、许可不明素材或无界 corpus 扩张。

不要通过增加单 task 的无限 review 次数来实现上述 continuation。每个 bounded task 仍保持少量独立 review；跨任务 recovery 用于隔离新 scope、保留失败历史并避免 sunk-cost repair。

## Five-Stage Closure Roadmap

### Stage 1 — Product Contract Reset

把正式 production contract 与仓库真实路由统一：

- `research-presentations`、template routing、tests 与本 Program Goal 一致；
- 未指定格式的科研组会默认 exact CUHK Beamer/PDF；
- derived CUHK PPTX scaffold 明确只用于 non-exact/test，不得进入 exact production；
- 023 的低级 PPTX design-profile renderer 不再是当前主生产路线；023 保留历史 evidence，不做第三轮或 recovery；
- 最终真实双 holdout、Terra item-level、Planner 和 user human gate 写入完成条件。

Stage 1 PASS 后的真实新增能力：普通 production route 已不会继续走错误的默认 PPTX/scaffold 路线。

### Stage 2 — Gold Scientific Composition Library

利用**已经下载/检查的成熟科研演示资源**，不无界扩 corpus。将真实 inspected pages 按 scientific job 重新筛成可运行的高质量 gold composition set，优先覆盖：

- motivation / research question；
- statistical model / estimator / theorem / proof intuition；
- method / experiment design；
- single-result / uncertainty / comparison / negative result / failure；
- medical-image aligned panels / overlay / error / zoom；
- discussion / next experiment。

每个 gold record 必须来自实际 rendered page inspection，并记录 source、page、rights/reuse boundary、scientific job、正文区域 composition、primary-object scale、reading order、annotation/legend/panel关系。

资源只有达到 `RUNTIME_SELECTED -> ACTUALLY_CONSUMED -> OUTPUT_AFFECTED` 才算真正用上。不能把“下载过/写过 audit”算采用。

Stage 2 PASS 后的真实新增能力：系统可以为真实 page job 检索成熟科研构图，而不是让模型自由发明 layout。

### Stage 3 — Executable CUHK Scientific Layout System

把 Stage 2 的 gold composition 变成 exact CUHK Beamer content-area 下的**可执行 scientific layouts/macros**。模型主要做 page-job/content/layout selection，不从空白画布自由画方块。

至少覆盖实际 holdout 所需的 equation/model/theorem、result figure、method/experiment、negative/failure、medical-image comparison、discussion/next-step 等布局。

- 数学：native LaTeX，使用 paper 原始记号；必要时做 term highlight、brace、邻近解释和真实例子；
- 统计图：presentation-native 重绘或重排，保证投影字号、legend、tick、annotation；
- 医学影像：真实同病例 panel、crop/zoom/overlay/GT/prediction/error/legend/callout；
- layout 不适配内容容量时换 layout 或拆页，不允许缩成不可读小字；
- 主方案失败不得回落到 generic cards/box-arrow/default plot。

成熟外部开源实现若直接解决 layout/render 问题，优先选择性 port / adapter；不得只 clone/audit，也不得重造明显低配版本。

Stage 3 PASS 后的真实新增能力：真实科研内容可以在 CUHK 模板内由成熟、受约束的 layout 生成，而不是 task-specific wireframe。

### Stage 4 — One-Call Production Entry + Bounded Quality Loop

正式 `research-presentations` 普通入口必须实际自动完成：真实 source ingestion、source fidelity/evidence map、storyline/page jobs、gold composition retrieval、CUHK layout generation、真实编译/render、page-level visual review、deck-level rhythm review和有限 repair。

关键页可内部生成/比较多个兼容 composition，但不要求用户逐页选择。若候选均低于成熟 reference bar，必须 no-winner，换 layout/拆页/修 figure 后 bounded retry；仍失败则 FAIL，不从垃圾候选里强制挑赢家。

禁止 holdout 直接调用 benchmark helper、task-specific generator 或 test fixture 绕过正式 skill。

Stage 4 PASS 后的真实新增能力：用户一次正常调用确实会走完整高质量 production path。

### Stage 5 — Two Real Paper Holdouts + Human Closure

最终必须用两个**未参与 exemplar extraction / rule distillation / tuning** 的真实公开 paper，从正常 production entrypoint one-shot 生成完整 CUHK 组会 deck：

1. statistics / biostatistics / methodology paper；
2. medical-imaging paper，必须使用真实论文 figures / medical images。

两个 deck 都必须是完整组会 presentation，而不是少数 benchmark pages。

## Final Quality Gates

只有以下全部成立，才允许进入最终 human closure：

- source fidelity：关键 claim、method、结果、限制都能追溯到 paper；
- content specificity：真实 paper 符号/对象/数据/图像主导，不是 placeholder notation；
- CUHK fidelity：实际由 canonical CUHK Beamer source 构建；
- resource use：关键页有真实 runtime reference retrieval/selection/consumption trace；
- page quality：无垃圾方块、generic arrows、AI 元语言、默认图表脸、明显无意义空白或不可读 figure；
- deck quality：storyline、信息密度和视觉节奏像成熟博士组会，而不是逐页模板化摘要；
- Terra：必须读取最终生成 item/page 的 item-level judgement；`overall PASS` 只代表 package assessable 时不得当作质量 PASS。主要内容页须达到 mature research-group-meeting / strong conference-talk bar；
- Planner：独立读取真实 source、production trace、render、reference use、Terra item reviews/contact sheet 后 PASS；
- production entry：验证正常用户调用而非 helper/fixture；
- no test-specific hardcode / holdout-specific layout hardcode。

Terra PASS + Planner PASS 后仍不能自行宣告长期完成。必须把两套真实最终 deck 提交到现有合法 `AWAIT_HUMAN_DECISION` 人工门，由用户实际查看。

**只有用户明确接受统计 paper deck 与医学影像 paper deck 两套结果，才允许写 `ONE_SHOT_QUALITY_PASS`。**

用户若认为任一 deck 仍像 AI、审美差、内容空洞、符号泛化、没有真正使用参考资源或不像能上组会的博士生汇报，则视为真实 production regression，必须按用户观察做最小修复后重新验收。
