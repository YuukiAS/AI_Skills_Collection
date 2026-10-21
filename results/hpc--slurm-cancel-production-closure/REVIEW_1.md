---
schema: AI_BRIDGE_REVIEWED_REVIEW_V1
task_key: hpc--slurm-cancel-production-closure
review_round: 1
decision: PASS
implementation_commit: 3e81802ab0251d3bf31ec2d808d4e3273505b2f6
---

# Current independent conclusion

Final release `f4517798a73adf29d3484306d60845488739f1fc`: independent implementation review, final CI identity and G5 PASS. The phased original reviewer reports below are preserved verbatim; earlier NOT_YET_VERIFIED flags describe their checkpoints and are superseded by the last formal identity review. No product changes were requested.

# 独立最终实现复核 — 2026-10-21

## 结论与身份

INDEPENDENT_IMPLEMENTATION_REVIEW=PASS
G4_REVISED_ACCEPTANCE=PASS
KEEP_TEST=NOT_RUN
LIVE_JOB_RETAIN_TEST=WAIVED_BY_CURRENT_USER
FORMAL_RELEASE=NOT_YET_VERIFIED
FORMAL_INSTALL=NOT_YET_VERIFIED

复核者为独立 implementation reviewer，不承担 Planner / Critic 角色。

冻结 implementation：
`3e81802ab0251d3bf31ec2d808d4e3273505b2f6`

复核时 task branch：
`reviewed/hpc--slurm-cancel-production-closure`

复核时 checkout HEAD：
`a647a8044591a5cf6bbd24f241fdc0f576b562e4`

三个产品脚本与冻结 implementation 逐字一致；完整
`skills/tools/hpc/slurm-workflows/` 及两个 protected-cancel 测试文件相对
冻结 implementation 无差异。

SHA256：

- setup_protected_cancel.py:
  `0fa4c9a601645470cf778038ea17f1c062c794fd31b2bc7bde3c0cb931327d03`
- slurm_cancel_hook.py:
  `1b5d2cc5cdbd390865fb14862e7c84a803f6a75b60141c8e629cb433dadeea65`
- slurm_protected_cancel_mcp.py:
  `e1582e92bbe6d9f0f2086761d3ef092c08d3481df10fbc5830c7f170244e34e9`

## 实现检查

未发现需要修改冻结 runtime 的阻断性问题：

- command declaration 在检查 mutable runtime 前识别无关 Bash；
  stale declaration 和 MCP 均保留无关命令隔离。
- root metadata.threadId 必须等于 Hook session_id；完整 command
  event 拒绝显式 subagent context。
- MCP 只能等待并消费 command guard 创建的 exact pending；
  session、turn、tool、cwd、owner、targets、operation、nonce、
  lifetime 和 pending state 均受检查。
- 缺失、错配、过期和已消费 pending 不会打开确认或获得取消权限；
  并行 handler 的早到等待有明确上限。
- 原始受保护 Bash 始终被拒绝。只有当前原生 required two-choice
  form 的 accept/confirm 答案进入执行路径；关闭、超时、无效响应
  和 retain 不执行取消。
- retain 在 reservation 前返回；确定性 MCP 集成测试明确检查
  零 invocation 和零 consumed reservation。
- 确认前重新解析，O_EXCL 创建 reservation，并对文件及目录 fsync；
  reservation 后再次解析 exact targets，重新核对 runtime identity，
  然后记录 durable invocation intent 并只调用冻结绝对路径一次。
- 重复事件受 immutable audit、pending state 和 exclusive reservation
  约束；失败和不明确结果没有自动重试路径。可能已经调用后的异常
  由 invocation-intent 检查保留 ambiguous 语义。

## 实际证据复核

读取 REVISED_G4_ACCEPTANCE.md、LIVE_CONFIRMATION_EVIDENCE.md、
REPLACEMENT_G4_EVIDENCE.md，并直接检查 canonical checkout 下三个
durable private evidence bundle。

三个 receipt 清单共 23 个文件均与记录 SHA256 一致：

- retain-ui-mapping-pass-20261021/
- post-confirm-20261020/
- replacement-g4-confirm-20261021/

