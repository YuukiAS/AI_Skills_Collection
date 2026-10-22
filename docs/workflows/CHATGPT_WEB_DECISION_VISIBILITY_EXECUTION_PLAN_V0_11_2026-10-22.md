# Planner–Critic 1.8：完整执行就绪计划 v0.11

日期：2026-10-22。任务：`chatgpt-web--pass-integrity`。
目标仓库：`YuukiAS/AI_Skills_Collection`。
已有设计分支：`design/chatgpt-web--pass-integrity-v0-4`。
唯一同版 Proposal：`docs/workflows/CHATGPT_WEB_DECISION_VISIBILITY_PROPOSAL_V0_11_2026-10-22.md`。
设计通过依据：用户转交的独立 Critic v0.10 `PROCEED`，原文存档于 `results/chatgpt-web--pass-integrity/DESIGN_CRITIC_V0_10_USER_FORWARDED_HANDOFF_2026-10-22.md`。
当前：最终执行就绪 Critic 待审；`READY_FOR_CODEX=NO`。正式 main 仍是角色合同 1.7；本包任何文字不得越权启动实施。

## 一、实施后的唯一新增用户能力与本轮明确决定

新用户能力：在正常插件/Bridge 等复杂架构讨论中，用户每轮得到有具体技术身份和因果解释的当前进度与技术判断；跨 `REVISE → PROCEED → PASS` 的多轮往返不靠用户重复提醒。下一接收方而非用户负责判断上一轮用户交付是否可继续利用。

沿用**两位人工角色**，不引入外部服务或写作模型。设计阶段 `PROCEED/REVISE` 仍从 Critic 回 Planner；最终唯一执行就绪技术 `PASS` 也先回原 Planner **一次**核对读者交付。Planner 只检查获准版本、独立技术结论和说明能否忠实交到用户，并最终给短 Codex 指令；不能进行第二次专业技术批准、不能自行扩权。用户实际多一次复制粘贴仅发生在唯一最终 PASS 后。

角色合同调整由本轮独立 Critic 决定是否批准，不留给 Codex 自行决定。该变更与当前 1.7 §6.1/§6.2 的“技术 PASS 直接给 COPY TO CODEX”发生实质冲突，因此必须由最终执行就绪审查明确批准，实施才可替换旧段落。

## 二、同版用户说明的固定身份（设计阶段已关闭事项 A）

每个**重要**架构 Proposal 的稳定读者章节语义是 `## 1. 用户决策说明`，但专业领域的正文内容和篇幅并不模板化。身份由原 Proposal 文件路径、Proposal 版本和审查所绑定的准确提交共同确定。本版的当前来源就是同版 Proposal 第 1 节，批次 commit 由后续生成的最终包 HEAD 冻结；文档自身不写自己所在提交的哈希。

当本任务需要实质修订架构、关键默认行为、技术保证、权限或实施边界，Planner 写一份完整的下一 Proposal 版本，并同步更新这段说明；不只在旧计划末尾追加 finding。Plan、Goal、Kickoff 和当前审查记录均引用它，不各自复制另一份“当前架构”。仅语言微修不机械失效，但不能悄悄删重要技术选择、结果和风险。Critic 每轮从同版源核对具体变化和用户承诺，而不能因为旧说明曾被认可就跳过当前版本。

## 三、正式代码/合同的明确变更点与实施限制

只在最终审查通过后，将两份角色合同从 1.7 升至 1.8。不得新建第三人工角色、状态枚举、机器控制协议或提示词编译器。

### 3.1 Planner Role Contract

