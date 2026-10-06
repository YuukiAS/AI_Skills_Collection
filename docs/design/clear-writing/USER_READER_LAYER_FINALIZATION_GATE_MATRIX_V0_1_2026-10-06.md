# 最终用户阅读层终审 Capability Gate Matrix

- Gate Matrix version: `v0.1`
- Date: `2026-10-06`
- Planner base main: `36e854fe06779400e2e1279083a34803c7c62a48`
- Companion Proposal: `USER_READER_LAYER_FINALIZATION_PROPOSAL_V0_1_2026-10-06.md`
- Companion Plan: `USER_READER_LAYER_FINALIZATION_PLAN_V0_1_2026-10-06.md`
- Tracking: `#13`
- Status: `DRAFT_FOR_CRITIC_REVIEW`
- Applies to: proposed Clear Writing bundled Skill `reader-layer-finalization`

## 0. Gate 原则

本矩阵验证的是普通用户是否真正获得跨 Project 的最终阅读层，不是 Skill 文件是否存在。

所有 Gate 服从以下规则：

1. **完整回答优先。** 必须审查首轮完整回答，不以单句、局部片段、字符串扫描、fixture、hash 或 self-check 代替。
2. **正常入口优先。** `@Clear Writing` 只用于诊断；正常入口必须在用户不提 Skill、不重复语言要求时成立。
3. **语义保真阻断。** 事实、数值、条件、权限、安全、证据强度、不确定性、时间、完成状态、精确标识或用户决定发生漂移，直接失败。
4. **不使用禁词或比例评分。** 普通英文是否应删除按语义角色判断，不按英文字符比例、固定词表或机械分数。
5. **不使用固定模板。** 自然结构按任务决定，不要求所有回答三段、固定标题或固定列表数。
6. **C5–C11 只算回归。** 它们不能标为 fresh；必须另有实现后才揭示的普通 Web holdout。
7. **错误表面不算。** Codex、hook、本地 source injection、直接读取 Skill 或外部 API PASS，不能替代 ChatGPT Web PASS。
8. **首答失败不能靠第二轮纠正洗白。** 用户必须再次说“用中文/别写英文/先说结论”即为当前正常入口失败。
9. **平台能力如实记录。** 不得声称存在独立第二次调用、发送前 hook 或确定 Skill 链，除非官方产品和实际运行证据同时成立。
10. **任何阻断性 Gate 失败即停止 release。** 不以更多 synthetic PASS 稀释真实失败。

---

## 1. Gate 总表

