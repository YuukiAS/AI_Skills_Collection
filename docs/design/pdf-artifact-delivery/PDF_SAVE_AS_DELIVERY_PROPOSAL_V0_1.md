# PDF 渲染完成后直接交付可另存为成品 — Planner 提案 v0.1

日期：2026-10-14  
状态：**提交独立 Critic 审查；未获实施授权；不得据此宣称产品已修复**  
目标仓库：`YuukiAS/AI_Skills_Collection`  
能力归属：独立技能 `render-chinese-math-pdf`，不是 `slurm-workflows`  
任务键：`documents-media--pdf-save-as-delivery`  
来源：`main`；设计分支：`design/documents-media--pdf-save-as-delivery-20261014`  
拟执行分支（通过独立审查和用户 Kickoff 后才建立）：`reviewed/documents-media--pdf-save-as-delivery`  
同版执行 Goal：`docs/goals/DOCUMENTS_MEDIA_PDF_SAVE_AS_DELIVERY_GOAL_V0_1.md`  
同版 Kickoff 草案：`docs/operations/prompts/PDF_SAVE_AS_DELIVERY_KICKOFF_DRAFT_V0_1.md`

## 1. 决策：只修复首次成品交付

真实问题：CAT-TRACE 的双语方法导读 PDF 已生成并报告 9 页 A4、字体、公式和整页检查，首次回复只给渲染说明；用户追问“可以另存为的pdf呢？次次问你要了？”之后，助手才展示同一 PDF 的文件卡片。用户明确希望**以后完成 PDF 渲染时不必再索要文件**。

**当前有证据直接支持**：最终回复没有自动附带可取用成品；同一对话在追问后出现文件卡片。截图不能单独证明该卡片实际下载后的字节同一性，也不能证明任何 Codex/ChatGPT 宿主都支持相同交付功能。不能据此预先断言远端上传已解决。

本轮用户成功标准：在支持文件交付的当前正常交互入口，用户发出一次“生成 PDF”请求，随后**首次完成回复**就有可打开、下载或另存为的**最终 PDF**；不依赖用户追加“发附件/给链接”。若宿主确实不支持，真实报告“已生成但尚未交付”，而非虚构下载链接或称整个用户任务完成。

## 2. 核实过的当前机制与分层归因

1. `skills/tools/documents-media/render-chinese-math-pdf/SKILL.md` 声明默认 Pandoc/XeLaTeX，完成状态 `complete` 由 PDF 渲染及内容检查构成；没有实际可下载交付检查。
2. `skills/tools/documents-media/render-chinese-math-pdf/scripts/render_scientific_pdf.py` 在 `render()` 生成 `receipt["status"] = "complete"` 和 `receipt["output_pdf"] = <绝对路径>`；`main()` 将回执保存或打印。它不调用宿主附件接口、用户可用链接生成或远端文件交接。这不是渲染器的文档遗漏，而是任务完成条件与宿主交付责任未接通。
3. `skills/tools/documents-media/render-chinese-math-pdf/references/checklists.md` 的“Final Report”只要求 PDF 路径、命令、页数、预览与故障，未要求用户实际取得文件。
4. `profiles/server-research-baseline.json` 同时安装 `render-chinese-math-pdf` 与 `slurm-workflows`；后者只管调度/监测，不应因为生成环境在 Slurm 上就让调度技能负责 PDF 附件。
5. 前次软件截图表明“追问后可展示文件卡片”是当前消费入口的可行线索，但其宿主接口、是否自动触发、文件位于何处与是否可下载，**留待 Executor 在真实环境只读/低风险探针确认**。仓库代码审查无法替代这个事实。

