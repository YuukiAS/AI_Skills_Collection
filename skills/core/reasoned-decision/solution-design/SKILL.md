---
name: solution-design
description: "在改善、配置、修复或实现方案前，调查现实已有能力和失败经验，优先复用并只设计有证据的剩余缺口。"
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
# Solution Design

用于非平凡的改善、配置、修复和实现问题，也用于为 `judgment-integrity` 发现候选、补充证据或设计最小验证。开始前读取 [task-state-contract.md](references/task-state-contract.md)，继承当前目标、已有能力、淘汰原因和关键未知。

## 执行规则

- **SD-01 目标与现状。** 先确认用户要达到的结果、当前环境已经具备的能力、必须保留的行为和可取舍内容。调查开始时不预选候选。
- **SD-02 现实解空间。** 按需检查当前上下文与项目、用户已有仓库和已安装能力、产品原生与官方生态、成熟实现、代表性成品、高价值社区经验及长期失败路线。从问题本身开放检索，先归纳解法类别，再深查少数强候选。
- **SD-03 来源作用。** 官方资料用于核实支持范围，具体实现用于核实工作机制，社区材料用于发现长期效果和失败模式。关键材料须核对对象、版本、环境和时点；重复转载不能充当多份独立证据。
- **SD-04 需求—能力对应。** 将每项必要需求标为已有能力完整覆盖、部分覆盖、组合后覆盖或仍有缺口。保留现状和移除非必要需求都可以进入候选比较。
- **SD-05 复用顺序。** 依次考虑直接采用、组合、局部扩展和最小自建。提出自建时须列出实际检查的现成路线、它们已覆盖的部分、仍未满足的硬约束、组合或扩展不足的原因、最小新增部分及维护成本。
- **SD-06 最小现场诊断。** 诊断故障时先定位真实状态持有者，优先读取文件、数据库、日志、命令接口、IPC 或只读 API，并尽量保留正在发生的现场。选择能区分主要解释的最小观测；重启、升级、重置和重装须有较小动作不足的依据。
- **SD-07 工具与用户动作。** 优先使用当前可用的网页、连接器和其他工具。只有事实需要用户权限或现场观测、且 GPT 无法直接取得时，才请求一个最小动作，并说明它将裁决哪个未知。
- **SD-08 调查停止。** 已有材料足以支持当前决定，且主要替代方案不会改变选择时结束调查。资料暂时不可访问时记录未核实范围，保留未知，不能据此声称没有现成方案。
- **SD-09 返回判断。** 向 `judgment-integrity` 返回实际来源、候选类别、覆盖关系、剩余未知、最小验证及观测结果。用户只要求建议时在建议完成后停止，不能自行扩成安装或实施任务。
- **SD-10 执行证据。** 本插件被调用时，回答同时附上 `reasoned-decision-execution-evidence.yaml`。按 [execution-evidence.yaml](references/execution-evidence.yaml) 的字段结构为每条实际使用的规则重复一组记录；`插件/技能与版本` 填写 `Reasoned Decision v0.1 / solution-design`，并写明“规则编号 → 成品原句或位置”。发生改写时填写改前与改后。两个技能同时使用时合并到同一个文件。插件未被调用时不附证据文件。
