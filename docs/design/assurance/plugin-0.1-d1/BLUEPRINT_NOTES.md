# D1 Blueprint 更新与草稿检查说明

已按 `MERGE_DECISIONS.md` 第 1、2 节和 `SPEC.md` 更新 [blueprint.json](blueprint.json)。三项原开放问题均已写成具体设计终点。离线、在线草稿检查都没有确定的内容缺口，均返回 2，表示检查尚未完整完成；不能据此宣布 D5–D8 通过或设计冻结。没有需要设计负责人重新选择方案的地方。

## 修改范围

在 `design/assurance-plugins-0.1-merged` 分支从 A 原稿复制后修改，只新增本目录的 `blueprint.json` 和本说明。A 原稿、合并规格和裁决文件均未改动；没有提交、推送或切换分支，也没有修改检查器源码。

没有新增或删除节点，保留原节点、端口和连接编号。以下 16 个节点有内容或接口更新；此外，全体节点的验收未运行说明从 D2 候选改为 D1 合并设计，仍保留 `not-run` 与空运行记录：

| 节点 | 已写入的改动 |
| --- | --- |
| `state` | 按规格第 1.1 节加入追加式 `history/events.jsonl`，保存 `event_id,at,actor,kind,state_revision,refs`；当前状态仍由 `STATE.json` 决定 |
| `dispatch` | 写入第 2.2 节的七级固定优先顺序，只取首个成立条件；允许并行的角色以明确批次派发，同一状态修订得到同一下一动作 |
| `revision` | 替换旧的三叶节点条件，写入至多两个既有节点、接口和已复述文字不变、九项语义哈希不变等全部小修条件与批准继承规则 |
| `metrics` | 明确原始事件日志用于重建三项衡量，并保留去重与原始记录要求 |
| `role-D5` | 输入改为已裁决的两档检查约定 |
| `role-D8` | 使用合并规格的角色卡：小修按第 5.1 节保留原复述和文字哈希，追加继承说明，不伪造复述 |
| `gates` | 写入 Blueprint 维护源的草稿、冻结两档入口及三态结果；检查未完成不能记通过 |
| `freeze` | 写入含 `semantic_hash` 的冻结记录；九项内容以键排序、UTF-8、无多余空白的规范化 JSON 拼接后计算 SHA-256；与当前内容不一致时拒绝交付派发 |
| `q-checker` | 原 Q1 关闭，改为“草稿与冻结检查”具体设计；依据为裁决第 2.3 节和规格第 6.2 节，保留被拒方案及理由 |
| `q-inheritance` | 原 Q2 关闭，保留编号并改为批准继承具体设计；文档版本加一、语义版本不变，原批准与原 D6–D8 记录按原范围有效，只重跑 D5；任一条件无法证明按大改 |
| `sign` | 用第 7.5 节十三项签发清单替换八项清单，逐项记 `yes/no/unknown`；单独保留最后一次证据后候选未变、权限边界未越界等条目 |
| `source-layout` | 保留原目录与分发设计；将表格内触发占位词检查的“TODO”改成同义中文“待办” |
| `execution-package` | 写入十二插件、三十二技能预算及正式市场接入，保留旧插件和旧技能；不采用先直接安装包的过渡方案 |
| `minimum` | 移除等待三项设计裁决的旧说法，保留检查器实际通过前不能宣称完整冻结和交付能力可用的要求 |
| `capability-check` | 使用合并规格第 10.2 节，去除私有试跑定位，只保留按授权提取去项目信息后的通用规则这一边界 |
| `q-capacity` | 原 Q3 关闭，改为“市场容量调整”具体设计，引用用户裁决第 2.1 节 |

三条原裁决连接同步更新了传递内容和说明。十四条需求均改为引用合并稿；小修、检查器、容量节点在需求路线中移到使用其决定的节点之前。源码、构建、真实环境三条正常走查同步了事件、调度、容量、检查、语义摘要与十三项签发；安装环境走查无需改动。`fail-checker` 改为检查入口不可用或外部来源不可访问时保留无法判断，`fail-package` 改为按已定容量修复，不再把 Q1/Q3 交回重新选择；对应反例、技术说明和读者说明同步更新。没有新增失败处理选择。

## 数量

| 内容 | 数量 |
| --- | ---: |
| 节点 | 54 |
| 叶节点 | 47，全部为具体设计终点 |
| 新增节点 / 关闭的开放问题 / 剩余开放问题 | 0 / 3 / 0 |
| 需求 | 14 |
| 有向连接 | 48，其中更新 3 条 |
| 正常走查 | 4，覆盖源码、构建、安装、真实环境，共 22 步 |
| 系统失败路径 | 9，共 20 个步骤和 9 段整体说明 |
| 失败四问 | 4，均有对应路径 |
| 节点验收器 | 63，全部未运行 |
| 依据记录 | 11，新增 `e-merge` |
| 冻结历史 | 0，`versions: []` |

以上数量描述设计内容，不表示插件已经实现或这些场景已经执行。

## 草稿检查

检查器分支为 `fix/draft-check-tier-20261111`，本次读取的提交为 `e14d7e4442445d555c90141a348675fbd598c7ae`。只运行现有检查入口，运行时报告由检查器写入其 `content/.cache/content-report.json`。该机器缓存不作为公开交付文件。

首次调用时终端没有 `npx`，退出码 127，检查未启动。加载机器已有的 `nodejs/24.16.0` 后，按以下命令实际运行。为避免公开文件记录本机绝对路径，这里用 `BLUEPRINT_WORKTREE` 和 `ASSURANCE_WORKTREE` 分别代表用户指定的检查器工作树与本次设计工作树；实际传入的是新 JSON 的绝对路径。

```bash
module load nodejs/24.16.0
cd "$BLUEPRINT_WORKTREE/content"
npx tsx check.mjs --stage draft --offline "$ASSURANCE_WORKTREE/docs/design/assurance/plugin-0.1-d1/blueprint.json"
npx tsx check.mjs --stage draft "$ASSURANCE_WORKTREE/docs/design/assurance/plugin-0.1-d1/blueprint.json"
```

第一次成功启动的离线检查返回 1，仅有两项占位词缺口，均为表格内“TODO”的字面误报；已以“待办”替换，未改变设计。随后离线检查无缺口才进入在线检查。最后同步需求顺序和三个已裁决节点的反例后，又按离线、在线顺序检查了最终同一份 JSON，结果如下：

| 最终检查 | 退出码 | 确定缺口 | 需人工审查的解释 | 未完成项 |
| --- | ---: | ---: | ---: | ---: |
| 离线草稿 | 2 | 0 | 92 | 3 |
| 在线草稿 | 2 | 0 | 92 | 18 |

离线三项未完成：启用 `--offline` 未核实 Git、外链和 npm；没有 `readability-review.json`；没有 `questions.json`。

在线十八项未完成：上述两份读者记录仍缺失；另外有 10 项 `git-source`、6 项 `github-link` 无法核实，统一原因为“未配置此GitHub来源的本地只读位置”。检查器现有来源映射没有覆盖 `YuukiAS/AI_Skills_Collection`。没有为绕过它而改 JSON 的公开仓库地址、写本机路径或修改检查器；这十六项须由检查器维护方补齐定位支持后重查。两份真实读者记录须由后续读者检查产生，不能合成。

92 项人工解释仍保留，主要涉及依据对主张的支持、是否遗漏同一事实的重复来源、外部摘录，以及九条失败路径是否可合并的提示。本次未把它们记为已完成的独立审阅，也没有据此自行合并失败路径。

另做了本地 Git 对象存在性检查：9 个去重的提交或提交加文件定位全部存在；原稿逐字节等于当前 HEAD 中的版本。该补充核对只证明本地对象存在，不能替代检查器尚未完成的在线来源核实。

## 来源与文件身份

合并稿相关的顶层来源和依据记录均绑定当前分支实际 HEAD：`66e670997525e3ad4d6fe4f5d27a795aa17eabee`，对应 `docs/design/assurance/plugin-0.1-d1/SPEC.md` 和 `MERGE_DECISIONS.md`。原有流程、生成器等依据保留其真实历史提交，没有把旧观察改写成新运行。新 JSON 和本说明尚未提交，没有自己的提交号；以该 HEAD 加相对路径说明工作树改动，不声称它们已经存在于该提交中。当前没有冻结历史，因此没有虚构版本的 `provenance`。

新 JSON 的 SHA-256：

```text
6931b4c6d5ed2a2cbe73d11076ee25d4773cb6ef9832b286875aed9e1ae235f1
```

按用户指定正则对新 JSON 和本说明做公开信息自查，匹配数为零。没有修改生产源文件、生成包、版本号或发布记录。后续需要的是实际读者记录、检查器来源定位支持及规定关卡，不需要设计负责人再决定本次三项已裁决方案。


## 续：D7 冷读后三项补定同步（2026-11-11）

已完整读取 D1 提交 `e750a9c6ff3926815d6d75cf34ac2c13dd54709d` 中的 SPEC 第 6.2 节末尾“上游改造的归属”、第 6.5 节、第 10.1 节，以及 MERGE_DECISIONS 第 5 节，并据此更新本 JSON。本节是本轮追加记录；前文的检查结果、来源提交和文件摘要保留为上一轮历史，当前结果以本节为准。没有新增设计选择，也没有提交、推送或切换分支。

### 本轮修改

- `freeze`：按第 6.5 节原文写入三个身份、首次冻结五步、语义哈希的逐字段范围及排除项。第 6.4 节的旧 `blueprint_sha256` 必填项改为 `snapshot_sha256` 与 `bundle_sha256`；删除“不覆盖错字说明”的旧解释，改为九个合同节点内的错字也会改变语义哈希、须按大改重新批准。输出接口、验收条款和反例同步。
- `gates`、`q-checker`：写入独立前置检查器的已交付归属、固定提交和只调用不修改上游的边界；关卡结果绑定同一 `snapshot_sha256`，追加历史后另用冻结档核对获批内容未变。影响完成语义的义务必须写在或明确引用到九个合同节点，只出现在其他节点算缺口，由 D5、D6 检查。
- `revision`、`q-inheritance`：照录第 6.5 节的覆盖、排除、计算、完整性义务和保守代价，并同步接口及验收；九个合同节点之外的错字，仍须满足第 5.1 节全部小修条件。
- `minimum`：使用本次提交的第 10.1 节，删除“冻结前可以继续实现其他部分”及“D5适配需要的上游工作由D1决定范围”的旧说法。冻结前不开始任何插件实现，只允许 D4 现实核查和材料整理；X2 只接入已经交付的固定检查器，不修改上游。
- `dispatch`、`state`：调度不得在冻结前派插件实施；状态说明区分批准、语义判断和文件存档三个身份，首次冻结按五步推进，没有增加另一套状态格式。
- `role-D5`：同步来自检查器的固定入口信息；`role-X1`：同步交接接口与验收，接收时核对完整冻结文件的 `bundle_sha256`。
- `q-capacity`：仅随合并稿依据更新提交定位，没有改变容量决定。

语义哈希规则照录在 `freeze`、`revision` 和 `q-inheritance`：固定顺序的九个合同节点取 `id,title,description,requirementIds,inputs,outputs,claims,authority,interface` 及每个验收器的 `id,name,required,oracle,method,criteria,environment,runner,counterexample`，再加这些节点引用的需求对象全文；排除 `designStatus,implementationStatus,evidenceIds,ringLabel,children` 及验收器的 `status,notRunReason,runs`，按规范化 JSON 依次拼接后计算 SHA-256。没有自行发明“语义片段”抽取办法。

首次冻结顺序是：同一内容快照的 D5 草稿档、D6、D7、D8 全部通过，用户批准该快照，冻结命令追加首版，D5 冻结档确认获批快照未变，最后才写含三个身份的 `freeze.json`。第 4 步不通过不写记录，交 D1 查明原因；快照未变时原关卡和批准继续有效。

同步更新三条连接：`c-gates-to-freeze`、`c-freeze-to-role-X1`、`c-q-checker-to-role-D5`。源码、构建和真实环境走查同步了实施前提、九项完整性、快照批准与冻结后的身份核对。现有 `fail-checker` 路径补充了追加历史后快照不一致的已定收场：检查入口或来源不可访问保留无法判断，冻结档不通过或内容不符则不写冻结记录，交 D1 查明原因，冻结前不实施；对应反例与注入绑定同步。没有新增节点、连接、走查或失败路径。

节点仍为 54、需求 14、连接 48、正常走查 4（22 步）、失败路径 9（20 步及 9 段整体说明）、验收器 63；均未借本次文档同步声明插件验收通过。新增 `e-checker-prerequisite` 后依据记录为 12；冻结历史仍为 `versions: []`。

### 需要重新复述的全部单位

以本轮开始时 HEAD 中的 JSON 为基线，调用固定检查器 `content/readability.ts` 的实际 `readerHash` 比较六项读者文字，并逐项核对差异。共 10 个单位的文字哈希改变，完整列表如下；其余 41 个单位的读者文字哈希未变。

| 复述单位 id | 类型 | 改动的读者字段 |
| --- | --- | --- |
| `ws-state` | 正常步骤 | `expectedResult` |
| `ws-dispatch` | 正常步骤 | `expectedResult` |
| `wb-source` | 正常步骤 | `exampleData`, `onError` |
| `wr-contract` | 正常步骤 | `expectedResult`, `onError` |
| `wr-gates` | 正常步骤 | `exampleData`, `expectedResult` |
| `wr-freeze` | 正常步骤 | `action`, `exampleData`, `expectedResult`, `why`, `onError` |
| `wr-owner` | 正常步骤 | `exampleData`, `expectedResult` |
| `fail-checker-whole` | 失败路径整体收场 | `action`, `exampleData`, `expectedResult`, `onError` |
| `fail-checker-step-1` | 失败步骤 | `exampleData` |
| `fail-checker-step-2` | 失败步骤 | `action`, `exampleData`, `expectedResult`, `onError` |

这些单位应由后续 D8 交给新的独立读者检查，不能沿用旧文字的通过记录。本次没有生成读者复述、补签记录或冻结历史。走查的技术说明和 `walk-built` 入口也同步了对应规则，但它们不属于上述六项读者文字，未单独伪造复述单位。

### 本轮草稿检查

检查器工作树保持 `fix/draft-check-tier-20261111`，实际提交为 `c05edcf51bc93f8be82180fd4ad28a250937f195`。先加载已有 `nodejs/24.16.0`，再依次运行离线、在线草稿档各一次，没有修改检查器源码。下列变量仅代指用户指定的两个工作树；实际调用传入新 JSON 的绝对路径，公开文件不记录本机定位。

```bash
module load nodejs/24.16.0
cd "$BLUEPRINT_WORKTREE/content"
npx tsx check.mjs --stage draft --offline "$ASSURANCE_WORKTREE/docs/design/assurance/plugin-0.1-d1/blueprint.json"
npx tsx check.mjs --stage draft "$ASSURANCE_WORKTREE/docs/design/assurance/plugin-0.1-d1/blueprint.json"
```

| 本轮检查 | 退出码 | 确定缺口 | 需人工审查的解释 | 未完成项 |
| --- | ---: | ---: | ---: | ---: |
| 离线草稿 | 2 | 0 | 92 | 3 |
| 在线草稿 | 2 | 0 | 92 | 2 |