原生 retain 审计 identity `33480a9f...` 的实际响应为
`{"action":"accept","content":{"decision":"retain"}}`。
schema 与两次真实确认一致；metadata thread 与 session 相同。
pending 为 ui_probe、空 Job 集合，最终 closed。

Job 5693449 与 6028303 的两条实际 confirm 审计分别具有一个
reservation、final_resolved、invocation_intent、returncode 0 和
consumed pending，事件顺序一致。当前 installed state 仍只有两份
reservation 和两份 invocation_intent，全部逐字等于历史快照。

已安装清单的 7 个文件全部与冻结候选安装 receipt 的哈希一致。
安装后的 Hook 和 MCP 源文件也与冻结源代码逐字一致。

同候选既有验证为 focused 54、full Slurm 69、full repository 401
PASS，candidate CI 39434396011 success。验证 receipt 对应的六份
日志哈希均一致。本次没有重复运行测试。

## 验收边界

用户已明确以真实 harmless native retain wire mapping、冻结候选的
确定性 retain 集成和两次真实 confirm 替代 live held-Job retain。
本结论仅按该修订合同接受 G4；不把 KEEP_TEST 改写为 PASS，也不
把 ui_probe 描述为真实 Job retain。

产品 reconciliation 的 NOT_VISIBLE 不单独证明终态取消；两个
Job 的 CANCELLED、零 runtime/allocation 来自既有独立 scheduler
verification receipt。本次未重新查询 scheduler。

本次未运行 scheduler 命令、创建或操作 Job、调用真实 scancel、
重开原生表单、改变 Hook/config/trust 或修改产品代码。

最终 main 集成、版本 metadata、最终 candidate CI、发布与正式
安装仍须独立关闭。收到最终 release candidate SHA 后，需补查
runtime identity 与 release delta；本报告不提前授予这些 gate PASS。


## 最终发布候选独立差异复核 — 2026-10-21

FINAL_CANDIDATE_IDENTITY_REVIEW=PASS
INDEPENDENT_IMPLEMENTATION_REVIEW=PASS
G4_REVISED_ACCEPTANCE=PASS
KEEP_TEST=NOT_RUN
FINAL_CI=NOT_VERIFIED
G5=NOT_VERIFIED
FORMAL_RELEASE=NOT_VERIFIED
FORMAL_INSTALL=NOT_VERIFIED

本次是同一次独立实现复核的最终候选补查，未发现新增阻断性缺陷。

精确候选：`b567479a88fce30637be60b6894a4fd5e2b0db18`。
冻结实现：`3e81802ab0251d3bf31ec2d808d4e3273505b2f6`。
main 基线：`c7f98f201c746d357344091f89cce7a3541154d9`。
正常合并：`6a1ece94609809bfe8289a04fa2f5d224e0d6fa9`。

上述三个前置 commit 均为最终候选的 ancestor。本地 remote-tracking
exact task branch 也指向最终候选；本次未重新联网查询远端。

三个 runtime 脚本及两个 protected-cancel 测试文件与冻结实现逐字一致。
因此 rules、declaration、安装生成逻辑保持原实现。SHA256：

| 文件 | SHA256 |
| --- | --- |
| setup_protected_cancel.py | 0fa4c9a601645470cf778038ea17f1c062c794fd31b2bc7bde3c0cb931327d03 |
| slurm_cancel_hook.py | 1b5d2cc5cdbd390865fb14862e7c84a803f6a75b60141c8e629cb433dadeea65 |
| slurm_protected_cancel_mcp.py | e1582e92bbe6d9f0f2086761d3ef092c08d3481df10fbc5830c7f170244e34e9 |

Slurm SKILL 相对冻结版仅 version `0.4 -> 0.5`。
Repository 从当前 main 的 `5.5.1` 升为 `5.5.2`；release-baseline
测试仅更新两个对应期望值。registry 相对 main 仅改变仓库版本和生成时间，
catalog 仅改变生成时间。README 仅改变两个版本字符串，其 SHA256
`ee6190e52390a40e35abfd09f64ef0616f8e4e28f031448eadb56005c8925483`
与已保存的实际 Clear Writing 检查回执一致。

