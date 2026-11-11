# Design Assurance 与 Delivery Assurance 插件 0.1 规格（D3 独立设计候选 B）

状态：独立设计候选。它用于 D1 对比、收敛和后续冻结，不代表已经通过 D5–D8，也不代表用户已经批准实现。

## 结论

两个插件应共享一套任务级状态、确定调度、角色卡、提示词模板、修订告知和衡量模式，但用户只看到两个正式入口，不增加第三个总控插件。**Design Assurance** 负责从原始任务到用户批准的冻结合同，包括 Grill Me、D1–D8、完整 Blueprint、九项冻结语义和设计修订；**Delivery Assurance** 从冻结版本接手，负责 X1–X5、实现返修、验收器治理、候选与证据绑定、偏离申报和 X1 唯一签发。共享部分只是两个插件共同打包的能力源和模式，不拥有任务，也不成为新的负责人。

0.1 必须能真实走通“复杂需求 → 两份独立设计 → D5–D8 → 用户冻结 → 实现与三类校准 → 同一最终候选证据 → X1 亲读签发”。首版不建设中央服务、数据库、长期监控、通用隐藏测试平台或默认模型裁判。最大的风险不是状态文件写得不够复杂，而是**冻结合同没有真正固定完成语义，或证据没有绑定到用户最终消费的同一候选**；这两处一旦含糊，后面的角色越多，越容易把降级实现包装成充分验收。另一个会直接影响发布的现实约束是：当前 `marketplacePluginBudget` 为 10，十个顶级插件名额已经占满；两个新插件的源实现可以完成，但正式列入 Marketplace 前必须先决定容量，不能擅自删除现有入口或把双插件偷合成单入口。

## 1. 总体结构与责任边界

Design Assurance 和 Delivery Assurance 共用以下机械能力：任务目录、状态模式、原子写入与冲突检测、角色卡格式、提示词生成器、版本差异、通知模板、证据定位和衡量模式。这些能力由共享源目录提供，但不以第三个插件名暴露，也不获得 D1 或 X1 的决定权。`workflow-core` 继续负责一般执行纪律和来源—实现—验证—报告流程，`ai-skills-core` 负责 AI_Skills_Collection 的源优先修改、生成、回放、回归、版本与发布闭环；两个 Assurance 插件只拥有本流程的专业语义。

Design Assurance 的阶段是：

`design.intake → design.parallel → design.merge → design.gates → design.awaiting_user_freeze → frozen`

Delivery Assurance 的阶段是：

`delivery.plan → delivery.implement → delivery.validate → delivery.repair → delivery.signoff → delivered`

另有四个显式阻塞或返回状态：

`blocked_user`、`blocked_environment`、`returned_to_design`、`failed`

冻结前唯一负责人是 D1；状态进入 `frozen` 后，D1 的当前负责人身份结束，X1 在新的线程接手。X1 退回设计后，状态进入 `returned_to_design`，必须重新指定 D1 线程并形成新的冻结版本。任何子角色的产物、检查结果或证据都不转移负责人身份。

## 2. 状态文件

### 2.1 默认位置与目录

每个被管理项目默认使用一个仓库内目录：

```text
.assurance/
└── tasks/
    └── <task-key>/
        ├── state.json
        ├── artifacts/
        │   ├── design/
        │   │   ├── d1/
        │   │   ├── d2/
        │   │   ├── d3/
        │   │   ├── d4/
        │   │   └── gates/
        │   │       ├── d5/
        │   │       ├── d6/
        │   │       ├── d7/
        │   │       └── d8/
        │   └── delivery/
        │       ├── x1/
        │       ├── x2/
        │       ├── x3/
        │       ├── x4/
        │       └── x5/
        ├── prompts/
        ├── evidence/
        ├── history/
        │   └── events.jsonl
        └── metrics.json
```

`state.json` 是当前状态的唯一权威。`events.jsonl` 是追加式审计和恢复线索，`metrics.json` 是可重建投影；两者都不能覆盖 `state.json`。产物一旦被状态引用，就用仓库相对路径与 SHA-256 固定。公共 AI_Skills_Collection 只保存模式、模板和公开安全测试，不保存私有项目正文、私有仓库内容、账号、凭据、原始数据或聊天全文。

### 2.2 必需字段