离线检查时间为 `2026-11-11T17:44:09.088Z`；三项未完成分别是离线未核实来源、缺 `readability-review.json`、缺 `questions.json`。在线检查时间为 `2026-11-11T17:44:42.757Z`；只剩上述两份读者记录缺失，上一轮的 16 项 Git 来源与链接定位未完成项已不再出现。结果 2 仍表示检查未完整完成，不能记为完整通过。92 项人工解释保留，不冒充独立审阅已完成。

合并稿依据已更新到 `e750a9c6ff3926815d6d75cf34ac2c13dd54709d`；检查器依据固定到上述完整提交号。JSON 的本轮改动没有自己的提交号，不声称已存在于这些提交中。原规格、裁决稿和 A 原稿未改动。

本轮新 JSON 的 SHA-256：

```text
0111f023f7bf503f72bee7c3dc8e7ba6406507c5f68c1786809e0a0da9b74dce
```

按与上一轮相同的正则检查本 JSON 和整份说明，匹配数为零。本轮没有需要 D1 新增裁决的事项；尚待实际读者记录和规定关卡，未宣布设计冻结或插件实现完成。


## 续：D7 第 2 轮补定同步（2026-11-11）

已完整读取 D1 提交 `53af663d61284727e6ee9d7dd76a5ce97867a7ec` 中 SPEC 第 6.5 节“semantic_hash 覆盖的范围（D7 第 2 轮后修订）”、第 7.5 节的整份一次签发与签发后撤回、第 1.4 节新增记录种类，以及 MERGE_DECISIONS 第 6 节，并同步到 JSON。没有新增设计选择；前两轮说明保留为历史，本轮规则和检查结果以本节为准。

### 修改的节点与规则

- `freeze`、`revision`、`q-inheritance`、`gates`：删除仅九个合同节点的哈希投影、九节点内错字一律大改、只在其他节点出现即视为遗漏的旧规则，改为完整写入最新第 6.5 节。哈希覆盖全部需求、连接、所有节点的规定定义字段和 `childIds`、验收器定义字段、全部正常走查与失败路径；只排除已指定的进度、运行和出处字段。按 Blueprint 原有顺序组成对象，再以键排序、UTF-8、无多余空白的规范化 JSON 计算 SHA-256，不解析引用或人工抽取“语义片段”。
- `revision`、`q-inheritance`：保留至多两个既有节点等窄范围条件，将旧的“哈希必须不变”改为第 6.5 节规定的相等或完整继承链核验。哈希变化只说明定义内容变了，不自动等于大改。D1 的小修继承记录包含 `from_semantic_hash`、`to_semantic_hash`、字段级差异、逐条等价理由和新 D5 结果。其余小修限制、前后告知及原读者记录的有效范围不放宽。
- `dispatch`、`freeze`、`sign`：当前哈希须等于获批值，或从获批值出发沿完整继承链到达当前值。链条断开、任一记录不符合第 5.1 节条件或经过大改记录，都拒绝派发并退回 D1；验收条款和反例同步。首次冻结五步与内容快照、定义哈希、完整文件三个身份的分工继续保留。
- `sign`：使用本次提交第 7.5 节全文，删去分单元签发许可，0.1 只支持对整个冻结范围一次签发；确需分批交付时，在设计阶段拆成多个各自冻结和签发的任务。十三项签发清单仍保留。
- `state`、`dispatch`、`sign`、`evidence`：写入签发后复核的两个动作与维持、撤回分支。先登记新事实、暂停对外交付声明，`phase` 从 `delivered` 回 `delivery`，`step=X1-review-release`，暂保留原 `delivery.release_ref`；X1 核对后决定 `upheld` 或 `revoked`。维持则回 `delivered`；撤回则当前签发引用置 `null`、指定证据标 `stale`，进入 `X1-repair`，命中五类设计退回条件才进入 `X1-design-return`。原签发永不改写、永不删除；按正常返修重验后新签发的 `supersedes` 指向被撤回签发。
- `record-check`：允许记录种类增加 `revocation`，核对 `release_ref` 指向的签发确实存在；验收中增加字段、决定值及引用错误的反例。入口仍只读，不代 X1 决定维持或撤回。

不可变记录路径为 `delivery/revocations/<revocation_id>.json`，字段原样写入：`schema_version:"assurance-revocation/0.1",revocation_id,task_id,release_ref,decision,trigger_ref,evidence_refs,invalidated_evidence,reason,decided_by,decided_at`；`decision` 只取 `upheld` 或 `revoked`。本次没有实际生成这些业务记录，只更新设计。

`q-checker`、`role-X1`、`minimum`、`q-capacity` 只随本轮 D1 来源提交更新引用，没有改变其检查器、交接、冻结前禁实现或容量决定。合并稿依据定位统一更新到本轮提交，其他历史依据和固定检查器提交保持原样。

连接 `c-q-inheritance-to-revision` 同步传递完整继承链及所需字段。新增 `fail-revocation`，检测组件和单步路线均为既有 `sign` 节点；情景直接取自 D1 的“签发后出现可能推翻原签发结论的新事实”，收场照录暂停、维持或撤回的既定流程，配套 `v-fail-revocation` 的反例注入和用户可见结果。未新增角色、分单元状态或额外决策。

当前数量为 54 个节点、14 条需求、48 条连接、4 条正常走查（22 步）、10 条失败路径（21 步及 10 段整体说明）、12 条依据记录。验收器由 63 增至 64，全部仍为 `not-run` 且运行记录为空；`versions: []` 保持不变。

### 受影响的全部复述单位

用固定检查器 `content/readability.ts` 的实际 `readerHash`，与本轮开始时 HEAD 中的 JSON 比较六项读者文字。5 个原有单位的哈希改变，新增撤回路径有 2 个新单位，完整清单如下：

| 复述单位 id | 类型 | 修改或新增内容 |
| --- | --- | --- |
| `ws-state` | 正常步骤 | `expectedResult` |
| `ws-dispatch` | 正常步骤 | `expectedResult` |
| `wr-contract` | 正常步骤 | `expectedResult`、`onError` |
| `wr-owner` | 正常步骤 | `exampleData` |
| `wr-sign` | 正常步骤 | `action`、`expectedResult`、`onError` |
| `fail-revocation-whole` | 失败路径整体收场 | 新增，六项读者文字均需复述 |
| `fail-revocation-step-1` | 失败步骤 | 新增，六项读者文字均需复述 |

原有另外 46 个单位的读者文字哈希未变。上述 7 个单位须交新的独立读者复述；不能沿用旧文字通过记录，也没有在本轮合成读者记录。

### 本轮检查与文件身份

检查器工作树保持 `fix/draft-check-tier-20261111`，提交为 `c05edcf51bc93f8be82180fd4ad28a250937f195`。加载已有 `nodejs/24.16.0` 后，离线、在线草稿档各实际运行一次；仅检查器运行时写其既有缓存报告，未修改检查器源码。变量代表用户指定的工作树，实际调用传入 JSON 的绝对路径，公开文件不记录本机路径。

```bash
module load nodejs/24.16.0
cd "$BLUEPRINT_WORKTREE/content"
npx tsx check.mjs --stage draft --offline "$ASSURANCE_WORKTREE/docs/design/assurance/plugin-0.1-d1/blueprint.json"
npx tsx check.mjs --stage draft "$ASSURANCE_WORKTREE/docs/design/assurance/plugin-0.1-d1/blueprint.json"
```

| 本轮检查 | 退出码 | 确定缺口 | 人工解释待审 | 未完成项 |
| --- | ---: | ---: | ---: | ---: |
| 离线草稿 | 2 | 0 | 92 | 3 |
| 在线草稿 | 2 | 0 | 92 | 2 |

离线检查时间为 `2026-11-11T17:57:41.161Z`，未完成项为离线未核实来源、缺 `readability-review.json`、缺 `questions.json`。在线时间为 `2026-11-11T17:58:29.467Z`，只剩这两份读者记录缺失。两次均无确定内容缺口，但退出码 2 仍不能记完整通过；92 项人工解释未当作独立审阅已完成。本轮没有实施或运行插件的哈希核验、签发、维持、撤回逻辑。

新 JSON 的 SHA-256：

```text
1b2ff929979962afba3019b47126f2405d726c488d5f16bf419e25bb9759aced
```

本轮只修改 `blueprint.json` 并在本说明追加记录；原规格和裁决文件未改，未 commit、未 push、未切分支。新改动尚无提交号，仅以本轮 HEAD 加路径和上述文件摘要标识，不声称这些改动已写进该提交。公开信息按原正则自查，新 JSON 和整份说明匹配数均为零。没有需要 D1 追加决定的事项，尚待实际读者记录和规定关卡。


## 续：D7 第 3 轮补定同步（2026-11-11）

已完整读取当前分支最新提交 `06672776a40d75b659dacf59ef458b7325f659f1` 中 SPEC 第 6.5 节“按排除法计算（D7 第 3 轮后改定）”“计算”“派发核验，按阶段绑定不同对象”及其上下文，以及 MERGE_DECISIONS 第 7 节，并按原决定同步 JSON。前文各轮记录保留为历史，本节说明当前投影与派发规则，没有新增设计选择。

### 修改的节点与同步范围

- `freeze`、`revision`、`q-inheritance`、`dispatch`、`gates`：所有重复的哈希规则统一替换为本次第 6.5 节原文，删除列举覆盖字段、`childIds` 和按字段清单重建对象的旧说法。以 `snapshot_sha256` 使用的同一 `snapshotOf` 内容快照为起点，只删除明确排除的字段，其余全部保留，再按键排序、UTF-8、无多余空白的规范化 JSON 计算 SHA-256。
- 排除清单原样保留三类：每个节点及其子节点的 `designStatus,implementationStatus,evidenceIds,ringLabel`；每个验收器的 `status,notRunReason,runs`；顶层 `sources,evidence,title,summary,complexityNote`。节点 `terminal` 中的 `mechanism,acceptance,retry,packages` 等、顶层 `failureQuestions` 及将来新增的字段默认参与计算；只有 D1 能改动排除清单，没有自行增加排除项。
- `dispatch`：输入、输出、接口、机制、验收条款及反例均写明每次派发在 `based_on` 中登记绑定对象。D2–D8，包括小修后的 D5 和大改后的整轮关卡，只核对本次受审 `snapshot_sha256`，不查批准链，首次冻结前可以正常派发。X1 接收及 X2–X5 的实施、验收、专项与裁判绑定有效冻结对象，才核对获批哈希或完整合格的小修继承链；链条断开、条件不符或经过大改记录则拒绝这次交付派发并退回 D1。
- `state`、`dispatch`：交付期间的修订草稿不影响未暂停工作，未受影响部分继续绑定原有效冻结对象；仅 `paused_scopes` 内节点暂停派发。小修继承记录写完后新值才有效，大改重新批准后才替换。冻结前不实施插件的既有边界继续保留，设计检查不再被笼统的批准链要求拦住。
- `revision`、`q-inheritance`、`freeze`、`gates`、`sign`：接口、验收或摘要中的笼统“当前哈希决定是否拒绝派发”统一限定到依据冻结合同的交付工作，并同步分阶段规则。签发后的暂停、维持、撤回及整份一次签发规则没有改变。

`record-check`、`q-checker`、`role-X1`、`evidence`、`minimum`、`q-capacity` 只随 D1 新提交更新依据定位，未改变本轮之外的设计。固定检查器提交仍为 `c05edcf51bc93f8be82180fd4ad28a250937f195`。

`c-dispatch-to-prompts` 同步携带派发阶段和 `based_on` 的绑定对象；`c-q-inheritance-to-revision` 把批准链校验范围限定为交付工作。走查 `ws-dispatch` 写明首次冻结前的设计派发不查批准链、交付草稿不阻断未暂停工作；`wr-contract` 改为解释排除式投影。`wr-freeze` 仅更新技术说明中的哈希计算定位。所有失败路径保持原样，没有新增节点、连接、走查或失败路径。

数量仍为 54 个节点、14 条需求、48 条连接、4 条正常走查（22 步）、10 条失败路径（21 步及 10 段整体说明）、12 条依据记录、64 个验收器。验收器仍全部 `not-run`，运行记录为空；`versions: []` 不变。

### 全部受影响复述单位

以本轮开始时 HEAD 中的 JSON 为基线，实际调用固定检查器 `content/readability.ts` 的 `readerHash` 比较六项读者文字。只修改以下 2 个复述单位，没有新增单位；其余 51 个单位的读者文字哈希未变。

| 复述单位 id | 类型 | 改动字段 |
| --- | --- | --- |
| `ws-dispatch` | 正常步骤 | `exampleData`、`expectedResult`、`why`、`onError` |
| `wr-contract` | 正常步骤 | `expectedResult` |

上述两个单位需由后续独立读者重新复述；本次没有生成或补签读者记录。`wr-freeze` 仅技术说明改变，不改变它的六项读者文字，因此未计入受影响复述单位。

### 本轮检查与文件身份

检查器分支保持 `fix/draft-check-tier-20261111`，提交仍为上述 `c05edcf` 完整提交。先加载机器已有 `nodejs/24.16.0`，再实际运行离线、在线草稿档各一次；未修改检查器源码。下列变量代指用户指定的两个工作树，实际命令传入 JSON 的绝对路径，公开文件不记录本机路径。

```bash
module load nodejs/24.16.0
cd "$BLUEPRINT_WORKTREE/content"
npx tsx check.mjs --stage draft --offline "$ASSURANCE_WORKTREE/docs/design/assurance/plugin-0.1-d1/blueprint.json"
npx tsx check.mjs --stage draft "$ASSURANCE_WORKTREE/docs/design/assurance/plugin-0.1-d1/blueprint.json"
```

| 本轮检查 | 退出码 | 确定缺口 | 人工解释待审 | 未完成项 |
| --- | ---: | ---: | ---: | ---: |
| 离线草稿 | 2 | 0 | 92 | 3 |
| 在线草稿 | 2 | 0 | 92 | 2 |

离线检查时间为 `2026-11-11T18:08:10.278Z`，未完成项为离线未核实来源、缺 `readability-review.json`、缺 `questions.json`。在线检查时间为 `2026-11-11T18:08:51.214Z`，只剩上述两份读者记录缺失。两次均无确定内容缺口，但退出码 2 仍不能记完整通过；92 项人工解释没有冒充独立审阅。本轮没有实际运行插件的排除式哈希或分阶段派发实现。

新 JSON 的 SHA-256：

```text
2a09885312849d5a6c0e293a8fe0df5262f76b701cb0232b90b0e064294ea7fb
```

合并稿依据更新到 `06672776a40d75b659dacf59ef458b7325f659f1`。JSON 本轮改动没有自己的提交号，按该 HEAD 加路径及上述摘要定位，不声称已经存在于该提交中。本轮只改 JSON 并追加本说明，SPEC、MERGE_DECISIONS 和 A 原稿保持不变；未 commit、未 push、未切分支。新 JSON 与整份说明按相同正则自查，匹配数均为零。没有需要 D1 新增决定的事项，尚待真实读者记录及规定关卡。


