# Mandatory research-presentation rule candidates — CAT-TRACE v3 review, 2026-08-27

本文件只保存本轮橙色/深橙色批注中 **用户明确要求以后必须形成通用规则** 的内容。它们不是 CAT-TRACE 专属科学决定；后续在 v4 方向确认后，应与现有 `TODO.md`、v2 candidates、active skill、shared QA 和 regression tests 做去重，然后把重复失败项优先提升为 hard QA，而不是继续停留在模糊建议层。

## 1. Rule inheritance：每轮必须继承上一轮规则

- [MANDATORY_CANDIDATE] 每个真实 deck revision task 在生成前必须读取上一轮 `accepted rules / regression constraints`，不能只读取当前 prompt。上一轮新增规则要么已经进入 active presentation skill，要么进入一个 tracked cumulative rule ledger；不能只留在历史聊天或一次性 prompt。
- [MANDATORY_CANDIDATE] 新一轮 task 必须建立 `inherited_rule_checklist`：`rule -> source round -> affected page/archetype -> implementation -> rendered verification`。没有 implementation / rendered verification 的规则不能算“已读取”。
- [MANDATORY_CANDIDATE] 如果某条规则在连续两轮出现同类失败，应从 soft guidance 升级为 hard regression gate。Generator 自报“已检查”不能代替 rendered evidence。
- [MANDATORY_CANDIDATE] 通用规则与项目规则分层：通用 style / QA 进入 presentation skill；本项目特有术语、页面保留/删除、科学事实进入 project revision ledger。每轮 task 同时读取两层。

## 2. Rendered overlap / geometry 必须直接 fail

来源：P2, P10；v2 已出现，v3 重复。

- [MANDATORY_CANDIDATE] 任何 visible text-text、text-node、edge-node、edge-text、edge-edge overlay 都直接 `REVISE/BLOCKED`，不能因 LaTeX 无 overfull warning 而通过。
- [MANDATORY_CANDIDATE] Overlay 必须从最终 rendered page 检查，而不是只看 TikZ source / object bounding boxes。
- [MANDATORY_CANDIDATE] 用户已在前轮指出的 overlap 类型要进入 regression test；下一轮相同位置或同类结构再次出现时视为 repeated regression。

## 3. Vertical-space utilization 是正式 QA，不是审美备注

来源：P9, P27, P29；v2 已提出，v3 重复。

- [MANDATORY_CANDIDATE] 核心内容明显缩小、而页面仍有大面积连续空白时，默认判 layout failure。不能把“页面没有 overflow”当成通过。
- [MANDATORY_CANDIDATE] 每个 archetype 应有 vertical occupancy / readable font 的软阈值。Theory、discussion、references、two-column model 等页面都应使用可用纵向空间提高字号、行距、图尺寸或层级间距。
- [MANDATORY_CANDIDATE] 如果 reference 数量较少，优先放大字号和行距；不得为了沿用固定布局而让下半页空白。
- [MANDATORY_CANDIDATE] Discussion questions 数量较少时，扩大每个 question block 的字号、行距和间距；不要把全部内容压在上半页。

## 4. Two-column + full-width 必须预留清晰的独立区域

来源：P9。

- [MANDATORY_CANDIDATE] 两栏只处理 peer-level 对象；若下方还有 shared/full-width scientific object，生成时必须预先划定第三个区域。
- [MANDATORY_CANDIDATE] 上下区域之间必须有可见 whitespace 和独立 heading/visual grouping；不得把 shared formula 像 footnote 一样贴在两栏底部。
- [MANDATORY_CANDIDATE] 如果 peer content + shared content 无法在正常字号下清楚分区，必须拆页，不能缩小全部内容。

## 5. Diagram construction 与 arrow QA 必须硬化

来源：P10；多轮重复。