```json
{
  "schema_version": "assurance-state-0.1",
  "process_version": "0.1",
  "task": {
    "task_key": "semantic-scope--goal",
    "label": "人类短名",
    "repository": "owner/repo",
    "branch": "target-branch",
    "state_root": ".assurance/tasks/<task-key>",
    "created_at": "ISO-8601"
  },
  "state_revision": 12,
  "previous_state_sha256": "<64 hex>",
  "phase": "design.gates",
  "owner": {
    "role": "D1",
    "thread_ref": "<opaque locator>",
    "assigned_at": "ISO-8601",
    "continuity_break": null
  },
  "blueprint": {
    "path": "artifacts/design/d1/blueprint.json",
    "version": 3,
    "sha256": "<64 hex>",
    "status": "candidate"
  },
  "freeze": null,
  "roles": {},
  "gates": {},
  "user_decisions": [],
  "revision": null,
  "delivery": {
    "candidate_id": null,
    "validators": [],
    "evidence": [],
    "deviations": [],
    "signoff": null
  },
  "metrics": {},
  "next_action": {
    "role": "D6",
    "tier": "planning-general",
    "thread_policy": "new",
    "preconditions": [],
    "prompt_path": "prompts/0012-D6-user-proxy.md",
    "expected_artifacts": []
  },
  "last_transition": {
    "from": "design.merge",
    "to": "design.gates",
    "decided_by": "D1",
    "decision_artifact": "artifacts/design/d1/merge-decision.json",
    "at": "ISO-8601"
  }
}
```

`roles` 中每次派发至少记录 `dispatch_id`、角色、档次、线程策略、输入版本、允许读写路径、提示词路径、状态、产物路径与哈希。`gates` 中 D5–D8 必须记录同一 `blueprint_sha256`。`freeze` 在用户批准后记录 Blueprint 版本、冻结合同路径、`semantic_hash`、用户批准原文定位与批准时间。`delivery` 中的所有正式证据必须引用同一 `candidate_id`。

### 2.3 谁写、什么时候写

D1 在设计阶段拥有状态语义写权，X1 在交付阶段拥有状态语义写权。其他角色只能写自己的派发目录，不得直接改 `state.json`。当负责人所在平台没有仓库写入工具时，插件的机械状态写入命令可以应用负责人已经签发的精确状态补丁；脚本只是执行者，不能替负责人补决定。

状态更新发生在：负责人接手、角色派发、角色产物接收、关卡结果接收、用户决定、修订分类、冻结、候选变更、证据失效、签发或退回。每次更新先读取 `state_revision` 和当前文件哈希，写入 `state_revision + 1` 与 `previous_state_sha256`，再通过同目录临时文件原子替换并提交。

### 2.4 冲突与恢复

不采用最后写入覆盖。更新命令必须带 `expected_revision`；修订号或前序哈希不符时返回 `STATE_CONFLICT`，保留两个输入并暂停依赖动作。若两份更新只是同一合同下互不冲突的角色证据，当前负责人可合并后产生一个新修订；若涉及负责人、冻结语义、候选身份或签发冲突，则必须停止并由当前负责人处理。

负责人线程不可恢复时，不得静默换线程。用户明确重新指定同角色负责人后，状态记录 `continuity_break`、最后有效修订、已发生的外部副作用和新线程定位。发布、付费、删除、部署等动作在中断后不能自动重放。

## 3. 调度与提示词生成

调度器只读取有效 `state.json`、流程 0.1 和角色卡，按以下优先级生成一个 `next_action`：

1. 状态冲突、哈希错误或负责人不合法；
2. 阻塞流程的用户专属决定；
3. 已派发且仍在进行的阻塞角色；
4. 失败关卡或失效证据对应的返修；
5. 当前阶段尚未完成的必跑角色；
6. 已满足触发条件的 D3、D4、X3、X4、X5；
7. 用户冻结、X1 签发或任务结束。

同一状态修订只能产生一个确定动作。多个并行角色可在一个“派发批次”中出现，但批次内部每个角色仍有独立提示词、输入哈希和产物路径；调度器必须明确“本批次可以并行”，不能让角色自行推断依赖。

线程策略如下：

| 角色 | 策略 |
|---|---|
| D1 | 同一设计版本链沿用；大改仍由当前 D1 负责，线程永久丢失才由用户重新指定 |
| D2、D3 | 每次设计轮次新开，互不读取 |
| D4 | 同一现实核查范围可沿用；目标分支、数据权限或核查问题改变时新开 |
| D5 | 每个 Blueprint 哈希使用干净运行；聊天承载时新开 |
| D6、D7 | 每个 Blueprint 哈希新开 |
| D8 | 每一步、每一轮都用新的读者 |
| X1 | 同一冻结合同和交付任务沿用 |
| X2 | 同一冻结合同和返修链沿用；冻结版本变化时新开 |
| X3 | 每次独立验收器实现或重写新开，不继承 X2 说服性叙述 |
| X4 | 同一候选与同一专项检查可沿用；候选变化后重新运行 |
| X5 | 每次最终专业判断新开，不看实现过程 |

