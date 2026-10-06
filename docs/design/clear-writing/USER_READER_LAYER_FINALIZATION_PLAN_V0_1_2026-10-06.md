# 最终用户阅读层终审 Plan

- Plan version: `v0.1`
- Date: `2026-10-06`
- Planner base main: `36e854fe06779400e2e1279083a34803c7c62a48`
- Companion Proposal: `USER_READER_LAYER_FINALIZATION_PROPOSAL_V0_1_2026-10-06.md`
- Companion Gate Matrix: `USER_READER_LAYER_FINALIZATION_GATE_MATRIX_V0_1_2026-10-06.md`
- Tracking: `#13`
- Status: `DRAFT_EXECUTION_PLAN_REQUIRES_CRITIC_PASS`
- Production authorization: `NO`

## 0. 执行前提

本 Plan 只有在独立 Critic 对同一版本 Proposal、Plan 和 Gate Matrix 给出 `PASS` 后，才能转化为 Executor Goal。当前轮次不得：

- 修改 live `writing-style` Plugin；
- 修改 PIE 或创建 C12；
- 创建 Executor；
- 启动 paid API、外部模型服务、Workspace Agent、MCP finalizer 或 automation；
- 修改任何真实 ChatGPT Project instructions；
- 发布、合并或 bump 版本。

Critic 若对 owner、正常入口、平台边界或验收方法有实质异议，应返回 `REVISE`，而不是让实现阶段试错决定架构。

---

## 1. 实现目标

在现有 Clear Writing（`writing-style`）中新增一个 bundled Skill：

```text
reader-layer-finalization
```

它在领域判断已经形成后，负责把普通聊天的最终可见解释重写为符合当前语言合同、自然、低机器味、结构清楚且语义保真的回答。

实现完成后，普通用户应能在已安装 Clear Writing、Project 已配置短激活桥的 ChatGPT Web 中直接提出领域问题，第一条回答就完成最终阅读层，不需要再追加：

- “说中文”；
- “不要英文”；
- “不要状态块”；
- “先说结论”；
- `@Clear Writing`。

该目标是可重复的高可靠行为，不声称平台级 100% 强制执行。

---

## 2. 冻结职责边界

### 2.1 新 Skill 负责

- 选择当前回复的目标语言与输出模式；
- 把普通来源英文、内部标签和日志框架转化为自然目标语言；
- 组织结论、动作、证据和机器细节的先后；
- 合并机械碎片和重复状态；
- 将精确机器内容与解释正文分层；
- 保留受保护语义；
- 在发送前核对是否发生事实、条件、权限、状态或标识漂移；
- 对纯机器输出、逐字内容和临时语言覆盖正确绕过或切换。

### 2.2 新 Skill 不负责

- 新事实研究或事实核查；
- 修改领域结论；
- 判断模型、定理、网络、权限、代码或设计本身是否正确；
- 创建引用、补证据或增强结论；
- 决定用户是否授权执行；
- 生成或修改 Project 长期设置；
- 调用另一个 Skill 作为必需运行步骤；
- 通过外部模型产生第二次重写。

### 2.3 其他能力保持

- `chinese-prose` 继续拥有中文文档/段落的具体成稿方法；
- `writing-fidelity` 继续拥有广义内容保真原则；
- `scientific-rewrite` 继续负责既有长文的结构化重写；
- Research Authoring、统计、前端、Server+VPS 等领域能力继续拥有其专业语义；
- PIE 不是本次实现范围，只可能在后续 bounded adaptation 中消费短激活桥。

---

## 3. 生产源设计

### 3.1 新目录

建议 canonical source：

```text
skills/writing/core/reader-layer-finalization/
├── SKILL.md
├── references/
│   ├── activation-and-language-modes.md
│   ├── protected-semantics-and-exact-identities.md
│   └── full-answer-counterexamples.md
└── evals/
    └── cases.json
```

实现者可以按仓库当前生成体系调整辅助文件名，但不得改变以下原则：

- `SKILL.md` 是被 ChatGPT 加载后的完整运行入口；
- references 只承载需要展开的边界和反例，不建立新的运行状态机；
- evals 是回归输入，不是关键词评分器；
- canonical source 仍在 `skills/writing/core/`，generated Plugin snapshot 不反向成为 source of truth。

