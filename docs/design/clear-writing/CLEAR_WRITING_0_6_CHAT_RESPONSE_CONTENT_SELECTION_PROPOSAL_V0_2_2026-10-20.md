# Clear Writing 0.6：普通聊天内容选择修订 Proposal v0.2

日期：2026-10-20  
状态：DRAFT_FOR_INDEPENDENT_CRITIC  
任务：`clear-writing--single-entry-artifact-finalization`  
分支：`design/clear-writing--single-entry-artifact-finalization`  
跟踪：Issue `#13`  
原批准 Proposal：`CLEAR_WRITING_0_6_SINGLE_ENTRY_ARTIFACT_FINALIZATION_PROPOSAL_V0_1_2026-10-20.md@3eefc626b86566113125a06fc6046a2bec1eafb2`  
原 execution-ready package：`d7b810d194ead881303aaca9c2e4f1d59a97c1f1`  
旧实现候选：`079bd7987bb33d624d244feb415327d5cf2343d8`  
新增真实回归输入：`results/clear-writing--single-entry-artifact-finalization/CHAT_RESPONSE_CONTENT_SELECTION_PLANNER_INTAKE_2026-10-20.md@2b4d74bd5acfafbb4473f669d80a3a48cd53b8c5`

## 1. Planner 判断

本次不是新版本、新任务或新产品架构；单入口、六项 canonical writing capability、Codex direct exposure、GitHub 外部文档 finalization 和 G1-G6 总体结构都保留。

但本次 **确实修改了原冻结 0.6 的 user-visible product behavior**：旧 wrapper 只负责识别 `CHAT_RESPONSE` 并把它路由给 `response-clarity`；新版要求 wrapper 在路由前先确定“用户真正要读什么”，把技术分析的 evidence pool 与 reader-facing answer content 分开，再把已经选定的内容交给现有 route 组织语言和保护事实。

因此：

- 旧 execution-ready PASS 不再覆盖新语义；
- `079bd798...` 仍是有价值的历史实现/证据基线，但不再是可安装的 0.6 release candidate；
- 正式 Personal Plugin 继续保持 0.5.0；
- 必须在同一 task 内形成新版 Plan / Goal / Runbook / Kickoff，并交原独立 Critic复核后才能重新实施。

## 2. 真实缺陷发生在哪里

Bridge Kit 0.11.1 完成汇报是已证明的 production regression：

- 用户显式选择 Clear Writing；
- 生成前实际读取了 installed `response-clarity` 与 `writing-fidelity`；
- 最终答复仍膨胀成 24 个编号章节、1128 行，并把大量“为了证明结论而调查到的内部实现/审计事实”直接变成用户正文。

现有 `response-clarity` 已经要求：结论先行、减少内部流程噪声、完整答案做碎片检查、核心问题回答后停止。因此问题不能再归因为“缺少少用列表/少写英文/不要日志”这些规则。

更符合证据的缺口是：

> **在语言组织之前，没有先把“分析需要知道的全部事实”与“本轮用户需要阅读的内容”分开。**

这发生在 `CHAT_RESPONSE` 的任务分解和内容纳入阶段，早于 `response-clarity` 的自然表达。

## 3. 三种修复路线比较

### A. 只修改 `response-clarity`

不选。

原因：

1. 当前 route 已经有停止条件、内部噪声清理、结论先行和整篇结构检查；
2. 本次 production trace 已证明该 route 内容进入生成上下文后仍可能失败；
3. 再把“证据池不是正文”塞进 canonical `response-clarity`，会扩大 Codex/direct-skill 等所有 consumer 的语义面，且重复 wrapper 已经拥有的 deliverable decomposition 职责；
4. 它仍然是在“准备如何表达”阶段补救，而不是先决定“哪些内容应进入回答”。

### B. 只增加末尾 whole-response 自检

不作为主修复；保留为第二道检查。

原因：如果草稿一开始就围绕审计清单、被否决架构和内部状态组织，末尾一句“删掉没价值的内容”仍可能只做表面压缩，而且无法明确保护用户真正要求的深入技术内容。

### C. 在唯一 `clear-writing` 入口的 `CHAT_RESPONSE` 分解阶段做 reader-value selection

采用。

原因：

- wrapper 已经负责识别交付对象、来源、受众和 route；
- 它是现有架构中最早能看到“用户问题 + deliverable type + detail request”的位置；
- 它可以在不改变领域结论的前提下决定哪些**已建立事实**需要出现在 reader-facing answer；
- 然后再把选定内容交给 `response-clarity`，并在需要时由 `writing-fidelity` 保护其中的事实、限制和机器字符串；
- 不需要新增 MCP/App/model/service/hook/state machine。

