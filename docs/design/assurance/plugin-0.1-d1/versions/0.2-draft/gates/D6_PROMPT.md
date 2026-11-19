# D6 用户代理追问：Assurance 0.2 草稿

请在全新的 GPT 网页端对话运行，使用 Thinking 最高推理。本提示词与 D8 必须使用不同的新对话。仓库：https://github.com/YuukiAS/AI_Skills_Collection；任务分支：`design/assurance-plugins-0.1-merged`。本轮草稿有未提交的机械修正，远端固定提交尚不含这些修正；不得直接审远端旧稿或分支的浮动 HEAD。

只读取公开仓库固定基线提交 `38f7aace61d4e352b6407e989962192f2949bba7` 的下列两份文件，再严格应用下文已批准的三处替换，得到本轮唯一受审草稿：
1. docs/design/assurance/ASSURANCE_PROCESS_V0_1_20261110.md（原需求）；
2. docs/design/assurance/plugin-0.1-d1/blueprint.json（唯一答案来源）。
不要读 SPEC、MERGE_DECISIONS、历史关卡或其他设计。不得自己补答案或提出新需求。

三处替换均已由 Claude 裁决并由用户明确授权，是与既有 R8 修订保持一致的机械修正；没有授权你修改其他字段。JSON Pointer 从 Blueprint 根开始：

- `/nodes/3/children/4/validators/1/criteria/0/value`：将 `8` 替换为 `9`。
- `/nodes/3/children/4/validators/1/method/command`：将 `按第 10.2a 节 D1 写定的输入、逐条检查、判定者和旧表现依据执行 R1–R8、S1；先由 X2 生成机械文件，X1 首次运行前核对并记录哈希后冻结；最终在同一个最终版本完整跑一遍。这是拟定操作说明，不是已运行记录。 分组按检查条统计：新能力 12、要修的真实问题 3、受影响的旧能力 1、冒烟 2；每条只属一类。` 替换为 `按第 10.2a 节 D1 写定的输入、逐条检查、判定者和旧表现依据执行 R1–R8、S1；先由 X2 生成机械文件，X1 首次运行前核对并记录哈希后冻结；最终在同一个最终版本完整跑一遍。这是拟定操作说明，不是已运行记录。 分组按检查条统计：新能力 14、要修的真实问题 3、受影响的旧能力 1、冒烟 2；每条只属一类。`。
- `/walkthroughs/1/steps/3/action`：将 `交付负责人使用同一最终包安排实际运行插件的工具（宿主，如 Claude Code、Codex 或 GPT 网页端）任务，按设计中的 8 个回归用例（R1–R8、S1）逐条检查。` 替换为 `交付负责人使用同一最终包安排实际运行插件的工具（宿主，如 Claude Code、Codex 或 GPT 网页端）任务，按设计中的 9 个回归用例（R1–R8、S1）逐条检查。`。

基线 Blueprint 原始字节 SHA-256：`6ade03081fffbfb59a13791c7e48f3c7eb84d7e62937087244e5d92036ced582`；本机完成三处替换后的完整文件原始字节 SHA-256：`c4a7d00cb74207179ec7e0b38a87d1590d6f83875a3f3fa4bea44003c9c340e5`；内容快照 `snapshot_sha256`：`b5391abe78519612324ab229cf5f338af465783b9f4d6ecb99b215dc9c9df484`。原始文件的其他字节保持原样，替换数字时只定位上述 Pointer。若你通过工具重新序列化 JSON，字节哈希可能改变，必须分别报告实际字节哈希和输入声明值，不得冒称已核验。用户也可附上本机 `codex-runs/assurance-02-gates/d6/blueprint.json` 的同一草稿副本；有附件时先核对三处值，勿再应用第二次。无法取得完整两份材料时报告 `NOT_RUN` 和缺失路径，不用常识补全。

完成检查后，必须使用已连接的 GitHub 直接把真实结果写入当前任务分支 `design/assurance-plugins-0.1-merged`：

- `docs/design/assurance/plugin-0.1-d1/versions/0.2-draft/gates/d6/round1/questions.json`
- `docs/design/assurance/plugin-0.1-d1/versions/0.2-draft/gates/d6/round1/RESULT.md`

如果目标文件不存在就直接创建；存在则先读取当前内容和 SHA，再按实际本轮结果更新。不得要求用户下载、复制、上传或手工转存结果。不得把本地 `codex-runs/` 当成最终证据位置。

GitHub 写入成功后，聊天里不要粘贴完整 `questions.json` 或 `RESULT.md`，只回复简短摘要：是否写入成功、blocking 数量、non-blocking 数量、两个 GitHub 路径。只有已连接 GitHub 确实不可写时，才报告 `WRITE_BLOCKED` 及真实失败原因；不要在写权限可用时退化为把完整机器结果交给用户搬运。

本轮只检查下列相对冻结基线 9e5943f33440587e0b220474caa89e41a5d0d697 新增或改写的节点。新增 8 个；既有 54 个均改变过自身字段（包括 category、roleTier、接口和短描述），因此本轮恰好覆盖当前 62 个节点。这是按差异得到的范围，不追加未变节点或旧冻结说明的四项审查。冻结审阅已在 Blueprint 中，检查其节点内答案及跨节点一致性；不要求恢复单独冻结说明。

节点清单：
`freeze-review`, `fr-decisions`, `fr-asks`, `fr-costs`, `fr-roles`, `fr-validation`, `fr-downloads`, `fr-nongoals`, `shared`, `state`, `writer`, `record-check`, `dispatch`, `prompts`, `revision`, `metrics`, `design`, `design-roles`, `role-D1`, `role-D2`, `role-D3`, `role-D4`, `role-D5`, `role-D6`, `role-D7`, `role-D8`, `clarify`, `gates`, `contract`, `contract-capability`, `contract-entry`, `contract-outcomes`, `contract-fidelity`, `contract-forbidden`, `contract-regression`, `contract-controls`, `contract-changes`, `contract-authorization`, `freeze`, `q-checker`, `q-inheritance`, `delivery`, `delivery-roles`, `role-X1`, `role-X2`, `role-X3`, `role-X4`, `role-X5`, `acceptance`, `calibration`, `candidate`, `evidence`, `deviation`, `sign`, `packaging`, `source-layout`, `planning-entry`, `execution-package`, `minimum`, `capability-check`, `web-later`, `q-capacity`

每节点至少逐项检查：怎么进入、需要什么输入；产出什么、交给谁；谁有权决定；失败或缺证据怎么办；怎样验收；中断后怎样恢复；会不会让既有能力变差。共 62×7=434 项。答案必须定位到 blueprint.json 的节点 id 与字段；找不到、含糊或互相矛盾时记缺口，并给影响及 owner=D1 或 user。仅将真实影响使用、开工或验收的缺口标为 blocking=true。不要为了凑数制造缺口；不要把未冻结/未实现自身当新问题。

写入 GitHub 的两份结果格式：
- `questions.json`：数组；每项 `id,nodeId,question,answerLocation`（无答案为 null）、`gap`（无缺口为 null）、`impact,blocking,owner`。
- `RESULT.md`：结论、阻塞问题与关闭条件、非阻塞问题、实际覆盖节点与未覆盖原因、受审文件原始 SHA-256。

写完后必须从同一分支重新读取这两个文件，确认内容真实存在且与本轮结果一致，再在聊天里只给摘要。

只发现转述偏差时定位原文，交 D1 按原文改正后机械核对，不发起无边界的新轮。改变责任、权限、费用、签发标准的问题交 D1 决定，不自行修改。
