# GPT Pro 设计任务 2：content-selection 与 clear-writing 两个插件 v0.1（合并设计）

## 为什么两个一起设计
它们是两道平级、先后的工序，都会被 research-authoring、presentations 等产出类插件调用：
- **content-selection**（原 artifact-content-design）：管"这位读者需要哪些内容、按什么顺序、哪些不该出现"。适用于文档、幻灯片、网站/软件界面、Blueprint 这类给人看的作品。v0.1 先一个 skill，必要时再拆。**已确认职责同时包括制作前内容准入，以及真实渲染后的整件作品复审**：单个元素各自合理，不代表组合后的焦点、层级、留白和冗余仍合理。
- **clear-writing**（原 writing-style 插件）：内容定下以后，管"怎么讲清楚"：先说结论、讲人话、对中文读者用中文、不绕。

两者分界必须在本次一起定，否则会重叠打架。`COVERAGE_*` 里的"边界条目"表是分界的直接证据。

## 用户已表态
- 两者都做成**独立插件、同一层级**；都要能被其他插件调用，也允许用户直接点名使用。content-selection 不再按 standalone Skill 方向设计。
- clear-writing 可以**整体推翻重来**。现有 6 个子 skill（response-clarity、zh、sci、scientific-rewrite、fidelity、product-ui-copy）是按语言/文体切的，用户每次都还要提醒"说人话"。请重新判断该怎么切（例如按读者场景），并说明现有 6 个各自去向。"保住已确认内容不被改坏"这一要求必须在新架构里有明确归属。
- 以后 presentations 插件会在 GPT 端调用 content-selection 决定每页放什么，在 Codex 端跑通用验收器；请让接口能支持这种用法（只需定接口，不设计 presentations 本身）。

## 本任务读取
- `docs/design/plugin-reset-2026-11/COVERAGE_content-selection.md`、`COVERAGE_clear-writing.md`（主输入）
- `TRIAGE_artifact-content-design.md`、`TRIAGE_writing-style.md`、`CROSS_PLUGIN_MAP.md`
- 现有实现：`plugins/codex/plugins/writing-style/`；早期相关设计（可选）：分支 `design/reader-facing-artifact-quality-20261024`。

## 写回位置
`docs/design/plugin-reset-2026-11/designs/CONTENT_SELECTION_AND_CLEAR_WRITING_DESIGN_V0_1.md`

## 补充要求
在设计书第 2 节后加一小节"**分界**"：用三五个真实边界条目举例，说明各归哪个插件、交接时传什么。第 4 节全覆盖表两个插件分开列。

content-selection 的设计必须同时说明两次介入：**制作前**如何做内容准入、排序和可见层级；**真实成品出来后**如何对整件作品复审，并把“删内容后布局失衡、组合后重复、内部过程泄漏、整体过度解释”等问题送回产物 owner。复审必须看实际消费对象，不能用字数、禁词、密度或“已经调用 skill”代替。

## 仓库与读取方式
- 仓库：`YuukiAS/AI_Skills_Collection`（公开），分支 `design/plugin-reset-triage-20261119`。
- 设计输入都在 `docs/design/plugin-reset-2026-11/`：`COVERAGE_<名>.md` 是**逐条全覆盖**索引（每条待办一行，已标簇、GPT/Codex 端、是否需要检查），`TRIAGE_<名>.md` 是按簇概括和用户原话式的不满，`CROSS_PLUGIN_MAP.md` 是跨插件重复根因。**请以这些汇总为准，不要逐条重读原始待办**；只有当某行信息不够判断时，再按行号回查原文件。
- 现有实现在 `plugins/codex/plugins/<插件>/`；两端如何安装和加载见仓库 `README.md` 与 `profiles/`。

## 背景
用户长期使用 GPT（网页/Pro）和 Codex。两者最大的共同问题：不考虑读者，该讲的不讲、讲不清，堆审计和后台记录，小修时把已确认的好内容改坏。用户要的是**尽快有一个能用的 v0.1**，之后版本号慢慢往上加；**允许推翻现有实现重做**，不必追求一次完美。

## 设计必须包含（按此顺序，作为一份 Markdown 设计书）
1. **一页结论**：用户读完这一页就知道插件长什么样、v0.1 做什么不做什么。
2. **架构**：插件 → 拆成哪几个 skill；每个 skill 管什么、何时被用到（用户点名、别的插件调用、还是自动）；skill 之间、插件之间谁调用谁。
3. **GPT 端与 Codex 端分工**：不要预设“GPT 只做内容、Codex 只做渲染”。对每个 skill 判断 GPT 端、Codex 端是否都需要；分别写清正常入口、实际职责、能观察到的证据，以及两端怎样交接。允许 GPT-only、Codex-only 或两端职责不同；没有真实价值的一端直接写“无”，不要为了对称硬造。
4. **全覆盖表**：COVERAGE 里的每个簇 → 由哪个 skill / 哪条规则处理；凡本轮不处理的条目，按行号列出并给一句理由。不得有既未处理也未说明的簇。
5. **必要验收检查**：v0.1 只要真正必要的，不超过 6 项。每项：检查什么｜机械可判还是需模型/人判｜覆盖哪些条目｜在哪一端运行。其余候选检查列入"以后版本"。
6. **现有实现怎么处理**：每个现有 skill/脚本：保留、并入、改写或删除，各一句理由。
7. **v0.1 与之后版本**：v0.1 范围；0.2、0.3 大致补什么。
8. **需要用户裁决的问题**：不超过 6 个，每个给选项、各自后果和你的推荐。

## 写这份设计书本身的规则（它的读者是用户本人）
- 中文；英文只保留确切名称。先说结论，再说理由。
- 正文只写用户需要知道和决定的东西；证据、行号、推导放附录。
- 不写"不是 X 而是 Y"式套话、口号、免责尾巴；不要整页"已核对/已检查"类审计说明。

## 回复格式
直接回复完整设计书 Markdown（一个文件）。用户会把它保存到上面写明的路径并提交。