| Gate | 核心问题 | 必需证据 | PASS 标准 | 阻断性失败 |
|---|---|---|---|---|
| G0 表面与资格 | 目标 ChatGPT Web 账户/工作区是否真实支持候选 Skill/Plugin？ | 计划、工作区、表面、Plugin 目录可见性、权限和安装策略记录 | 测试表面明确；候选能力可安装/可见；限制已记录 | 实际表面不支持、只能在 Codex/桌面运行、或资格不明却继续声称 Web 可用 |
| G1 候选身份与安装 | 被测试的是否是 immutable candidate？ | source commit、generated package identity、Plugin version、Skill 清单、安装/升级和 fresh conversation 证据 | source、package、安装可见身份一致；新 Skill 可见 | 读取 source 代替安装、候选版本不明、旧缓存或错误 package |
| G2 直接激活诊断 | 新 Skill 本身能否完成职责？ | `@Clear Writing` / direct skill prompts、正例/负例/边界完整回答 | direct 调用能完成阅读层、保真和绕过；不越权 | direct 调用仍泄漏、漂移、误改机器输出或接管领域判断 |
| G3 正常入口触发 | 用户不提 Skill 时是否真实消费？ | Project 短桥、fresh chat、indirect/follow-up prompts、产品可见 activation evidence（若表面提供） | 第一条回答表现出完整终审；无需用户提醒；相近表达稳定 | 只有 `@` 才工作、短桥只被复述、或用户第二轮提醒后才正常 |
| G4 多领域完整回答 | 终审能否在真实复杂任务后仍执行？ | AI Research Stack、Server+VPS、CAT-TRACE、frontend/Figma/code 的完整回答 | 每个领域事实由领域能力保持，最终阅读层自然且一致 | 某领域因英文 source/log/Skill 重新退化，或终审改变专业语义 |
| G5 普通英文与来源框架 | 非必要英文、source label、内部阶段是否真正消失？ | 带英文 repo/paper/log/Planner/Critic 输入的完整回答 + 人工语义角色审查 | 普通概念自然本地化；内部标签不成为主叙述；必要原文最多附属一次 | 仍以 `candidate/validation/routing/...` 等普通来源词搭骨架，或靠词表替换造成误删 |
| G6 阅读结构 | 段落和信息顺序是否真正面向用户？ | 完整回答人工审查 | 先结论/动作，再必要证据；段落连续；列表有真实结构；无重复状态块和裸日志替代判断 | 机械换行、单字段成段、状态堆砌、内部审计先于用户结论、固定模板化 |
| G7 精确标识 | 中文化是否保留需要复制/执行/定位的字符串？ | 主机名、端口、路径、分支、提交、命令、字段、正式方法/产品名用例 | 所有受保护标识逐字一致；解释与机器内容分层 | 任一关键标识被翻译、缩写、改写、丢失或错误替换 |
| G8 语义保真 | 表达优化是否保持全部受保护语义？ | source/领域结论与 final answer 的命题级对照；反例集 | 事实、条件、强度、权限、安全、不确定性、时间、完成状态和用户决定无漂移 | “未完成→已完成”“可选→必须”“未知→确定”“拒绝→恢复”等任一漂移 |
| G9 语言模式与临时覆盖 | 中文、英文、双语和当前消息覆盖是否正确？ | 中文 Project、英文 Project、双语 Project、单轮英文覆盖及下一轮恢复 | 持久语言合同正确；临时覆盖只影响当前轮；不强制中文 | 英文 Project 被中文化、双语边界扩大、临时覆盖永久化或默认语言未恢复 |
| G10 机器输出与 should-not-change | 纯 JSON/log/code/quote 是否保持协议？ | JSON-only、raw-log-only、patch/code-only、逐字引用及混合输出 | 纯机器内容原样/按协议；混合任务只改解释层；不添加禁止内容 | 字段、顺序、代码、日志或引用被改；纯机器请求被加解释；不相关回答被过度终审 |
| G11 多轮与污染恢复 | 长会话、英文材料和机器轮次后是否持续生效？ | fresh→follow-up→大量英文输入→机器输出→再解释的多轮记录 | 后续解释仍自然；无需再次提醒；临时模式不污染 | 几轮后漂移、读完英文 source 后回退、机器轮次导致长期绕过 |
| G12 Fresh Web 综合验收 | 普通用户最终是否真正得到能力？ | 实现后才揭示的 holdout；普通 ChatGPT Web；无 `@`、无再次提醒；独立 Reviewer | 关键场景首答通过阅读层、保真、标识、语言和绕过；候选身份可追溯 | holdout 首答失败、evidence 不是普通 Web、Reviewer 只能靠第二轮修正或无法确认实际候选 |

---

## 2. G0 — 表面与资格

### 必查

- ChatGPT plan / workspace / region；
- ChatGPT Web 是否可见 Plugins 与候选 Clear Writing；
- Skills-only Plugin 是否可用；
- 用户/角色是否允许安装；
- 若使用工作区自动安装，策略是否真实为 `Installed`；
- 该表面是否提供 Skill/Plugin 消费的可见线索；若不提供，必须说明证据边界。

### PASS

测试报告明确写出真实表面和限制，候选可通过受支持入口安装与使用。

### FAIL

- 只在 Codex 或 ChatGPT Desktop 本地 marketplace 可用，却声称普通 Web 可用；
- 资格/权限不清楚；
- 依赖本地 hook/script；
- 依赖未授权的外部服务。

---

## 3. G1 — 候选身份与安装

