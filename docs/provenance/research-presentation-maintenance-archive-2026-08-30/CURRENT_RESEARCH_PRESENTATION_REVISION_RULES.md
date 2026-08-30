# Current research-presentation revision rules

本文件是科研 PPT 在多轮人工返修期间的**当前累计规则入口**。在这些规则正式合并进 presentation plugin / shared QA 之前，真实项目的下一轮 Codex 执行必须先读取这里，不能只靠当前项目 prompt 重新描述一遍。

它不是某个 CAT-TRACE 页面清单；只保留已经从真实返修中确认、可跨项目复用的规则。项目自己的科学事实和逐页决定仍应留在项目 task / revision ledger 中。

## 0. 每轮执行前必须同步规则仓库

真实科研 PPT 的 Codex task 在修改任何 slide 之前必须：

1. 在当前机器找到本地 `YuukiAS/AI_Skills_Collection` checkout，并核对 `origin` 指向该仓库；
2. `git pull --ff-only`；
3. 记录本次读取的 AI_Skills_Collection commit SHA；
4. 至少读取：
   - 本文件；
   - `research-presentations/SKILL.md`；
   - `research-presentations/TODO.md`；
   - 最近与当前 deck 类型有关的 confirmed / mandatory candidate rules；
   - 英文科研 slide 还必须读取 `skills/writing/core/scientific-prose/SKILL.md`；
5. 在执行记录中建立 `inherited_rule_checklist`：`rule -> affected slide/archetype -> implementation -> rendered verification`。

仅写“已阅读规则”不算完成。规则必须能在最终 render 上验收。

优先级：**用户本轮明确要求 > 当前项目已确认约束 > 本文件 > active presentation skill > 旧候选记录。**

## 1. 重复失败升级为硬性失败

如果同一类错误已经在前两轮被指出，下一轮再次出现时直接判 `REVISE/BLOCKED`，不再视为审美讨论。当前已经达到这一等级的典型错误包括：

- visible text / box / edge overlay；
- diagram 箭头过短、过小、穿字、交叉、随机斜连；
- 核心内容很小而页面仍有大面积空白；
- 主图在投影距离不可读；
- audience-facing slide 出现 repo path、`audit`、`validation audit`、`manuscript draft`、task/result status、random seed 等内部记录语言；
- 用户已确认的格式在相邻同类页面上不一致。

LaTeX 无 overfull warning、文件成功编译、generator 自报“visual check passed”都不能覆盖这些失败。

## 2. 纵向空间必须真正利用

不要固定沿用某个小字号模板。如果页面下半部仍有明显连续空白，而核心公式、问题、references、table 或图仍然偏小，应优先：

- 放大核心对象；
- 增加正常行距 / block 间距；
- 增大主图；
- 删除低价值辅助对象；
- 必要时拆页。

References、discussion、theory、two-column model、figure-heavy slide 都适用。少量 references 必须主动放大字号和行距。

## 3. 首屏公式必须是真正核心对象

页面首行或第一视觉中心的 display math 只允许用于：主模型、主 estimand、核心 identity、正式结果、真正的 derivation step。

以下对象默认不能居中占据首屏：sample-size grid、parameter range、rank list、working-set size、短 notation definition。

新的 random quantity / estimand / formal result 在居中出现前，必须先让听众知道：**它是什么现实或统计对象，以及为什么关心它。**

## 4. 数学排版用固定选择逻辑

- 连续推导 / 多个等式：`align`；
- 同一左侧对象下互斥分支：`cases`；
- 短定义 / design settings：inline、left-aligned definition list 或 compact table；
- 公式项与语义标签需要一一映射时可用 `underbrace` 或 semantic coloring；
- 极限统一使用标准数学记法，例如 `\lim_{p\to\infty}`，不把 `as p grows` 之类普通英语塞进 operator。

## 5. 两栏只用于真正 peer-level 对象

Two-column 只在两个对象需要并行比较时使用。连续推导、因果链、模型流程优先单栏纵向。

两栏必须 top-aligned、视觉高度接近、heading / padding /字号一致。若下面还有 full-width shared object，必须预留独立第三块区域和足够 whitespace；正常字号放不下就拆页。

## 6. Diagram 必须先做拓扑，再做美化

顺序固定：

1. semantic graph；
2. reading direction；
3. node levels / columns；
4. legal edge paths；
5. anchors / ports；
6. box size；
7. arrow style；
8. color / polish。

