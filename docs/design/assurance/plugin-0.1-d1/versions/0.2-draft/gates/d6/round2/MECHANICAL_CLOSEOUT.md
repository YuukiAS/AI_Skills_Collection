# D6 round2 两处阻塞的机械核对

按用户转达的 Claude（D1）裁决，B1、B2 已作指定文字替换；改正文字与现有设计及直接引用一致。用户仍是冻结批准者，D7 仍是冷读开工关卡，9 个回归用例及其交付验收分工不变。本记录按 MERGE §29、§30 核对两处及其直接引用，不另开一轮全量 D6。

## 改动前后

基线提交：`ad388c4f39dbc51db4494e7f43ebcd1856ca28b2`。Blueprint 仅改 4 个标量字段。完整字段前后文字及 JSON Pointer 见 [changes-closeout.json](changes-closeout.json)；下表列出实际替换文字，其余正文不变。

| 位置 | 改动前 | 改动后 |
|---|---|---|
| B1：`fr-roles.terminal.mechanism` 的 D1 摘要 | D1 负责澄清、汇总、四关卡和批准冻结 | D1 负责澄清、汇总四道关卡结果，并在用户批准 snapshot_sha256 后执行冻结；批准者是用户 |
| B2：`gates.terminal.mechanism` 的“本轮整体完成条件” | D7 全部 9 个回归用例通过 | D7 冷读通过：新执行者仅凭 Blueprint 能列出开工前阻塞并判定可开工，且确认 Blueprint 中登记了全部 9 个回归用例及其执行负责环节 |
| B2：`wr-gates.expectedResult` | D7 全部 9 个回归用例通过 | D7 冷读通过：新执行者仅凭 Blueprint 能列出开工前阻塞并判定可开工，且确认 Blueprint 中登记了全部 9 个回归用例及其执行负责环节 |
| B2：`wr-gates.technical.expectedResult` | D7 全部 9 个回归用例通过 | D7 冷读通过：新执行者仅凭 Blueprint 能列出开工前阻塞并判定可开工，且确认 Blueprint 中登记了全部 9 个回归用例及其执行负责环节 |
| B2 直接依据：`MERGE_DECISIONS.md` §30 的整体完成条件 | D7 全部 9 个回归用例通过 | D7 冷读通过：新执行者仅凭 Blueprint 能列出开工前阻塞并判定可开工，且确认 Blueprint 中登记了全部 9 个回归用例及其执行负责环节 |

MERGE 同步的是同一处错误条件，不新增设计决定。历史审查结果和旧提示词保留真实原文；活动 D8 入口 `gates/D8_PROMPT.md` 更新为 round3。`acceptance-inventory.json` 仅同步 source 身份，非 source 字段全部不变。

## 直接引用与一致性

