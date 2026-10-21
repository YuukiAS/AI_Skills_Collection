# Clear Writing 0.6 Gate 执行手册 v0.3

日期：2026-10-20  
状态：DRAFT_PENDING_EXECUTION_READY_CRITIC  
任务：`clear-writing--single-entry-artifact-finalization`  
产品修订：`CLEAR_WRITING_0_6_CHAT_RESPONSE_CONTENT_SELECTION_PROPOSAL_V0_2_2026-10-20.md`  
执行计划：`CLEAR_WRITING_0_6_EXECUTION_READY_PLAN_V0_3_2026-10-20.md`

本手册在Critic PASS前不得执行 live mutation或正式 Web Gate。

## 1. 阶段顺序

固定顺序：

1. Codex implementation：wrapper content selection + archive ZIP/tar.gz repair。
2. cheap deterministic tests + known regression + should-not-change。
3. required CI。
4. independent implementation review。
5. freeze new final candidate。
6. Phase C-A preflight：真实0.5 archive materialization + restore bundle。
7. update existing Personal Plugin to 0.6.0。
8. G1-A Plugin Creator readback。
9. G1-B。
10. G2。
11. G3。
12. G4。
13. G5。
14. 原独立Critic `PROCEED_TO_FINAL_EVALUATION / REVISE`。
15. Critic冻结唯一fresh G6。
16. G6 + final aggregate review。
17. release closure。

任一关键失败不得跳过继续。

## 2. implementation前置

实现必须显式使用：

`workflow-core + ai-skills-core + writing-style`

允许修改路径以Plan v0.3为准。

### archive tests

必须真实构造gzip-compressed tar，不得只改扩展名。

至少证明：

- ZIP baseline restore PASS；
- tar.gz baseline restore PASS；
-两个格式得到相同restore payload/delete sets；
- tar traversal / symlink / hardlink / duplicate / device/fifo FAIL；
- unexpected 0.5 file set FAIL。

### wrapper semantic tests

不以关键词/字数作oracle。至少检查生成package确实包含新 `CHAT_RESPONSE_READER_VALUE_SELECTION_V1` contract，且：

- route table仍指向原六项route；
- canonical route bytes/parity仍按approved transform；
- exact-only/mixed contract未变；
- GitHub external-finalization contract未变。

## 3. known local replay

本地开发回放目的只是在cheap阶段找明显退化，不能替代Web。

Bridge completion、Phase C handoff、necessary-long-answer三类必须完整读取prompt/source并审完整输出。

PASS criteria与Web相同，但只标 `LOCAL_DEVELOPMENT_EVIDENCE`。

## 4. final candidate freeze

implementation review PASS后生成：

`results/clear-writing--single-entry-artifact-finalization/candidate/FINAL_CANDIDATE.json`

schema版本更新为：

`CLEAR_WRITING_06_FINAL_CANDIDATE_V2`

至少包含：

- source commit；
- writing_style_version = 0.6；
- personal_wrapper_version = 0.6.0；
- wrapper_archive_sha256；
- build_receipt_sha256；
- `CHAT_RESPONSE_READER_VALUE_SELECTION_V1`；
- `CW06_ROUTE_PROJECTION_V1`；
- `CW06_DETERMINISTIC_ZIP_V1`；
- archive reader compatibility identity；
- codex/profile identity；
- gate_rule_version = `CW06-v0.3`。

候选冻结后production source不得变化。

## 5. Phase C-A preflight

在任何live mutation前必须真实完成：

### A1 live identity

```text
writing-style = 0.5.0
scope = USER
discoverability = PRIVATE
same existing plugin identity
```

保存current release ID和complete file list。

### A2 account archive bytes

调用 Plugin Creator导出current 0.5 archive，并**真实把archive bytes落到可供approved builder消费的host/local file**。

只拿到URL/metadata不算PASS。

### A3 candidate bytes

重建new frozen 0.6.0 archive，验证size/hash == FINAL_CANDIDATE。

### A4 restore preparation

用真实0.5 archive bytes + new candidate执行approved `prepare-restore`，生成：

- forward restore 0.6.1 archive；
- `RESTORE_06_ONLY_PATHS.json`；
- `RESTORE_DELETE_PATHS.json`。

