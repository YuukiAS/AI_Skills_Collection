# D6 用户代理追问：第 1 轮结果

## 结论

本轮逐个检查了 Blueprint 的全部 54 个有效节点，并对每个节点至少追问了进入与输入、产出与接收者、决定权、失败或缺证据、验收、中断恢复、已有能力保护七类问题，共记录 378 个问题。发现 **2 条阻塞缺口**，没有为了增加数量而另列非阻塞缺口。

第一条发生在 `dispatch`：**冻结交接后，X2–X4 的直接派发权在 Blueprint 内部自相矛盾。** `dispatch.inputs`、`dispatch.outputs`、`dispatch.interface.boundaries` 及 `dispatch.terminal.mechanism` 的多处文字规定执行端 D4、D5、D7、X2–X4 由 D1 直接派发；但同一个 `dispatch.terminal.mechanism` 的 `X1-intake` 又规定新 X1 接收后“派 X2”，`role-X1.terminal.mechanism` 也把安排实现、校准、专项和独立判断列为 X1 职责。用户因此无法从设计中唯一判断交付阶段谁拥有 X2–X4 的派发权。影响是冻结交接后的第一步实施就可能出现双负责人、重复派发或越权，直接阻塞可靠开工。该缺口由 D1 负责关闭；关闭条件是交付阶段的派发责任在所有相关字段、角色卡、调度规则和走查中变成唯一且彼此一致，并与交付阶段的负责人和状态写权关系一致。

第二条发生在 `state`：**唯一权威 `STATE.json` 丢失或损坏时没有恢复规则。** `state.authority` 与 `state.terminal.mechanism` 把 `STATE.json` 定为唯一当前权威，并明确 `history/events.jsonl` 只能作为审计和恢复线索，不能覆盖当前状态；`record-check.terminal.mechanism` 只能只读检查记录，却没有定义已有 `STATE.json` 丢失、不可解析或无法确认修订号时，依据哪些记录恢复、谁确认恢复结果、怎样验证后重新取得可写基线。影响是负责人无法可靠确定 `phase`、`step`、`state_writer`、当前冻结对象和未决事项，而 `dispatch` 又要求有效 STATE，任务会停住且没有规定出口。该缺口由 D1 负责关闭；关闭条件是 Blueprint 明确这种故障的触发条件、可作为恢复依据的记录、恢复与核验责任人、冲突处理，以及恢复后重新建立唯一权威和继续派发所需的验证条件。

## 非阻塞建议

本轮没有发现需要单列的非阻塞缺口。对任务主动取消、额外灾备等流程原文没有要求的事项，没有自行扩展为新 gate 或新需求。

## 覆盖范围

已覆盖 54/54 个有效节点：`shared`、`state`、`writer`、`record-check`、`dispatch`、`prompts`、`revision`、`metrics`、`design`、`design-roles`、`role-D1`、`role-D2`、`role-D3`、`role-D4`、`role-D5`、`role-D6`、`role-D7`、`role-D8`、`clarify`、`gates`、`contract`、`contract-capability`、`contract-entry`、`contract-outcomes`、`contract-fidelity`、`contract-forbidden`、`contract-regression`、`contract-controls`、`contract-changes`、`contract-authorization`、`freeze`、`q-checker`、`q-inheritance`、`delivery`、`delivery-roles`、`role-X1`、`role-X2`、`role-X3`、`role-X4`、`role-X5`、`acceptance`、`calibration`、`candidate`、`evidence`、`deviation`、`sign`、`packaging`、`source-layout`、`planning-entry`、`execution-package`、`minimum`、`capability-check`、`web-later`、`q-capacity`。

每个节点都检查了七类用户问题；其中没有漏检节点。所有“有答案”的条目都在 `questions.json` 中记录了节点 id 与字段位置；两条阻塞缺口分别记录为 `q-dispatch-authority` 和 `q-state-recovery`。
