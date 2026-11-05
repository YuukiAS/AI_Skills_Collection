# Asteria Recovery + Frontend Design vNext：唯一执行总控

日期：2026-11-04；最后状态更新：2026-11-05  
状态：ACTIVE CONTROL PLANE — PHASE_B_COMPLETE / CLAUDE_INDEPENDENT_ADJUDICATION_COMPLETE / USER_CONVERGENCE_PENDING  
记录位置：本文件是跨 Asteria / Frontend Design / Design Assurance 的唯一总执行记录；产品设计事实仍留在各产品仓库，插件事实仍留在 AI_Skills_Collection。  
原则：不新建 Notion 路线图、不新增 Planner/Critic 系统、不等待所有基础设施完成才继续 Asteria。

## 使用规则：这份文件是唯一总控

从 2026-11-05 起，本文件不是参考资料，而是 Asteria Blueprint / Atlas 恢复、Frontend Design vNext 与 Design Assurance 协作的唯一执行总控。

后续每一次 ChatGPT / Codex / Claude / Work 参与本项目，在给出新的判断、计划、提示词、实现建议或阶段结论之前，都必须先重新读取本文件，至少核对：
- 当前阶段；
- 已冻结决定；
- 当前证据来源；
- 当前唯一 NEXT_ACTION；
- 明确禁止重新打开的旧问题。

任何新的高影响决定、阶段完成、路线变化或用户明确裁决，都必须回写本文件；不能只留在聊天记录、临时提示词、Codex 本地 ledger 或其它派生文档里。

派生文件可以保存证据和细节，但它们不能与本文件并列成为第二套路线图。本文件只引用必要证据，并把对后续执行真正有约束力的结论吸收进来。

如果本文件的 CURRENT_STATE 与实际执行结果冲突，先停止下一阶段，更新本文件后再继续。不得依赖模型“记得上次聊过什么”来补齐状态。



## CURRENT_STATE — 2026-11-05

Phase A：COMPLETE。静态证据包、历史入口和审阅材料已准备完成。

Phase B：COMPLETE。Blueprint + Atlas 历史审阅已完成，覆盖 48/48 条目，无遗漏。当前已知交接结论：
- Blueprint 已留下明确的交互与产品继承要求；
- Atlas 尚无整体通过的设计方案，只保留有限 theme 认可与可继续评估的原生插件底座；
- 产品设计和实现均尚未完成；
- Claude 尚未启动；
- 尚未制作新 UI。

Phase B 的完整结论目前保存在 Mac mini 本地：
`/Users/yuukias/Code/Asteria-Phase-A-Evidence/PHASE_B_REVIEW_CONCLUSIONS_20261105.md`

这份本地结论尚未进入 GitHub，因此当前控制面仍有一个明确缺口：**在进入 Phase C 之前，必须把 Phase B 中对未来设计有约束力的结论同步进本文件；不能只在本地结论文件里保留。**

### 当前唯一 NEXT_ACTION

Claude 网页端独立裁决已经完成。原始回答逐字保存在：

`docs/design/frontend-design/CLAUDE_INDEPENDENT_ADJUDICATION_RAW_20261105.md`

该回答现在是**新的独立证据**，不是自动接受的路线决定。下一步先由用户与当前协调线程判断其中哪些结论接受、哪些需要补证或反驳，再把真正接受的改变写回本总控；在此之前不进入 Phase C 正式设计。

本轮同时产生了一条明确的交付教训：Claude 的裁决提示词过度采用固定编号、强制栏目和审计式问题清单，实际把回答推成“十条裁决 + 依据 + 缺项”的报告腔。后续给 Claude 的提示词应保留必须回答的实质问题，但默认要求自然中文、先给核心判断再展开，不强制固定十段或机械审计格式。

在这一步完成并写回本文件之前：
- 不启动 Claude；
- 不做新 UI；
- 不进入 production implementation；
- 不重新做历史审阅；
- 不新建另一份总路线图。


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

### Phase B — 可核验压缩 + 用户最小审阅 Gate
Claude 此时仍不介入。

Phase B 的压缩只负责降低阅读量，不拥有新的产品裁决权。36 个 Blueprint 与 12 个 Atlas 历史版本继续保留为完整底表；压缩层必须满足“全量映射、零遗漏、可展开、可追源、判断稳定”。