## 续：D7 第 4 轮补定同步（2026-11-11）

已完整读取最新提交 `d530fed6192b69b1562459fa88305c6f49db3b63` 中 SPEC 第 6.5 节新增的“生成设计或核查事实的角色（D2、D3、D4）”及相关派发规则，以及 MERGE_DECISIONS 第 8 节，并按原决定更新 JSON。本节追加记录当前规则，前文各轮保留为历史；没有新增设计选择。

### 修改的节点与规则

- `clarify`：明确 D1 在 `D1-clarify` 结束时写不可变文件 `design/briefs/<brief_version>.json`。任务书只含需求、已有决定和事实，不含设计倾向；D2、D3 读同一份。需求改变而重新设计或大改时，D1 写新版本。
- 任务书字段按原文写为 `schema_version:"assurance-brief/0.1",task_id,brief_version,requirements,user_decisions,facts,open_questions,read_allowlist,read_denylist,created_at`。其中需求带原话出处，事实带来源，开放事项限设计者可处理的范围；保留已定读限，没有另添任务书字段、字段类型或哈希计算算法。
- `state`：在文件布局增加任务书位置，在已有 `dispatches` 字段说明 D2/D3/D4 的派发记录通过 `based_on.brief_sha256` 引用任务书身份。任务书出新版本后，旧版绑定结果标 `stale`，交 D1 判断还能支持的部分；没有另造任务书状态库或顶层状态字段。
- `dispatch`：输入、输出、接口、机制、验收和反例都区分三类对象：D2/D3/D4 的 `based_on` 写 `brief_sha256`；D5–D8 仍绑定受审 `snapshot_sha256`，不查批准链；交付工作继续绑定有效冻结对象。尚无 Blueprint 时也可派出独立设计，不要求 D1 先提供起始设计。
- `role-D2`、`role-D3`、`role-D4`：角色卡、输入、输出及验收绑定任务书身份；两位独立设计者同一任务书，互不读设计产物。D4 在正式任务书之前需要核查事实时，由 D1 先写仅含待核实问题的任务书版本，派发仍绑定该版本的 `brief_sha256`。
- `writer`：结果采纳时按本次角色核对绑定对象，不再对 D2/D3/D4 统一要求已有 Blueprint 内容身份；任务书换版后的旧结果保留并标 `stale`，不直接当当前结果采纳。
- `prompts`：提示词模板及读入清单加入任务书位置和身份，按角色提供任务书、受审快照或有效冻结对象，不让用户补找材料。`clarify` 的被拒方案按裁决加入：不由 D1 起始 Blueprint 给设计者共同基线，也不限制为只能接已有 Blueprint 的任务。
- `record-check`：已有只读记录检查设计增加 `brief` 种类，写明任务书路径和上述既定字段；仅检查结构和已声明引用，不负责写任务书或代替 D1 判断设计倾向。

`freeze`、`revision`、`q-inheritance`、`gates` 及 `state` 中重复的派发规则都同步了本轮原文，删除原先 D2–D8 一律绑定受审快照的说法。其他仅引用合并稿的节点更新来源提交；固定检查器仍为 `c05edcf51bc93f8be82180fd4ad28a250937f195`，排除式语义哈希、有效冻结对象、修订继承和签发撤回规则保持原决定。

同步四条已有连接：`c-dispatch-to-prompts`、`c-prompts-to-role-D2`、`c-prompts-to-role-D3`、`c-clarify-to-role-D2`。源码走查现在明确从澄清完成的无设计倾向任务书进入派发，随后交独立设计并核对返回的任务书版本。没有新增节点、连接、正常走查或失败路径，全部失败路径与本轮基线逐项相同。

数量仍为 54 个节点、14 条需求、48 条连接、4 条正常走查（22 步）、10 条失败路径（21 步及 10 段整体说明）、12 条依据记录、64 个验收器。验收器仍全部 `not-run` 且运行记录为空；`versions: []` 保持不变。本轮只写 Blueprint，没有创建真实受管任务的任务书、状态记录或检查脚本。

### 全部受影响复述单位

以本轮开始时 HEAD 中的 JSON 为基线，调用固定检查器 `content/readability.ts` 的实际 `readerHash` 比较六项读者文字。5 个原有单位的文字哈希改变，完整列表如下；没有新增复述单位，其余 48 个单位哈希未变。

| 复述单位 id | 类型 | 改动字段 |
| --- | --- | --- |
| `ws-state` | 正常步骤 | `exampleData`、`expectedResult` |
| `ws-dispatch` | 正常步骤 | `exampleData`、`expectedResult`、`why`、`onError` |
| `ws-prompts` | 正常步骤 | `exampleData`、`expectedResult` |
| `ws-designer` | 正常步骤 | `exampleData`、`expectedResult` |
| `ws-owner` | 正常步骤 | `exampleData`、`onError` |

这 5 个单位须交后续独立读者重新复述，不能复用旧文字的通过记录。本次没有生成或补签读者记录。源码走查入口与技术说明同步了任务书前提，但没有据此伪造额外复述单位。

### 本轮检查与文件身份

检查器分支保持 `fix/draft-check-tier-20261111`，实际提交为 `c05edcf51bc93f8be82180fd4ad28a250937f195`。先加载已有 `nodejs/24.16.0`，再实际运行离线、在线草稿档各一次；未修改检查器源码。下列变量代指用户指定的两个工作树，实际命令传入 JSON 的绝对路径，公开文件不记录本机路径。

```bash
module load nodejs/24.16.0
cd "$BLUEPRINT_WORKTREE/content"
npx tsx check.mjs --stage draft --offline "$ASSURANCE_WORKTREE/docs/design/assurance/plugin-0.1-d1/blueprint.json"
npx tsx check.mjs --stage draft "$ASSURANCE_WORKTREE/docs/design/assurance/plugin-0.1-d1/blueprint.json"
```

| 本轮检查 | 退出码 | 确定缺口 | 人工解释待审 | 未完成项 |
| --- | ---: | ---: | ---: | ---: |
| 离线草稿 | 2 | 0 | 92 | 3 |
| 在线草稿 | 2 | 0 | 92 | 2 |

离线检查时间为 `2026-11-11T18:19:15.785Z`，未完成项为离线未核实来源、缺 `readability-review.json`、缺 `questions.json`。在线检查时间为 `2026-11-11T18:20:00.310Z`，只剩上述两份读者记录缺失。两次均无确定内容缺口，退出码 2 仍不能记完整通过；92 项人工解释未当作独立审阅完成。本轮没有实际运行任务书生成、派发、换版或 `brief` 记录检查实现。

新 JSON 的 SHA-256：

```text
58b999ea31aa6e1450d39da46824819613e530d28332f382b024453f193bb615
```

合并稿依据更新到 `d530fed6192b69b1562459fa88305c6f49db3b63`。本轮 JSON 改动没有自己的提交号，以本轮 HEAD 加路径及上述摘要定位，不声称已存在于该提交中。只修改 JSON 并追加本说明，SPEC、MERGE_DECISIONS 和 A 原稿未改；未 commit、未 push、未切分支。新 JSON 和整份说明按相同正则做公开信息自查，匹配数均为零。没有需要 D1 新增决定的事项，尚待真实读者记录及规定关卡。


## 续：规划端角色每轮最多手动转交一次（用户要求，2026-11-11）

已完整读取最新提交 `0282199a26c1d437f25eae6f2532485831d57e16` 中 SPEC 第 2.1a 节全文、第 2.1 节表格的 D8 行，以及 MERGE_DECISIONS 第 11 节，并按原决定更新 JSON。限制只针对需要用户手动转交的规划端角色，每角色每轮最多一条提示词；执行端 Codex 由负责人直接派发，次数不限，不占用户的转交次数。本节是本轮追加记录，没有新增设计选择。

### 修改的节点与规则

- `dispatch`：在角色表之后原样加入第 2.1a 节，D8 行使用最新规格。同步输入、输出、接口、验收和反例；将旧的 GPT 负责人把外派工作一律交用户的表述限定为需要用户转交的规划端角色，执行端仍由负责人直接派发。既有阶段绑定、任务书、有效冻结对象及冻结前禁实施规则继续保留。
- `prompts`：提示词模板和验收写明，能自动派发时由负责人一次性批量派发，各单位新线程且只收到本单位材料；只能用户转交时，按规划端角色把整轮合成一条提示词，交给一个新线程，随机打乱单位顺序，逐个仅依据本单位文字作答，不借其他单位补全信息。执行端派发不占用户转交次数。
- `role-D8`：默认档次为规划端·普通 GPT 极高；负责人可自动派发时，允许用执行端最高推理档代替。每一步每一轮换新读者的原要求保留，由负责人批量完成；单线程合批如实记录 `reader_isolation: "single-thread-batch"`，不能声称每单位独立线程。单线程合批独立性降低，由 D1 判断时考虑；失败路径整体收场、冻结和签发相关步骤等关键单位，可以下一轮自动补做独立复述。
- `gates`：接收、派发与验收均区分自动批量独立读者和单线程合批，保留每个单位的实际复述与隔离记录，不把合批伪装为完全独立，也不要求用户逐条转交来满足默认线程要求。
- `contract-fidelity`：在原真实读者要求中明确第 2.1a 节授权的两种方式和单线程合批隔离降低，避免其他节点仍无条件要求每单位独立线程而与本次修订冲突。

其他节点仅随合并稿更新来源提交，没有改写既有哈希、任务书、撤回或容量规则。连接 `c-dispatch-to-prompts`、`c-gates-to-role-D8` 同步传递次数限制、派发方式和隔离标记。正常走查同步了规划端手动转交次数、执行端直接派发及 D8 结果记录方式；全部失败路径与本轮基线保持一致。

### 流程文档追加说明

在 `docs/design/assurance/ASSURANCE_PROCESS_V0_1_20261110.md` 的 D8 表格行之后，新增一段“2026-11-11 修订说明（D8 派发与用户转交）”，引用同仓库 `plugin-0.1-d1/SPEC.md` 第 2.1a 节，写明次数限制的适用范围、两种派发方式、隔离标记、D1 判断和 D8 档次例外。原表格行及所有原正文均保留；移除新增段落后，文件与本轮 HEAD 中的原文件一致。没有改流程版本名或追写虚构批准。

当前数量仍为 54 个节点、14 条需求、48 条连接、4 条正常走查（22 步）、10 条失败路径（21 步及 10 段整体说明）、12 条依据记录、64 个验收器。全部验收器仍为 `not-run`、运行记录为空，`versions: []` 不变。本轮没有真正派发读者、切换模型、运行 D8 或生成单线程合批结果记录。

### 全部受影响复述单位

以本轮开始时 HEAD 中的 JSON 为基线，实际调用固定检查器 `content/readability.ts` 的 `readerHash` 比较六项读者文字。只修改以下 3 个单位，没有新增复述单位；其余 50 个单位的文字哈希未变。

| 复述单位 id | 类型 | 改动字段 |
| --- | --- | --- |
| `ws-dispatch` | 正常步骤 | `expectedResult` |
| `ws-prompts` | 正常步骤 | `expectedResult`、`onError` |
| `wr-gates` | 正常步骤 | `exampleData`、`expectedResult`、`onError` |

这三个单位须按本次第 2.1a 节安排实际复述，不能复用旧文字的通过记录。本轮没有合成或补签读者记录。

### 草稿检查与文件身份

检查器分支保持 `fix/draft-check-tier-20261111`，实际提交仍为 `c05edcf51bc93f8be82180fd4ad28a250937f195`。先加载机器已有的 `nodejs/24.16.0`，再实际运行离线、在线草稿档各一次。没有修改检查器源码；仅运行产生其既有缓存报告。下列变量代指用户指定的工作树，实际调用传入 JSON 的绝对路径，公开文件不记录本机路径。

```bash
module load nodejs/24.16.0
cd "$BLUEPRINT_WORKTREE/content"
npx tsx check.mjs --stage draft --offline "$ASSURANCE_WORKTREE/docs/design/assurance/plugin-0.1-d1/blueprint.json"
npx tsx check.mjs --stage draft "$ASSURANCE_WORKTREE/docs/design/assurance/plugin-0.1-d1/blueprint.json"
```

| 本轮检查 | 退出码 | 确定缺口 | 人工解释待审 | 未完成项 |
| --- | ---: | ---: | ---: | ---: |
| 离线草稿 | 2 | 0 | 92 | 3 |
| 在线草稿 | 2 | 0 | 92 | 2 |

离线检查时间为 `2026-11-12T03:08:27.713Z`，未完成项是离线未核实来源、缺 `readability-review.json`、缺 `questions.json`。在线检查时间为 `2026-11-12T03:09:16.827Z`，只剩上述两份读者记录缺失。两次均无确定内容缺口，但退出码 2 仍不能记完整通过；92 项人工解释不代表独立审阅完成。本次仅验证设计内容，没有验证宿主自动批量能力或单线程合批执行效果。

新 JSON 的 SHA-256：

```text
8e153e2dc7ca211cad6837e1233ef779e8fd304918d76e7961f79f9660ade63d
```

合并稿依据更新到 `0282199a26c1d437f25eae6f2532485831d57e16`。JSON、流程追加说明和本说明均为尚未提交的工作树改动，没有自己的提交号；以该 HEAD 加路径及上述摘要标识，不声称已存在于该提交中。原 SPEC、MERGE_DECISIONS 和 A 原稿未改，流程原正文未删改；未 commit、未 push、未切分支。对本轮修改的三个文件按相同正则做公开信息自查，匹配数均为零。没有需要 D1 新增决定的事项，尚待真实读者记录和规定关卡。


## 续：D8 合批结果的冻结资格（D7 第 8 轮补定）

已完整读取最新提交 `c24c2a8be4ea66cce5b3843e690a0127182aca5f` 中 SPEC 第 2.1a 节“合批结果能否作为冻结依据”及上下文，以及 MERGE_DECISIONS 第 12 节，并按原决定同步 JSON。前一轮“关键单位可以下一轮补做”的说明，在冻结资格上受本轮强制条件约束：关键单位没有合格独立复述前，不能以合批通过冻结。没有新增设计选择。

### 修改的节点与规则

- `dispatch`：普通与关键单位分开核对。普通单位的单线程合批结果经 D1 逐单位判断复述正确，可以作为 D8 有效通过，保留 `reader_isolation: "single-thread-batch"`。关键单位必须由负责人通过执行端自动派发各自独立新读者；没有任何自动派发手段时，D8 记 `unknown`，冻结等待，不增加用户转交次数，也不以合批替代。
- `role-D8`：说明正文、输入输出、验收与反例都写明上述资格；不再仅笼统要求 D1 考虑隔离降低，或把关键单位的独立复述当作通过以后可选的补做。
- `gates`：除说明、接口和验收外，专门更新 JSON 内第 6.2 节关卡表的 D8 行。普通合批经过逐条判断可以有效通过，关键单位必须独立新读者正确复述；缺自动派发手段时 D8 为 `unknown`，冻结等待。
- `contract-fidelity`：明确普通合批可用、关键单位不接受合批证据，不能以“D1 已考虑隔离降低”代替关键单位独立性要求。
- `freeze`：冻结输入、说明正文、接口及验收都增加 D8 资格条件。普通合批可按规则支持通过；关键单位必须有各自独立新读者的正确复述。无自动派发手段时，不将合批记录补成 `passed`，不进入冻结。
- `prompts`：提示词和结果说明区分两种证据资格，关键单位由负责人经执行端自动派发，不靠追加用户手动转交来完成；缺手段时明确报告 `unknown` 和冻结等待。