这不是“研究证据选择”。统计、科研、产品和工程 domain owner 仍决定什么事实和证据支持结论；Clear Writing 只决定这些已经成立的内容中，哪些对当前读者问题有展示价值。

## 4. 新的最小机制：CHAT_RESPONSE_READER_VALUE_SELECTION_V1

只加入 `packaging/chatgpt/writing-style/clear-writing/SKILL.md` 的 `CHAT_RESPONSE` 路径。

### 4.1 先冻结本轮 answer contract

在写正文前，私下确定：

- 用户实际问了哪些问题；
- 回答类型：解释 / 完成汇报 / 诊断 / 受阻报告 / 决策 / 深入技术说明；
- 用户明确要求的详细程度；
- 用户真正需要的交付物；
- 是否存在必须给出的行动或下一接收方。

分析范围、repo audit范围、搜索结果数量不能自动扩大 answer contract。

### 4.2 evidence pool 与 user-facing content 分离

领域分析可以完整读取代码、日志、测试、设计稿、Gate、历史方案和被否决替代。

一项信息默认只有满足至少一个条件才进入普通聊天正文：

1. 直接回答用户某个问题；
2. 是理解主要机制、正常使用或关键因果链所必需；
3. 会实质改变用户对“是否完成 / 是否可信 / 风险多大”的判断；
4. 是必须保留的限制、不确定性、权限或失败边界；
5. 是用户下一步操作、复现或交接所必需；
6. 用户明确要求深入解释这项技术细节、推导、实现或审计证据。

若以上均不成立，信息留在内部 evidence pool，不默认进入正文。

尤其不因为“调查过”而自动展示：

- 被否决架构的完整清单；
- 重复的“没有 X / 没有 Y / 没有 Z”；
- 测试设施、审查流程和内部角色流水账；
- 多个证明同一结论、但不会继续改变可信度的证据；
- 仅用于定位实现、对当前用户判断没有增量的内部路径/状态。

这是语义筛选，不是禁词表，也没有固定长度、标题数或英文比例。

### 4.3 详细不等于审计倾倒

用户说“详细讲”时，应扩展：

- 功能是什么；
- 主要机制怎样工作；
- 正常怎么使用；
- 为什么可以相信结论；
- 真正的限制、风险和剩余项；
- 用户点名要求的技术细节。

“详细”不自动授权把所有审查记录、否决路线、文件清单和内部过程全部展开。

用户明确要算法、公式、证明、参数、实现细节或复现步骤时，这些内容本身具有 reader value，必须保留足够深度。

### 4.4 route 顺序

对 `CHAT_RESPONSE`：

```text
user request
-> CHAT_RESPONSE_READER_VALUE_SELECTION_V1
-> selected reader-facing content
-> response-clarity
-> writing-fidelity when selected content has protected meaning
-> whole-response reader-value check
-> final answer
```

`writing-fidelity` 保护“已进入 answer contract 的事实和精确内容”，不把 evidence pool 中所有背景事实升级成强制展示项。

### 4.5 最终 whole-response check

发送前的同一模型工作流必须重新检查完整答复：

- 原问题每一项是否已经回答；
- 用户要求的深度是否足够；
- 是否遗漏会改变结论、可信度、风险或行动的重要限制；
- 是否存在无法说明 reader value 的展开；
- 是否把内部审计过程误写成用户下一步；
- 若任务需要唯一下一接收方，是否已经直接给出。

这是 Skill instruction，不是平台级发送前 Hook。0.6 的正式 claim 只能是“在显式调用的正常入口中提高内容选择与整篇组织的可靠性”，不能声称不可绕过。

## 5. 保留的原 0.6 产品能力

完全保留：

- ChatGPT Personal Plugin 唯一顶层 `clear-writing` Skill；
- 六项 canonical source：
  - writing-fidelity
  - response-clarity
  - product-ui-copy
  - scientific-prose
  - scientific-rewrite
  - chinese-prose
- Codex Marketplace 六项 direct exposure；
- 正式中文文档、长技术材料重写、英文科研、产品界面文案与 exact-only/mixed 路线；
- GitHub UTF-8 text file 的 full read -> candidate -> expected-blob write -> readback；
- source/generated parity；
- 原有权限、保真、版本、README/changelog和Issue #13边界；
- G3 Reader Guide；
- fresh G6；
- `GPT-5.6 Sol`、explicit Clear Writing selection、one-answer / infra-only retry规则。

