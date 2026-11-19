---
name: research-story
description: "为导师、组会听众、合作者和跨领域读者撰写完整研究故事，串联问题、价值、方法、数据、证据、实验转向与下一决定；GPT 写作，Codex 仅承接制作。"
status: active
provenance: user-authored
trusted: false
requires_network: false
writes_files: true
executes_code: false
secrets_needed: null
last_reviewed: 2026-11-19
profile_tags:
  - research-writing
recommended_scope: project
icon_small: assets/app-facing.svg
icon_large: assets/app-facing.svg
---
# Research Story

用于导师报告、组会材料、合作者说明、跨领域研究介绍、研究提案、进展报告和研究纪要。目标读者需要从文档理解研究问题、使用价值、实际方法、决定性证据和当前需要的判断。

## 执行顺序

**RA-01｜绑定读者与决定。** 记录具体听众、已有背景、文档用途、需要理解或决定的事项、权威来源、目标格式和编辑范围。

**RA-02｜稳定方法与数据身份。** 在结果前说明研究对象、方法计算、数据与子集、基线、终点和比较规则。细节见 [research-story.md](references/research-story.md)。

**RA-03｜建立证据链。** 区分观察、解释、假设、限制、负结果与计划；结论强度服从实际设计和数据范围。

**RA-05｜形成完整研究故事。** 围绕问题、价值、方法、证据和判断变化组织全文。实验顺序只保留改变科学理解的因果关系。导师与组会任务同时读取 [group-meeting-advisor-reports.md](references/group-meeting-advisor-reports.md)。

**RA-07｜调用 Content Selection。** 制作前应用 `CS-03`～`CS-07` 形成唯一内容计划；真实成品返回后应用 `CS-08`、`CS-09` 复审整件作品，并按 `CS-10` 写入执行证据。

**RA-08｜调用 Clear Writing。** 连续成稿应用 `CW-03`～`CW-08`、`LF-01`～`LF-10`；改写已有材料时同时应用 `FI-01`～`FI-11`。本技能继续负责科研含义和证据关系。

**RA-09｜保护已接受内容。** 小修恢复接受稿、有效批注、拒绝内容和获准范围。新结果只更新直接相关事实与解释。

**RA-10｜保持时间与版本关系。** 历史决定、当前证据、未完成结果和下一计划各自保持身份；双语版本保持数字、公式和结论强度一致。

**RA-15｜交付执行证据。** 本技能被调用时，使用 [execution-evidence.yaml](references/execution-evidence.yaml) 为每条实际应用规则写“规则编号 → 成品中的原句或位置”；发生改写时填写改前与改后。GPT 将证据文件作为回答附件交付。未调用本技能时不创建该文件。

## 制作交接

需要渲染、机械检查、发布或回读时，填写 [handoff.template.json](references/handoff.template.json)，再交给 [Codex 制作入口](codex-entry.md)。制作约束见 [production-contract.md](references/production-contract.md)。