修改 `docs/workflows/PLANNER_ROLE_CONTRACT.md`：
- §2/§2.1：每次新的重要设计/恢复阶段，读取最新正式角色合同、当前任务完整版本和上轮真实审查定位；接收者不能仅靠最新聊天摘要推断原始技术证据，未变源可少读。
- §6：首轮重要 Proposal 前部必须直接写用户可用于理解和否决架构的当前说明；以实际技术名称、替代选择、代表性正常请求、重要失败路径、来源证据和适用边界组织。明确这与旧有可选“关键决定摘要”的不同：**当前最终将被交付的、与技术主体同版的真实完整章节**，而非审完技术后临场另写。
- §7：送 Critic 同时交完整技术包与**给用户看的说明原文**；审查对象不能只给摘要存在的字段。
- §10/§10.1：**接收 Critic 结果时的真实判别动作**。核对 verdict/阶段/版本/事实理由/用户说明/下一入口。技术结论完整但表达失焦，Planner 只能从 Critic 真实结论与同版已经受审 Proposal 恢复读者表述；依据不足、版本错位或安全/授权未审，停止下一步、交原 Critic 真正补审，不制造新的 PASS。已满足条件则直接继续当前任务，不为补文风无限循环。
- §11：唯一技术 PASS 的交接**第一次到 Planner**，Planner 核对批准的完整方案、Critic 原技术结论和当前读者说明；无技术语义修改后向用户交付并给出短 `COPY TO CODEX`。有实质矛盾不能发 Codex。沿用当前身份/权限/不重复索权机制，不增加新长期状态。

### 3.2 Critic Role Contract

修改 `docs/workflows/CRITIC_ROLE_CONTRACT.md`：
- §2/§4：从当前用户承诺和源码独立读技术事实，再反查 Proposal 的读者说明。重要机制可被替换却不改变正文，或核心 Hook/算法/模板、权限与运行路径被错误表述，视为实质设计/披露问题，不以语言通顺放行。
- §6：三类技术结论分别说明用户意义，`PROCEED` 仅准继续设计/准备完整执行包，`REVISE` 明确真实缺陷/保留/最小修复，唯一最终 `PASS` 说明获准机制和未证明边界。过去正式 `REVISE` 的关键问题必须在最终 PASS 说明如何关闭。
- §6.1/§6.2：唯一独立技术 `PASS` **仍与 `READY_FOR_CODEX=YES` 同时成立**，表示批准方案可交实施，但本轮机器下一接收者改为 `NEXT_HANDOFF=PLANNER`，由原 Planner做最终读者交付检查后才有 `COPY TO CODEX`。不发明新 machine status，技术 PASS 仍不代替用户授权。中间 `PROCEED/REVISE` 按现行下一 Planner 提示词要求执行。
- §6.3：最终技术 PASS 必须审用户实际将看到的同版架构说明、关键技术选择、旧问题的关闭与适用边界；独立判断不能由复制 Planner 摘要代替。PASS 最后附给 Planner 的自包含交接，而不是把审前 Kickoff 整份丢给用户。
- §9：现实失败优先查已有规则是否被真实消费；不得用同义的写作禁令替代上述接收工作。

### 3.3 为什么不改变其它产品与机制作法

现有 Project setting 已明确强制读取两份最新正式合同及自然中文要求，无需改设置。Bridge Kit 仍只处理既有授权/运行交接，不因本任务获得新权限。Clear Writing 作为可选表达辅助，不能替代独立技术判断或改变机器内容。

候选改动允许路径：
1. 上述两份 Role Contract；
2. `docs/workflows/CHATGPT_WEB_COLLABORATION_REGRESSIONS_2026-10-17.md`，如实固化真实失败与最终修复范围；
3. `results/chatgpt-web--pass-integrity/**`，只存当前任务的测试合同、原始回复、候选身份和最终验收依据；
4. 在确有必要时 `tests/test_chatgpt_web_governance_contract.py` 或同目录最小非运行时验证，用于发现关键机器身份或合同冲突；**机械检查不能替代专业中文质量**。

禁止改 `AGENTS.md`（本版不假定有缺少 locator 的证据）、根 README、其它生产源码、Project setting、Capability Gate Policy、任意 Plugin、Mica、Bridge 或 Plugin Creator。无仓库/plugin 版本发布，正式 Role Contract 版本从 1.7 → 1.8。README checked: no product-facing README update required for the planned docs-only governance scope；实施后仍须检查实际 diff 是否使这项判断改变。

