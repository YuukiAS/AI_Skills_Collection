# 某私有统计研究项目 v2 组会 PPT 批注整理（2026-08-27）

本文件记录 该项目 组会 PPT **v2** 的 Acrobat 批注。它首先保存项目事实：用户具体对哪些页面、哪些表达和哪些视觉结果不满意。可泛化的科研汇报规则另行提炼，不把 该项目 特例直接当作通用规范。

## 1. 批注来源与颜色约定

- 审阅文件：`group_meeting-v2(1).pdf`，27 页。
- 共读取到 74 个高亮批注，覆盖 P2–P25 和 P27；P1、P26 没有本轮 Acrobat 批注。
- 颜色大致分布：黄色 43、紫色 14、橙色 10、蓝色 6、绿色 1。
- 用户的颜色约定是经验性的：蓝色通常表示 **style / 格式体系**；紫色通常表示 **不像人说话 / AI 味**；黄色和橙色混合记录具体内容、逻辑、格式与视觉问题；绿色用于术语呈现方式。

## 2. 逐页写作与版式问题（公开安全摘要）

原始批注和科学内容留在私有项目仓库，此处不保存模型、数据细节或私有定位。以下只保留返修问题。

### P1

本轮无批注；此前已接受的标题页继续受保护。

### P2

图中文字重叠；首次出现的领域术语缺少稳定样式与必要解释；多个事实挤成一行。

### P3

例子标签像内部代号；缩写未在首次使用处解释。

### P4

参数定义缺少直观含义；挑战与解决方案断开；出现评论页面自身的元话语。

### P5

多个来源未在视觉上分开；公式纵向堆积，缺少推导桥接与对齐。

### P6

对照方法的机制过于压缩；只解释定义，未说明比较价值；正反对偶句式机械。

### P7

并列标题字号不一致；下方内容缺少小标题；双栏与通栏区域需要明确预留空间。

### P8

箭头短且交叠，连线路径不清；关系说明游离在图外。先定拓扑和阅读方向，再做美化。

### P9

普通语言用加号串接；内部状态说明进入了主页面。

### P10

文字溢出解释框；内部字段编码代替自然名称；公式项与解释标签缺少可辨识的对应。

### P11

表头大小写与句式不统一；表格语言像数据库状态字段。

### P12

例子缺少视觉层级；核心变换式太小；否定补充句压过正面结论。

### P13

不适合比较的顺序关系被机械排成双栏，阅读路径不清。

### P14

先验说明的数学层级与引导不足，应说明对象和作用后再给式子。

### P15–P17

理论内容应围绕新增解决的问题组织；区分正式结果与定义，不用未完成的证明填空间。

### P18–P21

实验设计参数不应冒充核心公式；指标需说明评价目标与方向；对照和消融需要真实结构。

### P22–P24

主图和辅助图太小，图注配对不清；数据规模缺少含义；变量用分号挤成长句。

### P25

三个讨论问题用了三套格式；背景不足；问题应由研究判断决定，不能由排版执行者临时发明。

### P26

本轮无批注；后续默认只做回归检查。

### P27

参考文献字号过小，页面下半部空白，需主动利用纵向空间。

## 3. 跨页问题分类

### A. 缺少统一的 presentation style system

集中页：P2、P5、P7、P10–P14、P17–P25、P27。

需要统一：sentence case、术语 first-use、example、question、mini-header、inline label、bullet、table header、two-column、formula hierarchy、metrics、caption、reference、dataset/simulation numbering。

### B. 最终 render 没有真正验收

集中页：P2、P7、P8、P10、P12、P13、P18、P19、P22–P24、P27。

反复出现：文字重叠、box overflow、箭头 overlay / 过短、主图过小、caption 失效、两栏不等高、字号不统一、大片未利用空白。以后编译成功不能视为交付成功。

### C. AI 味 / 模板化句式

集中页：P3、P4、P6、P9、P11–P13、P15、P17–P19、P21、P22、P24、P25。

