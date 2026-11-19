---
name: judgment-integrity
description: "在比较、推荐、最终确认或新证据出现时，核对对象、证据和跨轮状态，给出稳定且可纠正的明确判断。"
status: active
provenance: user-authored
trusted: false
requires_network: false
writes_files: true
executes_code: false
secrets_needed: null
last_reviewed: 2026-11-19
profile_tags: null
recommended_scope: project
icon_small: assets/app-facing.svg
icon_large: assets/app-facing.svg
---
# Judgment Integrity

用于产品选择、方案比较、最终确认、故障复发及新证据后的重新判断。开始前读取 [task-state-contract.md](references/task-state-contract.md)，恢复当前问题、约束、事实、完成状态、淘汰路线和关键未知。

## 执行规则

- **JI-01 当前对象。** 先确认具体对象、型号或变体、环境、时点及成功标准。缺失事实优先用当前网页、连接器和其他可用工具取得；确需用户权限或现场观测时，只请求会改变选择的最小信息。
- **JI-02 决定变量。** 先列出真正决定成功的属性，再选择能直接观察这些属性的证据形式。类别标签、重量、名称、兼容列表和通用素材只能在其相关性得到说明后参与判断。
- **JI-03 先淘汰再比较。** 淘汰违反硬约束、被当前事实否定、适用范围缺乏依据或没有新增价值的路线。对剩余路线比较效果、额外假设、权限、中断、维护、回退、复杂度及用户时间和信任成本。
- **JI-04 结论强度。** 按证据区分候选、有条件的首选、足以行动的推荐和经过真实验证的长期默认方案。决定性未知仍开放时，给出有条件的首选及最小补证动作。
- **JI-05 改判依据。** 改变正式推荐前，写清上一轮推荐、关键前提、新增或纠正的事实、受影响的变量与候选，以及排序怎样变化。新信息没有实质影响时延续原推荐；有影响时只更新相关部分。
- **JI-06 淘汰路线与复发。** 已淘汰路线只有在新证据解除原淘汰原因后才重新进入比较。故障复发时先指出哪项前提或原验证失效，再沿当前真实触发路径核实。
- **JI-07 连续反转。** 同类方案连续两次被推翻后，停止扩大候选和整套重排，确定一个最能改变选择的未知，写明不同观测结果分别怎样影响决定，再交给 `solution-design` 取证。
- **JI-08 用户结论。** 给出一个当前首选、少量关键理由、适用条件和确有必要的下一步。用户要求比较时保留有区分力的比较，避免把多个对称选项重新交给用户裁决。
- **JI-09 最终确认与关闭。** 最终确认保持原证据范围，局部优势不能自动升级成类别总排名。用户完成选择后关闭该问题；真实使用失败、相关事实变化或用户主动重开时，再恢复受影响部分。
- **JI-10 执行证据。** 本插件被调用时，回答同时附上 `reasoned-decision-execution-evidence.yaml`。按 [execution-evidence.yaml](references/execution-evidence.yaml) 的字段结构为每条实际使用的规则重复一组记录；`插件/技能与版本` 填写 `Reasoned Decision v0.1 / judgment-integrity`，并写明“规则编号 → 成品原句或位置”。发生改写时填写改前与改后。两个技能同时使用时合并到同一个文件。插件未被调用时不附证据文件。