中央 plugin source configuration、generated payload、Marketplace 和
profiles 相对 main 无差异。十个中央版本在 source、generated 和 baseline
中一致：workflow-core 0.5、ai-skills-core 0.5、writing-style 0.5、
research-writing 0.2、presentations 0.4、scientific-visualization 0.1、
web-development 0.4、statistical-modeling 0.1、bioinformatics 0.1、
medical-imaging 0.1。main 的无关改动已保留。

历史两次 confirm 证据未被重写；修订 G4、发布说明和维护条目均保留
`KEEP_TEST=NOT_RUN` 与用户明确免除 live held-Job retain 的边界，
没有把 harmless UI probe 描述为真实 Job retain。

本次只读检查，没有运行测试、scheduler、Job 操作、真实 scancel、
原生卡，也没有改变 config/trust。最终 candidate CI、G5、正式发布
和正式安装仍须取得各自证据；本结论不替代这些 gate。


## 最终候选增量复核

FINAL_CANDIDATE=f4517798a73adf29d3484306d60845488739f1fc
INDEPENDENT_FINAL_REVIEW=PASS
FINAL_CI=NOT_YET_VERIFIED
FORMAL_RELEASE=NOT_YET_VERIFIED

确认该候选为已通过独立复核的
`b567479a88fce30637be60b6894a4fd5e2b0db18` 的直接子 commit。

完整增量仅涉及两个文件：

- `tests/test_central_plugin_icon_assets.py`：将旧仓库版本期望
  `5.5.1` 修正为实际发布版本 `5.5.2`。
- `RELEASE_CANDIDATE_IDENTITY.md`：修正版本期望变更数量，保留首次
  CI `39639003443` 的单项失败及必须重跑最终候选 CI 的说明。

没有 runtime、安装生成逻辑、规则、图标、plugin 或其他行为变更。
此前冻结实现、修订 G4 与版本一致性的独立复核结论适用于本候选；
`KEEP_TEST=NOT_RUN` 边界保持。

本次仅只读核对完整 diff，未重跑测试或查询 scheduler。
新 CI `39639471530` 尚未在本复核中验收，正式发布仍待其成功。


## 正式发布与安装身份闭环复核

RELEASE_COMMIT=f4517798a73adf29d3484306d60845488739f1fc
INDEPENDENT_FINAL_REVIEW=PASS
FINAL_CI=PASS
G5=PASS
FORMAL_SOURCE_INSTALL_IDENTITY=PASS
G4_REVISED_ACCEPTANCE=PASS
KEEP_TEST=NOT_RUN

只读核验确认：

- CI `39639471530` 的 headSha 精确匹配上述发布 commit；
  四个 jobs 均 success，日志记录 `Ran 406 tests` 和 `OK`。
- 正式 source checkout HEAD、main/release 及对应 origin refs 均为
  该 commit；保存的 remote-refs 回读一致。Repository 版本为 5.5.2。
- 正式安装清单的 7 个文件与冻结候选 P0 清单一致，实际安装文件
  哈希全部匹配；三个 source 脚本仍逐字等于冻结实现。
- 实际 config 哈希与安装前后相同的回执一致。保存的 28 个 durable
  state 文件均匹配，仍只有两份 reservation 和两份 invocation intent。
- 最后一份 hooks/list 回读中三个 handler 均 enabled、trusted，
  warnings/errors 为空。
- 独立 copy install 的 SKILL 为 0.5，SKILL 与三个脚本均逐字等于
  正式 release source。

正常空编辑 reload、实际 git status 成功及 scancel --help 被
PreToolUse 以 unsupported_scancel_target_or_option 拒绝，依据
Executor 提供的真实工具结果与 formal receipt 接受；本独立复核者
未亲自重执行这些动作。hooks/list 本身不替代正常入口证据。

本轮仅读取 source、安装文件、回执、refs 和 CI 日志，没有执行任何
Slurm/Job 操作、原生卡或 config/trust mutation。没有新增实现缺陷，
无需修改产品；剩余工作仅为文档、状态与维护看板收尾。