禁止先摆 box 再用斜线补连。

主 diagram 应成为页面视觉中心。主箭头必须有足够可见线段、明确 arrowhead 和 node clearance；不得 crossing、overlay、穿字或随机连到矩形角。理解图所需的 set difference / condition / definition 应整合进 node、brace、annotation 或紧邻 caption，不要在图外悬一条补救公式。

每个 diagram 页必须单页高分辨率检查；contact sheet 只用于总览。

## 7. Figure-heavy slide 的主图必须可投影阅读

主图如果需要在最终 PDF 上额外放大才能看清 axis、legend、panel title、点线关系、地图点或照片主体，则直接 fail。

优先扩大主图，减少辅助图和正文，而不是把正文缩成 `scriptsize`。辅助图必须有紧邻的 caption / label。

## 8. 术语和小标题有统一层级

- Slide title / table header / Dataset / Simulation / Question 等默认 sentence case；
- 新领域术语 first use 使用稳定模板：术语本体强调，正式全称次一级，解释保持普通正文；
- 同一 deck 的 `Question`, `Example`, `Design`, `Metrics`, `Comparison`, `Data`, `Background` 只保留一套样式；
- supporting glossary 不应在页面底部突然成为视觉主项。

如果一个术语需要两三句才能解释给目标听众，优先在首次使用前单独建立 background context，而不是让后页反复补定义。

## 9. Metrics 使用方向符号并解释用途

优先 compact table / aligned list，例如：

- `RMSE ↓`；
- `PR-AUC ↑`；
- `Coverage → 95%` / `→ nominal`。

不要另设 `direction = lower/higher` 一列。多个同 family metrics 可合并，如 `Discovery RMSE ↓ (total / catalogue / open tail)`。

方向符号不能替代解释：每个 metric 仍需用很短的文字说明它检查什么统计性质。

## 10. Simulation 同类页必须格式闭合

若一组 simulation 都声称“每个回答一个论文问题”，则每页都必须有 Question；Design / Metrics / Baselines 的顺序和样式必须统一，除非科学对象确实不同。

Comparison 中要区分 focal method 与 baselines / ablations，不写 `ours; A; B` 的分号串。

## 11. Theory 在汇报里按“模型解决什么”组织，不按 theorem 数量组织

不要为了显得理论多，把 corollary / definition 强行升级为 theorem；也不要因为 manuscript 里 formal type 不同，就把 slide 标题机械写成 `Theorem / Corollary / Proposition`。

主 deck 先问：**proposed model 正式解决了 closest existing methods 不能同时解决的什么问题？** 然后选择能支撑这些新增能力的 formal guarantees。

推荐 presentation framing：

- slide title 直接写科学保证 / 新能力，例如 `Group marks preserve open-tail richness calibration`；
- formal theorem/corollary/proposition 的分类和 manuscript 编号是次要信息，可留 source note / speaker note，除非编号本身对现场讨论重要；
- 不能用“结果数量”代替理论价值；
- 一个简单 estimand decomposition 不包装成深 theorem；
- 每个 formal guarantee 必须明确 closest baseline 做不到什么，以及该保证为什么对 proposed model 必要。

## 12. Discussion 面向“领域专家但不熟悉当前 topic”的听众

Question block 可以使用一行 `Background` 恢复必要上下文。Background 只放 1–2 行必要事实，不给答案、不写内部实现状态。

A/B/C 选项必须统一左对齐、同一字号和间距。页面问题较少时应主动放大字号并使用纵向空间。

## 13. Internal-language hard ban

Audience-facing slide 默认禁止：

- `audit`, `validation audit`, `source audit`；
- `manuscript draft`；
- repo/file/task/result path；
- `summary_note.md` 等文件名；
- run status / internal phase / internal role；
- random seed、hash、commit 等实现信息，除非其本身就是科学内容。

数据来源写成人能读的 citation / source phrase。内部证据路径只放 execution result / speaker notes。

交付前同时扫描 source 和 compiled PDF text，并做人工同义检查。

## 14. 交付前必须做“规则继承验收”

最终交付必须至少有：

- full-deck render；
- contact sheet；
- diagram / figure-heavy / theory / discussion / references 等关键页单页高分辨率 render；
- `inherited_rule_checklist` 每条 PASS/FAIL；
- accepted-element regression check；
- source + PDF visible-text language scan；
- 对重复失败项的专门 regression 结论。

任何一项 FAIL 都不能自报“完成”。
