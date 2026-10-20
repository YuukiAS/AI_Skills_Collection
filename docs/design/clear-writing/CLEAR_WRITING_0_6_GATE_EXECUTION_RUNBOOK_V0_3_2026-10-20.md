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