- [MANDATORY_CANDIDATE] Diagram 必须先定 semantic graph 和 reading direction，再放 node；禁止先摆 node 后用随机 diagonal 补连。
- [MANDATORY_CANDIDATE] Architecture/mechanism diagram 应成为页面视觉中心；不能画成页面中央一个小组件再让大量空白包围。
- [MANDATORY_CANDIDATE] 主箭头必须有足够可见线段和明确 arrowhead；不能短到只剩箭头尖。Arrowhead size、line width、node clearance 必须使用 deck-level canonical style。
- [MANDATORY_CANDIDATE] 箭头不得 overlap、crossing、穿字或随机打到 box 角；必须用 semantic anchors / ports。
- [MANDATORY_CANDIDATE] Diagram 内理解节点所必需的 set difference、条件、定义要整合到 node / brace / annotation；不要把关键定义孤零零扔到 diagram 外。
- [MANDATORY_CANDIDATE] 每个 diagram 页必须单页高分辨率 render 验收；contact sheet 不足以通过。

## 6. Centered / first-line math 必须经过 semantic gate

来源：P4, P17, P18；与 v2 公式层级规则重复失败。

- [MANDATORY_CANDIDATE] 页面第一屏/首行居中的公式必须是已经有语义铺垫的核心 scientific object。新 estimand、新 random quantity、新 theorem quantity 不能在听众不知道“它表示什么/为什么关心”的情况下直接居中出现。
- [MANDATORY_CANDIDATE] Theorem / proposition 页如果需要先定义 quantity，优先先用一句自然语言说明对象，再写定义；不要以未解释的 `N=...` 直接开场。
- [MANDATORY_CANDIDATE] 任何 display formula 引入新符号时，同页或前文必须定义；不能依赖讲者临场补全。

## 7. Mathematical English / limit notation 使用标准写法

来源：P6, P17, P18；重复 regression。

- [MANDATORY_CANDIDATE] 极限条件使用标准数学表达，例如 `p -> infinity` 放在 `lim` 下标或紧邻数学句中；不得把 `as p grows`、`as all p_g grow` 等口语片段机械塞进公式。
- [MANDATORY_CANDIDATE] 同一 deck 中 limit / convergence / expectation notation 要统一；数学对象中的解释性短语放在公式外的 prose，不把普通英文当作 operator label。

## 8. 新公式不能只“扔公式”：新参数必须解释

来源：P8。

- [MANDATORY_CANDIDATE] Comparator/method slide 中出现 posterior/prior approximation、transfer distribution 等新公式时，公式中的新 location/scale/latent quantity 必须说明来源和作用。
- [MANDATORY_CANDIDATE] 一条公式如果听众无法回答“每个量从哪里来、下一步怎么用”，不能作为方法解释的唯一内容。

## 9. Internal engineering language / file path / draft status 永久禁止进入主 slide

来源：P15, P20, P25；多轮重复。

- [MANDATORY_CANDIDATE] Audience-facing slide 禁止出现 `validation audit`, `manuscript draft`, `summary_note.md`, repo path, task/result path, internal status 等实现/编辑记录。
- [MANDATORY_CANDIDATE] 数据来源应转成可读 citation / source phrase；内部 path 只留 notes / result record。
- [MANDATORY_CANDIDATE] 交付前必须同时扫描 source `.tex` 和 compiled PDF text；关键词表只作为第一道门，还必须人工检查同义内部语言。
- [MANDATORY_CANDIDATE] Random seed、run id、hash 等 reproducibility metadata 默认不放主 slide，除非其本身是科学问题的一部分。

## 10. Supporting definitions / glossary 不能破坏主层级

来源：P11。

- [MANDATORY_CANDIDATE] 次要数据库/缩写解释（例如某个 reference infrastructure）若不是本页核心，不得在页面底部以醒目整行 prose 抢占视觉层级。
- [MANDATORY_CANDIDATE] Supporting definition 优先贴近 first-use term、使用小型 footnote / margin note / parenthetical definition；如果需要两三句才能讲清楚，另设 background slide，而不是悬在主结构外。

## 11. Theory pages 必须按“解决什么现有模型解决不了的问题”选结果，并有正式编号体系

来源：P17 + 用户上一轮已确认原则。

- [MANDATORY_CANDIDATE] Theory coverage 先列 closest-method gaps，再选择 formal result。主 deck 中的 theorem/proposition 必须对应 proposed model 的关键合法性或新增能力，不能按“文件里有什么”选。
- [MANDATORY_CANDIDATE] Theory 页面使用稳定编号体系，并与 manuscript 对齐或在 deck 内自洽。`Theorem`, `Corollary`, `Proposition` 不能只有类型没有编号。
- [MANDATORY_CANDIDATE] 如果主要创新声称有多个 formal guarantees，deck 应检查是否完整覆盖最关键的 2–4 个，而不是为了页数只放一个或为了显得多而把普通定义包装成 theorem。

