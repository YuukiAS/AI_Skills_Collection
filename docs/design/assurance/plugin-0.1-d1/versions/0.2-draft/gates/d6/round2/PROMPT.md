# D6 第 2 轮：D1 修正后的定向复核

在全新的 GPT 网页端对话运行，使用最高推理；与 D8 使用不同的新对话。你是 D6 用户代理，Claude 以 D1 身份裁决。本提示词内嵌本轮全部必要材料，不需要读仓库设计或历史对话；不要扩大成 62 节点的全量重审。

只报告改动位置引入的问题；改动之外的新发现记为 non-blocking 留给 0.3，除非与改动直接矛盾。

## 身份与边界

公开仓库：https://github.com/YuukiAS/AI_Skills_Collection
任务分支：`design/assurance-plugins-0.1-merged`
修改前公开基线：`6c21bff4e83c26058d68f3f4680efe099cb1daba`
当前 Blueprint 原始字节 SHA-256：`d7c4055ca4485862230e8a3ab9edb4fc55e1bba4ca18c4a0e12f44d330ca8e9d`
当前 snapshot_sha256（RFC 8785 / snapshotOf，不含版本历史）：`3efb23ecf3d77ba81a1243d6d7b442f9878f876459941fae9c083a064b6a3b8d`

这些是输入声明值。只审内嵌摘录时请如实写“未独立核验完整文件哈希”；不得将摘录重新序列化后声称核验了原文件。缺必要材料时报告 NOT_RUN 和具体缺项，不补答案。

本轮首要对象：role-D1.description、role-D6.description、gates 的 0.2 差异范围和新增 D5 扫描；并核对同步的 wr-gates.technical.action 与当前证据摘要。直接引用节点：contract, fr-decisions, fr-downloads, fr-roles, revision, role-D2, role-D3, role-D4, role-D5, role-D7, role-D8, role-X1。连接仅用来确认直接关系，不沿引用递归扩大；其余正文只为判断改动是否引入矛盾而提供。第 2 步的读者改写由 D8 单独复述，不作为本轮新的全量审查对象。

## D1 已裁决的要求

- D1 将冻结审阅内容写入 Blueprint 的 freeze-review 节点组，用户在“冻结审阅”视图中完成审阅，不再另写冻结说明。
- D6 核对 freeze-review 节点内容与设计一致：答案是否在 Blueprint 中、是否与其他节点矛盾；不恢复独立冻结说明或其四项检查。
- D6 覆盖自上次通过以来自身字段变化的全部节点，本轮为 62 个；D8 覆盖文字有变化的读者单位，保留既有受影响相邻单位规则。首轮 62×7 的通过项不重新追问。
- 按 MERGE §29 的收敛规则，只复核改动及其直接引用；转述偏差按原文机械修正，不开无边界新轮。
- D5 在 D6/D8 之前运行废弃语义扫描。当前正文残留即报错，修正仅限已批准的 0.2 替换，逐处记录。0.1 历史、明确删除说明、准确历史引用和稳定机器 ID 保留。
- 本轮整体完成：D5 机械检查通过（快照差异与待 D8 项除外）＋ D6 无 blocking ＋ D7 全部 9 个回归用例通过 ＋ D8 全部受审单位复述正确；任何一关有 blocking 即未完成。这是条件定义，不是本次已经通过的声明；实际回归仍未运行。

## 首轮三个 blocking 的关闭条件

1. D1 短描述改为写入 freeze-review；与正文一致。
2. D6 短描述改为检查 freeze-review；与正文一致。
3. gates 和 wr-gates.technical.action 使用真实差异范围，不再仅限三个列举组；D8 范围按其读者文字差异规则。

逐项判断是否关闭；新增问题必须给出与某个具体改动的直接因果关系、影响及关闭条件。只追问对本轮改动确实适用的进入/输入、输出/接收人、决定权、失败、验收、恢复、旧能力问题，不强凑 434 项。

## 改动位置与前后文字（第 1、3 步）

