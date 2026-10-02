# Project Instructions Editor — Readability Design History

Date: 2026-10-01  
Status: PLANNING_ONLY  
Candidate future standalone Skill: `project-instructions-editor`

This document records the recent design evolution that led from a general ChatGPT readability problem to a candidate reusable Project-instruction editing capability. It is design evidence only.

**No production Skill, Plugin, profile, release, registry entry, README card, Marketplace package, or installation route is authorized or created by this document.**

## 1. Real problem

The user repeatedly observed that technically correct ChatGPT answers became difficult to read because Project-local instructions, engineering vocabulary, logs, status fields, and mathematical formatting leaked directly into the user-facing answer.

Two representative failures were preserved outside the public repository as private user evidence:

- an AI Research Stack answer with many ordinary English engineering phrases such as `source-of-truth`, `specialist routing`, `fallback`, `candidate consumption`, and design-document-style status language;
- a statistics explanation where ordinary statistical terms remained in English, simple parameter values and ratios were promoted to block equations, and the answer fragmented into many short lines.

The reusable problem is not “make everything Chinese.” It is:

> preserve exact machine identifiers and formal names when they matter, while transforming ordinary technical control language into a readable user-facing explanation.

## 2. v1 — stronger account-level readability rules

The first approach strengthened global personalization around four recurring failures:

1. unnecessary English in Chinese explanatory prose;
2. sentence-per-line and status-field fragmentation;
3. block-equation overuse for simple values and one-step relationships;
4. project/log/code language being copied directly into the explanation.

This was directionally correct but structurally incomplete. ChatGPT Project instructions can override global custom instructions, so account-level wording alone cannot guarantee Project-thread behavior.

## 3. v2 — two-layer architecture

The second design introduced two layers:

- account-level personalization as the complete user-reading contract;
- a short self-contained Project bridge for Projects that already have Project instructions.

The bridge repeated only the user-reading essentials:

- ordinary translatable technical terms should be Chinese;
- exact products, code, paths, fields, repository names, errors, and other machine identifiers may stay exact;
- prose should use natural paragraphs and only necessary structure;
- simple mathematics stays inline;
- machine-readable deliverables remain exact.

This version also removed mechanical rules such as English-word counts, fixed paragraph counts, and fixed block-equation counts.

## 4. v3 — machine-deliverable boundary and semantic English exception

Critic review exposed two remaining boundary problems.

First, readability rules must not rewrite required machine deliverables such as:

```text
RESULT=PASS
FINAL_HEAD=...
PUSHED=YES
```

v3 therefore separated:

- user-facing explanatory prose;
- exact machine deliverables required for copy, execution, parsing, or protocol compliance.

Second, “original terminology” was too broad an English exception. v3 narrowed the exception: an original term is retained only when the current answer genuinely needs exact source comparison, disambiguation, or retrieval/lookup. “The source is English” is not enough.

v3 also clarified that task recap dimensions such as background, goal, action, result, gap, and next step are logical dimensions, not mandatory headings or a fixed seven-part template.

Independent review returned PASS and recommended real Project regression rather than further global-rule design.

## 5. Real AI Research Stack regression

The AI Research Stack Project was used as the first real regression target.

A new Section 0 was added to its Project instructions as a user-reading bridge. The rest of the governance instructions were initially left semantically unchanged.

The next answer improved materially:

- the opening difference between `workflow-core 0.4` and planned `0.5` was explained in natural Chinese;
- many concepts became Chinese: core responsibility, specialist capability, environment judgment, alternate route, automatic downgrade, evidence strength, artifact identity, authorization boundary;
- simple prose became more continuous.

However, ordinary English leakage still remained, including:

- `source-of-truth`
- `specialist routing`
- `shell/PATH`
- `command not found`
- `fallback`
- “Bridge routing”

At the same time, retaining exact names such as `workflow-core 0.4/0.5`, Codex, Python, R, Node, XeLaTeX, Chromium, Bridge Kit, Reviewed Handoff, W1–W5, and `PATH` was reasonable.

This real regression showed that the bridge is effective but not sufficient by itself.