Claude 担任 D1 或 X1 且准备自己执行下一步时，先向用户发出事前说明，内容包括要运行的角色、原因、可读材料、写入位置和预期产物；说明写入状态后才执行。GPT 担任负责人时不代替用户启动其他线程，只生成可直接复制的完整提示词。

## 4. 角色卡

### 4.1 Design Assurance

| 角色 | 任务与档次 | 能读什么 | 不能读什么 | 产出位置 | 完成标准 | 回复格式 |
|---|---|---|---|---|---|---|
| D1 设计负责人 | 规划端·专业；持续统筹、Grill Me、合并、冻结语义、修订 | 用户原话、授权来源、状态、所有已完成设计产物与关卡证据 | 未授权私密材料；不得亲自写产品代码；不得把未完成子角色说成总体完成 | `artifacts/design/d1/`，包括 `grill.json`、`merge-decision.json`、合并 Blueprint、冻结合同与通知 | 需求有出处；取舍和被拒方案保留；D5–D8 同哈希通过；用户批准对象明确 | 先给当前判断与影响，再列产物路径、仍需决定事项和唯一下一步；不输出虚假 PASS |
| D2 独立设计者 A | 规划端·专业；完整 Blueprint | 当前任务、指定来源、仓库规则、允许的外部资料 | D3 分支、产物、摘要；D1 的偏好性合并结论 | `artifacts/design/d2/<dispatch-id>/` | 所有需求追到具体设计、实现或有 fallback 的开放问题；问题集中列出 | 自然中文说明设计组成、最小范围、最大风险与问题；附准确路径 |
| D3 独立设计者 B | 规划端·专业；完整 Blueprint | 与 D2 同类的当前任务和指定来源 | D2 分支、产物、摘要；不得借旧候选减少独立设计 | `artifacts/design/d3/<dispatch-id>/` | 同 D2，且明确不确定的平台断言 | 同 D2 |
| D4 现实核查 | 执行端·普通；已有代码、数据或环境时核实 | 目标仓库当前分支、授权数据、命令和现实环境 | 未授权数据、另一设计者分支；不得替 D1 决定产品语义 | `artifacts/design/d4/<dispatch-id>/REALITY_CHECK.md` 与原始探针证据 | 每个事实有来源、命令、实际输出或明确未运行；不把局部探针扩大成总体结论 | 说明已验证事实、不能推出什么、阻塞和产物路径 |
| D5 结构检查 | 执行端·普通；运行 Blueprint 检查器 | 固定 Blueprint 文件、固定 schema/validator 版本、必要来源定位 | 其他评审的说服性结论；不得修改 Blueprint | `artifacts/design/gates/d5/<blueprint-sha>/` | 官方或经批准移植的检查器零错误；九项冻结节点映射完整；记录工具版本与哈希 | 返回通过或逐项缺口、命令、输出、哈希；不宣布冻结 |
| D6 用户代理追问 | 规划端·普通；逐组件代表用户提问 | Blueprint、用户需求原文与获准说明 | D5/D7/D8 结论、D1 对缺口的辩解、实现方案之外的聊天背景 | `artifacts/design/gates/d6/<blueprint-sha>/questions.json` | 每个组件的入口、输入、输出、权威、边界、错误、验收、恢复均可从 Blueprint 回答；阻塞问题为零 | 按组件给问题、Blueprint 中的答案位置或缺口；不自行补答案 |
| D7 冷读 | 执行端·普通；只凭 Blueprint 判断能否开工 | Blueprint 和一句项目简介 | 原始需求、仓库说明、实现代码、D1/D2/D3/D6 讨论 | `artifacts/design/gates/d7/<blueprint-sha>/COLD_READ.md` | 不需要新的产品、架构、接口、验收、权限或资源决定即可开工；纯定位问题已有明确处理路线 | 列出所有仍需问的问题并标明阻塞性；零问题也要明确写零 |
| D8 读者复述 | 规划端·普通；每步由新读者复述 | 当前一步文字和一句项目简介 | 前后步骤、仓库、标准答案、前一读者复述、其他关卡结果 | `artifacts/design/gates/d8/<blueprint-sha>/readability-review.json` | 每步最后一轮复述保持动作、输入、输出、原因和失败处理；文字哈希匹配；读者不复用 | 原样保存收到文字、复述、判断、读者标识、轮次与哈希 |

### 4.2 Delivery Assurance

