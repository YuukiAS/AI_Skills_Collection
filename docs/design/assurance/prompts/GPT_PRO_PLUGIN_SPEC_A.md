# 设计 Design Assurance 与 Delivery Assurance 插件 0.1（独立设计者 A）

当前任务：把一套已经由用户认可的流程（Design Assurance 设计到冻结、Delivery Assurance 冻结到交付）设计成两个可以实现的插件。你是**独立设计者 A**：另有一位独立设计者在别的分支做同样的任务，你们互不参考；设计负责人（Claude）会对比两份设计，收敛成一份，再交 Codex 实现。

这是按这套流程本身做的第一次正式试跑，所以你的产出也要遵守它：交出一份完整的 Blueprint，并把需要设计负责人或用户回答的问题集中列出，不要自己猜。

## 工作位置

- 主仓库：`YuukiAS/AI_Skills_Collection`（**公开仓库**：不要写入私有项目的具体内容，只能写仓库名、分支和路径）。
- 只在这个分支工作：`design/assurance-plugins-0.1-pro-a`（从 `todo/assurance-plugins-20261109` 分出）。
- 产出目录：`docs/design/assurance/plugin-0.1-pro-a/`。
- **不要读** `design/assurance-plugins-0.1-pro-*` 中另一位设计者的分支。不要切到 main，不要 merge，不要开 PR，不要修改产出目录以外的文件。

## 先测试 GitHub 写入权限

在产出目录写 `WRITE_PROBE.md`，内容只写 `GPT Pro write probe passed.`。成功就继续；交付后删除它，不能删除就保留并在说明里注明。

## 先读这些

AI_Skills_Collection（本分支）：

1. `docs/design/assurance/ASSURANCE_PROCESS_V0_1_20261110.md`：**用户认可的流程 0.1，本任务的唯一依据。先完整读。** 其第 9 节是插件必须包含的部分，第 10 节是打包要求，第 11 节说明本任务在流程中的位置。
2. `docs/design/assurance/ASSURANCE_PROCESS_V3_20261110.png`：流程图（第四版在制作中，内容以文档为准）。
3. `docs/plugin-todos/design-assurance.md`、`docs/plugin-todos/delivery-assurance.md`、`docs/plugin-todos/assurance-sources-20261109.md`：历史材料汇总与来源索引，尤其是验收器归属的历史矛盾。
4. `AGENTS.md`：本仓库维护规则，正式插件改动要配合 workflow-core 与 ai-skills-core。
5. `plugins/codex/plugins/workflow-core/` 与 `skills/` 下一两个现有插件或技能：现有插件和 `SKILL.md` 的实际结构。

其他仓库（只读）：

- `YuukiAS/AI_Research_Toolkit`，分支 `research/delivery-anti-degradation-20261109`，`docs/research/delivery-anti-degradation-20261109/REPORT.md`：反降级调研，0.1 已吸收其结论。
- `YuukiAS/Asteria-Blueprint`，分支 `draft/blueprint-round7-20261107`：Blueprint 格式。读 `docs/planner-guide.md`、`docs/content-model.md`、`content/blueprint.schema.json`、`content/template.json`。**不要读任何 `test/` 开头的分支。**

路径若与实际不符，按目录实际内容找，并在 NOTES.md 记录。

## 要设计什么

两个插件，0.1 版，按流程文档第 9 节的部分逐一设计到能直接实现：

1. **状态文件：** 格式、字段、谁在什么时候写、冲突怎么办、放在被管理项目的哪里。
2. **调度：** 怎样根据状态与流程决定下一步发给哪个角色（档次、新开或沿用线程），怎样生成可直接复制给用户的提示词；Claude 担任负责人时自己执行的步骤怎样先告知用户。
3. **角色卡：** D1–D8、X1–X5 每张写全：任务、能读什么、不能读什么、产出写到哪、怎样算完成、回复格式。
4. **提示词规则与模板：** 自包含要求（仓库、分支、写入测试、先读什么、写回哪里、回复格式）。
5. **修订与告知：** 小修订与大改的判别规则（0.1 只给了原则，请细化成可判定的规则），事前事后告知模板。
6. **澄清（Grill Me）规则、冻结关卡 D5–D8 的通过标准、冻结合同格式**（在 Blueprint 上增加流程文档第 4 节的九项）。
7. **验收器规则、候选与证据记录格式、偏离申报模板、X1 签发清单。**
8. **衡量记录。**
9. **打包：** 两个插件在本仓库里的目录结构；规划端 `SKILL.md` 怎样同时被 Claude Code 与 GPT Work 直接使用；执行端 Codex 插件结构；ChatGPT 网页端以后另行打包时需要什么，只写说明不实现。
10. **最小可行范围：** 哪些部分 0.1 必须有，哪些可以留到 0.2。

## 规则

- 流程本身（角色、负责人、档次、验收器分级、退回条件、告知规则）已由用户认可，**不要改流程**；认为流程有问题的地方写进 QUESTIONS.md。
- 平台与工具的断言（例如 Claude Code 技能格式、Codex 插件结构）要有原始资料或仓库现有实现支持，记录出处；查不到就写成开放问题。
- 不要声称运行过任何脚本或检查器；没有本地终端就不要说运行过。

## 产出

在 `docs/design/assurance/plugin-0.1-pro-a/` 写：

- `blueprint.json`：两个插件的完整 Blueprint（按 Asteria-Blueprint 格式），每条分支落到真实实现、具体设计或开放问题。
- `SPEC.md`：自然中文的插件规格。先写结论（两个插件各由哪些部分组成、0.1 最小范围、最大风险），再按上面十项展开。
- `QUESTIONS.md`：需要设计负责人或用户回答的问题，每个写清为什么要问、选项和你的推荐；只列真正需要别人决定的。
- `NOTES.md`：实际读了哪些材料、查了哪些外部来源、哪些判断不确定。

## 回复格式

完成后不要输出机器状态块。直接用自然中文告诉用户：是否成功写入，写到了哪个分支和哪些文件，两个插件的组成与 0.1 最小范围，最大风险，以及 QUESTIONS.md 里最重要的几个问题。
