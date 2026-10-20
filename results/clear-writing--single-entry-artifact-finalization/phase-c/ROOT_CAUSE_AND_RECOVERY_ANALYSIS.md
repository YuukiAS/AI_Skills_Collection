# Clear Writing 0.6 Phase C 真实失败归因与同任务恢复结论

日期：2026-10-20  
任务：`clear-writing--single-entry-artifact-finalization`  
批准执行包：`d7b810d194ead881303aaca9c2e4f1d59a97c1f1`  
冻结候选：`079bd7987bb33d624d244feb415327d5cf2343d8`  
Phase C 安全停止证据：`38a81dc1df9a362ecee4be597cb3db5bd6fcac41`

## 一、核心结论

Phase C 停在正式 Personal Plugin 更新前是正确的；但本次失败不是“最后才遇到一个不可预见的平台故障”，而是 **execution-ready 现实核查没有真正闭合**。

在最终执行包获批前，有两个关键假设被当成了已解决事项：

1. Plugin Creator 导出的真实旧 release archive 能直接被批准的 `prepare-restore` 消费；
2. “长期 Planner 在 ChatGPT Web 执行 G1-G5”意味着该 Planner 本身能够自动创建并控制 fresh ChatGPT Web 对话、选择 `GPT-5.6 Sol` 并显式选择 Clear Writing。

这两个假设都没有在 execution-ready PASS 前用真实接口验证。

因此主根因不是规则缺失，而是 **已有 Planner/Critic 规则没有被落实到真实执行入口和真实恢复接口的预检**。

## 二、恢复包接口：最早何时能发现

### 已验证的真实接口

当前账户只读回读证明：

- live Clear Writing 仍为 `0.5.0`；
- USER / PRIVATE；
- 同一既有 plugin identity；
- live 27-file payload 与冻结 0.5 baseline 一致；
- 正向 26 条 `UPDATE_DELETE_PATHS.json` 与 live 非 manifest 文件集合完全一致。

Plugin Creator 的 `get_owned_plugin_archive` 当前真实返回：

```text
file_name = current.tar.gz
mime_type = application/gzip
version = 0.5.0
is_current = true
```

而冻结实现 `scripts/build_clear_writing_chatgpt_wrapper.py@079bd798...` 的 `prepare-restore` 路径对 baseline 和 candidate 都调用 `read_zip(...)`，内部只使用 `zipfile.ZipFile`。

Plugin Creator 的正式 `update_plugin` 接口明确接受 **ZIP 或 tar.gz**。因此“只支持 ZIP”不是平台要求，而是本任务 builder 的实现假设。

### 为什么这是可提前发现的问题

这个问题在三个更早阶段都可以被发现：

1. **Planner execution-ready 现实预检**：`get_owned_plugin_archive` 是无副作用只读动作，批准包已经把“保存真实 0.5 archive”设为恢复前置，却没有在 PASS 前实际调用它并绑定 `file_name/mime_type`。
2. **Critic execution-ready 审查**：当时 Critic 合同已经明确要求检查“失败后能否按现有接口恢复”，不能让团队在最后一步首次发现。Critic prompt 虽检查 overlay、`expected_release_id`、`delete_paths`、lower-version 和无直接 rollback，但没有把 archive 的真实传输格式和本地可消费性纳入独立 probe。
3. **Codex 实现**：Executor 为 baseline/candidate 共用了 `read_zip`，并把恢复测试建立在 synthetic ZIP baseline 上，没有兼容上游真实 archive 类型。

没有证据表明 Plugin Creator 的 archive 行为在批准后发生了变化；当前 0.5 release 本身早于本执行包。因此不应归为不可预见基础设施变化。

## 三、归档格式与“能否拿到实际字节”是两个独立问题

### A. 格式兼容缺陷

这是同一冻结任务内的普通实现 bug。

最小修复：原 Codex 任务把 archive reader 改为安全支持 Plugin Creator 的 ZIP / tar.gz 输入，并新增 traversal、symlink/hardlink、duplicate、unexpected-file-set 等 tar.gz 回归。不得改变 wrapper payload、六条 route、manifest、Gate 或产品语义。

该修复完成后，0.6 wrapper 的 exact raw ZIP 必须继续保持：

`e4c451841583cb6e1ae4212f8d8559b93ef4272f66d687d3f6762f6114a73dc6`