## 四、原始 Critic 技术权威、Planner 最终交付及失败分流（关闭 B）

1. 独立 Critic 的每次 review 必须含当前任务、审查阶段、exact package version/ref、真实技术决定及关键依据、未证事项、最终 verdict。不能把预期 verdict、Planner 结论或测试答案塞入 Critic 的真实输入冒充独立发现。
2. Critic 可写 repo 时保存完整原始 review；当前 Web Critic 只能输出回复时，则 `COPY TO PLANNER` 必须**完整携带关键技术事实及实质 findings**。交接可较长但由用户机械复制，原 Planner 直接按收到的原文归档，不伪造 Critic 提交身份。
3. 设计阶段 `PROCEED/REVISE` 已有接收方是 Planner，不额外添加第三线程。Planner 判断原结论的内容是否完整并实际完成后续工作；只有专业判断不能支持当前结论时才请求同一 Critic 做真正补审。
4. 唯一最终 execution-ready 技术 PASS：Critic 仍负责独立审 Proposal/Plan/Goal/Kickoff、关键执行接口、权限与恢复，给 `PASS` 与 `READY_FOR_CODEX=YES`；**只交给原 Planner**，用户再复制一次。Planner 接收后：保留原 verdict 与原所有限制，检查源提交/读者说明身份是否一致；从已审正文和 Critic facts 给出自然中文架构说明，最终输出短 `COPY TO CODEX`。
5. 接收不合格分两类：仅表达失焦而技术决定/论证完整，则 Planner 原源补正文，不新增技术事实；若需要新增依据才能解释，就说明原专业审查不完整，直接退 Critic。含新重大矛盾或改变原权限，则返回 Planner–Critic 设计阶段，旧批准对新范围失效。用户不能被要求自己解释技术、编排角色或补 review 文件。
6. 技术 PASS 的真实性不由 Planner 自签。Planner 也不能把自己的恢复说明标作原 Critic 原文，不能重新输出第二个 PASS 决定，不能补造 source locator。该交付接收只保证增加独立发现不合格回复的机会，不冒充浏览器级强制发送前 Hook。

## 五、关键执行接口真实性：保留 v0.7 审查职责

只审失败会导致无法实施、无法收集必要证据、无法安全恢复或跨执行面数据无法真正消费的**关键接口**，不机械检查全部低风险 API。

**GitHub 与同版文件：** Codex 在现有已授权 AI Skills 工作区、已存在且准确的 `design/chatgpt-web--pass-integrity-v0-4` 分支工作，不要求在系统 `/tmp` 创建新正式工作树、创建另一个分支或切换用户未授权分支。启动时只读验证 repo/root/origin、branch、HEAD、dirty ownership、用户授权的执行位置是否符合当前范围；若不符合、必须新建/切换工作区或已有无关 dirty change，停止并将必要最小路径差异交原 Planner；不能自行重写拓扑或强行覆盖。普通 commit/同名非强制 push 及经冻结验收后的 main 合入，只在用户发送最终合法授权的短 Kickoff 后按当前 AGENTS 实际规则运行。准确提交在**执行完真实 commit 后**填入候选证据，禁止自引用哈希。

**真实 Web 验证：** 没有已验证工具能自动在原生 ChatGPT Web 创建 fresh conversation、在指定线程加载未正式部署的 1.8 合同并切换独立角色。因此必须由用户完成必要的新会话/复制 UI 操作；Codex/Planner事先准备完整任务及定位提示词，用户不查源码/选内部 Reviewer/拼要求。该 UI 动作不授权付费或真实产品变更。

**审查文本归档：** 有 repo 写权限的原 Planner 使用当前 GitHub 接口保存实际收到的全文；没有则同任务 Codex 负责任务范围内存入 `results/`。用户只把完整回复机械转交，不能被要求建立审查文件或补来源引用。无真实全文不可称已验收整篇回复。

