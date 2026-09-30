# workflow-core 0.5 正常入口与执行路线可靠性提案 v0.1

日期：2026-09-30  
角色：Planner  
目标仓库：`YuukiAS/AI_Skills_Collection`  
目标插件：`workflow-core`（Verified Workflow）  
设计主题 / task key：`workflow-core--normal-entry-reliability`  
source branch/ref：`main`  
设计基线：`97de8aa3cf36a379aa978ec4f90535df5b04a538`  
当前插件版本：`0.4`  
审查阶段：设计提案，尚未进入实现

## 1. 结论

有必要继续做下一次正式 refinement，但现在**不直接改版本号，也不进入实现**。

建议把下一批正式用户可见改进冻结为 `workflow-core 0.5` 候选，目标不是增加一套新的 workflow，而是修复现有正常入口的三个基础可靠性问题：

1. 复杂任务应该更稳定地自然触发 workflow-core，同时简单单工具任务仍不应被它过度接管；
2. workflow-core 一旦触发，遇到工具、运行环境或资源问题时，必须先消费当前任务合同和匹配 specialist，再判断能力是否真的不存在；
3. 主路线失败后，不能把“当前 PATH 找不到”“某个可选 flag 不支持”或“第一次探测失败”直接升级成静默降级路线；只有与冻结目标真正等价且已授权的替代路线才可自动继续。

这是一批真实用户行为改变，因此如果实现、原失败回放、无关回归、正常入口和 release closure 全部通过，插件应从 `0.4 -> 0.5`。当前只是设计阶段，版本保持 `0.4`。

## 2. 为什么现在值得做

最近 STAT5060 Tutorial 1 在同一个真实任务中连续复现了两次同类问题：

- workflow-core 已经实际加载，但 Codex 只检查默认 shell 的 Python / R，便把当前 PATH 缺包或缺命令解释成“工具不可用”，准备改走 Node/标准库生成图；
- 中文数学 PDF 任务中，裸 XeLaTeX 缺 `ctex` 后，Codex先自行搜索 conda / TeX，再准备 HTML/Chromium 路线；直到用户第二次纠正，才读取已经安装、且明确规定 `render_resources/chinese_math_pdf`、环境探针和“不得自动 Chromium fallback”的 `render-chinese-math-pdf` specialist。

因此问题已经不是“忘记写一条规则”，而是正常消费链没有把现有原则落实到**触发 → specialist 路由 → 能力发现 → fallback 决策**上。

另有两个已有真实 TODO 与同一根因高度相关：

- tracking #8：把浏览器“没有 foreground / visible flag”误判成“没有可用浏览器能力”；
- tracking #9：把已经结束的旧任务局部禁令误当成当前全局约束。

它们都属于“没有先判断当前真实能力和当前有效合同，就过早得出阻塞或替代结论”。

## 3. 现实替代方案比较

### 方案 A：不升级，只在 STAT5060 / Longleaf 写项目规则

不采用。两次失败发生在不同专业子任务，且 #8、#9 已有跨项目证据。把规则写回 STAT5060、Longleaf 或某台机器，只会制造局部补丁。

### 方案 B：让 workflow-core 几乎所有任务都触发

不采用。OpenAI 当前 Skills 文档说明，模型先看到 skill 的名称和 description，再决定是否加载全文；官方最新指导还特别提醒，过宽或过长的 description 会增加错误触发和上下文负担。正确方向是提高**复杂任务的召回率**，而不是把 workflow-core 做成默认常驻大提示词。

### 方案 C：新增一个 Environment Discovery / Fallback 顶级 skill

不采用。当前 workflow-core 本来就拥有 source-of-truth、specialist routing、escalation 和 completion boundary。新建顶级 skill 会制造职责重复，也不能解决“workflow-core 已经加载但没按合同执行”的问题。

### 方案 D：在现有 workflow-core 内做一次 bounded 0.5 refinement

采用。保持根 `SKILL.md` 为简短路由器，把详细能力发现与 fallback 规则放进已有 `references/escalation-rules.md`，同时完善 trigger metadata、真实 invocation eval 和回归。这样既解决根因，又避免把根 skill 写成一套环境管理器。

