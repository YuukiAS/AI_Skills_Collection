# Assurance 0.2 四道关卡最终汇总

四道设计关卡已按本轮批准的收敛规则通过，可以交用户审阅当前 0.2 Blueprint。此处“通过”是设计关卡完成，不表示已获用户批准、已冻结、插件已实现或产品回归已经运行。本轮只整理审阅材料，不执行冻结。

## 当前审阅对象

- Blueprint：[当前设计](../../blueprint.json)，材料基线提交 `51d290f6`。
- `snapshot_sha256`：`dc6953587e95044854b914447effacaaa9edc9187b2a63fa4315dd999238a886`。
- Blueprint 原始字节 SHA-256：`2d6efbe759fa40202a385eca53dec8cb2250930e1574c3b7c424d686af790ec9`。
- 算法与 0.1 相同：对 `snapshotOf(bundle)` 的结果使用 `canonicalize@2.1.0` 作 RFC 8785 JCS 规范化，再对 UTF-8 字节计算 SHA-256，不加结尾换行。`versions` 不参与内容快照；不能以整个 Blueprint 文件的字节哈希替代。
- 本轮重新计算哈希并完成 draft schema 解析；Blueprint、内嵌历史及 `versions/0.1/` 均未修改。

历史报告 [GATES_0.2_REPORT.md](GATES_0.2_REPORT.md) 保留各阶段当时的状态；其中“待 D8”“D8 round3 尚未执行”等文字不是本轮最终结论。以下依据后续返回结果及关闭记录汇总，不回写原始审查结果。

## 按 wr-gates 的“整体完成”定义核对

以下逐项采用当前 Blueprint 的 `wr-gates.expectedResult`，与 [MERGE_DECISIONS §30](../../MERGE_DECISIONS.md) 及 [D6 机械收尾](gates/d6/round2/MECHANICAL_CLOSEOUT.md) 的修正一致。REVISION_0.2_PLAN 中较早的“D7 全部 9 个回归用例通过”已由该收尾纠正为冷读条件；本次不重写历史计划，也不把 D7 当成产品回归执行者。

- [x] **D5 机械检查通过，快照差异与待 D8 项按既定口径排除。** 固定检查器 `Asteria-Blueprint@229e1736f445bdecffd84773ad543e5f452d65df` 全量检查 62 节点，schema 成功，在线 `unresolved=0`，无新增机械错误。状态为 `PASS_WITH_DECLARED_EXCLUSIONS`，原始离线、在线退出码均为 **1**。6 条原始错误为冻结历史仍是 0.1，以及 5 条旧 reader 记录与当前文字哈希不同；D8 已由后续独立返回结果关闭语义关卡，未篡改旧 reader 记录或原检查器报告。
- [x] **废弃语义扫描零残留。** 当前 62 节点、8062 个字符串，残留 0；39 处准确历史引用或明确删除说明按规则允许。
- [x] **D6 无 blocking。** round1 覆盖 62 节点 × 7 类，共 434 项；3 个 blocking 在 round2 确认关闭。round2 新增 B1（批准者）与 B2（D7 职责）已由 D1 裁决替换，并按改动及直接引用完成机械核对，不另开全量追问。
- [x] **D7 冷读通过。** 全量冷读覆盖 62 节点，唯一阻塞 D7-B1 是回归正文 9 个用例与机器判据 `eq 8` 冲突；D1 裁决保留全部 9 个后，定向复核为 `TARGETED_RECHECK_PASS`，该项剩余阻塞 0。当前 Blueprint 登记 R1–R8、S1 共 9 个用例、20 条检查及负责执行环节：X1 组织并亲读原始输出，脚本由 X2 跑，真实宿主操作由 X4 跑，专业判断交 X5，指定用户判断的交用户。后续文字修正未改变该回归机制。此为原全量冷读加关闭唯一阻塞的复核，不声称重新做过一次完整独立冷读。
- [x] **D8 全部受审单位复述正确。** round1 的 6 单位中 4 个正确；`wr-gates` 与 `supp-clarify-0.2` 改写后在 round2 均返回 `confusions=[]`。D6 round2 修正又改变 `wr-gates`，其旧 round2 通过不能继承；round3 已对新文字返回正确复述、`confusions=[]`，`textHash=a3ff68fbf8b4c11450f21eff918758ec481d926fa38df8f2190baedeb750d3ea` 与当前文字一致。其余未变单位沿用最近一次真实通过记录，范围不扩大。
- [x] **任何一关有 blocking 即未完成；当前 blocking 均已关闭。** 按用户本轮确认及既有 D1 收敛裁决汇总。D8 保留每轮新对话合批、D1 逐项比对的 `single-thread-batch` 方式；全部正确即本轮有效通过，不增设单位例外。本报告不冒充新增独立 D1 审查。

