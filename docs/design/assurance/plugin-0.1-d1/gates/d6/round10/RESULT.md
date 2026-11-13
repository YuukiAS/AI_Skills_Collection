explanation_sha256: 3e5bc82387c2c894a34249ff888e4fe07ac5a15d76f8021db02cb9d02e721d20

# D6 第 10 轮结果

## 结论

本轮共发现 **2 条阻塞缺口**，两条都在用户批准前唯一阅读的冻结说明中；**Blueprint 本体的 54 个有效节点没有发现新的阻塞设计缺口**。

1. **冻结说明漏写 X3 的强制启用条件。** Blueprint 在 `shared/dispatch.terminal.mechanism` 的条件表，以及 `delivery/delivery-roles/role-X3.terminal.mechanism` 明确规定：科研数值或统计、安全相关验收，或验收器太弱需要换人重写时，X3 必须启用；X3 使用 GPT Work 极高，需要用户转交。冻结说明第 2 节只写了 X3 在哪里跑，没有写何时必须启用。用户会误判真实流程、人工转交次数和模型资源消耗，并可能把科研/统计/安全任务中的独立验收误解成可选项。由 D1 补入准确触发条件后，D6 必须对新说明重做冻结说明四项检查。

2. **冻结说明的回归用例描述弱于 Blueprint，且部分判定责任被改写。** 依据 `packaging/capability-check` 的 `inputs`、`interface.boundaries`、`validators[v-capability-check]`、`validators[v-regression-set]` 和 `terminal.acceptance`，R1–R7、S1 的固定输入、全部检查项、判定尺子和责任人已经写定。冻结说明却省略或概括了若干冻结条件：R1 未完整写出固定状态及正确下一步的四个要素，并把 Blueprint 只交 X5 判的 R1③概括成“X5 或你”；R2 漏掉路径禁入和验收器/回归统计一致性检查；R3 漏掉四个身份逐项一致及说明变动后重做 D6 检查；R4 漏掉阈值变化理由由 X5 判；R6 漏掉修订号续接、原派发置 stale、保留原记录和重派提示词列出既有写入；R7 漏掉 12/32 预算、包内资源可读及 X4/X1 的网页端责任；S1 把固定三条输入泛化。用户因此无法从唯一批准材料知道完整的最终完成门槛。由 D1 按 Blueprint 原义补全，不能改松、换输入或换责任人；说明一旦改动，原说明检查失效，D6 对新说明重做四项检查。

**非阻塞问题：没有。**

## Blueprint 全量复核

实际递归检查 **54 个有效节点**，包括全部子节点。每个节点都逐项核对了：入口与输入、输出与接收方、决定权、缺输入/缺证据/失败处理、验收与不能算完成的条件、中断或异常后的恢复，以及对既有能力的保护。每个节点的实际检查记录和精确答案位置都写入本轮 `questions.json`。

同时完整检查：
- `requirements`：14 条；
- `connections`：51 条；全部连接的起点、终点、输出端口和输入端口都能在对应节点找到，没有悬空端口；
- `walkthroughs`：4 条；
- `failurePaths`：13 条；13 条失败路径分别绑定 13 个唯一失败验收器，没有重复或缺失。

上述集合与节点规则交叉后，没有发现正常路径和失败路径对同一情况给出不同处理，也没有发现用户需求被 Blueprint 漏掉、缩小或延后到无明确接收方的情况。

## 冻结说明四项核对

### 1. 漏写

有两处实质漏写，均已计入阻塞缺口：

- 条件角色：漏写 X3 在科研数值/统计、安全相关验收、或弱验收器需换人重写时必须启用。
- 回归用例：冻结说明没有完整保留 R1–R7、S1 的固定输入、逐条检查、判定责任和部分恢复/身份条件，详见下方回归核对。

除此之外，冻结说明对主要取舍、宿主与人工转交、D8 合批取舍、市场 12/32、仓库文件状态、负责人恢复、小修与大改、状态恢复、项目自身 X1、整份签发、用户验收、签发后暂停/维持/撤回、权限费用、0.1 延后范围和网页端打包等内容，都能在 Blueprint 找到对应设计。

### 2. 多写或比 Blueprint 更强的承诺

除回归用例中 R1③ 把 Blueprint 的“X5 判”概括成“X5 或你”这一责任改写外，没有发现独立的额外承诺。

冻结说明附录里的 Blueprint 文件 SHA-256 `7bf8744cbcab1b72c53ba9eba574405f7766e422ee28cd60089f7eec0587bb66` 与本轮固定提交中的受审 `blueprint.json` 内容一致；附录的 `snapshot_sha256` `cf2c0967045c1a0eb8e7038006efd1da906ed2e573ca9eed18a7c5186b4d1ced` 也与 Blueprint 规定的内容快照计算结果一致。因此附录虽然写的是原设计分支/提交定位，但它描述的是与本轮固定提交相同的 Blueprint 内容快照，不构成对象错配。