## 4. 外部核查

本轮只使用少量官方资料验证 trigger / skill 设计方向：

1. OpenAI Skills 文档：skill 的 name / description 是模型是否考虑加载该 skill 的关键入口；完整指令只在匹配后加载。  
   https://developers.openai.com/plugins/concepts/skills
2. OpenAI Build skills：description 应描述用户目标与触发条件，详细步骤放正文；workflow boundary 应说明输入、步骤、停止/询问边界和 supporting files。  
   https://developers.openai.com/plugins/build/skills
3. OpenAI 2026-09-11 的 Codex 指导：skill description 应尽量短且精确；多 workflow skill 应用 progressive disclosure，让根文件只做必要路由。  
   https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra
4. OpenAI Skills eval 指导：至少分别测试显式调用、隐式调用、带上下文调用和负对照，并把 environment assumption 当作真实 failure source。  
   https://developers.openai.com/blog/eval-skills

这些资料支持的是“提高精确触发 + 真实回放”，不支持把 workflow-core 改成 always-on。

## 5. 0.5 候选机制

### 5.1 正常入口：提高复杂任务召回，但不扩大到简单任务

修改 `codex-workflow-protocol` 的 description、`agents/openai.yaml` 与 trigger eval，使以下任务更明确属于 workflow-core：

- 多阶段实现 / 返修 + 构建 / 渲染 + 最终验收；
- 需要跨 specialist 协作；
- 需要环境 / resource discovery 后才能执行冻结主路线；
- 需要在 primary route、等价恢复、非等价 fallback、Human Gate 之间做判断；
- 有显式 acceptance / release / recovery boundary。

保留负边界：

- 一条命令怎么写；
- 简单编译一次；
- 单纯把 Markdown 转 PDF；
- 普通解释 / 翻译 / 局部措辞。

不通过把 `allow_implicit_invocation` 变成更激进的全局开关解决；它已经是 `true`。重点是 metadata 与真实 invocation eval。

### 5.2 Specialist-first，而不是先自行发明替代实现

根 `SKILL.md` 增加一个很短的执行不变量：

> 当当前失败落在已有 specialist 的职责范围内时，在改变实现路线前先消费该 specialist 的合同和正式 probe / resource route；workflow-core 只决定什么时候需要 specialist、什么时候升级/停止，不自行发明领域替代方案。

例如：

- 中文数学 PDF 的 TeX/resource route 由 `render-chinese-math-pdf` 决定；
- 统计绘图方法由对应统计 / 可视化能力决定；
- Bridge 的 Git/Reviewed Handoff runtime 由 Bridge Kit 决定。

这不是要求启动时把所有 specialist 全读一遍。只有当前任务/失败真正进入某 specialist 的职责边界时才加载。

### 5.3 “当前 shell 找不到”只能证明当前 shell，不能证明能力不存在

把详细规则放入现有 `references/escalation-rules.md`，不新增环境管理系统。

在声明 capability unavailable 前，做**与当前项目和 specialist 相匹配的 targeted discovery**：

1. 当前用户 / frozen Goal / repo 规则指定的 canonical route；
2. 已匹配 specialist 指定的 probe、resource、wrapper 或 runtime；
3. 项目已声明的环境入口，例如 module、venv/conda、project runner、container、site profile；
4. 当前 shell 的 PATH / 默认命令状态作为局部证据。

禁止为了“保险”全盘扫描 home、`/overflow` 或系统目录。缺哪个事实，就查哪个 locator。

`command not found`、缺一个 package、某个可选 flag 不存在，只能支持对应局部结论，不能自动支持“整个能力不可用”。

### 5.4 Fallback 必须先过等价性判断

在切换 primary route 前先分类：

