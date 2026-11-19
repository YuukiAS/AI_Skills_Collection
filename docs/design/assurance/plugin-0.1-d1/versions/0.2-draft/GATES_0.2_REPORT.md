> 最新状态：D6/D8 首轮反馈已按 D1 裁决修正，新增扫描从 10 处降至 0。D5 全量重跑后，按本轮约定排除冻结快照差异与待 D8 项则通过；原始退出码仍为 1，在线未核实项为 0。D6/D8 第 2 轮尚未执行。详见 [本轮修正及 D5 结果](gates/d5/round2/RESULT.md)；下文保留先前执行记录，不作为本次定向复核通过声明。

# Assurance 0.2 草稿关卡报告（第 2 轮）

本轮已消除 D5 的检查器字段不兼容问题，并按 Claude 裁决关闭 D7-B1 的数量矛盾。D5 尚未通过：原检查器仍报告当前草稿与最近冻结快照不同；该项只记录，未修改设计或补做冻结。另五份读者记录标为“待 D8”，不作为 D5 阻塞。

D6、D8 按用户要求不运行；两份提示词已核对并补齐本轮材料身份、读取范围、结果落盘位置和回复格式，需由用户分别发送到全新的 GPT 网页对话。当前不能据此批准冻结。没有 commit 或 push。

## 受审对象与范围


- 分支：`design/assurance-plugins-0.1-merged`；基线提交：`38f7aace61d4e352b6407e989962192f2949bba7`，叠加下文列出的三处未提交机械修正。
- 0.1 冻结基线：`9e5943f33440587e0b220474caa89e41a5d0d697`。
- Blueprint 原始字节 SHA-256：`c4a7d00cb74207179ec7e0b38a87d1590d6f83875a3f3fa4bea44003c9c340e5`。
- 当前内容快照 `snapshot_sha256`：`b5391abe78519612324ab229cf5f338af465783b9f4d6ecb99b215dc9c9df484`。
- 冻结基线的内容快照：`8cd6ae62f6cbadf2a6a8776e900986d593d6ae93963e1f9460bd9d5c72ded733`。
- 内容快照按原检查器的 `snapshotOf` 取值，经 `canonicalize@2.1.0` 作 JCS 规范化后计算；不包含版本历史。

依 MERGE_DECISIONS §30 和 REVISION_0.2_PLAN：D5、D7 全量；D6、D8 只覆盖冻结以来的实际改动。节点差异按自身字段计算，子节点改动不重复归到父节点。新增 8 个，原有 54 个均有字段变化，无删除。原有节点中包含新增验收器分类、角色档次和卡片短描述的改动，不能把这些节点记作完全未改；因此 D6 的实际差异范围恰好是当前 62 个节点。

**新增节点（8 个）：** `freeze-review`, `fr-decisions`, `fr-asks`, `fr-costs`, `fr-roles`, `fr-validation`, `fr-downloads`, `fr-nongoals`。

**改动的既有节点（54 个）：** `shared`, `state`, `writer`, `record-check`, `dispatch`, `prompts`, `revision`, `metrics`, `design`, `design-roles`, `role-D1`, `role-D2`, `role-D3`, `role-D4`, `role-D5`, `role-D6`, `role-D7`, `role-D8`, `clarify`, `gates`, `contract`, `contract-capability`, `contract-entry`, `contract-outcomes`, `contract-fidelity`, `contract-forbidden`, `contract-regression`, `contract-controls`, `contract-changes`, `contract-authorization`, `freeze`, `q-checker`, `q-inheritance`, `delivery`, `delivery-roles`, `role-X1`, `role-X2`, `role-X3`, `role-X4`, `role-X5`, `acceptance`, `calibration`, `candidate`, `evidence`, `deviation`, `sign`, `packaging`, `source-layout`, `planning-entry`, `execution-package`, `minimum`, `capability-check`, `web-later`, `q-capacity`。

**D8 改动单位（5 个）：** `wb-capability`, `wr-gates`, `wr-freeze`, `fail-freeze-explanation-whole`, `fail-freeze-explanation-step-1`。同一失败路径闭包检查未增加其他单位。其余 55 个单位的文字和哈希均与真实的 0.1 最近一次通过记录一致；仅这些单位可以继承。