## 关卡证据

| 关卡 | 最终状态及证据文件 |
|---|---|
| D5 | 按声明排除项通过：[round3 结果](gates/d5/round3/RESULT.md)、[机器结果](gates/d5/round3/RESULT.json)、[废弃语义扫描](gates/d5/round3/deprecated-after.json)、[离线原报告](gates/d5/round3/offline-report.json)、[在线原报告](gates/d5/round3/online-report.json)、[检查器身份](gates/d5/round3/checker-identity.json)、[快照身份](gates/d5/round3/snapshot-identity.json) |
| D6 | 阻塞已关闭：[round1 结果](gates/d6/round1/RESULT.md)、[434 项追问](gates/d6/round1/questions.json)、[round2 结果](gates/d6/round2/RESULT.md)、[round2 追问](gates/d6/round2/questions.json)、[MECHANICAL_CLOSEOUT](gates/d6/round2/MECHANICAL_CLOSEOUT.md)、[逐字段替换](gates/d6/round2/changes-closeout.json)、[保护核对](gates/d6/round2/verification-closeout.json) |
| D7 | 全量冷读及唯一阻塞关闭：[原始冷读](gates/d7/round1/COLD_READ.md)、[原始结果](gates/d7/round1/RESULT.json)、[定向复核](gates/d7/round2/RESULT.json)、[三处机械修正](gates/d7/round2/changes.json)；后续职责修正与原回归机制的一致性见 D6 的 MECHANICAL_CLOSEOUT |
| D8 | 按改写逐轮收敛通过：[round1 说明](gates/d8/round1/RESULT.md)、[round1 原始复述](gates/d8/round1/RESULT.json)、[round2 原始复述](gates/d8/round2/RESULT.json)、[round2 受审文字](gates/d8/round2/units.json)、[round3 原始复述](gates/d8/round3/RESULT.json)、[round3 受审文字](gates/d8/round3/units.json) |

D7 文件本轮从既有执行证据中逐字复制到上述公开目录；保留原始失败结论及后续复核，未改成一份虚构的全量 PASS。各关早期文件中的哈希只标识当时受审对象；后续有效范围由已批准改动、直接引用核对及 D8 重读串联，不能把旧文件哈希宣称为当前哈希。

## 未关闭的非阻塞事项（留 0.3）

来源：[D6 round2 的 non-blocking 清单](gates/d6/round2/RESULT.md)。

| 事项 | 为什么不阻塞 0.2 | 后续处理 |
|---|---|---|
| `role-D1` 正文有两处近似重复的“D6 审 freeze-review”说明 | 语义一致，不影响职责或冻结判断 | 0.3 文字去重，按届时实际改动确定复核范围 |
| 废弃语义扫描对未来同义改写、枚举式旧范围的识别仍可改进 | 当前已知旧字符串和已批准替换有规则，当前实扫零残留 | 0.3 提高识别鲁棒性；不借本次材料整理修改扫描规则 |

以下是明确保留的边界，不冒充 0.3 缺陷：原检查器的排除项和 191 条人工提示如实保留；界面缺少结构化关卡记录时显示“未记录”；未知依赖大小显示“未记录”；9 个产品回归及插件验收仍为 `NOT_RUN`，应由原交付验收机制完成。用户批准与冻结也均未执行。

用户审阅入口及截图见 [approval/README.md](approval/README.md)。