- **同一冻结效果、质量、证据、安全/隐私边界与用户产物均保持不变，且已授权**：允许自动采用等价恢复路线；
- **只是当前入口没发现 capability**：继续 targeted discovery，不叫 fallback；
- **会改变方法、质量、统计/科学语义、可复现性、artifact identity、provider/recipient 或 acceptance evidence**：不得静默切换；
- **specialist / frozen contract 明确禁止的 fallback**：直接禁止；
- **确实没有合法等价路线**：报告 precise blocker，只有真正需要用户产品/授权决定时才进入 Human Gate。

因此，“Chromium 也能出 PDF”“Node 也能画点”“GEE 也能跑”都不能仅凭“能产出东西”被判成等价。

### 5.5 当前有效合同要区分 scope 与 lifetime

补一条小而通用的 source-of-truth 规则：

- current user instruction / current frozen task 优先决定本轮目标；
- 旧 task 的局部 prohibitions 在该 task 结束后不能自动升级成永久全局规则；
- repo-level safety、security、destructive-action、credential、data/privacy 等明确 durable boundary 仍持续有效；
- 真冲突且会改变产品/权限语义时才问用户。

这处理 tracking #9，不新建 instruction registry 或状态机。

### 5.6 可预见的 approval-sensitive effect 要提前处理，但不复制 Bridge

对 tracking #7 只做 workflow 层最小消费：

- frozen task 已经明确包含某个必需的 deployment、paid/external call、private transfer、resource allocation、Persistent Run 等效果时，在大量依赖工作前确认当前会话是否已有同一 bounded authorization；
- 已授权的 exact frozen effect 不重复索权；
- 新 provider/resource/purpose/artifact 或扩大副作用仍需正常 gate；
- Bridge-managed repo 优先消费 Bridge Kit 已有 upfront authorization / kickoff 机制；
- workflow-core 不新增 authorization store、schema、daemon、wrapper 或 Host Policy。

## 6. TODO 处理建议

| TODO | Planner v0.1 disposition | 0.5 是否处理 |
|---|---|---|
| Loaded workflow-core still misclassified environment capability... | `PROMOTE_NOW`，这是 0.5 主回归 | 是 |
| #5 Keep AI_Skills workflow rules separate from Bridge Kit runtime bugs | 候选 `HISTORICAL_RESOLVED`：Bridge 已有 `plugin-replay`，AI_Skills Executor 已消费；Critic 复核后再正式关闭 | 否 |
| #6 Real-task-driven Reviewed Handoff batches | 候选 `HISTORICAL_RESOLVED`：当前 continuous refinement / AGENTS 已明确 real-task-driven、bounded batch、关闭 watcher | 否 |
| #7 bounded kickoff | `PROMOTE_NOW`，但只做 workflow consumer / preflight，不复制 Bridge | 是 |
| #8 browser foreground capability | 合并为 0.5 的“capability discovery 不得由可选 flag 推断不存在”真实回归；不写浏览器专用大规则 | 是，合并 |
| #9 task-local prohibition lifetime | `PROMOTE_NOW`，补 active-contract scope/lifetime | 是 |
| #10 acceptance artifact packaging | 保持独立，056 后仍有剩余价值，但与本次 trigger/fallback 根因不同；不把 0.5 变成 mega-release | 否，后续独立 |
| #11 reviewed worktree authorization/runtime | 候选 `HISTORICAL_RESOLVED`：Bridge 0.9.0/0.9.1 + workflow-core 0.4 已提供 bootstrap/resume normal entry，并有 FB-G4/G5 真实证据 | 否 |

Critic 需要重点挑战上述“resolved / merge / defer”是否有直接证据，不能因 Planner 想缩 scope 就机械接受。

## 7. 预计修改层

若设计 PASS，预计只修改：

- `skills/core/codex-system/codex-workflow-protocol/SKILL.md`
- `skills/core/codex-system/codex-workflow-protocol/references/escalation-rules.md`
- 必要时小幅修改 `verification-matrix.md` / `task-template.md`
- `agents/openai.yaml`
- `evals/trigger_queries.json`
- workflow-core 专属回归 / invocation eval
- 生成层 Marketplace payload
- release 时的 workflow-core changelog / Marketplace version / repository release metadata

默认**不改**：