### 必查

```text
SOURCE_COMMIT
PACKAGE_COMMIT / BUILD ID
PLUGIN_SLUG = writing-style
DISPLAY_NAME = Clear Writing
VISIBLE_PLUGIN_VERSION
VISIBLE_SKILL = reader-layer-finalization
INSTALL_OR_UPGRADE_RESULT
FRESH_CONVERSATION_BOUNDARY
```

### PASS

- candidate source 与安装包一致；
- generated snapshot 无漂移；
- ChatGPT Web 中能看到正确 Plugin/Skill；
- 安装或升级后新会话加载候选；
- 证据可回溯到 immutable commit。

### FAIL

- 直接把本地 `SKILL.md` 粘进 prompt；
- 旧版本缓存；
- package 中没有新 Skill；
- 只看文件 hash，不看安装后的产品身份。

---

## 4. G2 — 直接激活诊断

### 正例

- 用中文解释一段混有普通英文流程词、路径和结论的技术材料；
- 把状态字段堆叠的回答改成自然结论；
- 保留主机、端口和命令，中文解释其意义；
- 在英文 Project 中形成自然英文最终回答。

### 负例/边界

- 纯 JSON；
- 原样日志；
- 代码补丁；
- 严格逐字引用；
- 用户明确要求双语；
- 用户要求只输出一个命令。

### PASS

直接调用时，Skill 的能力与边界均成立。

### 注意

G2 只证明 Skill 可工作，不证明普通入口。G2 PASS、G3 FAIL 时，整体仍失败。

---

## 5. G3 — 正常入口触发

### 测试设置

- Clear Writing 已安装；
- Project 只有获批短激活桥，不附完整 Skill 文本；
- 用户 prompt 不出现 `Clear Writing`、Skill slug、“说中文”“最终润色”等提示；
- 从 fresh conversation 开始；
- 使用 direct、indirect、follow-up、near-miss 四类请求。

### PASS

- 第一条相关完整回答已经完成终审；
- follow-up 仍保持；
- near-miss / 纯机器任务不错误触发自然语言改写；
- 相近表达不会出现一条触发、一条完全失效的明显不一致；
- 不需要用户第二轮纠正。

### FAIL

- 模型在正文中说“我已应用终审”，但输出仍违反合同；
- 只有 explicit `@` 才能完成；
- Project 短桥被复述而未消费；
- 依赖把 Skill 全文粘到 prompt；
- normal-entry evidence 来自 Codex 或 Work，而非普通 ChatGPT Web。

---

## 6. G4 — 多领域完整回答

每个用例都必须包含足够复杂的英文 source/log/internal material，使终审在真实压力下执行，而不是只回答一句简单问题。

### A. AI Research Stack

检查：

- Planner/Critic/Gate/状态字段不直接主导正文；
- 用户先得到结论、动作与下一步；
- repo、commit、path 等必要定位保留；
- 不把内部 Proposal label 当用户正式术语。

### B. Server+VPS

检查：

- 主机名、端口、路径、服务和权限逐字保留；
- 当前状态、授权、主备关系不漂移；
- 日志被消化成判断，必要片段再附后；
- 不因中文自然弱化安全/恢复边界。

### C. CAT-TRACE

检查：

- 数学、符号、定理状态和统计结论保持；
- 普通方法解释自然中文；
- 正式方法/数据集名仅在必要时保留；
- “待证明/已证明”“假设/结论”不混淆。

### D. Frontend / Figma / code

检查：

- 组件、Figma 节点、文件、函数和代码标识准确；
- UI/逻辑判断使用自然目标语言；
- 英文设计标签不自动成为主叙述；
- 不把未实现写成已完成。

### PASS

四类完整回答均通过 G5–G10；不得只给摘要片段。

---

## 7. G5 — 普通英文与来源框架

### 审查方法

人工逐项判断每个保留英文是否承担以下至少一种真实职责：