### 3.2 `SKILL.md` 必须包含的最小合同

#### A. 触发条件

在以下情况使用：

- 当前 Project / Custom Instructions 明确要求最终阅读层、自然中文、读者可见终审或 Clear Writing 最后处理；
- 用户要求解释、总结、判断、报告、答复、计划、审查结论等面向读者的完整输出；
- 领域任务读取了英文来源、日志、内部文档，最终回答需要转化为读者语言；
- 用户明确调用 Clear Writing 进行最后终审。

以下情况不得机械触发或必须进入绕过模式：

- 纯 JSON / YAML / CSV / XML；
- 纯代码、补丁、命令或原始日志；
- 逐字引用、严格转录或用户要求原样输出；
- 当前请求只要求机器可消费格式；
- 任务已经由更窄的受保护输出协议规定不得增加解释。

#### B. 优先级

目标语言和输出模式按以下顺序解析：

```text
当前消息的明确要求
> 当前 Project 的持久语言/输出合同
> 当前会话中仍有效的明确约定
> 用户/工作区默认偏好
```

当前消息的临时覆盖只影响当前回复，不写回长期设置。

#### C. 受保护语义

发送前必须保持：

- 事实、数字、公式、引用；
- 否定、比较、因果和条件；
- 结论强度与证据强度；
- 不确定性、未知和限制；
- 必须/可选、允许/禁止、授权/未授权；
- 安全、隐私和权限；
- 当前/过去/未来、已完成/未完成；
- 用户纠正、删除、拒绝、接受；
- 需要复制、执行、搜索或唯一定位的精确标识。

不得为了“说人话”补出新事实、删掉关键限制或把历史/来源意见改成当前决定。

#### D. 阅读层实现

- 先回答用户真正需要的结论、是否需要动作和下一步；
- 普通概念使用当前目标语言，不因来源英文而保留；
- 来源标题、阶段和内部字段只在用户任务本身讨论它们时出现；
- 段落按信息结构，而不是按字段或每句话换行；
- 列表只用于真正并列或步骤；
- 同一结论不以多个状态块重复；
- 裸日志、路径、哈希和内部审计不能代替已经消化的判断；
- 必要机器内容单独放在代码块、表格或紧凑清单中，并在正文说明其意义；
- 不使用固定段数、固定模板、禁词表或英文比例。

#### E. 精确字符串

保留与翻译的判断依据是语义角色，不是字符类型。以下在需要时原样保留：

- 仓库、分支、提交、路径和文件名；
- 命令、代码、配置键、枚举和协议值；
- 端口、主机名、设备名和服务名；
- 正式产品、方法、模型、数据集和标准名称；
- 用户需要复制、执行、搜索或唯一定位的原字符串。

同一个英文词若只是普通解释或内部流程用语，应自然本地化；若既需解释又需定位，可在首次出现时用目标语言为主、原字符串附属一次，后文不再让英文成为主叙述。

#### F. 最后核对

在发送前内部核对：

- 是否仍有无读者价值的来源英文或内部标签；
- 是否有机械换行、单字段成段或重复状态；
- 是否先给了用户结论；
- 是否把机器内容和解释分层；
- 是否改变了任何受保护语义；
- 是否错误地永久化了临时语言要求；
- 是否错误地改写了机器输出。

该核对不得在最终回答中输出成 `PASS/FAIL` 状态块，也不得声称存在独立第二次模型调用。

### 3.3 与现有 Skills 的复用方式

禁止实现为运行时 Skill 链。允许的复用方式：

- 从 `chinese-prose` 和 `writing-fidelity` 提炼必要的中央规则；
- 使用共享 reference 或生成检查保持同义合同一致；
- 在源码注释、设计文档和测试中记录来源；
- 若出现冲突，以新 Skill 对“普通聊天最终回答”的窄职责为准，不反向改变长文/产品文案等既有入口。

实现者不得为了消除少量重复而引入新的动态依赖、注册中心、Skill orchestrator 或 schema。

---

## 4. Plugin 打包与路由

### 4.1 打包

将 canonical source 通过仓库现有生成路线打包到：

```text
plugins/codex/plugins/writing-style/skills/reader-layer-finalization/
```

同时更新中央 Marketplace 配置中的 Skill 清单/Plugin 描述（若生成体系需要），确保：