**维护看板：** task tracking Issue/Project 按维护看板管理。Issue 可由合法工具创建/同步，但 GitHub Project mutation 若在当前环境不可用，输出准确 pending Project update 给下一个有合法入口的维护线程，不要求用户拖动看板。Project metadata 不能冒充候选能力验收。

## 六、真实回归与最终评估合同：保留 A/B/C，闭合 C

以下是当前唯一治理任务的**有界验证家族**，不是给所有插件新增通用 Gate 数量；详细输入、判定、候选污染/预算与停止语义见同版 `results/chatgpt-web--pass-integrity/VALIDATION_CONTRACT_V0_11_2026-10-22.md`。

A. 已知错误执行前批准（历史 Clear Writing package）：新 Critic 必须独立发现真实恢复归档/物化、fresh Web actor 和低层 task prompt 缩窄中央审查的缺口；正确保持 `REVISE`，不冒用旧 PASS。此项测真实接口与技术判断。
B. Phase C 非终态真实停顿：Planner 必须说清实际状态、安全停止、谁修哪个问题及唯一下一入口，不能只说“需要某环境”。此项测实用交接。
C. 历史真实复杂执行前方案：新 Critic 独立审完整方案而非沿用历史结论；只有证据确实支持才能 `PASS`。若真有 blocker，就 `REVISE`，不得替换题目或以另一批证据拼成正例。若真实 PASS，继续实际测试 Critic→Planner 的最终读者交付接收；如不能得到合法正例，当前治理候选不宣称此项通过，按同任务的正规审查路线处理样本/审查问题，不由 Codex自选赢家。
D. 真正多轮机制变化：复用只读的真实 Slurm 历史设计差异，至少一次由 Critic `REVISE`、Planner 实质修订技术及 Proposal 用户说明、Critic 再次核对。**第二轮起生成者只得到角色、普通任务和准确来源定位，不再附要出现的 Hook/Wrapper 等评分答案**。这是已见历史材料的跨轮开发回归，不冒称 fresh。
E. 候选整篇质量与默认生效：审查当前任务中被用户部分认可的示例只能作开发参考，不作完美范文；真正自然中文质量需要独立阅读完整回复与当轮技术源。角色合同正式合入 main 后，下一项真实、新发生、预先在运行前冻结的插件或复杂架构任务，再不补“请说人话”提示，观察是否自然读取合同、持续维护当前说明、每轮用户解释和最终接收方检查。新任务出现以前只称待验证，不伪造未来任务。

开发期可以重复已见材料定位原因；最终批次冻结候选、输入/来源、评审口径、次数后不得改题挑赢家。生成者不能读目标评价答案和旧错误回复后再声称“未经提示自动发现”。规范中明确保留一般复杂架构原理，不给生成模型固定段落模板。机械八类合同回放仅证明字段/版本/阶段迁移，不替代以上独立定性评价。

**用户成本预算**：普通设计阶段不增 UI 转发；正式技术 PASS 后永久增加一次机械转发给 Planner。候选实测使用已有 A/B/C 与一段只读多轮 D，不增加付费 API 或 Plugin Creator mutation。每项需要 fresh Web 时最多一次正常启动和必要的原两角色转发；具体用户操作由验证前准备的任务级 prompt 给出，不能让用户自己选择测试题、合并审查输出或手写评判。无偿但有 UI 成本，应记录真实轮次数及发现的修复价值，不能以“零费用”掩盖多次人工疲劳。

## 七、实施阶段、候选身份、独立安全门与合入

**实现前：** 当前 v0.11 仍为待审包；最终独立 Critic 只有确认全部关键设计、实际接收、负例/正控、权限/恢复合同闭合，才可给唯一 `PASS + READY_FOR_CODEX=YES`。此时 Critic 按现行已生效 1.7 规则把短实施入口给用户；本次 PASS 是**授权实现未来 1.8 行为**，不是已经采用新 1.8 的最终交付语义。不要在尚未实施 1.8 时把拟议“PASS先回 Planner”强加给这次首次实施批准；这区分部署机制与产品将来行为。