- 正式产品/方法/数据集名称；
- 代码、命令、字段、配置或协议值；
- 路径、文件、分支、提交、主机、端口；
- 需要复制、搜索或唯一定位的原字符串；
- 用户明确要求保留的原文；
- 当前语言合同允许的双语组成。

若不承担这些职责，应说明为什么没有自然本地化。不能用“source 是英文”“这是技术词”“有产品语境”作笼统理由。

### 同时检查

- source heading / phase / mechanism / design label 是否被误当官方名称；
- `Planner/Critic/Gate/PASS/FAIL` 是否在非工作流任务中泄漏；
- 英文原词是否在首次附属定位后继续重复成为主叙述；
- 同一普通概念是否前后中英反复切换。

### 不允许

- 英文字符比例阈值；
- 固定禁词；
- 简单替换器；
- 只检查标题不检查列表、表格、总结和结论。

---

## 8. G6 — 阅读结构

### PASS 特征

- 用户首先看到实际结论；
- 需要操作时明确说是否要动作、下一步是什么；
- 证据紧随其后，而不是先复述内部审计过程；
- 一个自然段承担一个完整意思，不是一句一段；
- 数字/状态不单独成段，除非其确有独立视觉职责；
- 列表数量由真实结构决定；
- 机器块前后有必要解释；
- 同一结论不以多套状态字段重复；
- 长回答可以有标题，短回答不强行套模板。

### FAIL 特征

- `RESULT = ...`、`STATUS = ...`、`NEXT = ...` 连续堆叠代替正文；
- 原始日志直接作为主要判断；
- 每句话单独换行；
- 大量项目符号没有并列关系；
- 先讲 Planner/Critic 如何工作，再很晚才回答用户；
- 为显得“自然”删除必要证据或精确内容。

---

## 9. G7 — 精确标识

### 受保护样例类型

```text
YuukiAS/AI_Skills_Collection
planner/reader-layer-finalization-v0.1
36e854fe06779400e2e1279083a34803c7c62a48
docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md
g1807htzh01.ll.unc.edu
22081
CURRENT.json
reader-layer-finalization
```

实际测试应使用对应项目的真实或安全脱敏标识。

### PASS

- 需要保留的字符串逐字一致；
- 不必要的哈希/路径可以从主叙述移到证据层或删除，但不能误改；
- 第一次出现可用中文解释，原字符串仍可复制；
- 后文不把解释和标识混为一体。

### FAIL

- 翻译主机、路径、配置键或 slug；
- 截断造成无法定位；
- 把两个相似实体合并；
- 为减少英文删除用户需要执行的命令或字段；
- 保留大量无用标识冒充“精确”。

---

## 10. G8 — 语义保真

### 必查维度

1. **事实与数字**：数值、数量、版本、日期、比较对象。
2. **逻辑关系**：否定、条件、因果、充分/必要、例外。
3. **模态**：必须、应当、可以、可能、建议、禁止。
4. **权限与授权**：可读/可写、已授权/待授权、用户-only action。
5. **安全与隐私**：风险、确认、不可逆、敏感边界。
6. **证据与不确定性**：已证实、支持、推测、未知、未验证。
7. **时间与完成**：过去/当前/未来、已完成/部分完成/未开始。
8. **归因与主体**：用户决定、source author、Planner、assistant、外部 reviewer。
9. **用户决定**：接受、拒绝、删除、纠正、保留。
10. **精确标识**：G7 的 protected set。

### 反例必须覆盖

- `not validated` → `validated`；
- `optional` → `mandatory`；
- `may` → `will`；
- `read-only` → `can modify`；
- `user rejected` → default recommendation；
- `future work` → current completed work；
- `evidence supports` → certain cause；
- source author proposal → assistant directive；
- one machine identity → another similar identity；
- JSON exact field → natural-language alias。

### PASS

命题级对照无实质漂移；必要重排可发生，但每个 source obligation 都在最终回答中得到等价保留、明确省略理由或正确机器分层。

### FAIL

任一阻断维度改变。文字更顺不构成豁免。

---

## 11. G9 — 语言模式与覆盖

### 用例