### A5 update transport

必须证明当前执行surface能把new 0.6 archive作为host-uploaded archive传给 `update_plugin`。

A2-A5任一未证明：

`STOP_BEFORE_LIVE_MUTATION`

正式0.5.0保持，不算产品Gate失败。

## 6. update existing Personal Plugin

只有Phase C-A全部PASS后：

- same plugin identity；
- expected_release_id = A1 readback；
- exact forward update delete_paths；
-不创建第二个writing-style。

更新后完整Plugin Creator readback。

## 7. CW06-G1

### G1-A

必须确认：

- version = 0.6.0；
- USER / PRIVATE；
- same plugin identity；
- dual manifest；
- package唯一top-level Skill = `clear-writing`；
-旧六top-level Skill不存在；
- route/support hashes与candidate一致。

### G1-B

真正fresh ChatGPT Web：

- `GPT-5.6 Sol`
- explicit Clear Writing
- one answer
- infra-only max one retry

exact prompt沿用v0.2：

```text
我刚跑完测试。先告诉我现在能不能交给审阅者、还缺什么；保留下面三个机器字符串不改：
branch=reviewed/cache--repair
status=WAITING_FOR_RESTORE_CHECK
command=python -m unittest tests.test_cache
```

PASS：先说人话，状态准确，机器字符串精确，不要求用户选内部route。

## 8. CW06-G2

所有任务：

- fresh ChatGPT Web conversation；
- `GPT-5.6 Sol`；
- explicit Clear Writing；
- one answer；
-只有没有产生模型答案的基础设施故障可同输入重试一次；
- product fail不reroll。

### T1 — Bridge Kit 0.11.1 completion known regression

source：

```text
repo = YuukiAS/GPT_Codex_AI_Bridge_Kit
ref = ba9013b9fbbd242e51b09f9d09291f417df17652
files:
README.md
QUICKSTART.md
CHANGELOG.md
AGENTS.md
```

exact prompt：

```text
请先完整读取下面四个文件，然后详细告诉我 Bridge Kit 0.11.1 现在到底是不是可以正常用了：

repo = YuukiAS/GPT_Codex_AI_Bridge_Kit
ref = ba9013b9fbbd242e51b09f9d09291f417df17652
files = README.md, QUICKSTART.md, CHANGELOG.md, AGENTS.md

我需要知道：
- 现在主要架构到底是什么；
- 0.11.1 相比前面实际增加或修了什么；
- 我平时到底怎么用；
- 为什么你认为这版已经完成或还没完成；
- 还有哪些真正没做。

请详细解释，但按我真正需要理解的内容组织。
```

Reviewer必须看到四份source +完整final response。

PASS重点：

-回答五个用户问题；
- detail充分；
- “为什么可信”使用必要证据但不变成审计ledger；
-内部被否决架构、daemon/database/state-machine等只在会改变用户理解时出现；
-不隐藏真实未完成项。

### T2-T7

完整沿用v0.2冻结prompt/判据：

- Chinese formal Markdown；
- long Chinese structural rewrite；
- English scientific prose；
- UI copy；
- exact-only；
- mixed content。

### T8 — necessary long answer

沿用v0.2 exact prompt：

```text
在一个多站点传感器研究里，s 表示站点，j 表示站点内传感器，t 表示时间。x_{s,j,t} 是观测值，mhat_{s,t} 是估计背景，d_{s,j,t}=x_{s,j,t}-mhat_{s,t}，a_{s,j,t}=d_{s,j,t}/vhat_{s,t}。请详细解释对象层级、三个下标、为什么先得到 d 再得到 a，以及 a 后面怎样用于比较或异常筛查。先建立直觉再讲公式；不要为了简短删掉必要解释。vhat 只被描述为“一个估计尺度量”，不要猜它具体是什么。
```

PASS：必要深度、公式关系、index角色、下游用途和“不猜vhat”全部保留。

### T9 — Phase C blocked handoff known regression

source：

```text
repo = YuukiAS/AI_Skills_Collection
ref = 38a81dc1df9a362ecee4be597cb3db5bd6fcac41
path = results/clear-writing--single-entry-artifact-finalization/phase-c/PHASE_C_STOP_BEFORE_LIVE_MUTATION.md
```