具体合同：
1. 48 个历史条目每一个都必须映射到且只映射到一个审阅组，生成覆盖表；不得因为“看起来重复”而从底表消失。
2. 每个审阅组必须列出其包含的全部 version id、原始截图/PDF 页、历史 verdict、两轮 Pro 的相关判断；压缩文字只是索引，原始证据始终可展开。
3. 每个“可能保留”判断必须指向具体局部和来源证据，不能写成整版 KEEP；用户裁决仍为 OPEN。
   两轮 GPT Pro 对同一历史资产若有不同判断，必须并列保留 `PRO_A / PRO_B`，不得由压缩者静默裁决成一个结论；只有原始证据或用户决定才能关闭分歧。
4. 压缩完成后必须做 coverage audit：48/48 映射、优先历史资产均有来源、历史已明确回答的问题没有重新包装成用户问题。
5. 用户质疑不能直接触发结论改变。若 GPT 修改某个分组、候选判断或推荐，必须记录 CHANGE_REASON，而且只能是：新增证据、发现来源冲突、发现原压缩错误、或用户作出新的明确决定。
6. 全量底表永久保留，因此任何压缩错误都可回退，不需要重新考古。

用户只需要看压缩后的少量审阅组，并对具体局部给出 KEEP / REPAIR / REJECT / UNSURE；真正会改变产品结构的少量取舍才需要用户回答。

完成门：coverage audit 通过；用户能够从任一压缩结论一跳回到原图/原页；形成最小 design brief、已确认局部资产、OPEN 决策和 Claude 只需读取的极小证据集合。

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

当前不再执行 Phase A / Phase B。唯一动作是把 2026-11-05 的 Phase B 完整交接结论同步进本文件并冻结 Phase C 输入。

只有同步完成后，才允许决定 Blueprint / Atlas 哪个先进入 Claude 正式设计、以及 Claude 的最小输入包。

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


## 8. Roadmap change discipline

用户质疑、追问或表达不满本身不是修改 Roadmap 的证据。后续任何路线变化都必须写明：
- OLD_DECISION：原结论；
- NEW_EVIDENCE：新增事实、来源冲突、发现的推理错误，或用户新的明确决定；
- CHANGE：因此改变的具体部分。

如果没有 NEW_EVIDENCE，则保持原 Roadmap，不因对话压力改口。


## 9. 最新状态日志

### 2026-11-05 — Phase B completed

NEW_EVIDENCE：
- Codex 报告 Blueprint + Atlas 历史审阅完成；
- 48/48 条目覆盖，无遗漏；
- 本地生成 `PHASE_B_REVIEW_CONCLUSIONS_20261105.md`；
- Blueprint 已形成明确交互要求；
- Atlas 没有整体通过方案，仅有有限 theme 认可与可评估原生插件底座；
- Claude 未启动，新 UI 未制作。

CHANGE：
- Phase B 状态改为 COMPLETE；
- Phase C 暂不启动；
- 先把本地 Phase B 结论中有执行约束力的内容同步进本文件；
- 本文件升级为唯一执行总控，后续每次回答和每个模型任务都必须先读取并围绕它继续。


## REUSE_AUDIT — 2026-11-05

本节记录“已有研究与公开轮子到底是否存在”，防止后续执行者重新造轮子或把“研究未被消费”误判成“没有研究”。

### Blueprint

已验证：Blueprint 并不缺 Deep Research。既有研究至少包括 `YuukiAS/AI_Research_Toolkit@main:docs/research/complex-system-showcase-20261026/` 的独立设计研究及其多轮结果，以及后续 architecture-evolution / Asteria Next 收敛研究。现有维护记录明确写明：Blueprint 已完成三份独立 Deep Research，均找到 20+ 个直接相关成熟参考。

这些研究和后续工具调查已经明确涉及可复用成熟方案，包括 LikeC4、IcePanel、Dagster、DataHub、Structurizr、React Flow / D3 / ELK，以及专业文档与交互系统案例。失败不能再解释为“GitHub 上没有轮子”；真正问题是研究结果没有稳定转成后续制作必须消费的视觉/交互资产、语义模型和验收约束，导致实现反复退化成普通 React Flow demo、dashboard、卡片、步骤页或 IDE 模板。