| 角色 | 任务与档次 | 能读什么 | 不能读什么 | 产出位置 | 完成标准 | 回复格式 |
|---|---|---|---|---|---|---|
| X1 交付负责人 | 规划端·专业；持续统筹、审查验收变化、维护候选证据、唯一签发 | 冻结 Blueprint、冻结合同、状态、最终产物、全部原始证据和偏离 | 不得写产品代码；不得自行改完成标准；不得只读实现者摘要代替原始证据 | `artifacts/delivery/x1/`，包括计划、验收映射、变更审查、`signoff.json` 或 `return-to-design.json` | 同一最终候选证据齐全；X3/X4/X5 条件正确处理；亲读最终产物和关键原始证据；声明不越界 | 先给交付/有限声明/失败/退回结论，再说明候选、证据、未覆盖范围和下一步 |
| X2 实现者 | 执行端·普通；数学符号、精细推导等用执行端·专业 | 冻结合同、目标仓库、现有代码、获准环境、验收规格 | 隐藏控制参考（若真实隔离）；不得改变冻结语义、删减范围或签发 | 授权实现路径及 `artifacts/delivery/x2/<dispatch-id>/` | 实现、正式验收实现、三类校准、回归、偏离和未运行项均有记录；不自报总体完成 | 说明改了什么、候选身份、运行了什么、结果、偏离、未运行项和产物路径 |
| X3 独立验收器实现者 | 执行端·专业；按条件必启 | 冻结语义、不可替代方法、验收规格、校准案例、当前候选身份和必要接口 | X2 的设计辩护、预期绿灯结论、与验收无关的实现叙述 | 授权验收代码路径及 `artifacts/delivery/x3/<dispatch-id>/` | 科研数值/统计/安全验收或弱验收重写独立完成；三类校准满足；说明与 X2 实现差异 | 返回验收器身份、依据、校准、捕获的失败、局限和路径；不签发 |
| X4 专项检查 | 执行端·专业或专门插件；按条件启用 | 冻结的该维度准则、当前最终候选、必要源材料和工具 | 实现者摘要、其他维度结论、修改完成标准的请求 | `artifacts/delivery/x4/<check-family>/<candidate-id>/` | 用现有正式工具或插件检查当前候选；原始证据、工具版本、范围和局限齐全 | 只报告该维度的证据、失败与不适用项，不给总体 PASS |
| X5 独立裁判 | 规划端·专业；开放专业判断无法机械化时必启 | 冻结判断准则、最终产物、必要原始数据或文献、当前候选身份 | 实现过程、X2 说服性摘要、X1 预期结论、其他裁判结论 | `artifacts/delivery/x5/<candidate-id>/` | 独立判断结论、推导、图表等是否满足冻结语义；证据和不确定性完整 | 给独立判断、依据、反例、未决点和证据路径；不签发、不改合同 |

用户只在冻结合同明确存在“必须由人判断”的项目时参加最终验收；其结果仍作为证据交给 X1，不能绕过 X1 的候选一致和其他签发检查。

## 5. 提示词规则与模板

每份派发提示词由“固定外壳 + 角色卡 + 本次材料”生成，必须自包含：

- 当前任务、角色、档次、线程策略和负责人；
- 目标仓库、唯一分支、允许写入路径和禁止读取的分支或材料；
- 当前状态修订、Blueprint 或冻结合同版本与哈希；
- 写入探针：在本角色产出目录创建唯一 `WRITE_PROBE_<dispatch-id>.md`，内容固定为 `Assurance role write probe passed.`；成功后继续，交付前删除，不能删除则说明；
- 按顺序列出的必读材料及其固定提交或当前分支；
- 任务、不得改变的流程、输入和开放问题；
- 精确产出文件、完成标准、原始证据要求；
- 回复格式和不得声称的状态。

模板如下：

```text
当前任务：<一句话说明本角色要完成什么，以及当前流程到哪里。>
运行身份：<D1–D8 或 X1–X5；档次；新开/沿用线程。>

目标仓库：<owner/repo>
唯一分支：<branch>
允许写入：<paths>
禁止读取或修改：<branches/paths/materials>

先测试写入：
<probe path and exact content>

当前权威：
- state revision: <n>
- Blueprint/freeze version: <version>
- SHA-256: <hash>
- current owner: <D1/X1>

先完整读取：
1. <source@revision:path>
2. ...

任务：
<角色卡任务 + 本次具体材料>

完成条件：
<可判定条件>

产出：
<exact paths>

回复：
<自然中文要说明什么；不得用局部 PASS 冒充总体完成>
```

公开仓库提示词只写私有项目的仓库名、分支和路径，不复制私有正文、数据、截图、原始证据或账号信息。需要真实私有内容时，角色在获准的项目环境读取，公共 AI_Skills 只保留模式和公开安全替代案例。

## 6. 修订与告知

### 6.1 小修订