### 3. 验收器

直接递归读取全部节点及子节点的 `validators`，得到 **68 个验收器**；全部 `required=true`，验收器 id 全部唯一。没有把 `terminal.acceptance` 当成验收器；后者共有 319 条检查条目，只是节点检查条款。

13 个失败验收器与 13 条 `failurePaths` 一一对应，因此其余 **55 个为正常能力验收器**。冻结说明的“55 个正常 + 13 个失败”与 Blueprint 一致。

按冻结说明的六类功能重新从 Blueprint 逐个归类，每个验收器恰好属于一类，无漏项、无重复：

- **任务状态与交接：8 个。** `v-shared`、`v-state`、`v-fail-recovery`、`v-writer`、`v-fail-write`、`v-record-check`、`v-revision`、`v-metrics`。
- **派发与提示词：3 个。** `v-dispatch`、`v-prompts`、`v-fail-role`。
- **13 个角色各自职责：15 个。** 两个角色组验收器 `v-design-roles`、`v-delivery-roles`，以及每个角色各一个基础职责验收器：`v-role-D1` 至 `v-role-D8`、`v-role-X1` 至 `v-role-X5`。D6 的额外失败验收器 `v-fail-freeze-explanation` 不归这一类，而归“从需求到冻结”。
- **从需求到冻结：18 个。** `v-design`、`v-fail-freeze-explanation`、`v-clarify`、`v-gates`、`v-fail-checker`、`v-contract`、九个合同子项验收器 `v-contract-capability`、`v-contract-entry`、`v-contract-outcomes`、`v-contract-fidelity`、`v-contract-forbidden`、`v-contract-regression`、`v-contract-controls`、`v-contract-changes`、`v-contract-authorization`，以及 `v-freeze`、`v-q-checker`、`v-q-inheritance`。
- **从冻结到签发：13 个。** `v-delivery`、`v-acceptance`、`v-fail-semantic`、`v-calibration`、`v-fail-calibration`、`v-candidate`、`v-evidence`、`v-fail-missing`、`v-deviation`、`v-fail-premise`、`v-sign`、`v-fail-candidate`、`v-fail-revocation`。
- **打包与安装：11 个。** `v-packaging`、`v-source-layout`、`v-planning-entry`、`v-execution-package`、`v-fail-package`、`v-minimum`、`v-capability-check`、`v-regression-set`、`v-web-later`、`v-fail-web-method`、`v-q-capacity`。

验收环境分类也与冻结说明一致：**真实环境 49 个、读源文件 17 个、生成包 1 个、安装结果 1 个**。

### 4. 回归用例

Blueprint 的完整回归用例集为 **8 个：R1–R7、S1；共 18 条检查**。分组与冻结说明的统计数字一致：**新能力 12 条、要修的真实问题 3 条、受影响的旧能力 1 条、冒烟 2 条**，每条只属于一类。

Blueprint 写定的实际内容、判定方式和责任人如下：

