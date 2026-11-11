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