1. 中文 Project + 英文来源；
2. 英文 Project + 中文来源；
3. 双语 Project；
4. 中文 Project 当前轮要求英文；
5. 英文覆盖后的下一轮普通中文请求；
6. 当前轮要求只保留英文正式术语；
7. 当前轮要求翻译，而非改写。

### PASS

- Project 持久合同是默认；
- 当前消息明确要求优先；
- 当前覆盖不写回长期设置；
- 下一轮恢复持久合同；
- 不把英文 Project 强制中文化；
- 双语边界由用户/Project 决定，不由 Skill 扩张。

---

## 12. G10 — 机器输出与 should-not-change

### 纯机器用例

- JSON-only；
- YAML/config；
- shell command only；
- code patch；
- raw log exact copy；
- CSV/table schema；
- error message exact quote；
- literal translation with alignment requirements。

### 混合用例

- 先中文结论，再给命令；
- 解释日志后附必要原文；
- 说明配置含义，但配置块原样；
- 解释代码缺陷，但 patch 不改格式。

### PASS

- 纯机器请求不加额外自然语言；
- 机器结构、字段、顺序、引号和语法不被终审改坏；
- 混合任务只优化解释层；
- should-not-change 的简短自然回答不会被强行扩展。

### FAIL

- 为了“自然”修改机器块；
- 在 JSON-only 前后加解释；
- 把原始错误字符串翻译掉；
- 对用户只要一句结论时输出完整审计模板。

---

## 13. G11 — 多轮稳定性

### 场景链

```text
1. fresh 普通领域问题
2. follow-up 要求进一步解释
3. 读取大量英文 repo/paper/log
4. 要求纯 JSON 或命令
5. 再问一个普通中文判断
6. 当前轮临时要求英文
7. 下一轮恢复默认语言
```

### PASS

- 1、2、3、5、7 保持最终阅读层；
- 4 正确绕过；
- 6 只对当前轮切换；
- 不需要用户再次提醒；
- 不因长上下文重新采用 source headings 和状态字段。

### FAIL

- 后半段明显退化；
- 一次绕过后永久不再终审；
- 临时英文污染下一轮；
- 读取英文材料后普通英文重新充斥主叙述；
- 模型开始输出内部自检状态。

---

## 14. G12 — Fresh ordinary ChatGPT Web 综合验收

### Fresh 要求

- holdout 在 implementation contract 冻结后才揭示；
- 不复用 C5–C11 原文；
- 不由实现者针对性调过；
- 使用普通 ChatGPT Web；
- Clear Writing 从候选安装路径加载；
- Project 只含获批短桥和其正常领域规则；
- 用户 prompt 不提 Skill、不重复语言要求；
- 第一条完整回答即送审。

### Holdout 至少包含

- 一个混合英文 repo + Planner/Critic 文档的复杂中文判断；
- 一个 Server+VPS 精确身份/权限/状态任务；
- 一个带公式、结论强度和待验证状态的统计任务；
- 一个 Figma/代码身份与用户决策混合任务；
- 一个英文 Project；
- 一个双语或临时覆盖；
- 一个纯机器输出边界；
- 一个不应触发重度终审的简单自然回答。

### 独立 Reviewer 必答

1. 用户是否第一眼得到结论？
2. 普通来源英文是否已被消化？
3. 内部阶段/状态/日志是否仍主导正文？
4. 段落和列表是否自然？
5. 所有精确标识是否正确？
6. 事实、条件、权限、安全、证据、不确定性、时间和完成状态是否保真？
7. 当前语言与覆盖是否正确？
8. 机器-only 是否未被改坏？
9. 是否确为普通 Web normal entry，而非 `@`、source injection 或第二轮提醒？
10. 是否有足够证据确认测试的是 immutable candidate？

### PASS

全部阻断维度通过；个别纯偏好差异可记录为非阻断改进，但不能掩盖重复性机器味、触发失败或语义漂移。

### FAIL

任一核心 holdout 首答出现：

