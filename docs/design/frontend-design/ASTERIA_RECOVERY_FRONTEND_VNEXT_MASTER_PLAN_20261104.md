# Asteria Recovery + Frontend Design vNext：单一执行主线

日期：2026-11-04  
状态：DRAFT MASTER PLAN — 用于收敛，不新增框架  
记录位置：本文件是跨 Asteria / Frontend Design / Design Assurance 的唯一总执行记录；产品设计事实仍留在各产品仓库，插件事实仍留在 AI_Skills_Collection。  
原则：不新建 Notion 路线图、不新增 Planner/Critic 系统、不等待所有基础设施完成才继续 Asteria。

## 0. 已冻结的事实

两轮 GPT Pro 已完成历史复盘、Claude 工具/成本研究和阶段提示词。共同结论：
- 失败不是单纯“审美差”，而是上游产品判断不稳、局部反馈扩大为整体重设、正确局部无法继承、研究未变成可执行资产、测试/截图可保护错误产品定义。
- Claude 值得用于高价值产品/视觉判断，但不能被当成自动正确，也不应承担可由 Codex/GPT 完成的搜索、整理、构建和机械实现。
- Claude 必须亲自看原始 PDF 与关键视觉证据，先独立判断，再与用户确认真正改变产品方向的少量问题。
- Frontend Design 现有 v0.4 已有 P0–P4、F-A–F-D、S1/S2/S3、真实宿主验收；本轮应升级现有能力，不新建平行插件。
- 当前 feedback-continuity 合同与 design_guard 原型是输入，不是最终 vNext。

## 1. 总顺序

### Phase A — GPT/Codex 收敛现有证据（Claude 之前）
目的：利用两轮 Pro，避免 Claude 花钱做低价值检索。

只做：
1. 核对两轮 Pro 的正式报告、Stage 1/2 prompt、已有 Deep Research、两套历史图库与原始 PDF。
2. 基于现有 Blueprint 36 条、Atlas 12 条历史条目建立“用户审阅队列”：每条只记录真实入口、失败原因、已有正面证据、Pro 的候选保留判断；用户裁决保持 OPEN，不替用户写 KEEP。
3. 汇总真正未决的产品问题，去重历史已经回答的问题。
4. 把现有 Frontend Design vNext 已知需求和 Design Assurance 边界冻结为设计合同，不先实现全部插件。

完成门：Claude 不再需要全仓扫描或重新研究；历史证据、候选保留项、未决问题和可直接打开的视觉入口可用。

### Phase B — GPT 收敛 + 用户最小审阅 Gate
Claude 此时仍不介入。

GPT 使用两轮 Pro、Phase A 静态证据包和历史用户反馈完成最后一次廉价压缩：
1. 把 36 个 Blueprint 与 12 个 Atlas 历史版本按“真正不同的设计思想/局部资产”合并成少量审阅组，不让用户逐个重看全部版本；
2. 每组只指出值得看的局部、历史失败、可能保留资产和真实截图入口；
3. 汇总真正仍未解决、会改变产品结构的少量问题，并去掉历史已经回答的问题；
4. 明确区分 GPT 的候选判断与用户确认。

用户只需要：
- 对少量审阅组做局部 KEEP / REPAIR / REJECT / UNSURE；
- 回答真正改变产品方向的少量取舍；
- 决定先推进哪个项目。

完成门：形成每个项目的最小 design brief、已确认 KEEP/REJECT、OPEN 决策和 Claude 需要看的极小证据集合。

### Phase C — Claude 首次正式设计介入
这是 Claude 第一次介入的正确位置。

为什么不是更早：历史诊断、版本筛选、PDF阅读和资料整理已经由两轮 Pro + GPT/Codex 完成；让 Claude 重做会重复消耗昂贵上下文。
为什么不是更晚：在具体视觉/产品方向还没有完成前介入，Claude 仍能贡献独立的前端审美、空间组织和产品设计判断，而不是只做美化。

Claude 只读取：
- 用户已确认的最小 design brief；
- KEEP / REPAIR / REJECT / OPEN；
- 每个项目 3–6 张真正决定方向的静态截图或 PDF 页；
- 必要的真实内容/数据样例；
- 一页以内的失败约束摘要。

Claude 不读取完整 438 页 PDF，不重读 36+12 全历史，不打开 Obsidian/浏览器/Figma，不重跑研究。

Claude 的任务：
1. 对用户已确认的产品目标做一次真实前端产品/视觉设计 pass；
2. 必要时指出当前 brief 中仍存在的一处关键冲突，但不得重新开启全历史诊断；
3. 为一次只处理的一个项目提出 1–2 个真正不同的窄范围设计方向/关键场景；
4. 允许使用官方 frontend-design Skill；
5. 输出足够让用户比较信息组织、图形职责、密度、上下文连续性和视觉质量的结果。