关键单位范围照录为两类：

1. 每条失败路径的整体收场说明，即 `failurePaths[*].explanation`。
2. `nodeId` 为 `gates`、`freeze`、`sign`、`revision`、`q-inheritance` 的所有正常走查步骤和失败步骤。

按当前 JSON 静态枚举，关键单位共 16 个：10 段失败路径整体收场、3 个正常走查步骤、3 个失败步骤；另外 37 个为普通单位。六个关键步骤的 id 为 `wr-gates`、`wr-freeze`、`wr-sign`、`fail-checker-step-2`、`fail-candidate-step-3`、`fail-revocation-step-1`。这只是按 D1 规则核对范围，不表示这些单位已经实际复述或通过。

连接 `c-gates-to-role-D8` 同步关键范围、派发责任和未知时的收场。已有 `fail-role` 路径补充 D8 关键单位无执行端自动派发手段的情景，明确 `unknown`、冻结等待、不得用合批或增加用户转交次数替代，并同步反例注入、技术说明及读者文字。没有新增失败路径或改变其他失败处理。

其他节点仅更新合并稿依据提交，没有改动既有任务书、哈希、签发与撤回决定。本轮不修改 SPEC、MERGE_DECISIONS、流程文档或 A 原稿。数量仍为 54 个节点、14 条需求、48 条连接、4 条正常走查（22 步）、10 条失败路径（21 步及 10 段整体说明）、12 条依据记录、64 个验收器。验收器仍全部 `not-run`、运行记录为空；`versions: []` 不变。

### 全部受影响复述单位

以本轮开始时 HEAD 中的 JSON 为基线，调用固定检查器 `content/readability.ts` 的实际 `readerHash` 比较六项读者文字。7 个原有单位的文字哈希改变，完整清单如下；无新增单位，其余 46 个单位文字哈希未变。

| 复述单位 id | 类型 | 改动字段 |
| --- | --- | --- |
| `ws-dispatch` | 正常步骤 | `expectedResult` |
| `ws-prompts` | 正常步骤 | `expectedResult`、`onError` |
| `wr-gates` | 正常步骤 | `expectedResult`、`why`、`onError` |
| `wr-freeze` | 正常步骤 | `exampleData`、`onError` |
| `fail-role-whole` | 失败路径整体收场 | `exampleData`、`expectedResult`、`onError` |
| `fail-role-step-1` | 失败步骤 | `exampleData` |
| `fail-role-step-2` | 失败步骤 | `exampleData`、`expectedResult`、`onError` |

这些单位须按当前资格规则取得实际复述，不能复用旧文字的通过记录；其中关键单位必须独立新读者，普通单位可以依本轮规则合批。本次没有派发 D8、生成复述或补签读者记录。

### 草稿检查与文件身份

检查器工作树保持分支 `fix/draft-check-tier-20261111`，提交为 `c05edcf51bc93f8be82180fd4ad28a250937f195`。先加载已有 `nodejs/24.16.0`，再实际运行离线、在线草稿档各一次，未修改检查器源码。下列变量代表用户指定的两个工作树，实际命令传入 JSON 的绝对路径，公开文件不记录本机路径。

```bash
module load nodejs/24.16.0
cd "$BLUEPRINT_WORKTREE/content"
npx tsx check.mjs --stage draft --offline "$ASSURANCE_WORKTREE/docs/design/assurance/plugin-0.1-d1/blueprint.json"
npx tsx check.mjs --stage draft "$ASSURANCE_WORKTREE/docs/design/assurance/plugin-0.1-d1/blueprint.json"
```

| 本轮检查 | 退出码 | 确定缺口 | 人工解释待审 | 未完成项 |
| --- | ---: | ---: | ---: | ---: |
| 离线草稿 | 2 | 0 | 92 | 3 |
| 在线草稿 | 2 | 0 | 92 | 2 |

离线检查时间为 `2026-11-12T03:20:50.277Z`，未完成项是离线未核实来源、缺 `readability-review.json`、缺 `questions.json`。在线检查时间为 `2026-11-12T03:21:41.002Z`，只剩上述两份读者记录缺失。两次均无确定内容缺口，退出码 2 仍不能记完整通过；92 项人工解释没有当作独立审阅完成。本次未实际验证读者自动派发能力、合批执行结果或 D8 冻结通过。

新 JSON 的 SHA-256：

```text
5f540d3e744245fe3f80c46ff4a715c7f11f6b0008196a901ca2de61f80be423
```

合并稿依据更新到 `c24c2a8be4ea66cce5b3843e690a0127182aca5f`。本轮工作树改动尚无自己的提交号，按该 HEAD 加路径及上述摘要定位，不声称改动已存在于该提交中。只修改 JSON 并追加本说明；未 commit、未 push、未切分支。新 JSON 和整份说明按相同正则公开信息自查，匹配数均为零。没有需要 D1 新增决定的事项，尚待真实读者记录和规定关卡。


## 续：规划端统一 GPT，D8 每轮新对话合批（第 13 节用户决定）

已完整读取最新提交 `c001f5aa02b65f53fa587181beb01716dfb389cc` 中整节改写的 SPEC 第 2.1a 节、第 2.1 节表格的 D8 行，以及 MERGE_DECISIONS 第 13 节，并同步 JSON。当前规则取代此前执行端代跑 D8、负责人批量新建读者、按单位换读者和特殊单位额外独立复述的要求。历史说明保留为各轮记录，当前角色与复述规则以本节为准，没有新增设计选择。

### 修改的节点与规则

- `dispatch`：第 2.1a 节整体换成最新原文，D8 表格行使用“规划端·普通：GPT 极高；每一轮换一个新对话，合批处理本轮全部单位”。规划端角色 D1–D3、D6、D8、X1、X5 一律 GPT 网页端，每角色每轮由用户转交一条提示词；执行端 D4、D5、D7、X2–X4 由 D1 派发，不限次数。原表格中规划端的其他宿主备选也按第 2.1a 节收窄为 GPT。
- `role-D8`：说明、输入输出、线程规则、操作轮次和验收均改为每轮一个新的 GPT 对话，合批处理本轮全部单位，随机顺序，逐单位只依据自身文字作答，记录 `reader_isolation: "single-thread-batch"`。D1 逐项比较原意和复述，全部正确就是本轮有效通过；读错则改写，下轮只放改过单位及受影响相邻单位，交新 GPT 对话重读，仍只转交一条。
- `gates`：JSON 内第 6.2 节关卡表的 D8 行明确改成“每轮新对话合批”，不再按单位要求独立线程；记录文本身份和合批方式，D1 逐项判断。没有保留本轮通过后再另派一类单位独立复述的条件。
- `freeze`、`contract-fidelity`：D8 本轮合批全部正确可作为有效通过，冻结说明如实披露用户接受的独立性取舍。不再以缺少旧的派发手段阻断合批，也不保留执行端代跑 D8 或按单位另做复述的门槛。
- `prompts`：移除旧宿主分支和两种读者派发方式；规划端只向 GPT 网页端转交每角色每轮的一条完整提示词，D8 包含本轮全部单位，后续返修轮只含改动及受影响相邻单位。执行端仍由 D1 派发，不占用户转交次数。
- `role-D1`、`role-D2`、`role-D3`、`role-D6`、`role-X1`、`role-X5`：角色卡、输入和验收明确规划端只在 GPT 网页端运行。`revision` 中旧的其他宿主负责人分支同步清理；既有修订告知、任务书、状态写权和结果交回职责保留。
- `planning-entry`、`capability-check` 及相关需求和验收：规划角色实际入口、宿主核对收窄为 GPT 网页端与 Codex 执行端，不再要求在其他宿主运行规划角色。其他平台文件格式的官方依据只作资源参考，不再形成运行规划角色的许可；没有新增网页端打包、安装或发布实现。

所有被取代的有效规则和反例已清理：执行端最高推理档代跑 D8、自动批量新建读者、按单位独立复述条件、因缺少该手段将 D8 记未知而等待的条件均不再适用。JSON 中按最新 SPEC 原文保留“旧规则改为新规则”的否定性说明，不能理解为继续执行旧规则。

连接 `c-dispatch-to-prompts` 和 `c-gates-to-role-D8` 同步当前协议。已有 `fail-role` 恢复为真实入口、档次或材料缺失的处理，删除针对旧 D8 派发手段的失败情景，并同步反例注入、说明与收场；没有新增失败路径。正常走查写明 GPT 运行范围、按轮合批、D1 逐项判断及下一轮重读。

数量仍为 54 个节点、14 条需求、48 条连接、4 条正常走查（22 步）、10 条失败路径（21 步及 10 段整体说明）、12 条依据记录、64 个验收器。验收器仍全部 `not-run`、运行记录为空；`versions: []` 不变。本轮没有实际运行 GPT 角色、派发执行端或完成 D8 复述。

### 全部受影响复述单位

以本轮开始时 HEAD 中的 JSON 为基线，实际调用固定检查器 `content/readability.ts` 的 `readerHash` 比较六项读者文字。7 个原有单位的文字哈希改变，无新增单位；其余 46 个单位文字哈希未变。

| 复述单位 id | 类型 | 改动字段 |
| --- | --- | --- |
| `ws-dispatch` | 正常步骤 | `expectedResult` |
| `ws-prompts` | 正常步骤 | `expectedResult`、`onError` |
| `wr-gates` | 正常步骤 | `exampleData`、`expectedResult`、`why`、`onError` |
| `wr-freeze` | 正常步骤 | `exampleData`、`onError` |
| `fail-role-whole` | 失败路径整体收场 | `exampleData`、`expectedResult`、`onError` |
| `fail-role-step-1` | 失败步骤 | `exampleData` |
| `fail-role-step-2` | 失败步骤 | `exampleData`、`expectedResult`、`onError` |

这些单位需按当前每轮新 GPT 对话的合批规则取得真实复述，不能复用旧文字的通过记录。本轮没有合成、复用或补签读者记录。

### 草稿检查与文件身份

检查器工作树仍为 `fix/draft-check-tier-20261111`，提交 `c05edcf51bc93f8be82180fd4ad28a250937f195`。先加载机器已有 `nodejs/24.16.0`，再实际运行离线、在线草稿档各一次；未修改检查器源码。变量代指用户指定的两个工作树，实际调用传入 JSON 的绝对路径，公开文件不记录本机路径。

```bash
module load nodejs/24.16.0
cd "$BLUEPRINT_WORKTREE/content"
npx tsx check.mjs --stage draft --offline "$ASSURANCE_WORKTREE/docs/design/assurance/plugin-0.1-d1/blueprint.json"
npx tsx check.mjs --stage draft "$ASSURANCE_WORKTREE/docs/design/assurance/plugin-0.1-d1/blueprint.json"
```

| 本轮检查 | 退出码 | 确定缺口 | 人工解释待审 | 未完成项 |
| --- | ---: | ---: | ---: | ---: |
| 离线草稿 | 2 | 0 | 92 | 3 |
| 在线草稿 | 2 | 0 | 92 | 2 |

离线检查时间为 `2026-11-12T03:29:17.780Z`，未完成项为离线未核实来源、缺 `readability-review.json`、缺 `questions.json`。在线检查时间为 `2026-11-12T03:30:32.128Z`，只剩上述两份读者记录缺失。两次均无确定内容缺口，退出码 2 仍不能记完整通过；92 项人工解释没有当作独立审阅完成。本次没有验证实际 GPT 对话执行、合批结果或正式冻结。

新 JSON 的 SHA-256：

```text
d8b1e414908b825fdfae7072bde0cfd3e1774de3650f8543172cc40626c2ce9e
```

合并稿依据更新到 `c001f5aa02b65f53fa587181beb01716dfb389cc`。本轮 JSON 改动尚无提交号，以该 HEAD 加路径及上述摘要定位，不声称已存在于该提交中。只修改 JSON 并追加本说明；SPEC、MERGE_DECISIONS、流程文档和 A 原稿未改，未 commit、未 push、未切分支。新 JSON 和整份说明按相同正则公开信息自查，匹配数均为零。没有需要 D1 新增选择的事项，尚待真实读者记录与规定关卡。


## 续：按阶段派发、状态恢复及 D8 第 1 轮术语改写（第 14 节）

本轮以设计分支 HEAD `a3dc0d96a57e18a1d6e2c542ca1acc6836cfd44f` 为准，完整读取 SPEC 第 1.3a 节、更正后的第 2.1a 节执行端派发项，以及 MERGE_DECISIONS 第 14 节。D8 的术语表和判断单均通过 `git show origin/gates/assurance-0.1-d1:<路径>` 读取，没有切换分支；该远端引用当时指向 `e6c614cac5a07a60f87c1dcfc9ff5c0e0629ce97`。文件位置分别为 `docs/design/assurance/plugin-0.1-d1/gates/d8/round1/GLOSSARY_ZH.md`、`docs/design/assurance/plugin-0.1-d1/gates/d8/round1/D1_JUDGMENT.json`，两份文件 SHA-256 分别为 `213e61f2823a05abed2407deb379229f665f62d07cfe3774d1d3e484c4326338`、`5345598735fed5a99c4cbae277b06652aad5400b29dff22e9d75865614b6c521`。

依用户补充，前两项规则同步可以修改必要的 `technical` 字段；第三项术语改写严格只动读者可见的六个字段。本轮先完成派发与恢复，再改术语，并比对各阶段内容；没有自行增订设计或术语解释。

### 已写入的规则与节点

- 设计阶段由 D1 派发 D4、D5、D7，准备 D2、D3、D6、D8 的提示词；交付阶段由 X1 派发 X2、X3、X4，准备 X5 的提示词。执行端不限次数，不占用户转交次数。`dispatch` 的输入、输出、接口、正文、验收和 `X1-intake` 表格项、D1/X1 角色卡以及重复规则全部同步，不再笼统写执行端由 D1 派发；`ws-dispatch` 的读者文字与技术说明同时改正。
- `state`、`writer`、`record-check` 写入 SPEC 第 1.3a 节完整原文，并同步接口、输出和验收：四种触发条件、发现者立即停下不派发不写记录、按有效历史状态和原始记录恢复、冲突不得自选、涉及冻结/批准/签发交用户、新状态修订号接基线递增及 `last_change.reason=recovery`、检查和远端回读后才能恢复派发、无有效历史状态须先获用户确认。恢复记录为不可变的 `recovery/<recovery_id>.json`，只采用 D1 给出的基线提交、补登事件、冲突、处理结果四类内容，没有自行命名机器字段或格式版本。
- 只读记录检查增加 `recovery` 类型。新增 `fail-recovery` 及对应 `v-fail-recovery`，把状态丢失或损坏与现有的写入结果不明区分开：前者需要历史有效状态和不可变事件的对照恢复，不能只重试写入。该路径的完整技术说明照录六步恢复，读者文字说明停下、负责人恢复、用户处理指定冲突以及恢复派发条件。
- 更新 `r-state`、`r-dispatch`、派发连接和依据引用。以下列出所有自身字段发生变化的节点；仅因子节点变化的容器不重复计入。部分节点只同步了固定来源引用或已有验收说明，没有新增规则。

