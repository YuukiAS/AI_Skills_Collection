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
