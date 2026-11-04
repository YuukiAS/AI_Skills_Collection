# DEPRECATED — DO NOT RUN

该提示词已于 2026-11-04 废弃。原因：它仍要求 Claude 重做大范围历史诊断，与 Phase A 已完成的 GPT Pro / Codex 证据压缩及“Claude 只用于高价值前端设计判断”的成本目标冲突。

当前唯一权威路线请读取：

`docs/design/frontend-design/ASTERIA_RECOVERY_FRONTEND_VNEXT_MASTER_PLAN_20261104.md`

Claude 的首次正式介入已移动到 Phase C：用户完成 Phase B 的最小历史资产与产品取舍确认后，Claude 只读取极小设计包并进行真实前端产品/视觉设计。

---

# Claude Stage 1 Final：Asteria 双项目独立视觉/产品诊断

RUN_ID=claude-stage1-final-static-evidence-20261104

你负责 Asteria Blueprint 与 Asteria Atlas 的 Stage 1 独立视觉/产品诊断。

本阶段不是重新设计，不是实现，不是打开真实宿主做操作，也不是复述 GPT Pro 的结论。你的价值在于：使用已经准备好的静态原始证据，独立判断过去哪里失败、哪些历史局部可能值得保留、哪些产品取舍仍需要用户决定，然后停止。

## 0. 唯一工作根目录

先读取：

`/Users/yuukias/Code/Asteria-Phase-A-Evidence/`

必须存在：
- `README.md`
- `MANIFEST.json`
- `SHA256SUMS.txt`
- `blueprint/contact-sheet.png`
- `blueprint/priority/`
- `blueprint/pdf-pages/`
- `atlas/contact-sheet.png`
- `atlas/priority/`
- `atlas/pdf-pages/`
- `pro/initial-pro-summary.md`
- `pro/gpt56-pro-summary.md`

如果这些核心文件明显缺失，先报告缺失，不要自行扩大搜索范围。

本地静态证据包已由 Codex 从固定历史归档生成。它只是读取便利层；历史事实权威仍是原始 PDF、固定 Git 提交和历史用户反馈。

## 1. 绝对禁止

本阶段禁止：

- 启动 Obsidian；
- 启动浏览器、Playwright、Chrome 或网页预览；
- 打开 Figma；
- 使用 Computer Use 操作 GUI；
- 为了“看得更完整”重新运行历史应用；
- 全仓递归扫描；
- 重跑 Deep Research；
- 生成完整 redesign；
- 写产品代码；
- 修改 Blueprint / Atlas 产品仓库；
- commit / push / merge；
- 安装 Skill 大全、MCP 大全或新的付费依赖；
- 把 GPT Pro 的建议直接当成用户决定；
- 把历史 `CURRENT_BEST`、`VISUAL_BASELINE`、`PARTIALLY_ADOPTED` 等标签自动升级成当前用户 `KEEP`。

不要为了展示勤奋而增加工具调用。静态证据已经准备好，优先直接读。

## 2. 先做视觉能力硬门

在任何诊断前：

1. 从 `blueprint/priority/` 任取一张界面图；
2. 直接读取图片像素；
3. 在本地过程记录中写出：
   - 3 个具体可见结构；
   - 1 个明确可见的文字片段；
   - 1 个空间/层级关系；
4. 再从 `atlas/priority/` 任取一张，做同样检查。

如果你无法可靠看到图片像素，只能得到文件名、元数据或抽取文本：

`STAGE1_STATUS = BLOCKED_VISION`

立即停止。不得用 PDF 纯文本或 GPT Pro 摘要冒充视觉审阅。

## 3. 独立诊断顺序：必须先于 GPT Pro 摘要

### Pass A：只看静态原始证据

先不要读取：

- `pro/initial-pro-summary.md`
- `pro/gpt56-pro-summary.md`

先读：

1. 两张 contact sheet；
2. Blueprint 17 个 priority 静态版本；
3. Atlas 9 个 priority 静态版本；
4. 两边各 8 张关键 PDF 页；
5. `MANIFEST.json` 中这些文件的来源、版本和历史 verdict。

关键 PDF 页是从原始 PDF 直接渲染的证据页，用于低成本首轮诊断。你不需要重新读完整 438 页。

如果某项判断必须依赖精确对话上下文，才允许按已知 PDF 页码额外提取相邻 1–3 页文字或渲染页；不得整本扫描。必须记录追加读取了哪些页以及为什么。

在这一阶段形成你自己的暂存结论：

- Blueprint 最有解释力的 3–5 个失败机制；
- Atlas 最有解释力的 3–5 个失败机制；
- 每个项目中你认为“可能值得保留”的具体局部；
- 明确已经失败、不值得复活的方向；
- 你认为仍未解决、会改变整体产品结构的问题。

这里使用：
- `CANDIDATE_KEEP`
- `CANDIDATE_REPAIR`
- `REJECT`
- `UNCERTAIN`

绝对不要使用 `ACCEPTED` 或代表用户确认的 `KEEP`。

### Pass B：再读两位 GPT Pro 摘要

完成并保存独立诊断后，才读取：

- `pro/initial-pro-summary.md`
- `pro/gpt56-pro-summary.md`

然后做一个很短的对照：

- `AGREE`：你的判断与 Pro 一致；
- `DISAGREE`：你认为 Pro 判断不成立；
- `PRO_ADDS_EVIDENCE`：Pro 给出了你之前没看到的证据；
- `NEEDS_SOURCE_CHECK`：双方冲突，必须回到具体 PDF 页或固定历史截图。