小修订必须同时满足：

1. 只影响至多两个既有节点，不新增、删除、替换或重排节点；
2. 不改需求原文或来源；
3. 不改连接、跨组件接口、权威、正常入口、失败路径、走查中给读者看的文字；
4. 不改冻结合同九项中的任何语义、阈值、范围、证据真实度、允许替代、旧功能承诺、权限或资源边界；
5. 不引入只有用户能决定的新问题；
6. 只修证据定位、提交或文件哈希、非语义技术说明、实现状态，且字段级差异能证明上述条件。

D1 先告知用户，再修改并产生新候选版本；受影响动作暂停，只重跑 D5。这里刻意把小修订范围收得很窄，是为了与流程 0.1“只重跑结构检查”一致，也避免修改读者文字后继续沿用旧 D8 复述。

### 6.2 大改

任一小修订条件不满足，或无法确定是否满足，都按大改。典型触发包括：需求、接口、权威、正常入口、失败处理、完成标准、证据真实度、声明范围、权限、费用、数据、账号、设备、用户专属决定，或需要新增/替换节点。D1 重新汇总，按影响派 D2、D3、D4，并重新运行 D5–D8；旧冻结和旧关卡证据保留历史但不再授权新实现。

交付端对日志、路径、选择器、解析、版本和等价运行器的机械修复不属于设计修订，但 X1 必须记录变更分类并重跑三类校准。只要需要改变“什么算完成”，立即转为大改并退回 D1。

### 6.3 告知模板

事前：

```text
准备修订：<对象与版本>
原因：<具体缺口及证据>
分类：小修订 / 大改
影响：<节点、角色、暂停范围、旧证据失效范围>
本轮动作：<D1 自行执行前的说明，或给用户复制的提示词>
```

事后：

```text
修订已完成：<旧版本> → <新版本>
实际差异：<字段或节点级变化>
原因归类：本可想到 / 跑了才知道
重新运行：<D5 或 D5–D8 及结果定位>
恢复范围：<哪些角色继续，哪些证据仍有效>
仍需决定：<无则写无>
```

缺少任何一次告知时，相关阶段不能继续。

## 7. Grill Me、冻结关卡和冻结合同

### 7.1 Grill Me

每个问题先归入：

- `USER_ONLY`：偏好、风险接受、权限、费用、账号、用途、不可替代的人类选择。成组问用户，并给选项、推荐和不回答影响；
- `RESEARCHABLE`：平台行为、现有代码、数据、文献、成熟实践。转成证据任务，不问用户猜事实；
- `DESIGNER_DECISION`：架构、默认值、实现取舍。D1 决定并保存理由、替代和被拒方案。

问题为零是合法结果。冻结前，所有会改变需求、接口、验收语义、权限或资源边界的 `USER_ONLY` 必须有带出处回答。

### 7.2 D5–D8 通过标准

| 关卡 | 通过标准 | 失败退回 |
|---|---|---|
| D5 结构检查 | Asteria Blueprint v3 结构和跨引用零错误；需求均有路线；叶子均为真实实现、具体设计或带 fallback 的开放问题；四类失败完整；九项冻结节点可编译；版本和哈希一致 | 回 D1 修结构；若改变语义，按大改 |
| D6 用户代理 | 每个组件的入口、输入、输出、权威、边界、错误、验收、证据、恢复均能从 Blueprint 回答；阻塞问题为零 | 回 D1 补设计；涉及用户专属决定时回 Grill Me |
| D7 冷读 | 只看 Blueprint 即可开工；没有新的产品、架构、接口、验收、权限或资源决定。明确列出的非阻塞开放问题必须有负责人和 fallback | 回 D1；不能让执行者临场决定 |
| D8 读者复述 | 每一步最后一轮复述保持动作、拿到什么、交出什么、原因和失败结果；每轮新读者；文字哈希与当前 Blueprint 一致 | 回 D1 重写对应文字并重新复述 |

四关可以并行，但只有同一 `blueprint_sha256` 的四个通过结果可以汇合。用户批准的对象必须明确到 Blueprint 版本、哈希、冻结合同 `semantic_hash` 和关卡证据路径。

### 7.3 冻结合同格式

Asteria v3 是严格结构，0.1 不向顶层随意塞自定义字段。每份 Blueprint 必须包含一个“冻结合同”节点，其下固定九个子节点；编译器将它们确定性导出为：

