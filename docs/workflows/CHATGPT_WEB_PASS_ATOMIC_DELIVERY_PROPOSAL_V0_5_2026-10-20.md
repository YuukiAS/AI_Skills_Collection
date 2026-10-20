# ChatGPT Web PASS 原子交付与正向回归修复 — Proposal v0.5

日期：2026-10-20  
任务键：`chatgpt-web--pass-integrity`  
目标仓库：`YuukiAS/AI_Skills_Collection`  
设计分支：`design/chatgpt-web--pass-integrity-v0-4`  
设计基线：`main@272f5cd1b3599acb0c5b95ef57ce00a0cf1b0ac3`  
上一版：`docs/workflows/CHATGPT_WEB_PASS_ATOMIC_DELIVERY_PROPOSAL_V0_4_2026-10-20.md@v0.4`  
上一轮 Critic：`results/chatgpt-web--pass-integrity/PASS_ATOMIC_DELIVERY_V0_4_CRITIC_REVIEW_2026-10-20.md`  
阶段：设计修订 + execution package；仍需独立 Critic；不得实施

## 1. 本轮只关闭什么

接受上一轮唯一 blocker：

`PASSINT-V04-01=ACCEPT`

v0.4 的根因判断和中央修复方向保持不变；只修正回归合同中的自相矛盾。

旧 Clear Writing 0.6 package：

`d7b810d194ead881303aaca9c2e4f1d59a97c1f1`

必须继续作为**兼容性负控**，因为其中 task-specific Critic prompt 明确：

- 将最终审查缩成四个旧 blocker；
- 通过后输出 `NEXT_HANDOFF=USER_AUTHORIZATION`；
- 没有要求中央合同规定的完整 execution-ready 审查和直接短 `COPY TO CODEX`。

因此它在 Planner/Critic 1.8 下的正确结果只能是 `REVISE`，不能再作为正向 PASS 测试对象。

## 2. 冻结的用户承诺

后续不得弱化：

1. execution-ready `PASS` 必须在同一条回复一次交齐，用户不再追问“架构是什么”“Codex prompt 在哪里”。
2. 同一条有效 PASS 必须同时包含：
   - 一屏实际架构说明；
   - 精确批准定位；
   - `READY_FOR_CODEX=YES`；
   - `NEXT_HANDOFF=CODEX`；
   - 可直接发送的短 `COPY TO CODEX`。
3. 任务专用 prompt 可以给对象、定位、风险重点和上一轮 finding，但不能缩窄最终 execution-ready 审查、改写 verdict、改写下一接收方或改写 PASS 输出合同。
4. 任务 prompt 与中央合同冲突时，该 package 本身必须 `REVISE`；不能用“中央合同优先，所以忽略冲突”继续 PASS。
5. Critic 发现兼容性冲突后仍应继续完成当前证据允许的其他审查，尽量一次报告全部真实 blocker。
6. PASS 后用户追问已批准机制时，先解释 approved package；只有发现真实矛盾或用户明确提出更强要求，才重新进入设计。
7. 矛盾证据可以由 Critic 自己在解释过程中发现，不要求必须由用户主动提供。
8. 当前 Project setting 与 Capability Gate Policy 1.2 已有正确顶层语义，本轮不重复修改。
9. 不修改 Clear Writing 0.6 产品架构、G1-G6 产品语义、Bridge Kit 或 Plugin Creator。

## 3. 1.8 的最小正式改动

### 3.1 Planner Role Contract 1.8

在 1.7 基础上只增加两个职责。

**A. 最终 Critic prompt 兼容性检查**

Planner 在把 execution-ready package 送 Critic 前，必须确认 task-specific prompt：

- 没有把最终审查缩成旧 finding closure；
- 没有重新定义 `PASS / REVISE`；
- 没有重新定义 `READY_FOR_CODEX`；
- 没有把下一入口改成 `USER_AUTHORIZATION` 或其他中间状态；
- 没有省略用户架构说明；
- 没有省略短 `COPY TO CODEX`；
- 没有要求全文复制 Kickoff Draft。

若存在冲突，Planner 必须先修 prompt；不能把冲突留给 Critic“自行理解”。

**B. 短 Codex handoff 可生成性检查**

Planner 在送最终审查前必须能从冻结 Goal/Kickoff/授权边界生成一个不猜测、不扩权的短 Codex handoff。若做不到，说明 execution package 尚未闭合。

### 3.2 Critic Role Contract 1.8

在 1.7 基础上增加三项。

**A. execution-ready compatibility hard gate**