- source 与 generated snapshot 一致；
- Plugin 仍名为 Clear Writing；
- slug 仍为 `writing-style`；
- 不创建 alias Plugin；
- 不引入 MCP、hook、脚本服务或新连接；
- 候选安装后能在 ChatGPT Web Plugin 详情中看到新 Skill。

### 4.2 metadata 路由

Skill description 必须围绕用户目标和上下文触发，不得写成无边界“每次回答都必须使用我”。建议语义：

> 在当前 Project 或用户偏好要求最终阅读层时，用于对已经形成的用户可见解释做最后语言与结构终审；保留事实、权限、证据强度和精确标识，并对纯机器输出或当前语言覆盖正确绕过。

需要通过 direct、indirect、follow-up、negative、boundary prompts 调整 metadata。不得以一个 direct `@` 成功证明正常路由。

### 4.3 短激活桥

候选包中提供一个 canonical Project bridge reference，不自动修改真实 Project：

```text
发送面向用户的解释性正文前，必须实际使用已安装的 Clear Writing `reader-layer-finalization`，按本 Project 当前语言合同完成最后阅读层；本条消息明确要求其他语言、双语或纯机器内容时，仅对本次切换或跳过。该终审只改表达和信息组织，不改事实、数值、条件、权限、安全、证据强度、不确定性、完成状态、时间关系或精确标识。未消费即未完成。
```

实现阶段只有在用户另行授权 Project setup/acceptance 后，才可把短桥写入试点 Project。不得把它扩写成 C11 的长 baseline。

### 4.4 Project 外兜底

提供一份不超过短桥复杂度的 Custom Instructions 建议，供普通非 Project 聊天使用。必须明确：

- Project instructions 会覆盖全局设置；
- 全局设置不是跨 Project 强制层；
- 未安装/未触发 Skill 时不能声称实际消费。

---

## 5. 测试与证据路线

### 5.1 静态与生成测试

至少保护：

- 新 Skill frontmatter、名称、描述和目录合法；
- canonical source 能生成 Plugin snapshot；
- source/snapshot 无漂移；
- Plugin 仍为单一 `writing-style` identity；
- 不新增 MCP、hooks、外部连接或 API key 要求；
- references/evals 完整进入候选包；
- 短激活桥没有被复制到多个独立 source；
- 版本与 changelog 在 release closure 前后符合政策。

静态测试不能宣称产品通过。

### 5.2 内容回归测试

开发/回归输入至少覆盖：

- C5–C11 代表性失败；
- 普通英文技术词与来源标签；
- Planner/Critic/验收字段泄漏；
- 状态块、机械换行和裸日志；
- 精确路径、哈希、端口、主机名；
- 已完成/未完成、必须/可选、允许/禁止；
- 用户已拒绝/删除的决定；
- 临时英文与双语覆盖；
- JSON/log/code-only 绕过。

C5–C11 只作为回归集，不得标为 fresh。

### 5.3 候选安装

按正式 Plugin 路径构建候选：

1. 从 immutable implementation commit 生成候选；
2. 安装/升级到明确测试账户或工作区；
3. 记录可见 Plugin version、Skill 清单和候选 commit；
4. 重新开始 fresh ChatGPT Web conversation；
5. 不从 source path 直接读取 Skill 代替安装；
6. 不用 Codex hook 或本地脚本冒充 Web 行为。

### 5.4 直接激活诊断

先用 `@Clear Writing` 验证：

- candidate identity 正确；
- Skill 可见且能被直接调用；
- 受保护语义与绕过模式基本工作。

该阶段仅诊断，不计 normal-entry PASS。

### 5.5 正常入口验收

在不提 Skill、不说“说中文”、不要求“最终润色”的情况下，使用真实领域问题验收：

- AI Research Stack；
- Server+VPS；
- CAT-TRACE；
- frontend/Figma/code；
- 英文 Project；
- 双语 Project；
- 当前消息英文覆盖；
- 纯机器输出。

每个高风险入口至少跨两个 fresh conversations 验证，另保留一组实现后才揭示的 holdout。通过标准看完整回答和受保护语义，不看单句或关键词比例。

### 5.6 多轮稳定性

必须测试：