首轮范围依据见 `scope.json`、`CHANGED_NODES.md`、`mechanical-audit.json`；本轮三处修改、哈希及保护核对见 `round2/d7/changes.json`、`round2/snapshot-identity.json`、`round2/mechanical-audit.json`。上述差异范围未扩大。

## 各关结果

| 关卡 | 第 2 轮范围 | 结果 |
|---|---|---|
| D5 | 用 `229e173` 检查器检查当前完整草稿；离线、在线 | schema 通过，均检查 62 个节点；原始退出码均为 1；剩 1 条冻结快照差异，另 5 条待 D8 |
| D6 | 提示词自包含核对；不执行追问 | `NOT_RUN`；当前材料覆盖 62 个节点、434 项追问 |
| D7 | 仅复核 D7-B1 的三处数量一致性 | 定向复核通过，D7-B1 已关闭；没有重跑全量独立冷读 |
| D8 | 提示词自包含核对；不执行复述 | `NOT_RUN`；5 个单位待复述，55 个未改单位保留原继承记录 |

### D5：指定版本的机械检查

使用 `YuukiAS/Asteria-Blueprint` 的 `229e1736f445bdecffd84773ad543e5f452d65df`。将 `content/check.mjs`、其直接及递归导入文件、schema 和包元数据共 15 个文件复制到证据目录 `round2/checker/content/`，逐文件核对源工作树、指定 commit 和副本字节一致。依赖引用原安装，报告和缓存只写本轮证据目录。没有修改检查器、schema、规则或 liveVerifier。

同一份修正后草稿分别使用 `--stage draft --offline` 和 `--stage draft`。两个命令的 schema 均成功解析，检查节点均为 62 个；上一轮 114 条不认识 `category`、`roleTier`、连接 `kind` 的错误全部消失，本轮没有剩余的字段版本不匹配错误。原始报告各有 6 条错误，逐条归属如下。

| 规则与位置 | 归属 | 本轮处理 |
|---|---|---|
| `freeze`，`versions` | 真实的草稿与最近冻结快照差异；不是字段版本不匹配 | 原检查器在 draft 档也执行这条规则，故退出码仍为 1；只记录，不补冻结、不改历史 |
| `reader-current-hash`，`wb-capability` | 待 D8 | 本轮走查数字已同步为 9，并刷新提示词文字与哈希；不作为 D5 阻塞 |
| `reader-current-hash`，`wr-gates` | 待 D8 | 不作为 D5 阻塞 |
| `reader-current-hash`，`wr-freeze` | 待 D8 | 不作为 D5 阻塞 |
| `reader-current-hash`，`fail-freeze-explanation-whole` | 待 D8 | 不作为 D5 阻塞 |
| `reader-current-hash`，`fail-freeze-explanation-step-1` | 待 D8 | 不作为 D5 阻塞 |

离线报告有 1 条预期的 `offline` 未核实提示；最终在线报告 `unresolved=0`，Git 来源与外链核实已实际执行，lychee 的 6 条外链均核实成功（无缓存命中）。两种模式各有 191 条人工审查提示，仍需相应角色判断，本轮没有代判为通过。

在线首次运行有 11 条来源定位未核实：复制后的检查器目录没有 Git origin，执行环境只映射了 AI_Skills_Collection，遗漏 Asteria-Blueprint。本轮使用检查器既有的 `BLUEPRINT_SOURCE_ROOTS` 配置补齐来源映射，仅重试在线检查，最终未核实项为 0。首次结果另存为 `online-setup-attempt-*`；这属于执行环境定位问题，不记作草稿错误，也没有用改规则消除错误。

证据：`round2/checker-identity.json`、`round2/d5/offline-report.json`、`round2/d5/online-report.json`、对应 `*-exit.json`、`round2/d5/check.log`、`round2/d5/online-check.log`、`round2/d5/RESULT.json`。首轮报告和旧检查器证据保留，未拿旧的零节点结果充当本轮检查。

### D7：Claude 裁决后的定向复核

用户本轮转达 Claude 裁决：R8 已正式纳入 0.2，成为第 9 个回归用例；将验收判据 `eq 8` 改成 `eq 9` 是与已批准修订保持一致的机械修正。只修改当前 Blueprint 的以下三处，冻结历史不变。

