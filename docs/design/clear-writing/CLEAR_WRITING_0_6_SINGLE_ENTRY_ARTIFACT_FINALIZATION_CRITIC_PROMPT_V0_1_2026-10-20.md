# Clear Writing 0.6：单入口与最终产物绑定——独立 Critic 审查提示词 v0.1

你现在担任 `YuukiAS/AI_Skills_Collection` 的全新独立 Critic，审查 Clear Writing 0.6 的产品归因与架构方案。

这不是实现验收，也不是继续 Planner 自审。你必须独立判断：本次失败究竟是否由当前 ChatGPT Personal Plugin 的多 Skill 暴露、缺少总入口和最终产物绑定造成；Planner 提出的“单入口 + 逐产物路由 + 写入后回读”是否真正解决问题，还是错误归因、过度设计或纸面约束。

本轮只给设计阶段结论：

```text
PROCEED
或
REVISE
```

不得给 `PASS`，不得输出 `READY_FOR_CODEX=YES`，不得实施任何修改。

## 一、Active Review Context

```text
target_repo = YuukiAS/AI_Skills_Collection
target_plugin_or_domain = writing-style / Clear Writing
design_topic_or_task_key = clear-writing--single-entry-artifact-finalization
source_branch_or_ref = design/clear-writing--single-entry-artifact-finalization
proposal_path_and_version = docs/design/clear-writing/CLEAR_WRITING_0_6_SINGLE_ENTRY_ARTIFACT_FINALIZATION_PROPOSAL_V0_1_2026-10-20.md / v0.1
proposal_commit = 3eefc626b86566113125a06fc6046a2bec1eafb2
review_stage = DESIGN_PROPOSAL_REVIEW_V0_1
tracking_issue = YuukiAS/AI_Skills_Collection#13
current_formal_plugin = writing-style 0.5 / ChatGPT personal wrapper 0.5.0
```

Planner 准备本审查包时，`AI_Skills_Collection/main` 为：

```text
aa2e6ade13cf6e038a69ec4a2b5fbe318bebed39
```

审查时必须先核实最新 `main`；若已经前进，读取最新规则并说明是否改变本方案判断。

## 二、首先读取当前治理来源

从 `YuukiAS/AI_Skills_Collection` 最新 `main` 实际读取：

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md`
- `docs/workflows/CONTINUOUS_REAL_WORLD_SKILL_REFINEMENT.md`
- `docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md`
- `TODO.md`
- `docs/plugin-todos/writing-style.md`
- `docs/design/READER_FACING_COMMUNICATION_PLUGIN_BOUNDARIES.md`

再读取 Issue `#13` 的当前正文和评论，核实其真实生命周期、旧设计、0.5 发布边界和当前追踪语义。

若本轮涉及正式能力修改和未来发布，必须按 `PLUGIN_CAPABILITY_GATE_POLICY.md` 审查 Capability Gate Matrix，不得用文件、测试、回执或 Skill 已加载冒充用户能力。

## 三、读取本轮冻结审查对象

从 exact commit：

```text
3eefc626b86566113125a06fc6046a2bec1eafb2
```

完整读取：

```text
docs/design/clear-writing/CLEAR_WRITING_0_6_SINGLE_ENTRY_ARTIFACT_FINALIZATION_PROPOSAL_V0_1_2026-10-20.md
```

不得只看摘要或本提示词中的转述。

## 四、直接核实现有实现，不接受 Planner 口头归因

### 4.1 当前 ChatGPT Personal Plugin

通过 Plugin Creator 或当前可用的等价正式工具，直接检查用户现有：

```text
writing-style / Clear Writing 0.5.0
Project Instructions Editor 0.2.8
```

至少核对：

- 两个插件各自的 manifest；
- `capabilities`；
- 顶层 Skill 数量；
- Skill 目录结构；
- 是否存在 root `plugin.json`；
- 是否存在唯一总入口；
- PIE 的唯一 Skill 是否真的拥有完整工作合同；
- Clear Writing 的六个 Skill 是否只是并列暴露；
- 更新是否采用 overlay，以及旧 Skill 路径是否必须显式删除。

不得因为 Planner 说“PIE 是单入口”就直接接受类比。

### 4.2 当前 canonical Clear Writing source

实际读取当前正式版本中：

- `skills/writing/core/writing-fidelity/SKILL.md`
- `skills/writing/core/response-clarity/SKILL.md`
- `skills/writing/core/product-ui-copy/SKILL.md`
- `skills/writing/core/scientific-prose/SKILL.md`
- `skills/writing/core/scientific-rewrite/SKILL.md`
- `skills/writing/core/chinese-prose/SKILL.md`
- `scripts/codex_marketplace_config.json`
- `plugins/codex/plugins/writing-style/.codex-plugin/plugin.json`
- `profiles` 中与 `writing-style` 直接相关的当前 exposure

重点核实：本次失败所违反的“正式中文文档路线、结构重写、中文终审、英文密度和内部流程语言清理”是否早已存在。若规则已存在，应把重点放在入口、路由、消费和最终产物，而不是建议继续堆同义规则。

### 4.3 历史调用策略与 Web Gate