- Longleaf `/users`、module、conda、TeX 实际环境；
- STAT5060 repo；
- `render-chinese-math-pdf` specialist 规则；
- Bridge Kit runtime / Host Policy；
- 新 plugin / 新顶级 skill；
- 新 state machine / authorization database / watcher / daemon；
- acceptance artifact #10 的正式实现。

若实现阶段证明必须改 Bridge Kit 才能完成本提案核心目标，停止并回 Planner/Critic，不在 0.5 中顺手扩 repo。

## 8. Capability Gate Matrix

### G1 — 正常入口与 specialist 组合

**能力**：复杂任务在不点名 workflow-core 时能自然加载 workflow-core；需要领域能力时同时加载正确 specialist；简单任务不过度触发。  
**区别**：只证明 routing / invocation，不证明 fallback 决策本身。  
**正常入口**：正式候选插件安装后的普通 Codex prompt。  
**证据**：至少包含显式调用、隐式调用、带噪上下文调用、负对照；加入真实近似任务，如“中文数学讲义返修 + 资源链渲染 + QA”与“只把 Markdown 转 PDF”的对照。必须有实际 plugin consumption evidence，而不是字符串扫描。  
**失败**：复杂任务未加载；简单任务明显误加载；需要 specialist 时 workflow-core 抢做领域实现。  
**回归边界**：当前简单命令/解释/单步渲染仍保持轻量。  
**最终候选**：是。

### G2 — 能力发现与 specialist-first

**能力**：primary tool 当前 PATH 不可见、默认环境缺包或某个可选入口失败时，先查冻结合同 + specialist + 项目已声明环境，再决定不可用。  
**区别**：证明 capability discovery；不直接证明非等价 fallback 被拦住。  
**正常入口**：正式候选处理安全 fixture / real-regression replay。  
**证据**：至少回放两类：  
1. 工具不在默认 PATH，但项目已有可发现环境/runner；  
2. renderer 默认 TeX 缺包，但 specialist 已提供 resource probe。  
并保留 #8 的“可选 foreground flag 不支持、普通 first-party mode 可用”作为第三种不同 surface 的回归。  
**失败**：直接把局部探测失败解释成 capability absent；在读取 specialist 前发明替代实现；无目标地大范围扫描主机。  
**回归边界**：真正不存在 capability 时仍要 fail closed，不得假装可用。  
**最终候选**：是。

### G3 — fallback 与授权边界

**能力**：只有真正等价且已授权的 route 才自动恢复；非等价/被 specialist 禁止的 fallback 停止；可预见的 approval-sensitive effect 提前处理且不重复索权。  
**区别**：证明 route substitution / authority，不等同于 G2 的“有没有找到能力”。  
**正常入口**：普通复杂任务与 Bridge-managed fixture 各一类。  
**证据**：  
- 明确禁止 Chromium 的 TeX fixture 不得切 Chromium；  
- 一个 lower-privilege 但冻结效果完全等价的 route 可以自动继续；  
- 同一已授权 frozen effect 不二次询问，新 provider/resource/purpose 仍 gate。  
**失败**：为了继续跑而降低质量/语义/证据；repo text 冒充当前用户授权；同一 exact effect 重复索权。  
**回归边界**：W2 的 least-privilege equivalent recovery 仍有效。  
**最终候选**：是。

### G4 — 当前合同 scope / lifetime

**能力**：旧 task 局部禁令不会压过新的明确目标；真正 durable 的安全/权限边界不会因“新任务”失效。  
**区别**：证明 instruction lifetime，而非 environment/fallback。  
**正常入口**：两组相反 fixture。  
**证据**：一个 stale task-local prohibition 被当前任务正确取代；一个 repo-level durable safety boundary 继续阻断越界。  
**失败**：旧任务造成假 Human Gate，或 durable safety 被错误过期。  
**回归边界**：现有 source-of-truth 与 authorization 规则不降级。  
**最终候选**：是。

### G5 — 最终候选 broad regression / integration