| 节点 | 修改字段 |
| --- | --- |
| `state` | `outputs`、`validators`、`interface`、`terminal` |
| `writer` | `outputs`、`validators`、`interface`、`terminal` |
| `record-check` | `inputs`、`validators`、`interface`、`terminal` |
| `dispatch` | `inputs`、`outputs`、`validators`、`interface`、`terminal` |
| `prompts` | `inputs`、`validators`、`interface`、`terminal` |
| `revision` | `validators`、`terminal` |
| `role-D1` | `outputs`、`validators`、`interface`、`terminal` |
| `role-D2` | `validators`、`terminal` |
| `role-D3` | `validators`、`terminal` |
| `role-D4` | `validators` |
| `role-D6` | `validators`、`terminal` |
| `role-D8` | `validators`、`interface`、`terminal` |
| `clarify` | `validators`、`terminal` |
| `gates` | `validators`、`interface`、`terminal` |
| `contract-fidelity` | `validators`、`interface`、`terminal` |
| `freeze` | `validators`、`interface`、`terminal` |
| `q-checker` | `validators`、`terminal` |
| `q-inheritance` | `validators`、`terminal` |
| `role-X1` | `outputs`、`validators`、`interface`、`terminal` |
| `role-X5` | `validators`、`terminal` |
| `evidence` | `validators` |
| `sign` | `validators` |
| `planning-entry` | `validators`、`terminal` |
| `minimum` | `validators` |
| `capability-check` | `validators` |
| `q-capacity` | `validators`、`terminal` |

总数为 54 个节点、14 条需求、48 条连接、4 条正常走查（22 步）、11 条失败路径（22 步及 11 段整体收场）、55 个复述单位、65 个验收器、12 条依据记录。验收器仍全部 `not-run`、运行记录为空；`versions: []` 不变。没有运行这些待实现的插件能力，没有模拟状态恢复或角色派发。

### 三类复述单位

实际调用固定检查器 `content/readability.ts` 的 `readerHash`，以本轮 HEAD 中的 JSON 为基线比较：27 个原有单位的读者文字哈希改变，26 个不变，新增 2 个单位。判断单中 `passed` 的 26 个单位已对完整对象逐字段比对，全部保持原样；不只检查文字哈希。

第一类，按术语表改写的 27 个单位，顺序与判断单相同：

| 单位 id | 实际修改的读者字段 |
| --- | --- |
| `wb-planning` | `action` |
| `ws-dispatch` | `action`、`expectedResult` |
| `fail-package-step-1` | `exampleData` |
| `wr-calibration` | `exampleData` |
| `fail-package-step-2` | `exampleData` |
| `fail-semantic-step-2` | `exampleData` |
| `fail-package-step-3` | `exampleData` |
| `fail-semantic-step-1` | `exampleData` |
| `fail-role-step-2` | `exampleData`、`expectedResult`、`onError` |
| `wr-contract` | `title`、`action`、`expectedResult` |
| `fail-role-whole` | `exampleData`、`expectedResult` |
| `wb-capability` | `action` |
| `wb-source` | `why`、`onError` |
| `wr-gates` | `title`、`exampleData`、`expectedResult` |
| `wr-candidate` | `action` |
| `fail-checker-whole` | `action`、`exampleData` |
| `wb-execution` | `exampleData` |
| `fail-semantic-whole` | `exampleData` |
| `wr-freeze` | `action`、`exampleData`、`expectedResult` |
| `fail-package-whole` | `exampleData` |
| `wr-build` | `onError` |
| `ws-prompts` | `onError` |
| `wr-asset` | `action`、`exampleData` |
| `fail-checker-step-2` | `action`、`exampleData` |
| `wr-owner` | `exampleData` |
| `wr-sign` | `action`、`exampleData` |
| `fail-role-step-1` | `exampleData` |

第二类，因前两项规则必须修改的原有单位：`ws-dispatch`，改了 `expectedResult` 与 `technical.expectedResult`，已同时列在第一类。27 个名单以外的原有单位没有被动修改，原先通过的 26 个单位无例外改动。失败路径 `fail-role` 自身的 `technical.handling` 改了派发人，但不是复述单位，未改变该路径已有步骤和整体收场的技术字段。

第三类，新增单位：`fail-recovery-whole`（失败路径整体收场）、`fail-recovery-step-1`（失败步骤）。这两个新增单位均需下一轮真实复述。27 个改写单位不能复用旧文字的通过记录，未合成、补签或声称已完成 D8 复述。

### 因前两项规则改动的全部 technical 字段

既有技术字段共改两处；第三项术语改写没有修改任何 `technical` 字段。逐项如下：

1. `ws-dispatch.technical.expectedResult`：
   - 原文：生成设计或核查事实的角色绑定任务书，检查设计的角色绑定快照，交付工作绑定有效冻结对象。规划端一律在 GPT 网页端，每角色每轮由用户转交一条；执行端由设计负责人派发，不限次数。
   - 新文：生成设计或核查事实的角色绑定任务书，检查设计的角色绑定快照，交付工作绑定有效冻结对象。规划端一律在 GPT 网页端，每角色每轮由用户转交一条；执行端在设计阶段由设计负责人（D1）派发，在交付阶段由交付负责人（X1）派发，次数不限。
2. `fail-role.technical.handling`：
   - 原文：保留缺项并给出符合角色宿主要求的完整提示词，不降档、不自审、不把 prepared 写成 sent。规划端只能由用户每角色每轮转交一条到 GPT 网页端，执行端由 D1 派发；D8 按每轮新 GPT 对话合批，不以缺少旧的派发方式阻断合批通过。
   - 新文：保留缺项并给出符合角色宿主要求的完整提示词，不降档、不自审、不把 prepared 写成 sent。规划端只能由用户每角色每轮转交一条到 GPT 网页端，执行端由当前阶段负责人派发（设计阶段 D1，交付阶段 X1）；D8 按每轮新 GPT 对话合批，不以缺少旧的派发方式阻断合批通过。

状态恢复失败路径是本轮新增内容，以下逐字段列出其新增技术内容，避免把新增误称为旧字段修改：

| 新增字段 | 内容 |
| --- | --- |
| `fail-recovery.technical.id` | fail-recovery |
| `fail-recovery.technical.question` | interrupted |
| `fail-recovery.technical.shortLabel` | 状态文件丢失或损坏 |
| `fail-recovery.technical.situation` | STATE.json 不存在、无法解析、未通过 state 记录检查，或者修订号与远端分支上的最新提交对不上。 |
| `fail-recovery.technical.brokenRequirementIds` | ["r-state"] |
| `fail-recovery.technical.detectedBy` | state |
| `fail-recovery.technical.route` | ["state"] |
| `fail-recovery.technical.outcome` | stop |
| `fail-recovery.technical.handling` | SPEC 第 1.3a 节完整原文，含触发条件和六步恢复。 |
| `fail-recovery.technical.userSees` | 当前派发和写记录已停止，由当前阶段负责人按历史与原始记录恢复；恢复冲突不自行选择，涉及冻结、批准或签发的交用户决定，无有效历史状态也先请用户确认。 |
| `fail-recovery.technical.validatorId` | v-fail-recovery |
| `fail-recovery-whole.technical.nodeId` | state |
| `fail-recovery-whole.technical.action` | SPEC 第 1.3a 节完整原文，含触发条件和六步恢复。 |
| `fail-recovery-whole.technical.exampleData` | STATE.json 不存在、无法解析、未通过 state 记录检查，或者修订号与远端分支上的最新提交对不上。 |
| `fail-recovery-whole.technical.expectedResult` | 恢复记录 recovery/<recovery_id>.json 包含基线提交、补登的事件、冲突和处理结果；STATE.json 的 revision 接基线递增，last_change.reason=recovery；检查通过和远端回读后才派发。 |
| `fail-recovery-step-1.technical.nodeId` | state |
| `fail-recovery-step-1.technical.action` | SPEC 第 1.3a 节完整原文，含触发条件和六步恢复。 |
| `fail-recovery-step-1.technical.exampleData` | STATE.json 不存在、无法解析、未通过 state 记录检查，或者修订号与远端分支上的最新提交对不上。 |
| `fail-recovery-step-1.technical.expectedResult` | 恢复记录 recovery/<recovery_id>.json 包含基线提交、补登的事件、冲突和处理结果；STATE.json 的 revision 接基线递增，last_change.reason=recovery；检查通过和远端回读后才派发。 |

### 交回 D1 的术语事项

`wr-calibration.expectedResult` 的“检查器”指该步骤实际运行的验收检查实现，原文是“得到检查器能否正确区分三种情况的原始结果”。术语表把“检查器”统一解释成“固定版本的 Blueprint 检查器”，直接套用会改变对象，所以本处保留原词；该单位的“来源独立的预期”已按词表解释。请 D1 指定本处是补一条适用于验收实现的解释，还是调整本处用词；本轮不自行选择。

以下仍需要词表补充的词没有自行编解释：`wb-planning` 的“固定源提交、包根、资源根”；`wb-source` 的“复制映射、生成器”；`wr-calibration` 的“校准、控制例”；`wr-build` 的“默认验收实现”；`wr-asset` 的“冻结语义”；`wr-candidate` 的“候选、对象身份、实际运行器”；`wr-freeze` 的“冻结档”；`wr-sign` 的“偏离结论”；`fail-semantic-whole`、`fail-semantic-step-1`、`fail-semantic-step-2` 的“阈值”。这里只列词和位置，不补新的定义或完成条件。

### 草稿检查、未完成项与文件身份

检查器提交仍为 `c05edcf51bc93f8be82180fd4ad28a250937f195`，源码工作树检查后无改动。先加载 `nodejs/24.16.0`，从检查器 `content/` 实际运行离线、在线各一次；下列变量代指用户指定工作树，运行时传入 JSON 的绝对路径，公开文件不记录本机路径。

```bash
module load nodejs/24.16.0
cd "$BLUEPRINT_WORKTREE/content"
npx tsx check.mjs --stage draft --offline "$ASSURANCE_WORKTREE/docs/design/assurance/plugin-0.1-d1/blueprint.json"
npx tsx check.mjs --stage draft "$ASSURANCE_WORKTREE/docs/design/assurance/plugin-0.1-d1/blueprint.json"
```

| 检查 | 检查时间（UTC） | 退出码 | 确定缺口 | 人工解释待审 | 未完成项 |
| --- | --- | ---: | ---: | ---: | ---: |
| 离线草稿 | `2026-11-12T05:13:44.276Z` | 2 | 0 | 92 | 3 |
| 在线草稿 | `2026-11-12T05:14:24.572Z` | 2 | 0 | 92 | 2 |

离线未完成项为来源未在线核实、缺 `readability-review.json`、缺 `questions.json`；在线只剩上述两份读者记录缺失。两次均没有确定内容缺口，退出码 2 不能写成完整通过。92 项证据解释仍需人工审查；本轮只完成机械草稿检查，尚未完成 D8 新文字复述、术语补定或正式冻结。

新 JSON 的 SHA-256：

```text
048b00d56e07f94e93947606c532892739a0f28727601cdc76f9e9898bd65cf8
```

合并稿依据使用本分支实际 HEAD `a3dc0d96a57e18a1d6e2c542ca1acc6836cfd44f` 加仓库内路径。JSON 尚未提交，没有自己的提交号，以该 HEAD、路径和上述摘要定位未提交文件，不声称新文件已存在于该提交中。只修改 JSON 并追加本说明，SPEC、MERGE_DECISIONS、流程文档和 A 原稿均未修改。未 commit、未 push、未切分支。按用户指定正则检查新 JSON 和整份说明，公开信息匹配数均为零。


## 续：采用术语表“补充”完成上一轮交回的改写

上一轮交回的术语已按 D1 新增的“补充”改写，没有自行编写定义。`wr-calibration` 的验收用“检查器”首次写为“验收检查程序（检查器，用来判定成品是否达标的程序）”；检查设计文件的 Blueprint 检查器继续保持区别。其余词使用补充表中的原文解释，每个单位首次出现时展开，再次出现时保留简称。

本轮开始时设计分支 HEAD 为 `b659193f508190d139192da554312d1c423e661f`，JSON 的 SHA-256 为 `048b00d56e07f94e93947606c532892739a0f28727601cdc76f9e9898bd65cf8`。术语表通过 `git show origin/gates/assurance-0.1-d1:docs/design/assurance/plugin-0.1-d1/gates/d8/round1/GLOSSARY_ZH.md` 完整读取，该远端引用当时指向 `dda47ca4265c8e894eb027ed74208c158cd88d7e`，文件 SHA-256 为 `eba6ac99577e6bd63cfc6a1f523970661b6c8d700e48562c72d878ae5481acc8`。本轮只改读者文字，既有设计字段和来源引用均保持原样。

### 本次改写的单位

| 单位 id | 改动的读者字段 |
| --- | --- |
| `wb-planning` | `action` |
| `wb-source` | `action`、`exampleData` |
| `wr-calibration` | `title`、`action`、`expectedResult` |
| `wr-build` | `expectedResult` |
| `wr-asset` | `action`、`exampleData`、`expectedResult`、`onError` |
| `wr-candidate` | `action`、`exampleData`、`onError` |
| `wr-freeze` | `expectedResult` |
| `wr-sign` | `exampleData` |
| `fail-semantic-whole` | `exampleData` |
| `fail-semantic-step-1` | `exampleData`、`expectedResult` |
| `fail-semantic-step-2` | `exampleData` |

上述 11 个单位覆盖固定源提交、包根/资源根、复制映射、生成器、校准、控制例、验收用检查器、默认验收实现、冻结语义、候选、对象身份、实际运行器、冻结档、偏离结论和阈值。`wr-build` 将原“候选产物”按词表写为带解释的“候选成品”，没有改变所指对象或增加步骤。

已逐字段核对：除这 11 个单位的六项读者字段外，整份 JSON 与本轮 HEAD 完全一致；全部 `technical` 字段未动，判断单中已经通过的 26 个单位完整对象未动。实际调用固定检查器的 `readerHash` 比较，11 个单位文字哈希改变、44 个不变、无新增单位。改过的文字需要下一轮真实复述，本轮没有补签读者通过记录。

节点、需求、连接、走查、失败路径和验收器数量均未变化：54 个节点、14 条需求、48 条连接、4 条正常走查（22 步）、11 条失败路径（22 步及 11 段整体收场）、55 个复述单位、65 个验收器、12 条依据记录。`versions: []` 保持原样。

### 草稿检查及未完成项

在用户指定检查器工作树的 `content/` 下，先加载 `nodejs/24.16.0`，实际运行离线、在线草稿档各一次。检查器仍为提交 `c05edcf51bc93f8be82180fd4ad28a250937f195`，未修改源码。下列变量代指用户指定的工作树，实际运行使用新 JSON 的绝对路径，公开说明中不记录本机路径。

