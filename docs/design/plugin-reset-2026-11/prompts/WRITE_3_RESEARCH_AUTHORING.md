# GPT 撰写任务 3：research-writing（Research Authoring）v0.1 的技能文字

按你写的设计书 `docs/design/plugin-reset-2026-11/designs/RESEARCH_AUTHORING_DESIGN_V0_1.md`（开头"用户裁决"段优先：命名 research-paper / research-citations，安装标识保留 research-writing，deck 仍按通用 deck 验收器硬规则）填写占位：
- `skills/writing/research/` 下 `research-notes`、`research-story`、`student-materials` 的 SKILL.md、`codex-entry.md` 与 references；
- `skills/writing/research/shared/` 下的说明文件、`compatibility/paper.md` 与 `compatibility/litcite.md`（只写一两句转接说明）、`research-reporting/SKILL.md` 的转接说明；
- `shared/scripts/check_research_artifact.py` 中的占位**只填面向人的提示文字**，不改任何代码逻辑；
- 回归案例 `notes-formula-explanation`、`supervisor-story`、`student-brief`、`accepted-material-minor-edit` 的期望行为。
`research-paper`、`research-citations` 的正文不要动。`codex-entry.md` 里 Codex 只出现渲染、机械检查、发布、回读；内容判断与写作全部在 GPT 端，调用 content-selection 与 clear-writing（已在本分支，按其规则编号引用）。

## 仓库与分支
- 仓库 `YuukiAS/AI_Skills_Collection`，分支 **`impl/plugin-reset-v0.1`**（Codex 已搭好机械骨架，提交 365d2319）。直接在该分支上写入、commit、push。
- 凡是需要文字的地方，骨架里都有占位 `<!-- GPT-WRITES: ... -->`，注明该写什么、对应设计书哪一节。用 `git grep -n "GPT-WRITES"` 列出全部占位。
- **只改源文件**：`skills/` 下的源技能树和 `docs/design/plugin-reset-2026-11/regressions/` 下的回归案例。不要直接修改 `registry.json`、`docs/SKILL_CATALOG.md`、`plugins/`、`profiles/` 等生成/投影层；Codex 之后统一重新生成。`plugins/` 与 `profiles/` 下的副本由生成器机械产出，不要手改，Codex 之后会重新生成。
- 不要改动骨架的目录结构、清单字段、脚本和测试；若你认为结构有问题，写在回复里，不要自行改结构。

## 写作要求
- SKILL.md 是给模型执行用的：短、可执行、可寻址。常驻部分只放最核心的规则，细节放 references/，在对应步骤处按需读取。每条规则有稳定编号，供执行证据文件引用。
- 每个技能都必须写明**执行证据**要求（用户裁决）：被调用时，GPT 回答附上一个证据文件，按骨架里的证据模板逐条写"规则编号 → 成品原句或位置"，有改写附改前→改后；未调用则不附任何东西。本插件没有 Codex 端。
- 不写"not X but Y / X, not Y / 不是…而是…"句式，不写口号和免责尾巴。中文为主，英文只保留确切名称。
- 旧技能的转接文件只写一两句：该入口已并入哪个新技能、去哪里读。
- 回归案例 `case.yaml` 的"期望行为"写成可判断的具体行为（应做什么、出现什么算失败），依据设计书第 5 节和开头裁决段。

## 完成后
commit 并 push 到 `impl/plugin-reset-v0.1`，回复：改了哪些文件、还剩哪些占位没填及原因、对骨架结构的意见（如有）。
