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

## 9. 2026-10-21 最终用户验收承诺：聊天理解与仓库终稿分开闭环

本节是本次用户补充并入同一0.6的正式语义，优先于前文仅关注CHAT_RESPONSE的较窄叙述；保留原单入口、六项专业route、GitHub-only外部范围、G1-G6和版本方向。现实正反证据对照见 `results/clear-writing--single-entry-artifact-finalization/CAT_TRACE_BRIDGE_READER_VALUE_COMPARISON_20261021.md`。

**聊天**：在进入`response-clarity`之前先识别当前问题及读者理解缺口、确定需要回答的结论/功能/机制/可信证据/限制/下一步，再决定必要实例与数学/技术深度。CAT-TRACE展示的是从具体调查情景、概率和变量作用逐步走到公式与限制，而不是固定标题或缩字数；第7节首次解释未闭合、第二次针对追问纠正，说明对复杂问题要保留准确的补充能力。只给执行状态时不造教学例子；用户要求完整推导/复现时不能以“内部细节”删除必要内容。

**GitHub文件**：同一请求中的GitHub UTF-8文本文件是独立于聊天的交付目标。依据文件是既有文稿润色、长技术结构改写或新建，根据完整源文/授权资料选六项既有路线；写入前必须形成**全文候选**并分别检查事实/条件/权限保真和整稿读者质量，禁止用局部差异、内部审计输出或聊天摘要代替。写入后回读同一路径全文，核对与候选一致，并对实际最终全文做独立定性评审。字节一致只证明身份，不能证明文稿可读。写前无法确认内容合格则不写；写后仍发现质量不合格时报告未通过，不能宣称终稿完成。

本轮用户同时要求**创建或修改**GitHub文件。原0.6主要冻结已有文件的`update_file`；新增的创建必须在同一个GitHub-only范围内预检查路径不存在、绑定授权分支/路径及写前分支头、使用非覆盖`create_file`，核对创建提交的父提交与写前头一致、再完整回读。该工具链尚未被正常Web验证，不能假装旧G3-A自动证明新建；因此同一G3增加一次G3-B非覆盖创建子任务，原Reader Guide G3-A完全保留。任何创建相关工具前置不成立则停止且G3不通过，不能静默收窄发布承诺。

两类交付必须在**同一用户请求**中都合格：聊天说清楚不能替代文稿，文件写入成功不能替代聊天，任一失败不得给双目标完成声明。纯技能合同不是平台发送前强制拦截，实际可信度只能来自同一候选正常Web调用的完整回答、完整文件、写前候选、写后回读与独立质量评审；现阶段只冻结待检验的因果机制，不得声称已证明稳定性。

正式完成时用户必须得到五个可用证据回答：聊天为什么更有机会说人话、文件为什么实经全文终审、CAT-TRACE理解链怎样进入机制、Bridge同类失败是否在实际Web重放中克服及样本限制、若失败由哪个原任务owner负责修复与是否需用户动作。不得用“测试数增加”替代其中任何一项。

## 10. 2026-10-22 最小补强：把读者价值筛选接到真实的解释组织

2026-10-22 用户提交了**同一 Bridge Kit 完成汇报的两版完整用户可见答复**。第一版已经包含正确的功能、门槛、测试和状态，但主要按组件/审计结果罗列，用户仍需要自己推断“这些机制为什么必要”。第二版在用户明确要求参考 CAT-TRACE 后，以“如果站错工作树会怎样”“旧进度为什么不该直接估ETA”“原进程是否可能仍活着，为什么不能重跑”等读者疑问组织材料，把风险情景、工作机制、用户后果、可信证据衔接起来，用户明确评价改善。

这证明了**可观察的组织方式改善**，但不是严格的因果实验：第二次同时有用户批评、明确参考CAT及追问重写，因此不能单独归因为“读CAT”或自动证明未来调用成功。第二版仍存在不少分节、重复的最终结论和可下沉实现细节，不能照抄其长度或版式。

现行修订已经解决“**讲什么**”：CHAT_RESPONSE先从用户提问中挑选读者有必要知道的事实；但“**怎样让读者顺着理解**”在文档里主要落在陌生科研解释段，对工程完成汇报尚无同样明确且可被普通入口消费的因果组织步骤。仅把CAT列为测试样本，不意味着正常使用无需再手动“参考CAT”就能表现良好。

**本次新增最小修改**：在唯一包装源码 `packaging/chatgpt/writing-style/clear-writing/SKILL.md` 的 `CHAT_RESPONSE` 路线里，把读者内容选择与一个简短的**读者疑问衔接**结合，且提供**一组极短、已脱敏的“部件清单式说明→问题—机制—后果式说明”对照示范**，直接位于会被加载的总入口，不另建可发现Skill，也不另拷六项专业写作规则。总入口仅规划本次读者需要理解的逻辑依赖；工程/科学事实仍由当前任务的领域所有者决定，语言句段仍交 `response-clarity`，正式文档的 Reader Plan 仍由 `scientific-rewrite` 负责。

工作顺序按任务自适应，而非固定模板：

1. 当前任务若仅要求状态、行动或精确输出，直接给结论和必要证据，不制造故事或分节。
2. 若用户要求“是什么、为什么、怎么用、凭什么可信”，私下列出需要连起来的实际读者疑问；对**每个真正需要解释的机制**，找出其针对的原问题/失败方式，选择足以帮助读者看懂的具体情景或对比，再说明机制怎样改变结果、关键证据及局限。不是要求每个技术名词都讲一遍。
3. 对陌生数学对象，必要时先用已知或明确标注假设的数字、变量层级和可检验比较建立直觉，再进入符号与公式、条件、后续推断；要保留足够深度和复现信息。
4. 形成完整答复时检查：用户问题是否被逐一回答、有没有读者要自己补的因果跳跃、有没有一整段只是说明“我审过很多东西”、有没有机械复制正例的标题结构或具体数字。

**短示范内容冻结（仅供包装入口内部对照，不是用户输出模板）**：

- 无效式：“实现了锁、最新文件读取、原子写入；没有第二数据库、后台监控和新调度器。”
- 有效式：“两个程序如果都拿旧版本改同一份文件，后写的就可能覆盖先写的。现在每次更新都先锁住并读取最新版，只改自己负责的内容后再原子写回。这降低了并发覆盖风险，但并不能单独证明整个项目已经通过验收。”

此示范仅是通用、公开且不含私有CAT研究数据的**理解推进对照**。实际用户问题并非文件并发时不能强行复用它，也不能机械生成“过去问题—方案—限制”的固定三段式。模型可按真实用户需要组织自然连续段落；标题多少、总字数和具体举例数量都不作机械判据。

预期因果作用是让显式选择Clear Writing后被加载的**同一入口**先处理内容与读者问题之间的对应关系，再调用六项已有专业路线；这比继续给`response-clarity`加“少写英文/少列表”规则更直接地针对已证实的内容选择与因果跳跃失败。但纯Skill仍由模型执行，这只是一条**待正常Web检验的增益假设**，没有强制发送前拦截保证。正式G2-T1 Bridge提示词中**不要求“参考CAT”**，正是为了核对这套简短示范能否在用户普通显式调用时迁移到工程叙述。
