# Clear Writing 0.6：读者问题因果解释迁移的最终执行前独立复核 v0.6

你继续担任原Clear Writing 0.6任务的独立Critic，不新建任务/版本，不实施。本轮是**用户最终质量承诺扩展后**的完整execution-ready复核，不是单独追审写作风格或重复过去的4个blocker。

## 当前对象

```text
target_repo = YuukiAS/AI_Skills_Collection
target_plugin_or_domain = writing-style / Clear Writing
design_topic_or_task_key = clear-writing--single-entry-artifact-finalization
source_branch_or_ref = design/clear-writing--single-entry-artifact-finalization
tracking_issue = #13
review_stage = REVISED_EXECUTION_READY_REVIEW_READER_AND_GITHUB
prior_package_commit = f2dc07cdd396f43788236a04e28f445fe1bfd3ec
old_release_candidate = 079bd7987bb33d624d244feb415327d5cf2343d8
```

从用户本轮给出的exact `PACKAGE_COMMIT` 完整读取以下同一快照：

1. `docs/design/clear-writing/CLEAR_WRITING_0_6_CHAT_RESPONSE_CONTENT_SELECTION_PROPOSAL_V0_2_2026-10-20.md`
2. `docs/design/clear-writing/CLEAR_WRITING_0_6_EXECUTION_READY_PLAN_V0_3_2026-10-20.md`
3. `docs/goals/CLEAR_WRITING_0_6_SINGLE_ENTRY_ARTIFACT_FINALIZATION_GOAL_V0_3_2026-10-20.md`
4. `docs/design/clear-writing/CLEAR_WRITING_0_6_GATE_EXECUTION_RUNBOOK_V0_3_2026-10-20.md`
5. `docs/operations/prompts/CLEAR_WRITING_0_6_KICKOFF_DRAFT_V0_3_2026-10-20.md`
6. `results/clear-writing--single-entry-artifact-finalization/CAT_TRACE_BRIDGE_READER_VALUE_COMPARISON_20261021.md`
7. `results/clear-writing--single-entry-artifact-finalization/PLANNER_REVISION_STATUS_20261021.json`
8. `docs/design/clear-writing/CLEAR_WRITING_0_6_EXECUTION_READY_CRITIC_PROMPT_V0_5_2026-10-21.md`。

先核实并实际读取最新`main`的`AGENTS.md`、Planner/Critic合同、Plugin Capability Gate Policy、AI Skills维护看板、版本规范、真实Skill refinement及writing-style TODO，再读本分支原产品Proposal、Phase C归因与执行职责修订、Issue #13和最新历史证据。若最新合同较历史prompt更新，以最新为准，不继承旧PASS。当前Personal Plugin必须实际只读回查0.5.0账户状态，不能以文档声称代替。

## 1. 必须独立核对真正正反材料

从`YuukiAS/CAT-TRACE@0d829fb17c458a076a15ec51893e917960107c21`全文读取本轮四份`docs/model/catalog_aware/CAT_TRACE_ZERO_SLOT_*20261021.md`，按上面的对照备忘录exact filenames定位。判断该类成功为什么与“长、有公式、有标题”不冲突：先问题和动机、再具体可检验例子、变量/公式与关系、适用条件/数值限制，且第7节第一次未完全解决困惑，需要第二次针对性补正。不得把它描述为无Clear Writing的因果对照试验或机械模板。

Bridge生产负例按`docs/plugin-todos/writing-style.md@de460300f55b5617654dd50b2a5cfec9ab89a094`、Issue #13评论`6293997950`/`6294277450`核实；原24章节完整ChatGPT回复未取得，不能声称逐字审核或用后续同类重放冒充原回答字节复现。

## 2. 必须回答的产品问题

- 0.5中响应技能被读取却仍出现内容选择失败，0.6单入口已解决什么，本轮`CHAT_RESPONSE`读者价值筛选与必要概念/例子/数学关系推进真正改变哪个生成阶段？
- 为什么这不是只给`response-clarity`重复增加同义写作建议，也不是只在末尾自检？领域层如何仍拥有事实真假、数学关系与研究结论？
- 哪些科学解释必须保持详细证明、数值、变量层级、实现/复现信息？如何避免学习CAT格式后产生机械“小故事+公式+六标题”模板？
- 同一个显式Clear Writing请求下，聊天和GitHub Markdown两个目标怎样各自路由、分别全文审查，文件的**保真、读者质量、写入身份**如何三证分离？聊天质量或hash单独PASS为什么不足？
- 正式GitHub-only支持目前以`update_file`修改已有文件为主，本轮用户明示“创建或修改”。方案新增`create_file`非覆盖创建以及路径不存在/branch HEAD/commit parent/全文回读的合同，在现有正常GitHub工具下是否真正可实现、是否有不可接受的写入竞争窗口？不能把它留给Codex自行决定；不可行则给确切REVISE并最小修订，不允许无声收窄用户要求。
- 若Skill未按计划做内容选择或写前文稿质量审查，哪些实际正常Web证据会令G2/G3直接失败并阻止0.6发布？不能把Skill内自检宣称为不可绕过发送前Hook，也不能以这一限制为借口不改进产品。

## 3. 现有六个Gate能否真正证明用户体验