**能力**：0.5 不破坏 0.3 的 W1–W5、0.4 的 Reviewed Handoff bootstrap/resume、candidate replay、Marketplace/source parity。  
**区别**：证明 shared routing/default prompt 改动后的兼容性。  
**正常入口**：同一 final candidate 的 candidate plugin replay + repository regression。  
**证据**：既有 056 workflow-core scenarios、0.4 Reviewed Handoff routing scenarios、source/generated/version checks、全仓风险匹配测试。  
**失败**：旧行为退化、不同 candidate 拼 evidence、只靠单元测试声称 normal-entry 成功。  
**最终候选**：是。

不要求固定更多 gate。若 Critic 认为 G2/G3 可合并且不会降低可诊断性，可合并；若认为某个 gate 只是重复 proxy，应删除。

## 9. 版本与发布决策

本设计阶段：

```text
Repository bump decision: NONE
Reason: 仅规划，没有 production behavior change。
Affected plugins:
- workflow-core: NO_BUMP
  Reason: 当前仍为设计候选，尚未实现、回放和 release closure。
```

若 0.5 最终实现并通过同一 final candidate 的所有 release gates：

```text
Repository bump decision: PATCH
Reason: workflow-core 在现有 collection contract 内获得兼容可靠性改进。
Affected plugins:
- workflow-core: 0.4 -> 0.5
  Reason: normal-entry routing、capability discovery、fallback/authorization、instruction-scope 行为发生用户可观察改变。
```

若届时 repository 仍是 `5.4.0`，预期 repository release 为 `5.4.1`；若 main 已有其他正式 release，按届时当前版本做下一次 PATCH，不预占版本号。

本轮不建议提升 workflow-core maturity；连续两次真实失败反而说明先修基础可靠性，再用新的独立真实任务判断 maturity。

## 10. 执行前停止条件

以下任一出现都必须返回 Planner/Critic，而不是扩大 0.5：

- 需要新增环境管理服务或机器 inventory；
- 需要修改 Longleaf `/users` / module / conda canonical architecture；
- 需要修改 Bridge Kit 才能完成核心机制；
- 需要新增授权数据库、状态机、watcher、daemon；
- 为提高触发率必须让 workflow-core 对普通单步任务几乎 always-on；
- Gate 只能靠 task-specific hardcode 才通过。

## 11. Maintenance Board 状态

本轮已进入正式 Planner design，但当前 ChatGPT surface：

- 没有 GitHub Project mutation 工具；
- 当前可用 Skills 列表里没有已安装的 Clear Writing / `writing-style`，因此不能伪装成已经满足 tracking Issue reader-facing copy 的强制前置条件。

所以本轮不创建/改写 tracking Issue，不声称 Project 已同步。下一次 Project-capable + Clear-Writing-capable maintenance action 应先机械核对本提案仍 current，再执行：

1. 为“environment capability / specialist-first / fallback”主问题创建或绑定一个 `maintenance-track` Issue，并在 source entry 回写 `tracking: #N`；
2. 将该 Issue 的 Project Status 设为 `DOING`，Area=`workflow-core`，当前执行锚点指向本 Proposal；
3. 若 Critic 同意 #8 合并，将 #8 作为同一 top-level idea 的 merged evidence 处理，并更新 source locator；若不同意则保持独立；
4. #7、#9 若纳入 0.5，Project Status 进入 `DOING` 并把当前执行锚点指向本 Proposal；
5. #5、#6、#11 只有在 Critic确认 resolved evidence 后才进入 closure；不得由本 Proposal 自行把它们标成 DONE；
6. #10 保持当前 lifecycle，不因 0.5 自动推进。

不得要求用户手工拖 Project 或补 locator。

## 12. 本 Proposal 不批准什么

- 不批准 Codex 实现；
- 不批准 branch/worktree 创建；
- 不批准版本 bump；
- 不批准 Bridge Kit、Longleaf 或 STAT5060 mutation；
- 不批准付费调用；
- 不批准 release / publish；
- 不宣称任何 TODO 已经正式关闭。

下一步仅是交给独立 Critic 审设计方向、TODO disposition 和 Gate Matrix。