至少读取：

- `docs/design/clear-writing/CLEAR_WRITING_EVERY_RESPONSE_INVOCATION_POLICY_PROPOSAL_V0_2_2026-10-18.md@1f905d294c3c2e5b0951c9d5e818c285d236cef7`
- 对应 Critic PASS：`50e09a2dc68a097ef21e0cf245f7951eb9d06f89`
- `results/clear-writing--every-response-invocation-policy/web-gate-v0.4/RESULT.md`
- 0.5 release closure 与 Issue #13 当前说明

必须区分：

1. 无显式调用时，Project policy / automatic selection 是否稳定；
2. 用户已经显式选择插件后，正确完整路线是否覆盖全部交付对象。

不得把历史 `W2=INCONCLUSIVE` 错误解释为本次显式调用失败的直接原因，也不得假装 0.5 已经证明当前任务类型。

## 五、读取真实失败，而不是抽象例子

通过 GitHub 读取：

```text
YuukiAS/AI_Research_Toolkit
commit = 0ff0f43f3b04286273490e4c4870975f4aa7a7f8
path = docs/research/software-production/16_THREE_RUN_SYNTHESIS_AND_DELIVERY_ASSURANCE_20261015/DELIVERY_ASSURANCE_V0_4_READER_GUIDE_20261019.md
```

同时使用用户在当前对话提供的证据：

- 用户消息中已经显式选择 `$clear-writing`；
- 后续助手承认读取了 `chinese-prose` 与 `response-clarity`，但没有把一次可验证的 Clear Writing 输出作为最终文档；
- 文档仍大量使用内部流程英文和机器化结构；
- 聊天回复与外部 GitHub 文档的质量不一致。

若无法访问完整对话证据，明确这一限制；但必须直接阅读公开 Reader Guide 全文，不能只凭 Planner 评价。

## 六、重新核对平台现实

只使用 OpenAI 官方当前资料，至少核实：

- ChatGPT 插件的直接选择语义；
- 一个插件包含多个 Skill 时的选择与加载机制；
- Skill metadata 与完整 instructions 的关系；
- 是否存在公开保证：选择插件后所有 Skill 会全部加载并按固定顺序执行；
- skills-only 插件能否在同一轮使用 GitHub/Drive/文件工具完成外部写入与回读；
- `Interactive` 与 `Skills` capability 在当前平台的真实含义；
- Personal Plugin overlay 更新和删除旧文件的实际合同。

若公开资料不能证明某项行为，必须把它列为待探针假设，不得用 PIE 的现状反推平台承诺。

## 七、独立审查核心问题

### CW06-D01：根因是否过度断言

判断 Proposal 是否正确区分：

- 已验证事实：用户已经显式选中插件；最终 GitHub 文档没有得到合格的完整终审；当前个人插件并列暴露六个 Skill；没有总入口和最终产物绑定；
- 合理推断：多 Skill 二次路由与多交付对象缺少 owner，使失败可以发生；
- 未验证假设：单入口一定能解决、某个 Skill 实际未加载、`Interactive` 比 `Skills` 更可靠。

若 Proposal 把推断写成事实，要求 `REVISE`；若边界已经充分清楚，关闭该 finding。

### CW06-D02：PIE 类比是否成立

独立判断 PIE 能用是否主要因为：

- 单 Skill；
- 任务范围窄；
- 完整输入门槛和输出合同；
- 主要交付物直接位于当前回答；
- manifest/capability 差异；
- 其他尚未识别的原因。

判断 Planner 是否只复制了 PIE 的表面结构，还是正确吸收了其真正优势。

### CW06-D03：单入口是不是最小正确方案

比较至少以下路线：

1. 仅改插件 metadata/default prompt；
2. 保留六个顶层 Skill，增加一个第七个协调 Skill；
3. ChatGPT Personal Plugin 只暴露一个总入口，六项能力变成该入口引用；
4. 直接引入 App/MCP 外部 finalizer；
5. 不改插件，只要求用户精确选择内部 Skill。

Critic 必须独立说明：采用路线是否真的最轻，是否存在更简单且同样能阻止本次失败的办法。

### CW06-D04：总入口是否成为错误的新领域 owner

检查 `clear-writing` 是否只拥有：

- 交付对象识别；
- 路线选择和组合；
- 候选先于写入；
- 写入后回读；
- 逐对象完成声明。

它不得重新决定科研结论、报告信息架构、幻灯片叙事、统计含义、科研图编码或产品语义，也不得复制六份专业规则形成第二套 source。

### CW06-D05：route references 是否可维护

检查 Proposal 的确定性生成和 source hash 方向是否足以防止：

- Personal Plugin 规则漂移；
- Codex Marketplace 与 ChatGPT 包装语义分裂；
- 人工复制六份 Skill；
- downstream 插件调用失效；
- 未来更新遗漏。

若“生成 route references”仍然等于维护两份正文，要求重新设计 source ownership。

### CW06-D06：最终产物绑定是否真实可执行

这是本轮最重要的反证点。

独立判断 skills-only 单入口能否在正常 ChatGPT Web 中做到：