最终审查开始时先检查 task-specific prompt 与中央合同兼容。冲突存在时当前 package 不得 PASS；但 Critic继续检查能检查的其余内容，尽量一轮报全 blocker。

**B. PASS atomic delivery**

同一条回复必须同时包含五项必要组成；缺任一项时不存在有效 PASS。不能“先 PASS 后补格式”。若历史回复已经错误给出不完整 PASS，只能对同一 exact package 做一次有界重审，不能靠后续零散补充追认。

**C. PASS 后解释稳定性**

用户后续问题按实际语义归类：

1. 解释请求：从 approved package 解释，不新增机制、不撤回 PASS；
2. 矛盾证据：若回答问题时发现 approved package 无法支持已批准承诺，明确指出失效语义，同一 task 回 Planner；
3. 新要求：只有用户明确增加原冻结范围之外的要求，才进入新设计。

“怎么保证”“为什么这样工作”等普通问题本身不自动升级成更强产品要求。

## 4. 两阶段 Clear Writing 回归

### 4.1 第一阶段：兼容性负控

固定输入：

`d7b810d194ead881303aaca9c2e4f1d59a97c1f1`

不修改该 commit。

1.8 实现后，使用其中旧 task-specific Critic prompt 做确定性/人工合同回放。

预期：

`REVISE`

至少应识别：

- “只复核四个 blocker”与最终全量审查冲突；
- `NEXT_HANDOFF=USER_AUTHORIZATION` 与中央 `NEXT_HANDOFF=CODEX` 冲突；
- PASS 输出合同缺少中央原子交付要求。

若 1.8 仍能让该 exact package PASS，治理修复失败。

### 4.2 第二阶段：真实正向 execution-ready 回归

只有第一阶段通过后，才准备新的 Clear Writing 0.6 review package。

允许的 Clear Writing 变化严格限于**审查兼容性**：

- 产品 Proposal、Plan、Goal、Runbook、Kickoff 的冻结产品语义不重新设计；
- 不修改 G1-G6 产品定义；
- 不新增 `create_blob`、MCP、App、网关、新 Gate 或全局写入拦截；
- 只修正 task-specific execution-ready Critic prompt，使其服从最新中央合同；
- 若 locator / package identity 因新 commit 必须同步，只做机械同步。

必须形成新的 exact package commit，不能继续称为 `d7b...`。

新的 task-specific Critic prompt 只能提供：

- 当前对象和 exact locators；
- 旧 finding 作为重点证据；
- 当前 package identity；
- Clear Writing 特有的事实边界。

它不得自行定义最终 verdict、完整审查范围、PASS 输出格式或下一接收方，而应明确这些由最新 `CRITIC_ROLE_CONTRACT.md` 决定。

随后独立 Critic 必须重新核对：

- 完整稳定用户承诺；
- Proposal / Plan / Goal / Kickoff；
- 正常成功链；
- G3 的真实 read → final candidate → pre-write identity check → write → readback → candidate equality → full artifact review；
- 关键失败、恢复、权限和 release boundary；
- G1-G6 是否仍由批准包真实定义。

如果全量审查发现新的真实产品 blocker，正确结果是 `REVISE`，继续同一 Clear Writing task 修复；不能为了制造治理“正向样本”强迫 PASS。

只有一个**本身合法**的新 package 真正得到一次 execution-ready PASS，而且同一条回复一次交齐五项原子交付，才算本治理正向 PASS 回归成功。

## 5. 正向 PASS 后的解释回归

若第二阶段合法 PASS，立即使用一个自然 follow-up 检查解释稳定性：

> 写入 repo 的文件怎么保证确实走了 Clear Writing？

合格行为：

- 直接解释 approved G3 链；
- 说明它保证的是显式 Clear Writing 入口内的 GitHub UTF-8 文本最终化声明；
- 不新增架构；
- 不撤回 PASS；
- 不把问题扩大成“所有插件所有写入全局不可绕过”。

若解释时发现 approved package 实际缺少支撑其既有声明的机制，应把它视为矛盾证据并回同一 task Planner。

若用户明确提出“所有插件所有 repo 写入都必须技术上不可绕过 Clear Writing”，才属于新的更强要求。

## 6. 验收与停止条件

### 6.1 确定性合同回放

至少覆盖：

