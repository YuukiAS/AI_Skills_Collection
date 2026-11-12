# D6 用户代理追问第 2 轮

## 结论

本轮按固定受审提交 `5de9e08a3f7a894c43457d6db67d21488e43bf63` 从头检查整份 Blueprint，共覆盖 54 个节点，记录 378 个用户视角问题。发现 3 个真实缺口，其中 **2 个阻塞、1 个不阻塞**。阻塞点都不是某个叶子实现细节，而是会直接影响“用户从哪里开始”和“D8 能否作为冻结依据”的流程语义。

### 阻塞缺口 1：规划端正式入口、角色宿主与执行派发没有闭合

用户从 Claude Code 或 GPT Work 的规划 `SKILL.md` 进入时，当前 Blueprint 无法给出与已认可流程一致的答案：一方面它准备了可供这些宿主读取的同源规划资源，另一方面 `dispatch`、`role-D1`、`role-X1`、`planning-entry` 等又把所有规划角色固定为 GPT 网页端，并把正常能力验收也写成 GPT 网页端规划。与此同时，`prompts` 要求 D1/X1 直接派发 Codex/GPT Work 执行端，却明确说明调度不自动跨宿主发消息。

答案位置：
- `nodes[id=planning-entry].terminal.mechanism §9.2`
- `nodes[id=dispatch].terminal.mechanism §2.1/§2.1a`
- `nodes[id=prompts].terminal.mechanism §4.2`
- `nodes[id=role-D1].terminal.mechanism`
- `nodes[id=role-X1].terminal.mechanism`
- `nodes[id=capability-check].terminal.mechanism §10.2`
- `requirements[id=r-dispatch]`
- `requirements[id=r-package]`

这会让用户在实际开工时卡住：按已认可流程，规划端·专业允许 Claude 或 GPT Pro，规划 `SKILL.md` 要能由 Claude Code 与 GPT Work 直接读取，而且本插件自身的实施流程明确由 Claude 担任 D1/X1；按当前 Blueprint，这些入口却不合法。若改走 GPT 网页端，又没有闭合负责人到执行端的直接派发能力。

**关闭条件：** D1 必须让 Blueprint 中的角色宿主、规划入口、执行派发和正常入口验收与已认可流程一致，并明确每个正式宿主如何进入 D1/X1、怎样把结果交给执行端。若要正式取消 Claude/GPT Work 的规划路径，则这不是技术补写，而是需要用户明确改变原要求。

### 阻塞缺口 2：D8 被无条件降成单线程合批，冻结证据比已认可流程弱

当前 Blueprint 把 D8 固定为“每轮一个新的 GPT 对话合批全部单位，全部复述正确即有效通过”，并明确用这一规则取代逐单位独立读者。已认可流程的条件更严格：负责人能自动派发时，每个单位应各起全新线程且只见本单位；只有必须由用户手工转交时才允许整轮单线程合批，并由 D1 考虑独立性降低，必要时在后续自动条件具备后对关键单位补独立复述；自动派发时 D8 还允许改用执行端最高推理档。

答案位置：
- `nodes[id=gates].inputs`
- `nodes[id=gates].outputs[id=to-role-D8]`
- `nodes[id=gates].terminal.mechanism §6.2`
- `nodes[id=role-D8].inputs`
- `nodes[id=role-D8].outputs`
- `nodes[id=role-D8].terminal.mechanism`
- `nodes[id=dispatch].terminal.mechanism §2.1a`
- `nodes[id=contract-fidelity].terminal.mechanism`

这会直接影响冻结：当前规则允许在本来具备更强隔离条件时仍使用较弱的单线程合批，并把它直接记为 D8 通过，随后进入用户批准和冻结。

**关闭条件：** D1 必须恢复“按实际派发能力分支”的 D8 规则：能自动派发时使用逐单位独立新线程；只有确需人工转交时才使用 `single-thread-batch`，并把隔离降低及其处理写入 D1 的判断和冻结记录。D8 的通过条件必须与这一路径一致。

## 不阻塞但应修正的退化点

`dispatch` 与 `prompts` 目前把所有规划角色都改成“用户每角色每轮手工转交一条提示词”。已认可流程只是限制**需要用户手工转交**时每角色每轮最多一条；负责人已有自动派发能力时，应直接使用该能力。当前写法仍可由用户人工完成，所以不阻塞，但会增加不必要的搬运工作，并使具备自动派发能力的宿主退化为人工流程。

位置：`nodes[id=dispatch].terminal.mechanism §2.1a/§2.4`、`nodes[id=prompts].terminal.mechanism §4.2`、`requirements[id=r-dispatch]`。

关闭条件是让“手工一条提示词”成为缺少自动派发能力时的用户路径，而不是所有规划角色的无条件正常路径。

## 覆盖范围

本轮没有只检查可能修改过的地方，而是重新覆盖全部有效节点，并对每个节点检查进入方式与输入、输出与接收者、决定权、失败或缺证处理、验收条件、中断恢复、已有能力保护七类问题。

覆盖节点：

`shared`, `state`, `writer`, `record-check`, `dispatch`, `prompts`, `revision`, `metrics`,
`design`, `design-roles`, `role-D1`, `role-D2`, `role-D3`, `role-D4`, `role-D5`, `role-D6`, `role-D7`, `role-D8`, `clarify`, `gates`, `contract`, `contract-capability`, `contract-entry`, `contract-outcomes`, `contract-fidelity`, `contract-forbidden`, `contract-regression`, `contract-controls`, `contract-changes`, `contract-authorization`, `freeze`, `q-checker`, `q-inheritance`,
`delivery`, `delivery-roles`, `role-X1`, `role-X2`, `role-X3`, `role-X4`, `role-X5`, `acceptance`, `calibration`, `candidate`, `evidence`, `deviation`, `sign`,
`packaging`, `source-layout`, `planning-entry`, `execution-package`, `minimum`, `capability-check`, `web-later`, `q-capacity`。

**省略节点：无。**

完整逐问题记录写入同目录的 `questions.json`。除上述 3 个缺口外，其余问题都能在 Blueprint 内找到明确位置；这只表示“现有设计已经回答了该用户问题”，不表示实现、安装或运行能力已经得到验证。