用户反复不接受的模式包括：

- `This page / This slide ...`
- `This is not X; it is Y` / `this is X, not Y`
- `X does ..., it does not ...` 的机械正反对偶
- `Why this matters`
- `the theorem says ...`
- `not only ...` 作为模板化补充
- `rather than ...` 仅为制造对比语气
- `currently ... only` 等内部状态语言
- `for advisor feedback rather than claimed ...`
- `first-paper ...`
- `Victoria example / Malagasy example / Role / regime / anchor` 等项目标签式语言

### D. Audience grounding 不足

集中页：P2–P4、P6、P9–P12、P18–P24。

目标听众是统计学教授：可以假设懂 Bayesian / regression / asymptotics / latent factors，但不能假设懂 OTU、COI、metabarcoding、GBIF、arthropod taxonomy、具体 plant trait encoding、该项目 内部 notation。

### E. 数学与信息层级没有规范

集中页：P4、P5、P7、P10、P12–P21、P24。

问题包括：核心公式和普通参数同样居中；不相关公式堆叠；`align` / `cases` / inline definition / `underbrace` 没有选择标准；公式与解释脱节。

### F. Theory 没有围绕“模型真正新增什么”组织

集中页：P15–P17、P25。

理论部分应围绕相对既有方法新增解决的问题组织，并说明正式结果间的逻辑关系；尚未完成的证明不占据主页面。具体科学主张留在私有项目仓库。

### G. Simulation / metrics 没有让统计老师快速判断实验

集中页：P18–P21。

需要分清 Design、DGP、estimand、metrics、comparison；metric 既要说明方向，也要说明它检查哪种统计性质。普通 design grid 不允许作为首行居中公式。

### H. Dataset 页缺少统一交付标准

集中页：P22–P24。

需要统一 dataset 标题与层级，但不强制三页同一布局。主图必须足够大；不同图片需要对应 caption/subcaption；真正重要的 rarity 需要定量 visual；字段/变量需要正常人能扫读的结构。

## 4. 第二轮已经确认的方向

用户在本记录之后确认：

1. 全 deck 使用 sentence case。
2. 新增简短背景，讲清听众不熟悉的领域术语之间的关系。
3. 不同对照方法拆页说明。
4. 同级对象保留两栏，但必须等高、对称；底部通栏内容只能在空间充足时保留。
5. 存在先后依赖的解释改成纵向阅读顺序。
6. 理论页覆盖支撑主要主张的正式结果；完整证明完成后再按讨论需要加入。
7. Dataset 1–3 统一标题与文字层级，但不强迫同一种图片布局。
8. 新术语需要统一 first-use style（粗体/颜色/斜体组合应服从模板）。
9. Metrics 推荐 table 或括号结构，并使用 `↑/↓`（或 target，如 coverage → nominal level）表达评价方向，同时解释 metric 作用；多个同类 RMSE 不机械重复箭头。
10. 首行居中的公式只允许核心 scientific object；`n={...}` 等 design settings 不得孤立居中。
11. Diagram QA 进一步收紧：箭头不得 overlay、不得过短，关系必须完整收进图中，diagram 应成为页面视觉中心。
12. 需要建立模板兼容的受控 palette；公式项与对应标签可同色，但不同项需要足够区分度。
13. 图片大小、reference 纵向空间利用、question style、数学环境选择都必须变成可复用标准，而不是每次人工判断。
14. AI 味是当前最大问题，需要多道写作与验收关口；不能只要求 Codex “最后润色一遍”。

## 5. 下一步

- 该项目后续具体执行说明留在私有项目仓库，此处不保存。
- 本轮可泛化经验单独整理为 research-presentation TODO candidates，并记录 AI-like scientific slide prose 的外部研究依据。
- active presentation skill / `scientific-prose` 的正式升级仍应走 AI_Skills_Collection 自己的审阅与合并流程，避免一次项目返修直接改坏全局规则。
