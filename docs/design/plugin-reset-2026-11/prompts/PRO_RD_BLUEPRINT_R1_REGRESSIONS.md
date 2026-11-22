# GPT Pro 任务：Reasoned Decision 0.1 —— 设计回归案例，并回应用户对待办的意见

## 背景

Reasoned Decision 是一个 ChatGPT 端插件，帮助模型在买东西、修故障、改配置这类具体问题上做出稳定、有依据的判断。0.1 版要解决 17 条待办（用户提出的真实失败）。我们做了一个 Blueprint 页面：每条待办对应到现有规则原文，Claude 给了初判（约束不足 / 适当 / 过度）和建议改法，用户已逐条表态。

现在卡在回归上：7 个回归只写了“检查什么规则”，没有场景、没有每轮 prompt，用户无法判断哪些该放进 0.1。你这一轮的主要任务是**把回归设计到用户能直接看懂、能直接拿去跑**的程度。本轮不改 skill 正文（下一轮再改）。

## 仓库

- `YuukiAS/AI_Skills_Collection`，分支 `impl/plugin-reset-v0.1`。只在下面“写回”列出的位置写文件；不改 `skills/`，不改其他分支，不开 PR。
- 先确认能写入；不能写就把全部结果贴在回复里，并说明无法写入。

## 必读

1. `AGENTS.md` 第 1.1.1 节（插件、规则和设计稿必须写人话）。**本任务所有产出都受它约束**：不得出现全大写下划线状态名（如 COMPLETED_ACTIONS）、给人看的英文短横线名称（如 state-owner-before-reset）、抽象名词堆砌（如“决定成功的属性”）。
2. `docs/design/plugin-reset-2026-11/blueprints/reasoned-decision/blueprint.yaml`：17 条待办（`todos`，含 `assessment` 初判）、现有规则（`rules`）、7 个回归（`regressions`）。
3. `docs/design/plugin-reset-2026-11/blueprints/reasoned-decision/decisions.yaml`：用户对每条待办的表态与备注（`todos.<id>.stance / note`）。
4. `docs/plugin-todos/reasoned-decision.md`：待办原文与用户原话。
5. 真实失败记录：`docs/design/reasoned-decision/evidence/` 下全部文件；`docs/design/plugin-reset-2026-11/regressions/` 下 `edge-revision`、`obsidian-existing-capability`、`keychron-object-evidence` 三个目录与 `CANDIDATES_2026-11-21.md`、`HOW_TO_TEST.md`。
6. 现有规则：`skills/core/reasoned-decision/` 下全部文件。
7. 回归案例文件格式：`docs/design/regression-runner/FORMAT_ZH.md`；现有空壳：`tools/regression-runner/examples/reasoned-decision/R1`–`R7/case.yaml`。

## 要做的

### 1. 回归设计（主任务）

对 R1–R7 逐个设计；如果你认为某几个应合并、某个不值得做、或缺一个必要的回归，直接提出并给理由（以 17 条待办都被至少一个回归覆盖为准）。每个回归写：

- **名称**：一句中文，说清在测什么（例如“先找状态存在哪，再考虑卸载重置”）。
- **场景**：用两三句话讲真实发生过的事（来自 evidence 文件），让没看过原对话的人也能懂。
- **每轮 prompt 原文**：用户在 ChatGPT 里实际要发的话。优先用 evidence 里用户的原话；需要补的地方写成自然的用户口吻，并在该轮注明“改写自 evidence 的哪一段”。不得编造与原案例矛盾的事实。多轮的写清每轮是新对话、接着上一轮，还是从第几轮分支。
- **附件与环境**：是否需要截图、文件、启用插件；模型。
- **怎么判通过**：3–5 条，每条是一个人读完对话就能判的句子，分“出现即失败”和“通过时必须有”。
- **覆盖的待办**：编号。
- **为什么值得放进 0.1**：一句话；以及如果只能选 3 个，你会选哪 3 个。

把每个回归按格式写进 `tools/regression-runner/examples/reasoned-decision/<R编号>/case.yaml`（覆盖空壳）。用 `python3 tools/regression-runner/check_case.py` 检查格式能过。

### 2. 回应用户对待办的意见

`decisions.yaml` 中用户选了“不同意”或“有疑问”的待办，逐条回应：

- **T11**：用户认为这主要是 Atlas 自己的问题，而 Reasoned Decision 通常解决单个具体问题。请判断它是否属于本插件，给出留下或移出（移到哪里）的理由。
- **T12**：用户认为“我说‘别折腾’时，只做剩下的那一个动作”这句不好。请给出更好的写法。
- **T14 与 T13、U1 与 T01**：用户要求去重。请给出合并后的一条需求文字。
- **T15**：用户赞同方向，但要求说人话。请给出改法。

### 3. 复核 Claude 的初判

对 17 条待办的 `assessment.status`（约束不足 / 约束适当 / 约束过度）和 `proposal`，只列出你不同意的，每条写依据。同意的不用写。

## 不要做的

- 不改 `skills/` 下任何文件。
- 不出现 AGENTS.md 1.1.1 禁止的写法；规则编号（如 SD-06）只在注明出处时出现，旁边配一句中文。
- 不写审计流水账。

## 写回

- `tools/regression-runner/examples/reasoned-decision/R*/case.yaml`（合并或新增回归时相应增删目录）；
- `docs/design/plugin-reset-2026-11/blueprints/reasoned-decision/PRO_R1_REVIEW.md`：开头不超过 8 行写最主要的结论（推荐 0.1 做哪几个回归），然后按上面 1–3 节。

commit 并 push 到 `impl/plugin-reset-v0.1`；冲突时先 pull 再 push，不改别人的文件。

## 回复

中文：改了哪些文件；推荐 0.1 做哪几个回归及一句理由；对 T11、T12 的结论。