| JSON Pointer | 修改 |
|---|---|
| `/nodes/3/children/4/validators/1/criteria/0/value` | `v-regression-set` 的通过用例数由 `8` 改为 `9`，operator 仍为 `eq` |
| `/nodes/3/children/4/validators/1/method/command` | 分组中的“新能力 12”改为“新能力 14”，与已批准的 R8 两条检查一致 |
| `/walkthroughs/1/steps/3/action` | `wb-capability` 的“8 个回归用例”改为“9 个回归用例” |

复核确认：正文枚举为 R1–R8、S1 共 9 个用例；通过用例数判据为 `eq 9`；失败、无法判断或未执行的检查条目数量仍须 `eq 0`；分组为 14+3+1+2=20 条；走查的输入行动与完成条件均指向 9 个用例。结构化差异比较确认 Blueprint 只改变上述三个标量字段。

**D7-B1 定向复核通过。** 首轮全量独立冷读及其原始阻塞记录保留在 `d7/COLD_READ.md`、`d7/RESULT.json`；本轮没有重新发起独立线程，也没有重新审其他项目。本轮复核的是设计判据的一致性，R1–R8、S1 的实际运行仍为 `NOT_RUN`，未伪造插件回归通过。

证据：`round2/d7/changes.json`、`round2/d7/RESULT.json`、`round2/mechanical-audit.json`。

### D6、D8：仅核对提示词，不执行

两份提示词均写明公开仓库、任务分支、固定基线提交、本轮未提交修改的身份、读取范围、结果落盘位置、回复格式和不得 commit 的边界。D6 与 D8 必须分别使用全新的 GPT 网页对话。

- **D6：`codex-runs/assurance-02-gates/d6/PROMPT.md`。** 只读固定提交中的原需求和 Blueprint，再应用提示词完整列出的三处已批准替换；不能直接把远端旧提交当作修正后草稿。也可使用已同步的 `d6/blueprint.json` 副本。62 个节点和七类问题范围保持不变，回复 `questions.json` 数组及 `RESULT.md` 内容，交回后落盘到本地证据目录 `d6/`。拿不到完整材料须报告 `NOT_RUN`，不得补答案或虚报哈希核验。
- **D8：`codex-runs/assurance-02-gates/d8/PROMPT.md`。** 五个单位的完整文字、顺序和逐单位哈希已内嵌；`wb-capability` 同步本轮数字修正，其余四个单位原样保留。只读内嵌材料，不读仓库、D6 或其他设计。回复 `RESULT.json` 数组，包含 subjectId、round、textHash、五点复述及 confusions，交回后落盘到本地证据目录 `d8/`，再由 D1 逐单位判断。

本轮没有发送这两条提示词，没有新追问、读者复述或 D1 通过判断。D5 使用的仍是原有真实历史记录；未追加记录。当前五个单位均待 D8，其余 55 个单位的继承范围不变。

证据：`round2/prompt-checks.json`、`d6/STATUS.json`、`d8/STATUS.json`、`d8/manifest.json`。提示词和材料的首轮副本保存在 `round2/d6/`、`round2/d8/`。

## 修改与保护核对

公开仓库只修改上述 Blueprint 三处判据/文字、`acceptance-inventory.json` 的来源身份元数据及本报告。验收清单的 325 条正文和所有非 `source` 字段不变；逐条 JSON Pointer 仍与当前 Blueprint 一致。`source.sha256` 同步本轮字节身份，`source.working_tree_uncommitted=true`，没有把未提交文件标为已发布。

Blueprint 内 `versions` 与本轮修改前完全相同；`versions/0.1/` 下历史文件，以及 SPEC、MERGE_DECISIONS、REVISION_0.2_PLAN、FREEZE_EXPLANATION 原件均未改。没有修改 production source、角色档次、检查器规则或 schema，没有冻结、commit、push 或发布。报告只写公开设计与相对证据路径；本机执行路径和日志保存在工作区证据目录。

首轮原报告保存在 `round2/REPORT-before.md`，首轮证据仍留在原位置；第 2 轮检查、逐项归属及保护核对以 `round2/` 下文件为准。完成时间与文件哈希见 `round2/final-checks.json`、`evidence-manifest.json`。