```text
识别外部文档
-> 获取全文
-> 生成终审候选
-> 调用现有连接器写回
-> 回读最终文件
-> 再报告完成
```

必须区分：

- Skill 能指导宿主模型调用现有工具；
- Skill 本身拥有不可绕过的事务或发送前 Hook。

Proposal 只能承诺前者，除非平台提供更强证据。若正常入口不能可靠完成该链，Critic 应判断应当：

- 收窄 0.6 claim；
- 增加受控 App/MCP；
- 或先做批准的小型探针。

不得让 Codex 在实施阶段自行猜。

### CW06-D07：ChatGPT 与 Codex 双 exposure 是否合理

检查“ChatGPT 单入口、Codex 六 Skill 直达”是否：

- 符合两种 surface 的真实使用方式；
- 保持同一 canonical source；
- 不造成两个产品合同；
- 不破坏 Research Authoring、Presentations、统计和科研图等下游消费；
- 有充分 parity 和兼容性 gate。

### CW06-D08：Capability Gate Matrix 是否完整且不过重

逐项审查 `CW06-G1..G6`：

- 是否覆盖真实显式调用入口；
- 是否验证完整 Reader Guide，而不是只看聊天回复；
- 是否绑定同一最终候选；
- 是否保留保真、exact-only、短答、必要长答和其他路线；
- 是否有完整 source + final artifact 的独立定性审查；
- fresh case 是否真正冻结后才运行；
- 是否有重复 Gate 可以合并；
- 是否漏掉 overlay 删除旧 Skill、Personal Plugin identity 或外部写入权限边界；
- 是否错误把文件清单、route receipt 或 hash parity 当成最终质量。

### CW06-D09：版本、发布与维护看板是否正确

核对：

```text
writing-style 0.5 -> 0.6
personal wrapper 0.5.0 -> 0.6.0
repository eventual PATCH
Issue #13 reused
Project lifecycle returns to DOING during new design round
```

判断是否需要新 Issue，是否会错误关闭 #13 原有 downstream adaptation，是否必须保留 `Resolution commit` 为空。

### CW06-D10：是否已具备进入 execution-ready Plan 的条件

本轮 `PROCEED` 只表示架构方向可继续。Critic 必须列出下一版执行包还必须冻结的决定，例如：

- wrapper 构建脚本和 source ownership；
- exact old-file delete list；
- manifest capability；
- 无副作用包装探针；
- GitHub/Drive/本地文件各自的目标身份和回读方式；
- Web Gate 输入、预算、重试、停止条件；
- independent reviewer 可访问的 source/final artifact；
- release/restore 过程。

若这些关键决定本应现在就属于产品架构，而 Proposal 留给 Executor 猜，给 `REVISE`。

## 八、审查方向与复杂度

Critic 必须同时防止两种错误：

1. **过简**：再加几句提示词，却继续让显式插件调用只改善聊天回复而漏掉真正产物；
2. **过重**：因为一次失败就新增 MCP、数据库、状态机、后台服务或第二套写作系统。

不要因为已有方案投入很多就保留，也不要因为单入口听起来直观就免于反证。关键判断是：它是否是当前平台上阻止本次真实失败的最小可验证机制。

## 九、禁止事项

本轮 Critic 不得：

- 修改仓库；
- 修改 Issue #13 或 GitHub Project；
- 创建分支、Goal、Kickoff 或 Reviewed Handoff task；
- 更新 Personal Plugin；
- 修改 Project setting；
- 运行真实 Web Gate；
- 调用付费模型；
- 把 design `PROCEED` 写成 execution-ready `PASS`；
- 要求用户手工维护看板、Plugin ID、ZIP 或 source locator。

## 十、输出要求

第一屏先用自然中文说明：

- 结论；
- Planner 的归因哪些成立、哪些不成立；
- 单入口方向是否保留；
- 最大剩余风险；
- Planner 下一步。

然后给出稳定 finding ID。只阻塞真实风险，不阻塞普通不确定感。

最后必须输出：

```text
DECISION=PROCEED|REVISE
ROOT_CAUSE_ASSESSMENT=SUPPORTED|PARTIALLY_SUPPORTED|UNSUPPORTED
SINGLE_ENTRY_DECISION=ACCEPT|REVISE|REJECT
ARTIFACT_BINDING_DECISION=ACCEPT|REVISE|REJECT
GATE_MATRIX_DECISION=ACCEPT|REVISE
PROPOSAL_PATH=docs/design/clear-writing/CLEAR_WRITING_0_6_SINGLE_ENTRY_ARTIFACT_FINALIZATION_PROPOSAL_V0_1_2026-10-20.md
PROPOSAL_COMMIT=3eefc626b86566113125a06fc6046a2bec1eafb2
READY_FOR_CODEX=NO
NEXT_HANDOFF=PLANNER
```

若 `REVISE`，必须附一份可直接交回长期 Planner 的完整最小返修提示词，只处理本轮 finding，不重新设计已经通过的无关 Clear Writing 能力。

若 `PROCEED`，明确下一步只是 Planner 准备完整 execution-ready Plan、Goal 和 Gate execution package，再交同一独立 Critic 做最终执行前审查；不得启动 Codex。