```json
{
  "schema_version": "assurance-freeze-contract-0.1",
  "task_key": "<task-key>",
  "contract_version": 3,
  "blueprint": {
    "path": "<repo-relative path>",
    "version": 3,
    "sha256": "<64 hex>"
  },
  "capability_and_claim_scope": {},
  "normal_entry_and_final_object": {},
  "outcome_semantics": {
    "pass": {},
    "fail": {},
    "unknown": {}
  },
  "evidence_and_irreplaceable_methods": {},
  "forbidden_substitutes": [],
  "protected_existing_behavior": {},
  "calibration_cases": {
    "positive": [],
    "bad": [],
    "missing_evidence": []
  },
  "change_authority": {
    "delivery_may_change": [],
    "return_to_design": []
  },
  "resource_boundaries": {
    "permissions": [],
    "data": [],
    "cost": [],
    "accounts": [],
    "devices": []
  },
  "semantic_hash": "<canonical JSON SHA-256>",
  "user_approval": {
    "locator": "<thread/message>",
    "approved_at": "ISO-8601"
  }
}
```

Blueprint 中的九个节点是语义权威，`freeze-contract.json` 是交付端的规范化投影。投影与 Blueprint 哈希不一致时拒绝交付派发。冻结合同不能只写“测试通过”；每项要说明用户最终能得到什么、什么失败、证据要观察什么、哪些替代被禁止，以及旧能力不能怎样退化。

## 8. 验收器、候选、证据、偏离和签发

### 8.1 验收器分级

| 变化 | X1 处理 |
|---|---|
| 增加日志、截图、探针等诊断 | 可批准；不改变结果语义 |
| 修路径、选择器、版本、解析或不稳定 | 可批准；修后重跑正例、坏例、缺证例 |
| 换同等真实度方法 | 可批准，但必须证明观察对象、阈值、覆盖和证据真实度不变 |
| 增加更严格坏例或回归 | 可批准，前提是不缩小冻结合同允许的合法实现空间 |
| 改阈值、范围、总体、入口、证据真实度、允许替代、旧功能或声明范围 | 不可批准；退回 D1 形成新冻结版本 |

每个验收器规格必须包括：冻结语义引用、声明、正常入口、最终对象、方法、准则、`pass/fail/unknown`、不可替代方法、运行器、环境、正/坏/缺证校准、候选绑定、实现者、准入者、变更分类和证据失效条件。

X3 在科研数值或统计、安全相关验收，以及校准证明验收器太弱需要换人重写时必须启用。X4 在交付物存在可由现成专门插件或工具检查的维度时启用。X5 在关键专业判断不能被冻结准则和机械检查充分给出时必须启用。新线程、独立工作树或“不告诉实现者测试内容”不等于真实隐藏；只有访问权限隔离成立时才可称隐藏用例。

### 8.2 候选与证据记录

`candidate.json` 至少包含：

```json
{
  "candidate_id": "<stable id>",
  "freeze_contract_version": 3,
  "freeze_semantic_hash": "<hash>",
  "source": {
    "repository": "owner/repo",
    "commit_or_file_set": "<identity>"
  },
  "build_object": {"path": "...", "sha256": "..."},
  "installed_or_deployed_object": {"identity": "..."},
  "runner": {"name": "...", "version": "..."},
  "environment": {},
  "data_and_parameters": {},
  "observed_at": "ISO-8601",
  "final_consumption_object": {},
  "allowed_claim_scope": []
}
```

每条证据至少包含：

```json
{
  "evidence_id": "<id>",
  "candidate_id": "<same final candidate>",
  "validator_id": "<id>",
  "evidence_type": "<type>",
  "fidelity": "<what it directly observes>",
  "producer": "<role/tool>",
  "observed_at": "ISO-8601",
  "raw_path": "<repo-relative or approved locator>",
  "sha256": "<64 hex>",
  "outcome": "pass|fail|unknown",
  "supports_claims": [],
  "does_not_support": [],
  "freshness": {},
  "invalidated_by": []
}
```

候选、冻结语义、运行器、样本、环境或最终对象变化时，先按 `invalidated_by` 使旧证据失效，再决定重跑范围。不同候选的局部绿灯不能拼接。

### 8.3 偏离申报

```json
{
  "deviation_id": "<id>",
  "frozen_clause": "<contract locator>",
  "expected": "<frozen behavior>",
  "actual": "<current behavior>",
  "reason": "<specific reason>",
  "user_impact": "<impact>",
  "substitute_used": null,
  "executed_checks": [],
  "unrun_checks": [],
  "evidence_gaps": [],
  "disposition": "repair|limited-claim|return-design|blocked",
  "decided_by": "X1"
}
```

X2 必须主动申报所有偏离、替代、未运行项和证据缺口。没有申报不代表没有偏离；X1 仍需对照冻结合同和最终产物检查。

### 8.4 X1 签发清单

X1 只能在以下项目逐项有 `yes/no/unknown` 后签发：