| 对象或引用节点 | 核对依据与关系 | 一致性结论 |
|---|---|---|
| B1 → `role-D1` | fr-roles 直接引用该角色；角色卡写“取得用户批准并冻结”“不代用户批准” | 新摘要与角色职责一致，取得批准和执行冻结均未变成自行批准 |
| B1 → `fr-decisions`、`freeze`、`c-gates-to-freeze` | 用户只批准 snapshot_sha256；关卡通过后请用户批准，再按五步顺序冻结 | 批准者、批准对象和先后顺序一致 |
| B1 → `role-D2` 至 `role-D8`、`dispatch`、`prompts`、`role-X1` 至 `role-X5`、`calibration`、`sign` | fr-roles 正文列出的其他来源；本次只替换 D1 摘要 | 所有来源节点原样保留；摘要之外的角色分工逐字未变，没有新增或转移决定权 |
| B1 反向文字引用：`dispatch`、`prompts`、`role-D1`、`role-D8`、`contract-fidelity`、`freeze`、`planning-entry`、`freeze-review` | 引用 fr-roles 的七部分排列、角色表或 D8 合批披露 | 定位仍有效，未改文字与批准权修正不矛盾 |
| B2 → `role-D7`、`c-gates-to-role-D7`、`c-role-D7-to-gates` | D7 只看 Blueprint，列出实质开工前仍须询问的决定，不实施；结果为开工阻塞或具体可行顺序交 D1 | 完成条件现为冷读与用例/执行环节登记确认，未要求 D7 执行回归 |
| B2 → `role-D1`、`role-D5`、`role-D6`、`role-D8`、`contract`、`freeze` | gates 的直接入/出连接及 v7-08 至 v7-10 连接：设计进入四关、结果回 D1、补缺口或批准后冻结 | 连接不变；其他三关完成条件及失败去向不变 |
| B2 反向文字引用：`fr-decisions`、`fr-downloads` | 前者把本次收口指向 gates/§30，后者引用 gates 的检查器下载规则 | §30 与 gates 已同步，下载规则不受本次替换影响 |
| B2 → `wr-gates` | nodeId 和 technical.nodeId 指向 gates；读者和技术 expectedResult 引用同一整体完成条件 | 两个镜像与 gates、MERGE §30 使用完全相同的 D7 冷读条件 |
| 原回归机制：`contract-regression` §6.3a、`acceptance`、`role-X1` 至 `role-X5` | D1 写用例集；X2 修复前复现旧问题；脚本由 X2 跑，真实宿主操作由 X4 跑，专业判断交 X5，写明用户判的交用户；X1 组织并亲读逐条原始输出，最终候选整份通过是签发前提 | 上述节点与验收器全部与基线相同；9 个用例的内容、判据、数量和执行分工不变，仍由原交付验收机制承担 |

直接引用按当前节点自身字段中的 fr-roles/gates 引用及直接连接端点定位，不递归展开其他设计问题。读取原回归机制只为确认分工保留，不重审其内容。

## 机械保护与重跑结果

结构化差异确认：只有 gates、fr-roles 两个节点自身字段变化，以及 wr-gates 两个 expectedResult 字段变化。所有角色卡、连接、需求、证据、验收条目和内嵌 versions 原样保留；0.1 历史文件无改动。见 [verification-closeout.json](verification-closeout.json)。

废弃语义扫描覆盖 62 节点、8062 个字符串，残留 **0**，允许的明确删除说明/历史引用 **39**。D5 固定检查器离线、在线均检查 62 节点，schema 成功，在线 unresolved=0，无新增机械错误。按既有 D1 排除口径通过；原始退出码均为 **1**，仍保留 1 条冻结快照差异和 5 条待 D8 记录。详见 [D5 round3](../../d5/round3/RESULT.md)。

Blueprint 原始字节 SHA-256：`2d6efbe759fa40202a385eca53dec8cb2250930e1574c3b7c424d686af790ec9`。

snapshot_sha256：`dc6953587e95044854b914447effacaaa9edc9187b2a63fa4315dd999238a886`。

以上身份不表示旧关卡结果已自动绑定新快照。当前机械核对不替代 D1 裁决、D7 冷读、D8 复述、用户批准或交付回归。

## D8 round3 范围

只有 wr-gates 的读者文字变化，其动作、输入、理由、失败后果不变。相邻 wr-contract、wr-freeze，以及关联 fail-checker、fail-freeze-explanation 文字与基线相同；本次替换没有引入需补入的受影响相邻单位。

已生成自包含的 [D8 round3/PROMPT.md](../../d8/round3/PROMPT.md)，只含 wr-gates。代码块正文与固定检查器 readerText 完全一致，textHash 为 `a3ff68fbf8b4c11450f21eff918758ec481d926fa38df8f2190baedeb750d3ea`。round3 尚未发送或执行，不预填复述或通过结论；返回后由 Claude（D1）裁决。

## 核对结论

B1、B2 按本轮 D1 裁决完成机械修正，两处及其直接引用一致，没有改变其他责任、权限、费用或签发标准。本轮未重做全量 D6，未执行产品回归、冻结或发布。