| 用例 | 固定输入 | 检查项与通过条件 | 判定责任 |
|---|---|---|---|
| R1 | 小型命令行工具增加导出功能；四道关卡只剩 D8；待复述 52 个单位；分别在 Claude Code、GPT Work 要负责人“继续” | ① 两边下一步完全一致：D8、GPT 极高、新对话、正确写回位置；② 只生成一条合批提示词且包含 52 个单位；③ 用户文字无未解释英文术语或内部字段名，产品名/命令/路径/文件名除外 | ①②脚本；③ X5 读全文，零处违规才过 |
| R2 | 四关卡都通过但尚未用户批准，请 D1 写冻结说明并发批准请求 | ① 按冻结说明骨架；正文无文件名、路径、哈希；验收器个数/分类、回归用例个数/分组与设计一致；② 批准请求含 `explanation_sha256`、`snapshot_sha256` 且与实际文件一致 | ①用户或 X5；②脚本 |
| R3 | 同一任务三个固定快照：A 四关卡齐且说明身份与 D6 检查一致；B 缺 D7；C 用户批准说明身份与 D6 检查身份不同 | ① A 生成冻结记录，`snapshot_sha256`、`explanation_sha256`、`bundle_sha256`、`semantic_hash` 均按设计一致；② B 拒绝并指出缺 D7；③ C 拒绝，指出说明身份不一致且须 D6 重做说明检查 | 全部脚本 |
| R4 | 一个交付状态同时含：阈值 0.95→0.90；证据属于候选 A 但待签 B；另一判据无原始证据 | ① 阈值修改视为改变完成定义，退回 D1；② 不签 B；③ 缺证据记“无法判断”且不签 | ①去向及②③脚本；①理由由 X5 判 |
| R5 | 派发实现“导出报告”，但未定 PDF 或 Markdown，同时要求无额外软件的同事可直接打开 | 执行端必须停下且不改代码；交回负责人；至少列 PDF、Markdown 两个选项及各自对“直接打开”的影响 | 脚本核对停下/未改代码；X5 判选项是否抓住真正选择 |
| R6 | 状态文件不可解析；git 上一个有效状态可作基线；其后有 D4 派发被记“已返回”但结果文件缺失；只留下不冲突的新笔记；无付费、发布、外部消息 | 新状态修订号续接基线；该派发置 stale；原记录保留；重派提示词列出原派发已留下的写入；因不涉及冻结/批准/签发/撤回且保守重派可行，不找用户 | 脚本 |
| R7 | 用现有生成器生成全部市场包并安装；上传网页端包，在新对话执行网页端三项操作 | ① 原 10 插件、30 技能仍在且 12/32 预算生效；② 只新增两个执行技能且包内资源可读；③ 网页端完成读取规则/角色卡/模板、生成正确下一提示词、按权限写回或如实给内容三件事 | ①②脚本；③ X4 观察，X1 亲读原始对话 |
| S1 | 安装环境中依次对 `writing-style`、`workflow-core`、`ai-skills-core` 发 Blueprint 写死的三条日常请求 | ① 三条都完成请求本身；② 没有任何请求进入 Assurance：不创建 `docs/assurance/` 文件，输出不出现 D1–D8、X1–X5、冻结、派发等 Assurance 用语 | ②脚本；①用户或 X5 |

整个用例的通过规则是：**某用例任一检查条不过，该用例就不过；8 个用例全部通过，0.1 才算完成。** X1 组织整个运行，亲读每个用例的原始输出并逐条记录。

重跑规则是：
- 开发过程中只重跑没过的用例，以及本次修改实际影响部分对应的用例；
- 最终候选确定后，必须在**同一个最终版本**上完整运行全部 8 个用例；
- 这次最终完整运行后，只要实现再次变化，就必须重新完整运行全部用例；
- 实施中新发现真实问题只允许追加新用例，不删改现有 R1–R7、S1。

因此，**回归用例的数量和四类统计与冻结说明一致，但内容、逐条判定和责任人并不完全一致**，构成上面的第 2 条阻塞缺口。

### 5. 单项超过 100 MB 的下载或安装

Blueprint 没有给任何相关对象提供大小证据，因此不能断言“确定没有超过 100 MB”。冻结说明在这一点上处理正确，明确写成“大小未记录”。

从 Blueprint 能确定正常实现/验收会涉及的对象包括：
- Python 3.10 或更新版本；
- `jsonschema[format-nongpl]==4.26.0` 及其格式依赖；
- Python 的 `rfc8785`；
- JavaScript 的 `canonicalize`，后二者具体版本实施时固定；
- 固定版本的 Blueprint 检查器；
- 两个 Codex 插件包、同源规划/共用资源及网页端既有打包方法；
- Claude Code、GPT Work、Codex、ChatGPT 网页端这些实际宿主，其当前安装状态在 Blueprint 中未记录。

冻结说明没有把未知大小写成“小于 100 MB”，也没有遗漏 Blueprint 中能识别出的必需下载/安装对象。Blueprint 的授权规则要求：第一次下载或安装任何依赖前先记录实际大小；单项超过 100 MB 必须先取得用户授权。

## 实际覆盖

- 有效节点：**54 / 54**。
- 子节点：已递归覆盖全部层级，没有只检查顶层。
- `requirements`：**14 / 14**。
- `connections`：**51 / 51**，并逐一核对起终节点和端口存在。
- `walkthroughs`：**4 / 4**。
- `failurePaths`：**13 / 13**，并核对每条对应验收器。
- 验收器：**68 / 68**，递归读取全部节点 `validators`；未把 319 条 `terminal.acceptance` 当验收器。
- 回归用例：**8 / 8**，共 18 条检查逐条核对。
- 冻结说明：完整读取固定提交中的 `FREEZE_EXPLANATION.md`；本轮实际检查的原始字节 SHA-256 为 **`3e5bc82387c2c894a34249ff888e4fe07ac5a15d76f8021db02cb9d02e721d20`**。
- 未覆盖对象：**没有**。

在 D1 修正两条冻结说明阻塞问题之前，当前冻结说明不能作为用户批准依据。Blueprint 本体无需因为本轮发现而补设计答案；修正说明后，按 Blueprint 自己的规则只需由 D6 对新说明重做冻结说明四项检查，Blueprint 未变时不必重做逐组件追问。
