---
name: student-materials
description: "根据课程权威材料撰写学生作业、项目简报、讲义和普通检查表，完整交代任务、必要背景、产出与公开规则，并保护累计批注和接受版式；GPT 写作，Codex 仅承接制作。"
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
# Student Materials

用于面向学生的作业说明、项目简报、讲义和普通文字检查表。题目、数据、评分政策、方法边界和教学要求从课程负责人或课程权威材料取得。

## 执行顺序

**RA-01｜绑定学生任务。** 记录学生要完成的任务、已有知识、交付物、公开规则、目标格式、课程权威来源、接受稿和编辑范围。

**RA-03｜保持来源与要求对应。** 题目、数据、分值、截止要求、方法边界和必要限制对应准确来源。未批准的教学要求保持缺口并交回课程负责人。

**RA-06｜写完整且适量的学生材料。** 学生应能识别要做什么、使用什么材料、提交什么、哪些规则影响完成任务。评分设计、答案生成、题库筛选、口试评判和替学生选择方法继续由相应教学负责人处理。

**RA-07｜调用 Content Selection。** 制作前应用 `CS-03`～`CS-07` 形成唯一内容计划，清理重复行政说明和其他读者材料；真实成品返回后应用 `CS-08`、`CS-09` 复审整件作品，并按 `CS-10` 写入执行证据。

**RA-08｜调用 Clear Writing。** 连续成稿应用 `CW-03`～`CW-08`、`LF-01`～`LF-10`；已有材料的修订同时应用 `FI-01`～`FI-11`。课程事实与教学含义仍由本技能根据权威来源确认。

**RA-09｜保护累计认可。** 恢复接受母版、有效批注、已拒绝内容和允许改动范围。删除意见持续有效，范围外内容保持。

**RA-11｜给出文档家族与语义分组。** 记录现有模板、纸张、字体、层级、元数据、需要相邻的题目与说明、连续区域以及已许可或禁止的分页。详细规则按需读取下列 references。

**RA-12｜形成制作交接。** 将确定正文、内容权威、允许改动、语义块和目标文件写入 handoff。用户认可、GPT 内容判断和机械检查分别记录。

**RA-15｜交付执行证据。** 本技能被调用时，使用 [execution-evidence.yaml](references/execution-evidence.yaml) 为每条实际应用规则写“规则编号 → 成品中的原句或位置”；发生改写时填写改前与改后。GPT 将证据文件作为回答附件交付。未调用本技能时不创建该文件。

## 按需读取

- 新稿或完整制作流程：[student-assessment-end-to-end-pre-execution-runbook.md](references/student-assessment-end-to-end-pre-execution-runbook.md)
- 既有接受稿和累计批注：[student-assessment-cumulative-acceptance-contract.md](references/student-assessment-cumulative-acceptance-contract.md)
- 接受正例与防复发：[student-assessment-hw1-nonrecurrence-amendment-v1.md](references/student-assessment-hw1-nonrecurrence-amendment-v1.md)
- 交付与打包：[student-assessment-delivery-closure-amendment-v1.md](references/student-assessment-delivery-closure-amendment-v1.md)
- 分页与阅读节奏：[student-assessment-semantic-pagination-amendment-v1.md](references/student-assessment-semantic-pagination-amendment-v1.md)

需要制作时填写 [handoff.template.json](references/handoff.template.json)，交给 [Codex 制作入口](codex-entry.md)，并遵循 [production-contract.md](references/production-contract.md)。