否则停止并回 Planner。

### B. 当前 Planner 是否能取得实际 archive bytes

这是单独的执行入口问题，不能被 tar.gz parser 修复掩盖。

当前 Plugin Creator action 返回的是短期 signed download URL + filename/mime metadata，而不是已经落到当前 Planner 工作目录的 file reference。当前 Planner surface 能取得 URL 和 release metadata，但本轮没有得到一个可直接传给本地 builder / `update_plugin` 的实际本地 archive path。

因此目前只能说：

- **archive format 已确认**；
- **archive byte materialization 在当前 Planner surface 尚未证明**。

后续不能用 repo/cache 的旧 0.5 文件冒充“真实账户 archive”。

## 四、真实 Web Gate 的执行入口归因

批准 Runbook 写的是：

> Phase C — ChatGPT Web distribution + G1-G5，由长期 Planner thread 在同一用户账号的 ChatGPT Web 使用 Plugin Creator / GitHub connector 执行。

这里混淆了两件事：

1. Planner 对话本身运行在 ChatGPT Web；
2. Planner 模型可以控制 ChatGPT 客户端 UI，自动创建新的 fresh conversation、切换模型、选择插件。

第 1 项成立不推出第 2 项成立。

当前 Planner surface 可以调用当前对话暴露的 Plugin Creator、GitHub、Skills 等工具，但没有一个动作能创建新的 ChatGPT conversation，并在那个新 conversation 中完成 UI 级 `GPT-5.6 Sol` + explicit Clear Writing selection。

这不是“ChatGPT Web 正常入口不存在”。正常入口对用户是真实存在的；用户可以新建聊天并选择模型/插件。失败的是 **执行职责分配**：Plan 把一个只能由 Web UI / 具有浏览器控制的执行入口完成的动作，错误分配给了不能操作客户端 UI 的长期 Planner 模型。

## 五、不需要“一个执行面同时拥有所有能力”

上一份 stop evidence 中“必须找到一个同时能 materialize archives 并自动跑 fresh Web gates 的执行面”结论过强，现予以修正。

只要以下 identity 和恢复合同保持不变，合法拆分执行入口不会降低 Gate：

1. archive / Personal Plugin mutation 入口绑定同一个 frozen candidate SHA、live plugin identity、pre-update release ID、restore archive；
2. Web Gate 每个 fresh conversation 都绑定更新后同一个 Personal Plugin release、`GPT-5.6 Sol` 和批准的 exact prompt；
3. G1-G5 evidence 回到同一个 task results root；
4. terminal failure 仍由拥有 Plugin Creator mutation/restore 能力的 owner 执行已冻结 restore；
5. 不用现有 Planner chat、本地 replay 或 helper 替代 fresh Web evidence。

因此产品 Gate 不需要降低，也不需要寻找“万能执行环境”。

但是，原批准 Runbook 把 Phase C owner 写成长期 Planner thread。把 Web UI 用户动作与 archive/mutation owner 分离，属于 **执行职责/交接语义修订**，必须由 Planner 做最小 amendment，再交原独立 Critic 复核后才可 live mutation。

## 六、Planner / Critic / Codex / Reviewer 责任归属

### Planner：主要责任

Planner 在批准执行包前已经受以下规则约束：

- 五遍预检必须核对现实环境、权限、资源和真实入口；
- 未知能力应先设计小 probe，不得把假设当功能；
- 风险与恢复必须写 owner、接口和何时需要用户；
- 非终态必须给唯一下一用户入口。

但执行包没有在 PASS 前真实导出 0.5 archive，也没有验证“长期 Planner thread”能创建 fresh Web chat。这是主要规划遗漏。

### Critic：独立审查遗漏

当时的 Critic Role Contract 已经明确写明：

- 必须查清谁执行；
- 失败后能否按现有接口恢复；
- 没有合法恢复路径要在执行前指出；
- 正常用户路径要问到唯一下一入口。

Critic 对 overlay/delete/version 做了较细审查，但没有独立核对 archive transport / byte materialization，也没有验证 Phase C owner 是否真的拥有 fresh-chat UI 操作能力。最终 execution-ready PASS 因而放过了两个本应阻塞的现实未知项。

这不是缺少新规则；不应继续往角色合同堆同义条款。

### Codex：一个明确的实现 bug

