# 迁移缺口

共 42 项，涉及 8 个案例。按“每案例的一个空字段或一轮空提示词 = 一项”计数；未冻结轮序整体计一项，不猜测应有几轮。

原文件均未修改。R1–R3 保留原四字段和两条完整判据，迁移副本在 `tools/regression-runner/examples/reasoned-decision/`；R4–R7 仅有空壳。`null` 表示未知，`[]` 才表示确定无需。

| 案例 | 项数 | 缺什么 |
| --- | --- | --- |
| RD-R1 | 4 | version；model；attachments；turns（完整冻结轮序与提示词） |
| RD-R2 | 4 | version；model；attachments；turns（完整冻结轮序与提示词） |
| RD-R3 | 4 | version；model；attachments；turns（完整冻结轮序与提示词） |
| RD-R4 | 6 | version；model；plugins；attachments；turns（完整冻结轮序与提示词）；criteria |
| RD-R5 | 6 | version；model；plugins；attachments；turns（完整冻结轮序与提示词）；criteria |
| RD-R6 | 6 | version；model；plugins；attachments；turns（完整冻结轮序与提示词）；criteria |
| RD-R7 | 6 | version；model；plugins；attachments；turns（完整冻结轮序与提示词）；criteria |
| INSTR-R1 | 6 | version；model；plugins；attachments；turn-1.prompt；turn-8.prompt |

指令 R1 第 1、8 轮原题含账号标识。为同时遵守“不出现用户名”和“不改原文”，提示词留空；其余七轮原文逐字保留。需来源维护者提供获准使用且无个人标识的冻结题面后才能运行，执行器不会自动替换。

指令 R1 原文只有正式设置 / 候选 v2 的相对描述，未给出本次测试的精确版本和模型；不拿历史运行模型替本轮定值。插件和附件是否无需也待确认。

指令 R1 明确要求同一普通新对话连续九轮，不能作为真实分支题。独立假案例 `synthetic-branch` 演示分支，不计入迁移缺口。

Reasoned Decision R1–R3 的来源是证据摘要、设计稿或覆盖表，未提供完整冻结的轮序、每轮原文与附件清单。已看到的历史引句不会被拼接成新回归题。

保真记录见 [MIGRATION_EVIDENCE.json](MIGRATION_EVIDENCE.json)：来源相对定位、SHA-256、保留的轮次和字段。