## 6. v4 — current Planner direction

The current Planner hypothesis is that the remaining leakage has a source-side cause:

- Section 0 requests a Chinese user-reading layer;
- Sections 1–18 still contain many ordinary English engineering concepts;
- those Project instructions are strong local context and continue to provide English lexical patterns.

The proposed architecture is therefore three-layered:

### A. User-reading layer

The Project's leading output section defines how the final explanatory answer should read.

Before sending the answer, explanatory prose should be rewritten into this layer rather than directly reusing wording from Project rules, logs, tables, or sources.

### B. Governance layer

The existing Project governance remains semantically unchanged, but ordinary English engineering/management/process vocabulary may be normalized into Chinese where exact English is not needed for lookup or execution.

This is a language-only refactor, not a governance redesign.

### C. Exact machine layer

Formal names and exact identifiers remain unchanged when precision matters, including repository/file names, paths, commands, fields, state values, fixed machine blocks, formal role/mechanism names, and versioned product/Skill names.

## 7. Important non-goals

The current work does **not** authorize:

- creating the `project-instructions-editor` Skill;
- adding a Skill directory;
- adding `agents/openai.yaml` or trigger evals;
- adding README standalone-Skill cards;
- changing repository or standalone-Skill versions;
- changing Marketplace topology;
- publishing or installing anything;
- introducing an English-word counter, paragraph counter, formula counter, linter service, daemon, state machine, or external checker.

The next step is independent Critic review of the current Planner architecture. A later user instruction will decide when the standalone Skill itself should be designed or implemented.

## 8. Related source

Maintenance inbox:

`docs/skill-todos/project-instructions-editor.md`

Current Planner proposal:

`docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_V4_PLANNER_PROPOSAL_2026-10-01.md`


## 9. v4.1 后的真实 Project 回归：从“继续加规则”转向“记录边界”

v4.1 架构通过后，AI Research Stack Project 使用同一个高风险问题反复做真实回归：比较 `workflow-core 0.4` 与规划中的 `0.5` 对实际使用的差异。

这些回归进一步确认：

- 用户阅读层能明显改善自然段、结论顺序和部分普通术语中文化；
- source-heavy 技术问答仍可能把 repo / design proposal 中的描述性英文标签带入最终解释；
- 模型为了检索或核对英文 source 而需要原文，不等于用户最终需要看到该原文；
- 精确身份 / 机器字符串与来源中的描述性标签必须分开；
- 继续围绕单个失败样本追加同义规则会迅速出现边际收益下降，并增加 Project-setting 字符预算压力。

更重要的是，本轮暴露了一个编辑流程问题：repo 中保存的 Candidate / Reference 可能落后于用户实际 Project Settings。未来编辑不能把旧 repo candidate 当 live truth；必须先取得真实 setting，再结合 Project 历史 thread 和 canonical repo 做 bounded edit。

详细经验见：

`docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_REAL_PROJECT_REGRESSION_LESSONS_2026-10-01.md`

## 10. 对未来 standalone Skill 的含义

中文可读性只是 `project-instructions-editor` 的一个真实验收维度，不应把未来 Skill 设计成中文润色器。

未来 Planner 应从更完整的 Project-instruction 生命周期出发：真实 live setting、Project 历史决定、repo 当前事实源、有限字符预算、多 scope 平衡、稳定 locator、exact identifier、bounded edit、语义保真和可审差异。

本轮明确留下的反模式也属于设计证据：

- 不用禁词表或大型中英替换词典代替语义判断；
- 不用英文数量/比例、固定段落/标题/公式数量等表面阈值；
- 不靠不断追加“禁止 XX”把 Project setting 变成规则墙；
- 不围绕单一 regression prompt 过拟合；
- 不因为某一版完整候选“看起来更干净”就覆盖用户 live setting 中后来新增且已接受的规则。

当前用户决定是暂时停止继续微调 AI Research Stack Project setting，把这些经验交给下一轮 Planner。下一轮仍只允许继续设计，standalone Skill implementation 需要新的明确授权。
