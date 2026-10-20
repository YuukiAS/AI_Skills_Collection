# ChatGPT Web PASS 原子交付与提示词兼容性修复 — Proposal v0.4

日期：2026-10-20  
任务键：`chatgpt-web--pass-integrity`  
目标仓库：`YuukiAS/AI_Skills_Collection`  
设计分支：`design/chatgpt-web--pass-integrity-v0-4`  
设计基线：`main@272f5cd1b3599acb0c5b95ef57ce00a0cf1b0ac3`  
阶段：设计提案；需要独立 Critic；不得实施

## 1. 本轮为何重新打开同一任务

Planner/Critic 1.7、Capability Gate Policy 1.2 和 2026-10-19 Project setting 已经解决了“复杂设计被轻易放行”的一部分问题。Delivery Assurance 与 STAT5060 两轮真实回归证明，Critic 能够独立读取当前事实、拒绝历史 PASS、追完整成功链和危险失败链，并把缺口转成具体返修任务。

但 Clear Writing 0.6 第一次真实走到 execution-ready `PASS` 时，立即暴露了尚未覆盖的正向路径缺口：

1. 任务专用 Critic prompt 要求“只复核四个 blocker”，并规定通过后停在 `NEXT_HANDOFF=USER_AUTHORIZATION`；
2. 最新 Critic 1.7 明确要求最终审查重新检查完整用户承诺和执行包，并在同一回复直接给短 `COPY TO CODEX`；
3. Critic 没有识别该冲突，先给了缺少 Codex handoff 的 `PASS`；
4. 用户连续追问后，Critic先补说明、再全文倾倒 Kickoff，仍没有一次完成正确交付；
5. 用户进一步询问已经批准的 G3 怎样保证仓库文件经过 Clear Writing 时，Critic没有先解释冻结架构，反而临时提出 `create_blob`、MCP 和全局写入拦截，随后又撤回。

因此，先前 `CANDIDATE_ACCEPTED` 只保留为历史阶段记录，当前治理候选重新进入同一任务键下的设计修订。这里不创建 successor，不重做 Clear Writing 产品架构，也不把问题下沉给 Bridge Kit。

## 2. 冻结的用户承诺

后续版本不得静默弱化以下要求：

1. execution-ready `PASS` 必须一次交齐，而不是由用户连续追问补齐。
2. 同一条 `PASS` 回复必须同时包含：可读的实际架构说明、精确批准定位、`READY_FOR_CODEX=YES`、`NEXT_HANDOFF=CODEX` 和可直接发送的短 `COPY TO CODEX`。
3. 缺少上述任一部分时，Critic 不得先输出 `PASS`；事后补发不能把不完整结论追认成有效 PASS。
4. 任务专用 prompt 不得缩窄最终审查范围、改变中央 verdict 语义或改变 PASS 的交付格式。
5. 用户询问“已经批准的机制怎样工作”时，先依据批准包解释，不得自动把问题升级为新产品要求或更重架构。
6. 只有用户明确提出新要求，或现有批准包被证据证明存在真实矛盾时，才重新进入设计；不得因一个正常解释问题擅自新增 MCP、App、网关、数据库、状态机或 Gate。
7. 用户不负责判断中央合同和任务 prompt 哪个优先，也不负责追问“Codex prompt 在哪里”。
8. 本轮不修改当前 Project setting；它已经包含唯一 PASS、用户说明和机器交接的顶层要求。修复应落在 Planner/Critic 合同和任务提示词生成责任中。

## 3. 根因

### 3.1 中央合同有规则，但没有把冲突检查设成明确批准硬门

Critic 1.7 已写明：最终 execution-ready 审查不能被任务 prompt 缩成旧 blocker closure，并且必须输出短 Codex handoff。但它没有把“任务专用 prompt 与中央合同冲突”明确列为 execution-ready package 自身的阻塞条件。

结果是 Critic可以一边读取中央合同，一边继续照低层任务 prompt 的旧输出格式执行。

### 3.2 PASS 要求分散存在，没有被冻结成不可拆分的一次性交付

当前合同分别要求：一屏说明、完整审查、短 handoff、唯一 PASS。它们语义上正确，但没有明确写成：**只有同一回复全部出现，PASS 才成立。**

这使 Critic 可以先发 PASS，再把缺失部分当成普通格式问题补交。

### 3.3 只验证了高质量 REVISE，没有验证高质量 PASS

Delivery Assurance 与 STAT5060 都是成功的 `REVISE` 回归，证明 Critic 会阻塞坏设计。但没有一个真实回归验证：Critic 决定 `PASS` 时，是否会同时讲清架构并交出可执行入口。

Clear Writing 0.6 是首个正向 PASS 实例，因此暴露问题并不意外；错误在于此前过早宣布治理候选完整接受。

### 3.4 缺少 PASS 后解释请求的稳定处理规则