## 12. Figure-heavy slide：主图、caption 与设计信息必须重新分层

来源：P20, P25；v2 已提出，v3 重复。

- [MANDATORY_CANDIDATE] Figure-heavy slide 的主图若在会议室投影下读不清 panel title、axis、legend、点/线关系，直接 fail；优先放大主图、删文字或拆页。
- [MANDATORY_CANDIDATE] Caption 只说明 visual encoding / uncertainty / line meanings 中真正需要的信息；不能复制论文式长 caption 到 slide。
- [MANDATORY_CANDIDATE] 每个辅助图必须有紧贴的 caption 或明确 label；不允许小图无 caption、让听众猜。
- [MANDATORY_CANDIDATE] 设计参数应保留科学判断需要的信息；seed、路径等 metadata 移出主页面。

## 13. Metric direction 使用箭头/target notation，不写 lower/higher 列

来源：P21；承接 v2 metric candidate。

- [MANDATORY_CANDIDATE] Metric table 名称直接携带方向：`RMSE ↓`, `PR-AUC ↑`, `Coverage -> nominal`，避免另设 `direction = lower/higher/near target` 的冗余列。
- [MANDATORY_CANDIDATE] 多个同 family metrics 合并方向说明，例如 `Discovery RMSE ↓ (total / catalogue / open tail)`。
- [MANDATORY_CANDIDATE] Metric 仍需说明它检查什么统计性质；方向符号不能替代 metric purpose。

## 14. Comparison block 不能用分号 dump，也不能把 focal method 当普通 competitor

来源：P21。

- [MANDATORY_CANDIDATE] Simulation comparison 必须明确 focal method 与 baselines/ablations 的角色。不要写 `Ours; baseline A; baseline B` 的分号串。
- [MANDATORY_CANDIDATE] 如果 comparison 项数 >= 3，优先 compact table / aligned list；若只有一个 baseline，则用一句自然对照关系。

## 15. Structured facts >= 3 行时必须使用真实 table/list structure

来源：P24。

- [MANDATORY_CANDIDATE] Dataset / cohort facts 超过约 3 个键值对时，使用 compact table、definition list、两列 aligned facts 或其它显式结构；禁止把 label/value 裸竖排成“像表格但不是表格”的文本堆。
- [MANDATORY_CANDIDATE] 数字结构必须易于横向扫描，并统一对齐单位与 thousands separator。

## 16. Question slide 使用统一 emphasis style，并可附一行必要 Background

来源：P21, P27。

- [MANDATORY_CANDIDATE] Research question / simulation question / supervisor question 应有统一 visual primitive：例如 left accent rule + bold Question，或轻量 callout；不能每页自由决定。
- [MANDATORY_CANDIDATE] Advisor/supervisor question 如果依赖前文技术背景，允许并鼓励一行 `Background`，前提是它确实帮助非本 topic 专家恢复必要事实。
- [MANDATORY_CANDIDATE] Background 不是答案；保持 1–2 行，不写内部实现细节。

## 17. References 必须主动利用纵向空间

来源：P29；v2 已提出，v3 重复。

- [MANDATORY_CANDIDATE] Reference 页字号由引用数量决定，不使用固定小字号。引用较少时必须放大字号/行距直到充分利用可用高度。
- [MANDATORY_CANDIDATE] 两栏 reference 顶部对齐、行距一致、列高尽量平衡；下半页大面积空白且文字仍小，直接判失败。

## 18. 下一步去重/提升规则

v4 方向确认后，逐条与以下现有规则对比：

- `research-presentations/TODO.md`
- `TODO_CAT_TRACE_V2_CANDIDATES_2026_08_27.md`
- active `SKILL.md`
- shared `visual-qa.md`
- archetypes / regression tests

处理优先级：

1. **v2 已有且 v3 重复失败**：优先提升为 hard QA / regression，不再新增重复文字；
2. v2 有但过于模糊：补可执行 layout primitive / threshold / rendered check；
3. v3 真正新增：进入 main TODO；
4. 只有 CAT-TRACE 才成立：留在项目 review，不进入通用 skill。