### Phase D — 用户选择 + Claude 设计冻结
一次只处理用户选择的一个项目。

Claude 使用真实内容做 1–2 个真正不同的窄范围方向，优先是可运行关键状态/关键任务链，而不是长篇视觉规范；允许使用官方 frontend-design Skill。候选必须让用户能直接比较信息组织、图形职责、密度、上下文连续性和视觉质量。

如果两个候选都失败，停止并回到问题判断，不自动生成第三套完整方向。

用户选中后，冻结项目级 DESIGN_BASELINE：已确认画面/行为、KEEP、未决问题、回滚点。Claude 后续视觉返修必须继承它。

### Phase E — Design Assurance Gate → Codex 完整实现
Design Assurance 不负责“设计得漂不漂亮”，而负责设计是否已经充分到值得实施：
- 核心真实任务是否覆盖；
- 关键对象/关系/状态是否有清楚语义；
- 机制/实现/证据/返回路径是否闭合；
- 是否仍有会改变整体结构的 OPEN 决策；
- 失败路径和回滚是否明确；
- 当前证据是否来自准确候选，而不是旧图/静态 PASS。

Claude 在 Design Assurance 中是可选的高质量产品/视觉 specialist，可提供独立设计批评或修订建议，但不是 PASS authority，也不是硬依赖。GPT Pro/Astra/其他足够强的设计模型可以替换这一 specialist 角色。

Design Assurance 合同通过后，Codex 按冻结方向做 production implementation、测试、自动化、截图/录制、提交与回读；不得重新发明产品方向。

### Phase F — Claude 定向视觉返修 + 真实验收
Codex 每次实现后，Claude 只处理真实渲染中需要高价值视觉/交互判断的差异；工程 bug 继续由 Codex 修。

每次返修沿用 Frontend Design S1/S2/S3：
- S1：局部工程/视觉差异；
- S2：有限设计调整；
- S3：只有用户明确要求或现有结构经证据证明不可修时才允许整体换向。

必须保留已确认 KEEP，并在真实浏览器/Obsidian 宿主下验证。接近完成时再按风险触发一次独立 Work/黑箱验收，用户最终接受。

## 2. Frontend Design vNext 到底改什么

不重建插件。现有 v0.4 + feedback-continuity 合同上补四件事：

1. **首次设计的任务建模 gate**：先建模真实用户任务、对象、关系、必须同时可见的信息，再选视觉隐喻；禁止从“架构图/知识图应该长什么样”直接套模板。
2. **关键场景先行**：全量实现前，用真实数据做 1–2 个可见/可操作关键场景，先验证产品组织和视觉方向。
3. **设计连续性**：已有产品反馈必须从准确 candidate + 用户反馈 + KEEP/REPAIR/UNTOUCHED/ROLLBACK 出发；S1/S2 不得静默升级 S3。
4. **候选晋升必须靠真实证据**：同 commit、真实宿主、相同任务链做前后验证；build/test/静态截图不能单独晋升设计基线。

模型层不硬编码供应商；能力路由上，当前实验优先把 Claude 用于高熵视觉/空间/信息组织问题，GPT 高/极高处理普通设计判断，GPT Pro 处理复杂科学/架构，Codex处理确定性实现，Work按风险做独立验收。

正式实现时间：现在先冻结 vNext requirements；完成至少一次 Claude Stage 2 + 用户选择 + 一轮真实返修后，利用新证据最终收敛 vNext，再由 Codex修改正式插件。这样 Frontend Design 不阻塞 Asteria，也不会在没有成功工作样本时凭空设计。

## 3. Design Assurance、Claude、Asteria 的边界

**Frontend Design**：产生和修改前端产品设计。  
**Design Assurance**：判断复杂设计是否足够明确、闭合、可实施；它是 gate/assurance，不是视觉设计师。  
**Delivery Assurance**：保证已经确定的设计/任务在跨模型、跨仓库、实现与证据交付中不失真；本轮不重做。  
**Asteria Blueprint / Atlas**：真实产品和试点，不是 assurance 层。

Claude：
- 可以在 Frontend Design 中承担高价值视觉/产品设计；
- 可以在 Design Assurance 中作为独立 specialist critic；
- 不能成为 Design Assurance 的唯一裁决者或硬依赖。

Asteria：
- 不能替代 Claude 的设计判断，因为 Asteria 是产品/表示系统，不是判断模型；
- 不能替代 Design Assurance，因为 Design Assurance 必须对不使用 Asteria 的项目也成立；
- 未来 Asteria Blueprint 若成熟，可以成为 Design Assurance 的一种可视化/证据表面，帮助展示 system → mechanism → implementation → evidence，但只能是可选 consumer，不应成为前置依赖。