- normal-entry 未触发；
- C11 类普通英文/状态框架泄漏；
- 语义/标识漂移；
- 语言模式错误；
- 机器协议破坏；
- 候选身份或表面无法确认。

---

## 15. Evidence Pack

实现审查包至少包含：

```text
00_SCOPE_AND_IDENTITIES.md
01_OFFICIAL_PRODUCT_CAPABILITY_CHECK.md
02_SOURCE_AND_PACKAGE_IDENTITY.md
03_INSTALL_AND_FRESH_SESSION.md
04_DIRECT_DIAGNOSTICS.md
05_NORMAL_ENTRY_FULL_ANSWERS/
06_PROTECTED_SEMANTICS_COMPARISON.md
07_LANGUAGE_AND_OVERRIDE_CASES.md
08_MACHINE_ONLY_AND_SHOULD_NOT_CHANGE.md
09_MULTI_TURN_STABILITY.md
10_FRESH_WEB_HOLDOUT.md
11_INDEPENDENT_REVIEW.md
12_VERSION_CHANGELOG_AND_ROLLBACK.md
```

每个完整回答证据必须记录：

- Project/语言模式；
- prompt；
- 必要输入来源；
- candidate identity；
- 是否 explicit mention；
- 是否用户第二轮纠正；
- 完整回答；
- 受保护语义对照；
- Reviewer 结论；
- 隐私处理说明。

不得只保存“PASS”摘要。

---

## 16. Fresh / Regression / Diagnostic 分类

| 分类 | 可用内容 | 可以证明什么 | 不能证明什么 |
|---|---|---|---|
| Regression | C5–C11、已有 Clear Writing failures | 已知失败是否复现 | fresh generalization、普通 Web 首答稳定性 |
| Diagnostic | direct `@`、source-level tests、local install | Skill/packaging 基本可用 | normal-entry 产品可用 |
| Fresh | 实现后揭示的新完整任务 | 未针对性调参的泛化 | 长期跨版本稳定性 |
| Real-use | 实际 Project 正常工作 | 用户正常入口价值 | 所有未来 Project 自动保证 |

所有最终声明必须注明证据类别。

---

## 17. Gate 结果格式

最终 Reviewer 必须输出：

```text
REVIEW_RESULT = PASS | REVISE
REVIEWED_COMMIT = <immutable candidate commit>
PLUGIN_IDENTITY = writing-style / Clear Writing / <version>
SURFACE = <exact ChatGPT Web plan/workspace>
NORMAL_ENTRY = PASS | FAIL
SEMANTIC_FIDELITY = PASS | FAIL
EXACT_IDENTITIES = PASS | FAIL
READER_LAYER_QUALITY = PASS | FAIL
LANGUAGE_MODES = PASS | FAIL
MACHINE_BYPASS = PASS | FAIL
MULTI_TURN = PASS | FAIL
FRESH_WEB_HOLDOUT = PASS | FAIL
INDEPENDENT_SECOND_CALL_CLAIMED = NO
CHAT_WEB_HOOK_CLAIMED = NO
RELEASE_RECOMMENDATION = YES | NO
BLOCKERS = <truthful list>
```

`PASS` 只允许在所有阻断项通过时给出。`REVISE` 不自动创建 successor task，不自动启动 Executor，也不允许用新的 prompt-only patch 继续旧循环。

---

## 18. 当前 Planner 判定

```text
GATE_MATRIX_STATUS = READY_FOR_INDEPENDENT_CRITIC_REVIEW
CURRENT_PRODUCTION_GATE = NOT_RUN
CURRENT_WEB_ACCEPTANCE = NOT_RUN
C5_C11_CLASSIFICATION = REGRESSION_ONLY
DIRECT_MENTION_CAN_PROVE_NORMAL_ENTRY = NO
STATIC_TESTS_CAN_PROVE_PRODUCT = NO
SEMANTIC_FIDELITY_BLOCKING = YES
MACHINE_BYPASS_BLOCKING = YES
FRESH_ORDINARY_WEB_BLOCKING = YES
```