**实现阶段：** 用户将获准短 Kickoff 发给 Codex，Codex 在已确认的既有设计分支修改 allowlist 内源文件；先运行轻量本地验证，必要时完成已冻结 deterministic regressions。无高风险授权不用真实调度器、Plugin Creator 或付费系统。

**候选冻结：** 在角色文本、回归合同和测试输入稳定后由 Codex commit，另在后继 evidence/manifest 记录 `GOVERNANCE_CANDIDATE_COMMIT` 与两份角色文件 blob、受影响的测试合同身份。文档不要求包含自己提交号。候选定义内容发生变更，旧候选相关评估须明确失效；仅后续证据追加不修改评估对象。

**实现后安全门：** 原独立 Critic 读取真实 source diff、完整角色合同、候选/测试输入身份、低成本回归、真实网页验证准备材料，以及当前剩余预算、用户操作与恢复路线。只允许 `PROCEED_TO_FINAL_EVALUATION / REVISE`，不制造第二次执行就绪 PASS。后者若只是普通技术实现缺陷而不改变冻结语义，由同一 Codex 任务修复后再检查。

**真实 Web 评估：** 达到安全门通过后，执行事先冻结的真实 A/B/C 与多轮 D，并在独立审查中阅读每条完整用户回复。任何重大失败要区分模型真实质量、输入被答案污染、工具/网页无法访问及协议错误；故障不得靠延长提示词或换题反复追 PASS。找到了需要改变冻结架构的真实失败，返回 Planner/Critic，不暗改规范。

**main 集成：** 只有必要已冻结验证达到真实条件，独立评审确认候选可以接受，且用户此前发送的 bounded Kickoff 涵盖普通集成/非强制推送时，才按 AI Skills `AGENTS.md §8.5` 进行合法的当前 main fetch、竞争修改/dirty 前检、普通非强制合入/推送和远端回读。若出现实际冲突、竞争性角色合同修改、权限越界或源候选漂移，STOP 返回任务 owner。仅远端 main 的角色文本确认为 1.8 且与受审候选同一内容，才可称正式源已升级；不涉及仓库发行版或插件发布。

**main 后用户正常入口：** 对已预先按第六节 E 规则选定的首个**新发生**真实复杂设计任务，在其第一次模型输入之前冻结任务身份和任务要求，然后让用户只按正常请求进入项目。没有这项未来真实任务之前，治理只能称“角色文本已升级、已见回归已通过”，**不得称长期无需提醒已在新任务验证**。此项不因等待自然任务就无限轮询或启动新自动化。

## 八、权限与安全停止

允许的待批准范围：上述有限治理文件、测试/结果目录、已存在授权分支上的普通 Git commit/push、必要用户主动触发且只读的真实 Web 验收，以及经过全部验收与合规预检之后的普通主分支集成。最终执行授权必须由用户实际发送批准入口表达，本 Critic 的文字不是授权。

禁止：修改 Project setting、`PLUGIN_CAPABILITY_GATE_POLICY.md`、Clear Writing/Slurm/Mica/Bridge/Plugin Creator 或其它产品；新后台运行、数据库、状态机、第三人工角色、付费模型、私人账号配置、真实作业取消/提交、正式插件发布、强推/历史改写、偷偷改变会话模型或审查样本。相关越界/角色合同冲突须停止并回 Planner/Critic。

停止并保持完整证据，如果最终技术 PASS 下一 Planner 接收链仍没有有效入口、真实 Web 未能获得实际审查全文、候选身份/审查对象不同、存在高影响边界未经授权、关键测试发现用户说明仍隐藏技术、或主分支冲突。未改变批准语义的普通脚本/文字实现问题由原 Codex 任务修复。用户已决定的普通配置不重新索取授权。