exact prompt：

```text
请读取下面这份 Clear Writing 0.6 Phase C 停止报告，然后直接告诉我：

1. 实际发生了什么；
2. 为什么会停；
3. 下一步唯一应该由谁接手；
4. 我现在要不要做什么；
5. 如果需要交给下一线程，直接给我完整可复制的提示词。

repo = YuukiAS/AI_Skills_Collection
ref = 38a81dc1df9a362ecee4be597cb3db5bd6fcac41
path = results/clear-writing--single-entry-artifact-finalization/phase-c/PHASE_C_STOP_BEFORE_LIVE_MUTATION.md
```

PASS：

-实际状态和原因清楚；
-唯一下一owner清楚；
-用户动作最小且明确；
-需要时附完整handoff；
-不把内部状态矩阵和路径堆成正文。

## 9. Web Gate user-only UI packet

如果执行时仍没有自动控制fresh ChatGPT Web conversation的合法工具，Planner在live mutation前生成：

`results/clear-writing--single-entry-artifact-finalization/web-gates/WEB_GATE_USER_PACKET.md`

它必须包含：

- final candidate identity；
- current Personal Plugin release identity；
-每个G1-B/G2/G3 exact prompt；
-明确“用户只执行UI动作，不判分”；
-每个response的原样粘贴位置。

用户动作只允许：

1. 新建fresh chat；
2.选择 `GPT-5.6 Sol`；
3.显式选择 Clear Writing；
4.发送对应exact prompt；
5.把完整assistant response原样交回Planner。

Planner负责source读取、判分、evidence归档和restore decision。

## 10. CW06-G3

Reader Guide合同完全沿用v0.2：

- exact source commit/path；
- dedicated Gate branch；
- full read；
- full candidate；
- pre-write blob recheck；
- expected-blob update；
- full readback；
- candidate equality；
-完整artifact review。

chat清楚不能替代document PASS。

## 11. CW06-G4

pre-G6 fidelity gate，输入：

- G2 T1-T9完整input/source/output；
- G3 source/final。

检查事实、数字、公式、版本、引用、状态、权限、限制、exact identifiers。

Bridge/Phase C T1/T9要特别检查：reader-value selection不得通过删除真实限制、失败状态或剩余项换取“清爽”。

## 12. CW06-G5

保持v0.2：

- source/generated parity；
- single-entry Personal package；
- Codex six direct routes；
- `codex-writing-style` profile；
- downstream ownership boundary；
- required tests/CI。

hash只证明parity，不证明聊天质量。

## 13. final-evaluation preflight and G6

G1-G5全PASS后停止。

原独立Critic读取完整evidence和同一candidate，给：

`PROCEED_TO_FINAL_EVALUATION` 或 `REVISE`。

只有PROCEED后才按原v0.2 fresh G6协议选择exactly one新的长技术文档。

Bridge和Phase C不得作为G6 fresh。

## 14. failure / restore

live mutation前失败：

-不restore；
- 0.5.0保持；
-准确记录infra vs product。

live mutation后terminal product fail或bounded infra path耗尽：

-停止后续Gate；
- Phase C-A owner执行已准备的0.6.1 forward restore；
- central0.6不发布。

用户不负责restore。

## 15. evidence standard

任何聊天质量PASS都必须保存：

- exact prompt；
- source identity；
- final candidate/release identity；
-完整assistant response；
- independent qualitative verdict。

禁止：

-字符数阈值；
-标题数阈值；
-英文比例；
-禁词表；
-只看第一屏；
-只看Skill load receipt；
-只看local replay。

## 16. 2026-10-21 绑定的正常使用补充验收（G1–G6不扩顶层）

### G2-T8-A：CAT-TRACE理解路径的真实科研解释

单独fresh ChatGPT Web会话，型号`GPT-5.6 Sol`，用户显式选择正式Clear Writing、使用本候选release，一次模型答案；仅无模型答案的基础设施故障可原输入重试一次。私有来源：

```text
repo=YuukiAS/CAT-TRACE
ref=0d829fb17c458a076a15ec51893e917960107c21
path=docs/model/catalog_aware/CAT_TRACE_ZERO_SLOT_SECTION_5_READER_EXPLANATION_20261021.md
```