Codex 的 `prepare-restore` 只接受 ZIP，而真实上游 Plugin Creator archive 是 tar.gz。测试 `test_restore_tool_sets_keep_root_manifest_out_of_delete_paths` 直接构造内存 baseline dict，archive 安全测试也只覆盖 ZIP，因此没有覆盖真实 upstream archive transport。

这属于原冻结任务内普通实现缺陷，应回 **同一 Codex 任务** 修复，不需要新 task，也不需要先重开产品架构。

### 独立 implementation Reviewer：集成覆盖不足

最终实施审查已经明确写了“恢复集合仅做本地模拟，没有账户 mutation”。它正确限制了自己的 PASS 范围，但没有把“尚未用真实 Plugin Creator archive 验证 restore input”提升为 Phase C 前必须闭合的集成前置。

它不是本次架构错误的 owner，但属于实现验收层漏掉的现实接口风险。

### Phase C 执行入口

Phase C 正确执行了 fail-closed：在 live mutation 前发现问题并停止，因此没有造成账户损坏。

问题不在“它停了”，而在它成了第一个真正碰到这两项现实前置的阶段。

## 七、上一条 Planner 最终回复为什么也失败

上一条用户可见回复不是因为 Clear Writing 没有加载。

当前对话有直接调用证据：用户显式调用 Clear Writing 后，Planner 实际读取了 `skills://plugins/writing-style/response-clarity`。该 Skill 已明确要求：

- 先给人能直接理解的结论；
- 进度/阻塞汇报不要写成日志；
- 机器状态放到证据层；
- 普通英文流程词中文化；
- 问题回答完就停止。

同时 Planner Role Contract 1.7 已明确要求每轮先给一屏自然中文，并在非终态给 **唯一下一用户入口**。

上一条回复仍以大量 `PHASE_C_STATUS`、`G1=NOT_RUN`、路径和内部状态组织内容，并用“需要找一个同时具备两种能力的执行面”代替明确的 Planner/Critic/Codex/user handoff。

因此这里有两个独立失败：

1. **Planner handoff contract 没有被执行**：没有选择唯一下一接收方；
2. **Clear Writing 已读取但没有真正约束最终表达**：属于 host consumption failure，不是 Skill 规则缺失。

本轮不为此新增 Clear Writing 同义规则；应修当前 Planner 的执行与交接行为。

## 八、最小恢复决定

当前 0.5.0 Personal Plugin 未被修改，仍安全。没有 forward restore 需要执行。

同一任务按以下顺序恢复：

1. **唯一下一接收方：原 Codex task。**
   只修 `prepare-restore` 对真实 Plugin Creator tar.gz 的兼容和测试；不碰产品语义，不重跑 G1-G6，不更新 Personal Plugin。
2. Codex 修复后必须证明 wrapper candidate raw ZIP bytes仍为原 hash；若一致，可复用 13 组语言回放，不 reroll；重新跑直接受影响测试与 required CI，并交原 implementation Reviewer。
3. Planner随后用新的 implementation/source commit 重绑 final candidate identity。
4. Planner同时提交 Phase C execution-owner amendment：archive/mutation 与 fresh Web UI Gate 可由不同合法入口承担，不再要求长期 Planner自己创建 fresh conversation。
5. 因第 4 项改变执行职责/交接语义，**在 live mutation 前交原独立 Critic做最小复核**；不重新审已通过的单入口产品架构和 G1-G6质量标准。
6. Critic通过后才重新进入 Phase C；archive byte materialization 必须在 mutation 前真实 PASS。
7. 只有到了真正 fresh Web gate，若当前平台没有自动创建新聊天的能力，才向用户提出最小 UI 动作；其余 prompt、identity、证据路径和失败恢复由 Planner提前准备。

## 九、当前状态

```text
LIVE_PERSONAL_PLUGIN=0.5.0
LIVE_MUTATION_PERFORMED=NO
RESTORE_REQUIRED=NO
FROZEN_0_6_WRAPPER_SHA256=e4c451841583cb6e1ae4212f8d8559b93ef4272f66d687d3f6762f6114a73dc6
CURRENT_FAILURE_CLASS=EXECUTION_READINESS_AND_BOUNDED_IMPLEMENTATION_BUG
NEXT_HANDOFF=ORIGINAL_CODEX_TASK
```