有冲突时只回源检查相关页，不重新读完整报告和完整 PDF。

## 4. 你必须特别判断的内容

### Blueprint

不要把它当“架构图网站”。

必须判断：

- 系统 / 对象 / 关系 / 机制 / 实现 binding / 证据 / 修订是否形成连续任务，而不是几个互不相干页面；
- 哪些机制应该使用状态、时序、数值循环、源码绑定等不同表达，而不是统一步骤卡；
- 历史上被局部认可的实现台到底哪些性质值得保留；
- 哪些版本因为过载失败，哪些因为模板化失败，哪些因为过度稀释失败；
- 当前历史候选中是否存在真正值得继承的视觉/交互语言，而不是默认重新开始。

已知历史决定不要重新问成全新问题：
- 多实现 binding；
- binding 可切换；
- 行号按需；
- 下钻仍保留全局上下文，非相关区域适度淡化；
- 彻底淘汰路线可下沉历史，仍影响当前系统的失败/阻塞关系不能被抹掉。

### Atlas

不要把它当“七分类目录”或普通 graph demo。

必须判断：

- 领域空间、研究问题、论文关系、筛选/比较、长文阅读各自应该承担什么职责；
- V05 空间社区/轻论文/稀疏关系到底哪些有价值，哪些只是当时像素和布局缺陷；
- V06/V07 原生工程价值与视觉价值必须分开；
- V08 Astra 的信息架构/语义缩放哪些值得保留，为什么其视觉仍被否决；
- V10 当前候选有什么真实进步、还有什么根本问题；
- seed 覆盖和全领域规模必须诚实区分。

已知历史决定不要重新问：
- Atlas 是科研关系地图，不是 taxonomy 海报；
- 20 篇只是种子，不代表整个领域；
- 论文层关系有必要，但不是所有关系都必须画成边；
- Obsidian 是最终真实宿主，但本阶段不打开它。

## 5. 这轮 Claude 的核心交付不是“新设计”，而是 Human Review Pack

你的最终输出必须先帮助用户高效审历史，而不是让用户重新看 48 个版本。

### A. Blueprint Review Shortlist

从 36 个历史版本中，只挑出你认为**最值得用户亲自重新看的 5–8 个版本或局部**。

每项必须说明：
- version id；
- 具体看哪张图/哪个局部；
- 你认为可能保留什么；
- 风险/为什么不能整版继承；
- 你的建议标签：`CANDIDATE_KEEP / CANDIDATE_REPAIR / UNCERTAIN`。

如果多个版本只是同一思路的重复，不要都塞给用户。

### B. Atlas Review Shortlist

同样只挑 4–6 个最值得用户亲自看的版本或局部。

### C. Cross-product Failure Diagnosis

用最少但最有解释力的机制解释为什么过去会失败。不要再写“更好的层级、更好的留白、更好的字体”这种空话。

重点区分：
- 产品判断错；
- 视觉表达错；
- 局部反馈被扩大；
- 正确资产丢失；
- 工程 PASS 保护错误定义；
- 真实宿主与静态设计脱节。

### D. Pending User Decisions

最后只提出**真正需要用户决定的问题**。

上限 6 个，能 3–4 个解决就不要问 6 个。

每个问题必须有：
1. 具体历史分歧；
2. 你看到的候选证据；
3. 你自己的推荐；
4. 用户到底需要选择什么。

不要问：
- 字号多少；
- 卡片圆角多少；
- React Flow 还是别的库；
- 工程实现方式；
- 用户已经明确回答过的问题。

如果某个问题你基于证据已经可以自己解决，就自己做推荐，不要甩回用户。

## 6. Skill / 工具判断

你可以读取本机已经存在的 Anthropic 官方 `frontend-design` Skill，判断它对 Stage 2 是否值得使用。

本阶段只回答：
- Stage 2 是否建议启用；
- 它能解决哪类已观察到的问题；
- 哪些问题它解决不了。

不要安装新工具。

不要因为存在 Skill 就把历史问题归结成“以前没用 Skill”。

## 7. 输出与保存

在：

`/Users/yuukias/Code/Asteria-Phase-A-Evidence/claude-stage1/`

保存：

- `INDEPENDENT_DIAGNOSIS_ZH.md`
- `HUMAN_REVIEW_SHORTLIST_ZH.md`
- `PENDING_USER_DECISIONS_ZH.md`
- `STAGE1_SUMMARY_ZH.md`

不要创建更多文件。

`STAGE1_SUMMARY_ZH.md` 必须非常短，包含：

- Stage 1 是否通过视觉能力门；
- Blueprint shortlist 数量；
- Atlas shortlist 数量；
- 你与两位 Pro 最重要的一致/分歧；
- 需要用户回答的问题数量；
- 是否建议 Stage 2 使用官方 frontend-design Skill；
- 明确写：`FULL_REDESIGN_STARTED = NO`。

## 8. 停止点

输出 shortlist 和少量用户问题后立即停止。

本轮不能：
- 进入 Stage 2；
- 生成新界面；
- 做完整视觉方向；
- 修改产品；
- 让 Codex 实现；
- 自行决定 Blueprint / Atlas 哪个先做。

最终只把 `STAGE1_SUMMARY_ZH.md` 的内容和 Pending User Decisions 展示给用户，并告诉用户 shortlist 文件在哪里。

等待用户审阅与回答。