1. 冻结版本、Blueprint 哈希和 `semantic_hash` 一致；
2. 当前 `candidate_id` 是用户将收到的最终对象；
3. 每项冻结义务有验收器或明确的人类判断；
4. 关键验收已完成正例、坏例、缺证例校准；
5. 正式验收、回归和专项检查作用于同一最终候选；
6. 正常入口与最终消费对象真实走通；
7. 旧能力和代表性回归未退化；
8. X3、X4、X5 的触发条件正确处理；
9. 偏离、替代、未运行项和证据缺口已有处置；
10. 权限、数据、费用、账号和设备边界没有越界；
11. 最后一次证据后候选未改变；
12. X1 已亲自打开最终产物和承载关键结论的原始证据，并在 `read_attestations` 中记录 `evidence_id`、`read_at` 和观察结论；
13. 最终声明没有超过冻结范围和实际证据。

任何 `unknown` 都不能写成无条件交付；可以给有限声明、等待补证或失败。X1 只在流程规定的五类情况退回设计，其余实现或验收程序缺陷都回 X2 同一任务返修。

## 9. 衡量记录

强制记录：

- 冻结后用户新增了多少个“本可想到”的问题，每个问题的位置、影响和归因；
- 退回设计的次数与类别；
- 每次修订是否都有事前和事后告知。

辅助记录：各阶段起止、角色派发和返修轮次、状态冲突、验收器机械修复次数、三类校准失败、候选证据错配、证据失效、X3/X4/X5 启用原因。所有计数必须能追到事件或版本，不保存私密正文。指标用于发现流程缺口，不用于自动降低关卡、删除角色或给模型排名。

## 10. 打包设计

### 10.1 推荐源目录

以下是候选 B 的推荐结构；`QUESTIONS.md` 中的规划技能复用决定可能把一个共享入口改成两个薄入口，但共享语义文件不变。

```text
skills/core/codex-system/
├── assurance-planning/
│   ├── SKILL.md
│   ├── references/
│   │   ├── process-0.1.md
│   │   ├── state-and-dispatch.md
│   │   ├── role-cards-design.md
│   │   ├── role-cards-delivery.md
│   │   ├── freeze-and-revision.md
│   │   └── validation-and-signoff.md
│   ├── schemas/
│   │   ├── assurance-state.schema.json
│   │   ├── freeze-contract.schema.json
│   │   ├── validator.schema.json
│   │   ├── candidate.schema.json
│   │   ├── evidence.schema.json
│   │   ├── deviation.schema.json
│   │   └── signoff.schema.json
│   └── templates/
│       ├── role-prompt.md
│       ├── pre-revision-notice.md
│       └── post-revision-notice.md
├── design-assurance-execution/
│   ├── SKILL.md
│   ├── scripts/
│   │   ├── state.py
│   │   ├── dispatch.py
│   │   ├── render_prompt.py
│   │   ├── compile_freeze_contract.py
│   │   └── validate_blueprint.*
│   └── references/
└── delivery-assurance-execution/
    ├── SKILL.md
    ├── scripts/
    │   ├── bind_candidate.py
    │   ├── validate_evidence.py
    │   ├── classify_validator_change.py
    │   ├── invalidate_evidence.py
    │   └── verify_signoff.py
    └── references/

scripts/codex_marketplace_config.json
assets/codex/plugin-icons/design-assurance/
assets/codex/plugin-icons/delivery-assurance/
tests/test_assurance_state.py
tests/test_assurance_dispatch.py
tests/test_assurance_prompts.py
tests/test_assurance_revision.py
tests/test_assurance_blueprint_adapter.*
tests/test_delivery_validator_governance.py
tests/test_delivery_evidence_binding.py
tests/test_delivery_signoff.py
```

`design-assurance` 插件配置打包 `assurance-planning` 与 `design-assurance-execution`；`delivery-assurance` 打包同一规划能力源与 `delivery-assurance-execution`。若运行时不能安全地在两个插件中复用同名规划技能，则生成两个不同名称的薄入口，但它们只能引用同一组 `references/`、schema 和模板，不能复制并分叉流程语义。

### 10.2 Marketplace 容量

当前 `scripts/codex_marketplace_config.json` 的 `marketplacePluginBudget` 是 10，现有顶级条目也正好有 10 个：`workflow-core`、`ai-skills-core`、`writing-style`、`research-writing`、`presentations`、`scientific-visualization`、`web-development`、`statistical-modeling`、`bioinformatics`、`medical-imaging`。因此，按当前配置直接追加两个插件会超过既有预算。