不新增 MCP、App、外部模型、后台服务、数据库、持久 ledger 或第二套 router。

## 6. 对旧候选和 Phase C 的影响

### 6.1 旧候选失效范围

`079bd798...` 的 wrapper 没有本 Proposal 的 reader-value selection，因此：

```text
079bd798... = HISTORICAL_IMPLEMENTATION_BASELINE
NOT_RELEASE_CANDIDATE_FOR_REVISED_0_6
```

旧 local replay、CI、implementation review 仍可作为“旧能力没有被破坏”的历史证据，但不能证明新版聊天内容选择。

### 6.2 archive compatibility

Plugin Creator 真实 0.5 archive 为 tar.gz，而旧 `prepare-restore` 只读 ZIP，这是同一 task 的 bounded implementation bug。

它不需要新架构，但不能与本次 wrapper revision 并行冻结不同 candidate。下一次获批实施时，把：

- wrapper content-selection change；
- safe ZIP/tar.gz archive reader repair；

放进同一 implementation candidate。任何已经单独完成但尚未集成的 archive patch只能作为待移植 diff，不能成为独立 release candidate。

### 6.3 Phase C execution responsibility

保留 `CLEAR_WRITING_0_6_PHASE_C_EXECUTION_RECOVERY_AMENDMENT_V0_1_2026-10-20.md` 的核心结论并纳入新版 Plan：

- archive/materialization + Plugin Creator mutation 和 fresh Web gate 不要求同一工具 surface；
- mutation owner必须在更新前证明真实0.5 archive bytes可取得、restore可生成；
- fresh Web G1-B/G2/G3仍是真正 ChatGPT Web正常入口；
- 当前没有模型工具能代用户自动创建新的 ChatGPT Web conversation并点选模型/插件时，这部分属于最小 user-only UI action；
- user只执行 UI动作，不负责设计 prompt、判断 PASS、拼证据或决定恢复。

## 7. 验收修订：不新增顶层 Gate

继续使用 `CW06-G1..G6`。

只修改 G2 的普通聊天覆盖方式：

- G1-B继续承担简单 ordinary-chat smoke；
- G2-T1 改为 Bridge Kit 0.11.1 **已知**复杂完成汇报回归；
- G2-T9 改为本次 Phase C **已知**受阻/交接回归；
- G2-T8继续作为“真正需要深度”的反向保护；
- G2-T2..T7保持原 route覆盖。

这样不新增顶层 Gate，也不靠增加一串同类回归制造通过感。

### Bridge known regression

真实 source冻结为：

```text
repo = YuukiAS/GPT_Codex_AI_Bridge_Kit
ref = ba9013b9fbbd242e51b09f9d09291f417df17652
files = README.md, QUICKSTART.md, CHANGELOG.md, AGENTS.md
```

用户 prompt只要求详细了解：

- 是否完成/可用；
- 主要架构；
- 0.11.1新增能力；
- 正常怎样使用；
- 为什么可信；
- 真正未完成项。

PASS 不是“越短越好”，而是完整回答这些问题，同时不自动复制对结论无增量的内部审计和排除清单。

### Phase C known regression

真实 source冻结为：

```text
repo = YuukiAS/AI_Skills_Collection
ref = 38a81dc1df9a362ecee4be597cb3db5bd6fcac41
path = results/clear-writing--single-entry-artifact-finalization/phase-c/PHASE_C_STOP_BEFORE_LIVE_MUTATION.md
```

回答必须说明：实际状态、阻塞根因、责任/下一接收方、用户是否需要动作；如果下一接收方需要提示词，直接给完整 prompt。不能只抛内部状态让用户自己找入口。

### 深度保护

G2-T8继续验证：数学/科研/工程解释在用户明确要求详细时，公式、对象层级、条件、推导直觉、重要限制必须保留。任何“为了内容筛选而机械缩短”均 FAIL。

G4仍对 G2 + G3 做 fidelity；G6仍是原 fresh长技术文档，不改成聊天样本。

## 8. 当前正式状态

- Personal Plugin：仍为 `0.5.0`、USER / PRIVATE；
- live mutation：NO；
- G1-G6：未运行；
- Issue #13：open / DOING；
- central writing-style 正式版本：0.5；
- 0.6 version direction：保持 `0.5 -> 0.6`，不另开0.7；
- repository release：成功时仍为 execution-time late-bound PATCH；
- #73/#49 downstream adaptation truth保持 pending。

本 Proposal 只改变同一0.6的 CHAT_RESPONSE行为和执行协调；不授权实现。