### Atlas

已验证：Atlas 有正式科学内容 Deep Research 基线，当前入口为 `YuukiAS/Asteria-Atlas@main:sources/dii/DEEP_RESEARCH_BASELINE_ZH.md`，并有 `prompts/DII_ATLAS_MVP_PRO_ZH.md` 消费该基线；更完整的方法协议与历史 seed 位于 `YuukiAS/Distributed_Imaging_Inference@research/dii-literature-map-20261027`。Atlas 同时已有可继续复用的原生 Obsidian 插件工程底座，而不是必须从零实现宿主。

截至本次审计，尚未在用户仓库中找到一份与 Blueprint 的 complex-system-showcase 研究同等级、专门系统调查 Atlas 前端/Obsidian 视觉案例与公开 GitHub 插件轮子并形成完整 prompt + result 的独立研究。2026-11-04 双项目工具调查覆盖了 Obsidian CLI、frontend-design、Figma、Playwright 等，但没有证据表明它已经系统消费 Breadcrumbs、Dataview、Graph Analysis 等 Atlas 相关公开机制。此项属于真实研究缺口，但不能与 Atlas 的科学内容 Deep Research 混为一谈。

### Frontend Design Skill

已验证存在官方 frontend-design Skill / Claude Code 插件，既有 Asteria 工具调查已将其列为可优先使用的设计能力。Skill 能帮助避免模板化前端、建立有意图的排版/色彩/布局/动效，但不能替代产品语义、科学关系设计、真实宿主验证，也不能自动保证外部公开轮子被真正复用。

### 后续硬约束

进入任何新设计之前，执行者必须先区分三件事：已有研究结论、已有可复用工程/公开轮子、仍然真实缺失的研究。禁止把“没有消费既有研究”重新解释成“需要再做一轮同范围研究”。若要补 Atlas 的外部设计/插件参考，只允许做针对当前缺口的窄研究，并把可复用机制直接映射到设计输入，而不是再生成一份孤立参考报告。


### 2026-11-05 — Claude independent adjudication gate added

OLD_DECISION：
- Phase B 完成后，先同步 Phase B 结论，再进入 Phase C。

NEW_EVIDENCE / USER_DECISION：
- 用户明确表示不接受 GPT 对“已有 Deep Research 是否充分、GitHub 是否已有可复用轮子、Frontend Design Skill 是否存在且有用、GPT 失败是否源于未消费研究”的单方面结论；
- 用户要求把两份原始项目对话、全部相关 Deep Research prompt/result、必要历史与工具/Skill 研究打包成单一 PDF，交给网页 Claude 独立裁决。

CHANGE：
- Phase C 正式设计继续暂停；
- 新增一次 Claude 独立裁决 Gate；
- Codex 只做证据工程，不替 Claude 下结论；
- Claude 独立裁决完成后，结论才允许进入本总控并影响 Phase C；
- 本 Gate 不允许启动新 UI 或 production implementation。


### 2026-11-05 — Claude independent adjudication completed

NEW_EVIDENCE：
- Claude 已完整读取 Core，并按索引回查 Supplement 的多个关键页，完成独立裁决；
- 原始回答逐字保存于 `CLAUDE_INDEPENDENT_ADJUDICATION_RAW_20261105.md`；
- Claude 明确给出了 GPT 是否继续使用、Design Assurance 是否应简化、Claude/Astra 位置、Blueprint/Atlas 继承还是重做等独立判断；
- Claude 同时明确列出自己未读/未验证的证据边界，因此本回答可作为有边界的独立证据，而不是最终事实权威；
- 实际输出形态为“十条裁决 + 依据 + 缺项”，证明当前 Claude 提示词结构过重，影响自然表达。

CHANGE：
- Claude 独立裁决 Gate 状态改为 COMPLETE；
- 不自动把 Claude 的结论写成冻结路线，等待用户收敛；
- 后续 Claude 提示词不再默认使用固定十项审计报告结构；保留问题本身，改用自然段和人话表达；
- Phase C 继续暂停，直到用户明确接受/修正本轮裁决并更新总控。
