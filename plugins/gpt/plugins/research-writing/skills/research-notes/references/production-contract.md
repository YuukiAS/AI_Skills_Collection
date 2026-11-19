# GPT 到 Codex 的制作合同

本合同适用于 `research-notes`、`research-story` 和 `student-materials` 的 Codex 制作入口。内容判断、读者判断、科研或教学论证和文字写作由 GPT 完成；Codex 接收确定正文，只负责渲染、机械检查、发布和回读。

## 必需输入

开始制作前取得以下材料：

1. 已填写的 `handoff.template.json`，其中 `candidate_identity.source` 指向完整正文。
2. `reader`、`reader_task`、`source_refs`、`content_authority`、`edit_scope` 和 `delivery_targets`。
3. 需要保护的 `required_meanings`、`required_relations`、`exact_items`、`rejected_content` 和 `semantic_blocks`。
4. GPT 已完成的 Content Selection 内容计划，至少对应 `CS-03`～`CS-07`；GPT 已完成的 Clear Writing 成稿与保真处理，至少对应 `CW-03`～`CW-08` 及任务实际使用的 `LF-*`、`FI-*`。
5. 本次唯一的执行证据文件位置。跨端任务在同一文件中继续记录，避免为每个制作步骤另建报告。

缺少完整正文、目标文件、允许改动范围或内容权威时，返回缺失字段及其影响。涉及内容删留、研究结论、教学要求、措辞或语义分组的决定，交回 GPT。

## Codex 制作步骤

**RA-12｜核对正文交接。** 确认正文身份、候选或接受状态、允许改动和目标位置。已有批准只覆盖其绑定的正文与范围。

**RA-13｜渲染与机械检查。**

- Markdown：保持确定正文，检查编码、结构、数学节点、表格、资源链接和目标平台回读。
- 正式 PDF：使用约定的 `render-chinese-math-pdf` 路线，取得全部页面；依赖缺失时报告准确缺口并保留正文。
- ZIP：按显式组件清单打包，核对每个组件与源文件一致；面向学生的包与执行证据分开。
- 幻灯片：继续运行通用 deck 验收器及其硬规则。本合同中针对文档 PDF 的留白与密度处理不改变 deck 验收标准。
- 运行 `shared/scripts/check_research_artifact.py`，保存逐项结果、已观察对象、未观察对象和返回码。程序结果只说明实际测得的机械性质。

**RA-14｜发布与回读。** 仅向 `delivery_targets` 中已授权的位置写入。发布后回读实际文件；源码回读和页面呈现分别记录。无法取得页面时，将该表面标为 `未观察`。

**RA-15｜追加机械证据。** 在执行证据文件中记录渲染器、检查结果、最终文件、页码或路径、发布提交和回读位置。保持 GPT 已写入的规则证据，不用机械通过替代内容判断。

## 返回给 GPT

交回以下对象：

- 最终文件及其身份；
- 完整可见文字和全部目标页面；
- `mechanical_results`、`observed_surfaces`、`unobserved_surfaces` 与具体 findings；
- 发布与回读结果；
- 已追加机械位置的执行证据文件。

制作中发现正文无法按既定约束呈现时，指出文件、页面、冲突约束和可复现证据，由 GPT 决定内容或语义布局。Codex 可以修复路径、编码、渲染参数、文件清单和其他机械问题。