- 第一轮正常触发；
- 读取大量英文 repo/log 后仍触发；
- follow-up 不退回内部状态腔；
- 临时英文覆盖后下一轮恢复 Project 默认；
- 机器输出轮次后下一次解释仍正常；
- 长会话中不需要用户重新提醒。

### 5.7 独立审查

独立 Reviewer 必须同时做：

- 阅读层审查：自然语言、结构、结论顺序、内部泄漏；
- 语义保真审查：事实、条件、权限、证据、不确定性、时间、精确标识；
- 产品入口审查：是否真实从普通 ChatGPT Web 自动消费，而不是 direct mention 或 source injection；
- 平台边界审查：没有伪称 hook、Skill 链或第二次调用。

Reviewer 不得只检查 Skill 文件或本地测试。

---

## 6. Gate 执行顺序

推荐顺序：

```text
G0 版本与表面资格
-> G1 安装和 candidate identity
-> G2 direct activation diagnostics
-> G3 normal-entry activation
-> G4 跨领域完整回答
-> G5 普通英文/来源框架/结构清理
-> G6 精确标识保留
-> G7 语义保真
-> G8 语言与临时覆盖
-> G9 机器输出与 should-not-change
-> G10 多轮稳定性
-> G11 fresh ordinary Web holdout
-> G12 独立综合审查与 release closure
```

任何高风险 Gate 失败都停止 release；不得用更多 synthetic cases 冲淡真实失败。

---

## 7. 计划阶段

### Phase 0 — Critic 冻结

输入：本 v0.1 Proposal / Plan / Gate Matrix。

输出：

- `PASS`：架构进入可执行状态；
- `REVISE`：返回 Planner；
- 不允许 Critic 直接修改 Proposal 或启动实现。

### Phase 1 — Canonical Skill source

- 创建新 Skill 与 references/evals；
- 建立语言模式、受保护语义、精确标识、结构和绕过合同；
- 加入真实反例；
- 不改 Plugin version；
- 运行静态/内容测试。

停止条件：职责与现有 Skills 冲突，或需要动态 Skill 链才能成立。

### Phase 2 — Plugin packaging

- 将 Skill 纳入 Clear Writing generated package；
- 更新必要 metadata 与生成测试；
- 不添加 MCP/hooks；
- 生成 immutable candidate。

停止条件：Plugin identity 分裂、Web 表面不可见、或需要额外服务。

### Phase 3 — Local and installed diagnostics

- direct mention；
- negative/boundary；
- candidate identity；
- source/snapshot consistency。

停止条件：安装不加载正确 Skill、机器输出被误改、或基本保真失败。

### Phase 4 — Authorized Project bridge trial

只有用户另行授权后：

- 在专门验收 Project 或获批真实 Project 中写入短桥；
- 不改其他 Project 规则；
- 记录 before/after；
- 验证 Project 外 Custom Instructions 仅为兜底。

停止条件：必须复制长模板、短桥仍不产生真实路由、或 Project 规则冲突。

### Phase 5 — Real ChatGPT Web acceptance

- 执行 Gate Matrix 的跨项目完整回答；
- 每个回答首轮验收；
- 收集实际 Plugin/Skill consumption evidence（以产品表面能提供的可见证据为准）；
- 不允许第二轮提醒后才计 PASS。

停止条件：normal-entry 系统性漏触发、C11 类失败复现、语义漂移或错误中文化。

### Phase 6 — Independent review

- 独立 Critic/Reviewer 读取 candidate、完整回答和受保护语义对照；
- 按 Gate Matrix 给出 PASS/REVISE；
- 把平台随机性和偶发失败如实归因，不以“多数时候可以”掩盖关键入口失败。

### Phase 7 — Version and release closure

仅在所有 Gate PASS 且用户批准发布后：

- 按当前 canonical 版本决定下一两段 Plugin version；
- 更新 `docs/plugin-changelogs/writing-style.md`；
- 更新 Marketplace config 和 generated manifest；
- 决定 repository release bump；
- 完成安装/升级/fresh-session replay；
- 发布与合并仍是单独批准动作。

### Phase 8 — Optional downstream adaptation

核心能力成立后，才可另开 bounded adaptation 评估：

- PIE 在创建/整理 Project instructions 时自动保留短激活桥；
- 新 Project setup 如何一次性配置；
- 哪些现有 Project 需要迁移。

此阶段不得命名为 C12，不得重新打开 C11，不得把 PIE 变回能力 owner。本 Plan 不创建 successor task。