```bash
module load nodejs/24.16.0
cd "$BLUEPRINT_WORKTREE/content"
npx tsx check.mjs --stage draft --offline "$ASSURANCE_WORKTREE/docs/design/assurance/plugin-0.1-d1/blueprint.json"
npx tsx check.mjs --stage draft "$ASSURANCE_WORKTREE/docs/design/assurance/plugin-0.1-d1/blueprint.json"
```

| 检查 | 时间（UTC） | 退出码 | 确定缺口 | 人工解释待审 | 未完成项 |
| --- | --- | ---: | ---: | ---: | ---: |
| 离线草稿 | `2026-11-12T05:18:46.470Z` | 2 | 0 | 92 | 3 |
| 在线草稿 | `2026-11-12T05:19:07.003Z` | 2 | 0 | 92 | 2 |

离线未完成项为使用离线模式未核实来源，以及缺 `readability-review.json`、缺 `questions.json`。在线只剩这两份读者记录缺失。两次均无确定内容缺口，退出码 2 仍不能记为完整通过；92 项证据解释仍待人工审查。本轮没有剩余需要新增定义的术语事项，尚待下一轮真实复述和规定关卡。

新 JSON 的 SHA-256：

```text
6530517cee7ddc2ca6da4c7c9a6a1d4410f5f088c491b69cdbf739fa621b42fa
```

新文件未提交，没有新的提交号，以本轮 HEAD 加仓库内路径及上述摘要定位。只修改 JSON 并追加本说明，未 commit、未 push、未切分支。新 JSON 和整份说明按用户指定正则自查，公开信息匹配数均为零。


## 续：D6 第 2 轮负责人宿主更正及 D8 第 2 轮指定文字

已按 D1 第 15 节决定补齐负责人宿主和规划入口，并逐字替换第 2 轮指定的 7 个单位。负责人 D1、X1 恢复为 Claude 或 GPT Pro，只有需要用户手动转交的 D2、D3、D6、D8、X5 受 GPT 网页端及每角色每轮一次转交约束；没有新增设计选择。

本轮完整读取设计分支 HEAD `79a252567fa0c88101a8f31573d89eabf9ad6a4b` 中 SPEC 第 2.1a 节两项更正及 MERGE_DECISIONS 第 15 节，并核对 SPEC 第 9.2 节的既定双规划宿主入口。指定改写文件通过 `git show origin/gates/assurance-0.1-d1:docs/design/assurance/plugin-0.1-d1/gates/d8/round2/REWRITES_ZH.json` 读取，远端引用当时指向 `bceaa9da6d6729a0bcdfbbc58f3a5bc1408ebb44`，文件 SHA-256 为 `6cf03089a1094aff780c572a07f98d0edfd9e0658d746186e391455031cbebbe`。

### Blueprint 与流程文档改动

- `dispatch`、`prompts` 的输入、输出、接口、说明和验收，所有重复的第 2.1a 节以及相关需求、连接、反例同步更正。负责人为 Claude 时直接派发执行端，为 GPT 时生成完整提示词交用户转交给 Codex。设计阶段仍由 D1 派发 D4/D5/D7、准备 D2/D3/D6/D8 提示词；交付阶段仍由 X1 派发 X2/X3/X4、准备 X5 提示词。没有把规划端的次数限制扩展到执行端。
- `role-D1`、`role-X1` 的输入、角色说明、长期线程规则和验收明确负责人例外，删除只允许 GPT 网页端的限制；调度角色表恢复“Claude 或 GPT Pro”。SPEC 第 2.1a 节关于本插件自身由 Claude 担任 D1、X1 的原文也已写入。
- `planning-entry` 恢复 SPEC 第 9.2 节，明确 Claude Code 与 GPT Work 读取同一固定来源的规划 `SKILL.md`、角色卡和支持文件；`capability-check` 的入口行、验收和相关依据恢复双规划宿主实际观察。需要转交的 GPT 角色和安装后的执行入口仍按各自职责验证，格式兼容不代替实际加载。
- 修订提示、冻结和关卡中的重复规则均同步，删除仍把所有规划端限定在 GPT 网页端的有效规定。复制的第 2.1a 节标题沿用当前 SPEC 原文，正文完整包含负责人例外，不沿用该标题作泛化约束。
- 在流程文档旧的 `2026-11-11` 修订说明之后，仅新增一段 `2026-11-12` 修订说明，引用 SPEC 第 2.1a 节。说明用户最终决定：需要转交的规划角色在 GPT 上跑、每角色每轮一次、D8 每轮新对话合批、负责人仍按原流程；明确取代上一段关于自动批量新建读者、执行端代跑 D8、关键单位独立复述及每步换读者的规定。已将新增段落从比较副本中移除核对，剩余字节与 HEAD 中原文完全一致，原正文和旧说明没有删改。

自身字段发生变化的节点：`state`、`writer`、`record-check`、`dispatch`、`prompts`、`revision`、`role-D1`、`role-D2`、`role-D3`、`role-D4`、`role-D6`、`role-D8`、`clarify`、`gates`、`contract-fidelity`、`freeze`、`q-checker`、`q-inheritance`、`role-X1`、`role-X5`、`evidence`、`sign`、`planning-entry`、`minimum`、`capability-check`、`q-capacity`。这里只列节点自身改动，不把子节点变化重复算作容器改动。

数量保持 54 个节点、14 条需求、48 条连接、4 条正常走查（22 步）、11 条失败路径（22 步及 11 段整体收场）、55 个复述单位、65 个验收器、12 条依据记录。没有新增节点、连接、走查、失败路径或验收器。验收器仍为未运行，`versions: []` 不变；本轮没有实际运行角色、派发执行端或完成正式冻结。

### 全部修改的复述单位

第一组，7 个单位按 D1 的 JSON 逐字段原样替换，已检查字符串完全一致，没有再润色：

| 单位 id | 指定替换字段 |
| --- | --- |
| `fail-role-step-2` | `exampleData`、`expectedResult`、`onError` |
| `fail-role-whole` | `exampleData`、`expectedResult` |
| `wr-owner` | `exampleData`、`expectedResult` |
| `ws-dispatch` | `action`、`expectedResult` |
| `wr-contract` | `expectedResult` |
| `fail-recovery-step-1` | `onError` |
| `wr-gates` | `action`、`exampleData` |

第二组，因负责人宿主和入口更正而额外修改的 3 个单位，单独列出供下一轮重读：

| 单位 id | 修改的读者字段 |
| --- | --- |
| `ws-prompts` | `action`、`expectedResult` |
| `wb-planning` | `expectedResult` |
| `fail-role-step-1` | `exampleData` |

`ws-prompts` 说明 Claude 负责人直接派执行端、GPT 负责人交完整提示词给用户，并把每轮一条的对象收窄为需要转交的规划角色；`wb-planning` 明确 Claude Code 与 GPT Work 实际读取同源规划材料；`fail-role-step-1` 将 GPT 档次示例收窄为需要用户转交的规划端角色。

实际调用固定检查器 `content/readability.ts` 的 `readerHash` 对本轮 HEAD 比较：10 个原有单位哈希改变、45 个不变，无新增单位。第一组给出的字段优先于负责人规则同步时形成的中间文字，其余未指定字段只在第一项必须更正时改动；没有借替换步骤改动技术说明。所有变动文字待下一轮真实复述，没有复用旧文字通过记录或补签记录。

### 负责人更正涉及的 technical 字段

沿用用户此前明确的边界：规则同步必须涉及的技术说明随规则更正，术语或指定文字替换只改六个读者字段。第 1 项共改了以下 4 个既有技术字段；第 3 项没有再修改任何 `technical`。除 `ws-dispatch.technical.expectedResult` 因第一项必须纠正原先“规划端一律 GPT”的说法外，指定 7 个单位的其他技术字段均与 HEAD 相同。

1. `ws-dispatch.technical.expectedResult`：
   - 原文：生成设计或核查事实的角色绑定任务书，检查设计的角色绑定快照，交付工作绑定有效冻结对象。规划端一律在 GPT 网页端，每角色每轮由用户转交一条；执行端在设计阶段由设计负责人（D1）派发，在交付阶段由交付负责人（X1）派发，次数不限。
   - 新文：生成设计或核查事实的角色绑定任务书，检查设计的角色绑定快照，交付工作绑定有效冻结对象。需要用户手动转交的规划端角色（D2、D3、D6、D8、X5）在 GPT 网页端，每角色每轮由用户转交一条；负责人 D1、X1 由 Claude 或 GPT Pro 担任，各自使用长期线程；规划 SKILL.md 由 Claude Code 和 GPT Work 直接读取。Claude 担任负责人时直接派发执行端；GPT 担任时生成完整提示词，由用户转交给 Codex。执行端在设计阶段由设计负责人（D1）派发，在交付阶段由交付负责人（X1）派发，次数不限。

2. `ws-prompts.technical.action`：
   - 原文：负责人把派发展开成可直接复制的提示词。
   - 新文：负责人把派发展开成可直接复制的提示词。Claude 担任负责人时直接派发执行端，GPT 担任时生成完整提示词交用户转交给 Codex。

3. `ws-prompts.technical.expectedResult`：
   - 原文：用户拿到该规划端角色本轮的一条完整提示词；读者复述在一个新的 GPT 对话里合批处理本轮全部单位。对话随机逐个作答，每单位只依据自身文字，由设计负责人逐项判断。
   - 新文：用户拿到需要转交的规划端角色本轮的一条完整提示词；读者复述在一个新的 GPT 对话里合批处理本轮全部单位。对话随机逐个作答，每单位只依据自身文字，由设计负责人逐项判断。

4. `fail-role.technical.handling`：
   - 原文：保留缺项并给出符合角色宿主要求的完整提示词，不降档、不自审、不把 prepared 写成 sent。规划端只能由用户每角色每轮转交一条到 GPT 网页端，执行端由当前阶段负责人派发（设计阶段 D1，交付阶段 X1）；D8 按每轮新 GPT 对话合批，不以缺少旧的派发方式阻断合批通过。
   - 新文：保留缺项并给出符合角色宿主要求的完整提示词，不降档、不自审、不把 prepared 写成 sent。需要用户手动转交的规划端角色（D2、D3、D6、D8、X5）由用户每角色每轮转交最多一条到 GPT 网页端；负责人 D1、X1 由 Claude 或 GPT Pro 担任，各自使用长期线程；规划 SKILL.md 由 Claude Code 和 GPT Work 直接读取。Claude 担任负责人时直接派发执行端；GPT 担任时生成完整提示词，由用户转交给 Codex。执行端由当前阶段负责人派发（设计阶段 D1，交付阶段 X1）；D8 按每轮新 GPT 对话合批，不以缺少旧的派发方式阻断合批通过。

### 草稿检查与未完成项

检查器仍为 `c05edcf51bc93f8be82180fd4ad28a250937f195`，未修改源码。先执行 `module load nodejs/24.16.0`，在检查器 `content/` 下实际运行离线、在线各一次。下列变量代指用户指定工作树，运行时传入 JSON 绝对路径，公开文件不记录本机路径。

```bash
module load nodejs/24.16.0
cd "$BLUEPRINT_WORKTREE/content"
npx tsx check.mjs --stage draft --offline "$ASSURANCE_WORKTREE/docs/design/assurance/plugin-0.1-d1/blueprint.json"
npx tsx check.mjs --stage draft "$ASSURANCE_WORKTREE/docs/design/assurance/plugin-0.1-d1/blueprint.json"
```

| 检查 | 时间（UTC） | 退出码 | 确定缺口 | 人工解释待审 | 未完成项 |
| --- | --- | ---: | ---: | ---: | ---: |
| 离线草稿 | `2026-11-12T05:50:38.587Z` | 2 | 0 | 92 | 3 |
| 在线草稿 | `2026-11-12T05:51:25.567Z` | 2 | 0 | 92 | 2 |

离线未完成项为离线模式未核实来源、缺 `readability-review.json`、缺 `questions.json`。在线只剩上述两份读者记录缺失。两次均没有确定内容缺口，退出码 2 不能记作完整通过；92 项证据解释仍需人工审查。本轮没有需要新增设计决定的事项，仍待变动单位的真实复述及规定关卡。

新 JSON 的 SHA-256：

```text
e9a76982321f30017ac9c255d71ac008434db5ca70728d6699c23dcaf5e23417
```

追加修订说明后的流程文档 SHA-256：`ed0999e16ccae70f99984303d7287ff7c81a0b790ea76059d7446a0b78a59588`。合并稿引用使用本分支实际 HEAD `79a252567fa0c88101a8f31573d89eabf9ad6a4b` 加仓库内路径；本轮 JSON 与流程文档改动尚未提交，没有自己的提交号，上述摘要定位当前文件，不声称未提交内容已存在于 HEAD 中。

只修改 JSON、流程文档并追加本说明。SPEC、MERGE_DECISIONS 和 A 原稿未改，未 commit、未 push、未切分支。新 JSON、整份说明和流程文档按用户指定正则公开信息自查，匹配数均为零。


## 续：网页端打包纳入 0.1，及本插件自身的 X1 分工（第 17 节用户决定）

网页端打包已写入 0.1 必需范围，既定的打包方法、包内内容、能力边界和三项真实验收完整落入 Blueprint；本插件自身的 X1 改为 GPT Work 极高，Claude 只做机械启动 Codex 的运输。通用的“Claude 或 GPT Pro 担任负责人”规则保留，没有新定打包工具、包格式或额外角色。

本轮以实际 HEAD `966d35aadf5e775c6f4cceb355edb5d2d6ee99a6` 为准，完整读取 SPEC 第 9.4 节及第 10.3 节改动、流程文档第 10、11 节修订和 MERGE_DECISIONS 第 17 节。SPEC 文件 SHA-256 为 `b2cc2b9932b55c74afa9b252179ea7eb8726a75b87547972613c2baf32ae6c94`；这些是当前决定的依据，并不代替方法已由 X2 定位或网页端验收已执行的证据。

### 节点、范围与验收

- `web-later` 的标题改为“网页端打包与验收”，描述、输入输出、接口、接入位置和验收均改成 0.1 的实际打包与真实验收。保留该节点及主验收器的稳定 id，便于沿用引用；名称中的职责和正文均不再表示以后实施。其 `terminal.mechanism` 与当前 SPEC 第 9.4 节全文逐字一致。
- X2 先在仓库和实际包中定位用户已测通的 thread handoff、thread instruction 所用方法和工具，记录来源后复用。没有自行选择另一套打包方式，也没有在本轮提前开展查包、打包或上传实施。
- 网页端包包含 design-assurance、delivery-assurance 两规划入口的同一份正文、完整角色卡、模板、结构定义、清单和图标；规则正文只来自 `shared/assurance/`。网页端没有本地终端，只负责读状态、生成下一条提示词，并在有仓库连接器时按派发写回，不能声称运行本地脚本或启动 Codex。
- X4 负责在真实 ChatGPT 网页端上传包、新开一个对话，实际读取规划正文、至少一张角色卡和一份模板，依据公开安全的示例任务状态生成正确的下一条完整提示词，并按要求写回指定分支，无写权限时如实给出内容。保留原始对话，由 X1 签发；只上传成功不算通过。
- `minimum` 删除网页端上架的延后说法，采用当前第 10.3 节，并加入网页端必需范围；`r-package` 的文本与需求路线、`packaging` 的最终对象和父职责验收、`execution-package` 的两端能力边界、`capability-check` 的输出、正文与验收均同步。原有执行端能力保持必需，不能由网页端观察替代。
- 所有提到“本插件自身的设计和实施由 Claude 担任 D1、X1”的句子均替换为当前特例：D1 仍由 Claude 担任，X1 由 GPT Work 极高在长期对话中持续负责；X1 写入仓库的派发由 Claude 只做机械启动 Codex 的运输，不参与交付判断。`role-X1` 另明确该特例的验收依据。没有把这个特例扩展成所有被管理任务的通用角色规则。