冻结的自然用户提示词：

```text
请通过已连接的GitHub读取这个文件的完整正文，再解释给一个尚未理解这部分推导的研究生：

repo = YuukiAS/CAT-TRACE
ref = 0d829fb17c458a076a15ec51893e917960107c21
path = docs/model/catalog_aware/CAT_TRACE_ZERO_SLOT_SECTION_5_READER_EXPLANATION_20261021.md

我想弄明白：既然最大值分布已经知道，为什么还要求分位数？为什么再引入一个标准正态变量？这些步骤到底使后续积分容易在哪里？请用必要的具体概率或调查地点例子让我先建立直觉，再讲清每个符号、公式关系和适用假设；保留分位数求根的计算成本、数值误差与尚未证明的效率结论。不要只复述原文标题，更不要为了简短删掉解释。
```

独立评审看源全文、提示词和最终聊天全文，判断是否真正解释了“为什么要这样做”、变量与数学关系、条件限制和计算代价；不能错误宣传从n维积分降到一维，也不能把辅助变量当生态新参数。CAT是已见正向参照，不是fresh G6，不因机械出现公式/例子就PASS。私有原文与涉及研究细节的完整输出仅放在权限匹配、独立Reviewer实际可读的受限位置；如果审查者取不到全文，停止而非将全文发到公开仓库。

### G2-T8-B：保持原v0.3 T8必要长答

v0.3 `T8 — necessary long answer` 中多站点传感器的**冻结原始提示词和判据完全保留**，作为T8-B另一条正常Web输出；两条各有一次尝试，不混合答案，不新增顶层Gate。G2-T1 Bridge工程回归及T9 Phase C交接回归不变；原24章节全文缺失的证据边界不能靠这次同类新问题掩盖。

### G3-A：原Reader Guide完整编辑与双交付

原v0.3第10节及v0.2冻结`10.1-10.3`的源提交、Gate分支、目标路径和原提示词不变。必须实际完整读取→正确的长技术文件保真/结构重写/中文终审路线→**写前有完整候选并分别完成事实和读者质量检查**→原expected-blob写入→全文回读一致；独立Reviewer实际核对原始用户问题、源全文、候选全文、仓库最终全文与聊天全文。仅hash相符但文档不可读或聊天仍为审计报告，G3-A FAIL。

### G3-B：同一GitHub受控分支的新文件非覆盖创建

仅在G3-A真实PASS后运行；使用同一个正式0.6插件release、一个新的显式选择Clear Writing的Web会话，不另增G7。固定来源仍为Reader Guide原始文件 `YuukiAS/AI_Research_Toolkit@0ff0f43f3b04286273490e4c4870975f4aa7a7f8`。目标仅限：

```text
repo=YuukiAS/AI_Research_Toolkit
branch=gate/clear-writing-0.6-reader-guide-regression
path=docs/research/software-production/16_THREE_RUN_SYNTHESIS_AND_DELIVERY_ASSURANCE_20261015/CW06_NEW_READER_INTRO.md
```

正式运行前必须确认目标文件不存在，branch就是已批准的G3测试分支；存在即`G3_PRECONDITION_BLOCKED`，不得覆盖、换名、强推或另建新分支。

冻结提示词：

```text
请先通过已连接的GitHub读取以下原始Reader Guide全文，再根据这份真实材料在我指定的测试分支创建一份全新的中文入门说明：

repo = YuukiAS/AI_Research_Toolkit
source_ref = 0ff0f43f3b04286273490e4c4870975f4aa7a7f8
source_path = docs/research/software-production/16_THREE_RUN_SYNTHESIS_AND_DELIVERY_ASSURANCE_20261015/DELIVERY_ASSURANCE_V0_4_READER_GUIDE_20261019.md
target_branch = gate/clear-writing-0.6-reader-guide-regression
target_path = docs/research/software-production/16_THREE_RUN_SYNTHESIS_AND_DELIVERY_ASSURANCE_20261015/CW06_NEW_READER_INTRO.md

这份新文件面向第一次了解这个方案的普通研发读者。请独立讲清楚它解决什么问题、正常怎么使用、主要机制是什么、当前真正完成了什么、还缺什么。不要修改原文件，也不能编造功能或用内部审计流水充正文。

写入前必须形成整篇终审候选，并检查内容保真和中文读者质量；写前再次确认目标不存在及分支没有意外漂移。只使用非覆盖的GitHub创建文件操作。写入后重新读取同一文件全文，确认就是被审查过的候选。聊天里另用自然中文说明创建内容和实际验证状态。
```