保持G1单入口/身份；G2 T1真实Bridge工程完成汇报、T9 Phase C交接、T8-A CAT-TRACE科研机制、T8-B原传感器长技术保护及其它原路线；G3-A原Reader Guide聊天+GitHub修改全链，G3-B同一Gate的GitHub新文本非覆盖创建+聊天全链；G4全部完整原题/源/聊天/候选/最终文件保真；G5六route/Marketplace/profile/版本兼容；G6原独立Critic冻结后的**唯一fresh**完整长技术文件任务。CAT、Bridge、Phase C均是已见，不得称为fresh。必要数据应受限保存并直接供独立Reviewer读取，不得只有摘要/哈希/图片。

重点核实模型、每任务一次产品答案、仅无模型输出infra最多一次重试、失败后不改题不挑赢家；G3两子任务都应绑定同一个正式候选和release，不增加G7。实施后只可用真实结果回答“是否更可靠”，不能用已知正负例加静态条款给出未经证明的低失败率断言。

## 4. Phase C、安全与候选身份

原`079bd798...`只能当历史实现基线。新版读者理解链、外部文件全文质量与新建合同、安全ZIP/tar.gz旧档案兼容必须成为**同一个下一候选**；原Codex archive-only修复不得单独发布或与新候选并发。真实插件0.5.0继续原封不动；Phase C-A必须先证明真实账户0.5档案字节可下载、`prepare-restore`可消费、0.6.1恢复包可验证并能向Plugin Creator上传；Phase C-B真正鲜开的Web `GPT-5.6 Sol`对话中显式选择Clear Writing，不允许当前Planner chat模拟。可以不同合法入口承担，但候选身份、用户授权、Gate条件和恢复负责人不能分裂。用户仅做真正UI-only的最小动作，Planner/Executor不能甩给用户提示词拼接、评判或恢复。

## 5. 审查边界与结论

当前只是Planner修订，不得修改repo/Issue/Project，不启动Codex，不更新Personal Plugin，不创建G3分支，不运行G1-G6，不用付费API。对完整用户承诺、Proposal/Plan/Goal/Kickoff及正常执行/关键失败与恢复链作真正最终审查，不缩成过去blocker点评。

只允许：

```text
DECISION=PASS
READY_FOR_CODEX=YES
```

或

```text
DECISION=REVISE
READY_FOR_CODEX=NO
```

若REVISE，给稳定`CW06-R5-xx`真实阻塞、最小关闭条件，并直接提供同任务Planner返修提示词。若PASS，严格绑定用户提供的exact PACKAGE_COMMIT和以上五份同版本包；说明它只批准后续实施，不是已通过Gates或已发布。按最新Critic合同直接给一份简短完整的Codex handoff供用户发送（不是自动执行授权）；不得留下路径/commit占位符让用户自己拼接。

## 六、2026-10-22 必须独立复核的最小新增改动

本次用户提供**同一Bridge任务的两版完整回答**，第二版在明确参照CAT-TRACE后更偏向读者疑问与现实情景，但也包含用户纠正与明确重写要求，存在混杂因素。必须读 `results/clear-writing--single-entry-artifact-finalization/CAT_TRACE_BRIDGE_READER_VALUE_COMPARISON_20261021.md` 新增的2026-10-22小节，并将对照与四篇CAT原文核实，不能只复述Planner的结论。

审查当前唯一`clear-writing`入口是否把以下能力变成**实际加载的一个紧凑指令与微型示范**，而非散落在Plan/Gate里或藏在运行时可能不读取的CAT私有参考文件：

- `CHAT_RESPONSE`先从当前user prompt确定真正需要回答/理解的问题；
- 内容选择与读者疑问的因果关系分层：用户遇到什么难题、现有机制如何起作用、为什么改变实际结果、应提供何种证据/条件；
- 对抽象科研对象按需用可核查的具体对比、变量、数学关系和限制建立理解；
- 在总入口直接内嵌一组**非敏感简短对照**，对比只列“锁/文件/原子写入/没有其他组件”和真正解释“两进程旧内容覆盖→锁内重读/原子替换→减少风险但不等于全局完成”的区别；
- 用户没要求深入解释时不强制举例/报告；用户明确要完整算法、公式、复现时不能以简短为名削弱；
- 不复制CAT私有事实进入分发，不给canonical `response-clarity`增加同义语义副本，不新增额外Skill/服务/第二模型/发送前Hook。

与此前包的区别是：**现有v0.3已经有读者价值筛选和CAT科研正例，此轮专门补上跨领域的可执行解释组织示范**。判断这是不是合理、低成本、能真实影响`clear-writing`正常入口的因果环节；若仅堆一个新禁词、重复已有写作规则或把CAT格式变成强制模板，应REVISE。

验收侧不得增加Gate或额外Web请求：G2-T1原Bridge自然prompt**没有“参考CAT”**，Reviewer需看到完整输入/来源/输出，检查至少一个重要机制是否真实完成用户问题→风险情景→工作机制→实际后果→可信限制的理解链，同时保证整个答复不是一长串不必要的审计清单。不能机械计数标题、例子、章节或字数。G2-T8-A/B、T9、G3双交付、G4-G6保留原完整合同。

历史`079bd798...`仍只是旧候选，正式writing-style保持0.5.0；新的简短总入口改动必须与已批准的ZIP/tar.gz兼容及前述0.6修订冻结成**同一下一候选**。只做Planner审查，不允许现在实施或声称网页调用已经改善。

本轮结论仍只能为完整`PASS + READY_FOR_CODEX=YES`或`REVISE + READY_FOR_CODEX=NO`。即使新增差异较小，仍应按最新Critic Role Contract独立审查完整用户承诺、Plan/Goal/Kickoff/Runbook、执行路径、权限、恢复、正常成功及失败链，不能只给本小节的局部PASS。