所有自身字段发生变化的节点如下，容器仅因子节点改变时不重复列入：

| 节点 id | 修改字段 |
| --- | --- |
| `state` | `validators` |
| `writer` | `validators` |
| `record-check` | `validators` |
| `dispatch` | `validators`、`terminal` |
| `prompts` | `validators`、`terminal` |
| `revision` | `validators`、`terminal` |
| `role-D1` | `validators`、`terminal` |
| `role-D2` | `validators` |
| `role-D3` | `validators` |
| `role-D4` | `validators` |
| `role-D6` | `validators` |
| `role-D8` | `validators`、`terminal` |
| `clarify` | `validators`、`terminal` |
| `gates` | `validators`、`terminal` |
| `contract-fidelity` | `validators`、`terminal` |
| `freeze` | `validators`、`terminal` |
| `q-checker` | `validators`、`terminal` |
| `q-inheritance` | `validators`、`terminal` |
| `role-X1` | `validators`、`terminal` |
| `role-X5` | `validators` |
| `evidence` | `validators` |
| `deviation` | `inputs`、`validators`、`interface` |
| `sign` | `validators` |
| `packaging` | `description`、`outputs`、`validators` |
| `planning-entry` | `validators`、`terminal` |
| `execution-package` | `validators`、`interface`、`terminal` |
| `minimum` | `description`、`outputs`、`validators`、`interface`、`terminal` |
| `capability-check` | `inputs`、`outputs`、`validators`、`interface`、`terminal` |
| `web-later` | `title`、`description`、`inputs`、`outputs`、`validators`、`interface`、`ringLabel`、`terminal` |
| `q-capacity` | `validators`、`terminal` |

新增三条连接：`c-capability-check-to-web-later` 将已定网页端专项验收交给对应职责；`c-web-later-to-capability-check` 返回三项原始对话证据；`c-web-later-to-deviation` 将方法找不到或无法复现的偏离交入既有偏离流程，由 X1 处理。连接及端口仅表示已定职责间的交接，不是新增后台派发能力。

### 走查、失败路径与复述单位

安装环境的 `walk-installed` 增加网页端入口、示例输入和输出，原有执行端两步完整保留。新增一步 `wi-web`，写清网页端三项实际观察、原始对话证据及权限边界。走查整体的 `entry`、`exit`、`exampleInput`、`expectedOutput` 和其对应技术元信息同步两端范围；这些整体元信息不计为独立复述单位。

新增 `fail-web-method`：X2 找不到或无法复现已测通的方法时，记录实际查找与复现结果，作为偏离交给 X1，不另造方法。该情形和安装包缺资源的失败路径需要不同处理，故单列；新增对应验收探针 `v-fail-web-method`，仍为 `not-run`。失败路线按格式规则停在发现问题的节点，后续偏离交接由处理正文及连接说明。

| 单位 id | 类型 | 本轮变化 |
| --- | --- | --- |
| `wi-web` | 安装环境正常步骤 | 新增网页端读取、提示词与写回验收 |
| `fail-web-method-whole` | 失败路径整体收场 | 新增方法缺失/无法复现的偏离处理 |
| `fail-web-method-step-1` | 失败步骤 | 新增保留实际结果并交 X1 的说明 |

实际调用固定检查器 `content/readability.ts` 的 `readerHash` 比较本轮 HEAD：新增 3 个单位，原有 55 个单位文字哈希均未变；另外已逐字段确认这 55 个完整对象，包括 `technical`，全部保持原样。本轮没有修改原有复述单位，也没有生成或补签读者通过记录；三个新单位仍需真实读者复述。

总数为 54 个节点、14 条需求、51 条连接、4 条正常走查（23 步）、12 条失败路径（23 步及 12 段整体收场）、58 个复述单位、66 个验收器、12 条依据记录。验收器仍全部 `not-run`、运行记录为空，`versions: []` 保持不变。没有实际运行网页端包、X4 专项验收或本插件自身的 X1/运输流程。

### 草稿检查与修正记录

检查器提交仍为 `c05edcf51bc93f8be82180fd4ad28a250937f195`，源码工作树检查后无改动。先加载 `nodejs/24.16.0`，在检查器 `content/` 下运行草稿档；下列变量代指用户指定的工作树，实际调用传入 JSON 的绝对路径，公开文件不记录本机路径。

```bash
module load nodejs/24.16.0
cd "$BLUEPRINT_WORKTREE/content"
npx tsx check.mjs --stage draft --offline "$ASSURANCE_WORKTREE/docs/design/assurance/plugin-0.1-d1/blueprint.json"
npx tsx check.mjs --stage draft "$ASSURANCE_WORKTREE/docs/design/assurance/plugin-0.1-d1/blueprint.json"
```

| 检查 | 时间（UTC） | 退出码 | 确定缺口 | 人工解释待审 | 未完成项 |
| --- | --- | ---: | ---: | ---: | ---: |
| 首轮离线 | `2026-11-12T17:03:20.792Z` | 1 | 4 | 92 | 3 |
| 修正后离线 | `2026-11-12T17:04:28.248Z` | 2 | 0 | 92 | 3 |
| 在线草稿 | `2026-11-12T17:05:12.900Z` | 2 | 0 | 92 | 2 |

首轮四项缺口是新增走查缺对应连线、失败步骤与路线不一致、失败路线终点未指向发现组件，以及验收反例缺少本路径注入绑定。按既有格式补齐后复跑离线，缺口已清零；这些修正未增加设计决定或改变三个新单位的读者文字。

修正后离线未完成项为离线模式未核实来源、缺 `readability-review.json`、缺 `questions.json`；在线只剩这两份读者记录缺失。退出码 2 不能记成完整通过，92 项证据解释仍待人工审查。没有待 D1 新增选择的事项，仍待规定关卡及真实网页端验收。

新 JSON 的 SHA-256：

```text
3e24c2239779e344fb654ebb3994d2da4e2e0d43ff085c6ad35c59fefec7fd9f
```

合并稿来源引用使用本分支实际 HEAD `966d35aadf5e775c6f4cceb355edb5d2d6ee99a6` 加仓库内路径。本轮 JSON 未提交，没有自己的提交号，以上摘要标识当前未提交文件，不声称已存在于该提交中。只修改 JSON 并追加本说明，SPEC、MERGE_DECISIONS、流程文档和 A 原稿均未修改；未 commit、未 push、未切分支。新 JSON 和整份说明按用户指定正则公开信息自查，匹配数均为零。


## 续：冻结说明固定格式与验收条目清单（第 20 节用户决定）

第 6.4a 节固定格式已完整写入 Blueprint，D1 编写、D6 对照检查、模板、走查与缺口退回规则均已同步。另已在用户指定的 D5 目录生成 `acceptance-inventory.json`，供 D1 整理说明时使用；本轮没有撰写冻结说明正文，也没有做功能分类。

本轮以实际 HEAD `811d05d9cf05c6514a15ea0bb65821b7f8b5797a` 为准，完整读取 SPEC 第 6.4 节改动、第 6.4a 节全文与 MERGE_DECISIONS 第 20 节。合并稿依据引用使用该提交加仓库内路径；JSON 与清单是当前未提交结果，没有新的提交号。

### 写入的规则和节点

- `freeze.terminal.mechanism` 加入第 6.4a 节全文，并逐字核对一致；重复出现的旧“至少讲清”清单全部改为新格式引用。
- 每次首次冻结或大改都按固定十节骨架顺序写，最后一节只在大改后重新批准时写；日常语言、正文一页左右、正文不出现文件名/路径/字段名/哈希/节点编号，技术信息仅放附录；验收器清单可单列、不受一页限制。说明中的每条承诺均须能在 Blueprint 找到出处，不能漏掉影响用户决定的内容。
- `freeze` 验收补上骨架、写法、验收器数量分类及各类功能/判定说明、大件逐项披露或“没有”、逐条出处与不漏写、D6 四项检查，以及附录中的身份、关卡和节点对应关系。
- `role-D1` 明确写固定格式说明并在冻结前与 Blueprint 一起交 D6；`role-D6` 增加可读的冻结说明及四项对照检查：漏写、多写、验收器数量分类、大件下载。缺口交回 D1 改写。`gates` 与调度批准步骤同步该检查。
- 在已有模板清单补入冻结说明模板设计定位 `shared/assurance/templates/freeze-explanation.md`，按第 6.4a 节分正文和附录；只写模板条目，本轮没有创建或实现产品模板文件。
- 新增 `fail-freeze-explanation` 及对应的 `v-fail-freeze-explanation`，说明 D6 发现冻结说明缺口后交回 D1 按固定格式改写。它和检查器不可用、网页端打包偏离有不同的处理责任，未合并成同一路径。

| 修改节点 | 修改的自身字段 |
| --- | --- |
| `state` | `validators` |
| `writer` | `validators` |
| `record-check` | `validators` |
| `dispatch` | `validators`、`terminal` |
| `prompts` | `validators` |
| `revision` | `validators`、`terminal` |
| `role-D1` | `outputs`、`validators`、`interface`、`terminal` |
| `role-D2` | `validators` |
| `role-D3` | `validators` |
| `role-D4` | `validators` |
| `role-D6` | `inputs`、`outputs`、`validators`、`interface`、`terminal` |
| `role-D8` | `validators` |
| `clarify` | `validators`、`terminal` |
| `gates` | `validators`、`terminal` |
| `contract-fidelity` | `validators` |
| `freeze` | `inputs`、`outputs`、`validators`、`interface`、`terminal` |
| `q-checker` | `validators`、`terminal` |
| `q-inheritance` | `validators`、`terminal` |
| `role-X1` | `validators` |
| `role-X5` | `validators` |
| `evidence` | `validators` |
| `deviation` | `validators` |
| `sign` | `validators` |
| `packaging` | `validators` |
| `source-layout` | `validators`、`interface`、`terminal` |
| `planning-entry` | `validators` |
| `execution-package` | `validators`、`terminal` |
| `minimum` | `validators` |
| `capability-check` | `validators` |
| `web-later` | `validators` |
| `q-capacity` | `validators`、`terminal` |

数量为 54 个节点、14 条需求、51 条连接、4 条正常走查（23 步）、13 条失败路径（24 步及 13 段整体收场）、60 个复述单位、67 个验收器对象、12 条依据记录。所有验收器仍为 `not-run`、运行记录为空；`versions: []` 保持原样。本轮没有用户批准、正式冻结或产品运行验收。

### 所有受影响复述单位

实际调用当前固定检查器的 `readerHash` 比较本轮 HEAD：两个原有单位文字哈希改变，新增两个单位，其余 56 个原有单位的完整内容未变。

| 单位 id | 类型 | 修改字段或用途 |
| --- | --- | --- |
| `wr-gates` | 修改 | `action` |
| `wr-freeze` | 修改 | `action`、`exampleData`、`onError` |
| `fail-freeze-explanation-whole` | 新增 | 失败路径整体收场 |
| `fail-freeze-explanation-step-1` | 新增 | 失败路径步骤 |

这些单位需要新一轮真实复述，没有补签或篡改既有读者记录。规则同步所需的既有技术字段也随之修改，逐项如下；新增失败路径及两个新单位的技术说明是新增内容。

| 技术字段 | 原文 | 新文 |
| --- | --- | --- |
| `wr-gates.technical.action` | 负责人在冻结前用草稿入口检查结构，并收集同一设计上的追问、冷读和逐步复述。 | 负责人在冻结前用草稿入口检查结构，并收集同一设计上的追问、冷读和逐步复述。 D6 冻结前对照 Blueprint 检查冻结说明漏写、多写、验收器数量分类和大件下载，发现问题交回 D1。 |
| `wr-freeze.technical.action` | 首次冻结五步：D5 草稿档/D6/D7/D8 同一 snapshot_sha256 通过；用户批准；冻结命令追加首版；D5 冻结档核对获批快照不变；写含 snapshot_sha256、bundle_sha256、semantic_hash 的 freeze.json。 | 首次冻结五步：D5 草稿档/D6/D7/D8 同一 snapshot_sha256 通过；用户批准；冻结命令追加首版；D5 冻结档核对获批快照不变；写含 snapshot_sha256、bundle_sha256、semantic_hash 的 freeze.json。 首次冻结或大改，D1 按第 6.4a 节给用户冻结说明，正文与技术附录分开，冻结前由 D6 对照 Blueprint 检查四项缺口。 |
| `wr-freeze.technical.exampleData` | 拿到获批快照、四项有效关卡结果、用户答复和追加历史后的完整文件；D8 合批已经设计负责人逐项判断正确。 | 拿到获批快照、四项有效关卡结果、用户答复和追加历史后的完整文件；D8 合批已经设计负责人逐项判断正确。；冻结说明按第 6.4a 节写成并由 D6 对照检查。 |

### 验收条目清单与汇总

清单逐节点、按原序取出每条 `terminal.acceptance`，保留节点 id、标题、原文、从零开始的条目索引、JSON 出处、顶层组件、单值 `needs` 及理由、`big_download` 和判断依据。已按原树顺序逐项核对，没有漏项、拆句、去重或改写条目。相同文字在不同节点仍保留各自的一条。

共有 **243 条验收条目**，Blueprint 中则是 **67 个 `validators` 对象**。这是两个不同口径，不能把 243 直接当作冻结说明中的验收器总数。`needs` 只是当前任务要求的机械需求判断，不是功能分类；D1 的功能分类未在本轮代做。

| 顶层组件 | file-check | real-host | expert | user | unclear | 合计 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 共用任务协议（`shared`） | 40 | 16 | 0 | 5 | 0 | 61 |
| 设计保障（`design`） | 71 | 28 | 0 | 5 | 2 | 106 |
| 交付保障（`delivery`） | 25 | 10 | 6 | 0 | 3 | 44 |
| 同源分发（`packaging`） | 18 | 12 | 1 | 0 | 1 | 32 |
| 合计 | 154 | 66 | 7 | 10 | 6 | 243 |

以下 6 条无法机械归入单一需要，已标 `unclear` 并保留原因，未拆成新的验收条件：