```json
[
  {
    "pointer": "/nodes/1/children/0/children/0/description",
    "before": "唯一负责人；规定验收语义；写冻结说明；审定改变完成标准的修订",
    "after": "唯一负责人；规定验收语义；将冻结审阅内容写入 Blueprint 的 freeze-review 节点组；审定改变完成标准的修订"
  },
  {
    "pointer": "/nodes/1/children/0/children/5/description",
    "before": "扮演用户逐组件追问，答案不在 Blueprint 里即缺口；并核对冻结说明",
    "after": "扮演用户逐组件追问，答案不在 Blueprint 里即缺口；核对 freeze-review 节点内容与设计一致"
  },
  {
    "pointer": "/nodes/1/children/2/terminal/mechanism",
    "changed_spans_with_100_char_context": [
      {
        "before": "该快照，freeze.json 不再包含 explanation_sha256。\n\n**本次 0.2 关卡与收口：** 按修订规则属于大改，在新快照上重跑：D5（机械，全量）、D7（Codex，全量）；D6、D8 只针对新增和改写的节点（`freeze-review` 组、D1 澄清节点、冻结节点），未改动节点沿用 0.1 的通过记录——这是 D1 依用户授权（2026/11/15“不要过多浪费时间",
        "after": "该快照，freeze.json 不再包含 explanation_sha256。\n\n**本次 0.2 关卡与收口：** 按修订规则属于大改，在新快照上重跑：D5（机械，全量）、D7（Codex，全量）。D6 覆盖自上次通过以来自身字段有变化的全部节点，按节点自身字段计算，子节点变化不重复归到父节点；本轮为全部 62 个节点。D8 覆盖文字有变化的读者单位，并按既有规则纳入受影响的同一步骤或同一失败路"
      },
      {
        "before": "，freeze.json 不再包含 explanation_sha256。\n\n**本次 0.2 关卡与收口：** 按修订规则属于大改，在新快照上重跑：D5（机械，全量）、D7（Codex，全量）；D6、D8 只针对新增和改写的节点（`freeze-review` 组、D1 澄清节点、冻结节点），未改动节点沿用 0.1 的通过记录——这是 D1 依用户授权（2026/11/15“不要过多浪费时间”）作",
        "after": "，freeze.json 不再包含 explanation_sha256。\n\n**本次 0.2 关卡与收口：** 按修订规则属于大改，在新快照上重跑：D5（机械，全量）、D7（Codex，全量）。D6 覆盖自上次通过以来自身字段有变化的全部节点，按节点自身字段计算，子节点变化不重复归到父节点；本轮为全部 62 个节点。D8 覆盖文字有变化的读者单位，并按既有规则纳入受影响的同一步骤或同一失败路径单位；文字和哈希均未变的单位沿用最近一次真实通过记录。范围以实际差异确定，不限于 freeze-review 组、D1 澄"
      },
      {
        "before": "eze.json 不再包含 explanation_sha256。\n\n**本次 0.2 关卡与收口：** 按修订规则属于大改，在新快照上重跑：D5（机械，全量）、D7（Codex，全量）；D6、D8 只针对新增和改写的节点（`freeze-review` 组、D1 澄清节点、冻结节点），未改动节点沿用 0.1 的通过记录——这是 D1 依用户授权（2026/11/15“不要过多浪费时间”）作出的收口决定，记",
        "after": "于大改，在新快照上重跑：D5（机械，全量）、D7（Codex，全量）。D6 覆盖自上次通过以来自身字段有变化的全部节点，按节点自身字段计算，子节点变化不重复归到父节点；本轮为全部 62 个节点。D8 覆盖文字有变化的读者单位，并按既有规则纳入受影响的同一步骤或同一失败路径单位；文字和哈希均未变的单位沿用最近一次真实通过记录。范围以实际差异确定，不限于 freeze-review 组、D1 澄清节点和冻结节点。D6/D8 定向复核只查改动位置及其直接引用；改动之外的新发现记为 n"
      },
      {
        "before": "on 不再包含 explanation_sha256。\n\n**本次 0.2 关卡与收口：** 按修订规则属于大改，在新快照上重跑：D5（机械，全量）、D7（Codex，全量）；D6、D8 只针对新增和改写的节点（`freeze-review` 组、D1 澄清节点、冻结节点），未改动节点沿用 0.1 的通过记录——这是 D1 依用户授权（2026/11/15“不要过多浪费时间”）作出的收口决定，记入 `",
        "after": "次通过以来自身字段有变化的全部节点，按节点自身字段计算，子节点变化不重复归到父节点；本轮为全部 62 个节点。D8 覆盖文字有变化的读者单位，并按既有规则纳入受影响的同一步骤或同一失败路径单位；文字和哈希均未变的单位沿用最近一次真实通过记录。范围以实际差异确定，不限于 freeze-review 组、D1 澄清节点和冻结节点。D6/D8 定向复核只查改动位置及其直接引用；改动之外的新发现记为 non-blo"
      },
      {
        "before": "不再包含 explanation_sha256。\n\n**本次 0.2 关卡与收口：** 按修订规则属于大改，在新快照上重跑：D5（机械，全量）、D7（Codex，全量）；D6、D8 只针对新增和改写的节点（`freeze-review` 组、D1 澄清节点、冻结节点），未改动节点沿用 0.1 的通过记录——这是 D1 依用户授权（2026/11/15“不要过多浪费时间”）作出的收口决定，记入 `MERGE",
        "after": "身字段有变化的全部节点，按节点自身字段计算，子节点变化不重复归到父节点；本轮为全部 62 个节点。D8 覆盖文字有变化的读者单位，并按既有规则纳入受影响的同一步骤或同一失败路径单位；文字和哈希均未变的单位沿用最近一次真实通过记录。范围以实际差异确定，不限于 freeze-review 组、D1 澄清节点和冻结节点。D6/D8 定向复核只查改动位置及其直接引用；改动之外的新发现记为 non-blocking 留给 0.3，除非与改动直接矛盾。若只发现转述性"
      },
      {
        "before": "sha256。\n\n**本次 0.2 关卡与收口：** 按修订规则属于大改，在新快照上重跑：D5（机械，全量）、D7（Codex，全量）；D6、D8 只针对新增和改写的节点（`freeze-review` 组、D1 澄清节点、冻结节点），未改动节点沿用 0.1 的通过记录——这是 D1 依用户授权（2026/11/15“不要过多浪费时间”）作出的收口决定，记入 `MERGE_DECISIONS.md`",
        "after": "62 个节点。D8 覆盖文字有变化的读者单位，并按既有规则纳入受影响的同一步骤或同一失败路径单位；文字和哈希均未变的单位沿用最近一次真实通过记录。范围以实际差异确定，不限于 freeze-review 组、D1 澄清节点和冻结节点。D6/D8 定向复核只查改动位置及其直接引用；改动之外的新发现记为 non-blocking 留给 0.3，除非与改动直接矛盾。若只发现转述性偏差，D1 按 Bluep"
      },
      {
        "before": "本次 0.2 关卡与收口：** 按修订规则属于大改，在新快照上重跑：D5（机械，全量）、D7（Codex，全量）；D6、D8 只针对新增和改写的节点（`freeze-review` 组、D1 澄清节点、冻结节点），未改动节点沿用 0.1 的通过记录——这是 D1 依用户授权（2026/11/15“不要过多浪费时间”）作出的收口决定，记入 `MERGE_DECISIONS.md` 第 30 节。D6/",
        "after": "覆盖文字有变化的读者单位，并按既有规则纳入受影响的同一步骤或同一失败路径单位；文字和哈希均未变的单位沿用最近一次真实通过记录。范围以实际差异确定，不限于 freeze-review 组、D1 澄清节点和冻结节点。D6/D8 定向复核只查改动位置及其直接引用；改动之外的新发现记为 non-blocking 留给 0.3，除非与改动直接矛盾。若只发现转述性偏差，D1 按 Blueprint 原文改正后机"
      },
      {
        "before": "2 关卡与收口：** 按修订规则属于大改，在新快照上重跑：D5（机械，全量）、D7（Codex，全量）；D6、D8 只针对新增和改写的节点（`freeze-review` 组、D1 澄清节点、冻结节点），未改动节点沿用 0.1 的通过记录——这是 D1 依用户授权（2026/11/15“不要过多浪费时间”）作出的收口决定，记入 `MERGE_DECISIONS.md` 第 30 节。D6/D8 若只发现转述性偏差，D1 按 Blueprint 原文改正后机械核对，不再开新轮。",
        "after": "变化的读者单位，并按既有规则纳入受影响的同一步骤或同一失败路径单位；文字和哈希均未变的单位沿用最近一次真实通过记录。范围以实际差异确定，不限于 freeze-review 组、D1 澄清节点和冻结节点。D6/D8 定向复核只查改动位置及其直接引用；改动之外的新发现记为 non-blocking 留给 0.3，除非与改动直接矛盾。若只发现转述性偏差，D1 按 Blueprint 原文改正后机械核对，"
      },
      {
        "before": "点），未改动节点沿用 0.1 的通过记录——这是 D1 依用户授权（2026/11/15“不要过多浪费时间”）作出的收口决定，记入 `MERGE_DECISIONS.md` 第 30 节。D6/D8 若只发现转述性偏差，D1 按 Blueprint 原文改正后机械核对，不再开新轮。",
        "after": "，并按既有规则纳入受影响的同一步骤或同一失败路径单位；文字和哈希均未变的单位沿用最近一次真实通过记录。范围以实际差异确定，不限于 freeze-review 组、D1 澄清节点和冻结节点。D6/D8 定向复核只查改动位置及其直接引用；改动之外的新发现记为 non-blocking 留给 0.3，除非与改动直接矛盾。若只发现转述性偏差，D1 按 Blueprint 原文改正后机械核对，不再开无边界的新轮。\n\n**D5 前置扫描：** D5 在 D6/D8 之前先运行废弃语义扫描：python tools/scan"
      },
      {
        "before": "/11/15“不要过多浪费时间”）作出的收口决定，记入 `MERGE_DECISIONS.md` 第 30 节。D6/D8 若只发现转述性偏差，D1 按 Blueprint 原文改正后机械核对，不再开新轮。",
        "after": "/D8 定向复核只查改动位置及其直接引用；改动之外的新发现记为 non-blocking 留给 0.3，除非与改动直接矛盾。若只发现转述性偏差，D1 按 Blueprint 原文改正后机械核对，不再开无边界的新轮。\n\n**D5 前置扫描：** D5 在 D6/D8 之前先运行废弃语义扫描：python tools/scan_deprecated_semantics.py（从本设计目录运行）。清单依据 RE"
      },
      {
        "before": "/15“不要过多浪费时间”）作出的收口决定，记入 `MERGE_DECISIONS.md` 第 30 节。D6/D8 若只发现转述性偏差，D1 按 Blueprint 原文改正后机械核对，不再开新轮。",
        "after": "核只查改动位置及其直接引用；改动之外的新发现记为 non-blocking 留给 0.3，除非与改动直接矛盾。若只发现转述性偏差，D1 按 Blueprint 原文改正后机械核对，不再开无边界的新轮。\n\n**D5 前置扫描：** D5 在 D6/D8 之前先运行废弃语义扫描：python tools/scan_deprecated_semantics.py（从本设计目录运行）。清单依据 REVISION_0.2_PLAN 与 MERGE_DECISIONS 的已批准删除或改名；扫描全部当前节点文字，并检查走查与当前证据摘要，排除 versions 冻结历史。现行要求出现残留即报错并停止 D6/D8；明确的删除说明、准确的历史引用和稳定机器 ID 不算残留。修正仅限已批准的 0.2 文字替换，逐处记录后重跑至残留为零；该扫描属于 D5，不代替原检查器。\n\n**本轮整体完成条件（D1 裁决）：** 四道关卡“整体完成”是指：D5 机械检查通过（快照差异与待 D8 项除外，废弃语义扫描须零残留）；D6 无 blocking；D7 全部 9 个回归用例通过；D8 全部受审单位复述正确。任何一关有 blocking 即未完成。"
      }
    ]
  },
  {
    "pointer": "/evidence/10/proves",
    "before": "第 17 节用户决定：网页端打包纳入 0.1，复用已测通方法并由 X4 真实验收、X1 签发；本插件自身的 X1 为 GPT Work 极高，Claude 仅做机械启动 Codex 的运输。第 15 节通用负责人规则继续有效。 第 20 节要求冻结说明固定格式，冻结前由 D6 对照检查，并对新快照重新跑规定关卡。 第 21 节补定普通恢复冲突的处置、原始记录保留、重派写入披露、用户决定边界及未决范围隔离。 第 22 节补定说明身份、改动后 D6 说明检查失效及实际下载大小和用户授权依据。 第 23 节明确执行端按档次表运行、GPT Work 极高不得用 Codex 代替、X4 记录选择与手动执行角色每轮一条。 第 24 节补定回归用例集、按条覆盖与逐条判、开发中选择性重跑与最终完整重跑；本插件合并为 R1–R7、S1 共 8 个用例。 第 25 节补定语义内容与机械文件的分工、新插件旧表现的公开历史依据，以及 R2 未批准起点、R3 三快照场景、R5 和 S1 固定输入与尺子。 第 26 节明确分组按检查条计，每条只属一类：新能力 12、真实问题 3、受影响旧能力 1、冒烟 2；冻结说明写明完整回归后代码变化须再完整重跑。 第 27 节写定 S1 的固定正文及 R6 场景条件；R6 只检验该保守恢复路线，其他路线由 state、writer 既有恢复验收器覆盖。 第 28 节将冻结说明漏写范围限定为七类固定清单，清单之外以设计为准，D6 按清单项、矛盾、数量与回归和大件下载检查。",
    "after": "第 17 节用户决定：网页端打包纳入 0.1，复用已测通方法并由 X4 真实验收、X1 签发；本插件自身的 X1 为 GPT Work 极高，Claude 仅做机械启动 Codex 的运输。第 15 节通用负责人规则继续有效。 第 20 节的旧批准载体已由第 30 节取代：用户在 Blueprint 的 freeze-review 视图中审阅并批准 snapshot_sha256。 第 21 节补定普通恢复冲突的处置、原始记录保留、重派写入披露、用户决定边界及未决范围隔离。 第 22 节的旧批准身份已由第 30 节取代；实际下载大小和用户授权依据仍保留。 第 23 节明确执行端按档次表运行、GPT Work 极高不得用 Codex 代替、X4 记录选择与手动执行角色每轮一条。 第 24 节补定回归用例集、按条覆盖与逐条判、开发中选择性重跑与最终完整重跑；本插件合并为 R1–R8、S1 共 9 个用例（第 30 节补入 R8）。 第 25 节补定语义内容与机械文件的分工、新插件旧表现的公开历史依据，以及 R2 未批准起点、R3 三快照场景、R5 和 S1 固定输入与尺子。 第 26 节明确分组按检查条计，每条只属一类：新能力 14（含第 30 节新增 R8 两条）、真实问题 3、受影响旧能力 1、冒烟 2；完整回归后代码变化须再完整重跑。 第 27 节写定 S1 的固定正文及 R6 场景条件；R6 只检验该保守恢复路线，其他路线由 state、writer 既有恢复验收器覆盖。 第 28 节的旧审查载体与四项检查已由第 30 节取代：七部分内容直接写入 freeze-review，D6 核对节点答案与矛盾；数量和分类由界面派生，下载未知大小如实标注。"
  },
  {
    "pointer": "/evidence/10/sources/0/revision",
    "before": "15613f70f3f0c86774da63caf80bd66cbb702f4d",
    "after": "6c21bff4e83c26058d68f3f4680efe099cb1daba"
  },
  {
    "pointer": "/evidence/10/sources/0/locator",
    "before": "第 1–3、5–28 节；冻结说明漏写范围及 D6 四项检查以第 28 节为准。",
    "after": "第 1–3、5–30 节；0.2 冻结审阅、批准身份和回归修订以第 30 节为准。"
  }
]
```

## 当前三个目标节点的相关正文

只摘录与修改直接相关的完整段落，未列出的旧文字不属本轮重新审查范围。

```json
[
  {
    "id": "role-D1",
    "description": "唯一负责人；规定验收语义；将冻结审阅内容写入 Blueprint 的 freeze-review 节点组；审定改变完成标准的修订",
    "terminal.mechanism_relevant_paragraphs": [
      "- **任务与线程：** 规划端·专业，长期同一线程。主持澄清，派出D2/D3/D4，汇总完整设计，规定验收语义，处理关卡缺口，取得用户批准并冻结；只统筹和写设计，不写产品或验收代码。\n- **可读：** 用户原要求、当前状态、已授权现实资料、独立设计交回的全部原稿、D5–D8原始结果、设计退回原始证据。\n- **不可读/不可做：** 独立设计尚在进行时不把A稿传给B或反之；不代独立角色作判断、不代用户批准、不按交付方愿望直接改松标准。\n- **写入：** 设计阶段的状态、汇总Blueprint、需求出处、设计修订、冻结记录；交付后仍写设计版本、设计关卡派发、修订决定、用户批准引用和冻结记录，状态登记交X1。\n- **完成：** 设计已收敛，四关卡均对正确版本有效，用户明确批准，冻结包可被新X1读到；否则准确停留在当前设计步骤。\n- **回复：** 中文说明当前设计、改变与影响、需要用户决定的具体问题；若可继续，附下一角色的完整提示词。",
      "用户在 Blueprint 中审阅并批准冻结，不再另写冻结说明。批准对象只有 `snapshot_sha256`；`freeze.json` 不再包含 `explanation_sha256`。0.1 的 `FREEZE_EXPLANATION.md/.pdf` 与 `versions/0.1/` 只作历史保留，不作为新草稿的批准对象。",
      "D6 像审其他组件一样审 `freeze-review`：答案是否在 Blueprint 中、是否与其他节点矛盾；取消原来对单独冻结说明的四项检查。正文写给用户看，不以文件名、路径、哈希开头或堆砌；具体规则和来源通过节点 id 定位。",
      "D6 像审其他组件一样审 freeze-review 节点组：答案是否在 Blueprint 中、是否与其他节点矛盾；发现缺口交回 D1，不以自己的常识补出答案后判通过。",
      "批准请求写明当前 Blueprint 的 snapshot_sha256 及打开“冻结审阅”视图的方式；用户只批准该快照，freeze.json 不再包含 explanation_sha256。"
    ]
  },
  {
    "id": "role-D6",
    "description": "扮演用户逐组件追问，答案不在 Blueprint 里即缺口；核对 freeze-review 节点内容与设计一致",
    "terminal.mechanism_relevant_paragraphs": [
      "- **任务与线程：** 规划端·普通，每轮新开；以用户视角沿所有有效组件追问正常使用、失败、边界和旧能力。\n- **可读：** 用户需求原文和来源、受审Blueprint、共同角色卡和其中的 freeze-review 节点组；答案必须在Blueprint中找到明确位置。\n- **不可读/不可做：** 负责人聊天、设计过程和为其辩解的摘要；不能以自己的常识补出答案后判通过。\n- **写入：** 每个组件的疑问、Blueprint答案位置、仍缺什么、对用户结果的影响及应由谁补。\n- **完成：** 全部有效组件有检查记录；所有影响任务结果、开工或验收的问题都能由Blueprint回答。非阻塞建议单列，不随意增新需求。\n- **回复：** 用户会在哪一步卡住或误解、缺口的位置与关闭条件；回D1。",
      "D6 像审其他组件一样审 freeze-review 节点组：答案是否在 Blueprint 中、是否与其他节点矛盾；发现缺口交回 D1，不以自己的常识补出答案后判通过。"
    ]
  },
  {
    "id": "gates",
    "description": "把检查、用户追问、冷读和复述绑定同一受审对象。",
    "terminal.mechanism_relevant_paragraphs": [
      "| 关卡 | 直接检查对象 | 通过标准 | 未通过交回哪里 |\n|---|---|---|---|\n| D5 | 准确版本的JSON、端口/连接、需求路线、证据来源、历史与所需相邻文件 | 原检查器适用范围真实运行完成；没有结构和跨引用错误；所有叶子是三种合法终点；四环境走查与四问失败路径有真实内容；来源可核对。机器检查不能代替专业与可读性结论 | 设计缺项回D1；检查器/环境问题也回D1说明具体取得办法，结果记无法判断 |\n| D6 | 原需求与Blueprint里的所有有效组件 | 逐组件问题都有Blueprint内答案定位；没有漏掉用户正常入口、关键失败、旧能力或必须决定的事项 | D1汇总补缺，按修订范围重判 |\n| D7 | Blueprint全文及最小运输封套 | 新执行者无需设计者再决定产品、科研、接口、验收或权限就能开始已定工作；开工阻塞问题为零，允许合同内普通实现自由度 | D1补全设计，不能让冷读者临场设计答案 |\n| D8 | 正常与失败走查中每一步、每条失败路径整体说明的当前文字 | 每轮新对话合批：本轮全部单位交一个新的 GPT 对话，随机逐个且只按自身文字复述，保留 single-thread-batch 标记和文本身份；D1 逐单位判断，全部正确即本轮有效通过 | D1 改写读错单位，下一轮只给改过单位及受影响相邻单位，在新 GPT 对话里重读，仍只转交一条 |",
      "D5–D8可以并行读取同一稳定受审版本。D1收集到修改意见后生成新版本，按实际影响标明哪些旧结果已失效，不能把不同版本各过一项拼成冻结。对首次冻结或大改，四关卡必须共同覆盖待批准的设计；小修按流程仅重跑D5，批准及读者记录按第5.1节“批准继承”沿用。",
      "**本次 0.2 关卡与收口：** 按修订规则属于大改，在新快照上重跑：D5（机械，全量）、D7（Codex，全量）。D6 覆盖自上次通过以来自身字段有变化的全部节点，按节点自身字段计算，子节点变化不重复归到父节点；本轮为全部 62 个节点。D8 覆盖文字有变化的读者单位，并按既有规则纳入受影响的同一步骤或同一失败路径单位；文字和哈希均未变的单位沿用最近一次真实通过记录。范围以实际差异确定，不限于 freeze-review 组、D1 澄清节点和冻结节点。D6/D8 定向复核只查改动位置及其直接引用；改动之外的新发现记为 non-blocking 留给 0.3，除非与改动直接矛盾。若只发现转述性偏差，D1 按 Blueprint 原文改正后机械核对，不再开无边界的新轮。",
      "**D5 前置扫描：** D5 在 D6/D8 之前先运行废弃语义扫描：python tools/scan_deprecated_semantics.py（从本设计目录运行）。清单依据 REVISION_0.2_PLAN 与 MERGE_DECISIONS 的已批准删除或改名；扫描全部当前节点文字，并检查走查与当前证据摘要，排除 versions 冻结历史。现行要求出现残留即报错并停止 D6/D8；明确的删除说明、准确的历史引用和稳定机器 ID 不算残留。修正仅限已批准的 0.2 文字替换，逐处记录后重跑至残留为零；该扫描属于 D5，不代替原检查器。",
      "**本轮整体完成条件（D1 裁决）：** 四道关卡“整体完成”是指：D5 机械检查通过（快照差异与待 D8 项除外，废弃语义扫描须零残留）；D6 无 blocking；D7 全部 9 个回归用例通过；D8 全部受审单位复述正确。任何一关有 blocking 即未完成。"
    ]
  }
]
```

## 直接引用上下文

```json
{
  "connections": [
    {
      "id": "c-role-D2-to-role-D1",
      "from": "role-D2",
      "to": "role-D1",
      "fromPort": "to-role-D1",
      "toPort": "from-role-D2",
      "label": "交回原稿",
      "relationship": "D1收到A完整原稿与真正未决问题。",
      "carries": [
        "blueprint",
        "specification",
        "questions",
        "source notes"
      ]
    },
    {
      "id": "c-role-D3-to-role-D1",
      "from": "role-D3",
      "to": "role-D1",
      "fromPort": "to-role-D1",
      "toPort": "from-role-D3",
      "label": "交回另稿",
      "relationship": "D1收到B完整原稿后自行比较；不回传A。",
      "carries": [
        "independent blueprint",
        "questions",
        "source notes"
      ]
    },
    {
      "id": "c-role-D4-to-role-D1",
      "from": "role-D4",
      "to": "role-D1",
      "fromPort": "to-role-D1",
      "toPort": "from-role-D4",
      "label": "现实事实",
      "relationship": "盘点和授权探针的真实证据进入设计。",
      "carries": [
        "observed facts",
        "uncertainty",
        "raw records"
      ]
    },
    {
      "id": "c-role-D1-to-contract",
      "from": "role-D1",
      "to": "contract",
      "fromPort": "to-contract",
      "toPort": "from-role-D1",
      "label": "形成合同",
      "relationship": "负责人把需求和独立设计收敛为带九项语义的Blueprint。",
      "carries": [
        "integrated blueprint",
        "tradeoffs",
        "nine obligations"
      ]
    },
    {
      "id": "c-contract-to-gates",
      "from": "contract",
      "to": "gates",
      "fromPort": "to-gates",
      "toPort": "from-contract",
      "label": "受审对象",
      "relationship": "九项语义与完整设计固定身份再进入四关卡。",
      "carries": [
        "subject_ref",
        "blueprint",
        "nine item node refs"
      ]
    },
    {
      "id": "c-gates-to-role-D5",
      "from": "gates",
      "to": "role-D5",
      "fromPort": "to-role-D5",
      "toPort": "from-gates",
      "label": "结构核查",
      "relationship": "明确指定文件与已批准接入方式。",
      "carries": [
        "subject_ref",
        "checker version",
        "source context"
      ]
    },
    {
      "id": "c-gates-to-role-D6",
      "from": "gates",
      "to": "role-D6",
      "fromPort": "to-role-D6",
      "toPort": "from-gates",
      "label": "用户追问",
      "relationship": "新读者逐组件追问只在设计中找答案。",
      "carries": [
        "blueprint",
        "question scope"
      ]
    },
    {
      "id": "c-gates-to-role-D7",
      "from": "gates",
      "to": "role-D7",
      "fromPort": "to-role-D7",
      "toPort": "from-gates",
      "label": "只读冷读",
      "relationship": "新执行者只收到Blueprint及无答案运输封套。",
      "carries": [
        "blueprint",
        "transport identity"
      ]
    },
    {
      "id": "c-gates-to-role-D8",
      "from": "gates",
      "to": "role-D8",
      "fromPort": "to-role-D8",
      "toPort": "from-gates",
      "label": "逐步读者",
      "relationship": "D8 每轮一条提示词交一个新 GPT 对话合批处理本轮全部单位；D1 逐项判断，错误改写后下轮新对话只重读改动与受影响相邻单位。",
      "carries": [
        "本轮全部复述单位及各自当前文字",
        "一个新 GPT 对话，随机逐单位仅凭自身文字作答",
        "reader_isolation: single-thread-batch",
        "D1 逐项判断；错读改写后下轮新对话只重读改动与受影响相邻单位"
      ]
    },
    {
      "id": "c-role-D5-to-gates",
      "from": "role-D5",
      "to": "gates",
      "fromPort": "to-gates",
      "toPort": "from-role-D5",
      "label": "检查交回",
      "relationship": "原始检查结果回D1纳入有效范围。",
      "carries": [
        "gate result",
        "subject identity",
        "raw output"
      ],
      "feedback": true
    },
    {
      "id": "c-role-D6-to-gates",
      "from": "role-D6",
      "to": "gates",
      "fromPort": "to-gates",
      "toPort": "from-role-D6",
      "label": "追问交回",
      "relationship": "真实缺口与答案位置进入收敛。",
      "carries": [
        "questions",
        "answer locations",
        "gaps"
      ],
      "feedback": true
    },
    {
      "id": "c-role-D7-to-gates",
      "from": "role-D7",
      "to": "gates",
      "fromPort": "to-gates",
      "toPort": "from-role-D7",
      "label": "冷读交回",
      "relationship": "开工阻塞或具体可行顺序交D1。",
      "carries": [
        "blocking questions",
        "execution outline"
      ],
      "feedback": true
    },
    {
      "id": "c-role-D8-to-gates",
      "from": "role-D8",
      "to": "gates",
      "fromPort": "to-gates",
      "toPort": "from-role-D8",
      "label": "复述交回",
      "relationship": "保留真实文字和复述，不制造通过记录。",
      "carries": [
        "reader identity",
        "text hash",
        "verbatim retelling",
        "judgment"
      ],
      "feedback": true
    },
    {
      "id": "c-gates-to-freeze",
      "from": "gates",
      "to": "freeze",
      "fromPort": "to-freeze",
      "toPort": "from-gates",
      "label": "关卡有效",
      "relationship": "D5 草稿档、D6、D7、D8 全部通过同一 snapshot_sha256 且无关键开放问题后，请用户批准该快照，再按五步顺序冻结。",
      "carries": [
        "gate refs",
        "validity",
        "coverage",
        "closed questions",
        "同一 snapshot_sha256 的四关卡通过与批准对象"
      ]
    },
    {
      "id": "c-revision-to-role-D1",
      "from": "revision",
      "to": "role-D1",
      "fromPort": "to-role-D1",
      "toPort": "from-revision",
      "label": "修订负责",
      "relationship": "原D1决定小修或大改并承担设计与告知。",
      "carries": [
        "change record",
        "nine-item comparison",
        "paused scopes"
      ],
      "feedback": true
    },
    {
      "id": "v7-01-role-D1-to-clarify",
      "from": "role-D1",
      "to": "clarify",
      "fromPort": "out-v7-01-role-D1-to-clarify",
      "toPort": "in-v7-01-role-D1-to-clarify",
      "kind": "normal",
      "label": "必跑",
      "relationship": "必跑",
      "carries": [
        "必跑"
      ]
    },
    {
      "id": "v7-03-role-D2-to-role-D1",
      "from": "role-D2",
      "to": "role-D1",
      "fromPort": "out-v7-03-role-D2-to-role-D1",
      "toPort": "in-v7-03-role-D2-to-role-D1",
      "kind": "normal",
      "label": "必跑",
      "relationship": "必跑",
      "carries": [
        "必跑"
      ]
    },
    {
      "id": "v7-05-role-D3-to-role-D1",
      "from": "role-D3",
      "to": "role-D1",
      "fromPort": "out-v7-05-role-D3-to-role-D1",
      "toPort": "in-v7-05-role-D3-to-role-D1",
      "kind": "optional",
      "label": "按条件",
      "relationship": "按条件",
      "carries": [
        "按条件"
      ]
    },
    {
      "id": "v7-07-role-D4-to-role-D1",
      "from": "role-D4",
      "to": "role-D1",
      "fromPort": "out-v7-07-role-D4-to-role-D1",
      "toPort": "in-v7-07-role-D4-to-role-D1",
      "kind": "optional",
      "label": "按条件",
      "relationship": "按条件",
      "carries": [
        "按条件"
      ]
    },
    {
      "id": "v7-08-role-D1-to-gates",
      "from": "role-D1",
      "to": "gates",
      "fromPort": "out-v7-08-role-D1-to-gates",
      "toPort": "in-v7-08-role-D1-to-gates",
      "kind": "normal",
      "label": "必跑",
      "relationship": "必跑",
      "carries": [
        "必跑"
      ]
    },
    {
      "id": "v7-09-gates-to-contract",
      "from": "gates",
      "to": "contract",
      "fromPort": "out-v7-09-gates-to-contract",
      "toPort": "in-v7-09-gates-to-contract",
      "kind": "normal",
      "label": "全部通过且用户批准",
      "relationship": "全部通过且用户批准",
      "carries": [
        "全部通过且用户批准"
      ]
    },
    {
      "id": "v7-10-gates-to-role-D1",
      "from": "gates",
      "to": "role-D1",
      "fromPort": "out-v7-10-gates-to-role-D1",
      "toPort": "in-v7-10-gates-to-role-D1",
      "kind": "back",
      "label": "否：补缺口",
      "relationship": "否：补缺口",
      "carries": [
        "否：补缺口"
      ],
      "feedback": true
    },
    {
      "id": "v7-11-role-D1-to-contract",
      "from": "role-D1",
      "to": "contract",
      "fromPort": "out-v7-11-role-D1-to-contract",
      "toPort": "in-v7-11-role-D1-to-contract",
      "kind": "revision",
      "label": "小修：沿用原批准，只重跑结构检查",
      "relationship": "小修：沿用原批准，只重跑结构检查",
      "carries": [
        "小修：沿用原批准，只重跑结构检查"
      ],
      "feedback": true
    },
    {
      "id": "v7-23-role-X1-to-role-D1",
      "from": "role-X1",
      "to": "role-D1",
      "fromPort": "out-v7-23-role-X1-to-role-D1",
      "toPort": "in-v7-23-role-X1-to-role-D1",
      "kind": "proposal",
      "label": "验收器提案；D1 决定是否采纳",
      "relationship": "验收器提案；D1 决定是否采纳",
      "carries": [
        "验收器提案；D1 决定是否采纳"
      ],
      "feedback": true
    },
    {
      "id": "v7-24-role-X1-to-role-D1",
      "from": "role-X1",
      "to": "role-D1",
      "fromPort": "out-v7-24-role-X1-to-role-D1",
      "toPort": "in-v7-24-role-X1-to-role-D1",
      "kind": "back",
      "label": "退回请求",
      "relationship": "退回请求",
      "carries": [
        "退回请求"
      ],
      "feedback": true
    }
  ],
  "referring_nodes": [
    {
      "id": "contract",
      "title": "九项冻结合同",
      "description": "能力与声明范围",
      "relevant_mechanism_paragraphs": []
    },
    {
      "id": "fr-decisions",
      "title": "决定与默认做法",
      "description": "决定与默认做法的审阅内容直接保存在 Blueprint 中，按正文引用的节点查阅原规则。",
      "relevant_mechanism_paragraphs": [
        "本次用户决定：D1 澄清采用前沿轮次与推荐式问法，保留三类分工；冻结审阅直接在 Blueprint 进行，只批准 snapshot_sha256，不再转述成单独冻结说明。来源节点：clarify、freeze、gates。"
      ]
    },
    {
      "id": "fr-downloads",
      "title": "下载与安装",
      "description": "下载与安装的审阅内容直接保存在 Blueprint 中，按正文引用的节点查阅原规则。",
      "relevant_mechanism_paragraphs": [
        "单项超过 100 MB 的下载或安装要记录名称、大约大小、用途和目标机器；未记录大小如实写“未记录”，不能凭常识说很小。第一次下载或安装任何依赖前先记录实际大小，超过 100 MB 先经用户授权再下载；同一范围已有有效授权时不重复问。单项大小由冻结审阅视图从 Blueprint 自动派生，并可跳回来源节点。来源节点：contract-authorization、freeze。"
      ]
    },
    {
      "id": "fr-roles",
      "title": "角色分工",
      "description": "角色分工的审阅内容直接保存在 Blueprint 中，按正文引用的节点查阅原规则。",
      "relevant_mechanism_paragraphs": [
        "各角色的档次与会话规则，直接引用 dispatch 节点 terminal.mechanism 中 SPEC 第 2.1 节原表；冻结审阅视图读取该原表，不另写或概括一张表。运行位置和手动转交规则直接引用同一节点第 2.1a 节。没有满足档次、独立性或工具能力的入口时，生成完整提示词等待，不自动降档。",
        "D1 负责澄清、汇总、四关卡和批准冻结；D2 每次独立设计必跑，D3 在复杂、高风险或用户要求时由 D1 启用并记理由，已启用不得为省事取消，两者互不看本轮对方产物；D4 在已有代码数据的具体未知项会改变判断时启用，只查具体未知；D5 检查结构引用来源，D6 逐组件追问答案与矛盾，D7 新执行者只读设计列开工阻塞，D8 合批复述由 D1 逐单位对照。D5–D8 均为必经关卡，本次修订覆盖与继承按 gates 中的本次收口决定。来源节点：role-D1、role-D2、role-D3、role-D4、role-D5、role-D6、role-D7、role-D8、gates。"
      ]
    },
    {
      "id": "revision",
      "title": "修订与告知",
      "description": "按语义和影响范围区别小修与大改，并记录真实告知。",
      "relevant_mechanism_paragraphs": []
    },
    {
      "id": "role-D2",
      "title": "D2：独立甲",
      "description": "交出一份完整 Blueprint",
      "relevant_mechanism_paragraphs": []
    },
    {
      "id": "role-D3",
      "title": "D3：独立乙",
      "description": "复杂或高风险时另出一份完整 Blueprint",
      "relevant_mechanism_paragraphs": []
    },
    {
      "id": "role-D4",
      "title": "D4：现实核查",
      "description": "已有代码或数据时盘点并跑小探针",
      "relevant_mechanism_paragraphs": []
    },
    {
      "id": "role-D5",
      "title": "D5：格式检查",
      "description": "跑 Blueprint 检查器",
      "relevant_mechanism_paragraphs": []
    },
    {
      "id": "role-D7",
      "title": "D7：冷读开工",
      "description": "只看 Blueprint，列出开工前还要问的问题",
      "relevant_mechanism_paragraphs": []
    },
    {
      "id": "role-D8",
      "title": "D8：逐步复述",
      "description": "每轮一个新读者合批复述全部步骤，复述不对就重写",
      "relevant_mechanism_paragraphs": [
        "- **任务与线程：** 规划端·普通：GPT 极高，只在 GPT 网页端运行。每轮合成一条提示词，交一个新 GPT 对话处理本轮全部单位；每轮换新对话，用户每轮只转交一次。\n- **可读与作答：** 每个单位的一句项目简介、当前单位短标题及动作、输入、输出、理由、失败后果；逐单位仅根据本单位文字作答，不借其他单位补全信息，不提供预期复述答案。\n- **写入：** 原样复述、实际看过的文字和身份、疑惑、读者与轮次，结果记录 reader_isolation: \"single-thread-batch\"。\n- **完成与返修：** D1 逐项比对原意与复述，全部正确即为本轮 D8 有效通过。读错则改写对应单位，下一轮只给改过单位及受影响相邻单位，仍合成一条提示词交新的 GPT 对话。\n- **冻结审阅：** fr-decisions、fr-roles 如实说明 D8 使用合批方式和用户接受的读者独立性取舍，不伪造逐单位独立读者记录。\n- **回复：** 逐单位原样交回复述与疑问，由 D1 判断；不自己宣称作者意图已被正确理解。"
      ]
    },
    {
      "id": "role-X1",
      "title": "X1：负责人",
      "description": "唯一负责人；只统筹不写代码；审查验收变化",
      "relevant_mechanism_paragraphs": []
    }
  ],
  "wr-gates": {
    "id": "wr-gates",
    "nodeId": "gates",
    "title": "完成四道冻结关卡",
    "action": "负责人在冻结前收集同一份当前设计上的结构检查、用户代理追问、冷读和读者复述结果；冻结审阅七部分也属于设计本身，同样接受用户代理追问。",
    "exampleData": "拿到含冻结审阅七部分的当前设计、对应的四道关卡结果及逐单位复述记录。验收与回归的数量、分类由界面从设计自动统计，角色档次表读取原表，下载大小未知的如实显示未记录。",
    "expectedResult": "四道关卡“整体完成”是指：D5 机械检查通过（快照差异与待 D8 项除外，废弃语义扫描须零残留）；D6 无 blocking；D7 全部 9 个回归用例通过；D8 全部受审单位复述正确。任何一关有 blocking 即未完成；设计负责人逐项比对原意与复述，全部正确时本轮合批就是 D8 有效通过，不另设单位例外。",
    "why": "四道关卡分别检查结构、用户缺口、能否直接开工和文字是否传达已定设计，不能用其中一道替代另一道；合批复述的独立性取舍由用户接受。",
    "onError": "任何一关有 blocking 即未完成，不能进入冻结。复述错误则改写相关单位，下一轮新对话只重读改动及同一步骤或同一失败路径中受影响的单位，旧文字的通过记录不能继续沿用；冻结审阅正文改动后按修订规则核对受影响关卡及批准对象。",
    "failurePathIds": [
      "fail-checker",
      "fail-freeze-explanation"
    ],
    "errorRefs": [
      {
        "nodeId": "gates",
        "index": 0
      },
      {
        "nodeId": "role-D6",
        "index": 1
      }
    ],
    "technical": {
      "nodeId": "gates",
      "action": "D5 草稿档、D6、D7、D8 绑定 snapshot_sha256；D6 像审其他组件一样审 freeze-review 中的答案与矛盾。按修订规则属于大改，在新快照上重跑：D5（机械，全量）、D7（Codex，全量）。D6 覆盖自上次通过以来自身字段有变化的全部节点，按节点自身字段计算，子节点变化不重复归到父节点；本轮为全部 62 个节点。D8 覆盖文字有变化的读者单位，并按既有规则纳入受影响的同一步骤或同一失败路径单位；文字和哈希均未变的单位沿用最近一次真实通过记录。范围以实际差异确定，不限于 freeze-review 组、D1 澄清节点和冻结节点。D6/D8 定向复核只查改动位置及其直接引用；改动之外的新发现记为 non-blocking 留给 0.3，除非与改动直接矛盾。若只发现转述性偏差，D1 按 Blueprint 原文改正后机械核对，不再开无边界的新轮。 D5 在 D6/D8 之前先运行废弃语义扫描：python tools/scan_deprecated_semantics.py（从本设计目录运行）。清单依据 REVISION_0.2_PLAN 与 MERGE_DECISIONS 的已批准删除或改名；扫描全部当前节点文字，并检查走查与当前证据摘要，排除 versions 冻结历史。现行要求出现残留即报错并停止 D6/D8；明确的删除说明、准确的历史引用和稳定机器 ID 不算残留。修正仅限已批准的 0.2 文字替换，逐处记录后重跑至残留为零；该扫描属于 D5，不代替原检查器。",
      "exampleData": "含 freeze-review 的同一 snapshot_sha256 及有效关卡结果；D8 保留 reader_isolation: single-thread-batch。",
      "expectedResult": "四道关卡“整体完成”是指：D5 机械检查通过（快照差异与待 D8 项除外，废弃语义扫描须零残留）；D6 无 blocking；D7 全部 9 个回归用例通过；D8 全部受审单位复述正确。任何一关有 blocking 即未完成。 D1 逐单位判断 D8；改写读错单位后，下轮新 GPT 对话只重读改过单位与受影响相邻单位。"
    }
  },
  "current_evidence_summary": {
    "id": "e-merge",
    "claim": "0.1 历史依据：D1 合并规格及用户最新角色运行要求。",
    "proves": "第 17 节用户决定：网页端打包纳入 0.1，复用已测通方法并由 X4 真实验收、X1 签发；本插件自身的 X1 为 GPT Work 极高，Claude 仅做机械启动 Codex 的运输。第 15 节通用负责人规则继续有效。 第 20 节的旧批准载体已由第 30 节取代：用户在 Blueprint 的 freeze-review 视图中审阅并批准 snapshot_sha256。 第 21 节补定普通恢复冲突的处置、原始记录保留、重派写入披露、用户决定边界及未决范围隔离。 第 22 节的旧批准身份已由第 30 节取代；实际下载大小和用户授权依据仍保留。 第 23 节明确执行端按档次表运行、GPT Work 极高不得用 Codex 代替、X4 记录选择与手动执行角色每轮一条。 第 24 节补定回归用例集、按条覆盖与逐条判、开发中选择性重跑与最终完整重跑；本插件合并为 R1–R8、S1 共 9 个用例（第 30 节补入 R8）。 第 25 节补定语义内容与机械文件的分工、新插件旧表现的公开历史依据，以及 R2 未批准起点、R3 三快照场景、R5 和 S1 固定输入与尺子。 第 26 节明确分组按检查条计，每条只属一类：新能力 14（含第 30 节新增 R8 两条）、真实问题 3、受影响旧能力 1、冒烟 2；完整回归后代码变化须再完整重跑。 第 27 节写定 S1 的固定正文及 R6 场景条件；R6 只检验该保守恢复路线，其他路线由 state、writer 既有恢复验收器覆盖。 第 28 节的旧审查载体与四项检查已由第 30 节取代：七部分内容直接写入 freeze-review，D6 核对节点答案与矛盾；数量和分类由界面派生，下载未知大小如实标注。",
    "doesNotProve": "裁决依据不是 D5–D8 通过、批准冻结、插件实现或正常入口验收的证据。 其中单独冻结说明的规则已由 0.2 修订计划和 MERGE_DECISIONS 第 30 节取代，回归用例以本轮工作树的第 10.2a 节为准。",
    "sources": [
      {
        "kind": "document",
        "repository": "https://github.com/YuukiAS/AI_Skills_Collection",
        "revision": "6c21bff4e83c26058d68f3f4680efe099cb1daba",
        "path": "docs/design/assurance/plugin-0.1-d1/MERGE_DECISIONS.md",
        "locator": "第 1–3、5–30 节；0.2 冻结审阅、批准身份和回归修订以第 30 节为准。"
      }
    ]
  }
}
```

## 新增扫描实现

文件：`docs/design/assurance/plugin-0.1-d1/tools/scan_deprecated_semantics.py`

```python
#!/usr/bin/env python3
"""D5: scan current Blueprint text; never scan or rewrite frozen versions."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import sys

DESIGN = Path(__file__).resolve().parents[1]

# Each concept is tied to an approved revision, rather than guessed from age.
RULES = [
    ("separate-freeze-explanation", r"冻结说明|FREEZE_EXPLANATION(?:\.md(?:/\.pdf)?|\.pdf)?",
     "REVISION_0.2_PLAN.md#修订二；MERGE_DECISIONS.md §30：改为 Blueprint freeze-review"),
    ("explanation-identity", r"explanation_sha256",
     "REVISION_0.2_PLAN.md#修订二 第2项；MERGE_DECISIONS.md §30：只批准 snapshot_sha256"),
    ("old-regression-count", r"(?:共\s*)?[8八]\s*个(?:回归)?用例|新能力\s*12|(?:共\s*)?18\s*条检查",
     "REVISION_0.2_PLAN.md#补充决定 第1项；MERGE_DECISIONS.md §30：9用例，14+3+1+2=20条"),
    ("old-gate-scope", r"D6、D8\s*只针对新增和改写的节点（[^）]+）",
     "MERGE_DECISIONS.md §30；D1 本轮裁决：D6 按自身字段差异，D8 按读者文字差异"),
    ("old-blueprint-identity", r"blueprint_sha256",
     "MERGE_DECISIONS.md §22、§30；SPEC.md §6.5：区分快照、语义及完整包身份"),
]

# Only these exact local phrases are migration/history statements. A negative
# elsewhere in the field must not hide a new positive use of a deleted concept.
PERMITTED = [
    r"不再另写冻结说明", r"取消原来对单独冻结说明的四项检查",
    r"不再另有冻结说明文件身份", r"不另生成冻结说明", r"不再转述成单独冻结说明",
    r"其中单独冻结说明的规则已由 0\.2 修订计划和 MERGE_DECISIONS 第 30 节取代",
    r"本仓库提交 `2965b008` 的第一版冻结说明",
    r"0\.1 的 `FREEZE_EXPLANATION\.md/\.pdf` 与 `versions/0\.1/` 只作历史保留",
    r"(?:不再包含|不含)\s*`?explanation_sha256`?",
    r"不再有\s*`explanation_sha256`",
    r"不再用旧 blueprint_sha256 或 explanation_sha256",
    r"`freeze\.json` 的必填字段 `blueprint_sha256` 以 `snapshot_sha256` 和 `bundle_sha256` 两项代替",
]


def strings(value, pointer=""):
    if isinstance(value, dict):
        for key, child in value.items():
            if pointer == "" and key == "versions":
                continue
            escaped = key.replace("~", "~0").replace("/", "~1")
            yield from strings(child, pointer + "/" + escaped)
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from strings(child, f"{pointer}/{index}")
    elif isinstance(value, str):
        yield pointer, value


def scan(bundle):
    findings, permitted, checked = [], [], 0
    node_count = sum(1 for pointer, _ in strings(bundle)
                     if re.fullmatch(r"/nodes/\d+(?:/children/\d+)*/id", pointer))
    for pointer, text in strings(bundle):
        checked += 1
        allowed = [m.span() for pattern in PERMITTED for m in re.finditer(pattern, text)]
        for rule, pattern, authority in RULES:
            for match in re.finditer(pattern, text):
                item = {"rule": rule, "pointer": pointer, "offset": match.start(),
                        "match": match.group(), "authority": authority,
                        "context": text[max(0, match.start()-45):match.end()+65]}
                if any(start <= match.start() and match.end() <= end for start, end in allowed):
                    permitted.append(item)
                else:
                    findings.append(item)
    return {"scope": "all current strings including all node fields, walkthroughs and evidence; excludes versions",
            "nodes_checked": node_count, "strings_checked": checked,
            "residual_count": len(findings), "permitted_migration_or_history_count": len(permitted),
            "findings": findings, "permitted": permitted}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("blueprint", nargs="?", type=Path, default=DESIGN / "blueprint.json")
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    raw = args.blueprint.read_bytes()
    report = scan(json.loads(raw))
    report["source_sha256"] = hashlib.sha256(raw).hexdigest()
    report["rules"] = [{"id": name, "pattern": pattern, "authority": authority}
                       for name, pattern, authority in RULES]
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({key: report[key] for key in
                      ["nodes_checked", "strings_checked", "residual_count",
                       "permitted_migration_or_history_count"]}, ensure_ascii=False))
    for finding in report["findings"]:
        print(f"{finding['pointer']} [{finding['rule']}] {finding['context']}")
    return 1 if report["residual_count"] else 0


if __name__ == "__main__":
    sys.exit(main())
```

扫描首跑 10 处残留，修正后 0；允许的删除说明和历史引用 39 处。扫描报告和逐处替换记录位于同分支 `gates/d5/round2/`。这是执行端机械证据，不代替你的定向判断。D5 原检查器本轮离线、在线均检查 62 节点，原始 exit 1，错误仅为 1 条快照差异及 5 条待 D8 记录，在线 unresolved=0；未伪造读者或冻结记录。

## 输出与直接写回

把真实结果直接写入同一任务分支：
- `docs/design/assurance/plugin-0.1-d1/versions/0.2-draft/gates/d6/round2/questions.json`
- `docs/design/assurance/plugin-0.1-d1/versions/0.2-draft/gates/d6/round2/RESULT.md`

questions.json 为数组，每项含 `id,nodeId,question,answerLocation,gap,impact,blocking,owner`，无缺口时 gap=null。RESULT.md 写三个 blocking 是否关闭、改动引入的问题、non-blocking（留 0.3）、实际覆盖与未覆盖、哈希核验范围；不把未做的全量审查或插件运行写为通过。

写入前只读目标结果文件（若存在）及其 SHA，保留其他结果。完成后从同一分支回读两份文件确认；不要改设计、冻结记录或其他关卡结果。GitHub 不可写时如实说明写入失败和原因；可写时不要要求用户手工搬运。

### 聊天中的最终回复必须是人话结论

不要把机器字段、JSON、状态枚举或大段文件内容当最终回复。先用自然中文直接告诉用户：

1. **D6 这一轮过没过。**
2. 如果通过：明确说“第 1 轮的 3 个阻塞都已关闭，本轮没有新的阻塞，可以继续下一步”。
3. 如果未通过：只说明还剩几个真正会阻塞冻结的问题，每个问题用一句自然中文说清“哪里还不对、为什么会影响冻结、谁需要修”。
4. 明确告诉用户下一步要做什么；如果用户无需操作，就直接说“你现在不用做任何事”。
5. 最后再附 GitHub 结果文件路径，作为证据定位。

禁止用类似“blocking=0 / non-blocking=2 / STATUS=PASS”作为主要用户回复。可以在自然中文结论后补数量，但不能让用户自己解释机器状态。不要把完整 `questions.json` 或 `RESULT.md` 粘到聊天里。