外部能力边界（2026-10-14 检查，**REFERENCE_ONLY，不当作当前消费端已运行证明**）：
- OpenAI [文件与产出物说明](https://developers.openai.com/api/docs/guides/agents-api/environments/files)：自托管环境的文件须由相应宿主/文件系统获取；OpenAI 托管环境才提供特定产出物 API。两者不可混用，不能因为远端文件路径存在便拼一个下载 URL。
- OpenAI [ChatGPT 文件库说明](https://help.openai.com/en/articles/20001052-using-library-to-manage-files-in-chatgpt)：ChatGPT 中已保存的文件可以下载；它不保证远端 Codex shell 下任一文件自动成为聊天附件。

## 3. 最小可行机制与现实替代

首选复用既有 **“渲染 → PDF 检查 → 回执”**，只补最后一段消费端交付：

1. **产物确认**：渲染/检查照旧；从真实回执定位本次最终 PDF，确认文件存在、非空、可读取，必要时用哈希确认交付副本与已验收版本一致；不新增专用登记系统或二次渲染器。
2. **适配已存在的交付入口**：正常运行技能的 Codex/对话宿主若提供文件卡片、受支持附件或可下载产物能力，就使用该入口将最终 PDF 提供给当前用户；需要先迁移到宿主可读取目录时，采用当前已获授权且可验证的文件转交，不发明伪 `sandbox:` URL，也不把仅对服务器进程有效的路径称为可另存为链接。
3. **首次回复绑定交付**：交付成功后，首次完成回复直接展示最终文件的真实入口，技术渲染报告简短置后。PDF 的“渲染成功”与用户任务的“交付完成”保持独立判断：原程序 `receipt.status=complete` 可以仍表示渲染结束，但不再单独支持面向用户的最终任务完成宣称。
4. **无法交付时明确未完成**：对话宿主不支持、远程文件不可取、无授权传输路径、发布/附加失败、文件过大或链接不可达时，不虚构文件卡、公开发布私有内容或要求用户自己找路径；说明 PDF 在哪里生成、为什么当前不能安全交付、最小恢复方式，并将用户任务标记为交付未完成。
5. **最小消费者修复**：先通过已安装技能的自然请求回放确定缺陷是“使用了已有交付能力但漏发”还是“宿主完全没有该能力”。前者优先修 `SKILL.md` 的最终响应行为与 `checklists.md` 的交付检查，并在真实消费入口复核；若证据证明现有正常入口**不会消费这些约束**，则在本仓库内找到实际加载的技能/消费者入口作有界修复。若必须更改外部 Codex 平台、Bridge Kit 或跨插件共用附件基础设施，**停止本轮实施并带证据返回 Planner–Critic**，不得顺手新建上传器、网络发布服务或改全局 Host 规则。

对照的简化替代：只加一句“输出 PDF 链接”，改动最少但没有验收和可达性判定，容易再次漏发；仅通过 README/根 AGENTS 声明亦不接通真实消费入口。对照的复杂替代：新增自动上传服务或通用附件服务器，不符合此次现有宿主已展示文件卡片的证据、会增加凭据/权限/私有数据风险，因此拒绝。**首选现有正式入口 + 真实交付验收**。

## 4. 严格边界与授权

- 限定 `render-chinese-math-pdf` 及其最终回复/交付约定；本轮不修改 `slurm-workflows`、科研内容、数据、统计模型、公式、中文排版、Pandoc/XeLaTeX 渲染路线、字体/默认纸型、`research-writing` 的文稿语义或整个 ChatGPT 平台。
- 原始 CAT-TRACE PDF/Markdown、SSH/Slurm 凭据、私人服务器路径或受保护论文内容不进入公开仓库、Issue、CI、第三方文件存储。使用公开安全的小型中英文数学文档完成正常入口回放；如果之后确需真实私有材料，先核实文件/收件端/用途/授权，不能默认上传。
- 不新增 Slurm 分配、作业提交/取消、GPU 使用、付费外部 API、公众分享 URL、云盘权限或跨账户发布。已有真实正常用户交付通道可以在其受限授权范围内用；**外部传输要单独满足真实授权**。
- 不要凭不同宿主的 API 文档推断当前 Codex UI 一定支持文件卡。只有当同一真实消费环境完成取用验证，才能声称该环境的交付能力 PASS。
- 既有完整 PDF 数学/字体验收继续有效，前序 `receipt` 仅代表渲染侧检查。不得因为更方便交付而降低数学保真、换输出 PDF、切浏览器降级渲染或提交图片冒充成品。
- 本轮不改变 Marketplace 拓扑、现有 profile membership、Bridge 状态/授权策略，不新建中央 plugin、数据库、定时任务或新上传服务。

## 5. 实施顺序与最小必要变更

**预检（先于修改）**：从最新版安装的 `server-research-baseline` 或等效实际消费 profile，用正常语言请求一份公开安全、可验证的小型数学 PDF，在当前代表性 Codex 消费入口中观察：真实回执、实际 PDF、首次最终回复、宿主能否提供可取用文件。无需新 Slurm 作业。记录是否已有文件卡能力与触发方式，不把截图示例当当前环境的自动能力。如果消费入口无法接收文件且没有安全可行的方式，停止并写明事实，不继续改文档自称解决。

**修复（仅允许最小范围）**：优先调整 `skills/tools/documents-media/render-chinese-math-pdf/SKILL.md`、`references/checklists.md` 和适用的既有测试/受影响的正常消费入口，使最终成品优先交付并明确未交付状态。无需改 `render_scientific_pdf.py` 就不改；若探针证明必须在同一 renderer 层增加最小副本身份/路径核对，则需说明现有回执为何不够且不新增跨宿主附件 API。测试脚本可以证明检查逻辑，不能冒充宿主文件卡实际出现。

**验收和发布**：开发期先运行便宜的回归，固定最终候选，再在**实际安装/载入技能的正常 Codex 对话**做终验，核查首次回复有可获取的实际成品，并下载/打开或以宿主实际文件交付证据核对文件身份与内容。独立 Reviewer 能访问必要运行截图/文件/回执；保留完整成功/失败记录，不挑选最好的一次。相同最终候选通过各 Gate 后才允许版本/集成。若当前宿主缺能力而需要另一个 owner，实现阶段停下重新走 Planner–Critic，不发布“已解决”。

## 6. Capability Gate Matrix（v0.1）

| Gate | 独立能力与正常入口 | 必需证据及失败定义 | 不应回归 / 最终候选 |
|---|---|---|---|
| D1 — 首次可获取成品 | 安装并实际加载的 `render-chinese-math-pdf`，以自然语言请求 PDF，优先覆盖本次报告所用的远端计算场景，另覆盖现有本地输出路径；不靠用户追加索取消息 | 第一次完成回复内有宿主真实附件/可下载文件；审查者可实际打开或另存为并核对是同一已通过检查的完整 PDF。只有远端绝对路径、伪链接、预览图、第二次索取后才出现文件，均 FAIL | 原数学/字体/项目模板/QA 不变；同一最终候选、真实消费界面直接通过 |
| D2 — 无法交付时如实处理 | 真实入口中模拟/复现宿主不可取、无授权传输或附件失败的情况，不向外上传私有文件 | 渲染侧可记录成功，但用户任务不得报告“已交付完成”；显示真实限制和最小恢复方式；没有伪链接/隐式外传。若错误被掩盖或要求用户自己猜服务器位置则 FAIL | 不破坏合法文件访问、源私密性和权限界限；与 D1 同候选 |
| D3 — 既有渲染和调用兼容 | 既有回归集合 + 直接 `.tex`、普通 Markdown、项目自带渲染合同以及非 PDF 任务不被误触发 | 现有命令/receipt 语义、完整文档质量检查、字体/公式、profile、无浏览器降级维持；不因新增交付行为导致渲染或输出身份漂移 | 同一最终候选完成已有便宜回归与必要可视/正式入口复核 |

分类：D1 是现有生产入口验收此前漏掉的“用户实际取得文件”证据类型；D2 是安全失败语义，与成功交付不同；D3 继承已有渲染可靠性 Gate 和 should-not-change 回归，**不重造同义 Gate**。先廉价回归与失败用例，再正常完整产物。若改到 shared runtime、profile、外部传输、插件路由或跨插件正式行为，必须退回扩大 Gate 的方案审查，不允许用本窄 Gate 直接发布。实际交付 UI 与 PDF 全文质量的证据都必须来自同一冻结最终候选；不以机械哈希/文件存在代替 D1。

## 7. 真实失败、停止与恢复

- **SKILL 文档改后仍不展示附件**：说明入口未消费或附件需宿主动作；先定位真正的消费者，不无限增加相似说明。任何必须跨所有平台统一上传的设计都超出此案。
- **远端文件无法安全取得**：保持已生成文件/receipt，不做自动外传，不生成伪下载链接；对用户报告交付尚未完成。待授权后仅走已支持的交接路径。
- **仅支持浏览器中点击保存而不支持程序侧附件**：不能以“技术上提供了文件路径”宣称目标达成。对受影响的宿主返回待解决缺口，必要时请 Critic 决定改 owner/scope。
- **回归失败**：按失败源归因并在本任务内修复；如果暴露冻结机制无效则停下交 Planner，不绕过 Gate 或更换最终样本。
- **预算/时间**：不需要付费模型、真实 Slurm 资源或永久在线守护；预检一次、已知回归+正常入口候选验证，失败后最多一次有证据的同范围修复，仍无解则停止报告，不无限多轮。
- **审查阶段**：本 Proposal + Goal + Kickoff 草案先交独立 Critic 作 `EXECUTION_READY` 审查。未经 PASS 不开执行，不把本次设计文档当授权。

## 8. 版本、README 与跟踪

当前核实：repository `5.4.4`；独立技能 `render-chinese-math-pdf` 的 `SKILL.md` 为 `0.2`。**此设计轮不改版本。**

- Repository bump decision: `NONE`（设计阶段）；若形成完整可安装的兼容改进并正式发布，预期为当时 latest main 的 `PATCH`，不预设 `5.4.5` 永远可用。
- Affected central plugins: 全部 `NO_BUMP`；`slurm-workflows` `NO_BUMP`。
- Standalone skill：预期 `render-chinese-math-pdf 0.2 → 0.3`，但仅在实际生效、D1–D3 同候选通过且准备正式发布时推进一次；只有维护文档或测试增加时 `NO_BUMP`。
- 发布前更新必要的元数据与根 `CHANGELOG.md`，检查 README 是否因版本/能力说明需同步；改 README 时遵守实际 Clear Writing 调用要求。不得提前改生成层、Marketplace、profile。
- 唯一真实反馈保存在 `docs/skill-todos/render-chinese-math-pdf.md` 的“PDF 渲染完成后未直接交付可另存为的成品”，当前 `status: NEW`，不与另一条“上游插件自动调用 renderer”的 TODO 混合。
- **维护看板待同步，不宣称已完成**：本轮 ChatGPT 工具未提供规定的 `writing-style`（Clear Writing）真实调用入口，也未提供 GitHub Project mutation；依据 `docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md` §6 不创建/改写读者可见追踪 Issue。下一具两种能力的维护环境应：核对该 TODO 尚无重复追踪 Issue → 实际调用 Clear Writing → 创建标题“PDF 渲染完成后直接提供可另存为文件”的 `maintenance-track` Issue，挂到 `AI Skills Maintenance`，Area=`standalone-skill`，本轮设计已启动时 Status=`DOING`；Issue 当前执行锚点指向本 Proposal、Goal、设计分支及最新提交，下一步为独立 Critic `EXECUTION_READY`；**同一动作在源 TODO 回填真实 `tracking: #N`**。绝不填写虚构 issue 编号、假称 Project 已同步，不让用户手动拖卡片。
- 当前实际改动仅在设计分支添加 Proposal、Goal、Kickoff 与 Critic 交接文档，不改运行代码或任何正式版本。README checked（设计轮）：no update required。

## 9. 交接角色与成功边界

Planner 本轮只提交可独立审查的 v0.1 方案。Critic 须独立复核真实代码/用户截图所支持的边界，尤其检查“给技能写交付说明”是否能被当前 Codex 正常入口真实消费；如不能，`REVISE` 而不是接受一个只在测试中有效的假 PASS。Critic 通过仅批准同版范围与冻结执行包，不代用户授权。最终用户是否真的可以不用再索取 PDF，只能在后续正常环境中交付真实成品并经复核后成立。