0.1 的设计仍保留两个独立插件身份、源技能和生成包；实现者不得为了过预算而自行删除现有插件、提高预算、把两个 Assurance 合并成一个插件，或只生成其中一个。D1 必须在实现包冻结前决定正式发布路线：扩大预算、经单独产品决定调整现有入口，或先完成两个可直接安装的候选包而暂不列入 Marketplace。候选包路线只能声称“可直接安装并已验证”，不能声称“已上架 Marketplace”。这个决定见 `QUESTIONS.md`。

### 10.3 Claude Code 与 GPT Work

规划规则的权威是源 `SKILL.md`，而不是某次提示词。Claude Code 的项目自动发现位置是 `.claude/skills/<skill>/SKILL.md`，所以实施阶段应提供安装适配器，把权威源复制到该位置并做字节或内容哈希一致检查；也允许在维护任务中按固定提交和精确路径直接读取。适配器不能改写角色权限或默认值。

对 GPT Work，0.1 只承诺经过验证的使用方式：提示词给出仓库、提交和 `SKILL.md` 路径并要求完整读取。没有官方或真实平台证据前，不宣称它会自动扫描任意仓库 `skills/` 路径。若设计负责人要求自动发现，这应成为独立 Capability Gate，而不是文档中的假设。

### 10.4 Codex 插件

实施时先改 `skills/` 和 `scripts/codex_marketplace_config.json`，再用现有生成器产生：

```text
plugins/codex/plugins/design-assurance/
├── .codex-plugin/plugin.json
└── skills/...

plugins/codex/plugins/delivery-assurance/
├── .codex-plugin/plugin.json
└── skills/...
```

生成目录只作构建产物。正式插件改动同时使用 `workflow-core + ai-skills-core + 目标 Assurance 插件`：前者管执行纪律，第二个管仓库维护闭环，目标插件管本流程专业语义。

### 10.5 ChatGPT 网页端

0.1 不实现网页端包。后续从同一权威技能生成根 `plugin.json`、`skills/` 和必要资源的便携包，再做真实上传、扫描、触发、权限、隐私、安装后行为和正常入口验收。网页端不得重新写一套角色或冻结规则。

## 11. 0.1 与 0.2 边界

| 0.1 必须有 | 0.2 才考虑 |
|---|---|
| 仓库内任务状态、修订链、冲突保护 | 中央服务、数据库、跨项目实时看板 |
| 确定调度、线程策略和自包含提示词 | 自动跨平台线程创建与恢复 |
| D1–D8、X1–X5 全角色卡 | 基于长期数据自动推荐角色组合 |
| Grill Me、D5–D8、九项冻结合同 | 图形化 Blueprint 编辑与流程可视化 |
| 小修订/大改和双告知 | 复杂多分支并行合并界面 |
| 验收器分级、三类校准、X3/X5 条件 | 通用隐藏测试托管和受保护验证服务 |
| 候选、证据、偏离、失效和 X1 签发 | 外部证明、签名、不可抵赖日志 |
| 必需衡量和公开安全端到端试跑 | 跨任务统计、模型比较和自动优化 |
| 两个独立插件的源实现与生成包；Marketplace 容量未决时只做直接安装候选 | ChatGPT 网页端正式打包、Marketplace 扩容后的公开发布 |

0.2 的任何项目都必须由真实试跑中的重复失败推动，并再次经过 Design Assurance；不能因为“以后可能需要”就把首版升级为平台工程。

## 12. 0.1 实现验收重点

在任何发布检查之前，先验证 `marketplacePluginBudget` 与顶级插件数量。容量未获批准时，验收对象是两个独立、可直接安装的最终候选包，而不是 Marketplace 上架；发布文案不得越过这一边界。

正式实现至少需要以下真实能力门：

1. 同一状态输入产生确定下一动作；并发旧修订不能覆盖新状态；
2. D2、D3 的提示词与可读材料确实互相隔离；
3. D5–D8 只能在同一 Blueprint 哈希上汇合；
4. 九项冻结合同能从 Blueprint 确定性导出并回读一致；
5. 代表性小修订通过，接口或语义变化被强制判为大改；
6. 关键验收器的正例、坏例、缺证例分别为 `pass/fail/unknown`；
7. 修改候选后旧证据自动失效，跨候选拼接被拒绝；
8. X1 未亲读最终产物或关键原始证据时不能签发；
9. 源技能、市场配置、生成插件、安装身份和正常入口一致；
10. 用公开安全的完整任务分别走通设计到冻结、冻结到交付，并覆盖状态冲突、结果不可信和前提失效三条关键失败链。

这些能力门由 D1 收敛后另行冻结。本候选没有运行它们，也不以 JSON 文件存在代替插件能力。
