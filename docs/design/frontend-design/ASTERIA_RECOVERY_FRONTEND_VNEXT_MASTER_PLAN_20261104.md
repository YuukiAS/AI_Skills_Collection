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

### Phase B — Claude Stage 1：独立视觉/产品诊断
这是 Claude 第一次介入的正确位置。

为什么不是更早：更早会把昂贵额度浪费在仓库搜索、PDF定位和重复研究。  
为什么不是更晚：如果用户先把所有产品选择都定完，Claude 只剩执行角色，失去其独立视觉/产品判断价值。

Claude 只做：
1. 亲自读取两份原始 PDF 的关键原文与关键视觉页、历史图库和少量必要 Deep Research 原文。
2. 在看 GPT Pro 最终结论前先形成自己的诊断。
3. 对历史版本提出 CANDIDATE_KEEP / CANDIDATE_REPAIR / REJECT 建议，但不得替用户升级为 ACCEPTED。
4. 识别 Blueprint / Atlas 真正尚未决定、会改变信息架构或视觉方向的问题。
5. 最后提出数量克制的用户问题后停止。
6. 探测当前 Claude Code / 中转的图片读取、官方 frontend-design Skill 等必要能力；不安装 Skill 大全，不做完整设计，不写产品代码。

完成门：用户拿到“Claude 独立判断 + 历史候选资产 + 少量真正未决问题”。

### Phase C — 用户设计收敛 Gate
这是本计划中用户必须集中介入的一次主要阶段。

用户需要决定的只有三类：
1. 历史资产：哪些局部明确 KEEP、哪些允许重做、哪些彻底不要；可以逐版本查看，但模型不得先替用户冻结。
2. 高影响产品取舍：例如 graph/非 graph 边界、信息密度、全局上下文保留、机制/论文详情的主要阅读方式等；只讨论 Claude 与两轮 Pro 都认为会改变整体设计的事项。
3. 本轮制作策略：先做 Blueprint 还是 Atlas、是否需要一还是两个候选、Claude 设计 spike 的范围。

用户不需要决定字体数值、每个组件样式、普通布局细节、实现技术和机械 QA。

这些确认写回本文件的 Decision Log，并在进入具体项目时写入该项目自己的 canonical design baseline。

### Phase D — Claude Stage 2：小范围可运行设计 spike
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
- Phase B 结束：集中确认历史 KEEP/REJECT 与少量高影响产品取舍。
- Phase D：从 1–2 个真实候选中选方向。
- Phase F：最终接受成品。

其余可由模型/工具自行推进，只有出现新的结构级冲突才重新询问。

## 6. 当前立即动作

1. 不再开第三轮 Pro。
2. 不开始 Claude full redesign。
3. 先用两轮 Pro + 现有历史图库完成 Phase A：用户审阅队列、Open Decisions、Claude Stage 1 最终合并输入。
4. 同时只冻结 Design Assurance 的权威 contract 和 Frontend Design vNext requirements；不等待完整插件实现。
5. Phase A 完成即进入 Claude Stage 1；Claude 的结果直接进入 Phase C，而不是再开一轮 GPT 研究。

## Decision Log

当前所有产品级决定均保持 OPEN。特别是：
- Blueprint / Atlas 哪个先进入 Stage 2：OPEN。
- 哪些历史版本/局部正式 KEEP：OPEN，等待用户审阅。
- 每个项目需要一个还是两个 Claude 候选：OPEN。
- Claude 是否在 Stage 2 直接产出可运行 design spike、还是先静态关键状态：建议优先可运行 spike，但待 Stage 1 能力探测与用户确认。


## 7. Phase A 当前执行状态

状态：ACTIVE（2026-11-04）

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
4. 收敛 Claude Stage 1 的最终必读清单。