## 4. Frontend Design vNext 与 Asteria 如何互相利用而不形成循环依赖

Asteria 不等待 Frontend Design vNext 正式发布。第一轮按冻结的 vNext 合同人工执行，直接推进产品。

Frontend Design vNext 也不等待两个 Asteria 全部完成。完成第一个项目的一次完整“Claude 设计 spike → 用户选择 → Codex实现 → Claude返修 →真实验收”循环后，就拥有足够新证据完成 vNext 设计和实现；第二个 Asteria 项目随后作为新版本插件的 fresh pilot / regression。

具体哪个项目先做、哪个历史案例成为回归，不在本文件预先替用户决定，由 Phase C 冻结。

## 5. 本计划需要用户确认的时点

不现在连续问几十个问题。

- Phase A：无需用户决定产品方向。
- Phase B：集中确认少量历史 KEEP/REPAIR/REJECT 与高影响产品取舍。
- Phase D：从 Claude 的 1–2 个真实候选中选方向并冻结。
- Phase F：最终接受成品。

其余可由模型/工具自行推进，只有出现新的结构级冲突才重新询问。

## 6. 当前立即动作

1. 不再开第三轮 Pro。
2. 不开始 Claude full redesign。
3. 先用两轮 Pro + 现有历史图库完成 Phase A：用户审阅队列、Open Decisions、Claude Stage 1 最终合并输入。
4. 同时只冻结 Design Assurance 的权威 contract 和 Frontend Design vNext requirements；不等待完整插件实现。
5. Phase A 完成后先进入 Phase B 的 GPT 收敛 + 用户最小审阅；只有形成最小 design brief 后才调用 Claude。

## Decision Log

当前所有产品级决定均保持 OPEN。特别是：
- Blueprint / Atlas 哪个先进入 Stage 2：OPEN。
- 哪些历史版本/局部正式 KEEP：OPEN，等待用户审阅。
- 每个项目需要一个还是两个 Claude 候选：OPEN。
- Claude 是否在 Stage 2 直接产出可运行 design spike、还是先静态关键状态：建议优先可运行 spike，但待 Stage 1 能力探测与用户确认。


## 7. Phase A 当前执行状态

状态：PHASE_A_COMPLETE（2026-11-04）

已经落地的 Phase A 文件：
- `PHASE_A_EVIDENCE_PACK_AND_REVIEW_QUEUE_20261104.md`：36 个 Blueprint + 12 个 Atlas 全量 OPEN 审阅队列、优先审阅层、静态证据入口和 Claude 输入约束；
- `DESIGN_ASSURANCE_CLAUDE_ROLE_DECISION_20261104.md`：Design Assurance 的具体步骤，以及 Claude / GPT Astra 共用的 Frontend Product & Visual Design Specialist 槽位。

新增硬约束：
- Claude 不负责启动 Obsidian、浏览器、Figma 或网页预览来理解历史；
- Claude 不负责机械截图、录屏、构建、PDF 批量渲染或全仓搜索；
- 这些工作由 GPT/Codex 在 Phase A / 实施验收阶段提前准备成静态证据；
- 对重要前端任务，当前生产策略要求 Claude 至少真实承担一次设计 pass；Claude不可用时由 GPT Astra 替代同一 specialist 角色；
- 用户对历史资产的最终裁决必须保持 OPEN，模型只能提供候选保留/修复/拒绝意见。

Phase A 下一机械动作：
1. Blueprint 生成静态 contact sheet；
2. 两份历史 PDF 生成精选关键页静态 page pack；
3. 核对 Mac mini 上 Claude 可直接读取所有静态证据；
4. 收敛 Claude Stage 1 的最终必读清单。\n\n机械执行入口：`CODEX_PHASE_A_STATIC_EVIDENCE_PREP_20261104.md`。该任务只生成本地 contact sheet、priority 静态图、16 个指定 PDF 页和 manifest；严禁启动 Obsidian/浏览器/Figma，严禁修改产品仓库。\n\nPhase A 静态包已报告 PASS：Blueprint priority 17/17、Atlas priority 9/9、两侧 PDF 关键页 8/8、两份 Pro 摘要 2/2，无 blocker；Blueprint 第 23 版原图继续明确为不可恢复。\n\nPhase A 静态证据准备已完成。原 `CLAUDE_STAGE1_FINAL_STATIC_EVIDENCE_PROMPT_20261104.md` 因仍要求 Claude 重做历史诊断、与节省 API 的目标冲突，现已废弃，不得执行。下一阶段为 Phase B：GPT 收敛 + 用户最小审阅。Claude 只在 Phase C 首次正式设计时介入。