当前合同规定 PASS 后若冻结语义改变则旧批准失效，却没有明确区分：

- 用户只是在问批准架构怎样工作；
- 用户提供了证明原批准有矛盾的新证据；
- 用户明确提出了新的更强产品要求。

没有这一区分，Critic容易在“重复批准原设计”和“临场重做架构”之间摇摆。

## 4. 方案

### 4.1 Planner 1.8：最终 Critic prompt 必须通过中央兼容性检查

Planner 在形成 execution-ready package 时，必须检查任务专用 Critic prompt：

- 可以写当前对象、证据重点、上一轮 blocker 和包定位；
- 可以要求优先核对某些返修点；
- 不得把最终审查限制为“只看这些 blocker”；
- 不得重新定义 `PASS / REVISE`、`READY_FOR_CODEX`、下一接收方或用户输出格式；
- 不得要求 `NEXT_HANDOFF=USER_AUTHORIZATION`；
- 不得省略实际架构说明或短 `COPY TO CODEX`；
- 不得要求全文复制 Kickoff Draft。

最终提示词应明确：阶段、审查对象和任务事实由当前包提供；verdict、完整审查责任和输出合同由最新中央 Critic 合同提供。

如果 Planner 无法从 Kickoff Draft 和批准定位生成一段不猜测、不扩权的短 Codex handoff，执行包本身尚未闭合，不能送最终审查。

### 4.2 Critic 1.8：先做审查合同兼容性检查

execution-ready 审查开始时，Critic 先检查当前任务 prompt 和完整包是否与最新中央合同兼容。

发现以下任一情况时，当前包不得 PASS：

- 最终范围被缩成旧 blocker closure；
- verdict 或下一接收方与中央合同冲突；
- PASS 输出不要求实际架构说明；
- PASS 输出不要求短 `COPY TO CODEX`；
- 任务 prompt 要求用户在 PASS 后再索取执行入口；
- 任务 prompt 要求把批准前控制面全文复制给用户。

Critic可以继续完成其余审查，尽量在同一轮报告全部真实 blocker，避免只修提示词后下一轮才发现产品缺口；但只要兼容性冲突未修，就不能 PASS。

### 4.3 execution-ready PASS 是一次不可拆分的交付

同一条回复必须同时交付：

1. 一屏自然中文架构说明：用户怎样触发、关键组件怎样连接、正常成功链、最重要失败与恢复、当前仍未证明什么；
2. 精确批准对象和提交定位；
3. `READY_FOR_CODEX=YES`；
4. `NEXT_HANDOFF=CODEX`；
5. 可直接发送的短 `COPY TO CODEX`，只包含任务、批准定位、当前授权和停止条件。

缺少任一项时，Critic 只能 `REVISE`。若此前已经错误输出了不完整 PASS，应明确宣布该回复无效，并对同一个 exact package 做一次有界重新审查；不能靠后续零散补充追认。

这不是新增 schema、状态机或第三角色，只是把现有 PASS 责任合并成一个不可拆分的回复合同。

### 4.4 PASS 后的解释稳定性

用户在 PASS 后追问时，先判断问题属于哪一类：

1. **解释请求**：从批准包直接解释，不改变设计、不新增机制、不撤回 PASS。
2. **矛盾证据**：若新证据证明批准包确有核心矛盾，明确说明哪项冻结语义失效，同一任务键回 Planner。
3. **新要求**：明确说明这是超出原批准范围的新产品要求，只有用户确认要增加时才开启新设计。

模型不得仅因用户问“怎么保证”就自动把一个范围内保证扩成平台全局不可绕过保证。

### 4.5 Project setting 与 Capability Gate Policy 本轮不改

当前 Project setting 已经要求唯一 PASS、一屏说明和机器交接；Capability Gate Policy 1.2 已经要求正向能力、跨组件成功链和风险匹配失败链。

本次失败发生在任务 prompt 与中央 Critic 合同的兼容性、PASS 一次性交付以及 PASS 后解释行为。因此修改这些已有 owner 即可，不继续向 Project setting 堆重复文本，也不新增 Gate Policy 条款。

## 5. 实施范围候选

若本 Proposal 获 `PROCEED`，后续执行包只允许修改：

1. `docs/workflows/PLANNER_ROLE_CONTRACT.md`：升级至 1.8；加入最终 Critic prompt 兼容性责任和短 handoff 可生成性检查。
2. `docs/workflows/CRITIC_ROLE_CONTRACT.md`：升级至 1.8；加入提示词兼容性硬门、PASS 原子交付和 PASS 后解释稳定性。
3. `docs/workflows/CHATGPT_WEB_COLLABORATION_REGRESSIONS_2026-10-17.md`：记录 Clear Writing 0.6 正向 PASS 回归。
4. `docs/workflows/CHATGPT_WEB_CRITIC_GOOD_REVIEW_EXAMPLES_2026-10-20.md`：在已有两个优质 REVISE 例子之外，补充一个优质 PASS 的正面样例；只有真实回归通过后才写成成功示例。
5. `results/chatgpt-web--pass-integrity/**`：保存合同回放和最终真实回归证据。

