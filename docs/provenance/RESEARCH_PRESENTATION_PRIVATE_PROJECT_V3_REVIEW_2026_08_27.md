# 某私有统计研究项目 v3 组会 PPT 批注记录 — 2026-08-27

本文记录用户对 该项目 group-meeting deck **v3**（29 页）的 Acrobat 批注。它先忠实保存本轮不满意点，再为下一轮逐页讨论提供依据；不在这里直接改 该项目 科学内容。

## 1. 批注概况

- PDF：`PRIVATE_PROJECT_v3.pdf`
- 页数：29
- Highlight comments：51
- 黄色：27
- 橙色：21
- 深橙色：3
- 用户明确约定：**本轮所有橙色/深橙色批注都必须转化为可复用规则，并在后续科研 PPT 中持续应用。**
- 黄色主要记录当前页具体内容、解释、科学叙事或局部样式问题；其中部分也可能在第二轮确认后上升为通用规则。

## 2. 逐页写作与版式问题（公开安全摘要）

原始批注和科学内容留在私有项目仓库，此处不保存模型、数据细节或私有定位。以下只保留返修问题。

### P1

本轮未报告新的页面问题。

### P2–P4

文字与标注间距不稳，叙事先后仍有跳跃；新术语和目标量需要先建立直观含义。

### P5–P8

比较方法仍有一句公式代替完整机制的问题；背景应先于新方法，公式中出现的新参数要就近解释。

### P9

核心内容偏小，纵向空间利用不足；并列区域缺少清楚的阅读边界。

### P10

节点内文字与公式拥挤；箭头可见长度、端点和交叠问题仍未解决。

### P11–P12

表格缺少使用背景；标题和字段句式不统一；结构化事实没有用真实表格或列表组织。

### P13–P14

公式和说明的层级不稳；纵向空间利用与支撑性定义的位置仍需修正。

### P15–P16

内部稿件状态或实施语言进入主页面；方法名与机制说明需让听众能定位对象。

### P17–P18

页面从未解释的数学符号开场；极限条件写成生硬口语；正式结果类型和编号应真实、自洽。

### P19

无本轮批注。

### P20

主图仍小，图注过长；仓库路径与随机种子挤占正文；设计取值和评价目标没有充分说明。

### P21

问题区需要统一视觉处理；指标方向应紧贴名称；方法比较不能用一串分号代替结构。

### P22–P23

无本轮批注。

### P24–P25

数据事实堆成裸数字；辅助图缺图注且偏小；内部检查语言再次进入主页面。

### P26

仅保留通用回归要求，不在此保存项目内容。

### P27

问题与背景的文字密度和可用空间不匹配。

### P28

仅保留通用回归要求，不在此保存项目内容。

### P29

参考文献字号和间距仍未随条目数量调整。

## 3. 按失败类型归类

### A. 重复出现、必须升级为 hard QA 的视觉问题

页：P2, P9, P10, P20, P24, P25, P27, P29。

核心问题：

- overlay / edge overlap 仍发生；
- diagram 箭头仍太小；
- 主图仍太小；
- 纵向空间大量浪费；
- structured facts 没有使用合适容器；
- reference/discussion 页人为压缩字号。

这些不是新的审美意见，而是 v2 已经提出、v3 再次违反的 regression。

### B. 数学对象层级与引导不足

页：P4, P6, P8, P15, P17, P18。

核心问题：

- 公式先于动机/定义；
- 新参数不解释；
- `as p grows` 等非标准数学英语直接进入公式；
- 非核心公式被放在视觉中心；
- theorem / corollary / proposition 编号与理论覆盖没有统一体系。

### C. Audience-first 仍执行不稳定

页：P2, P3, P7, P11, P12。

核心问题：

- OTU、catalogue、arthropod、Malagasy、phylogeny 等仍然先用后解释或只做形式定义；
- framework/term style 没有完全统一；
- 定义没有通过真实 case 建立直觉。

### D. 内部项目/工程语言继续泄漏

页：P15, P20, P25；相关局部还有 P12。

出现：

- manuscript draft；
- validation audit；
- repo path / summary note path；
- 不重要的 reproducibility metadata（seed）占据主页面。

这是多轮明确禁止后仍出现的严重 regression。

### E. Table / list / callout 选择仍不稳定

页：P11, P12, P21, P24, P27。

核心问题：

- table 缺 context；
- header capitalization / wording 不统一；
- facts 没有形成 table/list；
- question 没有稳定 visual treatment；
- comparison 继续用分号串；
- background 的好做法没有上升成 reusable pattern。

### F. 科学叙事顺序仍有跳跃

页：P2, P4, P7, P8, P17, P18。

核心问题：

- 新方法名称早于背景和方法动机；
- estimand 早于“为什么关心”；
- 对照方法仍有一句公式或边界代替完整机制；
- theorem 直接从符号开始，没有先说研究问题。

## 4. 对 v2 规则执行情况的复盘

v3 并不是完全没有使用 v2 新规则。该项目第三轮返修任务 明确吸收了：sentence case、first-use term style、mini-header、two-column rule、核心公式居中门槛、metrics table、main visual size、diagram contract、anti-AI scan、reference 放大等要求；源文件也新增了 `newterm`, `minihead`, `standalonehead`, `semanticlabel`, `metricrow` 等宏。

但结果说明当前流程存在一个关键缺口：**规则被写进 prompt ≠ 规则被可靠执行与验收。**

本轮重复失败包括：

- v2 已禁止 overlay，P2/P10 仍出现；
- v2 已要求利用纵向空间，P9/P27/P29 仍失败；
- v2 已要求 diagram 箭头足够大、无 overlay，P10 仍失败；
- v2 已禁止内部工程语言，P15/P20/P25 仍出现 manuscript/audit/path；
- v2 已规定首行居中公式必须是核心对象，P17/P18 仍从未解释的定义开场；
- v2 已要求主图足够大，P20/P25 仍然过小。

因此下一轮不能只把规则继续复制进 prompt；必须增加“继承 + 逐条验收 + regression evidence”机制。

## 5. 下一轮讨论边界

当前先保存全部 v3 批注并建立问题地图。下一步由 GPT 按 P1 -> P29 做第一轮审阅和修改方向讨论；用户确认后，再形成 v4 execution task。

所有橙色/深橙色项必须在 v4 task 前被映射到可复用规则，并标记是否：

1. 已有规则但 v3 执行失败 -> 升级为 hard regression gate；
2. 已有规则但太模糊 -> 补充可执行阈值/示例；
3. 真正新规则 -> 加入 presentation TODO candidates；
4. 该项目 特例 -> 不进入通用规则。