1. 旧 Clear Writing 冲突 prompt → 必须 REVISE；
2. 机器字段齐全但缺实际架构说明 → 不得 PASS；
3. 缺 `NEXT_HANDOFF=CODEX + COPY TO CODEX` → 不得 PASS；
4. 全文倾倒 Kickoff Draft → 不符合 PASS 合同；
5. prompt 只强调上一轮 blocker、但明确最终仍按中央合同全量复核 → 兼容；
6. PASS 后解释请求 → 只解释批准包；
7. 解释中发现真实矛盾 → 回 Planner；
8. 用户明确提出新更强要求 → 识别为新设计。

### 6.2 成功条件

本治理候选最终重新 `CANDIDATE_ACCEPTED` 需要：

- 1.8 合同实现与独立实现审查通过；
- 第一阶段负控按预期 REVISE；
- 第二阶段使用新的合法 Clear Writing package；
- 全量 execution-ready 审查若证据支持 PASS，则一次交齐五项；
- 随后的解释回归稳定；
- 若第二阶段发现真实产品 blocker，则治理候选保持未完成，先让 Clear Writing 同任务修复，不能换题追 PASS。

不机械增加第二个正向任务族；只有新证据说明 Clear Writing 无法覆盖本次修复目标时才考虑补充。

## 7. 实施范围

中央治理实现允许修改：

- `docs/workflows/PLANNER_ROLE_CONTRACT.md` → 1.8；
- `docs/workflows/CRITIC_ROLE_CONTRACT.md` → 1.8；
- `docs/workflows/CHATGPT_WEB_COLLABORATION_REGRESSIONS_2026-10-17.md`；
- `docs/workflows/CHATGPT_WEB_CRITIC_GOOD_REVIEW_EXAMPLES_2026-10-20.md`；
- `results/chatgpt-web--pass-integrity/**`。

第二阶段回归准备额外允许在 Clear Writing 现有设计分支上**仅修改 task-specific execution-ready Critic prompt 及必要 locator/package identity**，形成新的 exact package commit。不得借此修改产品 Proposal/Plan/Goal/Runbook/Kickoff 的产品语义或 production code。

禁止修改：

- 当前 Project setting；
- `PLUGIN_CAPABILITY_GATE_POLICY.md`；
- Clear Writing 产品架构/生产代码；
- Bridge Kit；
- Plugin Creator；
- 任何新角色、schema、状态机、数据库、服务、watcher、daemon 或统一 prompt compiler。

## 8. 实施后阶段

执行顺序冻结为：

1. 实施 Planner/Critic 1.8；
2. 独立实现审查；
3. 运行确定性兼容性回放；
4. 实现后最终评估前 Critic 安全门，只能 `PROCEED_TO_FINAL_EVALUATION / REVISE`；
5. 第一阶段旧 package 负控；
6. 准备新的 Clear Writing 兼容 package commit；
7. 第二阶段真实 execution-ready Critic 回归；
8. 若获得合法 PASS，再做解释 follow-up；
9. 证据成立后记录新的优质 PASS 示例并恢复治理任务 `CANDIDATE_ACCEPTED`。

其中第二阶段 Critic 的 PASS 是 **Clear Writing 0.6 自己的 execution-ready PASS**，不是本治理实现后的第二个治理 PASS。

## 9. 外部现实核查

OpenAI 关于 instruction hierarchy 的公开资料确认：不同来源指令会发生冲突，可靠行为依赖明确的优先级；低优先级约束不应覆盖更高优先级合同。v0.5 采用的只是这一轻量原则：中央角色合同拥有 verdict/交付语义，task prompt 只能补充当前任务事实和重点，不另建运行系统。

## 10. 看板

当前搜索未发现 `chatgpt-web--pass-integrity` 的现有 tracking Issue。

维护看板要求 reader-facing Issue / Project 文案在 mutation 前真实调用 Clear Writing；当前 Planner surface 没有可验证的 Clear Writing mutation 调用链，也没有 GitHub Project mutation surface，因此本轮不创建 Issue、不声称 Project 已同步、不要求用户手工维护。

下一次同时具备 Clear Writing 与 Project mutation 的 maintenance action 应：

- 创建或绑定一个 `maintenance-track` Issue；
- Area = repo；
- Status = DOING；
- 当前执行锚点 = 本 v0.5 package；
- 下一步 = 独立 Critic 审查；
- 将真实 `tracking: #N` 回写到对应 canonical maintenance source（若当时存在合法 source entry）。

## 11. 当前状态

`PASSINT-V04-01=CLOSED_IN_V0_5_DESIGN`

当前仍未实施 1.8，也未修改 Clear Writing 产品。

下一步：独立 Critic 审查 v0.5 Proposal + 同版 execution package。该轮仍是设计/执行包审查，只能 `PROCEED / REVISE`，不得提前给 Codex 入口。