- `contract-capability.terminal.acceptance[0]`：该条把真实宿主能力、用户批准、签发和不承诺事项合在一起，单一 needs 无法代表全部；未另拆条目或替 D1 做功能分类。
- `contract-changes.terminal.acceptance[0]`：该条涵盖验收资产语义、设计退回和用户专属决定；具体变化可能只需对照文件，也可能需用户决定，原文没有唯一验证场景。
- `calibration.terminal.acceptance[2]`：该条规定校准不能替代正常入口、回归或专业判断；三者分别可能需真实宿主、脚本或 X5，原文未指定本条独立的验证对象。
- `evidence.terminal.acceptance[2]`：亲读原始证据的质量观察依产物而定，可能需文件比较、真实宿主或 X5；原文未固定当前证据类型。
- `sign.terminal.acceptance[0]`：十三项清单及最终产物/必要证据的亲读可能同时含真实宿主、X5 或用户项目，未指定本次冻结任务具体必需子项，不能机械压成一种需要。
- `minimum.terminal.acceptance[0]`：完整任务链同时涉及角色、冻结、校准、证据、修订、签发，跨多个 needs；不拆功能子类或假定只读文件就能验完。

清单末尾的 `downloads` 单独列出 Python、jsonschema 及格式依赖、两种 JCS 库、两执行插件、各实际宿主和两网页端包，共 11 个依赖或环境/产物候选。全 JSON 的安装、下载及有关库名搜索位置和摘录保存在 `download_scan`，可复核并区分实际要求与第 6.4a 节中的类型示例。

Blueprint 没有写这些候选的发行包大小、平台或具体安装器；本轮不自行选择安装包、编译器或本地模型。没有可从 Blueprint 确认的单项超过 100 MB 的具体下载，条目 `big_download` 为 `null`，下载记录的大小及是否超过阈值仍为未知。**这不等于已证明“没有大件”**；清单已明确提醒 D1，实际安装版本、机器及大小仍待核实。网页端上传包、已有宿主可用性、泛指的模型/数据/镜像示例没有被改写成强制新下载安装要求。本轮没有下载或安装任何东西。

清单 SHA-256：`1da00a5f4cca868f9b41bb31063d763100610e150f15dccb3040a25726959382`。清单的 `source.sha256` 与下面的新 Blueprint 摘要一致。

### 草稿检查：预期读者缺口单列

检查器当前提交为 `529bbde9b7d0ae9d2be7084fff2b34d9e4a6af1e`，源码未改。该版本从受检 JSON 的同目录读取 `readability-review.json` 和 `questions.json`，未提供外置读者文件参数。因此在检查器缓存的本轮专用目录放三个只读输入链接：Blueprint 指向本轮新 JSON，读者文件和疑问文件分别指向用户指定 D5 目录的原件。三份链接均已核对原始字节，D5 目录原有 Blueprint、读者文件、疑问文件均未覆盖或修改。

先加载 Node 后，从检查器 `content/` 实际运行离线、在线各一次。变量代指用户给定工作树，公开说明不记录本机绝对路径：

```bash
module load nodejs/24.16.0
cd "$BLUEPRINT_WORKTREE/content"
CHECK_INPUT="$BLUEPRINT_WORKTREE/content/.cache/assurance-freeze-format-811d05d9/blueprint.json"
npx tsx check.mjs --stage draft --offline "$CHECK_INPUT"
npx tsx check.mjs --stage draft "$CHECK_INPUT"
```

| 检查 | 时间（UTC） | 原始退出码 | 预期读者缺口 | 其他缺口 | 人工解释待审 | 未完成核实 |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| 离线草稿 | `2026-11-13T05:11:30.429Z` | 1 | 4 | 0 | 92 | 1 |
| 在线草稿 | `2026-11-13T05:14:36.358Z` | 1 | 4 | 0 | 92 | 0 |

四项均为 `reader-current-hash`：`wr-gates`、`wr-freeze` 的旧文字记录不再匹配，`fail-freeze-explanation-whole`、`fail-freeze-explanation-step-1` 尚无新增单位记录。这四项按用户当前约定单列，不算本任务失败，但也没有修改检查器输出或把正式 D8/D5 写成通过。其他缺口为零；在线未完成核实为零。离线唯一未完成项是来源未联网核实。92 项证据解释仍待人工审查。

使用的读者原件 SHA-256 为 `c36ddb6392c62d597c05f11a3db71f838ab11fd2f336e298ce3a152b9062d2e7`；疑问文件原件 SHA-256 为 `37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570`。前后摘要一致。

新 JSON 的 SHA-256：

```text
540f99bcfafe6f358f42aee1f71a3b4d312655c488988f5cc60501a057b35670
```

只在指定工作树修改 JSON 并追加本说明，另在用户指定 D5 目录生成清单；检查器缓存只创建本轮只读输入链接与常规检查报告。SPEC、MERGE_DECISIONS、流程文档和原稿均未修改，未 commit、未 push、未切分支。新 JSON、整份说明和验收条目清单按用户指定正则自查，公开信息匹配数均为零。


## 续：普通恢复冲突的固定处置（第 21 节，D7 第 17 轮后补定）

普通恢复冲突的固定处置已写入 Blueprint，验收器对象数量仍为 **67 个，没有变化**。验收条目清单已按当前 JSON 重新生成，条目从 243 条增至 252 条；没有新增角色、节点、连接、验收器或复述单位，也没有新增设计选择。

本轮完整读取实际 HEAD `6aaa858524e5f3a429c8e6d2bd6aee8cce183e15` 中 SPEC 第 1.3a 节第 4 步及 MERGE_DECISIONS 第 21 节。`state`、`writer`、`record-check`、`dispatch` 的机制、状态与写者的接口边界、`fail-recovery` 的处理及两个复述单位的技术步骤，均逐字包含第 4 步的新四条规则。旧的笼统“不能自行选择、涉及冻结批准签发交用户”说法已删除。

### 写入内容与范围

- 涉及冻结、批准、签发、撤回的冲突交用户决定。
- 其余普通冲突只能按固定保守处置当作变化没有发生，相关派发记 `stale`，不采用结果；原始记录和事件原样保留，不删除、不改写。仍需工作时用新派发编号，新提示词列出原派发已留下的提交和文件，接收者从当前仓库状态出发，不能假设原派发没有执行过。
- 保守处置做不了时也交用户：包括原写入与重派工作冲突，或重派会有无法撤回的外部后果，如付费、对外发布、向他人发消息。本轮没有执行这些外部动作。
- 等待用户的冲突涉及的节点及依赖工作写入 `paused_scopes` 暂停派发；其余范围只有在恢复记录通过检查并回读后才恢复。`fail-recovery.outcome` 同步为 `recover`，不表示忽略检查门槛或恢复仍暂停的范围。
- 恢复记录原先列出的基线提交、补登事件、冲突、处理结果保留，补上每个冲突的处置方式 `stale-redispatch` 或 `user` 及暂停范围。本轮只补已有记录说明，没有另定机器字段名、结构版本或空值规则。`record-check` 只核对已有处置记录、暂停范围结构及已声明引用，不代替用户裁决、不执行重派或记录中的命令。
- 状态与写者的原单条冲突验收改为四条原文；派发验收补普通冲突重派、不能保守处置交用户、隔离与恢复三条；恢复记录验收补新内容。原有 `v-fail-recovery` 同步反例、预期收场和引用，没有另建验收器。

| 自身字段发生变化的节点 | 修改字段 |
| --- | --- |
| `state` | `outputs`、`validators`、`interface`、`terminal` |
| `writer` | `outputs`、`validators`、`interface`、`terminal` |
| `record-check` | `validators`、`terminal` |
| `dispatch` | `validators`、`terminal` |
| `prompts` | `validators` |
| `revision` | `validators`、`terminal` |
| `role-D1` | `validators` |
| `role-D2` | `validators` |
| `role-D3` | `validators` |
| `role-D4` | `validators` |
| `role-D6` | `validators` |
| `role-D8` | `validators` |
| `clarify` | `validators`、`terminal` |
| `gates` | `validators` |
| `contract-fidelity` | `validators` |
| `freeze` | `validators` |
| `q-checker` | `validators`、`terminal` |
| `q-inheritance` | `validators`、`terminal` |
| `role-X1` | `validators` |
| `role-X5` | `validators` |
| `evidence` | `validators` |
| `deviation` | `validators` |
| `sign` | `validators` |
| `packaging` | `validators` |
| `source-layout` | `validators` |
| `planning-entry` | `validators` |
| `execution-package` | `validators` |
| `minimum` | `validators` |
| `capability-check` | `validators` |
| `web-later` | `validators` |
| `q-capacity` | `validators`、`terminal` |

上述列表包含合并稿引用提交更新；仅因子节点变化的容器不重复列入。来源引用固定在本分支实际 HEAD 加仓库内路径，本轮未提交改动另用下述摘要定位。

### 全部修改的复述单位

| 单位 id | 改动的读者字段 |
| --- | --- |
| `fail-recovery-whole` | `exampleData`、`expectedResult`、`why`、`onError` |
| `fail-recovery-step-1` | `exampleData`、`expectedResult`、`why`、`onError` |

实际调用固定检查器 `readerHash` 比较本轮 HEAD：只改动 `fail-recovery-whole`、`fail-recovery-step-1`，无新增单位；其余 58 个单位的完整对象未变。两个单位说明普通冲突固定记 stale、保留记录、安全重派披露旧写入，以及用户决定与暂停范围，技术步骤照录新规则。没有生成或补签新的读者通过记录。

因规则同步修改的所有既有 `technical` 字段逐项如下：

| 技术字段 | 同步内容 |
| --- | --- |
| `fail-recovery-whole.technical.action` | 将原第 4 步替换为新四条原文，并补恢复记录每个冲突的处置方式和暂停范围。 |
| `fail-recovery-whole.technical.expectedResult` | 恢复记录列出处置方式 stale-redispatch/user 及暂停范围，检查和回读后只恢复未暂停范围。 |
| `fail-recovery-step-1.technical.action` | 将原第 4 步替换为新四条原文，并补恢复记录每个冲突的处置方式和暂停范围。 |
| `fail-recovery-step-1.technical.expectedResult` | 恢复记录列出处置方式 stale-redispatch/user 及暂停范围，检查和回读后只恢复未暂停范围。 |
| `fail-recovery.technical.outcome` | 由 stop 改为 recover，表示按新规则在检查回读后恢复未暂停范围，等待用户的范围仍暂停。 |
| `fail-recovery.technical.handling` | 完整恢复流程中的第 4 步换成新四条原文，恢复记录补处置方式和暂停范围。 |
| `fail-recovery.technical.userSees` | 收场分别说明普通冲突、交用户情形、暂停范围与其余范围恢复，不再笼统停住全部工作。 |

总量保持 54 个节点、14 条需求、51 条连接、4 条正常走查（23 步）、13 条失败路径（24 步及 13 段整体收场）、60 个复述单位、67 个验收器对象、12 条依据记录。所有验收器仍为 `not-run`、运行记录为空；`versions: []` 保持不变。未实际破坏或恢复任务状态，没有正式冻结。

### 重新生成验收条目清单

在用户指定 D5 目录重新生成 `acceptance-inventory.json`。逐条保留节点 id、标题、条目原文、从零开始的索引和 JSON 出处，按原树顺序重新提取；未拆句、合并、去重或做功能分类。未变的条目沿用上一轮相同的 `needs` 判断，改写或新增条目逐条重判；6 条 `unclear` 及其原因保留。清单所有原文、归属、索引、出处和汇总均已与当前 Blueprint 逐项核对。

**验收条目为 252 条，增加 9 条；`validators` 对象仍为 67 个，增量为零。** 两种口径没有混算。

| 顶层组件 | file-check | real-host | expert | user | unclear | 合计 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 共用任务协议（`shared`） | 43 | 19 | 0 | 8 | 0 | 70 |
| 设计保障（`design`） | 71 | 28 | 0 | 5 | 2 | 106 |
| 交付保障（`delivery`） | 25 | 10 | 6 | 0 | 3 | 44 |
| 同源分发（`packaging`） | 18 | 12 | 1 | 0 | 1 | 32 |
| 合计 | 157 | 69 | 7 | 13 | 6 | 252 |

已重搜整个当前 JSON 的下载/安装相关字符串，并更新 `download_scan` 及末尾 `downloads` 的所有出处。依赖与环境候选仍是 11 项，安装体积未知项没有被估算；没有可从 Blueprint 确认的具体单项超过 100 MB 下载，仍不能据此把大件说明写成“没有”。没有新增下载或安装要求，也没有下载或安装软件。

旧清单 SHA-256：`1da00a5f4cca868f9b41bb31063d763100610e150f15dccb3040a25726959382`；新清单 SHA-256：`d36254b36f53e2b353f8475cc691bf2b8ceff03d85411faff9ac271686005ba9`。清单 `source.sha256` 与下述当前 Blueprint 摘要一致。

### 草稿检查：本轮与既有读者缺口分列

检查器当前提交仍为 `529bbde9b7d0ae9d2be7084fff2b34d9e4a6af1e`，源码未修改。先加载 Node；在缓存目录建立本轮新 JSON、用户指定的读者文件与疑问文件的只读输入链接，再运行离线和在线草稿档各一次。D5 目录原有 Blueprint、读者文件和疑问文件未改写。

```bash
module load nodejs/24.16.0
cd "$BLUEPRINT_WORKTREE/content"
CHECK_INPUT="$BLUEPRINT_WORKTREE/content/.cache/assurance-recovery-conflicts-6aaa8585/blueprint.json"
npx tsx check.mjs --stage draft --offline "$CHECK_INPUT"
npx tsx check.mjs --stage draft "$CHECK_INPUT"
```

变量代指用户指定的工作树，实际传入绝对输入路径；公开说明不记录本机路径。

在改动前，已用当前读者文件对 HEAD 中 Blueprint 单独核对读者规则，确认已有 4 项缺口：`wr-gates`、`wr-freeze`、`fail-freeze-explanation-whole`、`fail-freeze-explanation-step-1`。这些是上一轮尚未补读的固定格式改动，本轮没有再改它们。

| 检查 | 时间（UTC） | 原始退出码 | 本轮读者缺口 | 既有读者缺口 | 其他缺口 | 人工解释待审 | 未完成核实 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 离线草稿 | `2026-11-13T05:34:08.710Z` | 1 | 2 | 4 | 0 | 92 | 1 |
| 在线草稿 | `2026-11-13T05:36:08.623Z` | 1 | 2 | 4 | 0 | 92 | 0 |

本轮两项为 `fail-recovery-whole`、`fail-recovery-step-1` 的 `reader-current-hash`。上述合计六项均按约定单列为预期读者记录缺口，其他缺口为零；没有修改原始检查器报告或把正式 D5/D8 写成通过。在线未完成核实为零；离线唯一未完成项是来源未联网核实。92 项证据解释仍待人工审查。

读者原件 SHA-256 仍为 `c36ddb6392c62d597c05f11a3db71f838ab11fd2f336e298ce3a152b9062d2e7`，疑问原件仍为 `37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570`。

新 JSON 的 SHA-256：

```text
361ce72d7e6a5acd0dab86fef246f7a52dc3209cf62b1e7d61665eea12b5238d
```

本轮没有需要 D1 新增选择的事项。只修改指定工作树中的 JSON 并追加本说明，另重新生成指定 D5 目录的验收条目清单；SPEC、MERGE_DECISIONS、冻结说明正文、流程文档和 A 原稿均未改。未 commit、未 push、未切分支。新 JSON、整份说明和清单按用户指定正则自查，公开信息匹配数均为零。