核对实际`create_file`、写前目标不存在、写前分支HEAD和创建提交parent一致、目标repo/branch/path、写前完整候选与最终仓库全文逐字一致。由于普通`create_file`没有自动提供branch HEAD比较并替代审阅的事务承诺，若目标身份意外漂移/无法核对/创建被拒绝，必须停止并报告未验证；不能谎称原编辑Gate证明了新建能力。独立Reviewer还必须判定新文件完整正文与聊天完整回复各自的真实性、连贯性和读者价值。

G3只有A与B两个子任务都合格才PASS；G4保真输入须包含G2-T8-A/B及G3-A/B各自的完整source/candidate/final。字节一致和文本质量分别审核；长中文正式文件绝不使用CHAT_RESPONSE精简逻辑删除必要源信息。

### 失败、费用、候选与最终可信声明

所有新增子任务仍使用同一候选、同一model、每项一次产品答案、基础设施无答案最多一次同输入重试、产品失败不reroll。它们不是fresh G6；G6仍待G1-G5真实PASS后由原Critic冻结。保存来源身份、完整答案及完整文稿的独立定性审查；私有研究输出不得未经授权写到公开证据路径。任一聊天或文件严重退化、漏证据/重要限制、GitHub写前候选未全文审校或回读失败，相关G2/G3 FAIL，按原Phase C恢复，中央0.6不得发布。质量声明只能绑定已经观察到的实际运行，不以一次成功声称长期故障率已足够低。

## 17. 2026-10-22 原G2不扩样本的跨领域解释检验

不新增Gate、不增加Web答复轮次、不修改原冻结提示词。用户已提供同一Bridge 0.11.1汇报的两版文本：第一版虽然包含大量事实，但主要以功能和审计证据排列；第二版在用户要求参考CAT并提供进一步反馈后，把仓库/工作树启动前检查、进度估算、重复运行等问题转成“如果发生什么、为什么危险、现在怎样预防、具体改善什么”的问答推进。这只能作为**已知的用户反馈对照**，不证明读取CAT是唯一改变因素；第二版自身仍有冗余，不是通过标准的全文模板。

**G2-T1 原样保留**：源仍为 `YuukiAS/GPT_Codex_AI_Bridge_Kit@ba9013b9fbbd242e51b09f9d09291f417df17652` 的README/QUICKSTART/CHANGELOG/AGENTS，exact Web prompt不提CAT。这个没有参考提醒的正常入口，是检验`clear-writing`能否把通用解释方式自带进回答的关键反证。独立Reviewer须查看完整提问、四份必要来源、最终答复全文，回答：

1. 能否不看源仓库，仅通过答复理解“Bridge完成什么、Lite/Review/Control如何选择、Persistent/进度/ETA/通知/恢复分别解决什么、是否仍有Program Run等限制”；
2. 遇到抽象的工作机制时，是否至少在最重要的机制上清晰给出**发生什么问题→现在怎样工作→为什么对用户有价值→可信证据/适用边界**，而不是孤立列功能名和测试数；
3. 哪些状态/架构否定项、审计输入仍没有改变用户判断，却被展开为章节或表格；
4. 是否保持详细说明所要求的真实复杂度，不把“像CAT”简化成例子堆砌、机械分段或缩短字数。

判定是语义质量：**不能规定至少几个例子、几个问答段、多少字、多少标题**。一条优秀机制解释不能掩盖整篇审计倾倒；事实不准确也不能靠文笔补救。无正常Web完整答复前，不得把新增示范记为产品通过。

**G2-T8-A/B**仍分别检查科研理解链和充分长答，防止仅学会工程状态汇报；T9仍须直接给真正下一责任方与提示词。G3双交付文档质量验收仍由独立全文审阅，不要求正式GitHub长文机械套用普通聊天示例；原G4/G5/G6、同一最终候选/插件身份、一次产品答复及仅基础设施无输出可重试的限制完全不变。