不修改 Project setting、Capability Gate Policy、Clear Writing 产品代码、Clear Writing 0.6 架构、Bridge Kit 或 Plugin Creator。

## 6. 验收设计

### 6.1 确定性合同回放

至少覆盖：

1. **冲突 prompt**：使用 Clear Writing 0.6 v0.2 任务 prompt 中“只复核四个 blocker + `NEXT_HANDOFF=USER_AUTHORIZATION`”的真实片段，预期结果必须是 `REVISE`，不能 PASS。
2. **缺架构说明**：即使机器字段齐全，缺少一屏实际架构说明也不得 PASS。
3. **缺 Codex handoff**：即使审查结论正确，缺少 `NEXT_HANDOFF=CODEX + COPY TO CODEX` 也不得 PASS。
4. **全文 Kickoff 倾倒**：输出完整 Kickoff Draft 而非短 handoff，判定不符合 PASS 合同。
5. **任务 prompt 只强调 blocker 但不缩窄最终范围**：允许通过兼容性检查。

### 6.2 真实正向 PASS 回归

治理实现后，使用 Clear Writing 0.6 的同一 exact execution package 做一次全新 execution-ready Critic 回归：

- Critic 在一条回复内完整给出架构说明、批准定位和短 Codex handoff；
- 用户无需追问“Codex prompt 在哪里”；
- 用户随后问“写入 repo 的文件怎样保证经过 Clear Writing”时，Critic只解释批准包已有的 G3：全文读取 → 完整终审候选 → 写前确认 → 写入 → 回读 → 与候选一致 → 全文审查；
- 不新增 `create_blob`、MCP、App、全局写入网关或新 Gate；
- 若用户进一步明确要求“所有插件的任何 repo 写入都不可绕过 Clear Writing”，Critic应识别为新的更强要求，不静默改写原 0.6 声明。

这次正向回归通过后，`chatgpt-web--pass-integrity` 才能重新记为 `CANDIDATE_ACCEPTED`。

## 7. 反证与简化检查

不采用以下更重方案：

- 不新增 PASS 状态机或 schema；
- 不建立统一 prompt compiler；
- 不新建第三审查角色；
- 不把所有 task prompt 集中到新服务；
- 不要求 Critic 在每次解释问题时重新全量审查执行包；
- 不修改 Clear Writing 产品架构来补治理缺陷。

最小充分修复是：中央合同明确优先级，Planner在交付前检查兼容性，Critic在批准前再次检查，PASS 回复一次性交齐，后续问题按解释/矛盾/新要求分类。

## 8. 外部现实核查

OpenAI 2026 年关于指令层级的公开研究强调：来自不同来源的指令可能冲突，可靠行为依赖于明确优先级，并且低优先级指令不能覆盖高优先级约束。这支持本方案把中央角色合同置于任务专用 prompt 之上，并显式验证冲突，而不是继续依赖模型自行“应该知道”优先级。

本方案只采用这一轻量原则，不引入新的运行系统。

## 9. Critic 本轮必须判断

本轮只是设计审查，结论只能是 `PROCEED / REVISE`，不得 PASS。

Critic 必须独立判断：

1. 根因是否正确归属于中央治理的正向 PASS 路径，而非 Clear Writing 产品架构；
2. 任务 prompt 兼容性硬门是否必要、充分且不会制造无边界全仓审查；
3. PASS 一次性交付是否应成为有效 PASS 的成立条件；
4. 缺一项即 REVISE 是否过严，是否存在更简单但同样可靠的处理；
5. PASS 后解释/矛盾/新要求三分法是否能阻止无依据架构摇摆，同时保留发现真实矛盾后的重开能力；
6. 用 Clear Writing 0.6 做一次真实正向 PASS 回归是否足以补上此前只有 REVISE 回归的缺口；
7. 本轮不修改 Project setting 和 Capability Gate Policy 是否正确；
8. 是否仍保持轻量，没有新角色、状态机、数据库、服务或产品层修改。

## 10. 当前状态与下一步

当前只提交 Proposal v0.4，不修改正式合同，不修改当前 Project setting，不实施 Clear Writing，不重新审查 Clear Writing 0.6 产品包。

原治理任务继续使用同一 `task_key=chatgpt-web--pass-integrity`。历史 `CANDIDATE_ACCEPTED` 记录保留，但当前有效状态为设计修订中。

维护看板需要绑定或更新 tracking Issue；当前 Planner surface不能真实调用 Clear Writing 后再安全修改 reader-facing Issue/Project，因此只记录 pending mutation，不要求用户手工维护，也不声称 Project 已同步。

下一入口：独立 Critic 审查本 Proposal v0.4，只能给 `PROCEED / REVISE`。