---

## 8. 失败归因

| 失败 | 主要归因 |
|---|---|
| Skill 未安装/候选身份错误 | packaging / distribution |
| 已安装但 indirect prompt 不触发 | metadata / activation architecture |
| 短桥存在但仍未消费 | platform/routing limitation 或 activation defect |
| 触发后仍泄漏普通英文与状态块 | Skill product defect |
| 语言自然但事实、权限、状态漂移 | fidelity defect，阻断 |
| exact identifiers 被翻译或改写 | exact-identity defect，阻断 |
| 英文/双语 Project 被强制中文 | language-mode defect，阻断 |
| JSON/log-only 被添加解释或改字段 | bypass defect，阻断 |
| direct `@` 通过、normal entry 失败 | product entry failure，不得降级为 PASS |
| hooks/Codex 通过、普通 Chat Web 失败 | wrong-surface evidence |
| fixture PASS、完整回答失败 | evaluation defect + product defect |

不得把所有失败都归为“模型随机性”。若关键入口需要用户反复提醒，产品目标未成立。

---

## 9. 安全、隐私与权限

- 终审 Skill 不新增外部数据传输；
- 不新增 MCP、远程服务或账户连接；
- 不把 Project 内容发送给第三方；
- 不放宽工具写入、授权或确认要求；
- 不因压缩表达而省略安全、隐私、权限和不可逆操作边界；
- 日志/路径清理不得删除用户完成诊断或复现所必需的信息；
- 真实验收材料若含私人仓库、账户、主机或网络信息，证据包必须按现有隐私规则最小化暴露。

---

## 10. 回退方案

若候选失败：

1. 停止发布；
2. 禁用/卸载候选，恢复上一正式 Clear Writing；
3. 从试点 Project 删除短激活桥，保留原语言规则；
4. 保留失败完整回答作为新证据；
5. 回到 Planner 判断是 metadata、产品表面、同轮限制还是 Skill 合同问题；
6. 不恢复旧 MCP/API finalizer；
7. 不追加临时关键词清单；
8. 不以 direct mention 模式替代 normal-entry 完成声明。

---

## 11. 跟踪生命周期

当前复用 tracking Issue `#13`。

本 v0.1 设计形成后，Issue 应进入 `DOING`，当前执行锚点指向 immutable Proposal/Plan/Gate Matrix commit，下一步为独立 Critic review。若当前表面不能修改 GitHub Project，必须记录待同步动作：

```text
Project: AI Skills Maintenance
Issue: #13
Status: TODO -> DOING
Area: writing-style
Current anchor: v0.1 reader-layer-finalization design package
Next action: independent Critic review
```

Critic PASS 不自动变更为 DONE。若核心 Plugin 已完成、但获批的实际 Project consumers 仍待适配，可按维护看板规则进入 `ADAPTING`；required consumers 必须当时基于正式产品合同冻结，不能事后无限扩大。

---

## 12. 版本决定

本设计轮次：

```text
Repository bump decision: NONE
Affected plugins:
- writing-style: NO_BUMP
- all others: NO_BUMP
```

后续 implementation/release 只有在真实 Web Gate、独立 review、version/changelog closure 全部完成后，才允许 bump exactly once。当前 Plan 不预先发布版本。

---

## 13. Execution-ready 判定

只有 Critic 明确确认以下项目，Plan 才可转为 Executor Goal：

- `PRIMARY_OWNER = writing-style / Clear Writing`
- `NEW_BUNDLED_SKILL = reader-layer-finalization`
- `NO_RUNTIME_SKILL_CHAIN_DEPENDENCY`
- `NO_CHAT_WEB_FINAL_HOOK_CLAIM`
- `NO_INDEPENDENT_SECOND_CALL_CLAIM`
- `PROJECT_BRIDGE_IS_ROUTING_DEFENSE_NOT_PRIMARY_CAPABILITY`
- `REAL_CHATGPT_WEB_COMPLETE_ANSWER_GATE_REQUIRED`
- `SEMANTIC_FIDELITY_IS_BLOCKING`
- `MACHINE_ONLY_BYPASS_IS_BLOCKING`
- `NO_PAID_API_OR_HOSTING`
- `NO_PIE_C12`

未满足时不得开始 production code。
